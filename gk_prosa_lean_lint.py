#!/usr/bin/env python3
"""
GK PROSA × LEAN LINT — piloto de leitura adversarial automatizada
(modelo: red team do pequalnp.com "lê cada afirmação da prosa contra o artefato formal").

Alvos do piloto (26/11/2026): `krajicek_ddp/RELATORIO_CONSOLIDADO.md` §9.1 (ponte L2→L3)
e o dossiê `krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md` (DD_Res ∈ P) contra
`lean4/Gothic_Generators/DDP.lean`, `krajicek_ddp/C_disjuncao_viavel.md` e
`krajicek_ddp/experimentos_disjuncao.py`.

Regras:
  P1 SORRY-REF    citações `DDP.lean:<n>` nos docs ≡ linha real (declaração com sorry
                  = warning do Lean 628:8/690:8, ou token `sorry` 630/692)
  P2 SORRY-COUNT  nº de tokens `sorry` reais em DDP.lean == 2 (docs dizem "2 sorry");
                  explica delta com `sorry_in_sources` do JSON (4 = 2 comentários)
  P3 QUOTE-CHECK  tokens pivô do enunciado-fonte presentes na prosa do dossiê
                  (fonte tem e prosa não = "PROSA DIZ MENOS"; fonte não tem = fonte mudou)
  P3b QUOTE-DIFF (r3) diff normalizado completo: os 3 blocos de citação de A.1 devem ser
                  IDÊNTICOS aos blocos-fonte de C_disjuncao_viavel.md §2.2–§2.3
  P3c F1-FRAGMENT (r4) o fragmento verbatim da linha §B-F1 ("But by (7) i_o is also
                  already in M*") aparece nas 3 transcrições do repo (F/G/A — fonte primária
                  arXiv HTML v5 conferida em 26/11/2026: o artigo escreve i_o, letra o)
  P9 XREF-9.2    (r4) as cross-references do §9.2 apontam para o que existe: §6.4/§7-item-6/
                  README-item-5/INDICE-DD7 com o condicional τ_N; terminologia "peer review"
                  em REL/README/INDICE
  P10 ARXIV-PRIME (r5) fonte primária salva em fontes/arxiv_2506.20221v4/v5.html: lacuna
                  "But by (7) … already in M*" presente NAS DUAS versões; v4 = Theorem 4,
                  v5 = Theorem 3 (renumeração); Problem 2.1 em ambas
  P4 EXP-REPRO    claim "3000/3000" ⇒ script do experimento existe (--replay: executa e
                  confere 3000/3000 + as 5 taxas de falha + médias)
  P5 BRIDGE-GUARD docs canônicos com `NP≠coNP`/`P≠NP` exigem marcador condicional
  P6 L2L3-GUARD   docs com `L2→L3` exigem marcador de ponte ABERTA
  P7 FRONT-MANIFEST (r2) frentes G–N: cada linha da tabela §B da AUDITORIA exige
                 marcadores LIDOS no artefato da frente (manifesto FRONT_MANIFEST)
  P8 ROUND-COUNT (r2) contagens de rodadas do §D.2 (N2=5, C2=5, Q2=3, N1=2)
                 batem com os cabeçalhos dos *_referee.md

Escopo e limites (honestidade): P5/P6 são heurísticos (marcador numérico, não leitura
semântica); logs `*_referee.md` e `A_teoremas_exatos.md` (transcrição verbatim do artigo)
recebem WARN, não FAIL. P3 usa 8 tokens pivô, não diff completo.

Uso: python gk_prosa_lean_lint.py [--replay]
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FAILS: list[str] = []

CANONICAL = [
    "README.md", "INDICE.md", "CONTRIBUICOES_DO_PROJETO.md",
    "PLANO_PESQUISA_E_DESENVOLVIMENTO.md", "ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md",
    "krajicek_ddp/RELATORIO_CONSOLIDADO.md", "krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md",
    "krajicek_ddp/CONTEXTO_COMUM.md",
]
SCAN_DIRS = ["", "krajicek_ddp", "ferramentas", "papers"]
SCAN_EXCLUDE_SUBSTR = ("pequalnp/", "support/", "fontes/")


def fail(rule: str, msg: str) -> None:
    FAILS.append(f"[{rule}] {msg}")


def md_files() -> list[Path]:
    out = []
    for d in SCAN_DIRS:
        base = ROOT / d if d else ROOT
        for p in sorted(base.glob("*.md")):
            rel = str(p.relative_to(ROOT)).replace("\\", "/")
            if any(rel.startswith(x) for x in SCAN_EXCLUDE_SUBSTR):
                continue
            out.append(p)
    return out


def norm(s: str) -> str:
    """Normaliza markdown para comparação: sem `*`, sem backticks, sem prefixo
    de blockquote `>` (senão frases que cruzam linhas de citação nunca casam),
    ∗ (asterisk operator) ≡ *, espaço único."""
    s = s.replace("`", "").replace("*", "").replace(">", "").replace("∗", "*")
    return re.sub(r"\s+", " ", s)


# ---------------------------------------------------------------- P1 / P2
def sorry_decl_lines(ddp: Path) -> tuple[list[int], list[int], list[int]]:
    """Retorna (decl lines, sorry token lines, todas as linhas com 'sorry')."""
    lines = ddp.read_text(encoding="utf-8").splitlines()
    token_lines, all_lines = [], []
    decl_lines: list[int] = []
    last_theorem: int | None = None
    for i, ln in enumerate(lines, start=1):
        if "sorry" in ln:
            all_lines.append(i)
        if re.match(r"\s*sorry\s*$", ln):
            token_lines.append(i)
        m = re.match(r"\s*(theorem|lemma)\s+", ln)
        if m:
            last_theorem = i
        if re.match(r"\s*sorry\s*$", ln) and last_theorem:
            decl_lines.append(last_theorem)
    return decl_lines, token_lines, all_lines


def rule_p1_p2() -> None:
    ddp = ROOT / "lean4" / "Gothic_Generators" / "DDP.lean"
    decls, tokens, all_lines = sorry_decl_lines(ddp)
    valid = set(decls) | set(tokens)

    bad = []
    cites = []
    for p in md_files():
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"DDP\.lean:(\d+)", text):
            n = int(m.group(1))
            cites.append((str(p.relative_to(ROOT)).replace("\\", "/"), n))
            if n not in valid:
                bad.append(f"{p.relative_to(ROOT)} cita DDP.lean:{n} "
                           f"(não é declaração com sorry {sorted(decls)} "
                           f"nem token sorry {sorted(tokens)})")
    for b in bad:
        fail("P1", b)

    # P2: contagem
    try:
        j = json.loads((ROOT / "gk_lean_verification.json").read_text(encoding="utf-8"))
        jcount = j.get("sorry_in_sources", {}).get("DDP.lean")
    except Exception as e:  # noqa: BLE001
        jcount = None
        fail("P2", f"gk_lean_verification.json ilegível: {e}")
    if len(tokens) != 2:
        fail("P2", f"esperado 2 tokens `sorry` em DDP.lean, achado {len(tokens)}: {tokens}")
    # docs canônicos que afirmam "2 sorry"
    for rel in CANONICAL:
        p = ROOT / rel
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        if re.search(r"\b2\s+`?sorry`s?", t) and len(tokens) != 2:
            fail("P2", f"{rel} afirma '2 sorry' mas tokens reais = {len(tokens)}")
    print(f"    decl(s) com sorry: {decls} · token sorry: {tokens} · "
          f"'sorry' em qualquer linha: {all_lines} · JSON sorry_in_sources={jcount}")


# ---------------------------------------------------------------- P3
PIVOT_TOKENS = [
    "E_i ⊆ D_i",                      # Lema 4.1(a)
    "E_s = ∅",                        # Lema 4.1(b)
    "O(|Π|²)",                        # Lema 4.1(c)
    "O(Σ_i |D_i|·|D_{pares}|)",       # Lema 4.1(c) — cota prática (viração de auditoria)
    "se E_t é resolvente",            # Lema 4.2(2) hipótese (viração de auditoria)
    "resolução pura",
    "no máximo |Π| linhas",          # Teorema 4.3
    "α_{i*} ∈ TAUT",                 # Teorema 4.3 (convenção Seção 2.1)
]


def rule_p3() -> None:
    dossier = ROOT / "krajicek_ddp" / "AUDITORIA_EXTERNA_DDRES_G-N.md"
    source = ROOT / "krajicek_ddp" / "C_disjuncao_viavel.md"
    dt = norm(dossier.read_text(encoding="utf-8", errors="replace"))
    st = norm(source.read_text(encoding="utf-8", errors="replace"))
    menos, naofont = [], []
    for tok in PIVOT_TOKENS:
        n = norm(tok)
        in_src, in_doc = n in st, n in dt
        if in_src and not in_doc:
            menos.append(tok)
        elif not in_src and in_doc:
            naofont.append(tok)
        elif not in_src and not in_doc:
            naofont.append(tok + " (ausente em AMBOS)")
    for t in menos:
        fail("P3", f"PROSA DIZ MENOS: token pivô na fonte ausente do dossiê → {t!r}")
    for t in naofont:
        fail("P3", f"FONTE DRIFT: token ausente em C_disjuncao_viavel.md → {t!r}")
    rule_p3b(dossier, source)


# âncoras dos 3 enunciados citados em A.1 (mesmas strings nos dois arquivos)
QUOTE_ANCHORS = ["Lema 4.1 (B)", "Lema 4.2 (B)", "Teorema 4.3 (B)"]


def _quote_blocks(path: Path, anchors: list[str]) -> dict[str, str]:
    """Extrai, para cada âncora, o bloco de blockquote que a segue (linhas '>'),
    parando na próxima âncora ou na primeira linha que não é citação."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    starts = [(i, a) for i, ln in enumerate(lines)
              for a in anchors if a in ln]
    blocks: dict[str, str] = {}
    for idx, (i, a) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        buf: list[str] = []
        for j in range(i, end):
            if j > i and not lines[j].lstrip().startswith(">"):
                break
            buf.append(lines[j])
        blocks[a] = norm(" ".join(buf)).strip()
    return blocks


def rule_p3b(dossier: Path, source: Path) -> None:
    db = _quote_blocks(dossier, QUOTE_ANCHORS)
    sb = _quote_blocks(source, QUOTE_ANCHORS)
    for a in QUOTE_ANCHORS:
        if a not in db:
            fail("P3b", f"dossiê não contém bloco de citação {a!r}")
            continue
        if a not in sb:
            fail("P3b", f"fonte não contém bloco {a!r} (renomeado? atualizar âncoras)")
            continue
        if db[a] != sb[a]:
            # primeiro ponto de divergência, com contexto curto
            k = min(len(db[a]), len(sb[a]))
            p = next((x for x in range(k) if db[a][x] != sb[a][x]), k)
            ctx = (f"...{db[a][max(0, p-30):p+30]}... vs "
                   f"...{sb[a][max(0, p-30):p+30]}...")
            fail("P3b", f"quote {a!r} difere da fonte na posição {p}: {ctx}")


# ---------------------------------------------------------------- P4
CLAIM_DOCS = [
    "INDICE.md", "CONTRIBUICOES_DO_PROJETO.md", "PLANO_PESQUISA_E_DESENVOLVIMENTO.md",
    "EVOLUCAO_PROJETO.md", "krajicek_ddp/RELATORIO_CONSOLIDADO.md",
    "krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md", "krajicek_ddp/C_disjuncao_viavel.md",
]


def rule_p4(replay: bool) -> None:
    claimers = []
    for rel in CLAIM_DOCS:
        p = ROOT / rel
        if p.exists() and "3000/3000" in p.read_text(encoding="utf-8", errors="replace"):
            claimers.append(rel)
    script = ROOT / "krajicek_ddp" / "experimentos_disjuncao.py"
    if claimers and not script.exists():
        fail("P4", f"'3000/3000' afirmado em {claimers} mas {script} NÃO existe")
    elif claimers:
        print(f"    claim '3000/3000' em {len(claimers)} docs; script existe")
        if replay:
            r = subprocess.run([sys.executable, str(script)], capture_output=True,
                               text=True, encoding="utf-8", errors="replace", timeout=600)
            out = r.stdout or ""
            # confronto r3: resultado + as 5 taxas + as médias do bloco §7 da fonte
            expected = [
                "3000/3000 corretos (100.0%)",
                "847/3000 =  28.2%", "436/3000 =  14.5%", "289/3000 =   9.6%",
                "1566/3000 =  52.2%", "1485/3000 =  49.5%",
                "media |pi| = 7.0, max = 20",
            ]
            missing = [e for e in expected if e not in out]
            if r.returncode != 0:
                fail("P4", f"--replay: rc={r.returncode}")
            for e in missing:
                fail("P4", f"--replay: saída não contém {e!r} (claim da fonte §7)")
            if not missing:
                print("    --replay: resultado + 5 taxas + médias IDÊNTICOS à fonte §7")


# ---------------------------------------------------------------- P7 / P8
# Manifesto das frentes (r2): frente -> [(arquivo, marcadores)].
# Marcadores calibrados por sonda em 26/11/2026 — todo marcador foi LIDO no
# artefato antes de entrar aqui (não inventado a partir do §B).
FRONT_MANIFEST = {
    "F1": [("krajicek_ddp/F1_verificacao_passo7.md", ["But by (7)"]),
           ("krajicek_ddp/CONTEXTO_COMUM.md", ["em **ambas** as versões"])],
    "G1": [("krajicek_ddp/G1_log_forcing.md", ["Log(M[G]) = Log(M)", "refutado"])],
    "G2": [("krajicek_ddp/G2_semente_Fsent.md", ["Teorema 2.1", "ZFC", "R3 ≡ BB"])],
    "H1": [("krajicek_ddp/H1_colecao_refutacao.md", ["Q-compactness", "retra"])],
    "I1": [("krajicek_ddp/I1_Qcompactness_ultrapoderes.md", ["A.7", "ultrapoder"])],
    "J1": [("krajicek_ddp/J1_Qcompactness_M0.md", ["Teorema K", "K.2", "inconsist"])],
    "J2": [("krajicek_ddp/J2_ponto_fixo.md", ["K-FP"])],
    "L1": [("krajicek_ddp/L1_phi_insatisfativel.md", ["L.1", "L.3", "L.4"])],
    "M": [("krajicek_ddp/M_canto_adversarial.md", ["M.2", "Ressalva", "parcial"])],
    "N1": [("krajicek_ddp/N1_refutacao_interna_CN_s.md", ["N.1", "N.2", "fechada", "§0.3"])],
    "N2": [("krajicek_ddp/N2_residuals_RA_RB.md", ["(C)", "omitente", "G_eff", "global"])],
    "C2": [("krajicek_ddp/C2_ddres_k.md", ["(O1)", "(O5)", "alternante", "C2.3"])],
    "Q2": [("krajicek_ddp/Q2_instancias_tau_n_q.md", ["Q2.1", "Q2.2", "Gödel II"]),
           ("27_TEOREMA_Q_GODEL2_BRIDGE_MO.md", None)],  # None = só existência
    # frentes fora da tabela §B (r3): E (INDICE linha VERIFICADO) e Q2.4 (status (C))
    "E": [("krajicek_ddp/E_ataque_problema21.md", ["E1–E5", "passo (5)", "frágil"])],
    "Q2.4": [("krajicek_ddp/Q2.4_fonte_SIGMA1_K19_KP90.md",
              ["Pudlák", "i-RFN", "K19", "(C)"]),
             ("krajicek_ddp/Q2.4_fonte_SIGMA1_referee.md", None)],  # referee exige existência
}
# Rodadas declaradas em AUDITORIA §D.2 -> (arquivo, expressão esperada)
ROUND_COUNT = {
    "N2": ("krajicek_ddp/N2_residuals_referee.md", "rodada 5"),
    "C2": ("krajicek_ddp/C2_ddres_k_referee.md", "rodada 5"),
    "Q2": ("krajicek_ddp/Q2_instancias_referee.md", "rodada 3"),
    "N1": ("krajicek_ddp/N1_referee.md", "rodada 2"),
}


def rule_p7() -> None:
    for front, entries in FRONT_MANIFEST.items():
        for rel, toks in entries:
            p = ROOT / rel
            if not p.exists():
                fail("P7", f"frente {front}: artefato ausente {rel}")
                continue
            if toks is None:
                continue  # checagem de existência apenas
            t = p.read_text(encoding="utf-8", errors="replace")
            miss = [x for x in toks if x not in t]
            for m in miss:
                fail("P7", f"frente {front}: {rel} sem marcador {m!r} "
                           f"(linha §B exige este conteúdo no artefato)")


def rule_p8() -> None:
    for front, (rel, expr) in ROUND_COUNT.items():
        p = ROOT / rel
        if not p.exists():
            fail("P8", f"§D.2: referee ausente para {front} ({rel})")
            continue
        if expr not in p.read_text(encoding="utf-8", errors="replace"):
            fail("P8", f"§D.2 afirma rodadas para {front}, mas {rel} "
                       f"não contém {expr!r}")


# ---------------------------------------------------------------- P5 / P6
COND_MARK = re.compile(
    r"\(ST\)|condicion|⟹|rodapé 2|retra[ií]|DESCART|abert[ao]|só condicion|"
    r"não[^.]{0,60}formaliz|não[^.]{0,40}afirmad|não[^.]{0,40}reivindic", re.I)
L2L3_MARK = re.compile(
    r"abert|não[^.]{0,60}(foi )?demonstrad|permanec|precisa ser demonstrada|"
    r"bridge aberto|não fechad", re.I)
P5_TARGET = re.compile(r"(NP ?≠ ?coNP|`P ?≠ ?NP`|P ?≠ ?NP)")


def rule_p5_p6() -> None:
    files = md_files()
    for p in files:
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        t = p.read_text(encoding="utf-8", errors="replace")
        reflexive = ("_referee.md" in rel) or rel.endswith("A_teoremas_exatos.md")
        if P5_TARGET.search(t) and not COND_MARK.search(t):
            if rel in CANONICAL:
                fail("P5", f"{rel} fala de NP≠coNP/P≠NP sem marcador condicional")
            else:
                print(f"    [P5 WARN] {rel}: sem marcador condicional (não canônico)")
        if re.search(r"L2→L3|L2↔L3|bridge L2", t) and not L2L3_MARK.search(t):
            if rel in CANONICAL:
                fail("P6", f"{rel} cita a ponte L2→L3 sem marcador de abertura")
            else:
                print(f"    [P6 WARN] {rel}: ponte sem marcador (não canônico)")
        _ = reflexive


F1_FRAGMENT = "But by (7) i_o is also already in M*"
F1_SOURCES = [
    "krajicek_ddp/F_CONTEXTO_ATAQUE.md",
    "krajicek_ddp/G_CONTEXTO_FORCING.md",
    "krajicek_ddp/A_teoremas_exatos.md",
]


def rule_p3c() -> None:
    """O fragmento verbatim da linha §B-F1 deve aparecer em TODAS as transcrições
    do repo (i_o = letra o, como no artigo; fonte primária: arXiv HTML v5 §3)."""
    for rel in F1_SOURCES:
        p = ROOT / rel
        if not p.exists():
            fail("P3c", f"fonte do fragmento F1 ausente: {rel}")
            continue
        if norm(F1_FRAGMENT) not in norm(p.read_text(encoding="utf-8", errors="replace")):
            fail("P3c", f"{rel} não contém o fragmento verbatim {F1_FRAGMENT!r} "
                        f"(linha §B-F1; artigo = i_o, letra o)")


def _block(path: Path, start_re: str, end_re: str) -> str:
    """Linhas de `start_re` até (exclusivo) a próxima linha que casa `end_re`."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    out, on = [], False
    for ln in lines:
        if not on:
            if re.search(start_re, ln):
                on = True
                out.append(ln)
            continue
        if re.search(end_re, ln):
            break
        out.append(ln)
    return " ".join(out)


def rule_p9() -> None:
    rel = ROOT / "krajicek_ddp" / "RELATORIO_CONSOLIDADO.md"
    read = ROOT / "README.md"
    ind = ROOT / "INDICE.md"
    cond = [
        ("§9.2(2)-§6.4", rel, r"^### 6\.4", r"^#{2,3} ", "CONDICIONAL à semântica de"),
        ("§9.2(2)-§7-item6", rel, r"^## 7\.", r"^## ", "parcial com merge pode falhar"),
        ("§9.2(2)-README-item5", read, r"^5\. \*\*Canto adversarial", r"^6\. \*\*",
         "pode falhar"),
        ("§9.2(2)-INDICE-DD7", ind, r"\*\*DD7\*\*", r"\*\*DD8\*\*", "pode falhar"),
    ]
    for cid, p, sr, er, marker in cond:
        if not p.exists():
            fail("P9", f"{cid}: arquivo ausente {p.name}")
            continue
        blk = _block(p, sr, er)
        if not blk:
            fail("P9", f"{cid}: seção/lista não encontrada (cross-ref do §9.2 quebrada)")
        elif marker not in blk:
            fail("P9", f"{cid}: marcador {marker!r} ausente na seção apontada")
    # §9.2(1): fórmula de terminologia nos 3 documentos nomeados
    for cid, p in [("§9.2(1)-REL", rel), ("§9.2(1)-README", read), ("§9.2(1)-INDICE", ind)]:
        if not p.exists() or "peer review" not in p.read_text(encoding="utf-8", errors="replace"):
            fail("P9", f"{cid}: marcador 'peer review' ausente "
                       f"(§9.2(1) diz fórmula padronizada neste documento)")


# ---------------------------------------------------------------- P10
def _visible_arxiv(path: Path) -> str:
    """Texto visível do HTML do arXiv (tags removidas, entidades decodificadas)."""
    s = path.read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s)


def rule_p10() -> None:
    """Fonte primária: a lacuna do passo (5) existe nas DUAS versões do artigo,
    com a renumeração Teorema 4 (v4) → Teorema 3 (v5) confirmada."""
    base = ROOT / "krajicek_ddp" / "fontes"
    texts: dict[str, str] = {}
    for v in ("v4", "v5"):
        p = base / f"arxiv_2506.20221{v}.html"
        if not p.exists():
            fail("P10", f"fonte primária ausente: {p.name} (baixar de arxiv.org/html/2506.20221{v})")
            continue
        sl = re.sub(r"\s+", "", _visible_arxiv(p))
        texts[v] = sl
        if "Butby(7)" not in sl or "isalsoalreadyin" not in sl:
            fail("P10", f"{v}: lacuna do passo (5) AUSENTE no HTML — claim de F1 quebrada")
        if "Problem2.1" not in sl:
            fail("P10", f"{v}: 'Problem 2.1' ausente (referência do dossiê §B-F1/G2)")
    if "v4" in texts:
        if "Theorem4" not in texts["v4"]:
            fail("P10", "v4 sem 'Theorem 4' (renumeração 4→3 não confirmada na v4)")
    if "v5" in texts:
        if "Theorem4" in texts["v5"]:
            fail("P10", "v5 contém 'Theorem 4' — renumeração 4→3 desconfirmada")
        if "Theorem3" not in texts["v5"]:
            fail("P10", "v5 sem 'Theorem 3' (renumeração não confirmada na v5)")


# ---------------------------------------------------------------- main
def main() -> int:
    replay = "--replay" in sys.argv
    print("=" * 70)
    print("GK PROSA × LEAN LINT — leitura adversarial automatizada (piloto)")
    print("=" * 70)
    rule_p1_p2();   print(f"  P1 sorry-ref / P2 count ..... "
                          f"{'OK' if not any(f.startswith('[P1]') or f.startswith('[P2]') for f in FAILS) else 'FALHA'}")
    rule_p3();      print(f"  P3/P3b quote pivô+diff ...... "
                          f"{'OK' if not any(f.startswith('[P3') for f in FAILS) else 'FALHA'}")
    rule_p4(replay);print(f"  P4 exp-repro (3000/3000) .... "
                          f"{'OK' if not any(f.startswith('[P4]') for f in FAILS) else 'FALHA'}")
    rule_p5_p6();   print(f"  P5 bridge-guards / P6 L2→L3 . "
                          f"{'OK' if not any(f.startswith('[P5]') or f.startswith('[P6]') for f in FAILS) else 'FALHA'}")
    rule_p7();      print(f"  P7 frentes §B+E+Q2.4 (15) ... "
                          f"{'OK' if not any(f.startswith('[P7]') for f in FAILS) else 'FALHA'}")
    rule_p8();      print(f"  P8 rodadas §D.2 (5/5/3/2) ... "
                          f"{'OK' if not any(f.startswith('[P8]') for f in FAILS) else 'FALHA'}")
    rule_p3c();     print(f"  P3c fragmento F1 × 3 fontes .. "
                          f"{'OK' if not any(f.startswith('[P3c]') for f in FAILS) else 'FALHA'}")
    rule_p9();      print(f"  P9 cross-refs do §9.2 ........ "
                          f"{'OK' if not any(f.startswith('[P9]') for f in FAILS) else 'FALHA'}")
    rule_p10();     print(f"  P10 fonte primária v4+v5 ..... "
                          f"{'OK' if not any(f.startswith('[P10]') for f in FAILS) else 'FALHA'}")
    print("-" * 70)
    if FAILS:
        for f in FAILS:
            print(f"  FALHA {f}")
        print(f"*** PROSA×LEAN LINT: {len(FAILS)} falha(s) ***")
        return 1
    print("*** PROSA×LEAN LINT OK: prosa consistente com artefatos ***")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

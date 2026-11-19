#!/usr/bin/env python3
"""
gk_claims_lint.py — Sistema imunologico do projeto: verificacao automatica
de consistencia de claims, reprodutibilidade e marcadores de honestidade.

Origem: sugestao da auditoria externa (2026-10-11, sec.4.5: "testes
automaticos que falhem se README/INDICE disser 'provado' para itens marcados
'rejeitado'") + incidentes reais (status "aguardando resposta" obsoleto apos
a resposta de Krajicek de 12/10/2026).

Regras:
  R1  guarda de retraidos: D1-D6/itens retraidos so com marcador na linha
  R2  "aguardando resposta" so em contexto historico (cronologia 11/10)
  R3  disclaimer de revisao interna presente (README, INDICE, CONTRIBUICOES)
  R4  "DD_Res ∈ P" sempre acompanhado de auditoria externa pendente (README, INDICE)
  R5  links markdown locais apontam para arquivos existentes
  R6  sha256 dos CSVs bate com o registrado nos JSONs (quando presente)
  R7  gk_lean_verification.json: build verde e 0 NOT_FOUND
  R8  INDICE contem a tabela DESCARTADOS com D1..D6
  R9  documentos canonicos indexados no INDICE
  R10 aviso de escopo do Lean presente no README (nao formaliza p-time/NP!=coNP)

Uso: python gk_claims_lint.py [--root DIR]
Exit: 0 = tudo OK; 1 = falhas; 2 = erro de execucao
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# linhas historicas permitidas para R2 (cronologia / citacoes do passado)
R2_ALLOW = ["| **11/10/2026**", "histór", "históric"]

# R1: padroes que NUNCA podem aparecer sem marcador de retracao na mesma linha
R1_PATTERNS = [
    r"s_P\s*[≥>=]\s*2\^\{?c",          # escala exponencial retraida (D4)
    r"barreira de interpretabilidade",   # D1 (como resultado estabelecido)
    r"gerador universal\s+T_\*",        # D6/T6
]

# R1: marcadores aceitos na mesma linha
R1_MARKERS = ["retra", "rejeit", "descart", "não usar", "nao usar",
              "não provado", "nao provado", "inválido", "invalido", "D1", "D2",
              "D3", "D4", "D5", "D6", "~~"]

DOCS_LINKED_FROM = [  # R5: arquivos cujos links locais devem resolver
    "CONTRIBUICOES_DO_PROJETO.md",
    "PLANO_PESQUISA_E_DESENVOLVIMENTO.md",
    "README.md",
    "AMBIENTE_E_FERRAMENTAS.md",
    "INDICE.md",
]

R3_FILES = ["README.md", "INDICE.md", "CONTRIBUICOES_DO_PROJETO.md"]
R4_FILES = ["README.md", "INDICE.md"]
R9_CANONICAL = [
    "CONTRIBUICOES_DO_PROJETO.md",
    "PLANO_PESQUISA_E_DESENVOLVIMENTO.md",
    "AMBIENTE_E_FERRAMENTAS.md",
    "EVOLUCAO_PROJETO.md",
    "CONTINUIDADE_PESQUISA.md",
    "ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md",
]


def fail(fails, rule, msg):
    fails.append(f"[{rule}] {msg}")


def check_r1_retracted(root, fails):
    """Padroes retraidos exigem marcador na mesma linha OU na anterior
    (janela de 2 — a prosa de retracao frequentemente quebra linha)."""
    targets = ["README.md", "INDICE.md", "CONTRIBUICOES_DO_PROJETO.md",
               "PLANO_PESQUISA_E_DESENVOLVIMENTO.md"]
    for name in targets:
        p = root / name
        if not p.exists():
            fail(fails, "R1", f"{name} nao encontrado")
            continue
        lines = p.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            low = line.lower()
            prev = lines[i - 1].lower() if i > 0 else ""
            for pat in R1_PATTERNS:
                if re.search(pat, line, re.IGNORECASE):
                    if not (any(m.lower() in low for m in R1_MARKERS) or
                            any(m.lower() in prev for m in R1_MARKERS)):
                        fail(fails, "R1",
                             f"{name}:{i+1} padrao retraido sem marcador: "
                             f"{line.strip()[:90]}")


def check_r2_stale_status(root, fails):
    """'aguardando resposta' so em contexto historico (apos resposta 12/10).
    Texto tachado (~~...~~) e historico por definicao -> permitido."""
    for base in [root, root / "krajicek_ddp"]:
        for p in base.glob("*.md"):
            for i, line in enumerate(
                    p.read_text(encoding="utf-8").splitlines(), 1):
                if "aguardando resposta" not in line.lower():
                    continue
                if "~~" in line:          # tachado = retratado/historico
                    continue
                if any(a.lower() in line.lower() for a in R2_ALLOW):
                    continue
                rel = p.name if base == root else f"krajicek_ddp/{p.name}"
                fail(fails, "R2",
                     f"{rel}:{i} status obsoleto: {line.strip()[:90]}")


def check_r3_disclaimer(root, fails):
    for name in R3_FILES:
        p = root / name
        if not p.exists():
            fail(fails, "R3", f"{name} nao encontrado")
            continue
        txt = p.read_text(encoding="utf-8").lower()
        if "peer review" not in txt or ("não é" not in txt and
                                        "nao e" not in txt and
                                        "não equivale" not in txt):
            fail(fails, "R3", f"{name} sem disclaimer "
                              "'NÃO é peer review'")


def check_r4_ddres_conditional(root, fails):
    for name in R4_FILES:
        p = root / name
        if not p.exists():
            fail(fails, "R4", f"{name} nao encontrado")
            continue
        txt = p.read_text(encoding="utf-8").lower()
        if "dd_res" in txt and "auditoria externa pendente" not in txt:
            fail(fails, "R4", f"{name} cita DD_Res sem 'auditoria externa "
                              "pendente'")


def _local_link_targets(md_text):
    """alvos locais de links markdown [..](alvo) (ignora http/#)."""
    for m in re.finditer(r"\]\(([^)\s]+)\)", md_text):
        t = m.group(1)
        if t.startswith(("http://", "https://", "#", "mailto:")):
            continue
        yield t.split("#")[0]


def check_r5_links(root, fails):
    for name in DOCS_LINKED_FROM:
        p = root / name
        if not p.exists():
            continue
        for t in _local_link_targets(p.read_text(encoding="utf-8")):
            if not t:
                continue
            if not (root / t).exists():
                fail(fails, "R5", f"{name}: link quebrado -> {t}")


def check_r6_shas(root, fails):
    """JSON com csv_sha256 deve bater com o CSV indicado."""
    checked = 0
    for jp in root.glob("gk_*.json"):
        try:
            data = json.loads(jp.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        meta = data.get("metadata", data)
        if not isinstance(meta, dict):
            continue
        sha = meta.get("csv_sha256")
        csv_name = meta.get("csv")
        if not sha or not csv_name:
            continue
        cp = root / csv_name
        if not cp.exists():
            fail(fails, "R6", f"{jp.name}: CSV ausente ({csv_name})")
            continue
        actual = hashlib.sha256(cp.read_bytes()).hexdigest()
        if actual != sha:
            fail(fails, "R6",
                 f"{jp.name}: sha256 divergente (JSON {sha[:12]}… vs "
                 f"CSV {actual[:12]}…)")
        checked += 1
    return checked


def check_r7_lean_json(root, fails):
    p = root / "gk_lean_verification.json"
    if not p.exists():
        fail(fails, "R7", "gk_lean_verification.json ausente")
        return
    d = json.loads(p.read_text(encoding="utf-8"))
    if not d.get("build_success"):
        fail(fails, "R7", "build_success != true")
    nf = d.get("summary", {}).get("not_found", None)
    if nf:
        fail(fails, "R7", f"theorems NOT_FOUND = {nf}")
    if d.get("sorry_in_sources", {}).get("Core.lean", 0) != 0:
        fail(fails, "R7", "Core.lean contem sorry (esperado 0)")


def check_r8_descartados(root, fails):
    p = root / "INDICE.md"
    if not p.exists():
        fail(fails, "R8", "INDICE.md ausente")
        return
    txt = p.read_text(encoding="utf-8")
    if "DESCARTADOS" not in txt.upper():
        fail(fails, "R8", "INDICE sem secao DESCARTADOS")
    for d in ["D1", "D2", "D3", "D4", "D5", "D6"]:
        # cada Dx deve aparecer na tabela de descartados (linha com motivo)
        if not re.search(rf"\|\s*{d}\s*\|", txt):
            fail(fails, "R8", f"INDICE sem linha {d} na tabela de descartados")


def check_r9_indexed(root, fails):
    p = root / "INDICE.md"
    if not p.exists():
        return
    txt = p.read_text(encoding="utf-8")
    for name in R9_CANONICAL:
        if name not in txt:
            fail(fails, "R9", f"{name} nao indexado no INDICE")


def check_r10_lean_scope(root, fails):
    p = root / "README.md"
    if not p.exists():
        fail(fails, "R10", "README ausente")
        return
    txt = p.read_text(encoding="utf-8").lower()
    if "np≠conp" not in txt and "np != conp" not in txt and \
       "np≠conp" not in txt and "nao está formalizado" not in txt and \
       "não está formalizado" not in txt:
        fail(fails, "R10", "README sem aviso de escopo do Lean "
                           "(o que NAO esta formalizado)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    fails = []
    try:
        check_r1_retracted(root, fails)
        check_r2_stale_status(root, fails)
        check_r3_disclaimer(root, fails)
        check_r4_ddres_conditional(root, fails)
        check_r5_links(root, fails)
        n6 = check_r6_shas(root, fails)
        check_r7_lean_json(root, fails)
        check_r8_descartados(root, fails)
        check_r9_indexed(root, fails)
        check_r10_lean_scope(root, fails)
    except Exception as e:  # erro de execucao
        print(f"[ERRO] {type(e).__name__}: {e}")
        return 2

    print("=" * 66)
    print("GK CLAIMS LINT — consistencia de claims / reprodutibilidade")
    print("=" * 66)
    print(f"  R1 guardas de retraidos ....... {'OK' if not any(f.startswith('[R1]') for f in fails) else 'FALHA'}")
    print(f"  R2 status obsoletos ........... {'OK' if not any(f.startswith('[R2]') for f in fails) else 'FALHA'}")
    print(f"  R3 disclaimer peer review ..... {'OK' if not any(f.startswith('[R3]') for f in fails) else 'FALHA'}")
    print(f"  R4 DD_Res condicional ......... {'OK' if not any(f.startswith('[R4]') for f in fails) else 'FALHA'}")
    print(f"  R5 links locais ............... {'OK' if not any(f.startswith('[R5]') for f in fails) else 'FALHA'}")
    print(f"  R6 sha256 CSV x JSON ({n6} pares) ... {'OK' if not any(f.startswith('[R6]') for f in fails) else 'FALHA'}")
    print(f"  R7 lean verification JSON ..... {'OK' if not any(f.startswith('[R7]') for f in fails) else 'FALHA'}")
    print(f"  R8 DESCARTADOS D1-D6 .......... {'OK' if not any(f.startswith('[R8]') for f in fails) else 'FALHA'}")
    print(f"  R9 docs canonicos indexados ... {'OK' if not any(f.startswith('[R9]') for f in fails) else 'FALHA'}")
    print(f"  R10 escopo Lean no README ..... {'OK' if not any(f.startswith('[R10]') for f in fails) else 'FALHA'}")
    print("-" * 66)
    if fails:
        print(f"FALHAS ({len(fails)}):")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("*** LINT OK: claims consistentes, evidencias verificaveis ***")
    return 0


if __name__ == "__main__":
    sys.exit(main())

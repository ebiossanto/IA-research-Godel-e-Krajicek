#!/usr/bin/env python3
"""
gk_alternating_family.py — Teste N2 do criterio-LP para a familia alternante
(C2.3) — decide o destino da via LP da rota negativa (r2 §5).

Candidato testado (o do proprio projeto): dado γ (CNF sobre x_1..x_n),
    Λ₁ := γ                      (insat ⟺ γ ∈ UNSAT)
    Λ₂ := REF_t(γ)               ("existe refutacao Res de γ em ≤ t passos")
REF_t(γ) e UNSAT ⟺ γ nao tem refutacao de tamanho ≤ t (γ sat ⇒ sempre unsat).

Testes (seed fixa, saidas JSON/CSV):
  T1 ALTERNANCIA: para cada γ amostrado, resolver γ e REF_t(γ);
     contar casos "exatamente um lado insat" vs "ambos insat" (falha de
     alternancia = γ insat com refutacao > t).
  T2 LINHAS MISTAS: para a uniao Λ₁⊎Λ₂ (sempre insat), obter prova DRAT do
     solver e contar clausulas ADICIONADAS que misturam variaveis x (lado 1)
     e y (lado 2) — violacao de linha-pura na prova do solver.
  T3 CONTROLE: prova DRAT do lado insat SOZINHO — deve ser 0 mistas
     (π "limpa" existe, mas exige saber o lado — circular p/ a reducao).

Leitura dos resultados vs criterio-LP (r2 §5):
  - se T2 achar mistas com frequencia: provas de solver nao sao linha-puras
    -> a reducao precisaria CONSTRUIR pi (e o Teorema de Necessidade do doc
    mostra que, para γ insat dificil, pi linha-pura poli NAO EXISTE);
  - T1 quantifica a alternancia do candidato (onde (C2.3) aguenta e onde quebra).

Uso: python gk_alternating_family.py [--n 4] [--t 6] [--samples 120] [--seed 20261119]
"""

import argparse
import csv
import hashlib
import itertools
import json
import random
from datetime import datetime, timezone
from pathlib import Path

try:
    from pysat.solvers import Cadical195, Glucose4
    PYSAT_OK = True
except ImportError:
    PYSAT_OK = False

OUT_JSON = Path("gk_alternating_family.json")
OUT_CSV = Path("gk_alternating_family.csv")
# (os nomes ganham sufixo _t{T}_n{N} no main p/ nao se sobrescreverem)


# ---------------- clauses over x_1..x_n (sem tautologias) ----------------
def all_clauses(n):
    """todas as clausulas sobre n vars: cada var em {abs,+,-}.
    Na representacao ternaria por variavel NAO existem tautologias
    (cada var aparece no maximo uma vez) — o antigo filtro
    `1 in tri and -1 in tri` excluia erroneamente clausulas validas
    como {1,-2} (vars diferentes) — bug-raiz do REF insatisfativel."""
    out = []
    for tri in itertools.product((0, 1, -1), repeat=n):
        cl = tuple(i + 1 for i, v in enumerate(tri) if v == 1) + \
             tuple(-(i + 1) for i, v in enumerate(tri) if v == -1)
        out.append(frozenset(cl))
    return out


def sample_gamma(rng, n, m):
    """γ aleatorio: m clausulas 3-literal (sem tautologias) sobre n vars."""
    lits = list(range(1, n + 1)) + [-i for i in range(1, n + 1)]
    clauses = set()
    while len(clauses) < m:
        l = rng.sample(lits, min(3, len(lits)))
        if any(-x in l for x in l):
            continue
        clauses.add(frozenset(l))
    return [frozenset(c) for c in clauses]


# ---------------- REF_t(gamma): CNF "existe refutacao em <= t passos" ----
def res_pairs(c, n, index):
    """Todos os pares (c1,c2) com resolvente exatamente c:
    c1 = S1 u {l}, c2 = S2 u {~l}, S1 u S2 = c, S1,S2 ⊆ c (subconjuntos!).
    (A versao anterior so tinha S1=S2=c — incompleta: ex. [-1] resolve
    [1,2] -> [2] exige S2=∅.)"""
    out = []
    cl = list(c)
    for v in range(1, n + 1):
        for sgn in (1, -1):
            l = sgn * v
            for mask in range(1 << len(cl)):
                s1 = frozenset(cl[i] for i in range(len(cl)) if (mask >> i) & 1)
                s2 = c - s1
                # sonsidade: c1\{l} = s1 exige l ∉ s1 (e ¬l ∉ s1 p/ c1 valida);
                # c2\{¬l} = s2 exige ¬l ∉ s2 (e l ∉ s2 p/ c2 valida)
                if l in s1 or -l in s1 or l in s2 or -l in s2:
                    continue
                c1, c2 = s1 | {l}, s2 | {-l}
                if c1 in index and c2 in index:
                    out.append((c1, c2))
    return list(dict.fromkeys(out))  # dedup (mesmo par via l/mask diferentes)


def build_ref_t(gamma_clauses, n, t):
    """
    Variaveis: y_{j,C} id = 1 + idx_C + (j-1)*|pool| (lado 2).
    Restricoes:
      (1) y_{t,∅}
      (2) cada passo j deriva alguma clausula
      (3) y_{j,C} -> [C ∈ γ]  ∨  ⋁_{j'<j} y_{j',c} (copia)
                      ∨  ⋁_{pares} (copia(c1) ∧ copia(c2))   (corte)
      (3) implementado com auxiliar a_par por par:
          y_{j,C} -> ⋁ a_par            (com copias na MESMA clausula)
          a_par -> copia(c1); a_par -> copia(c2)
      passo 1: so folhas (y_{1,c} -> [C ∈ γ]).
    """
    pool = all_clauses(n)                       # inclui ∅
    index = {c: i for i, c in enumerate(pool)}
    N = len(pool)

    def y(j, c):
        return 1 + index[c] + (j - 1) * N

    gamma_set = set(gamma_clauses)
    next_aux = 1 + N * t
    cnf = [[y(t, frozenset())]]                              # (1)
    for j in range(1, t + 1):
        cnf.append([y(j, c) for c in pool])                  # (2a) ≥1
        # (2b) EXATAMENTE-UM por posicao: a semantica correta e
        # "sequencia de <= t LINHAS" (nao profundidade em camadas —
        # com folhas em paralelo o t antigo contava profundidade)
        for i1 in range(N):
            for i2 in range(i1 + 1, N):
                cnf.append([-y(j, pool[i1]), -y(j, pool[i2])])
    for j in range(1, t + 1):
        for c in pool:
            if c in gamma_set:
                continue                                     # folha livre
            yc = y(j, c)
            copies = [y(jp, c) for jp in range(1, j)]
            if j == 1:
                cnf.append([-yc])                            # passo1: so folha
                continue
            pairs = res_pairs(c, n, index)
            if not pairs:
                cnf.append([-yc] + copies)                   # so copia
                continue
            auxs = []
            for (c1, c2) in pairs:
                a = next_aux
                next_aux += 1
                auxs.append(a)
                cnf.append([-a] + [y(jp, c1) for jp in range(1, j)])
                cnf.append([-a] + [y(jp, c2) for jp in range(1, j)])
            # yc -> copia OU corte: UM so OR (correcao do bug AND)
            cnf.append([-yc] + copies + auxs)
    seen, out = set(), []
    for cl in cnf:
        f = frozenset(cl)
        if f not in seen:
            seen.add(f)
            out.append(sorted(f))
    return out, next_aux - 1


# ---------------- solve helpers ----------------
def solve(clauses, proof=False):
    clauses = [sorted(c) for c in clauses]   # pysat exige listas de int
    try:
        with Cadical195(bootstrap_with=clauses, with_proof=proof) as s:
            ok = s.solve()
            pr = s.get_proof() if (proof and not ok) else None
            return ("UNSAT" if not ok else "SAT"), pr
    except Exception:
        with Glucose4(bootstrap_with=clauses, with_proof=proof) as s:
            ok = s.solve()
            pr = s.get_proof() if (proof and not ok) else None
            return ("UNSAT" if not ok else "SAT"), pr


def mixed_additions(proof_lines, split_var):
    """Conta clausulas ADICIONADAS da prova DRAT ASCII com literais dos DOIS
    lados (|lit| <= split_var = lado 1; > split_var = lado 2).
    Formato: adicao = linha de literais (ex.: '1 -2 0'); deletao = 'd ... 0'."""
    if not proof_lines:
        return 0, 0
    mixed = adds = 0
    for ln in proof_lines:
        if isinstance(ln, bytes):
            ln = ln.decode("utf-8", "replace")
        ln = ln.strip()
        if not ln or ln[0] in "dD":
            continue  # deletions
        if ln[0] in "aA":          # variante com prefixo 'a'
            ln = ln[1:].strip()
        toks = ln.split()
        if not toks or toks[-1] != "0":
            continue               # so linhas DRAT completas
        try:
            lits = [int(x) for x in toks[:-1]]
        except ValueError:
            continue
        if not lits:
            adds += 1              # clausula vazia: nao mista
            continue
        adds += 1
        s1 = any(1 <= abs(l) <= split_var for l in lits)
        s2 = any(abs(l) > split_var for l in lits)
        if s1 and s2:
            mixed += 1
    return mixed, adds


# ---------------- main ----------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--t", type=int, default=6)
    ap.add_argument("--samples", type=int, default=120)
    ap.add_argument("--m-min", type=int, default=10)
    ap.add_argument("--m-max", type=int, default=30)
    ap.add_argument("--seed", type=int, default=20261119)
    args = ap.parse_args()
    if not PYSAT_OK:
        print("[ERRO] pip install python-sat")
        return 2
    rng = random.Random(args.seed)
    n, t = args.n, args.t

    rows = []
    alt_ok = alt_fail = 0
    mixed_union = union_total = 0
    mixed_side = side_total = 0

    for i in range(args.samples):
        m = rng.randint(args.m_min, args.m_max)
        gamma = sample_gamma(rng, n, m)
        ref_cnf, y_max = build_ref_t(gamma, n, t)
        split = n  # lados: x <= n ; y > n

        g_stat, _ = solve(gamma)
        r_stat, _ = solve(ref_cnf)
        # alternancia: exatamente um lado insat
        g_unsat = g_stat == "UNSAT"
        r_unsat = r_stat == "UNSAT"
        alt = g_unsat != r_unsat  # XOR
        if alt:
            alt_ok += 1
        else:
            alt_fail += 1

        # uniao (sempre insat) — prova DRAT + scan de mistas
        union = gamma + ref_cnf
        u_stat, u_proof = solve(union, proof=True)
        n_mix, n_add = (0, 0)
        if u_stat == "UNSAT":
            union_total += 1
            n_mix, n_add = mixed_additions(u_proof, split)
            if n_mix:
                mixed_union += 1

        # controle: lado insat sozinho
        side = gamma if g_unsat else ref_cnf
        s_stat, s_proof = solve(side, proof=True)
        smix, sadd = (0, 0)
        if s_stat == "UNSAT":
            side_total += 1
            smix, sadd = mixed_additions(s_proof, split)
            if smix:
                mixed_side += 1

        rows.append({
            "i": i, "m": m, "gamma": g_stat, "ref_t": r_stat,
            "alternating": alt, "union": u_stat,
            "union_adds": n_add, "union_mixed": n_mix,
            "side_adds": sadd, "side_mixed": smix,
        })

    # ---------------- relatorio ----------------
    print("=" * 70)
    print(f"TESTE LP — familia alternante candidata (γ, REF_{t}(γ))  n={n}")
    print("=" * 70)
    print(f"Amostras: {len(rows)} | seed={args.seed} | "
          f"γ insat: {sum(1 for r in rows if r['gamma']=='UNSAT')}")
    print(f"\nT1 ALTERNANCIA: exatamente um lado insat em "
          f"{alt_ok}/{len(rows)} ({alt_ok/len(rows):.1%})")
    print(f"  falhas (ambos insat = γ insat com ref > t): {alt_fail}")
    if alt_fail:
        fails = [r for r in rows if not r["alternating"]]
        print(f"  ex.: m={fails[0]['m']} γ={fails[0]['gamma']} "
              f"REF_t={fails[0]['ref_t']}")
    print(f"\nT2 LINHAS MISTAS na prova DRAT da UNIAO: "
          f"{mixed_union}/{union_total} instancias com ≥1 clausula mista")
    print(f"T3 CONTROLE (lado insat sozinho): "
          f"{mixed_side}/{side_total} com mistas (esperado 0)")
    tot_add = sum(r["union_adds"] for r in rows)
    tot_mix = sum(r["union_mixed"] for r in rows)
    print(f"  total de adicoes na uniao: {tot_add}; mistas: {tot_mix}")

    # ---------------- saidas ----------------
    out_json = Path(f"gk_alternating_family_t{t}_n{n}.json")
    out_csv = Path(f"gk_alternating_family_t{t}_n{n}.csv")
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    sha = hashlib.sha256(out_csv.read_bytes()).hexdigest()

    payload = {
        "metadata": {
            "timestamp_utc": datetime.now(timezone.utc).isoformat()
                             .replace("+00:00", "Z"),
            "data_source": "gk_alternating_family.py (teste LP C2.3)",
            "seed": args.seed, "n": n, "t": t, "samples": args.samples,
            "m_range": [args.m_min, args.m_max],
            "csv": out_csv.name, "csv_sha256": sha,
        },
        "T1_alternancia": {"ok": alt_ok, "fail": alt_fail,
                           "rate": alt_ok / len(rows)},
        "T2_uniao_mistas": {"instancias_com_mistas": mixed_union,
                            "total": union_total,
                            "adicoes": tot_add, "mistas": tot_mix},
        "T3_controle_lado_sozinho": {"com_mistas": mixed_side,
                                     "total": side_total},
        "leitura_criterio_LP": (
            "Se T2 > 0: provas de solver da uniao NAO sao linha-puras. "
            "Pelo Teorema de Necessidade (C2_r2... doc): para γ insat dificil, "
            "pi linha-pura poli NAO existe -> criterio-LP responde MISTO -> "
            "RETRACAO desta via para a rota negativa; sobra C2.2 (promessa "
            "fraca), permanece (C)."
        ),
        "rows": rows,
    }
    out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"\n[OK] {out_json.name} + {out_csv.name} (sha256={sha[:16]}…)")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

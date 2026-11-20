#!/usr/bin/env python3
"""
gk_minref.py — Comprimento MINIMO de refutacao (exato) via gadget REF_t.

Arquitetura (v2 — a v1 tinha o bug de pares particionados: a resolucao
permite SOBREPOSICAO dos pais, ex. (a∨b),(b∨¬a) -> (b); pares so com
S1∪S2 = C disjuntos perdem passos validos e inflavam o minref):

  1. FECHO de resolucao de γ (saturacao sem tautologias — tautologias
     nunca sao necessarias numa refutacao e nao existem no pool ternario);
     γ SAT ⟺ ∅ ∉ fecho.
  2. pool = FECHO (limitado a n<=6: |fecho| <= 3^n) — qualquer derivação
     usa só clausulas do fecho (WLOG) => completude por construcao.
  3. Pares enumerados por forca bruta sobre o fecho: todo (c1,c2) com
     resolvente valido — inclui sobreposicoes (bug da v1 corrigido).
  4. REF_t(γ) com semantica de LINHAS (exatamente-um por posicao; AMO
     sequencial O(|fecho|)) — mesma semantica validada na fronteira
     (units=3, ABC=6, sat=None).

Modos:
  demo         suite de validacao + regressao do caso random2sat + limite
               superior por saturacao (minref <= |sequencia|)
  dimacs FILE  minref de instancia DIMACS (variaveis efetivas <= 6)
  --benchmark  familias sinteticas -> gk_minref_results.{csv,json}

Escopo honesto: n<=6; comprimento de REFUTACAO RESOLUCAO; sem claims de
lower bound geral.

Uso:
  python gk_minref.py demo
  python gk_minref.py dimacs instancia.cnf
  python gk_minref.py --benchmark --seed 20261119
"""

import argparse
import csv
import hashlib
import json
import random
import sys
import time
from pathlib import Path

from gk_alternating_family import solve

MAXVARS = 6
TMAX = 64
AMO = "seq"
MAX_AUX = 400_000      # orcamento de auxiliares por build (clausulas ~2x)


# ---------------- fecho + pares ----------------
def saturation(gamma):
    """Fecho de resolucao (sem tautologias), ordem deterministica.
    Retorna (lista_ordenada, set) ou None se gamma SAT (∅ ∉ fecho)."""
    gamma = [frozenset(c) for c in gamma]
    derived = {}
    def add(c, p1=None, p2=None):
        if c not in derived:
            derived[c] = (p1, p2)
            return True
        return False
    for c in sorted(gamma, key=sorted):
        add(c)
    changed = True
    while changed:
        changed = False
        for c1 in sorted(derived, key=sorted):
            for c2 in sorted(derived, key=sorted):
                if c1 == c2:
                    continue
                s1, s2 = set(c1), set(c2)
                for l in sorted(s1):
                    if -l in s2:
                        res = frozenset((s1 - {l}) | (s2 - {-l}))
                        if any(-x in res for x in res):
                            continue
                        if add(res, c1, c2):
                            changed = True
    if frozenset() not in derived:
        return None
    order = sorted(derived, key=lambda c: (len(c), sorted(c)))
    return order, derived


def closure_pairs(order):
    """Todo par (c1,c2) do fecho cujo resolvente (por algum l) e valido.
    Inclui sobreposicoes — correcao do bug da v1. Retorna dict C -> [(c1,c2)]."""
    pairs = {}
    for i, c1 in enumerate(order):
        for c2 in order[i:]:            # simetrico: (c1,c2) e (c2,c1)
            s1, s2 = set(c1), set(c2)
            for l in sorted(s1):
                if -l in s2:
                    res = frozenset((s1 - {l}) | (s2 - {-l}))
                    if any(-x in res for x in res):
                        continue
                    pairs.setdefault(res, set()).add(
                        (c1, c2) if c1 <= c2 or True else (c2, c1))
                    pairs[res].add((c2, c1))
    return {k: sorted(v, key=lambda p: (sorted(p[0]), sorted(p[1])))
            for k, v in pairs.items()}


# ---------------- REF_t sobre o fecho ----------------
def build_ref(order, pairs, leaves, t, amo="seq"):
    index = {c: i for i, c in enumerate(order)}
    N = len(order)
    def y(j, c):
        return 1 + index[c] + (j - 1) * N
    next_aux = 1 + N * t
    cnf = [[y(t, frozenset())]]                                # (1)
    for j in range(1, t + 1):
        cnf.append([y(j, c) for c in order])                   # (2a) >=1
        if amo == "seq":
            if N >= 2:
                r = list(range(next_aux, next_aux + N - 1))
                next_aux += N - 1
                cnf.append([-y(j, order[0]), r[0]])
                for i in range(1, N - 1):
                    cnf.append([-y(j, order[i]), r[i]])
                    cnf.append([-r[i - 1], r[i]])
                for i in range(1, N):
                    cnf.append([-y(j, order[i]), -r[i - 1]])
        else:  # pairwise
            for i1 in range(N):
                for i2 in range(i1 + 1, N):
                    cnf.append([-y(j, order[i1]), -y(j, order[i2])])
    for j in range(1, t + 1):
        for c in order:
            yc = y(j, c)
            if c in leaves:
                continue                                        # folha livre
            copies = [y(jp, c) for jp in range(1, j)]
            if j == 1:
                cnf.append([-yc])                               # so folha no passo 1
                continue
            ps = pairs.get(c, [])
            if not ps:
                cnf.append([-yc] + copies)
                continue
            auxs = []
            for (c1, c2) in ps:
                a = next_aux
                next_aux += 1
                auxs.append(a)
                cnf.append([-a] + [y(jp, c1) for jp in range(1, j)])
                cnf.append([-a] + [y(jp, c2) for jp in range(1, j)])
            cnf.append([-yc] + copies + auxs)
    seen, out = set(), []
    for cl in cnf:
        f = frozenset(cl)
        if f not in seen:
            seen.add(f)
            out.append(sorted(f))
    return out


# ---------------- nucleo ----------------
def effective_vars(gamma):
    vs = {abs(l) for c in gamma for l in c}
    return len(vs), (max(vs) if vs else 0)


def check_scope(gamma):
    ne, _ = effective_vars(gamma)
    if ne > MAXVARS:
        raise SystemExit(
            f"[ESCOPO] {ne} variaveis efetivas > {MAXVARS}: o fecho/pool "
            f"tem ate 3^n clausulas (inviable). minref cobre n <= {MAXVARS}.")
    return ne


def minref(gamma, nvars=None, tmax=TMAX, amo=AMO, with_sat_len=False):
    """(minref | None se SAT | ('>', t, nota)); opcional devolve |fecho|."""
    gamma = [frozenset(c) for c in gamma]
    st, _ = solve(gamma)
    if st == "SAT":
        return (None, None) if with_sat_len else None
    sat = saturation(gamma)
    if sat is None:
        return (None, None) if with_sat_len else None
    order, _ = sat
    pairs = closure_pairs(order)
    leaves = set(gamma)
    sat_len = len(order)
    # orcamento: auxs ~ t * pares-nao-folha — fecha com t <= t_cap
    total_pairs = sum(len(v) for k, v in pairs.items() if k not in leaves)
    t_cap = min(tmax, MAX_AUX // max(1, total_pairs))
    if t_cap < 1:
        return (("> ", "orcamento", f"{total_pairs} pares"), sat_len) \
            if with_sat_len else (">", "orcamento")
    lo, hi, t = 0, None, 1
    while t <= t_cap:
        ref = build_ref(order, pairs, leaves, t, amo=amo)
        if solve(ref)[0] == "SAT":
            hi = t
            break
        lo = t
        t *= 2
    if hi is None:
        res = (">", t_cap, "orcamento/tmax") if t_cap < tmax else \
              (">", tmax, "tmax")
        return (res, sat_len) if with_sat_len else res
    while hi - lo > 1:
        mid = (lo + hi) // 2
        ref = build_ref(order, pairs, leaves, mid, amo=amo)
        if solve(ref)[0] == "SAT":
            hi = mid
        else:
            lo = mid
    return (hi, sat_len) if with_sat_len else hi


def read_dimacs(path):
    nvars, clauses, cur = None, [], []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("c"):
            continue
        if line.startswith("p"):
            nvars = int(line.split()[2])
            continue
        for tok in line.split():
            v = int(tok)
            if v == 0:
                clauses.append(frozenset(cur))
                cur = []
            else:
                cur.append(v)
    return nvars, clauses


# ---------------- demo ----------------
def run_demo():
    print("=" * 70)
    print("MINREF — suite de validacao (fronteiras conhecidas + regressoes)")
    print("=" * 70)
    ok = True

    suite = [
        ("unidades {[1],[-1]}", [frozenset([1]), frozenset([-1])], 3),
        # ABC: min real = 5 (L1=[1,-2], L2=[1,2], L3=[-1], L4=res(L1,L2
        # em x2)=[1], L5=res(L4,L3)=∅). A v1 (pares particionados) reportava
        # 6 — perdia o passo com SOBREPOSICAO ({1} nos dois pais) — 6o bug,
        # descoberto pelo desenvolvimento do minref.
        ("ABC (5 = min real; v1 particionado dizia 6)",
         [frozenset([1, 2]), frozenset([1, -2]), frozenset([-1])], 5),
        ("gamma SAT", [frozenset([1, 2])], None),
    ]
    for name, g, expect in suite:
        got = minref(g)
        mark = "OK" if got == expect else "FALHA"
        if got != expect:
            ok = False
        print(f"  [{mark}] {name}: minref={got} (esperado {expect})")

    # regressao do caso que expôs o bug de sobreposicao (v1 -> >64)
    print("\n  regressao random2sat (bug sobreposicao da v1):")
    for fam, n, g in gen_families(20261119):
        if fam == "random2sat_n5_m12" and solve(g)[0] == "UNSAT":
            mr, sat_len = minref(g, with_sat_len=True)
            sane = isinstance(mr, int) and mr <= sat_len
            mark = "OK" if sane else "FALHA"
            if not sane:
                ok = False
            print(f"    [{mark}] minref={mr} <= |fecho|={sat_len} "
                  f"(encoder v1 com pares particionados reportava >64 "
                  f"nesta classe)")
            break

    print("-" * 70)
    print("*** VALIDACAO OK ***" if ok else "*** VALIDACAO FALHOU ***")
    return 0 if ok else 1


# ---------------- familias / benchmark ----------------
def gen_families(seed):
    """Familias com FECHO pequeno (dominio de projeto do minref: fecho
    <= ~100 clausulas). random-3SAT de n=5 produz fechos ~200 que estouram
    o orcamento de auxiliares — fora do escopo declarado (v1 do benchmark
    estourou timeout por isso)."""
    rng = random.Random(seed)
    insts = []
    # F1: random-2SAT n=5 (fecho <= units+2-clauses = 50)
    for m in (12, 16):
        for s in range(3):
            lits = list(range(1, 6)) + [-i for i in range(1, 6)]
            cls = set()
            while len(cls) < m:
                l = rng.sample(lits, 2)
                if any(-x in l for x in l):
                    continue
                cls.add(frozenset(l))
            insts.append((f"random2sat_n5_m{m}", 5, sorted(cls, key=sorted)))
    # F2: random-2SAT n=6 (fecho <= 12 + 60 = 72)
    for m in (15, 20):
        for s in range(3):
            lits = list(range(1, 7)) + [-i for i in range(1, 7)]
            cls = set()
            while len(cls) < m:
                l = rng.sample(lits, 2)
                if any(-x in l for x in l):
                    continue
                cls.add(frozenset(l))
            insts.append((f"random2sat_n6_m{m}", 6, sorted(cls, key=sorted)))
    # F3: cadeia unitaria (refutacao por propagacao)
    for k in (3, 4, 5):
        cls = [frozenset([1])]
        for i in range(1, k):
            cls.append(frozenset([-i, i + 1]))
        cls.append(frozenset([-k]))
        insts.append((f"cadeia_k{k}", k, cls))
    # F4: variantes de SOBREPOSICAO (o bug da v1) — ABC + ruido
    base = [frozenset([1, 2]), frozenset([1, -2]), frozenset([-1])]
    insts.append(("sobreposicao+u", 5, base + [frozenset([3])]))
    insts.append(("sobreposicao+e", 5, base + [frozenset([-3, 4])]))
    return insts


def _fmt_mr(mr):
    if mr is None:
        return "SAT"
    if isinstance(mr, tuple):
        return f">{mr[1]}({mr[2]})"
    return str(mr)


def run_benchmark(seed):
    print("=" * 70)
    print(f"MINREF — benchmark (seed={seed}, tmax={TMAX}, amo={AMO})")
    print("=" * 70)
    rows = []
    for fam, n, gamma in gen_families(seed):
        t0 = time.time()
        st, _ = solve(gamma)
        if st == "SAT":
            mr, sat_len = None, None
        else:
            mr, sat_len = minref(gamma, with_sat_len=True)
        dt = round(time.time() - t0, 2)
        rows.append({"family": fam, "n_vars": n, "n_clauses": len(gamma),
                     "sat": st, "minref": _fmt_mr(mr),
                     "fecho": sat_len, "seconds": dt})
        print(f"  {fam:20} cl={len(gamma):3} {st:4} minref={_fmt_mr(mr)} "
              f"fecho={sat_len} ({dt}s)", flush=True)

    csv_path = Path("gk_minref_results.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    sha = hashlib.sha256(
        csv_path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    dist = {}
    for r in rows:
        if r["sat"] == "UNSAT":
            k = r["minref"]
            dist[k] = dist.get(k, 0) + 1
    payload = {
        "metadata": {
            "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "data_source": "gk_minref.py v2 (fecho + pares completos)",
            "seed": seed, "tmax": TMAX, "amo": AMO,
            "csv": csv_path.name, "csv_sha256": sha,
            "sha_note": "sha256 sobre bytes normalizados CRLF->LF",
            "escopo": "n<=6; resolucao (nao DRAT/EF); sem claim de "
                      "lower bound geral",
        },
        "distribution_minref": dist,
        "rows": rows,
    }
    Path("gk_minref_results.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[OK] gk_minref_results.csv/json (sha256={sha[:16]}…)")
    print(f"dist minref (UNSAT): {dist}")
    print("=" * 70)
    return 0


# ---------------- main ----------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", nargs="?", choices=["demo", "dimacs"],
                    default="demo")
    ap.add_argument("file", nargs="?", help="arquivo DIMACS (modo dimacs)")
    ap.add_argument("--benchmark", action="store_true")
    ap.add_argument("--seed", type=int, default=20261119)
    ap.add_argument("--tmax", type=int, default=TMAX)
    args = ap.parse_args()

    if args.benchmark:
        return run_benchmark(args.seed)
    if args.mode == "dimacs":
        if not args.file:
            raise SystemExit("modo dimacs exige um arquivo")
        nvars, gamma = read_dimacs(args.file)
        check_scope(gamma)
        t0 = time.time()
        mr, sat_len = minref(gamma, with_sat_len=True)
        dt = round(time.time() - t0, 2)
        if mr is None:
            print(f"{args.file}: SAT (sem refutacao) [{dt}s]")
        elif isinstance(mr, tuple):
            print(f"{args.file}: minref > {mr[1]} ({mr[2]}) "
                  f"|fecho|={sat_len} [{dt}s]")
        else:
            print(f"{args.file}: minref = {mr} linhas "
                  f"(|fecho|={sat_len}) [{dt}s]")
        return 0
    return run_demo()


if __name__ == "__main__":
    sys.exit(main())

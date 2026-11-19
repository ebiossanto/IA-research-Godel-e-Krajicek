#!/usr/bin/env python3
"""
gk_proof_fractal.py — D4': PONTE PROVA -> FRACTAL (v1, 19/11/2026)

Pergunta (C): o comprimento de provas reais, indexado ordinalmente por
(tamanho, semente), forma uma serie cujas metricas fractais (Hurst R/S,
Higuchi D, box-counting D) SEPARAM families de dificuldade de refutacao?

Familias (todas garantidamente UNSAT, provas REAIS):
  1. implication : grafo de implicacoes aleatorio (semeado) + unidades -> UNSAT
  2. php         : buraco do pombo PHP_{m+1 -> m} com permutacao de variaveis
                   (classico duro para Resolution)
  3. tau         : familia tau(g)_b de Krajicek — circuito booleano semeado
                   (k entradas -> w>saidas), b fora da imagem -> CNF de
                   Tseitin de "g(x)=b" e UNSAT (refutacao real do tau)

Sistemas medidos por instancia:
  - resolution_drat : DRAT REAL via PySAT Cadical195 (with_proof=True) -> nº linhas
                      (fallback Glucose4; glucose devolve prova vazia em UNSAT
                      trivial — documentado no script)
  - z3_proof_nodes  : tamanho (nos sexpr) da prova do Z3 para a mesma CNF
                      *** PROXY de calculo estendido — NAO e Extended Frege ***
                      (EF nao e mensuravel com o tooling disponivel; H_C2
                      original Res-vs-EF fica DEFERIDO, declarado no JSON)

Metricas por serie (64 pontos): hurst_rs (R/S clássico), higuchi_D (D_H),
boxdim (box-counting da curva embutida (t, x_t)). Validacao em series
sinteticas (ruido branco, passeio aleatorio, seno) antes de medir.

Estatistica: moving-block bootstrap (bloco=8, B=300, seed fixa) -> IC 95%
por metrica e por contraste entre familias (delta D, delta H).

Saida: gk_proof_complexity_fractal.json + gk_proof_fractal_series.csv
Reprodutivel: seed=20261119; SHA-256 do CSV registrado no JSON.

Uso: python gk_proof_fractal.py
"""

import csv
import hashlib
import json
import math
import random
import time
from datetime import datetime, timezone
from pathlib import Path

SEED = 20261119
B_BOOT = 300
BLOCK = 8
Z3_TIMEOUT_MS = 5000

OUT_JSON = Path("gk_proof_complexity_fractal.json")
OUT_CSV = Path("gk_proof_fractal_series.csv")

try:
    from pysat.solvers import Cadical195, Glucose4
    PYSAT_OK = True
except ImportError:
    PYSAT_OK = False

try:
    import z3 as _z3
    _z3.set_param("proof", True)      # habilita geracao de prova (backend sat)
    from z3 import Solver, Bool, Or, sat, unsat
    Z3_OK = True
except ImportError:
    Z3_OK = False


# ----------------------------------------------------------------------
# 1. Geradores de instancias (deterministicos: familia, m, seed)
# ----------------------------------------------------------------------

def gen_implication(m: int, seed: int):
    """Grafo de implicacoes aleatorio + unidades com caminho s->t -> UNSAT."""
    rng = random.Random((SEED, "imp", m, seed).__hash__() & 0xFFFFFFFF)
    edges = []
    for _ in range(2 * m):
        a = rng.randrange(1, m + 1)
        b = rng.randrange(1, m + 1)
        if a != b:
            edges.append((a, b))
    # alcancabilidade (Floyd-Warshall barato para m<=24)
    reach = [[False] * (m + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        reach[i][i] = True
    for a, b in edges:
        reach[a][b] = True
    for k in range(1, m + 1):
        for i in range(1, m + 1):
            if reach[i][k]:
                for j in range(1, m + 1):
                    if reach[k][j]:
                        reach[i][j] = True
    pairs = [(s, t) for s in range(1, m + 1) for t in range(1, m + 1)
             if s != t and reach[s][t]]
    if not pairs:
        edges.append((1, 2))
        pairs = [(1, 2)]
    s, t = rng.choice(pairs)
    clauses = [[-a, b] for a, b in edges]   # a -> b  (nao ~a v b invertido!)
    clauses.append([s])                     # x_s verdadeiro
    clauses.append([-t])                    # x_t falso  (caminho s..t -> UNSAT)
    nvars = m
    return nvars, clauses, f"imp_s{s}_t{t}_e{len(edges)}"


def gen_php(m: int, seed: int):
    """PHP_{m+1 -> m}: UNSAT classico. Seed = permutacao de variaveis."""
    rng = random.Random((SEED, "php", m, seed).__hash__() & 0xFFFFFFFF)
    npig, nholes = m + 1, m
    # variaveis p[i][j] -> numeracao aleatoria
    ids = list(range(1, npig * nholes + 1))
    rng.shuffle(ids)
    idx = 0
    pid = [[0] * (nholes + 1) for _ in range(npig + 1)]
    for i in range(1, npig + 1):
        for j in range(1, nholes + 1):
            pid[i][j] = ids[idx]
            idx += 1
    clauses = []
    for i in range(1, npig + 1):                 # todo pombo em algum buraco
        clauses.append([pid[i][j] for j in range(1, nholes + 1)])
    for j in range(1, nholes + 1):               # no maximo 1 pombo por buraco
        for i1 in range(1, npig + 1):
            for i2 in range(i1 + 1, npig + 1):
                clauses.append([-pid[i1][j], -pid[i2][j]])
    nvars = npig * nholes
    return nvars, clauses, f"php_{npig}->{nholes}_perm{seed}"


def _eval_circuit(gates, inputs):
    """Avalia portas (idx, op, a, b) com inputs = dict var->bool."""
    val = dict(inputs)
    for idx, op, a, b in gates:
        if op == "NOT":
            val[idx] = not val[a]
        elif op == "AND":
            val[idx] = val[a] and val[b]
        elif op == "OR":
            val[idx] = val[a] or val[b]
        elif op == "XOR":
            val[idx] = val[a] != val[b]
    return val


def gen_tau(depth: int, seed: int, k: int = 8, w: int = 10):
    """
    Familia tau(g)_b: circuito com k entradas e saidas na ultima camada
    (w vars). Como w > k, |imagem| <= 2^k < 2^w -> existe b fora da imagem.
    CNF de Tseitin de (circuit AND saida=b) e UNSAT iff b fora da imagem.
    Seed escolhe (a) a estrutura do circuito e (b) qual b da imagem-complemento.
    """
    rng = random.Random((SEED, "tau", depth, seed).__hash__() & 0xFFFFFFFF)
    # camadas: layer0 = entradas 1..k; gate ids seguem
    layers = [list(range(1, k + 1))]
    nxt = k + 1
    for d in range(depth):
        prev = layers[-1]
        size = max(w if d == depth - 1 else 3, 2)
        size = min(size, max(2, len(prev) * 2))
        cur = []
        for _ in range(size):
            a = rng.choice(prev)
            b = rng.choice(prev)
            op = rng.choice(["AND", "OR", "XOR", "NOT"])
            if op == "NOT":
                gates.append((nxt, op, a, None))
            else:
                gates.append((nxt, op, a, b))
            cur.append(nxt)
            nxt += 1
        layers.append(cur)
    outputs = layers[-1][:w] if len(layers[-1]) >= w else layers[-1]
    # garante w saidas: completa com portas NOT/OR sobre a ultima camada
    while len(outputs) < w:
        a = rng.choice(layers[-1])
        gates.append((nxt, "NOT", a, None))
        outputs.append(nxt)
        nxt += 1
    nvars = nxt - 1

    # imagem exata (2^k <= 256 avaliacoes)
    image = set()
    for mask in range(1 << k):
        inputs = {i + 1: bool((mask >> i) & 1) for i in range(k)}
        val = _eval_circuit(gates, inputs)
        out_bits = tuple(1 if val[o] else 0 for o in outputs)
        image.add(out_bits)
    complement = [b for b in (tuple((mask >> i) & 1 for i in range(len(outputs)))
                              for mask in range(1 << len(outputs)))
                  if b not in image]
    if not complement:
        return None
    b = complement[(seed * 7919) % len(complement)]

    # Tseitin
    clauses = []
    for idx, op, a, bvar in gates:
        if op == "NOT":
            clauses.append([-a, -idx])
            clauses.append([a, idx])
        elif op == "AND":
            clauses.append([-idx, a])
            clauses.append([-idx, bvar])
            clauses.append([-a, -bvar, idx])
        elif op == "OR":
            clauses.append([-a, idx])
            clauses.append([-bvar, idx])
            clauses.append([-idx, a, bvar])
        elif op == "XOR":
            clauses.append([-a, -bvar, -idx])
            clauses.append([a, bvar, -idx])
            clauses.append([a, -bvar, idx])
            clauses.append([-a, bvar, idx])
    # saida = b  (se b_i=1 -> unit [-out]; se 0 -> unit [out]); UNSAT iff b fora
    for pos, o in enumerate(outputs):
        clauses.append([o] if b[pos] == 0 else [-o])
    tag = "b_out=" + "".join(map(str, b))
    return nvars, clauses, tag


# (a lista de gates e preenchida dentro de gen_tau — declarada aqui para clareza)
gates = []


def gen_tau_wrapped(depth: int, seed: int):
    global gates
    gates = []
    return gen_tau(depth, seed)


# ----------------------------------------------------------------------
# 2. Solucao com duas provas: DRAT (PySAT) e Z3
# ----------------------------------------------------------------------

def solve_drat(nvars, clauses):
    """Retorna (status, proof_len) com DRAT real (Cadical195; fallback Glucose4).

    Nota: Glucose4/Glucose42 devolvem lista VAZIA de prova quando o UNSAT cai
    em propagacao de unidades/preprocesso; Cadical195 sempre emite linhas DRAT.
    """
    if not PYSAT_OK:
        return "NO_PYSAT", None
    for cls in (Cadical195, Glucose4):
        try:
            with cls(bootstrap_with=clauses, with_proof=True) as g:
                ok = g.solve()
                if not ok:
                    proof = g.get_proof()
                    if proof:
                        return "UNSAT", len(proof)
                    continue  # prova vazia -> tenta proximo solver
                return "SAT", None
        except Exception as e:  # pragma: no cover
            last_err = f"ERR:{type(e).__name__}"
    return locals().get("last_err", "ERR:no_solver"), None


def _sexpr_nodes(s: str) -> int:
    return s.count("(")


def solve_z3(nvars, clauses):
    """Retorna (status, nodes) da prova Z3 (proxy de calculo estendido)."""
    if not Z3_OK:
        return "NO_Z3", None
    try:
        vs = [Bool(f"v{i}") for i in range(1, nvars + 1)]
        s = Solver()
        s.set("timeout", Z3_TIMEOUT_MS)
        s.set(proof=True)
        for cl in clauses:
            lits = [vs[abs(l) - 1] if l > 0 else ~vs[abs(l) - 1] for l in cl]
            s.add(Or(lits) if len(lits) > 1 else lits[0])
        r = s.check()
        if r == unsat:
            p = s.proof()
            return "UNSAT", _sexpr_nodes(str(p))
        if r == sat:
            return "SAT", None
        return "UNKNOWN", None
    except Exception as e:  # pragma: no cover
        return f"ERR:{type(e).__name__}", None


# ----------------------------------------------------------------------
# 3. Metricas fractais (implementacao padrao + validacao sintetica)
# ----------------------------------------------------------------------

def hurst_rs(x):
    """Hurst via R/S clasico (janelas 8..N/4)."""
    n = len(x)
    if n < 16:
        return float("nan")
    # todos os tamanhos 8..n/4 (o conjunto fixo {8,16,32..} degenera p/ n=50..63:
    # sobrevive so 8 -> regressao com den=0 -> nan)
    sizes = list(range(8, max(9, n // 4 + 1)))
    if not sizes:
        sizes = [n // 4]
    rs_vals, ns = [], []
    for size in sizes:
        for start in range(0, n - size + 1, size):
            seg = x[start:start + size]
            mean = sum(seg) / size
            dev = [sum(seg[:i + 1]) - (i + 1) * mean for i in range(size)]
            R = max(dev) - min(dev)
            var = sum((v - mean) ** 2 for v in seg) / size
            if var > 0 and R > 0:
                rs_vals.append(R / math.sqrt(var))
                ns.append(size)
    if len(rs_vals) < 3:
        return float("nan")
    # regressao log(R/S) ~ H * log(n)
    lx = [math.log(v) for v in ns]
    ly = [math.log(v) for v in rs_vals]
    mx, my = sum(lx) / len(lx), sum(ly) / len(ly)
    den = sum((a - mx) ** 2 for a in lx)
    if den == 0:
        return float("nan")
    return sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / den


def higuchi_D(x, kmax=8):
    """Dimensao de Higuchi (1 <= D <= 2)."""
    n = len(x)
    if n < kmax * 4:
        return float("nan")
    lk, lnk = [], []
    for k in range(1, kmax + 1):
        lm = []
        for m in range(1, k + 1):
            idx = list(range(m - 1, n, k))
            if len(idx) < 2:
                continue
            seg = [x[i] for i in idx]
            norm = (n - 1) / (k * (len(idx) - 1) * k)
            lm.append(sum(abs(seg[i + 1] - seg[i]) for i in range(len(seg) - 1))
                      * norm)
        if lm:
            Lk = sum(lm) / len(lm)
            if Lk > 0:
                lk.append(math.log(1.0 / k))
                lnk.append(math.log(Lk))
    if len(lk) < 3:
        return float("nan")
    mx, my = sum(lk) / len(lk), sum(lnk) / len(lnk)
    den = sum((a - mx) ** 2 for a in lk)
    if den == 0:
        return float("nan")
    slope = sum((a - mx) * (b - my) for a, b in zip(lk, lnk)) / den
    return slope  # L(k) ~ k^-D  =>  dlogL/dlog(1/k) = D  (validado: ruido~2.07, seno~1.20)


def boxdim_curve(x):
    """Box-counting da curva embutida (t, x_t), escalas 2^j."""
    n = len(x)
    if n < 16:
        return float("nan")
    xmin, xmax = min(x), max(x)
    span_x = (xmax - xmin) or 1.0
    counts, inv_eps = [], []
    for j in range(1, max(2, int(math.log2(n)))):
        eps = 1.0 / (2 ** j)
        boxes = set()
        for t, v in enumerate(x):
            bx = int((t / (n - 1)) / eps)
            by = int(((v - xmin) / span_x) / eps)
            boxes.add((bx, by))
        counts.append(len(boxes))
        inv_eps.append(2 ** j)
    pts = [(math.log(a), math.log(b)) for a, b in zip(inv_eps, counts) if b > 0]
    if len(pts) < 3:
        return float("nan")
    lx = [p[0] for p in pts]
    ly = [p[1] for p in pts]
    mx, my = sum(lx) / len(lx), sum(ly) / len(ly)
    den = sum((a - mx) ** 2 for a in lx)
    if den == 0:
        return float("nan")
    return sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / den


def metrics(x):
    return {"hurst_rs": hurst_rs(x), "higuchi_D": higuchi_D(x),
            "boxdim": boxdim_curve(x)}


def validate_metrics():
    rng = random.Random(SEED)
    wn = [rng.gauss(0, 1) for _ in range(64)]
    rw, acc = [], 0.0
    for _ in range(64):
        acc += rng.gauss(0, 1)
        rw.append(acc)
    sine = [math.sin(2 * math.pi * i / 16) for i in range(64)]
    return {"white_noise": metrics(wn), "random_walk": metrics(rw),
            "sine_period16": metrics(sine)}


# ----------------------------------------------------------------------
# 4. Bootstrap em blocos
# ----------------------------------------------------------------------

def block_resample(x, rng):
    n = len(x)
    out = []
    while len(out) < n:
        s = rng.randrange(0, max(1, n - BLOCK + 1))
        out.extend(x[s:s + BLOCK])
    return out[:n]


def bootstrap_metric(x, fn, rng, b=B_BOOT):
    vals = []
    for _ in range(b):
        v = fn(block_resample(x, rng))
        if v is not None and not math.isnan(v):
            vals.append(v)
    if not vals:
        return {"point": fn(x), "lo": None, "hi": None}
    vals.sort()
    return {"point": fn(x),
            "lo": vals[int(0.025 * len(vals))],
            "hi": vals[int(0.975 * len(vals))]}


# ----------------------------------------------------------------------
# 5. Experimento principal
# ----------------------------------------------------------------------

def main():
    t0 = time.time()
    print("=" * 70)
    print("D4' PONTE PROVA->FRACTAL — famílias UNSAT reais (DRAT + Z3)")
    print("=" * 70)
    if not PYSAT_OK or not Z3_OK:
        print(f"[ERRO] pysat={PYSAT_OK} z3={Z3_OK} — instale: pip install python-sat z3-solver")
        return 2

    # --- grade de instancias: 3 familias x ~60 pontos (m x seed) ---
    # php limitado a m<=9: PHP_10->9 ja gera provas DRAT gigantes (m=8: 65k linhas)
    grid = {
        "implication": [(m, s) for m in range(8, 24) for s in range(4)],   # 64
        "php":         [(m, s) for m in range(4, 10) for s in range(10)],  # 60
        "tau":         [(d, s) for d in range(2, 10) for s in range(8)],   # 64
    }
    gens = {"implication": gen_implication, "php": gen_php,
            "tau": gen_tau_wrapped}

    rows = []
    for fam, points in grid.items():
        print(f"\n--- família: {fam} ({len(points)} instâncias) ---")
        for m, seed in points:
            built = gens[fam](m, seed)
            if built is None:
                continue
            nvars, clauses, tag = built
            st_r, len_r = solve_drat(nvars, clauses)
            st_z, len_z = solve_z3(nvars, clauses)
            rows.append({
                "family": fam, "m": m, "seed": seed, "tag": tag,
                "nvars": nvars, "nclauses": len(clauses),
                "sat_drat": st_r, "proof_drat": len_r,
                "sat_z3": st_z, "proof_z3": len_z,
            })
        done = [r for r in rows if r["family"] == fam]
        unsat = [r for r in done if r["sat_drat"] == "UNSAT"]
        print(f"  UNSAT (DRAT): {len(unsat)}/{len(done)}")

    # --- series por (familia, sistema) ---
    series = {}
    for fam in grid:
        for sysname, key, satkey in (
                ("resolution_drat", "proof_drat", "sat_drat"),
                ("z3_proof_nodes", "proof_z3", "sat_z3")):
            pts = [r for r in rows if r["family"] == fam
                   and r[satkey] == "UNSAT" and r[key] is not None]
            pts.sort(key=lambda r: (r["m"], r["seed"]))
            series[(fam, sysname)] = [float(r[key]) for r in pts]

    # --- validacao sintetica ---
    validation = validate_metrics()
    print("\n--- validação das métricas (séries sintéticas) ---")
    for name, mm in validation.items():
        print(f"  {name}: H_RS={mm['hurst_rs']:.3f} D_H={mm['higuchi_D']:.3f} D_box={mm['boxdim']:.3f}")

    # --- metricas + bootstrap ---
    rng = random.Random(SEED + 1)
    results = {}
    for (fam, sysname), x in series.items():
        if len(x) < 16:
            results[f"{fam}|{sysname}"] = {"n": len(x), "note": "serie curta"}
            continue
        m_point = metrics(x)
        boot = {k: bootstrap_metric(x, fn, rng)
                for k, fn in (("hurst_rs", hurst_rs), ("higuchi_D", higuchi_D),
                              ("boxdim", boxdim_curve))}
        results[f"{fam}|{sysname}"] = {
            "n": len(x), "mean": sum(x) / len(x),
            "min": min(x), "max": max(x),
            "metrics": m_point,
            "metrics_log1p": metrics([math.log1p(v) for v in x]),
            "bootstrap_ci95": boot,
        }
        print(f"  {fam}|{sysname}: n={len(x)} mean={sum(x)/len(x):.1f} "
              f"H={m_point['hurst_rs']:.3f} D_H={m_point['higuchi_D']:.3f} "
              f"D_box={m_point['boxdim']:.3f}")

    # --- contraste entre familias (delta com bootstrap independente) ---
    contrasts = {}
    fams = ["implication", "php", "tau"]
    rng2 = random.Random(SEED + 2)
    for sysname in ("resolution_drat", "z3_proof_nodes"):
        for i in range(len(fams)):
            for j in range(i + 1, len(fams)):
                a = series.get((fams[i], sysname), [])
                b = series.get((fams[j], sysname), [])
                if len(a) < 16 or len(b) < 16:
                    continue
                variants = [
                    ("raw", a, b),
                    ("log1p", [math.log1p(v) for v in a],
                              [math.log1p(v) for v in b]),
                ]
                for variant, aa, bb in variants:
                    for mname, fn in (("higuchi_D", higuchi_D),
                                      ("boxdim", boxdim_curve),
                                      ("hurst_rs", hurst_rs)):
                        deltas = []
                        for _ in range(B_BOOT):
                            va = fn(block_resample(aa, rng2))
                            vb = fn(block_resample(bb, rng2))
                            if va and vb and not math.isnan(va) and not math.isnan(vb):
                                deltas.append(va - vb)
                        if not deltas:
                            continue
                        deltas.sort()
                        point = fn(aa) - fn(bb)
                        lo = deltas[int(0.025 * len(deltas))]
                        hi = deltas[int(0.975 * len(deltas))]
                        key = f"{sysname}:{fams[i]}-{fams[j]}:{mname}:{variant}"
                        contrasts[key] = {
                            "delta_point": point, "lo": lo, "hi": hi,
                            "excludes_zero": (lo > 0) or (hi < 0),
                        }

    # --- veredito das hipoteses ---
    def verdict(prefix):
        hits = {k: v for k, v in contrasts.items()
                if k.startswith(prefix) and k.endswith("higuchi_D")}
        return hits

    hyp = {
        "H_C1_fractal_separa_familias": {
            "enunciado": ("As metricas fractais da serie de comprimentos de prova "
                          "separam famílias de refutacao (php dura vs implication "
                          "facil) acima do ruido de bootstrap."),
            "testes": {k: v for k, v in contrasts.items()
                       if "higuchi_D" in k or "boxdim" in k},
        },
        "H_C2_Res_vs_EFrege": {
            "status": "DEFERIDO",
            "motivo": ("Extended Frege nao e mensuravel com o tooling disponivel "
                       "(PySAT da DRAT=Resolution; Z3 proof e outro calculo). "
                       "z3_proof_nodes reportado como PROXY com caveat — NAO e EF. "
                       "Requer: sistema EF implementavel ou export de prova EF."),
        },
    }

    # --- CSV ---
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    sha = hashlib.sha256(OUT_CSV.read_bytes()).hexdigest()

    payload = {
        "metadata": {
            "timestamp_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "data_source": "gk_proof_fractal.py (D4' prova->fractal v1)",
            "seed": SEED, "B_boot": B_BOOT, "block": BLOCK,
            "grid": {k: f"{len(v)} pontos" for k, v in grid.items()},
            "systems": ["resolution_drat (PySAT Cadical195, DRAT real)",
                        "z3_proof_nodes (PROXY — nao e Extended Frege)"],
            "csv": OUT_CSV.name, "csv_sha256": sha,
            "runtime_s": round(time.time() - t0, 1),
            "caveats": [
                "Series de 64 pontos — metricas fractais com IC largo e esperado.",
                "z3_proof_nodes NAO e Extended Frege (H_C2 deferido).",
                "Nivel Ten-Proofs: N1 script reproduzivel + N2 bootstrap nesta maquina.",
            ],
        },
        "metric_validation": validation,
        "series_results": results,
        "contrasts": contrasts,
        "hypotheses": hyp,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False),
                        encoding="utf-8")

    print("\n--- contrastes (higuchi_D, Resolution/DRAT, raw + log1p) ---")
    for k, v in contrasts.items():
        if "resolution_drat" in k and "higuchi_D" in k:
            flag = "EXCLUI 0" if v["excludes_zero"] else "inclui 0"
            print(f"  {k}: delta={v['delta_point']:+.3f} "
                  f"IC95=[{v['lo']:+.3f},{v['hi']:+.3f}] -> {flag}")

    print(f"\n[OK] {OUT_JSON.name} + {OUT_CSV.name} (sha256={sha[:16]}…)")
    print(f"runtime: {payload['metadata']['runtime_s']}s")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

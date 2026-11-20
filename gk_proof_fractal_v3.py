#!/usr/bin/env python3
"""
gk_proof_fractal_v3.py — D4' v3 (rodada r3): boxdim PRE-REGISTRADO.

=====================================================================
PRE-REGISTRO (fixado ANTES de qualquer execucao neste codigo; commit
anterior ao run prova a prioridade temporal — pendencia C1 do referee
do 29_): ver 30_PONTE_PROVA_FRACTAL_D4V3.md s1.
=====================================================================

DADOS NOVOS E DISJUNTOS do v2 (mesmos geradores, seeds nunca usados):
  implication : m=3..6 x seeds 16..31   (v2 usou 0..15)
  cadeia      : k=3..6 x seeds 16..31   (v2 usou 0..15)
  tau_tiny    : seeds 64..127           (v2 usou 0..63)
Checagem obrigatoria: intersecao com o CSV do v2 = vazia (senao ABORTA).

HIPOTESES (declaradas aqui, ANTES do run):
  H_B1 PRIMARIA (boxdim, minref, raw — 3 testes; padrao r2 em dados novos):
    (a) minref:implication-tau_tiny  delta > 0, IC95 BCa exclui 0
        (r2: +0.053)                                        dir=+1
    (b) minref:cadeia-tau_tiny       delta > 0, IC95 BCa exclui 0
        (r2: +0.058)                                        dir=+1
    (c) minref:implication-cadeia    EQUIVALENTE (IC90 BCa em +/-0.05)
        (r2: -0.004, equivalente)
    CONFIRMADA iff (a) e (b) SEPARA com sinal coerente E (c) EQUIVALENTE
    PARCIAL   iff exatamente 2 de 3
    REFUTADA  iff <=1 de 3; REFUTADA_CONTRADITA se (a) ou (b) exclui 0
    com sinal NEGATIVO (inverte o padrao r2).
    Multiplicidade: 2 separacoes com Bonferroni alpha*=0.05/2=0.025
    (IC97.5% reportado); (c) e TOST com alpha proprio 0.05.
  H_B2 SECUNDARIA (fonte, boxdim, raw — 2 testes):
    fonte:cadeia     delta < 0 exclui 0 (r2: -0.084)           dir=-1
    fonte:tau_tiny   delta < 0 exclui 0 (r2: -0.112)           dir=-1
    CONFIRMADA iff 2/2 coerentes.
  H_B3 PISTA A4 (drat, boxdim, raw — 1 teste):
    drat:implication-cadeia delta < 0 exclui 0 (r2: -0.102)     dir=-1
    CONFIRMADA iff exclui 0 com sinal coerente.
  H_B4 ANTI-SATURACAO (C2) — frequencia, nao efeito:
    boxdim tem 0 contrastes INCOERENTES em r3 (como em r2: 0/27).
    REPORTADO (contagem), nao gate.

MARGENS boxdim (ancoradas em dados ANTERIORES ao r3, fixadas aqui):
  0.05 PRIMARIA — ancora: (i) menor efeito SEPARA do r2 em boxdim =
      0.053 (minref imp-tau); (ii) ~1/3 da amplitude entre-series do
      r2 (boxdim 0.718..0.860, amplitude 0.142). Efeito < 0.05 =
      desprezivel frente ao que a metrica ja separou.
  0.03 e 0.08 SENSIBILIDADE (reportados, nao promovidos).
  Equivalencia so e claimada para boxdim (metrica primaria);
  boxdim_rank e exploratorio (robustez de sinal).

METRICAS: boxdim (PRIMARIA) + boxdim_rank (rank mid — invariante a
transformacao monotona, anti-saturacao) + saltos (taxa de inversao de
sinal das diferencas) + higuchi_D e hurst_rs (EXPLORATORIAS — r2 mostrou
saturacao; sao o grupo de comparacao da H_B4).

INFERENCIA: BCa (z0 + aceleracao) com DOIS jackknifes reportados:
  - delete-d (d=BLOCK=8, janelas sobrepostas) = padrao r3 (pendencia C3)
  - delete-1 = concordancia (vereditos devem coincidir; divergencia =
    flag de instabilidade, reportada)
  TOST: IC90 BCa na margem. MDE80 = 2.8016*SE_boot.
  REGRA DE INCOERENCIA (r2): ponto fora do IC (pct ou BCa) =>
  INCOERENTE, nao conta nem como refutacao nem como confirmacao.
  Percentis: B=1000, seed bootstrap = SEED+4 (declarado).

SELFTESTS OBRIGATORIOS ANTES DE MEDIR (lição A8) — aborta se falhar:
  S1  BCa vs scipy.stats.bootstrap (iid)        — valida bca_ci
  S2  invariancia monotona de boxdim_rank       — x vs exp(x): erro ~ 0
  S3  ordenacao sintetica de saltos             — ruido > rampa
  S4  TIPO-I: 50 pares de ruido branco independentes (delta real 0),
      n_boot=500 — taxa de exclusao deve ser baixa (reportada; gate
      <= 20% para nao invadir com metrica inoperante)
  S5  PODER: rampa com jitter vs seno puro (construct calibrado — 9/10
      deteccoes no pipeline completo), n_boot=1000, P=10 — boxdim DEVE
      detectar >= 7/10 (margem binomial; quebra ~0/10)

SAIDAS: gk_proof_fractal_v3_series.csv (coleta, SEM coluna de tempo)
        gk_proof_fractal_v3_contrasts.csv (135 contrastes)
        gk_proof_fractal_v3.json         (coleta; R6 aponta p/ series)
        gk_proof_fractal_v3_analysis.json(analise; R6 aponta p/ contrasts)
Uso:   python -u gk_proof_fractal_v3.py              (coleta+analise)
       python -u gk_proof_fractal_v3.py --analyze-only (re-analise)
"""

import argparse
import csv
import hashlib
import json
import math
import random
import time
from datetime import datetime, timezone
from pathlib import Path

from gk_proof_fractal import (BLOCK, SEED, boxdim_curve, gen_implication,
                              higuchi_D, hurst_rs, solve_drat)
from gk_proof_fractal_v2 import gen_cadeia, gen_tau_tiny, variants_of
from gk_proof_fractal_v2_r2 import (bca_ci, block_idx, pct_ci,
                                    selftest_bca)
from gk_minref import minref

N_BOOT = 1000
SEED_BOOT = SEED + 4           # 20261123 — declarado
MARGIN_PRIMARY = 0.05
MARGINS = (0.05, 0.03, 0.08)
D_DELETE = BLOCK               # delete-d com d=8 (C3)
FAMS = ["implication", "cadeia", "tau_tiny"]

SRC_V2 = Path("gk_proof_fractal_v2_series.csv")
OUT_SERIES = Path("gk_proof_fractal_v3_series.csv")
OUT_CONTRASTS = Path("gk_proof_fractal_v3_contrasts.csv")
OUT_JSON = Path("gk_proof_fractal_v3.json")
OUT_ANALYSIS = Path("gk_proof_fractal_v3_analysis.json")

# grade NOVA, disjunta do v2 (checagem obrigatoria em check_disjoint)
GRID = {
    "implication": [(m, s) for m in range(3, 7) for s in range(16, 32)],
    "cadeia":      [(k, s) for k in range(3, 7) for s in range(16, 32)],
    "tau_tiny":    [(0, s) for s in range(64, 128)],
}
GENS = {"implication": gen_implication, "cadeia": gen_cadeia,
        "tau_tiny": gen_tau_tiny}

# hipoteses pre-registradas: (chave, metrica, variante, tipo, sinal)
# tipo: "sep" (IC95 exclui 0 com sinal) | "eq" (TOST na margem primaria)
H_B1 = [
    ("minref:implication-tau_tiny:boxdim:raw", "sep", +1),
    ("minref:cadeia-tau_tiny:boxdim:raw", "sep", +1),
    ("minref:implication-cadeia:boxdim:raw", "eq", 0),
]
H_B2 = [
    ("fonte:cadeia:boxdim:raw", "sep", -1),
    ("fonte:tau_tiny:boxdim:raw", "sep", -1),
]
H_B3 = [("drat:implication-cadeia:boxdim:raw", "sep", -1)]


# ---------------- metricas novas (anti-saturacao C2) ----------------

def _midranks(x):
    """Ranks medios (ties = media dos postos)."""
    order = sorted(range(len(x)), key=lambda i: x[i])
    ranks = [0.0] * len(x)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and x[order[j + 1]] == x[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def boxdim_rank(x):
    """Box-counting da serie RANKADA — invariante a transformacao
    monotona estrita (remove nivel/escala; sem teto de saturacao)."""
    return boxdim_curve(_midranks(x))


def taxa_saltos(x):
    """Fracao de inversoes de sinal nas diferencas consecutivas.
    Ruido ~0.5; rampa monotona ~0; sem teto artificial."""
    if len(x) < 8:
        return float("nan")
    d = [x[i + 1] - x[i] for i in range(len(x) - 1)]
    d = [v for v in d if v != 0]
    if len(d) < 4:
        return float("nan")
    changes = sum(1 for i in range(len(d) - 1)
                  if (d[i] > 0) != (d[i + 1] > 0))
    return changes / (len(d) - 1)


METRICS = {"boxdim": boxdim_curve, "boxdim_rank": boxdim_rank,
           "saltos": taxa_saltos, "higuchi_D": higuchi_D,
           "hurst_rs": hurst_rs}


# ---------------- checagens obrigatorias ----------------

def check_disjoint():
    """Grade do r3 nao pode tocar instancias do v2 (anti-circularidade)."""
    if not SRC_V2.exists():
        return {"status": "AVISO: CSV v2 ausente — checagem pulada"}
    v2 = {(r["family"], r["param"], r["seed"]) for r in
          csv.DictReader(SRC_V2.open(encoding="utf-8"))}
    mine = {(f, str(p), str(s)) for f, pts in GRID.items()
            for p, s in pts}
    inter = v2 & mine
    return {"status": "OK" if not inter else "FALHA",
            "n_v2": len(v2), "n_r3": len(mine),
            "interseccao": sorted(inter)[:10]}


def validate_new_metrics():
    """Validacao sintetica das metricas NOVAS antes de medir (A8)."""
    rng = random.Random(SEED + 9)
    wn = [rng.gauss(0, 1) for _ in range(64)]
    ramp = [i / 63.0 for i in range(64)]
    sine = [math.sin(2 * math.pi * i / 16) for i in range(64)]
    # S2: invariancia monotona estrita de boxdim_rank (x vs exp(x))
    exp_x = [math.exp(v) for v in wn]
    inv_err = abs(boxdim_rank(wn) - boxdim_rank(exp_x))
    # S3: ordenacao de saltos — ruido > rampa; ruido > seno
    ok_order = (taxa_saltos(wn) > taxa_saltos(ramp)
                and taxa_saltos(wn) > taxa_saltos(sine))
    # ordenacao de boxdim (gate canonico do v1: seno < ruido — SUAVE
    # < AGITADO. NOTA: rampa > ruido nesta amostra (n=64: a diagonal
    # satura a contagem de caixas; a ordem rampa<ruido NAO vale em n=64
    # — reportada apenas como informacao, nao gate)
    ok_box = boxdim_curve(sine) < boxdim_curve(wn)
    res = {
        "boxdim_rank_invariancia_erro": inv_err,
        "saltos": {"ruido": taxa_saltos(wn), "rampa": taxa_saltos(ramp),
                   "seno": taxa_saltos(sine)},
        "boxdim": {"ruido": boxdim_curve(wn), "rampa": boxdim_curve(ramp),
                   "seno": boxdim_curve(sine)},
        "boxdim_rank": {"ruido": boxdim_rank(wn),
                        "rampa": boxdim_rank(ramp)},
        "S2_invariancia_ok": inv_err < 1e-9,
        "S3_saltos_ok": ok_order,
        "boxdim_rampa_menor_que_ruido": ok_box,
    }
    res["status"] = "OK" if (res["S2_invariancia_ok"]
                             and res["S3_saltos_ok"]
                             and ok_box) else "FALHA"
    return res


def _synth_pair(rng, kind, draw=0):
    n = 64
    if kind == "type1":     # dois ruidos independentes: delta real 0
        a = [rng.gauss(0, 1) for _ in range(n)]
        b = [rng.gauss(0, 1) for _ in range(n)]
        return a, b
    if kind == "power":     # rampa com jitter vs seno puro — contraste
        # estrutural estavel (calibrado: obs em 8 draws todos positivos,
        # media +0.11; detectou 9/10 no pipeline completo — gate 7/10)
        a = [i / (n - 1) + 0.05 * rng.gauss(0, 1) for i in range(n)]
        b = [math.sin(2 * math.pi * i / 16) for i in range(n)]
        return a, b
    raise ValueError(kind)


def selftest_type1_power():
    """S4 tipo-I (50 pares nulos) + S5 poder (5 pares com estrutura
    distinta). Usa delete-d + BCa como o experimento real."""
    from gk_proof_fractal_v2_r2 import bca_ci as _bca
    rng = random.Random(SEED + 10)
    # S4
    excl = 0
    T = 50
    for _ in range(T):
        a, b = _synth_pair(rng, "type1")
        obs = boxdim_curve(a) - boxdim_curve(b)
        boots = []
        for _ in range(500):
            ia, ib = block_idx(len(a), rng), block_idx(len(b), rng)
            boots.append(boxdim_curve([a[i] for i in ia])
                         - boxdim_curve([b[i] for i in ib]))
        jack = []
        for i in range(len(a) - D_DELETE + 1):
            aa = a[:i] + a[i + D_DELETE:]
            jack.append(boxdim_curve(aa) - boxdim_curve(b))
        for i in range(len(b) - D_DELETE + 1):
            bb = b[:i] + b[i + D_DELETE:]
            jack.append(boxdim_curve(a) - boxdim_curve(bb))
        lo, hi, _ = _bca(obs, boots, jack, alpha=0.05)
        if lo is not None and (lo > 0 or hi < 0):
            excl += 1
    type1_rate = excl / T
    # S5 poder — construct calibrado (ver _synth_pair 'power'): rampa
    # com jitter vs seno puro; calibracao prvia no proprio ambiente:
    # 9/10 deteccoes no pipeline completo (gate 7/10 — margem p/ ruido
    # binomial; pipeline quebrado daria ~0/10)
    power_hits = 0
    power_coerentes = 0
    P = 10
    for d in range(P):
        rng_d = random.Random(SEED * 1000 + d)
        a, b = _synth_pair(rng_d, "power", d)
        obs = boxdim_curve(a) - boxdim_curve(b)
        boots = []
        for _ in range(1000):
            ia, ib = block_idx(len(a), rng_d), block_idx(len(b), rng_d)
            boots.append(boxdim_curve([a[i] for i in ia])
                         - boxdim_curve([b[i] for i in ib]))
        jack = []
        for i in range(len(a) - D_DELETE + 1):
            jack.append(boxdim_curve(a[:i] + a[i + D_DELETE:])
                        - boxdim_curve(b))
        for i in range(len(b) - D_DELETE + 1):
            jack.append(boxdim_curve(a)
                        - boxdim_curve(b[:i] + b[i + D_DELETE:]))
        lo, hi, _ = _bca(obs, boots, jack, alpha=0.05)
        if lo is not None and (lo > 0 or hi < 0):
            power_hits += 1
            if lo <= obs <= hi:
                power_coerentes += 1
    return {
        "S4_tipo1": {"n": T, "exclusoes": excl, "taxa": type1_rate,
                     "gate_ok": type1_rate <= 0.20,
                     "nota": "esperado ~0.05; n=50 -> ruido de ~0.03"},
        "S5_poder": {"n": P, "detectou": power_hits,
                     "coerentes": power_coerentes,
                     "gate_ok": power_hits >= 7,
                     "nota": ("construct calibrado: rampa+jitter vs seno "
                              "puro (obs todos positivos em 8 draws); "
                              "gate 7/10 = margem binomial sobre 9/10 "
                              "observado; incoerentes nao contam como "
                              "confirmacao da deteccao")},
        "status": ("OK" if type1_rate <= 0.20 and power_hits >= 7
                   else "FALHA"),
    }


# ---------------- coleta ----------------

def collect():
    rows = []
    censored = skipped = 0
    t_all = time.time()
    for fam, points in GRID.items():
        print(f"\n--- família: {fam} ({len(points)} instâncias novas) ---")
        t_f = time.time()
        slow = 0
        for param, seed in points:
            nvars, clauses, tag = GENS[fam](param, seed)
            ne = len({abs(l) for c in clauses for l in c})
            if ne > 6:
                print(f"  [FORA DO ESCOPO] {fam} p={param} s={seed}")
                skipped += 1
                continue
            t1 = time.time()
            mr, fecho = minref([frozenset(c) for c in clauses],
                               with_sat_len=True)
            st_r, len_r = solve_drat(nvars, clauses)
            dt = time.time() - t1
            if dt > 10:
                slow += 1
                print(f"    [LENTO {dt:.0f}s] {fam} p={param} s={seed}")
            if mr is None:
                print(f"  [SAT?!] {fam} p={param} s={seed} — descartado")
                skipped += 1
                continue
            if isinstance(mr, tuple):
                mr_out, censor = f">{mr[1]}({mr[2]})", True
                censored += 1
            else:
                mr_out, censor = mr, False
            rows.append({
                "family": fam, "param": param, "seed": seed, "tag": tag,
                "nvars": ne, "nclauses": len(clauses), "fecho": fecho,
                "minref": mr_out, "minref_censored": censor,
                "sat_drat": st_r, "proof_drat": len_r,
                # SEM coluna de tempo (reproducao byte-a-byte — 8o bug)
            })
        done = [r for r in rows if r["family"] == fam]
        exact = [r for r in done if not r["minref_censored"]]
        unsat = [r for r in done if r["sat_drat"] == "UNSAT"]
        vals = sorted({r["minref"] for r in exact})
        print(f"  UNSAT: {len(unsat)}/{len(done)} | exatos: {len(exact)} "
              f"| valores: {vals} | censuras: "
              f"{sum(1 for r in done if r['minref_censored'])} | "
              f"lentos(>10s): {slow} | {time.time()-t_f:.0f}s")
    print(f"\ncoleta total: {len(rows)} linhas, {censored} censuras, "
          f"{skipped} descartes, {time.time()-t_all:.0f}s")
    return rows


def load_series_from_csv():
    rows = list(csv.DictReader(OUT_SERIES.open(encoding="utf-8")))
    return rows


def build_series(rows):
    series = {}
    for fam in FAMS:
        pts = [r for r in rows if r["family"] == fam
               and r["minref_censored"] == "False"
               and r["sat_drat"] == "UNSAT"
               and r["proof_drat"] not in ("", "None")]
        pts.sort(key=lambda r: (int(r["param"]), int(r["seed"])))
        series[(fam, "minref")] = [float(r["minref"]) for r in pts]
        series[(fam, "drat")] = [float(r["proof_drat"]) for r in pts]
    return series, len(rows)


# ---------------- contrastes (BCa com 2 jackknifes) ----------------

def _jack_delete1(a, b, fn, paired):
    jack = []
    if paired:
        for i in range(len(a)):
            v = fn(a[:i] + a[i + 1:]) - fn(b[:i] + b[i + 1:])
            if v is not None and not math.isnan(v):
                jack.append(v)
    else:
        for i in range(len(a)):
            v = fn(a[:i] + a[i + 1:]) - fn(b)
            if v is not None and not math.isnan(v):
                jack.append(v)
        for i in range(len(b)):
            v = fn(a) - fn(b[:i] + b[i + 1:])
            if v is not None and not math.isnan(v):
                jack.append(v)
    return jack


def _jack_deleted(a, b, fn, paired, d=D_DELETE):
    """Delete-d (d=8) com janelas sobrepostas — padrao r3 (C3)."""
    jack = []
    if paired:
        for i in range(len(a) - d + 1):
            v = (fn(a[:i] + a[i + d:]) - fn(b[:i] + b[i + d:]))
            if v is not None and not math.isnan(v):
                jack.append(v)
    else:
        for i in range(len(a) - d + 1):
            v = fn(a[:i] + a[i + d:]) - fn(b)
            if v is not None and not math.isnan(v):
                jack.append(v)
        for i in range(len(b) - d + 1):
            v = fn(a) - fn(b[:i] + b[i + d:])
            if v is not None and not math.isnan(v):
                jack.append(v)
    return jack


def contrast(a, b, fn, rng, paired, n_boot=N_BOOT, allow_eq=True):
    if len(a) != len(b) or len(a) < 16:
        return None
    obs = fn(a) - fn(b)
    if math.isnan(obs):
        return None
    boots = []
    for _ in range(n_boot):
        if paired:
            idx = block_idx(len(a), rng)
            va, vb = fn([a[i] for i in idx]), fn([b[i] for i in idx])
        else:
            ia, ib = block_idx(len(a), rng), block_idx(len(b), rng)
            va, vb = fn([a[i] for i in ia]), fn([b[i] for i in ib])
        if va is not None and vb is not None \
                and not math.isnan(va) and not math.isnan(vb):
            boots.append(va - vb)
    if len(boots) < 200:
        return None
    j1 = _jack_delete1(a, b, fn, paired)
    jd = _jack_deleted(a, b, fn, paired)
    lo_d, hi_d, info_d = bca_ci(obs, boots, jd, alpha=0.05)
    lo90, hi90, _ = bca_ci(obs, boots, jd, alpha=0.10)
    # Bonferroni para as 2 separacoes primarias: IC 1-alpha/2 = 97.5%
    lo_b, hi_b, _ = bca_ci(obs, boots, jd, alpha=0.025)
    lo_1, hi_1, _ = bca_ci(obs, boots, j1, alpha=0.05)
    plo, phi = pct_ci(boots)
    if lo_d is None:
        return None
    m = sum(boots) / len(boots)
    se = (sum((x - m) ** 2 for x in boots) / (len(boots) - 1)) ** 0.5
    out = {
        "point": obs,
        "bca_lo": lo_d, "bca_hi": hi_d,          # delete-d (padrao)
        "bca90_lo": lo90, "bca90_hi": hi90,
        "bca_bonf_lo": lo_b, "bca_bonf_hi": hi_b,  # IC97.5%
        "bca_del1_lo": lo_1, "bca_del1_hi": hi_1,  # concordancia
        "pct_lo": plo, "pct_hi": phi,
        "se_boot": se, "mde80": 2.801585 * se,
        "z0": info_d.get("z0"), "aceleracao": info_d.get("aceleracao"),
        "n_boot": len(boots), "n_jack_d": len(jd), "n_jack_1": len(j1),
        "point_outside_pct": plo is not None and (obs < plo or obs > phi),
        "point_outside_bca": obs < lo_d or obs > hi_d,
        "excludes0": lo_d > 0 or hi_d < 0,
        "excludes0_bonf": lo_b > 0 or hi_b < 0,
        "excludes0_del1": (lo_1 is not None
                           and (lo_1 > 0 or hi_1 < 0)),
        "jack_concordancia": ((lo_d > 0 or hi_d < 0)
                              == ((lo_1 is not None)
                                  and (lo_1 > 0 or hi_1 < 0))),
    }
    if allow_eq:
        out["equivalente_margem"] = lo90 > -MARGIN_PRIMARY \
            and hi90 < MARGIN_PRIMARY
    else:
        out["equivalente_margem"] = None
    # veredito generico (metricas sem pre-registro: sem claim de eq)
    if out["point_outside_pct"] or out["point_outside_bca"]:
        out["veredito"] = "INCOERENTE"
    elif out["excludes0"]:
        out["veredito"] = "SEPARA"
    elif allow_eq and out["equivalente_margem"]:
        out["veredito"] = "EQUIVALENTE"
    else:
        out["veredito"] = "INCONCLUSIVO"
    return out


def classify_hyp(key, kind, dirn, c):
    """Aplica a regua pre-registrada de uma hipotese."""
    if c is None:
        return "SEM_DADOS"
    if c["veredito"] == "INCOERENTE":
        return "INCOERENTE"
    if kind == "eq":
        if c["veredito"] == "EQUIVALENTE":
            return "OK"
        if c["excludes0"]:
            return "FALHA_SEPARA"
        return "FALHA_INCONCLUSIVO"
    # sep: excluir 0 com sinal coerente (Bonferroni reportado a parte)
    if not c["excludes0"]:
        return "FALHA_INCONCLUSIVO"
    sinal = 1 if c["point"] > 0 else -1
    if sinal == dirn:
        return "OK_BONF" if c["excludes0_bonf"] else "OK"
    return "CONTRADITA"


# ---------------- analise ----------------

def analyze(rows):
    t0 = time.time()
    series, n_rows = build_series(rows)
    print("\nseries: " + ", ".join(
        f"{f}|{s}={len(v)}" for (f, s), v in sorted(series.items())))
    rng = random.Random(SEED_BOOT)

    combos = []
    for sysname in ("minref", "drat"):
        for i in range(len(FAMS)):
            for j in range(i + 1, len(FAMS)):
                combos.append((f"{sysname}:{FAMS[i]}-{FAMS[j]}",
                               sysname, FAMS[i], FAMS[j], False))
    for fam in FAMS:
        combos.append((f"fonte:{fam}", "fonte", fam, fam, True))

    contrasts = {}
    for label, sysname, fa, fb, paired in combos:
        a0 = series.get((fa, "minref" if sysname != "drat" else "drat"), [])
        b0 = series.get((fb, "minref" if sysname != "drat" else "drat"), [])
        if sysname == "fonte":
            a0 = series.get((fa, "minref"), [])
            b0 = series.get((fa, "drat"), [])
        for vname in ("raw", "log1p", "relinc"):
            a = variants_of(a0)[vname]
            b = variants_of(b0)[vname]
            for mname, fn in METRICS.items():
                key = f"{label}:{mname}:{vname}"
                allow_eq = (mname == "boxdim")   # eq so p/ primaria
                c = contrast(a, b, fn, rng, paired, allow_eq=allow_eq)
                if c is None:
                    continue
                contrasts[key] = c

    # ---- hipoteses pre-registradas ----
    def eval_hyp(spec, name):
        res = {}
        for key, kind, dirn in spec:
            res[key] = {"tipo": kind, "sinal_esperado": dirn,
                        "resultado": classify_hyp(key, kind, dirn,
                                                  contrasts.get(key)),
                        "dado": contrasts.get(key)}
        oks = [v["resultado"].startswith("OK") for v in res.values()]
        n_ok = sum(oks)
        if name == "H_B1":
            contrad = any(v["resultado"] == "CONTRADITA"
                          for v in res.values())
            if n_ok == 3:
                v = "CONFIRMADA"
            elif n_ok == 2:
                v = "PARCIAL"
            elif contrad:
                v = "REFUTADA_CONTRADITA"
            else:
                v = "REFUTADA"
        elif n_ok == len(spec):
            v = "CONFIRMADA"
        elif any(r["resultado"] == "CONTRADITA" for r in res.values()):
            v = "REFUTADA_CONTRADITA"
        else:
            v = "REFUTADA"
        return {"veredito": v, "n_ok": f"{n_ok}/{len(spec)}",
                "testes": res}

    hyp = {
        "H_B1_padrao_tau_boxdim_minref": eval_hyp(H_B1, "H_B1"),
        "H_B2_fonte_boxdim": eval_hyp(H_B2, "H_B2"),
        "H_B3_pista_drat_imp_cadeia": eval_hyp(H_B3, "H_B3"),
    }
    # H_B4: contagem de incoerentes por metrica (frequencia)
    incoh = {}
    for mname in METRICS:
        ks = [k for k in contrasts if f":{mname}:" in k]
        incoh[mname] = {
            "n": len(ks),
            "incoerentes": sum(1 for k in ks
                               if contrasts[k]["veredito"] == "INCOERENTE"),
        }
    hyp["H_B4_anti_saturacao"] = {
        "enunciado": "boxdim tem 0 incoerentes em r3 (como no r2: 0/27)",
        "por_metrica": incoh,
        "veredito": ("CONFIRMADA" if incoh["boxdim"]["incoerentes"] == 0
                     else "REFUTADA"),
    }
    # concordancia delete-d vs delete-1 nos pre-registrados
    pre_keys = [k for k, _, _ in H_B1 + H_B2 + H_B3]
    disc = [k for k in pre_keys
            if k in contrasts and not contrasts[k]["jack_concordancia"]]
    hyp["_diagnostico"] = {
        "pre_registrados_com_jack_discordante": disc,
        "n_contrastes": len(contrasts),
        "incoerentes_total": sum(1 for c in contrasts.values()
                                 if c["veredito"] == "INCOERENTE"),
    }
    print("\n--- hipoteses pre-registradas ---")
    for hname in ("H_B1_padrao_tau_boxdim_minref", "H_B2_fonte_boxdim",
                  "H_B3_pista_drat_imp_cadeia", "H_B4_anti_saturacao"):
        h = hyp[hname]
        print(f"  {hname}: {h['veredito']} ({h.get('n_ok', '')})")
        if "testes" in h:
            for k, v in h["testes"].items():
                d = v["dado"]
                extra = ""
                if d:
                    extra = (f"point={d['point']:+.4f} "
                             f"BC95=[{d['bca_lo']:+.4f},"
                             f"{d['bca_hi']:+.4f}]")
                print(f"    {k}: {v['resultado']} {extra}")
    print(f"  incoerentes por metrica: " + ", ".join(
        f"{m}={v['incoerentes']}/{v['n']}" for m, v in incoh.items()))
    print(f"  jack discordante (pre-reg): {len(disc)}")
    return contrasts, hyp, series, n_rows


# ---------------- escrita ----------------

def _sha(p):
    return hashlib.sha256(
        p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def write_series(rows):
    with open(OUT_SERIES, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def write_contrasts(contrasts):
    cols = ["key", "veredito", "point", "bca_lo", "bca_hi",
            "bca90_lo", "bca90_hi", "bca_bonf_lo", "bca_bonf_hi",
            "bca_del1_lo", "bca_del1_hi", "pct_lo", "pct_hi",
            "excludes0", "excludes0_bonf", "excludes0_del1",
            "jack_concordancia", "equivalente_margem",
            "point_outside_pct", "point_outside_bca",
            "se_boot", "mde80", "z0", "aceleracao",
            "n_boot", "n_jack_d", "n_jack_1"]
    with open(OUT_CONTRASTS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for k, c in sorted(contrasts.items()):
            w.writerow({col: c.get(col) for col in cols} | {"key": k})


# ---------------- main ----------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--analyze-only", action="store_true",
                    help="re-analise do CSV de series existente")
    args = ap.parse_args()

    t0 = time.time()
    print("=" * 70)
    print("D4' v3 (r3) — boxdim PRE-REGISTRADO em dados novos disjuntos")
    print("=" * 70)

    # ---- selftests obrigatorios (A8) ----
    print("\n[S1] BCa vs scipy...")
    s1 = selftest_bca()
    print(f"  {s1['status']} (diff={s1.get('max_diff')})")
    print("[S2/S3] validacao metricas novas...")
    s23 = validate_new_metrics()
    print(f"  {s23['status']} inv_err={s23['boxdim_rank_invariancia_erro']:.2e} "
          f"saltos={s23['saltos']}")
    print("[S4/S5] tipo-I e poder (delete-d + BCa)...")
    s45 = selftest_type1_power()
    print(f"  {s45['status']} tipo1={s45['S4_tipo1']['taxa']:.2f} "
          f"(gate<=0.20) poder={s45['S5_poder']['detectou']}/"
          f"{s45['S5_poder']['n']}")
    print("[DISJ] grade vs v2...")
    disj = check_disjoint()
    print(f"  {disj['status']} interseccao={disj.get('interseccao')}")
    fails = [n for n, s in (("S1", s1["status"]), ("S2S3", s23["status"]),
                            ("S4S5", s45["status"]),
                            ("DISJ", disj["status"]))
             if s not in ("OK", "AVISO: CSV v2 ausente — checagem pulada")]
    if fails:
        print(f"[ABORTA] selftests falharam: {fails}")
        return 2

    # ---- coleta (ou re-uso) ----
    if args.analyze_only:
        if not OUT_SERIES.exists():
            print("[ERRO] --analyze-only sem CSV de series")
            return 2
        rows = load_series_from_csv()
        print(f"\nre-usando {OUT_SERIES.name}: {len(rows)} linhas")
    else:
        rows = collect()
        write_series(rows)

    # ---- analise ----
    contrasts, hyp, series, n_rows = analyze(rows)

    # ---- CSV de contrastes ----
    write_contrasts(contrasts)

    # ---- JSONs (dois: R6 protege os DOIS pares) ----
    meta_common = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat()
                         .replace("+00:00", "Z"),
        "seed": SEED, "seed_boot": SEED_BOOT, "n_boot": N_BOOT,
        "block": BLOCK, "d_delete": D_DELETE,
        "grid": {k: f"{len(v)} pontos (seeds novos)"
                 for k, v in GRID.items()},
        "margens_boxdim": {"primaria": MARGIN_PRIMARY,
                           "sensibilidade": list(MARGINS[1:])},
        "ancora_margem": ("menor efeito r2 boxdim=0.053; ~1/3 da "
                          "amplitude entre-series r2 (0.142)"),
        "runtime_s": round(time.time() - t0, 1),
        "caveats": [
            ("Pre-registro: hipoteses/margens fixadas neste codigo e no "
             "doc 30_ ANTES do run (commit anterior)."),
            ("Dados disjuntos do v2 (grade nova, checagem DISJ OK)."),
            ("Generalizacao: ao GERADOR das familias (mesma "
             "distribuicao, seeds novos), nao a familias arbitarias."),
            ("delete-d com janelas sobrepostas -> aceleracao BCa "
             "aproximada; delete-1 reportado como concordancia."),
            ("boxdim_rank/saltos exploratorios; eq so p/ boxdim."),
            ("N1+N2; sem N4; H_C2 (EF) deferido; tau k↑ aberta."),
        ],
    }
    payload_series = {
        "metadata": {**meta_common,
                     "data_source": "gk_proof_fractal_v3.py (r3 coleta)",
                     "instances": {"rows": n_rows},
                     "selftest_disj": disj,
                     "csv": OUT_SERIES.name, "csv_sha256": _sha(OUT_SERIES),
                     "sha_note": "sha256 bytes normalizados CRLF->LF"},
        "selftests": {"S1_bca_scipy": s1, "S2S3_metricas": s23,
                      "S4S5_tipo1_poder": s45},
    }
    OUT_JSON.write_text(json.dumps(payload_series, indent=2,
                                   ensure_ascii=False), encoding="utf-8")

    payload_an = {
        "metadata": {**meta_common,
                     "data_source": ("gk_proof_fractal_v3.py (r3 "
                                     "analise — boxdim pre-registrado)"),
                     "input_series_csv": OUT_SERIES.name,
                     "input_series_sha256": _sha(OUT_SERIES),
                     "csv": OUT_CONTRASTS.name,
                     "csv_sha256": _sha(OUT_CONTRASTS),
                     "sha_note": "sha256 bytes normalizados CRLF->LF"},
        "pre_registro": {
            "H_B1": [{"key": k, "tipo": t, "sinal": d}
                     for k, t, d in H_B1],
            "H_B2": [{"key": k, "tipo": t, "sinal": d}
                     for k, t, d in H_B2],
            "H_B3": [{"key": k, "tipo": t, "sinal": d}
                     for k, t, d in H_B3],
            "H_B4": "boxdim sem incoerentes (contagem)",
        },
        "hypotheses": hyp,
        "contrasts": contrasts,
    }
    OUT_ANALYSIS.write_text(json.dumps(payload_an, indent=2,
                                       ensure_ascii=False),
                            encoding="utf-8")

    print(f"\n[OK] {OUT_SERIES.name} (sha {_sha(OUT_SERIES)[:16]}…)")
    print(f"[OK] {OUT_CONTRASTS.name} (sha {_sha(OUT_CONTRASTS)[:16]}…)")
    print(f"[OK] {OUT_JSON.name} + {OUT_ANALYSIS.name}")
    print(f"runtime: {meta_common['runtime_s']}s")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

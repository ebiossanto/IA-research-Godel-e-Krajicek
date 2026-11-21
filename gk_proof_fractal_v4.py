#!/usr/bin/env python3
"""
gk_proof_fractal_v4.py — D4' v4 (rodada r4): n=384, margem por precisao,
diagnostico de z0, saltos confirmatorio.

=====================================================================
PRE-REGISTRO (fixado ANTES de qualquer execucao com dados novos; o
commit deste codigo e do doc 31_ precede o run — prioridade temporal
C1): ver 31_PONTE_PROVA_FRACTAL_D4V4.md s1.
=====================================================================

PENDENCIAS DO r3 ATENDIDAS AQUI:
  A1 margem ancorada TAMBEM em precisao:  primarya 0.08 = maior
     meia-largura IC90 dos pre-registrados do r3 (0.0805 em H_B3;
     demais 0.061-0.073) — efeitos abaixo do limite de resolucao do r3
     sao certificaveis como negligiveis. Sensibilidade 0.06/0.10.
  A3 veredito global EXAUSTIVO pre-definido (ver REGRAS abaixo) —
     inclui o caso INCOERENTE (r3 teve lacuna).
  A4 IC primario DECLARADO: BCa delete-d = primario; percentil =
     robustez (flag de discordancia reportada).
  A5 diagnostico de z0 extremo: H_C3 (bias por serie, bias_over_se,
     z0, empates, degenerados, discordancia) + saltos confirmatorio
     (H_C2). Raiz caracterizada na calibracao: block-resample destroi
     macroestruturas ASSIMETRICAS entre series (par com tendencia ->
     z0=3.29, IC degenerado); pares ESTACIONARIOS (estrutura local
     preservada) tem z0 saudavel (calib: zigzag-vs-branco z0 in
     [-0.52,+0.54]).
  A6 incoerentes simetricos (regra mantida).
  s6.1 n MAIOR: 384 por familia (r2:64, r3:64) -> alvo MDE80<0.06
     (H_C4) — previsao por escala sqrt(64/384): MDE 0.047-0.058 nos 6
     testes boxdim pre-registrados.

DADOS NOVOS E DISJUNTOS de r2 E r3 (mesmos geradores, seeds nunca
usados; checagem obrigatoria contra OS DOIS CSVs -> aborta se
intersectar):
  implication : m=3..6 x seeds 32..127   (r2:0..15, r3:16..31) = 384
  cadeia      : k=3..6 x seeds 32..127   (r2:0..15, r3:16..31) = 384
  tau_tiny    : seeds 128..511           (r2:0..63, r3:64..127) = 384

HIPOTESES (declaradas aqui, ANTES do run):
  H_C1 — PRIMARIA (boxdim, raw; 6 testes; mesmas chaves do r3):
    (a) minref:implication-tau_tiny      > 0  (r3:+0.0595 OK; r2:+0.053) d+1
    (b) minref:cadeia-tau_tiny           > 0  (r3:+0.0731 OK_BONF; r2:+0.058) d+1
    (c) minref:implication-cadeia  EQUIVALENTE em +/-0.08
        (r3: nao separa, eq@0.08 ok; BC90 r3=[-0.078,+0.053])
    (d) drat:implication-cadeia          < 0  (r3:-0.170 OK_BONF; r2:-0.102) d-1
        [pista A4]
    (e) fonte:tau_tiny                   < 0  (r3:-0.102 OK; r2:-0.112) d-1
    (f) fonte:cadeia                     < 0  (r3:-0.152 INCOERENTE; r2:-0.084) d-1
    Multiplicidade: 5 direcionais com Bonferroni alpha*=0.05/5=0.01
    (IC99% reportado); (c) TOST com alpha proprio 0.05 (IC90).
  H_C2 — SECUNDARIA (saltos, raw; 3 testes direcionais; ancoras r3):
    (a) minref:implication-tau_tiny > 0  (r3:+0.173 SEPARA)            d+1
    (b) drat:implication-cadeia     > 0  (r3:+0.110 SEPARA)            d+1
    (c) fonte:cadeia                > 0  (r3:+0.120 SEPARA)            d+1
    Bonferroni alpha*=0.05/3 (IC98.33% reportado).
  H_C3 — DIAGNOSTICO z0 (caracterizacao; D2 e claim):
    D1: contingencia |z0|>1.5 x |bias_over_se|>1.2 (taxa de coincidencia)
    D2: CLAIM — todo IC degenerado (lo==hi) tem |z0|>2.5
        (r3: unico degenerado z0=-2.75; calib n=256: z0=3.29 degenerado)
    D3: taxa de discordancia exclusao pct-vs-BCa: grupo |z0|>1.5 vs
        grupo <=1.5 (espera: muito maior no grupo extremo)
    D4: mediana |z0| em fonte:* vs pares de familia (espera: fonte
        maior — macroestruturas de fonte diferentes nao cancelam viés)
  H_C4 — ALVO DE DESIGN: MDE80 < 0.06 em TODOS os 6 testes boxdim
    pre-registrados (contagem reportada; falha de alvo, nao de hipotese).

REGRAS DE VEREDITO (exaustivas — A3; fixadas ANTES do run):
  Por teste: OK (IC95 BCa exclui 0, sinal coerente; "OK_BONF" se o IC
    Bonferroni do seu grupo tambem exclui) | FALHA_INCONCLUSIVO |
    CONTRADITA (exclui 0 com sinal OPOSTO — so direcionais) |
    EQUIVALENTE (c: IC90 no intervalo) | FALHA_SEPARA (c: exclui 0) |
    INCOERENTE (ponto fora do IC pct ou BCa — NAO conta em nenhuma
    direcao) | SEM_DADOS.
  Global: qualquer CONTRADITA -> REFUTADA_CONTRADITA; C = contaveis
    (OK*/FALHA*); |C| < ceil(0.6*n) -> INDETERMINADO (muitos
    incoerentes/sem dados); todos C OK -> CONFIRMADA; nenhum OK ->
    REFUTADA; senao -> PARCIAL (n_ok/|C|, n_incoh reportado).

SELFTESTS OBRIGATORIOS ANTES DO RUN (aborta se falhar; A8):
  S1  BCa vs scipy (iid)                                   — r2
  S2  invariancia monotona de boxdim_rank (erro exato 0)    — n=384
  S3  ordenacao saltos (ruido>seno; ruido>rampa) + boxdim
      seno<ruido (gate canonico)                            — n=384
  S4  TIPO-I: 30 pares branco-vs-branco, B=500, BCa delete-d
      n=384 — gate taxa <= 0.20 (calib: 0/30)
  S5  PODER: zigzag-vs-branco (par ESTACIONARIO — calibrado
      n=384: 10/10 coerentes, z0 in [-0.52,+0.54]), B=1000,
      P=10 — gate: >= 7/10 DETECCOES COERENTES
  DISJ interseccao grade x (r2 U r3) = vazia

INFERENCIA: BCa delete-d (d=8) primario + delete-1 concordancia +
percentil robustez (flag discordancia); TOST IC90; MDE80=2.8016*SE;
regra de incoerencia; B=1000, seed_boot=SEED+5=20261124.

SAIDAS: gk_proof_fractal_v4_series.csv (coleta, SEM tempo)
        gk_proof_fractal_v4_contrasts.csv (135 contrastes + diagnostico)
        gk_proof_fractal_v4.json (coleta; R6 -> series)
        gk_proof_fractal_v4_analysis.json (analise; R6 -> contrasts)
Uso:   python -u gk_proof_fractal_v4.py [--selftest-only | --analyze-only]
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
from gk_proof_fractal_v2_r2 import bca_ci, block_idx, pct_ci, selftest_bca
from gk_proof_fractal_v3 import METRICS, boxdim_rank, taxa_saltos
from gk_minref import minref

N_BOOT = 1000
SEED_BOOT = SEED + 5          # 20261124 — declarado
D_DELETE = BLOCK              # delete-d d=8 (mesmo bloco do resample)
MARGIN_PRIMARY = 0.08         # A1: maior meia-largura IC90 do r3 (0.0805)
MARGINS = (0.08, 0.06, 0.10)  # primaria + sensibilidade
FAMS = ["implication", "cadeia", "tau_tiny"]
MDE_TARGET = 0.06             # H_C4

SRC_R2 = Path("gk_proof_fractal_v2_series.csv")
SRC_R3 = Path("gk_proof_fractal_v3_series.csv")
OUT_SERIES = Path("gk_proof_fractal_v4_series.csv")
OUT_CONTRASTS = Path("gk_proof_fractal_v4_contrasts.csv")
OUT_JSON = Path("gk_proof_fractal_v4.json")
OUT_ANALYSIS = Path("gk_proof_fractal_v4_analysis.json")

GRID = {
    "implication": [(m, s) for m in range(3, 7) for s in range(32, 128)],
    "cadeia":      [(k, s) for k in range(3, 7) for s in range(32, 128)],
    "tau_tiny":    [(0, s) for s in range(128, 512)],
}
GENS = {"implication": gen_implication, "cadeia": gen_cadeia,
        "tau_tiny": gen_tau_tiny}

# hipoteses pre-registradas: (chave, tipo, sinal)
H_C1 = [
    ("minref:implication-tau_tiny:boxdim:raw", "sep", +1),
    ("minref:cadeia-tau_tiny:boxdim:raw", "sep", +1),
    ("minref:implication-cadeia:boxdim:raw", "eq", 0),
    ("drat:implication-cadeia:boxdim:raw", "sep", -1),
    ("fonte:tau_tiny:boxdim:raw", "sep", -1),
    ("fonte:cadeia:boxdim:raw", "sep", -1),
]
H_C2 = [
    ("minref:implication-tau_tiny:saltos:raw", "sep", +1),
    ("drat:implication-cadeia:saltos:raw", "sep", +1),
    ("fonte:cadeia:saltos:raw", "sep", +1),
]
BONF_ALPHA = {"boxdim": 0.05 / 5,     # H_C1: 5 direcionais
              "saltos": 0.05 / 3}     # H_C2: 3 direcionais


# ---------------- checagens obrigatorias ----------------

def check_disjoint():
    """Grade r4 nao pode tocar instancias de r2 NEM r3."""
    used = set()
    n_prev = 0
    for src in (SRC_R2, SRC_R3):
        if not src.exists():
            continue
        for r in csv.DictReader(src.open(encoding="utf-8")):
            used.add((r["family"], r["param"], r["seed"]))
        n_prev += 1
    if n_prev == 0:
        return {"status": "AVISO: CSVs anteriores ausentes — pulado"}
    mine = {(f, str(p), str(s)) for f, pts in GRID.items()
            for p, s in pts}
    inter = used & mine
    return {"status": "OK" if not inter else "FALHA",
            "n_prev": len(used), "n_r4": len(mine),
            "fontes_checadas": n_prev,
            "interseccao": sorted(inter)[:10]}


def validate_metrics_n384():
    """S2/S3 em n=384 (regime do experimento)."""
    rng = random.Random(SEED + 9)
    wn = [rng.gauss(0, 1) for _ in range(384)]
    ramp = [i / 383.0 for i in range(384)]
    sine = [math.sin(2 * math.pi * i / 16) for i in range(384)]
    inv_err = abs(boxdim_rank(wn) - boxdim_rank([math.exp(v) for v in wn]))
    ok_saltos = (taxa_saltos(wn) > taxa_saltos(ramp)
                 and taxa_saltos(wn) > taxa_saltos(sine))
    ok_box = boxdim_curve(sine) < boxdim_curve(wn)
    res = {"status": "OK" if (inv_err < 1e-9 and ok_saltos and ok_box)
           else "FALHA",
           "S2_invariancia_erro": inv_err,
           "saltos": {"ruido": taxa_saltos(wn), "rampa": taxa_saltos(ramp),
                      "seno": taxa_saltos(sine)},
           "boxdim": {"ruido": boxdim_curve(wn),
                      "seno": boxdim_curve(sine)},
           "S3_saltos_ok": ok_saltos, "boxdim_seno_menor_ok": ok_box}
    return res


def _zigzag(n, rng):
    return [(1.0 if i % 2 == 0 else -1.0) + 0.05 * rng.gauss(0, 1)
            for i in range(n)]


def _white(n, rng):
    return [rng.gauss(0, 1) for _ in range(n)]


def _pair_null(rng, n):
    return _white(n, rng), _white(n, rng)


def _pair_power(rng, n):
    """Par ESTACIONARIO (calibrado n=384: 10/10 coerentes, z0 saudavel)."""
    return _zigzag(n, rng), _white(n, rng)


def _pipeline_test(a, b, rng, n_boot, d=D_DELETE):
    obs = boxdim_curve(a) - boxdim_curve(b)
    boots = []
    for _ in range(n_boot):
        ia, ib = block_idx(len(a), rng), block_idx(len(b), rng)
        boots.append(boxdim_curve([a[i] for i in ia])
                     - boxdim_curve([b[i] for i in ib]))
    jack = []
    for i in range(len(a) - d + 1):
        jack.append(boxdim_curve(a[:i] + a[i + d:]) - boxdim_curve(b))
    for i in range(len(b) - d + 1):
        jack.append(boxdim_curve(a) - boxdim_curve(b[:i] + b[i + d:]))
    lo, hi, info = bca_ci(obs, boots, jack, alpha=0.05)
    excl = lo is not None and (lo > 0 or hi < 0)
    coh = excl and lo <= obs <= hi
    return excl, coh, info.get("z0")


def selftests():
    out = {}
    out["S1_bca_scipy"] = selftest_bca()
    out["S2S3"] = validate_metrics_n384()
    # S4 tipo-I: 30 pares nulos, B=500
    rng = random.Random(SEED_BOOT)
    excl = 0
    T = 30
    for _ in range(T):
        a, b = _pair_null(rng, 384)
        e, _, _ = _pipeline_test(a, b, rng, 500)
        excl += e
    out["S4_tipo1"] = {"n": T, "exclusoes": excl, "taxa": excl / T,
                       "gate_ok": excl / T <= 0.20,
                       "nota": "calibracao previa 0/30"}
    # S5 poder: 10 pares zigzag-vs-branco, B=1000, gate coerente >= 7
    hits = coer = 0
    P = 10
    z0s = []
    for d in range(P):
        rng_d = random.Random(SEED_BOOT * 100 + d)
        a, b = _pair_power(rng_d, 384)
        e, c, z0 = _pipeline_test(a, b, rng_d, 1000)
        hits += e
        coer += c
        z0s.append(z0)
    out["S5_poder"] = {"n": P, "detectou": hits, "coerentes": coer,
                       "gate_ok": coer >= 7, "z0_range": [min(z0s),
                                                          max(z0s)],
                       "nota": ("construct estacionario zigzag-vs-branco "
                                "(calib n=384: 10/10 coerentes); gate "
                                ">=7/10 coerentes")}
    out["DISJ"] = check_disjoint()
    ok = (out["S1_bca_scipy"]["status"] == "OK"
          and out["S2S3"]["status"] == "OK"
          and out["S4_tipo1"]["gate_ok"] and out["S5_poder"]["gate_ok"]
          and out["DISJ"]["status"] in ("OK",
                                        "AVISO: CSVs anteriores ausentes — pulado"))
    out["status"] = "OK" if ok else "FALHA"
    return out


# ---------------- coleta ----------------

def collect():
    rows = []
    censored = skipped = 0
    t_all = time.time()
    for fam, points in GRID.items():
        print(f"\n--- família: {fam} ({len(points)} instâncias novas) ---",
              flush=True)
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
            if dt > 120:
                slow += 1
                print(f"    [LENTO {dt/60:.1f}min] {fam} p={param} "
                      f"s={seed}", flush=True)
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
                # SEM coluna de tempo (byte-reprodutivel — 8o bug)
            })
        done = [r for r in rows if r["family"] == fam]
        exact = [r for r in done if not r["minref_censored"]]
        unsat = [r for r in done if r["sat_drat"] == "UNSAT"]
        vals = sorted({r["minref"] for r in exact})
        print(f"  UNSAT: {len(unsat)}/{len(done)} | exatos: {len(exact)} "
              f"| valores: {vals} | censuras: "
              f"{sum(1 for r in done if r['minref_censored'])} | "
              f"lentos(>2min): {slow} | {time.time()-t_f:.0f}s",
              flush=True)
    print(f"\ncoleta total: {len(rows)} linhas, {censored} censuras, "
          f"{skipped} descartes, {(time.time()-t_all)/60:.1f}min")
    return rows


def load_series_from_csv():
    return list(csv.DictReader(OUT_SERIES.open(encoding="utf-8")))


def build_series(rows):
    series = {}
    for fam in FAMS:
        pts = [r for r in rows if r["family"] == fam
               and str(r["minref_censored"]) == "False"
               and r["sat_drat"] == "UNSAT"
               and str(r["proof_drat"]) not in ("", "None")]
        pts.sort(key=lambda r: (int(r["param"]), int(r["seed"])))
        series[(fam, "minref")] = [float(r["minref"]) for r in pts]
        series[(fam, "drat")] = [float(r["proof_drat"]) for r in pts]
    return series, len(rows)


# ---------------- contrastes com diagnostico de z0 ----------------

def _jack(a, b, fn, paired, d):
    jack = []
    if d == 1:
        if paired:
            for i in range(len(a)):
                v = (fn(a[:i] + a[i + 1:]) - fn(b[:i] + b[i + 1:]))
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
    else:
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


def contrast(a, b, fn, rng, paired, allow_eq=True, n_boot=N_BOOT):
    if len(a) != len(b) or len(a) < 16:
        return None
    obs_a, obs_b = fn(a), fn(b)
    obs = obs_a - obs_b
    if math.isnan(obs):
        return None
    boots, vas, vbs = [], [], []
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
            vas.append(va)
            vbs.append(vb)
    if len(boots) < 200:
        return None
    jd = _jack(a, b, fn, paired, D_DELETE)
    j1 = _jack(a, b, fn, paired, 1)
    lo, hi, info = bca_ci(obs, boots, jd, alpha=0.05)
    if lo is None:
        return None
    lo90, hi90, _ = bca_ci(obs, boots, jd, alpha=0.10)
    lo_b5, hi_b5, _ = bca_ci(obs, boots, jd, alpha=0.01)
    lo_b3, hi_b3, _ = bca_ci(obs, boots, jd, alpha=0.05 / 3)
    lo_1, hi_1, _ = bca_ci(obs, boots, j1, alpha=0.05)
    plo, phi = pct_ci(boots)
    m = sum(boots) / len(boots)
    se = (sum((x - m) ** 2 for x in boots) / (len(boots) - 1)) ** 0.5
    bias = m - obs
    bias_a = (sum(vas) / len(vas)) - obs_a
    bias_b = (sum(vbs) / len(vbs)) - obs_b
    uniq = len(set(round(v, 12) for v in boots))
    jbar = sum(jd) / len(jd)
    jack_std = (sum((x - jbar) ** 2 for x in jd)
                / max(1, len(jd) - 1)) ** 0.5
    out = {
        "point": obs,
        "bca_lo": lo, "bca_hi": hi,                 # PRIMARIO (A4)
        "bca90_lo": lo90, "bca90_hi": hi90,
        "bca_bonf5_lo": lo_b5, "bca_bonf5_hi": hi_b5,  # alpha=0.01 (H_C1)
        "bca_bonf3_lo": lo_b3, "bca_bonf3_hi": hi_b3,  # alpha=.0167 (H_C2)
        "bca_del1_lo": lo_1, "bca_del1_hi": hi_1,
        "pct_lo": plo, "pct_hi": phi,                 # ROBUSTEZ (A4)
        "se_boot": se, "mde80": 2.801585 * se,
        # --- diagnostico z0 (H_C3) ---
        "z0": info.get("z0"), "aceleracao": info.get("aceleracao"),
        "boot_bias": bias, "bias_over_se": bias / se if se else None,
        "bias_serie_a": bias_a, "bias_serie_b": bias_b,
        "n_unique_boots": uniq,
        "tie_fraction": 1 - uniq / len(boots),
        "jack_std": jack_std,
        "degenerate": lo == hi,
        "z0_extreme": abs(info.get("z0") or 0) > 1.5,
        # --- flags ---
        "excludes0": lo > 0 or hi < 0,
        "excludes0_pct": plo is not None and (plo > 0 or phi < 0),
        "excludes0_bonf5": lo_b5 > 0 or hi_b5 < 0,
        "excludes0_bonf3": lo_b3 > 0 or hi_b3 < 0,
        "excludes0_del1": lo_1 is not None and (lo_1 > 0 or hi_1 < 0),
        "discordancia_pct_bca": ((lo > 0 or hi < 0)
                                 != (plo is not None and (plo > 0
                                                          or phi < 0))),
        "jack_concordancia": ((lo > 0 or hi < 0)
                              == (lo_1 is not None
                                  and (lo_1 > 0 or hi_1 < 0))),
        "point_outside_pct": plo is not None and (obs < plo or obs > phi),
        "point_outside_bca": obs < lo or obs > hi,
        "n_boot": len(boots), "n_jack_d": len(jd), "n_jack_1": len(j1),
    }
    if allow_eq:
        out["equivalente_d0.08"] = lo90 > -0.08 and hi90 < 0.08
        out["equivalente_d0.06"] = lo90 > -0.06 and hi90 < 0.06
        out["equivalente_d0.10"] = lo90 > -0.10 and hi90 < 0.10
    else:
        out["equivalente_d0.08"] = out["equivalente_d0.06"] = \
            out["equivalente_d0.10"] = None
    # veredito generico (r3: incoerencia nao conta nem p/ nem contra)
    if out["point_outside_pct"] or out["point_outside_bca"]:
        out["veredito"] = "INCOERENTE"
    elif out["excludes0"]:
        out["veredito"] = "SEPARA"
    elif allow_eq and out["equivalente_d0.08"]:
        out["veredito"] = "EQUIVALENTE"
    else:
        out["veredito"] = "INCONCLUSIVO"
    return out


# ---------------- vereditos pre-registrados (REGRAS exaustivas) ----------------

def classify_test(c, kind, dirn, metric):
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
    # direcional
    if not c["excludes0"]:
        return "FALHA_INCONCLUSIVO"
    sinal = 1 if c["point"] > 0 else -1
    if sinal != dirn:
        return "CONTRADITA"
    bonf = (c["excludes0_bonf5"] if metric == "boxdim"
            else c["excludes0_bonf3"])
    return "OK_BONF" if bonf else "OK"


def classify_global(results):
    """REGRAS exaustivas (A3): ver docstring/topo do script."""
    n = len(results)
    vals = list(results.values())
    if any(v == "CONTRADITA" for v in vals):
        return "REFUTADA_CONTRADITA"
    countable = [v for v in vals if v.startswith("OK")
                 or v.startswith("FALHA")]
    n_ok = sum(1 for v in countable if v.startswith("OK"))
    n_incoh = sum(1 for v in vals if v == "INCOERENTE")
    n_sem = sum(1 for v in vals if v == "SEM_DADOS")
    if len(countable) < math.ceil(0.6 * n):
        return (f"INDETERMINADO ({len(countable)}/{n} contaveis; "
                f"{n_incoh} incoerentes, {n_sem} sem dados)")
    if n_ok == len(countable):
        return f"CONFIRMADA ({n_ok}/{n})"
    if n_ok == 0:
        return f"REFUTADA (0/{len(countable)} contaveis)"
    return (f"PARCIAL ({n_ok}/{len(countable)} contaveis; "
            f"{n_incoh} incoerentes)")


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
        if sysname == "fonte":
            a0, b0 = series.get((fa, "minref"), []), \
                series.get((fa, "drat"), [])
        else:
            src = "minref" if sysname == "minref" else "drat"
            a0, b0 = series.get((fa, src), []), series.get((fb, src), [])
        for vname in ("raw", "log1p", "relinc"):
            a = variants_of(a0)[vname]
            b = variants_of(b0)[vname]
            for mname, fn in METRICS.items():
                key = f"{label}:{mname}:{vname}"
                c = contrast(a, b, fn, rng, paired,
                             allow_eq=(mname == "boxdim"))
                if c is None:
                    continue
                contrasts[key] = c

    # ---- hipoteses ----
    def eval_hyp(spec, name):
        res = {}
        for key, kind, dirn in spec:
            metric = "boxdim" if ":boxdim:" in key else \
                ("saltos" if ":saltos:" in key else "outros")
            res[key] = {"tipo": kind, "sinal_esperado": dirn,
                        "resultado": classify_test(contrasts.get(key),
                                                   kind, dirn, metric),
                        "dado": contrasts.get(key)}
        results = {k: v["resultado"] for k, v in res.items()}
        return {"veredito": classify_global(results), "testes": res}

    hyp = {"H_C1_boxdim_primaria": eval_hyp(H_C1, "H_C1"),
           "H_C2_saltos_secundaria": eval_hyp(H_C2, "H_C2")}

    # ---- H_C3 diagnostico z0 ----
    allc = list(contrasts.items())
    ext = [(k, c) for k, c in allc if c["z0_extreme"]]
    norm = [(k, c) for k, c in allc if not c["z0_extreme"]]
    deg = [(k, c) for k, c in allc if c["degenerate"]]

    def med(vals):
        if not vals:
            return None
        s = sorted(vals)
        return s[len(s) // 2]

    d1_match = sum(1 for _, c in allc
                   if (abs(c["z0"]) > 1.5)
                   == (abs(c["bias_over_se"] or 0) > 1.2))
    d2_ok = all(abs(c["z0"]) > 2.5 for _, c in deg)
    d3_ext = (sum(1 for _, c in ext if c["discordancia_pct_bca"])
              / len(ext)) if ext else None
    d3_norm = (sum(1 for _, c in norm if c["discordancia_pct_bca"])
               / len(norm)) if norm else None
    fonte_z0 = [abs(c["z0"]) for k, c in allc if k.startswith("fonte:")]
    fam_z0 = [abs(c["z0"]) for k, c in allc
              if k.startswith(("minref:", "drat:"))]
    hyp["H_C3_diagnostico_z0"] = {
        "n_contrastes": len(allc),
        "z0_extremos": len(ext), "z0_normais": len(norm),
        "degenerados": [{"key": k, "z0": c["z0"]} for k, c in deg],
        "D1_contingencia_z0_bias": {
            "coincidentes": d1_match, "n": len(allc),
            "taxa": d1_match / len(allc) if allc else None,
            "regra": "|z0|>1.5 <-> |bias_over_se|>1.2"},
        "D2_degenerados_com_z0_extremo": {
            "ok": d2_ok, "n_degenerados": len(deg),
            "claim": "todo degenerado tem |z0|>2.5"},
        "D3_discordancia_pct_vs_bca": {
            "taxa_z0_extremo": d3_ext, "taxa_normal": d3_norm},
        "D4_z0_fonte_vs_familia": {
            "mediana_fonte": med(fonte_z0),
            "mediana_familia": med(fam_z0),
            "n_fonte": len(fonte_z0), "n_familia": len(fam_z0)},
        "veredito_D2": ("CONFIRMADA" if d2_ok and deg else
                        ("SEM_DADOS" if not deg else "REFUTADA")),
    }

    # ---- H_C4 alvo MDE ----
    c1_keys = [k for k, _, _ in H_C1]
    mdes = {k: contrasts[k]["mde80"] for k in c1_keys
            if k in contrasts and contrasts[k].get("mde80")}
    n_ok_mde = sum(1 for v in mdes.values() if v < MDE_TARGET)
    hyp["H_C4_alvo_MDE"] = {
        "alvo": f"MDE80 < {MDE_TARGET} nos 6 testes boxdim",
        "n_atingido": f"{n_ok_mde}/{len(c1_keys)}",
        "valores": {k: round(v, 4) for k, v in mdes.items()},
        "veredito": ("ATINGIDO" if n_ok_mde == len(c1_keys)
                     else f"NAO_ATINGIDO ({n_ok_mde}/{len(c1_keys)})"),
    }

    hyp["_diagnostico"] = {
        "n_contrastes": len(contrasts),
        "incoerentes_total": sum(1 for c in contrasts.values()
                                 if c["veredito"] == "INCOERENTE"),
        "jack_discordantes": sorted(k for k, c in contrasts.items()
                                    if not c["jack_concordancia"]),
        "discordancia_pct_bca_total": sorted(
            k for k, c in contrasts.items()
            if c["discordancia_pct_bca"]),
    }

    print("\n--- hipoteses pre-registradas ---")
    for hname in ("H_C1_boxdim_primaria", "H_C2_saltos_secundaria"):
        h = hyp[hname]
        print(f"  {hname}: {h['veredito']}")
        for k, v in h["testes"].items():
            d = v["dado"]
            extra = ""
            if d:
                extra = (f"point={d['point']:+.4f} "
                         f"BC95=[{d['bca_lo']:+.4f},{d['bca_hi']:+.4f}] "
                         f"z0={d['z0']:+.2f} MDE={d['mde80']:.4f}")
            print(f"    {k}: {v['resultado']} {extra}")
    h3 = hyp["H_C3_diagnostico_z0"]
    print(f"\n  H_C3: extremos={h3['z0_extremos']}/{h3['n_contrastes']} "
          f"degenerados={len(h3['degenerados'])} D1={h3['D1_contingencia_z0_bias']['taxa']} "
          f"D2={h3['veredito_D2']} D3_ext={h3['D3_discordancia_pct_vs_bca']['taxa_z0_extremo']} "
          f"D4_fonte={h3['D4_z0_fonte_vs_familia']['mediana_fonte']} "
          f"fam={h3['D4_z0_fonte_vs_familia']['mediana_familia']}")
    h4 = hyp["H_C4_alvo_MDE"]
    print(f"  H_C4: {h4['veredito']} — {h4['n_atingido']} "
          f"{h4['valores']}")
    print(f"  incoerentes total={hyp['_diagnostico']['incoerentes_total']}"
          f"/{len(contrasts)}; jack discordantes="
          f"{len(hyp['_diagnostico']['jack_discordantes'])}")
    print(f"analise: {time.time()-t0:.0f}s")
    return contrasts, hyp, n_rows


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
            "bca90_lo", "bca90_hi", "bca_bonf5_lo", "bca_bonf5_hi",
            "bca_bonf3_lo", "bca_bonf3_hi", "bca_del1_lo", "bca_del1_hi",
            "pct_lo", "pct_hi", "excludes0", "excludes0_pct",
            "excludes0_bonf5", "excludes0_bonf3", "excludes0_del1",
            "discordancia_pct_bca", "jack_concordancia",
            "equivalente_d0.08", "equivalente_d0.06",
            "equivalente_d0.10", "point_outside_pct", "point_outside_bca",
            "se_boot", "mde80", "z0", "z0_extreme", "aceleracao",
            "boot_bias", "bias_over_se", "bias_serie_a", "bias_serie_b",
            "n_unique_boots", "tie_fraction", "jack_std", "degenerate",
            "n_boot", "n_jack_d", "n_jack_1"]
    with open(OUT_CONTRASTS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for k, c in sorted(contrasts.items()):
            w.writerow({"key": k} | {col: c.get(col) for col in cols
                                     if col != "key"})


# ---------------- main ----------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest-only", action="store_true")
    ap.add_argument("--analyze-only", action="store_true")
    args = ap.parse_args()

    t0 = time.time()
    print("=" * 70)
    print("D4' v4 (r4) — n=384, margem por precisao, z0 diagnosticado")
    print("=" * 70)

    st = selftests()
    print(f"\n[S1] BCa vs scipy: {st['S1_bca_scipy']['status']} "
          f"(diff={st['S1_bca_scipy'].get('max_diff')})")
    print(f"[S2S3] metricas n=384: {st['S2S3']['status']} "
          f"inv_err={st['S2S3']['S2_invariancia_erro']:.1e}")
    print(f"[S4] tipo-I: {st['S4_tipo1']['exclusoes']}/"
          f"{st['S4_tipo1']['n']}={st['S4_tipo1']['taxa']:.3f} "
          f"(gate<=0.20) {'OK' if st['S4_tipo1']['gate_ok'] else 'FALHA'}")
    print(f"[S5] poder: {st['S5_poder']['coerentes']}/"
          f"{st['S5_poder']['n']} coerentes (gate>=7) z0="
          f"{st['S5_poder']['z0_range']} "
          f"{'OK' if st['S5_poder']['gate_ok'] else 'FALHA'}")
    print(f"[DISJ] r2+r3 vs r4: {st['DISJ']['status']} "
          f"interseccao={st['DISJ'].get('interseccao')}")
    if st["status"] != "OK":
        print(f"[ABORTA] selftests: {st['status']}")
        return 2
    if args.selftest_only:
        print("\n(--selftest-only: abortando antes da coleta)")
        return 0

    if args.analyze_only:
        if not OUT_SERIES.exists():
            print("[ERRO] --analyze-only sem CSV de series")
            return 2
        rows = load_series_from_csv()
        print(f"\nre-usando {OUT_SERIES.name}: {len(rows)} linhas")
        mode = "analyze_only"
    else:
        rows = collect()
        write_series(rows)
        mode = "collect+analyze"

    contrasts, hyp, n_rows = analyze(rows)
    write_contrasts(contrasts)

    meta = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat()
                         .replace("+00:00", "Z"),
        "mode": mode,
        "seed": SEED, "seed_boot": SEED_BOOT, "n_boot": N_BOOT,
        "block": BLOCK, "d_delete": D_DELETE,
        "grid": {k: f"{len(v)} pontos (seeds novos vs r2+r3)"
                 for k, v in GRID.items()},
        "margens_boxdim": {"primaria": MARGIN_PRIMARY,
                           "sensibilidade": list(MARGINS[1:])},
        "ancora_margem": ("maior meia-largura IC90 dos pre-registrados "
                          "r3 = 0.0805 (H_B3); demais 0.061-0.073 — "
                          "ancora em PRECISAO (A1)"),
        "ic_primario": "BCa delete-d (A4); percentil = robustez",
        "regra_incoerencia": ("ponto fora do IC (pct ou BCa) => "
                              "INCOERENTE, nao conta em nenhuma "
                              "direcao (A3: regras globais exaustivas "
                              "declaradas no topo do script)"),
        "runtime_s": round(time.time() - t0, 1),
        "caveats": [
            ("Pre-registro: hipoteses/margens/regras fixadas neste "
             "codigo e no doc 31_ ANTES do run (commit anterior)."),
            ("Dados disjuntos de r2 E r3 (DISJ aborta em interseccao)."),
            ("Alvo MDE<0.06 por escala sqrt(64/384) — se nao atingido, "
             "e falha de ALVO (H_C4), nao de hipotese."),
            ("Escopo: distribuicao dos geradores (mesmos, seeds novos)."),
            ("delete-d janelas sobrepostas (aceleracao aproximada); "
             "delete-1 reportado como concordancia."),
            ("N1+N2; sem N4; H_C2 (EF) deferido; tau k↑ aberta."),
        ],
    }

    payload_series = {
        "metadata": {**meta,
                     "data_source": "gk_proof_fractal_v4.py (r4 coleta)",
                     "instances": {"rows": n_rows},
                     "selftests": st,
                     "csv": OUT_SERIES.name,
                     "csv_sha256": _sha(OUT_SERIES),
                     "sha_note": "sha256 bytes normalizados CRLF->LF"},
    }
    OUT_JSON.write_text(json.dumps(payload_series, indent=2,
                                   ensure_ascii=False), encoding="utf-8")

    payload_an = {
        "metadata": {**meta,
                     "data_source": ("gk_proof_fractal_v4.py (r4 "
                                     "analise — n=384, z0 diagnosticado)"),
                     "input_series_csv": OUT_SERIES.name,
                     "input_series_sha256": _sha(OUT_SERIES),
                     "csv": OUT_CONTRASTS.name,
                     "csv_sha256": _sha(OUT_CONTRASTS),
                     "sha_note": "sha256 bytes normalizados CRLF->LF"},
        "pre_registro": {
            "H_C1": [{"key": k, "tipo": t, "sinal": d}
                     for k, t, d in H_C1],
            "H_C2": [{"key": k, "tipo": t, "sinal": d}
                     for k, t, d in H_C2],
            "H_C3": "D1 contingencia; D2 CLAIM degenerados->|z0|>2.5; "
                    "D3 discordancia por grupo; D4 fonte vs familia",
            "H_C4": f"MDE80 < {MDE_TARGET} em todos os 6 boxdim",
            "regras_globais": "ver docstring do script (exaustivas)",
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
    print(f"runtime: {meta['runtime_s']}s")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

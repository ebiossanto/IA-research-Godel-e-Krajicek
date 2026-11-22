#!/usr/bin/env python3
"""
gk_proof_fractal_v6.py — D4' v6 (rodada r6): estratos EXATOS do relinc
+ CONSOLIDACAO da linha (redefinicao de (a), ramo concordante, tendencia
de saltos, meta-analise entre rodadas).

=====================================================================
PRE-REGISTRO (fixado ANTES de qualquer execucao com dados novos; o
commit deste codigo e do doc 33_ precede o run — prioridade temporal
C1): ver 33_PONTE_PROVA_FRACTAL_D4V6.md s1.
=====================================================================

PENDENCIAS DO r5 ATENDIDAS AQUI:
  r6-i ESTRATOS EXATOS DO RELINC (referee A4 do r5: 5/6 discordantes
     estavam em relinc). RAIZ: relinc NAO e ponto-a-ponto (diferenca
     de vizinhos) — o r5 reamostrava a serie JA DIFERENCIADA com
     estratos "ajustados" (runs[0]-=1: regra de fronteira implicita e
     errada). CORRECAO: reamostrar a SERIE PRIMITIVA x dentro dos
     estratos EXATOS de x e RECALCULAR relinc dentro de cada
     replicata (e do jackknife) — sem fronteira a aproximar; os
     estratos sao os de x, sempre. Para raw/log1p (ponto-a-ponto) o
     resultado e identico ao r5 (transformacao comuta com
     reamostragem) — so relinc muda.
     Teste: H_E1 = re-analise do CSV r5 congelado com o metodo
     corrigido (mesmos dados, so o metodo muda): discordancia em
     relinc deve cair de 5/45 para <=1/45.
  r6-ii CONSOLIDACAO (doc32 s6):
     - H_F2(a) REDEFINIDO: minref:imp-tau boxdim vira teste de
       EQUIVALENTE +/-0.05 (a direcao +1 falhou 3x — r5 referee A5);
       direcionais boxdim caem para 4 (Bonferroni alpha=0.05/4).
     - H_F1b TENDENCIA: meta-analise de Cochran (Q, 3 gl) sobre as4
       rodadas (r3, r4, r5, r6) dos 3 testes de saltos — decide a
       pergunta de declinio do r5 referee A1 com teste, nao com olho.
     - H_F4 RAMO CONCORDANTE: contagem em dados novos — se 0/135 de
       novo, recomendar remocao do ramo em r7 (r5 referee A3).
     - Smoke test de analyze() (stub do contrast) virou S7 OBRIGATORIO
       em toda execucao (licenca do bug do r5).

DADOS NOVOS E DISJUNTOS de r2..r5 (aborta se intersectar OS QUATRO):
  implication : m=3..6 x seeds 256..383   (r2:0..15 r3:16..31 r4:32..127 r5:128..255) = 512
  cadeia      : k=3..6 x seeds 256..383   (idem)                                       = 512
  tau_tiny    : seeds 1024..1535          (r2:0..63 r3:64..127 r4:128..511 r5:512..1023) = 512

HIPOTESES (declaradas aqui, ANTES do run):
  H_E1 — DIAGNOSTICO DO FIX (re-analise do CSV r5, MESMOS dados):
    discordancia da variante relinc (45 contrastes) com estratos
    exatos <= 1/45 (r5: 5/45). CONFIRMADA <=1; PARCIAL 2-4;
    REFUTADA >=5. (Rodada de METODO — nao nova confirmacao.)
  H_F1 — SALTOS PRIMARIO (4a rodada; mesmas 3 chaves/direcoes):
    (a) minref:imp-tau > 0 (r3:+0.173 r4:+0.185 r5:+0.138)   d+1
    (b) drat:imp-cadeia > 0 (r3:+0.110 r4:+0.117 r5:+0.080)   d+1
    (c) fonte:cadeia    > 0 (r3:+0.120 r4:+0.113 r5:+0.104)   d+1
    Bonferroni alpha*=0.05/3 (IC98.33%).
    H_F1a: CONFIRMADA iff 3/3 OK.
    H_F1b (tendencia, meta-analise): Cochran Q sobre as4 rodadas
      (r3+r4+r5 do CSVs congelados + r6; peso 1/SE^2) — p>0.05 ->
      SEM HETEROGENEIDADE (sem declinio detectavel); p<=0.05 ->
      REGISTRAR (sem claim de direcao). Caveat: rodadas mudam n e
      grades — Q captura variacao total entre rodadas.
  H_F2 — BOXDIM SECUNDARIO (6 testes; (a) REDEFINIDO como eq):
    (a) minref:imp-tau  EQUIVALENTE +/-0.05 (r5: FALHA -0.012; eq@0.05 la)
    (b) minref:cadeia-tau > 0  (r5: OK_BONF +0.025)             d+1
    (c) minref:imp-cadeia EQUIVALENTE +/-0.05 (r5: OK)          eq
    (d) drat:imp-cadeia < 0 [pista] (r5: OK_BONF -0.068)        d-1
    (e) fonte:tau < 0      (r5: OK -0.037)                      d-1
    (f) fonte:cadeia < 0   (r5: OK_BONF -0.051)                 d-1
    4 direcionais com Bonferroni alpha*=0.05/4 (IC98.75%); 2 TOST.
  H_F3 — RELINC EM DADOS NOVOS (caraterizacao): discordancia da
    variante relinc <= 10% (45 contrastes) com estratos exatos.
  H_F4 — RAMO CONCORDANTE (caraterizacao): contagem de *_FLAG em
    dados novos; se 0/135 de novo -> recomendar REMOCAO do ramo em r7.
  H_F5 — PODER: MDE80 < 0.06 nos 6 testes boxdim (continuidade r4/r5).

MARGENS boxdim (continuidade r5, ancoradas na precisao): 0.05
PRIMARIA + 0.03/0.08 sensibilidade.

REGRAS DE VEREDITO: identicas ao r5 (2 niveis; exaustivas; ver docstring
do r5 e doc 33 s1.5) — UNICA mudanca: o IC Bonferroni do grupo boxdim
passa a ser alpha=0.05/4 (4 direcionais em vez de 5).

SELFTESTS (aborta se falhar; A8):
  S1  BCa vs scipy (iid) — valida bca_ci
  S2  validacao de metricas n=512 (invariancia rank + ordenacoes)
  S4  TIPO-I: 40 nulos com grade, percentil estratificado + regra
      (gates <=0.15 cru e regra; BCa reportado)
  S5  PODER: 10 alternativos (efeito -0.049, sinal '-') — regra >=7/10
  S6  INCIDENCIA: discordancia do primario <=0.10 (bloco8 comparacao)
  S7  SMOKE DE ANALISE (NOVO, obrigatorio em toda execucao): analyze()
      com contrast() STUBADO sobre linhas fabricadas — pega bugs de
      plumbing do fim do analyze (licenca do pre.items() do r5)
  DISJ interseccao grade x (r2 U r3 U r4 U r5) = vazia
  (S1-S6 reaproveitam a calibracao validada do r5 via import)

INFERENCIA: percentil estratificado PRIMARIO + BCa estratificado
parceiro (regra 2 niveis) + Bonferroni (0.0125 boxdim / 0.0167
saltos) + bloco8 diagnostico nas 9 chaves. B=1000, seed_boot=SEED+7.

MODOS:
  python -u gk_proof_fractal_v6.py --selftest-only   # bateria+S7
  python -u gk_proof_fractal_v6.py --reanalise-r5    # H_E1 (~5min)
  python -u gk_proof_fractal_v6.py [--resume]        # coleta+analise
  python -u gk_proof_fractal_v6.py --analyze-only    # re-analise
SAIDAS: gk_proof_fractal_v6_series.csv / _contrasts.csv /
        gk_proof_fractal_v6.json / _analysis.json /
        gk_proof_fractal_v6_reanalise_r5.json + _contrasts.csv
"""

import argparse
import csv
import hashlib
import json
import math
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path

from gk_proof_fractal import (SEED, boxdim_curve, gen_implication,
                              higuchi_D, hurst_rs, solve_drat)
from gk_proof_fractal_v2 import gen_cadeia, gen_tau_tiny, variant_relinc
from gk_proof_fractal_v3 import METRICS
from gk_minref import minref
import gk_proof_fractal_v5 as v5
from gk_proof_fractal_v5 import (PROF_A, PROF_B, RUNS_SYNTH, _block_d,
                                 _jack_pooled, _pipeline_calib,
                                 _synth_family, build_series, calibrate,
                                 classify_global, runs_of, selftest_bca_scipy,
                                 strat_idx, validate_metrics_n512)

N_BOOT = 1000
SEED_BOOT = SEED + 7          # 20261126 — declarado
MARGIN_PRIMARY = 0.05
MARGINS = (0.05, 0.03, 0.08)
MDE_TARGET = 0.06
FAMS = ["implication", "cadeia", "tau_tiny"]

SRC_PREV = [Path("gk_proof_fractal_v2_series.csv"),
            Path("gk_proof_fractal_v3_series.csv"),
            Path("gk_proof_fractal_v4_series.csv"),
            Path("gk_proof_fractal_v5_series.csv")]
PRIOR_CONTRASTS = [Path("gk_proof_fractal_v3_contrasts.csv"),
                   Path("gk_proof_fractal_v4_contrasts.csv"),
                   Path("gk_proof_fractal_v5_contrasts.csv")]
R5_CONTRASTS = Path("gk_proof_fractal_v5_contrasts.csv")
R5_SERIES = Path("gk_proof_fractal_v5_series.csv")

OUT_SERIES = Path("gk_proof_fractal_v6_series.csv")
OUT_CONTRASTS = Path("gk_proof_fractal_v6_contrasts.csv")
OUT_JSON = Path("gk_proof_fractal_v6.json")
OUT_ANALYSIS = Path("gk_proof_fractal_v6_analysis.json")
OUT_REAN_CSV = Path("gk_proof_fractal_v6_reanalise_r5_contrasts.csv")
OUT_REAN_JSON = Path("gk_proof_fractal_v6_reanalise_r5.json")

GRID = {
    "implication": [(m, s) for m in range(3, 7) for s in range(256, 384)],
    "cadeia":      [(k, s) for k in range(3, 7) for s in range(256, 384)],
    "tau_tiny":    [(0, s) for s in range(1024, 1536)],
}
GENS = {"implication": gen_implication, "cadeia": gen_cadeia,
        "tau_tiny": gen_tau_tiny}

# transformacoes: relinc recalculado DENTRO da replicata (r6-i);
# raw/log1p ponto-a-ponto (comutam com reamostragem — identicos ao r5)
TRANSFORMS = {
    "raw": lambda x: x,
    "log1p": lambda x: [math.log1p(v) for v in x],
    "relinc": variant_relinc,
}

H_F1 = [
    ("minref:implication-tau_tiny:saltos:raw", "sep", +1),
    ("drat:implication-cadeia:saltos:raw", "sep", +1),
    ("fonte:cadeia:saltos:raw", "sep", +1),
]
H_F2 = [
    ("minref:implication-tau_tiny:boxdim:raw", "eq", 0),   # REDEFINIDO
    ("minref:cadeia-tau_tiny:boxdim:raw", "sep", +1),
    ("minref:implication-cadeia:boxdim:raw", "eq", 0),
    ("drat:implication-cadeia:boxdim:raw", "sep", -1),
    ("fonte:tau_tiny:boxdim:raw", "sep", -1),
    ("fonte:cadeia:boxdim:raw", "sep", -1),
]
PRE_KEYS = [k for k, _, _ in H_F1] + [k for k, _, _ in H_F2]  # 9 chaves
RELINC_KEYS_ALL = None   # preenchido em analyze (45 chaves relinc)


# ---------------- smoke S7 (stub do analyze) ----------------

def _smoke_rows():
    rows = []
    for fam, pts in GRID.items():
        for param, seed in pts:
            rows.append({"family": fam, "param": param, "seed": seed,
                         "tag": "smoke", "nvars": 5, "nclauses": 10,
                         "fecho": 20, "minref": 7,
                         "minref_censored": False, "sat_drat": "UNSAT",
                         "proof_drat": 9})
    return rows


def _smoke_flavor(flavor, allow_eq, with_block8):
    base = {
        "point": 0.05, "mde80": 0.04, "z0": 0.4, "aceleracao": 0.0,
        "pct_lo": 0.01, "pct_hi": 0.09,
        "pct90_lo": 0.015, "pct90_hi": 0.08,
        "pct_bonf4_lo": 0.008, "pct_bonf4_hi": 0.10,
        "pct_bonf3_lo": 0.01, "pct_bonf3_hi": 0.095,
        "bca_lo": 0.012, "bca_hi": 0.088,
        "bca90_lo": 0.016, "bca90_hi": 0.079,
        "point_outside": False, "point_outside_bca": False,
        "excludes0": True, "excludes0_bca": True,
        "excludes0_bonf4": True, "excludes0_bonf3": True,
        "concordante": True, "discordante": False,
        "equivalente_d0.05": None, "equivalente_d0.03": None,
        "equivalente_d0.08": None, "equiv_bca_d0.05": None,
        "veredito": "SEPARA",
        "bca_block8_lo": None, "bca_block8_hi": None,
        "block8_z0": None, "block8_outside": None,
        "n_boot": 1000, "n_jack": 1024,
    }
    if flavor == 2:
        base.update({"point": 0.20, "pct_lo": 0.10, "pct_hi": 0.30,
                     "bca_lo": 0.11, "bca_hi": 0.29,
                     "point_outside": True, "veredito": "SEPARA_FLAG"})
    elif flavor == 3:
        base.update({"point": 0.001, "pct_lo": -0.05, "pct_hi": 0.05,
                     "bca_lo": 0.02, "bca_hi": 0.06,
                     "point_outside": True, "excludes0": False,
                     "excludes0_bca": True, "concordante": False,
                     "discordante": True,
                     "veredito": "INCOERENTE_DISCORDANTE"})
    elif flavor == 4:
        base.update({"point": 0.01, "pct_lo": -0.05, "pct_hi": 0.07,
                     "bca_lo": -0.04, "bca_hi": 0.06,
                     "excludes0": False, "excludes0_bca": False,
                     "excludes0_bonf4": False, "excludes0_bonf3": False,
                     "veredito": "INCONCLUSIVO"})
    elif flavor == 5 and allow_eq:
        base.update({"point": 0.004, "pct_lo": -0.02, "pct_hi": 0.03,
                     "pct90_lo": -0.015, "pct90_hi": 0.02,
                     "bca_lo": -0.019, "bca_hi": 0.028,
                     "bca90_lo": -0.016, "bca90_hi": 0.021,
                     "excludes0": False, "excludes0_bca": False,
                     "equivalente_d0.05": True, "equiv_bca_d0.05": True,
                     "veredito": "EQUIVALENTE"})
    if with_block8:
        base.update({"bca_block8_lo": -0.3, "bca_block8_hi": -0.2,
                     "block8_z0": -2.4, "block8_outside": True})
    return base


def smoke_analyze():
    """S7: analyze() com contrast() STUBADO — exercita os caminhos de
    fim de analyze (classificadores, H_F1-F5, prints) sem custo.
    Prints suprimidos (os valores seriam dos stubs)."""
    global contrast, OUT_CONTRASTS
    orig = contrast
    state = {"i": 0}

    def stub(a0, b0, fn, tname, rng, paired, runs_a, runs_b,
             allow_eq=True, with_block8=False, n_boot=N_BOOT):
        state["i"] += 1
        flavor = (state["i"] % 5) or 5
        return _smoke_flavor(flavor, allow_eq, with_block8)

    contrast = stub
    import io as _io
    import contextlib as _ctx
    try:
        rows = _smoke_rows()
        buf = _io.StringIO()
        with _ctx.redirect_stdout(buf):
            contrasts, hyp, n_rows = analyze(rows, hetero=False)
        assert len(contrasts) == 135, len(contrasts)
        assert all(h in hyp for h in ("H_F1_saltos_4a_rodada",
                                      "H_F2_boxdim_consolidado",
                                      "H_F3_relinc_novos_dados",
                                      "H_F4_ramo_concordante",
                                      "H_F5_poder"))
        real = OUT_CONTRASTS
        OUT_CONTRASTS = real.with_suffix(".csv.smoke")
        write_contrasts(contrasts)
        OUT_CONTRASTS.unlink()
        OUT_CONTRASTS = real
    finally:
        contrast = orig
    return {"status": "OK", "n_contrastes": 135,
            "nota": "analyze() completo com stub (caminhos de fim)"}


# ---------------- contrastes: estratos EXATOS (r6-i) ----------------

def contrast(a0, b0, fn, tname, rng, paired, runs_a, runs_b,
             allow_eq=True, with_block8=False, n_boot=N_BOOT):
    """Percentil estratificado PRIMARIO sobre a SERIE PRIMITIVA; para
    relinc, a transformacao e recalculada DENTRO de cada replicata
    (estratos exatos de x — sem fronteira a aproximar; r6-i).
    raw/log1p comutam com a reamostragem -> identicos ao r5."""
    T = TRANSFORMS[tname]
    if len(a0) != len(b0) or len(a0) < 16:
        return None
    obs = fn(T(a0)) - fn(T(b0))
    if math.isnan(obs):
        return None
    boots = []
    for _ in range(n_boot):
        if paired:
            idx = strat_idx(runs_a, rng, len(a0))
            va = fn(T([a0[i] for i in idx]))
            vb = fn(T([b0[i] for i in idx]))
        else:
            ia = strat_idx(runs_a, rng, len(a0))
            ib = strat_idx(runs_b, rng, len(b0))
            va = fn(T([a0[i] for i in ia]))
            vb = fn(T([b0[i] for i in ib]))
        if va is not None and vb is not None \
                and not math.isnan(va) and not math.isnan(vb):
            boots.append(va - vb)
    if len(boots) < 200:
        return None

    def jk(x, y, drop):
        return fn(T(x[:drop] + x[drop + 1:])) - fn(T(y))
    jack = []
    if paired:
        for i in range(len(a0)):
            v = (fn(T(a0[:i] + a0[i + 1:]))
                 - fn(T(b0[:i] + b0[i + 1:])))
            if v is not None and not math.isnan(v):
                jack.append(v)
    else:
        for i in range(len(a0)):
            v = fn(T(a0[:i] + a0[i + 1:])) - fn(T(b0))
            if v is not None and not math.isnan(v):
                jack.append(v)
        for i in range(len(b0)):
            v = fn(T(a0)) - fn(T(b0[:i] + b0[i + 1:]))
            if v is not None and not math.isnan(v):
                jack.append(v)
    sb = sorted(boots)

    def q(p):
        return sb[min(len(sb) - 1, max(0, int(round(p * (len(sb) - 1)))))]
    plo, phi = q(0.025), q(0.975)
    p90lo, p90hi = q(0.05), q(0.95)
    pb4lo, pb4hi = q(0.00625), q(0.99375)     # Bonferroni 0.05/4 (boxdim)
    pb3lo, pb3hi = q(0.00835), q(0.99165)     # Bonferroni 0.05/3 (saltos)
    from gk_proof_fractal_v2_r2 import bca_ci
    lo, hi, info = bca_ci(obs, boots, jack, alpha=0.05)
    lo90b, hi90b, _ = bca_ci(obs, boots, jack, alpha=0.10)
    if lo is None:
        return None
    m = sum(boots) / len(boots)
    se = (sum((x - m) ** 2 for x in boots) / (len(boots) - 1)) ** 0.5
    bias = m - obs
    out = {
        "point": obs,
        "pct_lo": plo, "pct_hi": phi,
        "pct90_lo": p90lo, "pct90_hi": p90hi,
        "pct_bonf4_lo": pb4lo, "pct_bonf4_hi": pb4hi,
        "pct_bonf3_lo": pb3lo, "pct_bonf3_hi": pb3hi,
        "bca_lo": lo, "bca_hi": hi,
        "bca90_lo": lo90b, "bca90_hi": hi90b,
        "se_boot": se, "mde80": 2.801585 * se,
        "z0": info.get("z0"), "aceleracao": info.get("aceleracao"),
        "boot_bias": bias, "bias_over_se": bias / se if se else None,
        "point_outside": obs < plo or obs > phi,
        "point_outside_bca": obs < lo or obs > hi,
        "excludes0": plo > 0 or phi < 0,
        "excludes0_bca": lo > 0 or hi < 0,
        "excludes0_bonf4": pb4lo > 0 or pb4hi < 0,
        "excludes0_bonf3": pb3lo > 0 or pb3hi < 0,
        "n_boot": len(boots), "n_jack": len(jack),
    }
    excl_same_dir = (out["excludes0"] and out["excludes0_bca"]
                     and ((plo > 0) == (lo > 0))
                     and ((obs > 0) == (plo > 0)))
    both_include = (not out["excludes0"]) and (not out["excludes0_bca"])
    out["concordante"] = ((not out["point_outside"])
                          or excl_same_dir or both_include)
    out["discordante"] = out["point_outside"] and not out["concordante"]
    if allow_eq:
        out["equivalente_d0.05"] = p90lo > -0.05 and p90hi < 0.05
        out["equivalente_d0.03"] = p90lo > -0.03 and p90hi < 0.03
        out["equivalente_d0.08"] = p90lo > -0.08 and p90hi < 0.08
        out["equiv_bca_d0.05"] = lo90b > -0.05 and hi90b < 0.05
    else:
        out["equivalente_d0.05"] = out["equivalente_d0.03"] = \
            out["equivalente_d0.08"] = out["equiv_bca_d0.05"] = None
    if with_block8:
        boots8 = []
        for _ in range(n_boot):
            if paired:
                idx = _block_d(len(a0), rng, 8)
                va = fn(T([a0[i] for i in idx]))
                vb = fn(T([b0[i] for i in idx]))
            else:
                ia = _block_d(len(a0), rng, 8)
                ib = _block_d(len(b0), rng, 8)
                va = fn(T([a0[i] for i in ia]))
                vb = fn(T([b0[i] for i in ib]))
            if va is not None and vb is not None \
                    and not math.isnan(va) and not math.isnan(vb):
                boots8.append(va - vb)
        lo8, hi8, info8 = bca_ci(obs, boots8, jack, alpha=0.05)
        out["bca_block8_lo"] = lo8
        out["bca_block8_hi"] = hi8
        out["block8_z0"] = info8.get("z0") if info8 else None
        out["block8_outside"] = (lo8 is not None
                                 and (obs < lo8 or obs > hi8))
    else:
        out["bca_block8_lo"] = out["bca_block8_hi"] = None
        out["block8_z0"] = None
        out["block8_outside"] = None
    if out["point_outside"]:
        if excl_same_dir:
            out["veredito"] = "SEPARA_FLAG"
        elif both_include:
            out["veredito"] = "INCONCLUSIVO_FLAG"
        else:
            out["veredito"] = "INCOERENTE_DISCORDANTE"
    elif out["excludes0"]:
        out["veredito"] = "SEPARA"
    elif allow_eq and out.get("equivalente_d0.05"):
        out["veredito"] = "EQUIVALENTE"
    else:
        out["veredito"] = "INCONCLUSIVO"
    return out


# ---------------- classificadores (2 niveis; bonf por grupo) ----------------

def classify_test(c, kind, dirn, metric):
    if c is None:
        return "SEM_DADOS"
    bonf = (c["excludes0_bonf4"] if metric == "boxdim"
            else c["excludes0_bonf3"])
    outside = c["point_outside"]
    excl_dir = (c["excludes0"] and c["excludes0_bca"]
                and ((c["pct_lo"] > 0) == (c["bca_lo"] > 0))
                and ((c["point"] > 0) == (c["pct_lo"] > 0)))
    both_inc = (not c["excludes0"]) and (not c["excludes0_bca"])
    if kind == "eq":
        if not outside:
            if c.get("equivalente_d0.05"):
                return "OK"
            if c["excludes0"]:
                return "FALHA_SEPARA"
            return "FALHA_INCONCLUSIVO"
        if c.get("equivalente_d0.05") and c.get("equiv_bca_d0.05"):
            return "OK_FLAG"
        if excl_dir:
            return "FALHA_SEPARA_FLAG"
        if both_inc:
            return "FALHA_INCONCLUSIVO_FLAG"
        return "INCOERENTE_DISCORDANTE"
    if not outside:
        if not c["excludes0"]:
            return "FALHA_INCONCLUSIVO"
        sinal = 1 if c["point"] > 0 else -1
        if sinal != dirn:
            return "CONTRADITA"
        return "OK_BONF" if bonf else "OK"
    if excl_dir:
        sinal = 1 if c["pct_lo"] > 0 else -1
        if sinal != dirn:
            return "CONTRADITA_FLAG"
        return "OK_BONF_FLAG" if bonf else "OK_FLAG"
    if both_inc:
        return "FALHA_INCONCLUSIVO_FLAG"
    return "INCOERENTE_DISCORDANTE"


# ---------------- meta-analise entre rodadas (H_F1b) ----------------

def cochran_trend(key):
    """Q de Cochran sobre as4 rodadas (r3+r4+r5 dos CSVs congelados +
    r6 atual); peso 1/SE^2. Retorna dict ou None se faltar rodada."""
    pts = []
    for p in PRIOR_CONTRASTS:
        if not p.exists():
            continue
        for r in csv.DictReader(p.open(encoding="utf-8")):
            if r["key"] == key and r.get("se_boot"):
                try:
                    pts.append((p.stem.split("_")[-2],
                                float(r["point"]), float(r["se_boot"])))
                except (ValueError, IndexError):
                    pass
    return pts   # a rodada r6 e agregada pelo chamador


def cochran_Q(items):
    """items: [(label, point, se)] — Q com gl=len-1; p via chi2."""
    if len(items) < 2:
        return None
    ws = [1.0 / (s * s) for _, _, s in items if s > 0]
    th = [t for _, t, s in items if s > 0]
    if len(ws) != len(items) or not ws:
        return None
    wm = sum(ws) / len(ws)
    tbar = sum(w * t for w, t in zip(ws, th)) / sum(ws)
    Q = sum(w * (t - tbar) ** 2 for w, t in zip(ws, th))
    try:
        from scipy import stats as sstats
        p = float(sstats.chi2.sf(Q, len(items) - 1))
    except Exception:
        p = None
    return {"Q": round(Q, 4), "gl": len(items) - 1, "p": p,
            "rodadas": [(lab, round(t, 4), round(s, 4))
                        for lab, t, s in items]}


# ---------------- H_E1: re-analise do CSV r5 ----------------

def reanalise_r5():
    """Recalcula os45 contrastes relinc do CSV r5 congelado com os
    estratos EXATOS (mesmos dados, so o metodo muda) e compara a
    discordancia com a do r5 (5/45)."""
    t0 = time.time()
    rows = v5.load_series_from_csv() if v5.OUT_SERIES.exists() else None
    if rows is None:
        print("[ERRO] CSV do r5 ausente")
        return 2
    series, strata, n_rows = build_series(rows)
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
    n_done = 0
    for label, sysname, fa, fb, paired in combos:
        if sysname == "fonte":
            a0, b0 = series.get((fa, "minref"), []), \
                series.get((fa, "drat"), [])
            ra, rb = strata.get((fa, "minref"), []), \
                strata.get((fa, "drat"), [])
        else:
            a0, b0 = series.get((fa, sysname), []), \
                series.get((fb, sysname), [])
            ra, rb = strata.get((fa, sysname), []), \
                strata.get((fb, sysname), [])
        for mname, fn in METRICS.items():
            key = f"{label}:{mname}:relinc"
            c = contrast(a0, b0, fn, "relinc", rng, paired, ra, rb,
                         allow_eq=(mname == "boxdim"), with_block8=False)
            if c is None:
                continue
            contrasts[key] = c
            n_done += 1
            if n_done % 9 == 0:
                print(f"  relinc: {n_done}/45 contrastes "
                      f"({time.time()-t0:.0f}s)", flush=True)
    # comparacao com o r5 congelado
    old = {}
    if R5_CONTRASTS.exists():
        for r in csv.DictReader(R5_CONTRASTS.open(encoding="utf-8")):
            if r["key"].endswith(":relinc"):
                old[r["key"]] = r
    old_disc = sorted(k for k, r in old.items()
                      if r.get("discordante") == "True")
    new_disc = sorted(k for k, c in contrasts.items()
                      if c["discordante"])
    n = len(contrasts)
    verdict = ("CONFIRMADA" if len(new_disc) <= 1 else
               "PARCIAL" if len(new_disc) <= 4 else "REFUTADA")
    payload = {
        "metadata": {
            "timestamp_utc": datetime.now(timezone.utc).isoformat()
                             .replace("+00:00", "Z"),
            "data_source": ("gk_proof_fractal_v6.py --reanalise-r5 "
                            "(estratos exatos do relinc; MESMOS dados "
                            "r5, so o metodo muda)"),
            "input_series_csv": v5.OUT_SERIES.name,
            "input_contrasts_r5": R5_CONTRASTS.name,
            "seed_boot": SEED_BOOT, "n_boot": N_BOOT,
            "runtime_s": round(time.time() - t0, 1),
            "csv": OUT_REAN_CSV.name,
            "csv_sha256": _sha(OUT_REAN_CSV)
            if OUT_REAN_CSV.exists() else None,
            "sha_note": "sha256 bytes normalizados CRLF->LF",
        },
        "H_E1_diagnostico_relinc": {
            "enunciado": ("discordancia em relinc com estratos exatos "
                          "<= 1/45 (r5: 5/45)"),
            "r5_discordantes": old_disc,
            "r5_n": len(old),
            "novo_discordantes": new_disc,
            "novo_n": n,
            "veredito": verdict,
        },
        "contrasts": contrasts,
    }
    write_rean_csv(contrasts)
    payload["metadata"]["csv_sha256"] = _sha(OUT_REAN_CSV)
    OUT_REAN_JSON.write_text(json.dumps(payload, indent=2,
                                        ensure_ascii=False),
                             encoding="utf-8")
    h = payload["H_E1_diagnostico_relinc"]
    print(f"\nH_E1: {h['veredito']} — r5: {len(old_disc)}/{h['r5_n']} "
          f"discordantes -> r6-metodo: {len(new_disc)}/{n}")
    if old_disc:
        print("  r5 discordantes e status novo:")
        for k in old_disc:
            c = contrasts.get(k)
            print(f"    {k}: {'novo=' + c['veredito'] if c else 'AUSENTE'}")
    print(f"[OK] {OUT_REAN_CSV.name} + {OUT_REAN_JSON.name} "
          f"({time.time()-t0:.0f}s)")
    return 0


def write_rean_csv(contrasts):
    cols = ["key", "veredito", "point", "pct_lo", "pct_hi",
            "bca_lo", "bca_hi", "excludes0", "excludes0_bca",
            "point_outside", "concordante", "discordante",
            "se_boot", "mde80", "z0", "n_boot", "n_jack"]
    with open(OUT_REAN_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for k, c in sorted(contrasts.items()):
            w.writerow({"key": k} | {col: c.get(col) for col in cols
                                     if col != "key"})


# ---------------- coleta (checkpoint + resume) ----------------

def write_series(rows):
    if not rows:
        return
    tmp = OUT_SERIES.with_suffix(".csv.tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, OUT_SERIES)


def collect(existing=None):
    rows = list(existing) if existing else []
    done = {(r["family"], str(r["param"]), str(r["seed"])) for r in rows}
    if rows:
        print(f"resumo: {len(rows)} instancias do checkpoint — pulando",
              flush=True)
    censored = skipped = 0
    t_all = time.time()
    for fam, points in GRID.items():
        todo = [(p, s) for p, s in points
                if (fam, str(p), str(s)) not in done]
        if not todo:
            print(f"\n--- família: {fam} (ja completa) ---", flush=True)
            continue
        print(f"\n--- família: {fam} ({len(todo)} novas de "
              f"{len(points)}) ---", flush=True)
        t_f = time.time()
        slow = 0
        for param, seed in todo:
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
            })
            write_series(rows)
        done_n = sum(1 for r in rows if r["family"] == fam)
        exact = [r for r in rows if r["family"] == fam
                 and str(r["minref_censored"]) == "False"]
        unsat = [r for r in rows if r["family"] == fam
                 and r["sat_drat"] == "UNSAT"]
        vals = sorted({str(r["minref"]) for r in exact},
                      key=lambda v: int(v) if v.isdigit() else 0)
        print(f"  UNSAT: {len(unsat)}/{done_n} | exatos: {len(exact)} "
              f"| valores: {vals} | lentos: {slow} | "
              f"{time.time()-t_f:.0f}s", flush=True)
    print(f"\ncoleta total: {len(rows)} linhas, {censored} censuras, "
          f"{skipped} descartes, {(time.time()-t_all)/60:.1f}min")
    return rows


def load_series_from_csv():
    return list(csv.DictReader(OUT_SERIES.open(encoding="utf-8")))


def check_disjoint():
    used = set()
    n_src = 0
    for src in SRC_PREV:
        if not src.exists():
            continue
        for r in csv.DictReader(src.open(encoding="utf-8")):
            used.add((r["family"], r["param"], r["seed"]))
        n_src += 1
    if n_src == 0:
        return {"status": "AVISO: CSVs anteriores ausentes — pulado"}
    mine = {(f, str(p), str(s)) for f, pts in GRID.items()
            for p, s in pts}
    inter = used & mine
    return {"status": "OK" if not inter else "FALHA",
            "n_prev": len(used), "n_r6": len(mine), "fontes": n_src,
            "interseccao": sorted(inter)[:10]}


# ---------------- analise ----------------

def analyze(rows, hetero=True):
    t0 = time.time()
    series, strata, n_rows = build_series(rows)
    print("\nseries: " + ", ".join(
        f"{f}|{s}={len(v)} estratos={strata[(f, s)]}"
        for (f, s), v in sorted(series.items())))
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
            ra, rb = strata.get((fa, "minref"), []), \
                strata.get((fa, "drat"), [])
        else:
            a0, b0 = series.get((fa, sysname), []), \
                series.get((fb, sysname), [])
            ra, rb = strata.get((fa, sysname), []), \
                strata.get((fb, sysname), [])
        for vname in ("raw", "log1p", "relinc"):
            for mname, fn in METRICS.items():
                key = f"{label}:{mname}:{vname}"
                c = contrast(a0, b0, fn, vname, rng, paired, ra, rb,
                             allow_eq=(mname == "boxdim"),
                             with_block8=(key in PRE_KEYS))
                if c is None:
                    continue
                contrasts[key] = c

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

    hyp = {"H_F1_saltos_4a_rodada": eval_hyp(H_F1, "H_F1"),
           "H_F2_boxdim_consolidado": eval_hyp(H_F2, "H_F2")}

    # ---- H_F1b: tendencia/meta-analise entre rodadas ----
    if hetero:
        trend = {}
        for key, _, _ in H_F1:
            items = cochran_trend(key)
            d = contrasts.get(key)
            if d:
                items = items + [("r6", d["point"], d["se_boot"])]
            q = cochran_Q(items)
            trend[key] = q
        hyp["H_F1_saltos_4a_rodada"]["tendencia_Q"] = trend
        missing = any(t is None for t in trend.values())
        hyp["H_F1_saltos_4a_rodada"]["tendencia_veredito"] = (
            "SEM_DADOS (rodada anterior ausente)" if missing else
            "SEM_HETEROGENEIDADE" if all(
                (t["p"] is None or t["p"] > 0.05) for t in trend.values())
            else "HETEROGENEIDADE_REGISTRADA (sem claim de direcao)")

    # ---- H_F3: relinc em dados novos ----
    rel_keys = [k for k in contrasts if k.endswith(":relinc")]
    rel_disc = [k for k in rel_keys if contrasts[k]["discordante"]]
    hyp["H_F3_relinc_novos_dados"] = {
        "enunciado": ("discordancia da variante relinc <= 10% com "
                      "estratos exatos (r5: 5/45)"),
        "n": len(rel_keys), "discordantes": rel_disc,
        "taxa": (len(rel_disc) / len(rel_keys)) if rel_keys else None,
        "veredito": ("CONFIRMADA" if rel_keys
                     and len(rel_disc) / len(rel_keys) <= 0.10
                     else ("REFUTADA" if rel_keys else "SEM_DADOS")),
    }

    # ---- H_F4: ramo concordante ----
    allc = list(contrasts.items())
    flags = sorted(k for k, c in allc
                   if c["veredito"].endswith("_FLAG"))
    hyp["H_F4_ramo_concordante"] = {
        "enunciado": ("contagem de *_FLAG (ramo concordante) em dados "
                      "novos; 0/135 de novo -> recomendar remocao em r7"),
        "n_flags": len(flags), "flags": flags,
        "total": len(allc),
        "veredito": ("ZERO_DE_NOVO (candidato a remocao em r7)"
                     if not flags else
                     f"DISPAROU ({len(flags)}x) — ramo exercitado"),
    }

    # ---- H_F5: MDE ----
    d2_keys = [k for k, _, _ in H_F2]
    mdes = {k: contrasts[k]["mde80"] for k in d2_keys
            if k in contrasts and contrasts[k].get("mde80")}
    n_ok_mde = sum(1 for v in mdes.values() if v < MDE_TARGET)
    hyp["H_F5_poder"] = {
        "alvo": f"MDE80 < {MDE_TARGET} nos 6 testes boxdim",
        "n_atingido": f"{n_ok_mde}/{len(d2_keys)}",
        "valores": {k: round(v, 4) for k, v in mdes.items()},
        "veredito": ("ATINGIDO" if n_ok_mde == len(d2_keys)
                     else f"NAO_ATINGIDO ({n_ok_mde}/{len(d2_keys)})"),
    }

    hyp["_diagnostico"] = {
        "n_contrastes": len(contrasts),
        "vereditos": {},
        "z0_extremos": sum(1 for _, c in allc
                           if abs(c["z0"] or 0) > 1.5),
        "degenerados": sorted(k for k, c in allc
                              if c["bca_lo"] == c["bca_hi"]),
        "fora_do_IC": sorted(k for k, c in allc if c["point_outside"]),
        "discordantes": sorted(k for k, c in allc if c["discordante"]),
    }
    for _, c in allc:
        v = c["veredito"]
        hyp["_diagnostico"]["vereditos"][v] = \
            hyp["_diagnostico"]["vereditos"].get(v, 0) + 1

    print("\n--- hipoteses pre-registradas ---")
    for hname in ("H_F1_saltos_4a_rodada", "H_F2_boxdim_consolidado"):
        h = hyp[hname]
        print(f"  {hname}: {h['veredito']}")
        for k, v in h["testes"].items():
            d = v["dado"]
            extra = ""
            if d:
                extra = (f"point={d['point']:+.4f} "
                         f"CI=[{d['pct_lo']:+.4f},{d['pct_hi']:+.4f}] "
                         f"z0={d['z0']:+.2f} MDE={d['mde80']:.4f}"
                         + (" | bloco8_fora" if d.get("block8_outside")
                            else ""))
            print(f"    {k}: {v['resultado']} {extra}")
    if hetero and "tendencia_Q" in hyp["H_F1_saltos_4a_rodada"]:
        for k, t in hyp["H_F1_saltos_4a_rodada"]["tendencia_Q"].items():
            if t:
                print(f"    [tendencia] {k}: Q={t['Q']} gl={t['gl']} "
                      f"p={t['p']}")
        print(f"    tendencia: "
              f"{hyp['H_F1_saltos_4a_rodada']['tendencia_veredito']}")
    h3 = hyp["H_F3_relinc_novos_dados"]
    print(f"  H_F3: {h3['veredito']} — relinc discordantes "
          f"{len(h3['discordantes'])}/{h3['n']}")
    h4 = hyp["H_F4_ramo_concordante"]
    print(f"  H_F4: {h4['veredito']}")
    h5 = hyp["H_F5_poder"]
    print(f"  H_F5: {h5['veredito']} {h5['valores']}")
    dg = hyp["_diagnostico"]
    print(f"  diagnosticos: z0 extremos={dg['z0_extremos']}/"
          f"{dg['n_contrastes']} degenerados={len(dg['degenerados'])} "
          f"fora={len(dg['fora_do_IC'])} discordantes="
          f"{len(dg['discordantes'])} vereditos={dg['vereditos']}")
    print(f"analise: {time.time()-t0:.0f}s")
    return contrasts, hyp, n_rows


# ---------------- escrita ----------------

def _sha(p):
    return hashlib.sha256(
        p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def write_contrasts(contrasts):
    cols = ["key", "veredito", "point",
            "pct_lo", "pct_hi", "pct90_lo", "pct90_hi",
            "pct_bonf4_lo", "pct_bonf4_hi",
            "pct_bonf3_lo", "pct_bonf3_hi",
            "bca_lo", "bca_hi", "bca90_lo", "bca90_hi",
            "excludes0", "excludes0_bca", "excludes0_bonf4",
            "excludes0_bonf3", "point_outside", "point_outside_bca",
            "concordante", "discordante",
            "equivalente_d0.05", "equivalente_d0.03",
            "equivalente_d0.08", "equiv_bca_d0.05",
            "bca_block8_lo", "bca_block8_hi", "block8_z0",
            "block8_outside", "se_boot", "mde80", "z0", "aceleracao",
            "boot_bias", "bias_over_se", "n_boot", "n_jack"]
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
    ap.add_argument("--reanalise-r5", action="store_true")
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    t0 = time.time()
    print("=" * 70)
    print("D4' v6 (r6) — estratos EXATOS do relinc + consolidacao")
    print("=" * 70)

    s1 = selftest_bca_scipy()
    s2 = validate_metrics_n512()
    cal = calibrate()            # calibracao validada do r5 (re-execucao)
    smk = smoke_analyze()        # S7: analyze() stubado (obrigatorio)
    disj = check_disjoint()
    print(f"\n[S1] BCa vs scipy: {s1['status']} "
          f"(diff={s1.get('max_diff')})")
    print(f"[S2] metricas n=512: {s2['status']}")
    t4 = cal["S4_tipo1"]
    print(f"[S4] tipo-I: pct={t4['percentil_cru']}/{t4['n']} "
          f"regra={t4['regra_2niveis']}/{t4['n']} bca="
          f"{t4['bca_cru']}/{t4['n']} "
          f"{'OK' if t4['gate_ok'] else 'FALHA'}")
    print(f"[S5] poder: {cal['S5_poder']['regra_detectou']}/"
          f"{cal['S5_poder']['n']} "
          f"{'OK' if cal['S5_poder']['gate_ok'] else 'FALHA'}")
    s6 = cal["S6_incidencia"]
    print(f"[S6] incidencia: disc="
          f"{s6['percentil_estratificado']['discordancia']:.3f} "
          f"({'OK' if s6['percentil_estratificado']['gate_ok'] else 'FALHA'})")
    print(f"[S7] smoke analyze: {smk['status']} "
          f"({smk['n_contrastes']} contrastes stub)")
    print(f"[DISJ] r2..r5 vs r6: {disj['status']} "
          f"interseccao={disj.get('interseccao')}")
    ok = (s1["status"] in ("OK", "scipy ausente — pulado")
          and s2["status"] == "OK" and cal["status"] == "OK"
          and smk["status"] == "OK"
          and disj["status"] in ("OK",
                                 "AVISO: CSVs anteriores ausentes — pulado"))
    if not ok:
        print(f"[ABORTA] selftests: disj={disj['status']} "
              f"smk={smk['status']} cal={cal['status']}")
        return 2
    if args.selftest_only:
        print("\n(--selftest-only: abortando antes do run)")
        return 0
    if args.reanalise_r5:
        return reanalise_r5()

    if args.analyze_only:
        if not OUT_SERIES.exists():
            print("[ERRO] --analyze-only sem CSV de series")
            return 2
        rows = load_series_from_csv()
        print(f"\nre-usando {OUT_SERIES.name}: {len(rows)} linhas")
        mode = "analyze_only"
    else:
        existing = []
        if args.resume and OUT_SERIES.exists():
            existing = load_series_from_csv()
            grid_keys = {(f, str(p), str(s))
                         for f, pts in GRID.items() for p, s in pts}
            foreign = [(r["family"], r["param"], r["seed"])
                       for r in existing
                       if (r["family"], r["param"], r["seed"])
                       not in grid_keys]
            if foreign:
                print(f"[ERRO] checkpoint com {len(foreign)} linhas "
                      f"fora da grade: {foreign[:5]} — abortando")
                return 2
            print(f"--resume: {len(existing)} instancias do checkpoint",
                  flush=True)
        rows = collect(existing)
        write_series(rows)
        mode = ("resume+collect+analyze" if existing
                else "collect+analyze")

    contrasts, hyp, n_rows = analyze(rows, hetero=True)
    write_contrasts(contrasts)

    meta = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat()
                         .replace("+00:00", "Z"),
        "mode": mode,
        "seed": SEED, "seed_boot": SEED_BOOT, "n_boot": N_BOOT,
        "metodo_primario": ("percentil BOOTSTRAP ESTRATIFICADO (herdado "
                            "e validado do r5: S4-S6 re-executados); "
                            "relinc com estratos EXATOS — transformacao "
                            "recalculada dentro de cada replicata (r6-i)"),
        "regra_2_niveis": ("identica ao r5 (2 niveis; exaustiva); "
                           "bonf boxdim agora 0.05/4 (4 direcionais)"),
        "margens_boxdim": {"primaria": MARGIN_PRIMARY,
                           "sensibilidade": list(MARGINS[1:])},
        "grid": {k: f"{len(v)} pontos (seeds novos vs r2..r5)"
                 for k, v in GRID.items()},
        "runtime_s": round(time.time() - t0, 1),
        "caveats": [
            ("Pre-registro: hipoteses/margens/regras fixados neste "
             "codigo e no doc 33_ ANTES do run."),
            ("Dados disjuntos de r2..r5 (DISJ aborta)."),
            ("raw/log1p identicos ao r5 (transformacao ponto-a-ponto "
             "comuta); so relinc muda (estratos exatos)."),
            ("H_F1b (Cochran Q) compara rodadas com n/grades "
             "diferentes — captura variacao total, nao so declinio."),
            ("Checkpoint atomico + --resume (crash CaDiCaL)."),
            ("N1+N2; sem N4; H_C2 (EF) deferido; tau k↑ aberta."),
        ],
    }
    payload_series = {
        "metadata": {**meta,
                     "data_source": "gk_proof_fractal_v6.py (r6 coleta)",
                     "instances": {"rows": n_rows},
                     "selftests": {"S1_bca_scipy": s1, "S2_metricas": s2,
                                   "calibracao": cal, "S7_smoke": smk,
                                   "DISJ": disj},
                     "csv": OUT_SERIES.name,
                     "csv_sha256": _sha(OUT_SERIES),
                     "sha_note": "sha256 bytes normalizados CRLF->LF"},
    }
    OUT_JSON.write_text(json.dumps(payload_series, indent=2,
                                   ensure_ascii=False), encoding="utf-8")
    payload_an = {
        "metadata": {**meta,
                     "data_source": ("gk_proof_fractal_v6.py (r6 "
                                     "analise — estratos exatos + "
                                     "consolidacao)"),
                     "input_series_csv": OUT_SERIES.name,
                     "input_series_sha256": _sha(OUT_SERIES),
                     "csv": OUT_CONTRASTS.name,
                     "csv_sha256": _sha(OUT_CONTRASTS),
                     "sha_note": "sha256 bytes normalizados CRLF->LF"},
        "pre_registro": {
            "H_E1": "re-analise r5: relinc discord <=1/45 (separado)",
            "H_F1": [{"key": k, "tipo": t, "sinal": d}
                     for k, t, d in H_F1],
            "H_F1b": "Cochran Q entre r3..r6 (p>0.05 = sem tendencia)",
            "H_F2": [{"key": k, "tipo": t, "sinal": d}
                     for k, t, d in H_F2],
            "H_F3": "relinc discordancia <=10% em dados novos",
            "H_F4": "ramo concordante: 0/135 -> remover em r7",
            "H_F5": "MDE80 < 0.06 nos 6 boxdim",
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

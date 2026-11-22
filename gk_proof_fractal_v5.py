#!/usr/bin/env python3
"""
gk_proof_fractal_v5.py — D4' v5 (rodada r5): saltos primario, metodo de
IC NOVO (bootstrap estratificado + percentil primario) com calibracao de
incidencia, e regra de 2 niveis de incoerencia.

=====================================================================
PRE-REGISTRO (fixado ANTES de qualquer execucao com dados novos; o
commit deste codigo e do doc 32_ precede o run — prioridade temporal
C1): ver 32_PONTE_PROVA_FRACTAL_D4V5.md s1.
=====================================================================

PENDENCIAS DO r4 ATENDIDAS AQUI:
  r5-i METODO DE IC NOVO: o r4 mediu que BCa+bloco fixo DEGRADA com n
     (incoerencia 7%->33%; viés de destruicao de macroestrutura nao
     encolhe, SE encolhe -> z0 cresce). A raiz: as series sao
     INSTANCIAS INDEPENDENTES dentro de cada estrato de parametro
     (DGP: (param, seed) iid por seed), nao series temporais — o
     bloco era o modelo errado. METODO ESCOLHIDO PELA CALIBRACAO
     (S4-S6, dados sinteticos COM GRADE antes do run):
       - PRIMARIO = PERCENTIL com BOOTSTRAP ESTRATIFICADO (iid dentro
         do estrato; macro preservada). Calibracao: tipo-I 1/40=0.025
         (nominal ~0.05) vs BCa-estrat 8/40=0.20 (a correcao z0 com
         aceleracao~0 e instavel neste statistico — por isso BCa NAO
         e primario) e vs bloco8 incidencia ~50-100%.
       - PARCEIRO da regra de 2 niveis = BCa estratificado (mesmos
         boots; papel: concordancia quando o ponto cai fora).
       - DIAGNOSTICO head-to-head = BCa+bloco8 (metodo do r4) nas 9
         chaves pre-registradas — comparacao de incidencia em dados
         REAIS.
     Gates de calibracao (S4-S6): tipo-I cru E da regra <= 0.15;
     discordancia do primario <= 0.10; poder (regra) >= 7/10.
  r5-ii REGRA DE 2 NIVEIS (r4 A5): ponto fora do IC primario ->
     CONCORDANTE (os DOIS metodos concordam: excluem 0 no MESMO sinal
     coerente com o ponto, ou ambos incluem 0) -> CONTA com flag;
     DISCORDANTE -> nao conta em nenhuma direcao. Definicao formal:
     ver REGRAS abaixo.
  r5-iii SALTOS PRIMARIO (r4 H_C2 3/3 Bonferroni): H_D1 promove
     saltos a metrica PRIMARIA confirmatoria (3 testes, mesmas
     chaves/direcoes; ancoras r3+r4); boxdim vira SECUNDARIA (H_D2,
     os mesmos 6 testes do H_C1 do r4 reavaliados em serie nova com
     metodo novo).

DADOS NOVOS E DISJUNTOS de r2, r3 E r4 (checagem obrigatoria contra
OS TRES CSVs -> aborta se intersectar):
  implication : m=3..6 x seeds 128..255  (r2:0..15 r3:16..31 r4:32..127) = 512
  cadeia      : k=3..6 x seeds 128..255  (idem)                          = 512
  tau_tiny    : seeds 512..1023          (r2:0..63 r3:64..127 r4:128..511) = 512
n=512/familia fecha a pendencia de MDE do r4 (previsao: 6/6 < 0.06,
H_D4).

HIPOTESES (declaradas aqui, ANTES do run):
  H_D1 — PRIMARIA (saltos, raw; 3 direcionais; ancoras r3+r4):
    (a) minref:implication-tau_tiny > 0  (r3:+0.173, r4:+0.185)   d+1
    (b) drat:implication-cadeia     > 0  (r3:+0.110, r4:+0.117)   d+1
    (c) fonte:cadeia                > 0  (r3:+0.120, r4:+0.113)   d+1
    Bonferroni alpha*=0.05/3 (IC98.33% reportado).
    CONFIRMADA iff 3/3 OK (flags concordantes contam, reportados);
    PARCIAL 2/3; REFUTADA <=1/3; CONTRADITA se sinal oposto.
  H_D2 — SECUNDARIA (boxdim, raw; os 6 testes do H_C1 r4, serie nova,
    metodo novo, regra nova):
    (a) minref:imp-tau > 0 (r4: FALHA_INCONCLUSIVO -0.024)          d+1
    (b) minref:cadeia-tau > 0 (r4 +0.048 INCOERENTE)                d+1
    (c) minref:imp-cadeia EQUIVALENTE +/-0.05 (r4 INCOERENTE; r3 eq)
    (d) drat:imp-cadeia < 0 [pista] (r4 -0.107 INCOERENTE, pct exclui) d-1
    (e) fonte:tau < 0 (r4 -0.128 OK_BONF; r3 -0.102; r2 -0.112)     d-1
    (f) fonte:cadeia < 0 (r4 -0.092 INCOERENTE, pct exclui)          d-1
    Bonferroni alpha*=0.05/5 nos5 direcionais (IC99%); (c) TOST.
  H_D3 — INCIDENCIA (caraterizacao; gate e na calibracao S6):
    relatorio em dados REAIS: incidencia total e split
    concordante/discordante do primario; head-to-head bloco8 nas 9
    chaves; alvo: discordante <= 10%.
  H_D4 — ALVO DE DESIGN: MDE80 < 0.06 nos 6 testes boxdim
    (previsao sqrt(384/512): 0.024-0.059 -> 6/6).

MARGENS boxdim (ancoradas em PRECISAO do r4 — A1):
  0.05 PRIMARIA — ancora: maior meia-largura IC90 percentilica r4
     estimada (1,645*SE) = 0.040 (teste (e)); + folga.
  0.03 e 0.08 SENSIBILIDADE (reportadas, nao promovidas).

REGRAS DE VEREDITO (EXAUSTIVAS — 2 niveis; fixadas ANTES do run):
  Por teste, com CI PRIMARIO (percentil estratificado) e CI PARCEIRO
  (BCa estratificado):
    ponto DENTRO do CI primario:
      direcional: exclui 0 com sinal coerente -> OK (OK_BONF se o IC
        Bonferroni primario tambem exclui); exclui sinal oposto ->
        CONTRADITA; nao exclui -> FALHA_INCONCLUSIVO.
      equivalencia (c): IC90 primario na margem -> OK; exclui 0 ->
        FALHA_SEPARA; senao FALHA_INCONCLUSIVO.
    ponto FORA do CI primario:
      CONCORDANTE = os DOIS metodos concordam — (direcional) excluem 0
        no MESMO sinal coerente com o ponto, ou ambos incluem 0;
        (eq) os DOIS IC90 na margem, ou ambos excluem coerentes, ou
        ambos incluem 0 -> conta com FLAG (OK_FLAG / CONTRADITA_FLAG /
        FALHA_SEPARA_FLAG / FALHA_INCONCLUSIVO_FLAG).
      DISCORDANTE -> INCOERENTE_DISCORDANTE (nao conta em nenhuma
        direcao).
      SEM_DADOS quando nao ha teste.
  Global: CONTRADITA* -> REFUTADA_CONTRADITA; C = contaveis (OK*/
    FALHA*, incl. flags); |C| < ceil(0.6*n) -> INDETERMINADO; todos C
    OK -> CONFIRMADA; nenhum OK -> REFUTADA; senao PARCIAL. Flags
    reportados na string do veredito.

SELFTESTS OBRIGATORIOS ANTES DO RUN (aborta se falhar; A8):
  S1  BCa vs scipy (iid)                                   — valida bca_ci
  S2  invariancia monotona de boxdim_rank (erro 0)          — n=512
  S4  TIPO-I (calibracao): 40 pares NULOS com grade (mesmo
      perfil+iid), percentil estratificado + regra — gates:
      tipo-I cru <= 0.15 E regra <= 0.15 (BCa cru REPORTADO,
      prototipo: 0.20 — razao de nao ser primario)
  S5  PODER: 10 pares ALTERNATIVOS (perfilA+iid vs perfilB+zigzag;
      efeito medido na calibracao: -0.049, sinal FIXO '-'), B=1000 —
      gate: regra detecta >= 7/10 com sinal coerente
  S6  INCIDENCIA (gate central do r5): nos trials de S4+S5 —
      discordancia do primario <= 0.10; incidencia do primario e do
      bloco8-BCa (comparacao; prototipo: ~0.03 vs ~0.5-1.0)
  S3  ordenacao saltos + boxdim seno<ruido                  — n=512
  DISJ interseccao grade x (r2 U r3 U r4) = vazia

INFERENCIA: CI primario = PERCENTIL do bootstrap estratificado (95,
90/TOST, Bonferroni 0.01 H_D2 / 0.0167 H_D1 via quantis); parceiro =
BCa estratificado (concordancia); diagnostico = BCa+bloco8 nas 9
chaves; jackknife delete-one pooled (= delete-one dentro do estrato,
aceleracao BCa aproximada — declarada). MDE80=2.8016*SE.
B=1000 (S4:600), seed_boot=SEED+6=20261125.

SAIDAS: gk_proof_fractal_v5_series.csv (coleta, SEM tempo, checkpoint
        atomico por instancia + --resume — o crash CaDiCaL do r4
        continua possivel)
        gk_proof_fractal_v5_contrasts.csv (135 + diagnostico bloco8)
        gk_proof_fractal_v5.json (coleta; R6 -> series)
        gk_proof_fractal_v5_analysis.json (analise; R6 -> contrasts)
Uso:   python -u gk_proof_fractal_v5.py [--selftest-only | --analyze-only
       | --resume]
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
from gk_proof_fractal_v2 import gen_cadeia, gen_tau_tiny, variants_of
from gk_proof_fractal_v2_r2 import bca_ci, block_idx, pct_ci, selftest_bca
from gk_proof_fractal_v3 import METRICS
from gk_minref import minref

N_BOOT = 1000
SEED_BOOT = SEED + 6           # 20261125 — declarado
PRIMARY = "estratificado"      # metodo escolhido na calibracao S6
MARGIN_PRIMARY = 0.05          # A1: precisao r4 (1,645*SE max = 0.040)
MARGINS = (0.05, 0.03, 0.08)
MDE_TARGET = 0.06              # H_D4
FAMS = ["implication", "cadeia", "tau_tiny"]

SRC_PREV = [Path("gk_proof_fractal_v2_series.csv"),
            Path("gk_proof_fractal_v3_series.csv"),
            Path("gk_proof_fractal_v4_series.csv")]
OUT_SERIES = Path("gk_proof_fractal_v5_series.csv")
OUT_CONTRASTS = Path("gk_proof_fractal_v5_contrasts.csv")
OUT_JSON = Path("gk_proof_fractal_v5.json")
OUT_ANALYSIS = Path("gk_proof_fractal_v5_analysis.json")

GRID = {
    "implication": [(m, s) for m in range(3, 7) for s in range(128, 256)],
    "cadeia":      [(k, s) for k in range(3, 7) for s in range(128, 256)],
    "tau_tiny":    [(0, s) for s in range(512, 1024)],
}
GENS = {"implication": gen_implication, "cadeia": gen_cadeia,
        "tau_tiny": gen_tau_tiny}

H_D1 = [   # saltos PRIMARIO (r4 H_C2 3/3 — replicacao com metodo novo)
    ("minref:implication-tau_tiny:saltos:raw", "sep", +1),
    ("drat:implication-cadeia:saltos:raw", "sep", +1),
    ("fonte:cadeia:saltos:raw", "sep", +1),
]
H_D2 = [   # boxdim SECUNDARIO (H_C1 r4 — serie nova, metodo novo)
    ("minref:implication-tau_tiny:boxdim:raw", "sep", +1),
    ("minref:cadeia-tau_tiny:boxdim:raw", "sep", +1),
    ("minref:implication-cadeia:boxdim:raw", "eq", 0),
    ("drat:implication-cadeia:boxdim:raw", "sep", -1),
    ("fonte:tau_tiny:boxdim:raw", "sep", -1),
    ("fonte:cadeia:boxdim:raw", "sep", -1),
]
PRE_KEYS = [k for k, _, _ in H_D1] + [k for k, _, _ in H_D2]  # 9 chaves


# ---------------- estratos + reamostragem ----------------

def runs_of(pts):
    """Tamanhos dos estratos (runs de param consecutivo) da serie.
    int() obrigatorio: linhas do CSV chegam como string e linhas
    frescas como int — mistura quebrava o run (mesma familia de bug do
    r3: bool x str)."""
    runs, cur, n = [], None, 0
    for r in pts:
        p = int(r["param"])
        if p == cur:
            n += 1
        else:
            if cur is not None:
                runs.append(n)
            cur, n = p, 1
    if cur is not None:
        runs.append(n)
    return runs


def strat_idx(runs, rng, n_pts=None):
    """Reamostragem IID DENTRO de cada estrato de parametro — o DGP real
    (instancias independentes por seed; macroestrutura preservada)."""
    if n_pts is not None and sum(runs) != n_pts:
        # variante relinc: 1º estrato perde 1 ponto (aprox. declarada)
        runs = list(runs)
        runs[0] -= 1
        if runs[0] < 1 or sum(runs) != n_pts:
            runs = [n_pts]                # fallback: estrato unico
    idx, start = [], 0
    for n in runs:
        idx.extend(start + rng.randrange(n) for _ in range(n))
        start += n
    return idx


# ---------------- selftests / calibracao ----------------

def _synth_family(rng, profile, kind, per=128):
    out = []
    for p in range(4):
        for s in range(per):
            if kind == "iid":
                v = rng.gauss(0, 1)
            else:  # zig
                v = (1.0 if s % 2 == 0 else -1.0) + 0.3 * rng.gauss(0, 1)
            out.append(profile[p] + v)
    return out


PROF_A = [5.0, 6.0, 6.5, 7.0]
PROF_B = [5.0, 7.0, 9.0, 11.0]
RUNS_SYNTH = [128] * 4


def _block_d(n, rng, d):
    """Bloco de tamanho arbitrario (block_idx do r2 fixa BLOCK=8)."""
    out = []
    while len(out) < n:
        s = rng.randrange(0, max(1, n - d + 1))
        out.extend(range(s, min(n, s + d)))
    return out[:n]


def _pipeline_calib(method, a, b, rng, n_boot, runs_a, runs_b):
    obs = boxdim_curve(a) - boxdim_curve(b)
    boots = []
    for _ in range(n_boot):
        if method == "estrat":
            ia = strat_idx(runs_a, rng, len(a))
            ib = strat_idx(runs_b, rng, len(b))
        else:
            d = 8 if method == "bloco8" else 16
            ia, ib = _block_d(len(a), rng, d), _block_d(len(b), rng, d)
        boots.append(boxdim_curve([a[i] for i in ia])
                     - boxdim_curve([b[i] for i in ib]))
    jack = []
    for i in range(len(a)):
        jack.append(boxdim_curve(a[:i] + a[i + 1:]) - boxdim_curve(b))
    for i in range(len(b)):
        jack.append(boxdim_curve(a) - boxdim_curve(b[:i] + b[i + 1:]))
    lo, hi, info = bca_ci(obs, boots, jack, alpha=0.05)   # parceiro
    plo, phi = pct_ci(boots)                              # PRIMARIO
    if plo is None:
        return None
    out_pct = obs < plo or obs > phi
    out_bca = lo is not None and (obs < lo or obs > hi)
    excl_pct = plo > 0 or phi < 0
    excl_bca = lo is not None and (lo > 0 or hi < 0)
    same_dir = (excl_pct and excl_bca and ((plo > 0) == (lo > 0))
                and ((obs > 0) == (plo > 0)))
    both_inc = (not excl_pct) and (lo is not None and not excl_bca)
    concord = (not out_pct) or same_dir or both_inc
    # veredito direcional pela regra de 2 niveis (espelho do run real)
    if not out_pct:
        verdict = "EXCLUI" if excl_pct else "INCONCL"
    elif concord and same_dir:
        verdict = "EXCLUI_FLAG"
    elif concord and both_inc:
        verdict = "INCONCL_FLAG"
    else:
        verdict = "DISCORDANTE"
    return {"obs": obs, "excl_pct": excl_pct, "excl_bca": excl_bca,
            "outside_pct": out_pct, "outside_bca": out_bca,
            "verdict": verdict, "z0_pct": None, "z0_bca":
            info.get("z0") if info else None,
            "sd_boot": (sum((x - sum(boots) / len(boots)) ** 2
                            for x in boots) / (len(boots) - 1)) ** 0.5}


def validate_metrics_n512():
    rng = random.Random(SEED + 9)
    wn = [rng.gauss(0, 1) for _ in range(512)]
    ramp = [i / 511.0 for i in range(512)]
    sine = [math.sin(2 * math.pi * i / 16) for i in range(512)]
    from gk_proof_fractal_v3 import boxdim_rank, taxa_saltos
    inv_err = abs(boxdim_rank(wn) - boxdim_rank([math.exp(v) for v in wn]))
    ok = (taxa_saltos(wn) > taxa_saltos(ramp)
          and taxa_saltos(wn) > taxa_saltos(sine)
          and boxdim_curve(sine) < boxdim_curve(wn))
    return {"status": "OK" if (inv_err < 1e-9 and ok) else "FALHA",
            "inv_err": inv_err}


def calibrate():
    """S4 (tipo-I: cru e pela regra), S5 (poder) e S6 (incidencia) em
    dados sinteticos COM GRADE. Selecao do metodo: PRIMARIO = percentil
    estratificado (tipo-I calibrado); parceiro da regra = BCa
    estratificado; comparacao = bloco8 (metodo do r4)."""
    out = {}
    # S4 tipo-I: 40 pares nulos (mesmo perfil, iid)
    rng = random.Random(SEED_BOOT)
    T = 40
    ti_pct = ti_rule = ti_bca = 0
    for _ in range(T):
        a = _synth_family(rng, PROF_A, "iid")
        b = _synth_family(rng, PROF_A, "iid")
        r = _pipeline_calib("estrat", a, b, rng, 600,
                            RUNS_SYNTH, RUNS_SYNTH)
        if not r:
            continue
        ti_pct += 1 if r["excl_pct"] else 0
        ti_rule += 1 if r["verdict"] in ("EXCLUI", "EXCLUI_FLAG") else 0
        ti_bca += 1 if r["excl_bca"] else 0
    out["S4_tipo1"] = {
        "n": T, "percentil_cru": ti_pct, "regra_2niveis": ti_rule,
        "bca_cru": ti_bca,
        "taxa_pct": ti_pct / T, "taxa_regra": ti_rule / T,
        "taxa_bca": ti_bca / T,
        "gate_ok": (ti_pct / T <= 0.15) and (ti_rule / T <= 0.15),
        "nota": ("percentil deve calibrar (~0.05); BCa cru reportado "
                 "(prototipo: 0.20 — por isso NAO e primario); regra "
                 "de 2 niveis nao pode inflacionar a taxa"),
    }
    # S5 poder (efeito -0.049 medido, sinal '-') + S6 incidencia
    P = 10
    pw_rule = 0
    out_n_estrat = disc_estrat = 0
    b8_out = b8_n = 0
    z0s = []
    for d in range(P):
        rng_a = random.Random(SEED_BOOT * 100 + d)
        a = _synth_family(rng_a, PROF_A, "iid")
        b = _synth_family(rng_a, PROF_B, "zig")
        r = _pipeline_calib("estrat", a, b, rng_a, 1000,
                            RUNS_SYNTH, RUNS_SYNTH)
        if r:
            ok = r["verdict"] in ("EXCLUI", "EXCLUI_FLAG") \
                and r["obs"] < 0
            pw_rule += 1 if ok else 0
            out_n_estrat += 1 if r["outside_pct"] else 0
            disc_estrat += 1 if r["verdict"] == "DISCORDANTE" else 0
            z0s.append(r["z0_bca"])
        r8 = _pipeline_calib("bloco8", a, b, rng_a, 600,
                             RUNS_SYNTH, RUNS_SYNTH)
        if r8:
            b8_n += 1
            b8_out += 1 if r8["outside_bca"] else 0
    # incidencia do estratificado TAMBEM nos nulos + bloco8 comparativo
    rng2 = random.Random(SEED_BOOT + 1)
    for _ in range(T):
        a = _synth_family(rng2, PROF_A, "iid")
        b = _synth_family(rng2, PROF_A, "iid")
        r = _pipeline_calib("estrat", a, b, rng2, 600,
                            RUNS_SYNTH, RUNS_SYNTH)
        if r:
            out_n_estrat += 1 if r["outside_pct"] else 0
            disc_estrat += 1 if r["verdict"] == "DISCORDANTE" else 0
        r8 = _pipeline_calib("bloco8", a, b, rng2, 600,
                             RUNS_SYNTH, RUNS_SYNTH)
        if r8:
            b8_n += 1
            b8_out += 1 if r8["outside_bca"] else 0
    inc_estrat = out_n_estrat / (T + P)
    inc_bca8 = b8_out / b8_n if b8_n else None
    out["S5_poder"] = {"n": P, "regra_detectou": pw_rule,
                       "gate_ok": pw_rule >= 7,
                       "z0_bca_range": [min(z0s), max(z0s)] if z0s else None,
                       "nota": ("construct perfilA+iid vs perfilB+zig; "
                                "efeito -0.049 medido; deteccao = regra "
                                "da direita com sinal negativo")}
    out["S6_incidencia"] = {
        "percentil_estratificado": {
            "incidencia": inc_estrat,
            "discordancia": disc_estrat / (T + P),
            "gate_ok": (disc_estrat / (T + P)) <= 0.10},
        "bloco8_bca_comparacao": {"incidencia": inc_bca8,
                                  "n": b8_n},
        "nota": ("alvo: discordancia do primario <= 0.10 (prototipo: "
                 "percentil ~0.03, bloco8-BCa ~0.5-1.0); o primario "
                 "e o percentil estratificado — calibrado no S4"),
    }
    out["status"] = ("OK" if (out["S4_tipo1"]["gate_ok"]
                              and out["S5_poder"]["gate_ok"]
                              and out["S6_incidencia"]
                              ["percentil_estratificado"]["gate_ok"])
                     else "FALHA")
    return out


# ---------------- checagens obrigatorias ----------------

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
            "n_prev": len(used), "n_r5": len(mine), "fontes": n_src,
            "interseccao": sorted(inter)[:10]}


def selftest_bca_scipy():
    try:
        from scipy import stats as sstats
    except ImportError:
        return {"status": "scipy ausente — pulado"}
    import random as _r
    rng = _r.Random(SEED + 7)
    x = [rng.gauss(0, 1) + (i % 5) * 0.3 for i in range(64)]

    def stat(v):
        m = sum(v) / len(v)
        return sum((t - m) ** 2 for t in v) / len(v)
    rng2 = _r.Random(SEED + 8)
    obs = stat(x)
    boots = [stat([x[i] for i in [rng2.randrange(64)
                                  for _ in range(64)]])
             for _ in range(20000)]
    jack = [stat(x[:i] + x[i + 1:]) for i in range(64)]
    lo, hi, _ = bca_ci(obs, boots, jack)
    res = sstats.bootstrap((x,), stat, method="BCa", n_resamples=20000,
                           random_state=SEED + 8)
    diff = max(abs(lo - res.confidence_interval.low),
               abs(hi - res.confidence_interval.high))
    return {"status": "OK" if diff < 0.05 else "DIVERGENTE",
            "max_diff": round(diff, 5)}


# ---------------- coleta (checkpoint + resume — v4) ----------------

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
            write_series(rows)          # checkpoint atomico por instancia
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


def build_series(rows):
    series, strata = {}, {}
    for fam in FAMS:
        pts = [r for r in rows if r["family"] == fam
               and str(r["minref_censored"]) == "False"
               and r["sat_drat"] == "UNSAT"
               and str(r["proof_drat"]) not in ("", "None")]
        pts.sort(key=lambda r: (int(r["param"]), int(r["seed"])))
        runs = runs_of(pts)
        for sysname in ("minref", "drat"):
            series[(fam, sysname)] = [float(r["minref" if sysname
                                         == "minref" else "proof_drat"])
                                      for r in pts]
            strata[(fam, sysname)] = runs
    return series, strata, len(rows)


# ---------------- contrastes: estratificado primario ----------------

def _jack_pooled(a, b, fn, paired):
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


def contrast(a, b, fn, rng, paired, runs_a, runs_b, allow_eq=True,
             with_block8=False, n_boot=N_BOOT):
    """Contraste com bootstrap ESTRATIFICADO. PRIMARIO = percentil
    (calibrado no S4: tipo-I 0.025 vs BCa 0.20); PARCEIRO da regra de
    2 niveis = BCa estratificado; diagnostico = BCa+bloco8 (metodo r4)
    nas chaves pre-registradas."""
    if len(a) != len(b) or len(a) < 16:
        return None
    obs_a, obs_b = fn(a), fn(b)
    obs = obs_a - obs_b
    if math.isnan(obs):
        return None
    boots, vas, vbs = [], [], []
    for _ in range(n_boot):
        if paired:
            idx = strat_idx(runs_a, rng, len(a))
            va, vb = fn([a[i] for i in idx]), fn([b[i] for i in idx])
        else:
            ia = strat_idx(runs_a, rng, len(a))
            ib = strat_idx(runs_b, rng, len(b))
            va, vb = fn([a[i] for i in ia]), fn([b[i] for i in ib])
        if va is not None and vb is not None \
                and not math.isnan(va) and not math.isnan(vb):
            boots.append(va - vb)
            vas.append(va)
            vbs.append(vb)
    if len(boots) < 200:
        return None
    jack = _jack_pooled(a, b, fn, paired)
    # --- PRIMARIO: quantis do percentil estratificado ---
    sb = sorted(boots)

    def q(p):
        return sb[min(len(sb) - 1, max(0, int(round(p * (len(sb) - 1)))))]
    plo, phi = q(0.025), q(0.975)
    p90lo, p90hi = q(0.05), q(0.95)
    pb5lo, pb5hi = q(0.005), q(0.995)          # IC99% (bonf 0.01)
    pb3lo, pb3hi = q(0.00835), q(0.99165)      # IC98.33% (bonf .0167)
    # --- PARCEIRO: BCa estratificado (95 e 90) ---
    lo, hi, info = bca_ci(obs, boots, jack, alpha=0.05)
    lo90b, hi90b, _ = bca_ci(obs, boots, jack, alpha=0.10)
    if lo is None:
        return None
    m = sum(boots) / len(boots)
    se = (sum((x - m) ** 2 for x in boots) / (len(boots) - 1)) ** 0.5
    bias = m - obs
    out = {
        "point": obs,
        "pct_lo": plo, "pct_hi": phi,               # PRIMARIO
        "pct90_lo": p90lo, "pct90_hi": p90hi,
        "pct_bonf5_lo": pb5lo, "pct_bonf5_hi": pb5hi,
        "pct_bonf3_lo": pb3lo, "pct_bonf3_hi": pb3hi,
        "bca_lo": lo, "bca_hi": hi,                 # PARCEIRO (regra)
        "bca90_lo": lo90b, "bca90_hi": hi90b,
        "se_boot": se, "mde80": 2.801585 * se,
        "z0": info.get("z0"), "aceleracao": info.get("aceleracao"),
        "boot_bias": bias, "bias_over_se": bias / se if se else None,
        "point_outside": obs < plo or obs > phi,
        "point_outside_bca": obs < lo or obs > hi,
        "excludes0": plo > 0 or phi < 0,
        "excludes0_bca": lo > 0 or hi < 0,
        "excludes0_bonf5": pb5lo > 0 or pb5hi < 0,
        "excludes0_bonf3": pb3lo > 0 or pb3hi < 0,
        "n_boot": len(boots), "n_jack": len(jack),
    }
    # --- regra de 2 niveis (r5-ii): concordancia entre os DOIS metodos ---
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
    # diagnostico: BCa+bloco8 (metodo do r4) nas chaves pre-registradas
    if with_block8:
        boots8 = []
        for _ in range(n_boot):
            if paired:
                idx = _block_d(len(a), rng, 8)
                va, vb = fn([a[i] for i in idx]), fn([b[i] for i in idx])
            else:
                ia = _block_d(len(a), rng, 8)
                ib = _block_d(len(b), rng, 8)
                va, vb = fn([a[i] for i in ia]), fn([b[i] for i in ib])
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
    # veredito generico (2 niveis) p/ relatorio de todos os contrastes
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


# ---------------- regras exaustivas (2 niveis) ----------------

def classify_test(c, kind, dirn, metric):
    """Regra de 2 niveis: PRIMARIO = percentil estratificado; PARCEIRO =
    BCa estratificado. Ponto dentro -> veredito normal; ponto fora ->
    concordancia entre os DOIS metodos decide (conta com flag) ou
    discordancia (nao conta em nenhuma direcao)."""
    if c is None:
        return "SEM_DADOS"
    bonf = (c["excludes0_bonf5"] if metric == "boxdim"
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
    # direcional
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


def classify_global(results):
    n = len(results)
    vals = list(results.values())
    if any(v.startswith("CONTRADITA") for v in vals):
        return "REFUTADA_CONTRADITA"
    countable = [v for v in vals if v.startswith("OK")
                 or v.startswith("FALHA")]
    n_ok = sum(1 for v in countable if v.startswith("OK"))
    n_flag = sum(1 for v in countable if v.endswith("_FLAG"))
    n_incoh = sum(1 for v in vals if v == "INCOERENTE_DISCORDANTE")
    n_sem = sum(1 for v in vals if v == "SEM_DADOS")
    if len(countable) < math.ceil(0.6 * n):
        return (f"INDETERMINADO ({len(countable)}/{n} contaveis; "
                f"{n_incoh} discordantes, {n_sem} sem dados)")
    base = None
    if n_ok == len(countable):
        base = "CONFIRMADA"
    elif n_ok == 0:
        base = "REFUTADA"
    else:
        base = f"PARCIAL ({n_ok}/{len(countable)} contaveis)"
    extra = []
    if n_flag:
        extra.append(f"{n_flag} concordantes-com-flag")
    if n_incoh:
        extra.append(f"{n_incoh} discordantes")
    return base + (f" [{'; '.join(extra)}]" if extra else "")


# ---------------- analise ----------------

def analyze(rows):
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
            src = sysname
            a0, b0 = series.get((fa, src), []), series.get((fb, src), [])
            ra, rb = strata.get((fa, src), []), strata.get((fb, src), [])
        for vname in ("raw", "log1p", "relinc"):
            a = variants_of(a0)[vname]
            b = variants_of(b0)[vname]
            for mname, fn in METRICS.items():
                key = f"{label}:{mname}:{vname}"
                c = contrast(a, b, fn, rng, paired, ra, rb,
                             allow_eq=(mname == "boxdim"),
                             with_block8=(key in PRE_KEYS))
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

    hyp = {"H_D1_saltos_primario": eval_hyp(H_D1, "H_D1"),
           "H_D2_boxdim_secundario": eval_hyp(H_D2, "H_D2")}

    # ---- H_D3 incidencia em dados REAIS ----
    pre = {k: contrasts[k] for k in PRE_KEYS if k in contrasts}
    allc = list(contrasts.items())
    inc_strat = sum(1 for _, c in allc if c["point_outside"])
    disc_strat = sum(1 for _, c in allc if c["discordante"])
    block8_out = [k for k, c in pre if c.get("block8_outside")]
    block8_disc = [k for k, c in pre if c.get("block8_outside")
                   and not c["concordante"]]
    hyp["H_D3_incidencia"] = {
        "metodo_primario": "estratificado",
        "incidencia_total": f"{inc_strat}/{len(allc)}",
        "discordantes_total": f"{disc_strat}/{len(allc)}",
        "alvo_discordante_le": 0.10,
        "gate_real_ok": (disc_strat / len(allc)) <= 0.10
        if allc else None,
        "pre_registradas_bloco8": {
            "fora_do_IC": len(block8_out), "n": len(pre),
            "discordantes": block8_disc,
            "nota": "metodo do r4 nas mesmas 9 chaves (head-to-head)"},
        "veredito": None,
    }
    hyp["H_D3_incidencia"]["veredito"] = (
        "CONFIRMADA (discordante <=10% em dados reais)"
        if hyp["H_D3_incidencia"]["gate_real_ok"]
        else "REFUTADA (discordante >10%)")

    # ---- H_D4 MDE ----
    d2_keys = [k for k, _, _ in H_D2]
    mdes = {k: contrasts[k]["mde80"] for k in d2_keys
            if k in contrasts and contrasts[k].get("mde80")}
    n_ok_mde = sum(1 for v in mdes.values() if v < MDE_TARGET)
    hyp["H_D4_alvo_MDE"] = {
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
    }
    for _, c in allc:
        v = c["veredito"]
        hyp["_diagnostico"]["vereditos"][v] = \
            hyp["_diagnostico"]["vereditos"].get(v, 0) + 1

    print("\n--- hipoteses pre-registradas ---")
    for hname in ("H_D1_saltos_primario", "H_D2_boxdim_secundario"):
        h = hyp[hname]
        print(f"  {hname}: {h['veredito']}")
        for k, v in h["testes"].items():
            d = v["dado"]
            extra = ""
            if d:
                extra = (f"point={d['point']:+.4f} "
                         f"CI=[{d['bca_lo']:+.4f},{d['bca_hi']:+.4f}] "
                         f"pct=[{d['pct_lo']:+.4f},{d['pct_hi']:+.4f}] "
                         f"z0={d['z0']:+.2f} MDE={d['mde80']:.4f}"
                         + (" | bloco8_fora" if d.get("block8_outside")
                            else ""))
            print(f"    {k}: {v['resultado']} {extra}")
    h3 = hyp["H_D3_incidencia"]
    print(f"\n  H_D3: {h3['veredito']} — estratificado discordantes "
          f"{h3['discordantes_total']}; bloco8 pre-reg fora="
          f"{h3['pre_registradas_bloco8']['fora_do_IC']}/9")
    h4 = hyp["H_D4_alvo_MDE"]
    print(f"  H_D4: {h4['veredito']} {h4['valores']}")
    dg = hyp["_diagnostico"]
    print(f"  diagnosticos: z0 extremos={dg['z0_extremos']}/"
          f"{dg['n_contrastes']} degenerados={len(dg['degenerados'])} "
          f"vereditos={dg['vereditos']}")
    print(f"analise: {time.time()-t0:.0f}s")
    return contrasts, hyp, n_rows


# ---------------- escrita ----------------

def _sha(p):
    return hashlib.sha256(
        p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def write_contrasts(contrasts):
    cols = ["key", "veredito", "point",
            "pct_lo", "pct_hi", "pct90_lo", "pct90_hi",
            "pct_bonf5_lo", "pct_bonf5_hi",
            "pct_bonf3_lo", "pct_bonf3_hi",
            "bca_lo", "bca_hi", "bca90_lo", "bca90_hi",
            "excludes0", "excludes0_bca", "excludes0_bonf5",
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
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    t0 = time.time()
    print("=" * 70)
    print("D4' v5 (r5) — saltos primario + bootstrap estratificado "
          "+ regra de 2 niveis")
    print("=" * 70)

    s1 = selftest_bca_scipy()
    s2 = validate_metrics_n512()
    cal = calibrate()
    disj = check_disjoint()
    print(f"\n[S1] BCa vs scipy: {s1['status']} "
          f"(diff={s1.get('max_diff')})")
    print(f"[S2] metricas n=512: {s2['status']} inv_err={s2['inv_err']:.1e}")
    t4 = cal["S4_tipo1"]
    print(f"[S4] tipo-I: pct_cru={t4['percentil_cru']}/{t4['n']}"
          f"={t4['taxa_pct']:.3f} regra={t4['regra_2niveis']}/{t4['n']}"
          f"={t4['taxa_regra']:.3f} (gate<=0.15) | bca_cru="
          f"{t4['bca_cru']}/{t4['n']}={t4['taxa_bca']:.3f} (reportado) "
          f"{'OK' if t4['gate_ok'] else 'FALHA'}")
    print(f"[S5] poder (regra, sinal '-'): "
          f"{cal['S5_poder']['regra_detectou']}/"
          f"{cal['S5_poder']['n']} (gate>=7) "
          f"{'OK' if cal['S5_poder']['gate_ok'] else 'FALHA'}")
    s6 = cal["S6_incidencia"]
    print(f"[S6] incidencia: pct_estrat="
          f"{s6['percentil_estratificado']['incidencia']:.3f} "
          f"discordancia="
          f"{s6['percentil_estratificado']['discordancia']:.3f} "
          f"(gate<=0.10) | bloco8_BCA="
          f"{s6['bloco8_bca_comparacao']['incidencia']:.3f} "
          f"{'OK' if s6['percentil_estratificado']['gate_ok'] else 'FALHA'}")
    print(f"[DISJ] r2+r3+r4 vs r5: {disj['status']} "
          f"interseccao={disj.get('interseccao')}")
    ok = (s1["status"] in ("OK", "scipy ausente — pulado")
          and s2["status"] == "OK" and cal["status"] == "OK"
          and disj["status"] in ("OK",
                                 "AVISO: CSVs anteriores ausentes — pulado"))
    if not ok:
        print(f"[ABORTA] selftests/calibracao: {disj['status']}")
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

    contrasts, hyp, n_rows = analyze(rows)
    write_contrasts(contrasts)

    meta = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat()
                         .replace("+00:00", "Z"),
        "mode": mode,
        "seed": SEED, "seed_boot": SEED_BOOT, "n_boot": N_BOOT,
        "metodo_primario": ("percentil BOOTSTRAP ESTRATIFICADO por "
                            "parametro (iid dentro do estrato) — "
                            "selecionado na calibracao S4 (tipo-I 0.025 "
                            "vs BCa 0.20); parceiro da regra = BCa "
                            "estratificado; diagnostico = BCa+bloco8 "
                            "(metodo r4) nas 9 chaves pre-registradas"),
        "regra_2_niveis": ("ponto fora do IC primario -> CONCORDANTE "
                           "(ambos os metodos concordam: excluem mesmo "
                           "sinal coerente com o ponto, ou ambos "
                           "incluem 0) = conta com flag; DISCORDANTE = "
                           "nao conta em nenhuma direcao (r5-ii)"),
        "margens_boxdim": {"primaria": MARGIN_PRIMARY,
                           "sensibilidade": list(MARGINS[1:])},
        "ancora_margem": ("precisao r4: maior meia-largura IC90 "
                          "percentilica estimada (1,645*SE) = 0.040"),
        "grid": {k: f"{len(v)} pontos (seeds novos vs r2+r3+r4)"
                 for k, v in GRID.items()},
        "runtime_s": round(time.time() - t0, 1),
        "caveats": [
            ("Pre-registro: hipoteses/margens/regras/metodo fixados "
             "neste codigo e no doc 32_ ANTES do run."),
            ("Dados disjuntos de r2, r3 e r4 (DISJ aborta)."),
            ("Serie relinc: 1o estrato perde 1 ponto (aprox. "
             "declarada); confirmatorios sao raw."),
            ("Jackknife delete-one pooled = delete-one dentro do "
             "estrato (aceleracao BCa aproximada, declarada)."),
            ("Checkpoint atomico + --resume (crash CaDiCaL do r4 "
             "continua possivel — limitação de plataforma)."),
            ("N1+N2; sem N4; H_C2 (EF) deferido; tau k↑ aberta."),
        ],
    }
    payload_series = {
        "metadata": {**meta,
                     "data_source": "gk_proof_fractal_v5.py (r5 coleta)",
                     "instances": {"rows": n_rows},
                     "selftests": {"S1_bca_scipy": s1, "S2_metricas": s2,
                                   "calibracao": cal, "DISJ": disj},
                     "csv": OUT_SERIES.name,
                     "csv_sha256": _sha(OUT_SERIES),
                     "sha_note": "sha256 bytes normalizados CRLF->LF"},
    }
    OUT_JSON.write_text(json.dumps(payload_series, indent=2,
                                   ensure_ascii=False), encoding="utf-8")
    payload_an = {
        "metadata": {**meta,
                     "data_source": ("gk_proof_fractal_v5.py (r5 "
                                     "analise — estratificado + 2 "
                                     "niveis)"),
                     "input_series_csv": OUT_SERIES.name,
                     "input_series_sha256": _sha(OUT_SERIES),
                     "csv": OUT_CONTRASTS.name,
                     "csv_sha256": _sha(OUT_CONTRASTS),
                     "sha_note": "sha256 bytes normalizados CRLF->LF"},
        "pre_registro": {
            "H_D1": [{"key": k, "tipo": t, "sinal": d}
                     for k, t, d in H_D1],
            "H_D2": [{"key": k, "tipo": t, "sinal": d}
                     for k, t, d in H_D2],
            "H_D3": "incidencia real: estratificado <=10% discordante",
            "H_D4": "MDE80 < 0.06 nos 6 boxdim",
            "regras": "2 niveis (concordante/discordante) — ver "
                      "docstring do script (exaustivas)",
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

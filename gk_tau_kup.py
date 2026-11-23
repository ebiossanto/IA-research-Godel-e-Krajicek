#!/usr/bin/env python3
"""
gk_tau_kup.py — τ k↑: estendendo o minref para n>6 (pendencia
original da linha D4', ONDE_ESTAMOS s5-D4).

=====================================================================
PRE-REGISTRO (fixado ANTES de qualquer execucao com dados novos; o
commit deste codigo e do doc 34_ precede o run — prioridade temporal
C1): ver 34_TAU_KUP_MINREF.md s1.
=====================================================================

FRONTEIRA EMPIRICA (sondas 21-22/11/2026, seeds 1700+ — NUNCA os do
experimento; nao espiam valores):
  k=2 (n=5):  fecho<=211, pares~2k     -> exato SEMPRE (t_cap folgado)
  k=3 (n=7):  fecho=2059 (37s), DP=6s, d(vazia)=3, pares=766k
              -> exato ate minref=7 com max_aux=6M (REF_7 construido
                 e resolvido:173s); >=8 censurado
  k=4 (n=9):  fecho=3551 (124s), DP=19s, d(vazia)=3, pares=2.2M
              -> exato ate minref=5 com max_aux=8M (REF_5 construido
                 e UNSAT); >=6 censurado (REF_6 exigiria ~13M auxs —
                 memoria impraticavel; declarado)
  k>=5:       parede do fecho (nao testado; projetado inviavel)

ARGUMENTO DE CORRETEZA (pools de profundidade):
  d(C) =1 se C em gamma; senao min_{pares} max(d(c1),d(c2))+1.
  Toda linha j de uma refutacao com <= t linhas tem d <= j (inducao:
  folha d=1; resolvente de linhas <j tem d<=max+1<=j) => d(vazia)<=t
  (LIMITE INFERIOR, testado) e todo pool {d<=t} contem as linhas
  necessarias => REF_t sobre pool restrito e' EQUIVALENTE ao REF_t
  sobre o fecho cheio, com ORDENS DE GRANDEZA menos auxiliares.
  Pares deduplicados (nao-ordenados) — o auxiliar a_{j,C,p} e
  simetrico nos pais (metade dos auxs).

HIPOTESES (declaradas aqui, ANTES do run):
  H_t1 VIABILIDADE: em k=3, >=16/32 seeds (>=50%) tem minref EXATO
    com max_aux=6M. CONFIRMADA >=16; REFUTADA <16. (Consequencia
    pre-declarada: pontos censurados sao EXCLUIDOS da serie — regra
    existente — e o censuramento por nivel e' reportado.)
  H_t2 DINAMICA (crescimento com k): medias de minref exato crescem
    com o nivel — 2 contrastes adjacentes com bootstrap (percentil
    PRIMARIO + BCa parceiro + regra de 2 niveis + Bonferroni 0.05/2):
      (i)  media(k=3) - media(k=2) > 0
      (ii) media(k=4) - media(k=3) > 0
    CONFIRMADA iff 2/2 OK; PARCIAL 1/2; REFUTADA 0/2; CONTRADITA se
    sinal oposto em qualquer. CAVEAT (pre-declarado): censuras removem
    instancias (geralmente as de minref MAIOR) -> medias do nivel
    subestimam; uma falha pode ser artefato de censura (reportar
    censuras por nivel junto).
  ASSERT (por instancia): minref_exato >= d(vazia) — violacao = BUG
    (aborta com relatorio; e' teorema, nao hipotese).

METRICAS: descritivas (SEM hipotese — comparacoes cross-n de boxdim
sao confundidas, lição r4): hurst_rs, higuchi_D, boxdim, saltos,
boxdim_rank sobre a serie ordinal (k,seed) dos minref exatos e da
serie DRAT dos MESMOS pontos; CI percentil estratificado (B=1000,
estratos = niveis de k) como caracterizacao.

COLETA: por instancia — gen_tau(depth=1, seed, k, w=k+1) [nvars =
k + min(w, 2k) => k=2:5, k=3:7, k=4:9] + solve (UNSAT exigido) +
minref_deep(max_aux por nivel: {2:400k, 3:6M, 4:8M}, with_info) +
solve_drat. CHECKPOINT atomico por instancia + --resume (crash
CaDiCaL continua possivel). CSV SEM coluna de tempo.

GRADE: familia tau_tiny, param=k, k in {2,3,4}, seeds 1536..1667
(32 por nivel,96 total) — DISJ de r2..r6 (aborta se intersectar).

SELFTESTS (aborta se falhar):
  S1  BCa vs scipy (iid) — valida bca_ci
  S2  metricas n=96 (invariancia rank + ordenacoes)
  S3  maquina de contraste de medias: tipo-I (40 pares nulos n=32,
      gate <=0.15) + poder (10 pares com deslocamento +0.5 sigma,
      gate >=7/10) + regra de 2 niveis exercitada
  S4  DISJ: grade x (r2..r6) = vazia
  S5  SMOKE DE ANALISE (licenca r5): analyze() com contrast() STUBADO
      sobre linhas fabricadas — exercita H_t1/H_t2/metricas/assert
  ASSERT por instancia (minref >= lb) durante a coleta

INFERENCIA (contrastes de medias): percentil (B=1000) PRIMARIO +
BCa parceiro (bca_ci) + jackknife delete-one pooled + Bonferroni
0.05/2 (quantis 0.0125/0.998... = 0.0125/0.9875) + regra de 2 niveis
(identica a r5/r6) + MDE80=2.8016*SE.

SAIDAS: gk_tau_kup_series.csv + gk_tau_kup.json (R6 -> series)
Uso:   python -u gk_tau_kup.py [--selftest-only | --analyze-only |
       --resume]
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

import gk_proof_fractal as gpf
from gk_proof_fractal import (SEED, boxdim_curve, higuchi_D, hurst_rs,
                              solve_drat)
from gk_proof_fractal_v3 import METRICS, boxdim_rank, taxa_saltos
from gk_minref import minref_deep
from gk_proof_fractal_v2_r2 import bca_ci, pct_ci
from gk_proof_fractal_v5 import runs_of as _runs_of_rows, \
    selftest_bca_scipy

# ---------------- constantes ----------------

N_BOOT = 1000
SEED_BOOT = SEED + 8              # 20261127 — declarado
KS = (2, 3, 4)
SEEDS = range(1536, 1668)         # 32 por nivel (DISJ de r2..r6)
MAX_AUX_BY_K = {2: 400_000, 3: 6_000_000, 4: 8_000_000}
FAM = "tau_tiny"

SRC_PREV = [Path(f"gk_proof_fractal_v{i}_series.csv")
            for i in (2, 3, 4, 5, 6)]
OUT_SERIES = Path("gk_tau_kup_series.csv")
OUT_JSON = Path("gk_tau_kup.json")

GRID = {k: [(k, s) for s in SEEDS] for k in KS}


def gen_tau_k(k, seed):
    """tau(g)_b com depth=1, w=k+1 -> nvars = k + min(w, 2k):
    k=2 -> 5, k=3 -> 7, k=4 -> 9 (fronteira verificada por sonda)."""
    gpf.gates = []
    return gpf.gen_tau(1, seed, k=k, w=k + 1)


# ---------------- validacao de metricas (n=96) ----------------

def validate_metrics_n96():
    rng = random.Random(SEED + 9)
    wn = [rng.gauss(0, 1) for _ in range(96)]
    ramp = [i / 95.0 for i in range(96)]
    sine = [math.sin(2 * math.pi * i / 16) for i in range(96)]
    inv_err = abs(boxdim_rank(wn) - boxdim_rank([math.exp(v) for v in wn]))
    ok = (taxa_saltos(wn) > taxa_saltos(ramp)
          and taxa_saltos(wn) > taxa_saltos(sine)
          and boxdim_curve(sine) < boxdim_curve(wn)
          and inv_err < 1e-9)
    return {"status": "OK" if ok else "FALHA",
            "inv_err": inv_err,
            "saltos": {"ruido": taxa_saltos(wn), "rampa": taxa_saltos(ramp),
                       "seno": taxa_saltos(sine)},
            "boxdim": {"ruido": boxdim_curve(wn),
                       "seno": boxdim_curve(sine)}}


# ---------------- contraste de MEDIAS (2 niveis + bonf 0.05/2) ----

def mean_contrast(a, b, rng, n_boot=N_BOOT):
    """Delta = media(a) - media(b) com bootstrap IID (grupos
    independentes) — percentil PRIMARIO + BCa parceiro + jackknife
    delete-one pooled + Bonferroni 0.05/2 + regra de 2 niveis."""
    if len(a) < 8 or len(b) < 8:
        return None

    def mn(x):
        return sum(x) / len(x)
    obs = mn(a) - mn(b)
    if math.isnan(obs):
        return None
    boots = []
    for _ in range(n_boot):
        ia = [rng.randrange(len(a)) for _ in range(len(a))]
        ib = [rng.randrange(len(b)) for _ in range(len(b))]
        boots.append(mn([a[i] for i in ia]) - mn([b[i] for i in ib]))
    jack = []
    for i in range(len(a)):
        jack.append(mn(a[:i] + a[i + 1:]) - mn(b))
    for i in range(len(b)):
        jack.append(mn(a) - mn(b[:i] + b[i + 1:]))
    lo, hi, info = bca_ci(obs, boots, jack, alpha=0.05)
    if lo is None:
        return None
    plo, phi = pct_ci(boots)
    sb = sorted(boots)

    def q(p):
        return sb[min(len(sb) - 1, max(0, int(round(p * (len(sb) - 1)))))]
    b2lo, b2hi = q(0.0125), q(0.9875)      # Bonferroni 0.05/2
    m = sum(boots) / len(boots)
    se = (sum((x - m) ** 2 for x in boots) / (len(boots) - 1)) ** 0.5
    out = {
        "point": obs,
        "pct_lo": plo, "pct_hi": phi,
        "bca_lo": lo, "bca_hi": hi,
        "pct_bonf2_lo": b2lo, "pct_bonf2_hi": b2hi,
        "se_boot": se, "mde80": 2.801585 * se,
        "z0": info.get("z0"),
        "point_outside": obs < plo or obs > phi,
        "excludes0": plo > 0 or phi < 0,
        "excludes0_bca": lo > 0 or hi < 0,
        "excludes0_bonf2": b2lo > 0 or b2hi < 0,
        "n_boot": len(boots), "n_jack": len(jack),
    }
    excl_same_dir = (out["excludes0"] and out["excludes0_bca"]
                     and ((plo > 0) == (lo > 0))
                     and ((obs > 0) == (plo > 0)))
    both_include = (not out["excludes0"]) and (not out["excludes0_bca"])
    out["concordante"] = ((not out["point_outside"])
                          or excl_same_dir or both_include)
    out["discordante"] = out["point_outside"] and not out["concordante"]
    if out["point_outside"]:
        out["veredito"] = ("SEPARA_FLAG" if excl_same_dir else
                           "INCONCLUSIVO_FLAG" if both_include
                           else "INCOERENTE_DISCORDANTE")
    elif out["excludes0"]:
        out["veredito"] = "SEPARA"
    else:
        out["veredito"] = "INCONCLUSIVO"
    return out


def classify_mean(c, dirn):
    """Regra direcional de 2 niveis (idem r5/r6; bonf 0.05/2)."""
    if c is None:
        return "SEM_DADOS"
    v = c["veredito"]
    if v == "INCOERENTE_DISCORDANTE":
        return "INCOERENTE_DISCORDANTE"
    if v in ("SEPARA_FLAG", "INCONCLUSIVO_FLAG"):
        if not c["excludes0"]:
            return "FALHA_INCONCLUSIVO_FLAG"
        sinal = 1 if c["point"] > 0 else -1
        if sinal != dirn:
            return "CONTRADITA_FLAG"
        return "OK_BONF_FLAG" if c["excludes0_bonf2"] else "OK_FLAG"
    if v == "INCONCLUSIVO":
        return "FALHA_INCONCLUSIVO"
    sinal = 1 if c["point"] > 0 else -1
    if sinal != dirn:
        return "CONTRADITA"
    return "OK_BONF" if c["excludes0_bonf2"] else "OK"


# ---------------- metricas descritivas com CI ----------------

def metric_ci(x, fn, runs, rng, n_boot=N_BOOT):
    """Percentil estratificado (estratos = niveis de k) — CI
    DESCRIPTIVO (sem hipotese)."""
    if len(x) < 16:
        return {"point": fn(x), "lo": None, "hi": None}
    obs = fn(x)
    boots = []
    for _ in range(n_boot):
        idx, start = [], 0
        for n in runs:
            idx.extend(start + rng.randrange(n) for _ in range(n))
            start += n
        v = fn([x[i] for i in idx])
        if v is not None and not math.isnan(v):
            boots.append(v)
    if len(boots) < 200:
        return {"point": obs, "lo": None, "hi": None}
    boots.sort()
    return {"point": obs,
            "lo": boots[int(0.025 * len(boots))],
            "hi": boots[int(0.975 * len(boots))]}


# ---------------- selftests ----------------

def calibrate_mean_machinery():
    """S3: tipo-I e poder da maquina de contrastes de medias."""
    rng = random.Random(SEED_BOOT)
    ti, T = 0, 40
    for _ in range(T):
        a = [rng.gauss(0, 1) for _ in range(32)]
        b = [rng.gauss(0, 1) for _ in range(32)]
        c = mean_contrast(a, b, rng)
        if c and (c["excludes0"] or (c["point_outside"]
                                     and c["excludes0_bca"])):
            ti += 1
    pw, P = 0, 10
    for _ in range(P):
        a = [rng.gauss(1.0, 1) for _ in range(32)]   # deslocamento 1.0
        b = [rng.gauss(0.0, 1) for _ in range(32)]
        c = mean_contrast(a, b, rng)
        if c and c["veredito"] in ("SEPARA", "SEPARA_FLAG") \
                and c["point"] > 0:
            pw += 1
    return {
        "S3a_tipo1": {"n": T, "exclusoes": ti, "taxa": ti / T,
                      "gate_ok": ti / T <= 0.15},
        "S3b_poder": {"n": P, "detectou": pw, "gate_ok": pw >= 7,
                      "nota": "deslocamento de media =1.0 sigma"},
        "status": ("OK" if (ti / T <= 0.15 and pw >= 7) else "FALHA"),
    }


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
    mine = {(FAM, str(k), str(s)) for k in KS for s in SEEDS}
    inter = used & mine
    return {"status": "OK" if not inter else "FALHA",
            "n_prev": len(used), "n_r5": len(mine), "fontes": n_src,
            "interseccao": sorted(inter)[:10]}


# ---------------- smoke S5 (analyze com stub) ----------------

def _smoke_rows():
    rows = []
    for k in KS:
        for i, s in enumerate(SEEDS):
            base = {2: 5, 3: 7, 4: 9}[k]
            mr = base + (i % 3) * 2          # valores ficticios
            rows.append({"family": FAM, "param": k, "seed": s,
                         "tag": "smoke", "nvars": k + 3, "nclauses": 20,
                         "fecho": 100 + k, "lb": 3, "minref": mr,
                         "minref_censored": False, "sat_drat": "UNSAT",
                         "proof_drat": mr + 4, "t_testados": "3;4;5",
                         "pares_ultimo": 1000})
    return rows


def smoke_analyze():
    """S5: analyze() com mean_contrast() STUBADO (licenca r5)."""
    global mean_contrast
    orig = mean_contrast
    state = {"i": 0}

    def stub(a, b, rng, n_boot=N_BOOT):
        state["i"] += 1
        fl = state["i"] % 4
        base = {"point": 1.0, "pct_lo": 0.5, "pct_hi": 1.5,
                "bca_lo": 0.6, "bca_hi": 1.4,
                "pct_bonf2_lo": 0.4, "pct_bonf2_hi": 1.6,
                "se_boot": 0.2, "mde80": 0.56, "z0": 0.3,
                "point_outside": False, "excludes0": True,
                "excludes0_bca": True, "excludes0_bonf2": True,
                "concordante": True, "discordante": False,
                "veredito": "SEPARA", "n_boot": n_boot, "n_jack": 60}
        if fl == 1:
            base.update({"point_outside": True, "veredito": "SEPARA_FLAG"})
        elif fl == 2:
            base.update({"point": 0.01, "pct_lo": -0.5, "pct_hi": 0.5,
                         "excludes0": False, "excludes0_bca": False,
                         "excludes0_bonf2": False,
                         "veredito": "INCONCLUSIVO"})
        elif fl == 3:
            base.update({"point": 0.02, "pct_lo": -0.5, "pct_hi": 0.5,
                         "bca_lo": 0.3, "bca_hi": 0.8,
                         "point_outside": True, "excludes0": False,
                         "excludes0_bca": True, "concordante": False,
                         "discordante": True,
                         "veredito": "INCOERENTE_DISCORDANTE"})
        return base

    mean_contrast = stub
    import io as _io
    import contextlib as _ctx
    try:
        rows = _smoke_rows()
        buf = _io.StringIO()
        with _ctx.redirect_stdout(buf):
            res = analyze(rows, contrast_fn=stub)
        assert "H_t1_viabilidade" in res and "H_t2_dinamica" in res
        assert res["H_t1_viabilidade"]["veredito"]
        assert res["_assert"]["violacoes"] == []
        assert len(res["metricas"]) >= 2
    finally:
        mean_contrast = orig
    return {"status": "OK",
            "nota": "analyze() completo com stub (H_t1/H_t2/metricas)"}


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
    censored = skipped = viol = 0
    t_all = time.time()
    for k in KS:
        points = GRID[k]
        todo = [(p, s) for p, s in points
                if (FAM, str(p), str(s)) not in done]
        if not todo:
            print(f"\n--- tau k={k} (ja completa) ---", flush=True)
            continue
        print(f"\n--- tau k={k} (n={ {2:5,3:7,4:9}[k] } vars; "
              f"{len(todo)} novas; max_aux={MAX_AUX_BY_K[k]:,}) ---",
              flush=True)
        t_f = time.time()
        slow = 0
        for param, seed in todo:
            built = gen_tau_k(k, seed)
            if built is None:
                print(f"  [GEN None] k={k} s={seed}")
                skipped += 1
                continue
            nvars, clauses, tag = built
            ne = len({abs(l) for c in clauses for l in c})
            t1 = time.time()
            mr, fecho, info = minref_deep(
                [frozenset(c) for c in clauses],
                max_aux=MAX_AUX_BY_K[k], with_info=True)
            st_r, len_r = solve_drat(nvars, clauses)
            dt = time.time() - t1
            if dt > 180:
                slow += 1
                print(f"    [LENTO {dt/60:.1f}min] k={k} s={seed} "
                      f"mr={mr if not isinstance(mr, tuple) else '>'}",
                      flush=True)
            if mr is None:
                print(f"  [SAT?!] k={k} s={seed} — descartado")
                skipped += 1
                continue
            # ASSERT teorema: minref_exato >= d(vazia)
            if isinstance(mr, int) and info.get("lb") is not None \
                    and mr < info["lb"]:
                viol += 1
                print(f"  [BUG ASSERT] k={k} s={seed}: minref={mr} < "
                      f"lb={info['lb']} — VIOLACAO DO TEOREMA",
                      flush=True)
            if isinstance(mr, tuple):
                mr_out, censor = f">{mr[1]}({mr[2]})", True
                censored += 1
            else:
                mr_out, censor = mr, False
            rows.append({
                "family": FAM, "param": k, "seed": seed, "tag": tag,
                "nvars": ne, "nclauses": len(clauses), "fecho": fecho,
                "lb": info.get("lb"),
                "minref": mr_out, "minref_censored": censor,
                "sat_drat": st_r, "proof_drat": len_r,
                "t_testados": ";".join(str(t)
                                      for t in info.get("t_testados", [])),
                "pares_ultimo": (info.get("pares_testados") or [0])[-1],
            })
            write_series(rows)          # checkpoint atomico
        done_n = sum(1 for r in rows if int(r["param"]) == k)
        exact = [r for r in rows if int(r["param"]) == k
                 and str(r["minref_censored"]) == "False"]
        unsat = [r for r in rows if int(r["param"]) == k
                 and r["sat_drat"] == "UNSAT"]
        vals = sorted({int(r["minref"]) for r in exact})
        print(f"  UNSAT: {len(unsat)}/{done_n} | exatos: {len(exact)} "
              f"| valores: {vals} | censuras: "
              f"{sum(1 for r in rows if int(r['param']) == k and str(r['minref_censored']) == 'True')} "
              f"| lentos: {slow} | {time.time()-t_f:.0f}s", flush=True)
    print(f"\ncoleta total: {len(rows)} linhas, {censored} censuras, "
          f"{skipped} descartes, ASSERT violacoes={viol}, "
          f"{(time.time()-t_all)/60:.1f}min")
    return rows, viol


def load_series_from_csv():
    return list(csv.DictReader(OUT_SERIES.open(encoding="utf-8")))


# ---------------- analise ----------------

def analyze(rows, contrast_fn=mean_contrast):
    t0 = time.time()
    # asserts
    viol = []
    for r in rows:
        if str(r["minref_censored"]) == "False":
            try:
                if int(r["minref"]) < int(r["lb"]):
                    viol.append((r["param"], r["seed"],
                                 r["minref"], r["lb"]))
            except (TypeError, ValueError):
                pass
    # series por nivel (exatos) + drat dos MESMOS pontos
    lvl, lvl_drat = {k: [] for k in KS}, {k: [] for k in KS}
    for r in rows:
        if str(r["minref_censored"]) == "False" \
                and str(r["sat_drat"]) == "UNSAT" \
                and str(r["proof_drat"]) not in ("", "None"):
            k = int(r["param"])
            lvl[k].append(int(r["minref"]))
            lvl_drat[k].append(float(r["proof_drat"]))
    # serie ordinal completa (k,seed) dos exatos — para metricas
    pts = [r for r in rows if str(r["minref_censored"]) == "False"
           and str(r["sat_drat"]) == "UNSAT"]
    pts.sort(key=lambda r: (int(r["param"]), int(r["seed"])))
    ser_min = [int(r["minref"]) for r in pts]
    ser_drat = [float(r["proof_drat"]) for r in pts]
    runs = []
    for k in KS:
        n = sum(1 for r in pts if int(r["param"]) == k)
        if n:
            runs.append(n)

    rng = random.Random(SEED_BOOT)

    # ---- H_t1: viabilidade (k=3 exatos >=16/32) ----
    n3 = len(lvl[3])
    hyp_t1 = {"alvo": "k=3: >=16/32 (50%) exatos",
              "n_exatos_k3": n3, "n_grid_k3": len(GRID[3]),
              "veredito": ("CONFIRMADA" if n3 >= 16 else "REFUTADA")}

    # ---- H_t2: medias crescem com k (2 contrastes, regra 2 niveis) ----
    tests = {}
    for name, ka, kb in (("k3_k2", 3, 2), ("k4_k3", 4, 3)):
        a, b = lvl[ka], lvl[kb]
        if len(a) < 8 or len(b) < 8:
            tests[name] = {"resultado": "SEM_DADOS",
                           "n_a": len(a), "n_b": len(b)}
            continue
        c = contrast_fn(a, b, rng)
        tests[name] = {"resultado": classify_mean(c, +1),
                       "n_a": len(a), "n_b": len(b), "dado": c}
    res = {v["resultado"] for v in tests.values()}
    if "SEM_DADOS" in res and len(res) == 1:
        verdict_t2 = "SEM_DADOS"
    elif "CONTRADITA" in res or "CONTRADITA_FLAG" in res:
        verdict_t2 = "REFUTADA_CONTRADITA"
    else:
        n_ok = sum(1 for v in tests.values()
                   if str(v["resultado"]).startswith("OK"))
        n_incoh = sum(1 for v in tests.values()
                      if v["resultado"] == "INCOERENTE_DISCORDANTE")
        if n_ok == 2:
            verdict_t2 = "CONFIRMADA"
        elif n_ok == 0:
            verdict_t2 = ("REFUTADA" if n_incoh < 2 else
                          "INDETERMINADO")
        else:
            verdict_t2 = f"PARCIAL ({n_ok}/2)"
    hyp_t2 = {"enunciado": ("medias de minref exato crescem com k; "
                            "2 contrastes adjacentes (percentil "
                            "primario + BCa + regra 2 niveis + "
                            "bonf 0.05/2); caveat: censuras enviesam "
                            "medias para baixo (reportar por nivel)"),
              "testes": tests, "veredito": verdict_t2}

    # ---- metricas descritivas (serie ordinal exata + drat) ----
    metricas = {}
    for sname, ser in (("minref", ser_min), ("drat", ser_drat)):
        if len(ser) < 16:
            continue
        entry = {"n": len(ser), "mean": sum(ser) / len(ser),
                 "min": min(ser), "max": max(ser), "metricas": {}}
        for mname, fn in METRICS.items():
            entry["metricas"][mname] = metric_ci(ser, fn, runs, rng)
        metricas[sname] = entry

    # ---- tabela por nivel + censuras ----
    niveis = {}
    for k in KS:
        ex = lvl[k]
        cen = sum(1 for r in rows if int(r["param"]) == k
                  and str(r["minref_censored"]) == "True")
        niveis[str(k)] = {
            "nvars": {2: 5, 3: 7, 4: 9}[k],
            "exatos": len(ex), "censuras": cen,
            "minref_mean": (sum(ex) / len(ex)) if ex else None,
            "minref_min": min(ex) if ex else None,
            "minref_max": max(ex) if ex else None,
            "drat_mean": (sum(lvl_drat[k]) / len(lvl_drat[k]))
            if lvl_drat[k] else None,
        }

    out = {"H_t1_viabilidade": hyp_t1, "H_t2_dinamica": hyp_t2,
           "_assert": {"violacoes": viol,
                       "veredito": ("OK (minref >= d(vazia) em todas)"
                                    if not viol
                                    else f"BUG ({len(viol)} violacoes)")},
           "metricas": metricas, "niveis": niveis,
           "_diag": {"n_rows": len(rows),
                     "serie_n": len(ser_min),
                     "estratos": runs,
                     "censuras_total": sum(
                         1 for r in rows
                         if str(r["minref_censored"]) == "True")}}
    print(f"\n--- hipoteses (stub={contrast_fn is not mean_contrast}) ---")
    print(f"  H_t1: {hyp_t1['veredito']} "
          f"({hyp_t1['n_exatos_k3']}/{hyp_t1['n_grid_k3']} exatos k=3)")
    print(f"  H_t2: {hyp_t2['veredito']}")
    for name, t in hyp_t2["testes"].items():
        d = t.get("dado")
        extra = (f"point={d['point']:+.3f} "
                 f"pct=[{d['pct_lo']:+.3f},{d['pct_hi']:+.3f}] "
                 f"z0={d['z0']:+.2f}" if d else "")
        print(f"    {name}: {t['resultado']} {extra}")
    print(f"  ASSERT: {out['_assert']['veredito']}")
    for k in KS:
        nv = niveis[str(k)]
        print(f"  nivel k={k} (n={nv['nvars']}): exatos={nv['exatos']} "
              f"censuras={nv['censuras']} "
              f"mean_minref={nv['minref_mean'] and round(nv['minref_mean'],2)} "
              f"mean_drat={nv['drat_mean'] and round(nv['drat_mean'],2)}")
    for sname, e in metricas.items():
        mh = e["metricas"].get("higuchi_D", {})
        mb = e["metricas"].get("boxdim", {})
        ms = e["metricas"].get("saltos", {})
        print(f"  metricas[{sname}] n={e['n']}: "
              f"D_H={mh.get('point') and round(mh['point'],3)} "
              f"boxdim={mb.get('point') and round(mb['point'],3)} "
              f"saltos={ms.get('point') and round(ms['point'],3)}")
    print(f"analise: {time.time()-t0:.0f}s")
    return out


# ---------------- escrita ----------------

def _sha(p):
    return hashlib.sha256(
        p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


# ---------------- main ----------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest-only", action="store_true")
    ap.add_argument("--analyze-only", action="store_true")
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    t0 = time.time()
    print("=" * 70)
    print("TAU k UP — minref estendido para n>6 (fronteira k=4/n=9)")
    print("=" * 70)

    s1 = selftest_bca_scipy()
    s2 = validate_metrics_n96()
    s3 = calibrate_mean_machinery()
    smk = smoke_analyze()
    disj = check_disjoint()
    print(f"\n[S1] BCa vs scipy: {s1['status']} "
          f"(diff={s1.get('max_diff')})")
    print(f"[S2] metricas n=96: {s2['status']} "
          f"inv_err={s2['inv_err']:.1e}")
    print(f"[S3] maquina de medias: tipo-I={s3['S3a_tipo1']['exclusoes']}"
          f"/{s3['S3a_tipo1']['n']}={s3['S3a_tipo1']['taxa']:.3f} "
          f"(gate<=0.15) poder={s3['S3b_poder']['detectou']}/"
          f"{s3['S3b_poder']['n']} (gate>=7) "
          f"{'OK' if s3['status'] == 'OK' else 'FALHA'}")
    print(f"[S5] smoke analyze: {smk['status']}")
    print(f"[DISJ] r2..r6 vs grade: {disj['status']} "
          f"interseccao={disj.get('interseccao')}")
    ok = (s1["status"] in ("OK", "scipy ausente — pulado")
          and s2["status"] == "OK" and s3["status"] == "OK"
          and smk["status"] == "OK"
          and disj["status"] in ("OK",
                                 "AVISO: CSVs anteriores ausentes — pulado"))
    if not ok:
        print(f"[ABORTA] selftests: {disj['status']} smk={smk['status']} "
              f"s3={s3['status']} s2={s2['status']}")
        return 2
    if args.selftest_only:
        print("\n(--selftest-only: abortando antes do run)")
        return 0

    if args.analyze_only:
        if not OUT_SERIES.exists():
            print("[ERRO] --analyze-only sem CSV de series")
            return 2
        rows = load_series_from_csv()
        print(f"\nre-usando {OUT_SERIES.name}: {len(rows)} linhas")
        mode = "analyze_only"
        viol_from_collect = 0
    else:
        existing = []
        if args.resume and OUT_SERIES.exists():
            existing = load_series_from_csv()
            grid_keys = {(FAM, str(p), str(s))
                         for k in KS for p, s in GRID[k]}
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
        rows, viol_from_collect = collect(existing)
        write_series(rows)
        mode = ("resume+collect+analyze" if existing
                else "collect+analyze")

    results = analyze(rows)
    if viol_from_collect:
        print(f"[BUG] {viol_from_collect} violacoes do ASSERT na "
              f"coleta — ver results._assert")
        return 3

    meta = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat()
                         .replace("+00:00", "Z"),
        "mode": mode,
        "seed": SEED, "seed_boot": SEED_BOOT, "n_boot": N_BOOT,
        "fronteira": ("k=2 exato sempre; k=3 exato ate minref=7 "
                      "(max_aux=6M, REF_7 provado173s); k=4 exato ate "
                      "minref=5 (max_aux=8M, REF_5 provado); k>=5 "
                      "parede do fecho (nao testado)"),
        "max_aux_por_nivel": {str(k): v for k, v in
                              MAX_AUX_BY_K.items()},
        "grid": {str(k): f"{len(GRID[k])} seeds (1536..1667, DISJ)"
                 for k in KS},
        "argmento_pools": ("toda linha de refutacao <=t tem "
                           "profundidade <=t -> pool {d<=t} + pares "
                           "restritos sao equivalentes ao REF_t cheio"),
        "runtime_s": round(time.time() - t0, 1),
        "caveats": [
            ("Pre-registro: hipoteses/regras fixadas neste codigo e no "
             "doc 34_ ANTES do run (C1)."),
            ("Censuras excluidas da serie (regra existente) — medias "
             "por nivel subestimam se censura correlaciona com "
             "minref alto (caveat H_t2)."),
            ("Metricas DESCRIPTIVAS (sem hipotese) — boxdim cross-n "
             "confundido (licenca r4)."),
            ("Checkpoint atomico + --resume (crash CaDiCaL)."),
            ("N1+N2; sem N4; H_C2 (EF) deferido."),
        ],
    }
    payload = {
        "metadata": {**meta,
                     "data_source": "gk_tau_kup.py (tau k↑ — minref "
                                    "estendido n>6)",
                     "instances": {"rows": len(rows),
                                   "censuras": results["_diag"]
                                   ["censuras_total"],
                                   "serie_exata_n": results["_diag"]
                                   ["serie_n"]},
                     "selftests": {"S1_bca_scipy": s1, "S2_metricas": s2,
                                   "S3_maquina": s3, "S5_smoke": smk,
                                   "DISJ": disj},
                     "csv": OUT_SERIES.name,
                     "csv_sha256": _sha(OUT_SERIES),
                     "sha_note": "sha256 bytes normalizados CRLF->LF"},
        "pre_registro": {
            "H_t1": "k=3: >=16/32 exatos (max_aux=6M)",
            "H_t2": ("medias crescem com k;2 contrastes adjacentes; "
                     "bonf 0.05/2; caveat de censura"),
            "ASSERT": "minref_exato >= d(vazia) por instancia",
            "regras": "2 niveis (idem r5/r6) — ver docstring",
        },
        "results": results,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2,
                                   ensure_ascii=False), encoding="utf-8")
    print(f"\n[OK] {OUT_SERIES.name} (sha {_sha(OUT_SERIES)[:16]}…)")
    print(f"[OK] {OUT_JSON.name}")
    print(f"runtime: {meta['runtime_s']}s")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

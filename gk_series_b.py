#!/usr/bin/env python3
"""
gk_series_b.py — SÉRIES EM B: índice lex de b para σ fixo (D4' doc28 §7.3,
doc29 §3 — "série ordinal original do D4′ com minref").

=====================================================================
PRÉ-REGISTRO (fixado ANTES de qualquer execução com dados do
experimento; commit deste codigo e do doc 35_ precede o run — C1):
ver 35_SERIES_EM_B.md s1.
=====================================================================

SONDAS DE ENGENHARIA (seeds 5000-5004 do namespace "tau_b" — NUNCA os
do experimento; nao espiam valores do experimento):
  Configs avaliados (Fase A/B2/variação):
    (1,5) n=6 T=30  fecho=43   minref exato 0s   — variação mínima (plano
           em ss=5001); (1,6) n=7 T=62 fecho=57 — idem; ambos quase-planos
    (2,6) n=8 T=60  fecho=6305 — CENSURA mesmo @20M (t_cap=3) => DESCARTADO
           (parede n>=8 confirmada)
    (2,5) n=7 T=28-29 fecho~2059 — minref VARIA RICO (5<->7 alternando,
           var=0.928 em ss=5000) + drat varia (8/9)
  Censuras @6M por σ (varredura completa, sondas): ss=5000: 4/28 X |
    ss=5002: 0/28 | ss=5003: 0/28 | ss=5004: 3/29 X (nota ">7" =>
    minref>=8) — ~50% dos σ's contem instancia dificil. Sonda @20M:
    >2.2h na 1a instancia (REF_8/9 com prova UNSAT dura) => 20M
    INVIAVEL por custo (~6 dias) => max_aux=6M + exclusao de σ sujo.
  Calibração da máquina (calib_perm, B=300, seed 20261130):
    tipo-I 1-3/40 (gate<=0.15) e poder 10/10 nas grades (24,30)/(16,29);
    S=8 perde poder (3/10) => S>=16 escolhido; S=32 escolhido p/
    robustez a ~50% de σ's sujos (esperado ~16 limpos, P(>=12)~0.96).

DESENHO:
  Gerador gen_tau_at_b(depth, struct_seed, b_rank, k, w): estrutura do
  circuito fixa por (depth, struct_seed) no NAMESPACE "tau_b" (DISJ de
  "tau" — labels distintos no _det_seed); imagem computada; complemento
  ordenado LEX; b = complemento[b_rank] (fora da imagem => UNSAT por
  construcao; ASSERT por instancia).
  Grade: family="tau_b", param=struct_seed (σ), seed=b_rank.
    σ ∈ 6000..6031 (S=32; DISJ das sondas 5000-5004);
    b_rank ∈ 0..T_σ-1 (T_σ = 32 - |imagem_σ| ∈ {28,29}).
  Instância: gen -> solve (UNSAT exigido) -> minref_deep(max_aux=6M,
    with_info) -> solve_drat -> linha. CHECKPOINT atomico + --resume.
  CSV SEM coluna de tempo (byte-reprodutivel).

HIPÓTESES (declaradas aqui, ANTES do run):
  H_b1 VIABILIDADE: >=12/32 σ's USABLES = (0 censuras no σ) AND (minref
    com variancia > 0) AND (acf1 nao-nan). CONFIRMADA >=12; SEM_DADOS
    se <8; REFUTADA caso contrario. Consequencia pre-declarada: σ's nao
    utilizaveis sao EXCLUIDOS do H_b2 (reportados com contagem; ESCOPO:
    H_b2 fala dos σ's sem instancia minref>=8 — limitacao declarada).
  H_b2 DINAMICA (estrutura serial em b, PRIMÁRIA): por σ utilizavel,
    D_σ = acf1(serie real em ordem lex) - media_B acf1(B=1000
    permutacoes internas da MESMA serie); estatistica = media de D sobre
    σ; inferencia = bootstrap SOBRE σ (B=1000): percentil 95% PRIMARIO +
    BCa parceiro + jackknife delete-one + regra de 2 niveis (idem r5/r6)
    + MDE80; DIRECAO -1 (alternância/anti-persistência — base: sonda
    σ=5000 com D=-0,36; seeds de engenharia; caveat declarado).
    CONFIRMADA iff CI95 percentil exclui 0 E BCa concordante no mesmo
    sinal; CONTRADITA se exclui no sinal oposto; senao
    FALHA_INCONCLUSIVO (leitura estatistica obrigatoria: "sem suporte",
    poder declarado no S3). α=0.05 (hipotese unica confirmatoria — sem
    Bonferroni de grupo; H_b3 e descritiva).
  ASSERT (teorema): minref_exato >= d(vazia) por instancia — violacao =
    BUG (exit3).
  H_b3 DESCRIPTIVA (sem claim): contraste pareado D_minref - D_drat
    (mesma maquina) + tabelas por σ — candidata (C) a rodada futura.

MÉTRICAS: primária = **acf1** (autocorrelação defasada-1). HISTÓRICO:
a v1 do pré-registro usou `saltos` e o S3 FALHOU (poder 0/10) —
`taxa_saltos` ≡ 1.0 em série binária (toda transição ≠0 alterna sinal
obrigatoriamente) => D ≡ 0. Troca PRE-RUN (nada commitado ainda) para
acf1, escolhida por teste empírico (D: alternante −0,94 · blocos +0,93 ·
sonda real −0,36 · iid ±ruído; boxdim/rank fracos ~0,06). Descritivas
por série: boxdim, boxdim_rank, saltos, higuchi_D, hurst_rs — NOTA
pré-declarada: higuchi exige n>=32 e hurst n>=36 => NaN em T∈{28,29}
(registrado, nao usado em claim); saltos aparece só descritiva (S4
verifica a degeneração binária como contrato).

SELFTESTS (aborta se falhar; repetidos no run; A8):
  S1  BCa vs scipy (iid) — valida bca_ci
  S3  calibracao da MAQUINA COMPLETA (D_σ + bootstrap sobre σ):
      tipo-I 40 series iid (gate <=0.15) + poder 10 com padrao
      alternante+ruido (gate >=7/10)
  S4  metricas em T=28: saltos/boxdim nao-nan em serie rica;
      boxdim_rank invariante a transformacao monotona; hurst/higuchi
      NaN em T<32 (contrato declarado)
  S5  SMOKE de analyze() com bootstrap CONTRAST() STUBADO (licenca r5)
  S6  determinismo do drat (2 execucoes -> mesmo comprimento)
  DISJ grade x (v2..v6, tau_kup) = vazia
  ASSERT por instancia na coleta

SAIDAS: gk_series_b_series.csv + gk_series_b.json (R6 protege o par)
Uso:   python -u gk_series_b.py [--selftest-only | --analyze-only |
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
from gk_proof_fractal import (SEED, _det_seed, _eval_circuit, solve_drat)
from gk_proof_fractal_v3 import boxdim_rank, taxa_saltos
from gk_proof_fractal import boxdim_curve, higuchi_D, hurst_rs
from gk_minref import minref_deep
from gk_proof_fractal_v2_r2 import bca_ci, pct_ci
from gk_proof_fractal_v5 import selftest_bca_scipy

# ---------------- constantes ----------------

DEPTH = 1
K, W = 2, 5                       # config escolhida (sondas)
STRUCT_SEEDS = range(6000, 6032)  # S=32 (DISJ sondas 5000-5004); subiu
# de 16 p/ 32 PRE-COMMIT: sondas @6M mostraram ~50% de σ's "sujos"
# (contem instancia minref>=8 -> ponto censurado -> σ excluido);
# S=32 => esperado ~16 limpos, P(>=12)~0.96 (gate H_b1)
MAX_AUX = 6_000_000               # rápido (~120s/inst); X (minref>=8)
# censuram -> exclusao de σ; 20M INVIAVEL (sonda @20m >2.2h na 1a
# instancia = REF_8/9 com prova UNSAT dura)
N_BOOT = 1000                     # bootstrap sobre σ
B_SHUF = 1000                     # permutações internas por σ
SEED_BOOT = SEED + 11             # 20261130 — declarado
FAM = "tau_b"

SRC_PREV = [Path(f"gk_proof_fractal_v{i}_series.csv")
            for i in (2, 3, 4, 5, 6)] + [Path("gk_tau_kup_series.csv")]
OUT_SERIES = Path("gk_series_b_series.csv")
OUT_JSON = Path("gk_series_b.json")

GRID = [(s, r) for s in STRUCT_SEEDS for r in range(64)]
# param=σ, seed=b_rank; T_σ real (28-29) descoberto na coleta


# ---------------- gerador σ-fixo ----------------

def gen_tau_at_b(depth, struct_seed, b_rank, k=K, w=W):
    """Estrutura fixa por (depth, struct_seed) no namespace "tau_b";
    b = b_rank-esimo do complemento em ordem lex (fora da imagem)."""
    rng = random.Random(_det_seed(SEED, "tau_b", depth, struct_seed))
    gpf.gates = []
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
                gpf.gates.append((nxt, op, a, None))
            else:
                gpf.gates.append((nxt, op, a, b))
            cur.append(nxt)
            nxt += 1
        layers.append(cur)
    outputs = layers[-1][:w] if len(layers[-1]) >= w else layers[-1]
    while len(outputs) < w:
        a = rng.choice(layers[-1])
        gpf.gates.append((nxt, "NOT", a, None))
        outputs.append(nxt)
        nxt += 1
    nvars = nxt - 1

    image = set()
    for mask in range(1 << k):
        inputs = {i + 1: bool((mask >> i) & 1) for i in range(k)}
        val = _eval_circuit(gpf.gates, inputs)
        image.add(tuple(1 if val[o] else 0 for o in outputs))
    complement = sorted(
        b for b in (tuple((mask >> i) & 1 for i in range(len(outputs)))
                    for mask in range(1 << len(outputs)))
        if b not in image)
    if not complement:
        return None
    b = complement[b_rank % len(complement)]

    clauses = []
    for idx, op, a, bvar in gpf.gates:
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
    for pos, o in enumerate(outputs):
        clauses.append([-o] if b[pos] == 0 else [o])
    tag = "b_out=" + "".join(map(str, b))
    return nvars, clauses, tag, len(complement)


# ---------------- série + estrutura (D_σ) ----------------

def acf1(x):
    """Autocorrelação defasada-1 de Pearson. NaN se variância 0
    (serie constante) ou n<8. ESCOLHIDA como primaria (S3 pegou a
    degeneracao de saltos em serie binaria — ver doc 35 s1.4)."""
    n = len(x)
    if n < 8:
        return float("nan")
    m = sum(x) / n
    den = sum((v - m) ** 2 for v in x)
    if den == 0:
        return float("nan")
    num = sum((x[i] - m) * (x[i + 1] - m) for i in range(n - 1))
    return num / den


def acf_D(serie, rng, n_shuf=B_SHUF):
    """D = acf1(real) - media de acf1 sobre permutacoes internas.
    None se acf indefinido (serie constante)."""
    obs = acf1(serie)
    if obs is None or (isinstance(obs, float) and math.isnan(obs)):
        return None
    acc, n = 0.0, 0
    for _ in range(n_shuf):
        t = list(serie)
        rng.shuffle(t)
        v = acf1(t)
        if v is not None and not math.isnan(v):
            acc += v
            n += 1
    if n < n_shuf // 2:
        return None
    return obs - acc / n


def contrast_over_sigma(vals, rng, n_boot=N_BOOT):
    """Media sobre σ com bootstrap percentil (PRIMARIO) + BCa (parceiro)
    + jackknife delete-one + MDE — maquina da casa (r5/r6/τ k↑)."""
    n = len(vals)
    if n < 8:
        return None
    obs = sum(vals) / n
    boots = []
    for _ in range(n_boot):
        s = sum(vals[rng.randrange(n)] for _ in range(n)) / n
        boots.append(s)
    jack = [(sum(vals[:i] + vals[i + 1:])) / (n - 1) for i in range(n)]
    lo, hi, info = bca_ci(obs, boots, jack, alpha=0.05)
    if lo is None:
        return None
    plo, phi = pct_ci(boots)
    sb = sorted(boots)

    def q(p):
        return sb[min(len(sb) - 1, max(0, int(round(p * (len(sb) - 1)))))]
    m = sum(boots) / len(boots)
    se = (sum((x - m) ** 2 for x in boots) / (len(boots) - 1)) ** 0.5
    out = {"point": obs, "pct_lo": plo, "pct_hi": phi,
           "bca_lo": lo, "bca_hi": hi,
           "se_boot": se, "mde80": 2.801585 * se, "z0": info.get("z0"),
           "point_outside": obs < plo or obs > phi,
           "excludes0": plo > 0 or phi < 0,
           "excludes0_bca": lo > 0 or hi < 0,
           "n_boot": len(boots), "n_jack": len(jack), "n_sigma": n}
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


def classify_dirn(c, dirn):
    """Regra direcional de 2 níveis (idem r5/r6/τ k↑)."""
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
        return "OK_FLAG"
    if v == "INCONCLUSIVO":
        return "FALHA_INCONCLUSIVO"
    sinal = 1 if c["point"] > 0 else -1
    if sinal != dirn:
        return "CONTRADITA"
    return "OK"


# ---------------- selftests ----------------

def selftest_s3(n_ti=40, n_pw=10):
    """Calibracao da MAQUINA COMPLETA (D_σ + bootstrap sobre σ).

    Historico: a v1 usava saltos como D — S3 FALHOU (poder 0/10) porque
    taxa_saltos ≡ 1.0 em serie binaria (transições sempre alternam
    sinal) => D ≡ 0. Troca PRE-RUN para acf1 (doc 35 s1.4)."""
    rng = random.Random(SEED_BOOT)
    alf = [5, 7]
    n_sig = len(STRUCT_SEEDS)      # S do design (32) — fidelidade
    ti = 0
    for _ in range(n_ti):
        vals = []
        for _s in range(n_sig):
            serie = [rng.choice(alf) for _ in range(28)]
            d = acf_D(serie, rng)
            if d is not None:
                vals.append(d)
        c = contrast_over_sigma(vals, rng)
        if c and (c["excludes0"] or (c["point_outside"]
                                     and c["excludes0_bca"])):
            ti += 1
    pw = 0
    for _ in range(n_pw):
        vals = []
        for _s in range(n_sig):
            serie = []
            for r in range(28):
                base = 6 + (1 if r % 2 == 0 else -1)   # alternante 5/7
                v = base + rng.gauss(0, 0.35)
                serie.append(7 if v >= 6 else 5)
            d = acf_D(serie, rng)
            if d is not None:
                vals.append(d)
        c = contrast_over_sigma(vals, rng)
        # alternância => D < 0 => dirn = -1
        if c and c["veredito"] in ("SEPARA", "SEPARA_FLAG") and c["point"] < 0:
            pw += 1
    return {"S3a_tipo1": {"n": n_ti, "exclusoes": ti, "taxa": ti / n_ti,
                          "gate_ok": ti / n_ti <= 0.15},
            "S3b_poder": {"n": n_pw, "detectou": pw, "gate_ok": pw >= 7,
                          "nota": "padrao alternante 5/7 + ruido 0.35; "
                                  "dirn=-1 (D=acf1 real - media shuffles)"},
            "status": "OK" if (ti / n_ti <= 0.15 and pw >= 7) else "FALHA"}


def selftest_s4():
    """Metricas em T=28 (contratos declarados).

    Contratos:
    - saltos ≡ 1.0 em serie binaria com >=4 transicoes (S3 v1 pegou a
      degeneracao) e NaN com <4 — por isso NAO e' a primaria; aparece
      so descritiva;
    - serie de DEGRAU (14x5+14x7) tem 1 diff != 0 -> saltos NaN;
    - acf1: NaN em serie constante (variancia 0), definida em binaria
      nao-constante (e' a PRIMARIA);
    - hurst (n>=36) e higuchi (n>=32) NaN em T=28 — nao usados em claim.
    """
    alt = [5, 7] * 14
    esp = [5] * 14 + [7] * 14
    const = [5] * 28
    rng = random.Random(SEED_BOOT + 1)
    ricos = [rng.choice([5, 7]) for _ in range(28)]
    s_alt, s_esp = taxa_saltos(alt), taxa_saltos(esp)
    a_alt, a_const = acf1(alt), acf1(const)
    br_alt = boxdim_rank(alt)
    br_ric = boxdim_rank(ricos)
    br_esp = boxdim_rank(esp)
    hu = hurst_rs(alt)          # NaN em T=28 (n<36) — contrato
    hi = higuchi_D(alt)         # NaN em T=28 (n<32) — contrato
    mono = boxdim_rank([math.exp(v) for v in ricos])
    inv_err = abs(mono - br_ric) if not math.isnan(mono) else float("nan")
    ok = (abs(s_alt - 1.0) < 1e-9      # degeneracao binaria documentada
          and math.isnan(s_esp)        # contrato degrau=NaN
          and not math.isnan(a_alt) and a_alt < -0.9
          and math.isnan(a_const)      # constante -> NaN (filtro H_b1)
          and not math.isnan(br_alt) and not math.isnan(br_ric)
          and not math.isnan(br_esp)
          and math.isnan(hu) and math.isnan(hi)
          and not math.isnan(inv_err) and inv_err < 1e-9)
    return {"status": "OK" if ok else "FALHA",
            "saltos_alt_deg": s_alt, "saltos_degrau_nan": math.isnan(s_esp),
            "acf1_alt": a_alt, "acf1_const_nan": math.isnan(a_const),
            "boxdim_rank_alt": br_alt, "inv_err": inv_err,
            "hurst_nan_esperado": math.isnan(hu),
            "higuchi_nan_esperado": math.isnan(hi)}


def selftest_s6():
    """Determinismo do drat (2 execucoes -> mesmo comprimento)."""
    n, cl, tag, T = gen_tau_at_b(DEPTH, 5000, 0)
    r1 = solve_drat(n, cl)
    r2 = solve_drat(n, cl)
    return {"status": "OK" if r1 == r2 else "FALHA",
            "run1": str(r1), "run2": str(r2)}


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
    mine = {(FAM, str(s), str(r)) for s in STRUCT_SEEDS for r in range(64)}
    inter = used & mine
    return {"status": "OK" if not inter else "FALHA",
            "n_prev": len(used), "n_mine": len(mine), "fontes": n_src,
            "interseccao": sorted(inter)[:10]}


def smoke_analyze():
    """S5: analyze() com contrast_over_sigma() STUBADO (licenca r5)."""
    import io as _io
    import contextlib as _ctx
    orig = contrast_over_sigma
    state = {"i": 0}

    def stub(vals, rng, n_boot=N_BOOT):
        state["i"] += 1
        base = {"point": 0.1, "pct_lo": 0.05, "pct_hi": 0.15,
                "bca_lo": 0.06, "bca_hi": 0.14, "se_boot": 0.02,
                "mde80": 0.06, "z0": 0.1, "point_outside": False,
                "excludes0": True, "excludes0_bca": True,
                "concordante": True, "discordante": False,
                "veredito": "SEPARA", "n_boot": n_boot, "n_jack": 16,
                "n_sigma": len(vals)}
        if state["i"] == 2:
            base.update({"point": 0.01, "pct_lo": -0.1, "pct_hi": 0.1,
                         "bca_lo": -0.1, "bca_hi": 0.1,
                         "excludes0": False, "excludes0_bca": False,
                         "concordante": True, "veredito": "INCONCLUSIVO"})
        return base
    try:
        rows = _smoke_rows()
        globals()["contrast_over_sigma"] = stub
        buf = _io.StringIO()
        with _ctx.redirect_stdout(buf):
            res = analyze(rows)
        assert "H_b1_viabilidade" in res and "H_b2_estrutura" in res
        assert res["H_b1_viabilidade"]["veredito"]
        assert res["_assert"]["violacoes"] == []
    finally:
        globals()["contrast_over_sigma"] = orig
    return {"status": "OK", "nota": "analyze() completo com stub"}


def _smoke_rows():
    rows = []
    for s in STRUCT_SEEDS:
        for r in range(28):
            mr = 5 + (2 if (r % 2 == 0 and (s + r) % 3 == 0) else 0)
            rows.append({"family": FAM, "param": s, "seed": r,
                         "tag": "b_out=smoke", "nvars": 7, "nclauses": 20,
                         "fecho": 2059, "lb": 3, "minref": mr,
                         "minref_censored": False, "sat_drat": "UNSAT",
                         "proof_drat": 8 + (r // 14),
                         "t_testados": "3;4;5", "pares_ultimo": 1000})
    return rows


# ---------------- coleta ----------------

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
    for s in STRUCT_SEEDS:
        # T_dinamico: gera rank0 para descobrir o complemento
        r0 = gen_tau_at_b(DEPTH, s, 0)
        if r0 is None:
            print(f"  [GEN None] σ={s}")
            skipped += 1
            continue
        T = r0[3]
        todo = [r for r in range(T) if (FAM, str(s), str(r)) not in done]
        if not todo:
            print(f"--- σ={s} (já completa) ---", flush=True)
            continue
        print(f"--- σ={s} (T={T}; {len(todo)} novas; "
              f"max_aux={MAX_AUX:,}) ---", flush=True)
        t_f = time.time()
        for rank in todo:
            nvars, clauses, tag, Tinfo = gen_tau_at_b(DEPTH, s, rank)
            t1 = time.time()
            mr, fecho, info = minref_deep([frozenset(c) for c in clauses],
                                          max_aux=MAX_AUX, with_info=True)
            st_r, len_r = solve_drat(nvars, clauses)
            dt = time.time() - t1
            if dt > 180:
                print(f"    [LENTO {dt/60:.1f}min] σ={s} r={rank} "
                      f"mr={mr if not isinstance(mr, tuple) else '>'}",
                      flush=True)
            if mr is None:
                print(f"  [SAT?!] σ={s} r={rank} — descartado")
                skipped += 1
                continue
            if st_r != "UNSAT":
                print(f"  [BUG ASSERT] σ={s} r={rank}: solve={st_r} — "
                      f"construcao deveria ser UNSAT sempre",
                      flush=True)
                viol += 1
            # ASSERT teorema: minref_exato >= d(vazia)
            if isinstance(mr, int) and info.get("lb") is not None \
                    and mr < info["lb"]:
                viol += 1
                print(f"  [BUG ASSERT] σ={s} r={rank}: minref={mr} < "
                      f"lb={info['lb']} — VIOLACAO DO TEOREMA",
                      flush=True)
            if isinstance(mr, tuple):
                mr_out, censor = f">{mr[1]}({mr[2]})", True
                censored += 1
            else:
                mr_out, censor = mr, False
            rows.append({
                "family": FAM, "param": s, "seed": rank, "tag": tag,
                "nvars": nvars, "nclauses": len(clauses), "fecho": fecho,
                "lb": info.get("lb"),
                "minref": mr_out, "minref_censored": censor,
                "sat_drat": st_r, "proof_drat": len_r,
                "t_testados": ";".join(str(t)
                                      for t in info.get("t_testados", [])),
                "pares_ultimo": (info.get("pares_testados") or [0])[-1],
            })
            write_series(rows)          # checkpoint atomico
        n_done = sum(1 for r in rows if int(r["param"]) == s)
        print(f"  σ={s}: {n_done}/{T} | {time.time()-t_f:.0f}s",
              flush=True)
    print(f"\ncoleta total: {len(rows)} linhas, {censored} censuras, "
          f"{skipped} descartes, ASSERT violacoes={viol}, "
          f"{(time.time()-t_all)/60:.1f}min")
    return rows, viol


def load_series_from_csv():
    return list(csv.DictReader(OUT_SERIES.open(encoding="utf-8")))


# ---------------- análise ----------------

def build_sigma_series(rows):
    """Agrupa por σ: listas (rank ordenado) de minref e drat."""
    by = {}
    for r in rows:
        by.setdefault(int(r["param"]), []).append(r)
    out = {}
    for s, rs in by.items():
        rs.sort(key=lambda r: int(r["seed"]))
        cens = any(str(r["minref_censored"]) == "True" for r in rs)
        mr = [r["minref"] for r in rs]
        dr = [float(r["proof_drat"]) for r in rs
              if r["proof_drat"] not in ("", "None")]
        out[s] = {"rows": rs, "T": len(rs), "censored": cens,
                  "minref": mr, "drat": dr,
                  "sat_all": all(r["sat_drat"] == "UNSAT" for r in rs)}
    return out


def analyze(rows):
    t0 = time.time()
    viol = []
    for r in rows:
        if str(r["minref_censored"]) == "False":
            try:
                if int(r["minref"]) < int(r["lb"]):
                    viol.append((r["param"], r["seed"],
                                 r["minref"], r["lb"]))
            except (TypeError, ValueError):
                pass
    sig = build_sigma_series(rows)
    rng = random.Random(SEED_BOOT)

    # ---- H_b1: viabilidade (σ utilizável) ----
    det = {"completos": [], "nao_degenerados": [], "usaveis": [],
           "censurados": [], "constantes": [], "acf_nan": []}
    D_min, D_drat = {}, {}
    for s in sorted(sig):
        g = sig[s]
        if g["censored"]:
            det["censurados"].append(s)
            continue
        det["completos"].append(s)
        try:
            mr = [int(v) for v in g["minref"]]
        except (TypeError, ValueError):
            det["censurados"].append(s)
            continue
        if len(set(mr)) < 2:
            det["constantes"].append(s)
        d = acf_D(mr, rng)
        if d is None:
            det["acf_nan"].append(s)
            continue
        det["nao_degenerados"].append(s)
        det["usaveis"].append(s)
        D_min[s] = d
        if g["drat"] and len(g["drat"]) == g["T"]:
            dd = acf_D(g["drat"], rng)
            if dd is not None:
                D_drat[s] = dd
    n_us = len(det["usaveis"])
    verdict_b1 = ("CONFIRMADA" if n_us >= 12 else
                  "SEM_DADOS" if n_us < 8 else "REFUTADA")
    hyp_b1 = {"alvo": ">=12/32 σ's utilizáveis (completos + não-degenerados)",
              "n_usaveis": n_us, "detalhe": {k: v for k, v in det.items()},
              "veredito": verdict_b1}

    # ---- H_b2: estrutura serial (primária, dirn=-1 alternância) ----
    vals = [D_min[s] for s in sorted(D_min)]
    c = contrast_over_sigma(vals, rng) if len(vals) >= 8 else None
    verdict_b2 = classify_dirn(c, -1)
    hyp_b2 = {"enunciado": ("D_σ = acf1(real) - media_1000 acf1"
                            "(permutacoes internas); media sobre σ; "
                            "bootstrap percentil primario + BCa + regra "
                            "2 niveis; dirn=-1 (alternância/anti-"
                            "persistência — base sonda σ=5000, D=-0,36); "
                            "α=0.05 unica confirmatoria"),
              "n_sigma": len(vals), "dado": c, "veredito": verdict_b2,
              "D_por_sigma": {str(s): round(D_min[s], 4)
                              for s in sorted(D_min)}}

    # ---- H_b3 descritiva: minref vs drat (sem claim) ----
    pares = sorted(set(D_min) & set(D_drat))
    h3 = {"nota": "(P)/candidata (C) — DESCRIPTIVA, sem claim",
          "n_pares": len(pares),
          "media_D_minref": (sum(D_min[s] for s in pares) / len(pares)
                             if pares else None),
          "media_D_drat": (sum(D_drat[s] for s in pares) / len(pares)
                           if pares else None),
          "contraste": (contrast_over_sigma(
              [D_min[s] - D_drat[s] for s in pares], rng)
              if len(pares) >= 8 else None)}

    # ---- tabelas por σ + métricas descritivas ----
    tab = {}
    for s in sorted(sig):
        g = sig[s]
        mr = []
        try:
            mr = [int(v) for v in g["minref"]]
        except (TypeError, ValueError):
            pass
        entry = {"T": g["T"], "censored": g["censored"],
                 "minref_dist": (sorted(set(mr)) if mr else None),
                 "minref_mean": (sum(mr) / len(mr)) if mr else None,
                 "drat_mean": (sum(g["drat"]) / len(g["drat"]))
                 if g["drat"] else None,
                 "D_minref": D_min.get(s), "D_drat": D_drat.get(s),
                 "metricas_minref": {}, "metricas_drat": {}}
        if mr:
            for name, fn in (("boxdim", boxdim_curve),
                             ("boxdim_rank", boxdim_rank),
                             ("saltos", taxa_saltos),
                             ("higuchi_D", higuchi_D),
                             ("hurst_rs", hurst_rs)):
                v = fn(mr)
                entry["metricas_minref"][name] = (
                    None if v is None or (isinstance(v, float)
                                          and math.isnan(v)) else round(v, 4))
        if g["drat"]:
            for name, fn in (("boxdim", boxdim_curve),
                             ("boxdim_rank", boxdim_rank),
                             ("saltos", taxa_saltos)):
                v = fn(g["drat"])
                entry["metricas_drat"][name] = (
                    None if v is None or (isinstance(v, float)
                                          and math.isnan(v)) else round(v, 4))
        tab[str(s)] = entry

    out = {"H_b1_viabilidade": hyp_b1, "H_b2_estrutura": hyp_b2,
           "H_b3_descritiva": h3,
           "_assert": {"violacoes": viol,
                       "veredito": ("OK (minref >= d(vazia) em todas)"
                                    if not viol
                                    else f"BUG ({len(viol)} violacoes)")},
           "tabelas": tab,
           "_diag": {"n_rows": len(rows), "n_sigma": len(sig),
                     "n_usaveis": n_us,
                     "censuras_total": sum(
                         1 for r in rows
                         if str(r["minref_censored"]) == "True")}}
    print("\n--- hipoteses ---")
    print(f"  H_b1: {hyp_b1['veredito']} "
          f"({n_us}/32 σ's utilizáveis; censurados="
          f"{len(det['censurados'])}, constantes="
          f"{len(det['constantes'])}, acf_nan="
          f"{len(det['acf_nan'])})")
    d2 = c or {}
    print(f"  H_b2: {verdict_b2} (n={len(vals)}) "
          + (f"point={d2['point']:+.4f} pct=[{d2['pct_lo']:+.4f},"
             f"{d2['pct_hi']:+.4f}] bca=[{d2['bca_lo']:+.4f},"
             f"{d2['bca_hi']:+.4f}] mde={d2['mde80']:.4f} "
             f"z0={d2.get('z0')}" if d2 else "(SEM_DADOS)"))
    print(f"  H_b3 (descritiva): pares={h3['n_pares']} "
          f"D_minref={h3['media_D_minref']} D_drat={h3['media_D_drat']}")
    print(f"  ASSERT: {out['_assert']['veredito']}")
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
    print("SÉRIES EM B — índice lex de b para σ fixo (D4' doc28 §7.3)")
    print("=" * 70)

    s1 = selftest_bca_scipy()
    s3 = selftest_s3()
    s4 = selftest_s4()
    s6 = selftest_s6()
    smk = smoke_analyze()
    disj = check_disjoint()
    print(f"\n[S1] BCa vs scipy: {s1['status']} "
          f"(diff={s1.get('max_diff')})")
    print(f"[S3] maquina completa: tipo-I={s3['S3a_tipo1']['exclusoes']}"
          f"/{s3['S3a_tipo1']['n']}={s3['S3a_tipo1']['taxa']:.3f} "
          f"(gate<=0.15) poder={s3['S3b_poder']['detectou']}/"
          f"{s3['S3b_poder']['n']} (gate>=7) {s3['status']}")
    print(f"[S4] metricas T=28: {s4['status']} (inv_err="
          f"{s4['inv_err']:.1e}, hurst_nan={s4['hurst_nan_esperado']}, "
          f"higuchi_nan={s4['higuchi_nan_esperado']})")
    print(f"[S6] drat deterministico: {s6['status']} "
          f"({s6['run1']} vs {s6['run2']})")
    print(f"[S5] smoke analyze: {smk['status']}")
    print(f"[DISJ] v2..v6+tau_kup vs grade: {disj['status']} "
          f"interseccao={disj.get('interseccao')}")
    ok = (s1["status"] in ("OK", "scipy ausente — pulado")
          and s3["status"] == "OK" and s4["status"] == "OK"
          and s6["status"] == "OK" and smk["status"] == "OK"
          and disj["status"] in ("OK",
                                 "AVISO: CSVs anteriores ausentes — pulado"))
    if not ok:
        print(f"[ABORTA] selftests: disj={disj['status']} "
              f"smk={smk['status']} s3={s3['status']} s4={s4['status']} "
              f"s6={s6['status']}")
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
            grid_keys = {(FAM, str(s), str(r))
                         for s in STRUCT_SEEDS for r in range(64)}
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
        "b_shuf": B_SHUF,
        "config": f"k={K} w={W} depth={DEPTH} (nvars=7, T=28-29)",
        "max_aux": MAX_AUX,
        "grade": (f"family={FAM}, σ=6000..6031 (S=32), b_rank=0..T_σ-1 "
                  f"(lex), DISJ sondas 5000-5004 e r2..τk↑"),
        "gerador": ("estrutura fixa por (depth,struct_seed) no namespace "
                    "'tau_b'; b = complemento ordenado lex"),
        "runtime_s": round(time.time() - t0, 1),
        "caveats": [
            ("Pré-registro: hipóteses/regras/grade fixadas neste código e "
             "no doc 35_ ANTES do run (C1)."),
            ("Direção H_b2 (-1 alternância) baseada em sonda de "
             "engenharia σ=5000 (D=-0,36) — caveat declarado; métrica "
             "primária trocada de saltos p/ acf1 ANTES do commit "
             "(S3 pegou degeneração de saltos em série binária)."),
            ("higuchi (n>=32) e hurst (n>=36) NaN em T=28 — contrato "
             "S4; não usados em claim."),
            ("σ's não utilizáveis excluídos do H_b2 (regra "
             "pré-declarada; contagem no H_b1)."),
            ("H_b3 descritiva — candidata (C), sem claim."),
            ("N1+N2; sem N4; H_C2 (EF) deferido."),
        ],
    }
    payload = {
        "metadata": {**meta,
                     "data_source": "gk_series_b.py (séries em b — "
                                    "índice lex de b, σ fixo)",
                     "instances": {"rows": len(rows),
                                   "censuras": results["_diag"]
                                   ["censuras_total"],
                                   "n_sigma": results["_diag"]["n_sigma"],
                                   "n_usaveis": results["_diag"]
                                   ["n_usaveis"]},
                     "selftests": {"S1_bca_scipy": s1, "S3_maquina": s3,
                                   "S4_metricas": s4, "S6_drat": s6,
                                   "S5_smoke": smk, "DISJ": disj},
                     "csv": OUT_SERIES.name,
                     "csv_sha256": _sha(OUT_SERIES),
                     "sha_note": "sha256 bytes normalizados CRLF->LF"},
        "pre_registro": {
            "H_b1": (">=12/32 σ's utilizáveis (completos + "
                     "não-degenerados)"),
            "H_b2": ("estrutura serial em b: D_σ = acf1(real) - "
                     "media acf1(permutacoes); bootstrap sobre σ; "
                     "dirn=-1 (alternância); α=0.05 unica confirmatoria"),
            "H_b3": "descritiva (sem claim)",
            "ASSERT": "minref_exato >= d(vazia) por instancia",
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

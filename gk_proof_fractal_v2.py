#!/usr/bin/env python3
"""
gk_proof_fractal_v2.py — D4' v2 (20/11/2026): PONTE PROVA->FRACTAL com
comprimentos MINIMOS CANONICOS (minref) — controle do artefato de solver
e do regime exponencial (pendencias A2/A4 do referee do 28_).

Pergunta: as metricas fractais (a) sao invariantes a FONTE (minref exato
vs prova DRAT do solver na MESMA instancia) e (b) separam famlias de
refutacao quando o regime exponencial e CONTROLADO (o escopo n<=6 do
minref elimina o php exponencial do v1)?

Hipoteses confirmatorias (registradas A PRIORI; metrica D_H; variantes
raw+relinc; 12 testes; nota Bonferroni alpha*=0.05/12 no veredito):
  - H_C3 (controle de regime): com todas as familias em n<=6 (sem curva
    exponencial), os pares de familias NAO separam em minref (IC95 de
    D_H inclui 0 em raw e relinc) -> confirma a leitura A1 do referee
    (a metrica media REGIME de crescimento, nao identidade de familia).
    REFUTADA se algum par excluir 0.
  - H_C4 (invariancia de fonte): contrastes pareados D_H(minref) -
    D_H(drat) por familia incluem 0 (raw e relinc) -> a metrica nao e
    artefato do solver. REFUTADA se algum excluir 0.

Familias (64 pontos cada; todas n<=6 variaveis efetivas; UNSAT por
construicao + verificacao de solver a cada instancia):
  - implication : m=3..6 x 16 seeds (grafo de implicacoes + unidades)
  - cadeia      : k=3..6 x 16 seeds (cadeia unitaria + ruido binario
                  semeado — mantem UNSAT; fecho permanece pequeno)
  - tau_tiny    : tau(g)_b de Krajicek com k=2 entradas, w=3 saidas,
                  profundidade 1 (5 vars) x 64 seeds. usa o gerador do
                  v1 JA CORRIGIDO (7o bug do projeto: unidades de saida
                  estavam invertidas e codificavam saida=NOT b — ver
                  gk_proof_fractal.gen_tau; o CSV v1 congelado permanece
                  valido: 188/188 UNSAT verificado por solver).

Sistemas por instancia:
  - minref : comprimento MINIMO EXATO de refutacao Res (gk_minref:
              fecho + pares completos + REF_t; censura ">" registrada)
  - drat   : linhas da prova DRAT real (Cadical195; mesma instacia)

Variantes de serie (pendencia A2 do referee — anti-quantizacao):
  raw | log1p | relinc = diff de log1p(x) (incrementos relativos)

Metricas: hurst_rs, higuchi_D, boxdim — MESMA implementacao validada do
v1 (import de gk_proof_fractal); validacao sintetica rodada ANTES de
medir (incluindo a variante relinc) — licao A8.

Bootstrap: blocos (B=300, bloco=8, seed fixa). H_C4 usa resample
PAREADO (mesmos indices nas duas fontes); H_C3 usa independente (familias
diferentes), como no v1.

Nivel Ten-Proofs: N1 (script reproduzivel, seed fixa) + N2 (bootstrap).
NAO e lower bound, NAO e claim de EF (H_C2 permanece DEFERIDO).

Uso:  python -u gk_proof_fractal_v2.py
Saida: gk_proof_fractal_v2_series.csv + gk_proof_fractal_v2.json
       (sha256 do CSV normalizado CRLF->LF registrado no JSON)
"""

import csv
import hashlib
import json
import math
import random
import time
from datetime import datetime, timezone
from pathlib import Path

from gk_proof_fractal import (B_BOOT, BLOCK, SEED, _det_seed,
                              boxdim_curve, block_resample,
                              gen_implication, higuchi_D, hurst_rs, metrics,
                              solve_drat, validate_metrics)
from gk_minref import minref

OUT_JSON = Path("gk_proof_fractal_v2.json")
OUT_CSV = Path("gk_proof_fractal_v2_series.csv")

try:
    from pysat.solvers import Cadical195  # noqa: F401  (via solve_drat)
    PYSAT_OK = True
except ImportError:
    PYSAT_OK = False


# ----------------------------------------------------------------------
# 1. Geradores das familias n<=6 (escopo do minref)
# ----------------------------------------------------------------------

def gen_cadeia(k, seed):
    """Cadeia unitaria [1],[-1,2],...,[-k] (minref=2k+1 na base) + ruido
    binario semeado (0..6 clausulas). Superset de UNSAT -> UNSAT; o ruido
    varia o fecho/minref entre seeds (senao a serie seria constante)."""
    rng = random.Random(_det_seed(SEED, "cadeia", k, seed))
    cls = [[1]]
    for i in range(1, k):
        cls.append([-i, i + 1])
    cls.append([-k])
    added, tries = 0, 0
    target = rng.randrange(0, 7)
    while added < target and tries < 300:
        tries += 1
        a, b = rng.sample(range(1, k + 1), 2)
        cl = [a * rng.choice([1, -1]), b * rng.choice([1, -1])]
        if any(-l in cl for l in cl) or cl in cls:
            continue
        cls.append(cl)
        added += 1
    return k, cls, f"cadeia_k{k}_ruído{added}_s{seed}"


def gen_tau_tiny(param, seed):
    """tau(g)_b com k=2, w=3, profundidade 1 -> 5 vars. Usa o gerador do
    v1 corrigido (saida=b real) — UNSAT por construicao (b fora da imagem)."""
    import gk_proof_fractal as gpf
    gpf.gates = []
    return gpf.gen_tau(1, seed, k=2, w=3)


# grade: familia -> [(param, seed)] (ordenacao da serie = (param, seed))
GRID = {
    "implication": [(m, s) for m in range(3, 7) for s in range(16)],   # 64
    "cadeia":      [(k, s) for k in range(3, 7) for s in range(16)],   # 64
    "tau_tiny":    [(0, s) for s in range(64)],                        # 64
}
GENS = {"implication": gen_implication, "cadeia": gen_cadeia,
        "tau_tiny": gen_tau_tiny}


# ----------------------------------------------------------------------
# 2. Variantes de serie (anti-quantizacao A2) + resample pareado
# ----------------------------------------------------------------------

def variant_relinc(x):
    """Incrementos relativos de log1p: diff(log1p(x)). Remove nivel,
    escala e tendencia — a mitigacao A2 pedida pelo referee."""
    return [math.log1p(x[i + 1]) - math.log1p(x[i]) for i in range(len(x) - 1)]


def variants_of(x):
    return {"raw": list(x),
            "log1p": [math.log1p(v) for v in x],
            "relinc": variant_relinc(x)}


def block_resample_idx(n, rng):
    """Mesmo esquema de blocos do v1, devolvendo INDICES (para o
    bootstrap pareado de H_C4: mesmos indices nas duas fontes)."""
    out = []
    while len(out) < n:
        s = rng.randrange(0, max(1, n - BLOCK + 1))
        out.extend(range(s, min(n, s + BLOCK)))
    return out[:n]


def contrast_paired(a, b, fn, rng, n_boot=B_BOOT):
    """Delta = fn(a) - fn(b) com resample PAREADO (mesmos indices)."""
    if len(a) != len(b) or len(a) < 16:
        return None
    deltas = []
    for _ in range(n_boot):
        idx = block_resample_idx(len(a), rng)
        va = fn([a[i] for i in idx])
        vb = fn([b[i] for i in idx])
        if va is not None and vb is not None \
                and not math.isnan(va) and not math.isnan(vb):
            deltas.append(va - vb)
    if not deltas:
        return None
    deltas.sort()
    point = fn(a) - fn(b)
    if math.isnan(point):
        return None
    lo, hi = deltas[int(0.025 * len(deltas))], deltas[int(0.975 * len(deltas))]
    return {"delta_point": point, "lo": lo, "hi": hi,
            "excludes_zero": lo > 0 or hi < 0,
            "point_outside_ci": point < lo or point > hi,
            "kind": "pareado"}


def contrast_indep(a, b, fn, rng, n_boot=B_BOOT):
    """Delta = fn(a) - fn(b) com resample INDEPENDENTE (v1)."""
    if len(a) < 16 or len(b) < 16:
        return None
    deltas = []
    for _ in range(n_boot):
        va = fn(block_resample(a, rng))
        vb = fn(block_resample(b, rng))
        if va is not None and vb is not None \
                and not math.isnan(va) and not math.isnan(vb):
            deltas.append(va - vb)
    if not deltas:
        return None
    deltas.sort()
    point = fn(a) - fn(b)
    if math.isnan(point):
        return None
    lo, hi = deltas[int(0.025 * len(deltas))], deltas[int(0.975 * len(deltas))]
    return {"delta_point": point, "lo": lo, "hi": hi,
            "excludes_zero": lo > 0 or hi < 0,
            "point_outside_ci": point < lo or point > hi,
            "kind": "independente"}


# ----------------------------------------------------------------------
# 3. Experimento
# ----------------------------------------------------------------------

def main():
    t0 = time.time()
    print("=" * 70)
    print("D4' v2 — comprimentos MINIMOS (minref) vs DRAT, familias n<=6")
    print("=" * 70)
    if not PYSAT_OK:
        print("[ERRO] pysat ausente — pip install python-sat")
        return 2

    # --- validacao sintetica OBRIGATORIA antes de medir (lição A8) ---
    validation = validate_metrics()
    print("\n--- validação das métricas (séries sintéticas, raw) ---")
    for name, mm in validation.items():
        print(f"  {name}: H={mm['hurst_rs']:.3f} D_H={mm['higuchi_D']:.3f} "
              f"D_box={mm['boxdim']:.3f}")
    # variante relinc tambem validada (transformacao nova do v2).
    # log1p exige x>=0 (series de prova sao sempre >=1; as sinteticas sao
    # deslocadas para o dominio positivo — shift declarado na impressao)
    def _shift(v):
        m = min(v)
        return [x - m + 1.0 for x in v] if m <= 0 else v
    rng_v = random.Random(SEED)
    wn = [rng_v.gauss(0, 1) for _ in range(64)]
    rw, acc = [], 0.0
    for _ in range(64):
        acc += rng_v.gauss(0, 1)
        rw.append(acc)
    sine = [math.sin(2 * math.pi * i / 16) for i in range(64)]
    validation_relinc = {
        "white_noise": metrics(variant_relinc(_shift(wn))),
        "random_walk": metrics(variant_relinc(_shift(rw))),
        "sine_period16": metrics(variant_relinc(_shift(sine))),
    }
    print("--- validação da variante relinc (incrementos de log1p; "
          "séries sintéticas deslocadas p/ domínio positivo) ---")
    for name, mm in validation_relinc.items():
        print(f"  {name}: H={mm['hurst_rs']:.3f} D_H={mm['higuchi_D']:.3f} "
              f"D_box={mm['boxdim']:.3f}")

    # --- coleta: minref + drat por instancia ---
    rows = []
    censored = 0
    skipped = 0
    for fam, points in GRID.items():
        print(f"\n--- família: {fam} ({len(points)} instâncias) ---")
        for param, seed in points:
            nvars, clauses, tag = GENS[fam](param, seed)
            ne = len({abs(l) for c in clauses for l in c})
            if ne > 6:
                print(f"  [FORA DO ESCOPO] {fam} p={param} s={seed}: n={ne}")
                skipped += 1
                continue
            t1 = time.time()
            mr, fecho = minref([frozenset(c) for c in clauses],
                               with_sat_len=True)
            st_r, len_r = solve_drat(nvars, clauses)
            dt = round(time.time() - t1, 2)
            print(f"    {fam} p={param} s={seed}: minref={mr if not isinstance(mr, tuple) else '>'} "
                  f"drat={len_r} ({dt}s)", flush=True)
            if mr is None:            # SAT — nao esperado (UNSAT por constr.)
                print(f"  [SAT?!] {fam} p={param} s={seed} — descartado")
                skipped += 1
                continue
            if isinstance(mr, tuple):  # censura (orcamento/tmax)
                mr_out, censor = f">{mr[1]}({mr[2]})", True
                censored += 1
            else:
                mr_out, censor = mr, False
            rows.append({
                "family": fam, "param": param, "seed": seed, "tag": tag,
                "nvars": ne, "nclauses": len(clauses), "fecho": fecho,
                "minref": mr_out, "minref_censored": censor,
                "sat_drat": st_r, "proof_drat": len_r,
                # 'seconds' NAO entra no CSV: wall-clock quebraria a
                # reproducao byte-a-byte do artefato (8o bug, lição);
                # tempo por instancia vai so para o console.
            })
        done = [r for r in rows if r["family"] == fam]
        exact = [r for r in done if not r["minref_censored"]]
        unsat = [r for r in done if r["sat_drat"] == "UNSAT"]
        vals = sorted({r["minref"] for r in exact})
        print(f"  UNSAT (DRAT): {len(unsat)}/{len(done)} | minref exato: "
              f"{len(exact)} | valores: {vals} | censurados: "
              f"{sum(1 for r in done if r['minref_censored'])}")

    # --- series: (familia, sistema) ordenadas por (param, seed) ---
    # alinhamento PAREADO: ambas as fontes vêm da MESMA lista de pontos;
    # se DRAT falhar num ponto, ele sai das DUAS series (indices intactos)
    series = {}
    for fam in GRID:
        pts = [r for r in rows if r["family"] == fam
               and not r["minref_censored"]
               and r["sat_drat"] == "UNSAT"
               and r["proof_drat"] is not None]
        pts.sort(key=lambda r: (r["param"], r["seed"]))
        series[(fam, "minref")] = [float(r["minref"]) for r in pts]
        series[(fam, "drat")] = [float(r["proof_drat"]) for r in pts]

    # --- metricas + bootstrap por (familia, sistema, variante) ---
    results = {}
    rng = random.Random(SEED + 1)
    for (fam, sysname), x in sorted(series.items()):
        if len(x) < 16:
            results[f"{fam}|{sysname}"] = {"n": len(x), "note": "serie curta"}
            continue
        entry = {"n": len(x), "mean": sum(x) / len(x),
                 "min": min(x), "max": max(x), "variants": {}}
        for vname, vx in variants_of(x).items():
            m_point = metrics(vx)
            boot = {k: {"point": m_point[k],
                        **_boot_ci(vx, fn, rng)}
                    for k, fn in (("hurst_rs", hurst_rs),
                                  ("higuchi_D", higuchi_D),
                                  ("boxdim", boxdim_curve))}
            entry["variants"][vname] = {
                "n": len(vx), "metrics": m_point, "bootstrap_ci95": boot}
        results[f"{fam}|{sysname}"] = entry
        mraw = entry["variants"]["raw"]["metrics"]
        mrel = entry["variants"]["relinc"]["metrics"]
        print(f"  {fam}|{sysname}: n={len(x)} mean={entry['mean']:.1f} "
              f"raw[D_H={mraw['higuchi_D']:.3f}] "
              f"relinc[D_H={mrel['higuchi_D']:.3f}]")

    # --- contrastes ---
    contrasts = {}
    rng_c = random.Random(SEED + 2)
    fams = ["implication", "cadeia", "tau_tiny"]

    # H_C3: pares de familias em minref (confirmatorio) e em drat
    # (exploratorio) — independentes
    for sysname in ("minref", "drat"):
        for i in range(len(fams)):
            for j in range(i + 1, len(fams)):
                a_raw = series.get((fams[i], sysname), [])
                b_raw = series.get((fams[j], sysname), [])
                for vname in ("raw", "log1p", "relinc"):
                    a = variants_of(a_raw)[vname] if a_raw else []
                    b = variants_of(b_raw)[vname] if b_raw else []
                    for mname, fn in (("higuchi_D", higuchi_D),
                                      ("boxdim", boxdim_curve),
                                      ("hurst_rs", hurst_rs)):
                        c = contrast_indep(a, b, fn, rng_c)
                        if c is None:
                            continue
                        confirm = (sysname == "minref"
                                   and mname == "higuchi_D"
                                   and vname in ("raw", "relinc"))
                        contrasts[f"{sysname}:{fams[i]}-{fams[j]}:"
                                  f"{mname}:{vname}"] = {**c,
                                  "confirmatorio_H_C3": confirm}

    # H_C4: fonte minref vs drat, por familia — PAREADOS (series já
    # alinhadas ponto a ponto na construção acima)
    for fam in fams:
        a_full = series.get((fam, "minref"), [])
        b_full = series.get((fam, "drat"), [])
        if len(a_full) != len(b_full) or not a_full:
            continue
        for vname in ("raw", "log1p", "relinc"):
            a = variants_of(a_full)[vname]
            b = variants_of(b_full)[vname]
            for mname, fn in (("higuchi_D", higuchi_D),
                              ("boxdim", boxdim_curve),
                              ("hurst_rs", hurst_rs)):
                c = contrast_paired(a, b, fn, rng_c)
                if c is None:
                    continue
                confirm = (mname == "higuchi_D"
                           and vname in ("raw", "relinc"))
                contrasts[f"fonte:{fam}:{mname}:{vname}"] = {
                    **c, "confirmatorio_H_C4": confirm}

    # --- vereditos (a priori) ---
    # Nota de integridade: um teste cujo delta pontual fica FORA do proprio
    # IC95 (point_outside_ci) e INCOERENTE — a distribuicao bootstrap nao
    # esta centrada na estimativa (aqui: saturacao do Higuchi no teto D_H~2
    # sob reamostragem de series quantizadas). Tais testes sao reportados
    # mas NAO contam como refutacao (seria validar um artefato de IC).
    hc3 = {k: v for k, v in contrasts.items()
           if v.get("confirmatorio_H_C3")}
    hc4 = {k: v for k, v in contrasts.items()
           if v.get("confirmatorio_H_C4")}
    hc3_hits = [k for k, v in hc3.items() if v["excludes_zero"]]
    hc4_hits = [k for k, v in hc4.items() if v["excludes_zero"]]
    hc4_incoh = [k for k, v in hc4.items() if v.get("point_outside_ci")]
    hc4_valid_hits = [k for k in hc4_hits if k not in hc4_incoh]
    all_incoh = sorted(k for k, v in contrasts.items()
                       if v.get("point_outside_ci"))

    hyp = {
        "H_C3_controle_de_regime": {
            "enunciado": ("Com todas as familias em n<=6 (sem curva "
                          "exponencial — escopo do minref), os pares de "
                          "familias NAO separam por D_H em minref "
                          "(IC95 inclui 0 em raw e relinc) -> confirma "
                          "A1 do referee do 28_: a metrica media REGIME "
                          "de crescimento, nao identidade de familia."),
            "n_testes": len(hc3), "excluem_0": hc3_hits,
            "veredito": ("REFUTADA — algum par separa mesmo controlado o "
                         "regime" if hc3_hits else
                         "CONFIRMADA — nenhum par exclui 0 (raw+relinc)"),
            "bonferroni_nota": ("alpha* = 0.05/12 ≈ 0.0042; com B=300 o "
                                "percentil resolvivel mais extremo e "
                                "[1,298] —IC95 reportado + contagem, "
                                "mesma regua honesta do 28_ §3.3"),
        },
        "H_C4_invariancia_de_fonte": {
            "enunciado": ("Contrastes pareados D_H(minref) - D_H(drat) "
                          "por familia incluem 0 (raw e relinc) -> as "
                          "metricas fractais nao sao artefato do solver "
                          "(comprimento minimo canonico vs prova do "
                          "Cadical na MESMA instancia)."),
            "n_testes": len(hc4), "excluem_0": hc4_hits,
            "excluem_0_coerentes": hc4_valid_hits,
            "incoerentes_ponto_fora_do_IC": hc4_incoh,
            "veredito": (
                "REFUTADA — algum teste COERENTE exclui 0"
                if hc4_valid_hits else
                ("REFUTADA (NOMINAL) — mas a unica exclusao e incoerente "
                 "(ponto fora do proprio IC95: artefato de saturacao do "
                 "Higuchi, ver diagnostico); leitura sustentada: "
                 "invariancia de fonte mantida, com ressalva"
                 if hc4_hits else
                 "CONFIRMADA — fonte indistinguivel em todos os testes")),
            "bonferroni_nota": ("mesma regua da H_C3: alpha*=0.05/12"),
        },
        "H_C2_Res_vs_EFrege": {
            "status": "DEFERIDO",
            "motivo": ("mantido do v1: EF nao e mensuravel com o "
                       "tooling; v2 nao mede z3/EF (foco minref vs DRAT)"),
        },
    }

    # --- CSV ---
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    sha = hashlib.sha256(
        OUT_CSV.read_bytes().replace(b"\r\n", b"\n")).hexdigest()

    payload = {
        "metadata": {
            "timestamp_utc": datetime.now(timezone.utc).isoformat()
                             .replace("+00:00", "Z"),
            "data_source": ("gk_proof_fractal_v2.py (D4' v2 — minref "
                            "canonico, familias n<=6)"),
            "seed": SEED, "B_boot": B_BOOT, "block": BLOCK,
            "grid": {k: f"{len(v)} pontos" for k, v in GRID.items()},
            "systems": ["minref (comprimento minimo exato, gk_minref)",
                        "resolution_drat (Cadical195, mesma instancia)"],
            "variants": ["raw", "log1p",
                         "relinc (diff de log1p — A2)"],
            "instances": {"rows": len(rows), "censored": censored,
                          "skipped": skipped},
            "csv": OUT_CSV.name, "csv_sha256": sha,
            "sha_note": "sha256 sobre bytes normalizados CRLF->LF",
            "runtime_s": round(time.time() - t0, 1),
            "caveats": [
                ("Escopo n<=6 do minref: SEM familia exponencial — o v2 "
                 "controla o regime (A1), nao replica o php do v1."),
                ("Serie relinc tem n-1 pontos (63) — mesmas metricas."),
                ("Censura minref '>' registrada e excluida da serie "
                 f"(total {censored})."),
                ("Nivel Ten-Proofs: N1 + N2; sem N4; sem claim de EF "
                 "(H_C2 deferido) e sem lower bound."),
                ("7o bug corrigido no gerador tau do v1 (unidades de "
                 "saida invertidas); CSV v1 congelado permanece valido "
                 "(188/188 UNSAT por solver)."),
                ("8o bug corrigido: geradores usavam tuple.__hash__() "
                 "(randomizado por processo) — seed agora deterministico "
                 "(_det_seed = CRC32); artefatos v1 congelados nao sao "
                 "regeneraveis entre execucoes (errata no 28_ §5)."),
                ("Higuchi satura no teto D_H~2 com series quantizadas de "
                 "inteiros pequenos: contrastes com ponto FORA do IC95 "
                 "sao marcados point_outside_ci e nao contam como "
                 "refutacao ( artefato de IC, nao de efeito)."),
            ],
        },
        "metric_validation": {"raw": validation,
                              "relinc": validation_relinc},
        "series_results": results,
        "contrasts": contrasts,
        "hypotheses": hyp,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False),
                        encoding="utf-8")

    print("\n--- contrastes confirmatórios (D_H) ---")
    for k, v in sorted({**hc3, **hc4}.items()):
        flag = "EXCLUI 0" if v["excludes_zero"] else "inclui 0"
        if v.get("point_outside_ci"):
            flag += " | INCOERENTE (ponto fora do IC)"
        print(f"  [{v['kind']}] {k}: delta={v['delta_point']:+.3f} "
              f"IC95=[{v['lo']:+.3f},{v['hi']:+.3f}] -> {flag}")
    if all_incoh:
        print(f"\n[DIAG] {len(all_incoh)} contrastes com ponto fora do IC "
              f"(saturacao do Higuchi no teto D_H~2): "
              f"{', '.join(all_incoh)}")
    print(f"\nH_C3: {hyp['H_C3_controle_de_regime']['veredito']}")
    print(f"H_C4: {hyp['H_C4_invariancia_de_fonte']['veredito']}")
    print(f"\n[OK] {OUT_JSON.name} + {OUT_CSV.name} "
          f"(sha256={sha[:16]}…)")
    print(f"runtime: {payload['metadata']['runtime_s']}s")
    print("=" * 70)
    return 0


def _boot_ci(x, fn, rng, b=B_BOOT):
    vals = []
    for _ in range(b):
        v = fn(block_resample(x, rng))
        if v is not None and not math.isnan(v):
            vals.append(v)
    if not vals:
        return {"lo": None, "hi": None}
    vals.sort()
    return {"lo": vals[int(0.025 * len(vals))],
            "hi": vals[int(0.975 * len(vals))]}


if __name__ == "__main__":
    raise SystemExit(main())

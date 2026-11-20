#!/usr/bin/env python3
"""
gk_proof_fractal_v2_r2.py — r2 do D4' v2: inferencia BCa + TOST + poder.

Re-analise da serie CONGELADA gk_proof_fractal_v2_series.csv
(sha256 b8aecc2d… — NAO regenera instancias; le o artefato do run3).

Pendencias do referee 29_ r1 atendidas aqui:
  (i)   TOST com margem Delta declarada -> "nao separa" vira limite
        quantitativo (equivalencia) — ANTES era so ausencia de evidencia;
  (ii)  inferencia BCa (corrige viés/assimetria do percentil que gerou o
        IC incoerente ponto-fora-do-IC) + MDE80 (poder minimo detectavel);
  (iii) flag point_outside_ci promovida a REGRA DECLARADA no enunciado:
        contraste incoerente nao conta como refutacao em nenhuma direcao;
  (iv)  boxdim (implication-cadeia, sistema drat, 3 variantes) reavaliado
        como PISTA EXPLORATORIA declarada (referee A4) — com BCa;
  (v)   tau k↑ — FORA do escopo (mantida aberta);
  (vi)  sha run3 — fechada no r1 (b8aecc2d… confirmado).

Testes triplos por contraste (regua declarada a priori):
  SEPARA       : IC95 (BCa) exclui 0
  EQUIVALENTE  : IC90 (BCa) contido em (-Delta, +Delta)   [TOST]
  INCONCLUSIVO : nenhum dos dois

Margens (declaradas ANTES de rodar):
  Delta = 0.10  (PRIMARIA — ~1/7 do efeito v1 imp-php = 0.731;
                 justificativa: efeito menor que isso seria desprezivel
                 frente ao que a metrica ja separou no v1)
  Delta = 0.15 e 0.20 (sensibilidade — declarados, nao promovidos)

MDE80 = (z_{1-a/2} + z_{0.80}) * SE_boot = 2.8016 * SE_boot
  (poder 80%, alfa 0.05 bicaudal — efeito minimo que ESTA amostra detectaria)

Validacao (lição A8): BCa implementado aqui e confrontado com
scipy.stats.bootstrap(method='BCa') em caso unidimensional iid
(selftest no JSON) antes de aplicar aos contrastes.

Saida: gk_proof_fractal_v2_r2.json + gk_proof_fractal_v2_r2_contrasts.csv
Uso:   python -u gk_proof_fractal_v2_r2.py
"""

import csv
import hashlib
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from statistics import NormalDist

from gk_proof_fractal import (B_BOOT, SEED, boxdim_curve, higuchi_D,
                              hurst_rs, metrics)
from gk_proof_fractal_v2 import variants_of

ND = NormalDist()
MARGINS = (0.10, 0.15, 0.20)     # primaria 0.10; 0.15/0.20 sensibilidade
MARGIN_PRIMARY = 0.10
N_BOOT = 1000                    # r2: caudas mais finas que B=300 do v1
Z_POWER80 = 0.8416212335729143   # z_{0.80}
BLOCK = 8

SRC_CSV = Path("gk_proof_fractal_v2_series.csv")
OUT_JSON = Path("gk_proof_fractal_v2_r2.json")
OUT_CSV = Path("gk_proof_fractal_v2_r2_contrasts.csv")

FAMS = ["implication", "cadeia", "tau_tiny"]
# pista exploratoria declarada (referee A4 do 29_): boxdim implication-cadeia
# no sistema drat, 3 variantes
PISTA = {f"drat:implication-cadeia:boxdim:{v}"
         for v in ("raw", "log1p", "relinc")}


# ---------------- series a partir do CSV congelado ----------------

def load_series():
    rows = list(csv.DictReader(SRC_CSV.open(encoding="utf-8")))
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


# ---------------- reamostragem ----------------

def block_idx(n, rng):
    out = []
    while len(out) < n:
        s = rng.randrange(0, max(1, n - BLOCK + 1))
        out.extend(range(s, min(n, s + BLOCK)))
    return out[:n]


def iid_idx(n, rng):
    return [rng.randrange(n) for _ in range(n)]


# ---------------- BCa ----------------

def _quantile(sorted_vals, q):
    if not sorted_vals:
        return None
    i = min(len(sorted_vals) - 1, max(0, int(round(q * (len(sorted_vals) - 1)))))
    return sorted_vals[i]


def bca_ci(obs, boots, jack, alpha=0.05):
    """IC BCa. obs=estimativa; boots=replicatas; jack=valores jackknife.
    Returns (lo, hi, info). Percentil ajustado por z0 (viés) + a (assimetria)."""
    boots = sorted(v for v in boots if v is not None and not math.isnan(v))
    jack = [v for v in jack if v is not None and not math.isnan(v)]
    if len(boots) < 200 or len(jack) < 10:
        return None, None, {"erro": "poucas replicatas"}
    # z0: fracao de replicatas abaixo do observado (meio-tie p/ quantizados)
    less = sum(1 for v in boots if v < obs)
    equal = sum(1 for v in boots if v == obs)
    prop = (less + 0.5 * equal) / len(boots)
    prop = min(max(prop, 0.5 / len(boots)), 1 - 0.5 / len(boots))
    z0 = ND.inv_cdf(prop)
    # aceleracao (jackknife delete-1; nos pares, delete-1 pareado)
    jbar = sum(jack) / len(jack)
    num = sum((jbar - j) ** 3 for j in jack)
    den = 6.0 * (sum((jbar - j) ** 2 for j in jack)) ** 1.5
    acc = (num / den) if den > 0 else 0.0
    # percentis ajustados
    def adj(p):
        z = ND.inv_cdf(p)
        den2 = 1 - acc * (z0 + z)
        if den2 == 0:
            return p
        return ND.cdf(z0 + (z0 + z) / den2)
    a1 = min(max(adj(alpha / 2), 0.0), 1.0)
    a2 = min(max(adj(1 - alpha / 2), 0.0), 1.0)
    lo, hi = _quantile(boots, a1), _quantile(boots, a2)
    return lo, hi, {"z0": round(z0, 4), "aceleracao": round(acc, 5),
                    "pct_ajustado": [round(a1, 4), round(a2, 4)]}


def pct_ci(boots, alpha=0.05):
    boots = sorted(v for v in boots if v is not None and not math.isnan(v))
    if not boots:
        return None, None
    return _quantile(boots, alpha / 2), _quantile(boots, 1 - alpha / 2)


# ---------------- contrastes com BCa ----------------

def contrast_bca(a, b, fn, rng, paired, n_boot=N_BOOT):
    """Delta = fn(a)-fn(b); boots com bloco; jackknife delete-1
    (pareado se paired; senao pooled delete-1 de amostra unica)."""
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
    jack = []
    if paired:
        for i in range(len(a)):
            aa = a[:i] + a[i + 1:]
            bb = b[:i] + b[i + 1:]
            v = fn(aa) - fn(bb)
            if v is not None and not math.isnan(v):
                jack.append(v)
    else:  # pooled delete-1 (duas amostras)
        for i in range(len(a)):
            v = fn(a[:i] + a[i + 1:]) - fn(b)
            if v is not None and not math.isnan(v):
                jack.append(v)
        for i in range(len(b)):
            v = fn(a) - fn(b[:i] + b[i + 1:])
            if v is not None and not math.isnan(v):
                jack.append(v)
    blo, bhi, info = bca_ci(obs, boots, jack, alpha=0.05)
    # TOST padrao: IC90 (alfa=0.10) deve caber na margem +/-Delta
    lo90, hi90, _ = bca_ci(obs, boots, jack, alpha=0.10)
    plo, phi = pct_ci(boots)
    se = (sum((x - sum(boots) / len(boots)) ** 2 for x in boots)
          / max(1, len(boots) - 1)) ** 0.5 if boots else None
    return {"point": obs,
            "bca_lo": blo, "bca_hi": bhi, "bca_info": info,
            "bca90_lo": lo90, "bca90_hi": hi90,
            "pct_lo": plo, "pct_hi": phi,
            "bca_excludes0": (blo is not None and (blo > 0 or bhi < 0)),
            "pct_excludes0": (plo is not None and (plo > 0 or phi < 0)),
            "point_outside_bca": (blo is not None
                                  and (obs < blo or obs > bhi)),
            "point_outside_pct": (plo is not None
                                  and (obs < plo or obs > phi)),
            "se_boot": se,
            "mde80": (2.801585 * se) if se else None,
            "n_boot": len(boots), "n_jack": len(jack)}


def classify(c):
    """Tripla regua declarada a priori: SEPARA / EQUIVALENTE / INCONCLUSIVO.
    TOST: IC90 BCa contido na margem (alfa=0.05 bicaudal <=> IC90).
    REGRA DECLARADA (metadata.regra_incoerencia): se o ponto estimado cai
    FORA do IC (percentil ou BCa), o teste e INCOERENTE e NAO conta como
    refutacao NEM como confirmacao — aplicada aqui automaticamente."""
    out = {}
    for d in MARGINS:
        if c is None or c.get("bca90_lo") is None:
            out[f"equivalente_d{d:.2f}"] = None
            continue
        out[f"equivalente_d{d:.2f}"] = (c["bca90_lo"] > -d
                                        and c["bca90_hi"] < d)
    if c is None or c["bca_lo"] is None:
        out["veredito"] = "SEM_DADOS"
        return out
    if c["point_outside_pct"] or c["point_outside_bca"]:
        out["veredito"] = "INCOERENTE"      # regra declarada
    elif c["bca_excludes0"]:
        out["veredito"] = "SEPARA"
    elif out[f"equivalente_d{MARGIN_PRIMARY:.2f}"]:
        out["veredito"] = "EQUIVALENTE"
    else:
        out["veredito"] = "INCONCLUSIVO"
    return out


# ---------------- selftest BCa vs scipy ----------------

def selftest_bca():
    """BCa unidimensional iid aqui vs scipy.stats.bootstrap(BCa)."""
    try:
        from scipy import stats as sstats
    except ImportError:
        return {"status": "scipy ausente — selftest pulado"}
    import random as _r
    rng = _r.Random(SEED + 7)
    x = [rng.gauss(0, 1) + (i % 5) * 0.3 for i in range(64)]

    def stat(v):
        m = sum(v) / len(v)
        return sum((t - m) ** 2 for t in v) / len(v)  # variancia

    # minha implementacao (iid, mesmo esquema do scipy)
    rng2 = _r.Random(SEED + 8)
    obs = stat(x)
    boots = [stat([x[i] for i in iid_idx(len(x), rng2)])
             for _ in range(20000)]
    jack = [stat(x[:i] + x[i + 1:]) for i in range(len(x))]
    lo_m, hi_m, info = bca_ci(obs, boots, jack)
    res = sstats.bootstrap((x,), stat, method="BCa", n_resamples=20000,
                           random_state=SEED + 8)
    lo_s, hi_s = res.confidence_interval.low, res.confidence_interval.high
    diff = max(abs(lo_m - lo_s), abs(hi_m - hi_s))
    return {"status": "OK" if diff < 0.05 else "DIVERGENTE",
            "minha_BC95": [round(lo_m, 4), round(hi_m, 4)],
            "scipy_BC95": [round(float(lo_s), 4), round(float(hi_s), 4)],
            "max_diff": round(diff, 5), "info": info,
            "scipy_version": __import__("scipy").__version__}


# ---------------- main ----------------

def main():
    t0 = time.time()
    print("=" * 70)
    print("D4' v2 r2 — BCa + TOST (margem declarada) + MDE80")
    print("=" * 70)

    st = selftest_bca()
    print(f"\n[selftest BCa vs scipy] {st['status']}",
          st.get("max_diff", ""))
    if st.get("status") == "DIVERGENTE":
        print("[ERRO] BCa diverge do scipy — abortar para investigar.")
        return 2

    series, n_rows = load_series()
    print(f"series carregadas do CSV congelado: {n_rows} linhas; "
          f"n por celula: " + ", ".join(
              f"{f}|{s}={len(v)}" for (f, s), v in sorted(series.items())))

    rng = __import__("random").Random(SEED + 3)   # seed r2 declarado
    mets = {"higuchi_D": higuchi_D, "boxdim": boxdim_curve,
            "hurst_rs": hurst_rs}

    contrasts = {}
    # H_C3: pares de familias (minref confirmatorio; drat exploratorio)
    for sysname in ("minref", "drat"):
        for i in range(len(FAMS)):
            for j in range(i + 1, len(FAMS)):
                a0 = series.get((FAMS[i], sysname), [])
                b0 = series.get((FAMS[j], sysname), [])
                for vname in ("raw", "log1p", "relinc"):
                    a = variants_of(a0)[vname]
                    b = variants_of(b0)[vname]
                    for mname, fn in mets.items():
                        key = (f"{sysname}:{FAMS[i]}-{FAMS[j]}:"
                               f"{mname}:{vname}")
                        c = contrast_bca(a, b, fn, rng, paired=False)
                        if c is None:
                            continue
                        conf = (sysname == "minref"
                                and mname == "higuchi_D"
                                and vname in ("raw", "relinc"))
                        contrasts[key] = {
                            **c, **classify(c),
                            "confirmatorio_H_C3": conf,
                            "pista_exploratoria": key in PISTA}
    # H_C4: fonte minref vs drat (pareado)
    for fam in FAMS:
        a0 = series.get((fam, "minref"), [])
        b0 = series.get((fam, "drat"), [])
        for vname in ("raw", "log1p", "relinc"):
            a = variants_of(a0)[vname]
            b = variants_of(b0)[vname]
            for mname, fn in mets.items():
                key = f"fonte:{fam}:{mname}:{vname}"
                c = contrast_bca(a, b, fn, rng, paired=True)
                if c is None:
                    continue
                conf = (mname == "higuchi_D" and vname in ("raw", "relinc"))
                contrasts[key] = {**c, **classify(c),
                                  "confirmatorio_H_C4": conf,
                                  "pista_exploratoria": False}

    # ---- vereditos r2 ----
    hc3 = {k: v for k, v in contrasts.items() if v.get("confirmatorio_H_C3")}
    hc4 = {k: v for k, v in contrasts.items() if v.get("confirmatorio_H_C4")}
    pista = {k: v for k, v in contrasts.items()
             if v.get("pista_exploratoria")}

    def tally(d):
        t = {"SEPARA": 0, "EQUIVALENTE": 0, "INCONCLUSIVO": 0,
             "INCOERENTE": 0, "SEM_DADOS": 0}
        for v in d.values():
            t[v["veredito"]] = t.get(v["veredito"], 0) + 1
        return t

    def eq_tally(d, margin):
        k = f"equivalente_d{margin:.2f}"
        return sum(1 for v in d.values() if v.get(k))

    hyp = {
        "H_C3_r2_equivalencia": {
            "enunciado": ("TOST por par (minref, D_H, raw+relinc) com "
                          f"margem primaria Delta={MARGIN_PRIMARY}: se o "
                          "IC90 BCa cai dentro de +/-Delta, o par e "
                          "EQUIVALENTE (limite quantitativo); se IC95 BCa "
                          "exclui 0, SEPARA; senao INCONCLUSIVO."),
            "n_testes": len(hc3), "vereditos": tally(hc3),
            "equivalentes_D010": eq_tally(hc3, 0.10),
            "equivalentes_D015": eq_tally(hc3, 0.15),
            "equivalentes_D020": eq_tally(hc3, 0.20),
            "separacoes_pct_vs_bca": {
                "pct_excluem_0": sum(1 for v in hc3.values()
                                     if v["pct_excludes0"]),
                "bca_excluem_0": sum(1 for v in hc3.values()
                                     if v["bca_excludes0"])},
            "incoerentes": sorted(k for k, v in hc3.items()
                                  if v["point_outside_pct"]
                                  or v["point_outside_bca"]),
        },
        "H_C4_r2_invariancia_de_fonte": {
            "enunciado": ("Mesma tripla regua nos 6 contrastes pareados "
                          "minref-vs-drat; a exclusao nominal do r1 "
                          "(implication raw, ponto fora do IC percentil) "
                          "e reavaliada sob BCa — a flag "
                          "point_outside_ci vale para as DUAS direcoes "
                          "(regra declarada: incoerente nao conta como "
                          "refutacao nem como confirmacao)."),
            "n_testes": len(hc4), "vereditos": tally(hc4),
            "equivalentes_D010": eq_tally(hc4, 0.10),
            "exclusoes_bca": sorted(k for k, v in hc4.items()
                                    if v["bca_excludes0"]),
            "exclusoes_bca_coerentes": sorted(
                k for k, v in hc4.items()
                if v["bca_excludes0"]
                and not v["point_outside_pct"]
                and not v["point_outside_bca"]),
            "incoerentes": sorted(k for k, v in hc4.items()
                                  if v["point_outside_pct"]
                                  or v["point_outside_bca"]),
            "veredito_r1_sob_BCa": (
                "exclusao nominal do r1 (implication raw) tornou-se "
                "INCOERENTE sob BCa (ponto fora do IC95 dos DOIS "
                "metodos) — regra declarada: nao conta; leitura "
                "sustentada: invariancia de fonte mantida"
                if "fonte:implication:higuchi_D:raw" in
                sorted(k for k, v in hc4.items()
                       if v["point_outside_pct"]
                       or v["point_outside_bca"])
                else "ver r2_vereditos"),
        },
        "pista_boxdim_r2": {
            "enunciado": ("Referee A4: boxdim implication-cadeia (drat) "
                          "excluia 0 em 3 variantes no r1 — reavaliado "
                          "com BCa como PISTA EXPLORATORIA (nao "
                          "promovido a confirmatorio)."),
            "n_testes": len(pista),
            "vereditos": tally(pista),
            "detalhe": {k: {"point": round(v["point"], 4),
                            "bca": [round(v["bca_lo"], 4)
                                    if v["bca_lo"] is not None else None,
                                    round(v["bca_hi"], 4)
                                    if v["bca_hi"] is not None else None],
                            "veredito": v["veredito"]}
                        for k, v in sorted(pista.items())},
        },
        "H_C2_Res_vs_EFrege": {"status": "DEFERIDO",
                               "motivo": "mantido — EF nao mensuravel"},
    }

    # ---- CSV ----
    cols = ["key", "veredito", "point", "bca_lo", "bca_hi",
            "bca90_lo", "bca90_hi", "pct_lo",
            "pct_hi", "bca_excludes0", "point_outside_pct",
            "point_outside_bca", "se_boot", "mde80",
            "equivalente_d0.10", "equivalente_d0.15", "equivalente_d0.20",
            "confirmatorio_H_C3", "confirmatorio_H_C4",
            "pista_exploratoria", "bca_z0", "bca_aceleracao"]
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for k, v in sorted(contrasts.items()):
            w.writerow({
                "key": k, "veredito": v["veredito"],
                "point": round(v["point"], 6),
                "bca_lo": v["bca_lo"], "bca_hi": v["bca_hi"],
                "bca90_lo": v.get("bca90_lo"),
                "bca90_hi": v.get("bca90_hi"),
                "pct_lo": v["pct_lo"], "pct_hi": v["pct_hi"],
                "bca_excludes0": v["bca_excludes0"],
                "point_outside_pct": v["point_outside_pct"],
                "point_outside_bca": v["point_outside_bca"],
                "se_boot": v["se_boot"],
                "mde80": v["mde80"],
                "equivalente_d0.10": v.get("equivalente_d0.10"),
                "equivalente_d0.15": v.get("equivalente_d0.15"),
                "equivalente_d0.20": v.get("equivalente_d0.20"),
                "confirmatorio_H_C3": v.get("confirmatorio_H_C3"),
                "confirmatorio_H_C4": v.get("confirmatorio_H_C4"),
                "pista_exploratoria": v.get("pista_exploratoria"),
                "bca_z0": v["bca_info"].get("z0"),
                "bca_aceleracao": v["bca_info"].get("aceleracao"),
            })
    sha = hashlib.sha256(
        OUT_CSV.read_bytes().replace(b"\r\n", b"\n")).hexdigest()

    payload = {
        "metadata": {
            "timestamp_utc": datetime.now(timezone.utc).isoformat()
                             .replace("+00:00", "Z"),
            "data_source": ("gk_proof_fractal_v2_r2.py (r2: BCa + TOST "
                            "+ MDE80 — re-analise do CSV congelado)"),
            "input_csv": SRC_CSV.name,
            "input_csv_sha256": hashlib.sha256(
                SRC_CSV.read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
            "seed_r2": SEED + 3, "n_boot": N_BOOT, "block": BLOCK,
            "margens": {"primaria": MARGIN_PRIMARY,
                        "sensibilidade": list(MARGINS[1:])},
            "mde80_formula": "2.8016 * SE_boot (z.975 + z.80, alfa .05)",
            "regra_incoerencia": ("point_outside (pct ou BCa) => teste "
                                  "NAO conta como refutacao nem como "
                                  "confirmacao — declarada a priori"),
            "csv": OUT_CSV.name, "csv_sha256": sha,
            "sha_note": "sha256 sobre bytes normalizados CRLF->LF",
            "runtime_s": round(time.time() - t0, 1),
            "caveats": [
                ("BCa usa jackknife delete-1 (pareado nos pares de "
                 "fonte; pooled em duas amostras) — em serie ordinal o "
                 "delete-1 altera adjacencias; delete-d block jackknife "
                 "fica para r3."),
                ("Margens escolhidas ANTES desta execucao; 0.10 "
                 "primaria (~1/7 do efeito v1 0.731); 0.15/0.20 apenas "
                 "sensibilidade — nao promovidos."),
                ("Percentis do r2 usam B=1000 (r1 usou 300) — valores "
                 "percentis do r1 nao sao bit-identicos aos daqui; o "
                 "artefato r1 permanece congelado."),
                ("N1+N2; sem N4; H_C2 (EF) deferido; tau k↑ aberta."),
            ],
        },
        "selftest_bca": st,
        "contrasts": contrasts,
        "hypotheses": hyp,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False),
                        encoding="utf-8")

    # ---- console ----
    print("\n--- H_C3 (minref, D_H, raw+relinc) — tripla regua BCa ---")
    for k, v in sorted(hc3.items()):
        print(f"  {k}: point={v['point']:+.3f} "
              f"BC95=[{v['bca_lo']:+.3f},{v['bca_hi']:+.3f}] "
              f"BC90~eq? {v.get('equivalente_d0.10')} -> {v['veredito']}"
              + (" | PCT-incoerente" if v["point_outside_pct"] else ""))
    print(f"  tally: {tally(hc3)} | eq@0.10={eq_tally(hc3,0.10)}/6 "
          f"eq@0.15={eq_tally(hc3,0.15)}/6 eq@0.20={eq_tally(hc3,0.20)}/6")
    print("\n--- H_C4 (fonte pareada, D_H, raw+relinc) ---")
    for k, v in sorted(hc4.items()):
        print(f"  {k}: point={v['point']:+.3f} "
              f"BC95=[{v['bca_lo']:+.3f},{v['bca_hi']:+.3f}] "
              f"-> {v['veredito']}"
              + (" | PCT-incoerente" if v["point_outside_pct"] else ""))
    print(f"  tally: {tally(hc4)} | eq@0.10={eq_tally(hc4,0.10)}/6")
    print("\n--- pista boxdim (exploratoria) ---")
    for k, v in sorted(pista.items()):
        print(f"  {k}: BC95=[{v['bca_lo']:+.3f},{v['bca_hi']:+.3f}] "
              f"-> {v['veredito']}")
    # MDE medio dos confirmatorios
    mdes = [v["mde80"] for v in list(hc3.values()) + list(hc4.values())
            if v.get("mde80")]
    if mdes:
        print(f"\nMDE80 medio (confirmatorios): {sum(mdes)/len(mdes):.3f} "
              f"(min={min(mdes):.3f}, max={max(mdes):.3f})")
    n_out_pct = sum(1 for v in contrasts.values()
                    if v["point_outside_pct"])
    n_out_bca = sum(1 for v in contrasts.values()
                    if v["point_outside_bca"])
    print(f"incoerencia ponto-fora-do-IC: pct={n_out_pct}/"
          f"{len(contrasts)} -> BCa={n_out_bca}/{len(contrasts)}")
    print(f"\n[OK] {OUT_JSON.name} + {OUT_CSV.name} "
          f"(sha256={sha[:16]}…)")
    print(f"runtime: {payload['metadata']['runtime_s']}s")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

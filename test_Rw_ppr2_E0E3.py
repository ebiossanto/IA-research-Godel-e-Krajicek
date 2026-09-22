"""
PR20: Testa R_w (predicado PPR-2-ramo refinado, PR17) nos cenários E0–E3 do PR16.

Para cada config (κ, razão, |W|):
  1) Reproduz pares (α,b) com δ_F ≠ δ_S (RCS);
  2) Testa PPR-2-ramo com R_w = identidade + sentinela ALL→w*
     na transição σ_S → σ_F (slow → fast) e em transições genéricas σ → σ+step.

Condições (A)∨(B)∨(C) — ver 17_... §2.
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from itertools import product

ALL_SENTINEL = 'ALL_COV'
W_STAR_BASE = '00'

# ---------------------------------------------------------------------------
# Modelo (alinha com slow_vs_fast_delta_ext.py / test_Rw_ppr2.py)
# ---------------------------------------------------------------------------
def make_W(r):
    return [''.join(p) for p in product('01', repeat=r)]

def kappa_profile(w, w_star=W_STAR_BASE, level='base'):
    if level == 'base':
        if w.startswith(w_star):
            return 2
        return sum(ord(c) for c in w) % 2
    elif level == 'rich':
        if w.startswith(w_star):
            return 3
        if w.startswith('01') or w.startswith('10'):
            return 2
        return sum(ord(c) for c in w) % 2
    return 0

def covered(sigma, b, k):
    return k <= sigma and (k + 1) <= b

def first_uncovered(sigma, b, W, KAPPA):
    for w in sorted(W):
        if not covered(sigma, b, KAPPA[w]):
            return w
    return None  # ALL_COV

def uncovered_set(sigma, b, W, KAPPA):
    return {w for w in W if not covered(sigma, b, KAPPA[w])}

def delta(sigma, b, W, KAPPA):
    d = 0
    for w in W:
        k = KAPPA[w]
        if k > sigma or (k + 1) > b:
            d += 1
    return d

def R_w(x, w_star):
    if x == ALL_SENTINEL:
        return w_star
    return x

# ---------------------------------------------------------------------------
# PPR-2-ramo refinado (17 §2)
# ---------------------------------------------------------------------------
def ppr2_ramo(sigma_T, sigma_Tp, b, W, KAPPA, w_star):
    w0_T = first_uncovered(sigma_T, b, W, KAPPA)
    w0_Tp = first_uncovered(sigma_Tp, b, W, KAPPA)
    uncov_Tp = uncovered_set(sigma_Tp, b, W, KAPPA)

    if w0_T is None:
        return True, 'SKIP(T=all)', None, w0_T, w0_Tp

    r_w0 = R_w(w0_T, w_star)
    cond_A = r_w0 in uncov_Tp
    cond_B = (w0_T != w0_Tp) and (r_w0 == w_star)
    cond_C = (w0_Tp is None)
    ok = cond_A or cond_B or cond_C
    which = []
    if cond_A:
        which.append('A')
    if cond_B:
        which.append('B')
    if cond_C:
        which.append('C')
    status = 'OK(' + '+'.join(which) + ')' if ok else 'FAIL'
    return ok, status, r_w0, w0_T, w0_Tp

# ---------------------------------------------------------------------------
# Configs E0–E3 (replica slow_vs_fast_delta_ext.py)
# ---------------------------------------------------------------------------
CONFIGS = [
    # (nome, r, k_level, fast_step, slow_step, w_star)
    ('E0 base',           4, 'base', 2, 1, '00'),
    ('E1 rich-kappa',     4, 'rich', 2, 1, '00'),
    ('E2 3:1',            4, 'base', 3, 1, '00'),
    ('E3 |W|=64',         6, 'base', 2, 1, '00'),
]

B_VALUES = (2, 3, 4, 5, 8)
ALPHA_MAX = 6

def run_config(name, r, k_level, fast_step, slow_step, w_star):
    W = make_W(r)
    KAPPA = {w: kappa_profile(w, level=k_level) for w in W}

    # 1) Pares RCS (slow vs fast)
    rcs_pairs = []
    for alpha in range(ALPHA_MAX + 1):
        sf = fast_step * alpha
        ss = slow_step * alpha
        for b in B_VALUES:
            df = delta(sf, b, W, KAPPA)
            ds = delta(ss, b, W, KAPPA)
            if df != ds:
                rcs_pairs.append((alpha, b, ss, sf, ds, df))

    # 2) PPR-2 em transições slow→fast nos pares RCS
    ppr_pass = 0
    ppr_total = 0
    fails = []
    for (alpha, b, ss, sf, ds, df) in rcs_pairs:
        ok, status, _, _, _ = ppr2_ramo(ss, sf, b, W, KAPPA, w_star)
        ppr_total += 1
        if ok:
            ppr_pass += 1
        else:
            fails.append((alpha, b, ss, sf, status))

    # 3) PPR-2 em transições genéricas σ → σ+fast_step (varredura)
    gen_pass = 0
    gen_total = 0
    gen_fails = []
    for sigma in range(0, max(fast_step, slow_step) * ALPHA_MAX + 1):
        for b in B_VALUES:
            sigma_next = sigma + fast_step
            ok, status, _, _, _ = ppr2_ramo(sigma, sigma_next, b, W, KAPPA, w_star)
            gen_total += 1
            if ok:
                gen_pass += 1
            else:
                gen_fails.append((sigma, sigma_next, b, status))

    rcs_ok = len(rcs_pairs) > 0
    ppr_rcs_ok = (ppr_pass == ppr_total) if ppr_total else True
    ppr_gen_ok = (gen_pass == gen_total)

    print(f"\n=== {name} ===")
    print(f"  r={r} (|W|={len(W)}), kappa={k_level}, "
          f"fast_step={fast_step}, slow_step={slow_step}")
    print(f"  RCS pares (alpha,b) delta_F!=delta_S : {len(rcs_pairs)}/{(ALPHA_MAX+1)*len(B_VALUES)}")
    if rcs_pairs:
        ex = rcs_pairs[0]
        print(f"    exemplo: alpha={ex[0]}, b={ex[1]}: dS={ex[4]}, dF={ex[5]} (sigma_S={ex[2]}, sigma_F={ex[3]})")
    print(f"  PPR-2 em pares RCS (S->F)           : {ppr_pass}/{ppr_total} "
          f"{'OK' if ppr_rcs_ok else 'FAIL'}")
    if fails:
        for f in fails[:3]:
            print(f"    FAIL alpha={f[0]}, b={f[1]}: sigma {f[2]}->{f[3]} {f[4]}")
    print(f"  PPR-2 transicoes genericas          : {gen_pass}/{gen_total} "
          f"{'OK' if ppr_gen_ok else 'FAIL'}")
    if gen_fails:
        for f in gen_fails[:3]:
            print(f"    FAIL sigma {f[0]}->{f[1]}, b={f[2]}: {f[3]}")

    return {
        'name': name,
        'rcs': rcs_ok,
        'n_rcs': len(rcs_pairs),
        'ppr_rcs': ppr_rcs_ok,
        'ppr_rcs_ratio': f"{ppr_pass}/{ppr_total}",
        'ppr_gen': ppr_gen_ok,
        'ppr_gen_ratio': f"{gen_pass}/{gen_total}",
        'all_ok': rcs_ok and ppr_rcs_ok and ppr_gen_ok,
    }

def main():
    print("=" * 70)
    print("PR20 — R_w (PPR-2 refinado) nos cenarios E0–E3 (RCS robusta PR16)")
    print("=" * 70)

    results = []
    for cfg in CONFIGS:
        results.append(run_config(*cfg))

    print("\n" + "=" * 70)
    print("RESUMO PR20")
    print("=" * 70)
    all_ok = True
    for r in results:
        status = "OK" if r['all_ok'] else "FAIL"
        print(f"  {r['name']:20s}: RCS={'SIM' if r['rcs'] else 'NAO'} "
              f"({r['n_rcs']} pares), PPR-2(S->F)={r['ppr_rcs_ratio']} "
              f"{status}")
        all_ok = all_ok and r['all_ok']
    print("=" * 70)
    if all_ok:
        print("*** PR20: R_w PASSA PPR-2 em todos os cenarios E0–E3 ***")
        print("*** (pares RCS slow->fast + transicoes genericas) ***")
    else:
        print("*** ATENCAO: alguma config falhou — refinar R_w ou predicado ***")
    return all_ok

if __name__ == '__main__':
    main()

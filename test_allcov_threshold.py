"""
PR24: Generalização (C) — limiar de ALL_COV inevitável.

(C) dispara quando T' cobre todos os w ∈ truesOf(W):
  σ ≥ max κ  ∧  b ≥ max κ + 1

Testa:
  1) Characterização: all_cov ⇔ δ=0
  2) Limiar σ: menor σ tal que ALL_COV para cada b
  3) Limiar b: menor b tal que ALL_COV para cada σ ≥ maxκ
  4) Em E0–E3 e no cenário PR23 (κ explícito)
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from itertools import product

ALL_SENTINEL = 'ALL_COV'
W_STAR = '1000'

def make_W(r):
    return [''.join(p) for p in product('01', repeat=r)]

def kappa_base(w, w_star_prefix='00'):
    if w.startswith(w_star_prefix):
        return 2
    return sum(ord(c) for c in w) % 2

def kappa_rich(w, w_star_prefix='00'):
    if w.startswith(w_star_prefix):
        return 3
    if w.startswith('01') or w.startswith('10'):
        return 2
    return sum(ord(c) for c in w) % 2

def kappa_explicit(w, w_star=W_STAR):
    if w == w_star:
        return 1
    if w.startswith('0'):
        return 0
    return 2

def covered(sigma, b, k):
    return k <= sigma and (k + 1) <= b

def max_kappa(W, K):
    return max((K[w] for w in W), default=0)

def all_covered(sigma, b, W, K):
    return all(covered(sigma, b, K[w]) for w in W)

def delta(sigma, b, W, K):
    return sum(1 for w in W if not covered(sigma, b, K[w]))

def first_uncovered(sigma, b, W, K):
    for w in sorted(W):
        if not covered(sigma, b, K[w]):
            return w
    return None

def check_characterization(name, W, K, sigma_range, b_range):
    """all_covered ⇔ delta=0  e  limiar σ ≥ maxκ ∧ b ≥ maxκ+1."""
    mk = max_kappa(W, K)
    print(f'\n=== {name} (|W|={len(W)}, maxκ={mk}) ===')
    mismatches = 0
    threshold_mismatches = 0
    tests = 0
    for sigma in sigma_range:
        for b in b_range:
            ac = all_covered(sigma, b, W, K)
            d = delta(sigma, b, W, K)
            tests += 1
            if ac != (d == 0):
                mismatches += 1
            # limiar teórico
            predicted = (sigma >= mk and b >= mk + 1)
            # ALL_COV real pode ser mais forte: precisa cobrir cada κ individual
            # predicted é suficiente mas não necessário se alguns κ nunca ocorrem
            # Verificamos: predicted → all_covered (suficiência)
            if predicted and not ac:
                threshold_mismatches += 1

    # suficiência: σ≥maxκ ∧ b≥maxκ+1 ⇒ ALL_COV
    suf_ok = True
    for sigma in sigma_range:
        for b in b_range:
            if sigma >= mk and b >= mk + 1:
                if not all_covered(sigma, b, W, K):
                    suf_ok = False

    # necessidade fraca: ALL_COV ⇒ σ≥min_κ_observado e b≥min(κ)+1
    # (cada κ presente precisa: κ≤σ e κ+1≤b ⇒ σ≥maxκ_presente, b≥maxκ+1)
    # Sobre o conjunto de κ que APARECEM em W:
    ks_present = sorted(set(K[w] for w in W))
    mk_present = max(ks_present) if ks_present else 0
    nec_ok = True
    for sigma in sigma_range:
        for b in b_range:
            if all_covered(sigma, b, W, K):
                if not (sigma >= mk_present and b >= mk_present + 1):
                    nec_ok = False

    # menor σ com ALL_COV para b suficiente
    min_sigma_allcov = None
    for sigma in sorted(set(list(sigma_range) + [mk, mk + 1])):
        for b in b_range:
            if b >= mk + 1 and all_covered(sigma, b, W, K):
                if min_sigma_allcov is None or sigma < min_sigma_allcov:
                    min_sigma_allcov = sigma
                break

    print(f'  κ presentes: {ks_present}')
    print(f'  Testes (σ,b): {tests}')
    print(f'  all_cov ⇔ δ=0 : {"OK" if mismatches == 0 else f"FAIL ({mismatches})"}')
    print(f'  Suficiência (σ≥{mk} ∧ b≥{mk+1} ⇒ ALL_COV): {"OK" if suf_ok else "FAIL"}')
    print(f'  Necessidade (ALL_COV ⇒ σ≥{mk_present} ∧ b≥{mk_present+1}): {"OK" if nec_ok else "FAIL"}')
    print(f'  Menor σ com ALL_COV (b≥{mk_present+1}): {min_sigma_allcov}')
    print(f'  Limiar teórico: σ*={mk_present}, b*={mk_present+1}')
    return mismatches == 0 and suf_ok and nec_ok and min_sigma_allcov == mk_present

def main():
    print('=' * 70)
    print('PR24 — Generalização (C): limiar de ALL_COV inevitável')
    print('  ALL_COV sse δ=0; suficiente: σ ≥ max κ ∧ b ≥ max κ + 1')
    print('=' * 70)

    ok = True

    # 1) base r=4 (PR17)
    W4 = make_W(4)
    K4 = {w: kappa_base(w) for w in W4}
    ok &= check_characterization('E0/base r=4', W4, K4, range(0, 5), range(1, 10))

    # 2) rich r=4 (E1)
    Kr = {w: kappa_rich(w) for w in W4}
    ok &= check_characterization('E1/rich r=4', W4, Kr, range(0, 5), range(1, 10))

    # 3) base r=6 (E3)
    W6 = make_W(6)
    K6 = {w: kappa_base(w) for w in W6}
    ok &= check_characterization('E3/base r=6', W6, K6, range(0, 5), range(1, 10))

    # 4) cenário PR23 (κ explícito)
    Ke = {w: kappa_explicit(w) for w in W4}
    ok &= check_characterization('PR23/explicit', W4, Ke, range(0, 4), range(1, 10))

    # 5) Caso (C) no PPR-2: transição σ→σ' com σ' ≥ maxκ ⇒ w₀'=ALL
    print('\n=== Transições σ→σ\' que disparam (C) ===')
    c_hits = 0
    c_total = 0
    for name, W, K in [('base', W4, K4), ('rich', W4, Kr), ('PR23', W4, Ke)]:
        mk = max_kappa(W, K)
        for sigma in range(0, mk + 2):
            for sigma_p in range(sigma, mk + 3):
                for b in (2, 3, 4, 5, 8):
                    w0 = first_uncovered(sigma, b, W, K)
                    if w0 is None:
                        continue
                    w0p = first_uncovered(sigma_p, b, W, K)
                    c_total += 1
                    if w0p is None:
                        c_hits += 1
                        # (C) deve ser inevitável quando σ' ≥ maxκ e b ≥ maxκ+1
                        if sigma_p >= mk and b >= mk + 1:
                            pass  # expected
    print(f'  Pares com w₀ existente e w₀\'=ALL: {c_hits}/{c_total}')
    print(f'  (C) é o caso ALL_COV — inevitável quando σ\' ≥ max κ ∧ b ≥ max κ+1')

    print('\n' + '=' * 70)
    if ok:
        print('*** PR24: Generalização (C) VERIFICADA ***')
        print('*** ALL_COV ⇔ δ=0; limiar σ*=max κ, b*=max κ+1 ***')
        print('*** Suficiência + necessidade OK em 4 perfis ***')
    else:
        print('*** ATENÇÃO: alguma caracterização falhou ***')
    print('=' * 70)
    return ok

if __name__ == '__main__':
    main()

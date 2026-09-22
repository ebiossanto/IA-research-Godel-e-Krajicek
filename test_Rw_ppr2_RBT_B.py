"""
PR23: Cenário RBT explícito — condição (B) de PPR-2-ramo com w* ≠ w₀'.

Motivo: em PR17/19/20 a cond. (B) nunca disparou porque
  - W_STAR='00' é PREFIXO, mas compara-se r_w0 == W_STAR com palavra completa; e
  - R identidade só retorna w* se w₀ for exatamente w*.

Construção explícita (partial RBT, não ALL_COV):
  W = {0,1}^4, w* = '1000'
  κ: 0xxx → 0; w*='1000' → 1; 1xxx (≠ w*) → 2
  T  (σ=0, b=4): 0xxx cobertos, w* não-coberto ⇒ w₀ = w*
  T' (σ=1, b=4): w* coberto, 1001+ não-coberto ⇒ w₀' = '1001' ≠ w*
  R identidade: R(w₀)=w* = w*  ⇒  cond. (B) pura (A=F, C=F)

Verifica também Θ/CC-Θ (PR19) sob a cond. (B).
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from itertools import product

ALL_SENTINEL = 'ALL_COV'
W_STAR = '1000'

def make_W(r):
    return [''.join(p) for p in product('01', repeat=r)]

def kappa_explicit(w, w_star=W_STAR):
    if w == w_star:
        return 1
    if w.startswith('0'):
        return 0
    return 2

def covered(sigma, b, k):
    return k <= sigma and (k + 1) <= b

def first_uncovered(sigma, b, W, KAPPA):
    for w in sorted(W):
        if not covered(sigma, b, KAPPA[w]):
            return w
    return None

def uncovered_set(sigma, b, W, KAPPA):
    return {w for w in W if not covered(sigma, b, KAPPA[w])}

def R_w(x, w_star=W_STAR):
    if x == ALL_SENTINEL:
        return w_star
    return x

def ppr2_ramo(sigma_T, sigma_Tp, b, W, KAPPA, w_star=W_STAR):
    w0_T = first_uncovered(sigma_T, b, W, KAPPA)
    w0_Tp = first_uncovered(sigma_Tp, b, W, KAPPA)
    uncov_Tp = uncovered_set(sigma_Tp, b, W, KAPPA)

    if w0_T is None:
        return True, 'SKIP(T=all)', None, w0_T, w0_Tp, False, False, False

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
    return ok, status, r_w0, w0_T, w0_Tp, cond_A, cond_B, cond_C

# --- Θ (replica ppr3_ramos_theta.py sob cond. B) ---
def cert_uncov(w, sigma, b, k, valid=True):
    return {
        'claim': 'uncov', 'w': w, 'sigma': sigma, 'b': b, 'kappa': k,
        'valid': valid and (k > sigma or (k + 1) > b),
    }

def cert_all_cov(sigma, b, W, KAPPA):
    all_ok = all(covered(sigma, b, KAPPA[w]) for w in W)
    return {'claim': 'ALL_COV', 'sigma': sigma, 'b': b, 'valid': all_ok}

def cert_bits(c):
    w_bits = len(c.get('w', '0')) if c.get('w') else 0
    return 2 + w_bits + max(1, c['sigma'].bit_length()) + max(1, c['b'].bit_length())

def Theta(pi, sigma_Tp, W, KAPPA, w_star=W_STAR):
    if pi['claim'] != 'uncov' or not pi['valid']:
        return None, 'INVALID_PI', None
    w0 = pi['w']
    b = pi['b']
    w0_Tp = first_uncovered(sigma_Tp, b, W, KAPPA)
    uncov_Tp = uncovered_set(sigma_Tp, b, W, KAPPA)
    r_w0 = R_w(w0, w_star)
    if w0_Tp is None:
        return cert_all_cov(sigma_Tp, b, W, KAPPA), 'C', r_w0
    if w0 != w0_Tp and r_w0 == w_star:
        k_star = KAPPA.get(w_star, 0)
        out = cert_uncov(w0_Tp, sigma_Tp, b, k_star, valid=True)
        out['kappa'] = KAPPA[w0_Tp]
        out['valid'] = w0_Tp in uncov_Tp
        return out, 'B', r_w0
    if r_w0 in uncov_Tp:
        return cert_uncov(r_w0, sigma_Tp, b, KAPPA[r_w0], valid=True), 'A', r_w0
    return None, 'FAIL', r_w0

def verify_theta(pi, theta_out, cond, sigma_Tp, W, KAPPA, w_star=W_STAR):
    if theta_out is None:
        return False
    if cond == 'C':
        ok = theta_out['claim'] == 'ALL_COV' and theta_out['valid']
    elif cond in ('A', 'B'):
        ok = (theta_out['claim'] == 'uncov' and theta_out['valid']
              and theta_out['w'] in uncovered_set(sigma_Tp, theta_out['b'], W, KAPPA))
    else:
        ok = False
    if ok:
        import math
        bound = cert_bits(pi) + max(1, math.ceil(math.log2(len(W) + 1))) + 4
        ok = cert_bits(theta_out) <= bound
    return ok

def main():
    print('=' * 70)
    print('PR23 — Cenário RBT EXPLÍCITO: cond. (B) com w* ≠ w₀\'')
    print(f'  W={{0,1}}^4, w*={W_STAR}, κ: 0xxx→0, w*→1, 1xxx\\{{w*}}→2')
    print('=' * 70)

    W = make_W(4)
    KAPPA = {w: kappa_explicit(w) for w in W}

    # Varredura de b e pares de σ onde o RBT parcial (não ALL) ocorre
    b_values = (2, 3, 4, 5, 8)
    sigma_pairs = [(0, 1), (0, 2), (1, 2), (1, 3)]

    total = 0
    b_hits = 0
    pure_B = 0
    theta_B = 0
    theta_ok = 0
    fails = []

    print(f'\n{"σ→σ\'":8} {"b":>3} {"w₀":6} {"w₀\'":6} {"R(w₀)":6} '
          f'{"A":3} {"B":3} {"C":3} {"PPR-2":7} {"Θ[cond]":10}')
    print('-' * 70)

    for sigma_T, sigma_Tp in sigma_pairs:
        for b in b_values:
            ok, status, r_w0, w0, w0p, cA, cB, cC = ppr2_ramo(
                sigma_T, sigma_Tp, b, W, KAPPA)
            if w0 is None:
                continue
            total += 1
            if ok:
                b_hits += 1
            else:
                fails.append((sigma_T, sigma_Tp, b, status))
            if cB:
                pure_B += 1 if not (cA or cC) else 0

            # Θ sob a transição
            k0 = KAPPA[w0]
            pi = cert_uncov(w0, sigma_T, b, k0, valid=True)
            out, cond, _ = Theta(pi, sigma_Tp, W, KAPPA)
            th_ok = verify_theta(pi, out, cond, sigma_Tp, W, KAPPA)
            if cond == 'B':
                theta_B += 1
            if th_ok:
                theta_ok += 1
            th_w = (out['w'] if out and out.get('w') else
                    ('ALL' if out and out.get('claim') == 'ALL_COV' else '?'))
            print(f'{sigma_T}→{sigma_Tp}   {b:>3} {w0 or "-":6} {w0p or "ALL":6} '
                  f'{r_w0 or "-":6} {str(cA)[0]:3} {str(cB)[0]:3} {str(cC)[0]:3} '
                  f'{status:7} Θ[{cond}]→{th_w} {"OK" if th_ok else "FAIL"}')

    print('-' * 70)
    print(f'  PPR-2 global        : {b_hits}/{total}'
          f' {"OK" if b_hits == total else "FAIL"}')
    b_count = 0
    b_pure = 0
    for sigma_T, sigma_Tp in sigma_pairs:
        for b in b_values:
            w0 = first_uncovered(sigma_T, b, W, KAPPA)
            if w0 is None:
                continue
            w0p = first_uncovered(sigma_Tp, b, W, KAPPA)
            r_w0 = R_w(w0)
            if (w0 != w0p) and (r_w0 == W_STAR):
                b_count += 1
                if w0p is not None:
                    b_pure += 1
    print(f'  Cond. (B) RBT        : {b_count} com w₀≠w₀\' ∧ R(w₀)=w*'
          f'  (puros B: {b_pure})')
    print(f'  Θ CC-Θ               : {theta_ok}/{total}'
          f' {"OK" if theta_ok == total else "FAIL"}'
          f'  (sob cond. B: {theta_B})')
    if fails:
        print(f'  FAILs: {fails}')

    print('=' * 70)
    all_ok = (b_hits == total and b_pure > 0 and theta_ok == total)
    if all_ok:
        print('*** PR23: cond. (B) RBT NÃO-VÁCIA — disparos explícitos ***')
        print(f'*** w*={W_STAR} ≠ w₀\' nos pares σ→σ+1 (RBT parcial) ***')
        print('*** PPR-2 + CC-Θ OK sob (B) no modelo finito ***')
    else:
        print('*** ATENÇÃO: cenário (B) não fechou — revisar κ/σ/b ***')
    return all_ok

if __name__ == '__main__':
    main()

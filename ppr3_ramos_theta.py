"""
PR19: PPR-3 — Θ sobre provas de ramos (candidato R_w, predicado A∨B∨C).

Dado π = certificado de "w₀ não-coberto em T" (ramo ativo), Θ(π) deve
produzir certificado válido para a claim-alvo em T' sob (A)∨(B)∨(C):

  (C) T'=ALL_COV  → Θ(π) = certificado ALL_COV (progresso trivial)
  (B) RBT         → Θ(π) = certificado de w₀' não-coberto em T' (R(w₀)=w*)
  (A) transferência → Θ(π) = certificado de R(w₀) não-coberto em T'

CC-Θ: Θ correto sse o certificado emitido é válido e a condição PPR-2-ramo
corresponde. Cota: |Θ(π)| ≤ |π| + O(log |W|) — polinomial no modelo finito.
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from itertools import product

ALL_SENTINEL = 'ALL_COV'
W_STAR_BASE = '00'

def make_W(r):
    return [''.join(p) for p in product('01', repeat=r)]

def kappa_profile(w, level='base', w_star=W_STAR_BASE):
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
    return None

def uncovered_set(sigma, b, W, KAPPA):
    return {w for w in W if not covered(sigma, b, KAPPA[w])}

def R_w(x, w_star):
    if x == ALL_SENTINEL:
        return w_star
    return x

# ---------------------------------------------------------------------------
# Certificados (provas no modelo finito)
# ---------------------------------------------------------------------------
def cert_uncov(w, sigma, b, k, valid=True):
    """Certificado: w não-coberto em teoria com sigma, orçamento b."""
    return {
        'claim': 'uncov',
        'w': w,
        'sigma': sigma,
        'b': b,
        'kappa': k,
        'valid': valid and (k > sigma or (k + 1) > b),
    }

def cert_all_cov(sigma, b, W, KAPPA):
    """Certificado: todos w cobertos (ALL_COV)."""
    all_ok = all(covered(sigma, b, KAPPA[w]) for w in W)
    return {
        'claim': 'ALL_COV',
        'sigma': sigma,
        'b': b,
        'valid': all_ok,
    }

def cert_bits(c):
    """Tamanho aproximado do certificado em bits."""
    # claim(2) + w(|W| bits) + sigma + b + kappa  ~ O(log|W| + log sigma + log b)
    import math
    w_bits = len(c.get('w', '0')) if c.get('w') else 0
    return 2 + w_bits + max(1, c['sigma'].bit_length()) + max(1, c['b'].bit_length())

# ---------------------------------------------------------------------------
# Θ: transformador de certificados de ramos
# ---------------------------------------------------------------------------
def Theta(pi, sigma_Tp, W, KAPPA, w_star):
    """
    Dado π: certificado de w₀ uncov em T, produz certificado alvo em T'.
    Decide qual condição (A)/(B)/(C) vale e emite cert correspondente.
    """
    if pi['claim'] != 'uncov' or not pi['valid']:
        return None, 'INVALID_PI', None

    w0 = pi['w']
    b = pi['b']
    sigma_T = pi['sigma']

    w0_Tp = first_uncovered(sigma_Tp, b, W, KAPPA)
    uncov_Tp = uncovered_set(sigma_Tp, b, W, KAPPA)
    r_w0 = R_w(w0, w_star)

    # (C) T' cobre tudo
    if w0_Tp is None:
        out = cert_all_cov(sigma_Tp, b, W, KAPPA)
        return out, 'C', r_w0

    # (B) transição RBT: ramo muda e R(w0)=w*
    if w0 != w0_Tp and r_w0 == w_star:
        k_star = KAPPA.get(w_star, 0)
        out = cert_uncov(w0_Tp, sigma_Tp, b, k_star, valid=True)
        return out, 'B', r_w0

    # (A) transferência direta
    if r_w0 in uncov_Tp:
        k = KAPPA[r_w0]
        out = cert_uncov(r_w0, sigma_Tp, b, k, valid=True)
        return out, 'A', r_w0

    return None, 'FAIL', r_w0

def verify_theta(pi, theta_out, cond, sigma_Tp, W, KAPPA, w_star):
    """CC-Θ: certificado emitido é válido E cond é A/B/C."""
    if theta_out is None:
        return False
    if cond == 'C':
        ok = theta_out['claim'] == 'ALL_COV' and theta_out['valid']
    elif cond in ('A', 'B'):
        ok = (theta_out['claim'] == 'uncov' and theta_out['valid']
              and theta_out['w'] in uncovered_set(sigma_Tp, theta_out['b'], W, KAPPA))
    else:
        ok = False
    # cota: |Θ(π)| ≤ |π| + c·log|W|
    if ok:
        c_pi = cert_bits(pi)
        c_th = cert_bits(theta_out)
        # teto generoso: dobrar + log|W|
        import math
        bound = c_pi + max(1, math.ceil(math.log2(len(W) + 1))) + 4
        ok = c_th <= bound
    return ok

# ---------------------------------------------------------------------------
# Cenários (PR17 base + E0–E3)
# ---------------------------------------------------------------------------
def scenarios():
    # PR17: 3 transições com r=4 base
    W4 = make_W(4)
    K4 = {w: kappa_profile(w) for w in W4}
    yield 'PR17 σ0→σ2', W4, K4, 0, 2, '00', (2, 3, 4, 8)
    yield 'PR17 σ1→σ2', W4, K4, 1, 2, '00', (2, 3, 4, 8)
    yield 'PR17 σ0→σ1', W4, K4, 0, 1, '00', (2, 3, 4, 8)

    # E0–E3: transições slow→fast em pares RCS representativos
    for name, r, k_level, fast, slow in [
        ('E0', 4, 'base', 2, 1),
        ('E1', 4, 'rich', 2, 1),
        ('E2', 4, 'base', 3, 1),
        ('E3', 6, 'base', 2, 1),
    ]:
        W = make_W(r)
        K = {w: kappa_profile(w, level=k_level) for w in W}
        # usa alpha=1 como transição representativa (onde RCS aparece)
        ss, sf = slow * 1, fast * 1
        yield f'{name} σ{ss}→σ{sf}', W, K, ss, sf, '00', (2, 3, 4, 5, 8)

def main():
    print('=' * 70)
    print('PR19 — PPR-3: Θ sobre provas de ramos (R_w, cond. A∨B∨C)')
    print('=' * 70)

    total_pi = 0
    total_ok = 0
    total_fail = 0
    max_ratio = 0.0
    cond_counts = {'A': 0, 'B': 0, 'C': 0, 'FAIL': 0}

    for name, W, K, sigma_T, sigma_Tp, w_star, b_vals in scenarios():
        print(f'\n=== {name} ===')
        scen_ok = 0
        scen_total = 0
        for b in b_vals:
            w0 = first_uncovered(sigma_T, b, W, K)
            if w0 is None:
                continue  # π não existe (T=all-cov)
            k0 = K[w0]
            pi = cert_uncov(w0, sigma_T, b, k0, valid=True)
            if not pi['valid']:
                continue
            total_pi += 1
            scen_total += 1
            theta_out, cond, r_w0 = Theta(pi, sigma_Tp, W, K, w_star)
            cond_counts[cond] = cond_counts.get(cond, 0) + 1
            ok = verify_theta(pi, theta_out, cond, sigma_Tp, W, K, w_star)
            total_ok += 1 if ok else 0
            total_fail += 0 if ok else 1
            scen_ok += 1 if ok else 0
            if ok and pi:
                ratio = cert_bits(theta_out) / max(1, cert_bits(pi))
                max_ratio = max(max_ratio, ratio)
            status = 'OK' if ok else f'FAIL({cond})'
            th_w = theta_out['w'] if theta_out and theta_out.get('w') else (
                'ALL' if theta_out and theta_out.get('claim') == 'ALL_COV' else '?')
            print(f'  b={b}: π(w0={w0},σ={sigma_T}) -> Θ [{cond}] '
                  f'->{th_w} @σ={sigma_Tp}  {status}')
        print(f'  subtotal: {scen_ok}/{scen_total}')

    print('\n' + '=' * 70)
    print('RESUMO PR19 (CC-Θ)')
    print('=' * 70)
    print(f'  π válidos processados : {total_pi}')
    print(f'  Θ corretos (CC-Θ)     : {total_ok}/{total_pi}')
    print(f'  Condições disparadas  : A={cond_counts["A"]}, '
          f'B={cond_counts["B"]}, C={cond_counts["C"]}, '
          f'FAIL={cond_counts["FAIL"]}')
    print(f'  Máx |Θ(π)|/|π|        : {max_ratio:.2f}  (cota: ≤ 2+log|W|/|π|)')
    all_ok = (total_fail == 0 and total_pi > 0)
    print('=' * 70)
    if all_ok:
        print('*** PR19: CC-Θ VERIFICADO no modelo finito ***')
        print('*** Θ é polinomial: |Θ(π)| = |π| + O(log |W|) ***')
        print('*** Status: Θ construído e CORRETO sob (A)∨(B)∨(C) ***')
    else:
        print('*** ATENCAO: CC-Θ falhou — revisar Θ ou predicado ***')
    return all_ok

if __name__ == '__main__':
    main()

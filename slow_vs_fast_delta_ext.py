"""
PR16: Extensao do exp.13 — varia kappa, razao slow:fast, |W|.
Testa robustez da RCS (slow vs fast em delta com Phi fixa).
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from itertools import product

def make_W(r):
    return [''.join(p) for p in product('01', repeat=r)]

def kappa_profile(w, w_star='00', level='base'):
    """
    base: w* -> 2; genéricas hash 0/1
    rich: w* -> 3; prefixo w*+mid -> 2; resto 0/1
    """
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

def delta(sigma_T, b, KAPPA, W):
    d = 0
    for w in W:
        k = KAPPA[w]
        if k > sigma_T:
            d += 1
        else:
            if (k + 1) > b:
                d += 1
    return d

def sigma_fast(alpha, step=2):
    return step * alpha

def sigma_slow(alpha, step=1):
    return step * alpha

def run_config(name, r, k_level, fast_step, slow_step, alpha_max=6, b_values=(1,2,3,4,5,8)):
    W = make_W(r)
    KAPPA = {w: kappa_profile(w, level=k_level) for w in W}
    print(f"\n=== {name} ===")
    print(f"r={r} (|W|={len(W)}), kappa={k_level}, "
          f"fast_step={fast_step}, slow_step={slow_step}")
    count = 0
    total = 0
    examples = []
    for alpha in range(alpha_max + 1):
        sf = sigma_fast(alpha, fast_step)
        ss = sigma_slow(alpha, slow_step)
        for b in b_values:
            df = delta(sf, b, KAPPA, W)
            ds = delta(ss, b, KAPPA, W)
            total += 1
            if df != ds:
                count += 1
                if len(examples) < 3:
                    examples.append((alpha, b, df, ds))
    print(f"RCS pares (alpha,b) com delta_F != delta_S: {count}/{total}")
    for e in examples:
        print(f"  exemplo alpha={e[0]}, b={e[1]}: dF={e[2]}, dS={e[3]}")
    return count > 0, count, total

def main():
    print("=" * 70)
    print("PR16 — Robustez da RCS (slow vs fast, Phi fixa)")
    print("=" * 70)

    results = []
    # Base (replica 13)
    ok, c, t = run_config("E0 base (replica 13)", r=4, k_level='base',
                          fast_step=2, slow_step=1)
    results.append(("E0 base", ok, c, t))
    # E1: kappa rico
    ok, c, t = run_config("E1 kappa rich (3 niveis)", r=4, k_level='rich',
                          fast_step=2, slow_step=1)
    results.append(("E1 rich-kappa", ok, c, t))
    # E2: razao 1:3
    ok, c, t = run_config("E2 razao fast:slow = 3:1", r=4, k_level='base',
                          fast_step=3, slow_step=1)
    results.append(("E2 3:1", ok, c, t))
    # E3: |W|=64
    ok, c, t = run_config("E3 |W|=64", r=6, k_level='base',
                          fast_step=2, slow_step=1)
    results.append(("E3 r=6", ok, c, t))

    print("\n" + "=" * 70)
    print("RESUMO PR16")
    print("=" * 70)
    all_ok = True
    for name, ok, c, t in results:
        status = "RCS=SIM" if ok else "RCS=NAO"
        print(f"  {name:20s}: {status}  ({c}/{t} pares)")
        all_ok = all_ok and ok
    print("=" * 70)
    if all_ok:
        print("*** RCS ROBUSTA em todas as configuracoes testadas ***")
    else:
        print("*** ATENCAO: alguma config falhou — investigar ***")
    return all_ok

if __name__ == "__main__":
    main()

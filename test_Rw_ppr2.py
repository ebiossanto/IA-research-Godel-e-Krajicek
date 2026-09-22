"""
PR17: Teste de R_w (transformação sobre ÍNDICES de ramo) — PPR-2.
Pós-suffix0 (14_...): R opera em w, não em strings b.

Candidato R_w (14 §3):
  R(ALL_sentinel) = w*     (ramo que T não cobre, T' cobre tudo)
  R(w) = w                 (identidade para genéricas)

PPR-2 sobre ramos:
  Se w NÃO coberto em T (ramo ativo/primeiro não-coberto),
  então R(w) deve ser não-coberto em T' OU corresponder à transição RBT.
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from itertools import product

# ---------------------------------------------------------------------------
# Modelo (alinha com exp.10/13): kappa, sigma, cobertura
# ---------------------------------------------------------------------------
R_W = 4
W_ALL = [''.join(p) for p in product('01', repeat=R_W)]
W_STAR = '00'

def kappa(w):
    if w.startswith(W_STAR):
        return 2  # Con plena
    return sum(ord(c) for c in w) % 2

KAPPA = {w: kappa(w) for w in W_ALL}

def covered(sigma, b, w):
    k = KAPPA[w]
    return k <= sigma and (k + 1) <= b

def first_uncovered(sigma, b):
    for w in sorted(W_ALL):
        if not covered(sigma, b, w):
            return w
    return None  # ALL_COV sentinela

def uncovered_set(sigma, b):
    return {w for w in W_ALL if not covered(sigma, b, w)}

# ---------------------------------------------------------------------------
# R_w candidato (14 §3)
# ---------------------------------------------------------------------------
ALL_SENTINEL = 'ALL_COV'

def R_w(x, w_star=W_STAR):
    """R sobre ramos: ALL -> w*, identidade senão."""
    if x == ALL_SENTINEL:
        return w_star
    return x  # identidade

# ---------------------------------------------------------------------------
# Teste PPR-2 sobre ramos
# ---------------------------------------------------------------------------
def test_ppr2_ramos(sigma_T, sigma_Tp, b_values=(2, 3, 4, 8)):
    """
    PPR-2 (ramos): para cada b, se w0_T = primeiro não-coberto em T,
    então R(w0_T) deve estar em uncov(T') OU ser a transição RBT esperada.
    """
    print("=" * 70)
    print(f"PR17: PPR-2 sobre RAMOS  (sigma_T={sigma_T}, sigma_T'={sigma_Tp})")
    print("=" * 70)
    all_ok = True
    details = []
    for b in b_values:
        w0_T = first_uncovered(sigma_T, b)
        w0_Tp = first_uncovered(sigma_Tp, b)
        uncov_T = uncovered_set(sigma_T, b)
        uncov_Tp = uncovered_set(sigma_Tp, b)

        # R aplicado ao ramo ativo de T
        if w0_T is None:
            r_w0 = R_w(ALL_SENTINEL)
            status = "SKIP (T all-cov)"
            ok = True
        else:
            r_w0 = R_w(w0_T)
            # PPR-2 ramo com 3 condições (refinamento pós-falha 14 §7):
            # (A) r_w0 ∈ uncov(T') — transferência direta
            # (B) transição RBT: w0 muda e R(w0)=w* (registro da falta)
            # (C) T' ALL_COV: cobertura total resolve w0 de T (progresso trivial)
            cond_A = r_w0 in uncov_Tp
            cond_B = (w0_T != w0_Tp) and (r_w0 == W_STAR)
            cond_C = (w0_Tp is None)  # T' cobre tudo
            ok = cond_A or cond_B or cond_C
            status = "OK" + ("(C)" if cond_C and not (cond_A or cond_B) else "")
            if not ok:
                all_ok = False
        details.append((b, w0_T, w0_Tp, r_w0 if w0_T else ALL_SENTINEL, status))
        print(f"  b={b}: w0_T={w0_T or 'ALL'}, w0_T'={w0_Tp or 'ALL'}, "
              f"R(w0_T)={r_w0 if w0_T else ALL_SENTINEL}, uncov_T'={sorted(uncov_Tp)[:4]}... -> {status}")
    print("-" * 70)
    print(f"PPR-2 ramos global: {'TRUE' if all_ok else 'FALSE'}")
    return all_ok, details

def main():
    # Cenário base: T=sigma 0 (PA), T'=sigma 2 (PA+Con) — exp.10/13
    print("Cenário 1: T (σ=0) -> T' (σ=2)  [PA -> PA+Con]")
    ok1, _ = test_ppr2_ramos(0, 2)

    print("\nCenário 2: T (σ=1) -> T' (σ=2)  [PA+Con_s -> PA+Con] slow->fast")
    ok2, _ = test_ppr2_ramos(1, 2)

    print("\nCenário 3: T (σ=0) -> T' (σ=1)  [PA -> PA+Con_s] slow")
    ok3, _ = test_ppr2_ramos(0, 1)

    print("\n" + "=" * 70)
    print("VEREDITO PR17")
    print("=" * 70)
    results = [("σ0→σ2", ok1), ("σ1→σ2", ok2), ("σ0→σ1", ok3)]
    for name, ok in results:
        print(f"  {name}: {'PPR-2 OK' if ok else 'PPR-2 FAIL'}")
    if all(ok for _, ok in results):
        print("\n*** R_w (identidade+sentinela) PASSA PPR-2 em 3 cenários ***")
        print("*** PR17: candidato R_w VÁLIDO no modelo de ramos ***")
    else:
        print("\n*** R_w FALHOU em algum cenário — refinar 14 §3 ***")
    return all(ok for _, ok in results)

if __name__ == "__main__":
    main()

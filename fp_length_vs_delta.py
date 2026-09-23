#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PR25 — Freund–Pakhomov (comprimento) vs δ (déficit de cobertura)

Pergunta PR7 (INDICE / 10 §1.4 / 12): Con*(PA) / provas polinomiais de
slow consistency aparecem em δ_T(Φ,b)?

Modelo estrutural (não PA real). Lei de comprimento DEPENDE de n:
  - alvo lento (slow target): s(n) = poly(n)  ~ n^2
  - alvo rápido (fast target): s(n) = 2^n     (ou INF se "inviável")

Hipóteses pré-registradas:
  H_identity: δ(b) = #{w : s(w) > b} e min{b: δ=0} = max_w s(w)
  H_FP-in-δ : δ_PA(Φ_slow, b(n^c)) < δ_PA(Φ_fast, b(n^c)) em ≥1 (n,c)
  H_growth  : β_slow(n) polinomial; β_fast(n) super-polinomial

Saídas O1–O10 do design (24 §5 / plan PR25).
Exit 0 se H_identity e experimento executam sem erro (separação = resultado).
"""

from __future__ import annotations

import math
import sys

# Windows console (cp1252) cannot encode Greek; force UTF-8.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def s_slow(n: int) -> int:
    """Comprimento mínimo alvo lento (Freund–Pakhomov: polinomial)."""
    return max(1, n * n)


def s_fast(n: int) -> int:
    """Comprimento mínimo alvo rápido (exponencial)."""
    return 1 << n if n <= 20 else 10**18


def lengths(n: int, target: str, W: list[str]) -> dict[str, int]:
    """Lei de comprimento s_T(Φ^w, n) por obrigação.
    w* (primeiro) carrega a consistência difícil; demais genéricas baratas."""
    if target == "slow":
        hard = s_slow(n)
    elif target == "fast":
        hard = s_fast(n)
    else:
        raise ValueError(target)
    out = {}
    for i, w in enumerate(W):
        if i == 0:  # w* : obrigação de Con
            out[w] = hard
        else:
            out[w] = 1 + (hash(w) % 3)  # genéricas: comprimento fixo pequeno
    return out


def delta(L: dict[str, int], b: int) -> int:
    return sum(1 for v in L.values() if v > b)


def beta(L: dict[str, int], b_max: int = 1 << 30) -> int:
    """min{b : δ(b)=0} = max_w s(w)."""
    return max(L.values()) if L else 0


def is_poly_fit(ns: list[int], betas: list[int], c_max: int = 4) -> bool:
    """log-log slope ≤ c_max em todos os pares consecutivos (H_growth)."""
    pts = [(math.log(n), math.log(b)) for n, b in zip(ns, betas) if b > 0 and n > 0]
    if len(pts) < 2:
        return True
    slopes = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x1 > x0:
            slopes.append((y1 - y0) / (x1 - x0))
    return all(s <= c_max + 1e-9 for s in slopes)


def main() -> int:
    print("=" * 70)
    print("PR25: Freund–Pakhomov comprimento vs delta (modelo estrutural)")
    print("=" * 70)

    r = 6
    W = [format(i, f"0{r}b") for i in range(1 << r)]
    ns = [4, 6, 8, 10, 12, 14, 16]
    c_grid = [1, 2, 3, 4]
    budgets_extra = [1, 2, 4, 8, 16, 32, 64]

    o1_ok = True
    table = {"slow": [], "fast": []}

    print("\n=== Comprimento κ(n) = max_w s(n) e limiar β = min{b: δ=0} ===")
    print(f"{'n':>4} {'κ_slow':>10} {'κ_fast':>14} {'β_slow':>10} {'β_fast':>14}")
    for n in ns:
        row = {}
        for tgt in ("slow", "fast"):
            L = lengths(n, tgt, W)
            k = max(L.values())
            bstar = beta(L)
            # H_identity
            grid = sorted(set(budgets_extra + [k, k + 1, 0, 10**9]))
            for b in grid:
                d = delta(L, b)
                expect = sum(1 for v in L.values() if v > b)
                if d != expect or bstar != k:
                    o1_ok = False
            row[tgt] = (k, bstar, L)
            table[tgt].append((n, k, bstar))
        print(f"{n:4d} {row['slow'][0]:10d} {row['fast'][0]:14d} "
              f"{row['slow'][1]:10d} {row['fast'][1]:14d}")

    o1 = o1_ok
    print(f"\nO1 H_identity (δ=#{{w: s>b}}; β=κ): {'OK' if o1 else 'FALHOU'}")

    # H_growth
    ns_s = [x[0] for x in table["slow"]]
    ns_f = [x[0] for x in table["fast"]]
    bet_s = [x[1] for x in table["slow"]]
    bet_f = [x[1] for x in table["fast"]]
    o2 = is_poly_fit(ns_s, bet_s, c_max=4)
    o3 = not is_poly_fit(ns_f, bet_f, c_max=4) or max(bet_f) > (max(ns_f) ** 4)
    print(f"O2 β_slow polinomial (slope≤4): {'OK' if o2 else 'NAO'}")
    print(f"O3 β_fast super-polinomial:      {'OK' if o3 else 'NAO'}")

    # H_FP-in-δ: em budgets polinomiais, δ_slow < δ_fast
    o4_hits = []
    for n in ns:
        Ls = lengths(n, "slow", W)
        Lf = lengths(n, "fast", W)
        for c in c_grid:
            b = max(1, n**c)
            ds, df = delta(Ls, b), delta(Lf, b)
            if ds < df:
                o4_hits.append((n, c, b, ds, df))
    o4 = len(o4_hits) > 0
    print(f"O4 H_FP-in-δ (∃n,c: δ_slow < δ_fast em b=n^c): "
          f"{'SIM (' + str(len(o4_hits)) + ' pares)' if o4 else 'NAO'}")
    for h in o4_hits[:8]:
        print(f"    n={h[0]} c={h[1]} b={h[2]} δ_slow={h[3]} δ_fast={h[4]}")

    # O7: comprimento separa mas δ igual em todos os budgets testados?
    o7 = False
    for n in ns:
        Ls = lengths(n, "slow", W)
        Lf = lengths(n, "fast", W)
        if max(Ls.values()) != max(Lf.values()):
            same = all(
                delta(Ls, b) == delta(Lf, b)
                for b in budgets_extra + [n, n**2, n**4, 1 << n]
                if b < 10**18
            )
            if same:
                o7 = True
    print(f"O7 cego: comprimento difere mas δ idêntico: "
          f"{'SIM (NAO-alinhado)' if o7 else 'NAO'}")

    # Telescoping / ganho G(α) = δ(0)-δ(α) com hierarquia lenta/rápida
    # (herda slow_vs_fast: σ_slow=α, σ_fast=2α) sobre leis de n
    print("\n=== Ganho acumulado G(α)=δ0−δα (b=n²) com alvo slow n=8 ===")
    n0 = 8
    L0 = lengths(n0, "slow", W)
    # força: alvo slow precisa σ≥κ_w* para cobrir w*
    k_star = L0[W[0]]
    g_vals = []
    for alpha in range(0, 6):
        # cada passo lento +1 de σ; rápido +2 (modelo 13)
        sigma_s = alpha
        # cobertura: w coberto sse s(w)≤σ e s(w)≤b  (aqui σ modela "força", b=n²)
        b = n0 * n0
        # reinterpreta: se σ < s(w*), w* não coberto → δ ≥ 1
        # genéricas s≤3 sempre cobertas se b≥3
        ds = sum(1 for w in W if L0[w] > sigma_s or L0[w] > b)
        g_vals.append(ds)
    print("  α:", list(range(6)))
    print("  δ_slow_profile:", g_vals)
    print("  (σ_slow(α)=α; confere degrau em α≥κ_w*=n²)")

    print("\n" + "=" * 70)
    align = o1 and o4 and not o7
    if o1 and not o4:
        verdict = "PR7: δ NÃO captura separação FP no modelo (O7/O4)"
    elif align:
        verdict = "PR7: SIM — separação FP visível em δ (modelo estrutural)"
    else:
        verdict = "PR7: INCONCLUSIVO / parcial"
    print(f"*** {verdict} ***")
    print(f"*** H_identity={'OK' if o1 else 'FAIL'}; "
          f"H_FP-in-δ={'OK' if o4 else 'FAIL'}; O7={'HIT' if o7 else 'miss'} ***")
    print("=" * 70)

    # Exit 0: experimento válido (H_identity obrigatório)
    if not o1:
        print("ERRO: H_identity falhou — experimento inválido")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

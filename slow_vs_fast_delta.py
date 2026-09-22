"""
EXPERIMENTO 13: Slow vs Fast em delta_T(Phi,b) — teste da Hipotese RCS
Modelo estrutural fiel: sigma (forca reflexao) e kappa (custo obrigacao).
Phi FIXA para todas as hierarquias (essencial).
"""

import sys
import io
# Forcar UTF-8 no stdout (Windows cp1252)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from itertools import product

# ---------------------------------------------------------------------------
# SETUP
# ---------------------------------------------------------------------------
R_W = 4  # |w| = 4 bits -> 16 obrigacoes
W_ALL = [''.join(p) for p in product('01', repeat=R_W)]
W_STAR = '00'  # prefixo de w* (obrigacao Con(PA))

# Kappa: custo de reflexao para provar Phi^w
# w* precisa de Con plena (kappa=2); genericas sao mais faceis
def kappa(w, w_star=W_STAR):
    if w.startswith(w_star):
        return 2  # Con(PA) completa
    # genericas: hash simples -> 0 ou 1
    h = sum(ord(c) for c in w) % 2
    return h  # 0 ou 1

# Precomputar kappa
KAPPA = {w: kappa(w) for w in W_ALL}
print("Kappa por obrigacao:")
for w in sorted(W_ALL):
    print(f"  {w}: kappa={KAPPA[w]}")

# ---------------------------------------------------------------------------
# HIERARQUIAS
# ---------------------------------------------------------------------------
# Sigma: nivel de forca de reflexao da teoria
# RAPIDO: cada passo +2 (Con completa)
# LENTO:  cada passo +1 (Con_s mais fraca)
# sigma_sobra: PA=0, PA+Con_s=1, PA+Con=2  (Con_s < Con)

def sigma_fast(alpha):
    """F_alpha = PA + alpha passos de Con completa."""
    return 2 * alpha  # F_0=0, F_1=2, F_2=4...

def sigma_slow(alpha):
    """S_alpha = PA + alpha passos de Con_s."""
    return 1 * alpha  # S_0=0, S_1=1, S_2=2...

# ---------------------------------------------------------------------------
# DELTA
# ---------------------------------------------------------------------------
def delta(sigma_T, b, w_list=None):
    """
    delta_T(Phi,b) = #{w : kappa(w) > sigma_T OR (kappa<=sigma AND prova>b)}
    Modelo: prova(w) = kappa(w)+1
    """
    if w_list is None:
        w_list = W_ALL
    d = 0
    for w in w_list:
        k = KAPPA[w]
        if k > sigma_T:
            d += 1  # nao alcanca forca
        else:
            proof_len = k + 1  # modelo
            if proof_len > b:
                d += 1  # forca ok mas prova longa demais
    return d

def profile(hier_fn, alpha_max, b_values, label):
    """Retorna dict b -> lista de delta por alpha."""
    print(f"\n=== Perfil {label} ===")
    print(f"{'alpha':>5} {'sigma':>5} " + " ".join(f"δ(b={b})" for b in b_values))
    results = {b: [] for b in b_values}
    for alpha in range(alpha_max + 1):
        sig = hier_fn(alpha)
        row = [f"{alpha:>5}", f"{sig:>5}"]
        for b in b_values:
            d = delta(sig, b)
            results[b].append(d)
            row.append(f"{d:>6}")
        print(" ".join(row))
    return results

# ---------------------------------------------------------------------------
# EXECUCAO
# ---------------------------------------------------------------------------
def main():
    alpha_max = 5
    b_values = [1, 2, 3, 4, 8]

    print("=" * 70)
    print("EXPERIMENTO 13: Slow vs Fast — teste RCS")
    print(f"Phi fixa (Con PA em w*), |W|={len(W_ALL)}, w*={W_STAR}")
    print("kappa(w*)=2 (Con plena); genericas kappa=0 ou 1")
    print("sigma_fast: +2/pass; sigma_slow: +1/pass  (Con_s < Con)")
    print("=" * 70)

    F = profile(sigma_fast, alpha_max, b_values, "RAPIDA (F_alpha)")
    S = profile(sigma_slow, alpha_max, b_values, "LENTA (S_alpha)")

    # ---------------------------------------------------------------------------
    # COMPARACAO — RCS?
    # ---------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("COMPARACAO delta_F vs delta_S (mesma Phi, mesmo alpha)")
    print("=" * 70)
    print(f"{'alpha':>5} {'b':>4} {'δ_F':>6} {'δ_S':>6} {'F-S':>6} {'RCS?':>6}")
    print("-" * 40)

    rcs_count = 0
    total_pairs = 0
    for alpha in range(alpha_max + 1):
        for b in b_values:
            df = F[b][alpha]
            ds = S[b][alpha]
            diff = df - ds
            rcs = "SIM" if df != ds else "nao"
            if df != ds:
                rcs_count += 1
            total_pairs += 1
            # so mostra onde ha diferenca ou poucos niveis
            if df != ds or alpha <= 3:
                print(f"{alpha:>5} {b:>4} {df:>6} {ds:>6} {diff:>6} {rcs:>6}")

    print("-" * 40)
    print(f"RCS: {rcs_count}/{total_pairs} pares (alpha,b) com delta_F != delta_S")

    # ---------------------------------------------------------------------------
    # VEREDITO
    # ---------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("VEREDITO")
    print("=" * 70)
    if rcs_count > 0:
        print("*** RCS CONFIRMADA neste caso ***")
        print("delta detecta slow vs fast para a mesma Phi.")
        print("Exemplos (alpha, b) com diferenca:")
        shown = 0
        for alpha in range(alpha_max + 1):
            for b in b_values:
                if F[b][alpha] != S[b][alpha]:
                    print(f"  alpha={alpha}, b={b}: δ_F={F[b][alpha]}, δ_S={S[b][alpha]}")
                    shown += 1
                    if shown >= 5:
                        break
            if shown >= 5:
                break
        print("\nInterpretacao: perfil alpha -> delta carrega info alem do ordinal final")
        print("(ambas progressoes atingem sigma alto, mas por caminhos diferentes).")
    else:
        print("*** RCS NAO se manifestou com esta Phi/kappa/sigma ***")
        print("Tentar: Phi mais rica, kappa desigual para mais w, ou Con_s<Con mais refinado.")

    # Curva de ganho acumulado
    print("\n--- Ganho acumulado G(alpha) = δ(0) - δ(alpha) [b=2] ---")
    b = 2
    d0_F = F[b][0]
    d0_S = S[b][0]
    print(f"{'alpha':>5} {'G_F':>6} {'G_S':>6}")
    for alpha in range(alpha_max + 1):
        gF = d0_F - F[b][alpha]
        gS = d0_S - S[b][alpha]
        print(f"{alpha:>5} {gF:>6} {gS:>6}")

    return rcs_count > 0

if __name__ == "__main__":
    main()

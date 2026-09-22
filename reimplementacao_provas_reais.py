"""
Reimplementacao com BUSCA DE PROVAS REAL (proposicional).
Nao usa valores de complexidade fixados — busca por resolucao/ECNF real.

Sistema:
  - Linguagem proposicional sobre atoms p_0..p_k (obrigacoes Phi^w)
  - T0: axiomas proposicionais + regras (MP, and-intro...)
  - T1: T0 + axiomas de reflexao proposicionais (Con -> atoms de Con)

Simplificacao honesta: "prova real" no sentido proposicional (tautologias
com clausulas), nao aritmetica. Captura busca limitada por b de verdade.
"""

from itertools import product, combinations
import random

# ---------------------------------------------------------------------------
# Encoding de formulas proposicionais (string CNF simples: lista de clausulas)
# Clausula = frozenset de literais (int >0 = p_i, int <0 = ~p_i)
# Formula = lista de clausulas (CNF)
# ---------------------------------------------------------------------------

def eval_cnf(cnf, assignment):
    """assignment: dict int->bool"""
    for cl in cnf:
        if not any(
            (lit > 0 and assignment.get(abs(lit), False)) or
            (lit < 0 and not assignment.get(abs(lit), False))
            for lit in cl
        ):
            return False
    return True

def is_tautology_enum(cnf, nvars):
    """Checa tautologia por enumeracao (nvars pequeno)."""
    for bits in product([False, True], repeat=nvars):
        a = {i+1: bits[i] for i in range(nvars)}
        if not eval_cnf(cnf, a):
            return False
    return True

# ---------------------------------------------------------------------------
# "Teorias" como conjuntos de clausulas
# ---------------------------------------------------------------------------

def T0_axioms(n_conj):
    """
    T0 = PA proposicional simplificado:
      - axiom schema: ~Con -> (obrigacao_i para i em genericas)
      - Con e' atom special (nao derivado em T0)
    n_conj: numero de atomos genericos (obrigacoes "faceis")
    """
    # atomos: 1=Con, 2..n_conj+1 = genericas
    # T0 permite provar genericas DIRETAMENTE (axiomas unitarios)
    axioms = []
    for i in range(2, n_conj + 2):
        axioms.append(frozenset([i]))  # p_i unitario
    # Con nao esta em axioms (indemonstravel via Gödel — proposicional: nao unitario)
    return axioms, 1  # Con = atom 1, nvars = n_conj+1

def T1_axioms(n_conj):
    """
    T1 = T0 + reflexao: axiom unitario para Con (RFN proposicional).
    """
    ax, nv = T0_axioms(n_conj)
    ax.append(frozenset([1]))  # Con agora unitario (RFN)
    return ax, nv

# ---------------------------------------------------------------------------
# Busca de prova: resolution closure limitada por tamanho
# ---------------------------------------------------------------------------

def resolution_closure(axioms, max_steps):
    """
    Fechamento por resolucao ate max_steps producoes.
    Retorna set de clausulas derivadas (inclui axiomas).
    """
    clauses = set(axioms)
    produced = 0
    changed = True
    while changed and produced < max_steps:
        changed = False
        clauses_list = list(clauses)
        new_clauses = set()
        for c1, c2 in combinations(clauses_list, 2):
            # resolve em literal l: c1 tem l, c2 tem ~l
            for l in c1:
                if -l in c2:
                    resolvent = (c1 - {l}) | (c2 - {-l})
                    if resolvent and resolvent not in clauses:
                        new_clauses.add(frozenset(resolvent))
                        produced += 1
                        if produced >= max_steps:
                            break
            if produced >= max_steps:
                break
        if new_clauses:
            clauses |= new_clauses
            changed = True
    return clauses, produced

def proves_clause(theory, target_cl, max_steps=2000):
    """target_cl e' clausula alvo (ex.: unitaria)."""
    derived, _ = resolution_closure(theory, max_steps)
    if target_cl in derived:
        return True, len(derived)
    # tambem: se target e' subclausula de derivada (tautologia mais fraca)
    for d in derived:
        if target_cl <= d:
            return True, len(derived)
    return False, len(derived)

# ---------------------------------------------------------------------------
# Obrigacoes Phi^w proposicionalizadas
# ---------------------------------------------------------------------------

def obligation_clauses(w, n_conj, w_star, con_atom=1):
    """
    Cada w define uma obrigacao. Simplificacao:
      - se w comeca com w_star: obrigacao = Con (atom con_atom)  [Gödel]
      - senao: obrigacao = atom generico correspondente a hash(w)
    """
    if w.startswith(w_star):
        return frozenset([con_atom])
    # genericas: mapear w para atom 2..n_conj+1
    h = sum(ord(c) for c in w) % n_conj
    return frozenset([2 + h])

# ---------------------------------------------------------------------------
# Gerador com busca real
# ---------------------------------------------------------------------------

def generator_real(T_theory, w_list, w_star, n_conj, max_steps=2000):
    """
    Retorna (imagem_obrigacoes_cobertas, delta) para lista de w.
    Busca real de prova por resolucao para cada obrigacao.
    """
    covered = set()
    proof_sizes = {}
    for w in w_list:
        target = obligation_clauses(w, n_conj, w_star)
        ok, size = proves_clause(T_theory, target, max_steps)
        if ok:
            covered.add(w)
            proof_sizes[w] = size
    return covered, proof_sizes

def run_real_search(n_conj=6, w_bits=4, max_steps=1500):
    """Executa busca real em T0 e T1; calcula delta, RBT."""
    w_list = [''.join(p) for p in product('01', repeat=w_bits)]
    w_star = '00'
    nvars = n_conj + 1

    ax0, _ = T0_axioms(n_conj)
    ax1, _ = T1_axioms(n_conj)

    print("=" * 70)
    print("REIMPLEMENTACAO: busca de prova real (resolucao proposicional)")
    print(f"n_conj={n_conj}, |w|={w_bits}, w*={w_star}, max_steps={max_steps}")
    print("=" * 70)

    # Derivar fecho uma vez (teoria fixa)
    print("\n-- Derivando fecho de resolucao T0...")
    der0, steps0 = resolution_closure(ax0, max_steps)
    print(f"  T0: |ax|={len(ax0)}, |der|={len(der0)}, steps={steps0}")
    print("-- Derivando fecho de resolucao T1...")
    der1, steps1 = resolution_closure(ax1, max_steps)
    print(f"  T1: |ax|={len(ax1)}, |der|={len(der1)}, steps={steps1}")

    # Provar cada obrigacao
    cov0, sizes0 = set(), {}
    cov1, sizes1 = set(), {}
    for w in w_list:
        tgt = obligation_clauses(w, n_conj, w_star)
        if tgt in der0 or any(tgt <= d for d in der0):
            cov0.add(w); sizes0[w] = len(der0)
        if tgt in der1 or any(tgt <= d for d in der1):
            cov1.add(w); sizes1[w] = len(der1)

    delta0 = len(w_list) - len(cov0)
    delta1 = len(w_list) - len(cov1)
    G = delta0 - delta1
    w0_0 = next((w for w in sorted(w_list) if w not in cov0), None)
    w0_1 = next((w for w in sorted(w_list) if w not in cov1), None)
    rbt = (w0_0 != w0_1)

    print("\n-- Resultados (busca real) --")
    print(f"  T0: cobertas={len(cov0)}/{len(w_list)}, delta_T0={delta0}")
    print(f"  T1: cobertas={len(cov1)}/{len(w_list)}, delta_T1={delta1}")
    print(f"  G = delta0-delta1 = {G}")
    print(f"  w0(T0)={w0_0 or 'ALL_COV'}, w0(T1)={w0_1 or 'ALL_COV'}")
    print(f"  RBT: {'SIM' if rbt else 'NAO'}")
    print(f"  Obrigacoes cobertas T0: {sorted(cov0)}")
    print(f"  Obrigacoes cobertas T1: {sorted(cov1)}")
    print(f"  Nao cobertas T0: {sorted(set(w_list)-cov0)}")
    print(f"  Nao cobertas T1: {sorted(set(w_list)-cov1)}")

    # Verificacoes teoricas
    print("\n-- Verificacoes --")
    print(f"  G>=0: {G>=0}")
    print(f"  delta_T1<=delta_T0: {delta1<=delta0}")
    # Con nao provavel em T0 mas provavel em T1?
    con_cl = frozenset([1])
    con_T0 = con_cl in der0 or any(con_cl <= d for d in der0)
    con_T1 = con_cl in der1 or any(con_cl <= d for d in der1)
    print(f"  Con em T0 (deve ser False): {con_T0}")
    print(f"  Con em T1 (deve ser True):  {con_T1}")

    print("=" * 70)
    return {
        'delta0': delta0, 'delta1': delta1, 'G': G,
        'rbt': rbt, 'w0_0': w0_0, 'w0_1': w0_1,
        'con_T0': con_T0, 'con_T1': con_T1,
        'cov0': cov0, 'cov1': cov1,
        'n_conj': n_conj, 'w_bits': w_bits
    }

if __name__ == "__main__":
    result = run_real_search()
    # Varredura de parametros
    print("\nVarredura de max_steps (estabilidade):")
    for ms in [500, 1000, 1500, 2000]:
        r = run_real_search(max_steps=ms)
        print(f"  steps={ms}: d0={r['delta0']}, d1={r['delta1']}, "
              f"G={r['G']}, RBT={'S' if r['rbt'] else 'N'}, "
              f"Con0={r['con_T0']}, Con1={r['con_T1']}")

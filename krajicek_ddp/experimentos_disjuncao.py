# -*- coding: utf-8 -*-
"""
experimentos_disjuncao.py  --  EQUIPE C (casos concretos / sistemas fracos)
Problema DD_P de Krajicek (arXiv:2506.20221v4), secao de experimentos.

Objetivo: investigar computacionalmente a propriedade de disjuncao viavel
(feasible disjunction property) e o problema de busca DD_P para RESOLUCAO.

Convencao de trabalho (ver documento C_disjuncao_viavel.md, Sec. 3.1):
  * um disjunto alpha_i e uma formula em DNF sobre um conjunto de atomos X_i;
  * os conjuntos X_1, ..., X_m sao disjuntos (disjuncao disjunta);
  * a prova pi : Res |- vee_i alpha_i corresponde a uma refutacao por
    resolucao do conjunto de clausulas  Lambda = vee_i C_i,  C_i = nao-alpha_i
    (uma CNF sobre X_i, com uma clausula por termo de alpha_i);
  * "alpha_i e tautologia"  <=>  "C_i e insatisfativel".

O script faz 4 coisas:
  (1) gera instancias aleatorias (C_1, C_2) com exatamente um lado
      insatisfativel, e constroi uma refutacao por saturacao;
  (2) verifica o ALGORITMO DE PROJECAO (Teorema C.1 do documento: recorte
      ("trimming") que elimina enfraquecimentos + lema da pureza), que deve
      devolver sempre um indice i* com C_{i*} insatisfativel, e ate uma
      refutacao pura dessa lado de tamanho <= |pi|;
  (3) testa heuristicas ingenuas ("escolher o maior alpha_i", "o que tem
      mais termos", "o que tem mais termos unitarios", ...) e mede as taxas
      de falha; procura contra-exemplos minimos por enumeracao exaustiva;
  (4) testes de unidade: uma refutacao "misturada" com enfraquecimentos
      (que quebra o rotulo ingenuo "ultimo passo") ainda e tratada pelo
      algoritmo de projecao; e a extensao D_P (disjunctos com atomos p
      compartilhados + restricao pela atribuicao a) tambem funciona.

Rodar com:  python experimentos_disjuncao.py
Somente biblioteca padrao (sem dependencias externas).
"""

import random
import itertools
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ---------------------------------------------------------------------------
# Representacao: literal = 2*var + s   (s = 1 significa negado).
# complemento(l) = l ^ 1.   Clausula = frozenset de literais.
# ---------------------------------------------------------------------------


def compl(l):
    return l ^ 1


def is_taut_clause(cl):
    return any(compl(l) in cl for l in cl)


def clause_vars(cl):
    return {l >> 1 for l in cl}


def dnf_tautology(terms, nvars, off=0):
    """Teste exaustivo: a DNF (lista de termos) e tautologia?
    off = deslocamento das variaveis locais (var_local = var - off)."""
    for m in range(1 << nvars):
        ok = False
        for t in terms:
            good = True
            for l in t:
                var, s = (l >> 1) - off, l & 1
                if ((m >> var) & 1) != s:
                    good = False
                    break
            if good:
                ok = True
                break
        if not ok:
            return False
    return True


def cnf_unsat(clauses, nvars, off=0):
    """Teste exaustivo: a CNF (lista de clausulas) e insatisfativel?
    off = deslocamento das variaveis locais (var_local = var - off)."""
    for m in range(1 << nvars):
        sat = True
        for c in clauses:
            cok = False
            for l in c:
                var, s = (l >> 1) - off, l & 1
                if ((m >> var) & 1) == s:
                    cok = True
                    break
            if not cok:
                sat = False
                break
        if sat:
            return False
    return True


def not_dnf(clauses):
    """Nao-alpha a partir de C = nao-alpha: termos = clausulas negadas."""
    return [frozenset(compl(l) for l in c) for c in clauses]


def not_cnf(terms):
    """C = nao-alpha a partir de alpha (DNF): clausulas = termos negados."""
    return [frozenset(compl(l) for l in t) for t in terms]


# ---------------------------------------------------------------------------
# Construtor de refutacoes por saturacao (resolucao pura; sem enfraquecimento).
# devolve (linhas, refs) onde refs[i] = ("ax",) ou ("res", j, k) e
# linhas[-1] == frozenset() (clausula vazia).
# ---------------------------------------------------------------------------


def build_refutation(clauses, budget=40000):
    seen = {}
    order = []
    refs = []
    for c in clauses:
        if is_taut_clause(c):
            continue
        if c not in seen:
            seen[c] = len(order)
            order.append(c)
            refs.append(("ax",))
            if c == frozenset():
                return order, refs
    changed = True
    while changed:
        changed = False
        cur = list(order)
        for i in range(len(cur)):
            for j in range(i + 1, len(cur)):
                a, b = cur[i], cur[j]
                for l in list(a):
                    if compl(l) in b:
                        r = (a - {l}) | (b - {compl(l)})
                        if is_taut_clause(r):
                            continue
                        if r not in seen:
                            seen[r] = len(order)
                            order.append(r)
                            refs.append(("res", seen[a], seen[b]))
                            if r == frozenset():
                                return order, refs
                            changed = True
                            if len(order) > budget:
                                return None, None
    return None, None


# ---------------------------------------------------------------------------
# Algoritmo de projecao (Teorema C.1): recorte + pureza.
# ---------------------------------------------------------------------------


def resolved_literal(orig_j, orig_k):
    """Literal l em orig_j com ~l em orig_k (literal resolvido no passo)."""
    for l in orig_j:
        if compl(l) in orig_k:
            return l
    return None


def trimming(order, refs):
    """
    Elimina enfraquecimentos mantendo uma derivacao valida da clausula vazia
    (Lema de recorte, Sec. 4.1 do documento).  trim[i] e uma clausula
    derivavel por resolucao pura (sem enfraquecimento) tal que trim[i] esta
    CONTIDA em order[i].  Devolve (trim, trefs) com
    trefs[i] = ("ax",) | ("same", j) | ("res", j, k), onde:
      ("ax",)    : trim[i] = order[i] e axioma (clausula de entrada);
      ("same", j): trim[i] = trim[j] (copia; nenhuma inferencia);
      ("res",j,k): trim[i] = resolucao de trim[j] e trim[k] em um literal.
    Regras: folhas => elas mesmas; enfraquecimento C->C u D => trim = trim(C);
    resolucao de linhas originais A, B (A contem l, B contem ~l) =>
      * se l em trim(A) e ~l em trim(B): resolve de fato;
      * se l nao esta em trim(A): herda trim(A)  (trim(A) subset de A\\{l});
      * caso contrario: herda trim(B)          (trim(B) subset de B\\{~l}).
    Invariante: trim[i] subset de order[i] e trim[i] e derivavel.
    """
    trim = [None] * len(order)
    trefs = [None] * len(order)
    for i, c in enumerate(order):
        kind = refs[i]
        if kind[0] == "ax":
            trim[i] = c
            trefs[i] = ("ax",)
        elif kind[0] in ("weaken", "same"):
            j = kind[1]
            trim[i] = trim[j]
            trefs[i] = ("same", j)
        else:  # ("res", j, k) no nivel ORIGINAL: linhas j e k com l, ~l
            j, k = kind[1], kind[2]
            lit = resolved_literal(order[j], order[k])
            assert lit is not None
            a, b = trim[j], trim[k]
            if lit in a and compl(lit) in b:
                trim[i] = (a - {lit}) | (b - {compl(lit)})
                trefs[i] = ("res", j, k)
            elif lit not in a:
                trim[i] = a            # a subset de A\\{l} subset de resolvente
                trefs[i] = ("same", j)
            else:
                trim[i] = b            # b subset de B\\{~l} subset de resolvente
                trefs[i] = ("same", k)
        assert trim[i] is not None and trim[i] <= c, "invariante violada"
    return trim, trefs


def reachable(root, trefs):
    """Conjunto de indices necessarios para justificar a linha `root`."""
    stack = [root]
    keep = set()
    while stack:
        i = stack.pop()
        if i in keep:
            continue
        keep.add(i)
        kind = trefs[i]
        if kind[0] == "res":
            stack.append(kind[1])
            stack.append(kind[2])
        elif kind[0] == "same":
            stack.append(kind[1])
        # ("ax",): folha, nada a fazer
    return sorted(keep)


def verify_sub_refutation(sub, lam_i):
    """
    Verifica que sub = [(idx, trim, tref), ...] e uma refutacao POR RESOLUCAO
    valida (sem enfraquecimento) de alguma CNF, a partir de lam_i: toda folha
    pertence a lam_i, todos os passos de resolucao sao validos, e a ultima
    linha e o vazio.  Devolve True/False.
    """
    derived = set()
    for pos, (idx, cl, tr) in enumerate(sub):
        if tr[0] == "ax":
            if cl not in lam_i:
                return False
        elif tr[0] == "same":
            if tr[1] not in derived:
                return False
            if cl != sub[[i2 for i2, _, _ in sub].index(tr[1])][1]:
                return False
        elif tr[0] == "res":
            j, k = tr[1], tr[2]
            cj = [c for i2, c, _ in sub if i2 == j]
            ck = [c for i2, c, _ in sub if i2 == k]
            if not cj or not ck:
                return False
            lit = resolved_literal(cj[0], ck[0])
            if lit is None:
                return False
            if cl != (cj[0] - {lit}) | (ck[0] - {compl(lit)}):
                return False
        derived.add(idx)
        if pos == len(sub) - 1 and cl != frozenset():
            return False
    return True


def project_dd(order, refs, x_ranges, lam, lam_sides):
    """
    Entrada: derivacao (possivelmente com enfraquecimentos) da clausula vazia a
    partir de Lambda = C_1 u ... u C_m (clausulas puras por lado, lados dados
    por x_ranges = [(lo_i, hi_i)]; lam_sides[i] e o lado de lam[i]).
    Saida: (i_star, sub) com C_{i_star} insatisfativel e sub uma refutacao
    pura de C_{i_star} por resolucao pura, de tamanho <= |derivacao|.
    (Teorema C.1: recorte + lema da pureza.)
    """
    trim, trefs = trimming(order, refs)
    n = len(trim)
    last = trefs[-1]
    if last[0] == "ax":
        # clausula vazia e axioma de entrada: devolve o lado daquele axioma
        for i in range(n):
            if trim[i] == frozenset() and trefs[i][0] == "ax":
                s = lam_sides[lam.index(order[i])]
                return s, [(i, trim[i], trefs[i])]
        raise AssertionError("vazio axiomático sem lado")
    j, k = last[1], last[2]
    sj = side_of(trim[j], x_ranges)
    sk = side_of(trim[k], x_ranges)
    assert sj is not None and sj == sk, "pureza violada no ultimo passo"
    i_star = sj
    keep = reachable(n - 1, trefs)
    sub = [(i, trim[i], trefs[i]) for i in keep]
    # pureza: toda linha alcancavel e pura (lema da pureza aplicado a
    # derivacao recortada, que e livre de enfraquecimento)
    for i, cl, _ in sub:
        assert side_of(cl, x_ranges) in (i_star, None), "linha impura"
    assert sub[-1][1] == frozenset(), "subderivacao nao deriva o vazio"
    lam_i = [c for c in lam if side_of(c, x_ranges) == i_star]
    assert verify_sub_refutation(sub, lam_i), "subderivacao invalida"
    return i_star, sub


def side_of(cl, x_ranges):
    """Lado de uma clausula: i se todas as variaveis estao em X_i; senao None."""
    vs = clause_vars(cl)
    if not vs:
        return None  # vazio: "puro" para qualquer lado
    for i, (lo, hi) in enumerate(x_ranges):
        if vs <= set(range(lo, hi)):
            return i
    return None


def sides_of_all(order, x_ranges):
    out = []
    for c in order:
        s = side_of(c, x_ranges)
        out.append(s if s is not None else -1)
    return out


# ---------------------------------------------------------------------------
# Geracao aleatoria de instancias.
# ---------------------------------------------------------------------------


def random_side_clauses(rng, lo, hi, max_clauses=4, max_width=2):
    """CNF aleatoria sobre as variaveis [lo,hi)."""
    nvars = hi - lo
    lits = []
    for v in range(lo, hi):
        lits.append(2 * v)
        lits.append(2 * v + 1)
    cls = []
    for _ in range(rng.randint(1, max_clauses)):
        w = rng.randint(1, max_width)
        c = frozenset(rng.sample(lits, min(w, len(lits))))
        if is_taut_clause(c):
            continue
        cls.append(c)
    return list(dict.fromkeys(cls))


def random_instance(rng, one_taut=True):
    """
    Gera C_1 (sobre X_1) e C_2 (sobre X_2) disjuntos.
    Se one_taut: exatamente um lado e insatisfativel (caso interessante de DD).
    """
    while True:
        n1 = rng.randint(2, 3)
        n2 = rng.randint(2, 3)
        c1 = random_side_clauses(rng, 0, n1)
        c2 = random_side_clauses(rng, n1, n1 + n2)
        if not c1 or not c2:
            continue
        u1 = cnf_unsat(c1, n1, 0)
        u2 = cnf_unsat(c2, n2, n1)
        if one_taut and (u1 == u2):
            continue
        if not one_taut and (not u1 and not u2):
            continue
        return c1, c2, (n1, n2), (u1, u2)


# ---------------------------------------------------------------------------
# Heuristicas ingenuas (usam apenas os alfas, nao a prova).
# ---------------------------------------------------------------------------

HEURISTICS = {
    "maior_em_literais":
        lambda a1, a2: 0 if sum(len(t) for t in a1) >= sum(len(t) for t in a2) else 1,
    "mais_termos":
        lambda a1, a2: 0 if len(a1) >= len(a2) else 1,
    "mais_termos_unitarios":
        lambda a1, a2:
            0 if sum(1 for t in a1 if len(t) == 1) >= sum(1 for t in a2 if len(t) == 1) else 1,
    "termo_maior":
        lambda a1, a2: 0 if max(len(t) for t in a1) >= max(len(t) for t in a2) else 1,
    "sempre_o_primeiro":
        lambda a1, a2: 0,
}


def run_random_experiments(trials=3000, seed=20261010):
    rng = random.Random(seed)
    stats = {h: {"ok": 0, "fail": 0} for h in HEURISTICS}
    stats["projecao"] = {"ok": 0, "fail": 0}
    provas = []
    min_counter = {h: None for h in HEURISTICS}
    n_instances = 0
    taut_side_count = {0: 0, 1: 0}

    for _ in range(trials):
        c1, c2, (n1, n2), (u1, u2) = random_instance(rng, one_taut=True)
        lam = c1 + c2
        order, refs = build_refutation(lam)
        if order is None:
            continue  # saturacao estourou o orcamento (raro nos parametros)
        n_instances += 1
        x_ranges = [(0, n1), (n1, n1 + n2)]

        # alfas em DNF
        alpha1, alpha2 = not_dnf(c1), not_dnf(c2)
        truth = [dnf_tautology(alpha1, n1, 0), dnf_tautology(alpha2, n2, n1)]
        assert truth[0] != truth[1], "instancia deveria ter exatamente um tautologo"
        taut_side = truth.index(True)
        taut_side_count[taut_side] += 1

        # (2) algoritmo de projecao (ja verifica internamente a sub-refutacao)
        i_star, sub = project_dd(order, refs, x_ranges, lam,
                                 [0] * len(c1) + [1] * len(c2))
        # conferir: lado devolvido e realmente o tautologo?
        cs = [c1, c2][i_star]
        ns = [n1, n2][i_star]
        if cnf_unsat(cs, ns, 0 if i_star == 0 else n1) and len(sub) <= len(order):
            stats["projecao"]["ok"] += 1
        else:
            stats["projecao"]["fail"] += 1

        # (3) heuristicas
        total_lits = sum(len(t) for t in alpha1) + sum(len(t) for t in alpha2)
        for h, f in HEURISTICS.items():
            guess = f(alpha1, alpha2)
            if guess == taut_side:
                stats[h]["ok"] += 1
            else:
                stats[h]["fail"] += 1
                key = (total_lits, c1, c2)
                if min_counter[h] is None or key < min_counter[h][0]:
                    min_counter[h] = (key, (c1, c2, n1, n2, taut_side))

        provas.append((len(order), len([c1, c2][taut_side])))

    return n_instances, stats, min_counter, provas, taut_side_count


# ---------------------------------------------------------------------------
# Enumeracao exaustiva de contra-exemplos minimos (2 variaveis por lado).
# ---------------------------------------------------------------------------


def all_clauses(vars_):
    lits = []
    for v in vars_:
        lits.append(2 * v)
        lits.append(2 * v + 1)
    out = []
    for w in (1, 2):
        for comb in itertools.combinations(lits, w):
            c = frozenset(comb)
            if not is_taut_clause(c):
                out.append(c)
    return out


def exhaustive_minimal_counterexamples():
    """
    Enumera CNFs C_1 (2 vars, ate 3 clausulas) e C_2 (2 vars, ate 3 clausulas),
    com C_1 insatisfativel e C_2 satisfativel, e procura o menor contra-exemplo
    (por numero total de literais nos dois alfas) para cada heuristica.
    """
    cls = all_clauses([0, 1])
    cnfs = []
    for w in (1, 2, 3):
        for comb in itertools.combinations(cls, w):
            cnfs.append(list(comb))
    results = {}
    for h in HEURISTICS:
        best = None
        for c1 in cnfs:
            if not cnf_unsat(c1, 2):
                continue
            for c2 in cnfs:
                if cnf_unsat(c2, 2):
                    continue
                a1, a2 = not_dnf(c1), not_dnf(c2)
                if dnf_tautology(a1, 2) and not dnf_tautology(a2, 2):
                    if HEURISTICS[h](a1, a2) == 1:  # errou: tautologo e o lado 0
                        total = sum(len(t) for t in a1) + sum(len(t) for t in a2)
                        cand = (total, c1, c2)
                        if best is None or cand < best:
                            best = cand
        results[h] = best
    # variante com 3 variaveis de um lado para "mais_termos_unitarios"
    cls3 = all_clauses([2, 3, 4])
    cnfs3 = []
    for w in (1, 2, 3):
        for comb in itertools.combinations(cls3, w):
            cnfs3.append(list(comb))
    best = None
    for c1 in cnfs:
        if not cnf_unsat(c1, 2):
            continue
        for c2 in cnfs3:
            if cnf_unsat(c2, 3, 2):
                continue
            a1, a2 = not_dnf(c1), not_dnf(c2)
            if dnf_tautology(a1, 2) and not dnf_tautology(a2, 3, 2):
                if HEURISTICS["mais_termos_unitarios"](a1, a2) == 1:
                    total = sum(len(t) for t in a1) + sum(len(t) for t in a2)
                    cand = (total, c1, c2)
                    if best is None or cand < best:
                        best = cand
    results["mais_termos_unitarios (lado 2 com 3 vars)"] = best
    return results


# ---------------------------------------------------------------------------
# Testes de unidade.
# ---------------------------------------------------------------------------


def unit_tests():
    print("=" * 74)
    print("TESTES DE UNIDADE")
    print("=" * 74)

    # T1: refutacao pura minima. C1 = { {x}, {¬x} } (insat.), C2 = { {y} } (sat.)
    x, y = 0, 1
    c1 = [frozenset([2 * x]), frozenset([2 * x + 1])]
    c2 = [frozenset([2 * y])]
    order, refs = build_refutation(c1 + c2)
    i_star, sub = project_dd(order, refs, [(0, 1), (1, 2)], c1 + c2,
                             [0, 0, 1])
    print("T1 (refutacao pura): |pi| = %d -> lado devolvido = %d (esperado 0),"
          " sub-refutacao de tamanho %d"
          % (len(order), i_star, len(sub)))
    assert i_star == 0

    # T2: refutacao MISTURADA com enfraquecimento, ultimo passo com pais de
    # lados "rotulados" diferentes. Linhas:
    #   0: {x}        (axioma, lado 0)
    #   1: {¬x}       (axioma, lado 0)
    #   2: {y}        (axioma, lado 1)
    #   3: {y, ¬x}    (enfraquecimento de 2, rotulo 'lado 1')
    #   4: {¬x, ¬y}   (enfraquecimento de 1, rotulo 'lado 0')
    #   5: {¬x}       (resolucao de 3 e 4 em y; pai de rotulos 1 e 0)
    #   6: {}         (resolucao de 0 e 5 em x)
    order2 = [frozenset([2 * x]), frozenset([2 * x + 1]), frozenset([2 * y]),
              frozenset([2 * y, 2 * x + 1]), frozenset([2 * x + 1, 2 * y + 1]),
              frozenset([2 * x + 1]), frozenset()]
    refs2 = [("ax",), ("ax",), ("ax",),
             ("weaken", 2), ("weaken", 1), ("res", 3, 4), ("res", 0, 5)]
    # rotulagem ingenua "origem" (enfraquecimento herda; resolucao herda o
    # primeiro pai): usada apenas para ILUSTRAR que ela pode falhar
    origin = [0, 0, 1, 1, 0, 1, None]   # rotulos calculados a mao acima
    print("T2 (refutacao misturada): rotulagem ingenua de origem: linha 5"
          " ('{~x}') recebe rotulo %d (lado 1), mas os pais do ultimo passo"
          " (linhas 0 e 5) ficam com rotulos %d e %d -> rotulagem AMBIGUA"
          % (origin[5], origin[0], origin[5]))
    i_star2, sub2 = project_dd(order2, refs2, [(0, 1), (1, 2)],
                               order2[:3], [0, 0, 1])  # Lambda = {x} u {~x} u {y}
    trim_len = len(sub2)
    print("T2: algoritmo de projecao devolve lado %d (esperado 0) com"
          " sub-refutacao pura (sem enfraquecimento) de tamanho %d"
          " (|pi| = %d)" % (i_star2, trim_len, len(order2)))
    assert i_star2 == 0 and trim_len <= len(order2)

    # T3: extensao D_P (atomos p compartilhados + restricao).
    # beta_1(p,q1) = p | q1 ; beta_2(p,q2) = ~p | q2 (disjuncao TAUTOLOGIA,
    # como exige pi : Res |- beta_1 | beta_2; atoms q1, q2 disjuntos, p comum).
    # Atribuicao a com a(p) = 1: beta_1(a,q1) = 1 (tautologia),
    # beta_2(a,q2) = q2 (NAO-tautologia). Logo DD deve devolver o lado 0.
    # nao-beta_1 = ~p /\ ~q1 ; nao-beta_2 = p /\ ~q2.
    # pi: refutacao de {~p},{~q1},{p},{~q2}. Restringe-se pi por a(p)=1
    # (a clausula {~p} reduz-se ao vazio; a clausula {p} e apagada) e aplica-se
    # o algoritmo de projecao ao conjunto restrito (Corolario C.2).
    p, q1, q2 = 0, 1, 2            # p compartilhado; q1 do lado 1; q2 do lado 2
    a_p = 1
    nb1 = [frozenset([2 * p + 1]), frozenset([2 * q1 + 1])]   # {~p}, {~q1}
    nb2 = [frozenset([2 * p]), frozenset([2 * q2 + 1])]       # {p}, {~q2}
    order3, refs3 = build_refutation(nb1 + nb2)
    assert order3 is not None, "pi deveria provar beta_1 | beta_2 (tautologia)"

    def restrict(clauses, assign):
        # clausula contendo literal VERDADEIRO sob `assign` e apagada;
        # literais FALSIFICADOS sao removidos.
        out = []
        for c in clauses:
            if any(((l >> 1) in assign) and ((l & 1) != assign[l >> 1]) for l in c):
                continue
            out.append(frozenset(l for l in c
                                 if not ((l >> 1) in assign)))
        return out
    r1, r2 = restrict(nb1, {p: a_p}), restrict(nb2, {p: a_p})
    # r1 = { {}, {~q1} } (o vazio prova que beta_1(a,q1) e tautologia);
    # r2 = { {~q2} }
    order4, refs4 = build_refutation(r1 + r2)
    assert order4 is not None
    i_star4, sub4 = project_dd(order4, refs4, [(q1, q1 + 1), (q2, q2 + 1)],
                               r1 + r2, [0] * len(r1) + [1] * len(r2))
    print("T3 (D_P com restricao): a(p)=%d, |pi| = %d -> lado devolvido = %d"
          " (esperado 0: beta_1(a,q1) e tautologia)" % (a_p, len(order3), i_star4))
    assert i_star4 == 0
    print("Todos os testes de unidade passaram.")


# ---------------------------------------------------------------------------
# Programa principal.
# ---------------------------------------------------------------------------


def fmt_clause(c):
    def fl(l):
        return ("~" if (l & 1) else "") + "x%d" % (l >> 1)
    return "{" + ",".join(sorted(fl(l) for l in c)) + "}"


def fmt_cnf(cs):
    return " /\\ ".join(fmt_clause(c) for c in cs)


def main():
    unit_tests()
    print()
    print("=" * 74)
    print("EXPERIMENTOS ALEATORIOS")
    print("=" * 74)
    n, stats, min_counter, provas, tsc = run_random_experiments(trials=3000)
    print("Instancias geradas com refutacao encontrada: %d" % n)
    print("Distribuicao do lado tautologo (simetria do gerador): "
          "lado 0 = %d, lado 1 = %d" % (tsc[0], tsc[1]))
    tot = stats["projecao"]["ok"] + stats["projecao"]["fail"]
    print("Algoritmo de projecao (Teorema C.1): %d/%d corretos (%.1f%%)"
          % (stats["projecao"]["ok"], tot,
             100.0 * stats["projecao"]["ok"] / max(tot, 1)))
    print()
    print("Taxas de falha das heuristicas ingenuas (apenas instancias com")
    print("exatamente um disjunto tautologo):")
    for h in HEURISTICS:
        s = stats[h]
        t = s["ok"] + s["fail"]
        print("  %-28s falha em %4d/%4d = %5.1f%%"
              % (h, s["fail"], t, 100.0 * s["fail"] / max(t, 1)))
    print()
    if provas:
        avg_p = sum(p for p, _ in provas) / len(provas)
        avg_side = sum(q for _, q in provas) / len(provas)
        mx = max(p for p, _ in provas)
        print("Tamanhos de refutacao: media |pi| = %.1f, max = %d; "
              "refutacao minima de um lado: media = %.1f"
              % (avg_p, mx, avg_side))
    print()
    print("Contra-exemplos minimos encontrados (menor numero total de literais):")
    for h in HEURISTICS:
        mc = min_counter[h]
        if mc is None:
            print("  %-28s: nenhum" % h)
        else:
            (total, _c1k, _c2k), (c1, c2, n1, n2, taut) = mc
            print("  %-28s: |alpha_1|+|alpha_2| = %d literais; tautologo = lado %d"
                  % (h, total, taut))
            print("      C_1 (lado 0, taut=%s): %s   [vars x0..x%d]"
                  % (taut == 0, fmt_cnf(c1), n1 - 1))
            print("      C_2 (lado 1, taut=%s): %s   [vars x%d..x%d]"
                  % (taut == 1, fmt_cnf(c2), n1, n1 + n2 - 1))
    print()
    print("=" * 74)
    print("ENUMERACAO EXAUSTIVA (lados com 2 variaveis, CNFs com ate 3 clausulas)")
    print("(os dois lados sao enumerados de forma independente; na exibicao as")
    print(" variaveis do lado 2 aparecem renomeadas como x0,x1 / x2,x3,x4)")
    print("=" * 74)
    ex = exhaustive_minimal_counterexamples()
    for h, best in ex.items():
        if best is None:
            print("  %-38s: nenhum contra-exemplo" % h)
        else:
            total, c1, c2 = best
            print("  %-38s: contra-exemplo minimo com %d literais no total"
                  % (h, total))
            print("       C_1 = %s (insatisfativel)" % fmt_cnf(c1))
            print("       C_2 = %s (satisfativel)" % fmt_cnf(c2))
    print()
    print("Observacao honesta: as heuristicas acima usam apenas os alfas.")
    print("O algoritmo de projecao usa a PROVA (a estrutura da refutacao) e,")
    print("pelo Teorema C.1, nunca falha. Heuristica nao e algoritmo.")


if __name__ == "__main__":
    main()

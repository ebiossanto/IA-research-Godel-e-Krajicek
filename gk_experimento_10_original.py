"""
EXPERIMENTO 10 — Instâncias finitas dos geradores g_T^{a,b}
Simulacao estruturalmente fiel de:
  - T0 = PA (obrigacoes com complexidade de prova finita ou infinita)
  - T1 = PA + RFN_{Pi1}(PA) ( Con(T0) torna-se provavel )
  - deficit delta_T(Phi, b)
  - Reflection Branch Transition (RBT)
  - busca por candidatos R (PPR-2)

Nao faz busca real de provas em PA; usa valores de complexidade de prova
que reproduzem a estrutura matematica (Godel 2: Con(PA) = infinito em PA).
"""

from itertools import product

# ---------------------------------------------------------------------------
# 1. CODIFICACAO FIXA
# ---------------------------------------------------------------------------
# Formula Phi: "Con(PA) essentially" via padding
# |Phi| = bits do prefixo fixo
PHI_STR = "PA_CON_ENCODING"  # representacao textual; comprimento em bits abaixo
PHI_LEN_BITS = 12            # a(n) precisa ser >= isto para Phi ser escolhida

# w* : o prefixo binario fixo que codifica a obrigacao Con(T)
# Todos os elementos de A_Phi comecam com w*
W_STAR = "00"                # |w*| = 2; logo r = |Phi|+1 mas para W usamos r_w = 4 p/ exemplo
# Para o experimento: usamos r_w = 4 (palavras w de 4 bits) — suficiente p/ demonstrar mecanismo
R_W = 4

# ---------------------------------------------------------------------------
# 2. ESTRUTURA DE OBRIGACOES (Phi^w)
# ---------------------------------------------------------------------------
# Cada w em {0,1}^r define uma obrigacao Phi^w.
# Na construcao de 09: Phi^w = "finitos elementos de A_Phi comecam com w"
# Sob a codificacao com Con(T): se T inconsistente, infinitos x com prefixo w*;
# se consistente, A_Phi vazio -> todos Phi^w verdadeiros.

# Para o experimento FINITO assumimos T0 consistente (metamathematicamente):
# Logo TODOS os Phi^w sao verdadeiros em N.  W^true = {0,1}^r.

def all_words(r):
    return [''.join(p) for p in product('01', repeat=r)]

W_TRUE = all_words(R_W)  # todos verdadeiros (T0 consistente)

# ---------------------------------------------------------------------------
# 3. COMPLEXIDADE DE PROVA POR OBRIGACAO (em T0 e T1)
# ---------------------------------------------------------------------------
# s_T(Phi^w) = comprimento da menor prova de Phi^w em T, ou INF se indecidivel/nao-provavel
INF = float('inf')

# Em T0 = PA:
#   - obrigacoes "genericas" Phi^w (w != w*): provaveis em PA com prova razoavel
#     (ex.: consequencias triviais da consistencia + padding)
#   - obrigacao Con(T) associada a w*: NAO provavel em PA (Godel 2) -> s = INF
#
# Em T1 = PA + RFN_{Pi1}(PA):
#   - todas as obrigacoes verdadeiras provaveis; Con(T) prova-se com prova
#     que usa o axioma de reflexao -> prova um pouco mais longa mas finita

def proof_complexity_T0(w, r=R_W, w_star=W_STAR):
    """Comprimento minimo de prova de Phi^w em T0=PA."""
    # Obrigacao Con(T) (prefixo w*): nao provavel em PA
    if w.startswith(w_star):
        # Para w que "capturam" a obrigacao Con: nao provaveis
        # Apenas w* exato (ou os w que sao extensao minima) representam Con
        # Simplificacao: apenas w == w* + padding irrelevante -> nao provavel
        # Usamos: w que COMECA com w* e tem exatamente o resto "livre" ainda
        # Sao obrigações sobre A_Phi: se w* cobre todos os x, Phi^w* = Con
        # Para w comecando com w* mas maiores: tambem herdam indecidibilidade
        # nos cenarios tipicos; aqui marcamos so w* exato como INF p/ clareza
        if w == w_star + '0' * (r - len(w_star)) or w.startswith(w_star):
            # Todos os w comecando com w* tem status de Con (nao provavel em T0)
            # EXCETO se w e' tao especifico que trivializa — mantemos INF p/ mecanismo
            return INF
    # Obrigacoes genericas: provaveis em PA
    # Deterministico e reprodutivel: comprimento = hash simples + constante
    h = sum(ord(c) for c in w)
    return 8 + (h % 17)  # valores entre 8 e 24

def proof_complexity_T1(w, r=R_W, w_star=W_STAR):
    """Comprimento minimo de prova de Phi^w em T1=PA+RFN."""
    if w.startswith(w_star):
        # Con(T) provavel em T1 via reflexao: prova finita
        # Usamos valor fixo B' = 20 (usa axioma de reflexao)
        return 20
    # Genericas: mesma prova que em T0 (T1 estende T0)
    return proof_complexity_T0(w, r, w_star)

# ---------------------------------------------------------------------------
# 4. DELTA, COBERTURA, GANHO
# ---------------------------------------------------------------------------

def coverage(T_complex_fn, b):
    """Conjunto de w cobertos (s_T <= b)."""
    return {w for w in W_TRUE if T_complex_fn(w) <= b}

def delta(T_complex_fn, b):
    """delta_T(Phi, b) = |W^true| - |Cov_T|."""
    return len(W_TRUE) - len(coverage(T_complex_fn, b))

def gain(b, r=R_W, w_star=W_STAR):
    """G = delta_T0 - delta_T1 >= 0."""
    d0 = delta(lambda w: proof_complexity_T0(w, r, w_star), b)
    d1 = delta(lambda w: proof_complexity_T1(w, r, w_star), b)
    return d0, d1, d0 - d1

def first_uncovered(T_complex_fn, b):
    """Primeiro w nao coberto em ordem lex (ou None se todos cobertos)."""
    for w in sorted(W_TRUE):
        if T_complex_fn(w) > b:
            return w
    return None  # todos cobertos -> ramo "all-covered" = 0^{...}

# ---------------------------------------------------------------------------
# 5. GERADOR g_T^{a,b} (mecanismo)
# ---------------------------------------------------------------------------

def generator(T_complex_fn, u, a, b, phi_len=PHI_LEN_BITS):
    """
    Mecanismo de 09 §4:
      - u com |u|=n
      - Phi = prefixo de u de tamanho <= a(n) (aqui: se n>=phi_len e prefixo valido)
      - W = {0,1}^r com r = phi_len+1 ? — usamos R_W para palavras
      -saida = w0 . u0 ou 0^{n+1}
    Simplificacao: assumimos Phi sempre presente se n >= phi_len.
    """
    n = len(u)
    # Passo A: descricao
    if n < phi_len or phi_len > a(n):
        return '0' * (n + 1)
    # Assume prefixo = u[:phi_len] e' o codigo de Phi (para u que comecam com PHI bits)
    # No experimento: so entradas da forma Phi . u0
    phi = u[:phi_len]
    u0 = u[phi_len:]
    # Passo E: selecao
    w0 = first_uncovered(T_complex_fn, b)
    if w0 is None:
        return '0' * (n + 1)
    # Normalizacao 09 §3: |w0| = r = R_W (aqui fixo p/ experimento)
    # Nota: na teoria r = |Phi|+1; aqui usamos R_W como proxy da familia W
    return w0 + u0

# ---------------------------------------------------------------------------
# 6. RBT — Reflection Branch Transition
# ---------------------------------------------------------------------------

def check_RBT(b, r=R_W, w_star=W_STAR):
    """
    RBT ocorre se o primeiro ramo nao coberto muda de T0 para T1,
    ou se T1 cobre todos (ramo all-covered) enquanto T0 nao.
    """
    f0 = first_uncovered(lambda w: proof_complexity_T0(w, r, w_star), b)
    f1 = first_uncovered(lambda w: proof_complexity_T1(w, r, w_star), b)
    rbt = (f0 != f1)
    return f0, f1, rbt

# ---------------------------------------------------------------------------
# 7. BUSCA POR CANDIDATO R (PPR-2 simplificado)
# ---------------------------------------------------------------------------
# PPR-2: b notin rng(g0)  =>  R(n,b) notin rng(g1)
# Para o experimento finito: enumeramos b fora da imagem e testamos R simples.

def image(T_complex_fn, n, a, phi_len=PHI_LEN_BITS):
    """Enumerar g_T(u) para u = Phi . u0 com |u|=n."""
    if n < phi_len:
        return set()
    u0_len = n - phi_len
    img = set()
    for bits in product('01', repeat=u0_len):
        u = 'PA_CONENCOD'[:phi_len].ljust(phi_len, '0') + ''.join(bits)  # prefixo fixo
        # Correcao: usar PHI real
        u = PHI_STR[:phi_len].ljust(phi_len, '0') + ''.join(bits)
        out = generator(T_complex_fn, u, a, b=64)  # b fixo p/ imagem
        img.add(out)
    return img

def complement(img, n):
    """{0,1}^{n+1} menos img"""
    all_out = {''.join(p) for p in product('01', repeat=n+1)}
    return all_out - img

def test_R_candidates(n_values=(8, 10, 12, 14, 16), b_test=32):
    """
    Testa R simples: identidade, extensao de prefixo, XOR const.
    PPR-2: se b fora de rng(g0) entao R(b) fora de rng(g1).
    """
    candidates = []
    results = []
    for n in n_values:
        if n < PHI_LEN_BITS:
            continue
        a = lambda x: max(PHI_LEN_BITS, min(x, 16))
        # Imagens (com b fixo alto p/ determinismo do gerador)
        def gen0(u): return generator(lambda w: proof_complexity_T0(w), u, a, b_test)
        def gen1(u): return generator(lambda w: proof_complexity_T1(w), u, a, b_test)
        # Enumerar entradas
        img0, img1 = set(), set()
        u0_len = n - PHI_LEN_BITS
        phi_prefix = PHI_STR[:PHI_LEN_BITS].ljust(PHI_LEN_BITS, '0')
        for bits in product('01', repeat=u0_len):
            u = phi_prefix + ''.join(bits)
            img0.add(gen0(u))
            img1.add(gen1(u))
        comp0 = {''.join(p) for p in product('01', repeat=n+1)} - img0
        # Testar R: extensao de prefixo 0, XOR 0, XOR 1...
        for R_name, R_fn in [
            ("id", lambda s: s),
            ("xor1", lambda s: ''.join('1' if c=='0' else '0' for c in s)),
            ("prefix0", lambda s: '0' + s[:n]),  # ajusta tamanho
            ("suffix0", lambda s: s + '0'),
        ]:
            ok = True
            for b_out in comp0:
                # PPR-2: b fora img0 => R(b) fora img1
                r_out = R_fn(b_out)
                if r_out in img1:
                    ok = False
                    break
            status = "CANDIDATE" if ok else "refuted"
            results.append((n, R_name, status, len(comp0)))
            if ok:
                candidates.append((n, R_name))
    return results, candidates

# ---------------------------------------------------------------------------
# 8. EXECUCAO PRINCIPAL — preencher tabelas §4
# ---------------------------------------------------------------------------

def main():
    print("=" * 78)
    print("EXPERIMENTO 10 — Instancias finitas g_T^{a,b}")
    print("T0=PA, T1=PA+RFN_{Pi1}(PA)  |  |Phi|=", PHI_LEN_BITS, " bits, r=|w|=", R_W)
    print("W^true = {0,1}^", R_W, " (T0 consistente => todos verdadeiros)")
    print("=" * 78)

    # --- Tabela 4.1: delta e ganho ---
    print("\n--- Tabela 4.1: deficit delta e ganho G ---")
    print(f"{'n':>4} {'b':>4} {'|Wtrue|':>8} {'d_T0':>6} {'d_T1':>6} {'G=d0-d1':>8} {'w0(T0)':>8} {'w0(T1)':>8}")
    print("-" * 70)

    n_values = [8, 10, 12, 14, 16]
    b_values = [4, 8, 12, 16, 20, 24, 32, 48, 64]

    table_41 = []
    for n in n_values:
        for b in b_values:
            # n < |Phi|: sem Phi escolhida -> todas saidas 0, delta cheio
            if n < PHI_LEN_BITS:
                d0, d1, G = len(W_TRUE), len(W_TRUE), 0
                w0_0 = w0_1 = "0000"
            else:
                d0, d1, G = gain(b)
                w0_0 = first_uncovered(lambda w: proof_complexity_T0(w), b) or "ALL_COV"
                w0_1 = first_uncovered(lambda w: proof_complexity_T1(w), b) or "ALL_COV"
            table_41.append((n, b, len(W_TRUE), d0, d1, G, w0_0, w0_1))
            if n == 12 and b in (4, 8, 16, 20, 24, 32, 64):  # n=12 = |Phi| minimo
                print(f"{n:>4} {b:>4} {len(W_TRUE):>8} {d0:>6} {d1:>6} {G:>8} {w0_0:>8} {w0_1:>8}")
    print(f"[n=12 e' o menor n com Phi valida (|Phi|=12); n<12: delta cheio trivialmente]")

    # Resumo por b (independente de n neste modelo simplificado)
    print("\n--- Resumo delta(b) [modelo: independente de n] ---")
    print(f"{'b':>4} {'d_T0':>6} {'d_T1':>6} {'G':>4} {'RBT?':>6} {'w0_T0':>8} {'w0_T1':>8}")
    print("-" * 55)
    for b in b_values:
        d0, d1, G = gain(b)
        w0, w1, rbt = check_RBT(b)
        w0s = w0 or "ALL"
        w1s = w1 or "ALL"
        print(f"{b:>4} {d0:>6} {d1:>6} {G:>4} {'SIM' if rbt else 'nao':>6} {w0s:>8} {w1s:>8}")

    # --- Tabela 4.2: complemento de imagem ---
    print("\n--- Tabela 4.2: imagens e complemento (b_gen=32) ---")
    print(f"{'n':>4} {'|rng g0|':>10} {'|comp g0|':>10} {'|rng g1|':>10} {'|comp g1|':>10}")
    print("-" * 55)
    for n in [8, 10, 12, 14, 16]:
        if n < PHI_LEN_BITS:
            # Sem entrada valida: todas entradas produzem saida 0^{n+1}
            total = 2 ** (n + 1)
            print(f"{n:>4} {1:>10} {total-1:>10} {1:>10} {total-1:>10}")
            continue
        a = lambda x: max(PHI_LEN_BITS, min(x, 16))
        def gen0(u, n=n): return generator(lambda w: proof_complexity_T0(w), u, a, 32)
        def gen1(u, n=n): return generator(lambda w: proof_complexity_T1(w), u, a, 32)
        img0, img1 = set(), set()
        u0_len = n - PHI_LEN_BITS
        phi_prefix = PHI_STR[:PHI_LEN_BITS].ljust(PHI_LEN_BITS, '0')
        for bits in product('01', repeat=u0_len):
            u = phi_prefix + ''.join(bits)
            img0.add(gen0(u))
            img1.add(gen1(u))
        total = 2 ** (n + 1)
        print(f"{n:>4} {len(img0):>10} {total-len(img0):>10} {len(img1):>10} {total-len(img1):>10}")

    # --- Tabela 4.3: RBT detalhado ---
    print("\n--- Tabela 4.3: RBT (Transicao de Ramo por Reflexao) ---")
    print(f"{'b':>4} {'w0_T0':>8} {'w0_T1':>8} {'RBT':>6} {'Transicao'}")
    print("-" * 60)
    rbt_count = 0
    for b in b_values:
        w0, w1, rbt = check_RBT(b)
        w0s = w0 or "ALL_COV"
        w1s = w1 or "ALL_COV"
        if rbt:
            rbt_count += 1
            trans = f"{w0s} -> {w1s}"
        else:
            trans = "-"
        print(f"{b:>4} {w0s:>8} {w1s:>6} {'SIM' if rbt else 'nao':>6} {trans}")
    print(f"\nRBT ocorre em {rbt_count}/{len(b_values)} valores de b testados.")

    # --- Busca por R ---
    print("\n--- Busca por candidato R (PPR-2 simplificado) ---")
    results, candidates = test_R_candidates()
    print(f"{'n':>4} {'R':>10} {'status':>12} {'|comp g0|':>10}")
    print("-" * 42)
    for n, R_name, status, ncomp in results:
        print(f"{n:>4} {R_name:>10} {status:>12} {ncomp:>10}")
    if candidates:
        print(f"\nCANDIDATOS R (PPR-2 vale nas amostras): {candidates}")
    else:
        print("\nNenhum candidato R simples passou em PPR-2 para as amostras.")

    # --- Verificacoes teoricas rapidas ---
    print("\n--- Verificacoes teoricas ---")
    # G >= 0 sempre
    G_nonneg = all(gain(b)[2] >= 0 for b in b_values)
    print(f"G >= 0 para todo b testado: {G_nonneg}")
    # delta nao-crescente em T0 <= T1 (monotonicidade Teo 2)
    mono = all(delta(lambda w: proof_complexity_T1(w), b) <=
               delta(lambda w: proof_complexity_T0(w), b) for b in b_values)
    print(f"delta_T1 <= delta_T0 (Teo 2): {mono}")
    # delta decrescente em b (para T fixo)
    d0_seq = [delta(lambda w: proof_complexity_T0(w), b) for b in b_values]
    dec = all(d0_seq[i] >= d0_seq[i+1] for i in range(len(d0_seq)-1))
    print(f"delta_T0 nao-crescente em b: {dec}  sequencia={d0_seq}")
    # Teorema 4: existe b* tal que delta_T0=1 e delta_T1=0 (se w* unico INF em T0)
    # No nosso modelo: todos w comecando com w* sao INF em T0
    n_wstar = sum(1 for w in W_TRUE if w.startswith(W_STAR))
    print(f"Obrigacoes com prefixo w*={W_STAR} (nao-provaveis em T0): {n_wstar}")
    # Para b >= 20: T1 cobre tudo; T0 cobre as genericas (max ~24) mas nao w*
    # delta_T0 para b>=24: so w* nao cobertas
    for b in [20, 24, 32, 64]:
        d0, d1, G = gain(b)
        print(f"  b={b}: delta_T0={d0}, delta_T1={d1}, G={G}")

    # --- Veredicto experimento ---
    print("\n" + "=" * 78)
    print("VEREDICTO DO EXPERIMENTO")
    print("=" * 78)
    print(f"1. delta diminui de T0 para T1? {mono} (G>=0 sempre: {G_nonneg})")
    print(f"2. RBT ocorre? {rbt_count > 0} ({rbt_count}/{len(b_values)} valores de b)")
    print(f"3. Candidato R encontrado? {bool(candidates)} {candidates if candidates else ''}")
    print(f"4. delta decresce com b (para T0)? {dec}")
    print(f"5. Teorema 4 (delta_T0=1, delta_T1=0) alcancavel? ", end="")
    # Para b grande o suficiente (>= max provas genericas): delta_T0 = n_wstar (so w*), delta_T1=0
    b_large = 64
    d0, d1, G = gain(b_large)
    print(f"b=64: d0={d0}, d1={d1} -> {'SIM parcial (d0=n_wstar, d1=0)' if d0 == n_wstar and d1 == 0 else 'ver valores'}")
    print("=" * 78)

    return table_41, results, candidates

if __name__ == "__main__":
    main()

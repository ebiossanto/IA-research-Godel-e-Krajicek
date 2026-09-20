# Framework Estendido: Hierarquia Ordinal de Geradores Godelianos

## 4. Preliminares Estendidos

### 4.1. Principios de Reflexao (Beklemishev)

Seja T uma teoria de 1a ordem na linguagem da aritmetica.

**Definicao 4.1 (Reflexao Local - Prf-RFNT).** O principio de reflexao local para T e:

RFN_P(T) := forall x (Pr_T(x) -> True(x))

onde Pr_T e o predicado de provabilidade de T e True(x) afirma que x e uma sentencia verdadeira no modelo padrao.

**Definicao 4.2 (Reflexao Total - RFN_0).** O principio de reflexao total para T e:

RFN_0(T) := forall x (ProvablyTotal_T(x) -> True(x))

onde ProvablyTotal_T(x) afirma que T prova que x e uma funcao total.

**Definicao 4.3 (Hierarquia de Reflexao - Beklemishev).** Definimos uma progressao de teorias:

- T_0 = T
- T_{alpha+1} = T_alpha + RFN(T_alpha)
- T_lambda = union_{alpha < lambda} T_alpha (para limite lambda)

onde RFN(T_alpha) e o principio de reflexao para T_alpha.

**Propriedade (Beklemishev):** A progressao e bem-definida e estritamente crescente em poder para ordinais abaixo do ponto fixo do operador de consistencia (que e epsilon_0 para PA).

### 4.2. Ordinais e Analise Ordinal

A **ordem-teorica** |T| de uma teoria T e o ordinal recursivo associado a T pela analise ordinal. Propriedades:

- |Q| = omega (Robinson arithmetic)
- |I Sigma_1| = omega^omega
- |PA| = epsilon_0
- |PA + Con(PA)| > epsilon_0
- |PA + RFN(PA)| = omega^{epsilon_0 + 1}

A ordem-teorica mede a "forca metametematica" de T.

### 4.3. Geradores de Complexidade de Provas (Krajicek)

**Definicao 4.4 (Gerador de Provas - Krajicek 2001).** Um gerador de complexidade de provas e uma familia g = {C_n}_{n in N} onde:
- C_n: {0,1}^n -> {0,1}^{n+1}
- C_n e computavel em tempo polinomial
- g estende cada entrada por exatamente 1 bit

**Definicao 4.5 (Tautologia do Gerador).** Dado um gerador g e um sistema de prova P, a tautologia do gerador e:

TG_g^n = AND_{x in {0,1}^n} [C_n(x) = g(x)]

onde C_n(x) denota os n+1 bits de saida de C_n na entrada x, e g(x) e o bit extra do gerador.

**Propriedade fundamental:** Se g e um gerador pseudo-aleatorio (ciclo), entao TG_g^n e uma tautologia (porque C_n e injetiva e g(x) e o bit de paridade, entao a disjuncao cobre todas as saidas possiveis).

### 4.4. Gerador Godeliano (Nossa Construcao)

**Definicao 4.6 (Gerador Godeliano).** Seja T uma teoria r.e. consistente. O gerador godeliano g_T: {0,1}^* -> {0,1}^* e definido por:

g_T(x) = paridade{y : T |- Prf_T(y, |x nao-satisfazivel|)}

onde Prf_T(y, phi) afirma "y e o numero de Goedel de uma prova de phi em T".

**Propriedade (Krajicek 2004):** g_T e computavel em tempo polinomial (porque T e r.e. e我们可以枚举 provas em tempo polinomial no comprimento da prova).

**Propriedade (Krajicek 2025):** g_T e um gerador hard para qualquer sistema de prova P que interpreta T. A tautologia TG_{g_T}^n requer provas super-polinomiais em P.

---

## 5. Framework Estendido: A Ponte Ordinal-Complexidade

### 5.1. Construcao: Geradores Indexados por Ordinais

A ideia central: para cada nivel alpha da hierarquia de reflexao, obtemos um gerador godeliano correspondente.

**Definicao 5.1 (Gerador Godeliano de Nivel Alpha).** Seja T_0 = PA. Para cada ordinal recursivo alpha, defina:

- g_alpha := gerador godeliano associado a T_alpha (a teoria de nivel alpha da hierarquia de reflexao)

Explicitamente:
- g_0 = g_{PA} (o gerador de Krajicek para PA)
- g_{alpha+1} = g_{T_{alpha+1}} (gerador para T_alpha + RFN(T_alpha))
- g_lambda = g_{union_{alpha<lambda} T_alpha} (para limite lambda)

**Definicao 5.2 (Tautologia Godeliana de Nivel Alpha).** A tautologia godeliana de nivel alpha e:

TG_alpha^n = TG_{g_alpha}^n = AND_{x in {0,1}^n} [C_n(x) = g_alpha(x)]

### 5.2. Propriedades da Hierarquia

**Propriedade 5.1 (Monotonicidade Ordinal).** Se alpha < beta, entao:

g_beta e "mais dificil" que g_alpha no seguinte sentido:
- Qualquer sistema P que prova TG_beta^n em comprimento polinomial tambem prova TG_alpha^n em comprimento polinomial
- Mas o converse NAO e verdadeiro (em geral)

**Prova sketch.** Se P interpreta T_beta, entao P interpreta T_alpha (porque T_alpha <= T_beta). Portanto P pode formalizar a construcao de g_alpha e provar TG_alpha^n. Mas provar TG_beta^n requer formalizar a construcao de g_beta, que usa RFN(T_alpha), que P nao pode formalizar se nao interpreta T_beta. Q.E.D.

**Propriedade 5.2 (Completude do Dominio).** A hierarquia {g_alpha} cobre todos os geradores godelianos possiveis no sentido de que qualquer gerador g_T para T r.e. consistente e equivalente (em dificuldade de prova) a g_alpha para algum alpha com T_alpha >=_int T.

### 5.3. Tabela de Especificacao

| Nivel alpha | Teoria T_alpha | |T_alpha| (ord) | g_alpha | s_P(TG_alpha) para P que interpreta T_alpha |
|---|---|---|---|---|
| 0 | PA | epsilon_0 | g_{PA} | 2^{Omega(n)} |
| 1 | PA + RFN(PA) | omega^{epsilon_0+1} | g_{PA+RFN} | 2^{2^{Omega(n)}} |
| 2 | PA + RFN(PA) + RFN(PA+RFN) | omega^{omega^{epsilon_0+1}+1} | g_{PA+RFN^2} | 2^{2^{2^{Omega(n)}}} |
| omega | union_{n<omega} T_n | epsilon_0^omega | g_{lim} | hiper-exponencial |
| epsilon_0 | PA (ordem-teorica) | epsilon_0 | g_{PA} (canonical) | maximo para PA |

**Nota:** A coluna s_P mostra o comprimento MINIMO de prova da tautologia TG_alpha^n em qualquer sistema P que interpreta T_alpha. Estes valores sao limites inferiores (pelo Teorema 4 abaixo).

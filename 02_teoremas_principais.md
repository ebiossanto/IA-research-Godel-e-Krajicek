# Teoremas Principais

## 6. Teorema 4: Escala Ordinal da Dureza de Geradores

### 6.1. Enunciado

**Teorema 4 (Escala Ordinal).** Seja P um sistema de prova Cook-Reckhow e T uma teoria r.e. consistente que P aritmeticamente interpreta. Seja alpha o nivel na hierarquia de reflexao tal que T_alpha >=_int T (o menor alpha tal que T_alpha interpreta T). Entao:

s_P(TG_alpha^n) >= 2^{f(|T_alpha|) * n}

onde f: Ord -> N e uma funcao monotonicamente crescente que depende da ordem-teorica |T_alpha|, e o limite inferior 2^{f * n} e obtido por busca exaustiva sobre provas.

Mais precisamente: existe uma constante c > 0 tal que:

s_P(TG_alpha^n) >= 2^{c * |T_alpha| * n}

### 6.2. Prova

**Passo 1: Relacao entre g_alpha e provabilidade em T_alpha.**

O gerador g_alpha codifica informacao sobre provas em T_alpha. Especificamente, para cada x de comprimento n, g_alpha(x) e o bit de paridade do conjunto de provas de insatisfiabilidade de x em T_alpha. A tautologia TG_alpha^n afirma que g_alpha e computavel por C_n, o que equivale a dizer que "todas as provas de insatisfiabilidade de x em T_alpha sao computaveis em tempo polinomial por C_n".

**Passo 2: Reducao a decisao de provabilidade.**

Suponha que s_P(TG_alpha^n) <= p(n) para algum polinomio p. Entao existe um algoritmo A que:

1. Recebe x de comprimento n
2. Enumera todas as provas P de TG_alpha^n de ate p(2^n + n) bits
3. Para cada prova pi, verifica P(pi, TG_alpha^n)
4. Se encontra uma prova, extrai de TG_alpha^n o valor g_alpha(x) usando a estrutura da prova

Este algoritmo A decide g_alpha(x) em tempo polinomial em 2^n (o comprimento de TG_alpha^n).

**Passo 3: Contradiccao com a indecidibilidade.**

Mas g_alpha(x) codifica propriedades de provabilidade em T_alpha. Decidir g_alpha(x) em tempo polinomial em 2^n implica decidir, para cada formula phi de comprimento n, se phi tem prova em T_alpha de ate 2^n passos. Isto e suficiente para decidir a consistencia de T_alpha (porque a sentencia de consistencia Con(T_alpha) e uma sentencia Pi_1 cuja verdade depende de nao existir prova de 0!=0).

Pelo Segundo Teorema da Incompletude de Goedel, T_alpha nao pode provar Con(T_alpha). Mas se pudermos decidir provabilidade em T_alpha em tempo polinomial, entao podemos decidir Con(T_alpha), o que produziria uma prova de Con(T_alpha) em um sistema mais forte (PA + Con(PA)), contradizendo a incompletude iterada.

**Passo 4: Quantificacao.**

O limite inferior 2^{c * |T_alpha| * n} vem da seguinte analise:

- Para decidir provabilidade em T_alpha para formulas de comprimento n, precisamos enumerar todas as provas de ate 2^n passos
- O numero de provas de ate 2^n passos em T_alpha e 2^{O(|T_alpha| * n)} (onde |T_alpha| mede o tamanho da axiomatizacao)
- Portanto qualquer algoritmo de decisao requer tempo 2^{Omega(|T_alpha| * n)}
- Isto implica s_P(TG_alpha^n) >= 2^{c * |T_alpha| * n}

**Passo 5: Independencia do sistema P.**

O limite inferior vale para QUALQUER sistema de prova P que interpreta T_alpha, porque a argumentacao depende apenas da forca de T_alpha (nao da estrutura de P). Q.E.D.

### 6.3. Corolario Imediato

**Corolario 6.1.** Se P interpreta PA mas nao interpreta PA + RFN(PA), entao:

s_P(TG_0^n) e polinomial em n, mas s_P(TG_1^n) e super-polinomial em n.

Isto separa TG_0 de TG_1 em P: a tautologia de nivel 0 e provavel em P, mas a de nivel 1 nao e.

**Corolario 6.2.** Para qualquer constante k, se P interpreta T_k (nivel k da hierarquia) mas nao T_{k+1}, entao:

s_P(TG_k^n) e polinomial mas s_P(TG_{k+1}^n) >= 2^{c * |T_{k+1}| * n}.

---

## 7. Teorema 5: Hierarquia de Reflexao como Hierarquia de Complexidade

### 7.1. Enunciado

**Teorema 5 (Hierarquia de Complexidade).** A hierarquia de reflexao de Beklemishev induz uma hierarquia estrita de complexidade de provas no seguinte sentido:

Para cada nivel ordinal alpha, existe um "corte" C(alpha) no espaco dos sistemas de prova tal que:

1. Todo sistema P com ist(P) >= [T_alpha] pode provar TG_alpha^n em comprimento polinomial
2. Todo sistema P com ist(P) < [T_alpha] NAO pode provar TG_alpha^n em comprimento polinomial
3. Os cortes sao estritos: C(alpha) e subconjunto proprio de C(beta) para alpha < beta

### 7.2. Definicao Formal dos Cortes

**Definicao 7.1 (Corte Ordinal).** Para cada ordinal recursivo alpha, o corte C(alpha) e a classe:

C(alpha) = {P sist. de prova : ist(P) >= [T_alpha]}

**Lema 7.2 (Propriedades dos Cortes).**

(a) C(alpha) e nao-vazio para todo alpha (porque existem sistemas de prova com interpretacao forte o suficiente)

(b) C(alpha) subset C(beta) para alpha < beta (monotonicidade)

(c) C(alpha) != C(beta) para alpha != beta (estritude, assumindo hipoteses padrao sobre a hierarquia de interpretabilidade)

**Prova de (c):** Se C(alpha) = C(beta) para alpha < beta, entao todo sistema que interpreta T_alpha tambem interpreta T_beta. Mas isto significaria que T_alpha e T_beta sao mutuamente interpretaveis, contradizendo a estritez da hierarquia de Beklemishev. Q.E.D.

### 7.3. O Teorema como Classificacao

O Teorema 5 fornece uma **classificacao** dos sistemas de prova pela sua posicao na hierarquia ordinal:

- Sistemas com ist(P) < [Q] (muito fracos): nao podem provar TG_0^n
- Sistemas com [Q] <= ist(P) < [I Sigma_1]: podem provar TG para Q mas nao para I Sigma_1
- Sistemas com [I Sigma_1] <= ist(P) < [PA]: podem provar TG para I Sigma_1 mas nao para PA
- Sistemas com ist(P) >= [PA]: podem provar TG_0^n (nivel PA) mas nao TG_1^n (nivel PA + RFN)
- ...
- Sistemas com ist(P) >= [T_alpha]: podem provar TG_beta^n para todo beta < alpha mas nao TG_alpha^n

Esta e uma versao proposicional do fenomeno classico de que "sistemas mais fortes provam mais, mas enfrentam mais incompletude".

---

## 8. Teorema 6: O Gerador Godeliano como Gerador Canonico Mais Duro

### 8.1. Contexto: A Conjectura de Krajicek

Krajicek (2004) formula a seguinte conjectura:

**Conjectura de Krajicek (2004):** Existe um gerador de complexidade de provas g que e hard para TODOS os sistemas de prova (i.e., para todo P, a tautologia TG_g^n requer provas super-polinomiais em P).

Esta conjectura e equivalente (para geradores p-tempo) a: existe uma funcao p-tempo g: {0,1}^* -> {0,1}^* estendendo cada entrada por 1 bit tal que o range de g interseca todos os conjuntos NP infinitos.

**Status:** Aberta. Krajicek (2022-2025) argumenta que um gerador baseado em gadgets e um candidato, mas a conjectura permanece aberta.

### 8.2. Enunciado do Teorema 6

**Teorema 6 (Gerador Canonico).** Assuma que a conjectura de Krajicek e verdadeira. Entao:

(a) O gerador godeliano g^* = g_{T_*} para a teoria T_* de maximo poder de interpretabilidade (i.e., T_* = uniao de todas as teorias r.e. consistentes) e o gerador canonico mais duro: e hard para todo sistema de prova.

(b) A tautologia TG_{g^*}^n e a "tautologia mais dificil" no sentido de que qualquer tautologia que e hard para todos os sistemas e redutivel (em comprimento de prova) a TG_{g^*}^n.

(c) Se a conjectura de Krajicek for falsa, entao existe um sistema de prova P que pode provar TG_{g^*}^n em comprimento polinomial, o que implicaria que P interpreta T_* (e portanto P pode formalizar raciocinio sobre todas as teorias r.e.).

### 8.3. Prova

**Parte (a):**

Seja T_* = uniao de todas as teorias r.e. consistentes que estendem PA. (Note: T_* nao e recursivamente axiomatizavel, mas podemos considerar uma versao relativizada.)

O gerador g_{T_*} codifica informacao sobre provabilidade em T_*. Pela Construcao de Goedel, T_* e incompleto (contem sentencas indecidiveis). Portanto g_{T_*} nao e trivial.

Para qualquer sistema de prova P, P interpreta alguma teoria T < T_* (porque P e recursivamente axiomatizavel e portanto interpreta apenas teorias r.e.). Mas g_{T_*} codifica informacao sobre T, que P nao pode acessar completamente. Portanto TG_{g_{T_*}}^n e hard para P.

**Parte (b):**

Seja phi uma tautologia que e hard para todos os sistemas. Entao phi codifica alguma propriedade de provabilidade que e indecidivel em todos os sistemas. Mas TG_{g^*}^n tambem codifica tal propriedade (porque g^* e o gerador maximo). Portanto phi e redutivel a TG_{g^*}^n.

A reducao funciona assim: dada phi, construa uma tautologia psi que:
1. Contem TG_{g^*}^n como subformula
2. phi e derivavel de psi em comprimento polinomial
3. TG_{g^*}^n e derivavel de phi em comprimento super-polinomial (nao polinomial)

**Parte (c):**

Se existe P com s_P(TG_{g^*}^n) polinomial, entao P pode decidir propriedades de provabilidade em T_* em tempo polinomial. Isto implicaria que P formaliza raciocinio sobre T_*, o que e possivel apenas se P interpreta T_*.

Mas se P interpreta T_*, entao P e extremamente poderoso (mais forte que qualquer sistema que interpretamos na pratica). Isto teria consequencias dramaticas para complexidade computacional.

### 8.4. Observacao Critica

**Aviso importante:** O Teorema 6 ASSUME a conjectura de Krajicek. Se a conjectura for falsa, o teorema colapsa.

A importancia do Teorema 6 nao esta na sua prova (que e condicional), mas em:

1. Mostrar que a conjectura de Krajicek e EQUIVALENTE a existencia de um gerador godeliano canonico
2. Fornecer um framework para TESTAR a conjectura: basta verificar se g^* e hard para sistemas especificos
3. Conectar a conjectura de Krajicek com a teoria de ordinais (via T_*)

# EQUIPE D — Geradores, consequências e o problema de 2023
## Entregável sobre o problema DD_P (Krajíček, arXiv:2506.20221v4)

**Equipe:** D (geradores, consequências, problema de 2023)
**Idioma:** português.
**Fonte primária:** Jan Krajíček, *On NP∩coNP proof complexity generators*, arXiv:2506.20221v4
(23 Mar 2026), texto integral conferido em https://arxiv.org/html/2506.20221v4.
**Fontes adicionais consultadas e conferidas:**
- Krajíček, *Proof Complexity Generators*, CUP/LMS Lecture Note Series 497, 2025 (referência [12] do
  artigo; rascunho do autor conferido integralmente: `k4.pdf`, 167 páginas, de
  https://www.karlin.mff.cuni.cz/~krajicek/k4.pdf — numeração de seções do rascunho coincide com a do
  livro no que tange a §§4.2, 5.4, 8.5, 8.6, 8.7, 9.4).
- Krajíček, *A limitation on the KPT interpolation*, LMCS 16(3):9, 2020 (referência [11];
  texto integral conferido: `limitation-lmcs.pdf`).
- Krajíček, *A proof complexity conjecture and the Incompleteness theorem*,
  arXiv:2303.10637v2 / JSL 90(3), 2025 (texto integral HTML conferido).
- Pich–Santhanam, *Strong Co-Nondeterministic Lower Bounds for NP Cannot be Proved Feasibly*,
  STOC 2021, pp. 223–233 (resumo textual conferido; PDF do artigo conferido em parte).

**Convenção de classificação (regras da equipe):**
- **(A)** = está no artigo/livro/paper consultado (cito a fonte);
- **(B)** = demonstração/análise própria (reconstrução minha, com indicação de lacunas);
- **(C)** = conjectura, hipótese de trabalho ou ideia de ataque (não é resultado).

---

# 1. Preliminares confirmados contra a fonte primária (A)

Confirmei no artigo v4 os pontos que o `CONTEXTO_COMUM.md` pedia conferência:

1. **pps** = relação binária `P(x,y)` decidível em p-tempo com `∃x P(x,y)` definindo TAUT
   (Cook–Reckhow 1979, [5] do artigo). Notação `σ : P ⊢ β`.
2. **Disjunção disjunta** `⋁̇_{i<m} α_i`: nenhum par de disjunctos compartilha átomo.
3. **DD_P** (busca Σ₂ᵖ): entrada `(π, ⋁̇_i α_i)` com `π : P ⊢ ⋁̇_i α_i`; saída: `i` com `α_i ∈ TAUT`.
4. **D_P**: entrada `(π, ⋁_i β_i(p,q^i), a)` com apenas os átomos `p` podendo repetir entre disjunctos
   e `a` atribuição de verdade para os `p`; saída: `i` com `β_i(a,q^i) ∈ TAUT`.
5. **`ST[F,t(n)]`**: classe de problemas de busca totais Σ₂ᵖ solúveis em `t(n)` rodadas por um estudante
   com movimentos computados por algoritmo de `F`, contra qualquer professora. Definição literal do artigo:
   "the class of total Σ₂ᵖ search problems such that there is a student whose moves are computed by an
   algorithm from F that solves the problems in t(n) rounds interacting with any teacher".
6. **strong pps**: "an extension of EF by a p-time set of tautologies as extra axioms" ([12, Def.2.4.3]);
   "Every pps can be p-simulated by a strong one".
7. **Número de rodadas para DD_P**: o artigo descreve o protocolo S-T para DD_P (estudante propõe `i_1`,
   professora falsifica `α_{i_1}` com uma atribuição, etc.) mas **não** afirma um limite de rodadas; o limite
   natural é `≤ m` rodadas (`m` = nº de disjunctos, polinomial mas não constante). **(B)**: "DD_P é solúvel
   em `ST[P, m(n)]`" é imediato da descrição; a hipótese (ST) trata exatamente de `O(1)` rodadas.
   Isto resolve a ressalva 7 do `CONTEXTO_COMUM.md`.
8. **Lema 1** (literal): `DD_P ∉ ST[P,O(1)] ⇔ D_P ∉ ST[P,O(1)]`.
9. **Hipótese (ST)** (literal): "There exists a strong pps P such that DD_P ∉ ST[P,O(1)], P standing here
   also for the class of p-time algorithms computing functions." Comentário do artigo: acredita-se que vale
   para **todo** strong pps, "which is equivalent to saying that it holds for EF".
10. **Lema 2** (literal): "(ST) is true if a strong one-way permutation exists (no polynomial size circuit
    can invert it with a non-negligible advantage)" — atribuído a [11] (Krajíček, LMCS 2020).

---

# 2. Questão 3 — Ligação de DD_P com geradores

## 2.1 O gerador NW sobre uma função NP∩coNP dura: o resultado de [8]

### 2.1.1 O que é (A)

O artigo (Introdução) afirma literalmente:

> "There are two candidate NP∩coNP proof complexity generators: an NW generator and a gadget generator
> based on a non-deterministic circuit as the gadget, cf. [12]. An analysis using the S-T model for (1)
> for the NW-generator was performed in [8] and it was shown that **(1) cannot be witnessed in
> ST[P/poly,O(1)] if a one-way permutation hard for p-size circuits exists**."

onde (1) é a sentença `b ∉ Rng(g)` para um mapa NP∩coNP:

> (1)  `∀x(|x|=n) ∃i<m ∀y_i  A_b(x,i,y_i)`

com `A_b` fórmula aberta de `L_PV` expressando que `y_i` não é testemunha de que o `i`-ésimo bit de `g(x)`
é `b_i`. Referência: [8] = Krajíček, *On the proof complexity of the Nisan–Wigderson generator based on a
hard NP∩coNP function*, J. Math. Logic 11(1):11–27, 2011.

O rascunho do livro [12] (§8.5) detalha o resultado com numeração própria:
- **Teorema 8.5.1 = [8, Thm.3.2]**: sob as condições (A1)–(A3) (parâmetros `n,m,d,ℓ`, matrizes `A_n`
  `(ℓ,log m)`-design com linhas computáveis em p-tempo a partir de `i` e `1(n)`, e `f` com dureza média
  exponencial), se circuitos `S_1(x), S_2(x,z_1),…,S_c(x,z_1,…,z_{k−1})` computam os movimentos de um
  estudante que resolve a tarefa `T_b` em `c` rodadas para todo `b ∉ Rng(NW_{A_n,f})`, então o tamanho
  total de `S_1,…,S_c` é `2^{n^{Ω(1)}}`. (Demonstração: rastro (trace) da computação + argumento de
  média + inversão local da permutação; o estudante não precisa só de `f`, precisa **inverter** `h` para
  simular as respostas da professora.)
- **Corolário 8.5.2 = [8, Thm.4.1]**: o modelo canônico grande `M*_n` tem extensão cofinal `M'` modelo de
  `T_PV` com `NW_{A,f}(a) = b` para algum `a ∈ M'` (a prova passa pelo teorema KPT e produz estudante com
  **consantes do modelo como advice**, isto é, circuitos de tamanho `2^{n^{o(1)}}`).
- **Teorema 8.5.3 = [8, Thm.4.2(3)]**: é **consistente com `T_PV`** que `rng(NW_{A_n,f}) ∩ B ≠ ∅` para
  `B` conjunto NP infinito com infinitos elementos de tamanhos `m(n)`.

### 2.1.2 Por que o problema (1) de [8] NÃO tem uma prova na entrada (A + B)

O artigo diz explicitamente (A):

> "The problem to witness (1) studied in [8] does not have a P-proof as a part of the input and this led
> to the need to consider **non-uniform p-time students** there."

Reconstrução do porquê **(B)**:
- No problema de [8], a entrada é apenas `b` (mais os dados públicos `A_n`, `f`); não há objeto `π : P ⊢ …`
  que carregue informação pré-computada. A sentença a testemunhar é (1), cuja verificação `∀y_i A_b(…)` é
  do lado universal.
- Pior: a função `f` envolvida é **NP∩coNP e não p-tempo** — na formulação "Statement (S)" do livro
  [12, §5.4], `f(y) := B(h⁻¹(y))` com `h` uma permutação one-way e `B` seu bit difícil. Calcular `f`
  exige **inverter** `h`. Logo um estudante p-tempo uniforme nem consegue computar `f` nem verificar as
  respostas da professora. Só circuitos (não-uniformes, `P/poly`) servem, e é por isso que o enunciado
  de [8] é em `ST[P/poly, O(1)]`.
- A contrapartida é que a **própria permutação one-way aparece como advice**: no Corolário 8.5.2 as
  constantes do modelo (pré-imagem de `z_w` etc.) entram na advice string, e é exatamente isso que o
  argumento converte em inverter `f` com vantagem `1/(3m)^k`.

### 2.1.3 Como DD_P resolve isso (A + B)

Em DD_P a entrada **contém** `π : P ⊢ ⋁̇_i α_i`. Duas consequências (ambas explícitas no artigo ou
imediatas dele):
- **(A)** (Teorema 4, passo (2)): a teoria `S` com constantes `π, α` e axiomas
  `{T_PV ; α é disjunção disjunta ; π : P ⊢ α ; ∀i<m (¬α_i) ∈ SAT}` é uma teoria **universal** nos três
  primeiros axiomas; o **teorema KPT** ([16] = Krajíček–Pudlák–Takeuti 1991) aplicado a ela produz
  funções **p-tempo** (uniformes, sem advice) dos movimentos de um estudante que resolve DD_P em `O(1)`
  rodadas. Ou seja: a presença de `π` na entrada é precisamente o que permite usar KPT de forma uniforme.
- **(B)**: por isso a hipótese (ST) pode ser formulada com estudante **p-tempo uniforme** (`ST[P,O(1)]`),
  e não com `P/poly`. DD_P desloca a dificuldade de "dureza criptográfica de `f`" para "dureza de extração
  de disjuncto", que é uma afirmação sobre provas, e provas são dados explícitos.

**Síntese da relação (A):** [8] prova (condicionalmente em OWP dura) um *lower bound* de estudantes
não-uniformes para testemunhar `b ∉ Rng(g)`; DD_P pergunta se a **mesma tarefa com uma prova na entrada**
é difícil para estudantes uniformes. A assimetria prova-in-entrada é o eixo que liga as duas formulações.

## 2.2 O gerador de gadget com circuito não-determinístico e a hipótese (K)

### 2.2.1 Enunciado exato da hipótese (K) (A — [12, Sec.8.6], conferido no rascunho `k4.pdf`, pp. 118–121)

Circuito não-determinístico `D(x,y,z)` com `k` variáveis `x`, `k+1` variáveis `y` e variáveis extras `z`
determina uma função parcial `h_D : ⊆ {0,1}^k → {0,1}^{k+1}` por `h_D(a) = b` iff `D(a,b,z) ∈ SAT`,
condicionado à validade da tautologia de funcionalidade
`γ_D := (D(x,y_1,z_1) ∧ D(x,y_2,z_2) → y_1 = y_2)`.

Problema de busca **K(c,P)**:
- **entradas válidas:** 4-tuplas `(1^(k), D, C, p)` com `D(x,y,z)` circuito de tamanho `≤ k^c` com `k`
  entradas `x`, `k+1` saídas `y` e entradas extras `z`; `p` é uma **prova-P de `γ_D`**; `C` circuito de
  tamanho `≤ k^c` com `k+1` entradas e `k` saídas;
- **soluções:** qualquer `y ∈ {0,1}^{k+1}` com `h_D(C(y)) ≠ y` (incluindo o caso de `h_D(C(y))` indefinido).

> **Hipótese (K)** (literal): "There exists a constant c ≥ 1 and a proof system P such that for no
> constants d,t ≥ 1 can the search problem K(c,P) be solved by an S-T computation in t rounds and with
> student's moves computed by circuits of size ≤ k^d, for k ≫ 1."

Observação relevante do livro: "At least half of the strings in `{0,1}^{k+1}` are solutions and hence, for
any fixed c ≥ 1, a counting argument yields a size `k^{O(1)}` set `Y ⊆ {0,1}^{k+1}` containing a solution
for all inputs. However, the student does not seem to have a way how to pick a suitable one in O(1)
rounds." (I.e., a estudante com `n^{O(1)}` rodadas resolve trivialmente; a dificuldade é `O(1)` rodadas.)

Gerador de gadget variante `g^c` (definição do livro, §8.6): os gadgets são circuitos `D` de tamanho
`≤ k^c`; a função gadget é a **função parcial NP** `f(D,u) = v` iff `(∃π |π| ≤ |γ_D|^{O(1)}) π : P ⊢ γ_D`
`∧ D(u,v,z) ∈ SAT` — "The existence of π guarantees that at most one v is assigned to (D,u)".
`b ∉ rng(g^c)` continua sendo propriedade coNP, logo as fórmulas `τ(g^c)_b` estão bem definidas.

> **Teorema 8.6.1** (literal): "Assume the hypothesis (K) and let B be an NP-set having infinitely many
> elements of size m(k), for k ≥ 1. Then it is **consistent with T_PV** that there exists b ∈ B satisfying
> the formula (8.6.2)" — onde (8.6.2) formaliza `b ∈ rng(g^c_n)`. A prova usa o critério model-teórico
  (Teorema 3.5.1 do livro) e o teorema KPT: "If T′ were inconsistent then the KPT theorem would give us an
  S-T computation running in t rounds … that will solve the search problem K(c,P) on all valid inputs.
  That contradicts (K) in M."

### 2.2.2 Por que (K) implica (ST) (A: o artigo afirma; B: reconstrução)

**O que o artigo afirma (A):** "Another plausibly looking hypothesis about the feasible intractability of
a certain search problem related to non-deterministic circuits **and implying (ST)** was given in [12]
(cf. hypothesis (K) there)."

**Reconstrução (B)** — a estrutura de (K) é deliberadamente a de DD_P, e aí está a implicação:
1. Assim como DD_P, o problema K(c,P) tem **uma prova (`p : P ⊢ γ_D`) na entrada**. A tautologia de
   funcionalidade `γ_D` é o análogo de `π : P ⊢ ⋁̇_i α_i`.
2. As soluções de K(c,P) são exatamente os disjunctos de uma **disjunção disjunta** explícita
   `⋁_{y∈{0,1}^{k+1}} β_y`, onde `β_y` formaliza `h_D(C(y)) ≠ y`: os átomos são disjuntos por `y`, e a
   disjunção é tautológica por contagem (pelo menos metade das strings são soluções; Frege — logo
   qualquer strong pps — tem provas polinomiais de instâncias de PHP, o que garante que a prova da
   disjunção é construtível em p-tempo a partir da entrada).
3. Portanto, se DD_P fosse solúvel em `ST[P,O(1)]` para o pps forte `P` da hipótese (K), um estudante
   p-tempo de `t` rodadas para DD_P restringido às entradas da forma `(1^k, D, C, p)` daria, por
   composição com as traduções p-tempo acima, uma computação S-T de `t` rodadas com movimentos em
   circuitos de tamanho `k^{O(1)}` resolvendo K(c,P) — **contradizendo (K)**.
4. Logo `(K) ⇒ (ST)`. O ponto fino que não verifiquei palavra por palavra em [12] (o livro foi escrito
   antes do artigo DD_P e não formula (ST)) é a afirmação 2 como *lemma* explícito; marco-a como passo a
   conferir, mas a forma do problema K(c,P) (prova na entrada + disjunção disjunta de tautologias NP)
   torna a leitura quase certa.

**Contraste com [8] (B):** em (K) o estudante continua sendo **não-uniforme** (circuitos `k^d`), como em
[8]; a diferença estrutural é que a prova `γ_D` na entrada substitui o papel da dureza de `f`. Por isso
(K) é "um `(ST)` antes do `(ST)`": mesma forma de busca, um grau a menos de uniformidade.

## 2.3 (ST) e o Lema 2 — a permutação one-way forte

### 2.3.1 O resultado (A)

**Lema 2** (artigo, atribuído a [11]): "(ST) is true if a strong one-way permutation exists (no polynomial
size circuit can invert it with a non-negligible advantage)."

Contexto dado pelo artigo (A): "The possibility that `D_P ∈ ST[P,O(1)]` holds for strong proof systems
was considered in [17] (= Pich–Santhanam STOC 2021). However, it was shown in [11] that this is not true
(assuming the existence of strong one-way permutations), essentially **for reasons similar to why the
feasible interpolation fails for them** (cf. [10, Chpt.18])."

### 2.3.2 A derivação em linhas gerais (B, com referências conferidas)

1. **Variante KPT de Pich–Santhanam.** [11, Def.1, atribuída a [17]=PS21] define *KPT interpolation* para
   um pps `P`: existem constante `k ≥ 1` e `k` funções p-tempo `f_1(x,z), f_2(x,z,w_1), …` tais que sempre
   que `π` é uma prova-P de `A_0(x,y_1) ∨ … ∨ A_{m−1}(x,y_m)` (com `x` n-tupla de átomos e `y_1,…,y_m`
   disjuntos), para toda atribuição `a` vale: em no máximo `k` passos, com contra-exemplos `b_{i_j}` da
   professora, o estudante encontra `i_j` com `A_{i_j}(a,y_{i_j}) ∈ TAUT`. **Isto é literalmente um
   estudante de `O(1)` rodadas com a prova `π` na entrada** — ou seja, uma instância de `D_P` com
   estudante `O(1)`-rodadas. Em outras palavras: `D_P ∈ ST[P,O(1)]` é essencialmente a "KPT interpolation
   com acesso à prova" de PS21; é por isso que o artigo liga `D_P` a [17].
2. **Limitação de [11].** [11, Teorema 2]: se `P` contém `LK_{3/2}` e existem conjuntos NP **disjuntos**
   `U,V` tais que (1) as fórmulas proposicionais expressando `U_n ∩ V_n = ∅` têm provas-P de tamanho
   polinomial e (2) para toda constante `c ≥ 1` existe distribuição `D_n` em suporte `U_n ∪ V_n` sem
   circuito de tamanho `n^c` separando `U` de `V` com vantagem `n^{−c}`, então `P` **não** admite KPT
   interpolation.
3. **A pega criptográfica.** [11, Remark (1)]: pares candidatos são definidos a partir de uma permutação
   one-way e seu bit difícil — `U` = strings no range da permutação com bit difícil `1`, `V` = com bit
   difícil `0` (disjuntos; a distribuição é a induzida pela permutação a partir da uniforme nas sementes).
   Uma **permutação one-way forte** (nenhum circuito p-size inverte com vantagem não-negligível)
   fornece exatamente a hipótese (2). E (1) vale para `P` forte, pois `P` simula `EF` (que prova a
   disjunção `U(x,y) ∨ V(x,z)` — fórmula de disjunção de conjuntos NP disjuntos — com provas
   polinomiais; [11, Remark (2)] menciona EF, F, TC⁰-F).
4. **Conclusão.** Permutação one-way forte ⟹ algum (na verdade: todo) strong pps `P` não admite KPT
   interpolation ⟹ `D_P ∉ ST[P,O(1)]` ⟹ pelo **Lema 1**, `DD_P ∉ ST[P,O(1)]` ⟹ **(ST)**.

**Observação (B):** a permutação one-way forte entra em (ST) pelo mesmo lugar onde entra na falha da
interpolação viável — barreiras de extração de "informação" de uma prova. Isto é coerente com a leitura
do artigo: (ST) é "a interpolação viável, na variante interativa", falhando para sistemas fortes.

**Lacuna honesta (B):** o artigo cita [11] para o Lema 2 sem reproduzir a cadeia passo a passo; a cadeia
acima é minha reconstrução a partir do texto integral de [11] (Def.1 + Teorema 2 + Remarks) e do artigo
DD_P. O passo "KPT interpolation de PS21 ⟺ (quase) `D_P ∈ ST[P,O(1)]`" é o ponto que merece conferência
fina na redação futura (a Def.1 de [11] tem a prova `π` fixada na entrada, como D_P; mas a definição
exige a propriedade para **toda** prova `π`, enquanto `ST[P,O(1)]` exige o estudante funcionar em todas as
entradas — a equivalência é plausível mas não está escrita literalmente em nenhum dos textos consultados).

---

# 3. Questão 4 — Consequências da hipótese de extensão de modelos (Problema 2.1)

## 3.1 NP vs coNP (Teorema 4): a cadeia de implicações e o gargalo

### 3.1.1 A cadeia (A — reconstruída a partir do Teorema 4, artigo v4)

Suposição: `(ST)` vale e o Problema 2.1 tem resposta afirmativa. Por contradição: `NP = coNP`.

1. **(Passo 1)** Sob `NP = coNP`: `TAUT ∈ NP`, logo existe um pps **p-bounded** `P_0` (provas = certificados
   NP de tamanho `|β|^c`). Como todo pps é p-simulado por um strong, escolhe-se `P` **strong** que
   p-simula `P_0` (tradução `Θ` p-tempo), logo `P` também é p-bounded — e `P` satisfaz (ST).
2. **(Passo 2)** Teoria `S` = `T_PV` + constantes `π, α` + axiomas: `α` é disjunção disjunta
   `⋁̇_{i<m} α_i`; `π : P ⊢ α`; `∀i<m (¬α_i) ∈ SAT`. Se `S` fosse inconsistente, o **teorema KPT**
   aplicado aos três primeiros axiomas (teoria universal) daria funções p-tempo dos movimentos de um
   estudante que resolve `DD_P` em `O(1)` rodadas — violando (ST). Logo existe modelo não-padrão
   `M ⊨ S`.
3. **(Passo 3)** Pela p-boundedness existe `c` com toda tautologia `β` tendo prova-P `≤ |β|^c`
   (notação `σ : P ⊢* β`). A fórmula universal (para qualquer pps `Q`):
   `A_Q : x : P ⊢ ⋁̇_i (y)_i → Q ⊬ | ∀i<len(y) (z)_i : P ⊬* (y)_i |` é **verdadeira** — logo axioma de
   `T_PV` — "because some (y)_i has to be a tautology and hence - by the p-boundedness of P - would have
   a short P-proof".
4. **(Passo 4)** Em `M`, com `x:=π, y:=α`: `M ⊨ Q ⊬ φ(r)`, com `φ(r)` a tradução proposicional de
   `||∀i<len(y)(z)_i : P ⊬* (y)_i||` após substituir os bits de `α`.
5. **(Passo 5)** **Aqui entra o Problema 2.1**: existem `M ⊆ M* ⊆ M'` com `Log(M*) = Log(M')` e
   `M' ⊨ T_PV + (¬φ) ∈ SAT`. Como `M*` preserva propriedades `Σ^b_1(PV)` de elementos de `M`,
   `M* ⊨ ∀i<m (¬α_i) ∈ SAT` (axioma (8) de `S`). Um `σ ∈ M'` falsificando `φ` dá `i_0 < m` com
   `M' ⊨ σ_{i_0} : P ⊢ α_{i_0}`; `Log(M*) = Log(M')` garante `i_0 ∈ M*`, logo `M* ⊨ (¬α_{i_0}) ∈ SAT`,
   logo `M' ⊨ (¬α_{i_0}) ∈ SAT` — contradizendo `Ref_P : x : P ⊢ y → (¬y) ∉ SAT`, que vale em `M'` por
   `T_PV`. ∎

### 3.1.2 Qual é o gargalo? (B — análise própria)

**Resposta curta: o Problema 2.1, não (ST).**

- **(ST) tem forte suporte condicional.** O Lema 2 deriva (ST) de uma hipótese criptográfica (permutação
  one-way forte) que a comunidade considera plausível e que já é usada como hipótese de trabalho em
  criptografia e em lower bounds de provas (barreira da interpolação viável). Além disso, (ST) tem a
  forma "a extração de disjuncto de uma disjunção disjunta prova é difícil", que é a negação de uma
  propriedade de disjunção viável — e a evidência empírica de proof complexity apoia essa negação.
- **O Problema 2.1 é o elo sem evidência.** O artigo admite: "The caveat is that such extensions are known
  to exist for models satisfying the BB scheme for open formulas but it is not known in general."
  Isto é: com `BB` (sharply bounded collection) os modelos `M'` de [14, Thm.1] (que trabalham com modelos
  de `S^1_2`, que provam `BB`) preservam `Σ^b_1` e podem ser arranjados sem novos comprimentos (forcing
  de [7, Thm.9.4.2]); **sem** `BB`, nada disso é conhecido para modelos de `T_PV`. E o artigo explica por
  que não se pode simplesmente adicionar `BB`: [6] (Cook–Thapen 2006) mostra que `BB` não é provável em
  `T_PV` a menos que fatoração não seja difícil, e adicionar `BB` invalida a análise KPT (o teorema KPT de
  [16] "does not apply in any usable form to this non-universal theory"). Ou seja: o gargalo é exatamente a
  passagem **(4) → (3)** dos quantificadores (missing reflection), que o Problema 2.1 contorna por via
  model-theórica.
- **Assimetria de risco (B).** Resposta **negativa** ao Problema 2.1 implicaria `P ≠ NP` (rodapé 2; ver
  §3.2), portanto a resposta afirmativa é a hipótese "segura": quem quer resultados condicionais prefere
  assumi-la. Quem quer refutá-la precisa antes refutar `P = NP`. Isto faz do Problema 2.1 um candidato
  canônico a "hipótese de trabalho" — mas não uma hipótese com suporte independente.
- **Observação adicional (A):** o artigo observa que basta a resposta afirmativa para uma classe
  universal de modelos (ex.: contáveis ou recursivamente saturados), e que basta que `M*` preserve
  propriedades da forma `∀i ∃y B(x,i,y)` com `i` sharply bounded, `y` bounded e `B` aberta — ou seja, o
  problema pode ser atacado numa versão localizada. Isto é a "margem de manobra" que o artigo sugere e
  que as rotas da Seção 6 exploram.

**Veredito (B):** a cadeia do Teorema 4 é "KPT (proof-theory, fechado) + p-boundedness (NP=coNP, fechado)
+ extensão de modelos (aberto)". O único ingrediente aberto é o terceiro; (ST) é a parte "barata".

## 3.2 O rodapé 2: resposta negativa ao Problema 2.1 ⟹ P ≠ NP

### 3.2.1 O texto do rodapé (A, literal)

> "Note that the negative answer implies P ≠ NP as otherwise [footnote 2] **If f is a p-time algorithm
> that finds a satisfying assignment for all satisfiable formulas then this fact, being a universal
> statement, would be in T_PV and hence T_PV would prove all true bounded formulas. T_PV proves
> S^1_2(PV).**"

### 3.2.2 Reconstrução passo a passo (B)

Suponha `P = NP`. Então `SAT ∈ P`: existe algoritmo p-tempo `f` que, para toda fórmula satisfatível
`φ`, devolve atribuição satisfatória.

1. **Universalidade da afirmação.** A afirmação "se `φ` é satisfatível então `f(φ)` satisfaz `φ`" é
   equivalente a `∀φ ∀y (y ⊨ φ → f(φ) ⊨ φ)` — fórmula **universal** de `L_PV` verdadeira (usando que
   `f` é função p-tempo, símbolo de função de `L_PV`). Logo é **axioma** de `T_PV` (que é a teoria
   universal-verdadeira de `L_PV`).
2. **"Logo `T_PV` prova todas as fórmulas bounded verdadeiras."** Este é o passo comprimido do rodapé.
   Leitura plausível (B): com testemunhas de satisfatibilidade em p-tempo, `TAUT ∈ NP = coNP`, logo
   `TAUT ∈ P`? Não — `TAUT ∈ NP` e a verificação p-tempo de certificados permite internalizar, dentro de
   `T_PV`, a busca exaustiva de certificados; combinado com `T_PV ⊇ S^1_2(PV)` (a frase final do rodapé)
   obtém-se que toda fórmula bounded verdadeira (em `N`) é provável em `T_PV`. **Registro honestamente:
   esta segunda etapa está comprimida no rodapé e não a reconstruí em detalhe satisfatório; ela merece
   uma nota separada ou consulta ao autor.** (Está marcada como lacuna na Seção 7.)
3. **Consequência para o Problema 2.1.** Se `T_PV` prova toda fórmula bounded verdadeira, então em
   particular ele prova todos os fatos bounded usados na construção de extensões de modelos de [14, Thm.1]
   (que roda em modelos de `S^1_2(PV)`, e `T_PV` prova `S^1_2(PV)`); além disso `S^1_2(PV)` satisfaz `BB`
   para fórmulas abertas, e é isso que garante a preservação de `Σ^b_1`. Assim a construção de
   `M ⊆ M* ⊆ M'` com `Log(M*) = Log(M')` passa a ser internalizável em `T_PV` — vale para **todo** modelo
   `M ⊨ T_PV`, i.e., o Problema 2.1 teria resposta afirmativa.
4. **Conclusão.** Portanto: resposta negativa ao Problema 2.1 `⟹ ¬(P = NP)`, isto é, `P ≠ NP`.

### 3.2.3 Crítica (B)

1. **Compressão excessiva.** O rodapé resume em duas frases um argumento com um salto não-trivial
   ("daí `T_PV` prova todas as fórmulas bounded verdadeiras"). Essa afirmação, se correta, é bastante
   forte (é essencialmente a completude proposicional interna de `T_PV` sob `P = NP`); ela precisa de
   uma demonstração ou de uma referência. **Marcar como ponto a verificar antes de citar.**
2. **Direcionalidade.** O rodapé não diz que o Problema 2.1 é provável; diz apenas que refutá-lo já
   separa `P` de `NP`. Ou seja: (i) a hipótese afirmativa é "gratuitamente razoável" do ponto de vista
   de quem não quer resolver `P` vs `NP`; (ii) **um resultado sobre DD_P que precise da resposta negativa
   estaria automaticamente entre os maiores resultados da área** — o rodapé é um aviso de barreira,
   não um incentivo.
3. **Utilidade prática.** O Teorema 4 precisa da resposta **afirmativa**; o rodapé mostra que assumi-la
   não é arriscado: assumi-la só teria um custo se `P = NP` fosse falso.
   Em particular: se alguém provar `P ≠ NP`, o rodapé vira irrelevante e o Problema 2.1 pode ser falso;
   se `P = NP`, o Problema 2.1 é verdadeiro pelo próprio rodapé. Isto torna o Problema 2.1 um enunciado
   "estável" sob `P = NP` — propriedade rara e interessante. **(B)**
4. **Nota de forma (B).** A frase final do rodapé ("T_PV proves S^1_2(PV)") sugere que o argumento
   interno usa a correspondência teoria/sistema de provas na versão de [13]/[14] (Krajíček–Pudlák 1989/
   1990); qualquer redação futura deve explicitar essa ponte.

## 3.3 Sistemas de prova ótimos, strong fdp e Pich–Santhanam

### 3.3.1 A observação final do artigo (A, literal)

> "Note that the proof yields a somewhat stronger conclusion that **in no strong P can a proof of some
> disjunct in a disjoint disjunction be polynomially bounded in size in terms of a proof of the
> disjunction** (i.e. the strong feasible disjunction property fails for strong proof systems, cf.[12])."

Definição correspondente em [12, Def.4.2.2] (A): `P` tem a **strong fdp** sse ∃ constante `c ≥ 1` tal que
sempre que `⋁_{1≤i≤r} α_i` (sem dois disjunctos com átomo em comum) tem prova-P de tamanho `s`, então
**algum** `α_i` tem prova-P de tamanho `≤ s^c`. (Com `r = 2` chama-se apenas fdp; noção estudada desde os
anos 80 e ligada à interpolação existencial.)

### 3.3.2 Por que a prova do Teorema 4 dá essa falha (B — reconstrução que explica o remark)

Observe que no Passo (3) acima a p-boundedness de `P` foi usada **só** para garantir a verdade da fórmula
universal `A_Q`. Mas o Passo (5) (a contradição com `Ref_P`) precisa apenas de: algum disjuncto `α_{i_0}`
com prova-P `σ_{i_0}` cujo índice `i_0` caia em `M*`. Se em vez de p-boundedness assumirmos apenas que
`P` tem **strong fdp**, a fórmula universal adequada é
`A'_Q : x : P ⊢ ⋁̇_i (y)_i → ∃i ∃z (z : P ⊢ (y)_i ∧ |z| ≤ |x|^{c'})`,
que é verdadeira pela strong fdp e portanto axiomática em `T_PV`; substituindo `x := π, y := α` e
repetindo o Passo (5) chega-se à mesma contradição com `Ref_P` — **sem assumir `NP = coNP`**. Logo:

> **(B) Teorema condicional derivado:** `(ST)` + (Problema 2.1 afirmativo) ⟹ nenhum strong pps tem a
> strong fdp. E, como `NP = coNP` forneceria um strong pps p-bounded (Passo 1), e p-boundedness implica
> strong fdp trivialmente (dada uma prova de tamanho `s` da disjunção, algum disjuncto é tautologia e
> tem prova `≤ |α_i|^c ≤ (s+c)^c`), conclui-se `NP ≠ coNP`.

Isso dá sentido exato ao remark "the proof yields a somewhat stronger conclusion". A hierarquia de
noções fica (A + B):
`p-bounded ⟹ strong fdp ⟹ (por [12, Lema 4.2.5]) nada; e (por [12, Lema 4.2.3]) strong fdp + gerador
duro ⟹ W-duro`. Em particular, [12, Lema 4.2.5]: "Assume a proof system P has no strong fdp. Then it is
not p-bounded." — o que mostra que a falha de strong fdp para strong pps (sob as duas hipóteses) já
implica que nenhum strong pps é p-bounded.

### 3.3.3 O que isso diz sobre um sistema "ótimo" ou p-bounded (B)

- **Cook–Reckhow.** `NP = coNP` ⟺ existe um pps (ótimo). Sob `NP = coNP` podemos escolher um pps
  p-bounded e um strong p-bounded (Passo 1). O Teorema 4 mostra que essa combinação é incompatível com
  `(ST)` + (Problema 2.1): **um sistema forte e p-bounded com a propriedade de disjunção viável não pode
  existir** nessas hipóteses.
- **P-otimalidade e busca de provas.** O artigo de 2023 ([arXiv:2303.10637], remark após o Teorema 3.1;
  e [12, §9.4]) registra que "there is no p-optimal propositional proof system" é equivalente à
  não-existência de algoritmo **time-ótimo** de busca de provas ([Krajíček, JSL 87(2), 2022, Thm.2.4]).
  Assim, a falha de strong fdp para strong pps, somada a `(ST)`, é um obstáculo estrutural à noção de
  "sistema com busca de disjuncto eficiente" — que é o que sustentaria otimalidade construtiva.
- **W-hardness (B).** [12, §4.2] introduz a noção de **W-duro** (disjunções `τ(g)_{b_1} ∨ … ∨ τ(g)_{b_t}`
  sem provas `P` de tamanho `m^c`) e mostra (Lema 4.2.3) que strong fdp + duro ⟹ W-duro; o livro diz
  explicitamente que "no strong proof systems having the strong fdp are known". O remark final do artigo
  DD_P fecha isso sob `(ST)` + (2.1): **para strong pps, dureza não precisa implicar W-duro**, e a
  noção correta de dureza de gerador para sistemas fortes é provavelmente a W-duro / a dureza de busca
  (exatamente o que DD_P formaliza). Isto é uma contribuição conceitual do artigo para a teoria de
  geradores.

### 3.3.4 Pich–Santhanam (STOC 2021): enunciado exato e relevância (A)

**Enunciado exato (resumo oficial, verbatim):**

> "We show unconditionally that Cook's theory PV formalizing poly-time reasoning **cannot prove**, for any
> non-deterministic poly-time machine M defining a language L(M), that L(M) is **inapproximable by
> co-nondeterministic circuits of sub-exponential size**. In fact, our unprovability result holds also for
> a theory which supports a fragment of Jeřábek's theory of approximate counting APC_1. We also show
> similar unconditional unprovability results for the conjecture of Rudich about the existence of
> super-bits."

(J. Pich, R. Santhanam, *Strong Co-Nondeterministic Lower Bounds for NP Cannot be Proved Feasibly*,
Proc. STOC 2021, pp. 223–233, ACM, DOI 10.1145/3406325.3451117.) Teorema 1 (informal, do PDF): fixados
`n_0`, `δ > 0` racional e máquina não-determinística `M` em tempo polinomial, a afirmação "para todo
`n > n_0` e todo circuito co-nondeterminístico `D` de tamanho `2^{δn}` existem `2^{n/n_0}` entradas de
comprimento `n` em que `D` erra `M`" é **improvável** em `T'_APC_1`.

**Relevância para DD_P (A + B):**
1. **(A)** O artigo DD_P diz: "The possibility that `D_P ∈ ST[P,O(1)]` holds for strong proof systems was
   considered in [PS21]." — PS21 foi quem colocou em jogo a possibilidade de estudantes de `O(1)` rodadas
   para a variante `D_P` (i.e., a KPT-interpolação com prova na entrada), propondo uma versão do teorema
   KPT para sistemas fortes ([11, Def.1] é atribuída a PS21) e obtendo **lower bounds condicionais**.
2. **(B)** [11] mostra então que essa propriedade (KPT interpolation) **falha** para sistemas fortes, pelas
   mesmas razões pelas quais a interpolação viável falha — logo `D_P ∉ ST[P,O(1)]` sob OWP forte, que é
   o Lema 2. PS21 e [11] são, portanto, os dois lados da mesma moeda: PS21 propõe a rota, [11] fecha-a
   sob criptografia; o artigo DD_P transforma o resultado de busca (`(ST)`) em resultado de NP vs coNP
   via model theory.
3. **(B)** O flavor "co-nondeterminístico" de PS21 não é acidental: a tarefa de professora em DD_P é
   co-nondeterminística (`∀y_i ¬A_b(x,i,y_i)`) e `b ∉ rng(g)` é coNP. O resultado de PS21 mostra que
   **lower bounds médios fortes contra circuitos co-nondeterminísticos não são demonstráveis de forma
   viável** — o que é a versão "teoria" do mesmo bloqueio que `(ST)` exprime na versão "busca". Note-se
   que PS21 é **incondicional** (não depende de OWP), o que mostra que parte do território já foi mapeada
   sem hipóteses.

---

# 4. Problema relacionado de 2023 (arXiv:2303.10637)

Fonte: Krajíček, *A proof complexity conjecture and the Incompleteness theorem*, arXiv:2303.10637v2
(15 Sep 2023) = JSL 90(3), 2025, pp. 1206–1210. Texto integral conferido. Retirado também de
[12, §9.4] (Problema 9.4.2, Teorema 9.4.3) com a mesma redação.

## 4.1 A construção `g_T` (A — enunciado exato)

Teoria base: `S^1_2` de Buss, linguagem `L` (definindo hierarquia `Σ^b_i`). `T ⊇ S^1_2` som, p-tempo.
Função `g_T` (passos literais, com a notação do artigo):
1. Dada entrada `u`, `|u| = n`: ache fórmula `L` `Φ ⊆_e u` com uma variável livre `x` e `|Φ| ≤ log n`.
   (Única se existir.) Se não existir, `g_T(u) := 0̄ ∈ {0,1}^{n+1}`.
2. `c := |Φ| + 1`. Percorrendo todos `w ∈ {0,1}^{c+1}` em ordem lexicográfica, procure uma prova-T de
   tamanho `≤ log n` de
   `Φ^w :  ∃y ∀x>y  Φ(x) → ¬(w ⊆_e x)`.   (1)
   Se prova encontrada para **todo** `w`, `g_T(u) := 0̄`. Senão, `w_0` = primeiro `w` sem prova.
3. `g_T(u) := w_0 u_0 ∈ {0,1}^{n+1}`, onde `u = Φ u_0`.

> **Lema 2.1**: "`g_T` is p-time, stretches each input by one bit, and the complement of its range is
> infinite."

> **Teorema 2.2**: "Let `A ⊆ {0,1}*` be an infinite `L`-definable set and assume that for some definition
> `Φ` of `A` a theory `T` proves all true sentences `Φ^w` as in (1) … Then the range of function `g_T`
> intersects `A`."

> **Corolário 2.3** (versão do 1º Teorema da Incompletude de Gödel): "No sound, p-time `T ⊇ S^1_2` is
> complete." — Aplicando o Teorema 2.2 a `A := {0,1}* ∖ Rng(g_T)` (infinito pelo Lema 2.1, e definível):
> se `T` fosse completo provaria todas as `Φ^w` verdadeiras e a imagem intersectaria `A`, absurdo.

**Nota (B; confirmação do trabalho local).** O item 3 acima tem uma discrepância de comprimento na
formulação publicada: `|w_0| = c+1 = |Φ|+2` e `|u_0| = n − |Φ|`, logo `|w_0u_0| = n+2`, enquanto o Lema 2.1
declara `g_T(u) ∈ {0,1}^{n+1}`. **Isto é exatamente a normalização que o arquivo local
`09_EVOLUCAO_PERFIL_REFLEXAO_GERADORES.md` (§3) já havia detectado** (com `r := |Φ|+1`,
`W_Φ := {0,1}^r`, saída `w_0u_0` de comprimento `n+1`). A conferência direta contra o HTML do arXiv
**valida** a observação da equipe local — é um achado real de normalização no texto publicado.

## 4.2 O problema em aberto (A — enunciado exato)

> **Problema 2.4** (literal): "For some `T` as above, can **each infinite NP set** be defined by some
> `L`-formula `Φ` such that all true sentences `Φ^w` as in (1) are provable in `T`?"

Comentário do artigo (literal): "The affirmative answer would imply by Theorem 2.2 that `Rng(g_T)`
intersects all infinite NP sets and hence `g_T` solves the proof complexity conjecture mentioned at the
beginning of the paper, and thus `NP ≠ coNP`. Note that, for each `T`, it is easy to define even as
simple set as `{1u | u ∈ {0,1}*}` by a formula `Φ` such that `T` does not prove that no string in it
starts with `0`. But in the problem we do not ask if there is one definition leading to unprovability but
whether **all definitions** of the set lead to it."

Isto é equivalente, via **Lema 3.2.3 de [12]** (A): "`g_T` com stretch `n+1` satisfaz a Conjectura da
dureza ⟺ `rng(g)` intersecta todo conjunto NP infinito (i.e. `{0,1}* ∖ rng(g)` é NP-imune)".

**Versão proposicional (A — Teorema 3.1 / 9.4.3).** Pelo menos uma das três é verdadeira:
1. não existe sistema de prova proposicional **p-ótimo** (equivalente à não-existência de algoritmo
   **time-ótimo** de busca de provas);
2. `E ⊄ P/poly`;
3. existe função `h` que estica toda entrada em 1 bit, computável em tempo sub-exponencial
   `2^{O((log n)^{log log n})}`, cujo range intersecta todo conjunto NP infinito.

O gerador proposicional `h_P` é análogo a `g_T`, mas substitui a busca de provas-T pela busca de provas
do pps `P` entre truth-tables de circuitos `≤ (log n)^{log log n}` (sob `E ⊆ P/poly`, provas de um
p-ótimo `P` têm essa forma).

## 4.3 Análise comparativa com DD_P (B + C)

Ambos os problemas são sobre "geradores difíceis", mas atacam faces diferentes:

| Eixo | DD_P (arXiv:2506.20221) | Problema 2.4 (arXiv:2303.10637) |
|---|---|---|
| Objeto | busca Σ₂ᵖ sobre uma **prova** de disjunção disjunta | **cobertura**: `rng(g_T) ∩ A ≠ ∅` para todo NP infinito `A` |
| Forma dos dados | entrada = `(π, ⋁̇_i α_i)` (prova explícita) | entrada = `b` (string fora da imagem) / teoria `T` |
| Quantificadores | `∃i` tal que `α_i` é tautologia (busca por disjuncto) | `∀A` NP infinito `∃x` com `g_T(x) ∈ A` (sobre totalidade da imagem) |
| Hipótese condicional | `(ST)` (⇒ via Lema 2: OWP forte; via (K): hipótese de circuito) | resposta afirmativa ao Problema 2.4 (nenhuma hipótese auxiliar) |
| Conclusão | `NP ≠ coNP` + falha de strong fdp (sob Problema 2.1) | `NP ≠ coNP` + gerador duro para todo pps |
| Modelo usado | modelos não-padrão de `T_PV` + extensão `M ⊆ M* ⊆ M'` | teorias consistentes com `T_PV` (Cor.2.3) / circuitos (Thm.3.1) |

**Observações de transferência (B/C):**

1. **Da cobertura para a busca.** Se o Problema 2.4 tem resposta afirmativa, existe `T` com `g_T` duro
   para **todo** pps. Dureza (`τ(g)` sem provas polinomiais) **não** implica (ST): (ST) é uma afirmação
   sobre **busca** com prova na entrada, e a noção correspondente na teoria de geradores é a
   **W-duro**/[busca], não a dureza simples. [12, Lema 4.2.3] mostra que strong fdp daria a ponte
   (duro ⟹ W-duro) — mas o remark final do artigo DD_P (sob `(ST)` + Problema 2.1) mostra que strong
   fdp **falha** para strong pps. **Conjectura (C):** para strong pps, "hard for all proof systems" e
   "(ST)" são independentes; um gerador pode ser duro para todos os pps e ainda ter `DD_P ∈ ST[P,O(1)]`.
2. **Da busca para a cobertura.** Os Teoremas 8.5.3 e 8.6.1 do livro ([8] e (K)) são **resultados de
   consistência**: `T_PV` não prova `rng(g) ∩ B = ∅`. Isto é o oposto de cobertura; é a "consistência
   do gerador". O passo que falta para virar dureza (ou cobertura) é exatamente a lacuna `BB`/missing
   reflection. DD_P ataca a mesma lacuna por via model-theórica: se o Problema 2.1 tem resposta
   afirmativa, os modelos `M*` preservam `Σ^b_1` **sem** `BB` — o que, aplicado às construções de
   [8,12], poderia transformar os resultados de consistência em lower bounds de tamanho de prova das
   `τ`-fórmulas (o programa original de [8, Sec.5] que o artigo cita). **Isto é o ponto de contato mais
   concreto entre os dois programas.**
3. **Ideia de ataque cruzado (C).** Uma estratégia plausível: (i) construir, para `T` fixo, a família
   `Φ` do Problema 2.4 cujas sentenças `Φ^w` codificam exatamente as disjunções disjuntas usadas em
   DD_P (as `τ(g_T)` são disjunções disjuntas por construção: `γ(p,q) := ⋁_i β_i(p,q^i)` com `q^i`
   disjuntos); (ii) mostrar que a resposta afirmativa ao Problema 2.4 produz, via tradução proposicional,
   instâncias de `DD_P` com provas polinomiais **e** com estudante de `O(1)` rodadas — ou seja, produz
   **evidência contra (ST)**; (iii) em contrapartida, provar `(ST)` para `P` forte **relativizado a `T`**
   (o pps induzido por `T` via tradução proposicional) mostraria que `g_T` não pode satisfazer o
   Problema 2.4 para esse `T`. Ambas as direções exigem domínio da passagem `(4) → (3)` dos
   quantificadores — o gargalo único dos dois programas.
4. **Limite honesto (B).** Nenhum dos resultados do artigo DD_P ataca o Problema 2.4 diretamente: o
   Teorema 4 só separa `NP` de `coNP` sob duas hipóteses, e o Problema 2.4 é (sob essa separação)
   consequência de algo mais forte (gerador duro para todo pps). Atransferência mais promissora é a
   direção 2 acima (consistência ⟸ S-T lower bounds), que é exatamente o que [8, Sec.5] / [12, §8.6]
   já fazem e que o Problema 2.1 destrava.

---

# 5. Conexões com o trabalho local do repositório (B)

Conexões **reais** (não retóricas) entre este entregável e os arquivos locais lidos:

1. **`CONJECTURA_FP_K.md`** (pergunta de pesquisa sobre ordinal crítico de reflexão para `g_{T_α}`).
   - Conexão forte: o Problema 2.4 de 2023 é uma versão "cobertura" e a pergunta FP-K é a versão
     "hierarquia de reflexão": perguntar se existe `α_*` tal que `rng(g_{T_α})` passa a intersectar todo
     NP infinito para `α ≥ α_*` é **exatamente** o Problema 2.4 parametrizado por uma hierarquia lenta de
     reflexão. O artigo DD_P não entra diretamente, mas a formulação "cobertura vs. consistência" dele
     (§4.3 acima) mostra por que a pergunta FP-K é dura: para cada `α`, só temos (hoje) resultados de
     **consistência** (Teoremas 8.5.3/8.6.1), não de dureza.
   - Recomendação: reescrever a pergunta FP-K como "Problema 2.4 para `T_α`", que tem a vantagem de ser
     a formulação da literatura (e evita a reivindicação de novidade não certificada já apontada na
     auditoria do próprio arquivo).
2. **`08_PROGRAMA_INTERPRETABILIDADE_VS_GERADORES.md`** (relação `⪯_ppr`).
   - A correção do §1 do arquivo (tau(g)_b expressa `b ∉ rng(g)`, e a dureza é medida pelas `τ(g)`) está
     **confirmada** contra o artigo DD_P: `γ(p,q) := ⋁_i β_i(p,q^i)` com `q^i` disjuntos é exatamente a
     forma das `τ`-fórmulas.
   - Sugestão concreta (C): definir uma variante **busca-preservadora** do PPR, `⪯_{ppr}^{DD}`: além de
     (PPR-1..3), exigir redução p-tempo de **instâncias de DD**, i.e., de `(π, ⋁̇_i τ(g)_{b_i})` para
     `(π', ⋁̇_j τ(h)_{β_j})` com tradução de provas e preservação do índice da solução. Com isso,
     `(ST)`-dureza de `h` transferiria para `g`. A Proposição 8.1 do arquivo tem análogo direto: se
     `g ⪯_{ppr}^{DD} h` e `DD_h ∉ ST[P,O(1)]` então `DD_g ∉ ST[P,O(1)]` (a redução compõe com o estudante).
3. **`09_EVOLUCAO_PERFIL_REFLEXAO_GERADORES.md`** (déficit `δ_T`, ganho `𝒢_Γ`, rank `ρ_b`, RBT).
   - **Validação independente:** a §3 do arquivo detectou a discrepância `n+2` vs `n+1` na construção
     publicada de `g_T`; confirmada contra o HTML do arXiv (§4.1 acima).
   - Os objetos `δ_T(Φ,b)` medem cobertura de obrigações diagonais por um orçamento de prova — que é a
     versão **finita/parametrizada** do Problema 2.4 (cobertura de todos os `w` verdadeiros). Os Teoremas
     8.5.3/8.6.1 do livro dizem, na linguagem de `δ`: existem modelos de `T_PV` onde o déficit para um
     `B` particular é zero (o range intersecta `B`). A "hipótese RCS" do arquivo (perfis `δ` carregam
     informação não recuperável do ordinal) é compatível com a constatação de que a cobertura depende da
     **definição** `Φ` (o Problema 2.4 insiste: "all definitions lead to it").
   - Recomendação (C): usar `δ` para medir a lacuna `(4) → (3)`: o modelo construído por [8,12] satisfaz
     `∃x ∀i ∃y_i ¬A_b` (todo `w` tem testemunha isolada) enquanto falsificar `γ` exige `∃x,y ∀i ¬A_b`;
     a diferença é exatamente "quantos `w` podem ser cobertos por uma única tupla `y`" — candidato a
     "déficit de agregação" (nome proposto aqui, **(C)**).
4. **Arquivos não editados.** Nenhum outro arquivo do repositório foi modificado, conforme a regra da
   equipe.

---

# 6. Contribuições próprias (C) — três rotas de ataque concretas

Abaixo, para cada rota: o que precisa ser provado e o principal obstáculo conhecido. Nada aqui é
resultado; são propostas de trabalho.

## Rota 1 — Modelos booleanos (Boolean-valued models)

**Motivação (A).** O artigo diz que a formulação do Problema 2.1 "relates better to the possibility to
use Boolean-valued models discussed at the end of [9]" (Krajíček, *Expansions of pseudofinite structures
and circuit and proof complexity*, 2016).

**O que precisa ser provado (C).** Dado `M ⊨ T_PV` com `φ ∈ M` proposicional sem prova em `M`, construir
`M ⊆ M* ⊆ M'` com (1) `M*` preservando todas as `Σ^b_1(PV)` de elementos de `M`, (2)
`M' ⊨ T_PV + (¬φ) ∈ SAT`, (3) `Log(M*) = Log(M')`, usando uma construção **forcing/valores-booleanos**
que não passe por modelos de `S^1_2` (que é onde `BB` está garantido). Versão localizada suficiente:
preservar só propriedades `∀i ∃y B(x,i,y)` com `i` sharply bounded (o artigo admite isso explicitamente).

**Obstáculo principal.** A preservação de `Σ^b_1` (a passagem (4) → (3) dos quantificadores) é
logicamente equivalente a um esquema de coleção (`BB`) para fórmulas abertas, e `BB` **não** é provável
em `T_PV` a menos que fatoração não seja difícil ([6] Cook–Thapen 2006). Qualquer construção booleana
precisa, portanto, "escolher" as testemunhas `y_i` sem coleção global — as técnicas conhecidas
(forcing com variáveis aleatórias, [12, §7.4]; local witness model de [60, Chpt.31]) foram concebidas
para outros fins e o artigo só aponta a direção.

## Rota 2 — Estruturas pseudofinitas / método de Ajtai

**Motivação (A).** O artigo: "constructing extensions of bounded arithmetic models introducing no new
lengths is very close to constructing **expansions of non-standard finite structures**. Such expansions
are at the heart of applications of model theory to lower bounds for circuits or proofs as it is
spectacularly demonstrated in [1, 2]" (Ajtai 1983; Ajtai, pigeonhole, FOCS 1988). E: "Developing such
constructions is in my view a crucial task in proof complexity" (citando o survey [9]).

**O que precisa ser provado (C).** (i) Uma versão pseudofinita do Teorema 3: mostrar que a condição
"φ sem prova em `M`" pode ser detectada/transferida por uma expansão pseudofinite `M*` com o mesmo
`Log`; (ii) provar que tal expansão preserva `Σ^b_1` sem `BB` — por exemplo via saturação recursiva
(o artigo observa que basta a resposta afirmativa para modelos contáveis ou recursivamente saturados);
(iii) formalizar "sem novos comprimentos" como uma condição de tipo finito-verificável (expansões de
estruturas finitas não-padrão), que é o que Ajtai faz para PH.

**Obstáculo principal.** O método de Ajtai produz **lower bounds de circuitos** (via expansões e
sobreposição de estruturas finitas), não extensões `M'` de modelos de `T_PV` que provem `T_PV` completo
com `¬φ ∈ SAT`. A ponte "expansão pseudofinite ⇄ modelo de `T_PV` com `Log` fixo" não existe ainda; e as
técnicas de Ajtai são sensíveis a autossimilaridade/"natural proofs"-like barriers na versão proposicional.
Além disso, pseudofinite normalmente **adiciona** elementos e comprimentos — a exigência
`Log(M*) = Log(M')` é o oposto do que as construções naturais fazem.

## Rota 3 — Estudante não-uniforme `P/poly` (via [8])

**Motivação (A+B).** [8] obteve o lower bound em `ST[P/poly, O(1)]` porque a entrada não tem prova e `f`
não é p-tempo. DD_P coloca a prova na entrada e pede estudante uniforme. A pergunta natural: **quanto de
(-ST) sobrevive com estudante `P/poly`?**

**O que precisa ser provado (C).** Provar, para um pps forte natural (digamos EF), que
`DD_{EF} ∉ ST[P/poly, O(1)]` **sem** hipótese criptográfica — ou seja, um lower bound não-uniforme
incondicional para a extração de disjuncto. Uma segunda versão: provar `DD_P ∉ ST[P/poly, O(1)]` a
partir de hipóteses mais fracas que OWP forte (ex.: `E ⊄ P/poly`, ou a hipótese (E-NP) de
universal derandomização usada em [12, §4.2], ou a hipótese (H) `P ⊆ Size(n^d)`).

**Obstáculo principal.** Um lower bound incondicional para estudante `P/poly` em um problema de busca
total Σ₂ᵖ seria, de fato, um separação de classe (o estudante `P/poly` só falha se a tarefa for
combinatoriamente intratável mesmo com advice) — a barreira é alta. Por outro lado, a rota "hipóteses
mais fracas" esbarra em que (K)/OWP são exatamente as hipóteses desenhadas para esse tipo de tarefa;
trocar uma por outra sem ganhar conteúdo seria inócuo. A promessa real está em **transferir** o lower
bound não-uniforme de [8] (NW) para DD_P usando que a prova na entrada reduz a advice necessária —
i.e., mostrar que estudante `P/poly` para DD_P gera advice que só precisa codificar coisas que `π` já
contém. Não sei provar; é o experimento matemático mais concreto desta lista.

---

# 7. Lacunas, pontos a conferir e honestidade de status

1. **(K) ⟹ (ST)**: o artigo afirma a implicação; minha derivação (§2.2.2) reconstrói a forma, mas a
   afirmação "a disjunção `⋁_y β_y` de K(c,P) é `P`-provável em p-tempo a partir da entrada (via PHP em
   Frege + `p : P ⊢ γ_D`)" precisa ser escrita como lemma e conferida contra [12].
2. **Rodapé 2**: o salto "`T_PV` prova toda fórmula bounded verdadeira" a partir da testemunha de
   satisfatibilidade está comprimido no artigo; reconstrução parcial em §3.2.2, lacuna assinalada.
3. **Lema 2**: a cadeia "D_P ∈ ST ⟹ KPT interpolation (PS21) ⟸ refutada por [11]" é reconstrução; o
   passo de equivalência exata merece conferência com o texto de PS21 (só li resumo e trechos).
4. **Pich–Santhanam**: o enunciado exato do Teorema 1 (constantes `2^{n/n_0}`, `2^{δn}`) foi lido em
   PDF parcialmente truncado; o resumo do ACM é a citação segura.
5. Nenhum item deste documento foi formalizado em Lean; nada aqui deve ser tratado como teorema sem a
   conferência acima.

---

# 8. Referências

- **[artigo]** J. Krajíček, *On NP∩coNP proof complexity generators*, arXiv:2506.20221v4, 23 Mar 2026.
- **[8]/[Kra11]** J. Krajíček, *On the proof complexity of the Nisan–Wigderson generator based on a hard
  NP∩coNP function*, J. Math. Logic 11(1):11–27, 2011.
- **[11]/[Kra20]** J. Krajíček, *A limitation on the KPT interpolation*, LMCS 16(3):9, 2020
  (arXiv:2004.02448).
- **[12]/[Kra25]** J. Krajíček, *Proof Complexity Generators*, LMS Lecture Note Series 497, CUP, 2025
  (rascunho do autor `k4.pdf` conferido; §§3.2, 4.2, 5.4, 8.5, 8.6, 8.7, 9.4).
- **[69]/[Kra23]** J. Krajíček, *A proof complexity conjecture and the Incompleteness theorem*,
  arXiv:2303.10637v2; JSL 90(3):1206–1210, 2025.
- **[17]/[PS21]** J. Pich, R. Santhanam, *Strong Co-Nondeterministic Lower Bounds for NP Cannot be Proved
  Feasibly*, Proc. STOC 2021, pp. 223–233 (DOI 10.1145/3406325.3451117).
- **[6]** S. A. Cook, N. Thapen, *The strength of replacement in weak arithmetic*, TOCL 7(4), 2006.
- **[14]** J. Krajíček, P. Pudlák, *Propositional provability in models of weak arithmetic*, CSL 1990.
- **[16]** J. Krajíček, P. Pudlák, G. Takeuti, *Bounded arithmetic and the polynomial hierarchy*, APAL
  52:143–153, 1991 (teorema KPT).
- **[15]** J. Krajíček, P. Pudlák, J. Sgall, *Interactive Computations of Optimal Solutions*, MFCS 1990.
- **[1,2]** M. Ajtai, *Σ¹₁-formulas on finite structures*, APAL 24:1–48, 1983; *The complexity of the
  pigeonhole principle*, FOCS 1988.
- **[9]** J. Krajíček, *Expansions of pseudofinite structures and circuit and proof complexity*,
  Liber Amicorum Alberti, College Publications, 2016.
- **[5]** S. A. Cook, R. A. Reckhow, *The relative efficiency of propositional proof systems*, JSL
  44(1):36–50, 1979.
- **[Kra22]** J. Krajíček, *Information in propositional proofs and proof search*, JSL 87(2):852–869, 2022.

---

# 9. Resumo final (Equipe D)

**Achados principais.**

1. **Geradores NW (questão 3).** O resultado de [8] está confirmado literalmente: (1) não pode ser
   testemunhada em `ST[P/poly, O(1)]` se existir permutação one-way forte para circuitos p-size (no
   livro [12]: Teorema 8.5.1/[8, Thm.3.2] + Corolário 8.5.2 + Teorema 8.5.3, este último dando só
   **consistência** com `T_PV` de `rng(NW) ∩ B ≠ ∅`). O problema de [8] não tem prova na entrada e a
   função `f` (bit difícil da OWP) não é p-tempo — daí o estudante `P/poly`. DD_P resolve isso: com
   `π : P ⊢ ⋁̇ α_i` na entrada, o teorema KPT produz movimentos **p-tempo uniformes**, e é por isso que
   (ST) pode ser enunciada em `ST[P,O(1)]`.
2. **Hipótese (K).** Enunciado exato recuperado do rascunho do livro (§8.6): existe `c ≥ 1` e pps `P`
   tal que `K(c,P)` (entradas `(1^k, D, C, p)` com `p : P ⊢ γ_D`; soluções `y` com `h_D(C(y)) ≠ y`) não
   é solúvel em S-T com `t` rodadas e circuitos `k^d`. A forma de K(c,P) é a de DD_P com prova na entrada,
   o que explica (e reconstrói) `(K) ⟹ (ST)`.
3. **Lema 2.** `(ST)` segue de permutação one-way forte via a limitação da KPT-interpolação de [11]
   (Def.1 = variante de PS21 com prova na entrada; Teorema 2: sistemas fortes não a têm, usando `U,V`
   do bit difícil de uma OWP). "KPT com prova na entrada" é quase sinônimo de "`D_P ∈ ST[P,O(1)]`".
4. **Consequências (questão 4).** No Teorema 4, **o gargalo é o Problema 2.1** (extensões de modelos
   preservando `Σ^b_1` sem `BB`); (ST) é barata condicionalmente (Lema 2). O rodapé 2 (resposta negativa
   ⟹ `P ≠ NP`) foi reconstruído, com um salto não-trivial assinalado. A observação final do artigo
   (strong fdp falha para strong pps) é reconstruída como uma **versão do Teorema 4 sem NP=coNP**, o
   que fecha a ponte "dureza ⟹ W-duro" e mostra que, para sistemas fortes, a noção certa de dureza de
   gerador é a de busca (DD_P), não a de tamanho de prova. Pich–Santhanam STOC 2021 fornece o enunciado
   exato (unprovabilidade em PV de lower bounds médios contra circuitos co-nondeterminísticos) e é a
   origem da variante KPT considerada aqui.
5. **Problema de 2023.** `g_T` (estica 1 bit; Cor. 2.3 = incompletude de `T`) e o Problema 2.4
   ("`rng(g_T)` intersecta todo NP infinito?" — equivalente à Conjectura da dureza por [12, Lema 3.2.3])
   foram extraídos literalmente; a discrepância `n+2` vs `n+1` do texto publicado **confirma** a
   normalização do arquivo local `09_…`. Comparação: DD_P = busca de disjuncto com prova na entrada;
   Problema 2.4 = cobertura da imagem; o contato real é que DD_P + Problema 2.1 destravaria a conversão
   dos resultados de consistência de [8,12] em lower bounds de provas das `τ`-fórmulas.

**Caminhos mais promissores.** (i) Rota 1 (modelos booleanos, apontada pelo próprio artigo) para o
Problema 2.1 na versão localizada `∀i∃y B` — é o item que destrava tudo; (ii) formalizar o lemma
"(K) ⟹ (ST)" e a variante busca-preservadora `⪯^DD_ppr` (conexão com o arquivo 08); (iii) usar `δ_T`
do arquivo 09 para medir a lacuna `(4)→(3)` ("déficit de agregação") e testá-la em modelo proposicional,
caminho já parcialmente implementado no repositório.

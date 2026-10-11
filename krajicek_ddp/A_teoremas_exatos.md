# A — Enunciados exatos, modelo S-T, redução ao aritmético (Problema DD_P)

**Equipe A (teoria).** Fonte primária: Jan Krajíček, *On NP∩coNP proof complexity
generators*, arXiv:2506.20221v4 (23 Mar 2026), https://arxiv.org/html/2506.20221v4
— **texto integral conferido nesta rodada** (todas as citações abaixo marcadas **(A✔)**
foram verificadas literalmente no HTML do artigo).

**Convenção de proveniência (regra 2 da equipe):**
- **(A✔)** = transcrição literal/paráfrase fiel **conferida no artigo**;
- **(A?)** = informação vinda só do `CONTEXTO_COMUM.md`, ainda não conferida;
- **(P)** = demonstração / razão própria desta equipe;
- **(C)** = conjectura / ideia de trabalho.

---

## 1. Enunciados exatos (transcrição fiel + tradução em palavras)

### 1.0 Fato de fundo: o que é `T_PV` neste artigo **(A✔)**
> "The provability of such a statement in **the true universal `L_PV`-theory `T_PV`** …"
> (Introdução) e "**is true and hence in `T_PV`**" (Thm 4, passo (3)),
> e "a pps `P` may be incomplete in a model of `T_PV` but it will always be **sound** as
> that is expressible by a **universal `L_PV`-formula**" (antes do Teorema 3).

**Tradução:** neste paper, `T_PV` é tratado como a **teoria universal verdadeira** em
`L_PV`: *todo sentença universal verdadeira de `L_PV` está em `T_PV`*, e por isso todo
modelo `M ⊨ T_PV` satisfaz a **correção (soundness) de todo pps**. Este fato é a chave
para §3(a) e para o passo (5) do Teorema 4 (`Ref_P`). *Não registrado no
`CONTEXTO_COMUM.md`* — registre-se aqui. **(A✔)**

### 1.1 pps — propositional proof system **(A✔)**
> "Recall from [5] that a propositional proof system (abbr. pps) is a **p-time decidable
> binary relation `P(x,y)`** such that the condition `∃x P(x,y)` defines `TAUT`. Instead
> of writing `P(σ,β)` we use the suggestive notation **`σ : P ⊢ β`** … `P ⊢ β` means that
> `β` has a `P`-proof."

**Tradução:** um sistema de prova é um *verificador de certificados* `P`, polinomial nos
dois argumentos, tal que uma fórmula é tautologia **se e somente se** tem certificado.
`P` é **relação**, não função: uma tautologia pode ter muitas provas, um não-teorema
nenhuma; `Prf_P(σ,β)` é, por construção, um predicado PV.

**Divergência com a formalização do usuário (registrada):** o usuário formalizou
`P : {0,1}* → TAUT`, p-time e **sobrejetora** — esta é a versão *função*, **não** a de
Cook–Reckhow usada no artigo. Problemas da versão função: (i) exige um gerador canônico
(único objeto-prova) por tautologia, hipótese que a noção clássica não faz; (ii) as noções
centrais do artigo — **p-simulação**, **strong pps**, prova curta `σ : P ⊢* β`, `Ref_P` —
são definidas sobre *relações* e não são invariantes por essa troca; (iii) mascara o fato
de que "provar" é relacional (não-determinismo), que é justamente o que faz de DD_P um
problema de *busca*. **Decisão: adotar a relação binária.** **(P)**

### 1.2 Disjunção disjunta (disjoint disjunction) **(A✔)**
> "A propositional disjunction `⋁_{i<r} α_i` is a **disjoint disjunction**, denoted
> `⋁̇_{i<m} α_i`, if **no two `α_i` have an atom in common**. We often leave `m` out …
> as **`m` is bounded by the size of the formula**."

**Tradução:** os disjunctos variam sobre conjuntos de átomos **mutuamente disjuntos**.
Consequência-chave **(P):** atribuições sobre átomos de `α_i` e `α_j` não conflitam e
fusíveis; e **`m ≤ |α|`**, o que é decisivo para §2 (limite de rodadas).

### 1.3 DD_P **(A✔)**
> **(abstract)** "… the following **`Σ^p_2` search problem `DD_P`** determined by a
> propositional proof system `P`: given a `P`-proof `π` of a disjunction `⋁_i α_i`, no
> two `α_i` having an atom in common, find `i` such that `α_i ∈ TAUT`."
> **(Seção 1)** "**input:** a pair `π, ⋁̇_i α_i` s.t. `π : P ⊢ ⋁̇_i α_i`;
> **solution:** any `i` s.t. `α_i ∈ TAUT`."

**Tradução:** dado um *certificado* de que uma disjunção de peças independentes é teorema,
devolva **um** pedaço que já é teorema por si só. Busca **total** (há sempre resposta),
**não funcional** (várias respostas possíveis). **Totalidade (A✔):** se cada `α_i` fosse
falsificável, a união das atribuições (átomos disjuntos ⇒ sem conflito) falsificaria a
disjunção inteira, contradizendo `P ⊢`.

**Observação de detalhe (P):** o argumento de totalidade admite duas reduções **p-time de
uma única testemunha**: (i) *restrição*: falsificante de `α` restringe-se a falsificante
de algum `α_i` (varredura `i<m`); (ii) *extensão*: falsificante de `α_i` estende-se
(irrelevante o resto) a falsificante de `α`, pois `α_i` falsa já falsa a disjunção.
**Nenhuma usa coleta (collection)/BB** — ponto central em §3(a).

### 1.4 D_P (generalização) **(A✔)**
> "**input:** a triple `π, ⋁_i β_i(p,q^i), a` s.t. `π : P ⊢ ⋁_i β_i`, **only atoms `p`
> can occur in more than one `β_i`**, and `a` is a truth assignment to atoms `p`;
> **solution:** any `i` s.t. `β_i(a,q^i) ∈ TAUT`."

**Tradução:** relaxa-se a disjunção disjunta para permitir **um bloco `p` compartilhado**,
cuja verdade é **dada na entrada**; só os `q^i` continuam disjuntos. Fixado `a`, os
`β_i(a, q^i)` tornam-se effectively disjuntos. **(P)**

Contexto **(A✔)**: "The possibility that `D_P ∈ ST[P,O(1)]` holds for strong proof
systems was considered in [17] (Pich–Santhanam, STOC 2021). However, it was shown in
[11] that this is not true (assuming the existence of **strong one-way permutations**),
essentially for reasons similar to why the **feasible interpolation** fails for them."

### 1.5 Modelo S-T e `ST[F, t(n)]` **(A✔)**
> "**`ST[F,t(n)]`**: the class of **total `Σ^p_2` search problems** such that there is a
> **student whose moves are computed by an algorithm from `F`** that solves the problems
> in **`t(n)` rounds** interacting with **any teacher**."
> "The S-T model makes sense for general total search problems where **the condition for
> the acceptance of a solution, here `∀y ¬A_b(x,i,y)`, starts with a universal
> quantifier**. Here all such search problems will be `Σ^p_2`."
> Movimento do professor (descrição do artigo): "S … proposes its first candidate
> solution `i_1`. If it is correct T will acknowledge this and the computation stops …
> Otherwise she will send to S a **counter-example**, some `w_1` such that
> `¬A_b(a,i_1,w_1)`. In that case the computation enters the second round with S
> proposing a second candidate solution `i_2` … The computation goes for a number of
> rounds until a solution is found. **We are interested in the case where the number of
> rounds is bounded by a constant.**"

**Tradução:** jogo "aluno–professor": o aluno *sugere*, o professor *refuta* com
contra-exemplo. Aluno fraco (algoritmo de `F`), professor **arbitrário** (sem restrição
de tempo). A complexidade mede-se pelo **número de rodadas** `t(n)`. Origem: [15]
Krajíček–Pudlák–Sgall, MFCS 1990; definição `ST` seguindo [12, Def.2.4.3/8.6].

### 1.6 strong pps **(A✔)**
> "Following [12, Def.2.4.3] we define a **strong pps** to be an **extension of EF**
> (Extended Frege, cf. [5]) by a **p-time set of tautologies as extra axioms** (see
> [12, Thm.2.4.4] …). **Every pps can be p-simulated by a strong one.**"

### 1.7 Lema 1 **(A✔)**
> `DD_P ∉ ST[P,O(1)]  ⇔  D_P ∉ ST[P,O(1)]`

**Tradução:** a barreira de O(1) rodadas de DD_P e a da sua generalização D_P coincidem
— pode-se trocar um pelo outro nas hipóteses/teses sem ganho nem perda.

### 1.8 Lema 2 **(A✔)**
> "**([11]) `(ST)` is true if a strong one-way permutation exists** (no polynomial size
> circuit can invert it with a non-negligible advantage)."

**Tradução:** a hipótese central é consequência de uma hipótese criptográfica clássica —
não é "ad hoc". ([11] = Krajíček, *A limitation on the KPT interpolation*, LMCS 16(3),
2020.)

### 1.9 Hipótese (ST) **(A✔)**
> "**Hypothesis (ST):** There exists a strong pps `P` such that
> **`DD_P ∉ ST[P,O(1)]`**, `P` standing here also for the class of p-time algorithms
> computing functions."
> "In fact, we do think that the hypothesis is true **for all strong proof systems**
> (which is **equivalent to saying that it holds for EF**, the Extended Frege proof
> system) but for the statement this apparently weaker formulation suffices."

**Tradução:** para **algum** (conjectura: para **todos**, em particular EF) strong pps,
nenhum aluno p-time resolve DD_P com **número constante de rodadas**. A palavra-chave é
**constante** — ver §2.

### 1.10 Problema 2.1 (o coração aberto) **(A✔)**
> "**Problem 2.1.** Assume `M ⊨ T_PV` and that it satisfies **Condition 1 in Theorem 3**.
> Does it follow that there are `L_PV`-structures `M*, M'`: `M ⊆ M* ⊆ M'` such that
> **(1)** `M*` preserves **all `Σ^b_1(PV)`-properties of elements of `M`**;
> **(2)** `M' ⊨ T_PV + (¬φ) ∈ SAT`;
> **(3)** `Log(M*) = Log(M')`?"

> "The assumption we shall use in Theorem 4 is that the problem has the **affirmative**
> solution. Note that the **negative answer implies `P ≠ NP`** as otherwise [rodapé 2]."
> "The problem asks about **all** models of `T_PV` but it would suffice to get the
> affirmative answer for a **sufficiently universal class of models** (e.g. **countable
> or recursively saturated**). Also, it suffices if `M*` preserves from `M` properties of
> the form **`∀i ∃y B(x,i,y)` with `i` sharply bounded, `y` bounded and `B` open**."
> "… this formulation also relates better to the possibility to use **Boolean-valued
> models discussed at the end of [9]**."
> "constructing extensions of bounded arithmetic models introducing **no new lengths** is
> very close to constructing **expansions of non-standard finite structures**. Such
> expansions are at the heart of applications of model theory to lower bounds for circuits
> or proofs as it is spectacularly demonstrated in **[1,2]** (Ajtai). Developing such
> constructions is in my view a **crucial task in proof complexity**; the survey **[9]**
> discusses this in detail (cf. also [10, Chpt.20])."

**Tradução:** dado um modelo não-padrão que **não consegue provar `φ`** (nenhum pps tem
prova de `φ` lá dentro), dá para estendê-lo a `M'` onde `¬φ` é satisfatível, **sem** que
o andaim `M*` perca nenhum fato `Σ^b_1` sobre os elementos de `M` e **sem** que os
comprimentos mudem entre `M*` e `M'`? O artigo **assume** resposta afirmativa.

**Pendência resolvida:** a referência **[9]** = J. Krajíček, *Expansions of pseudofinite
structures and circuit and proof complexity*, Liber Amicorum Alberti, College
Publications, 2016. E **[1],[2]** = Ajtai, *Σ¹₁-formulas on finite structures* (APAL 1983)
e *The complexity of the pigeonhole principle* (1988). **(A✔)**

### 1.11 Teorema 3 (após [14] = Krajíček–Pudlák, CSL 1990, Thm. 1) **(A✔)**
> "Assume `M` is a **non-standard model of `T_PV`** and let `φ ∈ M` be a propositional
> formula (in the sense of the model). The following two statements are equivalent:
> **(1)** `φ` has **no proof in `M` in any proof system**;
> **(2)** There exists an extension `M' ⊇ M` such that `M' ⊨ T_PV + (¬φ) ∈ SAT`."
>
> Comentários: "The fact that the construction in [14] works with models of `S^1_2`
> implies that `M'` **preserves (i.e. will satisfy) all `Σ^b_1` properties of elements of
> `M` true there** (this uses that the models satisfy the **sharply bounded collection
> principle `BB` for open `Σ^b_1`-formulas**, a consequence of `S^1_2`)."
> "… one can arrange that `M'` **introduces no new lengths** into `M`:
> `Log(M') = Log(M)` **(5)**, where **`Log(M) = { |m| : m ∈ M }`**. A construction which
> yields this (**with an additional requirement on `M`**) is the **forcing construction
> underlying [7, Thm.9.4.2]**."

**Tradução:** "não ter prova dentro de `M`" ⟺ "pode ser falsificado numa extensão". E os
dois ingredientes do Problema 2.1 existem **separadamente**: preservação `Σ^b_1` (via
modelos de `S^1_2`, usando **BB para fórmulas abertas**) e `Log(M')=Log(M)` (via forcing,
**com uma condição extra em `M`**). O Problema 2.1 pede **os dois ao mesmo tempo** numa
cadeia `M ⊆ M* ⊆ M'`, e sem a condição extra em `M`. É a tensão que cria o problema aberto. **(P)**

### 1.12 Teorema 4 **(A✔)** — enunciado e esquema da prova, item a item
> **Enunciado:** "Assume that **Problem 2.1 has the affirmative solution**. Then
> **Hypothesis (ST) implies `NP ≠ coNP`**."

> **(1)** "Assume for the sake of a contradiction that (ST) and `NP = coNP` both hold …
> Take a strong pps `P` that satisfies the condition in (ST) and is also **p-bounded**."
> **(2)** Teoria `S` na linguagem de `L_PV` + constantes `π, α`, axiomas:
> `T_PV`; "`α` is a **disjoint disjunction** `⋁̇_{i<m} α_i` (`m` determinado por `α`)";
> "`π : P ⊢ α`"; "`∀i<m (¬α_i) ∈ SAT`".
> "If `S` were **inconsistent** then applying the **KPT theorem** (cf. [16,7,12]) to the
> universal theory with axioms listed in the **first three items** would give **p-time
> functions computing moves of a student that solves `DD_P` in a constant number of
> rounds**, thus violating (ST)." Logo: "Let `M` be a model (**necessarily non-standard**)
> of `S`."
> **(3)** `c ≥ 1` com toda `β ∈ TAUT` tendo prova `P` de tamanho `≤ |β|^c`; notação
> `σ : P ⊢* β` := `(σ : P ⊢ β) ∧ (|σ| ≤ |β|^c)`.
> **Claim:** "For any pps `Q` the **universal formula `A_Q`**:
> `x : P ⊢ ⋁̇_i (y)_i → Q ⊬ || ∀i<len(y) (z)_i : P ⊬* (y)_i ||`   (6)
> … **is true and hence in `T_PV`**."
> Justificativa: "some `(y)_i` has to be a **tautology** and hence — by the
> **p-boundedness of `P` — would have a **short `P`-proof**."
> **(4)** "All `A_Q` hold in `M` and we can substitute `x := π` and `y := α`. This yields
> **`M ⊨ Q ⊬ φ(r)`**", onde `φ(r)` é obtida de
> `|| ∀i<len(y) (z)_i : P ⊬* (y)_i ||(r,q)` substituindo os bits de `α` pelos átomos `q`
> ("hence the sharply bounded universal quantifier becomes `⋀_{i<m}`") e `r` corresponde
> aos bits de `z`.
> **(5)** Pelo Problema 2.1: `M ⊆ M* ⊆ M'` com `Log(M*) = Log(M')` (7) e
> `M' ⊨ T_PV ∧ ¬φ ∈ SAT`. "`M*` satisfies the last axiom of `S`:
> `M* ⊨ ∀i<m (¬α_i) ∈ SAT` **(8)** **as it preserves the `Σ^b_1(PV)`-properties from `M`**."
> Seja `σ ∈ M'` atribuição aos átomos `r` falsificando `φ` em `M'`; `σ = (σ_i)_{i<m}`,
> logo "exist `i_0 < m` com `M' ⊨ σ_{i_0} : P ⊢ α_{i_0}`. **But by (7) `i_0` is also
> already in `M*`** and hence by (8) we get `M' ⊨ (¬α_{i_0}) ∈ SAT`.
> That contradicts **`Ref_P`**: `x : P ⊢ y → (¬y) ∉ SAT`, which holds in `M'` as it
> models `T_PV`."

**Tradução em palavras (P):** suponha `NP = coNP`, (ST) e (2.1) afirmativo. Escolha um
strong pps p-bounded que satisfaça (ST). Se a teoria `S` ("`α` é disjunção disjunta
provada por `π`, mas **nenhum** pedaço é tautologia") fosse inconsistente, **KPT
extrairia** da inconsistência estratégias p-time do aluno — i.e., um solucionador de DD_P
em **rodadas constantes** — refutando (ST). Logo `S` tem modelo `M`. Nesse `M`, a fórmula
universal `A_Q` (verdadeira porque p-boundedness ⇒ toda tautologia tem prova curta) dá
`M ⊨ Q ⊬ φ(r)`. O Problema 2.1 estende `M` a `M'` que **falsifica `φ`**, mantendo `M*` com
os mesmos fatos `Σ^b_1` (⇒ (8) sobrevive) e os mesmos comprimentos (⇒ `i_0 ∈ M*`). Aí `M'`
veria "σ_{i_0} prova α_{i_0}" **e** "¬α_{i_0} ∈ SAT", contradizendo `Ref_P`, válido em `M'`
por `T_PV`. Contradição ⟹ `NP ≠ coNP`.

**Mecanismo de `i_0 ∈ M*` (P, leitura):** o artigo escreve literalmente "by (7) `i_0` is
also already in `M*`". O salto usa `Log(M) = {|m| : m ∈ M}`: `|i_0| ∈ Log(M') = Log(M*)`,
isto é, `M*` contém um elemento do mesmo comprimento de `i_0`; para concluir `i₀ ∈ M*`
pressupõe-se que as estruturas `L_PV` são **fechadas para strings mais curtas** (downward
closed) — convenção usual mas **não explicitada no artigo**; registre-se como lacuna de
detalhe a confirmar.

### 1.13 Observação final — strong feasible disjunction property **(A✔)**
> "Note that the proof yields a somewhat stronger conclusion that **in no strong `P` can
> a proof of some disjunct in a disjoint disjunction be polynomially bounded in size in
> terms of a proof of the disjunction** (i.e. **the strong feasible disjunction property
> fails for strong proof systems**, cf. [12])."

**Tradução:** não há constante `c` com: `π : P ⊢ ⋁̇_{i<m} α_i` ⟹ ∃`i` com `α_i ∈ TAUT`
e prova `P` de `α_i` de tamanho `≤ |π|^c`. "Prova curta do todo ⟹ prova curta de uma
parte" **quebra** para strong pps. É a formulação "feasible" do conteúdo do Teorema 4 —
e, em palavras, **é exatamente o que impede DD_P de cair em `O(1)` rodadas**. **(P)**

---

## 2. Precisão do modelo S-T: quantas rodadas para DD_P? E que classe de complexidade?

### 2.1 Número de rodadas — resposta: **até `m` rodadas** (`m ≤ |α| ≤ n`): polinomial, **não** constante

**O que o artigo diz (A✔):** **nada de número exato** — apenas:
"S then proposes his second candidate solution, using also the counter-example he learned
in the first round, and the computation proceeds **analogously for some number of
rounds**." Não há cota de rodadas escrita no texto. (Isto resolve o item 7 do
`CONTEXTO_COMUM.md`: **não há número literal a citar**; a cota abaixo é derivação nossa.)

**Algoritmo e cota (P):**
1. `S` mantém um vetor "já refutados" e propõe o **menor índice `i` ainda não refutado**.
2. Se `α_i ∈ TAUT` → `T` aceita → fim.
3. Senão `T` devolve atribuição falsificante de `α_i` (`T` é **arbitrária**; achar essa
   atribuição é NP-difícil, mas o professor não tem limite de tempo). `S` marca `i` e
   repete. `S` pode ainda **testar de graça** outros `j`: estende a atribuição recebida aos
   átomos de `α_j` (valores arbitrários) e avalia `α_j` em tempo p-time — se falsa, `j`
   também sai. Cada rodada elimina **pelo menos um** índice.
4. Cada movimento de `S` é p-time (varredura de `m ≤ n` bits) → `S ∈ P`. ✔

**Consequências (P):**
- **Banco de dados do aluno:** um contra-exemplo para `α_i` só menciona átomos de `α_i`;
  como são **disjuntos**, ele **não informa nada** sobre `α_j` (`j≠i`) além de "o índice
  `i` está descartado" (e o teste-barato do passo 3). Logo, no **pior caso** cada rodada
  elimina exatamente um índice.
- **Cota:** `DD_P ∈ ST[P, t(n)]` com **`t(n) ≤ m ≤ |α| ≤ n`** — i.e. **`O(n)` rodadas**,
  polinomial, **não constante**.
- **Por que é exatamente o ponto do artigo:** DD_P é *fácil* no modelo S-T; a dificuldade
  **não** é computacional, é de **profundidade de interação**. A hipótese **(ST)** postula
  que **nenhum** aluno p-time consegue `O(1)` (perguntas independentes do tamanho da
  entrada) para algum strong pps. Portanto:
  - "DD_P ∈ ST[P, O(1)]" é **falso sob (ST)**;
  - "DD_P não é solúvel em S-T" também é **falso** (o algoritmo acima existe);
  - `O(n)` vs `O(1)` é a fronteira nítida; `Lema 1` permite trocar DD_P por D_P, `Lema 2`
    ancora (ST) em one-way permutations fortes.
- **Nota (P):** o artigo diz explicitamente "**`m` is bounded by the size of the
  formula**" — é a hipótese que permite converter "≤ `m` rodadas" em cota polinomial na
  entrada.

### 2.2 Classe de complexidade: o que está certo e o que está errado na afirmação do usuário

A afirmação "**DD_P é um problema de busca total Σ₂ᵖ**" mistura três coisas. Separando:

| # | Afirmação | Veredito |
|---|-----------|----------|
| (i) | "DD_P é um problema `Σ^p_2`" (**rótulo**) | **Correto e é a terminologia do artigo (A✔):** abstract — "the following **`Σ^p_2` search problem `DD_P`**"; Seção 1 — `ST[F,t(n)]` = "class of **total `Σ^p_2` search problems**". **Não corrigir o rótulo.** |
| (ii) | "a classe `Σ₂ᵖ` vem da forma do critério de aceitação **`∀y ¬A(x,i,y)` (dois blocos de quantificadores)**" | **Errado — corrigir.** `∀y ¬A(x,i,y)` tem **UM** bloco sobre matriz p-time: é `Π^P_1 = coNP`, **não** `Σ^p_2`. O artigo diz justamente que o critério "**starts with a universal quantifier**". |
| (iii) | "verificar `α_i ∈ TAUT` é coNP" | **Correto (A✔/P):** `A(α_i,y)` (avaliação) é p-time ⟹ `∀y¬A` é coNP, e é **coNP-complete** para entradas válidas (redução de TAUT). |
| (iv) | "DD_P é um problema de busca total" | **Correto (A✔)** — totalidade garantida pelo argumento da §1.3, e vale também internamente a modelos não-padrão (ver §3(a)). |

**Formulação correta (P):**
> `DD_P` é um problema de busca **total** cuja **relação-resposta**
> `R(x,i) ⇔ Valid(x) ∧ (α_i ∈ TAUT)` está em **coNP** (`Π^P_1`) e é coNP-complete sobre
> entradas válidas. Como `coNP ⊆ Σ^p_2`, `DD_P` é legitimamente chamado — e o artigo o
> chama — de "**`Σ^p_2` search problem**", e é por isso que `Σ^p_2` aparece na **definição
> de `ST[F,t(n)]`** (envelope de classe, não complexidade exata). Os **dois blocos**
> `∃i ∀y` aparecem **só no nível da sentença de totalidade/aceitação do problema como um
> todo** (`∃i<m ∀y ¬A`), não na verificação de um candidato. `DD_P` **não** é
> `Σ^p_2-complete`.

---

## 3. Redução ao aritmético (questão 2)

### 3(a) A sentença de totalidade de DD_P em `T_PV` / `S^1_2(PV)`

Notação: `u = ⟨π,α⟩`, `α = ⋁̇_{i<m} α_i`, `k_i = |α_i|`, `A(α_i,y)` = avaliação p-time de
`α_i` na atribuição `y`.

```
Valid_P(u) := Prf_P(π,α) ∧ Disj(α)                      (predicado PV, p-time)
Tot_DD     := ∀u [ Valid_P(u) → ∃ i<m  ∀ y<2^{k_i} ¬A(α_i, y) ]
```
Prénexa com `u` livre: `∃i<m ∀y<2^{k_i} [ ¬Valid_P(u) ∨ ¬A(α_i,y) ]` — matriz
quantifier-free, **dois blocos limitados** ⟹ **`Tot_DD` é `Σ^b_2`**; fechada por `∀u`
(unbounded), `∀∃∀` = `Π_3` na hierarquia aritmética. **(P)**

**Está em `T_PV`? Resposta: sim (como consequência de sentenças universais que estão em
`T_PV`).** **(P), com premissas (A✔):**
1. `T_PV` é a **teoria universal verdadeira** em `L_PV` (§1.0) ⟹ **`Ref_P`:
   `x : P ⊢ y → (¬y) ∉ SAT`** (isto é, a correção de todo pps) **está em `T_PV`** — o
   artigo diz explicitamente que "it will always be **sound** as that is expressible by a
   universal `L_PV`-formula". ✔
2. Existe função PV `ext(y_i, α, i)` que **estende** uma atribuição falsificante de `α_i`
   (átomos disjuntos, resto arbitrário) a uma falsificante de `α`; a correção
   `¬A(α_i,y_i) → ¬A(α, ext(...))` é **quantifier-free** e vale. ✔ **(P)**
3. Logo a sentença **universal**
   `∀π,α,i,y_i [ (Prf_P(π,α) ∧ Disj(α)) → (¬A(α_i,y_i) → ¬∀z A(α,z)) ]`
   é verdadeira e universal ⟹ **está em `T_PV`**; juntando com `Ref_P` (também universal),
   `T_PV ⊢ ∀π,α,i,y_i [ Valid_P(π,α) → A(α_i,y_i) ]`.
4. Não-vazio: se `m = 0`, `α = ⊥` (disjunção vazia) e `Prf_P(π,⊥)` é refutado por
   `Ref_P`; logo `Valid_P → m ≥ 1`, e da universal acima obtém-se `∃i<m ∀y A(α_i,y)`.
   **`T_PV ⊢ Tot_DD`.** (Segue também em `S^1_2(PV)`, que contém `T_PV`.) **(P)**

**Conclusões importantes (P):**
- A **totalidade de DD_P é barata**: a redução de testemunha usa **uma única
  testemunha** (extensão/restrição), **não** precisa de **BB**. A pergunta "a totalidade
  é formalizável?" tem resposta **positiva e elementar**.
- **BB não é o que falta aqui.** BB (sharply bounded collection) é preciso **noutro
  sítio**: para trocar os quantificadores internos entre (3) `∃x,y ∀i<m ¬A_b(x,i,(y)_i)`
  e (4) `∃x ∀i<m ∃y_i ¬A_b(x,i,y_i)` na análise dos geradores (item 11 do contexto,
  **A✔**), e **para o preservamento `Σ^b_1`** na construção via modelos de `S^1_2` (§1.11,
  **A✔**).
- Onde está a dificuldade, portanto, **não** é formalizar DD_P, é a **constância de
  rodadas** (hipótese (ST)) e o **preservamento `Σ^b_1` + `Log`** (Problema 2.1). **(P)**
- Cuidado de leitura: em modelo **não-padrão**, "`α_i ∈ TAUT`" significa `M ⊨ ∀y A`
  (`y` percorre o universo de `M`) — a totalidade vale *no modelo*, que é o que o Teorema 4
  precisa; para fórmulas **padrão** isso dá tautologia padrão apenas se `M` contiver as
  strings padrão (convenção usual). **(P/C)**

### 3(b) A hipótese de extensão de modelos (Problema 2.1) — os 3 requisitos

Dados `M ⊨ T_PV` não-padrão e `φ` proposicional verificando a **Condition 1 do Teorema
3** ("`φ` não tem prova em `M` em nenhum pps"), pede-se `L_PV`-estruturas `M ⊆ M* ⊆ M'`:

1. **Preservação `Σ^b_1`:** `M*` satisfaz **todas** as `Σ^b_1(PV)`-propriedades de
   elementos de `M`. *Papel (P):* transporta de `M` para `M*` o último axioma de `S`
   (`∀i<m (¬α_i) ∈ SAT` é `Σ^b_1`: testemunha = atribuição, matriz p-time) — é a eq. (8)
   do passo (5).
2. **Verdade nova:** `M' ⊨ T_PV` **e** `(¬φ) ∈ SAT`. *Papel (P):* permite **falsificar
   `φ`** em `M'` e extrair, da falsificação `σ`, um índice `i_0` com prova de `α_{i_0}`.
3. **Mesmos comprimentos:** `Log(M*) = Log(M')`, com `Log(M) = {|m| : m ∈ M}`. *Papel
   (P):* transporta de `M'` para `M*` o **índice** `i_0` (e os tamanhos), fechando a
   contradição com `Ref_P`.

Remover qualquer um dos três e o passo (5) do Teorema 4 quebra. **(P)**
O artigo admite **relaxamentos**: classe universal de modelos (contáveis ou
recursivamente saturados); e preservar só `∀i∃y B(x,i,y)` com `i` sharply bounded,
`y` bounded, `B` **aberta**. **(A✔)**

### 3(c) Cadeia exata de implicações

```
 (Problema 2.1) AFIRMATIVO ──┬── (ST) ───────► NP ≠ coNP      [Teorema 4, A✔]
                             │
 (Problema 2.1) NEGATIVO ────────────────────► P ≠ NP         [rodapé 2, A✔]
```
Por contrapositiva:
- `NP = coNP` ⟹ **ou** (2.1) negativo **ou** ¬(ST); em particular `NP = coNP ∧ (ST)` é
  **inconsistente**.
- `P = NP` ⟹ **(2.1) tem resposta afirmativa** (contrapositiva literal do rodapé 2);
  somando o Teorema 4: `P = NP ∧ (ST)` ⟹ `NP ≠ coNP`, mas `P = NP` ⟹ `NP = coNP` ⟹
  contradição. **Consequência nossa (P): `(ST) ⟹ P ≠ NP`.**
- **Não trocar as conclusões:** `(2.1)AF ∧ (ST) ⟹ NP ≠ coNP` é **mais forte** que
  `¬(2.1) ⟹ P ≠ NP`; `NP ≠ coNP` não implica `P ≠ NP` nem vice-versa.

**Rodapé 2 — transcrição literal (A✔):**
> "If `f` is a **p-time algorithm that finds a satisfying assignment for all satisfiable
> formulas** then this fact, **being a universal statement, would be in `T_PV`** and
> hence **`T_PV` would prove all true bounded formulas**. `T_PV` proves `S^1_2(PV)`."

**Reconstrução do argumento (P, a partir do texto literal):**
1. `P = NP` ⟹ `SAT ∈ P` ⟹ existe `f` p-time que, para **toda** fórmula satisfatível,
   devolve atribuição satisfatória.
2. A correção de `f` pode ser escrita como sentença **universal** de `L_PV`
   (`∀ψ,y [ y ⊨ ψ → f(ψ) ⊨ ψ ]`, matriz quantifier-free; `f` é um símbolo de função de
   `L_PV`); sendo verdadeira, **está em `T_PV`** (teoria universal verdadeira, §1.0).
3. Por **reduções p-time de Cook**, toda fórmula limitada verdadeira se comunica com
   `SAT` por uma correção igualmente universal ⟹ `T_PV` prova **todas as fórmulas
   limitadas verdadeiras** (literal: "hence `T_PV` would prove all true bounded
   formulas"), em particular — segundo o rodapé — "`T_PV` proves `S^1_2(PV)`".
4. Se todo `M ⊨ T_PV` é (também) modelo de `S^1_2(PV)` (que **satisfaz `BB` para
   fórmulas abertas**), a construção de [14] (§1.11) **aplica-se a todo `M`**: dá `M'`
   falsificando `φ` **e** preservando `Σ^b_1`; e o forcing de [7, Thm.9.4.2] dá
   `Log(M') = Log(M)`. Com `M* := M` (preservação `Σ^b_1` trivial) e
   `Log(M) = Log(M')`, os três requisitos do Problema 2.1 estão satisfeitos ⟹
   **resposta afirmativa**.
5. Contrapositiva: **resposta negativa ⟹ `P ≠ NP`.** ✔ **(A✔)**

*Reservas (P):* (α) o salto 3→4 ("todas as fórmulas limitadas verdadeiras ⟹ `S^1_2(PV)`
⟹ a construção de [14] aplica-se") é a parte que o rodapé **comprime**; reproduzindo-o
literalmente é isso que ele afirma, mas a redação "`T_PV` proves `S^1_2(PV)`" é ambígua
(pode ler-se como premissa conhecida ou como conclusão sob a hipótese). (β) O ponto
`M* := M` é a minha leitura do porquê de a resposta afirmativa ser "fácil" sob `P=NP`;
confirmar se o autor usa `M*=M` ou outro arranjo.

### 3(d) Papel exato de BB, preservação `Σ^b_1`, Log-preservation e KPT

| Instrumento | Papel exato | Fonte |
|---|---|---|
| **BB** (sharply bounded collection, [3] Buss) | Esquema para fórmulas **abertas** de `L_PV` que troca `∃y_i` e `∀i` — é o que converte (4) `∃x ∀i<m ∃y_i ¬A_b(x,i,y_i)` em (3) `∃x,y ∀i<m ¬A_b(x,i,(y)_i)`. Segundo **Cook–Thapen [6]** (título real: *The strength of replacement in weak arithmetic*, TOCL 7(4), 2006), **não é provável em `T_PV` "a menos que fatoração não seja difícil"**; e **acrescentá-lo a `T_PV` invalida a análise de (1) de [8,12]** ("the KPT theorem of [16] does not apply in any usable form to this non-universal theory"). **Também** é o que garante que `M'` preserva `Σ^b_1` na construção via `S^1_2` (§1.11: "BB for open `Σ^b_1`-formulas, a consequence of `S^1_2`"). **É, portanto, o motivo do paper existir:** o método do paper é um **passeio em torno de BB**, trocando prova-teoria por teoria dos modelos. | **(A✔)** |
| **Preservação `Σ^b_1`** (req. 1 de 2.1) | Transporta de `M` para `M*` o axioma `∀i<m (¬α_i) ∈ SAT` (eq. (8)); sem ele não há contradição com `Ref_P`. **Não** é dado por `Log`-equality — `Log` só controla comprimentos, não verdade. | (A✔)+(P) |
| **Log-preservation** (req. 3) | `Log(M*) = Log(M')`, `Log(M)={|m|:m∈M}`: transporta de `M'` para `M*` o **índice** `i_0` ("by (7) `i_0` is also already in `M*`"). Arranjo-se `Log(M')=Log(M)` via **forcing** [7, Thm.9.4.2], mas "**with an additional requirement on `M`**" — detalhe que o Problema 2.1 precisa remover. | (A✔)+(P) |
| **KPT** ([16] Krajíček–Pudlák–Takeuti, APAL 52, 1991) | Motor do passo (2): de uma **prova de inconsistência** de `S` (aplicada aos **três primeiros axiomas**, i.e. `T_PV` + "`α` é disjunção disjunta" + "`π : P ⊢ α`"), KPT **extrai funções p-time dos movimentos do aluno** que resolvem `DD_P` em **rodadas constantes** ⟹ viola (ST). Ou seja: **KPT = "inconsistência ⟹ solucionador `O(1)`"**; (ST) = "não existe solucionador `O(1)`" ⟹ `S` **tem** modelo não-padrão `M`. | (A✔)+(P) |

**Síntese (P):** `KPT` fornece a *existência* do modelo `M`; `BB` (indisponível em
`T_PV`) forneceria o *preservamento*; o Problema 2.1 é exatamente a pergunta "dá para ter
o preservamento **sem** BB?". `Log` fecha a contagem; `Ref_P` dá a contradição.

---

## 4. Correções à formalização do usuário + enunciado corrigido

### 4.1 Lista de correções
1. **pps ≠ função.** Trocar "`P : {0,1}* → TAUT`, p-time e sobrejetora" pela **relação
   binária** `P(x,y)` p-time com `∃x P(x,y) ⇔ y ∈ TAUT` (Cook–Reckhow), notação
   `σ : P ⊢ β`. (§1.1)
2. **Rótulo `Σ₂ᵖ`: mantiver; justificativa: corrigir.** "DD_P é um problema de busca
   total `Σ₂ᵖ`" **coincide com o artigo** (abstract: "the `Σ^p_2` search problem DD_P").
   Mas **não** se justifique dizendo que `∀y ¬A(x,i,y)` tem *dois* blocos: esse critério
   tem **um** bloco e é **coNP** (`Π^P_1`); a expressão "starts with a universal
   quantifier" é do próprio artigo. `Σ₂ᵖ` é o **envelope** de `ST[F,t(n)]`
   (`coNP ⊆ Σ₂ᵖ`), e os dois blocos `∃i∀y` valem para a **sentença de totalidade**.
   (§2.2)
3. **Nº de rodadas.** DD_P **é** solúvel em S-T; o artigo **não** dá número — a cota
   correta (nossa) é **`≤ m ≤ |α| ≤ n` rodadas** (`O(n)`: polinomial, **não** `O(1)`).
   Nunca afirmar "DD_P ∈ ST[P,O(1)]" (falso sob (ST)) nem "DD_P não é solúvel em S-T"
   (falso). (§2.1)
4. **`strong pps` vs `pps`.** (ST) é sobre **strong** pps (`EF` + axiomas tautológicos
   p-time); registrar que todo pps é p-simulado por um strong e que a conjectura é
   para **todo** strong = **para EF**.
5. **Falta a hipótese sobre `M`.** O Problema 2.1 supõe `M ⊨ T_PV` **não-padrão** com `φ`
   verificando a **Condition 1 do Teorema 3**. Sem isso, a pergunta não se coloca.
6. **Preservação é de `M*`, não de `M'`**; e `Log` é igual entre `M*` e `M'` (**não**
   entre `M` e `M'` — embora `Log(M')=Log(M)` seja arranjável via forcing, "com uma
   condição adicional em `M`").
7. **Não confundir as conclusões.** `(2.1)AF ∧ (ST) ⟹ NP ≠ coNP` (Thm 4) **vs**
   `¬(2.1) ⟹ P ≠ NP` (rodapé 2).
8. **O artigo assume (2.1) afirmativo** — é hipótese de trabalho, não resultado.
9. **`T_PV` é a teoria universal verdadeira em `L_PV`** neste artigo (§1.0). Formalizar
   algo "em `T_PV`" significa: mostrar que é **sentença universal verdadeira** (ou
   consequência de uma). Isto **simplifica** a pergunta 3(a): a totalidade de DD_P está
   formalizada, é `Σ^b_2` e é teorema de `T_PV`. Não é ela o ponto aberto.
10. **BB não é necessário para a totalidade de DD_P** (só para o *swap* de quantificadores
    (3)/(4) e para o preservamento `Σ^b_1`). Não misturar os dois usos.

### 4.2 Enunciado corrigido, limpo e pronto para publicação **(A✔ corrigido por (P))**

> **Definição (pps).** Uma relação binária `P(x,y)` decidível em tempo polinomial é um
> *sistema de prova proposicional* se `∃x P(x,y)` é verdadeiro exatamente para
> `y ∈ TAUT`; escrevemos `σ : P ⊢ y`. `P` é *strong* se `P = EF + S` com `S ⊆ TAUT`
> decidível em p-time; todo pps é p-simulado por um strong.
>
> **Definição (disjunção disjunta, `DD_P`).** `α = ⋁̇_{i<m} α_i` se nenhum par
> `α_i,α_j` (`i≠j`) compartilha átomo (`m ≤ |α|`). Dado `u = (π,α)` com `π : P ⊢ α`,
> `DD_P(u)` pede um `i<m` com `α_i ∈ TAUT`. `DD_P` é **total** (correção de `P` +
> disjunção dos átomos; formalização: `Σ^b_2`, teorema de `T_PV` — §3(a)) e sua
> **relação-resposta está em coNP**; por isso o artigo o chama de "`Σ^p_2` search
> problem".
>
> **Definição (modelo S-T).** `ST[F,t(n)]` é a classe dos **problemas de busca totais
> `Σ^p_2`** resolvíveis em `t(n)` rodadas de um jogo aluno–professor, em que os movimentos
> do aluno são computados por algoritmo de `F` e o professor (arbitrário) aceita ou devolve
> contra-exemplo. `DD_P` é soluvel nesse modelo em **`≤ m ≤ n` rodadas** (p-time), mas a
> hipótese abaixo nega a resolução em **`O(1)`** rodadas.
>
> **Hipótese (ST).** Existe strong pps `P` com `DD_P ∉ ST[P,O(1)]` (`P` denota também a
> classe de algoritmos p-time). Conjectura-se que vale para todo strong pps, equivalente
> a valer para **EF**. Lema 1: idem para `D_P`. Lema 2: vale se existir permutação one-way
> forte.
>
> **Problema 2.1.** Seja `M ⊨ T_PV` não-padrão e `φ` proposicional sem prova em `M` em
> nenhum pps (Condition 1 do Teorema 3). Existem `L_PV`-estruturas `M ⊆ M* ⊆ M'` com
> (i) `M*` preserva **todas** as `Σ^b_1(PV)`-propriedades de elementos de `M`;
> (ii) `M' ⊨ T_PV` e `(¬φ) ∈ SAT`;
> (iii) `Log(M*) = Log(M')`?
> *(Afirmativa + `(ST)` ⟹ `NP ≠ coNP` [Teorema 4]. Negativa ⟹ `P ≠ NP` [rodapé 2].)*
>
> **Teorema 4 (forma).** (2.1 afirmativo) + (ST) ⟹ `NP ≠ coNP`.
> **Observação final.** Para nenhum strong `P` a prova de um disjuncto numa disjunção
> disjunta é polinomialmente limitada pelo tamanho de uma prova da disjunção — a
> **strong feasible disjunction property** falha para strong pps.

---

## 5. Contribuição própria **(C)** — formulações alternativas do Problema 2.1

*Contexto (A✔): o próprio artigo aponta "constructing extensions … introducing no new
lengths is very close to constructing **expansions of non-standard finite structures**"
(citando **Ajtai [1,2]**) e "the possibility to use **Boolean-valued models** discussed
at the end of **[9]**". As formulações abaixo desenvolvem essas pistas em enunciados
precisos — o que é (C), mesmo que a direção seja (A).*

**(C1) Via expansões de estruturas pseudofinitas (à la Ajtai).**
Reformular (2)+(3): pedir que `M'` seja uma **expansão pseudofinita** de `M` (todo sub
conjunto *finito* de `Th(M')` é satisfatível em `M`; cf. Ajtai, *Σ¹₁-formulas on finite
structures*). Como fórmulas `Σ^b_1` com parâmetros de `M` são detectáveis por aproximações
finitas, a pseudofinitude daria a preservação `Σ^b_1` **quase de graça**, reduzindo o
Problema 2.1 a:
> *Existe expansão pseudofinite `M'` de `M` com `¬φ ∈ SAT` e `Log(M') = Log(M)`?*
Teste a fazer: pseudofinitude **não** preserva automaticamente `Log` — verificar se o
forcing de [7, Thm.9.4.2] é compatível com a condição de pseudofinitude (é aqui que a
"additional requirement on `M`" do artigo pode ser a mesma restrição).

**(C2) Via modelos de valores booleanos (remetendo a [9]).**
Substituir a cadeia `M ⊆ M* ⊆ M'` por um **forcing booleano** `𝔹` sobre `M` que falsifica
`φ`. A preservação `Σ^b_1` vira **continuidade monótona** dos valores de verdade das
fórmulas `Σ^b_1` com parâmetros de `M`; `Log(M*) = Log(M')` vira **igualdade de suportes**
(`support`). A pergunta vira:
> *Existe um forcing booleano que falsifica `φ` sem mudar suportes nem valores `Σ^b_1`?*
Vantagem: condições/folga vêm embutidas (é a técnica por trás de [7, Thm.9.4.2] e do
"Boolean-valued models discussed at the end of [9]"). Nesta formulação `M*` é o
"andaim" e `M'` é o quociente por um ideal — as três condições tornam-se **uma só
propriedade de continuidade**.

**(C3) `Log`-preservação como *consequência*; `Σ^b_1` reduzido ao subfragmento; e
formulação por realização de tipos.**
- **(C3a)** Conjectura: (iii) `Log(M*) = Log(M')` é **consequência** de (i)+(ii) + o
  arranjo do forcing de [7, Thm.9.4.2] (cuja construção **já** produz `Log`-equality) —
  i.e., dá para **remover** a condição (iii), deixando o Problema 2.1 com **duas**
  condições. Teste: rastrear onde a prova do Teorema 4 usa `Log` *independentemente* de
  (i). Se em nenhum sítio, (iii) é redundante.
- **(C3b)** Conjectura dual: o requisito (i) pode ser trocado pelo subfragmento
  **`∀i∃y B` (i sharply bounded, y bounded, B aberta)** — o que o artigo já admite — e
  então **re-derivado** a partir desse subfragmento + (iii). Se verdadeiro, (1) e (3)
  tornam-se **equivalentes** e o problema fica com um só requisito de preservação.
- **(C3c)** Formulação sintética única (a que proponho para publicação):
  > *Seja `M ⊨ T_PV` não-padrão e `φ` sem prova em `M`. Existe uma extensão `M' ⊇ M` com
  > `M' ⊨ T_PV ∧ ¬φ ∈ SAT` cujo **`Σ^b_1`-tipo sobre `Log(M)`** coincide com o de `M`
  > (mesmos comprimentos e mesmas verdades `Σ^b_1` com parâmetros de `M`)?*
  Isto **unifica (i) e (iii)** num só enunciado de **realização de tipos** (`type
  realization`) na linguagem `Σ^b_1` — e elimina explicitamente o `M*` (conjectura
  auxiliar: `M* = M` basta; se falso, `M*` é só "o andaim de suportes" da formulação C2).

**Marcação:** (C1)–(C3) são formulações/ideias **não** demonstradas; nenhuma delas está
no artigo nesta forma. A verificação (i)→(iii) etc. é trabalho futuro da equipe.

---

## 6. Pendências (atualizadas após a conferência do artigo)
- [x] Rodapé 2 — transcrição literal obtida (§3(c)); a **reconstrução** 1–5 é **(P)** e
      a leitura da frase "`T_PV` proves `S^1_2(PV)`" continua ambígua (α/β em §3(c)).
- [x] Número de rodadas — **o artigo não dá número** ("some number of rounds"); cota
      `≤ m ≤ |α|` é **(P)**.
- [x] Referência **[9]** identificada (Krajíček 2016, *Expansions of pseudofinite
      structures…*); **[1],[2]** = Ajtai 1983/1988; **[6]** = Cook–Thapen, *The strength of
      replacement in weak arithmetic*, TOCL 7(4), 2006.
- [ ] Confirmar o mecanismo "`i_0 ∈ M*` by (7)" (fechamento para strings mais curtas) —
      §1.12, lacuna de detalhe.
- [ ] Confirmar se, sob `P = NP`, o autor toma `M* := M` (§3(c), reserva β).

# Equipe C — Disjunção viável e `DD_P` para sistemas fracos (e não só)

**Escopo desta nota.** Mapear e, quando possível, provar/refutar a propriedade de
disjunção viável (*feasible disjunction property*) e o problema de busca `DD_P`
para sistemas de prova, começando pelos fracos. Idioma: português. Convenções de
marcação, conforme as regras da equipe:

- **(A)** = fato extraído do artigo de Krajíček (arXiv:2506.20221v4) ou de outra
  fonte publicada verificada (com referência);
- **(B)** = demonstração própria desta nota (com prova escrita);
- **(C)** = conjectura, ideia de trabalho ou status aberto discutido honestamente.

**Fontes primárias verificadas** (além do artigo, cujo texto integral foi lido na
versão HTML do arXiv — citações literais abaixo são dessa versão):

- **[K97]** J. Krajíček, *Interpolation theorems, lower bounds for proof systems,
  and independence results for bounded arithmetic*, J. Symbolic Logic 62 (1997),
  457–486. (Resumo verificado: deriva "feasible interpolation theorems" para
  (a) resolução, (b) um sub-sistema de LK, (c) *linear equational calculus*,
  (d) *cutting planes*.)
- **[P97]** P. Pudlák, *Lower bounds for resolution and cutting plane proofs and
  monotone computations*, J. Symbolic Logic 62 (1997), 981–998.
- **[Gar24]** M. Garlík, *Failure of Feasible Disjunction Property for k-DNF
  Resolution and NP-Hardness of Automating It*, CCC 2024 (LIPIcs 300, 33:1–33:23);
  preprint arXiv:2003.10230 / ECCC TR20-037 (texto integral verificado).
- **[AM20]** A. Atserias, M. Müller, *Automating resolution is NP-hard*, FOCS 2019 /
  J. ACM (2020).
- **[Pap26]** T. Papamakarios, *Feasible disjunction for random resolution*,
  ECCC TR26-154 (2026) (texto integral verificado).
- **[Pap24]** T. Papamakarios, *Depth-d Frege Systems Are Not Automatable Unless
  P = NP*, CCC 2024 (LIPIcs 300, 22:1–22:17).
- **[Ale04]** M. Alekhnovich, *Non-automatizability of bounded-depth Frege
  proofs*, Computational Complexity 13 (2004), 47–68.
- **[Pud03]** P. Pudlák, *On reducibility and symmetry of disjoint NP pairs*,
  TCS 295 (2003), 323–339 (origem, com [Rud97] S. Rudich, RANDOM 1997, da noção
  de disjunção viável, segundo [Pap26]).
- **[HKT24]** P. Hubáček, E. Khaniki, N. Thapen, *TFNP intersections through the
  lens of feasible disjunction*, ITCS 2024 (LIPIcs 287, 63:1–63:24);
  **[LPR24]** Y. Li, W. Pires, R. Robere, *Intersection classes in TFNP and proof
  complexity*, ITCS 2024 (LIPIcs 287, 74:1–74:22).
- **[K19]** J. Krajíček, *Proof Complexity*, CUP 2019 (caps. 5.7, 17.7, 18);
  **[K25]** J. Krajíček, *Proof complexity generators*, LMS Lecture Notes 497,
  CUP 2025 (= [12] do artigo); **[K20]** J. Krajíček, *A limitation on the KPT
  interpolation*, LMCS 16(3), 2020 (= [11] do artigo).
- **[Hak85]** A. Haken, *The intractability of resolution*, TCS 38 (1985) 141–147
  (cotas exponenciais de resolução para o princípio da casa dos pombos).
- **[BKT14]** S. Buss, L. Kołodziejczyk, N. Thapen, *Fragments of approximate
  counting*, JSL 79 (2014) 496–525 (resolução aleatória).

---

## 0. Três noções que NÃO se confundem (e o que cada uma implica)

A palavra "disjunção viável" circula com dois significados diferentes no
literatura e no artigo. Para evitar confusões nesta nota:

**(i) `DD_P ∈ P`** — existe algoritmo **determinístico polinomial** que, dado
`(π, ⋁̇_{i<m} α_i)` com `π : P ⊢ ⋁̇_i α_i`, devolve `i` com `α_i ∈ TAUT`.

**(ii) Propriedade de disjunção viável (FDP, "fraca" no sentido de [Gar24])** —
existe polinômio `p` tal que: sempre que `A ∨ B` (com `A`, `B` sem átomos em
comum) tem prova `P` de comprimento `t`, então **`A` ou `B` tem prova `P` de
comprimento ≤ p(t)`**. Versão "forte" (a do artigo, chamada *strong feasible
disjunction property*): o mesmo com a prova do disjunto limitada por poli no
tamanho da **prova da disjunção** apresentada. A diferença crucial: (ii) é uma
afirmação **existencial sobre comprimentos de prova**, (i) é uma afirmação sobre
um **algoritmo que encontra o índice**. Nenhuma implica a outra a priori.

**(iii) `DD_P ∈ ST[P, O(1)]`** — resolvível no modelo aluno–professor
(Krajíček–Pudlák–Sgall, [15] do artigo) com aluno p-time e **número constante**
de rodadas. Distinguir de **`DD_P ∈ ST[P, poly]`** (rodadas polinomiais).

**Proposição 0.1 (B).** As noções (i) e (ii) são **independentes no que se
sabe hoje**: nenhuma das direções `(i) ⟹ (ii)` e `(ii) ⟹ (i)` é conhecida
como válida, nem como falsa. Os dados de fronteira (todos verificados):
(a) resolução tem (i) — Teorema 4.3 abaixo — e (ii) e interpolação viável;
(b) resolução aleatória com erro dinâmico tem (ii) ([Pap26]) mas (i) é
**aberto** ([Pap26] explicita que o interpolante do argumento "não é
computável em tempo polinomial") — logo (i) não é conhecido como implicado
por (ii); (c) `Res(k)` (`k ≥ 2`) **não** tem (ii) ([Gar24], Teorema 1) e (i)
é **aberto** — logo (ii) não é conhecido como implicado por (i); (d) para
strong pps, (ii)-forte **falha** (observação final do artigo, sob as hipóteses
do Teorema 4) e (iii) falha para `O(1)` rodadas sob (ST), enquanto (i) falha
para o `P` nomeado por (ST) (Proposição 0.2). Adicionalmente, (A): interpolação
viável é preservada para baixo sob p-simulação, mas **FDP não é** ([Pap26]) —
mais um indício de que (i)/FI e (ii) são noções de "natureza" diferente.

**Proposição 0.2 (A).** `(ST)` diz: existe strong pps `P` com
`DD_P ∉ ST[P, O(1)]`. Como algoritmo p-time = aluno com **0/1 rodadas**:

> `(ST) ⟹ ∃` strong pps `P` com `DD_P ∉ P`.

O artigo afirma ainda (texto verificado): *"we do think that the hypothesis is
true for all strong proof systems (which is equivalent to saying that it holds
for EF, the Extended Frege proof system)"*. Ou seja: **a crença é de que
`DD_EF ∉ P`** (e `DD_P ∉ P` para todo strong pps), condicionalmente a (ST), que
por sua vez é verdadeira se existir permutação one-way dura para circuitos
p-size ([K20], citado como Lemma 2 no artigo).

**Proposição 0.3 (B).** `DD_P ∈ ST[P, O(m·poly)] ⊆ ST[P, poly]` vale para
**todo** pps `P`, sem hipótese nenhuma. Estratégia trivial do aluno: propor
`i_1`; se a professora devolve atribuição falsificando `α_{i_1}`, essa atribuição
— por causa da disjunção disjunta — só usa átomos de `α_{i_1}`, então o aluno
descarta `i_1`; prossegue. Após `m−1` contra-exemplos sobra no máximo um índice;
pela totalidade de `DD_P` ele é tautológico; o aluno o propõe e para. Cada
movimento do aluno é p-time. *Nota (B):* o artigo só afirma "The problem can be
solved in the S-T model described in the Introduction" e **não** fixa o número
de rodadas; a estratégia acima usa até `m` rodadas, e `m` é polinomial mas
**não constante** — exatamente a lacuna que (ST) pressupõe ser intransponível.

**Proposição 0.4 (B).** Interpolação viável (no sentido de [K97]) **implica**
`DD_P ∈ P`. Demonstração: se `P` tem interpolação viável, dado
`π : P ⊢ α_1 ∨ α_2` com átomos disjuntos, os átomos compartilhados são nenhum,
o interpolante é uma constante `⊤` ou `⊥`, e qualquer interpolante é uma
resposta correta para `DD` (com `¬α_1 ⊨ C ⊨ ¬α_2`: `C = ⊤` força `α_2` tautologia;
`C = ⊥` força `α_1` tautologia). Para `m > 2`, agrupe:
`α_1 ∨ (α_2 ∨ ⋯ ∨ α_m)` (ainda disjunto; associação/commutação de `∨` são baratas
em sistemas razoáveis) e itere: `m−1` chamadas, cada uma p-time no tamanho da
entrada, total polinomial. □
*Corolário (A):* como resolução tem interpolação viável [K97], `DD_Res ∈ P`
segue de [K97] — mas ver Teorema 4.3: a prova é **direta e mais forte**
(a sub-prova do disjunto tem tamanho ≤ `|π|`, não apenas poli(`|π|`)).

---

## 1. (A) O que o artigo afirma — transcrição e comentário

### 1.1 Definições (artigo, Seção 1)

**(A)** Disjunção disjunta `⋁̇_{i<m} α_i`: nenhum par `α_i, α_j` (`i ≠ j`)
compartilha átomo. `DD_P`: entrada `(π, ⋁̇_i α_i)` com `π : P ⊢ ⋁̇_i α_i`;
saída: `i` com `α_i ∈ TAUT`. Totalidade: se cada `α_i` tivesse atribuição
falsificante, a **união** dessas atribuições (átomos disjuntos ⇒ sem conflito)
falsificaria a disjunção inteira, contradizendo `π` (somete de `P`).
`D_P` (generalização): `π : P ⊢ ⋁_i β_i(p,q^i)` com **apenas** os átomos `p`
podendo ocorrer em mais de um `β_i`; `a` é atribuição para os `p`; saída `i` com
`β_i(a,q^i) ∈ TAUT`. **Lemma 1** (artigo): `DD_P ∉ ST[P,O(1)] ⟺ D_P ∉ ST[P,O(1)]`.

### 1.2 A hipótese (ST) e o contexto [17,11]

**(A)** Strong pps = extensão de EF por um conjunto p-time de tautologias como
axiomas extras; todo pps é p-simulado por um strong ([K25, Thm. 2.4.4]).
**(A)** `(ST)`: existe strong pps `P` com `DD_P ∉ ST[P,O(1)]`.
**(A)** O artigo registra: a possibilidade `D_P ∈ ST[P,O(1)]` para strong pps
foi considerada em [17] = Pich–Santhanam, STOC 2021, *"Strong Co-Nondeterministic
Lower Bounds for NP Cannot be Proved Feasibly"*, mas **"it was shown in [11]
that this is not true (assuming the existence of strong one-way permutations),
essentially for reasons similar to why the feasible interpolation fails for
them (cf. [10, Chpt.18])"** — ou seja: (a) `D_P ∉ ST[P,O(1)]` sob permutações
one-way fortes ([K20]); (b) **a interpolação viável falha para strong pps**
sob as mesmas hipóteses criptográficas ([K19, Cap. 18]).

### 1.3 A observação final do artigo (transcrição literal + comentário)

> *"Note that the proof yields a somewhat stronger conclusion that in no strong
> `P` can a proof of some disjunct in a disjoint disjunction be polynomially
> bounded in size in terms of a proof of the disjunction (i.e. the strong
> feasible disjunction property fails for strong proof systems, cf.[12])"*

**(A) comentário.** Em termos da Seção 0: o artigo mostra que, **sob as
hipóteses do Teorema 4** — resposta afirmativa ao Problema 2.1 **e** `(ST)` — a
**(ii) forte falha para todo strong pps**: não existe polinômio `p` com
"algum disjunto de uma disjunção disjunta tem prova de tamanho ≤ `p(|π|)`",
onde `π` é a prova apresentada da disjunção. Estrutura da prova (artigo,
Seção 3): assume-se `NP = coNP`, escolhe-se strong pps `P` que satisfaz (ST) e é
p-bounded; a inconsistência da teoria `S` (axiomas: `T_PV`, `α` é disjunção
disjunta, `π : P ⊢ α`, `∀i<m (¬α_i) ∈ SAT`) daria, pelo **teorema KPT** de
[Krajíček–Pudlák–Takeuti 1991], um aluno p-time resolvendo `DD_P` em `O(1)`
rodadas, violando (ST); logo existe modelo não-padrão `M`; a p-boundedness
garante a verdade (portanto pertencimento a `T_PV`) da fórmula universal `A_Q`
que "certifica provas curtas de disjunctos tautológicos"; o Problema 2.1 estende
`M` a `M* ⊆ M'` com `Log(M*) = Log(M')`, e a contradição final vem do
princípio de reflexão `Ref_P`. Duas observações honestas:

- **(B)** A falha da FDP **forte** não refuta, por si, `DD_P ∉ P` (nem `∈ ST`):
  FDP fala de *comprimento de provas*; `DD_P` fala de *encontrar um disjunto
  tautológico*, o qual pode ter prova longuíssima. O que refuta `DD_P ∈ P` para
  esse `P` é **(ST) diretamente** (Proposição 0.2).
- **(B)** Resolução **não** é strong (não p-simula EF), então nada aqui entra em
  conflito com o Teorema 4.3 abaixo. Consistente com [Pap26]: FDP não é
  preservada para baixo sob p-simulação (diferente de interpolação viável).

---

## 2. Resolução: o caso principal, com teorema positivo

### 2.1 Convenção de apresentação da entrada (importante e honesta)

`π : Res ⊢ ⋁̇_i α_i` significa, por definição, uma **refutação por resolução**
de `¬(⋁_i α_i) ≡ ⋀_i ¬α_i`. Analisamos a entrada na forma canônica:

- **α_i em DNF** sobre átomos `X_i` (disjuntos entre si): então `¬α_i` é uma
  CNF `C_i` com uma cláusula por termo de `α_i`, com `|C_i| ≤ |α_i|`, **sem
  blow-up**, e a refutação é de `Λ = C_1 ⊎ ⋯ ⊎ C_m` — conjuntos de cláusulas
  **puros por lado**. Este é o caso substantivo, pois **tautologia de DNF é
  coNP-completa**.
- **α_i em CNF** (inclusive Horn, 2-CNF): a checagem de tautologia de uma CNF é
  **linear** (cada cláusula precisa conter `p` e `¬p` para algum átomo `p`);
  logo `DD_P ∈ P` neste caso para **qualquer** pps `P`, ignorando `π`.
- **α_i gerais**: a conversão `CNF(¬α_i)` pode ser exponencial; qualquer
  apresentação fiel de `π` que resulte numa refutação de uma CNF `Λ = ⨄_i Λ_i`
  com `Λ_i` puro sobre `X_i` (e `α_i ∈ TAUT ⟺ Λ_i` insatisfatível) é coberta
  pelo Teorema 4.3, pois cada cláusula de `CNF(¬α_i)` só usa átomos de `X_i`.

### 2.2 Lema de recorte (eliminação de enfraquecimento)

Algumas apresentações de resolução admitem a regra de **enfraquecimento**
(`de C derive C ∨ D` — ver a definição usada em [Pap26]).

> **Lema 4.1 (B) — recorte.** Seja `Π = (D_1,…,D_s)` uma refutação de `Λ` com
> resolução **e** enfraquecimento. Existe algoritmo que calcula cláusulas
> `E_1,…,E_s` tal que (a) `E_i ⊆ D_i` para todo `i`; (b) `(E_1,…,E_s)` é uma
> derivação de `Λ` por **resolução pura** (sem enfraquecimento) com `E_s = ∅`;
> (c) cada `E_i` usa no máximo `|D_i|` literais e o custo é `O(|Π|²)` no
> pior caso (`O(Σ_i |D_i|·|D_{pares}|)` na prática).

*Demonstração.* Processa-se `Π` na ordem das linhas (folhas primeiro),
mantendo o invariante: **`E_i ⊆ D_i` e `E_i` é derivável por resolução pura a
partir de `Λ`** (com linhas auxiliares entre os `E_j`, `j < i`, já calculados).

- Folha `D_i ∈ Λ`: `E_i := D_i` (própria cláusula, `E_i ⊆ D_i` ✓).
- Enfraquecimento `D_i = D_j ∪ F`: `E_i := E_j`. Como `E_j ⊆ D_j ⊆ D_i` ✓ e
  `E_j` é derivável ✓ (nenhuma inferência nova).
- Resolução `D_i = (D_j ∖ {l}) ∪ (D_k ∖ {¬l})` com `D_j ∋ l`, `D_k ∋ ¬l`:
  - se `l ∈ E_j` **e** `¬l ∈ E_k`: `E_i := (E_j ∖ {l}) ∪ (E_k ∖ {¬l})` — uma
    inferência de resolução válida, e `E_i ⊆ D_i` ✓;
  - se `l ∉ E_j`: `E_i := E_j`; como `E_j ⊆ D_j ∖ {l} ⊆ D_i` ✓, a inclusão vale,
    e `E_i` é derivável sem nova inferência (basta reaproveitar `E_j`);
  - senão (`l ∈ E_j` e `¬l ∉ E_k`): `E_i := E_k ⊆ D_k ∖ {¬l} ⊆ D_i` ✓.

No fim, `E_s ⊆ D_s = ∅`, logo `E_s = ∅`. Coletando as linhas `E_i` distintas
com suas justificações (cada uma justificada por no máximo uma inferência de
resolução sobre linhas anteriores, ou reaproveitando uma linha anterior),
obtém-se uma refutação pura de `Λ` com no máximo `s` linhas. □

### 2.3 Lema da pureza e o algoritmo de projeção

> **Lema 4.2 (B) — pureza.** Seja `Λ = Λ_1 ⊎ ⋯ ⊎ Λ_m` com `Λ_i` usando só
> variáveis de `X_i` e `X_1,…,X_m` disjuntos. Se `(E_1,…,E_t)` é derivação por
> resolução pura de `Λ` com `E_t = ∅`, então: (1) **toda** linha `E_j` usa
> variáveis de um único `X_i` (linha *pura*); (2) se `E_t` é resolvente de
> `E_a ∋ l` e `E_b ∋ ¬l`, então `E_a` e `E_b` são puras **sobre o mesmo lado**
> `i*`.

*Demonstração.* (1) por indução: folhas são puras; resolvente de `E_a ∋ v` e
`E_b ∋ ¬v`: ambas contêm a variável `v`, logo, pela hipótese de indução, ambas
são puras e `v` pertence ao mesmo `X_i` para as duas; o resolvente também só
tem variáveis de `X_i`. (2) os dois pais contêm a variável de `l`; aplicando
(1), ambos são puros sobre o mesmo lado. □

> **Teorema 4.3 (B) — `DD_Res ∈ P`, com sub-prova ótima.** Seja `Λ = ⨄_{i<m} Λ_i`
> com `Λ_i` puro sobre `X_i` (disjuntos), e `Π` uma refutação de `Λ` por
> resolução (com ou sem enfraquecimento, tree-like ou dag-like). Em tempo
> `O(|Π|·m)` (com constante pequena; na prática linear em `|Π|`) devolve-se um
> índice `i*` com `Λ_{i*}` insatisfatível (logo, na convenção da Seção 2.1,
> `α_{i*} ∈ TAUT`), junto de uma **refutação pura de `Λ_{i*}` com no máximo
> `|Π|` linhas**.

*Algoritmo e demonstração.* (1) Aplique o Lema 4.1: obtenha `(E_1,…,E_s)` refutação
pura de `Λ`, `E_s = ∅`. (2) Se `E_s = ∅` já é uma linha **axioma** de `Λ`
(isto é, `Λ` contém a clausula vazia), algum `Λ_{i*}` contém `∅`, logo é
insatisfatível: devolva esse `i*`. (3) Caso contrário, `E_s` é resolvente de
`E_a ∋ l`, `E_b ∋ ¬l`; ambos são não vazios, logo (Lema 4.2) puros sobre um
mesmo lado `i* := lado(E_a) = lado(E_b)`. (4) Restrinja a derivação às linhas
**acessíveis** a partir de `E_s` (reconstruindo as dependências: pais de
resolução; e, no caso de reaproveitamento "cópia", a linha-fonte). Pela prova
do Lema 4.2, toda linha acessível é pura sobre `i*` (indução retroativa: os
pais de um resolvente compartilham variável, logo são do mesmo lado; cópias
mantêm a linha; folhas acessíveis são puras e, por construção, pertencem a
`Λ_{i*}`). (5) A lista das linhas acessíveis (deduplicadas) é uma refutação
**sem enfraquecimento** de `Λ_{i*}` — cada inferência continua válida e
todas as folhas pertencem a `Λ_{i*}` — e termina em `∅`; logo `Λ_{i*}` é
insatisfatível e `α_{i*}` é tautologia. O número de linhas é ≤ `s = |Π|`. Cada
passo é linear (testar `vars(linha) ⊆ X_i` é `O(|Π|·m)` no total). □

**Comentários.**
- **(B)** Tree-like é subcaso (uma árvore é um DAG). Dag-like coberto.
- **(B)** O teorema dá a **FDP com polinômio `p(t) = t`** (ótimo) para resolução
  — reprovando, de forma autocontida e construtiva, o fato citado em [Gar24]
  ("It is known and easy to see that resolution has the weak feasible
  disjunction property") e a construção "clássica" dos capítulos de
  interpolação ([K19, Cap. 17.7]). O ponto delicado (enfraquecimento) é
  resolvido pelo Lema 4.1, que não é discutido nas fontes que consultamos.
- **(B)** O algoritmo encontra **garantidamente um** lado (o do último passo).
  Testar **todos** os lados `i` (recolher as linhas puras de `X_i` e verificar
  se derivam `∅`) também é p-time e encontra todos os lados cuja refutação
  esteja "dentro" de `Π`; mas um lado insatisfatível **precisa** ter sua
  refutação dentro de `Π`? **Não** — apenas o lado `i*` é garantido. Exemplo:
  `Λ_2 = {{y}}` satisfatível, mas o lado 2 pode contribuir linhas puras
  inúteis. Isto delimita o que a estrutura da refutação impõe: ela **revela**
  (ao menos) um disjunto tautológico, mas não "diagnostica" todos.
- **(B) Corolário 4.4 (DD e D_P para Res).** Dada entrada de `D_P`
  `(π, ⋁_i β_i(p,q^i), a)`, restrinja `π` pela atribuição `a` dos átomos `p`:
  a restrição de uma refutação é uma refutação (regras comutam com restrição;
  cláusulas satisfeitas são apagadas e literais falsificados removidos), de
  tamanho ≤ `|π|`, de `⋀_i ¬β_i(a,q^i)`, cujos conjuntos são puros sobre os
  conjuntos disjuntos `q^i`. Teorema 4.3 aplicado devolve `i` com
  `β_i(a,q^i) ∈ TAUT` em `O(|π|·m)`. **Portanto `D_Res ∈ P`** — coerente com
  Lemma 1 do artigo e com o fato de que Res não é strong.

### 2.4 A proposição da missão sobre interpolação viável estava INVERTIDA

A missão pedia para citar que "a interpolação viável para Res é FALSO". Verifiquei
nas fontes: **é o contrário**.

- **(A)** [K97] (resumo verificado): *"We derive from it several corollaries:
  (1) Feasible interpolation theorems for the following proof systems: (a)
  resolution, (b) …, (c) linear equational calculus, (d) cutting planes."*
  Ver também [P97] (versão **monotona**, usada para cotas exponenciais via
  Alon–Boppana nas fórmulas clique-coloração) e [K19, Cap. 17.7] (as
  construções). [Gar24] confirma: *"Resolution also has feasible interpolation,
  a prominent concept in proof complexity introduced by Krajíček"*, e nota
  (citando Pudlák [Pud03]): *"the weak feasible disjunction property has been
  observed in all proof systems that were shown to have feasible interpolation.
  This is because known feasible interpolation algorithms … actually construct a
  refutation of one of the conjuncts."*
- **(B)** Não localizei nenhuma referência "Otten–Cook" sobre interpolação de
  resolução (nas bibliografias de [Gar24], [Pap26], [K97], [K19] não aparece
  nada correspondente). A referência correta para "FI para Res" é **[K97]**;
  para "FI **falha**", a afirmação correta é: **FI falha para strong pps**
  sob permutações one-way fortes ([K20]; [K19, Cap. 18]; é a razão citada no
  artigo para a refutação de [17]). Para `Res(2)` e além, a FI "parece falhar"
  — crença registrada em [Pap26] ("`Res(2)` is precisely the point in the
  bounded-depth Frege hierarchy where feasible interpolation seems to fail
  too"), sem teorema.
- **(B)** A fronteira exata é, portanto: FI vale para Res, Cutting Planes,
  linear equational calculus ([K97]); FI é **aberta** para Frege; FI **falha**
  para strong pps sob cripto; e para níveis intermediários (`Res(2)`, `Res(⊕)`)
  é creença de falha ([Pap26]).

### 2.5 Casos especiais pedidos

- **(c) `α_i` pequenos.** Se todo `α_i` tem tamanho ≤ `c·log n` (`n` = tamanho
  da entrada), testar tautologia por enumeração de atribuições custa
  `2^{c·log n} = n^c` por disjunto: `DD_P ∈ P` trivialmente, para qualquer `P`.
  Se `|α_i| ≤ n^ε`, o custo é `2^{n^ε}` (subexponencial, não polinomial).
- **`α_i` em CNF** (Horn-CNF, 2-CNF inclusos): teste linear por cláusula
  (ver Seção 2.1); `DD_P ∈ P` para qualquer `P`, sem usar `π`.
- **(b) `m` variável**: Teorema 4.3 é `O(|Π|·m)`; a redução FI ⟹ DD usa
  `m−1` chamadas (Proposição 0.4). Nenhum problema de complexidade.
- **(d) restrições da estrutura da refutação**: discutido no comentário (4) do
  Teorema 4.3: as linhas puras do lado `i*` **refutam** `Λ_{i*}`; linhas puras
  de lados satisfatíveis nunca derivam `∅` (consistência), mas podem existir.
  A restrição "positiva" extraída é: *o último passo da refutação pura sempre
  tem os dois pais no mesmo lado* — este é o único "diagnóstico" estrutural
  garantido, e é exatamente o que o algoritmo explora.

---

## 3. Mapa por sistema

### 3.1 Resolução (tree-like, dag-like, com/s enfraquecimento)

- **(B)** `DD_Res ∈ P` com sub-prova de tamanho ≤ `|π|` (Teorema 4.3);
  `D_Res ∈ P` (Corolário 4.4); FDP com `p(t)=t`.
- **(A)** FI vale ([K97]); FDP fraca vale ([Gar24], "known and easy to see").
- **(A)** Automatizar resolução é NP-dura ([AM20]) — **logo `DD_Res ∈ P` não
  implica automatizabilidade**; a distinção é real e conhecida.
- **(A)** Res não é p-bounded: `PHP` requer `2^{Ω(n)}` ([Hak85]) — logo
  **`DD_P ∈ P` não implica p-boundedness** (ver Seção 5).

### 3.2 `Res(τ)` e `Res(k)` (k-DNF resolution)

**Definição (A) [Gar24]:** `Res(k)` (introduzida por Krajíček, [K19, Cap. 5.7])
tem linhas que são k-DNFs e regras: ∧-introdução (até `k` literais), axioma
`x ∨ ¬x`, corte, enfraquecimento. (`Res(1)` ≈ resolução com enfraquecimento;
`Res(k)` p-simula `Res`.) Este é o sistema natural para a linha
"k-DNF / AC⁰-Res" da missão.

- **(A) Teorema 1 de [Gar24]:** para todo `k ≥ 2`, `Res(k)` **não** tem a
  propriedade de disjunção viável fraca. Mais precisamente: existem famílias
  `{A_n}` (tamanho `n^{O(1)}`) e `{B_{n,k}}` (tamanho `n^{O(k)}`) de CNFs
  **disjuntas em variáveis** e **ambas insatisfatíveis**, tais que: (1) toda
  refutação `Res(k)` de `A_n` tem tamanho `> 2^{n^α}`; (2) toda refutação
  `Res(k)` de `B_{n,k}` tem tamanho `> 2^{βn}`; (3) `A_n ∧ B_{n,k}` tem
  refutação `Res(2)` de tamanho `O(k²n^{7k+7})`. A construção usa o princípio
  de reflexão de resolução **relativizado** `k` vezes (técnica Dantchev–Ris).
- **(A)** Automação: se `NP ⊄ P` (resp. `QP`, `SUBEXP`), então `Res(k)` não é
  automatizável em tempo polinomial (resp. quasipolinomial, subexponencial)
  para todo `k ≥ 1` (generalizando [AM20]).
- **(C) Análise honesta do que isso NÃO diz sobre `DD`:** em todas as instâncias
  de Garlík **ambos** os disjunctos são tautologias (ambos os lados são CNFs
  insatisfatíveis) — ou seja, o teorema é sobre **comprimento de provas**, e
  qualquer resposta seria correta para `DD`. **`DD_{Res(k)} ∈ P` permanece
  aberto**; não localizei resultado em nenhuma direção. O obstáculo para o
  Teorema 4.3 é nítido: a ∧-introdução de `Res(k)` cria linhas que **misturam**
  átomos de lados diferentes (ex.: `(l_1 ∧ l_2)` com `l_i` de lados distintos),
  quebrando o Lema 4.2; o Lema 4.1 não salva, pois não é enfraquecimento.
  **Conjectura de trabalho (C):** `DD_{Res(k)} ∉ P` para `k ≥ 2` a menos que
  `P = NP`; uma redução teria que produzir, a partir de uma tautologia `β`,
  uma disjunção disjunta **com exatamente um** lado tautológico e "escondido" —
  exatamente o que as construções de reflexão de [Gar24] não fazem (elas dão
  dois lados insatisfatíveis).

### 3.3 Sistemas de profundidade limitada (AC⁰-Res, Frege de profundidade `d`)

- **(A)** Não-automatizabilidade: [Ale04] (bounded-depth Frege), [Pap24]
  (Frege de profundidade `d`, todo `d ≥ 1`, s/ `P = NP`). De novo: automação
  dura ≠ `DD` duro (para Res, `DD ∈ P` e automação NP-dura coexistem).
- **(A)** FI: aberta para Frege; "parece falhar" a partir do patamar `Res(2)`
  (crença de [Pap26], apoiada em [Pud03]); abaixo disso, aberta.
- **(A)** FDP: falha em `Res(2)` ([Gar24]) e, segundo Pudlák ([Pud03], relatado
  em [Gar24]), é *"very unlikely to occur unless the system is very weak"*.
- **(C)** `DD_P` para AC⁰-Frege/Frege de profundidade fixa: **aberto**. Nenhum
  teorema positivo (o método de pureza não se estende: fórmulas de largura
  arbitrária misturam lados livremente) nem negativo (as técnicas de [Gar24]
  só dão comprimento de provas).

### 3.4 Frege, Extended Frege e strong pps

- **(A)** `(ST)` ⟹ `DD_P ∉ ST[P,O(1)]` para algum strong `P` ⟹ `DD_P ∉ P`
  para esse `P`; crença do autor: vale para **todos** os strong pps, i.e.
  equivalente a valer para EF. `(ST)` é verdadeira se existir permutação
  one-way forte ([K20] via Lemma 2 do artigo).
- **(A)** Sob (Problema 2.1 afirmativo) + `(ST)`: **FDP forte falha para todo
  strong pps** (observação final transcrita na Seção 1.3) e `NP ≠ coNP`
  (Teorema 4).
- **(A)** FI também falha para strong pps sob as mesmas hipóteses cripto
  ([K20]; [K19, Cap. 18]) — citado pelo artigo ao discutir [17,11].
- **(B)** Nota sobre o passo (1) do Teorema 4 do artigo ("sob `NP = coNP`,
  escolher strong pps que satisfaz (ST) e é p-bounded"): p-boundedness de um
  strong pps segue de `NP = coNP` — pois `TAUT ∈ NP` dá certificados curtos
  `w`, e o "programa de Cook" de `V(β,w)=1` tem prova EF curta, portanto prova
  `P` curta para todo strong `P ⊇ EF`. (Coerente com a Proposição 5.4 abaixo.)

### 3.5 Resolução aleatória (e a fronteira FDP × FI)

- **(A) [Pap26]:** resolução aleatória com **erro dinâmico** `ε ∈ (0,1)` tem a
  propriedade de disjunção viável: se `F ∧ G` (variáveis disjuntas) tem
  refutação aleatória de tamanho `s` e erro dinâmico `ε`, então `F` ou `G` tem
  refutação aleatória de tamanho `s` e erro ≤ `(1+ε)/2` (Teorema 3.2; corolário
  mantém `ε` com tamanho `s^{O(1+log(1/ε))}`). A prova é **não construtiva**
  (minimax de von Neumann), e o artigo explicita: o critério `V_F ≥ (1−ε)/2` é
  um interpolante, *"Unfortunately, it is not a polynomial-time computable
  interpolant."*
- **(A)** É *"the first instance of a proof system not known to have feasible
  interpolation, which nevertheless has the feasible disjunction property"* —
  confirmação empírica de que (i) e (ii) da Seção 0 são noções independentes.
- **(C)** `DD` para resolução aleatória: **aberto**; o argumento de [Pap26]
  fornece existência (um lado tem refutação curta), não um algoritmo que ache
  o lado.

### 3.6 Sistemas de "interseção" (TFNP ∩) — ligação com `D_P`

- **(A)** [HKT24] e [LPR24] mostram que, ao restringir sistemas que têm FI e
  FDP para os subsistemas correspondentes a **interseções de classes TFNP**,
  obtêm-se subsistemas em que a FDP **falha** (relato verificado em [Pap26]).
- **(C)** A generalização `D_P` do artigo (átomos `p` compartilhados) tem sabor
  de tais interseções; uma conexão formal ("`D_P` para o subsistema de
  interseção de `P`") pode ser o lugar certo para transferir os resultados
  negativos de [HKT24, LPR24] para a versão O(1)-rodadas de `D_P`. Deixamos
  como problema aberto.

---

## 4. Disjunctos em Horn / 2-CNF / profundidade limitada (lado da fórmula)

**(B)** Resumo: o "lado fraco" aqui é a **fórmula**, não o sistema.

- `α_i` CNF arbitrária (2-CNF, Horn-CNF inclusas): tautologia ⟺ toda cláusula
  contém `p` e `¬p` — teste **linear**; `DD_P ∈ P` para qualquer `P` (nem usa
  `π`). O mesmo vale para `D_P` restrito a essas apresentações.
- `α_i` DNF: tautologia é coNP-completa — caso substantivo; para resolução, o
  Teorema 4.3 resolve; para sistemas fortes, é o caso difícil.
- `α_i` de profundidade `d` fixa com `d ≥ 2`: tautologia continua coNP-completa
  para `d ≥ 2` (via CNF→DNF etc.); nenhuma simplificação.
- **(C)** A pergunta realmente interessante para "sistemas limitados de
  profundidade" é sobre o **sistema de prova**, tratada na Seção 3.2–3.3.

---

## 5. p-boundedness: análise rigorosa da afirmação da missão

Lembrando a afirmação a verificar: *"se `P` é p-bounded (toda tautologia tem
prova de tamanho ≤ `|β|^c`) então `DD_P ∈ P` — dá para fazer enumerando todas
as provas de tamanho ≤ `|β|^c` para cada `i` e testando a condição (é
determinístico e polinomial)"*.

### 5.1 A enumeração NÃO é polinomial (a afirmação, como está, é falsa)

**(B) Proposição 5.1.** O algoritmo por enumeração custa
`Θ(2^{|β|^c+1})` testes por disjunto, i.e. `m · 2^{n^{c}+O(1)} · poly(n)` no
total (`n` = tamanho da entrada). Para **todo** `c ≥ 1` isso é
superpolinomial (exponencial em `n^c`).

*Demonstração.* O número de cadeias binárias de comprimento `≤ N` é
`2^{N+1} − 1`. Com `N = |β|^c = n^{Θ(1)}`, obtemos `2^{n^{Θ(1)}}` candidatos `σ`;
cada teste `P(σ,β)` é p-time, mas há exponencialmente muitos. Não há como
"fatiar" melhor sem mais informação: `P` é arbitrária (relação binária
qualquer), então o conjunto `{σ : P(σ,β)}` não tem estrutura explorável. □

**Conclusão honesta (B):** a afirmação da missão, com a justificativa dada,
**não se sustenta**. O custo exato é exponencial. O que **é** verdade:

- **(B) Proposição 5.2 (versão construtiva, correta).** Se além de p-bounded
  existir algoritmo p-time `f` tal que, para **toda** tautologia `β`,
  `f(β)` é uma prova `P` de `β` (p-boundedness "construtiva" — em particular,
  se `P` é automatizável em tautologias), então `DD_P ∈ P`: para cada `i`,
  compute `f(α_i)` e verifique `P(f(α_i),α_i)`; pela totalidade e pela correção (sometevidade) de P,
  o primeiro `i` aceito é tautológico, e algum é aceito (pela p-boundedness +
  construtividade). Custo `m·poly(n)`.
- **(B) Proposição 5.3.** A implicação bruta "p-bounded (existencial)
  `⟹ DD_P ∈ P`" é um **problema aberto**: não encontrei algoritmo nem
  redução; o obstáculo é exatamente a não-construtividade (p-boundedness é
  uma afirmação ∀∃ sobre provas; `DD_P` é busca por certificados).
  *Observação (B):* sob as hipóteses do Teorema 4 do artigo, `NP ≠ coNP` é
  deduzido, e então **nenhum** pps é p-bounded (Proposição 5.4); logo, sob
  essas hipóteses, a implicação é vazia. O conteúdo da questão concentra-se,
  portanto, no mundo `NP = coNP`.

### 5.2 Duas propriedades auxiliares (B)

- **Proposição 5.4 (B).** Para **qualquer** pps `P`: `P` p-bounded `⟹ NP = coNP`.
  (`⟹`): `β ∈ TAUT ⟺ ∃σ (|σ| ≤ |β|^c ∧ P(σ,β))`, com verificação p-time:
  `TAUT ∈ NP`. Recíproca **para existência**: se `NP = coNP`, `TAUT ∈ NP`;
  tome o pps `P_0` dado por `P_0((w),β) := V(β,w)` para um verificador p-time
  `V` de TAUT: toda tautologia tem certificado `w` polinomial, logo `P_0` é
  p-bounded (e p-simulado por um strong pps, que também fica p-bounded — ver
  Seção 3.4, item (B)). A recíproca **para um `P` fixo qualquer** é falsa em
  princípio: p-boundedness de, ex., resolução sob `NP = coNP` não é deduzível
  por esse argumento (não há razão conhecida para toda tautologia ter prova
  de resolução polinomial). (Cook–Reckhow observaram a versão existencial:
  "existir sistema polynomially limitado ⟺ `NP = coNP`"; verif. em [Gar24].)
- **Proposição 5.5 (B) — a recíproca é FALSA.** `DD_P ∈ P` **não** implica
  `P` p-bounded: resolução é a contra-exemplo (Teorema 4.3 dá `DD_Res ∈ P`;
  `PHP` tem refutações `2^{Ω(n)}` [Hak85], logo Res não é p-bounded). A
  dica da missão ("para usar `DD_P` precisaríamos de uma prova `P` de uma
  disjunção disjunta contendo `β`, e construir essa prova já exige o que
  queremos") está correta e é confirmada por este contra-exemplo: `DD_P`
  só fala sobre instâns que **já trazem** uma prova da disjunção; ele não
  produz provas de tautologias arbitrárias.

---

## 6. Tabela-síntese: para quais `P` existe algoritmo polinomial para `DD_P`?

Legenda das colunas: **(i)** `DD_P ∈ P` (determinístico p-time);
**(ii)** `DD_P ∈ ST[P, O(1)]`; **(iii)** `DD_P ∈ ST[P, poly]`;
**FDP** = propriedade de disjunção viável (fraca, salvo indicação).

| Sistema `P` | (i) `DD_P ∈ P` | (ii) `∈ ST[P,O(1)]` | (iii) `∈ ST[P,poly]` | FDP | Hipótese usada | Referência |
|---|---|---|---|---|---|---|
| Resolução (tree/dag, com ou sem enfraquecimento) | **SIM** (Teorema 4.3; sub-prova ≤ `\|π\|`) | SIM (0/1 rodadas) | SIM | **SIM**, com `p(t)=t` | nenhuma | (B) acima; (A) [K97] (FI), [Gar24] (FDP "easy") |
| `Res(τ)` com axiomas `τ` puros por lado | **SIM** (mesmo argumento) | SIM | SIM | SIM (`p(t)=t`) | nenhuma | (B) |
| `α_i` em CNF (2-CNF, Horn, …), qualquer `P` | **SIM** (teste linear por cláusula; ignora `π`) | SIM | SIM | — (pergunta sobre o sistema, não se decide aqui) | nenhuma | (B) |
| `\|α_i\| ≤ c·log n`, qualquer `P` | **SIM** (enumeração `n^{O(c)}`) | SIM | SIM | — (idem) | nenhuma | (B) |
| `Res(k)`, `k ≥ 2` (k-DNF resolution) | **ABERTO** (crença: `∉ P` s/ `P≠NP`) | aberto | SIM | **NÃO** (fraca) | — / `NP ⊄ P` p/ automação | [Gar24] (FDP, automação); (C) |
| Resolução aleatória (erro dinâmico `ε∈(0,1)`) | **ABERTO** | aberto | SIM | **SIM** (não construtiva, minimax) | nenhuma | [Pap26] |
| Frege de profundidade `d` / AC⁰-Frege | **ABERTO** | aberto (crença: não) | SIM | aberto (crença de falha a partir de `Res(2)`) | — | [Ale04],[Pap24] (automação); [Pud03] via [Gar24],[Pap26] |
| Frege, EF, strong pps | **NÃO** para o `P` de (ST) (crença: para todos, eq. EF) | **NÃO** (o próprio (ST)) | SIM | **NÃO** (forte) | (ST) [+ Probl. 2.1 p/ `NP≠coNP`]; (ST) segue de OWF forte | artigo (Lemma 1, Thm 4, obs. final); [K20],[K25],[K19] |

**O que cada noção implica (síntese lógica).** `(i) ⟹ (ii) ⟹ (iii)`, e
`(iii)` vale trivialmente para todo `P` (Proposição 0.3, `≤ m` rodadas).
`(ii)` não implica `(i)` conhecidamente — mas `(ST)` nega `(ii)` e, com ele,
`(i)`, para um strong `P`. FDP é **independente** de `(i)`: vale para random
resolution com `(i)` aberto ([Pap26]) e falha para `Res(k)` com `(i)` aberto
([Gar24]); `(i)` vale para Res com FDP ótima e com automação NP-dura ([AM20]).
Interpolação viável **implica** `(i)` (Proposição 0.4), mas `(i)` não a implica
(é o caso Res? — não: Res tem FI; o candidato natural é random resolution,
onde FI é aberta).

---

## 7. Experimentos computacionais

**Arquivo:** `experimentos_disjuncao.py` (Python 3, só stdlib; rodei com
`python` 3.12 no Windows). **O que ele faz** (ver docstring do arquivo):

1. Gera instâncias aleatórias: `C_1` (sobre `X_1`) e `C_2` (sobre `X_2`),
   disjuntas, com **exatamente um** lado insatisfatível; `α_i := ¬C_i` (DNF);
   constroi refutação de `C_1 ∪ C_2` por saturação;
2. Verifica o **algoritmo de projeção** (Lema 4.1 + Lema 4.2 + Teorema 4.3),
   incluindo verificação independente da sub-refutação devolvida;
3. Testa heuristicas ingênuas que usam **só os `α`** (maior em literais; mais
   termos; mais termos unitários; maior termo; "sempre o primeiro") e mede
   taxas de falha; procura contra-exemplos **mínimos** por enumeração exaustiva;
4. Testes de unidade: refutação **pura** (T1); refutação **misturada com
   enfraquecimento** cujo último passo tem pais de "origens" diferentes — a
   rotulagem ingênua falha, o algoritmo recupera o lado correto (T2); extensão
   `D_P` via restrição (T3).

**Saída real (resumo; semente 20261010):**

```
T1 (refutacao pura): |pi| = 4 -> lado devolvido = 0 (esperado 0), sub-refutacao de tamanho 3
T2 (refutacao misturada): rotulagem ingenua ... AMBIGUA
T2: algoritmo de projecao devolve lado 0 (esperado 0) com sub-refutacao pura de tamanho 5 (|pi| = 7)
T3 (D_P com restricao): a(p)=1, |pi| = 5 -> lado devolvido = 0 (esperado 0)
Todos os testes de unidade passaram.

Instancias geradas com refutacao encontrada: 3000
Distribuicao do lado tautologo (simetria do gerador): lado 0 = 1515, lado 1 = 1485
Algoritmo de projecao (Teorema C.1): 3000/3000 corretos (100.0%)

Taxas de falha das heuristicas ingenuas (apenas instancias com exatamente um
disjunto tautologo):
  maior_em_literais            falha em  847/3000 =  28.2%
  mais_termos                  falha em  436/3000 =  14.5%
  mais_termos_unitarios        falha em  289/3000 =   9.6%
  termo_maior                  falha em 1566/3000 =  52.2%
  sempre_o_primeiro            falha em 1485/3000 =  49.5%

Tamanhos de refutacao: media |pi| = 7.0, max = 20; refutacao minima de um lado: media = 3.1
```

**Contra-exemplos mínimos (enumeração exaustiva; lados com 2 variáveis, CNFs
com até 3 cláusulas; na exibição as variáveis do lado 2 são renomeadas):**

```
maior_em_literais        : 5 literais  C_1 = {x0} /\ {~x0} (insat.)   C_2 = {x0} /\ {x0,x1} (sat.)
mais_termos              : 6 literais  C_1 = {x0} /\ {~x0} (insat.)   C_2 = {x0}/\{x1}/\{x0,x1} (sat.)
mais_termos_unitarios    : 7 literais  C_1 = {x0}/\{x1,~x0}/\{~x0,~x1} (insat.)  C_2 = {x0}/\{x1} (sat.)
termo_maior              : 4 literais  C_1 = {x0} /\ {~x0} (insat.)   C_2 = {x0,x1} (sat.)
mais_termos_unitarios (lado 2 com 3 vars): 5 literais  C_1 = {x0}/\{~x0}  C_2 = {x2}/\{x3}/\{x4}
```

**Leitura honesta dos dados.**

- **(B)** O algoritmo de projeção acertou **3000/3000** — consistente com o
  Teorema 4.3 (a prova é um teorema; o experimento é sanity check, incluindo a
  implementação do recorte, que de fato contorna a refutação "misturada" T2,
  onde a rotulagem ingênua falha). Note-se que em T2 o algoritmo devolve
  sub-refutação de tamanho 5 (`≤ |π| = 7`), mostrando que o recorte pode
  desperdiçar um fator, mas nunca excede `|π|`.
- **(B)** As heuristicas **falham com frequência real** (9,6%–52% das instâncias
  aleatórias; e falham já no tamanho mínimo: ex. "maior em literais" erra com
  `α_1 = ¬x₀ ∨ x₀` (tautologia, 2 literais) vs `α_2 = ¬x₀ ∨ (¬x₀∧¬x₁)`
  (3 literais, não-tautologia)). **Heurística ≠ algoritmo**: nenhuma regra
  puramente sintática sobre os `α` observados garante sucesso — é preciso usar
  a **prova** (é o que o Teorema 4.3 faz). Os experimentos não provam nada
  (e não poderiam provar `DD ∉ P` para nada); eles apenas ilustram que a
  "cheirar" o lado certo não funciona, e servem de teste de implementação para
  o algoritmo que **é** correto.
- **(B)** Bug encontrado e corrigido durante o desenvolvimento (registrado por
  honestidade): a primeira versão avaliava a satisfaibilidade do lado 2 com os
  índices de variáveis globais errados, produzindo assimetria espúria (89% dos
  lados tautológicos eram o lado 2). Corrigido com deslocamento local; a nova
  execução é simétrica (1515/1485) e as taxas acima são as definitivas.

---

## 8. Limitações, e status aberto mais promissores

1. **(C)** `DD_{Res(k)} ∈ P` para `k ≥ 2`? Nenhum resultado conhecido. O
   método de pureza quebra exatamente na ∧-introdução; as construções de
   [Gar24] dão dois lados tautológicos (bom para FDP, inúteis para DD). Uma
   separação `DD_{Res(2)} ∉ P` (s/ `P ≠ NP`) exigiria famílias com **um**
   lado tautológico "escondido". Este é, na nossa avaliação, o problema mais
   concreto deixado em aberto por esta nota.
2. **(C)** `DD_P ∈ P` para p-bounded `P` (Proposição 5.3): aberto; o algoritmo
   por enumeração é exponencial (Proposição 5.1). Sob `NP ≠ coNP` a questão é
   vazia (nenhum pps é p-bounded).
3. **(C)** Conexão entre `D_P` (com átomos `p` compartilhados) e as
   interseções TFNP de [HKT24, LPR24]: pode ser o canal para levar resultados
   negativos de FDP para dentro da análise S-T de `D_P` (Lemma 1 do artigo).
4. **(B)** Para random resolution com erro dinâmico, `DD ∈ P`? O minimax de
   [Pap26] é não construtivo; talvez uma versão "computável" do teorema dê um
   algoritmo quasipolinomial; não investigamos.
5. **(C)** Frege/EF: a única barreira conhecida para `DD_EF ∈ P` é (ST)
   (condicional a OWF forte). Uma refutação **incondicional** de `DD_EF ∈ P`
   estaria, na hierarquia de dificuldade, acima de `NP ≠ coNP`? Não sabemos;
   note que `DD_EF ∈ P` seria um algoritmo p-time para um problema de busca
   `Σ₂ᵖ` total com soluções verificáveis em coNP — um resultado surpreendente
   mas não contradictório com nada conhecido.

---

## 9. Referências (com verificação)

Todas as entradas marcadas com "verif." foram conferidas no texto integral ou
no resumo oficial consultado durante este trabalho (arXiv/ECCC/Dagstuhl/LIPIcs).

- [AM20] Atserias & Müller, *Automating resolution is NP-hard*, FOCS 2019 / JACM 2020. (verif. via [Pap24], [Gar24])
- [Ale04] Alekhnovich, *Non-automatizability of bounded-depth Frege proofs*, Comp. Complexity 13 (2004) 47–68. (verif. título em lista de referências de [Pap24])
- [BKT14] Buss, Kołodziejczyk, Thapen, *Fragments of approximate counting*, JSL 79 (2014) 496–525. (verif. via [Pap26])
- [Gar24] Garlík, CCC 2024, LIPIcs 300, 33:1–33:23; arXiv:2003.10230; ECCC TR20-037. (verif. integral)
- [Hak85] Haken, *The intractability of resolution*, TCS 38 (1985) 141–147.
- [HKT24] Hubáček, Khaniki, Thapen, ITCS 2024, LIPIcs 287, 63:1–63:24. (verif. título/venue via [Pap26])
- [K19] Krajíček, *Proof Complexity*, CUP 2019.
- [K20] Krajíček, *A limitation on the KPT interpolation*, LMCS 16(3), 2020. (= [11] do artigo; verif. no artigo)
- [K25] Krajíček, *Proof complexity generators*, LMS 497, CUP 2025. (= [12] do artigo; verif. no artigo)
- [K97] Krajíček, *Interpolation theorems, lower bounds for proof systems, and independence results for bounded arithmetic*, JSL 62 (1997) 457–486. (verif. resumo: FI para resolução, cutting planes, etc.)
- [LPR24] Li, Pires, Robere, ITCS 2024, LIPIcs 287, 74:1–74:22. (verif. via [Pap26])
- [Pap24] Papamakarios, *Depth-d Frege Systems Are Not Automatable Unless P = NP*, CCC 2024, LIPIcs 300, 22:1–22:17. (verif.)
- [Pap26] Papamakarios, *Feasible disjunction for random resolution*, ECCC TR26-154, 2026. (verif. integral)
- [P97] Pudlák, *Lower bounds for resolution and cutting plane proofs and monotone computations*, JSL 62 (1997) 981–998. (verif. via slides/[K97])
- [Pud03] Pudlák, *On reducibility and symmetry of disjoint NP pairs*, TCS 295 (2003) 323–339. (verif. via [Pap26])
- [Rud97] Rudich, *Super-bits, demi-bits, and NP/qpoly-natural proofs*, RANDOM 1997. (verif. via [Pap26])
- [KPS90] Krajíček, Pudlák, Sgall, *Interactive computations of optimal solutions*, MFCS 1990. (= [15] do artigo, modelo S-T; verif. no artigo)
- [KPT91] Krajíček, Pudlák, Takeuti, *Bounded arithmetic and the polynomial hierarchy*, APAL 52 (1991) 143–153. (= [16] do artigo, teorema KPT; verif. no artigo)
- [PS21] Pich, Santhanam, STOC 2021, 223–233. (= [17] do artigo; verif. no artigo)
- [Artigo] Krajíček, *On NP∩coNP proof complexity generators*, arXiv:2506.20221v4 (23 Mar 2026). (texto integral verificado na versão HTML)

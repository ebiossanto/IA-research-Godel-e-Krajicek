# G1 — Lema de Log e medidas no forcing booleano de [Kra95, Thm 9.4.2]

**Arquivo:** `G1_log_forcing.md` (Frente G1, subagente, rodada de 11 Out 2026).
**Entregável único desta missão.** Marcação: **(A)** = artigo/fonte; **(P)** = demonstração
própria; **(C)** = conjectura/hipótese de trabalho não verificada. Idioma: português.

**Resumo dos resultados desta rodada (detalhados nos §§2–4):**
- **(L1) PROVADO (P):** `Log(M[G]) = Log(M)` na construção booleana de [Kra98, §4] (= fonte do
  [Kra95, §9.4]): toda medida de `M[G]` vem de `M`. A construção é "medida a medida".
- **"Additional requirement on M" localizado (A):** não é sobre `Log` (que é de graça); é sobre
  a **existência do genérico/semente**: `M` contável (ou ℵ₁-/recursivamente-saturado),
  `SAT_n(M)` não reconhecível por circuito em `M`, função counter-example em `P/poly`, e
  **definabilidade das famílias no ordenamento parcial `P`** (errata oficial 9.4.1/Claim 6).
- **(R1) REFUTADO (P):** fixar nomes curtos colapsa a genericidade (os átomos `p_i` *são* nomes
  de comprimento 1), e — golpe independente e decisivo — **(F-b') é refutado em geral**
  (Teorema 4.3: selar `M'∩m = M∩m` é incompatível com `M' ⊨ T_PV + (¬φ) ∈ SAT`). O índice `i_0`
  do falsificador é **necessariamente novo** (`i_0 ∈ M' \ M`); o passo do artigo
  "by (7) i_o is also already in M*" é necessariamente falso sob a leitura (8)-em-`M*`.
- **[Kra95, Thm 9.4.2]:** enunciado verbatim **não obtido** (livro pago; IA restrita), mas a
  **errata oficial** de Krajíček fixa o conteúdo (extensão `(M', X')` Σ^{1,b}_0-elementar, +
  modelo de `V^1_1`), e a construção-fonte correspondente foi obtida integralmente
  ([Kra95], *On Frege and Extended Frege Proof Systems*, §5; e [Kra98, §4] verbatim).

---

## §0. O que já se sabia antes desta rodada (estado do contexto)

**(A)** O artigo-alvo **arXiv:2506.20221v4** (e **v5 / LMCS 22(2:14)2026**, aceito 17 Mar 2026)
contém a lacuna literal:

> "But by (7) i_o is also already in M∗ and hence by (8) we get: M′ ⊨ (¬α_{i_0}) ∈ SAT."

— persistente em v5/LMCS. O Problema 2.1 pede `M'` com `Log(M') = Log(M)`, cofinal,
`φ'` com prova em `M'` mas `φ` sem prova em `M`. Contexto: `Log(M) = {|m| | m ∈ M}` (inalterado).

**(A)** Do contexto `G_CONTEXTO_FORCING.md`: §9.4 de [Kra95] = extensões booleano-valoradas
(prefácio do livro aponta valorações booleanas nas "sections 3.1, **9.4**, 12.7 and 13.3");
[Kra98, §4] explicita a construção (`B(p)`, ultrafiltro `G` fechado sob EF-provability, nomes
`∈ M`, elementos `⟨ν_G(C_1),…,ν_G(C_ℓ)⟩`, Teorema 4.1, Claims 1–2 da semente); [Kra16] diz
literalmente que nas forcings "[17,15] one naturally adds many new elements into [n]".

**(A/P)** `F2_versao_finita.md`: (F-b') `M'∩m = M∩m`; (F-sent) `M' ⊨ ∀i<m (¬α_i) ∈ SAT`;
`(F-b') ⟹ (F-sent)`; leitura de `φ = ⋀_{i<m} ¬(r_i : P ⊢ α_i)`; `Ref_P ∈ T_PV`;
sobe `Σ^b_1` para extensões.

**(A)** `F1_verificacao_passo7.md`: cita verbatim o artigo — "… one can arrange that M′
introduces no new **lengths** into M: Log(M′) = Log(M) (5) … A construction which yields this
(**with an additional requirement on M**) is the forcing construction underlying [7, Thm.9.4.2]."

**(A)** Coletado nesta rodada (fontes novas em `fontes/`):
- **Errata oficial** de Krajíček para o livro (`krajicek_upravy.html`, `kraj_err.pdf`,
  de `karlin.mff.cuni.cz/~krajicek/upravy.html` + `err.pdf`): correções na §9.4 — ver §5.
- **[Kra95] §5 = a construção-fonte**: `kraj95_frege.pdf/.txt` = *On Frege and Extended Frege
  Proof Systems* (Feasible Mathematics II, 1995), Seção 5 "A Forcing Construction"
  (Theorem 5.1 + construção `M*[G]` com corte, condições (1)–(5), ultrafiltro `F` em `B`).
  [Kra98] declara o Teorema 4.1 "a special case of [5, Thm 5.1]" e remete a "[4, Chpt. 9.4]"
  (= o livro). ⇒ §5 do artigo de 1995 **é** a construção subjacente ao Thm 9.4.2.
- **[Kra98] §4 verbatim** extraído (`kra98_full.txt`) — base da §1 abaixo.
- Sumário do livro (hbz-nrw): §9.4 "Model-theoretic constructions", **pp. 172–180**.

---

## §1. Formalização da construção `M[G]` (precisão para raciocinar sobre tamanhos)

Fonte: **(A)** [Kra98, §4] (verbatim extraído; OCR com ligaduras quebradas, transcrição
normalizada) e **(A)** [Kra95], *On Frege and EF*, §5 (versão `V^1_1`). Comentários **(P)**.

### 1.1 A base (versão `PV`, [Kra98, §4])

Seja `M ⊨ PV` e `p = (p_1,…,p_n) ∈ M` uma sequência de **átomos proposicionais** (elementos
de `M`!). Definir:
- `Circuit_M(p)`: todos os circuitos com uma saída formados a partir dos átomos `p_i`;
- relação `C₁ ~ C₂` sse existe **prova EF em `M`** de `C₁ ↔ C₂`; `B(p) := Circuit_M(p)/~`
  é uma álgebra de Booleanos **em `M`** (a relação é definida em `M`, mas os `[C]` são classes
  externas — ver Pegadinha 4);
- `G`: **ultrafiltro em `B(p)` fechado sob EF-provability in `M`**, i.e., sempre que existe
  prova EF em `M` de `D` a partir de `C_1,…,C_k` e `ν_G(C_i)=1` para todo `i`, então `ν_G(D)=1`;
- `ν_G(C) = 1` sse `[C] ∈ G`; `ν_G(C) ∈ {0,1}` por ser ultrafiltro;
- **`Names_M(p) := { ⟨C_1,…,C_ℓ⟩ ∈ M : C_j ∈ Circuit_M(p) }`** — **os nomes são elementos de
  `M`** (sequências internas); `ℓ = comprimento do nome ∈ M` (o comprimento é p-tempo
  definível internamente);
- **`M[G]`**: o universo é `{ ⟨ν_G(C_1),…,ν_G(C_ℓ)⟩ : ⟨C_1,…,C_ℓ⟩ ∈ Names_M(p) }` — um
  elemento para **cada** nome em `M`; i.e., `M[G]` é a imagem do mapa `N ↦ ν_G(N)` sobre
  `Names_M(p)`;
- operações: para `f` função **PV** e `ℓ ∈ Log(M)` um comprimento, `D^t_{f,ℓ}(y_{ij})`
  (`i ≤ k`, `j ≤ ℓ`) é o circuito **em `M`** que computa (**provably in PV**) o `t`-ésimo bit
  de `f(x_1,…,x_k)` para entradas `x_i` de comprimento **no máximo** `ℓ` com bits
  `y_{i1},…,y_{iℓ}`; e `f(w_1,…,w_k)` para `w_i = ⟨ν_G(C_{i1}),…,ν_G(C_{iℓ})⟩` é definido
  **bit a bit** por `⟨ν_G(D^1_{f,ℓ}(y_{ij}:=C_{ij})), ν_G(D^2_{f,ℓ}(…)), …⟩` (uma sequência que
  é, ela própria, o valor de um **nome de `M`**).

**Teorema 4.1 (A).** Se `G` é fechada sob EF-provability in `M`, então `M[G]` é extensão
**cofinal** de `M` e **modelo de PV**. Moreover, se `ν_G(C)=1` para todo `C ∈ Circuit_M(p)`
que em `M` computa constantemente 1, então `M[G]` é extensão **`Σ^b_1`-elementar** e cofinal.

**Claims 1–2 (A).** Dado um conjunto `T` de fórmulas proposicionais (sobre os átomos `p`)
**sem refutação EF em `M`**, existe ultrafiltro `G` em `B(p)`, fechado sob EF-provability,
com `ν_G(C)=1` para todo `C ∈ T` (e para todo `C` constante-1 em `M`). Prova: os majorantes
de `T` geram um filtro não-trivial (a refutação EF de `T` daria, por soundness de EF em
modelos de PV, um circuito reconhecendo `SAT_n(M)` na aplicação de [Kra98]); qualquer
ultrafiltro estendendo serve.

### 1.2 Comprimento em `M[G]` (definição interna) — **(P)**

`M[G] ⊨ PV` (Teorema 4.1), logo `M[G]` tem sua própria função `|·|^{M[G]}`. Para
`w = ⟨ν_G(C_1),…,ν_G(C_ℓ)⟩`, `|w|^{M[G]}` é o comprimento do **código** (função PV interna)
da tupla de bits `(ν_G(C_1),…,ν_G(C_ℓ))`. Com a codificação de Cook (`⟨x_0,…,x_{ℓ-1}⟩` =
número cujos dígitos na base `2n+2` são `x_i + 1`; dígitos **≥ 1**), o comprimento do código
é determinado por `(ℓ, n)` com desvio `±1`:

> `|w|^{M[G]} ∈ {F(ℓ,n) − 1, F(ℓ,n), F(ℓ,n) + 1}`, onde `F(ℓ,n) := |⟨1,…,1⟩|` (tupla cheia
> de `ℓ` dígitos) é computável em p-tempo a partir de `(ℓ, n) ∈ M`.

### 1.3 Pegadinhas explícitas (as pedidas) — **(P)**

1. **`|w| ≠ ℓ` em geral** (trailing zeros / dígitos do código): o comprimento do *elemento*
   difere do comprimento do *nome* por `O(1)` (limitado por `F(ℓ,n)±1`). Inofensivo para
   `Log` (§2), porque `Log(M)` é fechado sob sucessor: se `k = |m| ∈ Log(M)` então
   `k+1 = |2^k| ∈ Log(M)` e `k−1 = |2^{k−2}| ∈ Log(M)` (`exp ∈ PV`, `2^k, 2^{k−2} ∈ M`).
2. **Comprimentos de tuplas não-alfabéticas**: aqui as tuplas são de **bits** `ν_G(C_j) ∈ {0,1}`
   — não há constantes `±` nem "tuplas não-alfabéticas" na versão `PV`. (Tal pegadinha só
   apareceria em codificações de outra natureza, ex.: estruturas ordenadas — não é o caso.)
3. **Elementos de `M` que não são números**: na versão `PV`, `M` é mono-sorted e **todos** os
   elementos de `M[G]` são números (códigos de tuplas de bits); `M ⊆ M[G]` literalmente, via
   **circuitos-constantes**: para `m ∈ M`, o nome `⟨bit_0(m),…,bit_ℓ(m)⟩` (circuitos constantes)
   avalia para o próprio `m`. Na versão `V^1_1` do livro (**dois sorts** `N`, `X`; ver §5) há
   elementos não-numéricos (conjuntos = tuplas características) e um **corte** `M*` — ver 5.3:
   lá `Log` exige cuidado extra (Pegadinha 5).
4. **`ν_G` é externo; `B(p)` é interno**: `[C]` é uma classe de equivalência *externa* (sobre
   a relation EF-em-`M`); `ν_G(C)` decide-a via pertinência em `G`. `ν_G` é um homomorfismo
   de avaliação: **`[C] = C^B([p_1],…,[p_n])`**, logo `ν_G(C) = C(ν_G(p_1),…,ν_G(p_n))` —
   **o valor de qualquer circuito é determinado pelos valores dos átomos**. Consequência
   decisiva para o §4: *fixar os átomos fixa tudo*.
5. **Casos limite**:
   - `ℓ = 0` (nome vazio): `w = 0`, `|w| = 1 = |2^0| ∈ Log(M)` ✓;
   - nomes **curtos** (`ℓ < |m|`): `w < 2^ℓ ≤ 2^{|m|-1} ≤ m/2` — elementos novos **abaixo de `m`**
     (é o mecanismo de (L3)); nada os impede de ser novos;
   - `ℓ = |m|`: `w` pode ficar abaixo ou acima de `m` conforme os bits altos;
   - nomes **longos** (`ℓ ≥ m`): `w` tipicamente `≥ m`.
   Todos os casos têm `ℓ ∈ M` (o nome é um elemento de `M`) — é isso que o §2 capitaliza.

---

## §2. Teorema (L1): `Log(M[G]) = Log(M)` — prova

> **Teorema 2.1 (L1) (P).** Na construção da §1.1 (com qualquer ultrafiltro `G` fechado sob
> EF-provability in `M`), vale `Log(M[G]) = Log(M)`, onde `Log(M[G]) = {|w|^{M[G]} : w ∈ M[G]}`
> e `Log(M) = {|m|^M : m ∈ M}`. Isto é: **medida a medida — todas as medidas de `M[G]` vêm
> de `M`**.

**Prova.**

**(⊇) `Log(M) ⊆ Log(M[G])`.** `M ⊆ M[G]` (§1.3, item 3: circuitos-constantes). E `|·|` é
absoluto em `M ⊆ M[G]` para parâmetros antigos: ambos são modelos de `PV`, isto é, ambos
interpretam as funções `PV` pelas funções p-tempo **reais**, logo `|m|^{M[G]} = |m|^M` para
todo `m ∈ M`. Logo `Log(M) ⊆ Log(M[G])`.

**(⊆) `Log(M[G]) ⊆ Log(M)`.** Seja `w ∈ M[G]` arbitrário. Pela definição, existe **nome**
`N = ⟨C_1,…,C_ℓ⟩ ∈ Names_M(p) ⊆ M` com `w = ⟨ν_G(C_1),…,ν_G(C_ℓ)⟩`. Então:
1. `ℓ = |N|^M ∈ M` (o nome é um elemento de `M`; o comprimento de uma sequência interna é
   um elemento interno — p-tempo);
2. pela §1.2, `|w|^{M[G]} ∈ {F(ℓ,n)−1, F(ℓ,n), F(ℓ,n)+1}` com `F(ℓ,n)` computável em p-tempo
   a partir de `(ℓ, n) ∈ M`, logo `F := F(ℓ,n) ∈ M`;
3. `F = |2^{F−1}|` com `2^{F−1} ∈ M` (exp ∈ PV) ⟹ `F ∈ Log(M)`; e `F±1 ∈ Log(M)` pela
   fechamento sob sucessor (§1.3, item 1; `2^F, 2^{F−2} ∈ M`);
4. logo `|w|^{M[G]} ∈ Log(M)`.

Como `w` era arbitrário, `Log(M[G]) ⊆ Log(M)`. ∎

> **Observação 2.2 ("medida a medida" = todas as medidas vêm de `M`) (P).** O ponto não é que
> `|w| = ℓ`; é que **`|w|` é `PV`-calculável a partir do nome `⟨C_1,…,C_ℓ⟩ ∈ M`** (função fixa
> `F` de `(ℓ,n)`, com desvio `±1`). Cada medida de `M[G]` é, portanto, "herdada" de um objeto
> velho. Note que isto **não** diz nada sobre *membership* de elementos abaixo de `m` — ver §4.

> **Observação 2.3 (não é automatismo; onde a prova usa hipóteses) (P).** A prova usa:
> (a) nomes `∈ M` (sem isso, `ℓ ∉ M` e o argumento morre); (b) codificação de Cook com
> dígitos `≥ 1` (sem isso, `|w|` poderia depender dos bits genéricos); (c) `exp ∈ PV`
> (fechamento de `Log` sob sucessor). Nenhuma hipótese sobre `G` além de fechamento EF é usada.

> **Advertência 2.4 (versão `V^1_1` do livro; Pegadinha 5) (P)+(C).** Na versão do livro
> (dois sorts; ver §5), `N^{M*[G]} = N^{M*}` (o sort numérico é o **corte** `N^{M*} =
> {v : ∃w ∈ N^M, v ≤ w}` de uma extensão elementar `M'` de `M`), e os elementos do sort `X`
> têm comprimento dentro do corte. Aí `Log(M*) = Log(M)` exige que o corte **não acrescente
> comprimentos novos**: se `v` no corte tiver `|v| ∉ M`, então `|v| ∈ Log(M*) \ Log(M)`
> (pois `|m| ∈ M` para todo `m ∈ M`, logo comprimentos fora de `M` não estão em `Log(M)`).
> Para extensões **end-extension** o corte é `N^M` e (L1) vale tal qual; no caso geral,
> **(L1) para a versão do livro é plausível mas não provado aqui** — `(C)`: é provável que a
> "additional requirement on M" inclua exatamente esta condição de fidelidade de comprimento
> do corte (§3).

---

## §3. (L1) ⟹ candidata a [Kra95, Thm 9.4.2]? E o "additional requirement on M"

### 3.1 Sim, é a candidata — mas (L1) não é o que exige requisito — **(P)**

**(L1)** mostra que a construção é "medida a medida": `Log(M[G]) = Log(M)` vale **sem nenhuma
hipótese extra sobre `M`** (só `M ⊨ PV` + `G` fechada). O próprio artigo atribui ao
"forcing construction underlying [7, Thm.9.4.2]" exatamente a produção de `Log(M') = Log(M)`
"(with an additional requirement on `M`)" **(A)**. Logo: **o requisito extra NÃO é sobre `Log`**
(que é de graça, pelo Teorema 2.1) — ele é sobre a **existência do genérico/da semente**.
Isto é consistente com a errata do livro (§5): o Thm 9.4.2 produz uma extensão
`(M', X')` Σ^{1,b}_0-elementar (+ modelo de `V^1_1`), construída por forcing w.r.t. um
**ordenamento parcial `P`** com um **corte** — as exigências técnicas aparecem aí.

### 3.2 As hipóteses plausíveis do "additional requirement on M" — **(A)** com justificativa

1. **`M` contável (ou ℵ₁-saturado / recursivamente saturado) (A).** [Kra95] §5 (frege.pdf),
   construção explícita: *"Assume that `M` is countable, and that `M` and `¬σ` satisfy (a)"*.
   Justificativa: o filtro genérico `G` (ou `G ⊆ P`) existe por genericidade sobre famílias
   **definidas em `M`**; para famílias internas não-triviais, a genericidade se obtém por
   enumeração (contagem) ou por saturação ℵ₁ (realização de tipos). O próprio artigo admite:
   *"it would suffice … for a sufficiently universal class of models (e.g. **countable or
   recursively saturated**)"* **(A)** — logo a contagem é **tolerável** para os propósitos do
   artigo, mas **não está no enunciado do Problema 2.1** (que pede todo `M ⊨ T_PV`).
2. **`SAT_n(M)` não reconhecível por circuito (em `M`) (A).** [Kra98, §4, 2ª prova do Thm 2.1]:
   *"Let `M` be a countable model of PV in which `SAT_n(M)` is not recognized by a circuit, and
   that admits a counterexample function in `P/poly`"*. Justificativa: o **Claim 1** (semente
   `T` sem refutação EF em `M`) usa exatamente isto — uma refutação EF de `T` combinaria os
   `W`'s e `Z`'s num circuito **em `M`** reconhecendo `SAT_n(M)`. Sem a não-reconhecibilidade,
   a semente é refutável e o forcing não arranca.
3. **Função counter-example em `P/poly` (A).** Usada no **encadeamento** `M ⊆ M₁ ⊆ M₂ ⊆ …`
   (iteração do Thm 2.1 de [Kra98]); para um único passo de extensão pode ser dispensável.
4. **Definabilidade no forcing (A — errata oficial!).** Errata 9.4.1/Claim 6 (p.174):
   *item (b) "should be stated for `u` bounded by any element (universally quantified) of the
   cut and not by the cut itself — this violates the required **definability of the sets in the
   forcing notion** (the partial ordering `P`)"*. I.e., as famílias de condições e o corte
   devem ser **definíveis em `M`** — restrição sobre `M` (e sobre o que se pode selar).
5. **Enumerabilidade de `T`/das condições (C).** Uma semente `T` não-padrão (como em [Kra98]:
   uma fórmula para cada nome `∈ M`) precisa ser "gerenciável" pelo argumento de genericidade;
   a contagem de `M` a cobre, mas para `M` arbitrário exigiria uma versão interna
   (família `Δ`-definável) — `(C)`: plausivelmente parte do item 4.

### 3.3 O que (L1) **não** entrega — **(P)**

(L1) não dá `M' ∋` falsificadores novos, não dá `(¬φ) ∈ SAT`, não dá `(8)`, e não dá
`M' ∩ m = M ∩ m` (nem a impede). É um lema de **contabilidade de medidas**, e é exatamente
por isso que `Log(M')=Log(M)` é **insensível** a elementos novos abaixo de `m` (F1, §2.1):
o balde de medida `k` tem `~2^k` elementos e `Log` controla só quais baldes existem.

---

## §4. Análise de (F-b') e do reparo (R1): resultado — **refutados**

### 4.1 Sem pinning: `M[G] ∩ m ⊋ M ∩ m` (confirma (L3)) — **(P)**

Nomes curtos existem em `M` (ex.: `⟨p_1,…,p_ℓ⟩` com `ℓ < |m|`, ou qualquer tupla de circuitos
de comprimento `ℓ < |m|`) e seus valores `⟨ν_G(C_1),…,ν_G(C_ℓ)⟩ < 2^ℓ ≤ 2^{|m|-1} ≤ m/2` são
**novos em geral** (a menos que `G` os coincida com strings antigas). Logo `M[G] ∩ m` contém
tipicamente `~2^{|m|}` elementos, dos quais `M ∩ m` é só parte: **(F-b') falha**.
Coerente com **(A)** [Kra16]: *"In the forcing from [17,15] one naturally adds **many new
elements into [n]** (and, in fact, does not include all of [n] from M into M′)"*.

### 4.2 (R1) ingênuo: colapso total da genericidade — **(P), Teorema**

> **Teorema 4.1 (colapso do pinning).** Seja `T_pin` um conjunto de condições que **fixa todos
> os nomes de comprimento `ℓ ≤ |m|−2` aos valores de um valuation fixo `v: p ↦ {0,1}`**
> ("valores-padrão"), i.e., `ν_G(C) = C(v)` para toda circuito `C` com `|C-nome| ≤ |m|−2`.
> Então `ν_G(p_i) = v(p_i)` para **todo** átomo `p_i`, e `M[G] = M`: a extensão é trivial.

**Prova.** Os átomos `p_i` **são nomes de comprimento 1** (item 4 da §1.3: `ν_G` é avaliação
em `B(p)`: `ν_G(C) = C(ν_G(p_1),…,ν_G(p_n))`). Fixar nomes curtos inclui fixar
`⟨p_i⟩`, `⟨p_i,p_j⟩`, … — em particular `ν_G(p_i) = v(p_i)`. Pelo item 4 da §1.3, daí segue
`ν_G(C) = C(v)` para **todo** circuito `C`, i.e., `ν_G` é a avaliação `v` — todo elemento de
`M[G]` é `⟨C_1(v),…,C_ℓ(v)⟩ ∈ M` (valores de circuitos sobre `v ∈ M` são elementos de `M`).
Logo `M[G] ⊆ M`; com `M ⊆ M[G]`, `M[G] = M` (trivial). ∎

> **Observação 4.2 (a "intrinsidade" do valor-padrão) (P).** O contexto já alertava: "o valor
> em `M` de um nome não é intrínseco (os átomos `p_i` são genéricos)". O Teorema 4.1 mostra que
> **qualquer** tentativa de fixar nomes curtos a valores fixos tem de fixar um valuation `v`
> dos átomos — e aí o forcing deixa de forçar.

### 4.3 Variantes propostas — todas refutadas pelo mesmo núcleo — **(P)**

- **"Só nomes sem átomos"** (fixar apenas nomes de circuitos-constantes): consistente, mas
  **não sela `[0,m)`** — nomes curtos *sobre átomos* continuam livres e dão elementos novos
  abaixo de `m/2`. Inútil para (F-b').
- **"Átomos distintos para semente e para nomes curtos"**: não escapa — nomes curtos
  **arbitrários** podem usar *qualquer* átomo. Argumento da **janela deslizante**: para
  `ℓ₀ := |m|−2`, o nome `⟨p_s, p_{s+1}, …, p_{s+ℓ₀−1}⟩` tem valor `< 2^{ℓ₀} ≤ m/4 < m`;
  selar `[0,m)` obriga esse valor a ser **antigo**, i.e., a decidir o bloco
  `p_s … p_{s+ℓ₀−1}`. Com `s = 1,2,…`, as janelas cobrem **todos** os átomos
  `p_1,…,p_N` (para `N ≥ ℓ₀`) — de volta ao Teorema 4.1.
- **"Comprimento mínimo dos átomos"**: irrelevante — nomes curtos podem repetir/construir
  qualquer átomo (`⟨C,…,C⟩`), e o que importa é o valor do nome, não o tamanho dos átomos.
- **`N < ℓ₀` (pouquíssimos átomos)**: a selagem deixa de decidir átomos, mas aí todo nome
  curto tem valor determinado por poucos bits e `M[G] ⊆ {poucas strings} ∪ … = M` —
  extensão trivial de novo.

### 4.4 O golpe de misericórdia: **(F-b') é refutado em geral** — **(P), Teorema**

> **Teorema 4.3 (refutação de (F-b')).** Seja `M ⊨ T_PV` modelando `S` ((S1)–(S4) de F2,
> em particular `π : P ⊢ α`, `α = ⋁̇_{i<m} α_i`, `∀i<m (¬α_i) ∈ SAT`) e `φ` sem prova em `M`
> (leitura de F2 §0: `φ(r) = ⋀_{i<m} ¬(r_i : P ⊢ α_i)` — sob a qual o artigo afirma
> `M' ⊨ σ_{i_0}:P ⊢ α_{i_0}` para algum `i_0 < m` **(A)**). Então **não existe** `M' ⊇ M` com
> `M' ⊨ T_PV`, `M' ⊨ (¬φ) ∈ SAT` **e** `M' ∩ m = M ∩ m`.

**Prova.** Suponha `M'` assim. `M' ⊨ (¬φ) ∈ SAT` dá falsificador `σ ∈ M'` com
`M' ⊨ ⋁_{i<m}(σ_i : P ⊢ α_i)`, i.e., existe `i_0 ∈ M'` com `i_0 <^{M'} m` e
`M' ⊨ σ_{i_0} : P ⊢ α_{i_0}` **(A)**. Por `(F-b')`: `i_0 ∈ M' ∩ m = M ∩ m`, logo `i_0 ∈ M`.
1. `(S4)` em `M`: `M ⊨ (¬α_{i_0}) ∈ SAT` — sentença `Σ^b_1` com parâmetros antigos
   `i_0, α ∈ M`; a testemunha é antiga e a avaliação de p-tempo é absoluta ⟹ **sobe**:
   `M' ⊨ (¬α_{i_0}) ∈ SAT`.
2. `Ref_P = "x:P⊢y → (¬y)∉SAT"` é universal-verdadeira, logo `Ref_P ∈ T_PV` **(A, F2 §0)**;
   `M' ⊨ T_PV` vale com **parâmetros novos** `σ_{i_0}, α_{i_0} ∈ M'` ⟹ `M' ⊨ (¬α_{i_0}) ∉ SAT`.
3. 1. e 2. contradizem-se. ∎

> **Corolário 4.4 (o passo do artigo é necessariamente falso) (P).** Se `M* ⊇ M` com
> `M* ⊨ (8)` (`∀i<m (¬α_i) ∈ SAT` com `∀` sobre `M* ∩ m`) e `M* ⊆ M' ⊨ T_PV`, então
> `i_0 ∉ M*` — pela mesma prova com `M*` no lugar de `M'` no passo 1. Logo a configuração
> assertada pelo artigo — *"`i_o` is also already in `M*` and hence by (8)"* — é **impossível**:
> ou `i_0 ∉ M*` (o passo "(7) ⟹ `i_0 ∈ M*`" falha, como já suspeitava F1), ou `M* ⊭ (8)` em
> `i_0` (a preservação alegada falha). Em qualquer caso a prova do Teorema 4 **não fecha** —
> a lacuna é **fatal**, não presentacional.
> **Ressalva honesta (P):** o Corolário usa a leitura de `φ` e de (8) de `F2_versao_finita.md`
> (que transcreve o artigo: `σ = (σ_i)_{i<m}`, `M' ⊨ σ_{i_0}:P⊢α_{i_0}`, `(8)` instanciável em
> `i_0`); se a numeração interna do v5 distinguisse "(8) só para `i ∈ M`", o passo do artigo
> estaria apenas sem fundamento (não refutado) — mas aí o Teorema 4 também não teria o insumo
> que precisa.

### 4.5 Colisão (R1) × semente σ, quantificada (antes do Teorema 4.3) — **(P)**

- `σ = (σ_i)_{i<m}` tem **nome** de comprimento `n ≈ m·b` com `b = |α|^c` (p-boundedness);
  como `|α| ≥ m` ⟹ `b ≫ |m|`; logo o nome de `σ` e os nomes canônicos dos blocos `σ_i`
  (comprimento `b`) estão **fora** do raio de pinning `ℓ ≤ |m|−2`. Formalmente **compatível**.
- Porém: `σ_{i_0}` **novo é obrigatório** — se `σ_{i_0} ∈ M` (nome curto ⟹ pinning ⟹ antigo),
  a absolutidade de `Prf_P` em parâmetros antigos daria `M ⊨ σ_{i_0}:P⊢α_{i_0}`, contradizendo
  `Ref_P`+`(S4)` em `M`. Isto é a **versão quantificada** da colisão: selar `[0,m)` empurra
  `σ_{i_0}` para `≥ m` (`σ_{i_0}` novo e grande), o que é formalmente viável — mas o
  **Teorema 4.3** mostra que mesmo assim a selagem + `(¬φ) ∈ SAT` é impossível em qualquer `M'`.
- **Veredito (R1):** refutado em todas as variantes naturalmente propostas. O forcing
  booleano de [Kra95]/[Kra98] **não** constrói `(F-b')`, e `(F-b')` não é construível por
  método algum (Teorema 4.3).

### 4.6 Consequência estratégica — **(P)**

Como `(F-b') ⟹ (F-sent)` (F2 §3) e `(F-b')` é **falso**, as hipóteses finitas viáveis são
apenas do tipo **`(F-sent)`/`(F-inst)`** — e o Teorema 4.3 mostra que elas **exigem** elementos
novos abaixo de `m` (`i_0 ∈ M' \ M` é obrigatório): a "janela" `[0,m)` **tem** de abrir-se.
Resta (R3): semear em `M[G]` testemunhas `(¬α_i) ∈ SAT` para **todo** `i ∈ M' ∩ m` — para
`i` antigo é de graça (`Σ^b_1` sobe); para `i` novo não há garantia, e cobrir `∀i<m` com
testemunhas é exatamente o conteúdo que `BB` daria de graça (indisponível) — ou seja, o forcing
só entregaria `(F-sent)` semeando-a **diretamente** (monolítico), o que recai na dificuldade
do enunciado. Rota (R4) ([Kra16]: preservar a teoria de primeira ordem de `A_W`) permanece a
alternativa endossada pela literatura.

---

## §5. Busca do enunciado de [Kra95, Thm 9.4.2] — o que se obteve (e o que não)

### 5.1 O que NÃO se obteve (honestidade total) — **(P)**

- **Enunciado verbatim do Teorema 9.4.2 (p.175): não obtido.** O livro está pago (Cambridge
  Core) e no Internet Archive (`boundedarithmeti0000kraj`, empréstimo) com OCR **bloqueado**
  (djvu.txt e "search inside" retornam 403); Google Books API indisponível nesta rodada
  (rate-limit 429); o PDF do hbz-nrw (`kra95_book.pdf`) contém **só o sumário** (que confirma
  §9.4 = "Model-theoretic constructions", pp. 172–180, e §12.7 "Forcing in nonstandard models",
  §13.3 "Boolean valuations"). Errata via ORCID: link Proton Drive não acessível por script;
  mas a mesma errata está (acessível e baixada) em `karlin.mff.cuni.cz/~krajicek/`.

### 5.2 O que SE obteve — **(A)**

1. **Errata oficial do livro** (`upravy.html` + `err.pdf`; arquivos em `fontes/`), trechos
   **verbatim** sobre a §9.4:
   - *"9.4.1, Claim 6, p.174: item (b) should be stated for 'u' bounded by any element
     (universally quantified) of the cut and not by the cut itself — this violates the required
     definability of the sets in the forcing notion (the partial ordering `P`)."*
   - *"9.4.2, p.175: The extension `(M', X')` is not only `Σ^{1,b}_0`-elementary but also a
     model of `V^1_1`."*
   ⇒ **Conteúdo do Thm 9.4.2**: produz, por forcing w.r.t. um ordenamento parcial `P`
   (com um **corte** e famílias **definíveis em `M`** — Claim 6 de 9.4.1), uma extensão
   `(M', X')` que é `Σ^{1,b}_0`-elementar (e, pela correção, modelo de `V^1_1`). Os objetos
   `(M', X')` são de **dois sorts** — versão `V^1_1`, não `PV`.
2. **A construção-fonte correspondente, integral**: [Kra95], *On Frege and Extended Frege Proof
   Systems* (≈ o §9.4 do livro; [Kra98] diz: Thm 4.1 é "a special case of [5, Thm 5.1]", ver
   também "[4, Chpt. 9.4]"), `fontes/kraj95_frege.{pdf,txt}`, Seção 5 "A Forcing Construction":
   `M` contável; extensão elementar `M'` com `t` cofinal; corte `M*` (`N^{M*} = {v : ∃w ∈ N^M, v ≤ w}`);
   átomos novos `q_γ` para cada fórmula booleana `γ`; `C*` = tuplas com comprimento **no corte**;
   `G` satisfazendo (1)–(5) (inclusive (5): indução `Σ^{1,b}_1`); `M*[G] := (N^{M*}, C*/~)` com
   `~` dado por `⟨φ₁⟩_u = ⟨φ₂⟩_u ∈ G`; Claims 1–7; final: ultrafiltro `F` em `B` (abertos
   regulares de `P`) e valoração booleana — **e a observação final**: "the boolean values are
   assigned only to formulas from `Fle*` and not to all formulas from `Fle`. In fact, **there
   is no apparent way how to extend consistently the valuation `ν` to `Fle`**" (as
   valorações booleanas são **parciais** — tema da Seção 6 do artigo e do finitização).
3. **[Kra98, §4] verbatim** (`fontes/kra98_full.txt`): base da §1; Teorema 4.1; Claims 1–2;
   e a hipótese explícita da aplicação: *"Let `M` be a **countable** model of `PV` in which
   `SAT_n(M)` is not recognized by a circuit, and that admits a counterexample function in
   `P/poly`"* (base do §3.2).

### 5.3 Confronto com (L1)/(R1) — **(P)**

- **(L1) × Thm 9.4.2**: na versão do livro, comprimentos vêm do **corte** (`C*` exige
  `|α| ∈ N^{M*}`) — i.e., "medida a medida" **com o corte como intermediário**; `Log`-preservação
  exige o corte não acrescentar comprimentos (Advertência 2.4) — coerente com a errata (exigências
  técnicas sobre `P`/corte) e com o "additional requirement on M" do artigo.
- **(R1) × Thm 9.4.2**: o colapso do §4.2 usa só `ν_G(C) = C(ν_G(p))` e nomes `∈ M` — vale
  igualmente na versão do livro (lá as "condições" são atribuições parciais em `P`; selar
  `[0,m)` obriga a decidir todos os átomos curtos → genericidade trivial). Além disso, o
  **Teorema 4.3** é independente de qualquer forcing: `(F-b')` é impossível para
  `M' ⊨ T_PV + (¬φ) ∈ SAT`. ⇒ Nenhuma versão do Thm 9.4.2 pode entregar `(F-b')` com semente.

---

## §6. Veredito e próximos passos

### 6.1 Veredito (≤ 600 palavras) — **(P)**

1. **(L1) é verdadeiro e provado (Teorema 2.1).** Na construção booleana de [Kra95]/[Kra98]
   (`M[G]` com nomes `∈ M`), `Log(M[G]) = Log(M)`: toda medida de `M[G]` é calculável via PV
   a partir de um nome velho (`|w| ∈ {F(ℓ,n)±1}`, com `(ℓ,n) ∈ M`). A construção é, no que
   diz respeito a `Log`, **"medida a medida" sem nenhuma hipótese extra sobre `M`** — as
   pegadinhas (`|w| ≠ ℓ`, codificação, sorts) foram tratadas e não quebram o lema. Ressalva
   única: na versão `V^1_1` do livro (dois sorts + corte), `Log`-preservação exige que o corte
   não acrescente comprimentos — `(C)`, provavelmente parte do "additional requirement".
2. **O "additional requirement on M" do artigo não é sobre `Log`** (que é de graça): é sobre a
   **existência do genérico/da semente**. Candidatos com base sólida: `M` **contável** (ou
   ℵ₁-/recursivamente saturado) — [Kra95] §5 e o próprio artigo ("countable or recursively
   saturated"); **`SAT_n(M)` não reconhecível por circuito** — Claim 1 de [Kra98]; função
   counter-example em `P/poly` (iteração); e **definabilidade das famílias no ordenamento
   parcial `P`** — errata oficial 9.4.1/Claim 6. O enunciado verbatim do Thm 9.4.2 não foi
   obtido (livro pago; IA restrito), mas a errata fixa seu conteúdo: extensão `(M', X')`
   `Σ^{1,b}_0`-elementar e modelo de `V^1_1`, por forcing com corte.
3. **(R1) é refutado** (Teorema 4.1): fixar nomes curtos aos valores-padrão fixa os átomos
   (que *são* nomes de comprimento 1) e colapsa `ν_G` — `M[G] = M`, sem falsificador. Variantes
   (átomos distintos, comprimento mínimo) não escapam (janela deslizante). A colisão com a
   semente `σ` é, formalmente, inofensiva em comprimentos (`nome(σ) ≈ m·b ≫ |m|`), mas
   irrelevante dada a refutação seguinte.
4. **(F-b') é refutado em geral** (Teorema 4.3), e esta é a achada central: se `M' ⊨ T_PV +
   (¬φ) ∈ SAT` então `M' ∩ m ⊋ M ∩ m` **necessariamente** — o índice `i_0` do falsificador é
   **sempre novo** (`i_0 ∈ M' \ M`). Corolário: o passo do artigo "by (7) `i_o` is also already
   in `M*`" (v4 **e** v5/LMCS) não é só não provado — a configuração que afirma é **impossível**
   quando `M* ⊨ (8)` (Corolário 4.4): a prova do Teorema 4 tem lacuna **fatal**. Isso confirma
   e fecha a suspeita de F1/F2 com um teorema de impossibilidade.
5. **Estratégia corrigida**: as únicas hipóteses finitas vivas são `(F-sent)`/`(F-inst)`, e elas
   **pressupõem** a abertura da janela `[0,m)` para elementos novos (obrigatório, item 4).
   O forcing booleano candidato-seja ele o do Thm 9.4.2, seja a versão `PV` de [Kra98]—
   entrega `(L1)` de graça, entrega `(L2)`-tipo semente quando `T` não tem refutação EF em `M`,
   mas **não** entrega `(F-sent)` sem semear testemunhas para `∀i<m` (o papel de `BB`).
   A correção do Teorema 4 deve ser a **troca 2.1 → (F-sent)** (como já propunha F2), com
   (F-sent) assumido nua e monoliticamente; a rota alternativa endossada por [Kra16]
   (preservação de teoria de primeira ordem de `A_W`, (R4)) permanece o plano B.

### 6.2 Próximos passos concretos — **(P)/(C)**

1. **Fechar o enunciado verbatim do Thm 9.4.2** (última pendência da §5): Google Books
   (desbloquear rate-limit), Cambridge Core (preview do cap. 9), ou empréstimo do IA por
   conta humana; confrontar com a Advertência 2.4 (corte × comprimentos).
2. **Publicar/precisar o Teorema 4.3** na linguagem exata do v5 (v4↔v5 renumeração):
   redigir a refutação de `(F-b')` e o Corolário 4.4 como nota curta ao autor (Krajíček já
   responde F1; ver `F1_verificacao_passo7.md` §5 — o email está pronto; acrescentar o
   Teorema 4.3).
3. **(F-sent) construtivo?** Semear em `M[G]` testemunhas `(¬α_i) ∈ SAT` para `i` novos:
   modelar o custo da semente (uma condição por `i`? colapsa em "collections"); verificar se
   a saturação ℵ₁ de `M` (do §3.2) ajuda a semear o `∀i<m` inteiro de uma vez — `(C)`.
4. **Testar a Advertência 2.4**: construir (ou refutar a existência de) uma extensão elementar
   não-end-extension `M'` de `M ⊨ PV` cujo corte acrescente comprimento novo — decidir se a
   "additional requirement" do livro é exatamente essa fidelidade de comprimento.
5. **Documentar em `G_CONTEXTO_FORCING.md`** os resultados desta rodada ((L1) provado;
   (R1)/(F-b') refutados; errata localizada) para as demais frentes.

### 6.3 Lacunas honestas — **(P)**

- Enunciado verbatim de [Kra95, Thm 9.4.2]: **não obtido** (§5.1).
- (L1) para a versão `V^1_1` com corte **não-end-extension**: **não provado** (Advertência 2.4).
- Consistência da semente tipo (L2) ("`T` sem refutação EF em `M`" nas aplicações ao
  artigo-alvo): **não provada aqui** — depende de `SAT_n(M)` não reconhecível (o que `M ⊨ T_PV`
  não garante) e é o verdadeiro ponto onde o "additional requirement" aperta.
- O Corolário 4.4 condiciona-se à leitura de (8)/`φ` de `F2_versao_finita.md` (transcrição do
  artigo) — se o v5 a alterasse, reavaliar.

---
*Fontes novas salvas em `fontes/`: `kraj95_frege.{pdf,txt}` (construção-fonte §5), `kra98_full.txt`
(§4 verbatim), `krajicek_upravy.html` + `kraj_err.{pdf,txt}` (errata oficial), `kra95_book.pdf`
(só sumário).*

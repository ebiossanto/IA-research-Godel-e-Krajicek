# F2 — A versão finita/combinatória do Problema 2.1 e o lema de suficiência finita

**Arquivo:** `F2_versao_finita.md` (subagente, rodada de 10 Out 2026).
**Fonte primária:** `F_CONTEXTO_ATAQUE.md` — transcrição verbatim do artigo (arXiv:2506.20221v4, §3,
item (5) da prova do Teorema 4) e da definição `Log(M) = {|m| | m ∈ M}`.
**Marcação:** **(A)** = artigo (transcrição/resumo do texto do artigo); **(P)** = demonstração própria;
**(C)** = conjectura / hipótese de trabalho não verificada.
**Regra:** português; entregável apenas neste arquivo.

---

## §0. Configuração fixa e notação

Objetivo deste documento: mostrar que **toda a máquina `M*` + `Log` + preservação do esquema
`Σ^b_1` pode ser substituída por uma ou duas sentenças finitas sobre `M'`**, e que a passagem
final do item (5) da prova do Teorema 4 fecha sem elas.

Notação fixa ao longo de todo o texto:

- **`P`** — sistema de prova **strong** e **p-bounded**, escolhido no item (1) da prova do
  Teorema 4 **(A)**.
- **`T_PV`** — teoria universal dos cálculos polinomiais; contém **toda a teoria universal
  verdadeira em `L_PV`** **(A, contexto §3, E1)**. Consequência usada à vontade: toda sentença
  universal verdadeira no mundo padrão vale em qualquer `M' ⊨ T_PV`, com **quaisquer parâmetros
  de `M'`**.
- **`Ref_P`** — a sentença universal verdadeira
  `∀x∀y ( x:P⊢y → (¬y)∉SAT )` **(A)**. Logo `Ref_P ∈ T_PV` **(P)**.
- **`m ∈ M`** — comprimento da disjunção; **`α = ⋁̇_{i<m} α_i ∈ M`** — disjunção **disjunta**
  (axioma (S2)); **`π ∈ M`** — derivação `π : P ⊢ α` (axioma (S3)) **(A)**.
- **`S`** — a teoria do item (2) da prova do Teorema 4 **(A)**, cujos axiomas são:
  - (S1) todos os axiomas de `T_PV`;
  - (S2) `α = ⋁̇_{i<m} α_i` (disjunção disjunta);
  - (S3) `π : P ⊢ α`;
  - (S4) `∀i<m (¬α_i) ∈ SAT` — é exatamente a sentença (8) do artigo **(A)**.
- **`φ = φ(r)`** — a fórmula que não tem prova em `M`. Leitura reconstruída do passo (5) **(P)**:
  `φ(r)` é a conjunção indexada de afirmações de **não-prova**,
  `φ(r) ≡ ⋀_{i<m} ¬( r_i : P ⊢ α_i )`. Daí que um falsificador de `φ` é obrigatoriamente uma
  "lista de candidatos a prova" que **contém** uma prova em algum índice — é literalmente o que o
  artigo declara: *"`σ = (σ_i)_{i<m}` and we have `M' ⊨ σ_{i_0}:P ⊢ α_{i_0}` for some `i_0 < m`"*
  **(A)**.
- **`M ∩ m := { x ∈ M | x < m }`**; idem para `M' ∩ m`.
- **`θ ∈ SAT`** é `Σ^b_1` (existe atribuição falsificante) **(A/P)**; logo `¬φ ∈ SAT` é `Σ^b_1`
  e a sentença (8) `∀i<m (¬α_i) ∈ SAT` é `Π^b_2` (matriz `Σ^b_1` sob limitador) **(A, contexto §4A)**.

Fatos de transferência usados sem cerimônia **(A, contexto §3)**:

- `Σ^b_1` (matriz aberta/`∃`) **sobe**: `M ⊆ M'`, `M ⊨ θ ⟹ M' ⊨ θ` para `θ ∈ Σ^b_1`.
- Sentenças **universais** descem: `M* ⊆ M'`, `M' ⊨ θ ⟹ M* ⊨ θ` para `θ` universal.
- Subestrutura de modelo de teoria universal é modelo: `M* ⊆ M' ⊨ T_PV ⟹ M* ⊨ T_PV`, em
  particular `M* ⊨ Ref_P` **(A, contexto §3 E1)**.

---

## §1. Formulações finitas

### (F-b') — versão membership / domínio

> **(F-b') (P, a partir da variante (b') da Equipe E).** Dados `M ⊨ T_PV` **não-padrão** modelando
> a teoria `S` do item (2) (axiomas (S1)–(S4) acima) e uma fórmula `φ` sem prova em `M`,
> **existe** `M' ⊇ M` tal que
>
> 1. `M' ⊨ T_PV`;
> 2. `M' ⊨ (¬φ) ∈ SAT`;
> 3. **`M' ∩ m = M ∩ m`** (nenhum elemento novo abaixo de `m`).

### (F-sent) — versão sentença (o alvo minimalista)

> **(F-sent) (P).** Dados `M ⊨ T_PV` não-padrão modelando `S` e `φ` sem prova em `M`,
> **existe** `M' ⊇ M` tal que
>
> 1. `M' ⊨ T_PV`;
> 2. `M' ⊨ (¬φ) ∈ SAT`;
> 3. **`M' ⊨ ∀i<m (¬α_i) ∈ SAT`**, ou seja, `M' ⊨ (8)` — o último axioma de `S` vale **em `M'`**.

### Por que ambas são condições **finitas** **(P)**

1. **Número finito de exigências.** Cada uma é um par (trio) de sentenças da forma `M' ⊨ θ`.
   Não há quantificação sobre estruturas, nem sobre todos os modelos, nem sobre comprimentos.
2. **Parâmetros fixos e finitos.** Todo `θ` envolvido tem parâmetros tomados da lista finita
   `π, α, m, φ` (mais `i_0, α_{i_0}` no uso), todos elementos de `M`, fixados **antes** de
   construir `M'`. Nenhum elemento de `M' \ M` é mencionado na hipótese.
3. **Nenhuma igualdade global de estruturas.** A condição extra de (F-b') é uma igualdade de
   *domínios recortados em `m`* (`M' ∩ m = M ∩ m`), isto é, uma condição sobre a fibra de um
   único elemento `m`; não é uma igualdade de funções, relações, `Log` ou teorias.
4. **Contraste com o Problema 2.1 original (A).** O Problema 2.1 exige:
   (i) uma cadeia `M ⊆ M* ⊆ M'`; (ii) a preservação de **todo o esquema** `Σ^b_1(PV)` de `M`
   para `M*` (infinitamente muitas sentenças); (iii) `Log(M*) = Log(M')`, uma igualdade de dois
   **conjuntos de comprimentos** — afirmação sobre o universo inteiro, **não expressível** como
   satisfação de uma sentença fixa. As formulações finitas trocam "esquema + igualdade global"
   por "uma ou duas sentenças com parâmetros em `M`".

---

## §2. Teorema principal — o lema de suficiência finita

> **Teorema (lema de suficiência finita) (A)+(P).** Suponha **(ST)** (a afirmação do artigo que é
> contradita por um estudante `p`-tempo resolvendo `DD_P` em `O(1)` rodadas), e que existe `P`
> **strong** e **p-bounded** satisfazendo (ST). Se **(F-sent)** vale para **todo** `M` modelando
> `S`, então `NP ≠ coNP`.

### Prova — itens (1)–(4) **(A)**

**(1)** Sob `NP = coNP`, escolhe-se `P` **strong**, **p-bounded**, satisfazendo (ST) **(A)**.

**(2)** Considere a teoria `S` com axiomas (S1)–(S4) da §0 **(A)**. Se `S` fosse **inconsistente**,
o Teorema de Krajíček–Pudlák (KPT 1990, Teorema 3 do artigo) produziria um
**estudante `p`-tempo resolvendo `DD_P` em `O(1)` rodadas**, contrariando (ST) **(A)**. Logo `S`
é consistente.

**(3)** Sendo consistente, `S` tem modelo; toma-se um modelo **não-padrão** `M ⊨ S` (o caráter
não-padrão de `M` é o que garante `m` não-padrão, sem a qual a disjunção seria finita e o problema
degenera) **(A)**.

**(4)** A fórmula **universal** `A_Q` é verdadeira em `M` **por `p`-boundedness de `P`** **(A)**.
Substituindo `x := π`, `y := α` (ambos em `M`, pelos axiomas (S2)–(S3)) obtém-se
**`M ⊨ Q ⊬ φ(r)`**, isto é, **`φ` não tem prova em `M`** **(A)**. É exatamente a hipótese de
(F-sent).

Até aqui nada mudou em relação ao artigo; a única alteração está no item (5).

### Item (5) reescrito com (F-sent) **(P)**

Por hipótese (F-sent) aplicada a esse `M` e essa `φ`, existe `M' ⊇ M` com:

> **(a)** `M' ⊨ T_PV`, `M' ⊨ (¬φ) ∈ SAT` e `M' ⊨ ∀i<m (¬α_i) ∈ SAT` (= (8) vale **em `M'`**).

> **(b)** De `(¬φ) ∈ SAT` em `M'`: existe falsificador `σ ∈ M'` com `M' ⊨ ¬φ(σ)`. Pela leitura de
> `φ` como conjunção de "não-prova" (§0), isso força um índice `i_0 < m` (no sentido de `M'`)
> com **`M' ⊨ σ_{i_0}:P ⊢ α_{i_0}`** **(A)**. Note: `σ_{i_0}` e `α_{i_0}` são projeções `p`-tempo
> de `σ, α, i_0`, logo estão em `M'`.

> **(c)** Como `i_0 ∈ M'` e `i_0 < m`, a sentença universal (com limitador) (8) de (a) instancia
> em `i_0`: **`M' ⊨ (¬α_{i_0}) ∈ SAT`** **(P)**.

> **(d)** `Ref_P = "x:P⊢y → (¬y)∉SAT"` é sentença **universal verdadeira**, logo pertence à teoria
> universal verdadeira `T_PV` **(A, contexto E1)**, logo vale em `M'` (pois `M' ⊨ T_PV`) com
> **quaisquer parâmetros de `M'`**; em particular com `σ_{i_0}, α_{i_0} ∈ M'`:
> `M' ⊨ σ_{i_0}:P⊢α_{i_0} → (¬α_{i_0}) ∉ SAT` **(P)**.

**(b)** dá a antecedente; **(c)** dá a negação da consequente. **Contradição** **(P)**.

Toda a derivação foi feita **dentro** da hipótese `NP = coNP` (com (ST), `P` strong/p-bounded e
(F-sent)); como a contradição é real, a hipótese é falsa e conclui-se **`NP ≠ coNP`** **(A)+(P)**. ∎

### O que **não** é usado **(P)**

No item (5) reescrito **não aparecem**:

1. o submodelo intermediário **`M*`** (nunca é construído nem referido);
2. a igualdade **`Log(M*) = Log(M')`** (condição (iii) de 2.1) — e, por consequência, nenhum
   forcing do tipo Krajíček 1995, Thm 9.4.2 **(A, [7])**;
3. a preservação de **todo** o esquema `Σ^b_1(PV)` (condição (ii) de 2.1);
4. a transferência `M → M* → M'` (o "detour" que levava (8) até a posição em que `Ref_P` pudesse
   vê-la);
5. o passo frágil **"`by (7) i_0 is also already in M*`"** **(A)** — não há `M*`, logo não há de
   onde deduzir `i_0 ∈ M*`: `i_0 ∈ M'` já basta, porque (8) vale em `M'`.

---

## §3. Implicações entre formulações

### (F-b') ⟹ (F-sent) **(P)**

Seja `M'` como em (F-b'). Tome `i ∈ M'` qualquer com `i <^{M'} m`.

1. Pela condição de domínio, `i ∈ M' ∩ m = M ∩ m`, logo `i ∈ M` e `i <^{M} m`
   (como `M ⊆ M'` é subestrutura, `<` é herdado: `<^{M'} ∩ M² = <^{M}`) **(P)**.
2. Pelo axioma (S4) de `S`, `M ⊨ (¬α_i) ∈ SAT`; os parâmetros `i, α_i, α ∈ M` **(P)**.
3. `(¬α_i) ∈ SAT` é `Σ^b_1`, portanto **sobe**: `M ⊆ M'` dá `M' ⊨ (¬α_i) ∈ SAT` **(A)**.
4. `i` era arbitrário com `i < m` em `M'`; logo `M' ⊨ ∀i<m (¬α_i) ∈ SAT` **(P)**.

Junto com `M' ⊨ T_PV` e `M' ⊨ (¬φ) ∈ SAT` (comuns às duas formulações), isso é exatamente
(F-sent). ∎

Observação: **as testemunhas de cada instância vêm de `M`** (elementos antigos, uma a uma) e
sobem por preservação `Σ^b_1` para cima; o que a condição de domínio garante é que **não existem
índices novos a cobrir**. Em outras palavras, (F-b') converte o `∀i<m` (infinito do ponto de
vista não-padrão) num `∀i<m` sobre `M ∩ m`, que é "antigo" **(P)**.

### O Problema 2.1 original ⟹ (F-sent)? **(A)+(C)**

Seja **(F-inst)** a condição fraca: *"`M' ⊨ (¬α_{i_0}) ∈ SAT` para o índice `i_0` produzido pelo
falsificador `σ`"*. Então:

- **2.1 ⟹ (F-inst)** **se** o passo "`by (7) i_0 is also already in M*`" do artigo for válido
  **(A)**: `i_0 ∈ M*` + `M* ⊨ (8)` (que o artigo obtém por preservação fraca `Σ^b_1`) dá a
  instância em `M*`, que **sobe** para `M'` por `Σ^b_1`. Note que (F-inst) é **tudo** que o
  item (5) original consome de 2.1.
- **2.1 ⟹ (F-sent) não segue.** (F-sent) exige a instância para **todo** `i < m` **em `M'`**,
  inclusive para `i ∈ M' \ M` com `i < m`. A igualdade `Log(M*) = Log(M')` **não** exclui tais
  `i` novos (contexto §2: um `j ∈ M'\M*` com `j < m` tem `|j| ≤ |m|`, comprimento já presente em
  `Log(M)`), e (8) foi estabelecida em `M*`, não em `M'`; `Π^b_2` **não desce** nem **sobe**
  automaticamente (a matriz `Σ^b_1` só sobe, e os `i` novos nem estão em `M*`) **(P)**.
- **Ressalva central (C).** O passo "`(7) ⟹ i_0 ∈ M*`" é **questionável** — é exatamente o ponto
  que a F1 da equipe está verificando. `Log` é o conjunto das **medidas** de `M*`, e a igualdade
  de medidas não impede elementos novos curtos (contexto §2, leituras (L1)/(L2)/(L3)). **Se o
  passo for lacunoso, 2.1 nem mesmo entrega (F-inst)** e, nesse caso, **(F-sent) é uma hipótese
  independente**: o Teorema do §2 continua valendo, mas o item (5) original fica **em aberto** e
  a "correção" do artigo passa a ser justamente a troca 2.1 → (F-sent) **(P)**.

Inversos: (F-sent) **não** implica 2.1 (exige bem menos) e **não** implica (F-b') (não controla
o domínio). A cadeia que se demonstra é apenas `(F-b') ⟹ (F-sent)` **(P)**.

---

## §4. Comparação de força (honesto)

| | Problema 2.1 original | (F-sent) |
|---|---|---|
| O que exige de `M'`/`M*` | cadeia `M ⊆ M* ⊆ M'`; **todo** o esquema `Σ^b_1(PV)`; **`Log(M*) = Log(M')`** | **uma única sentença** extra: `M' ⊨ (8)`, com parâmetros `m, α ∈ M` |
| Custo de enunciado | global (estruturas inteiras, infinitas sentenças, igualdade de conjuntos) | local (uma sentença `Π^b_2` com parâmetros fixos) |
| Caminho até a contradição | frágil: `(7) ⟹ i_0 ∈ M*` (não demonstrado), depois `M* → M'` por `Σ^b_1` | direto: instanciar (8) em `i_0 ∈ M'` e aplicar `Ref_P` em `M'` |
| Número de peças móveis | `M*`, `Log`, forcing ([7], Thm 9.4.2) | zero peças móveis |

Comentário **(P)**:

1. **2.1 exige muito e entrega por um caminho frágil.** Toda a riqueza (esquema + `Log`) existe
   só para transportar **uma instância** de (8) de `M` até `i_0` em `M'`; e o transporte passa
   por um passo que o próprio texto comprime ("by (7) ..."), o ponto hoje sob investigação.
2. **(F-sent) exige uma única sentença extra em `M'` — e ela é o "missing reflection" em forma
   pura.** Transformar `∀i<m ∃y F(i,y)` (a forma "coletada" de (8), `Π^b_2`) em **testemunhas
   presentes em `M'`** é exatamente o que o forcing/genericidade fazia disfarçadamente: o esquema
   BB (Cook–Thapen) daria `M ⊨ ∃z∀i<m F(i,(z)_i)` (que é `Σ^b_1` e **sobiria** para `M'`
   automaticamente), mas BB **não está disponível** **(A, contexto §4B)**. (F-sent) pede,
   explicitamente, o que BB daria de graça: é o mesmo conteúdo, só que enunciado como hipótese
   construtiva sobre `M'` em vez de deduzido.
3. **Qual é mais plausível?** **(C)** Nenhum dos dois é conhecido como construível; mas:
   - a exigência `Log(M*) = Log(M')` é *global* e o único uso dela no artigo é um passo de
     pertinência de um único índice — um "canhão para matar um pardal" cujo gatilho não está
     demonstrado;
   - (F-b') (`M' ∩ m = M ∩ m`) evita novos índices, mas `m` é **não-padrão**: "selar" o segmento
     inicial `[0,m)` é uma exigência sobre um recorte infinito do ponto de vista das condições de
     forcing, de custo comparável ao de `Log`;
   - (F-sent) é a única que **reduz tudo a uma sentença sobre `M'`**, sem estrutura intermediária
     e sem contabilidade de medidas. Como alvo de ataque, é a mais **enxuta**; como exigência de
     construção, continua **difícil** (cobrir `∀i<m` testemunhas), porém agora *monolítica*:
     ou se semeia a sentença inteira, ou nada.
   Leitura de trabalho: **(F-sent) é mais plausível como hipótese nua**, porque ela é
   *exatamente* a instância global que a prova consome e nada mais; 2.1 é mais plausível como
   *construção* (forcing entrega `Log` barato), mas a ligação 2.1 → item (5) é que está em
   suspensão.

---

## §5. A "lista finita de parâmetros"

### 5.1 O que o item (5) realmente consome **(P)**

Releia a prova do §2 e liste tudo que é **usado**:

- de `M`: `π` (axioma (S3)), `α` (axioma (S2) e parâmetro de `Ref_P`), `m` (limite do `∀` e da
  disjunção), `φ` (a sentença `¬φ ∈ SAT`);
- de `M'`: o falsificador `σ`, o índice `i_0`, os termos `σ_{i_0}` e `α_{i_0}`.

Note que `σ` entra **apenas em `M'`**; a hipótese nunca precisa dizer `σ ∈ M*`.

### 5.2 Teorema do colapso: exigir `σ ∈ M*` é refutado **(P)**

> **Teorema (colapso).** Nas hipóteses do item (5) (2.1 ou (F-sent), com `M* ⊆ M'`,
> `M* ⊨ T_PV`, `M*` fechado sob funções `PV`, e `M* ⊨ (8)` como afirma o artigo), **não existe**
> `M*` contendo o falsificador `σ`.

**Demonstração.** Suponha `σ ∈ M*`.

1. **`i_0 ∈ M*`.** `σ` codifica a tupla `(σ_i)_{i<m}`, logo `m ≤ |σ|`. A busca
   *"menor `i < m` tal que `(σ)_i` é `P`-derivação de `α_i`"* percorre no máximo `m` índices e
   cada verificação é `p`-tempo em `(|σ|, |α|)` — portanto o custo total é
   `O(m · poly(|σ|+|α|)) ⊆ poly(|σ|+|α|)`: **`i_0` é `p`-tempo decodificável de `(σ, α, m)`**.
   Cálculos `p`-tempo são absolutos em modelos de `PV` (as funções são interpretadas pelas
   funções reais), e o mundo padrão também encontra tal `i`, porque
   `M' ⊨ σ_{i_0}:P⊢α_{i_0}` com verificação `p`-tempo absoluta. Como `M*` é subestrutura fechada
   em `PV`, **`i_0 ∈ M*`**.
2. **`α_{i_0} ∈ M*`.** `α_{i_0} = (α)_{i_0}` é `p`-tempo em `(α, i_0) ∈ M*`; fechamento `PV`.
3. **Instância de (8) em `M*`.** `i_0 ∈ M*`, `i_0 < m` (`m ∈ M*`), e `M* ⊨ (8)` **(A)**, logo
   `M* ⊨ (¬α_{i_0}) ∈ SAT`.
4. **Sobe para `M'`.** `(¬α_{i_0}) ∈ SAT` é `Σ^b_1` com parâmetro `α_{i_0} ∈ M*` ⟹
   `M' ⊨ (¬α_{i_0}) ∈ SAT`.
5. **Contradição em `M'`.** O falsificador dá `M' ⊨ σ_{i_0}:P⊢α_{i_0}` **(A)**; `Ref_P ∈ T_PV`
   vale em `M'` com esses parâmetros **(A)**; logo `(¬α_{i_0}) ∉ SAT` em `M'` — contradição com
   o passo 4. ∎

**Análise crítica da rota encurtada (P).** O resumo do brief diz *"`Ref_P` em `M*` contradiz
`σ_{i_0}:P⊢α_{i_0}`"*; isso tem **uma lacuna**: `σ_{i_0}:P⊢α_{i_0}` é `Σ^b_1` e só sabemos que
vale **em `M'`** — `Σ^b_1` **não desce** para `M*` (só `Π` desce). É `Δ`/atómico? Não: `P⊢` é
`∃z` (existe derivação), e o testemunho `z` pode estar em `M' \ M*`. **A contradição tem de ser
montada em `M'`**, como fizemos acima; a conclusão (colapso) é a mesma, mas a rota correta é
`M* →(Σ^b_1)→ M'`, não `Ref_P` dentro de `M*`.

**Consequência.** `σ ∈ M*` é **insatisfazível** sob as hipóteses correntes (sob `NP = coNP`).
Portanto uma "condição finita" que exigisse `σ ∈ M*` **não seria um relaxamento**: estabelecê-la
já provaria `NP ≠ coNP`, o que a torna **vazia como hipótese de trabalho** e inconstruível pelo
forcing. É por isso que a exigência é **refutada por colapso** **(P)**.

### 5.3 Por que `σ` deve ficar fora de `M*` **(P)**

- `σ` é o **falsificador de `φ`**, isto é, a testemunha de `(¬φ) ∈ SAT` — sentença que, pela
  construção, **só vale em `M'`** (`φ` não tem prova em `M`, e nada em `S` dá `M ⊨ (¬φ) ∈ SAT`).
  Logo `σ` é um objeto **genuinamente novo** (`σ ∈ M' \ M`).
- Metê-lo na "base de reflexão" `M*` arrasta, **por fechamento `PV`**, `i_0` e `α_{i_0}` junto —
  e aí (8) dentro de `M*` colapsa a configuração inteira (§5.2).
- A economia correta é: **levar de `σ` só as consequências `p`-tempo curtas que a prova usa**
  (`i_0`, e `σ_{i_0}` apenas como parâmetro **em `M'`**), e deixar o próprio `σ` fora.

### 5.4 A lista finita correta **(P)**

> **Proposição (lista finita).** A condição (iii) do Problema 2.1,
> `Log(M*) = Log(M')`, pode ser substituída por:
>
> **`M* ⊇ { π, α, m, i_0, α_{i_0} }`**, com `i_0 < m`, `α_{i_0} = (α)_{i_0}`, e
> **`M* ⊨ (¬α_{i_0}) ∈ SAT`** (a única instância de (8) usada),
>
> **sem** exigir `σ ∈ M*`.

**Verificação de que a lista fecha o item (5) (P):**

1. `σ ∈ M'` falsifica `φ` ⟹ `i_0 < m` e `M' ⊨ σ_{i_0}:P⊢α_{i_0}` (σ e projeções em `M'`) **(A)**.
2. `i_0, m, α ∈ M*` ⟹ `α_{i_0} ∈ M*` (fecha: a lista é fechada sob a única projeção `PV`
   necessária — `α_{i_0}` é gerado a partir de `α` e `i_0`, ambos listados).
3. Hipótese finita: `M* ⊨ (¬α_{i_0}) ∈ SAT` ⟹ **sobe** para `M'` (`Σ^b_1`).
4. `σ_{i_0} ∈ M'` (projeção `PV` de `σ ∈ M'` com `i_0 ∈ M'`; note que `σ_{i_0}` **não** precisa
   estar em `M*`).
5. `Ref_P ∈ T_PV` vale em `M'` com parâmetros `σ_{i_0}, α_{i_0}` ⟹ contradição com 1+3. ∎

**Observação sobre a ordem das exigências (C).** `i_0` só é definido depois de fixado o
falsificador `σ ∈ M'`; logo a proposição é condição sobre o **tripla construído** `(M*, i_0, σ)`,
não exigência prévia sobre `M` — lícito, pois (§5.2) `σ` deve existir **fora** de `M*` enquanto
`i_0` é semeado **dentro**.

**Coerência da lista (P).** A lista é **consistente** justamente porque **não é fechada em
`σ`**: `i_0` é *semeado* em `M*` (pertinência exigida, não derivada), enquanto `σ` permanece
fora; já `α_{i_0}` é derivado (e portanto obrigatório). Exigir `σ ∈ M*` acrescentaria
`σ_{i_0}` e a instância de (8) **em `M*`** de graça — e isso é precisamente o que o §5.2 mostra
ser impossível.

**Caso degenerado (P).** Sob **(F-b')** a lista encolhe ainda mais: `i_0 ∈ M'` e `i_0 < m` dão
`i_0 ∈ M ∩ m`; então `i_0, α_{i_0}, σ_{i_0}` já estão "antigos" e o axioma (S4) de `S` fornece
a instância **em `M`**, que sobe para `M'`. Aí **não há `M*` algum**: a lista de parâmetros é só
`{π, α, m, φ}`, todos em `M`.

## §6. O que fica em aberto **(C)**

1. **Construtibilidade de (F-sent):** provar que `M'` pode ser estendido satisfazendo `¬φ ∈ SAT`
   **e** (8) — cobrir `∀i<m` com testemunhas em `M'` é o coração do problema (forcing decide
   "medida a medida"; cobrir `i` não-padrão é infinito do ponto de vista das condições).
2. **Veredito da F1 sobre "`by (7) ⟹ i_0 ∈ M*`":** se lacunoso, 2.1 não entrega nem (F-inst), e a correção do Teorema 4 passa a ser a troca 2.1 → (F-sent)/(F-b').
3. **(F-b') vs (F-sent):** se selar `[0,m)` for mais barato que semear testemunhas para índices
   novos, (F-b') ganha; do contrário (F-sent) é a hipótese canônica.
4. **Redução de (F-sent) a menos:** só a instância em `i_0` (=(F-inst)) é *necessária*; (F-sent) é
   *suficiente* — se 2.1 der (F-inst) sem dar (F-sent), o Teorema do §2 vale com hipótese mais fraca.

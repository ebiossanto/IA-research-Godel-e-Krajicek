# G2 — Semente de (F-sent): consistência da semente e construção (ou obstrução)

> Frente G2. **Nota de autoria (honestidade de processo):** esta frente foi atribuída a um
> subagente, que gravou o esqueleto e falhou 5× em completá-lo (falha de infraestrutura
> repetida, foreground e background). O conteúdo abaixo foi então produzido pelo orquestrador,
> que tem o contexto completo das rodadas F/G. **Marcar como (P) é portanto correto**: são
> demonstrações próprias, sujeitas a referee (próximo passo: subagente-referee独立, §6).
> Marcação: **(A)** = fonte/artigo; **(P)** = próprio; **(C)** = conjectura.
> Idioma: português.

## §0. Plano e mapa da frente

**Estado recebido (das frentes anteriores):**
- **G1, Teorema 2.1 (L1) (P):** no forcing booleano de [Kra95, §9.4]/[Kra98, §4],
  `Log(M[G]) = Log(M)` — "medida a medida" **provado**, sem hipótese extra sobre `M`.
- **G1, Teorema 4.3 (P):** `(F-b')` (`M' ∩ m = M ∩ m`) é **impossível** junto de
  `M' ⊨ T_PV + (¬φ) ∈ SAT` — o índice `i_0` é sempre novo. Corolário 4.4: o passo do artigo
  "by (7) `i_o` is also already in `M*`" é **necessariamente falso** (v4 e v5/LMCS).
- **G1, §4.2:** reparo (R1) (pinning de nomes curtos) colapsa a genericidade (`M[G]=M`).
- **F2:** `(F-sent)` = `M' ⊨ T_PV + (¬φ) ∈ SAT + M' ⊨ ∀i<m (¬α_i) ∈ SAT` é **suficiente**
  para `NP ≠ coNP` (lema de suficiência finita, §2 do F2); `(F-b') ⟹ (F-sent)`.

**Pergunta desta frente:** o forcing booleano pode **construir** um `M'` com `(F-sent)`
(a correção viva do Teorema 4)? Resposta em duas metades:

1. **§1 (L2): a semente do falsificador `σ` é consistente** — provado (usa só o item (1)
   do artigo: "`φ` sem prova em `M` em qualquer pps"). `σ` é elemento **novo de medida velha**
   (nome `∈ M`) — a resposta positiva à pergunta "semente de elementos novos de medida velha".
2. **§2–§4: a semente de `(F-sent)` inteiro é impossível** — Teorema de obstrução global:
   **nenhum** `M' ⊨ T_PV` (de forcing ou de outro método) satisfaz `(F-sent)` junto do
   falsificador; a configuração do artigo é **falsa em ZFC**. Logo a correção do Teorema 4
   disponível em `ZFC` é uma **troca de hipótese** (F2), nunca uma construção verificável
   em `ZFC`; e uma demonstração por reductio sob `NP = coNP` (inclusive via construção
   provada sob `NP=coNP` — referee R5) permanece legítima, com motor a localizar (§2.6, §6).

---

## §1. (L2) Consistência da semente do falsificador — **Teorema provado**

### 1.1 Configuração

`M ⊨ T_PV + (S1)–(S4)` **(A, F2 §0)**; em particular `M ⊨ (S4)`:
`∀i<m (¬α_i) ∈ SAT`. `φ(r) = ⋀_{i<m} ¬(r_i : P ⊢ α_i)`, `r = (r_i)_{i<m}` variáveis livres
**proposicionais** indexadas por `m ∈ M` **(A, leitura F2 §0)**; `φ` **não tem prova em `M`
em qualquer pps** (item (1) do artigo) **(A)**. A construção booleana usa como átomos
`p := (r_i)_{i<m} ∈ M` — lícito: átomos são apenas elementos de `M` codificando variáveis
proposicionais, nada impede que sejam "antigos" **(P)**.

### 1.2 Teorema

> **Teorema 1.1 (L2) (P).** *(Corrigido após referee — G2_referee, R1.)* Nas condições
> acima, o conjunto de condições
> `T_σ := { ¬φ } ∪ { C ∈ Circuit_M(p) : C ≡ 1 em M }`
> (a semente que faz `ν_G(φ) = 0`, mais as condições de fechamento `Σ^b_1`-elementar de
> [Kra98, Thm 4.1]) **não tem refutação EF em `M`**.
> Logo o ultrafiltro `G` de [Kra98, Claims 1–2] existe e `M[G] ⊨ (¬φ) ∈ SAT`, com
> `σ := ν_G(p) = (ν_G(r_i))_{i<m}` elemento de `M[G]` **novo** (G1 §4.5) e de **medida velha**
> (o nome de `σ` é o nome canônico `⟨r_1,…,r_m⟩ ∈ M`) — "semente de elementos novos de
> medida velha" **confirmada**.

**Prova.** *(Sinal corrigido: a condição a ser realizada é `ν_G(¬φ) = 1`, logo o que se
semear é `¬φ` — referee R1.)* Suponha refutação EF de `T_σ` em `M`. EF é finitista: a
refutação usa finitas condições de fechamento `C_1,…,C_k` (cada uma com `M ⊨ EF ⊢ C_j`,
por definição de `C ≡ 1 em M` — `ν_G(C)=1` obrigatório) e a condição `¬φ` (o conjunto é
unitário nessa parte). Refutação EF de `{C_1,…,C_k, ¬φ}` em `M` + provas EF em `M`
de `C_1,…,C_k` ⟹ **prova EF em `M` de `φ`** (de `¬φ` e `EF ⊢ C_j` deriva-se `⊥`, i.e.
`EF ⊢ ¬¬φ`; concatenação interna de derivações finitas, p-tempo-verificável) — contradizendo
o item (1) **(A)** (`EF` é um dos "any proof systems").
Logo não há refutação; Claims 1–2 de [Kra98] aplicam-se **(A)**. ∎

### 1.3 Comentários e reservas honestas

1. **O truque "forma de `σ`" é desnecessário aqui** — e é bom saber por quê: como `p` são as
   próprias variáveis de `φ`, `φ` **é** uma fórmula sobre `Circuit_M(p)` e o falsificador é a
   avaliação genérica `ν_G(φ)=0`. O "espelhamento" (Kra98: `φ'(p,⟨Z⟩)`) só seria preciso se
   `φ` fosse sobre átomos antigos que quiséssemos movidos **(P)**.
2. **Diferença de hipótese com [Kra98]**: a aplicação publicada de [Kra98] exige
   "`SAT_n(M)` não reconhecível por circuito" para o seu seed específico (SAT sobre `W`);
   o nosso seed só exige o item (1) — **mais limpo** **(A+P)**.
3. **Reserva sobre `T_PV` vs `PV` (o ponto (C3) do contexto):** [Kra98, Thm 4.1] garante
   `M[G] ⊨ PV` (+ `Σ^b_1`-elementaridade com as condições de fechamento) — **não**
   `M' ⊨ T_PV`. Felizmente §2.4 abaixo mostra que a correção do Teorema 4 **não precisa**
   de `M' ⊨ T_PV`: a contradição usa só absolutidade p-tempo + soundness real de `P` **(P)**.
4. **`(¬φ) ∈ SAT` é `Σ^b_1`** e portanto sobe automaticamente de `M[G]` para extensões
   maiores — a semente é estável **(P)**.

---

## §2. O núcleo (R3): semear `(F-sent)` — e o Teorema de obstrução

### 2.1 A parte grátis

Para `i ∈ M ∩ m`: `M ⊨ (¬α_i) ∈ SAT` por (S4) **(A)**; testemunha antiga; `(¬α_i) ∈ SAT`
é `Σ^b_1` ⟹ sobe para qualquer extensão `M' ⊇ M` **(A, transferência F2 §0)**. **(P)**

### 2.2 A parte nova: candidatos a índice vêm de nomes

Todo `i ∈ M' ∩ m` é `i = ν_G(N)` para algum nome `N = ⟨C_1,…,C_ℓ⟩ ∈ M` com valor `< m`
(G1 §1.1) **(P)**. As condições naturais para (F-sent) são
`τ_N := "ν_G(α̃_{ν_G(N)}) tem atribuição falsificante genérica"`, onde `α̃_j` é `α_j`
**espelhado** sobre átomos novos: como `α = ⋁̇_{i<m} α_i` (disjunção disjunta **(A, (S2))**),
todos os átomos de todos os `α_i` estão entre os `≲ |α|` átomos de `α` — **um único mapa de
espelhamento** para `i < m` inteiro **(P)**. Cada `τ_N` é um circuito **em `M`** (tamanhos
internos ≤ `poly(|α|)`), logo condição legítima **(P)**.

### 2.3 Consistência de subconjuntos finitos

- **Só índices antigos:** os `α_{i_1},…,α_{i_k}` (`i_j ∈ M`) são disjuntos-variáveis
  ((S2): "no two `α_i` have an atom in common" **(A, verbatim em A_teoremas_exatos.md §1.2)**,
  absoluto p-tempo) e cada um é falsificável ((S4) em `M`); a **união** dos falsificadores
  falsifica a conjunção — e um falsificador **real** da conjunção implica **não-refutação EF
  em `M`** (pois `Ref_EF ∈ T_PV` vale em `M` **(A, F2 §0)**: uma refutação EF em `M` seria
  uma derivação real de `⊥`, contradizendo a soundness real de EF) — todo subconjunto finito
  de condições antigas é **consistente** **(P)**. *(Passo "falsificador real ⟹ não-refutação"
  acrescentado a pedido do referee R3.)*
- **Com índices novos:** a consistência de `τ_{N_1},…,τ_{N_k}` pede que `α_{i_{N_1}}∧…∧α_{i_{N_k}}`
  tenha atribuição falsificante **no mundo real** (os elementos de `M[G]` são strings reais;
  `Fals` é p-tempo e absoluta em modelos de `PV`) — e para `i` não-padrão **não há proteção
  (S4)**. A consistência conjunta de `τ_N` para **todos** os candidatos `N` é literalmente a sentença
  coletada `∃z ∀i<m Fals((z)_i, (α)_i)` — o conteúdo exato de **BB** (Cook–Thapen), que
  **não está disponível** **(A, F2 §4.2; contexto §4B)** **(P)**. Esta é a redução pedida:
  > **(R3) ≡ BB.** Semear `(F-sent)` no forcing booleano é equivalente, sobre `M ⊨ S`,
  > a coletar testemunhas para `∀i<m` — o esquema BB disfarçado de condições de forcing.
  > *(Ressalva honesta (P), a pedido do referee R3: a direção "coleção ⟹ semente
  > consistente" está fechada aqui só para **subconjuntos finitos** da semente; a passagem
  > ao ultrafiltro com semente de tamanho interno `m` usa os Claims 1–2 de [Kra98] e o
  > fechamento do filtro — declarado, mas merece conferência. Igualmente: o espelhamento
  > uniforme `α_i ↦ α̃_i` para `i` **não-padrão** é plausível (os átomos de `α_i` estão
  > sempre entre os de `α`) mas não está formalizado.)*

### 2.4 Teorema de obstrução global — **achado central**

> **Teorema 2.1 (obstrução) (P).** *(Corrigido após referee — G2_referee, R2: a hipótese
> `M' ⊨ T_PV` é necessária; a versão "incondicional" foi refutada — sem hipótese sobre `M'`,
> `Prf_P`/`Fals` podem ser interpretados não-realmente em argumentos novos.)* Sejam `P` um
> pps qualquer, `M ⊨ (S1)–(S4)`, `M' ⊇ M` com **`M' ⊨ T_PV`**, e suponha
> `σ ∈ M'` com `M' ⊨ ¬φ(σ)`, i.e. existe `i_0 ∈ M'`, `i_0 < m`, com
> `M' ⊨ σ_{i_0} : P ⊢ α_{i_0}`. Então:
> **(a)** `M' ⊨ (¬α_{i_0}) ∉ SAT`;
> **(b)** portanto `M' ⊨ ∀i<m (¬α_i) ∈ SAT` (=(F-sent)) é **falsa** em `M'`;
> **(c)** analogamente, para **qualquer** `M*` com `M ⊆ M* ⊆ M'` fechado sob `PV`:
> `M* ⊨ (8)` com `i_0 ∈ M* ∩ m` é **impossível** (reproduz e generaliza G1, Cor. 4.4).
> **(a′)** Basta `M' ⊨ PV` no lugar de `T_PV` (ver prova, rota alternativa) **(P)**.

**Prova.**
(a) **Rota interna (a de F2 §2(d), correta):** `M' ⊨ T_PV` ⟹ `M' ⊨ Ref_P` (universal-verdadeira,
com **quaisquer** parâmetros de `M'`, inclusive não-padrões) **(A, F2 §0)**. A hipótese dá
`M' ⊨ Prf_P(σ_{i_0}, α_{i_0})`; `Ref_P` instanciada em `(σ_{i_0}, α_{i_0})` dá
`M' ⊨ (¬α_{i_0}) ∉ SAT` **(P)**. Nada aqui usa "mundo real": o raciocínio é inteiramente
interno a `M'` — é o que conserta a falha apontada pelo referee (derivações não-padrões são
cobertas por `Ref_P` interna, não por soundness externa) **(P)**.
(a′) **Rota externa, com hipótese mínima:** se `M' ⊨ PV`, `Prf_P` e `Fals` são interpretados
pelas funções p-tempo **reais**; `M' ⊨ Prf_P(σ_{i_0}, α_{i_0})` ⟹ `σ_{i_0}` é **realmente**
uma derivação `P` de `α_{i_0}` (o teste p-tempo é absoluto, para objetos padrões e
não-padrões — são números reais); soundness **real** de qualquer pps (axiomas tautológicos,
regras soundes — vale em `V` para todo pps, inclusive sobre objetos não-padrões) ⟹
`α_{i_0}` não tem falsificador real algum; `Fals` absoluta ⟹ nenhuma `y ∈ M'` satisfaz
`Fals(y, α_{i_0})` ⟹ `M' ⊨ (¬α_{i_0}) ∉ SAT` **(P)**. **Sem nenhuma hipótese de modelo
sobre `M'`, ambas as rotas falham** ( referee R2(i) ) **(P)**.
(b) `(F-sent)` instanciada em `i_0` daria `M' ⊨ (¬α_{i_0}) ∈ SAT` — contradição com (a) **(P)**.
(c) `i_0 ∈ M* ∩ m` + `M* ⊨ (8)` ⟹ `M* ⊨ (¬α_{i_0}) ∈ SAT`; testemunha `y ∈ M* ⊆ M'` — pela
absolutidade de `Fals` (rota (a′), com `M* ⊨ PV` por fechamento) — realmente falsifica
`α_{i_0}`, ou seja `M* ⊨ Fals(y, α_{i_0})` ⟹ `M' ⊨ Fals(y, α_{i_0})` — contradição com (a) **(P)**. ∎

> **Corolário 2.2 (impossibilidade de construção) (P).** *(Com a hipótese `M' ⊨ T_PV`
> restaurada pelo referee R2.)* Não existe método algum (forcing booleano de [Kra95,
> Thm 9.4.2], forcing iterado, ultrapoder, saturação, compactness, "rota (R4)") que, sob
> quaisquer hipóteses **verificáveis em `ZFC`**, **construa** um `M' ⊨ T_PV` com
> `(¬φ) ∈ SAT` **e** `(F-sent)` (ou `M*` com (8) e `i_0 ∈ M*`): a configuração é falsa
> em `ZFC` (Teorema 2.1). Em particular a hipótese do artigo (Problema 2.1) **não pode
> valer** no cenário em que o artigo a aplica — e é exatamente aí que a lacuna do item (5)
> é fatal. A "correção" do Teorema 4 disponível hoje é uma **troca de hipótese** (F2);
> uma correção por **construção** só pode existir como lemma provado **sob `NP = coNP`**
> (ver §2.5.1 corrigido — e então esse lemma, por si só, já provaria `NP ≠ coNP`).

### 2.5 O que a obstrução **não** diz (honestidade)

1. **Reductio via construção é legítima (corrigido após referee R5 — o argumento anterior
   era não-sequitur).** O roteiro "sob `NP=coNP`, construir `M'` com a configuração ⟹ `⊥`"
   **é** uma prova válida de `NP ≠ coNP` — nada o proíbe. O que o Teorema 2.1 estabelece é:
   (i) tal lemma de construção **não pode ser provado em `ZFC` puro** (sua conclusão é falsa
   em `ZFC`); (ii) se for provado **em `ZFC + NP=coNP`**, então `ZFC + NP=coNP ⊢ ⊥` — ou
   seja, **o próprio lemma já é uma demonstração de `NP ≠ coNP`**. Logo a rota de construção
   sob `NP=coNP` permanece **aberta e legítima**; o que a obstrução elimina é apenas a
   pretensão de construir `M'` por hipóteses verificáveis em `ZFC` (ex.: "para todo `M`",
   "sob saturação", "sob qualquer forcing") — que era a aparência do item (5) do artigo.
   A §2.6 é **um** ataque possível entre outros, não o único **(P)**.
2. **`σ_{i_0}` novo é obrigatório** (G1 §4.5), e `i_0` novo também — tudo coerente: são
   exatamente os elementos que a obstrução "perdoa" e que `(F-sent)` não pode cobrir.
3. **(F-sent) nua permanece uma hipótese lógica perfeitamente não-vazia** como axioma sobre
   um `M'` hipotético (é `Π^b_2`, consistente **sem** o falsificador); o que é impossível é
   `(F-sent)` **junto** de `(¬φ) ∈ SAT` — e é justamente essa dupla que F2 consome, sob
   `NP=coNP`, dentro da reductio **(P)**.

### 2.6 A rota viva (research frontier)

Sob `NP = coNP` + `P` strong p-bounded + `M ⊨ S` **(A)**: a semente `T_2` da §2.2–2.3
tem ou não refutação EF em `M`? Teorema 2.1 garante que **nenhum** `G` universal existe
satisfazendo-a toda — logo, em `M`, ou alguma instância `τ_N` isolada já é refutável, ou
todo `G` estende só parte e `(F-sent)` falha. O que se quer provar (e ainda não se provou) **(C)**:
> sob `NP=coNP` + p-boundedness, alguma refutação EF **interna** de condições de coleção
> produz um circuito/derivação contradizendo `(S4)` ou `(ST)` — fechando a reductio sem
> construir `M'`. Isto é exatamente o padrão de [Kra98, Claim 1] (refutação ⟹ circuito
> para `SAT_n(M)`) — e é o ataque recomendado para a próxima rodada.

---

## §3. Rotas alternativas — veredito unificado pelo Teorema 2.1

| Rota | O que prometia | Veredito |
|---|---|---|
| (a) `M` ℵ₁-/recursivamente-saturado ("additional requirement" de G1 §3.2) | realizar o tipo `∀i<m falsificável` de uma vez | **Morta** como entrega de (F-sent)+falsificador: o tipo é **ZFC-impossível** (Thm 2.1); saturação não viola soundness real. Permanece útil só para a existência do **falsificador σ** (L2), que é consistente. **(P)** |
| (b) Forcing iterado `M[G₁][G₂]` | segundo passo conserta o primeiro | **Morta** (mesma obstrução; `(F-sent)` é `Π^b_2`, não sobe por Σ^b_1-elementaridade de passo algum). **(P)** |
| (c) (R4) [Kra16]: preservar a teoria de primeira ordem de `A_W` | alternativa a "sem novos elementos em `[n]`" | **Viva para o Problema 2.1 original** (é o que [Kra16] endossa), mas **não entrega (F-sent)** — preservação FO não controla `(8)` (`Π^b_2`). Serve para a versão original do problema, não para a correção. **(A+P)** |
| (d) Ultrapoder/corte (`N^{M*} = {v : ∃w∈N^M, v≤w}`, [Kra95] §5) | corte não acrescenta medidas (G1, Advertência 2.4) | **Morta** para (F-sent) (mesma obstrução); **viva** só para a parte `Log` (L1 com corte) — confirma que `Log` nunca foi o gargalo. **(P)** |

**Leitura:** o gargalo do artigo **não é `Log`, não é `M*`, não é o forcing** — é a
**coleção `∀i<m ∃y`** (= BB), e o Teorema 2.1 mostra que ela não pode ser "entregue" em
lugar nenhum junto do falsificador. **(P)**

---

## §4. Teoremas finais

> **Teorema 4.1 (correção minimal do Teorema 4, versão finita) (P).** *(T_PV restaurado —
> referee R4; F2 tinha a hipótese certa.)* Suponha **(ST)** e
> existe `P` strong p-bounded. Se para **todo** `M ⊨ S` não-padrão existe `M' ⊇ M` **cofinal**
> com `Log(M') = Log(M)`, **`M' ⊨ T_PV`**, `M' ⊨ (¬φ) ∈ SAT` e `M' ⊨ ∀i<m (¬α_i) ∈ SAT`,
> então `NP ≠ coNP`.

**Prova.** Segue F2, §2: (1)–(4) dão `P`, `S` consistente, `M ⊨ S` não-padrão e `φ` sem
prova em `M`; (5) = (F-sent) dá `M'` com as quatro propriedades; a contradição fecha em `M'`
por `(F-sent)` instanciada em `i_0` (dá `(¬α_{i_0}) ∈ SAT`) contra `Ref_P ∈ T_PV` instanciada
em `(σ_{i_0}, α_{i_0})` (dá `(¬α_{i_0}) ∉ SAT`) — Teorema 2.1(a) **(A+P)**.
**Observação (P):** para **só** a contradição basta `M' ⊨ PV` no lugar de `T_PV`
(Teorema 2.1(a′)); mantém-se `T_PV` no enunciado por fidelidade ao Problema 2.1 e ao F2.
**Observação (P):** `Log(M') = Log(M)` e a cofinalidade **não entram** na contradição —
são heranças do enunciado original; podem ser removidas se se desejar o enunciado mínimo
(hipótese nua: só `M' ⊨ T_PV + (¬φ) ∈ SAT + (F-sent)`, com `M' ⊇ M`). ∎

> **Teorema 4.2 (o que o forcing booleano entrega) (P).** Nas hipóteses do artigo
> (`M ⊨ T_PV + (S1)–(S4)`), o forcing de [Kra95, Thm 9.4.2]/[Kra98, §4] produz, **sem
> hipótese extra alguma sobre `M` além de `M ⊨ PV`**: (i) `Log(M[G]) = Log(M)` (G1, (L1));
> (ii) cofinalidade; (iii) `M[G] ⊨ (¬φ) ∈ SAT` com `σ` novo de medida velha (Teorema 1.1);
> (iv) `Σ^b_1`-elementaridade opcional. **Não produz** (e não pode produzir) `(F-sent)`
> (Teorema 2.1/Corolário 2.2). O "additional requirement on M" do artigo diz respeito só à
> **existência do genérico** (contagem/saturação, não-reconhecibilidade de `SAT_n(M)` —
> G1 §3.2), não a `Log` nem a `(F-sent)`.

---

## §5. Consequência para o artigo e para as 4 questões de pesquisa

1. **Correção do Teorema 4 (a troca exata):** remover o item (5) (`M*`, `Log`, "by (7)…")
   e substituir a hipótese 2.1 por **(F-sent)** (ou pela fraca **(F-inst)**: `M' ⊨ (¬α_{i_0}) ∈ SAT`
   para o `i_0` do falsificador — F2 §6.4), com `M'` exigido como
   **cofinal + Log + `M' ⊨ T_PV` + (¬φ)∈SAT + (F-sent)** (`T_PV` é exigido — referee R4;
   para a contradição basta `PV`, mas mantém-se por fidelidade a 2.1/F2).
   **(F-b') está refutado** (G1 Thm 4.3) — não pode figurar como hipótese de correção.
2. **Redução a aritmética limitada (Q2 do usuário):** pinpoint final — a hipótese exata
   substituta de 2.1 é **uma instância do esquema de coleção sobre `M'`** (forma coletada de
   (8)), i.e., **BB em forma finita com parâmetros `α, m`**; o forcing não a fornece, e o
   Teorema 2.1 mostra que ela é **inconsistente com o falsificador** — o que explica por que
   BB é "exactly what is missing" em [Kra16].
3. **Geradores NW/gadget (Q3):** intactos; a obstrução não toca `(ST)` nem `Ref_P` nem a
   relação com NW — fica como na rodada D.
4. **P vs NP (Q4):** o condicional corrigido (Teorema 4.1) é **mais fraco em hipótese**
   que o do artigo (uma sentença `Π^b_2` vs esquema+Log+cadeia) e **inatacável por
   construção** — é a forma canônica do que a prova consome.

---

## §6. Veredito (≤ 600 palavras) e próximos passos

**Veredito (P):**

1. **(L2) é verdadeiro e provado (Teorema 1.1):** a semente do falsificador `σ` é consistente
   no forcing booleano, usando **só** o item (1) do artigo ("`φ` sem prova em `M` em qualquer
   pps") — mais limpo que a hipótese publicada de [Kra98]. `σ` é **elemento novo de medida
   velha**: a resposta à pergunta central ("se o forcing aceita semente de elementos novos de
   medida velha") é **SIM**, e com ela `(¬φ) ∈ SAT` é **construível** em `M'` cofinal com
   `Log(M') = Log(M)` — meia resposta positiva ao Problema 2.1 corrigido.
2. **Mas `(F-sent)` é impossível junto do falsificador (Teorema 2.1/Corolário 2.2)** — com
   `M' ⊨ T_PV` (ou `PV`), por `Ref_P` interna + absolutidade; nenhuma rota técnica (saturação,
   forcing iterado, ultrapoder, (R4)) escapa, porque a obstrução é **em ZFC**, não técnica.
   A configuração do artigo (`M* ⊨ (8)` com `i_0 ∈ M*`) é falsa **em ZFC** — confirma e
   universaliza o Corolário 4.4 de G1: a lacuna do item (5) é **fatal** para qualquer
   correção **por construção verificável em ZFC** — nem v4 nem v5/LMCS têm como consertá-la
   construindo a configuração. *(Nuance de referee R5: uma construção provada **sob
   `NP=coNP`** permanece legítima — e esse lemma, isoladamente, já provaria `NP ≠ coNP`.)*
3. **A "correção" disponível é uma troca de hipótese (F2 + Teorema 4.1 aqui):** 2.1 → (F-sent)
   (ou (F-inst)), com `M'` exigido como cofinal + Log + `T_PV` + duas sentenças; `M*` é que
   é descartável (`T_PV` ficou — referee R4). O Teorema corrigido é **mais enxuto** e
   **exato**: sua hipótese é literalmente o conteúdo de BB que a prova consome — e que
   [Kra16] já apontava como indisponível.
4. **Fronteiras vivas (duas):** (i) sob `NP=coNP` + `P` p-bounded, **construir** a
   configuração é um caminho legítimo (a construção, sendo provável só sob `NP=coNP`, já
   provaria `NP ≠ coNP`) — localizar **onde** o forcing a produziria e por que esse passo
   exige `NP=coNP` é o ataque de reductio (Claim 1 de [Kra98] invertido: refutação EF
   interna da coleção ⟹ circuito/derivação contradizendo `(S4)`/`(ST)` — §2.6); (ii) a
   rota (R4) de [Kra16] (preservação FO de `A_W`) permanece viva para o Problema 2.1
   original, sem tocar em `(F-sent)`.

**Próximos passos concretos:**
1. ~~Referee~~ **CONCLUÍDO** nesta rodada (§7): Teoremas 1.1, 2.1, 4.1 corrigidos (sinal,
   `T_PV`, meta-lógica); referee R3 (espelhamento não-padrão; passagem a semente infinita)
   registrado como lacuna formal.
2. Ataque à §2.6 (refutação EF interna da coleção sob NP=coNP) — a nova Equipe H.
3. Atualizar a nota editorial (F1 §5) com o **Teorema 2.1** (a configuração do artigo é
   falsa em ZFC, com `M' ⊨ T_PV`) e o **Teorema 4.3 de G1** — argumento de peso decisivo
   para o autor.
4. Formalização Lean do Teorema 2.1 (Ref_P interna + absolutidade de `Prf_P`/`Fals`) em
   `DDP.lean` (Equipe B).

**Lacunas honestas:** a §2.6 é `(C)` (conjectura de ataque, não resultado); a equivalência
"R3 ≡ BB" (§2.3) está provada na direção "`(F-sent)` ⟹ coleção" e na direção "coleção ⟹
semente consistente" apenas para subconjuntos finitos — a passagem ao ultrafiltro com
semente não-finita usa [Kra98, Claims 1–2] como declarado e merece conferência; o
espalhamento `α_i ↦ α̃_i` para `i` não-padrão é plausível, não formalizado (referee R3).

---

## §7. Relatório do referee e correções aplicadas (transparência)

Referee independente (`G2_referee.md`), 5 pontos:

| Ponto | Veredito | Correção aplicada |
|---|---|---|
| R1 (sinal da semente, Thm 1.1) | PARCIAL — semear contém `φ`, refutação dá `¬φ` | §1.2: semente é `{¬φ}`; refutação ⟹ `EF ⊢ φ` ⟹ item (1) **(corrigido)** |
| R2 (Thm 2.1 "incondicional") | ERRO — sem hipótese sobre `M'`, absolutidade falha; soundness externa não cobre não-padrões | Thm 2.1: hipótese `M' ⊨ T_PV` restaurada; rota interna (`Ref_P`) + rota externa com `M' ⊨ PV` (a′) **(corrigido)** |
| R3 (disjunção disjunta) | OK (+2 ressalvas) | §2.3: passo "falsificador real ⟹ não-refutação EF em `M`" acrescentado; ressalvas formalizadas como lacunas **(corrigido)** |
| R4 (descartar `T_PV`, Thm 4.1) | ERRO — entra o furo do R2 | Thm 4.1: `M' ⊨ T_PV` restaurado; observação de que `PV` basta **(corrigido)** |
| R5 (meta-argumento §2.5.1) | ERRO (não-sequitur) — construção sob `NP=coNP` é legítima e é a própria prova | §2.5.1 reescrito; §6 item 2/4 ajustados **(corrigido)** |

Nenhum dos 5 pontos derruba o **resultado central** (obstrução com `T_PV`; (L2); (F-b')
refutado — este nem foi atacado). O referee está salvo em `G2_referee.md`.

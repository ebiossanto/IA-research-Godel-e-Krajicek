# F3 — Ataque construtivo de (F-b') e (F-sent)

**Objetivo da rodada:** construir (ou honestamente delimitar a impossibilidade de construir)
um `M'` que satisfaça uma das duas formulações finitas do §4(A) de `F_CONTEXTO_ATAQUE.md`.
Marcação: **(A)** = artigo (arXiv:2506.20221v4 / Krajíček [7]), **(P)** = raciocínio próprio,
**(C)** = conjectura. Sem uso de web.

---

## 1. Os dois enunciados finitas (copiados do contexto §4(A)) **(P)**

Toda a máquina `M*` + preservação `Σ^b_1` + `Log` existe para transportar a sentença (8)
`∀i<m (¬α_i) ∈ SAT` de `M` (onde ela é axioma de `S`) até `M'` no índice `i_0`. Se obtivermos
uma das condições abaixo, `M*` e `Log` tornam-se desnecessários:

- **(F-b') — versão membership (Equipe E, variante (b')):** exigir
  `M' ∩ m = M ∩ m` ("nenhum elemento novo abaixo de `m`"). Então `i_0 < m, i_0 ∈ M'` ⟹
  `i_0 ∈ M ⊆ M*`; `M ⊨ (8)` instancia em `i_0`: `M ⊨ (¬α_{i_0}) ∈ SAT`; `Σ^b_1` sobe
  `M ⊆ M'`: `M' ⊨ (¬α_{i_0}) ∈ SAT`; `Ref_P` em `M'` dá a contradição. **(F-b') ⟹ (F-sent).**
- **(F-sent) — versão sentença (alvo minimalista):** exigir diretamente
  `M' ⊨ T_PV + (¬φ) ∈ SAT + ∀i<m (¬α_i) ∈ SAT`. A contradição fecha com `i_0 ∈ M'` qualquer
  (sem pertinência a `M*`): `M' ⊨ (8)` instancia em `i_0` e `Ref_P` em `M'` fecha.
  Ambas as exigências extras de `M'` são sentenças com parâmetros em `M`
  (`¬φ ∈ SAT` é `Σ^b_1`; (8) é `Π^b_2`). **(P)** as duas exigências são sobre o *mesmo* `M'`,
  e (F-b') é a mais forte do ponto de vista construtivo (ela *impõe* a aritmética de `M`
  no segmento `m`, ao passo que (F-sent) deixa `M' ∩ m` livre, exigindo só a sentença (8)).

## 2. Por que a rota "M* + Log" do artigo não resolve o problema de membership **(A)/(P)**

Recapite em 5 linhas: (i) `Log(M) = {|m| : m ∈ M}` é o conjunto dos **comprimentos** padrono,
não dos elementos **(A)**. (ii) `Log(M*) = Log(M')` logo não impede elementos novos em `M'`
com comprimento antigo **(P)**. (iii) Um elemento novo `j ∈ M' \ M*` com `j < m` tem
`|j| ≤ |m|`, comprimento já presente em `Log(M) = Log(M*) = Log(M')` **(P)**. (iv) Logo a
igualdade de `Log` é satisfeita "com folga" e o passo `i_0 ∈ M*` ("by (7)") não se segue da
definição literal **(P)**. (v) É exatamente para fechar essa lacuna que propomos (F-b'),
que substitui a exigência de *medidas* por uma exigência de *membership* sobre o segmento
`m` — e é essa exigência que agora tentamos construir.

## 3. Construção por compactness/Henkin para (F-b') **(P)**

Considere a teoria (em `L_PV`, com os símbolos de `SAT`, `⊢`, etc.):

```
T = T_PV ∪ { (¬φ) ∈ SAT } ∪ { Diag^b_1(M) } ∪ { sentenças universais verdadeiras
                                                com parâmetros de M }.
```

onde `Diag^b_1(M)` é o diagrama `Σ^b_1` de `M` (todas as fórmulas `Σ^b_1` com parâmetros
de `M` que valem em `M`, e também — para o diagrama completo — a negação das `Σ^b_1` que
falham; ver (a)).

**(a) O diagrama `Σ^b_1` é seguro (sobe). (P)** Uma fórmula `Σ^b_1` `∃y ψ(x,y)` com `ψ`
decidível/aberto transfere **para cima**: se `M ⊨ ∃y ψ(a,y)` vale; e se `M ⊨ ¬∃y ψ(a,y)`,
então em qualquer extensão `M ⊆ M'` o mesmo `y` testa a falsidade? — cuidado: a falsidade
de `∃y ψ` é `Π^b_1` e **não** transfere para cima. Logo só posso colocar no diagrama as
partes **positivas** `∃y ψ(a,y)` verdadeiras em `M` (elas sobem automaticamente) e as
partes negativas `∀y ¬ψ(a,y)` verdadeiras em `M` **apenas se** `∀y ¬ψ` for universal
verdadeira no sentido de `T_PV` (aí valem em `M'` com parâmetros novos, por serem universais).
**Conclusão (P):** o diagrama a incluir é `Diag^+(M) = { ∃y ψ(a,y) : ψ aberto, a ∈ M,
M ⊨ ∃y ψ(a,y) }`, que sobe de graça, unido ao diagrama universal de `M`.

**(b) Universais com parâmetros de M podem falhar em extensões — mas se `M'` for
subestrutura de um modelo `N ⊨ T_PV`, valem de graça. (P)** Se `N ⊨ T_PV` e `M' ⊆ N`
(subestrutura), então toda sentença universal verdadeira em `N` vale em `M'` com **todos**
os parâmetros de `M'`, em particular com parâmetros de `M`. Como `T_PV` é axiomatizado por
sentenças universais **(A)**, qualquer subestrutura de modelo de `T_PV` é modelo. Logo:
construir `M'` ⇝ construir `N ⊨ T_PV` com `M ⊆ M' ⊆ N` e com `M'` contendo o falsificador `σ`.

**(c) O problema vira: construir `N ⊨ T_PV` contendo `M` e um falsificador `σ`. (P)**
Consistência por subconjuntos finitos: dado qualquer subconjunto finito `T_0 ⊂ T`, ele usa
finitamente muitos parâmetros de `M` e finitamente muitas `Σ^b_1` positivas. Se `M` é modelo de
`T_PV` (hipótese de partida: `M ⊨ T_PV ∧ ...`), então `T_0` tem modelo: basta estender `M`
com um `σ` falsificador "genérico" e interpretar `SAT`/`⊢` de modo a satisfazer as finitas
exigências, *desde que* nenhuma universal com parâmetros de `M` seja contradita por `σ`.
Por compactness, daí sai `N`.

**Onde o argumento pode falhar — honestidade (P):**
1. **Universais sobre `M` podem ser falsificados por elementos novos.** Uma universal
   `∀x θ(a,x)` verdadeira em `M` pode falhar em `N` se `σ` (elemento novo) viola `θ(a,σ)`.
   Como `Ref_P` é universal, `σ` não pode violar `Ref_P` — mas `σ` viola *justamente* o
   que a universal proíbe? Não: `σ` satisfaz `(¬φ) ∈ SAT`, o que é `Σ^b_1`, não universal.
   Ainda assim, a universal `Ref_P` liga `σ_{i_0}:P ⊢ α_{i_0}` com `(¬α_{i_0}) ∉ SAT`;
   se impusermos `(¬α_{i_0}) ∈ SAT` (o que queremos!), `Ref_P` força `σ_{i_0}:P ∬ α_{i_0}`,
   contradizendo o papel de `σ`. **Esse é exatamente o ponto onde a contradição final do
   artigo mora (P)** — ou seja: a teoria `T` acima é **inconsistente** se levarmos a sério
   `T_PV` (que contém `Ref_P`) + `∀i<m (¬α_i) ∈ SAT` + falsificador `σ`. Detalhe:
   `∀i<m (¬α_i) ∈ SAT` está em `T` só se `m` e os `α_i` forem parâmetros de `M` e a sentença
   for universal/`Σ^b_1` adequada — ver §5. Se `T` é inconsistente, o que "construímos" é
   a prova da lacuna do artigo; se é consistente, a construção fecha (F-b'). **(C)** a
   consistência de `T` é precisamente a questão em aberto.
2. **Compactness não produz `M' ∩ m = M ∩ m`.** Nada em `T` proíbe `N` de criar elementos
   novos abaixo de `m`; o diagrama positivo não restringe isso. Para isso preciso de uma
   **condição extra de genericidade** — é aí que reaparece o forcing de [7] (§6).

## 4. O cerne: fechamento PV e elementos novos abaixo de `m` **(P)**

Seja `M' = Sub(M ∪ {σ})` a subestrutura gerada (fechada sob as funções `L_PV`). Que elementos
novos `j < m` podem surgir?

- `|x|` (medida/comprimento): se `|σ| < m`, então `|σ|` é novo abaixo de `m` **e** é
  *antigo* como comprimento (`|σ| ≤ |φ|^c`, medida já em `Log(M)`). Este é o caso "degrau".
- `x ⊖ y` (diferência truncada): `σ ⊖ σ = 0` (antigo), mas `|σ| ⊖ k` para `k < m` pode dar
  um valor novo abaixo de `m` se `|σ| < m`.
- Decodificação `(σ)_i`: para `i < m` **já em `M`** dá `(σ)_i`, que é novo mas **≥?**
  — `(σ)_i` pode ser qualquer número, em particular `< m` (um `σ_i` pequeno!).
- Composições: `|(|σ| ⊖ |σ|)| = |0|`, `(|σ| ⊖ |σ|) ⊕ c = c` — todas antigas; mas
  `(σ ⊖ a) ⊕ b` para `a,b ∈ M` fixa `σ`-dependências.

**Lema de evitamento (tentativa). (P)** *Se escolhemos `σ` com `|σ_i| ≥ m` para todo `i < m`
e `|σ| ≥ m`, então nenhum elemento novo abaixo de `m` aparece em `Sub(M ∪ {σ})`?*
**Refutação parcial (P):** falsa como está — `|σ| ⊖ |σ| = 0` é antigo, ok, mas
`|σ| ⊖ c` para `c ∈ M` com `c < |σ|` dá um valor que **pode** ser `< m` e novo (se
`|σ| ≈ m`); além disso `(σ)_i` com `i` novo? — `i` precisa existir. O que salva é que
`i < m` e `m ∈ M` fixo: os `i` relevantes já estão em `M ∩ m`.

**Reconhecimento honesto (P):** σ_i **pode** ser pequeno (`σ_i < m`), e aí `σ_i` é um
elemento novo abaixo de `m` já que `σ ∉ M` não garante `σ_i ∉ M`... na verdade `σ_i ∈ M` seria
*possível*; o problema é `σ_i ∉ M` com `σ_i < m`. **Não há garantia óbvida de que haja
falsificador com todos os `σ_i` em `M ∪ {≥ m}`.** O que dá folga: **há muitos falsificadores**
— `φ` tem, em geral, um conjunto `Σ^b_1`-aberto de falsificadores, e podemos variar `σ` dentro
dessa classe escolhendo `σ_i` grandes (`|σ_i| ≥ m`) sempre que a semântica de `φ` permitir.
**(C)** Se a classe de falsificadores admite escolha com `σ_i ≥ m` para todo `i < m`, o
"lema de evitamento" vale em forma fraca: `Sub(M ∪ {σ}) ∩ m = M ∩ m` **exceto** pelos
valores `(|σ| ⊖ c)` etc., que se controlam exigindo `|σ| ≥ m + max{c ∈ M ∩ m}`... o que é
uma condição de forcing ("`|σ|` grande"), não um teorema. Ver §6.

## 5. (F-sent) via semente: cobertura de índices novos e circularidade **(P)**

Exigir `z` com `∀i<m F(i,(z)_i)` é `Σ^b_1` (∃z + matriz decidível + `∀i<m` sharply bounded),
logo **sobe** de `M` para `M'` **se valer em `M`**. Duas armadilhas:

1. **Circularidade de índices (P):** os `i < m` cobertos por `z` incluem índices que **só
   existirão em `M'`** (elementos novos abaixo de `m`, §4). `z` deve cobrir `i` que ainda
   não existe quando `z` é escolhido em `M`. Escolher `z ∈ M` cobre só `i ∈ M ∩ m`; a extensão
   cria `i` novos e `∀i<m F(i,(z)_i)` pode **falhar** em `M'`? Não — a sentença é `Σ^b_1` e
   `Σ^b_1` *sobe*: se vale em `M`, vale em `M'`. **Mas** a premissa `M ⊨ (8) ⟹
   M ⊨ ∃z∀i<m F` é exatamente o esquema **BB** (coleta para `m` não-padrão) — não
   disponível **(A)/(P)**. Ou seja: para `(F-sent)` basta que a *extensão* **contenha** tal `z`
   (requisito de construção, não de teoria) — mas aí `z` precisa cobrir `i` novos que só
   existem em `M'`: escolhemos `z` *depois* de `M'`? Circular.
   Duas saídas possíveis **(C)**: (S1) o forcing **semeia** `z` e cada `F(i, ·)` no momento
   em que o índice `i` aparece (aí `z` é construída "em transfinito" dentro do próprio
   forcing, e a circularidade vira ordem de construção); (S2) exigir apenas a cobertura dos
   `i ∈ M ∩ m` (índices antigos) — mas isso **não** é (F-sent), que pede `∀i<m` com `m` do
   modelo-alvo. A saída (S1) é a que [7] provavelmente usa; confirmá-la é o passo 1 do §6.
2. **Onde BB reaparece (P):** a coleta para `m` não-padrão — `∀i<m ∃w F(i,w) ⟹
   ∃z ∀i<m F(i,(z)_i)` — é o "missing reflection" escondido na genericidade do
   forcing **(A)**.
   Se o forcing de [7] decide "medida a medida", ele cobre cada `i` cuja medida já foi
   tratada; cobrir **todos** `i < m` (incluindo medidas já vistas mas `i` novos) é precisamente
   o ponto onde BB seria usado para colapsar `∀i<m ∃w` em uma única `z`.

## 6. Status honesto e plano **(P)**

**(F-b') e (F-sent) permanecem ABERTAS após esta rodada.** O que esta rodada estabeleceu:

- A construção por compactness/Henkin *quase* funciona: o diagrama `Σ^b_1` positivo sobe,
  os universais valem "de graça" se `M'` for subestrutura de `N ⊨ T_PV`, e a consistência
  finita parece plausível **desde que** o forcing selecione `σ` sem criar elementos novos
  abaixo de `m` (§4) e sem cobrir índices novos (§5).
- Onde pode falhar: (i) universais com parâmetros de `M` sendo falsificadas por `σ` (§3(c));
  (ii) `σ_i` pequeno criando elemento novo `< m` (§4); (iii) circularidade da semente `z`
  cobrindo `i` que só existirão em `M'` (§5).

**Para decidir, seria preciso saber a estrutura das condições do forcing de [7] Thm 9.4.2**
(livro de 1995, Cap. 4/9): se elas são "medida a medida" e se aceitam **semente de elementos
novos** (um `σ` fixado no início, com `|σ_i| ≥ m`) sem violar a genericidade.

**Plano de 3 passos (P):**
1. **Obter a descrição do forcing de [7]** (Krajíček 1995, Cap. 4/9 — Thm 9.4.2): o que é
   uma condição, o que ela decide, como `Log(M') = Log(M)` é preservado.
2. **Testar se a construção semeada mantém `M' ∩ m = M ∩ m`**: dado `σ` com `|σ_i| ≥ m`
   (`i < m`), o fechamento PV cria elementos novos `< m`? Se não cria → (F-b') fecha.
3. **Se falhar, cair para (F-sent) com cobertura de índices novos**: exigir que o forcing
   *semeie* as testemunhas `F(i, ·)` para todo `i < m` **que aparecer**, o que reabre a
   questão BB (coleta para `m` não-padrão) — mas talvez o forcing a incorpore por construção.

**Tabela-resumo dos obstáculos (P):**

| # | Obstáculo | Onde aparece | Bloqueia | Alvo |
|---|-----------|--------------|----------|------|
| O1 | `Log` é sensível a comprimentos, não a elementos | §2 (A) | o passo "by (7)" | motiva (F-b') |
| O2 | universais com parâmetros de `M` podem falhar com `σ` novo | §3(c) | compactness ingênuo | ambos |
| O3 | diagrama `Σ^b_1` só sobe na parte positiva | §3(a) | diagrama completo | ambos |
| O4 | `σ_i` pode ser `< m` (elemento novo abaixo de `m`) | §4 | `M' ∩ m = M ∩ m` | (F-b') |
| O5 | nenhum "lema de evitamento" provado | §4 | fechamento PV | (F-b') |
| O6 | semente `z` cobre `i` que só existirão em `M'` | §5 | `Σ^b_1` coletada | (F-sent) |
| O7 | BB (coleta para `m` não-padrão) reaparece | §5 | construção de `z` | (F-sent) |
| O8 | estrutura do forcing de [7] desconhecida | §6 | decisão final | ambos |

**Marcação global:** itens de §1–§2 são (A) adaptado por (P); §3–§5 são (P), com (C) assinalado
onde a conclusão é conjectural; §6 é (P) com (C) implícito na abertura dos dois problemas.

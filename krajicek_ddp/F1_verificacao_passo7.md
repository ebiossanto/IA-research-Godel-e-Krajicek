# F1 — Verificação crítica do passo "But by (7) i_o is also already in M∗"

**Objeto:** Teorema 4, §3, item (5) da prova (arXiv:2506.20221v4) — a frase de onde se
extrai a exigência E4 da tabela E1–E5: `i_0 ∈ M*`.
**Marcação:** **(A)** = texto do artigo; **(P)** = demonstração/análise própria; **(C)** = conjectura.
**Data:** 10/10/2026. **Verificação externa (arXiv v4):** concluída — §6 (lacuna confirmada).

---

## §1. Transcrição literal (A)

(A) Texto verbatim do artigo — §3, item (5) da prova do Teorema 4 (extraído do HTML do
arXiv em 10 Out 2026):

> "Now we conclude the proof by using the assumption that Problem 2.1 has the affirmative
> solution. This gives us M ⊆ M* ⊆ M′ such that
>
> Log(M*) = Log(M′), (7)
>
> and M′ ⊨ T_PV ∧ ¬φ ∈ SAT. Note that M* satisfies the last axiom of S:
>
> M* ⊨ ∀i<m (¬α_i) ∈ SAT (8)
>
> as it preserves the Σ^b_1(PV)-properties from M.
>
> Let σ ∈ M′ be an assignment to the atoms r that falsifies the formula φ in M′.
> Hence σ = (σ_i)_{i<m} and we have M′ ⊨ σ_{i_0}:P ⊢ α_{i_0} for some i_0 < m.
> **But by (7) i_o is also already in M∗** and hence by (8) we get:
>
> M′ ⊨ (¬α_{i_0}) ∈ SAT.
>
> That contradicts Ref_P which holds in M′ as it models T_PV."

(A) Definição de Log no §2 do artigo (verbatim):

> "where Log(M) = {|m| | m ∈ M}"

— ou seja, **Log(M) é o conjunto dos comprimentos (medidas) padrono dos elementos de M**,
não um conjunto de elementos. É essa definição literal que está sob exame.

(A) Contexto imediato da definição no §2 (verbatim, v4; confere-se com a web em §6):

> "Further it is remarked at the end of [14] that one can arrange that 𝐌′ introduces no
> new **lengths** into 𝐌: Log(𝐈𝐊′) = Log(M) (5) ... A construction which yields this
> (with an additional requirement on 𝐌) is the forcing construction underlying
> [7, Thm.9.4.2]."

O próprio artigo, portanto, descreve (7)/(5) como exigência de **"no new lengths"** —
sobre comprimentos, não sobre elementos. A expressão "(with an additional requirement on
𝐌)" refere-se a uma exigência **sobre M** (a ser verificada em [7]), não a uma proibição
de elementos novos com medidas velhas em 𝐌′.

O passo sob verificação é a frase em negrito. Toda a máquina (7)+(8)+`M*` existe unicamente
para transportar (8) de `M` até o índice `i_0` que só é garantido existir em `M'`; E4
(`i_0 ∈ M*`) é o elo único entre `M*` e o falsificador. Se E4 cai, (7) e `M*` perdem função
no ponto (5) — ver §4 e `F2_versao_finita.md`.

---

## §2. Análise (P): `Log(M*) = Log(M')` não implica `i_0 ∈ M*`

### §2.1 O que (7) controla — e o que não controla

(P) `Log(M) = {|m| : m ∈ M}` é o conjunto das **medidas**. A medida satisfêz
`j < m ⟹ |j| ≤ |m|`. Suponha `m ∈ M ⊆ M*` e um elemento novo `j ∈ M' \ M*` com `j < m`.
Então `|j| ≤ |m| ∈ Log(M) = Log(M*) = Log(M')`: a igualdade de Log **continua válida com
folga**, porque `|j|` é uma medida já presente. Em outras palavras:

> A igualdade de Log é **insensível a elementos novos abaixo de `m`** (e, de fato, a
> qualquer elemento novo cuja medida já figure em Log).

`Log` é um requisito por-"balde" de medidas; cada balde de medida `k` contém `~2^k`
elementos (não-padrão, quando `k` é não-padrão). Controlar quais baldes existem não
controla quais elementos de um balde antigo existem. Logo (7) é **compatível** com
`M' ∩ m ⊋ M ∩ m`, e portanto (7) sozinha **não** produz `i_0 ∈ M*`.

### §2.2 Esquema de contra-exemplo (P) (esquemático)

Um contra-exemplo completo exige construir `M'`; o esquema lógico é este:

1. Seja `M ⊨ T_PV` qualquer com `m ∈ M` (padrão ou não; o caso não-padrão é o relevante).
2. Seja `j ∈ M' \ M` com `j < m` um índice "novo". Nada em `Log` o proíbe: `|j| ≤ |m|`
   e `|m| ∈ Log(M)`.
3. Construção sugerida: forçar sobre `M` à la [7, Thm 9.4.2] semeando explicitamente `j`
   (ou um falsificador `σ` cujo suporte toque `M' ∩ m \ M`). A condição do teorema —
   `Log(M') = Log(M)` — só restringe medidas; `j` usa medida velha, logo a condição
   permanece satisfeita. Como `T_PV` é universal e `M*`, `M'` são fechadas/subestruturas
   apropriadas, `M' ⊨ T_PV` é grátis (E1).
4. Configuração obtida: `M ⊆ M'`, `Log(M') = Log(M)`, mas `M' ∩ m ⊋ M ∩ m`. Escolhendo o
   falsificador `σ` de `φ` cujo primeiro índice falsificável `i_0` cai em `M' ∩ m \ M`,
   obtém-se exatamente a situação em que o artigo afirma `i_0 ∈ M*` e ela é falsa.

(C→P) Não identificamos nenhum mecanismo em [7, Thm 9.4.2] que proíba **elementos novos
com medidas velhas**: a hipótese "Log igual" é um requisito sobre medidas ("no new
lengths", §1), e o forcing decide sentenças "medida a medida"; dentro de uma medida
antiga já presente, semear um elemento novo não afronta a condição. A conferência
página-a-página do Thm 9.4.2 em [7] permanece pendente, mas **não há impedimento
aparente** — e a releitura direta do v4 (§6) não revelou nenhum texto adicional sobre
`Log` que reforce a condição até membership de elementos.

### §2.3 Eliminação das leituras (L1)/(L2)/(L3) da Equipe E

- **(L1) refutada pelo próprio texto:** o artigo define `Log(M) = {|m| | m ∈ M}` no §2 —
  medida crua, sem partes canônicas nem requisitos `Σ^b_1`. Não há como ler (7) mais forte
  que "conjunto de comprimentos". (A)+(P)
- **(L2) refutada por §3(a):** `i_0` é p-tempo definível a partir de `σ`, mas `σ ∈ M'`
  apenas — e exigir `σ ∈ M*` é refutado por colapso (§3(c)). O parâmetro que define `i_0`
  mora fora de `M*`. (P)
- **(L3) não reconstruída:** não encontramos argumento comprimido admissível que feche o
  passo; §3(b) fecha a última rota natural (prova mais curta via p-boundedness). (P)

---

## §3. Tentativas de reparo — todas examinadas, com resultado honesto

### §3(a) Reparo (a): `i_0` = menor índice com `σ_{i_0}:P ⊢ α_{i_0}` (p-tempo definível de `σ`)

(P) A verificação de prova é p-tempo; logo "menor `i < m` tal que `σ_i:P⊢α_i`" é
computável em p-tempo a partir de `σ` (e da lista `α`). Como `σ ∈ M'` e `M'` é fechada
sob funções PV, conclui-se apenas `i_0 ∈ M'` — que o artigo **já tem** (`i_0 ∈ M'` nunca
esteve em dúvida; o problema é passar de `M'` para `M*`).

Falha do reparo: p-tempo definível de `σ` só transfere pertinência para estruturas que
**contenham `σ`** (ou os dados relevantes de `σ`). Como `σ ∈ M'` apenas, o reparo é
circular: pressupõe o próprio `i_0 ∈ M*` que se quer provar, ou pressupõe `σ ∈ M*`,
refutado por §3(c). **Resultado: reparo (a) falha.** O problema não é definibilidade de
`i_0`, é o **local do parâmetro** que o define.

### §3(b) Reparo (b): p-boundedness — `|σ_{i_0}| ≤ |α_{i_0}|^c`

(P) Passo a passo:

1. **O que p-boundedness dá.** Toda prova `σ_i` de `α_i` tem medida `≤ |α_{i_0}|^c`. Como
   `α_{i_0}` é parâmetro antigo (`α_i ∈ M`), `|α_{i_0}| ∈ Log(M)`: toda prova candidata tem
   **comprimento velho**.
2. **Por que comprimento velho ≠ elemento velho.** O conjunto `{x : |x| ≤ k}` tem
   cardinalidade `~2^k` (gigantesca e não-padrão para `k` não-padrão). Ter todos os
   comprimentos velhos em Log não força conter **nenhum** elemento específico velho.
   p-boundedness é uma afirmação de Log — e Log não dá membership (§2). Da forma como
   está, o reparo entrega exatamente E5, não E4.
3. **Tentativa de fechar via "prova mais curta".** Seja `σ'` a prova mais curta de
   `α_{i_0}` em `M'` (existe: `M' ⊨ σ_{i_0}:P⊢α_{i_0}`). Buscar entre candidatos de
   comprimento `≤ |α_{i_0}|^c` é p-tempo **com clock**, definível em PV a partir de
   `α_{i_0}`. Como `α_{i_0} ∈ M ⊆ M*`, parece que `σ' ∈ M*` por fechamento PV — daí
   `M* ⊨ σ':P⊢α_{i_0}` e contradição com (8)+Ref_P em `M*`...
4. **...mas isso é impossível, e o impossível é o diagnóstico.** Se `σ' ∈ M*` **e**
   `P(σ', α_{i_0})` valesse em `M*`, então `Ref_P` em `M*` (válido: `M* ⊆ M' ⊨ T_PV` e
   `T_PV` é universal — E1) daria `(¬α_{i_0}) ∉ SAT` em `M*`, contradizendo (8) em `M*`
   (que dá `(¬α_{i_0}) ∈ SAT`). Contradição **interna a `M*`** — mas `M*` é modelo. Logo,
   em qualquer instância real, obrigatoriamente: **ou `σ' ∉ M*`, ou `M* ⊭ P(σ', α_{i_0})`.**
5. **Por que ambas as saídas são naturais (não-absoluteness).** "Existe prova de comprimento
   `≤ L` de `α`" é `Σ^b_0` (∃ tableau de comprimento `≤` clock). Para parâmetros **não-padrões**,
   o alcance do quantificador sharply bounded é `M ∩ [0, 2^L]`, e isso é **dependente do
   modelo**: `M* ∩ [0, 2^L] ⊊ M' ∩ [0, 2^L]` é permissível. Em `M'` a busca encontra
   `σ_{i_0}`; em `M*` ela pode falhar (nenhum candidato-prova abaixo do clock pertence a
   `M*`) e retornar o default. Predicados p-tempo com clock **não são absolutos** entre
   subestruturas para parâmetros não-padrões: os quantificadores sharply bounded "enxergam"
   elementos novos abaixo do clock. O fechamento PV garante que o resultado **interno da
   busca em `M*`** está em `M*` — mas esse resultado pode ser justamente o default "sem
   prova", e é em `M'` que a verificação é necessária.
6. **Conclusão do reparo (b).** p-boundedness dá comprimento velho para `σ_{i_0}` (e nada
   mais); membership `σ_{i_0} ∈ M*` (ou `i_0 ∈ M*`) não se segue; e a rota "prova mais
   curta ∈ `M*`" é **refutada pela consistência de `M*`** (item 4). **Reparo (b) falha.**

Observação (P): os itens 4–5 mostram algo mais geral — **toda** correção que arraste para
dentro de `M*` dados suficientes para reabrir a verificação (8)+(proof-check) esbarra em
`Ref_P` em `M*`. O falsificador não pode ser "domesticado" pelo submodelo.

### §3(c) Reparo (c): exigir `σ ∈ M*` — refutado por colapso

(P) Recapitulando o colapso (contexto §4(C)): se `σ ∈ M*`, então `i_0` (menor índice
falsificador, p-tempo definível de `σ`) entra em `M*` por fechamento PV; com
`α_{i_0} ∈ M*`, teríamos **dentro de `M*`**: (8) dá `(¬α_{i_0}) ∈ SAT`, enquanto
`σ_{i_0}:P⊢α_{i_0}` — a contradição com `Ref_P` apareceria já em `M*`, mostrando
`M* ⊭ T_PV`, o que é impossível (`M* ⊆ M' ⊨ T_PV`, teoria universal). Ou seja: em toda
instância satisfatível, `σ ∉ M*` é **obrigatório**.

Consequência: exigir `σ ∈ M*` como "correção" do passo é **refutado** — a exigência torna
as hipóteses inconsistentes (ou, na dosagem mais fraca, é no máximo inútil: nunca poderá
ser atendida). O falsificador tem de ficar **fora** de `M*`; e então `i_0` tem de ser obtido
sem `σ` — que é exatamente o que §3(a) e §3(b) mostram ser inviável pelas rotas óbvias.
**Reparo (c) refutado.**

(C) Ressalva técnica honesta: o colapso pressupõe que a verificação `P(σ_{i_0}, α_{i_0})`
transfira para `M*` quando os argumentos estão em `M*`; para parâmetros não-padrão essa
transferência para baixo é precisamente a sutileza do item §3(b)5. Isso não enfraquece a
conclusão: ou o colapso vale (e `σ ∈ M*` é inconsistente), ou a verificação não transfere
(e `σ ∈ M*` é inútil para reabrir (8)+proof-check em `M*`). Nos dois casos, `σ ∈ M*` não
repara o passo.

---

## §4. Veredito

**Classificação: (iii) — lacuna em v4**, com a ressalva de que o passo é **(ii) válido sob
hipótese extra identificada**. Justificativa da exclusão das demais:

- **(i) rejeitado.** Nenhuma leitura de (7) como "conjunto de comprimentos" produz
  `i_0 ∈ M*` (§2); (L1) é excluída pela definição literal do artigo, (L2) por §3(a),
  (L3) não foi reconstruída e §3(b) fecha a última rota natural.
- **(ii) válido sob (H): `M' ∩ m = M ∩ m`** ("nenhum elemento novo abaixo de `m`").
  Sob (H): `i_0 ∈ M'`, `i_0 < m` ⟹ `i_0 ∈ M ⊆ M*`. Daí o artigo fecha: (8) vale em `M`
  (é axioma de `S` lá) e instancia em `i_0 ∈ M`; `(¬α_{i_0}) ∈ SAT` é `Σ^b_1` (∃z +
  matriz aberta, `∀i<m` sharply bounded), logo **sobe** `M ⊆ M'`; `Ref_P` universal em
  `M'` contradiz `σ_{i_0}:P⊢α_{i_0}`. Note: sob (H), `M*` e `Log` até podem ser
  dispensados do argumento.
- **(iii) portanto,** como (7) está escrita, falta a hipótese (H) ou equivalente: o passo
  é uma lacuna **local** (uma frase), não um colapso do Teorema 4.

**Correção mínima (duas variantes,⇄ ver também `F2_versao_finita.md` neste diretório):**

1. **Substituir (7) por condição de domínio:** em vez de `Log(M*) = Log(M')`, exigir
   `M' ∩ m = M ∩ m` (a forma (F-b') do contexto §4(A)). Aí `i_0 ∈ M ⊆ M*` por membership
   puro, `Log` torna-se desnecessário, e o resto da prova do artigo corre intacto.
2. **Exigir (8) diretamente em `M'` (versão F-sent):** `M' ⊨ T_PV + (¬φ) ∈ SAT +
   ∀i<m (¬α_i) ∈ SAT`. A contradição fecha com `i_0 ∈ M'` **qualquer** (sem E4, sem `M*`,
   sem `Log`): `M' ⊨ (8)` instancia em `i_0` e `Ref_P` em `M'` fecha. Ambas as exigências
   extras são sentenças com parâmetros em `M` (`¬φ ∈ SAT` é `Σ^b_1`; (8) é `Π^b_2`).
   Detalhamento: `F2_versao_finita.md`.
3. **Variante conservadora (C, não verificada):** manter (7) **e acrescentar** (H) — se o
   forcing de [7, Thm 9.4.2] puder ser arranjado para não semear elementos abaixo do `m`
   já presente (plausível: `m` e seus vizinhos de medida antiga podem ser fixados como
   "já decididos"), a prova do artigo fecha como está, com acréscimo de uma linha.

Recomendação operacional: reportar como **(iii)**, oferecendo a correção **(ii)** com (H)
como caminho mínimo para o autor consertar o item (5).

---

## §5. Conselho editorial — como reportar ao autor

Princípios: (1) localizar o passo com citação exata; (2) mostrar a conta concreta (Log é
medidas; `j < m` novo não muda Log); (3) oferecer a correção mínima já pronta; (4) perguntar
se há argumento oculto, sem acusar; (5) lembrar que a lacuna é local e o teorema é
plausivelmente consertável — o tom é de colaboração.

Esboço de nota (em inglês, para o autor do artigo):

> Dear Dr. Krajíček, I am reading arXiv:2506.20221v4 with great interest. In §3, item (5)
> of the proof of Theorem 4, the sentence "But by (7) i_o is also already in M∗" seems to
> derive `i_0 ∈ M*` from `Log(M*) = Log(M′)`. Since `Log(M) = {|m| : m ∈ M}` records only
> measures, and any new element `j < m` has `|j| ≤ |m|` (a measure already in `Log(M)`),
> condition (7) appears compatible with `M′` containing indices below `m` outside `M*`.
> The step would follow from the additional domain condition `M′ ∩ m = M ∩ m`; alternatively
> the axiom (8) could be required directly in `M′`, which would close the contradiction
> without `M*` and `Log`. Am I missing an argument — e.g., a feature of the forcing in
> [7, Thm 9.4.2] that also prevents new elements of old measure below `m`? Best regards.

Observações finais ao autor interno (organização): o passo é a **única** função de `M*` e
`Log` no item (5) (tabela E4); se ele cai como lacuna, o ataque da Equipe E/estratégia 3(c)
ganha um alvo preciso — e as versões finitas (F-b')/(F-sent) são exatamente as correções
mínimas, cf. `F2_versao_finita.md` e `E_ataque_problema21.md` §1.5.

---

## §6. Estado da verificação externa — **CONCLUÍDA (10/10/2026)**

- **(A)** Transcrição §1, definição de `Log` e passo (5): conferidas diretamente no HTML de
  v4 (https://arxiv.org/html/2506.20221v4), extraído em 10/10/2026. Transcrição idêntica à
  de `F_CONTEXTO_ATAQUE.md` §1.
- **(A) Busca por texto adicional sobre `Log`:** ocorrências de "Log" no paper inteiro:
  (i) §2, definição + "introduces no new lengths" + (5); (ii) Problem 2.1, item (3)
  (`Log(𝐌*) = Log(𝐌′)`); (iii) Teorema 4, item (5), (7). **Nenhuma nota de rodapé, remark
  ou definição ampliada** de `Log` (nada de "partes canônicas", nada de elementos
  canônicos por medida). A frase de §2 "(with an additional requirement on 𝐌)" refere-se a
  uma exigência **sobre M** no construction de [7, Thm 9.4.2], não a restrição de
  elementos novos em 𝐌′.
- **(A) Verificações de apoio do item (5), confirmadas no v4:** (a) Problem 2.1 exige apenas
  (1) preservação `Σ^b_1(PV)` de `𝐌*`, (2) `𝐌′ ⊨ T_PV + (¬φ) ∈ SAT`, (3) `Log` igual —
  **nada sobre domínios abaixo de `m`**; (b) o remark "it suffices if 𝐌* preserves from 𝐌
  properties of the form `∀i∃y B(x,i,y)`" também é só sobre preservação, não membership;
  (c) o §2 confirma o traspasse `Σ^b_1` para cima usado na correção (ii) ("𝐌′ preserves
  (i.e. will satisfy) all Σ^b_1 properties of elements of 𝐌").
- **Pendente apenas:** conferência página-a-página de [7, Thm 9.4.2] (livro, não online) —
  irrelevante para o veredito, pois o passo do artigo só pode apoiar-se no que o artigo
  afirma, e o artigo afirma apenas (7).
- **Conclusão da verificação externa:** não há texto em v4 que resolva o passo. O veredito
  §4 — **(iii) lacuna local, reparável por (ii) sob `M′ ∩ m = M ∩ m`** — permanece tal
  como está, agora sem pendência de leitura do artigo.

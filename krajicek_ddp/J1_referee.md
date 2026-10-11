# Referee hostile — `J1_Qcompactness_M0.md`

> Relatório final (regravação do esqueleto pré-leitura; o esqueleto foi gravado **antes**
> da leitura, conforme procedimento). Revisor: referee hostile de lógica/proof complexity.
> Marcação usada: **(A)** = fonte/artigo; **(P)** = próprio; **(C)** = conjetura.
> Fontes conferidas: `H1_colecao_refutacao.md` §1.1, `I1_Qcompactness_ultrapoderes.md`
> (A.1, A.2, A.5, A.7, B.3(ii), C.1, C.3), `A_teoremas_exatos.md` §1.1, §1.11, §1.12, §3(b), §3(d),
> `CONTEXTO_COMUM.md` itens 11–14, `F2_versao_finita.md` §0 (definição de (S1)–(S4)).

---

## VEREDITO: **REVISION** — 3 FATAL, 5 MAIOR, 6 MENOR, 3 ESTILO

**Borda para REJECT:** o Teorema J (e portanto "C.3 decidida", §6 L147–152) **não está
provado**; pior, sem a análise de tamanhos ele pode ser **falso** (receita de
contraexemplo no FATAL 2). Se a correção de F1–F3 sair negativa (nenhum `C_N` de tamanho
padrão, ou `τ_N` universalmente 0), o resultado central cai e o texto vira REJECT.
A arquitetura do argumento, porém, é recuperável — por isso REVISION e não REJECT.

---

## §1. FATAL

### F1 — `J.0(b)`: princípio geral **falso** + propriedade de tamanho nunca verificada
**Local:** L29–37 (enunciado L31–33; prova L35–37); repetido na checklist L135.

1. *"Monotonia de tamanho de funções p-tempo: entrada não-padrão dá saída não-padrão"*
   é **falsa em geral**: `f ≡ 0`, `f(x) = x mod 2`, projeção de 1 bit são p-tempo e mandam
   entrada não-padrão em saída **padrão**. O que é verdade é só: *entrada padrão ⟹ saída
   padrão* (a direção usada em J.0(a), correta).
2. A conclusão de J.0(b) (`code(C)=p` padrão ⟹ `C` padrão) é salvageável **só** por uma
   propriedade específica do esquema de codificação: `code` é injetiva com inversa
   p-tempo (**decodificação**), ou `|code(C_N)| ≥ |N|`. Nenhuma das duas é demonstrada —
   a prova de J argumenta sobre `|C_N|` vs `|N|`, que é a instância **outra** (ver F2).
3. **Buraco maior:** J.0/J §2 nunca analisam o tamanho de `δ_N` e `τ_N`. Pela definição
   da semente (H1 §1.1 L30–35) `δ_N` é "circuito em `M` (comparação p-tempo nos bits,
   **`m` fixo**)" — com `m` não-padrão embutido — e `τ_N` é uma **disjunção interna
   finita** sobre `q` (intervalo governado por `|α|`/átomos, não-padrão). Sob a leitura
   natural ("`m`, `α` embutidos no texto"), `|C_N|` é **não-padrão para todo `N`**, o que
   torna **falsa** a classificação da L71–72: *"Os membros padrão de `𝒯` são exatamente
   `{C_N : N padrão} ∪ {1}`"*.

**Correção sugerida:** (i) reescrever J.0(b) como *decodificação* ("`code` tem inversa
p-tempo; entrada padrão ⟹ saída padrão" — direção segura); (ii) acrescentar um lema de
tamanhos com a análise explícita de `δ_N`, `τ_N`, `m` e do intervalo de `⋁_q`, citando a
definição de H1 §1.; (iii) trocar "exatamente" por ⊆, ou provar a inclusão contrária.

### F2 — `J.1`: "α_{i₀} de tamanho padrão" **não segue** de `i₀` padrão; sem isso `τ_N(v)` não se sustenta
**Local:** L46–51 (L48 é o pulo).

A cadeia exigida é: `(S4)` interno `⊨ ∃σ Fals(σ, α_{i₀})` ⟹ **falsificador real**.
Isso só vale se **`α_{i₀}` tiver tamanho padrão**:

* `m` é não-padrão e `α` é uma disjunção disjunta de `m` peças; **nada em (S2)–(S4)**
  garante que a peça de **índice padrão** tenha tamanho padrão (a peça 0 pode ser
  gigante; `m ≤ |α| ≤ n` não ajuda).
* A testemunha σ que `(S4)` fornece é um elemento de `M_0` — **pode ser não-padrão**
  (resposta direta à pergunta do referee: *nem todo elemento de `M_0` é número real*;
  o que se precisa é a convenção `ℕ ⊆ M_0` + fechamento para baixo, **não declarada** —
  é a mesma "convenção usual mas não explicitada" que `A` já registrou em §1.12 L245).
* Com `α_{i₀}` ou σ não-padrões, `Fals(σ, α_{i₀})` é `Δ^b_0` **com dados não-padrões**
  e **não é absoluto** — exatamente o Limite A.7 do I1 (L91–97). "σ falsificador"
  significa avaliação **real** de circuito padrão **só** quando circuito, atribuição e
  leitura são todos padrão; caso contrário é avaliação interna.
* Faltam ainda: (a) a testemunha estar **no intervalo da `⋁_q`** de `τ_N` (limite de
  tamanho não discutido); (b) decidir o sentido de "`C_N(v)` verdadeira para toda `v`
  real" — se `C_N` é de tamanho não-padrão, "tautologia real" **nem se aplica**
  (A.7(b) do I1).

**Contraexemplo-orientação (o teorema pode ser falso):** se existir `N` padrão com `C_N`
de tamanho padrão e `τ_N(v)=0` para toda `v` real, então `C_N` é uma fórmula real
**insatisfatível**; pelo Lema A.2 do I1 (completude clássica de EF) existe `d* ∈ ℕ`
refutando `L = {C_N}` — refutação **genuína**, com `M_0 ⊨ "premissa ∈ L"` — e o Teorema J
**cai**. Logo J.1 não é decorativo: é o load-bearing theorem, e está asserted, não provado.

**Correção sugerida:** provar que `|p|` padrão com `p = C_N` **força** `|α_{i₀}|` padrão
(pela codificação: `τ_N` embute `D(α, i₀)`), **ou** declarar `|α_i|` padrão para `i`
padrão como hipótese nova sobre `M_0` (o que rebaixa o escopo "todo `M_0`"), **ou**
reescrever J.1 em termos de absolutidade só para dados padrão e reencaixar no Teorema J.

### F3 — `Teorema J`: o caso que **sobrou** (constantes-1) nunca é provado
**Local:** L73 ("`C_N` (N padrão) ou `1` — tautologia **real** pelo Lema J.1"); L41–42
(só afirmado entre parênteses); prova de J.1 L52–53 pula direto para EF.

* Se F1(3) estiver correta (nenhum `C_N` de tamanho padrão), então **toda** premissa
  padrão de `d*` é um `C ≡ 1 em M` de tamanho padrão — e J.1 **não** a cobre. O único
  caso remanescente do Teorema J é justo o que o texto não demonstra.
* O argumento que falta é curto e existe: `|C|` padrão + `C ∈ M_0` ⟹ `C` é circuito
  real (fechamento para baixo); `M_0 ⊨ ∀v (v ⊨ C)` (definição de `≡ 1`) ⟹ vale para
  toda atribuição **real** `v ∈ M_0`, e a avaliação de circuito **padrão** sob dados
  padrão é absoluta (I1 A.3/A.4) ⟹ `C` tautologia real.

**Correção sugerida:** enunciar e provar "Constantes-1 padrão são tautologias reais"
como Lema J.1′, e reescrever a classificação do Teorema J como disjunção de casos com
a inclusão correta.

---

## §2. MAIOR

### M1 — `Corolário J.3`: "em particular, toda refutação interna ... usa premissas de tamanho **não-padrão**" (L81–82) não decorre do Teorema J
O Teorema J só trata `d* ∈ ℕ` (usa J.0(a)). Para `d ∈ M_0` **não-padrão**, as linhas
podem ser de tamanho padrão (não-padrão é o **número** de passos, não cada linha). A
afirmação é *provável*, mas por outro argumento: premissa padrão ∈ `𝒯` padrão ⟹
tautologia real (F1–F3) ⟹ satisfeita por **toda** atribuição interna (avaliação absoluta
de circuito padrão) ⟹ contradiz **soundness interna** `Ref_EF ∈ T_PV` (I1 Nota A.5).
Nenhum desses passos está no texto. Ainda ambíguo: "usa premissas não-padrões" = *todas*
ou *alguma*? **Correção:** provar o Caso Interno à parte (2 linhas, citando `Ref_EF ∈ T_PV`)
eprecisar o quantificador.

### M2 — §4, Rota 2 (L107–108): *non sequitur*
*"Nenhuma refutação genuína ... — logo nenhum objeto padrão organiza a coleção."* O
Teorema J nega **refutações EF genuínas**, não "objetos padrão que organizam `i ↦ σ_i`".
Um objeto padrão não pode organizar `i ↦ σ_i` para `i < m` não-padrão trivialmente por
domínio (não é teorema nenhum); e a impossibilidade de um seletor **p-tempo** é B.3(ii),
não J. **Correção:** ou definir "organiza" = "produz refutação genuína" (e mostrar a
redução), ou retirar a Rota 2 da lista de "rotas mortas por J" — como está, o
estreitamento do item 2 conta um resultado que não tem.

### M3 — `J.2`: a justificativa escrita é falsa como afirmação geral (L62–63)
*"(S4) para `i` padrão dá falsificador **real** de `α_i`"* — não dá (é o mesmo pulo de F2).
No **ramo** em uso a padronidade salva: se `Ref_P(r_i, α_i)` com `r_i` real, então `α_i`
é **linha** de `r_i` (conclusão p-tempo de entrada padrão ⟹ padrão, J.0(a)) ⟹ `α_i`
padrão ⟹ absolutidade ⟹ `α_{i₀}` tem falsificador real ⟹ contradição com "autologia
real". **Correção:** mover a padronidade de `α_i` para dentro do ramo e escrever o passo.
Com isso J.2 fecha (ver §5).

### M4 — Citação inexistente: `A_teoremas_exatos.md §1.14` (L102 e L140)
`A` **não tem** §1.14 (seções 1.0–1.13, depois §2). BB/Cook–Thapen está em **§3(d)**
(L442) e `CONTEXTO_COMUM.md` item 11. Conteúdo citado ✓ ("não provável em `T_PV` a menos
que fatoração não seja difícil"; ano/venue TOCL 2006 ✓ — título real *The strength of
replacement in weak arithmetic*, TOCL 7(4)) — só a referência está errada. **Correção:**
apontar §3(d)/CONTEXTO item 11.

### M5 — "item (1) do artigo" é **ambíguo** e "hipóteses verbatim do Teorema 4" é impreciso
**Local:** L12 (§0), L87–88 (J.4), L133 (checklist), L148 (§6).
O verbatim *"φ não tem prova em `M` em nenhum pps"* é a **Condition 1 do Teorema 3**
(`A` §1.11; `CONTEXTO_COMUM` item 12; `A` §3(b) L374–375) — **não** o item (1) da prova
do **Teorema 4** (`A` §1.12(1) = "supor `NP=coNP` e `(ST)` ... escolher `P` p-bounded").
Além disso, as hipóteses do **Teorema 4** são *(Problema 2.1 afirmativo) + (ST)*;
`M ⊨ S` (=(S1)–(S4)) e Condition 1 são **ingredientes das provas** (S é derivada via KPT).
**Correção:** "hipóteses **reformuladas** (P): `M_0 ⊨ T_PV+(S2)+(S3)+(S4)` **+ Condition 1
do Teorema 3**"; e citar `A §1.11` + `CONTEXTO item 12`, não "§1.9–1.12".

---

## §3. MENOR

1. **N1 (L89)** — `"...nenhum d ∈ M_0 satisfaz Ref_EF(d, φ), i.e., M_0 não refuta internamente {¬φ}"`:
   a equivalência *refutação de `{¬φ}` ⟺ prova de `φ`* é padrão mas está escondida no
   "i.e."; escrever o lema de conversão (2 passos; EF simula Frege + `¬¬φ ⟺ φ`, p-tempo).
2. **N2 (L43–44, 52–53)** — J.1 conclui *"nenhuma subfamília ... tem refutação EF alguma
   (**interna** ou genuína)"*, mas a prova dada cobre só derivações **reais** (axiomas
   tautologias + preservação sob atribuições reais). O caso interno exige
   `Ref_EF ∈ T_PV` (I1 Nota A.5) + "tautologia real de circuito padrão é satisfeita por
   toda atribuição interna" (absolutidade). 2 linhas — mas falta.
3. **N3 (L60–64)** — convenções não declaradas em J.2: `r` real **∈ `M_0`** (`ℕ ⊆ M_0`);
   `(r)_i = 0` para `i ≥ |r|` (convenção das funções de sequência de PV); `0` não codifica
   derivação. Todas plausíveis/`(A)`-padrão, mas precisam ser enunciadas.
4. **N4 (L114–121, J.5)** — (a) "a instância local de BB é **positiva em `T_PV`**": seria
   "em `T_PV + (S4)`" (e, se vale em **todo** `M_0`, por completude de 1ª ordem é
   demonstrável de `T_PV+(S4)` — remark necessária); (b) "se **não** ... a rota (B) de
   `H1 §3.3` é **confirmada**" — salto: não-colecção interna ≠ "refutações só globais";
   e o Teorema J já mata a rota-padrão **em qualquer caso**, logo a não-colecção não é o
   que confirma (B). Apoiar ou rebaixar para `(C)`.
5. **N5 (L49, 54–55)** — duas imprecisões de fonte: (a) "absolutidade ... (`cálculo padrão
   finito — Lema J.0`)" — J.0 **não** prova absolutidade de avaliação (é fato à parte:
   I1 A.3/A.4, §5 item 5); (b) a Nota (A) diz que absolutidade de circuito padrão é
   "exatamente o que o artigo usa em (8)" — **não**: o artigo usa preservação `Σ^b_1` de
   `M*` sobre `M` para **parâmetros de `M` (possivelmente não-padrões)**; mecanismo
   diferente do que J invoca. Trocar a glossa.
6. **N6 (§6 L147–152)** — "C.3 está **decidida** ... em **todo** `M_0` com as hipóteses
   do artigo" herda M5 e F1–F3; rebaixar para "**condicionada** à análise de tamanhos
   (F1–F3)". Checklist L136 (`I1 item 7` p/ absolutidade de circuito) aponta para o item
   errado (item 7 = Σ₁-soundness de ultrapoderes); o cite certo é I1 A.3/A.4.

---

## §4. ESTILO

1. **E1 (L123)** — "(C) Conjetura (P)": marca dupla; manter só **(C)**.
2. **E2 (L154)** — "Próxips passos" → "Próximos passos".
3. **E3 (L18–20)** — "nenhum `d*` ... de modo algum `L`" — pleonasmo/confuso; e
   "interna-mente" (L17) com hifenização estranha.

---

## §5. O que está **CORRETO** (declarado explicitamente)

* **J.0(a)** (L29–31, 35): correta. `d* ∈ ℕ` ⟹ decodificação p-tempo ⟹ toda linha,
  inclusive premissas, é string de tamanho padrão. É o passo que **impede** que `¬φ`
  (tamanho não-padrão, `m` não-padrão) seja premissa de derivação real — essencial.
* **Tamanho não-padrão de `¬φ`** (L72): correto (`φ = ⋀_{i<m} ...` proposicional
  desenrolado, `m` não-padrão — `A` §1.12(4)).
* **J.2 no mérito** (tese): correta — suporte de `r` real é padrão; para `i` padrão no
  suporte, `Ref_P` real + soundness real de `P` (`A §1.1`: pps é soundo **e** completo
  por definição) dá autologia real; para `i` não-padrão, `(r)_i = 0`. Só a *justificação*
  do passo `(S4) → falsificador real` está mal escrita (M3), e a correção é local.
* **Teorema J.4 (tese)**: correta **como condicional a Condition 1 do Teorema 3**, que o
  §0 de fato declara como hipótese. `item (1) ⟹` nenhum `d ∈ M_0` prova `φ` em EF ✓ (EF é
  pps). Só faltam N1 e a correção de M5.
* **Composição do Teorema J — sem circularidade** ✓: J.0 (tamanho) ⟶ J.1 (tautologias,
  usa só `(S4)` + absolutidade) ⟶ soundness **real** de EF (I1 §5 item 5). Nenhum lema
  usa o outro; `¬φ` é tratado por tamanho, não por J.1/J.2.
* **Completude de `P` **não** é usada** ✓ — confirmado como pedido: as provas usam só
  (i) soundness real de `P` (J.2), (ii) soundness real de EF (J, J.1), (iii) Condition 1
  (assumida, não derivada). `P` "soundo e completo" (L13) é `(A)` por **definição** de
  pps (`A` §1.1: `∃x P(x,y)` define `TAUT`) e é enunciado, nãoconsumido.
* **Fidelidade a C.3** ✓: o enunciado do Teorema J (L16–20) reproduce literalmente a
  pergunta de `I1` Proposição C.3 (`d* ∈ ℕ` + pertinência interna das premissas em `L`),
  inclusive a cautela "sem afirmar avaliação real de `d*` contra `L` não-padrão".
* **§4 Rota 1 (B.3(ii))** ✓: "nenhum seletor p-tempo" está correto (o "incondicional" é
  sob as hipóteses correntes `(S2)+(S3)+Ref_P`); "esse `F` é necessariamente não-p-tempo"
  (L118) ✓; BB/Cook–Thapen em substance ✓ (só o cite está errado, M4).
* **Marcação (C)** da conjetura de independência (L123–126) ✓ está feita, e as "Lacunas
  honestas" (L163–168) são precisas — inclusive ao antecipar os alvos deste referee.

---

## §6. Respostas diretas às 5 reivindicações

1. **J.0** — (a) **correto**. (b) **F1**: o princípio "entrada não-padrão ⟹ saída
   não-padrão" é falso; a instância necessária é `|code(C_N)| ≥ |N|` **ou** decodificação
   p-tempo, provada contra H1 §1.1 (não está). A busca interna sobre `Names` (intervalo
   não-padrão) **é legítima** como existencial de 1ª ordem (não precisamos executá-la);
   o que **exige** o argumento de tamanho é a conclusão `N` padrão — sem ele, o caso
   "p = C_N" do Teorema J não fecha, e a classificação "exatamente" (L71–72) é não provada
   e provavelmente falsa (m e α embutidos ⟹ nenhum `C_N` seria padrão).
2. **J.1** — **F2**: `δ_N(v)` internamente verdadeira ✓ (padrão < não-padrão **em `M_0`**,
   não "comparação real" — terminologia errada em L47). O pulo `(S4)+absolutidade ⟹
   falsificador **real**` exige `|α_{i₀}|` padrão, **não** dedutível de `i₀` padrão; σ
   interna é elemento de `M_0` e pode ser não-padrão; "falsificador" = avaliação real só
   com dados padrão. Toda a conclusão "nenhuma subfamília ... tem refutação EF" é correta
   **dada** as tautologias reais + soundness real de EF, mas o caso interno precisa de
   `Ref_EF ∈ T_PV` (N2).
3. **J.2 + J.4** — salto "refutação interna de `{¬φ}` = prova interna de `φ`": **correto,
   não enunciado** (N1). Uso do item (1): **correto como hipótese declarada**, mas o nome
   e o cite estão errados (M5: é Condition 1 do **Teorema 3**, §1.11 — o item (1) do
   §1.12 é outra coisa); "verbatim do artigo" não se sustenta para "hipóteses do Teorema 4".
4. **Teorema J** — composição **sem circularidade** ✓; **completude de `P` não usada**
   ✓ (confirmado, §5 acima). O que falta é só o conteúdo de F1–F3.
5. **§4 / J.5** — estreitamento do item 2: Rota 1 ok; **Rota 2 é non sequitur** (M2);
   Rota 3 plausível mas "é precisamente isso que BB forneceria" é `(C)`-flavored e deveria
   ser marcado. Conjetura de independência: **marcada (C)** ✓ (mas "Conjetura (P)" E1).
   Salto "coleção interna F ⟶ BB/Cook–Thapen": BB é esquema de coleção sharply bounded
   para **fórmulas abertas**; a multifunção `i ↦ Fals(F(i), α_i)` tem `Fals` `Σ^b_1` com
   **parâmetros não-padrões** `α_i` — a equivalência com a instância de BB precisa ser
   justificada (N4a) antes de dizer que "BB forneceria (ou não)".

---

## §7. Exigências para re-submissão (ordem de ataque)

1. **Lema de tamanhos** (fecha F1 + F2 + a classificação): tamanhos de `δ_N`, `τ_N`,
   `¬φ`, `α_i` (i padrão) e o intervalo da `⋁_q`, a partir de H1 §1.1.
2. **J.1 reescrito** só para dados padrão + caso constante-1 como lema próprio (F3).
3. **J.3 — Caso Interno** separado via `Ref_EF ∈ T_PV` (M1).
4. **§4 Rota 2** reescrita ou retirada (M2); **J.5** com BB justificado e `(C)` correto.
5. **Citações**: §3(d) no lugar de §1.14; Condition 1 do Teorema 3 no lugar de "item (1)";
   I1 A.3/A.4 no lugar de "I1 item 7".
6. **§0/§6**: "hipóteses reformuladas (P)" e escopo "decidida" → "condicionada".

---
---

# Revisão da v2

> Alvo: `J1_Qcompactness_M0.md` **v2** (213 linhas, marcada "pós-referee"). Rodada 2.
> Fontes reaproveitadas + releitura de `A` §1.0 (definição de `T_PV`) e §4.2 L513–518.

## VEREDITO v2: **REVISION (leve)** — 0 FATAL, 3 MAIOR, 5 MENOR

Melhora substancial: as 8 correções da rodada 1 foram aplicadas, sete delas de fato; os
três FATAL foram eliminados por **retirada + hipótese explícita (Hjoint)** — manobra
legítima (§A). O **Teorema K está correto no mérito** (é o achado da v2), mas o passo (a)
tem a fundação errada (MAIOR-1) e o §2/§4 tem descompasso de quantificadores (MAIOR-3);
J.0′ continua não estabelecido e o artigo avisa contra (MAIOR-2). Com as três correções:
**RECOMENDADO**.

## §A. Status das 8 correções da rodada 1

| # | Item rodada 1 | Status v2 | Verificação |
|---|---|---|---|
| FATAL-1 | J.0(b) falso + classificação de tamanhos | **RESOLVIDA** | J.0(b) retirado (L36–38); classificação dispensada; J′ usa só J.0(a). Substituição por hipótese explícita é **legítima** — (Hjoint) é enunciada, rotulada e analisada; nenhum problema novo escondido (Ref_EF ∈ T_PV é usado corretamente). |
| FATAL-2 | J.1 "tautologia real" não provada | **RESOLVIDA** | J.1 retirado; a necessidade virou (Hjoint), com o obstáculo identificado (ponto fixo) em vez de contornado. |
| FATAL-3 | caso constantes-1 só afirmado | **RESOLVIDA** | §2(i): "constantes-1: satisfatíveis **internamente** trivialmente" — correto para o novo framework (≡1 em `M_0` ⟹ toda atribuição interna satisfaz). |
| M1 | J.3 exigia soundness interna | **RESOLVIDA** | J′ usa `Ref_EF ∈ T_PV` (L74). ✓ |
| M2 | Rota 2 = non sequitur | **RESOLVIDA** | §4 reescrito; a "morte" da rota-padrão não é mais reivindicada. ✓ |
| M3 | J.2 justificada mal | **RESOLVIDA** | J.2′ com descompasso de tamanhos — e está **correta** (§E). ✓ |
| M4 | `§1.14` inexistente | **RESOLVIDA** | L442 + CONTEXTO item 11 (conferidos). ✓ |
| M5 | "item (1)" ambíguo | **RESOLVIDA** | "Condition 1 do Teorema 3", L190/L375/L514 (os três conferidos). ✓ |

## §B. Teorema K (§3) — auditoria (a)–(d)

**Tese correta.** A amalgamação "união de falsificadores com suportes disjuntos (S2) +
`Ref_P`" é o mecanismo de B.3(i)/B.1, e K o fecha para `m` não-padrão. A conclusão
"`T_PV+(S2)–(S4)+BB` inconsistente" e a decisão negativa de J.5 são **corretas**.

**(a) Compreensão Δ^b_0 — MAJOR-1 (fundação errada, conclusão salvável).**
`T_PV` é a **teoria universal verdadeira** de `L_PV` (`A` §1.0 L19–26, verbatim). A
instância "∃x ∀i<a (x(i)=1 ↔ φ(i,z))" **não é universal** — logo não é axioma — e a
citação "padrão — Cook–Nguyen" (checklist §5 nº 4) cobre `PV`/`IΔ_0+exp` (onde a soma
limitada é provável por indução `Δ_0`), **não** modelos arbitrários da teoria universal
verdadeira (que podem falhar indução; o artigo até avisa, L21–22, que um pps "may be
incomplete in a model of `T_PV`"). **Reparo local (recomendado):** não usar compreensão —
definir `σ* := G(F,α)` com `G` **função PV** (união dos suportes; `|α| ≥ m` ⟹ p-tempo);
existência: símbolo de função é total em `L_PV`-estrutura ✓; correção: a sentença
**universal verdadeira** `∀F,α,σ,i,p (σ=G(F,α) ∧ i<m ∧ p∈at(α_i) → (σ_p=1 ↔ (F(i))_p=1))`
está em `T_PV` ✓ e vale em `M_0` **para dados não-padrões** ✓. (Reparo alternativo: provar
a instância de compreensão necessária a partir das instâncias de indução `Δ_0` de matriz
**universal** — absorção de quantificadores limitados por guardas em `L_PV` — argumento
que a v2 não tem.)

**(b) `σ*↾at(α_i) = F(i)↾at(α_i) ⟹ Fals(σ*, α_i)` — CORRETO, com lema faltando.**
Bits de `F(i)` fora de `at(α_i)` **não** atrapalham: (S2) (`A` §1.2: "no two `α_i` have an
atom in common" ✓) dá disjunção de suportes; e o "logo" exige **localidade da avaliação**
("σ,τ concordam em `at(β)` ⟹ ev(β,σ)=ev(β,τ)") — sentença **universal verdadeira** de
`L_PV` (`ev` é símbolo de função PV), logo axioma de `T_PV` e válida para todos os
elementos de `M_0`, não-padrões inclusive. Enunciar o lema.

**(c) Composicionalidade para circuito não-padrão — conclusão correta, justificativa errada.**
"Δ^b_0, passo a passo, interno" **não** é fundação: absolutidade `Δ^b_0` falha com dados
não-padrões (era o ponto A.7 do I1). O caminho certo é o de (b): "∀i<m Fals(σ*,α_i) ∧
`α = ⋁_{i<m} α_i` ⟹ Fals(σ*,α)" pré-prensificado é sentença **universal verdadeira**
(absorção de `∀i<m` por guarda `i<m`, `A_b` PV) ⟹ axioma de `T_PV` ⟹ vale em `M_0` para
o `α` não-padrão. Reescrever este passo.

**(d) Contradição com (S3) — CORRETA, mas a menção à Nota A.5(β) é desnecessária e
perigosa.** Basta `Ref_P ∈ T_PV` pela **rota (α)** (definicional: "`x : P ⊢ y → (¬y) ∉ SAT`
é sentença universal verdadeira" — `A` §1.0 L21–22 verbatim + §1.12(5)); a rota (β)
(provabilidade em `PV` por indução `Δ_0`) **não** transfere para modelos arbitrários de
`T_PV`. Trocar a glossa.

## §C. Corolário K.2 — legítimo; fidelidade do remark PARCIAL

Aplicação de BB a `∀i<m ∃y Fals(y,(α)_i)`: matriz `Fals` é **aberta/`Δ^b_0`** (`Fals` e
projeção `D` são PV ✓); `y` bounded (`|y| ≤ |α|` ✓); `i` **sharply bounded** (`i<m≤|α|` ✓).
A forma coletada `∃z ∀i<m Fals((z)_i,(α)_i)` dá exatamente o `F` proibido por K ✓.
**MENOR:** a leitura "o Teorema K é **o mecanismo** da invalidação (L442)" é (P) exagerada:
o artigo diz que, com BB, "the KPT theorem of [16] does not apply in any usable form to
this non-universal theory" — o motivo declarado é a **perda de universalidade**; K é um
mecanismo **adicional** no nível da semente. Reenunciar como "contribuição (P) coerente
com a remark", não como o seu mecanismo.

## §D. Lema J.0′ (completude interna de EF) — NÃO ESTABELECIDO (MAIOR-2)

* Em `PV`/`IΔ_0+exp`: **plausível** (expansão de Shannon + indução `Δ_0` sobre `|φ|`,
  concatenação PV; fórmula de indução tem matriz com quantificadores universais após
  guardas). Não refutado.
* Em **modelos de `T_PV`** (o que J.0′ precisa): **não demonstrado**, e o artigo avisa
  em contrário (L21–22: pps "may be incomplete in a model of `T_PV`"). A rota seria
  mostrar que **todas** as instâncias de indução usadas são de matriz universal
  (verificável, mas é um argumento novo que a v2 não escreve).
* **O que cai se J.0′ falhar:** Condição J.4 (satisfatibilidade interna de `¬φ`), §0.3
  ("internamente-satisfatível"), §2(ii) e — não registrado nas "Lacunas honestas" — o
  **ramo 2 da dicotomia** de §2 ("refutação interna **existe** por completude interna
  J.0′"). J.2′, K e J′ (condicionado a (Hjoint)) **não** dependem dele ✓ (a v2 afirma
  isso corretamente, mas omite a dicotomia). Acrescentar à lista de lacunas.

## §E. J.2′ e Condição J.4 — CORRETOS

* **J.2′ correta** (M3 bem resolvido). Duas notas de sustentação a escrever: (i)
  "`(r)_i` padrão ⟹ última linha padrão ≠ `(α)_i` não-padrão": vale porque um strong pps
  tem conclusão = linha (`|β| ≤ |σ|·poly`), e a comparação interna `|β| vs k` padrão é
  correta; (ii) o uso "padrão < não-padrão" vale em **todo** `M ⊨ T_PV` — para cada `k`
  padrão, `∀x (x<k → ⋁_{j<k} x=j)` é sentença **universal verdadeira** ⟹ axioma; logo
  `ℕ` é segmento inicial e restrições a posições padrão de objetos internos são padrão.
* **Condição J.4 correta** (condicionada a J.0′): Condition 1 ⟹ `M_0 ⊭ ∃d Ref_EF(d,φ)`
  (EF é pps ✓) + contrapositiva de J.0′ ⟹ `M_0 ⊨ ∃r ¬φ(r)`; e `r` é não-padrão por J.2′ ✓.

## §F. §2/§4 (Hjoint, J.6) — MAIOR-3: descompasso de quantificadores + releitura de `code(N,q)`

1. **(Hjoint)** quantifica sobre **toda** subfamília **internamente finita** (L65–67), mas
   §2(iii) e **J.6** (L128–131) falam de "subfamília **padrão finita**" `N_1,…,N_k`. Logo
   "Sim ⟹ (Hjoint) ⟹ C.3 negativa" (L132) **não segue**: subfamílias com condições
   não-padrões ficam de fora. Corrigir o quantificador (ou justificar a redução).
2. **"Ponto fixo" é uma releitura de H1 §1.1.** `τ_N := ⋁_q (q cod. atribuição ∧ Fals(q,(α)_{code(N,q)}))`
   e a semântica declarada em H1 diz `ν_G(τ_N)=1 ⟺ M[G] ⊨ (¬(α)_{ν_G(N)}) ∈ SAT` — o
   **índice depende de `ν_G(N)`** (da atribuição), não de `q`. A leitura "q* falsifica o
   disjuncto que N escolhe **em q***" (auto-referente) é outra fórmula; se for essa a
   intenção, H1 precisa de nota de correção. A "redução" é além disso quase-circular:
   "τ_N(v) ⟺ ∃q falsificando (α)_{code(N,q)}" é o **conteúdo** de `τ_N`, não uma redução
   a um problema externo. Reescrever §2(iii)/J.6 com o quantificador certo e o status
   honesto ("reformulação do obstáculo", não equivalência demonstrada).

## §G. MENORES

1. **§0.3 (L26–27)** — "a **semente** é realmente-insatisfatível / internamente-satisfatível":
   o escopo provado é a condição **`¬φ`** (J.2′+J.4); a semente `𝒯` como um todo não foi
   tratada (J.1, que fazia esse trabalho, foi retirado). Trocar "a semente" por "`¬φ`".
2. **§4 (L142–143)** — "K morre ... mais forte que a hipótese de Cook–Thapen": K e
   Cook–Thapen medem coisas diferentes (consistência com a semente vs. provabilidade de
   BB em `T_PV`); "mais forte" é `(C)`-flavored — marcar.
3. **§5 nº 4** — "compreensão limitada em `T_PV` — **padrão** — Cook–Nguyen": cite errado
   (ver MAJOR-1); nº 3 — a menção "indução `Δ^b_0` da Nota A.5(β) vale para `P`" é
   desnecessária (rota (α) basta) e transfere mal (§B(d)).
4. **§2 dicotomia (L87–90)** — usa J.0′ sem registrar na lista de dependências (§D).
5. **§6 (L168)** — "J.2′+J.4: `¬φ` satisfatível só por atribuições não-padrões" é
   **condicional** a J.0′; rebaixar junto com §0.3.

## §H. Créditos da v2 (o que está correto)

* **Teorema K: tese correta e é o achado da v2** — fecha B.3(iii) com prova, decide J.5
  negativamente em todo modelo, e dá conteúdo novo para a nota editorial.
* **J′: prova limpa e honesta** — premissas padrão (J.0(a)) + `Ref_EF ∈ T_PV` + (Hjoint);
  sem circularidade; escopo "sob (Hjoint)" declarado no enunciado e no §6 ✓.
* **J.2′/Condição J.4** corretas (§E) — a anatomia "realmente-insatisfatível /
  internamente-satisfatível (condicional)" é o local exato da não-compactude.
* Citações da rodada 1 todas reparadas; checklist §5 com os itens "a verificar" marcados
  (nº 6) — transparência adequada.

## §I. Exigências para RECOMENDADO

1. **K passo (a):** reescrever via função PV `G` + sentença universal de correção (ou
   provar a instância de compreensão a partir de induções `Δ_0` de matriz universal).
2. **K passo (c) + lema de localidade** (item (b)) como sentenças universais de `T_PV`;
   retirar a glossa (β) do passo (d).
3. **§2/§4:** corrigir o quantificador (interna-finita vs padrão-finita) e o status da
   leitura `code(N,q)` (nota em H1 se ela mudar).
4. **J.0′:** ou prova (instâncias de indução universais) ou rebaixar §0.3/§2/§6 a
   condicionais explícitos, com a dicotomia incluída nas lacunas.

---
---

# Rodada 3 — v3

> **Rodada 3 — relatório final** (esqueleto pré-leitura gravado antes da leitura, conforme
> procedimento; preservadas as rodadas 1–2 acima). Alvo: `J1_Qcompactness_M0.md` v3 (244 L).

## VEREDITO v3: **REVISION (leve)** — 0 FATAL, 1 MAIOR, 4 MENOR

As três correções MAIOR da rodada 2 foram aplicadas (duas inteiramente, uma em ¾); os
MENOR-1..5 também. A re-auditoria do Teorema K encontrou **um** novo defeito local no
**passo 2** (sentença falsa para α malformado **e** não-universal — Π_2 disfarçado), com
reparo no **mesmo padrão** que a v3 já usa no passo 0 (localizador + bicondicional +
predicado de shape). Com essa reescrita (~6 linhas): **RECOMENDADO**.

## §A. Aplicação das correções da rodada 2

| Item rodada 2 | Status v3 | Verificação |
|---|---|---|
| **MAJOR-1** (fundação de K: compreensão não é universal) | **PARCIAL** | A troca por funções PV `G`,`H` + correção como sentença universal verdadeira (§1.0 L18–27) é **a rota certa e legítima** (ver §B). Mas o **passo 2** herda o mesmo defeito: sua sentença não é universal (§C). |
| **MAJOR-2** (J.0′ retraiado) | **RESOLVIDO** | Retração com verbatim L21–22 ✓; Condição J.4 → aberta ✓; §0.3 (L28–30), §2(ii), dicotomia (L94–97), §4 (L158–159), §6 (L193–194) ajustados ✓. Nenhuma consequência esquecida: §0.2 já é "(Hjoint) ⟹ C.3"; §4 registra a recíproca como não-reivindicada; §5 nº 3/4 continuam corretos como certificados (A). *Nota de coerência (MENOR-4):* explicitar se a pergunta aberta "M_0 ⊨ ∃r ¬φ(r)" é com ou sem Condition 1. |
| **MAJOR-3** (quantificadores) | **RESOLVIDO** | J.6 (L155–159) agora quantifica "subfamília **interna**-mente finita" ✓ unificado com (Hjoint); "≡" virou "**(Hjoint) ⟹ C.3**, recíproca não reivindicada" (L161–163) ✓; a leitura de `τ_N` está marcada como **ponto de referee** (L87–91) + checklist nº 11 ✓ — tratamento correto (as duas leituras de H1 §1.1 realmente diferem; a correspondência fica aberta e registrada). |
| MENOR-1 (§0.3 "a semente") | RESOLVIDO | §0.3 fala só de `¬φ` ✓. |
| MENOR-2 ("mais forte que Cook–Thapen") | RESOLVIDO-PARCIAL | K.2 (L138–141) agora: "coerente com, **não idêntica** à, razão do artigo (perda de universalidade do KPT)" ✓. §4 (L164–166) mantém "mais forte", mas agora **qualificado** ("K sem hipótese de fatoração; CT restringe só a provabilidade de BB") — aceitável. |
| MENOR-3 (citações §5) | RESOLVIDO | §5 nº 2/3/5/6 corretos; **exceto** nº 7, que ainda afirma composicionalidade como "sentença universal" — corrigir junto com o passo 2 (MAJOR-R3). |
| MENOR-4/5 (dicotomia ⊣ J.0′; §6 condicional) | RESOLVIDOS | L94–97 e L193–194 ✓. |

## §B. Teorema K, passo 0 (correção de `G`/`H`) — **SÓLIDO**

A prensificação é legítima e a rota é a do artigo (§1.0: `T_PV` = toda sentença universal
verdadeira; L21–22: soundness de pps "expressible by a universal `L_PV`-formula"):
escreve-se a correção de `G`,`H` como sentença **universal** (matriz quantifier-free com
símbolos PV: `G(F,α)_p`, `i=H(F,α,p)`, `i<m`, `p∈at(α_i)`, `(F(i))_p`), ela é **verdadeira
em ℕ** (definição dos programas), logo ∈ `T_PV`, logo **vale em `M_0` para os próprios
símbolos `G`,`H` mesmo com entradas não-padrões** — exatamente o escape que a compreensão
não tinha. O bicondicional com `i = H(...)` **faz o que precisa**: se existe testemunho,
`H` devolve uma (menor) ⟹ lado direito verdadeiro ⟹ `(G)_p=1`; se não existe, o lado
direito é falso para **todo** `i` ⟹ `(G)_p=0`. ✓

**MENOR-1 (L110–112):** a sentença tem `m` **livre** (não quantificado; aparece em `i<m`)
e quantifica `j` **sem uso**; e `at(α_i)` deve ser declarado predicado PV. Correção:
`m := m(α)` (função PV que lê o comprimento do código), remover `j`, nomear `A(α,i,p)`.

**MENOR-2 (L112):** `H` precisa ser **total** e devolver testemunho quando um existe
("menor testemunho" é indefinido quando não existe — qualquer valor serve, a bicondicional
continua correta). Especificar em uma linha.

## §C. Teorema K, passo 2 — **MAJOR-R3** (o único defeito novo)

A sentença `∀α,σ* [(∀i<m Fals(σ*,(α)_i)) → Fals(σ*,α)]` (L124–125) tem **dois** defeitos:

1. **Falsa para códigos malformados.** Para `α` que não é um big-or de `m` blocos,
   `D(α,i)` lê lixo e a implicação falha (ex.: `α = ¬β` com `(α)_i` projetado arbitrário).
   Como só sentenças **verdadeiras** entram em `T_PV`, ela não é axioma. **Correção:**
   predicado de **shape** `S(α,m)` ("código de `⋁_{i<m} β_i`", p-time) — e `M_0 ⊨ S(α,m)`
   é **de graça**: é o conteúdo do axioma **(S2)**.
2. **Não é universal.** `∀i<m` no antecedente não prensifica para fora: a negação é
   `∃α,σ*[S ∧ ∀i<m ¬… ∨ ¬ψ]` — Σ_2; Π_2 não colapsa a Π_1 (não-absolvição do limite
   aritmético limitado). A alegação "universal ⟹ ∈ T_PV" falha.

**Reparo local (mesmo padrão do passo 0):** introduzir `W(α,σ)` = big-or p-tempo de
`ev((α)_i,σ)` para `i<m(α)` e localizador `Winv` (menor `i` com valor 1, senão `m(α)`);
as sentenças **universais verdadeiras** são:
(i) `S(α,m(α)) → (ev(α,σ) = W(α,σ))`;
(ii) `i<m(α) ∧ ev((α)_i,σ)=1 → W(α,σ)=1`; (iii) `W(α,σ)=1 → (Winv(α,σ)<m(α) ∧ ev((α)_{Winv(α,σ)},σ)=1)`;
(iv) `W(α,σ) ∈ {0,1}`. Em `M_0`: de `∀i<m ev((α)_i,σ*)=0`, instancia `i:=Winv(α,σ*)`,
divide por `Winv<m` e conclui `W=0` ⟹ `ev(α,σ*)=0` (por (i)) — tudo lógica de 1ª ordem
sobre axiomas. **Tese de K não muda; só a sentença do passo 2.**

## §D. Passos 1 e 3; J.5-sound — OK

* **Passo 1 (localidade):** a sentença "σ,τ concordam em `at(β)` ⟹ `Fals(q,β)↔Fals(q',β)`"
  é universal verdadeira ✓; a dedução `σ*↾at(α_i) = F(i)↾at(α_i)` usa a correção de `G`
  nos **dois** sentidos + `(S2)` (colisão `p∈at(α_h)∩at(α_i)` com `h≠i` é proibida) ✓ —
  correto e sem apelo a padrão. Bits de `F(i)` fora de `at(α_i)`: de fato inócuos ✓.
* **Passo 3:** `Ref_P ∈ T_PV` rota (α) + `(S3)` ⟹ `M_0 ⊨ ∀σ ev(α,σ)=1`; com `Fals(σ*,α)`,
  contradição ✓. A remoção da indução `Δ_0` (A.5(β)) está registrada e correta ✓.
* **J.5-sound (L59–62):** correta — `Ref_EF`/`Ref_P` são sentenças universais verdadeiras
  (matriz quantifier-free via `ev`) ⟹ ∈ `T_PV` ⟹ valem para dados não-padrões ✓.
  **MENOR-3:** J.5-sound só trata fórmula **única**; J′ (L73) usa a versão de **lista**
  (`Ref_EF(d*, premissas, ⊥)`). Reduzir por **conjunção**: premissas padrão ⟹ `⋀Γ` padrão
  (J.0(a)) ⟹ instância de fórmula única ✓. Uma linha.

## §E. K.2 e J.2′

* **K.2:** escopo **honesto** ✓ — "coerente com, não idêntica à, razão do artigo (perda
  de universalidade do KPT)"; aplicação de BB legítima (matriz aberta `Δ^b_0`, `i`
  sharply bounded, L442) — reconfirmo. Nada reivindicado demais no §3; em §4 a comparação
  com Cook–Thapen está agora qualificada (aceitável).
* **J.2′:** **ainda correto** (idêntica à v2, que foi validada): descompasso de tamanhos
  `(r)_i` padrão vs `(α)_i` não-padrão; ramo `(α)_i` padrão via soundness real + `(S4)` +
  absolutidade (com os suportes já anotados na rodada 2: restrição a posições padrão é
  padrão por `∀x(|x|≤k → ⋁x=numeral)` ∈ `T_PV`). ✓

## §F. MENORES e ESTILO

1. MENOR-1: `m` livre / `j` sem uso / `at` não declarado (§B).
2. MENOR-2: totalidade e especificação de `H` (§B).
3. MENOR-3: J.5-sound vs lista de premissas em J′ (§D).
4. MENOR-4: §0 (L14) × §2(ii): dizer se a pergunta aberta "M_0 ⊨ ∃r ¬φ(r)" carrega
   Condition 1 como hipótese (hoje ambíguo).
5. ESTILO: L39 "contraexembro" → "contraexemplo"; §5 nº 7 (composicionalidade "universal")
   e nº 10 ficam a atualizar após o reparo do passo 2.

## §G. Exigência única para RECOMENDADO

Reescrever o **passo 2** do Teorema K conforme §C (shape `S(α,m)` = conteúdo de (S2) +
`W`/`Winv` + as quatro sentenças universais), ajustar §5 nº 7, e aplicar os MENOR-1..4.
Nada mais: **a tese de K, K.2, J.2′, J′-condicional e a retratação de J.0′ estão firmes**,
e a v3 é a versão mais honesta da frente até agora.

---
---

# Rodada 4 — v3b

> **Rodada 4 — verificação final (relatório completo)** (esqueleto pré-leitura gravado
> antes da leitura, conforme procedimento; rodadas 1–3 preservadas acima). Alvo:
> `J1_Qcompactness_M0.md` v3b (276 L).

## VEREDITO v3b: **RECOMENDADO** — condicionado a 2 micro-correções obrigatórias (meia linha cada)

O MAJOR-R3 da rodada 3 (passo 2 de K) está **RESOLVIDO**: `S(α,m)`, `Winv`/`Widx` PV
totais, quatro sentenças universais, dedução em `M_0` correta. Nenhum FATAL, nenhum
MAJOR. Restam dois deslizes localíssimos (guarda de `m`; axioma que garante o shape) e
notas cosméticas — nenhum toca a verdade do Teorema K nem a dedução.

## §A. Passo 2 de K reescrito — **RESOLVIDO** (com 2 deslizes)

1. **`S(α,m)`**: predicado de shape p-time ✓; a dedução só precisa de `M_0 ⊨ S(α,m)`,
   que existe — **mas o texto o atribui a `(S4)`/`(S1)` (L132), errado: é `(S2)`**
   ("`α` é disjunção disjunta `⋁̇_{i<m} α_i`", `A` §1.2; `(S4)` é `∀i<m(¬α_i)∈SAT`, `(S1)`
   = `T_PV`, nenhum dos dois fala do shape). **Micro-correção obrigatória nº 1:**
   `(S4)`/`(S1)` → **`(S2)`**.
2. **`Winv`/`Widx`**: PV e **totais** ✓ (laço `i<m`, `m ≤ |α|` ⟹ p-tempo; "senão `m`"
   torna `Widx` total ✓). Notação: `Winv(α,σ*,i) = Eval((α)_i,σ*)` — mesmo símbolo de
   avaliação de J.5-sound ✓ consistente.
3. **Verdade das (i)–(iv):** (i)–(iii) TRUEs ✓ (guardadas por `S`; `Widx` é de fato o
   menor testemunho). **(iv) é verdadeira para o shape `S`** ✓: sob `S(α,m)`, `α` é o
   big-or **literal** dos blocos; `Widx = m` ⟺ nenhum bloco avalia 1 (definição de
   `Widx`), e o OR de disjunctos todos 0 avalia 0 — correção de avaliação real de
   circuito bem-formado. **Universalidade:** as quatro têm matriz quantifier-free
   (símbolos PV + guardas) e **nenhum `∀i<m` no antecedente** — o localizador faz
   exatamente o serviço exigido (L142–143) ✓ MAJOR-R3(ii) fechado.
4. **Dedução em `M_0` (L145–147): correta, sem lacuna.** `M_0 ⊨ ∀i<m Winv(...)=0`
   (§1 + identidade `Fals = Eval=0`); se `Widx<m`, (ii) dá `Winv(...,Widx)=1` e a
   **instância em `i = Widx`** da hipótese dá 0 — contradição ✓ (instanciação legítima:
   `Widx<m` é exatamente a guarda); logo, com (i) (`Widx ≤ m`) e a linearidade de `≤`
   (axiomas de ordem, sentenças universais verdadeiras ∈ `T_PV` ✓), **`Widx = m`** — o
   passo "contradiz ⟹ `Widx = m`" é válido por trichotomia da ordem, **não há lacuna**;
   (iv) conclui `Eval(α,σ*)=0` ✓. (iii) (minimalidade) é correta mas **não usada** —
   mantê-la ou cortá-la, indiferente.
5. **DESLIZE (MENOR-obrigatório nº 1): `m` continua mal amarrado.** As cinco sentenças
   (correção de `G`/`H` L116 e (i)–(iv)) quantificam/livram `m` **sem guarda**. Para
   (i)–(iv) isso é inofensivo (o antecedente `S(α,m)` as torna verdadeiras por
   vacuidade quando `m ≠ m(α)`, pois `Widx`/`Winv` usam `m(α)` internamente). **Mas a
   sentença de correção de `G`/`H` com `∀m` LIVRE é FALSA**: com `m < m(α)` e testemunho
   só em índice `j ∈ [m,m(α))`, `H(F,α,p,m)` devolve "não achado" (`≥ m`) ⟹ lado direito
   falso, enquanto `(G(F,α))_p = 1` (`G` usa `m(α)`) — bicondicional falha ⟹ a alegação
   "esta sentença é verdadeira" (L118) é falsa como escrita. **Micro-correção obrigatória
   nº 2:** acrescentar a guarda `m = m(α)` (ou substituir o termo `m(α)`) em L116 — com
   isso a sentença volta a ser verdadeira e universal, e a prova de K fecha como está.

## §B. MENORES da rodada 3 — status

| MENOR rodada 3 | Status v3b | Verificação |
|---|---|---|
| `m` livre / `j` sem uso / `at` não declarada | **PARCIAL** | `j` removido ✓; `at` declarada p-tempo (L112–113) ✓; `m` "ligado" por `∀m` **sem guarda** ⟹ sentença de correção falsa para `m ≠ m(α)` (§A.5). |
| Totalidade de `H` | **RESOLVIDO** | L111–112 (`O(m·|α|)`, `|α| ≥ m`) + convenção "senão `m`" (L121–122) ✓. |
| J.5-sound via **conjunção** para listas | **RESOLVIDO** | L63–64: `ψ = ψ_1∧…∧ψ_k` padrão por J.0(a) ✓; "v satisfaz as premissas" ⟺ `v ⊨ ⋀ψ_j` ✓. |
| Condition 1 coerente (§2(ii)/§0) | **RESOLVIDO** | L82–86: pergunta aberta feita **com** Condition 1 como hipótese ✓; §0 L14 coerente ✓. |
| Typo "contraexembro" | **RESOLVIDO** | L39 ✓. |

## §C. Regressão §§0–6 e §7

* **§5 nº 7** (composicionalidade "sentença universal") está agora **correto** ✓ (é (iv));
  nº 10, nº 11 ok. **Nota:** nº 6 ainda lista só `G`,`H` — acrescentar `Widx`/`Winv`
  (cosmético). **§0–§4, §6:** nenhuma inconsistência com o passo 2 novo ✓ (K continua
  "incondicional"; J.5 decidida negativa; J′ condicionada; J.6 governa C.3) ✓.
* **§7 registra a rodada 3 corretamente** ✓ (L254–264: MAJOR-R3 com as duas facetas —
  falsidade para α malformado e Π_2 — mais os MENORES; "0 FATAL, 1 MAIOR" fiel) ✓.

## §D. Condições para publicação (ordem de ataque: nenhuma)

1. Guarda `m = m(α)` na sentença de correção de `G`/`H` (L116).
2. `(S4)`/`(S1)` → `(S2)` na garantia de `S(α,m)` (L132).
3. Opcional: §5 nº 6 com `Widx`/`Winv`; cortar ou marcar (iii) como não-usada.

**Fecho das quatro rodadas:** a tese de **K** ("nenhuma coleção interna para os
falsificadores de `(S4)`"; corolário: `T_PV+BB` inconsistente com a semente, coerente com
a remark de L442) está **firme**; **K.2** com escopo honesto; **J.2′** correta;
**J′** condicionada a (Hjoint) e honesta; a completude interna permanece **retraída**
(com o verbatim L21–22). As pendências remanescentes são **abertas e declaradas**
((Hjoint)/J.6; correspondência das duas leituras de `τ_N`) — é o trabalho futuro, não
defeito desta versão.

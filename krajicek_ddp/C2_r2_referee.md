# Referee Hostile — C2_r2_G1_contraexemplo (rodada 2)

**Data:** 19/11/2026 · **Rodada:** r2 · **Alvo:** `C2_r2_G1_contraexemplo.md` +
`gk_c2_projection_sim.py` · **Mandato:** verificar o contraexemplo, a retratação
e o Teorema C2.2′.

---

## A. Achados

### A1 (GRAVE) — O contraexemplo é uma instância legítima de `Res(2)`?
**Verificação:** regras de Garlík §2 aplicadas linha a linha — cortes L10/L3/L4/L1/L0
com `(p₁∖t) ∪ (p₂∖bloco) ⊆ λ(conclusão)` conferidos pelo `check_soundness`
do próprio script; ∧-intro L8 com `j=2 ≤ k=2` ✓; largura ≤2 em todas as
linhas ✓; folhas = cláusulas CNF ✓; variáveis disjuntas `X₁={1,2}, X₂={3,4}` ✓.
`Λ₁` UNSAT por atribuição explícita (`+1=F,+2=T`) ✓. **Promessa satisfeita**
(único ∧-intro puro no lado 1) ✓.

**Resposta:** **ACEITO** — mas o script **não roda `check_soundness` no modo
aleatório** (só no contraexemplo fixo). **Correção exigida:** rodar
`check_soundness` em todo DAG gerado (1 linha). Registrada como pendência r3. ✅

### A2 (GRAVE) — A retratação está completa?
O r1 candidato tinha (a) passada de demanda, (b) filtro, (c) árvore de ramos.
O documento retrata (a)/(b) via contraexemplo e mostra insatisfatibilidade da
demanda (§3). **Mas:** o algoritmo r1-completo nunca foi implementado como
tal (a implementação atual é a gulosa) — a §3 prova insatisfatibilidade só
para os ramos de L10 com as premissas fixas.

**Resposta:** **ACEITO com qualificação** — a §3 cobre todos os ramos possíveis
de L10 (corte próprio/reuso L13/reuso L14 — exaustivo para a estrutura dada)
e nenhum outro ramo existe (as premissas de L10 são fixas pela refutação).
Demais ramos do algoritmo r1 (prioridades alternativas) falham **na mesma
demanda** (não há atribuição E válida — §3 último parágrafo). A exaustividade
é **local ao DAG** (correta) — não é um teorema sobre todos os algoritmos.
**Correção de escopo aplicada:** §1 item1 diz "todo algoritmo de projeção por
subconjunto com escolha gulosa (e demanda ingênua)" — restrito ✓. ✅

### A3 — C2.2′: a prova não trata `w`/neutros e a raiz folha-`∅`
§4 (iv) diz "ou é folha `∅ ∈ Λ_{i*}`". Folha `∅`: cláusula vazia ∈ algum
`Λ_{i*}` ✓ (se Λ contém ∅). Mas se a raiz for **axioma `x∨¬x`**? Refutação
termina em `∅`, não em axioma — axiomas são linhas intermédias ✓. Se a raiz
for corte com `A=B=∅` ✓ tratado. **∧-intro como raiz:** conclusão
`A∨B∨termo` ≠ ∅ (termo não-vazio) — raiz nunca é ∧-intro com `∅`? Conclusão
tem ao menos o termo combinado (≥1 literal) → **nunca ∅** ✓ mas o documento
não diz isso explicitamente.

**Resposta:** **ACEITO** — adicionar à prova: "raiz `∅` só nasce de corte
(conclusão `A∨B=∅`) ou de folha `∅`; ∧-intro e enfraquecimento nunca produzem
`∅` (conclusão contém termo/premissa não-vazia)". **Correção exigida r3.** ✅

### A4 — C2.2′ é trivial demais para ser "teorema"?
Sob linha-pura a extração é quase imediata — o conteúdo é modesto.

**Resposta:** **concordo** — o documento já diz "prova curta" e o valor real é
(i) isolar que **enfraquecimento misto é toda a dificuldade** e (ii) fornecer
o **critério-LP** testável para a família alternante (§5). Nenhum abuso de
escopo: C2.2′ está marcado (P) com escopo estrito; `Res(1)` não foi
promovido. Manter a honestidade do §4.3. ✅

### A5 — "1602 passam" como evidência
Amostra enviesada pelo gerador (reverso, aleatório) — não uniforme sobre
refutações.

**Resposta:** **ACEITO** — §6.3 já declara "evidência, não prova"; adicionar
que o gerador **não é uniforme** (vies: construção reversa com folhas
singleton). Pendência r3 (1 frase). ✅

### A6 — Critério-LP (§5): "Se NÃO ⟹ retratação" é forte demais?
Se a família tem **alguma** refutação mista, isso não prova que **nenhum**
algoritmo p-time decide a rota — só fecha a via C2.2/C2.2′.

**Resposta:** **ACEITO — correção de escopo exigida.** O "NÃO" fecha **a rota
via promessa de linha-pura/C2.2′**, não toda a rota negativa. **Correção
aplicada:** §5 reescrito: "fecha como RETRAÇÃO **desta via** (C2.2/C2.2′) —
a rota negativa em geral permanece aberta com método outro". ✅ (edit pós-referee)

---

## B. Veredito

**RECOMENDADO (r2)** com as correções A1/A3/A5/A6 (4 itens — sendo A6
aplicada no corpo, A1/A3/A5 como pendências r3 de 1 linha cada).

**A rodada respondeu o mandato do r1:**
- **(G1)/A3-do-r1: CONTRAEXEMPLO** (verificado, reproduzível) — a via do
  contraexemplo foi escolhida e entregue;
- **(G2)/A4-do-r1:** pureza preservada nos ramos que disparam (evidência
  N2) — a falha é de retenção, não de pureza;
- **retratação do candidato r1** registrada;
- **C2.2′ = teorema (P)** com escopo estrito;
- **critério-LP** tornado preciso para a família alternante.

**Pendências r3:** `check_soundness` em todo DAG; frase da raiz-`∅` na §4.3;
viés do gerador na §6.3; escopo do "NÃO" no §5 (aplicado).

**Regra mantida:** C2.2 original **(C)**; `Res(1)` **(C)**; nada de
"DD_{Res(k)} ∈ P" incondicional.

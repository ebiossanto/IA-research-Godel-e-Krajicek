# Relatório do ataque — versão finita/combinatória do Problema 2.1

**Data:** 11 Out 2026 · **Fonte:** arXiv:2506.20221v4 (Krajíček, *On NP∩coNP proof complexity
generators*) · **Frentes:** F1 (verificação do passo frágil), F2 (lema de suficiência finita),
F3 (ataque construtivo). Documentos: `F_CONTEXTO_ATAQUE.md`, `F1_verificacao_passo7.md`,
`F2_versao_finita.md`, `F3_ataque_construtivo.md`.

---

## Resultado central (o que esta rodada establisheceu)

**1. A hipótese do Teorema 4 pode ser drasticamente enfraquecida — dispensando `M*`,
`Log` e todo o esquema `Σ^b_1`. (F2, teorema provado.)**

> **Teorema (lema de suficiência finita).** (ST) + `P` strong e p-bounded + **(F-sent)**
> para todo `M` modelando `S` ⟹ `NP ≠ coNP`,
> onde **(F-sent)**: existe `M' ⊇ M` com `M' ⊨ T_PV`, `M' ⊨ (¬φ) ∈ SAT` e
> `M' ⊨ ∀i<m (¬α_i) ∈ SAT`.

A prova reproduz os itens (1)–(4) da prova original do artigo e reescreve o item (5) assim:
o falsificador `σ ∈ M'` de `φ` entrega `i_0 < m` com `M' ⊨ σ_{i_0}:P ⊢ α_{i_0}`; (F-sent)
instancia em `i_0` dando `M' ⊨ (¬α_{i_0}) ∈ SAT`; `Ref_P` (universal verdadeira, logo em
`T_PV`, logo válida em `M'` com parâmetros de `M'`) contradiz. **Nenhum `M*`, nenhuma
igualdade de `Log`, nenhuma preservação `Σ^b_1` é usada.** Toda a máquina intermediária
do artigo existe só para transportar a sentença (8) de `M` até `M'` no índice `i_0` —
e a versão finita dispensa o transporte ao exigir (8) diretamente em `M'`.

**2. A versão membership (F-b') é equivalente em força para o uso e é mais natural: (F-b') ⟹ (F-sent).** (F2, prova.) Se `M' ∩ m = M ∩ m` então todo `i < m` de `M'` é antigo;
`M ⊨ (8)` instancia nele e as testemunhas sobem para `M'` por `Σ^b_1` para cima. Além
disso, (F-b') é **finita** no sentido pedido pelo usuário original: a condição (iii)
`Log(M*) = Log(M')` é substituível pela pertinência de uma **lista finita de parâmetros**
`{π, α, m, i_0, α_{i_0}}` — **sem** o falsificador `σ`, que é **refutado por colapso**
se exigido em `M*` (se `σ ∈ M*`, `i_0` entra por fechamento PV e a contradição explode
cedo demais; `σ` tem de morar em `M'` pois testemunha `¬φ ∈ SAT`).

**3. O passo "But by (7) i_o is also already in M*" do artigo é uma lacuna em v4. (F1, veredito.)**
`Log(M) = {|m| | m ∈ M}` é o conjunto dos **comprimentos** padrono; um elemento novo
`j < m` tem `|j| ≤ |m|`, medida já presente, então a igualdade `Log(M*) = Log(M')`
**sobrevive** à adição de `j` — ou seja, é insensível a elementos novos abaixo de `m`,
que é exatamente onde mora `i_0`. Os três reparos tentados e refutados: (a) `i_0` como
menor índice (p-tempo definível de `σ`, que está em `M'`, logo não ajuda); (b) p-boundedness
(dá medida velha para a prova, não membership; e a rota "prova mais curta ∈ `M*`" colapsa
por consistência de `M*` — p-time com clock não é absoluto entre subestruturas para
parâmetros não-padrão); (c) `σ ∈ M*` (refutado por colapso). Releitura do HTML de v4
confirmou: `Log` ocorre 3× no paper, nenhuma nota amplia a definição. **Correção mínima:**
trocar (7) por "`M' ∩ m = M ∩ m`" (= F-b') ou exigir (8) diretamente em `M'` (= F-sent).

**4. (F-b') e (F-sent) permanecem ABERTAS — este é o novo problema central. (F3.)**
O ataque construtivo por compactness/Henkin deliniou o obstáculo exato:
- o diagrama `Σ^b_1` **positivo** de `M` é seguro (sobe); a parte negativa não transfere;
- universais com parâmetros de `M` podem ser falsificados por elementos novos — é por isso
  que [7, Thm 9.4.2] usa forcing (é o preço de `M' ⊨ T_PV`);
- o cerne PV: fechar `M ∪ {σ}` sob funções PV pode produzir elementos novos abaixo de `m`
  (funções redutoras: `|x|`, `⊖`, decodificação `(σ)_i`); o "lema de evitamento" (`|σ_i| ≥ m`)
  foi **parcialmente refutado** — mas a liberdade de escolher `σ` entre muitos falsificadores
  de `φ` pode dar folga;
- em (F-sent), semear uma lista `z` de testemunhas é `Σ^b_1` (sobe), mas cobre índices que
  só existirão em `M'` — circularidade; e o esquema **BB** reaparece como coleta para `m`
  não-padrão. Obstáculos catalogados O1–O8.

---

## O que isso muda no panorama

| | Problema 2.1 (artigo) | Versão finita (esta rodada) |
|---|---|---|
| Exigências | esquema `Σ^b_1` **todo** + `Log(M*)=Log(M')` + `M*` intermediário | **uma** sentença `(8)` em `M'` (ou `M' ∩ m = M ∩ m`) |
| Natureza | infinita (igualdade global de estruturas) | **finita** (sentenças com parâmetros `π, α, m, φ` em `M`) |
| Passo de saída | frágil ("by (7) i_0 ∈ M*" — lacuna) | direto (instanciação + `Ref_P`) |
| Status | assumido no artigo, com lacuna em v4 | **aberto, mas formulado finitamente** |

A versão finita é **o que o artigo precisa** e é atacável por combinatoria/teoria de
modelos clássica, em contraste com a versão original, cuja hipótese é "forte mas com
entrega frágil".

---

## Próximo passo concreto (ordem recomendada)

1. **Obter a descrição das condições de forcing de [7, Thm 9.4.2]** (Krajíček 1995, Cap. 4
   e 9.4.2 — ou [10] Cap. 20): elas são "medida a medida"? aceitam **semente** de elementos
   novos de medida velha? Isso decide se (F-b') é construível.
2. **Testar (F-b')** nessa construção: se o forcing semeado com um falsificador `σ` mantém
   `M' ∩ m = M ∩ m`, o Teorema 4 fica corrigido e a hipótese finita é provada.
3. **Se falhar, cair para (F-sent)** com cobertura de índices novos (colmar O1–O8 do F3),
   ou estudar se a liberdade de escolher `σ` (muitos falsificadores) permite o lema de
   evitamento de elementos pequenos.
4. **Comunicação ao autor**: F1 §5 traz um rascunho de nota editorial respeitosa apontando
   o passo exato, a conta concreta e as duas correções possíveis (F-b' ou F-sent) — a
   verificar se há argumento oculto em [7] antes de enviar.

**Marcação de status:** tudo nesta rodada é **(P)** (demonstração própria da equipe) ou
**(C)** (conjectura), exceto as transcrições **(A)** do artigo. O lema de suficiência finita
(F2) é um **teorema** — dependente apenas de (F-sent), cuja verdade é o novo ponto aberto.

# PEQUALNP_MAPA — IDs relevantes de pequalnp.com classificados (A)/(C) pelo protocolo do projeto

**Data:** 26/11/2026 · **Companheiro:** `MAPEAMENTO_DDP_vs_PEqualNP.md` (+ `_referee.md`, r1)
**Propósito:** mapa de referência rápida dos lemas do fleet pequalnp que tocam os eixos do
repositório (complexidade de provas DD_P/minref, lower bounds de circuito, meta-complexidade),
**cada afirmação classificada segundo a taxonomia do AGENTS §2**.

---

## 0. Fontes (snapshots imutáveis — sha256, regeneração)

| Fonte | sha256 / identificação | Uso |
|---|---|---|
| `pequalnp/plan.json` | `1B751ECE178C985…` (`updated_at 2026-11-24T20:32:00Z`) | targets, chains, hard_links + status |
| `pequalnp/overview.json` | `2EA0AD8CE252…` | linhas de ataque e suas rows |
| `pequalnp/papers.json` | `A2E9F3F7DDED…` | claims do Note 1 (status `checked`) |
| clone `pequalnp/pequalnp-proofs@89a01cd` (Apache-2.0) | commit `89a01cdee376a95ca23acd8cdf2e68f2bc493983` | provas Lean correspondentes |
| páginas `/papers/note-1`, `/live` (24–26/11/2026) | run-IDs citados abaixo vêm do Note 1 | enunciados e runs |

**Regenerar as tabelas brutas:** `python pequalnp/extract_ids.py [prefixos…]` (emite markdown
a partir dos 3 JSONs; rows ausentes do registro aparecem com `where = attack/rows`).

## 1. Notação (decisão **(P)** sobre a taxonomia (A)/(P)/(C) do AGENTS §2)

| Marca | Significado | Obrigação |
|---|---|---|
| **(A)** | resultado já estabelecido na literatura; **fonte primária nomeada** no registro deles | citar a fonte original (confirmar artigo exato antes de citar) |
| **(A)-nc** | **extensão nossa (P)**: resultado *externo*, verificado no checker deles (`Lean 4.36 + Mathlib pinados`), **sem peer review**; ou registro negativo (refutação) deles | citação obrigatória `pequalnp ID + commit 89a01cd + data`; **NUNCA** citar como teorema da literatura nem como resultado nosso |
| **(C)** | conjectura/alvo aberto (`conjecture`/`in_work`/`OPEN`) | exige teste empírico ou formalização antes de qualquer uso |
| — | registro sem status individual neste snapshot | **não usar como premissa** sem consultar o ledger do site |

> ⚠️ **Honestidade de escopo:** "checked" = aceito pelo checker deles. O próprio site afirma que a
> prosa "has not been read by a human mathematician". Resultados marcados *"(open in refereed
> work)"* são **novidade alegada por eles** — classificados (A)-nc, jamais (A).

---

## 2. TABELA 1 — Complexidade de provas (eixo do `krajicek_ddp/` e do `gk_minref`)

### 2a. Cadeia Res(+) / PC-F2 (programa Proof complexity) — 20 rows, todas `checked`

| ID | Enunciado (fonte: plan.json) | Status | Class. |
|---|---|---|---|
| `L-pcx-017` | TARGET: refutações Res(+) da fórmula de pombal (PHP) não são polinomialmente limitadas | checked | **(A)-nc** — *open in refereed work* |
| `L-pcx-022` | TARGET: idem para o **bit-PHP** (pombal de bits) | checked | **(A)-nc** — *open in refereed work* |
| `L-pcx-048` | TARGET: alguns 3-CNFs-insatisfatíveis sem refutações dag-like Res(+) polinomialmente limitadas | checked | **(A)-nc** |
| `L-pcx-054` | TARGET: Res sobre ≤k equações de paridade (termwise weakening) não é polinom. limitado em pombal funcional, todo k | checked | **(A)-nc** |
| `L-pcx-027` | HARD LINK: pombal funcional sem refutação PC/F2 de grau B quando furos ≥ 2B−1 | checked | **(A)-nc** |
| `L-pcx-036` | refutações dag-like Res(+) de bit-PHP com > exp(n / (32768 log²n)) linhas | checked | **(A)-nc** |
| `L-pcx-041` | critério geral: tamanho de refutação Res(+) limita a dimensão de espaço separado de polinômios de baixo grau | checked | **(A)-nc** |
| `L-pcx-042` | grau→tamanho: CNF sem refutação PC/F2 grau D ⇒ Res(+) com exp(D²/(1024v)) linhas | checked | **(A)-nc** |
| `L-pcx-043` | existem expandores de fronteira bipartidos de grau limitado (n+1 pombos, n furos) | checked | **(A)-nc** |
| `L-pcx-044` | rank normalizado monótono: dim(V_k/Z)/N(k) não cresce com k | checked | **(A)-nc** |
| `L-pcx-045` | Res(+) fechado sob restrição: refutação de comprimento S ⇒ ≤ 2S no restrito | checked | **(A)-nc** |
| `L-pcx-046` | pombal em expandor de fronteira sem refutação PC/F2 grau D quando 2(D+1) ≤ expansão | checked | **(A)-nc** |
| `L-pcx-047` | re-tipagem: refutação Res(+) de PHP ⇒ PHP sobre qualquer grafo bipartido, ≤ 2× | checked | **(A)-nc** |
| `L-pcx-049` | pombal funcional em expandor grau d sem PC/F2 grau D quando dD ≤ expansão | checked | **(A)-nc** |
| `L-pcx-051` | Res(k,+) com enfraquecimento semântico trivial: largura ≤ k, m cláusulas ⇒ 2m+1 linhas | checked | **(A)-nc** |
| `L-pcx-052` | Res(1,+) = Res(+) (mesmos comprimentos) | checked | **(A)-nc** |
| `L-pcx-053` | baseline pombal fraco: Res(+) de PHP_m^N ≥ exp(D²/(256bm))/2 linhas sob expansão | checked | **(A)-nc** |
| `L-pcx-033` | cadeia C: refut Res(+) de bit-PHP ⇒ refut PC de baixo grau com blocos de extensão por linha | checked | **(A)-nc** |
| `L-pcx-034` | cadeia D: remover blocos de refut PC deixa consequência row-linear não-nula de bit-PHP | checked | **(A)-nc** |
| `L-pcx-038` | remoção de blocos: grau-D com blocos ⇒ peso f no fecho PC grau-k(D+1) | checked | **(A)-nc** |
| `L-pcx-071` | **HARD LINK aberto**: dag-like Res(+) não polinomialmente limitado em CNFs de largura e grau F2 constantes | **conjecture** | **(C)** |

### 2b. Biblioteca ligada (Res(lin)/cutting planes sobre bit-PHP) — todas `checked`

| ID | Enunciado | Status | Class. |
|---|---|---|---|
| `L-lib-090` | Beame–Whitmeyer: dags de retângulo para pombal de bits são superpolinomiais | checked | **(A)\*** (fonte: Beame–Whitmeyer; confirmar artigo exato) |
| `L-lib-105` | Beame–Whitmeyer: dags de triângulo para pombal de bits são superpolinomiais | checked | **(A)\*** |
| `L-lib-089` | refutações Res(lin) estreitas de coeficientes pequenos viram dags de retângulo pequenos | checked | **(A)-nc** |
| `L-lib-091` | bit-PHP exige refutações superpolinomiais restritas (linhas O(log n) eqs., coef. ≤ n) | checked | **(A)-nc** |
| `L-lib-102` | Res(lin) sobre inteiros: linhas n^Ω(1) eqs. em bit-PHP | checked | **(A)-nc** |
| `L-lib-103` | Res(lin) tree-like sobre inteiros superpolinomial em bit-PHP | checked | **(A)-nc** |
| `L-lib-106` | cutting planes ⇒ dags de triângulo sem mais nós, sob qualquer split | checked | **(A)-nc** |
| `L-lib-107` | cutting planes de bit-PHP superpolinomial em linhas | checked | **(A)-nc** |

### 2c. Registros negativos (paralelo operacional com nossos D1–D6)

| ID | O que morreu | Status | Class. |
|---|---|---|---|
| `L-alg-002` | candidato 1: saturação de resolução de largura-k decide 3-SAT | **refuted** | (A)-nc — **não usar como premissa** |
| `L-alg-003` | premissa: 3-CNFs-insat. têm refutações Res(lin) de tamanho polinomial | **refuted** | (A)-nc — idem |
| `L-alg-004` | HARD LINK: bit-PHP exige refutações dag-like Res(lin) superpolinomiais (inteiros) | **refuted** | (A)-nc — **bug de definição: 1 passo podia afirmar o próprio pombal** |
| `L-alg-005` | versão reescrita (regras sintáticas) do mesmo alvo | **retired** | (C) — sem rota de prova, programa estacionado |

> **Lição para nós (P):** `L-alg-004` morreu por uma **regra de inferência que podia conjeturar o
> teorema-alvo** — exatamente a classe de falha que o nosso verificador `gk_dd_cert.py` (recusa
> adulteração) e a detecção G1 de violação endereçam. Candidato a caso de teste do verificador.

---

## 3. TABELA 2 — Circuit lower bounds (L-clb)

| ID | Enunciado | Status | Class. | Conexão |
|---|---|---|---|---|
| `L-clb-036` | OPEN: SAT sem circuitos fan-in-2 de tamanho O(n^1.01) | **in_work** | **(C)** | correspondência Krajíček–Pudlák (algoritmo rápido ⇒ lower bound) — mesmo tronco do `krajicek_ddp/` |
| `L-clb-024` | olhar fresco: algoritmo de análise de circuito → lower bound | linha `stopped` | (C) — linha morta | mapear no nosso "graveyard" pessoal antes de reabrir |

---

## 4. TABELA 3 — Meta-complexidade (L-meta)

### 4a. Cadeia partial-MCSP / paridade (plane question)

| ID | Enunciado | Status | Class. |
|---|---|---|---|
| `L-meta-009` | **Murray–Williams**: NP-hardness de MCSP separa EXP de NP∩P/poly | checked | **(A)** (fonte: Murray–Williams; confirmar ano/artigo) |
| `L-meta-016` | TARGET: NP-hardness de **partial** MCSP separa EXP de NP∩P/poly | checked | **(A)-nc** |
| `L-meta-021` | partial MCSP ∈ NP | checked | **(A)-nc** |
| `L-meta-017`/`018`/`019`/`023`/`024` | zero-completion, hardwiring (≤1 portão), SIZE≡HasCircuitSize em slices, testemunha curta, família para bit-language | checked | **(A)-nc** (infra) |
| `L-meta-025` | paridade de n entradas exige ≥ 3(n−1) portões | checked | **(A)-nc** |
| `L-meta-026` | paridade de n entradas tem circuito com 4(n−1) portões | checked | **(A)-nc** |
| `L-meta-027`/`028`/`029`/`030` | soluções isoladas ≤ 2k·2^(m−m/2k); paridade não é OR de poucos CNFs largura-k; mapa q-local → núcleo da redução | checked | **(A)-nc** (redução paridade→partial MCSP) |

### 4b. Note 1 — função de aresta: **ground truth verificado** (para calibrar comprimento em `gk_F*`/D4′)

Fonte: `papers.json` (8 claims `checked`) + página `/papers/note-1` (10 statements, incl. `L-meta-107`
e `L-meta-112`). Run-IDs do checker, conforme a tabela §0 do Note 1:

| ID | Enunciado (resumo) | Tamanho exato / bound | Run | Class. |
|---|---|---|---|---|
| `L-meta-102` | caminho P_n | exato: n + ⌊n/2⌋ − 2 (n≥2) | run-011301 | **(A)-nc** |
| `L-meta-106` | ciclo C_n (n≥5) | exato: n + ⌈n/2⌉ − 1 | run-012105 | **(A)-nc** |
| `L-meta-104` | floresta (lower bound) | ≥ \|E\| + τ(G) − 1 | run-011343 | **(A)-nc** |
| `L-meta-105` | circuito-cobertura (upper) | ≤ \|E\| + \|T\| − 1 | run-011310 | **(A)-nc** |
| `L-meta-154` | idem sem portões NOT | ≤ \|E\| + \|T\| − 1 | run-013182 | **(A)-nc** |
| `L-meta-113` | remover NOT sem custo (ciclos ≥ 9, hubs ≥ 9) | — | run-014387 | **(A)-nc** |
| `L-meta-115` | lower bound sem NOT (ciclos ≥ 9, hubs ≥ 7) | — | run-012892 | **(A)-nc** |
| `L-meta-204` | threads longos (ciclos ≥ 7, hubs ≥ 7) | ≥ \|A\|+\|E\|+k−1 | run-013633 | **(A)-nc** |
| `L-meta-107` | lema do reader (s−3/s−4 sem "pair funnel") | — | run-011915 | **(A)-nc** |
| `L-meta-112` | 4-ciclo | exato: s ≥ 3 | run-011875 | **(A)-nc** |

> **Uso previsto (C):** famílias de comprimento **ótimo conhecido** para calibrar `gk_minref` e as
> métricas de comprimento do D4′ — **não** como estrutura de grafo (circuitos ≠ DAGs de refutação;
> ver referee R2 do mapeamento).

### 4c. Conjecturas principais (alvos abertos)

| ID | Conjectura | Status | Class. |
|---|---|---|---|
| `L-meta-1629` | funções de incidência ponto–reta de plano de ordem q precisam de circuitos AND/OR (fan-in 2) com gates lineares no nº de incidências | **conjecture** (target) | **(C)** |
| `L-meta-3754` | HARD LINK: em circuito least lift-fixed AND/OR sem 4-ciclo, todo AND gate está "abaixo de F" | **conjecture** | **(C)** — primeira rung: 12 casos, 2 checados, 10 conjecturas |
| `L-meta-1592`/`1593` | grafos grau máx. 3 sem ciclo curto exigem \|E\|+τ−1 portões (NOT permitido) | linha `stopped` | **(C)** — "o caso cúbico precisa de um passo novo num vértice de grau 3" |
| `L-meta-1407` + rows da linha `clean-ands` | some least circuito AND/OR sem 4-ciclo só tem AND gates limpos | linha `stopped` | **(C)** |

### 4d. Linhas de ataque (status da linha; status **individual das rows = pendente**, não usar como premissa)

| Linha (overview.json) | Status | Rows (IDs) | Class. das rows |
|---|---|---|---|
| `above-three-a-vertex` — >3 gates/vértice para grafo explícito AND/OR | live | L-meta-17164, 17154, 18006, 18163, 18153, 18135, 17746, 17964 | **(A)-nc†** |
| `not-gates-on-the-promise` — NOT contados (coroa ≥ 2N−1; compl. ≥ 2N, N≥3) | live | L-meta-17183, 17185, 17187, 17166 | **(A)-nc†** |
| `several-outputs-product` — produto matricial Booleano 2×n: plain é least (≥ 8n−5) | live | L-meta-17111, 17895, 17774 | **(A)-nc†** |
| `gates-removed-one-input-at-a-time` — fixar 1 input nomeado e contar portões | live | L-lib-361…368 | **(A)-nc†** |
| `candidate-family` — busca de família de grafos cara a representar | live | L-meta-17144, 17145, 17146, 17153 | **(A)-nc†** |
| `small-circuits-found` — circuitos pequenos p/ 3-coloreabilidade, Hamilton, majority | live | L-meta-17124, 18044, 18130, 17709, 8977, 18006 | **(A)-nc†** |
| `petersen` — tamanho exato da função aresta de Petersen com NOT | support | L-meta-651…1745 (13 rows) | **(A)-nc†** |
| `graph-form` / `degree-three` / `clean-ands` / `table-*` / `depth-probes` | **stopped** | (ver `extract_ids.py L-meta`) | (C) — linhas mortas; **registrar no nosso graveyard antes de reabrir** |

† = **status individual não está nestes snapshots** (vêm de `attack.rows`); verificar no ledger do
site (páginas `/lemma/…` ou feed) antes de qualquer uso como premissa.

---

## 5. TABELA 4 — Fundamentos formalizados por eles (referência rápida)

| ID | Enunciado | Status | Class. |
|---|---|---|---|
| `L-lib-031` | Cook–Levin: SAT NP-completo **nas definições do projeto deles** | checked | **(A)\*** — mapear definições antes de citar |
| `L-lib-032` | 3-SAT NP-completo | checked | **(A)\*** |
| `L-lib-019` | Ladner: P≠NP ⇒ linguagem NP nem em P nem NP-hard | checked | **(A)\*** |
| `L-lib-015` | existe linguagem NP-completa | checked | **(A)\*** |
| `L-lib-073` | máquinas→circuitos: DTIME(t) tem circuitos O((t+n)³) | checked | **(A)\*** (padrão clássico) |
| `L-lib-053` | NP ⊊ NEXP (hiararquia de tempo) | checked | **(A)\*** |

\* = fonte clássica, **confirmar referência exata** antes de citar; `L-lib-031` é sobre definições
prórias deles → exigente de mapeamento (ver mapeamento §6, ressalva de honestidade de escopo).

---

## 6. Conexões diretas com o nosso trabalho (status: propostas, **(C)**)

| Eixo nosso | Dois lados do mapa | Próximo passo proposto |
|---|---|---|
| `krajicek_ddp/` (DD, Res, refutação) | §2a/§2b: Res(+) bit-PHP `L-pcx-022` vs nosso `gk_minref`/`gk_dd_cert` | cross-check: nossas famílias k=2,w=5 contra o critério `L-pcx-041` (tamanho ⇒ dimensão) |
| `gk_minref` (comprimento mínimo exato) | §2c: refutação `L-alg-004` morta por regra "adivinhadora" | usar `L-alg-004` como caso de teste do verificador `gk_dd_cert.py` |
| D4′ / `gk_F*` (pontes prova↔fractal) | §4b: tamanhos exatos da função aresta | calibrar **comprimento** ótimo conhecido (não estrutura de grafo) |
| Meta-complexidade (eixo descartado `support/03`) | §4a: cadeia partial-MCSP `L-meta-009…030` | se reabilitar o eixo: seguir o padrão de formalização deles, citando (A)-nc |
| Disciplina de descartados (D1–D6) | §2c + §4d linhas `stopped` | montar nosso "graveyard" com causa de morte (modelo `/graveyard` deles) |

---

## 7. Varredura 27/11/2026 — deltas de status (ver `VARREDURA_2026-11-27.md`)

| Item | 26/11 (§0 desta página) | **27/11 (novo)** |
|---|---|---|
| `L-clb-036` (SAT sem circuitos n^1.01) | `in_work` | **`conjecture`** — "no seat on it today" (plan_novo) |
| Linha `proof-complexity` | `dormant` | **`support`** + rows **`L-pcx-203`, `L-pcx-204`** (restrição→linhas; sparse×complete PHP) |
| `L-pcx-205` (novo, fora do plano) | — | **anel de n switches ⇒ refutação ≤ `48n+1` linhas** (A-064) — candidato (A)-nc ao eixo minref |
| Linha `clean-ands` (`L-meta-1407`+rows, §4c) | `stopped` (conjectura aberta) | **MORTA**: `L-meta-25474` refuta a simplificação para todo grafo |
| Linha `candidate-family` (§4d) | `live` | **`first line`** — alvo de 201 portões na tabela 32×32 batido em 52 min |
| `small-circuits-found` (§4d) | `live` | `stopped` |
| Novos custos exatos | — | escada/chain (A-053/054), matching-complemento ≥2N **com NOT** (A-056), `2n−1`×`≤4` (A-052/A-060) — **modelo "one-a-side" (≠ Note 1 full-input)** |
| Papers | Note 1 | **inalterado** (sem Note 2) |
| **`L-gct-026` (alvo GCT: claim cúbico "unrefereed 2026")** | fonte anônima ("unrefereed 2026 reports") | ✅ **FONTE CONFIRMADA (27/11)**: registro público do lemma (`data/lemma/L-gct-026.d43713ec6215.json`) declara *"the manuscript of 24 September 2026 cited by arXiv:2610.40484"*; o HTML de **arXiv:2610.40484** (Sheshadri, 29/10/2026) cita literalmente **"OpenAI. A cubic lower bound… Preprint, 24 September 2026. github.com/openai/math/…/A-cubic-lower-bound-for-border-determinantal-complexity…"** ⇒ = **`openai/math` #108** (MathVet `full`, challenge `PermanentCubic`); constantes: pequalnp `c=5529600e, m≥1408` × Sheshadri `n³/(8.8·10⁶e), n≥1408` (constante dele pior; nota registrada). Evidências: `pequalnp/lemma_L-gct-026.json`, `openai_math/arxiv_2610.40484.html` |

*Nota de monitoramento:* monitorar `data.pequalnp.com/head.json` — troca de hash em
`files.papers` = novo paper; `plan_v2` (`ruled_out`) = cemitério vivo; `letters` = respostas
de especialistas (LT-003 sobre `|E\|+τ−1` já **replied**).

**Classificação desta página:** documento de referência **(P)** (nossa curadoria e notação);
todo conteúdo de afirmação é **(A)/(A)-nc/(C)** conforme coluna própria.
*Revisar sempre que os snapshots forem rebaixados (sha256 da §0 mudou ⇒ regenerar tabelas;
script: `pequalnp/_varredura_diff.py`).*

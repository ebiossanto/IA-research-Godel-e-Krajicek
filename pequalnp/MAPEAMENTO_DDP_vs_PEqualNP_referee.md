# REFEREE HOSTILE — `MAPEAMENTO_DDP_vs_PEqualNP.md` (rodada r1)

**Data:** 26/11/2026 · **Alvo:** `pequalnp/MAPEAMENTO_DDP_vs_PEqualNP.md` (decisão §4.4)
**Protocolo:** AGENTS §3, Passo 4 — nenhuma entrega concluída sem uma rodada de crítica implacável.
Cada item: **objeção → investigação → veredito → correção aplicada (ou pendência explícita).**

---

## R1 — Quantificador excessivo na decisão ("toda e qualquer noção de circuito")

**Objeção:** a §4.4 diz "toda e qualquer noção formal de circuito Booleano", mas o projeto tem um
layer Python (`gk_minref`, `gk_dd_cert`, `proof-fractal`) com convenções próprias e um eixo D4′
que trabalha com DAGs de refutação. O quantificador engole camadas que nunca usarão `FanInTwo`.
**Investigação:** `grep -i circuit lean4/` → 0 definições (R9); os scripts Python não falam Lean.
**Veredito: SUSTENTADA em parte.**
**Correção aplicada:** §4.4 condição 3 restringe o padrão a "(a) definições formais em Lean e
(b) convenções declaradas em textos"; scripts Python mantêm implementação própria com
correspondência documentada. O quantificador agora tem escopo explícito.

## R2 — Confusão entre DAG de refutação e circuito Booleano

**Objeção:** a §5.3(3) sugere "ground truth calibrado" das famílias do Note 1 para os experimentos
D4′ (fractal de refutações). Um circuito e um DAG de refutação são categorias diferentes: portões
*computam funções*; nós de refutação *derivam cláusulas*. Medir dimensão de um não é medir do outro.
**Veredito: SUSTENTADA.** Risco real de *overfitting conceitual* exatamente do tipo que a
ponte L2→L3 (`RELATORIO_CONSOLIDADO.md` §9.1) já é acusada de ter.
**Correção aplicada:** §4.4 condição 4 coloca DAGs de refutação e métricas fractais **fora do
escopo do padrão**; §5.3(3) reclassificado como **(C)** com a frase "famílias de tamanho exato
como calibração de *comprimento* (não de estrutura de grafo)".

## R3 — Licença e repositório embutido

**Objeção:** Apache-2.0 exige preservar avisos; e `pequalnp/pequalnp-proofs/` é um git embutido
que pode entrar por engano num `git add -A`.
**Investigação:** `LICENSE` = Apache 2.0 (verificado no clone); `git status` da raiz mostra apenas
`gk_series_b_series.csv` untracked antes desta sessão.
**Veredito: SUSTENTADA (operaçional).**
**Correção aplicada:** §0 registra commit + licença + aviso; decisão §4.4(2) exige cabeçalho de
atribuição com caminho e commit. **PENDÊNCIA DO AUTOR:** decidir `pequalnp/pequalnp-proofs/` em
`.gitignore` ou desmembrar antes de qualquer `git add` amplo.
**→ RESOLVIDO (mesma entrega):** `.gitignore` raiz, linha `pequalnp/pequalnp-proofs/`
(verificado `git check-ignore -v` → casa; artefatos do estudo seguem trackeáveis).

## R4 — "Vendorização sem Mathlib compila" — a afirmação mais arriscada

**Objeção:** afirmei que `GateOp/Gate/Circuit/wires/eval/size` e `FanInTwo/HasCircuitSize` não usam
Mathlib, mas os arquivos *deles* importam Mathlib no topo. Sem teste, isso era **(C)** disfarçada de **(A)**.
**Investigação (executada nesta sessão):** criado `pequalnp/_r4_test_circuitcore.lean`
(`import Init` puro, toolchain **v4.34.0** nossa):
- 1ª execução `lake env lean pequalnp\_r4_test_circuitcore.lean` → **ERRO: `Unknown identifier Set`**
  (confirmou: `Set` é do Mathlib; a forma literal deles não vendoriza limpa).
- Adaptado `FanInTwo` para **disjunção explícita**
  (`g.op = and ∨ g.op = or ∨ g.op = not`), equivalente lógico exato → **2ª execução: EXIT=0**
  (inclui `List.ofFn` em `HasCircuitSize` e teoremas `by decide` de sanidade NAND).
**Veredito: REFUTADA parcialmente; tese central CONFIRMADA com uma adaptação.**
**Correção aplicada:** §4.4(2) atualizado — vendorização viável **com a única adaptação
`Set`→disjunção explícita**, testada em v4.34.0. **(C) restante explícito:** `Circuit.depth`,
`SIZE`, `PPoly`, `MCSP` **não** entram no núcleo (usam `Language`/`Polynomial`/`ncard` — Mathlib
sim); e a forma *literal* deles (com `Set`) só é reproduzível com Mathlib verde.

## R5 — "Checked" ≠ revisado por pares; e run IDs não estão no git

**Objeção:** o documento classifica resultados deles como (A), mas o próprio site diz "the prose has
not been read by a human mathematician", e os `run-XXXXXX` do ledger vivem em JSONs do site, não no
commit clonado.
**Veredito: SUSTENTADA.**
**Correção aplicada:** §6 já traz a ressalva; **reforçado aqui:** citar (A)-não-revisado =
*site + ID de lemma + commit*; nunca "teorema da literatura". Os contadores do `overview.json`
(11.670 etc.) são **snapshot com sha256 registrado** (§0) — não vale citá-los como atuais depois de
novo fetch.

## R6 — Drift de toolchain (4.36.0 deles vs 4.34.0 nossa)

**Objeção:** vendorizar de um repo em toolchain mais nova pode quebrar ao sincronizar; a escolha
4.34 pode também divergir do `FoundationBridge` (que usa Mathlib).
**Veredito: SUSTENTADA (gerida).**
**Correção aplicada:** §4.4(2) torna o commit `89a01cd` o marco de sincronização; qualquer
re-sincronização futura repete o teste R4. **Não há decisão de toolchain aqui** — fora do escopo
desta sessão.

## R7 — Sanidade matemática do próprio teste

**Objeção:** um teste que compila não prova que o circuito testado calcula NAND.
**Investigação:** `nandCircuit` = portão 0 `AND [0,1]` → fiação 2; portão 1 `NOT [2]` → fiação 3;
`output = 3`. Teoremas verificados: `[true,false]↦true`, `[true,true]↦false` (por `decide`,
semântica de fiação ausente = `false` não exercitada aqui — escopo menor que o modelo cheio).
**Veredito: SUSTENTADA em parte; aceito como sanidade mínima**, registrado que o caso "fiação
inexistente lê false" **não** é coberto pelo teste.

## R8 — Números citados

- 432 `.lean` em `MetaComplexity/` (recursivo, `Get-ChildItem -Filter`) — OK.
- 15.974 `.lean` em `lean/` — OK (medido, inclui fixtures).
- 621 linhas / 22 theorems / 2 `sorry`s reais em `DDP.lean` (4 ocorrências da palavra, 2 em prosa
  nas linhas 30–32 e comentário 625) — OK.
**Veredito: MANTIDOS.**

## R9 — "Zero definições de circuito em `lean4/`"

**Objeção:** a varredura `Circuit|circuito|FanIn|HasCircuit` era case-sensitive e não pegava
"circuits" em inglês.
**Investigação:** reexecutada **case-insensitive** `circuit` → mesmos 2 achados (prosa em
`DDP.lean:289` e `DDP.lean:688`).
**Veredito: CONFIRMADA.**

---

## Veredito geral da rodada r1

**APROVADO COM CORREÇÕES** — todas aplicadas ao `MAPEAMENTO_DDP_vs_PEqualNP.md`
(R1 escopo, R2 fora-de-escopo D4′, R3 pendência de git, R4 status atualizado com teste EXIT=0,
R5 citão, R6 marco de sincronização, R7 limitação do teste, R8/R9 confirmados).

**Pendências explícitas que NÃO foram resolvidas (não prometer nada além disso):**
1. ~~(Autor) `.gitignore`/desmembramento do clone embutido antes de `git add` amplo.~~
   **RESOLVIDO:** `.gitignore` raiz, linha `pequalnp/pequalnp-proofs/` (verificado com
   `git check-ignore -v`); **aberto em r1b**: `PEQUALNP_MAPA.md` (tabela de IDs) — itens 2–4 abaixo inalterados.
2. (C) Vendorização **completa** (`depth`, `SIZE`, `PPoly`, `MCSP`) — exige Mathlib verde no projeto.
3. (C) Cross-checks minref×`IsRefutation` e `dd-cert`×`RUPWitness/FromResolution` — só propostos.
4. O `sorry`-count de `DDP.lean` (2) **não foi alterado por esta sessão** — nenhuma mudança em
   `lean4/`.

*Reavaliar em r2 se qualquer item acima mudar.*

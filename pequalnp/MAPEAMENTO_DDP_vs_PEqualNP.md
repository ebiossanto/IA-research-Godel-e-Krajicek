# MAPEAMENTO: `lean4/Gothic_Generators/DDP.lean` ↔ `lean/PEqualNP/MetaComplexity` (pequalnp.com)

**Data:** 26/11/2026 · **Sessão:** análise de https://pequalnp.com (/, /papers, /live) + baixa de artefatos
**Taxonomia:** **(A)** = extraído de fonte exata · **(P)** = decisão/argumento próprio do projeto · **(C)** = conjectura/hipótese pendente de teste

---

## 0. Artefatos baixados (reprodutibilidade)

| Artefato | Fonte | Identificação |
|---|---|---|
| `pequalnp/overview.json` | `https://data.pequalnp.com/data/map/overview.26ea0ad8ce25.json` | sha256 `2EA0AD8C…DA8CD` |
| `pequalnp/plan.json` | `https://data.pequalnp.com/data/plan.1b751ece02b7.json` | sha256 `1B751ECE…178C985`; `updated_at 2026-11-24T20:32:00Z` |
| `pequalnp/papers.json` | `https://data.pequalnp.com/data/papers.a2e9f3f7dded.json` | sha256 `A2E9F3F7…57C4C71` (claims do Note 1) |
| `pequalnp/pequalnp-proofs/` (clone raso) | `https://github.com/open-goat/pequalnp-proofs` | commit `89a01cdee376a95ca23acd8cdf2e68f2bc493983` (2026-11-27, "L-meta-25275 (#37411)"), **Apache License 2.0** |

- Toolchain deles: `leanprover/lean4:v4.36.0` + Mathlib pinado `fc4f59e577feb1a4956671bc04ac18aaaf8cd842` (`lean/lakefile.toml`).
- Toolchain nossa: `leanprover/lean4:v4.34.0` (`lean-toolchain` raiz); `lakefile.toml` raiz **sem Mathlib** (roots `Gothic_Generators.Core`, `Gothic_Generators.DDP`, `srcDir = lean4`).
- Escala: ~15.974 arquivos `.lean` no clone (16.027 arquivos no total); **432 `.lean`** sob `lean/PEqualNP/MetaComplexity/` (recursivo).
- ⚠️ `pequalnp/pequalnp-proofs/` é um repositório git embutido — **resolvido em 26/11/2026**: linha
  `pequalnp/pequalnp-proofs/` adicionada à raiz `.gitignore` (verificado com `git check-ignore -v`);
  artefatos do estudo (JSONs, MDs, scripts) continuam trackeáveis.

## 1. Arquitetura formal deles **(A)**

Camada de definições (`lean/PEqualNP/Defs/`, "the definitions every statement is read against"):

| Arquivo | Papel |
|---|---|
| `CircuitLowerBounds.lean` | `GateOp` (and/or/not/**mod m**/**maj** — fan-in ilimitado na base!), `Gate` (op + `List ℕ`), `Circuit` (lista de portões em ordem + índice de saída), `Circuit.wires/eval/size/depths/depth`, `Decides`, `SIZE(s)` (fan-in ≤ 2 como predicado), `PPoly`, `AC0`, `AC0Mod`, `ACC0`, `TC0`, `THRTHR` |
| `MetaComplexity.lean` | `FanInTwo` (predicado), `HasCircuitSize n f s`, `tableIndex`/`tableFun`, `MCSP`, `Large`/`UsefulAgainst` (propriedades naturais — o framework de "natural properties" da meta-complexidade), `encodePartial`, `Consistent`, `PartialMCSP` |
| `MetaComplexityMinimal.lean` | `circuitFun n C`, `IsMinimalCircuit`, `NearMinimal`, `LgpYes`/`LgpNo` (problema do último portão) |
| `ProofComplexity.lean` | `Literal V = V × Bool`, `Clause = Finset (Literal V)`, `ClauseSat`, `Satisfies`, `IsResolvent` (sem enfraquecimento), `IsDerivation` (**cláusula mais nova primeiro**), `IsRefutation` (comprimento = `π.length`), `PHP m n` |

Padrão de statement: **um arquivo = um teorema**, nome totalmente qualificado (`PEqualNP.MetaComplexity.L105`), docstring = enunciado informal, corpo = termo de prova delegado a helpers. Verificado por `lean/CheckLemma.lean` + `tools/check-lean.mjs` (toolchain e Mathlib pinados; CI em PRs). Contribuição externa via `/desk/next` (gap designado, lease com beat de 45 min, um arquivo por PR — `lean/PEqualNP/`**`Outside`**`/`).

## 2. O nosso `DDP.lean` (estado) **(A)**

- 621 linhas, **22** `theorem`/`lemma`, **2 `sorry`s intencionais** (`dd_solvable_in_ST_O1`, `pbounded_implies_feasible`) documentados como não-removíveis.
- **`import Init` apenas — sem Mathlib, por decisão explícita** (cabeçalho: limites de tempo são meta-teoria e ficam como predicados sobre estruturas).
- Conceitos: `Formula` (indutiva binária), `atoms`, `size`, `DisjointAtoms`/`DisjointDisjunction` (disjunção disjunta de Krajíček §2), `orAll`, `dget`, `Valuation = Nat → Bool`, `Eval`, `Tautology`, `PropProofSystem`/`Valid`, `DDFeasible`, teorema de totalidade de DD_P.
- **Varredura `Circuit|FanInTwo|HasCircuit` em `lean4/`: ZERO definições de circuito** (só 2 menções em prosa). Lacuna confirmada.

## 3. Tabela de mapeamento conceito ↔ conceito

| Nosso (`DDP.lean` / projeto) | Deles (`PEqualNP`) | Relação |
|---|---|---|
| `Formula` (indutiva, conectivos binários) | `Gate`/`GateOp` (programa de linha reta) | análogos sintáticos; **fórmula ≠ circuito** (fórmula = árvore; circuito = DAG com fiação) |
| `Valuation = Nat → Bool`, `Eval`, `Tautology` | `a : V → Bool`, `ClauseSat`, `Satisfies`; `Circuit.eval` | semântica; `Valuation` infinita vs `Fin n → Bool` |
| `DisjointDisjunction` (disjunção disjunta) | — | **exclusivo nosso** (Krajíček §2); eles não têm |
| `PropProofSystem`/`Valid` (pps de Cook–Reckhow abstrato) | `IsDerivation`/`IsRefutation` (Res concreto, sem enfraquecimento) | pps abstrato vs pps concreto; ponte = instanciar `Valid` como Res |
| `DD_P` (problema de busca aluno–professor) | — | **exclusivo nosso** |
| **— (nada)** | `Circuit`, `FanInTwo`, `HasCircuitSize`, `Circuit.size` | **nossa lacuna central** |
| **— (nada)** | `MCSP`, `PartialMCSP`, `Large`, `UsefulAgainst` | lacuna meta-complexidade (nosso `support/03` está DESCARTADO) |
| **— (nada)** | `SIZE`, `PPoly`, `AC0`/`ACC0`/`TC0` | lacuna classes não-uniformes |
| `gk_minref.py` (comprimento mínimo exato, Python) | `IsRefutation` + `π.length` | nosso empírico × formal deles; candidato a formalização futura **(C)** |
| `gk_dd_cert.py` (DRAT→DAG, verificador) | `RUPWitness/FromResolution.lean`, `SearchRUP.lean` | par candidato a cross-check **(C)** |
| D4′: dimensão fractal de DAGs de refutação | — | **não confundir**: DAG de refutação ≠ circuito Booleano (nós derivam cláusulas, não computam funções) |

## 4. A decisão pedida: o modelo de circuito deles entra como padrão do projeto?

### 4.1 O que o modelo deles é, regra por regra **(A)**

1. Circuito = **programa de linha reta**: portões em ordem, portão `j` produz fiação `n + j`; **aciclicidade por construção** (portão só vê fiações já existentes).
2. **Semântica total**: fiação inexistente lê `false`; saída inexistente lê `false` → constante `false` tem tamanho **0**, constante `true` (AND de lista vazia) tem tamanho **1**.
3. `GateOp.not` = negação da **cabeça** da lista; entradas extras ignoradas; em lista vazia = `true`.
4. `FanInTwo` é **predicado** (`op ∈ {and,or,not} ∧ inputs.length ≤ 2`), não um subtipo — toda lema carrega a hipótese.
5. `size` = nº de portões (**NOT conta**; entradas não contam).
6. Funções: `HasCircuitSize n f s` sobre `f : (Fin n → Bool) → Bool`; `circuitFun n C x = C.eval (List.ofFn x)`.

### 4.2 A favor **(P)**

- **Não há nada a migrar**: zero formalização de circuito em `lean4/` — custo de adoção ≈ 0, lock-in ≈ 0.
- É um modelo **checado, documentado e Apache-2.0** (reuso limpo com atribuição), alinhado à literatura (Krajíček/Pudlák, MCSP) e ao nosso layer Python (minref/fractal).
- **Interop**: qualquer lemma dos 11.670 lemas checados deles que queiramos citar/reusar fala `HasCircuitSize`/`FanInTwo`. Padrão = poder citar sem tradução.
- Resolve de uma vez a pergunta "qual convenção de tamanho?" que hoje cada script `gk_*` decide por conta própria.

### 4.3 Objeções (respondidas na rodada referee — ver `*_referee.md`) **(P)**

| Objeção | Resposta |
|---|---|
| `DDP.lean` é deliberadamente `import Init` puro | **Concedida.** A decisão NÃO toca `DDP.lean`: o padrão vale para módulos/futuros, não retroage. |
| Toolchain 4.34.0 (nós) vs 4.36.0 + Mathlib pinado (eles) | Concedida → adoção por **vendorização atribuída** de um núcleo novo, não por dependência imediata. |
| Definições de circuito deles num arquivo que importa Mathlib | **Testado nesta sessão (R4)**: núcleo vendorizado compila com `import Init` puro em v4.34.0 (**EXIT=0**), **com uma adaptação**: `Set` (Mathlib) → disjunção explícita em `FanInTwo`. `depth`/`SIZE`/`PPoly`/`MCSP` exigem Mathlib de verdade → ficam de fora do núcleo **(C)**. Ver `_r4_test_circuitcore.lean` e referee R4. |
| Escopo do projeto é prova/Gödel, não complexidade de circuito | Concedida e incorporada: adoção **condicional** ("no dia em que formalizarmos algo de circuito"), não importação agora. |
| DAG de refutação ≠ circuito | Concedida: o padrão vale para circuitos Booleanos **propios**; a ponte D4′ fica de fora do escopo do padrão. |

### 4.4 DECISÃO **(P)**

> **SIM — adotar o modelo de circuito de PEqualNP como PADRÃO DEFACTO do projeto para toda e
> qualquer noção formal de "circuito Booleano" (e para definições citadas em documentos), com
> quatro condições:**
>
> 1. **Não tocar `DDP.lean`** (continua `import Init`, sem Mathlib, 2 `sorry`s documentados).
> 2. **Adoção por vendorização atribuída**: se/when formalizarmos circuito, criar
>    `lean4/Gothic_Generators/CircuitCore.lean` com as definições **literais** deles
>    (`GateOp`, `Gate`, `Circuit`, `wires`, `eval`, `size`, `FanInTwo`, `HasCircuitSize`),
>    cabeçalho citando `open-goat/pequalnp-proofs@89a01cd`, `Defs/CircuitLowerBounds.lean` e
>    `Defs/MetaComplexity.lean`, licença Apache-2.0 — **com a adaptação já testada (R4)**: `Set`
>    é Mathlib; em `Init` puro usa-se a disjunção explícita `g.op = and ∨ g.op = or ∨ g.op = not`
>    (equivalente lógico exato; teste `pequalnp/_r4_test_circuitcore.lean` → `lake env lean` EXIT=0
>    em v4.34.0). A forma *literal* deles (com `Set`) e `depth`/`SIZE`/`PPoly`/`MCSP` só entram
>    quando `FoundationBridge` estiver verde com Mathlib **(C)**.
> 3. **Convenções obrigatórias em definições Lean novas e em textos que declarem tamanho/circuito**:
>    tamanho = nº de portões (NOT conta, entradas não), fan-in ≤ 2 sobre AND/OR/NOT, semântica de
>    fiação ausente = `false`, `FanInTwo` como hipótese. **Escopo (referee R1):** o padrão vale para
>    formalização em Lean e para convenções declaradas; scripts Python (`gk_*`) mantêm implementação
>    própria, mas o documento que os descreve deve **explicitar a correspondência** com essas
>    convenções.
> 4. **Fora do escopo do padrão**: DAGs de refutação (DRAT→DAG, minref) e métricas fractais D4′ —
>    são estruturas de prova, não circuitos; não renomear nem forçar a adaptação.
>
> Classificação da decisão: **(P)** (norma interna própria; a definição em si é **(A)** com a fonte exata acima).

## 5. Efeitos práticos imediatos

1. `pequalnp/` passa a ser a **fonte canônica de referência de circuito** do projeto (indexado no `INDICE.md`).
2. Ao formalizar qualquer afirmação de circuito futura, **não inventar definição**: usar `CircuitCore` vendorizado (condição 2 acima).
3. Candidatos de cross-check **(C)** (não-commitment): `gk_minref` × `IsRefutation`/comprimento;
   `gk_dd_cert` × `RUPWitness/FromResolution.lean`; tabela de tamanhos exatos de função aresta
   (Note 1: L-meta-102/104/105/106/113/115/154/204) como **calibração de COMPRIMENTO ótimo
   conhecido** para experimentos `gk_F*`/D4′ — **não** como estrutura de grafo (circuitos ≠ DAGs
   de refutação; escopo do padrão exclui D4′, ver referee R2).
4. Aproveitar o padrão de **statement-ledger** deles (arquivo = teorema, docstring = enunciado, run do verificador) como meta-modelo para o `claims-lint`/auditoria externa `DD_Res ∈ P`.

## 6. Referências exatas (para citação (A))

- `pequalnp-proofs@89a01cd` → `lean/PEqualNP/Defs/CircuitLowerBounds.lean` (GateOp, Gate, Circuit, size, SIZE)
- `pequalnp-proofs@89a01cd` → `lean/PEqualNP/Defs/MetaComplexity.lean` (FanInTwo, HasCircuitSize, MCSP)
- `pequalnp-proofs@89a01cd` → `lean/PEqualNP/Defs/MetaComplexityMinimal.lean` (circuitFun, IsMinimalCircuit)
- `pequalnp-proofs@89a01cd` → `lean/PEqualNP/Defs/ProofComplexity.lean` (IsResolvent, IsDerivation, IsRefutation, PHP)
- `pequalnp-proofs@89a01cd` → `README.md` (protocolo do checker e de contribuição `/desk/next`)
- Site: https://pequalnp.com/papers/note-1 (24/11/2026, 10 statements checked), https://pequalnp.com/live
- **Ressalva de honestidade de escopo**: "checked" = aceito pelo checker deles com toolchain/Mathlib pinados; **não é peer review** — classificar sempre como (A)-não-revisado por pares.

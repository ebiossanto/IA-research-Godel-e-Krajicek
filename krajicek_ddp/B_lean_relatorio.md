# Relatório — Equipe B (formalização Lean 4 do DD_P)

**Missão:** construir o esqueleto formal do problema DD_P (Krajíček, arXiv:2506.20221v4)
em Lean 4, no espírito do projeto `Gothic_Generators`.

---

## 1. O que foi entregue

| Arquivo | Conteúdo |
|---|---|
| `lean4/Gothic_Generators/DDP.lean` (695 linhas) | Esqueleto formal completo (só `import Init`, namespace `GothicGenerators.DDP`, doc em português) |
| `lean4/Gothic_Generators/DDP_Experiments.lean` (138 linhas) | Exemplos concretos verificados por avaliação finita e `native_decide` |
| `lakefile.toml` | `roots = ["Gothic_Generators.Core", "Gothic_Generators.DDP"]` (o restante preservado) |

**Compilação:** Lean 4 (`leanprover/lean4:v4.34.0`, a do `lean-toolchain`) foi **instalado**
neste ambiente (não estava presente; instalação via `elan`). Resultado final:

```
$ lake build
⚠ [3/4] Replayed Gothic_Generators.DDP
warning: lean4/Gothic_Generators/DDP.lean:628:8: declaration uses `sorry`
warning: lean4/Gothic_Generators/DDP.lean:690:8: declaration uses `sorry`
Build completed successfully (4 jobs).
EXIT=0
```

Os **únicos** dois `sorry` são os intencionais (§3). `DDP_Experiments.lean`, por não ser
root no `lakefile` (a missão fixou a lista de roots), foi verificado com `lean` direto
com `LEAN_PATH` apontando para `.lake/build/lib/lean` — **compila sem erros e sem
warnings**. (Nota de processo: houve ~4 iterações de correção de erros de tipo, todos
transcritos/corrigidos; o build final é limpo.)

## 2. O que foi formalizado e **provado** (sem `sorry`)

1. **Fórmulas** (`Formula`): `atom/bot/top/imp/and/or/not`; `atoms : Formula → List Nat`;
   `size`; `DisjointAtoms`; `DisjointDisjunction` via `List.Pairwise`; `orAll` (disjunção
   da lista, `orAll [] = ⊥`); `dget α i` (acesso i-ésimo — `List.get` do Lean 4 exige
   `Fin`, então `dget` é a tradução fiel de `α.get i`; lema `dget_eq`).
2. **Semântica** (`Eval`, `Tautology`), com lema central **`eval_congr`**: valorações que
   concordam nos átomos de `φ` avaliam `φ` igualmente (prova por indução em `φ`, caso a
   caso). **`TautologyDecidableAt`**: TAUT é decidível — `valuations` enumera as
   valorações com suporte nos átomos (`exists_agree` prova que toda valoração concorda
   com alguma enumerada) e `checkTaut_iff` mostra que a checagem finita decide `Tautology`.
3. **Sistema de prova** `structure PropProofSystem` com `Valid : List Formula → Formula → Bool`
   (decidível) + axioma de **sonoridade** `sound : Valid σ φ = true → Tautology φ`.
   Justificativa (escolha pedida): a pps de Cook–Reckhow é uma relação binária decidível
   `P(x,y)`; um `Bool` é exatamente a característica decidível dessa relação, e o certificado
   `σ` codifica o `x` de `P(x,y)`. A sonoridade é o axioma que garante `P(x,y) ⇒ TAUT`.
4. **Entrada/tarefa DD_P** (`DDInstance`, `DDTask`): `π`, `α : List Formula`, com
   `DisjointDisjunction α` e `Valid π (orAll α) = true`; concluir `∃ i < |α|, α_i ∈ TAUT`.
5. **LEMA DE TOTALIDADE — provado integralmente**, em duas formas:
   - `dd_counterexample_exists` (construtivo): indução em `α`; para cada disjuncto não-
     tautológico escolhe `vᵢ` falsificante (`exists_falsifier`, `falsifier`), e define
     `u := unionVal (atoms α₀) v₀ v_rest`. Os lemas `unionVal_mem/not_mem` + `eval_congr`
     mostram que `u` avalia cada disjuncto como a falsificante individual (a
     **consistência** — não-conflito — vem da disjunção de átomos: os átomos de `α₀` não
     aparecem na cauda, então `u` fora de `atoms α₀` é a valoração da cauda);
     `eval_orAll_congr` propaga a falsificação para `orAll`. Resulta `Eval u (orAll α) = false`.
   - `dd_totality` (a forma pedida): `hdisj + (¬∃i, α_i taut) ⇒ ¬Tautology (orAll α)`;
     e a contrapositiva `dd_totality_contrapositive`.
   - `dd_task_total`: sonoridade + contrapositiva ⇒ **toda entrada DD_P tem solução**.
6. **Modelo aluno–professor**: `structure Student` (`propose : Nat → List (Nat × Valuation) → Nat`),
   `orderStudent` (sequencial), `professor` honesto (aceita i.taut, senão envia falsificante;
   `professor_none_iff`), `play` (executa n rodadas), **`play_correct`** (toda aceitação é
   num índice realmente tautológico), **`order_none_implies`** (sem aceitação em n rodadas
   ⇒ nenhum disjuncto < n é tautologia), `StudentSolves`, `DDFeasibleInST` (esqueleto
   `DD_P ∈ ST[P, budget]` com `budget : Nat → Nat`), e o teorema **provado**
   `dd_solvable_in_m_rounds`: com orçamento `m` = nº de disjunctos, o estudante sequencial
   resolve; corolário `dd_feasible_in_ST_linear : DDFeasibleInST P (fun m => m)`.
7. **Disjunção viável**: `PBounded`, `FeasibleDisjunction`, `StrongFeasibleDisjunction`,
   e `pbounded_spec` **provado** (o núcleo semântico de `PBounded ⇒ FeasibleDisjunction`:
   existe `i < |α|` e certificado `σ : P ⊢ α_i` com `|σ| ≤ |α_i|^c`).
8. **Exemplos** (`DDP_Experiments.lean`): `α₁=[p₀,¬p₁]` e `α₂=[p₀∨p₁,¬p₂]` disjunções
   disjuntas **não-tautológicas** com falsificador explícito; `α₃=[p₀∨¬p₀, p₁]` com
   `⋁̇α₃ ∈ TAUT` e o contrapositivo do lema de totalidade extraindo o índice 0; tautologia
   `p₀∨¬p₀` decidida; e uma instância `DDInstance` real sobre o sistema `taugP`
   (Valid = checkTaut) resolvida pelo teorema geral em 2 rodadas.

## 3. O que ficou com `sorry` (intencionais, 2)

- **`dd_solvable_in_ST_O1`** (linha 628): `DD_P ∈ ST[P, O(1)]`. A hipótese **(ST)** de
  Krajíček postula que isto é **falso** para strong pps (equivalente a valer para EF).
  Deixar `sorry` é correto: provar (ou refutar) seria decidir uma questão meta-teórica
  **aberta**. O artigo só demonstra a versão com `m` rodadas (polinomial, não constante),
  que aqui está **provada** (`dd_solvable_in_m_rounds`).
- **`pbounded_implies_feasible`** (linha 690): `PBounded c ⇒ FeasibleDisjunction`.
  A parte semântica já está provada (`pbounded_spec`); falta o **limite de tempo** da
  busca exaustiva, que exige máquina de Turing/circuitos — ver §4.

## 4. Análise honesta: o que a formalização captura vs. o que NÃO captura

**Captura (conteúdo matemático puro, verificável pela máquina):**
- O lema de totalidade do DD_P, com a construção explícita da valoração falsificante
  `v = ⋃ vᵢ` (a parte realmente sutil: consistência da união via disjunção de átomos).
- Que toda entrada DD_P **tem** solução (`dd_task_total`) sob sonoridade — i.e., que DD_P
  é um problema de busca **total** no sentido fraco "∃ solução".
- Que o protocolo S-T com estudante sequencial e professor honesto encontra a solução em
  `m` rodadas, e que qualquer aceitação do professor é correta.

**NÃO captura (e não pode, de forma não-trivial, num sistema de prova como Lean):**
1. **"p-time", `O(1)` rodadas, `ST[P, ·]`**: `Student`, `DDFeasibleInST`, `PBounded` e
   `FeasibleDisjunction` são *predicados sobre estruturas*. O "F p-time" do aluno, o
   orçamento polinomial, e o "T arbitrário" são noções de **meta-teoria/complexidade**
   sobre implementações; num sistema de prova só se expressa a *relação* entre
   estruturas, não o custo computacional real. O modelo S-T original exige estudante
   p-time e classe `ST[P, O(1)]`; aqui `Student` é uma função arbitrária e a classe
   degenera num esqueleto predicado. Formalizar "p-time" exigiria codificar máquinas de
   Turing/circuitos e medir tempo — um projeto inteiro à parte, e mesmo assim seria um
   *axioma* de correspondência, não um fato do Lean.
2. **A hipótese (ST) e o Problema 2.1** são enunciados de **meta-teoria** (sobre strong
   pps, modelos não-padrão de `T_PV`, permutações one-way, `NP` vs `coNP`). Eles não são
   "teoremas dentro de um sistema" mas afirmações **sobre** sistemas;均使其 dependem de
   `NP ≠ coNP`-style assumptions. Por isso `dd_solvable_in_ST_O1` é `sorry` **permanente**:
   não é uma lacuna de trabalho, é o limite do que se pode afirmar sem decidir questões
   abertas. O que formalizamos — a direção **verificável** ("S-T com m rodadas resolve",
   provada) — é exatamente o que o artigo usa como **fato**, enquanto `O(1)` é a
   **hipótese (ST)**.
3. **Sonoridade/completude da pps**: `sound` é um **axioma** da estrutura `PropProofSystem`,
   não demonstrado — reflete que, para um pps concreto (ex. EF), a sonoridade é um teorema
   meta-teórico, não algo codificável aqui.

**Caminhos promissores (seguimento):** (i) instanciar `PropProofSystem` com um sistema
concreto pequeno (ex. tabelas de verdade / cutting planes sobre fórmulas fixas) e provar
`sound` para ele; (ii) formalizar o enunciado de `ST[F, t(n)]` sobre uma máquina de Turing
de referência para tornar "O(1) rodadas" uma afirmação precisa (mantendo-a como hipótese);
(iii) estender a `D_P` (a generalização de Krajíček) reproduzindo o Lema 1
(`DD_P ∉ ST[P,O(1)] ⇔ D_P ∉ ST[P,O(1)])` na parte finita/verificável.

---
*Equipe B — formalização concluída; build `lake build` = sucesso (exit 0), 2 `sorry`s intencionais.*

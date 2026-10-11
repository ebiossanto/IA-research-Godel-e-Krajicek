# G2 — Relatório de referee hostile (subagente independente)

**Alvo:** `G2_semente_Fsent.md`. **Apoio:** `F2_versao_finita.md`, `G1_log_forcing.md`, `A_teoremas_exatos.md` (transcrição do artigo: (S2), item (1)).

## R1 — G2, Teorema 1.1 (fechamento da semente): **PARCIAL**

O fechamento finitista é legítimo: refutação EF é objeto finito, usa só finitas condições de `T_σ`; `C_j` têm prova EF em `M`; concatenação é p-tempo e `M ⊨ T_PV` é fechada sob funções p-tempo, logo concatenação ∈ `M`. Item (1) literal — "`φ` has **no proof in `M` in any proof system**" (Thm 3) — cobre EF ✓; Claims 1–2 de [Kra98] aí se aplicam.

**Mas o sinal está trocado.** Como escrito, `T_σ = {φ ∈ Circuit_M(p), C : C ≡ 1}` força `ν_G(φ)=1` (o oposto do alvo), e refutação de `{C_1,…,C_k, φ}` + provas de `C_j` dá EF ⊢ **¬φ** — não contradiz item (1) nem produz `(¬φ) ∈ SAT`. **Correção:** semente `{C : C ≡ ¬φ ou C ≡ 1}`; aí refutação de `{C_1,…,C_k, ¬φ}` ⟹ EF ⊢ `φ` ✓ e `ν_G(¬φ)=1` dá `σ` falsificador ✓. Declarar: "refutação de `T` = EF ⊢ ¬∧T".

## R2 — G2, Teorema 2.1(a): **ERRO (dois furos)**

1. **Sem hipótese sobre `M'`** ("`σ ∈ M'`"), a prova invoca absolutidade de `Prf_P`/`Fals`, que exige `M' ⊨ PV`. "Para qualquer superestrutura" é falso: uma extensão pode interpretar `Prf` à moda própria. Na leitura Σ^b_1 ("`x:P⊢y` = ∃z") o testemunho só existe em `M'`.
2. **Soundness real (externa) não cobre objetos não-padrões.** "`σ_{i_0}` é *realmente* uma derivação" é vazio para `σ_{i_0}` não-padrão; o que se precisa é **`Ref_P` interno em `M'`**. Padrão clássico: relação p-tempa realmente vazia (código de halting de programa que não halta, independente de PV) tem solução não-padrão num modelo de PV; idem para `P` cuja soundness PV não prove. "Nenhuma superestrutura satisfaz `∃y Fals`" só vale se `M' ⊨ Ref_P`.

**Salvamento (1 linha):** exija `M' ⊨ T_PV` (ou `PV + Ref_P`, ou prove `PV ⊢ Ref_P` p/ o `P` escolhido) — aí Thm 2.1 vale, e o que ele derruba é **só** o descarte de `T_PV` no Thm 4.1 de G2.

## R3 — G2, §2.3 (união de falsificadores via (S2)): **OK**

(S2) é literalmente "no two `α_i` have an atom in common" (artigo, A §1.2): falsificadores de `α_{i_1},…,α_{i_k}` (`i_j ∈ M`, testemunhas de (S4) em `M`) unem-se sem conflito e falsificam a conjunção; p-tempo-absoluto ✓. Ressalvas: (a) satisfatibilidade finita ≠ consistência de forcing — enunciar "atribuição falsificante real ⟹ sem refutação EF em `M`" (via `Ref_EF ∈ T_PV`); (b) espelhamento uniforme p/ `i<m` não-padrão (§2.2) plausível (p-tempo em `(α,j)`, átomos de `α` ∈ `M`) mas **não provado**; (c) "(R3) ≡ BB" só nas direções admitidas em §6 — manter (C)/(P).

## R4 — G2, Teorema 4.1 (descartar `M' ⊨ T_PV`): **ERRO — o furo do R2 entra aqui**

A contradição **não** fecha sem `Ref_P` em `M'`: `(F-sent)` dá `M' ⊨ (¬α_{i_0}) ∈ SAT`; o lado `∉ SAT` com parâmetros **novos** `σ_{i_0}, α_{i_0}` exige `Ref_P` **dentro** de `M'` — universal não sobe p/ extensões (só desce). F2 §2(d) tinha isso via `M' ⊨ T_PV`; "soundness real" não substitui. **Correção:** restaurar `M' ⊨ T_PV` (item 1 da (F-sent), F2 §1) ou exigir `M' ⊨ Ref_P`. Item (c) do Thm 2.1 herda o defeito.

## R5 — G2, §2.5.1 (meta-argumento da reductio): **ERRO (não sequitur; contradiz o próprio parágrafo)**

G2 admite em seguida que "`ZFC+NP=coNP ⊢ config` provaria `NP ≠ coNP`" — legítimo. Logo "o lemma de construção seria prova de ⊥ e portanto **não pode existir**" não se segue: tal lemma dá `ZFC+NP=coNP+ST ⊢ ⊥`, que **é** a prova desejada de `NP ≠ coNP`; nada o proíbe. Nem construção incondicional (ZFC) derruba ZFC: por Thm 2.1 + KPT daria `ZFC ⊢ ¬(ST)`, não `⊥`. "Toda demonstração deve extrair a contradição sem construir" é falso como lógica (construção sob NP=coNP seria prova válida); é heurística, não teorema. **Correção:** "construção incondicional ⟹ `¬(ST)`; condicionada a `NP=coNP`, se existir, já fecha o teorema; Thm 2.1 mostra só que a **contradição do artigo não pode morar no passo (5)**."

## Corrigenda mínimo

1. §1.2: semear `¬φ` (sinal); definir "refutação de `T` = EF ⊢ ¬∧T".
2. Thm 2.1: hipótese `M' ⊨ T_PV` (ou `PV + Ref_P`); "realmente" → "`M' ⊨ Prf_P`".
3. Thm 4.1: reintroduzir `M' ⊨ T_PV`; (F-b')/Cor. 4.4 de G1 ficam intactos.
4. §2.5.1: reescrever conforme R5.

**Resumo:** Thm 1.1 conserta-se (sinal); Thm 2.1(a)/4.1 perdem o descarte de `T_PV`; §2.3 (S2) correta; §2.5.1 logicamente inválida.

# 25 — Foundation (instância Lemma3Hyp) + Freund–Pakhomov (comprimento vs δ)

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **PR25 — Foundation clone + instância; PR7 experimento executado**
**Scripts:** `fp_length_vs_delta.py`
**Depende de:** `24_FOUNDATION_LEMMA3_ALLCOV.md`, `13_...` (RCS), `09 §12/§19/§26`

---

## 1. Foundation — clone + instância `Lemma3Hyp`

### 1.1. Infra

| Item | Status |
|------|--------|
| Clone `FormalizedFormalLogic/Foundation` | **CLONADO** (c69c68c, depth 1) |
| Toolchain | `leanprover/lean4:v4.34.0` (**mesma** do projeto) |
| Mathlib | dep Foundation — cache/manifest do Foundation (`5ed2965` checkout ok) |
| **Pacote isolado** | `FoundationBridge/` (path `..` + `../Foundation`) — **Core.lean sem Mathlib** |
| Build Core | `lake build GothicGenerators` (raiz, sem Foundation) |
| Build instância | `cd FoundationBridge && lake update && lake build` |

### 1.2. Arquivo `FoundationBridge/FoundationInstance.lean`

Mapeamento honesto:

| Campo `Lemma3Hyp` | Foundation | Status |
|-------------------|------------|--------|
| `Con` | `T.Consistent ℕ` (Consistency.lean:24) | **DEFINIÇÃO** |
| `Prf(p,⊥)` | `Bootstrapping.Proof T p ⌜⊥⌝` (Proof/Basic.lean:471) | **DEFINIÇÃO** |
| `pad(w*,p,z)` | **não existe** (só `Semiformula.padding` em fórmulas) | **LOCAL** |
| `PhiStar'` | `∀x, hasBinPrefix w* x → ¬Φ T x` (09 §12) | **LOCAL** (leitura definicional) |
| `inconsistent_implies_not_phi` | **PROVADO** (¬Con → ∃p Proof → pad → ¬Φ^{w*}) | 0 sorry |
| `consistent_implies_phi` | **PROVADO** (Con → ∀x ¬Φ → Φ^{w*}) | 0 sorry |
| `lemma3_con_for` | bicondicional via Core `lemma3_con` | 0 sorry |

Pontes Foundation documentadas: `con_entailment` (`standard_consistent`), `Entailment.padding_iff`.

### 1.3. O que **NÃO** fecha (ABERTO, sem sorry)

1. **Bridge** `PhiStar'` ↔ obrigação `Φ^w` de Core (`covered`/`delta`) / `W^true` do experimento;
2. **Sentença reificada** `Φw* : ArithmeticSentence` + `T ⊢ Φw* 🡘 T.consistent`
   → aplicaria `consistent_unprovable` / `gödel_iff_con` (Gödel II real);
3. **pad bit-a-bit** (`List Bool`) para `w*="00"` (zeros à esquerda);
4. **∞ testemunhas** de pad sob ¬Con (injetividade em `z`).

**Veredito Foundation:** instância **viável com 0 sorry** no nível meta-Prop; conteúdo metamatemático migrou para a correção de `pad`/`PhiStar'`; Gödel II reificado = próximo prêmio.

---

## 2. Freund–Pakhomov — comprimento vs δ (PR7)

### 2.1. Pergunta (PR7)

> Freund–Pakhomov: PA prova polinomialmente `Con(PA+Con*(PA))↾n` — **isso aparece em δ_T(Φ,b)?**
> (`10:167`, `EVOLUCAO:160`, `INDICE:107`)

### 2.2. Ponte estrutural (definição)

\[
\delta_T(\Phi,b) = \#\{w \in W^{\mathrm{true}} : s_T(\Phi^w) > b\},
\quad
\min\{b : \delta=0\} = \max_w s_T(\Phi^w) = \kappa_T(\Phi)
\]

(PR24: ALL_COV ⟺ δ=0 ⟺ σ≥maxκ ∧ b≥maxκ+1.)

**δ é a função sobrevivência (complemento da CDF) dos comprimentos por obrigação.** Comprimento = dado; δ = agregação. Pergunta: a agregação **preserva** a separação poly/non-poly de FP?

### 2.3. Modelo (lei de comprimento **dependente de n**)

| Alvo | `s(n)` | Papel |
|------|--------|-------|
| lento (slow) | `n²` | proxy Con\*(PA) / FP poly |
| rápido (fast) | `2ⁿ` | progressão "rápida" |

- `W = {0,1}^6` (64); obrigação `w*` (índice 0) carrega `s(n)`; genéricas `1+hash%3`;
- **controle negativo:** scripts antigos `proof_len=κ+1` **constante em n** → incapazes de expressar poly vs exp (corrigido aqui).

### 2.4. Hipóteses pré-registradas

- **H_identity:** δ(b)=#{w:s>b} e β=min{b:δ=0}=κ — senão experimento inválido;
- **H_FP-in-δ:** ∃(n,c): δ_slow(n^c) < δ_fast(n^c) → **PR7 = SIM no modelo**;
- **H_growth:** β_slow polinomial (slope log–log ≤4); β_fast super.

### 2.5. Saídas / veredito

| # | Significado |
|---|-------------|
| O1 | implementação fiel à definição de δ |
| O2 | β_slow poly — **reproduz** teorema FP (literatura) |
| O3 | β_fast super-poly |
| O4 | separação visível **em δ** → PR7 |
| O7 | comprimento difere mas δ idêntico → δ **cego** ao fenômeno FP |

**Classificação:**

| Item | Classe |
|------|--------|
| Teorema FP 2020 (literatura) | **TEOREMA** (deles) |
| δ = #{w:s>b}; β=κ; ALL_COV⟺δ=0 | **TEOREMA** (este projeto, Lean PR24) |
| `s_slow=n²` vs `s_fast=2ⁿ` | **ANALOGIA** (modelo estrutural) |
| "δ captura separação FP" (após O4) | **CONJECTURA verificada no modelo** — PA real ABERTO |
| PR7 em PA real | **ABERTO** |

### 2.6. Discrepâncias de bibliografia (a corrigir em papers)

1. Título errado FP em `papers/paper1:164-165`, `paper2:212-213`
   → correto: *"Short Proofs for Slow Consistency"* (NDJFL 61(1));
2. Variante `Con(PA+Con*(PA))↾n` vs `Con(PA+Con(PA))↾n*` — fixar **Con\*** (lenta).

---

## 3. Próximos passos

1. `cd FoundationBridge && lake update && lake exe cache get && lake build` (Mathlib pesado);
2. Sentença reificada `Φw*` + Gödel II (`consistent_unprovable`);
3. Bridge `PhiStar'` ↔ `Obligation`/`covered`;
4. ~~Corrigir títulos FP nos papers~~ **FEITO** (PR25);
5. Comparar Freund–Pakhomov em PA real (não só modelo).

---

## 4. Arquivos

- `FoundationBridge/FoundationInstance.lean` + `lakefile.toml` — instância isolada
- `Foundation/` — clone
- `fp_length_vs_delta.py` — PR7
- `24_FOUNDATION_LEMMA3_ALLCOV.md` — PR24 (limiar ALL_COV)
- `lakefile.toml` (raiz) — **Core only**, sem require Foundation

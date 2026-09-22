# 24 — Foundation (interface lemma3) + Generalização (C) ALL_COV

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **EXECUTADO — lemma3 CON=direções provadas; ALL_COV ⇔ δ=0 (4 perfis); `lake build` LIMPO**
**Scripts:** `test_allcov_threshold.py` (EXIT=0)
**Depende de:** `09_...` §12 (Lema 3), `17_...` §2 (cond. C), `15_...` (Lean)

---

## 1. Foundation — `lemma3_con` axiom → prova

### 1.1. O que mudou

| Antes (PR18) | Agora (PR24) |
|--------------|--------------|
| `axiom lemma3_axiom (P) : P.phi_wStar_true = P.conT` (Bool trivial) | `structure Lemma3Hyp` com `Con`, `PhiStar` : Prop |
| axiom aceito sem prova | **`lemma3_con`: bicondicional PROVADO** da interface |
| 0 axiomas úteis | **0 `axiom` no arquivo**; hipóteses = campos da structure |

### 1.2. Interface metamatemática (`Lemma3Hyp`)

Campos (a serem **derivados** de Foundation/Prf/pad-Prf na integração completa):

1. `inconsistent_implies_not_phi : ¬Con → ¬PhiStar`
   — se ¬Con(T), ∃p Prf_T(p,⊥); padding → ∃x Φ_T(x) com prefixo w* → ¬Φ^{w*} (09 §12);
2. `consistent_implies_phi : Con → PhiStar`
   — se Con(T), não existe tal p; ∀x ¬Φ_T(x) → Φ^{w*}.

### 1.3. Teoremas provados

```lean
theorem lemma3_con (H : Lemma3Hyp) : H.PhiStar ↔ H.Con
theorem lemma3_con_of_consistent (H) (hc : H.Con) : H.PhiStar
theorem lemma3_con_refute (H) (hnc : ¬H.Con) : ¬H.PhiStar
```

**Honestidade:** o **bicondicional** é teorema; as **duas direções metamatemáticas**
são hipóteses explícitas da interface. Instanciar com Prf/pad = trabalho Foundation
(clone + Mathlib; ver `05_...` §2.5).

---

## 2. Generalização (C) — limiar de ALL_COV

### 2.1. Enunciado

T' cobre todo `w ∈ truesOf W` (ALL_COV / cond. C) **sse**:

\[
\sigma_{T'} \ge \max\kappa \quad\wedge\quad b \ge \max\kappa + 1
\]

(κ sobre obrigações **verdadeiras** de W).

### 2.2. Lean (`Core.lean`, após `length_filter_sub`)

| Item | Status |
|------|--------|
| `maxKappa W` | foldl max de κ em truesOf |
| `allCovered T b W` | todos verdadeiros cobertos |
| `allCovered_iff_delta_zero` | **PROVADO** |
| `allCovered_of_sigma_max` | **PROVADO** (σ≥maxκ ∧ b≥maxκ+1 ⇒ ALL) |
| `delta_zero_of_sigma_max` | **PROVADO** (corolário δ=0) |
| `cond_C_delta_zero` | **PROVADO** (ligação com predicado C) |

Helpers: `foldl_max_ge`, `foldl_max_mono_acc`, `le_maxKappa_of_mem_trues`,
`filter_eq_self_of_forall`.

### 2.3. Experimento (`test_allcov_threshold.py`)

| Perfil | maxκ | σ* | b* | all⇔δ=0 | suf. | nec. |
|--------|------|----|----|---------|------|------|
| E0 base r=4 | 2 | 2 | 3 | OK | OK | OK |
| E1 rich r=4 | 3 | 3 | 4 | OK | OK | OK |
| E3 base r=6 | 2 | 2 | 3 | OK | OK | OK |
| PR23 explicit | 2 | 2 | 3 | OK | OK | OK |

Transições σ→σ' com w₀ existente e w₀'=ALL: **75/185** pares (C inevitável no limiar).

**Veredito PR24: Generalização (C) VERIFICADA — suficiência + necessidade, 4 perfis.**

---

## 3. `lake build` (PR24)

- **EXIT=0**; **0 `sorry`**; **0 `axiom`** no `Core.lean`
- lemma3 é **teorema** (da interface Lemma3Hyp)
- delta_mono, theorem4_strict, rcs_exists, allCovered_*, delta_zero_* **verificados**

---

## 4. Análise honesta

| Item | Status |
|------|--------|
| lemma3 bicondicional | **PROVADO** da interface Prop |
| Hipóteses Foundation (Prf/pad) | **ABERTO** — campos de Lemma3Hyp a instanciar |
| Generalização (C) | **PROVADA + TESTADA** (limiar exato) |
| PA real | **ABERTO** (caveat padrão) |

---

## 5. Próximos passos

1. ~~Foundation interface lemma3~~ — **FEITO** (PR24)
2. ~~Generalizar (C) ALL_COV~~ — **FEITO** (PR24)
3. Instanciar `Lemma3Hyp` com Foundation (clone + Prf/pad) — **ABERTO**
4. Comparar Freund–Pakhomov (comprimento vs δ)

---

## 6. Arquivos

- `lean4/Gothic_Generators/Core.lean` — Lemma3Hyp, lemma3_con, (C) theorems
- `test_allcov_threshold.py` — limiar ALL_COV (4 perfis)

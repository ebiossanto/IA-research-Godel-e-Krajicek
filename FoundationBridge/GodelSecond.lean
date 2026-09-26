/-
  GothicGenerators.GodelSecond
  PR27 — rota A: Φw* reificada := T.consistent (Gödel II).
  PR28 — rota B: Φw* padded com prefixo w* (09 §12, doc27).

  Requires Foundation build (Mathlib). Core.lean stays Init-only.
-/
import Foundation.FirstOrder.Incompleteness.Consistency
import Foundation.FirstOrder.Incompleteness.Second
import Foundation.FirstOrder.Incompleteness.ProvabilityAbstraction.Basic
import Foundation.FirstOrder.Arithmetic.Exponential.Exp
import Foundation.FirstOrder.Arithmetic.IOpen.Basic

namespace GothicGenerators
namespace GodelSecond

open FFL FFL.Entailment FFL.FirstOrder
open FFL.FirstOrder.Arithmetic
open FFL.FirstOrder.Arithmetic.Bootstrapping

/-- Rota A: a sentença Φw* canônica É a sentença de consistência do Foundation. -/
noncomputable def PhiW (T : ArithmeticTheory) [T.Δ₁] : ArithmeticSentence :=
  T.consistent.val

/-- T ⊢ Φw* 🡘 Con(T) — identidade (mesma sentença). -/
theorem phiW_iff_consistent (T : ArithmeticTheory) [T.Δ₁] :
    T ⊢ PhiW T 🡘 T.consistent.val :=
  show T ⊢ T.consistent.val 🡘 T.consistent.val from E_id

/-- Gödel II transportado: T ⊬ Φw*. -/
theorem unprovable_phiW (T : ArithmeticTheory) [T.Δ₁] [𝗜𝚺₁ ⪯ T]
    [Consistent T] :
    T ⊬ PhiW T :=
  consistent_unprovable T

/-! ## Rota B — Φw* com padding w* (09 §12)

Sentença fechada: `∀x [x tem bloco binário w* → ¬∃p,z [Proof_T(p,⊥) ∧
x = w*·2^(⟪p,z⟫+1) + ⟪p,z⟫]]`. Prefixo e pad reificados via `expDef`/`pairDef`
(gráficos Σ₀ com defined-instances; `!expDef e k` ⇔ `e = Exp.exp k`,
`!pairDef b p z` ⇔ `b = ⟪p,z⟫`). Padrão de prova: `complete` (FixedPoint.lean:132)
+ `internalize_provability`/`modus_ponens_sentence` (FGH.lean:84-117). -/

/-- Φw* (rota B): sentença de Gödel II com padding w*. -/
noncomputable def phiWStarB (T : ArithmeticTheory) [T.Δ₁] (wStar : ℕ) : ArithmeticSentence :=
  “∀ x, (∃ k r e, x = ↑wStar * e + r ∧ r < e ∧ !expDef e k) →
     ¬∃ p z b c, !(proof T).pi p !!⌜(⊥ : ArithmeticSentence)⌝ ∧
       !pairDef b p z ∧ !expDef c (b + 1) ∧ x = ↑wStar * c + b”

/-- Entailment central: `T ⊢ Φw* 🡒 T.consistent`.
    Semântica: num modelo V ⊧ T, se V ⊧ Φw* então ¬∃d Proof_V(d,⊥):
    de uma prova d de ⊥ montamos o testemunha x = w*·2^(⟪d,0⟫+1)+⟪d,0⟫,
    que tem prefixo w* (crescimento `lt_exp`+`exp_monotone`) e satisfaz o
    bloco de pad com prova d — contradizendo V ⊧ Φw*. -/
theorem phiWStarB_consistent (T : ArithmeticTheory) [T.Δ₁] [𝐈𝚺₁ ⪯ T] (wStar : ℕ) :
    T ⊢ phiWStarB T wStar 🡒 T.consistent.val := by
  haveI : 𝗘𝗤 _ ⪯ T := Entailment.WeakerThan.trans (𝓣 := 𝗜𝚺₁) inferInstance inferInstance
  exact complete.{0} T _ fun (V : Type) _ _ ↦ by
    haveI : V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁ := ModelsTheory.of_provably_subtheory V 𝗜𝚺₁ T inferInstance
    simp only [models_iff, Theory.consistent.defined]
    intro hΦ hCon
    obtain ⟨d, hd⟩ := hCon
    let b : V := ⟪d, 0⟫
    refine hΦ ((wStar : V) * Exp.exp (b + 1) + b)
      ⟨b + 1, b, Exp.exp (b + 1), by simp, ?lt, ?exp⟩
      ⟨d, 0, b, Exp.exp (b + 1), ?prf, ?pair, ?exp2, by simp [b]⟩
    · case lt => exact lt_of_lt_of_le (lt_exp b) (le_of_lt (by simp))
    · case exp => simp [b, expDef]
    · case prf => simpa using hd
    · case pair => simp [b, pairDef]
    · case exp2 => simp [b, expDef]

/-- Gödel II rota B: T ⊬ Φw* (sentença padded com prefixo w*). -/
theorem unprovable_phiWStarB (T : ArithmeticTheory) [T.Δ₁] [𝗜𝚺₁ ⪯ T]
    [Consistent T] (wStar : ℕ) : T ⊬ phiWStarB T wStar := by
  intro h
  have hent := phiWStarB_consistent T wStar
  have hprov : Bootstrapping.Provable T (⌜phiWStarB T wStar⌝ : ℕ) :=
    Bootstrapping.internalize_provability (V := ℕ) h
  have hcons : Bootstrapping.Provable T (⌜T.consistent.val⌝ : ℕ) :=
    Bootstrapping.modus_ponens_sentence T
      (Bootstrapping.internalize_provability (V := ℕ) hent) hprov
  exact consistent_unprovable T (Bootstrapping.provable_iff_provable.mp hcons)

end GodelSecond
end GothicGenerators

/-
  GothicGenerators.FoundationInstance
  PR25 — instancia `GothicGenerators.Lemma3Hyp` a partir da API do Foundation
  (Saitou–Noguchi): Con, Prf (Bootstrapping.Proof), pad local.

  STATUS HONESTO:
  • Con := T.Consistent ℕ (Foundation Consistency.lean:24)
  • Prf := Bootstrapping.Proof (Proof/Basic.lean:471)
  • pad/hasBinPrefix: LOCAIS (gap: Foundation só tem Semiformula.padding em fórmulas)
  • PhiStar': leitura definicional de 09 §12; ponte com obrigação δ/CorE ainda ABERTA
  • 0 sorry; Core.lean continua import Init sem Mathlib
-/
import Gothic_Generators.Core
import Foundation.FirstOrder.Incompleteness.Consistency
import Foundation.FirstOrder.Incompleteness.Second
import Foundation.FirstOrder.Syntax.Classical.Padding
import Foundation.FirstOrder.Arithmetic.Bootstrapping.Syntax.Proof.Basic

namespace GothicGenerators
namespace FoundationInstance

open FFL FFL.Entailment FFL.FirstOrder
open FFL.FirstOrder.Arithmetic FFL.FirstOrder.Arithmetic.Bootstrapping

/-- Prefixo binário de valor: x = w·2^k + r, r < 2^k.
    Nota: leading zeros se perdem em ℕ (w*="00" → 0); fidelidade bit a bit
    exigiria wStar : List Bool. -/
def hasBinPrefix (w x : ℕ) : Prop := ∃ k r, x = w * 2 ^ k + r ∧ r < 2 ^ k

/-- pad w p z = w deslocado + código do par (p,z) — prefixo w por construção. -/
def pad (w p z : ℕ) : ℕ := w * 2 ^ (Nat.pair p z + 1) + Nat.pair p z

lemma pair_lt_two_pow (n : ℕ) : n < 2 ^ (n + 1) := by
  have h1 : n < 2 ^ n := Nat.lt_pow_self (by omega)
  have h2 : 2 ^ n ≤ 2 ^ (n + 1) := Nat.pow_le_pow_right (by omega) (by omega)
  exact lt_trans h1 h2

lemma hasBinPrefix_pad (w p z : ℕ) : hasBinPrefix w (pad w p z) :=
  ⟨Nat.pair p z + 1, Nat.pair p z, rfl, pair_lt_two_pow (Nat.pair p z)⟩

section
variable (T : ArithmeticTheory) [T.Δ₁] (wStar : ℕ)

/-- Φ_T(x) := ∃p,z [Proof_T(p,⊥) ∧ x = pad(w*,p,z)] (10 §2.4). -/
noncomputable def Phi (x : ℕ) : Prop :=
  ∃ p z : ℕ,
    Bootstrapping.Proof T p (⌜(⊥ : ArithmeticSentence)⌝ : ℕ) ∧ x = pad wStar p z

/-- Φ_T^{w*}: nenhum x com prefixo w* satisfaz Φ (09 §12). -/
def PhiStar' : Prop := ∀ x, hasBinPrefix wStar x → ¬ Phi T wStar x

/-- Con canônico desdobrável: ¬∃d, Proof T d ⌜⊥⌝. -/
def conProp : Prop := ¬ ∃ d : ℕ, Bootstrapping.Proof T d (⌜(⊥ : ArithmeticSentence)⌝ : ℕ)

lemma con_iff : T.Consistent ℕ ↔ conProp T := by
  simp [Theory.Consistent, Provable, conProp]

/-- Instância do Lema 3 a partir de Foundation (Prf/pad/Con). -/
def lemma3Hyp : Lemma3Hyp where
  Con := T.Consistent ℕ
  PhiStar := PhiStar' T wStar
  inconsistent_implies_not_phi := by
    intro hnc hs
    obtain ⟨p, hp⟩ := Classical.not_not.mp ((con_iff T).mp hnc)
    exact hs (pad wStar p 0) (hasBinPrefix_pad wStar p 0) ⟨p, 0, hp, rfl⟩
  consistent_implies_phi := by
    intro hc x _ hx
    obtain ⟨p, _, hp, -⟩ := hx
    exact hc ⟨p, hp⟩

/-- Corolário: recupera lemma3_con do Core para T. -/
theorem lemma3_con_for :
    (lemma3Hyp T wStar).PhiStar ↔ T.Consistent ℕ :=
  lemma3_con (lemma3Hyp T wStar)

/-- Ponte interna ↔ sintática (Foundation Consistency.lean:75). -/
theorem con_entailment (T : ArithmeticTheory) [T.Δ₁] [R₀ ⪯ T] :
    T.Consistent ℕ ↔ Entailment.Consistent T :=
  standard_consistent T

/-- Padding de fórmulas do Foundation (sorte: fórmulas, não códigos). -/
example (σ : ArithmeticSentence) (k : ℕ) :
    T ⊢ σ.padding k 🡘 σ :=
  Entailment.padding_iff σ k

/-! ABERTO (documentado, sem sorry):
  1. Bridge PhiStar' ↔ obrigação Φ^w de Core (covered/delta) / W^true.
  2. Sentença reificada Φw* : ArithmeticSentence + T ⊢ Φw* 🡘 T.consistent
     → consistent_unprovable / gödel_iff_con (Gödel II).
  3. pad bit-a-bit com List Bool (leading zeros de w*="00").
  4. ¬Con → ∃∞ x, Phi (injetividade de pad em z). -/

end

end FoundationInstance
end GothicGenerators

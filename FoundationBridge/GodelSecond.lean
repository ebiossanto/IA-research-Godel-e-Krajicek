/-
  GothicGenerators.GodelSecond
  PR27 — rota A: Φw* reificada := T.consistent (Gödel II).

  Requires Foundation build (Mathlib). Core.lean stays Init-only.
-/
import Foundation.FirstOrder.Incompleteness.Consistency
import Foundation.FirstOrder.Incompleteness.Second
import Foundation.FirstOrder.Incompleteness.ProvabilityAbstraction.Basic

namespace GothicGenerators
namespace GodelSecond

open FFL FFL.Entailment FFL.FirstOrder
open FFL.FirstOrder.Arithmetic

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

/-! ABERTO (rota B): Φw* padded com prefixo w* (09 §12) — internalização
    via `definability` + entailment não-trivial (padrão FGH.lean). -/

end GodelSecond
end GothicGenerators

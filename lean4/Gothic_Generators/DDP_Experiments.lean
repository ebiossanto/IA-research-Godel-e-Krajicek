import Gothic_Generators.DDP

/-!
# DD_P — exemplos concretos (Equipe B)

Verificações por avaliação finita de fórmulas pequenas, pela decisão de TAUT
(`checkTaut`), e uma mini-execução do protocolo aluno–professor com um
sistema de exemplo.
-/

namespace GothicGenerators
namespace DDP
namespace Experiments

/-- Proposições atômicas `p₀, p₁, p₂`. -/
abbrev p0 : Formula := Formula.atom 0
abbrev p1 : Formula := Formula.atom 1
abbrev p2 : Formula := Formula.atom 2

-- =========================================================================
-- Exemplo 1: α₁ = [p₀, ¬p₁] — disjunção disjunta NÃO-tautológica
-- =========================================================================

def α1 : List Formula := [p0, Formula.not p1]

theorem disjoint_α1 : DisjointDisjunction α1 := by
  show DisjointDisjunction [p0, Formula.not p1]
  rw [DisjointDisjunction, List.pairwise_cons]
  constructor
  · intro ψ hψ
    simp at hψ
    subst hψ
    intro p hp1 hp2
    simp [atoms] at hp1 hp2
    omega
  · exact List.pairwise_cons.mpr ⟨by simp, List.Pairwise.nil⟩

/-- A atribuição `p₁ ↦ verdadeiro, demais ↦ falso` falsifica `⋁̇ α₁`
    (comportamento esperado do lema de totalidade: os contra-exemplos
    individuais unem-se sem conflito, pois os átomos são disjuntos). -/
theorem eval_α1_false : Eval (fun q => decide (q = 1)) (orAll α1) = false := by
  native_decide

/-- E portanto `⋁̇ α₁` não é tautologia. -/
theorem not_tautology_α1 : ¬ Tautology (orAll α1) := fun h => by
  have he := h (fun q => decide (q = 1))
  rw [eval_α1_false] at he
  exact Bool.noConfusion he

-- =========================================================================
-- Exemplo 2: α₂ = [p₀ ∨ p₁, ¬p₂] — disjunção disjunta, não-tautológica
-- =========================================================================

def α2 : List Formula := [Formula.or p0 p1, Formula.not p2]

theorem disjoint_α2 : DisjointDisjunction α2 := by
  show DisjointDisjunction [Formula.or p0 p1, Formula.not p2]
  rw [DisjointDisjunction, List.pairwise_cons]
  constructor
  · intro ψ hψ
    simp at hψ
    subst hψ
    intro p hp1 hp2
    simp [atoms] at hp1 hp2
    omega
  · exact List.pairwise_cons.mpr ⟨by simp, List.Pairwise.nil⟩

theorem eval_α2_false : Eval (fun q => decide (q = 2)) (orAll α2) = false := by
  native_decide

-- =========================================================================
-- Exemplo 3: tautologia e decidibilidade de TAUT
-- =========================================================================

/-- `p₀ ∨ ¬p₀` é tautologia (note: [p₀, ¬p₀] NÃO é disjunção disjunta —
    ambos os disjunctos contêm o átomo 0). -/
theorem taut_p0_or_not : Tautology (Formula.or p0 (Formula.not p0)) := fun v => by
  cases h : v 0 <;> simp [Eval, h]

/-- TAUT é decidível (instância fornecida por `TautologyDecidableAt`). -/
example : Decidable (Tautology (Formula.or p0 (Formula.not p0))) :=
  inferInstance

/-- A checagem finita confirma a tautologia. -/
example : checkTaut (Formula.or p0 (Formula.not p0)) = true := by
  native_decide

/-- E rejeita a não-tautologia `⋁̇ α₁`. -/
example : checkTaut (orAll α1) = false := by
  native_decide

-- =========================================================================
-- Exemplo 4: totalidade — disjunção disjunta COM um disjuncto tautológico
-- =========================================================================

def α3 : List Formula := [Formula.or p0 (Formula.not p0), p1]

theorem disjoint_α3 : DisjointDisjunction α3 := by
  show DisjointDisjunction [Formula.or p0 (Formula.not p0), p1]
  rw [DisjointDisjunction, List.pairwise_cons]
  constructor
  · intro ψ hψ
    simp at hψ
    subst hψ
    intro p hp1 hp2
    simp [atoms] at hp1 hp2
    omega
  · exact List.pairwise_cons.mpr ⟨by simp, List.Pairwise.nil⟩

theorem taut_orAll_α3 : Tautology (orAll α3) := fun v => by
  cases h : v 0 <;> simp [Eval, orAll, α3, h]

/-- Pelo lema de totalidade (contrapositiva), `⋁̇ α₃ ∈ TAUT` força algum
    disjuncto a ser tautologia — aqui o índice 0. -/
theorem exists_taut_α3 : ∃ i, i < α3.length ∧ Tautology (dget α3 i) :=
  dd_totality_contrapositive α3 disjoint_α3 taut_orAll_α3

-- =========================================================================
-- Exemplo 5: sistema de exemplo e protocolo aluno–professor
-- =========================================================================

/-- Sistema de prova "de exemplo": `σ : P ⊢ φ` sse `φ` passa na checagem
    finita de tautologia. É sonoro por construção (via `checkTaut_iff`). -/
def taugP : PropProofSystem :=
  ⟨fun _ φ => checkTaut φ, fun _σ φ h => (checkTaut_iff φ).mp h⟩

/-- Instância de DD_P sobre `taugP`: `π = []`, disjunção `⋁̇ α₃`. -/
def inst3 : DDInstance taugP :=
  ⟨[], α3, disjoint_α3, by native_decide⟩

/-- Pelo teorema de solubilidade em m rodadas (prova completa em DDP.lean),
    o estudante sequencial resolve `inst3` com ≤ 2 rodadas. -/
theorem solves_inst3 : StudentSolves orderStudent 2 α3 :=
  dd_solvable_in_m_rounds taugP inst3

end Experiments
end DDP
end GothicGenerators

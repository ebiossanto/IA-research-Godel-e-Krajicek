import Init

/-! Teste R4 (mapeamento pequalnp): vendorização do núcleo de circuito SEM Mathlib.
Extraído literalmente de open-goat/pequalnp-proofs@89a01cd, lean/PEqualNP/Defs/
CircuitLowerBounds.lean + MetaComplexity.lean (Apache-2.0), apenas o que não
precisa de Mathlib. Ver MAPEAMENTO_DDP_vs_PEqualNP.md §4.4(2) e referee R4. -/

namespace R4Test

inductive GateOp where
  | and
  | or
  | not
  | mod (m : Nat)
  | maj

def GateOp.eval : GateOp → List Bool → Bool
  | GateOp.and, l => l.all id
  | GateOp.or, l => l.any id
  | GateOp.not, l => !(l.headD false)
  | GateOp.mod m, l => (l.count true % m) == 0
  | GateOp.maj, l => decide (l.length ≤ 2 * l.count true)

structure Gate where
  op : GateOp
  inputs : List Nat

structure Circuit where
  gates : List Gate
  output : Nat

def Circuit.wires (C : Circuit) (x : List Bool) : List Bool :=
  C.gates.foldl (fun w g => w ++ [g.op.eval (g.inputs.map fun i => w.getD i false)]) x

def Circuit.eval (C : Circuit) (x : List Bool) : Bool :=
  (C.wires x).getD C.output false

def Circuit.size (C : Circuit) : Nat := C.gates.length

-- ADAPTAÇÃO R4: `Set` não existe em `Init` (é do Mathlib) → disjunção explícita.
-- Equivalente literal de `g.op ∈ ({and, or, not} : Set GateOp) ∧ inputs.length ≤ 2`.
def FanInTwo (C : Circuit) : Prop :=
  ∀ g ∈ C.gates,
    (g.op = GateOp.and ∨ g.op = GateOp.or ∨ g.op = GateOp.not) ∧ g.inputs.length ≤ 2

def HasCircuitSize (n : Nat) (f : (Fin n → Bool) → Bool) (s : Nat) : Prop :=
  ∃ C : Circuit, FanInTwo C ∧ C.size ≤ s ∧ ∀ x : Fin n → Bool, C.eval (List.ofFn x) = f x

-- Sanity: NAND de 2 entradas (2 portões: AND depois NOT; saída = fiação 3).
def nandCircuit : Circuit :=
  { gates := [⟨GateOp.and, [0, 1]⟩, ⟨GateOp.not, [2]⟩], output := 3 }

theorem nand_test : Circuit.eval nandCircuit [true, false] = true := by decide
theorem nand_test2 : Circuit.eval nandCircuit [true, true] = false := by decide

end R4Test

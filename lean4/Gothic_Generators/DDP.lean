import Init

/-!
# DD_P — formalização esqueleto (Krajíček, arXiv:2506.20221v4)

Este módulo formaliza, em Lean 4 (apenas `Init`, sem dependências), o **problema DD_P**
de Jan Krajíček, *On NP∩coNP proof complexity generators* (seção sobre o modelo
aluno–professor e a hipótese (ST)):

* uma **pps** (propositional proof system) no sentido de Cook–Reckhow é uma relação binária
  `P(x, y)` decidível em tempo polinomial tal que `∃x P(x, y)` define TAUT; aqui a modelamos
  como um predicado decidível `Valid : List Formula → Formula → Bool` (o primeiro argumento
  é o código/certificado da prova, abstração de `x`);
* uma **disjunção disjunta** `⋁̇_{i<m} α_i` é uma lista de fórmulas em que nenhum par
  compartilha átomo;
* o problema de busca **DD_P**: entrada `(π, ⋁̇_i α_i)` com `π : P ⊢ ⋁̇_i α_i`; saída: um
  índice `i` com `α_i ∈ TAUT`;
* o **lema de totalidade** (demonstrado aqui integralmente): se nenhum `α_i` é tautologia,
  escolhendo para cada `i` uma atribuição falsificante `v_i` e unindo-as (possível pela
  disjunção de átomos — sem conflito), falsifica-se a disjunção inteira; logo, sob
  sonoridade de `P`, toda entrada de DD_P tem solução.

NOTAÇÃO: como `List.get` do Lean 4 exige um índice `Fin l.length`, usamos o acesso total
`dget α i` (definido abaixo), que satisfaz `dget α i = α.get ⟨i, h⟩` para `i < α.length` —
a tradução fiel de `α.get i` nos enunciados de [Krajíček].

**O que este arquivo NÃO captura** (ver `krajicek_ddp/B_lean_relatorio.md`): limites de
tempo polinomiais ("p-time", "O(1) rodadas", p-boundedness) são enunciados de
meta-teoria/complexidade sobre *implementações*; não são expressíveis de forma não-trivial
dentro de um sistema de prova como Lean. Eles aparecem aqui como *predicados sobre
estruturas* com hipóteses explícitas, e as partes genuinamente abertas (a hipótese (ST),
o Problema 2.1, a questão `DD_P ∈ ST[P, O(1)]`) ficam como `sorry` intencionais, com a
estratégia nos comentários.

CONVENÇÃO (regras da equipe): **(A)** = extraído do artigo; **(B)** = demonstração própria
(aqui: tudo que está provado); **(C)** = conjectura/esboço.
-/

namespace GothicGenerators
namespace DDP

-- =========================================================================
-- (A) Fórmulas proposicionais
-- =========================================================================

/-- Fórmulas proposicionais sobre variáveis numeradas (`atom p` = proposicional `x_p`).
    `imp`, `and`, `or`, `not` são conectivos; `bot`/`top` são as constantes. -/
inductive Formula where
  | atom : Nat → Formula
  | bot : Formula
  | top : Formula
  | imp : Formula → Formula → Formula
  | and : Formula → Formula → Formula
  | or : Formula → Formula → Formula
  | not : Formula → Formula
  deriving DecidableEq

/-- Lista dos átomos (variáveis proposicionais) de uma fórmula
    (com eventuais repetições — irrelevante para as propriedades usadas). -/
def atoms : Formula → List Nat
  | Formula.atom p => [p]
  | Formula.bot => []
  | Formula.top => []
  | Formula.imp φ ψ => atoms φ ++ atoms ψ
  | Formula.and φ ψ => atoms φ ++ atoms ψ
  | Formula.or φ ψ => atoms φ ++ atoms ψ
  | Formula.not φ => atoms φ

/-- Tamanho sintático (número de nós) de uma fórmula — usado nas versões
    p-limitadas da propriedade de disjunção viável. -/
def size : Formula → Nat
  | Formula.atom _ => 1
  | Formula.bot => 1
  | Formula.top => 1
  | Formula.imp φ ψ => 1 + size φ + size ψ
  | Formula.and φ ψ => 1 + size φ + size ψ
  | Formula.or φ ψ => 1 + size φ + size ψ
  | Formula.not φ => 1 + size φ

/-- Fórmulas cujos átomos são mutuamente disjuntos. -/
def DisjointAtoms (φ ψ : Formula) : Prop :=
  ∀ p, p ∈ atoms φ → p ∈ atoms ψ → False

/-- Simetria de `DisjointAtoms`. -/
theorem DisjointAtoms.symm {φ ψ : Formula} (h : DisjointAtoms φ ψ) :
    DisjointAtoms ψ φ :=
  fun p hψ hφ => h p hφ hψ

/-- **(A) Disjunção disjunta** `⋁̇_i α_i` (Krajíček, §2): nenhum par `α_i, α_j`
    (`i ≠ j`) compartilha átomo. Formalizado com `List.Pairwise`. -/
def DisjointDisjunction (fs : List Formula) : Prop :=
  List.Pairwise (fun φ ψ => DisjointAtoms φ ψ) fs

/-- Disjunção de uma lista é `φ₁ ∨ (φ₂ ∨ (… ∨ ⊥))`; `orAll [] = ⊥`. -/
def orAll : List Formula → Formula
  | [] => Formula.bot
  | φ :: fs => Formula.or φ (orAll fs)

@[simp] theorem orAll_nil : orAll ([] : List Formula) = Formula.bot := rfl
@[simp] theorem orAll_cons (φ : Formula) (fs : List Formula) :
    orAll (φ :: fs) = Formula.or φ (orAll fs) := rfl

/-- Acesso `i`-ésimo de uma lista de fórmulas (total; `⊥` fora do domínio).
    `dget α i` desempenha o papel de `α.get i` dos enunciados de Krajíček
    (o `List.get` do Lean 4 exige `Fin α.length`). -/
def dget (α : List Formula) (i : Nat) : Formula :=
  if h : i < α.length then α.get ⟨i, h⟩ else Formula.bot

/-- **(B)** `dget` coincide com `List.get` no domínio válido. -/
theorem dget_eq (α : List Formula) (i : Nat) (h : i < α.length) :
    dget α i = α.get ⟨i, h⟩ := by
  simp [dget, h]

-- =========================================================================
-- (A) Semântica
-- =========================================================================

/-- Valoração (atribuição de verdade) das variáveis proposicionais. -/
abbrev Valuation := Nat → Bool

/-- Avaliação semântica de uma fórmula sob uma valoração. -/
def Eval (v : Valuation) : Formula → Bool
  | Formula.atom p => v p
  | Formula.bot => false
  | Formula.top => true
  | Formula.imp φ ψ => !(Eval v φ) || Eval v ψ
  | Formula.and φ ψ => Eval v φ && Eval v ψ
  | Formula.or φ ψ => Eval v φ || Eval v ψ
  | Formula.not φ => !(Eval v φ)

/-- **(A) TAUT**: `φ` é tautologia sse toda valoração a faz verdadeira. -/
def Tautology (φ : Formula) : Prop := ∀ v : Valuation, Eval v φ = true

@[simp] theorem eval_orAll_nil (v : Valuation) :
    Eval v (orAll ([] : List Formula)) = false := rfl
@[simp] theorem eval_orAll_cons (v : Valuation) (φ : Formula) (fs : List Formula) :
    Eval v (orAll (φ :: fs)) = (Eval v φ || Eval v (orAll fs)) := rfl

-- ---------------------------------------------------------------------------
-- Congruência de avaliação (lema auxiliar central)
-- ---------------------------------------------------------------------------

/-- **(B) Lema auxiliar**: se `v` e `w` concordam nos átomos de `φ`, então
    `Eval v φ = Eval w φ`. É o que permite "embutir" uma atribuição parcial
    numa global sem alterar o valor de `φ`. -/
theorem eval_congr :
    ∀ (φ : Formula) (v w : Valuation),
      (∀ p, p ∈ atoms φ → v p = w p) →
      Eval v φ = Eval w φ := by
  intro φ
  induction φ with
  | atom p =>
    intro v w h
    simp only [Eval]
    exact h p (by simp [atoms])
  | bot =>
    intro v w _h
    rfl
  | top =>
    intro v w _h
    rfl
  | not φ ih =>
    intro v w h
    simp only [Eval, atoms] at h ⊢
    rw [ih v w h]
  | imp φ ψ ihφ ihψ =>
    intro v w h
    simp only [Eval, atoms, List.mem_append] at h ⊢
    rw [ihφ v w (fun p hp => h p (Or.inl hp)),
        ihψ v w (fun p hp => h p (Or.inr hp))]
  | and φ ψ ihφ ihψ =>
    intro v w h
    simp only [Eval, atoms, List.mem_append] at h ⊢
    rw [ihφ v w (fun p hp => h p (Or.inl hp)),
        ihψ v w (fun p hp => h p (Or.inr hp))]
  | or φ ψ ihφ ihψ =>
    intro v w h
    simp only [Eval, atoms, List.mem_append] at h ⊢
    rw [ihφ v w (fun p hp => h p (Or.inl hp)),
        ihψ v w (fun p hp => h p (Or.inr hp))]

-- ---------------------------------------------------------------------------
-- Decidibilidade de TAUT sobre fórmulas proposicionais
-- ---------------------------------------------------------------------------

/-- **(B)** Enumeração das valorações com suporte finito em `ps`
    (para `ps = []`, a valoração nula). -/
def valuations : List Nat → List Valuation
  | [] => [fun _ => false]
  | p :: ps =>
      (valuations ps).flatMap fun v =>
        [(fun q => if q = p then true else v q),
         (fun q => if q = p then false else v q)]

/-- **(B) Lema auxiliar**: toda valoração `v` concorda com alguma valoração
    enumerada de `valuations ps`, em todos os pontos de `ps`. -/
theorem exists_agree (ps : List Nat) (v : Valuation) :
    ∃ w ∈ valuations ps, ∀ p ∈ ps, w p = v p := by
  induction ps with
  | nil =>
    exact ⟨fun _ => false, by simp [valuations], fun p hp => absurd hp (by simp)⟩
  | cons p ps ih =>
    obtain ⟨w0, hw0, hagree0⟩ := ih
    cases hv : v p with
    | true =>
      refine ⟨(fun q => if q = p then true else w0 q), ?_, ?_⟩
      · simp only [valuations, List.mem_flatMap]
        exact ⟨w0, hw0, by simp⟩
      · intro q hq
        cases List.mem_cons.mp hq with
        | inl heq =>
          subst heq
          simp [hv]
        | inr himem =>
          by_cases hqp : q = p
          · subst hqp
            simp [hv]
          · have hred : (fun r => if r = p then true else w0 r) q = w0 q := by
              simp [hqp]
            rw [hred]
            exact hagree0 q himem
    | false =>
      refine ⟨(fun q => if q = p then false else w0 q), ?_, ?_⟩
      · simp only [valuations, List.mem_flatMap]
        exact ⟨w0, hw0, by simp⟩
      · intro q hq
        cases List.mem_cons.mp hq with
        | inl heq =>
          subst heq
          simp [hv]
        | inr himem =>
          by_cases hqp : q = p
          · subst hqp
            simp [hv]
          · have hred : (fun r => if r = p then false else w0 r) q = w0 q := by
              simp [hqp]
            rw [hred]
            exact hagree0 q himem

/-- **(B)** Checagem efetiva de tautologia: avalia `φ` em todas as valorações
    com suporte nos átomos de `φ`. -/
def checkTaut (φ : Formula) : Bool :=
  (valuations (atoms φ)).all fun v => decide (Eval v φ = true)

/-- **(B)** A checagem finita decide `Tautology`. -/
theorem checkTaut_iff (φ : Formula) : checkTaut φ = true ↔ Tautology φ := by
  constructor
  · intro h v
    obtain ⟨w, hwmem, hagree⟩ := exists_agree (atoms φ) v
    have hweval : Eval w φ = Eval v φ :=
      eval_congr φ w v (fun p hp => hagree p hp)
    have hwall : Eval w φ = true :=
      of_decide_eq_true ((List.all_eq_true.mp h) w hwmem)
    rw [← hweval]
    exact hwall
  · intro h
    unfold checkTaut
    rw [List.all_eq_true]
    intro w _hw
    exact decide_eq_true (h w)

/-- **(B) TautologyDecidableAt**: TAUT é decidível para fórmulas proposicionais
    (óbvia matematicamente, mas necessária para que os `if ht : Tautology …`
    do modelo aluno–professor sejam efetivos). -/
def TautologyDecidableAt (φ : Formula) : Decidable (Tautology φ) := by
  by_cases h : checkTaut φ = true
  · exact isTrue ((checkTaut_iff φ).mp h)
  · exact isFalse (fun ht => h ((checkTaut_iff φ).mpr ht))

instance tautologyDecidable (φ : Formula) : Decidable (Tautology φ) :=
  TautologyDecidableAt φ

-- =========================================================================
-- (A) Sistema de prova (Cook–Reckhow) e sonoridade
-- =========================================================================

/-- **(A) pps** no sentido de Cook–Reckhow: a relação `P(x, y)` é *decidível em
    tempo polinomial* e `∃x P(x, y)` define TAUT. Modelamos a decisão da
    relação pelo predicado booleano `Valid σ φ` ("`σ` é um código de prova de
    `φ` em `P`"), e registramos a **sonoridade** como axiomática da estrutura.

    Justificativa da modelagem (escolha pedida pela missão): o artigo usa a
    relação binária de Cook–Reckhow; um `Bool` é a característica decidível de
    uma relação. O vínculo `∃σ, Valid σ φ = true ↔ Tautology φ` se decomponde em
    (i) sonoridade, abaixo, e (ii) completude/sobrejetividade, propriedade do
    sistema concreto, deixada como hipótese quando necessária.

    O "tempo polinomial" de `Valid` é **estatístico** (sobre máquinas de Turing
    / circuitos) e não é formalizável dentro do próprio sistema — ver relatório. -/
structure PropProofSystem where
  /-- Código de prova de `φ` em `P` (abstração de `x` em `P(x, y)`). -/
  Valid : List Formula → Formula → Bool
  /-- **(A) Sonoridade** (Cook–Reckhow): prova ⇒ tautologia. -/
  sound : ∀ (σ : List Formula) (φ : Formula), Valid σ φ = true → Tautology φ

/-- **(B) Corolário operacional** da sonoridade: `σ : P ⊢ φ` implica `φ ∈ TAUT`. -/
theorem valid_implies_tautology (P : PropProofSystem)
    (σ : List Formula) (φ : Formula) (hσ : P.Valid σ φ = true) : Tautology φ :=
  P.sound σ φ hσ

-- =========================================================================
-- (A) O problema DD_P — entrada e tarefa
-- =========================================================================

/-- **(A) Entrada de DD_P**: um código `π` de prova em `P` de uma disjunção
    disjunta `⋁̇_{i<m} α_i`. (A teoria implícita do sistema é embutida em `P`;
    axiomas extras exigiriam hipótese de satisfatibilidade — ver relatório.) -/
structure DDInstance (P : PropProofSystem) where
  /-- Código da prova `π`. -/
  pi : List Formula
  /-- Disjunctos `α_0, …, α_{m-1}`. -/
  alpha : List Formula
  /-- `⋁̇_i α_i` é disjunção disjunta. -/
  disj : DisjointDisjunction alpha
  /-- `π : P ⊢ ⋁̇_i α_i`. -/
  proof : P.Valid pi (orAll alpha) = true

/-- **(A) Tarefa de busca DD_P**: encontrar `i < |α|` com `α_i ∈ TAUT`. -/
def DDTask (P : PropProofSystem) (inst : DDInstance P) : Prop :=
  ∃ i, i < inst.alpha.length ∧ Tautology (dget inst.alpha i)

-- =========================================================================
-- (B) LEMA DE TOTALIDADE — o núcleo, provado integralmente
-- =========================================================================
--
-- Ideia (extraída de [Krajíček, §2/§3] e aqui realizada passo a passo):
-- se cada `α_i` não é tautologia, escolhe-se `v_i` com `Eval v_{i} α_i = false`;
-- pela disjunção de átomos, `v := ⋃ v_i` (restrita aos átomos de `α_i` vale `v_i`,
-- fora dela vale a união recursiva das demais) é **consistente** e **total**, e
-- falsifica `⋁̇ α_i` — contradizendo a sonoridade de `P`.

/-- **(B) Lema auxiliar**: toda fórmula não-tautológica tem valoração falsificante. -/
theorem exists_falsifier (φ : Formula) (h : ¬ Tautology φ) : ∃ v, Eval v φ = false := by
  apply Classical.byContradiction
  intro hnc
  apply h
  intro v
  cases hv : Eval v φ with
  | true => rfl
  | false => exact absurd ⟨v, hv⟩ hnc

/-- **(B)** Valoração falsificante escolhida (não construtiva; a *existência*
    basta para o argumento meta-teórico). -/
noncomputable def falsifier (φ : Formula) (h : ¬ Tautology φ) : Valuation :=
  Exists.choose (exists_falsifier φ h)

/-- **(B) União de valorações**: em `s` vale `v1`, fora de `s` vale `v2`.
    Total por construção; a consistência (ausência de conflito) é fornecida
    pela disjunção de átomos nos lemas abaixo. -/
def unionVal (s : List Nat) (v1 v2 : Valuation) : Valuation :=
  fun p => if p ∈ s then v1 p else v2 p

@[simp] theorem unionVal_mem (s : List Nat) (v1 v2 : Valuation) (p : Nat)
    (hp : p ∈ s) : unionVal s v1 v2 p = v1 p := by
  simp [unionVal, hp]

@[simp] theorem unionVal_not_mem (s : List Nat) (v1 v2 : Valuation) (p : Nat)
    (hp : p ∉ s) : unionVal s v1 v2 p = v2 p := by
  simp [unionVal, hp]

/-- **(B) Lema auxiliar**: duas valorações que concordam em todos os disjunctos
    avaliam `orAll` igualmente. -/
theorem eval_orAll_congr (fs : List Formula) (v w : Valuation)
    (h : ∀ ψ ∈ fs, Eval v ψ = Eval w ψ) :
    Eval v (orAll fs) = Eval w (orAll fs) := by
  induction fs with
  | nil => rfl
  | cons ψ gs ih =>
    rw [eval_orAll_cons, eval_orAll_cons,
        h ψ (List.mem_cons_self),
        ih (fun g hg => h g (List.mem_cons_of_mem ψ hg))]

/-- **(B) LEMA DE TOTALIDADE (forma construtiva)**: sob disjunção disjunta,
    se nenhum disjuncto é tautologia, existe valoração que falsifica a
    disjunção inteira. A valoração é a união das falsificantes individuais. -/
theorem dd_counterexample_exists :
    ∀ (α : List Formula),
      DisjointDisjunction α →
      (∀ i, i < α.length → ¬ Tautology (dget α i)) →
      ∃ v, Eval v (orAll α) = false := by
  intro α
  induction α with
  | nil =>
    intro _hdisj _hnt
    exact ⟨fun _ => false, rfl⟩
  | cons φ fs ih =>
    intro hdisj hnt
    -- desdobramento da disjunção disjunta
    obtain ⟨hφfs, hpair⟩ := List.pairwise_cons.mp hdisj
    -- o disjuncto φ (índice 0) não é tautologia
    have h0 : (0 : Nat) < (φ :: fs).length := Nat.zero_lt_succ fs.length
    have hg0 : dget (φ :: fs) 0 = φ := by
      rw [dget_eq (φ :: fs) 0 h0]
      exact List.get_cons_zero
    have hφ : ¬ Tautology φ := by
      intro ht
      rw [← hg0] at ht
      exact hnt 0 h0 ht
    -- a cauda também é disjunção disjunta sem disjunctos tautológicos
    have hfs : ∀ i, i < fs.length → ¬ Tautology (dget fs i) := by
      intro i hi
      have hlt : i + 1 < (φ :: fs).length := by
        rw [List.length_cons]
        omega
      have hgeti : dget fs i = dget (φ :: fs) (i + 1) := by
        rw [dget_eq fs i hi, dget_eq (φ :: fs) (i + 1) hlt]
        simp
      rw [hgeti]
      exact hnt (i + 1) hlt
    obtain ⟨vfs, hvfs⟩ := ih hpair hfs
    -- falsificante do disjuncto de cabeça
    obtain ⟨vφ, hvφ⟩ := exists_falsifier φ hφ
    -- união das valorações (consistente pela disjunção de átomos)
    let u : Valuation := unionVal (atoms φ) vφ vfs
    have hφu : Eval u φ = false := by
      rw [eval_congr φ u vφ (fun p hp => unionVal_mem (atoms φ) vφ vfs p hp), hvφ]
    have hall : ∀ ψ ∈ fs, Eval u ψ = Eval vfs ψ := by
      intro ψ hψ
      apply eval_congr ψ u vfs
      intro p hp
      apply unionVal_not_mem (atoms φ) vφ vfs p
      intro hpd
      exact hφfs ψ hψ p hpd hp
    have hfinal : Eval u (orAll (φ :: fs)) = false := by
      rw [eval_orAll_cons]
      rw [hφu]
      rw [eval_orAll_congr fs u vfs hall]
      rw [hvfs]
      exact Bool.or_false false
    exact ⟨u, hfinal⟩

/-- **(B) LEMA DE TOTALIDADE (forma pedida)**: se `⋁̇ α_i` tem disjunctos todos
    não-tautológicos (e os átomos são disjuntos), então `⋁̇ α_i` não é tautologia. -/
theorem dd_totality (α : List Formula) (hdisj : DisjointDisjunction α)
    (h : ¬ ∃ i, i < α.length ∧ Tautology (dget α i)) :
    ¬ Tautology (orAll α) := by
  intro htaut
  obtain ⟨v, hv⟩ :=
    dd_counterexample_exists α hdisj (fun i hi ht => h ⟨i, hi, ht⟩)
  exact Bool.noConfusion (Eq.trans (Eq.symm (htaut v)) hv)

/-- **(B) Contrapositiva de dd_totality** — o "totality argument" de
    [Krajíček, §2/§3]: numa disjunção disjunta *provada* num sistema sonoro,
    algum disjuncto é tautologia. -/
theorem dd_totality_contrapositive (α : List Formula)
    (hdisj : DisjointDisjunction α) (htaut : Tautology (orAll α)) :
    ∃ i, i < α.length ∧ Tautology (dget α i) := by
  apply Classical.byContradiction
  intro hnt
  obtain ⟨v, hv⟩ :=
    dd_counterexample_exists α hdisj (fun i hi ht => hnt ⟨i, hi, ht⟩)
  exact Bool.noConfusion (Eq.trans (Eq.symm (htaut v)) hv)

/-- **(B) Totalidade da tarefa DD_P**: toda entrada de DD_P tem solução —
    usa sonoridade de `P` + lema de totalidade. Este é o conteúdo verificável
    de "DD_P é um problema de busca *total*" (o "Σ₂ᵖ-total" é meta-teoria). -/
theorem dd_task_total (P : PropProofSystem) (inst : DDInstance P) :
    DDTask P inst :=
  dd_totality_contrapositive inst.alpha inst.disj
    (P.sound inst.pi (orAll inst.alpha) inst.proof)

-- =========================================================================
-- (A) Modelo aluno–professor (Krajíček–Pudlák–Sgall; ST[F, t(n)])
-- =========================================================================
--
-- Protocolo: S recebe a entrada e propõe índice i₁; se α_{i₁} ∈ TAUT, T aceita
-- e a computação termina; senão T envia um contra-exemplo (valoração que
-- falsifica α_{i₁}) e S propõe i₂ usando o histórico, etc.
-- `ST[F, t(n)]`: problemas de busca totais solúveis em t(n) rodadas com
-- estudante cujos movimentos são computados por F (T arbitrário).

/-- **(A) Aluno (estudante)**: dado o número da rodada e o histórico de
    pares (índice proposto, contra-exemplo recebido), produz o próximo índice.
    A *correção dos movimentos* (F = p-time) é meta-teórica; modelamos só a
    função. -/
structure Student where
  propose : Nat → List (Nat × Valuation) → Nat

/-- **(A)** Estudante "sequencial": propõe 0, 1, 2, … (ignora o histórico). -/
def orderStudent : Student := ⟨fun n _ => n⟩

/-- **(A) Professor honesto**: para proposta `i < |α|`, aceita (`none`) sse
    `α_i ∈ TAUT`; caso contrário envia um contra-exemplo. Propostas fora do
    domínio são rejeitadas com contra-exemplo sentinela. -/
noncomputable def professor (α : List Formula) (i : Nat) : Option Valuation :=
  if _hi : i < α.length then
    if ht : Tautology (dget α i) then none
    else some (falsifier (dget α i) ht)
  else some (fun _ => false)

/-- **(B)** Caracterização do professor honesto. -/
theorem professor_none_iff (α : List Formula) (i : Nat) :
    professor α i = none ↔ i < α.length ∧ Tautology (dget α i) := by
  unfold professor
  by_cases hi : i < α.length
  · by_cases ht : Tautology (dget α i)
    · simp [hi, ht]
    · simp [hi, ht]
  · simp [hi]

/-- **(A) Execução do diálogo** por `n` rodadas, com histórico `hist`.
    Devolve `some i` se o professor aceitou em alguma rodada, `none` caso
    contrário (rodadas esgotadas com rejeição). -/
noncomputable def play (s : Student) (α : List Formula) :
    Nat → List (Nat × Valuation) → Option Nat
  | 0, _ => none
  | n + 1, hist =>
    match professor α (s.propose n hist) with
    | none => some (s.propose n hist)
    | some v => play s α n ((s.propose n hist, v) :: hist)

@[simp] theorem play_zero (s : Student) (α : List Formula)
    (hist : List (Nat × Valuation)) : play s α 0 hist = none := rfl

theorem play_succ (s : Student) (α : List Formula) (n : Nat)
    (hist : List (Nat × Valuation)) :
    play s α (n + 1) hist =
      match professor α (s.propose n hist) with
      | none => some (s.propose n hist)
      | some v => play s α n ((s.propose n hist, v) :: hist) := rfl

theorem play_order_succ (α : List Formula) (n : Nat)
    (hist : List (Nat × Valuation)) :
    play orderStudent α (n + 1) hist =
      match professor α n with
      | none => some n
      | some v => play orderStudent α n ((n, v) :: hist) := rfl

/-- **(B) Correção do protocolo**: qualquer aceitação do professor ocorre num
    índice corretamente tautológico (o professor é honesto por construção). -/
theorem play_correct (s : Student) (α : List Formula) :
    ∀ (n : Nat) (hist : List (Nat × Valuation)) (i : Nat),
      play s α n hist = some i →
      i < α.length ∧ Tautology (dget α i) := by
  intro n
  induction n with
  | zero =>
    intro hist i h
    rw [play_zero] at h
    exact absurd h (by intro h2; cases h2)
  | succ n ih =>
    intro hist i h
    rw [play_succ] at h
    cases hp : professor α (s.propose n hist) with
    | none =>
      have hj := (professor_none_iff α (s.propose n hist)).mp hp
      simp only [hp] at h
      have hiej : s.propose n hist = i := Option.some.inj h
      rw [← hiej]
      exact hj
    | some v =>
      simp only [hp] at h
      exact ih ((s.propose n hist, v) :: hist) i h

/-- **(B)** Se o estudante sequencial esgota `n` rodadas sem aceitação, então
    nenhum disjuncto de índice `< n` é tautologia (e todos estão no domínio). -/
theorem order_none_implies (α : List Formula) :
    ∀ (n : Nat) (hist : List (Nat × Valuation)),
      play orderStudent α n hist = none →
      ∀ j, j < n → j < α.length → ¬ Tautology (dget α j) := by
  intro n
  induction n with
  | zero =>
    intro hist h j hj _hjl
    omega
  | succ n ih =>
    intro hist h j hj
    rw [play_order_succ] at h
    cases hp : professor α n with
    | none =>
      simp only [hp] at h
      exact absurd h (by intro h2; cases h2)
    | some v =>
      simp only [hp] at h
      intro hjl htau
      have hnn : ¬ (n < α.length ∧ Tautology (dget α n)) := fun hcon => by
        rw [(professor_none_iff α n).mpr hcon] at hp
        cases hp
      by_cases hjeq : j = n
      · subst hjeq
        exact hnn ⟨hjl, htau⟩
      · exact (ih ((n, v) :: hist) h j (by omega) hjl) htau

/-- **(A)** O estudante `s` resolve a entrada `α` em `k` rodadas: o diálogo
    aceita, em algum índice corretamente tautológico. -/
def StudentSolves (s : Student) (k : Nat) (α : List Formula) : Prop :=
  ∃ i, play s α k [] = some i ∧ i < α.length ∧ Tautology (dget α i)

/-- **(A) DDFeasibleInST**: esqueleto de `DD_P ∈ ST[P, budget]` — existe um
    estudante cujos movimentos são dados por `Student` (o "F p-time" é
    meta-teórico) que resolve toda entrada de DD_P em `budget m` rodadas,
    para `m` = número de disjunctos. -/
def DDFeasibleInST (P : PropProofSystem) (budget : Nat → Nat) : Prop :=
  ∃ s : Student, ∀ (inst : DDInstance P),
    StudentSolves s (budget inst.alpha.length) inst.alpha

/-- **(B) DD_P ∈ ST[P, m]** com `m` = nº de disjunctos: o estudante sequencial,
    com um professor honesto (o caso melhor para S; professor arbitrário só
    ajuda), acha um disjuncto tautológico em ≤ m rodadas. Este é o resultado
    que o artigo usa como "DD_P é soluvel no modelo S-T" — note que `m` é
    *polinomial*, mas **não constante**. -/
theorem dd_solvable_in_m_rounds (P : PropProofSystem)
    (inst : DDInstance P) :
    StudentSolves orderStudent inst.alpha.length inst.alpha := by
  obtain ⟨i0, hi0, ht0⟩ := dd_task_total P inst
  by_cases hplay : play orderStudent inst.alpha inst.alpha.length [] = none
  · exfalso
    have hnone :=
      order_none_implies inst.alpha inst.alpha.length [] hplay
    exact (hnone i0 hi0 hi0) ht0
  · cases h : play orderStudent inst.alpha inst.alpha.length [] with
    | none => exact absurd h hplay
    | some i =>
      exact ⟨i, h, play_correct orderStudent inst.alpha _ [] i h⟩

/-- **(B)** Corolário: `DD_P` é soluvel em `m` rodadas no modelo S-T
    (orçamento linear no nº de disjunctos). -/
theorem dd_feasible_in_ST_linear (P : PropProofSystem) :
    DDFeasibleInST P (fun m => m) :=
  ⟨orderStudent, fun inst => dd_solvable_in_m_rounds P inst⟩

/-- **(C) ABERTO / HIPÓTESE (ST)**: `DD_P` soluvel em O(1) rodadas para todo
    strong pps é exatamente o que a hipótese (ST) de Krajíček postula ser
    **falso** (o artigo aposta que falha para todo strong pps — equivalente a
    valer para EF). Este `sorry` é intencional e **não deve ser removido**:
    provar (ou refutar) aqui equivaleria a decidir a hipótese (ST) — questão
    meta-teórica aberta. -/
theorem dd_solvable_in_ST_O1 (P : PropProofSystem) :
    DDFeasibleInST P (fun _ => 1) := by
  sorry

-- =========================================================================
-- (A) Disjunção viável (feasible disjunction property)
-- =========================================================================

/-- **(A) p-boundedness** (Krajíček): existe `c` tal que toda tautologia `β`
    tem P-prova de tamanho `≤ |β|^c`. Propriedade de *implementação* de `P`
    (meta-teórica); aqui é hipótese explícita. -/
def PBounded (P : PropProofSystem) (c : Nat) : Prop :=
  ∀ β : Formula, Tautology β →
    ∃ σ : List Formula, P.Valid σ β = true ∧ σ.length ≤ (size β) ^ c

/-- **(A) Feasible disjunction property** (forma índice): de uma prova de
    `⋁̇ α_i`, acha-se (em tempo p — extra-estatístico) o índice `i` com
    `α_i ∈ TAUT`. -/
def FeasibleDisjunction (P : PropProofSystem) : Prop :=
  ∃ find : List Formula → List Formula → Nat,
    ∀ (π α : List Formula),
      DisjointDisjunction α →
      P.Valid π (orAll α) = true →
      find π α < α.length ∧ Tautology (dget α (find π α))

/-- **(A) Strong feasible disjunction property**: de uma prova de `⋁̇ α_i`,
    acha-se uma P-prova de algum disjuncto tautológico, com tamanho limitado
    polinomialmente (exponente `c`). O artigo observa que esta propriedade
    **falha** para strong proof systems (sob Problema 2.1 afirmativo + (ST)). -/
def StrongFeasibleDisjunction (P : PropProofSystem) (c : Nat) : Prop :=
  ∃ find : List Formula → List Formula → List Formula,
    ∀ (π α : List Formula),
      DisjointDisjunction α →
      P.Valid π (orAll α) = true →
      ∃ i, i < α.length ∧
        P.Valid (find π α) (dget α i) = true ∧
        (find π α).length ≤ (size (dget α i)) ^ c

/-- **(B) Núcleo CORRETO** de `PBounded ⟹ FeasibleDisjunction`: a *especificação*
    (existência de `i` e de certificado curto) é provável; o que não é
    formalizável é o limite de tempo da busca. -/
theorem pbounded_spec (P : PropProofSystem) (c : Nat) (hpb : PBounded P c)
    (α : List Formula) (hdisj : DisjointDisjunction α)
    (π : List Formula) (hπ : P.Valid π (orAll α) = true) :
    ∃ i σ, i < α.length ∧ P.Valid σ (dget α i) = true ∧
      σ.length ≤ (size (dget α i)) ^ c := by
  obtain ⟨i, hi, hti⟩ :=
    dd_totality_contrapositive α hdisj (P.sound π (orAll α) hπ)
  obtain ⟨σ, hvalid, hlen⟩ := hpb (dget α i) hti
  exact ⟨i, σ, hi, hvalid, hlen⟩

/-- **(C) ABERTO quanto à formalização**: `PBounded c ⟹ FeasibleDisjunction`.
    Estratégia da prova (não formalizável em Lean por limites de tempo):
    1. `find π α` enumera, em ordem, todos os pares `(i, σ)` com `i < |α|` e
       `|σ| ≤ (max_j |α_j|)^c`, testando `P.Valid σ (α_i) = true` (decidível!);
    2. a busca é finita e pula corretamente — correção *semântica* garantida
       por `pbounded_spec` (existe par aceito);
    3. o tempo é polinomial na entrada porque o comprimento do certificado é
       limitado por potência do tamanho da fórmula e o número de candidatos é
       polinomial.
    As partes 2 e 3 exigem máquina de Turing / circuitos, i.e., meta-teoria
    fora do escopo de Lean; a parte semântica já está em `pbounded_spec`. -/
theorem pbounded_implies_feasible (P : PropProofSystem) (c : Nat)
    (hpb : PBounded P c) : FeasibleDisjunction P := by
  sorry

end DDP
end GothicGenerators

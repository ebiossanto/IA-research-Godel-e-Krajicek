import Init

/-!
PR15/PR18/PR21/PR22/PR24 — Formalização Lean 4
STATUS: delta_mono, theorem4_strict, rcs_exists PROVADOS;
lemma3_con PROVADO da interface Foundation (Lemma3Hyp);
generalização (C): allCovered/maxKappa.
-/

namespace GothicGenerators

abbrev Budget := Nat → Nat

structure Obligation where
  idx : String
  kappa : Nat
  isTrue : Bool
  deriving DecidableEq

structure Theory where
  name : String
  sigma : Nat
  deriving DecidableEq

def covered (T : Theory) (b : Nat) (o : Obligation) : Bool :=
  decide (o.isTrue ∧ o.kappa ≤ T.sigma ∧ o.kappa + 1 ≤ b)

def truesOf (W : List Obligation) : List Obligation := W.filter (·.isTrue)

def covOf (T : Theory) (b : Nat) (W : List Obligation) : List Obligation :=
  (truesOf W).filter (covered T b)

def delta (T : Theory) (b : Nat) (W : List Obligation) : Nat :=
  (truesOf W).length - (covOf T b W).length

def sigmaFast (α : Nat) (fastStep : Nat) : Nat := fastStep * α
def sigmaSlow (α : Nat) (_slowStep : Nat) : Nat := α

-- =========================================================================
-- delta_mono (PR18)
-- =========================================================================

theorem covered_mono
    {T S : Theory} {b : Nat} {o : Obligation}
    (hσ : T.sigma ≤ S.sigma)
    (hc : covered T b o = true) :
    covered S b o = true := by
  unfold covered at hc ⊢
  simp only [decide_eq_true_iff] at hc ⊢
  obtain ⟨h1, h2, h3⟩ := hc
  exact ⟨h1, Nat.le_trans h2 hσ, h3⟩

theorem length_filter_mono
    {α : Type} {p q : α → Bool} {L : List α}
    (h : ∀ x ∈ L, p x = true → q x = true) :
    (L.filter p).length ≤ (L.filter q).length := by
  induction L with
  | nil => simp
  | cons a as ih =>
    by_cases hp : p a = true
    · have hq : q a = true := h a (List.mem_cons_self) hp
      rw [List.filter_cons_of_pos hp, List.filter_cons_of_pos hq]
      simp only [List.length_cons]
      exact Nat.succ_le_succ (ih fun x hx hxp => h x (List.mem_cons_of_mem a hx) hxp)
    · rw [List.filter_cons_of_neg (by
        intro hpa
        exact hp (by simpa using hpa))]
      by_cases hq : q a = true
      · rw [List.filter_cons_of_pos hq]
        simp only [List.length_cons]
        have ih' := ih fun x hx hxp => h x (List.mem_cons_of_mem a hx) hxp
        exact Nat.le_trans ih' (Nat.le_succ _)
      · rw [List.filter_cons_of_neg (by
          intro hqa
          exact hq (by simpa using hqa))]
        exact ih fun x hx hxp => h x (List.mem_cons_of_mem a hx) hxp

theorem delta_mono
    (T S : Theory) (b : Nat) (W : List Obligation)
    (h : T.sigma ≤ S.sigma) :
    delta S b W ≤ delta T b W := by
  unfold delta truesOf covOf
  have hmono : ∀ x ∈ W.filter (·.isTrue),
      covered T b x = true → covered S b x = true := by
    intro x _ hx
    exact covered_mono h hx
  have hlen : ((W.filter (·.isTrue)).filter (covered T b)).length ≤
              ((W.filter (·.isTrue)).filter (covered S b)).length :=
    length_filter_mono hmono
  exact Nat.sub_le_sub_left hlen (W.filter (·.isTrue)).length

-- =========================================================================
-- lemma3_con (PR24): interface Foundation → prova da equivalência
-- =========================================================================
--
-- Lema 3 (09 §12): Φ_T^{w*} ↔ Con(T).
-- Em integração completa com Foundation (Saitou–Noguchi), as hipóteses
-- abaixo seriam DERIVADAS de Prf / pad-Prf / aritmética.
-- Aqui: bicondicional PROVADO a partir da interface metamatemática
-- (substitui o axiom triviais sobre Bools).

/-- Hipóteses metamatemáticas do Lema 3 (09 §12).
    `inconsistent_implies_not_phi`: se ¬Con(T), existe p com Prf_T(p,⊥);
    padding → ∃x Φ_T(x) com prefixo w* → ¬Φ_T^{w*}.
    `consistent_implies_phi`: se Con(T), não existe tal p;
    ∀x ¬Φ_T(x) → Φ_T^{w*}. -/
structure Lemma3Hyp where
  Con : Prop
  PhiStar : Prop
  inconsistent_implies_not_phi : ¬Con → ¬PhiStar
  consistent_implies_phi : Con → PhiStar

/-- Lema 3: Φ_T^{w*} ↔ Con(T) (bicondicional PROVADO da interface). -/
theorem lemma3_con (H : Lemma3Hyp) : H.PhiStar ↔ H.Con := by
  constructor
  · intro h
    exact Classical.byContradiction
      (fun hnc => H.inconsistent_implies_not_phi hnc h)
  · intro h
    exact H.consistent_implies_phi h

/-- Forma "só uma direção" usada por theorem4 (Con → Φ^{w*}). -/
theorem lemma3_con_of_consistent (H : Lemma3Hyp) (hc : H.Con) : H.PhiStar :=
  H.consistent_implies_phi hc

/-- Direção refutação: ¬Con → ¬Φ^{w*}. -/
theorem lemma3_con_refute (H : Lemma3Hyp) (hnc : ¬H.Con) : ¬H.PhiStar :=
  H.inconsistent_implies_not_phi hnc

-- =========================================================================
-- Generalização (C) — ALL_COV (defs; provas após auxiliares de lista)
-- =========================================================================
--
-- (C) dispara quando T' cobre todo w ∈ truesOf W.
-- Inevitável sse σ_T' ≥ max κ e b ≥ max κ + 1 (sobre obrigações verdadeiras).

/-- maior κ entre obrigações verdadeiras de W (0 se vazio). -/
def maxKappa (W : List Obligation) : Nat :=
  (W.filter (·.isTrue)).foldl (fun acc o => max acc o.kappa) 0

/-- Toda obrigação verdadeira de W está coberta em T. -/
def allCovered (T : Theory) (b : Nat) (W : List Obligation) : Bool :=
  (W.filter (·.isTrue)).all (covered T b)

-- =========================================================================
-- Auxiliares de lista
-- =========================================================================

theorem length_filter_sub {α : Type} (L : List α) (p : α → Bool) :
    L.length - (L.filter p).length = (L.filter (fun x => !p x)).length := by
  induction L with
  | nil => simp
  | cons a as ih =>
    by_cases hp : p a = true
    · rw [List.filter_cons_of_pos hp]
      have hnp : (fun x => !p x) a = false := by simp [hp]
      rw [List.filter_cons_of_neg (by
        intro h
        have h' : (fun x => !p x) a = true := by simpa using h
        rw [hnp] at h'
        exact Bool.noConfusion h')]
      simp only [List.length_cons]
      omega
    · have hpf : p a = false := by
        cases hpa : p a <;> simp_all
      rw [List.filter_cons_of_neg (by
        intro h
        exact hp (by simpa using h))]
      have hnp : (fun x => !p x) a = true := by simp [hpf]
      rw [List.filter_cons_of_pos (by simpa using hnp)]
      simp only [List.length_cons]
      have hle : (as.filter p).length ≤ as.length := List.length_filter_le _ _
      omega

theorem length_filter_strict {α : Type} :
    ∀ (L : List α) (p q : α → Bool),
      (∀ x ∈ L, p x = true → q x = true) →
      (∃ x ∈ L, p x = false ∧ q x = true) →
      (L.filter p).length < (L.filter q).length := by
  intro L
  induction L with
  | nil =>
    intro p q _ hex
    obtain ⟨x, hx, _, _⟩ := hex
    simp at hx
  | cons b bs ih =>
    intro p q hmono hex
    obtain ⟨a, haL, hpa, hqa⟩ := hex
    by_cases hb : b = a
    · subst hb
      rw [List.filter_cons_of_neg (by simpa using hpa),
          List.filter_cons_of_pos (by simpa using hqa)]
      simp only [List.length_cons]
      have hle : (bs.filter p).length ≤ (bs.filter q).length :=
        length_filter_mono fun x hx hp => hmono x (List.mem_cons_of_mem b hx) hp
      omega
    · have ha' : a ∈ bs := by
        cases List.mem_cons.mp haL with
        | inl he => exact absurd he (fun h => hb h.symm)
        | inr he => exact he
      by_cases hpb : p b = true
      · have hqb : q b = true := hmono b (List.mem_cons_self) hpb
        rw [List.filter_cons_of_pos hpb, List.filter_cons_of_pos hqb]
        simp only [List.length_cons]
        refine Nat.succ_lt_succ (ih p q (fun x hx hp =>
          hmono x (List.mem_cons_of_mem b hx) hp) ⟨a, ha', hpa, hqa⟩)
      · rw [List.filter_cons_of_neg (by
          intro hpb'
          exact hpb (by simpa using hpb'))]
        by_cases hqb : q b = true
        · rw [List.filter_cons_of_pos hqb]
          simp only [List.length_cons]
          have hle : (bs.filter p).length ≤ (bs.filter q).length :=
            length_filter_mono fun x hx hp => hmono x (List.mem_cons_of_mem b hx) hp
          have hlt : (bs.filter p).length < (bs.filter q).length :=
            ih p q (fun x hx hp => hmono x (List.mem_cons_of_mem b hx) hp)
              ⟨a, ha', hpa, hqa⟩
          omega
        · rw [List.filter_cons_of_neg (by
            intro hqb'
            exact hqb (by simpa using hqb'))]
          exact ih p q (fun x hx hp => hmono x (List.mem_cons_of_mem b hx) hp)
            ⟨a, ha', hpa, hqa⟩

-- =========================================================================
-- theorem4_strict (PR21)
-- =========================================================================

theorem theorem4_strict
    (T T' : Theory) (W : List Obligation) (B B' b : Nat)
    (h1 : ∀ w ∈ W, w.isTrue = true → w.idx ≠ "w*" → (w.kappa + 1) ≤ B)
    (h2 : ∀ w ∈ W, w.idx = "w*" → w.isTrue = true → T.sigma < w.kappa)
    (h3 : ∀ w ∈ W, w.idx = "w*" → w.isTrue = true → w.kappa ≤ T'.sigma)
    (_h4 : T.sigma ≥ B) (h5 : T'.sigma ≥ max B B')
    (hb : b ≥ max B B')
    (h6 : ∀ w ∈ W, w.isTrue = true → w.idx = "w*" ∨ covered T b w = true)
    (h7 : ∀ w ∈ W, w.idx = "w*" → w.isTrue = true → w.kappa + 1 ≤ b)
    (h8 : (W.filter (fun w => decide (w.idx = "w*") && w.isTrue)).length = 1) :
    delta T b W = 1 ∧ delta T' b W = 0 := by
  have hex_list : ∃ w, W.filter (fun v => decide (v.idx = "w*") && v.isTrue) = [w] := by
    match hr : W.filter (fun v => decide (v.idx = "w*") && v.isTrue) with
    | [] => rw [hr] at h8; simp at h8
    | [w] => exact ⟨w, hr⟩
    | _ :: _ :: _ => rw [hr] at h8; simp at h8
  obtain ⟨wstar, hfw⟩ := hex_list

  have hmem_fw : wstar ∈ W.filter (fun v => decide (v.idx = "w*") && v.isTrue) := by
    rw [hfw]; simp
  have hwW : wstar ∈ W := (List.mem_filter.mp hmem_fw).1
  have hpred : (decide (wstar.idx = "w*") && wstar.isTrue) = true :=
    (List.mem_filter.mp hmem_fw).2
  have hand : decide (wstar.idx = "w*") = true ∧ wstar.isTrue = true := by
    simp only [Bool.and_eq_true] at hpred
    exact hpred
  have hidx : wstar.idx = "w*" := by
    have := hand.1
    simpa using this
  have htrue : wstar.isTrue = true := hand.2

  have hstar_trues : wstar ∈ truesOf W := List.mem_filter.mpr ⟨hwW, htrue⟩

  have himpl : ∀ w ∈ truesOf W, w.idx = "w*" → w = wstar := by
    intro w hwm hi
    have hW : w ∈ W := (List.mem_filter.mp hwm).1
    have hT : w.isTrue = true := (List.mem_filter.mp hwm).2
    have hfw2 : w ∈ W.filter (fun v => decide (v.idx = "w*") && v.isTrue) := by
      rw [List.mem_filter]; exact ⟨hW, by simp [hi, hT]⟩
    rw [hfw] at hfw2
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hfw2
    exact hfw2

  have hchar : ∀ w ∈ truesOf W, covered T b w = true ↔ w ≠ wstar := by
    intro w hwm
    have hW : w ∈ W := (List.mem_filter.mp hwm).1
    have hT : w.isTrue = true := (List.mem_filter.mp hwm).2
    constructor
    · intro hc heq
      cases heq
      have hlt := h2 wstar hwW hidx htrue
      unfold covered at hc
      simp only [decide_eq_true_iff] at hc
      obtain ⟨_, hkle, _⟩ := hc
      exact absurd hkle (Nat.not_le.mpr hlt)
    · intro hne
      cases h6 w hW hT with
      | inl hi =>
        exact absurd (himpl w hwm hi) hne
      | inr hc => exact hc

  have heq : ∀ w ∈ truesOf W, (!covered T b w) = decide (w.idx = "w*") := by
    intro w hwm
    have hW : w ∈ W := (List.mem_filter.mp hwm).1
    have hT : w.isTrue = true := (List.mem_filter.mp hwm).2
    cases hc : covered T b w with
    | true =>
      rw [Bool.not_true]
      have hne : w ≠ wstar := (hchar w hwm).mp hc
      rw [eq_comm, decide_eq_false_iff_not]
      intro hi
      exact hne (himpl w hwm hi)
    | false =>
      rw [Bool.not_false]
      rw [eq_comm, decide_eq_true_iff]
      by_cases hne : w = wstar
      · rw [hne]; exact hidx
      · exact absurd ((hchar w hwm).mpr hne) (by
          intro h
          exact Bool.noConfusion (Eq.trans h.symm hc))

  have huncov_count : ((truesOf W).filter (fun w => !covered T b w)).length = 1 := by
    have hfilter : (truesOf W).filter (fun w => !covered T b w) =
                   (truesOf W).filter (fun w => decide (w.idx = "w*")) := by
      apply List.filter_congr
      intro w hwm
      exact heq w hwm
    rw [hfilter]
    have heq2 : (truesOf W).filter (fun w => decide (w.idx = "w*")) =
                W.filter (fun w => decide (w.idx = "w*") && w.isTrue) := by
      unfold truesOf
      rw [List.filter_filter]
    rw [heq2, hfw]
    simp

  have hdeltaT : delta T b W = 1 := by
    unfold delta covOf truesOf
    rw [length_filter_sub]
    exact huncov_count

  have hall_cov_T' : ∀ w ∈ truesOf W, covered T' b w = true := by
    intro w hwm
    have hW : w ∈ W := (List.mem_filter.mp hwm).1
    have hT : w.isTrue = true := (List.mem_filter.mp hwm).2
    unfold covered
    rw [decide_eq_true_iff]
    cases h6 w hW hT with
    | inl hi =>
      exact ⟨hT, h3 w hW hi hT, h7 w hW hi hT⟩
    | inr hct =>
      have hex' : covered T b w = true := hct
      unfold covered at hex'
      rw [decide_eq_true_iff] at hex'
      obtain ⟨_, hkle, hbnd⟩ := hex'
      have hne : w.idx ≠ "w*" := by
        intro heq
        have hlt := h2 w hW heq hT
        exact absurd hkle (Nat.not_le.mpr hlt)
      have hk1 : w.kappa + 1 ≤ B := h1 w hW hT hne
      have hT'sig : w.kappa ≤ T'.sigma := by
        have : w.kappa + 1 ≤ T'.sigma :=
          Nat.le_trans hk1 (Nat.le_trans (Nat.le_max_left B B') h5)
        omega
      have hb' : w.kappa + 1 ≤ b :=
        Nat.le_trans hk1 (Nat.le_trans (Nat.le_max_left B B') hb)
      exact ⟨hT, hT'sig, hb'⟩

  have huncov_T' : (truesOf W).filter (fun w => !covered T' b w) = [] := by
    rw [List.filter_eq_nil_iff]
    intro w hwm
    rw [hall_cov_T' w hwm, Bool.not_true]
    intro h
    exact Bool.noConfusion h

  have hdeltaT' : delta T' b W = 0 := by
    unfold delta covOf
    rw [length_filter_sub, huncov_T']
    simp

  exact ⟨hdeltaT, hdeltaT'⟩

-- =========================================================================
-- rcs_exists (PR21)
-- =========================================================================

theorem rcs_exists
    (W : List Obligation)
    (fastStep slowStep : Nat)
    (hfast : 2 ≤ fastStep)
    (hslow : 1 ≤ slowStep)
    (hex : ∃ o ∈ W, o.isTrue = true ∧ slowStep < o.kappa) :
    ∃ (α b : Nat),
      let SF : Theory := ⟨"F", sigmaFast α fastStep⟩
      let SS : Theory := ⟨"S", sigmaSlow α slowStep⟩
      delta SF b W ≠ delta SS b W := by
  obtain ⟨o, hoW, hoT, hok⟩ := hex
  have hk2 : 2 ≤ o.kappa := by omega

  refine ⟨(o.kappa + fastStep - 1) / fastStep, o.kappa + 1, ?_⟩
  simp only [sigmaFast, sigmaSlow]

  have hα : fastStep * ((o.kappa + fastStep - 1) / fastStep) ≥ o.kappa := by
    have hmod : (o.kappa + fastStep - 1) % fastStep < fastStep :=
      Nat.mod_lt _ (by omega)
    have hdiv : fastStep * ((o.kappa + fastStep - 1) / fastStep) +
                (o.kappa + fastStep - 1) % fastStep = o.kappa + fastStep - 1 := by
      have := Nat.div_add_mod (o.kappa + fastStep - 1) fastStep
      omega
    omega

  have hmul_eq : fastStep * o.kappa =
                 o.kappa * (fastStep - 1) + o.kappa := by
    have hsplit : fastStep = (fastStep - 1) + 1 := by omega
    have h1 : fastStep * o.kappa = o.kappa * fastStep := by
      rw [Nat.mul_comm]
    have h2 : o.kappa * fastStep = o.kappa * ((fastStep - 1) + 1) := by
      congr 1
    have h3 : o.kappa * ((fastStep - 1) + 1) =
              o.kappa * (fastStep - 1) + o.kappa * 1 := by
      rw [Nat.mul_add]
    have h4 : o.kappa * (fastStep - 1) + o.kappa * 1 =
              o.kappa * (fastStep - 1) + o.kappa := by
      rw [Nat.mul_one]
    rw [h1, h2, h3, h4]

  have hlt_mul : o.kappa + fastStep - 1 < fastStep * o.kappa := by
    rw [hmul_eq]
    have hkle : 2 ≤ o.kappa := hk2
    have hm : 1 ≤ fastStep - 1 := by omega
    have hprod_lb : 2 * (fastStep - 1) ≤ o.kappa * (fastStep - 1) :=
      Nat.mul_le_mul hkle (Nat.le_refl _)
    have h2 : (fastStep - 1) + 1 ≤ 2 * (fastStep - 1) := by omega
    have h3 : (fastStep - 1) + 1 ≤ o.kappa * (fastStep - 1) :=
      Nat.le_trans h2 hprod_lb
    omega


  have hα_lt : (o.kappa + fastStep - 1) / fastStep < o.kappa := by
    by_cases hge : o.kappa ≤ (o.kappa + fastStep - 1) / fastStep
    · have h1 : fastStep * o.kappa ≤
                fastStep * ((o.kappa + fastStep - 1) / fastStep) :=
        Nat.mul_le_mul_left _ hge
      have h2 : (o.kappa + fastStep - 1) / fastStep * fastStep ≤
                o.kappa + fastStep - 1 := Nat.div_mul_le_self _ _
      have hcomm : fastStep * ((o.kappa + fastStep - 1) / fastStep) =
                   ((o.kappa + fastStep - 1) / fastStep) * fastStep := by
        rw [Nat.mul_comm]
      have h2' : fastStep * ((o.kappa + fastStep - 1) / fastStep) ≤
                 o.kappa + fastStep - 1 := by
        rw [hcomm]; exact h2
      have hcomm2 : fastStep * o.kappa = o.kappa * fastStep := by
        rw [Nat.mul_comm]
      have h3 : o.kappa * fastStep ≤ o.kappa + fastStep - 1 := by
        rw [← hcomm2]; exact Nat.le_trans h1 h2'
      have hlt : o.kappa * fastStep < o.kappa * fastStep := by
        have := Nat.lt_of_le_of_lt h3 hlt_mul
        rw [hcomm2] at this
        exact this
      exact absurd hlt (Nat.lt_irrefl _)
    · exact Nat.lt_of_not_le hge

  have hSF : covered ⟨"F", fastStep * ((o.kappa + fastStep - 1) / fastStep)⟩
                (o.kappa + 1) o = true := by
    unfold covered
    rw [decide_eq_true_iff]
    refine ⟨hoT, hα, ?_⟩
    omega

  have hSS' : covered ⟨"S", (o.kappa + fastStep - 1) / fastStep⟩
                 (o.kappa + 1) o = false := by
    unfold covered
    rw [decide_eq_false_iff_not]
    intro h
    obtain ⟨_, hle, _⟩ := h
    exact absurd hle (Nat.not_le.mpr hα_lt)

  have hmono : ∀ w ∈ truesOf W,
      covered ⟨"S", (o.kappa + fastStep - 1) / fastStep⟩ (o.kappa + 1) w = true →
      covered ⟨"F", fastStep * ((o.kappa + fastStep - 1) / fastStep)⟩
        (o.kappa + 1) w = true := by
    intro w _ hc
    refine covered_mono ?_ hc
    show ((o.kappa + fastStep - 1) / fastStep) ≤
         fastStep * ((o.kappa + fastStep - 1) / fastStep)
    omega

  have ho_trues : o ∈ truesOf W := List.mem_filter.mpr ⟨hoW, hoT⟩

  have hstrict : ∃ w ∈ truesOf W,
      covered ⟨"S", (o.kappa + fastStep - 1) / fastStep⟩ (o.kappa + 1) w = false ∧
      covered ⟨"F", fastStep * ((o.kappa + fastStep - 1) / fastStep)⟩
        (o.kappa + 1) w = true :=
    ⟨o, ho_trues, hSS', hSF⟩

  have hlen_lt :
      ((truesOf W).filter (covered ⟨"S", (o.kappa + fastStep - 1) / fastStep⟩ (o.kappa + 1))).length <
      ((truesOf W).filter (covered ⟨"F", fastStep * ((o.kappa + fastStep - 1) / fastStep)⟩ (o.kappa + 1))).length :=
    length_filter_strict (truesOf W)
      (covered ⟨"S", (o.kappa + fastStep - 1) / fastStep⟩ (o.kappa + 1))
      (covered ⟨"F", fastStep * ((o.kappa + fastStep - 1) / fastStep)⟩ (o.kappa + 1))
      hmono hstrict

  have hdelta_lt :
      delta ⟨"F", fastStep * ((o.kappa + fastStep - 1) / fastStep)⟩ (o.kappa + 1) W <
      delta ⟨"S", (o.kappa + fastStep - 1) / fastStep⟩ (o.kappa + 1) W := by
    unfold delta covOf
    have abstract : ∀ (tf cF cS : Nat), cS < cF → cF ≤ tf → cS ≤ tf →
        tf - cF < tf - cS := by
      intro tf cF cS h hf hs
      omega
    have hleF : ((truesOf W).filter
        (covered ⟨"F", fastStep * ((o.kappa + fastStep - 1) / fastStep)⟩
          (o.kappa + 1))).length ≤ (truesOf W).length :=
      List.length_filter_le _ _
    have hleS : ((truesOf W).filter
        (covered ⟨"S", (o.kappa + fastStep - 1) / fastStep⟩
          (o.kappa + 1))).length ≤ (truesOf W).length :=
      List.length_filter_le _ _
    exact abstract _ _ _ hlen_lt hleF hleS

  exact Nat.ne_of_lt hdelta_lt

-- =========================================================================
-- (C) generalizado — provas (PR24; após length_filter_sub)
-- =========================================================================

/-- foldl max é ≥ acc em qualquer lista. -/
theorem foldl_max_ge (L : List Obligation) (acc : Nat) :
    List.foldl (fun c x => max c x.kappa) acc L ≥ acc := by
  induction L generalizing acc with
  | nil => simp
  | cons a as ih =>
    rw [List.foldl_cons]
    exact Nat.le_trans (Nat.le_max_left acc a.kappa) (ih (max acc a.kappa))

/-- foldl max é monótono no acc. -/
theorem foldl_max_mono_acc :
    ∀ (L : List Obligation) (c1 c2 : Nat),
      c1 ≤ c2 →
      List.foldl (fun c x => max c x.kappa) c1 L ≤
      List.foldl (fun c x => max c x.kappa) c2 L := by
  intro L
  induction L with
  | nil => intro c1 c2 h; simp; exact h
  | cons a as ih =>
    intro c1 c2 h
    rw [List.foldl_cons, List.foldl_cons]
    refine ih (max c1 a.kappa) (max c2 a.kappa) ?_
    have h1 : c1 ≤ max c2 a.kappa := Nat.le_trans h (Nat.le_max_left _ _)
    have h2 : a.kappa ≤ max c2 a.kappa := Nat.le_max_right _ _
    omega

/-- maxKappa W ≥ o.kappa para toda o ∈ truesOf W. -/
theorem le_maxKappa_of_mem_trues
    {W : List Obligation} {o : Obligation}
    (ho : o ∈ truesOf W) :
    o.kappa ≤ maxKappa W := by
  unfold maxKappa at ⊢
  unfold truesOf at ho
  induction W generalizing o with
  | nil => simp at ho
  | cons a as ih =>
    by_cases ha : a.isTrue = true
    · rw [List.filter_cons_of_pos (by simp [ha])] at ho
      rw [List.filter_cons_of_pos (by simp [ha]), List.foldl_cons]
      cases List.mem_cons.mp ho with
      | inl heq =>
        subst heq
        exact Nat.le_trans (Nat.le_max_right 0 o.kappa) (foldl_max_ge _ _)
      | inr himem =>
        have hih : o.kappa ≤ List.foldl (fun c x => max c x.kappa) 0
            (as.filter (·.isTrue)) := ih himem
        have hmono := foldl_max_mono_acc (as.filter (·.isTrue)) 0
          (max 0 a.kappa) (Nat.le_max_left 0 a.kappa)
        exact Nat.le_trans hih hmono
    · rw [List.filter_cons_of_neg (by simp [ha])] at ho
      rw [List.filter_cons_of_neg (by simp [ha])]
      exact ih ho

/-- Se todos os elementos de L satisfazem p, filter p L = L. -/
theorem filter_eq_self_of_forall {α : Type} (L : List α) (p : α → Bool)
    (h : ∀ x ∈ L, p x = true) :
    L.filter p = L := by
  induction L with
  | nil => simp
  | cons a as ih =>
    rw [List.filter_cons_of_pos (h a (List.mem_cons_self)),
        ih (fun x hx => h x (List.mem_cons_of_mem a hx))]

/-- ALL_COV ⇔ delta = 0. -/
theorem allCovered_iff_delta_zero
    (T : Theory) (b : Nat) (W : List Obligation) :
    allCovered T b W = true ↔ delta T b W = 0 := by
  unfold allCovered delta covOf truesOf
  constructor
  · intro h
    have hall : ∀ o ∈ W.filter (·.isTrue), covered T b o = true :=
      List.all_eq_true.mp h
    have heq : (W.filter (·.isTrue)).filter (covered T b) =
               W.filter (·.isTrue) :=
      filter_eq_self_of_forall _ _ hall
    rw [heq, Nat.sub_self]
  · intro h
    have h0 : ((W.filter (·.isTrue)).filter
        (fun x => !(covered T b x))).length = 0 := by
      rw [← length_filter_sub]
      exact h
    have hnil : (W.filter (·.isTrue)).filter
        (fun x => !(covered T b x)) = [] :=
      List.eq_nil_of_length_eq_zero h0
    rw [List.all_eq_true]
    intro o ho
    by_cases hc : covered T b o = true
    · exact hc
    · exfalso
      have hm : o ∈ (W.filter (·.isTrue)).filter
          (fun x => !(covered T b x)) :=
        List.mem_filter.mpr ⟨ho, by simp [hc]⟩
      rw [hnil] at hm
      exact absurd hm List.not_mem_nil

/-- Limiar: se σ_T ≥ max κ e b ≥ max κ+1, toda verdadeira está coberta. -/
theorem allCovered_of_sigma_max
    (T : Theory) (b : Nat) (W : List Obligation)
    (hσ : maxKappa W ≤ T.sigma)
    (hb : maxKappa W + 1 ≤ b) :
    allCovered T b W = true := by
  unfold allCovered
  rw [List.all_eq_true]
  intro o ho
  unfold covered
  rw [decide_eq_true_iff]
  have hT : o.isTrue = true := (List.mem_filter.mp ho).2
  have hmk : o.kappa ≤ maxKappa W :=
    le_maxKappa_of_mem_trues (List.mem_filter.mpr ⟨(List.mem_filter.mp ho).1, hT⟩)
  exact ⟨hT, Nat.le_trans hmk hσ, by omega⟩

/-- Corolário (C): nessas condições, δ_T' = 0 (ALL_COV). -/
theorem delta_zero_of_sigma_max
    (T : Theory) (b : Nat) (W : List Obligation)
    (hσ : maxKappa W ≤ T.sigma)
    (hb : maxKappa W + 1 ≤ b) :
    delta T b W = 0 :=
  (allCovered_iff_delta_zero T b W).mp (allCovered_of_sigma_max T b W hσ hb)

/-- Condição (C) no predicado PPR-2-ramo: w₀' = None (ALL) ⇒ δ_T' = 0. -/
theorem cond_C_delta_zero
    (T : Theory) (b : Nat) (W : List Obligation)
    (hall : allCovered T b W = true) :
    delta T b W = 0 :=
  (allCovered_iff_delta_zero T b W).mp hall

end GothicGenerators

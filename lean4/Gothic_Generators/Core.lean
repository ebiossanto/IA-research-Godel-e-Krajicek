import Init

/-!
PR15/PR18/PR21 — Formalização Lean 4
STATUS: delta_mono, theorem4_strict, rcs_exists; lemma3_con = axiom.
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
-- lemma3_con: axiom (pendente Foundation/pad-Prf)
-- =========================================================================

structure PhiConstruction where
  wStar : String
  conT : Bool
  phi_wStar_true : Bool

axiom lemma3_axiom (P : PhiConstruction) : P.phi_wStar_true = P.conT

theorem lemma3_con (P : PhiConstruction) : P.phi_wStar_true = P.conT :=
  lemma3_axiom P

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

end GothicGenerators

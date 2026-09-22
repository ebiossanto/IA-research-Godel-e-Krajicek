/-
  PR15/PR18/PR21 — Formalização Lean 4
  STATUS (PR21): delta_mono, theorem4_strict, rcs_exists PROVADOS (sem sorry);
  lemma3_con = axiom (pendente Foundation/pad-Prf).
-/

namespace GothicGenerators

abbrev Budget := ℕ → ℕ

structure Obligation where
  idx : String
  kappa : ℕ
  isTrue : Bool

structure Theory where
  name : String
  sigma : ℕ

def covered (T : Theory) (b : ℕ) (o : Obligation) : Bool :=
  o.isTrue && o.kappa ≤ T.sigma && (o.kappa + 1) ≤ b

def delta (T : Theory) (b : ℕ) (W : List Obligation) : ℕ :=
  let trues := W.filter (·.isTrue)
  let cov := trues.filter (covered T b)
  trues.length - cov.length

def sigmaFast (α : ℕ) (fastStep : ℕ) : ℕ := fastStep * α
def sigmaSlow (α : ℕ) (slowStep : ℕ) : ℕ := α

-- =========================================================================
-- delta_mono (PR18)
-- =========================================================================

theorem covered_mono
    {T S : Theory} {b : ℕ} {o : Obligation}
    (hσ : T.sigma ≤ S.sigma)
    (hc : covered T b o = true) :
    covered S b o = true := by
  unfold covered at hc ⊢
  simp only [Bool.and_eq_true] at hc ⊢
  obtain ⟨h1, h2, h3⟩ := hc
  exact ⟨h1, Nat.le_trans h2 hσ, h3⟩

theorem length_filter_mono
    {α : Type} {p q : α → Bool} {L : List α}
    (h : ∀ x ∈ L, p x = true → q x = true) :
    (L.filter p).length ≤ (L.filter q).length := by
  induction L with
  | nil => simp
  | cons a as ih =>
    simp only [List.filter_cons]
    by_cases hp : p a = true
    · have hq : q a = true := h a (List.mem_cons_self a as) hp
      simp only [hp, hq, if_true, List.length_cons]
      exact Nat.succ_le_succ (ih fun x hx hxp => h x (List.mem_cons_of_mem a hx) hxp)
    · simp only [hp, if_false]
      have := ih fun x hx hxp => h x (List.mem_cons_of_mem a hx) hxp
      simp only [List.length_cons]
      exact Nat.le_trans this (Nat.le_succ _)

theorem delta_mono
    (T S : Theory) (b : ℕ) (W : List Obligation)
    (h : T.sigma ≤ S.sigma) :
    delta S b W ≤ delta T b W := by
  unfold delta
  set trues := W.filter (·.isTrue) with htrues
  set covT := trues.filter (covered T b) with hcT
  set covS := trues.filter (covered S b) with hcS
  have hsub : ∀ o ∈ covT, o ∈ covS := by
    intro o ho
    obtain ⟨hW, hc⟩ := List.mem_filter.mp (by rw [← hcT]; exact ho)
    exact List.mem_filter.mpr ⟨hW, covered_mono h hc⟩
  have hlen : covT.length ≤ covS.length := length_filter_mono hsub
  exact Nat.sub_le_sub_left hlen trues.length

-- =========================================================================
-- lemma3_con: axiom
-- =========================================================================

structure PhiConstruction where
  wStar : String
  conT : Bool
  phi_wStar_true : Bool

axiom lemma3_axiom (P : PhiConstruction) : P.phi_wStar_true = P.conT

lemma lemma3_con (P : PhiConstruction) : P.phi_wStar_true = P.conT :=
  lemma3_axiom P

-- =========================================================================
-- Auxiliares de lista
-- =========================================================================

theorem length_filter_sub {α : Type} (L : List α) (p : α → Bool) :
    L.length - (L.filter p).length = (L.filter (fun x => !p x)).length := by
  induction L with
  | nil => simp
  | cons a as ih =>
    simp only [List.filter_cons]
    cases h : p a with
    | isTrue =>
      simp only [h, if_true, List.length_cons, Bool.not_true]
      simp only [List.filter_cons, Bool.not_true, if_false]
      rw [ih]; omega
    | isFalse =>
      simp only [h, if_false, List.length_cons, Bool.not_false]
      simp only [List.filter_cons, Bool.not_false, if_true]
      rw [ih]; omega

theorem length_filter_strict {α : Type} (L : List α) (p q : α → Bool)
    (hmono : ∀ x ∈ L, p x = true → q x = true)
    (hex : ∃ x ∈ L, p x = false ∧ q x = true) :
    (L.filter p).length < (L.filter q).length := by
  obtain ⟨a, haL, hpa, hqa⟩ := hex
  induction L generalizing a with
  | nil => simp at haL
  | cons b bs ih =>
    simp only [List.filter_cons]
    by_cases hb : b = a
    · subst hb
      simp only [hpa, if_false, hqa, if_true]
      have hle : (bs.filter p).length ≤ (bs.filter q).length :=
        length_filter_mono fun x hx hp => hmono x (List.mem_cons_of_mem b hx) hp
      simp only [List.length_cons]
      omega
    · have ha' : a ∈ bs := by
        cases List.mem_cons.mp haL with
        | inl he => exact absurd he hb
        | inr he => exact he
      by_cases hpb : p b = true
      · have hqb : q b = true := hmono b (List.mem_cons_self b bs) hpb
        simp only [hpb, if_true, hqb, if_true, List.length_cons]
        refine Nat.succ_lt_succ (ih a ha' hpa hqa fun x hx hp =>
          hmono x (List.mem_cons_of_mem b hx) hp)
      · simp only [hpb, if_false]
        by_cases hqb : q b = true
        · simp only [hqb, if_true, List.length_cons]
          have hle : (bs.filter p).length ≤ (bs.filter q).length :=
            length_filter_mono fun x hx hp => hmono x (List.mem_cons_of_mem b hx) hp
          have hlt : (bs.filter p).length < (bs.filter q).length :=
            ih a ha' hpa hqa fun x hx hp => hmono x (List.mem_cons_of_mem b hx) hp
          omega
        · simp only [hqb, if_false]
          exact ih a ha' hpa hqa fun x hx hp => hmono x (List.mem_cons_of_mem b hx) hp

-- =========================================================================
-- theorem4_strict (PR21) — PROVA COMPLETA
-- =========================================================================

theorem theorem4_strict
    (T T' : Theory) (W : List Obligation) (B B' b : ℕ)
    (h1 : ∀ w ∈ W, w.isTrue = true → w.idx ≠ "w*" → (w.kappa + 1) ≤ B)
    (h2 : ∀ w ∈ W, w.idx = "w*" → w.isTrue = true → T.sigma < w.kappa)
    (h3 : ∀ w ∈ W, w.idx = "w*" → w.isTrue = true → w.kappa ≤ T'.sigma)
    (h4 : T.sigma ≥ B) (h5 : T'.sigma ≥ max B B')
    (hb : b ≥ max B B')
    (h6 : ∀ w ∈ W, w.isTrue = true → w.idx = "w*" ∨ covered T b w = true)
    (h7 : ∀ w ∈ W, w.idx = "w*" → w.isTrue = true → w.kappa + 1 ≤ b)
    (h8 : (W.filter (fun w => w.idx = "w*" && w.isTrue)).length = 1) :
    delta T b W = 1 ∧ delta T' b W = 0 := by
  classical
  -- Extrair o único wstar true com idx=w*
  have hex_list : ∃ w, W.filter (fun v => v.idx = "w*" && v.isTrue) = [w] := by
    match hr : W.filter (fun v => v.idx = "w*" && v.isTrue) with
    | [] => rw [hr] at h8; simp at h8
    | [w] => exact ⟨w, hr⟩
    | _ :: _ :: _ => rw [hr] at h8; simp at h8
  obtain ⟨wstar, hfw⟩ := hex_list

  have hmem_fw : wstar ∈ W.filter (fun v => v.idx = "w*" && v.isTrue) := by
    rw [hfw]; simp
  have hwW : wstar ∈ W := (List.mem_filter.mp hmem_fw).1
  have hidx : wstar.idx = "w*" := (List.mem_filter.mp hmem_fw).2.1
  have htrue : wstar.isTrue = true := (List.mem_filter.mp hmem_fw).2.2

  set trues := W.filter (·.isTrue) with htrues
  set covT := trues.filter (covered T b) with hcT
  set covT' := trues.filter (covered T' b) with hcT'

  have hstar_trues : wstar ∈ trues := by
    rw [htrues]; exact List.mem_filter.mpr ⟨hwW, htrue⟩

  -- covered T b w = true ↔ w ≠ wstar (para w ∈ trues)
  have hchar : ∀ w ∈ trues, covered T b w = true ↔ w ≠ wstar := by
    intro w hwm
    have hW : w ∈ W := by rw [htrues] at hwm; exact hwm.1
    have hT : w.isTrue = true := hwm.2
    constructor
    · intro hc heq
      subst heq
      have hlt := h2 wstar hwW hidx htrue
      unfold covered at hc
      simp only [Bool.and_eq_true] at hc
      obtain ⟨_, hkle, _⟩ := hc
      exact absurd hkle (Nat.not_le.mpr hlt)
    · intro hne
      cases h6 w hW hT with
      | inl hi =>
        have hfw2 : w ∈ W.filter (fun v => v.idx = "w*" && v.isTrue) := by
          rw [List.mem_filter]; exact ⟨hW, by simp [hi, hT]⟩
        rw [hfw] at hfw2
        simp only [List.mem_cons, List.nil_eq, or_false] at hfw2
        exact absurd hfw2.symm hne
      | inr hc => exact hc

  -- wstar não coberto em T
  have hstar_ncov : covered T b wstar = false := by
    have hiff := hchar wstar hstar_trues
    simp only [ne_self_iff_false, iff_false] at hiff
    cases hc : covered T b wstar
    · rfl
    · exact absurd hc hiff

  -- Equivalência: não-coberto em T ↔ idx=w* (em trues)
  have heq : ∀ w ∈ trues, !(covered T b w) = (decide (w.idx = "w*")) := by
    intro w hwm
    have hW : w ∈ W := by rw [htrues] at hwm; exact hwm.1
    have hT : w.isTrue = true := hwm.2
    cases hc : covered T b w with
    | isTrue =>
      simp only [Bool.not_true]
      -- covered = true → w ≠ wstar → idx ≠ w* (por unicidade)
      have hne : w ≠ wstar := (hchar w hwm).mp hc
      rw [decide_eq_false_iff_not]
      intro hi
      -- w.idx = w* e w ∈ trues → w = wstar
      have hfw2 : w ∈ W.filter (fun v => v.idx = "w*" && v.isTrue) := by
        rw [List.mem_filter]; exact ⟨hW, by simp [hi, hT]⟩
      rw [hfw] at hfw2
      simp only [List.mem_cons, List.nil_eq, or_false] at hfw2
      exact hne hfw2.symm
    | isFalse =>
      simp only [Bool.not_false]
      rw [decide_eq_true_iff]
      -- covered = false → w = wstar → idx = w*
      have : w = wstar := by
        by_contra hne
        exact hc ((hchar w hwm).mpr hne)
      rw [this]; exact hidx

  -- |não-cobertos em T| = |idx=w* filter| = 1
  have huncov_count : (trues.filter (fun w => !(covered T b w))).length = 1 := by
    have hfilter : trues.filter (fun w => !(covered T b w)) =
                   trues.filter (fun w => decide (w.idx = "w*")) := by
      apply List.filter_congr'
      intro w hwm
      exact heq w hwm
    rw [hfilter]
    have heq2 : trues.filter (fun w => decide (w.idx = "w*")) =
                W.filter (fun w => w.idx = "w*" && w.isTrue) := by
      rw [htrues]
      rw [List.filter_filter]
      congr 1
      funext w
      simp [Bool.and_comm]
    rw [heq2, hfw]

  -- delta T = 1
  have hdeltaT : delta T b W = 1 := by
    unfold delta
    rw [length_filter_sub]
    exact huncov_count

  -- Todo true coberto em T'
  have hall_cov_T' : ∀ w ∈ trues, covered T' b w = true := by
    intro w hwm
    have hW : w ∈ W := by rw [htrues] at hwm; exact hwm.1
    have hT : w.isTrue = true := hwm.2
    unfold covered
    simp only [hT, Bool.true_and, Bool.and_eq_true]
    cases h6 w hW hT with
    | inl hi =>
      exact ⟨h3 w hW hi hT, h7 w hW hi hT⟩
    | inr hct =>
      have hex' : covered T b w = true := hct
      unfold covered at hex'
      simp only [hT, Bool.true_and, Bool.and_eq_true] at hex'
      obtain ⟨hkle, hbnd⟩ := hex'
      have hne : w.idx ≠ "w*" := by
        intro heq
        have hlt := h2 w heq hT
        exact absurd hkle (Nat.not_le.mpr hlt)
      have hk1 : w.kappa + 1 ≤ B := h1 w hW hT hne
      have hT'sig : w.kappa ≤ T'.sigma := by
        have : w.kappa + 1 ≤ T'.sigma :=
          Nat.le_trans hk1 (Nat.le_trans (Nat.le_max_left B B') h5)
        omega
      have hb' : w.kappa + 1 ≤ b :=
        Nat.le_trans hk1 (Nat.le_trans (Nat.le_max_left B B') hb)
      exact ⟨hT'sig, hb'⟩

  have huncov_T' : trues.filter (fun w => !(covered T' b w)) = [] := by
    apply List.filter_eq_nil.mpr
    intro w hwm
    simp only [hall_cov_T' w hwm, Bool.not_true]

  have hdeltaT' : delta T' b W = 0 := by
    unfold delta
    rw [length_filter_sub, huncov_T']
    simp

  exact ⟨hdeltaT, hdeltaT'⟩

-- =========================================================================
-- rcs_exists (PR21) — PROVA COMPLETA
-- =========================================================================

theorem rcs_exists
    (W : List Obligation)
    (fastStep slowStep : ℕ)
    (hfast : 2 ≤ fastStep)
    (hslow : 1 ≤ slowStep)
    (hex : ∃ o ∈ W, o.isTrue = true ∧ slowStep < o.kappa) :
    ∃ (α b : ℕ),
      let SF : Theory := ⟨"F", sigmaFast α fastStep⟩
      let SS : Theory := ⟨"S", sigmaSlow α slowStep⟩
      delta SF b W ≠ delta SS b W := by
  obtain ⟨o, hoW, hoT, hok⟩ := hex
  have hk2 : 2 ≤ o.kappa := by omega

  -- Escolha: α = ceil(κ/fastStep), b = κ+1
  refine ⟨(o.kappa + fastStep - 1) / fastStep, o.kappa + 1, ?_⟩
  simp only [sigmaFast, sigmaSlow]

  set α := (o.kappa + fastStep - 1) / fastStep
  set b := o.kappa + 1
  set SF : Theory := ⟨"F", fastStep * α⟩
  set SS : Theory := ⟨"S", α⟩

  -- Propriedades de α
  have hα_ge : fastStep * α ≥ o.kappa := by
    have hmod : (o.kappa + fastStep - 1) % fastStep < fastStep := Nat.mod_lt _ (by omega)
    have heq : o.kappa + fastStep - 1 = α * fastStep + (o.kappa + fastStep - 1) % fastStep := by
      simp [α, Nat.div_add_mod]
    omega

  have hα_lt : α < o.kappa := by
    by_contra hge
    push_neg at hge
    have h1 : fastStep * o.kappa ≤ fastStep * α := Nat.mul_le_mul_left _ hge
    have h2 : α * fastStep ≤ o.kappa + fastStep - 1 := Nat.div_mul_le_self _ _
    rw [Nat.mul_comm] at h2
    have h3 : fastStep * o.kappa ≤ o.kappa + fastStep - 1 := Nat.le_trans h1 h2
    omega

  have hσ_mono : SS.sigma ≤ SF.sigma := by
    simp only [SF, SS, Theory.sigma]
    omega

  -- o coberto em SF
  have hSF : covered SF b o = true := by
    unfold covered
    simp only [hoT, Bool.true_and, Bool.and_eq_true]
    refine ⟨hα_ge, ?_⟩
    simp only [b]
    omega

  -- o não coberto em SS
  have hSS' : covered SS b o = false := by
    unfold covered
    simp only [hoT, Bool.true_and]
    have hnb : (o.kappa ≤ SS.sigma && o.kappa + 1 ≤ b) = false := by
      simp only [SS, Theory.sigma]
      simp only [Bool.and_eq_true, Bool.not_and, Bool.not_false, Bool.or_true, Bool.not_le]
      exact hα_lt
    simpa [b] using hnb

  set trues := W.filter (·.isTrue) with htrues
  set covSF := trues.filter (covered SF b) with hcSF
  set covSS := trues.filter (covered SS b) with hcSS

  have ho_trues : o ∈ trues := by
    rw [htrues]; exact List.mem_filter.mpr ⟨hoW, hoT⟩

  have hmono : ∀ w ∈ trues, covered SS b w = true → covered SF b w = true := by
    intro w _ hc
    exact covered_mono hσ_mono hc

  have hsub : ∀ w ∈ covSS, w ∈ covSF := by
    intro w hw
    obtain ⟨hW, hc⟩ := List.mem_filter.mp (by rw [← hcSS]; exact hw)
    exact List.mem_filter.mpr ⟨hW, hmono w hW hc⟩

  have hstrict : ∃ w ∈ trues, covered SS b w = false ∧ covered SF b w = true :=
    ⟨o, ho_trues, hSS', hSF⟩

  have hlen_lt : covSS.length < covSF.length :=
    length_filter_strict trues (covered SS b) (covered SF b) hmono hstrict

  have hSF_delta : delta SF b W = trues.length - covSF.length := by
    unfold delta
    simp only []
    congr 1
    · rw [htrues]
    · rw [htrues, hcSF]

  have hSS_delta : delta SS b W = trues.length - covSS.length := by
    unfold delta
    simp only []
    congr 1
    · rw [htrues]
    · rw [htrues, hcSS]

  have hdelta_lt : delta SF b W < delta SS b W := by
    rw [hSF_delta, hSS_delta]
    omega

  exact ne_of_lt hdelta_lt

end GothicGenerators

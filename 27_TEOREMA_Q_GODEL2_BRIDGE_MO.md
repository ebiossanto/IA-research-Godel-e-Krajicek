# 27 — Teorema Q (transferência) + Gödel II reificado + bridge δ + MathOverflow

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **PR27 — Q formalizado; bridge δ em Core; Gödel II (rota T.consistent); rascunho MO**
**Depende de:** `26_REVISAO_EXTERNA_PONTUAL.md` (Q1), `24`/`25` (Foundation), `09 §12`/`§35`

---

## 1. Teorema Q — transferência aritmético → proposicional

### 1.1. Enunciado (obrigatório antes de qualquer limite inferior)

Seja:

- \(T\) teoria formal;
- \(P\) sistema de prova proposicional (Cook–Reckhow);
- \((\tau_n)_{n\in\mathbb N}\) família **uniforme** (computável) de traduções
  \(\tau_n : \mathrm{Sent}(T) \to \mathrm{Form}_{\mathrm{prop}}\);
- \(q : \mathbb N\times\mathbb N \to \mathbb N\) limitante.

**Hipótese (Q):**

\[
\forall n\,\forall \varphi\,\forall m:\quad
\bigl[\pi \text{ é } P\text{-prova de } \tau_n(\varphi) \wedge |\pi| = m\bigr]
\Longrightarrow
\exists \pi'\,\bigl[\pi' \text{ é } T\text{-prova de } \varphi \wedge |\pi'| \le q(n,m)\bigr].
\]

**Corolário (transferência de limite inferior).** Se toda \(T\)-prova de \(\varphi\) tem comprimento \(\ge L(n)\), então toda \(P\)-prova de \(\tau_n(\varphi)\) tem comprimento \(m\) com \(q(n,m) \ge L(n)\); em particular

\[
m^*(n) := \min\{\, m : q(n,m) \ge L(n) \,\}.
\]

Um \(L(n) = 2^{c\cdot h(\alpha)\cdot n}\) **só** vira limite inferior proposicional se \(q\) crescer no máximo polinomialmente em \(m\). Sem \((\tau_n,q)\): **nenhum** limite inferior exponencial decorre da incompletude.

### 1.2. Classificação

| Item | Classe |
|------|--------|
| Existência de \((\tau_n,q)\) para o par \((T,P)\) de interesse | **ABERTO (Q1)** |
| Corolário condicional acima | **TEOREMA** (se Q vale — lógica elementar) |
| Q4 (separação Cutting Planes/Frege só com incompletude) | **bloqueado em Q** |
| T4–T6 antigos (escala exponencial) | **REJEITADOS** — não usam Q |

### 1.3. Lean (Core, sem Mathlib) — esqueleto condicional

Ver `lean4/Gothic_Generators/Core.lean` seção `TransferQ`:

```lean
structure TransferQ where
  PropForm := Nat
  tau : Nat → Nat → Nat          -- tau n φ : código da tradução
  qbound : Nat → Nat → Nat       -- q n m
  -- P-prova de τ_n(φ) com |π|=m ⇒ ∃π', T-prova de φ com |π'|≤q n m
  lifts : ∀ n φ m, PropProof 1 (tau n φ) m → PropProof 1 φ (qbound n m)
```

(O campo `lifts` é a hipótese **Q**; o corolário de limite inferior é provado
a partir de `lifts` — ver Core.)

---

## 2. Gödel II reificado — Φw*

### 2.1. Duas rotas (Foundation)

| Rota | Definição | Status |
|------|-----------|--------|
| **A (canônica, suficiente p/ Gödel II)** | `Φw* := T.consistent.val` | `T ⊢ Φw* 🡘 T.consistent` = **rfl**; `consistent_unprovable` ⇒ `T ⊬ Φw*` |
| **B (padding w*, 09 §12)** | `Φw*` = internalização de `∀x, prefix w* x → ¬∃p,z Proof∧pad` | **ABERTA** — exige `definability` + lema de entailment (padrão `FGH.lean`) |

**Rota A está escrita** em `FoundationBridge/GodelSecond.lean`
(needs `lake build` FoundationBridge — Mathlib cache).

### 2.2. Veredito honesto

- Gödel II **já existe** no Foundation (`Second.lean:19`): `T ⊬ T.consistent.val`;
- A "prova de que Φw* ≡ Con" na rota A é **trivial** (mesma sentença);
- O conteúdo não-trivial (padding/prefixo) permanece na **rota B** = ABERTO;
- Prop-level: `lemma3_con_for` (PR25) já fecha `PhiStar' ↔ T.Consistent ℕ`.

---

## 3. Bridge δ — Core (verificável agora)

### 3.1. Por que não há identidade de tipos

| Lado | Tipo |
|------|------|
| `PhiStar'` / `Lemma3Hyp.PhiStar` | `Prop` (testemunhas/prefixo) |
| `covered` / `delta` | `Bool`/`Nat` sobre `Obligation` finita |

`covered` **não** menciona provabilidade; codifica Gödel II como
**κ = σ_T + 1** (não coberto em T; coberto em T' com σ' ≥ σ+1).

### 3.2. Camada Core (`Realizes` + lemas)

- `wStarObl T` : obrigação `idx="w*"`, `kappa = T.sigma+1`, `isTrue=true`
- `wStarObl_not_covered` : Gödel II finito ⇒ `covered T b = false`
- `wStarObl_covered_of_sigma` : `T'` mais forte ⇒ coberta
- `delta_ge_one_of_true_uncovers` : verdadeira + não coberta ⇒ `δ ≥ 1`
- junção com `theorem4_strict` / `allCovered_iff_delta_zero`

**Camada Foundation** (descarregar `Realizes` campos com Prf/pad) = ABERTO
até build FoundationBridge.

---

## 4. MathOverflow — PERGUNTA (rascunho; não postar sem confirmação)

**Arquivo:** `27_MATHOVERFLOW_PERGUNTA.md`
**Tag:** `proof-theory`
**Formato:** pergunta, **não** "novo teorema"; originalidade não reivindicada.

---

## 5. Próximos

1. `lake build` Core com seção `TransferQ` + bridge δ — **obrigatório EXIT=0**
2. `cd FoundationBridge && lake exe cache get && lake build` — rota A
3. Rota B (padding reificado) — ABERTO
4. MathOverflow: **publicar só com confirmação explícita** do autor
5. Nenhum limite inferior antes de Q com \((\tau_n,q)\) concretos

---

## 6. Arquivos

- `lean4/Gothic_Generators/Core.lean` — `TransferQ`, bridge δ
- `FoundationBridge/GodelSecond.lean` — rota A
- `27_MATHOVERFLOW_PERGUNTA.md` — rascunho
- `04_questoes...` Q1 — já reformulado (PR26)

# 15 — Formalização Lean 4 (PR15): Lema 3, Teorema 4, RCS

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **PR22: `lake build` LIMPO — delta_mono, theorem4_strict, rcs_exists VERIFICADOS pela máquina; lemma3=axiom (único axioma); zero sorry**
**Arquivo:** `lean4/Gothic_Generators/Core.lean`

---

## 1. Objetivo

Transformar em Lean 4:
1. **Lema 3:** Φ_T^{w*} ↔ Con(T)
2. **Teorema 4:** δ_T=1, δ_T'=0 (sob hipóteses)
3. **Teorema 2:** monotonicidade δ
4. **Resultado 13/RCS:** ∃α,b. δ_F ≠ δ_S

---

## 2. O que foi criado

| Item | Lean | Status |
|------|------|--------|
| Obligation, Theory | structures | **OK** (abstração finita; `deriving DecidableEq`) |
| covered, delta | defs | **OK** (`decide` sobre Prop) |
| delta_mono (Teo 2) | theorem | **VERIFICADO** (`lake build` PR22) |
| lemma3_con | theorem | **AXIOM** (`lemma3_axiom` — pendente Foundation/pad-Prf) |
| theorem4_strict | theorem | **VERIFICADO** (h1–h8; `lake build` PR22) |
| rcs_exists | theorem | **VERIFICADO** (2≤fastStep, 1≤slowStep; α=⌈κ/fastStep⌉, b=κ+1; `lake build` PR22) |
| example δ_F=0 ∧ δ_S=1 | example | **native_decide VERIFICADO** |

**Toolchain:** Lean 4.34.0 + Lake 5.0.0 (`lean-toolchain`, `lakefile.toml`); só `Init` (sem Mathlib).

---

## 3. Dependências restantes

1. **Foundation (Saitou–Noguchi)** ou equivalente: `Prf`, `Con`, aritmética (para `lemma3_con`)
2. Formalizar `pad` e Φ^w (quantificadores)
3. ~~Provar monotonia de filtros em List (delta_mono)~~ **FEITO** (PR18)
4. ~~Fechar `theorem4_strict` e `rcs_exists`~~ **FEITO** (PR21)
5. ~~Instalar toolchain e rodar `lake build`~~ **FEITO** (PR22 — build limpo)

**Estimativa (do 05_lean4):** 14–22 semanas para completo.

---

## 4. Honestidade

- **NÃO** é certificação total (`lemma3_con` é axiom — único axioma aceito);
- Abstração `Obligation` **não** é a fórmula aritmética completa;
- `example` com `native_decide` só valida a **instância numérica** do modelo 13;
- `delta_mono`/`theorem4_strict`/`rcs_exists` são provas verificadas **no modelo finito** (não em PA aritmética).

---

## 5. Próximos (PR22 cont.)

1. Integrar Foundation para `lemma3_con` (axiom → prova);
2. Formalizar `pad` e Φ^w;
3. Cenário RBT explícito w* ≠ w₀' (condição B);
4. Comparar Freund–Pakhomov.

---

## 6. Arquivos

- `lean4/Gothic_Generators/Core.lean`
- Relacionado: `05_verificacao_lean4.md` (plano antigo)

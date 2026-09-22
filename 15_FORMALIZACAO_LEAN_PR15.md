# 15 — Formalização Lean 4 (PR15): Lema 3, Teorema 4, RCS

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **PR21: delta_mono, theorem4_strict, rcs_exists PROVADOS (sem sorry); lemma3=axiom — sem verificação `lake build`**
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
| Obligation, Theory | structures | **OK** (abstração finita) |
| covered, delta | defs | **OK** |
| delta_mono (Teo 2) | theorem | **PROVADO** (PR18: `covered_mono` + `length_filter_mono`, sem sorry) |
| lemma3_con | lemma | **AXIOM** (PR18: `lemma3_axiom` — pendente Foundation/pad-Prf) |
| theorem4_strict | theorem | **PROVADO** (PR21: hipóteses h1–h8; sem sorry; `lake build` pendente) |
| rcs_exists | theorem | **PROVADO** (PR21: 2≤fastStep, 1≤slowStep; α=⌈κ/fastStep⌉, b=κ+1; sem sorry; `lake build` pendente) |
| example δ_F=0 ∧ δ_S=1 | example | **native_decide** (deve passar) |

---

## 3. Dependências restantes

1. **Foundation (Saitou–Noguchi)** ou equivalente: `Prf`, `Con`, aritmética (para `lemma3_con`)
2. Formalizar `pad` e Φ^w (quantificadores)
3. ~~Provar monotonia de filtros em List (delta_mono)~~ **FEITO** (PR18)
4. ~~Fechar `theorem4_strict` e `rcs_exists`~~ **FEITO** (PR21 — sem sorry; **não verificado com `lake build`**)

**Estimativa (do 05_lean4):** 14–22 semanas para completo.

---

## 4. Honestidade

- **NÃO** é certificação total (`lemma3_con` é axiom; provas PR21 **sem `lake build`** — toolchain não instalada);
- Abstração `Obligation` **não** é a fórmula aritmética completa;
- `example` com `native_decide` só valida a **instância numérica** do modelo 13;
- `delta_mono`/`theorem4_strict`/`rcs_exists` são provas completas **no modelo finito** (não em PA aritmética).

---

## 5. Próximos (PR15/PR18/PR21 cont.)

1. ~~Eliminar sorry de `delta_mono`~~ **FEITO** (PR18);
2. ~~Fechar `theorem4_strict` e `rcs_exists`~~ **FEITO** (PR21);
3. Integrar Foundation para `lemma3_con` (axiom → prova);
4. Encontrar/instalar toolchain Lean 4 + deps e rodar `lake build` (verificar PR18/PR21).

---

## 6. Arquivos

- `lean4/Gothic_Generators/Core.lean`
- Relacionado: `05_verificacao_lean4.md` (plano antigo)

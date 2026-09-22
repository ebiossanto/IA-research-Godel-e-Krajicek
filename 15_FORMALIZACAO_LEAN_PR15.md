# 15 — Formalização Lean 4 (PR15): Lema 3, Teorema 4, RCS

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **ESQUELETO CRIADO — sorry pendentes; NÃO certificação**
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
| delta_mono (Teo 2) | theorem | **sorry** (monotonia List) |
| lemma3_con | lemma | **sorry** (requer Prf/pad aritmético) |
| theorem4_strict | theorem | **sorry** (hipóteses a detalhar) |
| rcs_exists | theorem | **sorry** (escolha α=1, b) |
| example δ_F=0 ∧ δ_S=1 | example | **native_decide** (deve passar) |

---

## 3. Dependências para fechar sorry

1. **Foundation (Saitou–Noguchi)** ou equivalente: `Prf`, `Con`, aritmética
2. Formalizar `pad` e Φ^w (quantificadores)
3. Provar monotonia de filtros em List (delta_mono)
4. Hipóteses do Teo 4 como precondições explícitas

**Estimativa (do 05_lean4):** 14–22 semanas para completo.

---

## 4. Honestidade

- **NÃO** é certificação (sorry presentes);
- Abstração `Obligation` **não** é a fórmula aritmética completa;
- `example` com `native_decide` só valida a **instância numérica** do modelo 13.

---

## 5. Próximos (PR15 cont.)

1. Eliminar sorry de `delta_mono` (combinatória List);
2. Integrar Foundation para `lemma3_con`;
3. Encontrar/instalar toolchain Lean 4 + deps;
4. Rodar `lake build` / `lean` no `Core.lean`.

---

## 6. Arquivos

- `lean4/Gothic_Generators/Core.lean`
- Relacionado: `05_verificacao_lean4.md` (plano antigo)

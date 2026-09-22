# 19 — PPR-3: Θ sobre Provas de Ramos (CC-Θ no Modelo Finito)

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **EXECUTADO — CC-Θ VERIFICADO 32/32; Θ polinomial no modelo finito**
**Script:** `ppr3_ramos_theta.py`
**Depende de:** `14_...` §4 (design Θ ramos), `17_...` (predicado A∨B∨C), `11_...` §3 (CC-Θ), `18_...` (E0–E3)

---

## 1. Definição (PPR-3 sobre ramos)

**PPR-3-ramo:** dado π = certificado de "w₀ não-coberto em T" (ramo ativo),
Θ(π) deve ser certificado válido para a claim-alvo em T' sob (A)∨(B)∨(C):

| Cond | Significado | Θ(π) emite |
|------|-------------|-------------|
| **(A)** | R(w₀) ∈ uncov(T') | certificado uncov(R(w₀)) @ T' |
| **(B)** | transição RBT (w₀≠w₀', R(w₀)=w*) | certificado uncov(w₀') @ T' |
| **(C)** | T' = ALL_COV | certificado ALL_COV @ T' |

**CC-Θ (condição de correção):** Θ é correto sse
1. o certificado emitido é **válido** (claim verdadeira em T');
2. a condição correspondente (A/B/C) **vale**;
3. **cota polinomial:** |Θ(π)| ≤ |π| + O(log |W|).

---

## 2. Implementação (`ppr3_ramos_theta.py`)

- **Certificados finitos:** tuplas (claim, w, σ, b, κ) — tamanho O(log|W| + log σ + log b);
- **Θ:** decide A/B/C e emite o cert correspondente;
- **verify_theta:** valida cert + cota |Θ(π)| ≤ |π| + ⌈log|W|⌉ + 4;
- **Cenários:** 3 transições PR17 + 4 configs E0–E3 (α=1, b∈{2,3,4,5,8}).

---

## 3. Resultado (EXECUTADO 22/09/2026)

| Cenário | π processados | CC-Θ |
|---------|---------------|------|
| PR17 σ0→σ2 | 4 | **4/4** |
| PR17 σ1→σ2 | 4 | **4/4** |
| PR17 σ0→σ1 | 4 | **4/4** |
| E0 σ1→σ2 | 5 | **5/5** |
| E1 σ1→σ2 | 5 | **5/5** |
| E2 σ1→σ3 | 5 | **5/5** |
| E3 σ1→σ2 | 5 | **5/5** |
| **TOTAL** | **32** | **32/32** |

**Condições disparadas:** A=14, B=0, C=18, FAIL=0
**Máx |Θ(π)|/|π|:** 1.11 (cota respeitada)

**Veredito PR19: CC-Θ VERIFICADO no modelo finito; Θ polinomial.**

---

## 4. Análise honesta

| Item | Status |
|------|--------|
| Θ sobre provas de ramos | **CONSTRUÍDO e CORRETO** (32/32) |
| Cota | **POLINOMIAL:** \|Θ(π)\| = \|π\| + O(log \|W\|) |
| Condição (B) RBT | **0 disparos** neste setup — testar com w* ≠ w₀' explícito |
| PA real / provas de FOL | **ABERTO** — modelo κ/σ, não pad-Prf |
| suffix0 (11) | **VÁCUO/abandonado** — Θ de ramos é o sucessor |
| PPR completo (08 R3) | **ABERTO** |

**Limitação:** certificados são estruturais (não provas LK/NBQ). Generalizar:
(1) formalizar π como sequente de cobertura; (2) Θ como transformação de regras.

---

## 5. Comparação com 11 (suffix0)

| | suffix0 (11) | R_w ramos (19) |
|--|--------------|----------------|
| R opera em | strings b (n+1) | índices w |
| PPR-2 | **VÁCUO** (tamanho n+2) | **PASSA** (A∨B∨C) |
| Θ | enum O(2^n) | **cert O(log \|W\|)** |
| CC-Θ | não provada | **VERIFICADA 32/32** |

---

## 6. Próximos

1. ~~Θ sobre provas de ramos~~ — **FEITO** (PR19, CC-Θ 32/32)
2. Testar (B) com cenário RBT explícito (w* ≠ w₀')
3. Formalizar π/Θ em Lean (sequentes de cobertura)
4. Fechar sorries theorem4/rcs; Foundation lemma3

---

## 7. Arquivos

- `ppr3_ramos_theta.py` — script PR19
- `test_Rw_ppr2_E0E3.py` — PR20 (PPR-2 em E0–E3)
- `14_...` §4, `17_...`, `11_...` §3 — fundamentação

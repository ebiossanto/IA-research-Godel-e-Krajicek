# 23 — Condição (B) RBT Explícita: w* ≠ w₀' (PPR-2 + CC-Θ)

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **EXECUTADO — cond. (B) NÃO-VÁCIA: 10 disparos; PPR-2 20/20; CC-Θ 20/20**
**Script:** `test_Rw_ppr2_RBT_B.py`
**Depende de:** `14_...` §7 (ABERTO cond. B), `17_...` §2 (predicado), `19_...` (Θ), `18_...` (B=0)

---

## 1. Por que (B) era sempre 0

Nos testes PR17/19/20:

1. `W_STAR = '00'` é **prefixo**, mas a condição compara `r_w0 == w_star` com **palavra completa** de comprimento r → nunca igual;
2. `R` identidade só emite `w*` se `w₀` **já for** `w*` (ou o sentinela ALL, tratado à parte).

Resultado: **B=0** em 32 cenários PR19 e em E0–E3.

---

## 2. Construção explícita (RBT parcial, não ALL)

| Item | Valor |
|------|-------|
| W | {0,1}⁴ (16 ramos) |
| w* | **'1000'** (palavra completa, não prefixo) |
| κ | `0xxx → 0`; `w* → 1`; `1xxx \ {w*} → 2` |
| T (σ=0, b≥2) | 0xxx cobertos; w* não-coberto → **w₀ = '1000' = w*** |
| T' (σ=1, b≥2) | w* coberto; '1001'+ não-coberto → **w₀' = '1001' ≠ w*** |
| R | identidade (+ sentinela ALL→w* como em 14 §3) |

**RBT parcial:** o primeiro ramo ativo **muda** de w* para o sucessor lex `'1001'`,
sem cobertura total — o caso intermediário que (C) não cobre.

---

## 3. Resultado (EXECUTADO 22/09/2026)

Varredura: pares σ→σ' ∈ {(0,1),(0,2),(1,2),(1,3)} × b ∈ {2,3,4,5,8}.

| Métrica | Valor |
|---------|-------|
| PPR-2 (A∨B∨C) | **20/20** |
| Cond. **(B)** com w₀≠w₀' ∧ R(w₀)=w* | **10** (6 puros B + 4 B+C) |
| Casos **puros (B)** (A=F, C=F) | **6** (σ 0→1 todos b + σ 0→2 b=2) |
| CC-Θ (Θ correto + cota) | **20/20** (sob (B): 6) |
| FAIL | **0** |

**Exemplo canônico (B puro):** σ 0→1, qualquer b:
`w₀=1000`, `w₀'=1001`, `R(w₀)=1000=w*`, A=F, C=F → **OK(B)**;
Θ emite certificado uncov('1001')@σ' → **CC-Θ OK**.

---

## 4. Análise honesta

| Item | Status |
|------|--------|
| Cond. (B) RBT | **NÃO-VÁCIA** — 10 disparos explícitos |
| w* ≠ w₀' | **CONFIRMADO** ('1000' → '1001') |
| RBT parcial (sem ALL) | **TESTADO** — distinto de (C) |
| PPR-2 + CC-Θ sob (B) | **PASSA** no modelo finito |
| Causa raiz do B=0 anterior | **prefixo vs palavra completa** + R identidade |
| PA real / pad-Prf | **ABERTO** (caveat padrão) |

**Limite:** κ explícito é construído para forçar o cenário — não é o κ natural
dos experimentos 10/13; serve para validar o **predicado**, não para afirmar
frequência de RBT em PA.

---

## 5. Próximos passos

1. ~~Cond. (B) RBT explícito (w* ≠ w₀')~~ — **FEITO** (PR23)
2. Generalizar (C): quando ALL_COV é inevitável (σ_T' ≥ max κ)
3. Foundation para `lemma3_con` (Prf/pad)
4. Comparar Freund–Pakhomov (comprimento vs δ)

---

## 6. Arquivos

- `test_Rw_ppr2_RBT_B.py` — cenário + PPR-2 + Θ
- Atualiza: `14` §7.6, `17` §6.6, `18` §7.4, `19` §4/§5.2

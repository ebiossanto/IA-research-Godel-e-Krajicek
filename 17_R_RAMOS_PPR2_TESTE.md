# 17 — R_w Testado: PPR-2 sobre Ramos (refinamento pós-falha)

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** TESTADO — R_w identidade+sentinela PASSA PPR-2 (3 cenários) com refinamento
**Depende de:** `14_...` (design R_w), `10_...` (RBT), `08_...` (PPR), `13_...`/`16_...` (RCS)
**Script:** `test_Rw_ppr2.py`

---

## 1. Motivo do refinamento (após 14 §7)

Candidato original (14 §3):

\[
R(\bot_{\text{all}}) = w^\star,\quad R(w) = w
\]

**Predicado PPR-2 original (14 §5):** se w não coberto em T, então R(w) não coberto em T' **ou** R(w)=w* com falta RBT em T'.

**Falha observada (σ→ALL_COV):** quando T' cobre **tudo**, `uncov(T')=∅` → R(w) nunca ∈ uncov(T') e falta RBT **não existe** (ALL_COV). Predicado original **insuficiente** para transição → ALL_COV (ex.: exp.10 0000→ALL_COV).

---

## 2. Refinamento: predicado PPR-2-ramo (3 condições)

Para cada b, seja w₀ = primeiro não-coberto em T (ramo ativo).

| Cond | Significado |
|------|-------------|
| **(A)** | R(w₀) ∈ uncov(T') — transferência direta do ramo |
| **(B)** | w₀ ≠ w₀' ∧ R(w₀)=w* — transição RBT registrada |
| **(C)** | w₀' = ALL_COV — **cobertura total** em T' resolve w₀ de T (progresso trivial) |

\[
\text{PPR-2-ramo} \iff (A) \lor (B) \lor (C)
\]

**(C) é novo:** captura "reflection resolve tudo" (RBT: w₀→ALL). Sem (C), R_w identidade falha sempre que T'=ALL_COV.

---

## 3. Resultado (`test_Rw_ppr2.py`)

| Cenário | σ_T→σ_T' | b=2,3,4,8 | PPR-2 |
|---------|----------|-----------|-------|
| 1 | 0→2 (PA→PA+Con) | b≥3: T'=ALL → **(C)** | **TRUE** |
| 2 | 1→2 (slow→fast) | b≥3: T'=ALL → **(C)** | **TRUE** |
| 3 | 0→1 (PA→PA+Con_s) | b=2: **(A)**; b≥3: **(A)** | **TRUE** |

**Veredito PR17: R_w (identidade+sentinela) PASSA PPR-2 em 3/3 cenários** com predicado refinado.

---

## 4. Análise honesta

| Item | Status |
|------|--------|
| R_w identidade+sentinela | **TESTADO — PASSA** (com (C)) |
| Predicado original 14 §5 | **REFINADO** (faltava caso ALL_COV) |
| Condição (C) | **Ad hoc?** Não: é exatamente RBT 0000→ALL_COV (exp.10) |
| PPR-3 (Θ provas) | **ABERTO** (08 R3, 14 §4) |
| PPR completo | **ABERTO** |

**Limitação:** teste é no modelo κ/σ (proporcional/estrutural), não sobre provas PA reais. Coerente com caveats 09/10/13.

---

## 5. Conexão com RCS (13/16)

RCS: δ_F ≠ δ_S com **mesma Φ**, diferenças em **quais w** cobertos.

PPR-2-ramo mostra: o ramo ativo w₀ de T transfere para T' via R com progresso (A/B/C). A **magnitude** da diferença δ (RCS) não é capturada por R_w pontual — PPR opera em **transferência de cobertura**, não em **contagem**. Complementares, não concorrentes.

---

## 6. Próximos passos (14 §7 atualizado)

1. ~~Implementar R_w~~ — **FEITO** (PR17)
2. ~~Verificar PPR-2 ramos~~ — **FEITO** (3/3 TRUE)
3. Generalizar (C): caracterizar quando ALL_COV é inevitável (σ_T' ≥ max κ)
4. PPR-3: Θ sobre provas de ramos (14 §4) — ABERTO
5. Testar R_w nos cenários E0–E3 do 16 (RCS robusta)

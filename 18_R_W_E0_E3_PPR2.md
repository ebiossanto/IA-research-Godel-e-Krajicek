# 18 — R_w nos Cenários E0–E3: PPR-2 com RCS Robusta (PR20)

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **EXECUTADO — R_w PASSA PPR-2 em 4/4 cenários E0–E3**
**Script:** `test_Rw_ppr2_E0E3.py`
**Depende de:** `14_...` (design), `17_...` (predicado refinado), `16_...` (RCS robusta)

---

## 1. Motivo

PR17 testou R_w em 3 transições σ fixas (cenários PA→Con). PR20 pergunta:

> O predicado refinado (A)∨(B)∨(C) e R_w identidade+sentinela continuam válidos
> nas **variações de κ, razão slow:fast e |W|** onde a RCS é robusta (E0–E3)?

---

## 2. Setup

Para cada config E0–E3 (`test_Rw_ppr2_E0E3.py`):

1. **Reproduz pares RCS:** contagem de (α,b) com δ_F ≠ δ_S (replica PR16);
2. **PPR-2 slow→fast:** nos pares RCS, testa R_w na transição σ_S → σ_F;
3. **PPR-2 genérico:** varredura σ → σ+fast_step para todo σ e b∈{2,3,4,5,8}.

Predicado: **(A)** R(w₀)∈uncov(T') ∨ **(B)** transição RBT com R(w₀)=w* ∨ **(C)** T'=ALL_COV.

---

## 3. Resultados (EXECUTADO 22/09/2026)

| Config | RCS pares | PPR-2 slow→fast | PPR-2 genérico | Veredito |
|--------|-----------|-----------------|----------------|----------|
| **E0** base | 4/35 | **4/4 OK** | **65/65 OK** | **PASSA** |
| **E1** κ rich | 7/35 | **7/7 OK** | **65/65 OK** | **PASSA** |
| **E2** 3:1 | 4/35 | **4/4 OK** | **95/95 OK** | **PASSA** |
| **E3** \|W\|=64 | 4/35 | **4/4 OK** | **65/65 OK** | **PASSA** |

**Exemplo E0:** α=1, b=3: dS=4, dF=0 (σ_S=1 → σ_F=2); condição **(C)** (T'=ALL_COV).

**Veredito PR20: R_w PASSA PPR-2 em todos os cenários E0–E3.**

---

## 4. Análise honesta

| Item | Status |
|------|--------|
| R_w + predicado (A∨B∨C) | **TESTADO em 4/4 configs** (PR17+PR20) |
| Robustez a κ/razão/\|W\| | **SIM** — não artefato de config única |
| PPR-3 (Θ provas) | **FEITO** (19, PR19: CC-Θ 32/32) |
| PPR completo (R3) | **ABERTO** (08) |
| Natureza | Modelo κ/σ estrutural — **não** PA real |

**Limitação:** condições (A)/(C) dominam; (B) rara neste modelo (exige w* ≠ w₀'). Generalizar (C): ALL_COV inevitável quando σ_T' ≥ max κ.

---

## 5. Conexão com RCS (13/16)

- RCS: **magnitude** δ_F ≠ δ_S com mesma Φ;
- PPR-2: **transferência** do ramo ativo w₀ via R_w;
- Complementares: RCS conta défices; R_w move o primeiro não-coberto.

---

## 6. Próximos

1. ~~Testar R_w em E0–E3~~ — **FEITO** (PR20)
2. ~~PPR-3: Θ sobre provas de ramos (14 §4)~~ — **FEITO** (PR19, CC-Θ 32/32)
3. Caracterizar quando ALL_COV é inevitável (σ ≥ max κ)
4. Cond. (B) RBT explícito (w* ≠ w₀')
5. Fechar sorries Lean (theorem4, rcs); Foundation lemma3

---

## 7. Arquivos

- `test_Rw_ppr2_E0E3.py` — script PR20
- `test_Rw_ppr2.py` — script PR17 (base)
- `slow_vs_fast_delta_ext.py` — configs E0–E3 (PR16)

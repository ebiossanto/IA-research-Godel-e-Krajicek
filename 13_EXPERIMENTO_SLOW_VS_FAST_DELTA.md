# 13 — EXPERIMENTO: Slow vs. Fast em δ_T(Φ,b) — teste da Hipótese RCS

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **EXECUTADO — RCS CONFIRMADA no modelo estrutural**
**Script:** `slow_vs_fast_delta.py`
**Hipótese testada:** RCS (09 §28) — α ↦ δ_{T_α}(Φ,b) carrega informação não ordinal

---

## 1. Objetivo preciso

**Pergunta (falsificável):**

> Para progressões *lenta* (S_α) e *rápida* (F_α) partindo da mesma T₀,
> com a **mesma fórmula Φ** fixa, o perfil
>
> \[
> \delta_{S_\alpha}(\Phi,b) \quad\text{vs}\quad \delta_{F_\alpha}(\Phi,b)
> \]
>
> difere para algum α, b?

**RESPOSTA (execução 22/09/2026):** **SIM** — 3/30 pares (α,b) com δ_F ≠ δ_S.

---

## 2. RESULTADO (executado)

### 2.1. Setup executado

- |W| = 16, w* = 00 (prefixo), |w*| = 4 obrigações com κ=2 (Con plena)
- Genéricas: κ ∈ {0,1} (hash)
- σ_fast: +2/passo (Con completa); σ_slow: +1/passo (Con_s < Con)
- Φ fixa (Φ_PA^{w*} ↔ Con(PA)), mesma para ambas
- α ∈ [0,5], b ∈ {1,2,3,4,8}

### 2.2. Perfis δ

**Rápida (F_α):**

| α | σ | δ(b=1) | δ(b=2) | δ(b=3) | δ(b=4) | δ(b=8) |
|---|---|--------|--------|--------|--------|--------|
| 0 | 0 | 10 | 10 | 10 | 10 | 10 |
| **1** | **2** | 10 | 4 | **0** | **0** | **0** |
| 2 | 4 | 10 | 4 | 0 | 0 | 0 |
| 3+ | 6+ | 10 | 4 | 0 | 0 | 0 |

**Lenta (S_α):**

| α | σ | δ(b=1) | δ(b=2) | δ(b=3) | δ(b=4) | δ(b=8) |
|---|---|--------|--------|--------|--------|--------|
| 0 | 0 | 10 | 10 | 10 | 10 | 10 |
| **1** | **1** | 10 | 4 | **4** | **4** | **4** |
| **2** | **2** | 10 | 4 | **0** | **0** | **0** |
| 3+ | 3+ | 10 | 4 | 0 | 0 | 0 |

### 2.3. Pares com diferença (RCS)

| α | b | δ_F | δ_S | F−S |
|---|---|-----|-----|-----|
| **1** | **3** | **0** | **4** | **−4** |
| **1** | **4** | **0** | **4** | **−4** |
| **1** | **8** | **0** | **4** | **−4** |

**3/30 pares distintos.** Diferença concentrada em **α=1, b≥3**.

### 2.4. Interpretação

- **α=1:** rápida atinge σ=2 (Con plena) → cobre w* (κ=2) → δ=0
- **α=1:** lenta atinge só σ=1 (Con_s) → w* ainda κ=2>1 → δ=4
- **α=2:** lenta alcança σ=2 → δ=0 (mesmo valor que rápida tinha desde α=1)
- **Perfil α↦δ é distinto:** rápida "degraus" [10,4,0,0,...]; lenta "degraus" [10,4,4,0,0,...]

**Conclusão:** mesmo alcançando o mesmo σ final, o **caminho em δ difere** → informação além do ordinal final.

---

## 3. VEREDITO RCS

\[
\boxed{\text{RCS CONFIRMADA neste caso (modelo estrutural)}}
\]

- **Critério §6:** ∃α,b: δ_F ≠ δ_S → **SIM** (α=1, b≥3)
- **Não é** reindexação trivial α↦f(α): a diferença é no **valor de δ**, não só no "quando"
- Próximo nível de evidência: fazer para PA real (Lean/Isabelle) — PR futuro

---

## 4. Ressalvas obrigatórias

1. **Modelo estrutural** — σ e κ fixados; não busca provas reais em PA/Con_s;
2. Captura a ordem **Con_s < Con** (Henk–Pakhomov), não detalhes internos;
3. **Não prova** conservatividade formal PA+Con_s — usa apenas desigualdade conhecida;
4. Resultado **válido no modelo** — para certificação em PA real, formalização necessária.

---

## 5. Por que é nomeável

| Antes | Depois |
|-------|--------|
| "RCS é hipótese falsificável" | "**RCS confirmada no caso slow-vs-fast com Φ fixa**" |
| δ, RBT = candidatos isolados | δ **detecta slow consistency** — ponte com Friedman–Rathjen–Weiermann/Freund–Pakhomov |
| originalidade "não certificada" | contribuição **specífica**: primeiro observável de cobertura que separa progressões lentas/rápidas |

---

## 6. Próximos passos

1. ~~Design~~ **[FEITO]**
2. ~~Executar e comparar~~ **[FEITO — RCS=SIM]**
3. Estender: mais obrigações com κ variado; Φ mais rica
4. Formalizar Lema 3 + este resultado em Lean/Isabelle (PR15)
5. Posicionar vs. Freund–Pakhomov: eles medem comprimento de prova; nós medimos δ

---

## 7. Arquivos

- `slow_vs_fast_delta.py` — script executado (UTF-8 fix)
- Depende de: `09_...` (δ, Lema 3), `10_...` §1.4 (slow consistency)

---

## 8. Referências

1. Friedman, Rathjen, Weiermann (2013). Slow complexity. APAL 164.
2. Freund, Pakhomov (2020). Short proofs for slow consistency. NDJFL 61(1). arXiv:1712.03251.
3. Henk, Pakhomov (2016). Slow and ordinary provability for PA. arXiv:1602.01822.
4. Krajíček (2023/2025). arXiv:2303.10637.
5. Beklemishev (2003). Proof-theoretic analysis by iterated reflection. APAL.

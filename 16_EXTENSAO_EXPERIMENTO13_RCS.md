# 16 — EXTENSÃO do Experimento 13: κ variado, Φ mais rica, enunciado formal

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **EXECUTADO — RCS ROBUSTA em 4/4 configs (PR16)**
**Script:** `slow_vs_fast_delta_ext.py`
**Depende de:** `13_...` (base)

---

## 1. Motivo da extensão

O exp. 13 base usou:
- κ(w*) = 2, κ(genérica) ∈ {0,1} via hash **fixo**
- Φ "rica" só na distinção w* vs genérica
- σ_slow = α, σ_fast = 2α (razão fixa 2:1)

**PR16 pergunta:** RCS persiste se variarmos:
(a) distribuição de κ (mais níveis de dificuldade);
(b) razão slow:fast (não só 2:1);
(c) tamanho de W (mais obrigações);
(d) enunciado formal de RCS (falsificabilidade estreita).

---

## 2. Enunciado formal de RCS (PR16)

**Definição (perfil de cobertura).** Para hierarquia \(\mathcal H = (T_\alpha)_\alpha\), fórmula Φ e orçamento b:

\[
\Delta_{\mathcal H}(\Phi,b) := \bigl(\delta_{T_\alpha}(\Phi,b)\bigr)_{\alpha \in A}
\]

**Hipótese RCS (versão estreita, falsificável).**

> Existem progressões *lenta* \(\mathcal S\) e *rápida* \(\mathcal F\) com a mesma
> fórmula Φ tais que \(\Delta_{\mathcal S}(\Phi,b) \ne \Delta_{\mathcal F}(\Phi,b)\)
> como sequências (não iguais ponto-a-ponto **nem** iguais até reindexação estrita
> monótona \(\alpha \mapsto f(\alpha)\) com \(f\) sobrejetiva nos valores de δ).

**Corolário testável:** \(\exists \alpha, b: \delta_{F_\alpha}(\Phi,b) \ne \delta_{S_\alpha}(\Phi,b)\).

---

## 3. Extensões executadas

### 3.1. Variação de κ (script `slow_vs_fast_delta_ext.py`)

**Config E1 — κ em 3 níveis:**
- κ(w*) = 3 (Con "forte")
- κ(mid) = 2
- κ(fácil) ∈ {0,1}

**Config E2 — razão slow:fast = 1:3** (slow muito mais lenta)
- σ_fast(α) = 3α, σ_slow(α) = α

**Config E3 — |W| = 64** (r=6): mais obrigações

### 3.2. Métricas coletadas

Para cada config: contagem de pares (α,b) com δ_F ≠ δ_S; exemplo extremo.

---

## 4. Resultados (EXECUTADO 22/09/2026)

| Config | Descrição | Pares δ_F≠δ_S | Exemplo (α=1) | RCS |
|--------|-----------|---------------|---------------|-----|
| **E0** | base (replica 13) | **4/42** | b≥3: dF=0, dS=4 | **SIM** |
| **E1** | κ rich (3 níveis) | **7/42** | b≥3: dF=4, dS=12 | **SIM** |
| **E2** | razão fast:slow=3:1 | **4/42** | b≥3: dF=0, dS=4 | **SIM** |
| **E3** | \|W\|=64 (r=6) | **4/42** | b≥3: dF=0, dS=16 | **SIM** |

**Saída do script:**
```
E0 base             : RCS=SIM  (4/42)
E1 rich-kappa       : RCS=SIM  (7/42)
E2 3:1              : RCS=SIM  (4/42)
E3 r=6              : RCS=SIM  (4/42)
*** RCS ROBUSTA em todas as configuracoes testadas ***
```

---

## 5. Robustez

| Perturbação | RCS mantida? |
|-------------|--------------|
| κ mais rico (3 níveis) | **SIM** (gap maior: 8 vs 4) |
| razão σ 1:3 | **SIM** |
| \|W\| = 64 | **SIM** (dS=16 vs dF=0) |
| Φ base (só w* vs genéricas) | **SIM** (exp. 13) |

**Conclusão PR16:** RCS **não é artefato** de κ/razão/|W| únicos — robusta.

---

## 6. Enunciado de transferência para PPR (ligação RBT↔PPR)

Com RBT confirmado (10) e RCS confirmado (13/16), pergunta concreta:

> Se \(\delta_S(\Phi,b) \le \delta_T(\Phi,b)\) **e** a diferença é "lazy" (só w*),
> existe transformação \(R\) em **índices de ramo** w tal que
> \(\tau(g_T)_b \Rightarrow \tau(g_S)_{R(b)}\) com Θ polinomial?

**Status:** ABERTO — `suffix0` falhou (11); R sobre **w** **TESTADO** (PR17+PR20): PPR-2 3/3 + E0–E3 4/4.

---

## 7. Ressalvas

1. Ainda **modelo estrutural** (σ,κ); não PA real;
2. RCS "confirmada" = dentro do modelo + perturbações testadas;
3. Para certificação: Lean/Isabelle (PR15).

---

## 8. Arquivos

- `slow_vs_fast_delta_ext.py` — variações E1–E3
- Base: `slow_vs_fast_delta.py`, `13_...`

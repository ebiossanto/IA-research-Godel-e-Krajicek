# 33 — Ponte Prova → Fractal (D4′ v6 / r6): estratos exatos do `relinc` + consolidação da linha

**Data:** 22/11/2026 · **Classificação:** **(P)** experimento próprio + **(C)**
hipóteses **pré-registradas** · **Nível Ten-Proofs:** N1 + N2 · **Não** é lower
bound; **não** é claim de EF.

> **PROTOCOLO DE PRIORIDADE TEMPORAL:** hipóteses, margens, regras e a correção
> de método deste documento e do script `gk_proof_fractal_v6.py` foram fixados e
> **commitados ANTES de qualquer execução** (re-análise H_E1 inclusa) — o hash
> do commit de pré-registro prova a ordem (C1). Selftests (S1–S7) executados
> antes do commit e repetidos no run.

**Linha:** `28_`(v1) → `29_`(r2) → `30_`(r3) → `31_`(r4) → `32_`(r5) → **este
(r6)** — rodada de **correção de método + consolidação** das pendências r5.

**Reproduzir:**
```powershell
python -u gk_proof_fractal_v6.py --selftest-only    # bateria S1-S7 (~5min)
python -u gk_proof_fractal_v6.py --reanalise-r5     # H_E1 (~5min)
python -u gk_proof_fractal_v6.py [--resume]         # coleta + análise (~2.5h)
python -u gk_proof_fractal_v6.py --analyze-only     # re-análise (~1.5h)
# → gk_proof_fractal_v6_series.csv + _contrasts.csv + 2 JSONs
#   + gk_proof_fractal_v6_reanalise_r5.json + _contrasts.csv
# seed=20261119 · seed_boot=20261126 · B=1000
```

---

## 1. Pré-registro (fixado antes de qualquer execução)

### 1.1 Pendências do r5 fechadas aqui

| Pendência r5 (referee/§6) | Solução r6 |
|---|---|
| **(i) estratos exatos do `relinc`** (A4: 5/6 discordantes em `relinc`; suspeita = aproximação `runs[0]−=1`) | **Correção de raiz:** `relinc` não é ponto-a-ponto → o bootstrap **reamostra a série primitiva `x`** nos estratos exatos de `x` e **recalcula `relinc` dentro de cada réplica** (e do jackknife) — sem fronteira a aproximar. `raw`/`log1p` (ponto-a-ponto) são **identicos** ao r5 (transformação comuta). Teste: **H_E1** (re-análise do CSV r5, mesmo dados) |
| **(ii) H_D2(a) redefinido** (A5: direção `+1` falhou 3×) | **(a) vira teste de EQUIVALENTE ±0,05**; direcionais boxdim caem para 4 → Bonferroni α=0,05/**4** |
| **(iii) tendência de `saltos`** (A1: magnitude caiu?) | **H_F1b: meta-análise de Cochran (Q, gl)** sobre as **4 rodadas** (r3+r4+r5 dos CSVs congelados + r6), peso 1/SE² — teste, não olho |
| **(iv) ramo concordante** (A3: 0 ocorrências no r5) | **H_F4:** contagem em dados novos; **0/135 de novo → recomendar remoção em r7** |
| **(v) smoke test como procedimento** (lição do bug do r5) | **S7 obrigatório em toda execução:** `analyze()` com `contrast()` stubado (135 contrastes, caminhos de fim) |
| (vi) n/MDE (r4) e método (r5) | mantidos: n=512, percentil+estratificado validado (S4–S6 re-executados) |

### 1.2 Dados — novos, disjuntos de r2..r5 (aborta se intersectar os quatro)

| Família | Grade r6 | Evitados |
|---|---|---|
| `implication` | m=3..6 × seeds **256..383** (512) | r2:0–15 · r3:16–31 · r4:32–127 · r5:128–255 |
| `cadeia` | k=3..6 × seeds **256..383** (512) | idem |
| `tau_tiny` | seeds **1024..1535** (512) | r2:0–63 · r3:64–127 · r4:128–511 · r5:512–1023 |

### 1.3 Hipóteses

**H_E1 — DIAGNÓSTICO DO FIX (re-análise do CSV r5 congelado — mesmos dados,
só o método muda):** discordância da variante `relinc` (45 contrastes) com
estratos exatos **≤ 1/45** (r5: 5/45). `CONFIRMADA` ≤1 · `PARCIAL` 2–4 ·
`REFUTADA` ≥5. *(Rodada de método — não é nova confirmação; os5 chaves
discordantes do r5 são listadas com seu status novo.)*

**H_F1 — SALTOS PRIMÁRIO (4ª rodada; mesmas 3 chaves/direções):**

| # | Chave | r3 | r4 | r5 | Esperado |
|---|---|---|---|---|---|
| (a) | `minref:imp−τ > 0` | +0,173 | +0,185 | +0,138 | d+1 |
| (b) | `drat:imp−cadeia > 0` | +0,110 | +0,117 | +0,080 | d+1 |
| (c) | `fonte:cadeia > 0` | +0,120 | +0,113 | +0,104 | d+1 |

Bonferroni α*=0,05/3. **H_F1a:** `CONFIRMADA` ⟺ 3/3 OK.
**H_F1b (tendência):** Cochran Q sobre as **4 rodadas** (r3/r4/r5 lidos dos
CSVs congelados + r6; peso 1/SE²) — **p > 0,05 → `SEM_HETEROGENEIDADE`**
(sem declínio detectável); p ≤ 0,05 → `HETEROGENEIDADE_REGISTRADA` (sem claim
de direção). *Caveat declarado: as rodadas mudam n e grades — Q captura a
variação total entre rodadas, não só declínio temporal.*

**H_F2 — BOXDIM SECUNDÁRIO (6 testes; (a) REDEFINIDO como eq):**
(a) `minref:imp−τ` **EQUIVALENTE ±0,05** (r5: FALHA −0,012; eq@0,05 passou lá) ·
(b) `minref:cadeia−τ > 0` (r5: OK_BONF +0,025) d+1 ·
(c) `minref:imp−cadeia` **EQUIVALENTE ±0,05** (r5: OK) ·
(d) `drat:imp−cadeia < 0` [pista] (r5: OK_BONF −0,068) d−1 ·
(e) `fonte:τ < 0` (r5: OK −0,037) d−1 ·
(f) `fonte:cadeia < 0` (r5: OK_BONF −0,051) d−1.
**4 direcionais com Bonferroni α*=0,05/4** (IC98,75%); 2 TOST.

**H_F3 — RELINC EM DADOS NOVOS:** discordância da variante `relinc`
(45 contrastes) **≤ 10%** com estratos exatos (caraterização).

**H_F4 — RAMO CONCORDANTE:** contagem de `*_FLAG` em dados novos;
**0/135 de novo → `ZERO_DE_NOVO` e recomendação formal de remoção do ramo
em r7**; qualquer ocorrência → `DISPAROU` (ramo exercitado).

**H_F5 — PODER:** MDE80 < 0,06 nos 6 testes boxdim (continuidade r4/r5).

### 1.4 Margens (continuidade r5, ancoradas em precisão)

**0,05 primária** + 0,03/0,08 sensibilidade (ancoragem r4: 1,645×SE =
0,040). Equivalência só para `boxdim`.

### 1.5 Regras de veredito

**Idênticas ao r5** (2 níveis, exaustivas — ver doc 32 §1.5): ponto dentro →
veredito normal; ponto fora → concordância entre os dois métodos decide
(conta com flag) ou discordância (não conta); global: CONTRADITA* →
REFUTADA_CONTRADITA; |C| < ⌈0,6n⌉ → INDETERMINADO; todos OK → CONFIRMADA;
senão PARCIAL. **Única mudança:** o IC Bonferroni do grupo **boxdim** passa de
α=0,05/5 para **α=0,05/4** (4 direcionais após a redefinição de (a)).

### 1.6 Selftests (executados antes do commit; repetidos no run; A8)

| # | Teste | Resultado |
|---|---|---|
| S1 | BCa vs `scipy` (iid) | **OK** diff 0,013 |
| S2 | Métricas n=512 (invariância rank + ordenações) | **OK** |
| S4 | Tipo-I 40 nulos: percentil/regra/BCa | **3/40 · 3/40 · 13/40** (gates ≤0,15 ✓; BCa reportado) |
| S5 | Poder 10 alternativos (regra, sinal `−`) | **10/10** ✓ |
| S6 | Incidência/discordância do primário | **0,000** ✓ |
| **S7 (NOVO)** | **Smoke de `analyze()` com `contrast()` stubado** — 135 contrastes, classificadores, H_F1–F5, `write_contrasts` | **OK** |
| DISJ | grade r6 × (r2∪r3∪r4∪r5) = ∅ | **OK** |

---

## 2. Método (execução)

1. **`--reanalise-r5`** → H_E1: recalcula os45 contrastes `relinc` do CSV r5
   congelado com o método corrigido → `gk_proof_fractal_v6_reanalise_r5.{json,csv}`
   (comparação com os5 discordantes originais).
2. **Coleta** (1536 instâncias novas; checkpoint atômico + `--resume`) →
   `gk_proof_fractal_v6_series.csv`.
3. **Análise**:135 contrastes (percentil estratificado primário; `relinc`
   recalculado por réplica; BCa parceiro; bloco8 diagnóstico nas9 chaves;
   meta-análise H_F1b) → `gk_proof_fractal_v6_contrasts.csv` + 2 JSONs.

## 3. Resultados *(pós-execução)*

## 4. Interpretação *(pós-execução)*

## 5. Limitações *(pós-execução)*

## 6. Próximos passos *(pós-execução)*

---

**Referências:** `32_` + referee (A1–A8 → §1.1) · `31_`–`28_` (linha) ·
`gk_proof_fractal_v6.py` (pré-registro executável) · Cochran (1954) Q ·
Efron (1993) BCa · Politis & Romano (1994) bootstrap estratificado ·
Lakens (2017) TOST

# 30 — Ponte Prova → Fractal (D4′ v3 / r3): boxdim PRÉ-REGISTRADO em dados novos

**Data:** 20/11/2026 · **Classificação:** **(P)** experimento próprio + **(C)**
hipóteses **pré-registradas** · **Nível Ten-Proofs:** N1 (script, seeds
determinísticos) + N2 (bootstrap). **Não** é lower bound; **não** é claim de EF.

> **PROTOCOLO DE PRIORIDADE TEMPORAL:** as hipóteses (§1), margens, grade e
> regras de veredito deste documento e do script `gk_proof_fractal_v3.py`
> foram fixados e **commitados ANTES de qualquer execução com dados novos**
> — o hash do commit de pré-registro prova a ordem. Isso responde à
> pendência C1 do referee do 29_ ("margens escolhidas depois de ver os
> dados"): aqui âncora, margens e testes precedem os dados. Autochecagem
> executada **após** o commit: resultado em §3.

**Linha:** `28_` (v1: separação = regime) → `29_` §8 (r2: BCa/TOST — sem
separação; equivalência ±0,20; saturação não resolvida) → **este (r3):
métrica nova pré-registrada, dados disjuntos, inferência delete-d**.

**Reproduzir:**
```powershell
python -u gk_proof_fractal_v3.py              # coleta + analise (~20min)
python -u gk_proof_fractal_v3.py --analyze-only  # re-analise (~2min)
# → gk_proof_fractal_v3_series.csv + gk_proof_fractal_v3_contrasts.csv
#   + gk_proof_fractal_v3.json + gk_proof_fractal_v3_analysis.json
# seed=20261119 · seed_boot=20261123 · B=1000 · delete-d d=8
```

---

## 1. Pré-registro (fixado antes do run)

### 1.1 Dados — novos e disjuntos do r2 (anti-circularidade)

Mesmos geradores, **seeds nunca usados** (checagem automática: interseção
com o CSV do r2 = vazia → `DISJ OK`, senão o script **aborta**):

| Família | Grade r3 | Seeds do r2 (evitados) |
|---|---|---|
| `implication` | m=3..6 × seeds **16..31** (64) | 0..15 |
| `cadeia` | k=3..6 × seeds **16..31** (64) | 0..15 |
| `tau_tiny` | seeds **64..127** (64) | 0..63 |

192 instâncias; minref exato + DRAT por instância; **escopo n≤6**
(mesmo do v2); CSV **sem coluna de tempo** (reprodução byte-a-byte — 8º
bug). As hipóteses abaixo foram derivadas do **padrão observado no r2**
(dados anteriores) e valem para a **distribuição do gerador** — não para
famílias arbitrárias (escopo declarado).

### 1.2 Hipóteses (métrica primária: **boxdim**)

**Por que boxdim:** foi a **única** métrica sem contrastes incoerentes no
r2 (0/27 vs Higuchi 4/27 e Hurst 4/27 — §8.5 do 29_) e o único padrão
exploratório que sobreviveu ao BCa em 2/3 variantes (pista A4). Escolha
**documentada antes** dos dados novos; Higuchi/Hurst entram apenas como
grupo de comparação (exploratórias).

- **H_B1 — PRIMARIA (boxdim, sistema `minref`, variante `raw`; 3 testes):
  o padrão-r2 "τ é o par-ímpar" replica em dados novos.**
  - (a) `minref:implication−tau_tiny`: Δ > 0, IC95 BCa exclui 0
    (r2: **+0,053**) — sinal esperado `+1`
  - (b) `minref:cadeia−tau_tiny`: Δ > 0, IC95 exclui 0 (r2: **+0,058**)
    — sinal `+1`
  - (c) `minref:implication−cadeia`: **EQUIVALENTE** (IC90 BCa ⊂ ±0,05)
    (r2: −0,004, equivalente)
  - **CONFIRMADA** ⟺ (a) e (b) separam com sinal coerente **e** (c) é
    equivalente · **PARCIAL** ⟺ exatamente 2/3 · **REFUTADA** ⟺ ≤1/3 ·
    **REFUTADA_CONTRADITA** se (a) ou (b) exclui 0 com sinal **negativo**
    (inverte o padrão r2).
  - Multiplicidade: as 2 separações usam **IC97,5% (Bonferroni
    α*=0,05/2)** reportado ao lado do IC95; (c) é TOST com α próprio
    0,05.
- **H_B2 — SECUNDARIA (fonte, boxdim, `raw`; 2 testes):**
  `fonte:cadeia` Δ < 0 exclui 0 (r2: **−0,084**) e `fonte:tau_tiny`
  Δ < 0 exclui 0 (r2: **−0,112**) — sinal `−1` (minref tem boxdim
  **menor** que DRAT nessas famílias). **CONFIRMADA** ⟺ 2/2 coerentes.
- **H_B3 — PISTA A4 (drat, boxdim, `raw`; 1 teste):**
  `drat:implication−cadeia` Δ < 0 exclui 0 (r2: **−0,102**) — sinal `−1`.
  **CONFIRMADA** ⟺ exclui 0 com sinal coerente.
- **H_B4 — ANTI-SATURAÇÃO (C2; contagem, não efeito):** `boxdim` tem
  **0 contrastes incoerentes** em r3 (como no r2: 0/27). Reportado por
  métrica; não decide as demais.

### 1.3 Margens (ancoradas em dados **anteriores** ao r3)

| Margem | Valor | Âncora (documentada antes do run) |
|---|---|---|
| **Primária** | **Δ = 0,05** | (i) menor efeito SEPARA do r2 em boxdim = **0,053** (minref imp−τ); (ii) ~1/3 da amplitude entre-séries do r2 (boxdim 0,718–0,860 → 0,142). Efeito < 0,05 é desprezível frente ao que a métrica já separou. |
| Sensibilidade | 0,03 / 0,08 | reportados, **não promovidos** (tabela cheia, como no r2 §8.2) |

**Equivalência só é claimada para `boxdim`** (métrica primária);
`boxdim_rank` e `saltos` são exploratórios (robustez de sinal).

### 1.4 Inferência

- **BCa** (z0 + aceleração) com **DOIS jackknifes reportados**:
  **delete-d (d=8, janelas sobrepostas)** = padrão r3 (pendência C3 do
  r2) e **delete-1** = concordância — divergência entre eles é
  **flag de instabilidade**, reportada por hipótese.
- TOST: IC90 BCa na margem primária. **MDE80** = 2,8016 × SE_boot.
- **Regra de incoerência** (r2, mantida): ponto fora do IC (pct ou BCa)
  ⇒ `INCOERENTE` — **não conta como refutação nem como confirmação**.
- Percentis: **B=1000**, seed bootstrap `SEED+4=20261123` (declarado).

### 1.5 Métricas

`boxdim` (PRIMARIA) · `boxdim_rank` (box-counting da série **rankada** —
invariante a transformação monotona; anti-saturação) · `saltos` (taxa de
inversão de sinal das diferenças; ruído≈0,5, rampa≈0) · `higuchi_D` e
`hurst_rs` (EXPLORATÓRIAS — grupo de comparação da H_B4).

### 1.6 Selftests obrigatórios (executados ANTES do run; A8)

Resultado da bateria pré-run (o script aborta se algum falhar):

| # | Teste | Resultado |
|---|---|---|
| S1 | BCa vs `scipy.stats.bootstrap` (iid, 20k resamples) | **OK** — diff máx 0,013 |
| S2 | Invariancia monotona de `boxdim_rank` (x vs exp(x)) | **OK** — erro 0,0 (exato) |
| S3 | Ordenação sintética de `saltos` (ruído>seno; ruído>rampa) + gate canônico `boxdim(seno)<boxdim(ruído)` | **OK** (0,69>0,13; 0,79<0,85) |
| S4 | **Tipo-I**: 50 pares de ruído branco (Δ real 0), BCa delete-d | **OK** — 2/50 = **0,04** (nominal 0,05) |
| S5 | **Poder**: rampa+jitter vs seno puro (construct calibrado), P=10 | **OK** — **9/10** detectam (gate ≥7; 6 coerentes) |
| DISJ | Interseção grade r3 × grade r2 = ∅ | **OK** — 192 × 192, interseção vazia |

> **Nota de calibração (honestidade):** o gate de S5 (≥7/10) foi fixado
> **após** calibração em séries sintéticas (9/10 observados) — calibração
> de código, não de hipótese: afeta só se o pipeline está operante, não os
> vereditos sobre dados reais. Um construct inicial (`sorted vs ruido`,
> Δ=0,05) foi **rejeitado pelo próprio gate** (2/5) por ser fraco demais
> em n=64 — registrado para não reescolher constructs depois.

---

## 2. Método (execução)

Coleta → `gk_proof_fractal_v3_series.csv` (sem tempo) · análise → 135
contrastes (27 combinações × 5 métricas × variantes raw/log1p/relinc) →
`gk_proof_fractal_v3_contrasts.csv` + JSONs (R6 protege os **dois**
pares CSV↔JSON). Vereditos das hipóteses pela régua §1.2.

## 3. Resultados *(preenchido após a execução — ver §4 do commit de resultados)*

## 4. Interpretação *(pós-run)*

## 5. Limitações *(pós-run; escopo declarado em §1.1)*

## 6. Próximos passos *(pós-run)*

---

**Referências:** `29_PONTE_PROVA_FRACTAL_D4V2.md` §8 + referee §C–D
(pendências r2 atacadas: C1 pré-registro → §1; C2 saturação → H_B4 +
métricas rank/saltos; C3 jackknife → delete-d) · `28_` (origem D4′) ·
`gk_proof_fractal_v3.py` (pré-registro executable) ·
`gk_proof_fractal_v2_r2.py` (BCa/TOST reaproveitados) ·
Efron (1987) BCa · Lakens (2017) TOST · Kish (1995) delete-d jackknife

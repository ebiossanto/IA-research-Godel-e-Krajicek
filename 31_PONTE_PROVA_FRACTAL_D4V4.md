# 31 — Ponte Prova → Fractal (D4′ v4 / r4): n=384, margem por precisão, z0 diagnosticado

**Data:** 20/11/2026 · **Classificação:** **(P)** experimento próprio + **(C)**
hipóteses **pré-registradas** · **Nível Ten-Proofs:** N1 + N2 · **Não** é lower
bound; **não** é claim de EF.

> **PROTOCOLO DE PRIORIDADE TEMPORAL:** hipóteses, margens, regras de veredito,
> grade e alvos deste documento e do script `gk_proof_fractal_v4.py` foram
> fixados e **commitados ANTES de qualquer execução com dados novos** — o hash
> do commit de pré-registro prova a ordem (C1). Autochecagem (selftests) executada
> **antes** do commit e repetida no run; resultado em §1.6/§3.

**Linha:** `28_` (v1) → `29_` §8 (r2) → `30_` (r3) → **este (r4)** — cada rodada
fecha as pendências da anterior (tabela §1.1).

**Reproduzir:**
```powershell
python -u gk_proof_fractal_v4.py --selftest-only   # só bateria (~1min)
python -u gk_proof_fractal_v4.py                   # coleta + análise (~3.5h)
python -u gk_proof_fractal_v4.py --analyze-only    # re-análise (~10min)
# → gk_proof_fractal_v4_series.csv + _contrasts.csv + 2 JSONs
# seed=20261119 · seed_boot=20261124 · B=1000 · delete-d d=8
```

---

## 1. Pré-registro (fixado antes do run)

### 1.1 Pendências do r3 fechadas aqui

| Pendência r3 (referee) | Solução r4 |
|---|---|
| **A1** margem ancorada só em efeito (0,05 impossível) | **Δ=0,08 primária** ancorada em **precisão**: maior meia-largura IC90 dos pré-registrados r3 = **0,0805** (H_B3; demais 0,061–0,073) — efeitos abaixo do limite de resolução do r3 são certificáveis; sensibilidade 0,06/0,10 |
| **A3** veredito global com INCOERENTE indefinido | **Regras exaustivas** (§1.5) — todo caso possível tem veredito pré-definido |
| **A4** primariedade do IC não declarada | **BCa delete-d = primário**; percentil = robustez (flag `discordancia_pct_bca`) |
| **A5** z0 extremo/IC degenerado sem diagnóstico | **H_C3** (bias por série, bias/SE, contingências D1–D4) + **`saltos` confirmatório** (H_C2) |
| **§6.1** n maior p/ MDE<0,06 | **n=384/família** (1152 instâncias) → **H_C4** alvo |

### 1.2 Dados — novos, disjuntos de r2 **e** r3 (aborta se intersectar)

| Família | Grade r4 | Evitados |
|---|---|---|
| `implication` | m=3..6 × seeds **32..127** (384) | r2: 0..15; r3: 16..31 |
| `cadeia` | k=3..6 × seeds **32..127** (384) | r2: 0..15; r3: 16..31 |
| `tau_tiny` | seeds **128..511** (384) | r2: 0..63; r3: 64..127 |

Mesmos geradores (escopo: distribuição do gerador, seeds nunca usados);
`DISJ OK` contra os **dois** CSVs anteriores; CSV sem coluna de tempo.

### 1.3 Hipóteses

**H_C1 — PRIMARIA (boxdim, `raw`; 6 testes; mesmas chaves/direções do r3):**

| # | Chave | Esperado | Âncoras r3 / r2 |
|---|---|---|---|
| (a) | `minref:implication−tau_tiny` | > 0 | +0,0595 OK / +0,053 |
| (b) | `minref:cadeia−tau_tiny` | > 0 | +0,0731 OK_BONF / +0,058 |
| (c) | `minref:implication−cadeia` | **EQUIVALENTE ±0,08** | não separa; eq@0,08 ✓ r3 |
| (d) | `drat:implication−cadeia` [pista A4] | < 0 | −0,170 OK_BONF / −0,102 |
| (e) | `fonte:tau_tiny` | < 0 | −0,102 OK / −0,112 |
| (f) | `fonte:cadeia` | < 0 | −0,152 **INCOERENTE** / −0,084 |

Multiplicidade: 5 direcionais com **Bonferroni α*=0,05/5=0,01** (IC99%
reportado); (c) TOST α próprio 0,05 (IC90).

**H_C2 — SECUNDARIA (`saltos`, `raw`; 3 direcionais; âncoras r3):**
`minref:imp−τ > 0` (+0,173 SEPARA) · `drat:imp−cadeia > 0` (+0,110) ·
`fonte:cadeia > 0` (+0,120) — Bonferroni α*=0,05/3 (IC98,33%).
Justificativa: `saltos` foi a **única métrica 0/27 incoerente no r3** e é
estatística **local** (preservada pelo block-resample → z0 saudável).

**H_C3 — DIAGNOSTICO z0 (caracterização; D2 é claim):**
- **D1** contingência `|z0|>1.5` × `|bias_over_se|>1.2` (taxa de coincidência);
- **D2 CLAIM:** todo IC degenerado (`lo==hi`) tem `|z0|>2,5` (r3: único
  degenerado z0=−2,75; calibração n=256: z0=3,29 degenerado);
- **D3** taxa de discordância exclusão pct-vs-BCa: grupo `|z0|>1,5` vs `≤1,5`;
- **D4** mediana `|z0|` em `fonte:*` vs pares de família (espera: fonte maior).

**Base empírica do diagnóstico (calibração pré-run, séries sintéticas):**
a raiz do z0 extremo é o **viés de macroestrutura assimétrica** —
block-resample destrói tendências; par com tendência (rampa vs seno) →
z0=+3,29 e IC degenerado; pares **estacionários** (estrutura local
preservada: zigzag-vs-branco) → z0∈[−0,52;+0,54] e **10/10 coerentes**.
Explica o r3: pares de família (mesma grade) tiveram z0=0,63/0,66/−0,06;
`fonte:cadeia` (macroestruturas de fonte diferentes) z0=−2,17.

**H_C4 — ALVO DE DESIGN:** `MDE80 < 0,06` nos **6** testes boxdim
pré-registrados (previsão por escala √(64/384): 0,047–0,058). Falha de
**alvo** (contada), não de hipótese.

### 1.4 Margens (ancoradas em precisão do r3 — A1)

| | Valor | Âncora (fixada antes do run) |
|---|---|---|
| **Primária** | **0,08** | maior meia-largura IC90 r3 = **0,0805** (H_B3); demais pré-registrados 0,061–0,073 |
| Sensibilidade | 0,06 / 0,10 | menor meia-largura não-degenerada r3 (0,061) / arredondamento superior — reportadas, não promovidas |

Equivalência **só para `boxdim`** (métrica primária); `boxdim_rank`/`saltos`
exploratórios exceto H_C2 (direcional).

### 1.5 Regras de veredito (exaustivas — A3; fixadas antes do run)

**Por teste:** `OK` (IC95 BCa exclui 0, sinal coerente; `OK_BONF` se o IC
Bonferroni do grupo também exclui) · `FALHA_INCONCLUSIVO` · `CONTRADITA`
(exclui 0 com sinal **oposto**; só direcionais) · `EQUIVALENTE` ((c): IC90
na margem) · `FALHA_SEPARA` ((c): exclui 0) · **`INCOERENTE`** (ponto fora
do IC pct ou BCa — **não conta em nenhuma direção**) · `SEM_DADOS`.

**Global:** qualquer `CONTRADITA` → **REFUTADA_CONTRADITA**; C = contáveis
(OK*/FALHA*); **|C| < ⌈0,6·n⌉ → INDETERMINADO** (muitos incoerentes/sem
dados); todos C OK → **CONFIRMADA**; nenhum OK → **REFUTADA**; senão →
**PARCIAL** (n_ok/|C|, com n_incoh reportado).

### 1.6 Selftests (executados antes do commit; repetidos no run; A8)

| # | Teste (n=384, regime do experimento) | Resultado |
|---|---|---|
| S1 | BCa vs `scipy.stats.bootstrap` (iid) | **OK** diff 0,013 |
| S2 | Invariância monotona `boxdim_rank` (x vs exp x) | **OK** erro 0,0 |
| S3 | Ordenação `saltos` (ruído>seno>rampa) + `boxdim(seno)<boxdim(ruído)` | **OK** |
| S4 | **Tipo-I**: 30 pares branco-vs-branco, B=500, BCa delete-d | **OK** — 0/30 = 0,000 (gate ≤0,20) |
| S5 | **Poder**: zigzag-vs-branco (par estacionário calibrado), P=10, B=1000 | **OK** — **10/10 coerentes** (gate ≥7; z0∈[−0,59;+0,24]) |
| DISJ | interseção grade r4 × (r2 ∪ r3) = ∅ | **OK** |

> **Nota de calibração (honestidade):** três constructs de poder foram
> **rejeitados** antes do escolhido — `sorted-vs-ruido` (r3, Δ fraco),
> `rampa-vs-seno` e `rampa σ-diferente` (n=256: z0=3,29, IC degenerado,
> 0/6 coerentes) por **viés de macroestrutura assimétrica**; o escolhido
> (`zigzag-vs-branco`, estacionário) passou 10/10. Registrado para não
> reescolher constructs depois do run.

---

## 2. Método (execução)

Coleta (minref + DRAT por instância, 1152 instâncias) →
`gk_proof_fractal_v4_series.csv` (sem tempo) → análise: 135 contrastes
(9 combinações × 3 variantes × 5 métricas) com **BCa delete-d primário** +
delete-1 concordância + percentil robustez + diagnóstico z0 por contraste
(bias_a/bias_b/bias_over_se/z0/empates/degenearção/discordância) →
`gk_proof_fractal_v4_contrasts.csv` + 2 JSONs (R6 protege os dois pares).
Vereditos pelas regras §1.5.

## 3. Resultados *(pós-run)*

## 4. Interpretação *(pós-run)*

## 5. Limitações *(pós-run)*

## 6. Próximos passos *(pós-run)*

---

**Referências:** `30_PONTE_PROVA_FRACTAL_D4V3.md` + referee (A1–A7 → §1.1) ·
`29_` §8 (r2) · `28_` (origem) · `gk_proof_fractal_v4.py` (pré-registro
executável) · Efron (1987) BCa · Lakens (2017) TOST · Politis & Romano (1994)
stationary bootstrap (contexto do viés de macroestrutura)

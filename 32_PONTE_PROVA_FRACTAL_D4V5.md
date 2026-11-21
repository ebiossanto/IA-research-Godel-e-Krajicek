# 32 — Ponte Prova → Fractal (D4′ v5 / r5): `saltos` primário, percentil estratificado, regra de 2 níveis

**Data:** 21/11/2026 · **Classificação:** **(P)** experimento próprio + **(C)**
hipóteses **pré-registradas** · **Nível Ten-Proofs:** N1 + N2 · **Não** é lower
bound; **não** é claim de EF.

> **PROTOCOLO DE PRIORIDADE TEMPORAL:** hipóteses, margens, regras, **método de
> IC (selecionado pela calibração)** e grade deste documento e do script
> `gk_proof_fractal_v5.py` foram fixados e **commitados ANTES de qualquer
> execução com dados novos** — o hash do commit de pré-registro prova a ordem
> (C1). Selftests/calibração executados antes do commit e repetidos no run.

**Linha:** `28_` → `29_`(r2) → `30_`(r3) → `31_`(r4) → **este (r5)** — cada
rodada fecha as pendências da anterior (§1.1).

**Reproduzir:**
```powershell
python -u gk_proof_fractal_v5.py --selftest-only   # bateria + calibração (~5min)
python -u gk_proof_fractal_v5.py                   # coleta + análise (~3.5h; --resume p/ crash)
python -u gk_proof_fractal_v5.py --analyze-only    # re-análise (~1.5h)
# → gk_proof_fractal_v5_series.csv + _contrasts.csv + 2 JSONs
# seed=20261119 · seed_boot=20261125 · B=1000 (S4:600)
```

---

## 1. Pré-registro (fixado antes do run)

### 1.1 Pendências do r4 fechadas aqui

| Pendência r4 (referee/§6) | Solução r5 |
|---|---|
| **(i) método de IC novo** (BCa+bloco fixo degrada com n) + **calibração de incidência** | **Percentil + bootstrap estratificado por parâmetro** como primário (DGP real: instâncias iid dentro de cada estrato; macro preservada → viés≈0) — **selecionado pela calibração S4–S6** (§1.6); BCa estratificado = parceiro da regra; BCa+bloco8 = diagnóstico head-to-head nas 9 chaves pré-registradas |
| **(ii) regra de 2 níveis** (A5: (d)(f) bloqueados) | `INCOERENTE_CONCORDANTE` → **conta com flag**; `DISCORDANTE` → não conta (§1.5) |
| **(iii) `saltos` primário** (3/3 Bonferroni no r4) | **H_D1** promove `saltos` a métrica confirmatória primária; boxdim → secundária (H_D2) |
| **(v) n p/ MDE<0,06** (r4: 4/6) | **n=512/família** (1536 instâncias) → **H_D4** (previsão √(384/512): 6/6) |
| expectativas só com série-base (A3) | âncoras H_D1 = r3+r4 (duas rodadas); H_D2 = r4 |

### 1.2 Dados — novos, disjuntos de r2, r3 **e** r4 (aborta se intersectar)

| Família | Grade r5 | Evitados |
|---|---|---|
| `implication` | m=3..6 × seeds **128..255** (512) | r2:0–15 · r3:16–31 · r4:32–127 |
| `cadeia` | k=3..6 × seeds **128..255** (512) | idem |
| `tau_tiny` | seeds **512..1023** (512) | r2:0–63 · r3:64–127 · r4:128–511 |

Estratos de parâmetro: imp/cadeia = 4 estratos de 128; tau = 1 estrato de 512
(serie puramente iid — sem macro a preservar). `DISJ OK` contra os **três**
CSVs anteriores; CSV sem coluna de tempo; checkpoint atômico + `--resume`.

### 1.3 Hipóteses

**H_D1 — PRIMARIA (`saltos`, `raw`; 3 direcionais; âncoras r3+r4):**

| # | Chave | Esperado | r3 | r4 |
|---|---|---|---|---|
| (a) | `minref:implication−tau_tiny` | > 0 | +0,173 | +0,185 |
| (b) | `drat:implication−cadeia` | > 0 | +0,110 | +0,117 |
| (c) | `fonte:cadeia` | > 0 | +0,120 | +0,113 |

Bonferroni α*=0,05/3 (IC98,33% reportado). **CONFIRMADA** ⟺ 3/3 OK (flags
concordantes contam e são reportados) · **PARCIAL** 2/3 · **REFUTADA** ≤1/3 ·
**CONTRADITA** sinal oposto.

**H_D2 — SECUNDARIA (boxdim, `raw`; os 6 testes do H_C1 do r4, série nova +
método novo + regra nova):** (a) imp−τ>0 (r4: FALHA −0,024) · (b) cadeia−τ>0
(r4: INCOERENTE +0,048) · (c) imp−cadeia **EQUIVALENTE ±0,05** (r4
INCOERENTE; r3 equivalente) · (d) drat imp−cadeia<0 [pista] (r4 INCOERENTE,
pct exclui) · (e) fonte:τ<0 (r4 OK_BONF; r3/r2 replicam) · (f) fonte:cadeia<0
(r4 INCOERENTE, pct exclui). Bonferroni α*=0,05/5 nos5 direcionais; (c) TOST.

**H_D3 — INCIDENCIA (caracterização; gate é a calibração S6):** relatório em
dados reais — incidência total e split concordante/discordante do primário +
head-to-head bloco8 nas 9 chaves; **alvo: discordante ≤10%**.

**H_D4 — ALVO DE DESIGN:** MDE80 < 0,06 nos 6 testes boxdim (previsão
√(384/512): 0,024–0,059 → 6/6). Falha de alvo = contada, não de hipótese.

### 1.4 Margens (ancoradas em precisão do r4 — A1)

| | Valor | Âncora (fixada antes do run) |
|---|---|---|
| **Primária** | **0,05** | maior meia-largura IC90 **percentílica** do r4 estimada (1,645×SE) = **0,040** ((e); demais 0,016–0,036) |
| Sensibilidade | 0,03 / 0,08 | reportadas, não promovidas |

### 1.5 Regras de veredito (exaustivas, 2 níveis — fixadas antes do run)

**Por teste** — CI **primário** = percentil estratificado; CI **parceiro** = BCa
estratificado:
- **Ponto DENTRO do primário:** direcional → `OK` (`OK_BONF` se o Bonferroni
  primário também exclui) / `CONTRADITA` (sinal oposto) / `FALHA_INCONCLUSIVO`;
  equivalência (c) → `OK` (IC90 na margem) / `FALHA_SEPARA` / `FALHA_INCONCLUSIVO`.
- **Ponto FORA do primário:** **CONCORDANTE** = os dois métodos concordam
  (direcional: excluem 0 no **mesmo sinal coerente com o ponto**, ou **ambos
  incluem 0**; eq: os dois IC90 na margem, ou ambos excluem coerentes, ou ambos
  incluem 0) → **conta com FLAG** (`OK_FLAG`, `CONTRADITA_FLAG`,
  `FALHA_SEPARA_FLAG`, `FALHA_INCONCLUSIVO_FLAG`); **DISCORDANTE** →
  `INCOERENTE_DISCORDANTE` (não conta em nenhuma direção); `SEM_DADOS`.
- **Global:** qualquer `CONTRADITA*` → `REFUTADA_CONTRADITA`; C = contáveis
  (OK*/FALHA*, flags incluídos); |C| < ⌈0,6·n⌉ → `INDETERMINADO`; todos C OK →
  `CONFIRMADA`; nenhum OK → `REFUTADA`; senão `PARCIAL` — flags reportados na
  string.

### 1.6 Selftests e **calibração do método** (executados antes do commit; repetidos no run)

**A calibração escolheu o método — é para isso que ela existe.** Sequência
(honestidade total): (1) protótipo com 4 candidatos mostrou que o
**estratificado derruba a incidência** (bloco8 50–100% → estratificado ~0–3%);
(2) a bateria completa **S4 revelou que BCa-estratificado tem tipo-I 13/40 =
0,325** (a correção z0 com aceleração≈0 é instável neste statístico) enquanto o
**percentil dá 3/40 = 0,075** → **primário = percentil estratificado**, BCa
estratificado rebaixado a **parceiro da regra**, bloco8 mantido só como
diagnóstico. Tudo antes de qualquer dado novo.

| # | Teste (n=512, regime real) | Resultado |
|---|---|---|
| S1 | BCa vs `scipy.stats.bootstrap` (iid) | **OK** diff 0,013 |
| S2 | Invariância monotona `boxdim_rank` (erro exato) | **OK** 0,0 |
| S4 | **Tipo-I** 40 nulos com grade: percentil cru / regra / BCa cru | **0,075 / 0,075 / 0,325** (gates ≤0,15 ✓; BCa reportado — razão de não ser primário) |
| S5 | **Poder** 10 alternativos (perfilA+iid vs perfilB+zig; efeito medido −0,049, sinal `−`), regra | **10/10** (gate ≥7 ✓) |
| S6 | **Incidência**: percentil-estratificado (total / discordância) vs bloco8-BCa | **0,000 / 0,000** (gate ≤0,10 ✓) vs **0,200** |
| DISJ | interseção grade r5 × (r2∪r3∪r4) = ∅ | **OK** |

> **Nota de calibração:** constructs rejeitados antes do escolhido (lição r3):
> `sorted-vs-ruido`, `rampa-vs-seno`, `rampa σ-diferente` (viés de macro
> assimétrico → z0 catastrófico). O construct do r5 usa **grade real** (4
> estratos com níveis) — exatamente o que o S4 precisa medir. O efeito (−0,049)
> e o sinal (`−`) foram medidos em calibração e **fixados** antes do run.

---

## 2. Método (execução)

Coleta (1536 instâncias, checkpoint atômico + `--resume` por causa do crash
CaDiCaL) → `gk_proof_fractal_v5_series.csv` → análise: 135 contrastes
(27 combinações × 3 variantes × 5 métricas) com **percentil estratificado
primário** + BCa estratificado parceiro + Bonferroni (0,01/0,0167) + bloco8
diagnóstico nas 9 chaves → 2 CSV/JSON (R6 protege os dois pares). Vereditos
pelas regras §1.5.

## 3. Resultados *(pós-run)*

## 4. Interpretação *(pós-run)*

## 5. Limitações *(pós-run)*

## 6. Próximos passos *(pós-run)*

---

**Referências:** `31_` + referee (A1–A8 → §1.1) · `30_` (r3) · `29_` §8 (r2) ·
`28_` (origem) · `gk_proof_fractal_v5.py` (pré-registro executável) ·
Efron (1987) BCa · Politis & Romano (1994) bootstrap estratificado/estacionário ·
Lakens (2017) TOST

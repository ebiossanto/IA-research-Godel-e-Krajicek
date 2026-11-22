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

## 3. Resultados (execução: 21–22/11/2026)

**Execução e incidentes (registro honesto):**
- **Coleta (6 tentativas):** 3 crashes nativos `Cadical195.__del__`
  (`0xC0000005`, mesma família do r4) contidos pelo checkpoint atômico +
  `--resume`; **1536/1536 UNSAT**, 0 censuras, 0 descartes, estratos
  `[128×4]`/`[512]` corretos.
- **2 bugs de plumbing** pós-pré-registro (diffs separados, hipóteses/margens/
  regras/método **intactos**): (1) `runs_of` comparava `param` sem `int()` →
  estrato do tau virava `[503,9]` pela mistura str/int do checkpoint vs coleta
  fresca (corrigido `8209433`); (2) `for k, c in pre` iterava dict sem
  `.items()` → `ValueError` no **fim** do `analyze()` antes de escrever os
  artefatos, destruindo ~1,5h de análise (corrigido `0919e6b`). **Lição:** smoke
  test de análise com `contrast()` stubado passou a ser obrigatório — executado
  com sucesso **antes** do relançamento (exercitou classificadores, H_D1–H_D4,
  diag e `write_contrasts`).
- **Análise final:** 1 tentativa, 90min, exit 0.
- **Artefatos:** série `df3737ce…` (input idêntico no JSON da análise ✓) ·
  contrastes `c30b13f2…` · selftests S1–S6 OK no run.

### 3.1 H_D1 — PRIMARIA (`saltos`): **CONFIRMADA (3/3 OK_BONF)** ✅

| # | Teste | r3 (âncora) | r4 | **r5** | pct95 | Bonferroni (pct99) | z0 |
|---|---|---|---|---|---|---|---|
| (a) | minref:imp−τ > 0 | +0,173 | +0,185 | **+0,1383** | [+0,077; +0,181] ✅ | [+0,064; +0,198] ✅ | +0,38 |
| (b) | drat:imp−cadeia > 0 | +0,110 | +0,117 | **+0,0799** | [+0,064; +0,165] ✅ | [+0,049; +0,175] ✅ | −1,39 |
| (c) | fonte:cadeia > 0 | +0,120 | +0,113 | **+0,1035** | [+0,069; +0,166] ✅ | [+0,061; +0,176] ✅ | −0,50 |

**3/3 `OK_BONF`** — percentil **e** Bonferroni excluem, pontos dentro dos ICs,
z0 saudáveis (|z0| ≤ 1,39), **3ª rodada consecutiva de confirmação**
(r3→r4→r5, dados disjuntos cada vez). **Item #1 do pedido entregue.**

### 3.2 H_D2 — SECUNDARIA (boxdim): **PARCIAL (5/6 contáveis; 0 discordantes)**

| # | Teste | r4 | **r5 point** | pct95 | Veredito |
|---|---|---|---|---|---|
| (a) | minref:imp−τ > 0 | FALHA −0,024 | **−0,0115** | [−0,019; +0,035] | **FALHA_INCONCLUSIVO** (3ª vez: efeito ≈ 0) |
| (b) | minref:cadeia−τ > 0 | INCOERENTE | **+0,0252** | [+0,016; +0,064] | **OK_BONF** (1ª limpa) |
| (c) | minref:imp−cadeia ≡ ±0,05 | INCOERENTE | **−0,0367** | [−0,047; −0,012] | **OK = EQUIVALENTE @0,05** (TOST passa) |
| (d) | drat:imp−cadeia < 0 [pista] | INCOERENTE | **−0,0681** | [−0,079; −0,054] | **OK_BONF** (4ª rodada) |
| (e) | fonte:τ < 0 | OK_BONF −0,128 | **−0,0366** | [−0,070; −0,003] | **OK** (4ª rodada; magnitude caiu) |
| (f) | fonte:cadeia < 0 | INCOERENTE | **−0,0508** | [−0,061; −0,042] | **OK_BONF** (1ª limpa) |

- **(c) é o desfecho de TOST clássico:** CI95 **exclui 0** (efeito existe:
  −0,037) **e** IC90 cabe em ±0,05 (**praticamente equivalente**) — diferença
  estatisticamente detectável porém menor que a margem. Fecha a pendência do
  r3 (eq@0,05 não certificável lá).
- **(a) fracassou pela 3ª vez** — a direção positiva prevista não existe
  (efeito ≈ 0); o padrão-τ em boxdim sobrevive só em (b).
- **(d)(f) limpos pela 1ª vez** — o head-to-head prova que o método do r4
  **bloquearia 4/9** das chaves (bloco8 `z0=±3,29` em todas) vs **0/9** do
  primário (§3.3).

### 3.3 H_D3 — INCIDENCIA: **CONFIRMADA** — o método novo resolveu o problema do r4

| Métrica | r4 (n=384, BCa+bloco8) | **r5 (n=512, pct+estrat)** |
|---|---|---|
| Incoerentes/discordantes | **45/135 (33%)** | **6/135 (4,4%)** ✅ (gate ≤10%) |
| z0 extremos | 61/135 | **12/135** |
| ICs degenerados | 16 | **2** (ambos `saltos:relinc`) |
| **Head-to-head (9 chaves pré-reg.)** | bloco8: **4/9 fora** | primário: **0/9 fora** |

- Os 6 discordantes estão **todos em variantes `relinc`/`log1p`** (4 em
  `saltos:relinc`) — **0 em `raw`** (a variante confirmatória). Hipótese
  técnica registrada: o ajuste de estratos do `relinc` (1º estrato −1 ponto,
  **aproximação declarada** no pré-registro) pode contribuir — pendência r6.
- **Item #2 do pedido entregue:** método novo **com calibração de incidência**
  (S4–S6 antes do run) **e** verificação em dados reais (4,4% ≤ 10%).

### 3.4 H_D4 — ALVO DE DESIGN: **ATINGIDO (6/6)** ✅

MDE80 dos 6 testes boxdim: **0,014 · 0,017 · 0,025 · 0,039 · 0,043 · 0,052**
— todos < 0,06 (r4: 4/6). Fecha a pendência de poder do r4.

### 3.5 Diagnósticos

- **Vereditos (135):** `SEPARA 53 · INCONCLUSIVO 69 · EQUIVALENTE 7 ·
  INCOERENTE_DISCORDANTE 6` — **nenhum `*_FLAG`**: a metade "concordante"
  da regra de 2 níveis **não disparou uma única vez** em dados reais (todos os
  6 pontos fora eram discordantes) — a regra de flag foi exercitada só no
  smoke test (limitação honesta, §5).
- **Por métrica (discordantes):** saltos 5/27 · hurst 1/27 · boxdim **0/27**
  · boxdim_rank 0/27 · higuchi **0/27**.
- delete-d vs delete-1 não se aplica mais (jackknife do método novo é o
  delete-one estratificado; a concordância r3/r4 ficou sem objeto).

## 4. Interpretação

1. **Os três itens pedidos foram entregues e confirmados:**
   (i) **`saltos` primário: CONFIRMADA 3/3 Bonferroni** em 3 rodadas
   independentes — a métrica local é a âncora experimental da linha;
   (ii) **método novo com calibração**: percentil+estratificado — incidência
   real **4,4%** (r4: 33%), head-to-head **0/9 vs 4/9** que o método antigo
   bloquearia, tipo-I 0,075 calibrado antes do run;
   (iii) **regra de 2 níveis** aplicada e exaustiva — com a ressalva de que o
   ramo "concordante" nunca precisou disparar (§3.5).
2. **boxdim amadureceu:** as 3 chaves que o r4 perdeu para incoerência
   (b)(d)(f) saíram **limpas e confirmadas**; (c) virou **equivalência
   certificada a ±0,05**; (a) permanece sem efeito (3 rodadas) — o
   "padrão-τ" é real só em (b).
3. **O mecanismo do r4 está fechado:** o problema nunca foi "n = maior" nem a
   métrica — era o **modelo de dependência do bootstrap** (bloco em série
   temporal para dados iid-estratificados). Corrigido o modelo, a incoerência
   caiu 33% → 4,4% e os ICs degenerados 16 → 2.
4. **Poder resolvido:** MDE 6/6 < 0,06 — a régua de n do r4 está cumprida.

## 5. Limitações

1. **Ramo "concordante" da regra não testado em dados reais** (0 ocorrências)
   — só em smoke test; se um dia disparar, é a primeira vez.
2. **Discordantes concentrados em `relinc` (5/6)** — a aproximação de estratos
   do `relinc` (1º estrato −1) é a suspeita principal; `raw` (confirmatório)
   está limpo, mas a variante exploratória precisa de tratamento exato em r6.
3. **(a) do H_D2: previsão direcional errada 3×** — qualquer rodada futura
   deve redefinir (a) como hipótese de equivalência, não de separação positiva.
4. **(e) encolheu** (−0,11/−0,13 → −0,037) — continua excluindo 0, mas a
   magnitude não é estável entre rodadas; leitura: efeito de fonte pequeno.
5. Escopo: distribuição dos geradores (seeds disjuntos r2–r4); n=512; N1+N2;
   H_C2 (EF) deferido; τ k↑ aberta.
6. Incidentes de execução (§3): 2 bugs de plumbing pós-pré-registro — nenhum
   tocou as regras; custo: ~1,5h + 2 arranques.

## 6. Próximos passos (r6)

1. **Estratos exatos do `relinc`** (fronteiras recalculadas após a diferença)
   ou retirá-lo das contagens — fecha a suspeita de §3.2/§5.2.
2. Redefinir H_D2(a) como **equivalência** (3 falhas direcionais) e discutir
   se `fonte:τ` (e) deve manter magnitudes entre rodadas.
3. Consolidação da linha: com método, régua, poder e métrica primária
   estabilizados, a próxima pergunta científica pode ser **τ k↑** (pendência
   original) ou **séries em b** — não mais infraestrutura de IC.
4. τ k↑ (exige escopo minref>n6) e H_C2 (EF) permanecem abertas.

---

**Referências:** `31_` + referee (A1–A8 → §1.1) · `30_` (r3) · `29_` §8 (r2) ·
`28_` (origem) · `gk_proof_fractal_v5.py` (pré-registro executável) ·
Efron (1987) BCa · Politis & Romano (1994) bootstrap estratificado/estacionário ·
Lakens (2017) TOST

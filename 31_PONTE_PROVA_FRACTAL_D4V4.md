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

## 3. Resultados (execução: 20–21/11/2026)

**Execução e incidente (registro honesto):** o run1 morreu com **crash
nativo** no destrutor `Cadical195.__del__` (exit `0xC0000005` — violação
de acesso; mesma família do `0xC0000409` do v1; traceback perdido no
stderr do PowerShell). A reprodução standalone de `cadeia` (384/384 em
486s, exit 0) mostrou que o bug é **probabilístico** (timing de GC), não
determinístico. **Resposta:** fix de plumbing `3d244ab` (checkpoint
atômico por instância + `--resume`, **sem tocar no pré-registro** —
hipóteses/margens/regras/grade de `9fe7165` intactas) + loop de retry.
Resultado: **3 tentativas**, perda máxima de instâncias em voo, coleta
completa. Autenticidade dos dados: geradores `_det_seed` determinísticos
→ mesma instância produz o mesmo resultado em qualquer processo;
selftests+DISJ reexecutados em cada tentativa.

- **Coleta:** **1152/1152 UNSAT** · 0 censuras · 0 descartes · 51,8min
  (tentativa final) · `DISJ OK` (r2∪r3) · CSV `c92f0968…` (sem tempo);
  10 instâncias lentas (>2min; máx. 20,1min).
- **Selftests no run:** S1 OK · S2/S3 OK · S4 tipo-I **0/30** ·
  S5 poder **10/10 coerentes** · DISJ OK.
- **Análise:** 135 contrastes (56min) → `8419f25b…`.
- **Vereditos globais (135):** `INCOERENTE 45 · SEPARA 43 ·
  INCONCLUSIVO 41 · EQUIVALENTE 6`.

### 3.1 H_C1 — PRIMARIA (boxdim, 6 testes): **INDETERMINADO (2/6 contáveis; 4 incoerentes)**

| # | Teste | point | BC95 | pct | z0 | Veredito |
|---|---|---|---|---|---|---|
| (a) | minref:imp−τ > 0 | **−0,0244** | [−0,045; +0,023] | [−0,090; **−0,005**] | +0,94 | **FALHA_INCONCLUSIVO** (sinal invertido vs r3) |
| (b) | minref:cadeia−τ > 0 | +0,0476 | **[+0,038; +0,038] degenerado** | [−0,045; +0,019] | **+3,29** | **INCOERENTE** |
| (c) | minref:imp−cadeia ≡ ±0,08 | −0,0720 | [−0,105; −0,073] (ponto fora) | [−0,072; +0,003] | −1,98 | **INCOERENTE** (eq@0,06/0,08/0,10: todos **False**) |
| (d) | drat:imp−cadeia < 0 [pista] | −0,1069 | [−0,110; −0,108] (ponto fora) | **[−0,101; −0,055] exclui** | −2,46 | **INCOERENTE** |
| (e) | fonte:τ < 0 | **−0,1281** | **[−0,186; −0,098] ✅** | [−0,152; −0,061] ✅ | −0,84 | **OK_BONF** |
| (f) | fonte:cadeia < 0 | −0,0916 | [−0,118; −0,095] (ponto fora) | **[−0,087; −0,049] exclui** | −2,23 | **INCOERENTE** (idem r3) |

Aplicadas as **regras exaustivas do pré-registro (A3)**: contáveis = 2 <
⌈0,6·6⌉ = 4 → **INDETERMINADO** (não "REFUTADA", não "CONFIRMADA" —
exatamente o caso que o r3 deixou em aberto). Leitura dos contáveis:
**(e) confirma** (3ª rodada consecutiva: r2 −0,112 → r3 −0,102 →
r4 −0,128); **(a) efeito ≈ 0 com sinal invertido** (r3: +0,0595 —
era 1,4σ com percentil incluindo 0; o padrão-τ em boxdim **não se
sustenta**); (c) não é equivalente em **nenhuma margem** e apontaria
separação negativa se fosse coerente. Em (d) e (f) **os DOIS métodos
excluem 0 no sinal esperado**, mas o ponto estimado cai fora do IC
BCa → a regra pré-registrada bloqueia: **evidência indicativa, não
confirmação**.

### 3.2 H_C2 — SECUNDARIA (saltos, 3 testes): **CONFIRMADA (3/3)** ✅

| Teste | âncora r3 | r4 point | BC95 | BC99 (Bonf.) | pct | z0 |
|---|---|---|---|---|---|---|
| minref:imp−τ > 0 | +0,173 | **+0,1847** | [+0,132; +0,246] | [+0,113; +0,259] ✅ | [+0,122; +0,240] ✅ | +0,19 |
| drat:imp−cadeia > 0 | +0,110 | **+0,1173** | [+0,082; +0,207] | [+0,063; +0,207] ✅ | [+0,019; +0,146] ✅ | +0,96 |
| fonte:cadeia > 0 | +0,120 | **+0,1134** | [+0,055; +0,178] | [+0,037; +0,194] ✅ | [+0,052; +0,175] ✅ | +0,06 |

**3/3 `OK_BONF`** — Bonferroni (α=0,05/3) **e** percentil concordam,
pontos dentro do IC, z0 saudáveis (|z0| ≤ 0,96), âncoras r3 replicadas
com desvios ≤0,012. **Resultado positivo principal do r4.**

### 3.3 H_C3 — DIAGNOSTICO z0: **D2 CONFIRMADA; escalada com n quantificada**

| Métrica | incoerentes r4 (n=384) | r3 (n=64) |
|---|---|---|
| boxdim | 13/27 | 3/27 |
| boxdim_rank | 10/27 | 3/27 |
| higuchi_D | 12/27 | 0/27 |
| hurst_rs | 8/27 | 3/27 |
| **saltos** | **2/27** | **0/27** |
| **total** | **45/135 (33%)** | **9/135 (7%)** |

- **D1:** contingência `|z0|>1,5` ⟺ `|bias/SE|>1,2` → **127/135 = 94,1%**
  (z0 ≈ viés/SE confirmado — z0 é literalmente a correção de viés).
- **D2 (claim): CONFIRMADA** — todos os **16 degenerados** (`lo==hi`)
  têm `|z0|>2,5` (todos no **clamp** z0=±3,29 = Φ⁻¹(1−0,5/B): viés tão
  extremo que ~todo o bootstrap fica de um lado só).
- **D3:** discordância pct-vs-BCa: grupo extremo **47,5%** vs normal
  **32,4%** (maior no extremo, mas a base já é alta — 53/135 = 39%
  discordam no total).
- **D4: EXPECTATIVA REVERTIDA** — mediana |z0|: família **1,54** >
  fonte **0,82** (esperava-se fonte > família, com base no r3). A
  hipótese r3 de "macroestruturas de fonte não cancelam" é **falsificada**
  aqui; o fator dominante é o **par família×parâmetro**, não a fonte.
- **Mecanismo (achado central):** o viés bootstrap (destruição de
  macroestrutura pelo bloco fixo d=8) **não encolhe com n**, enquanto o
  SE encolhe ~1/√n → `z0 = viés/SE` **cresce com n** → BCa colapsa
  (degeneera/desloca). Coerente com a escalada 7%→33%. **Bloco fixo +
  BCa é inadequado para n grande neste desenho.**

### 3.4 H_C4 — ALVO DE DESIGN: **NAO_ATINGIDO (4/6)**

MDE80 dos 6 testes boxdim: 0,033 · 0,027 · 0,047 · 0,055 · **0,061 (a,
perdeu por 0,0009)** · **0,068 (e)** → 4/6 < 0,06. A previsão √(64/384)
acertou em 4; erros de −4% a +40% ((e) escalou pior que o previsto).
**Falha de alvo, não de hipótese** (como declarado).

### 3.5 Diagnósticos gerais

- **delete-d vs delete-1: 0/135 discordâncias** (3ª rodada consecutiva —
  C3/r3 replicado; os dois jackknifes são operacionalmente equivalentes).
- **Discordância pct-vs-BCa: 53/135 (39%)** — a escolha do IC primário
  (A4: BCa) está sob tensão quantificada (pendência r5).
- **MDE de saltos:** 0,085–0,095 vs efeitos 0,113–0,185 → razão ≥1,2;
  detecções a 3,4σ–6σ — solidez compatível com o 3/3.

## 4. Interpretação

1. **`saltos` é a métrica que sobrevive** (H_C2): estatística **local**
   preservada pelo block-resample → viés≈0 → z0 saudável → BCa e
   percentil concordam → **3/3 com Bonferroni, 2 rodadas de âncora
   (r3→r4)**. É a candidata natural a **métrica primária de r5**.
2. **O padrão-τ em boxdim não se sustenta** (H_C1): (a) virou ≈0 com
   sinal invertido — o "OK" do r3 era fraco (percentil nunca excluiu);
   (c) não é equivalente em nenhuma margem; (d)(f) têm a evidência bruta
   (dois métodos excluem) mas são bloqueados pela regra. **Única
   replicação boxdim sólida: fonte:τ (e), 3 rodadas.**
3. **BCa com bloco fixo degrada com n** (H_C3): mecanismo quantificado
   (D1 94%, D2 confirmada, escalada 7%→33%) — **achado de método** que
   vai para r5: bloco escalonado (`d = n/32`), *stationary bootstrap* ou
   percentil-com-nota devem ser decididos **antes** da próxima série.
4. **Expectativa D4 revertida** — registrada como falsificada, não
   contornada.
5. **O que o r4 responde:** (i) alvo de poder quase atingido (4/6);
   (ii) regras exaustivas produziram o veredito correto
   (`INDETERMINADO`) em vez de forçar confirmação/refutação; (iii) o
   diagnóstico de z0 saiu de "suspeita" para **mecanismo medido**.

## 5. Limitações

1. **H_C1 sem resposta** (INDETERMINADO) — desfecho legítimo do
   pré-registro, mas 4/6 incoerentes: o experimento primário não
   decidiu. A regra de incoerência (pré-registrada desde r2) é estrita
   demais para (d)(f) (ambos os métodos excluem, ponto fora) — mudá-la
   é pendência de r5 com pré-registro novo.
2. **H_C4: 4/6** ((a) perdeu por 0,0009; (e) 0,0684).
3. **D4 revertido** — a justificativa r3 para "fonte pior" estava errada.
4. **Discordância pct-vs-BCa 39%** — a primariedade BCa (A4) resolveu
   a continuidade mas está empiricamente tensionada.
5. **Coleta em 3 processos** (incidente §3): consistência garantida por
   geradores determinísticos + selftests por tentativa; o artefato
   canônico é o CSV final (`c92f0968…`).
6. N1+N2; sem N4; H_C2 (EF) deferido; τ k↑ aberta.

## 6. Próximos passos (r5)

1. **Método de IC decidido ANTES da série:** candidatos — bloco
   escalonado `d=n/32` (mantém efetivos ~32), *stationary bootstrap*
   (Politis–Romano, bloco médio ~n/16) ou percentil com nota de viés;
   BCa+bloco fixo fica **descartado para n grande** (medido aqui).
2. **`saltos` como métrica primária pré-registrada** (3/3 em duas
   rodadas); boxdim mantida como secundária com a régua revisada
   (pré-registrar o tratamento de "ponto fora mas métodos concordam").
3. Reavaliação de H_C1 com método novo — preferencialmente **nova série**
   (pré-registro limpo) em vez de re-análise pós-hoc dos dados r4.
4. τ k↑ (pendência inalterada) e séries em b com minref.
5. MDE: para (a)/(e) < 0,06, n≈512 ou aceitar alvo por família.

---

**Referências:** `30_PONTE_PROVA_FRACTAL_D4V3.md` + referee (A1–A7 → §1.1) ·
`29_` §8 (r2) · `28_` (origem) · `gk_proof_fractal_v4.py` (pré-registro
executável) · Efron (1987) BCa · Lakens (2017) TOST · Politis & Romano (1994)
stationary bootstrap (contexto do viés de macroestrutura)

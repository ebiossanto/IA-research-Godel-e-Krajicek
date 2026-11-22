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

## 3. Resultados (execução: 22/11/2026)

**Execução:** H_E1 (re-análise)1 tentativa, ~36min; run completo em **4
tentativas** (3 crashes `Cadical195.__del__` contidos pelo checkpoint —
coleta final **1536/1536 UNSAT**, 0 censuras; estratos corretos) + análise
~86min. Selftests S1–S7 OK em **cada** tentativa (S7 smoke pegou o caminho
antes de queimar análise — a lição do r5 virou rotina). Progress print
adicionado pós-pré-registro (`a2316b9`, plumbing). **Artefatos:** série
`5571b05f…` (input idêntico ✓) · contrastes `c567dbfd…` · H_E1
`d3b6b336…`.

### 3.1 H_E1 — FIX DOS ESTRATOS (re-análise do CSV r5): **PARCIAL (2/45)**

Discordância `relinc`: **5/45 → 2/45**; **todos os5 originais
resolvidos** (3→`INCONCLUSIVO`, 2→`SEPARA` — todos contáveis). Os2
restantes são chaves novas (`higuchi_D:relinc` de pares minref), não as do
r5. A fronteira aproximada era a causa suspeita — confirmada como
principal. *(Alvo pré-registrado era ≤1/45;2 = PARCIAL pela régua.)*

### 3.2 H_F1 — SALTOS PRIMÁRIO (4ª rodada): **CONFIRMADA [1 flag]** ✅

| # | Teste | r3 | r4 | r5 | **r6** | Veredito |
|---|---|---|---|---|---|---|
| (a) | minref:imp−τ > 0 | +0,173 | +0,185 | +0,138 | **+0,1046** | **OK_BONF** |
| (b) | drat:imp−cadeia > 0 | +0,110 | +0,117 | +0,080 | **+0,1686** | **OK_BONF_FLAG** ⚠ |
| (c) | fonte:cadeia > 0 | +0,120 | +0,113 | +0,104 | **+0,1426** | **OK_BONF** |

- **(b) é a primeira disparação real do ramo "concordante"**: ponto
  (0,1686) caiu **0,0012 acima** do IC percentílico [0,064; 0,167], mas
  percentil **e** BCa excluem0 positivo coerentemente → `OK_BONF_FLAG`
  **conta com flag**. Sem a regra de 2 níveis (r4 A5), este teste seria
  perdido — exatamente o caso `(d)(f)` do r4.
- **H_F1b (Cochran Q, 4 rodadas): `SEM_HETEROGENEIDADE`** — p = **0,221 /
  0,134 / 0,708** (gl=3). **A pergunta de declínio do r4 (A1) foi
  respondida com teste:** as magnitudes variam (0,10–0,19) sem tendência
  detectável. *(Caveat declarado: rodadas com n/grades diferentes — Q
  captura variação total.)*

### 3.3 H_F2 — BOXDIM SECUNDÁRIO (com (a) redefinido): **CONFIRMADA (6/6)** ✅

| # | Teste | r5 | **r6 point** | pct95 | Veredito |
|---|---|---|---|---|---|
| (a) | imp−τ ≡ ±0,05 (redefinido) | FALHA −0,012 | **+0,0083** | [−0,008; +0,021] | **OK = EQUIVALENTE** (eq@**0,03** ✓ também) |
| (b) | cadeia−τ > 0 | OK_BONF +0,025 | **+0,0446** | [+0,028; +0,054] | **OK_BONF** |
| (c) | imp−cadeia ≡ ±0,05 | OK −0,037 | **−0,0363** | [−0,049; −0,020] | **OK = EQUIVALENTE** (TOST: CI95 exclui 0, IC90 na margem) |
| (d) | pista drat imp−cadeia < 0 | OK_BONF −0,068 | **−0,0768** | [−0,082; −0,058] | **OK_BONF** |
| (e) | fonte:τ < 0 | OK −0,037 | **−0,0653** | [−0,077; −0,022] | **OK_BONF** |
| (f) | fonte:cadeia < 0 | OK_BONF −0,051 | **−0,0597** | [−0,060; −0,041] | **OK_BONF** |

**6/6 — a consolidação do boxdim**: as6 previsões (2 equivalências +
4 direcionais com Bonferroni 0,05/4) passam; **5 de6 teriam sido
bloqueados pelo método do r4** (`bloco8_fora` em5). A redefinição de (a)
como equivalência (A5) foi acertada — e (a) é equivalente até na margem
apertada0,03.

### 3.4 H_F3 / H_F4 / H_F5

- **H_F3 CONFIRMADA:** `relinc` discordante **1/45 (2,2%)** em dados
  novos (r5: 5/45; gate ≤10%) — o fix dos estratos vale fora da
  re-análise também.
- **H_F4 `DISPAROU (4x)`:** o ramo concordante disparou4 vezes em
  dados reais (r5:0) — **mantido** (não remove em r7): `drat:imp−cadeia:saltos`
  raw+log1p, `fonte:cadeia:boxdim:log1p`, `fonte:cadeia:hurst:relinc`.
- **H_F5 ATINGIDO 6/6:** MDE80 = **0,014–0,042** (melhor que r5).

### 3.5 Diagnósticos

- **Vereditos (135):** `SEPARA 61 · INCONCLUSIVO 58 · EQUIVALENTE 5 ·
  SEPARA_FLAG 4 · INCOERENTE_DISCORDANTE 7`.
- **Por métrica:** boxdim **0 incoerentes** (21 SEPARA +5 EQ +1 FLAG) ·
  boxdim_rank 0 · higuchi 0 (27 todos INCONCLUSIVO) · saltos3 · hurst4.
- **z0 extremos 28/135** (r5:12; r4:61) e4 degenerados — subiu vs r5
  (nota honesta); **discordância total7/135 =5,2%** (r5:4,4%) — estável
  abaixo do gate10%.
- Os7 discordantes: pares `drat:cadeia−τ:saltos` e `*:hurst_rs` — nenhum
  confirmatório.

## 4. Interpretação

1. **Consolidação entregue:** com método, régua, margens e métrica
   primária fixados, o r6 rodou **6/6 no boxdim** e **3/3 no saltos**
   (4ª rodada) — as previsões pré-registradas passaram sem ajuste.
2. **A regra de 2 níveis se pagou** na primeira disparação real: (b) do
   H_F1 seria perdida pela régua do r4 (ponto fora), mas concordância
   dos métodos a salvou **com flag visível** — transparência + não
   desperdiço.
3. **A pergunta do declínio (r4 A1) está respondida:** Cochran Q **sem
   heterogeneidade detectável** em3/3 testes (p=0,13–0,71) — não há
   tendência detectável em4 rodadas ("não detecta" ≠ "não há", referee
   A6); as variações de magnitude são compatíveis com ruído entre
   amostras.
4. **O fix dos estratos do `relinc` valeu:** H_E1 (5→2 no mesmo dado) e
   H_F3 (1/45 em dado novo) — a fronteira aproximada era a causa.
5. **Poder no máximo da linha:** MDE 0,014–0,042 (6/6) — n=512 com
   método calibrado entrega a régua mais fina até agora.

## 5. Limitações

1. **(c) é TOST de novo** (CI95 exclui0 mas IC90 na margem → equivalente)
   — leitura "diferente mas <Δ" mantida; o parceiro BCa discorda da
   equivalência (`bca_eq=False`) — dentro do primário decide (pré-registrado).
2. **z0 extremos subiram12→28** e4 degenerados (r5) — ainda muito abaixo
   de r4 (61/16), mas a tendência entre r5→r6 pede monitoramento; os7
   discordantes estão todos fora dos confirmatórios.
3. **Cochran entre rodadas com n/grades diferentes** (declarado) — Q mede
   variação total, não só declínio temporal.
4. **H_E1 = PARCIAL** (2/45 vs alvo ≤1/45) — fix bom, não perfeito.
5. Escopo: distribuição dos geradores; n=512; N1+N2; H_C2 (EF) deferido;
   τ k↑ aberta; incidentes:3 crashes CaDiCaL + progress print pós-pré-reg.

## 6. Próximos passos

1. **A linha de IC/infra está consolidada** (método + régua + margens +
   métrica + poder estáveis por2 rodadas) — a próxima rodada deve ser
   **científica, não de infraestrutura**: **τ k↑** (pendência original;
   exige estender o escopo do minref para n>6 ou método alternativo de
   comprimento mínimo) ou **séries em b** (índice lex de b — a série
   ordinal original do D4′).
2. Monitorar z0 extremos (12→28) — se r7 subir de novo, investigar a
   origem (pare `drat:cadeia−τ` aparece em2 rodadas).
3. H_C2 (EF) permanece deferido; ramo concordante mantido (disparou4×).

---

**Referências:** `32_` + referee (A1–A8 → §1.1) · `31_`–`28_` (linha) ·
`gk_proof_fractal_v6.py` (pré-registro executável) · Cochran (1954) Q ·
Efron (1993) BCa · Politis & Romano (1994) bootstrap estratificado ·
Lakens (2017) TOST

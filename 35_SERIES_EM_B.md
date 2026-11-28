# 35 — Séries em b: índice lex de b para σ fixo (série ordinal do D4′)

**Data:** 26/11/2026 · **Classificação:** **(P)** experimento próprio +
**(C)** hipóteses pré-registradas · **Nível Ten-Proofs:** N1 + N2 ·
**Não** é claim de EF · **não** é lower bound.

> **PROTOCOLO DE PRIORIDADE TEMPORAL:** hipóteses, direção, grade,
> orçamentos e regras deste documento e do script `gk_series_b.py` foram
> fixados e **commitados ANTES de qualquer execução com dados do
> experimento** — o hash do commit de pré-registro prova a ordem (C1).
> As **sondas de engenharia** (struct seeds 5000–5004 do namespace
> `tau_b`, nunca os do experimento 6000–6015) foram executadas antes e
> registradas aqui; elas não contêm dados do experimento.

**Linha:** próxima da linha D4′ (`ONDE_ESTAMOS`): "séries em b (índice
lex — a série ordinal original do D4′)" — origem: `28_PONTE…` §7.3
("índice lex de b para σ fixo") e `29_…` §3 ("séries em b (índice lex)
**com minref**").

**Reproduzir:**
```powershell
python -u gk_series_b.py --selftest-only    # bateria (~3min)
python -u gk_series_b.py [--resume]          # coleta + análise (~17h)
python -u gk_series_b.py --analyze-only      # re-análise (~segundos)
# → gk_series_b_series.csv + gk_series_b.json
# seed=20261119 · seed_boot=20261130 · B=1000 (bootstrap) · 1000 (shuf)
```

---

## 1. Pré-registro (fixado antes do run)

### 1.1 Sondas de engenharia (seeds 5000–5004, namespace `tau_b`)

| Config | nvars | T (série) | fecho | minref | Veredito de desenho |
|---|---|---|---|---|---|
| (1,5) | 6 | 30 | 43 | exato, 0s | descartada — variação mínima (σ=5001 plano) |
| (1,6) | 7 | **62** | **57** | exato, 0s | descartada — minref quase plano (2/62 pontos≠5) |
| (2,6) | 8 | 60 | 6305 | **CENSURA @20M** (`t_cap=3`) | **DESCARTADA — parede n≥8** |
| **(2,5)** | **7** | **28–29** | ~2059 | **exato @6M (~115–140s/inst)** | **ESCOLHIDA** — variação rica: minref 5↔7 (var 0,928 em σ=5000); drat 8/9 |

**Censuras @6M por σ (varredura COMPLETA de4 sondas):**

| σ | fecho | X (censurados) | nota |
|---|---|---|---|
| 5000 | 2059 | **4/28** | minref desconhecido (censurado) |
| 5002 | 2124 | **0/28** ✓ | minref ∈{5,7} |
| 5003 | 2059 | **0/28** ✓ | alternante 5/7 quase perfeito |
| 5004 | 2124 | **3/29** | nota **`>7`** → minref **≥8** |

→ **~50% dos σ's contêm instância difícil (minref≥8)**. A sonda
**@20M** (mesmos4 X de σ=5000) está **>2,2h na primeira instância**
(REF_8/REF_9 com prova UNSAT dura — Alekhnovich-like) ⇒ **20M
INVIAVEL** por custo (~6 dias para a grade). **Decisão:** `max_aux=6M`
(pontos X censuram → σ sujo excluído) + **S=32** para robustez à taxa
~50% de sujos (esperado ~16 limpos; **P(≥12) ≈ 0,96**; gate H_b1 ≥12
inalterado).

- **Calibração prévia da máquina** (`calib_perm`, B=300, seed 20261130):
  tipo-I 1–3/40 (gate ≤0,15) e poder 10/10 nas grades (16,29)/(24,30);
  **S=8 perde poder (3/10)** → S≥16 justificado;
- **Métricas:** `hurst_rs` exige n≥36 e `higuchi_D` n≥32 (contrato:
  NaN em T=28 — declarado, não usado em claim).

### 1.2 Gerador σ-fixo e grade (DISJ)

`gen_tau_at_b(depth, struct_seed, b_rank, k=2, w=5)`:
- **σ fixo** = estrutura do circuito por `(depth, struct_seed)` no
  **namespace `tau_b`** (`_det_seed(SEED, "tau_b", …)` — DISJ do
  namespace `tau` usado em r2–τ k↑);
- imagem exata computada; **complemento ordenado lexicograficamente**;
  `b = complemento[b_rank]` (∉ imagem → UNSAT por construção; ASSERT
  por instância);
- **Equivalência sonda×script verificada: 5/5** (hash das cláusulas +
  tag + T idênticos).

**Grade:** `family="tau_b"`, `param=struct_seed` (σ), `seed=b_rank`:
- **σ ∈ 6000..6031 (S=32)** — DISJ das sondas (5000–5004) e de r2–τ k↑
  *(S subiu de16→32 pré-commit: sondas @6M mostraram ~50% de σ's
  sujos; S=32 dá P(≥12 limpos)≈0,96)*;
- `b_rank ∈ 0..T_σ−1` com `T_σ = 32 − |imagem_σ| ∈ {28,29}`;
- **~896 instâncias; ~115–140s/inst (sonda) → run ~30h**;
- `max_aux = 6M` (ver §1.1 — 20M inviável por custo).

### 1.3 Hipóteses

**H_b1 — VIABILIDADE (gate):** ≥ **12/32 σ's USULIZÁVEIS** = (0 censuras
no σ) AND (minref com variância > 0) AND (`acf₁` não-NaN).
`CONFIRMADA` ≥12 · `SEM_DADOS` <8 · `REFUTADA` caso contrário.
*Consequência pré-declarada:* σ's não utilizáveis são **excluídos** do
H_b2 (contagem reportada; **escopo:** H_b2 fala dos σ's **sem instância
minref≥8** — limitação declarada; sondas: ~50% dos σ's são sujos;
σ's constantes são o risco residual — k=1: metade dos σ's era plana).

**H_b2 — ESTRUTURA SERIAL EM b (PRIMÁRIA):** por σ utilizável,
`D_σ = acf₁(série real em ordem lex) − média₁₀₀₀ acf₁(permutações
internas da mesma série)`; estatística = média de D sobre σ;
inferência = **bootstrap sobre σ** (B=1000): **percentil 95% PRIMÁRIO +
BCa parceiro + jackknife delete-one + regra de 2 níveis** (idêntica a
r5/r6/τ k↑) + MDE80. **Direção −1 (alternância/anti-persistência)** —
*caveat pré-declarado:* a direção deriva da sonda σ=5000 (engenharia,
não experimento; D=−0,36 lá); se o sinal real for oposto com CI
excluindo 0 → `CONTRADITA` (honesto — registrado com o sinal).
`CONFIRMADA` iff percentil95 exclui 0 **E** BCa concordante no mesmo
sinal; senão `FALHA_INCONCLUSIVO` (leitura estatística obrigatória:
"sem suporte", poder declarado no S3). **α = 0,05 — hipótese única
confirmatória** (sem Bonferroni de grupo).

> **Histórico da métrica primária (transparência):** a v1 deste
> pré-registro usou `saltos` e o **S3 FALHOU (poder 0/10)** antes de
> qualquer commit — `taxa_saltos` é **degenerada em série binária**
> (com2 valores, toda transição ≠0 alterna sinal obrigatoriamente →
> `saltos ≡ 1,0` para série **e** permutações → D ≡ 0). Troca **pré-run**
> para **acf₁** (autocorrelação defasada-1), escolhida por teste
> empírico de poder: D(alternante)=**−0,94** · D(blocos)=**+0,93** ·
> D(sonda real)=**−0,36** · D(iid)=±ruído; `boxdim`/`boxdim_rank` fracos
> (~0,06). Nada foi commitado até aqui — C1 intacto.

**H_b3 — DESCRIPTIVA (sem claim):** contraste pareado
`D_minref − D_drat` (mesma máquina) + tabelas por σ — **(P)/candidata
(C)** a rodada futura (seleção = pós-hoc, proibido verbo confirmatório).

**ASSERT (teorema, não hipótese):** `minref_exato ≥ d(∅)` por instância
+ `solve = UNSAT` por construção — violação = bug → exit3.

### 1.4 Métricas

- **Primária:** **`acf₁`** (autocorrelação defasada-1 de Pearson) —
  escolhida por teste empírico de poder (ver nota do H_b2); NaN em
  série constante (variância 0) → filtro do H_b1;
- **Descritivas por série:** `boxdim`, `boxdim_rank`, `saltos`,
  `higuchi_D`, `hurst_rs` — **contratos NaN pré-declarados:** higuchi
  (n≥32) e hurst (n≥36) retornam NaN em T∈{28,29} (S4 verifica);
- **`saltos` não é primária:** degenerada em série binária
  (`saltos ≡ 1,0` com ≥4 transições; NaN com <4) — descoberto pelo S3
  **antes** do commit; fica só descritiva (S4 fixa o contrato).

### 1.5 Regras de veredito

Regra de 2 níveis **idêntica a r5/r6/τ k↑** aplicada ao contraste
bootstrap-sobre-σ (ponto dentro → veredito normal; ponto fora →
concordância percentil×BCa decide com flag ou discordância não conta);
direção +1 para H_b2; global: `OK`/`OK_FLAG` → CONFIRMADA;
`FALHA_INCONCLUSIVO*` → sem suporte; `CONTRADITA*` → REFUTADA.
H_b1 por contagem (gate). H_b3 sem veredito (descritiva).

### 1.6 Selftests (antes do commit; repetidos no run; A8)

| # | Teste | Gate |
|---|---|---|
| S1 | BCa vs `scipy` (iid) | diff ~0,01 |
| S3 | **Máquina completa** (D_σ + bootstrap sobre σ): tipo-I 40 séries iid + poder 10 (alternante 5/7 + ruído 0,35, dirn=−1) | tipo-I ≤0,15 · poder ≥7/10 — **resultado: 4/40=0,100 · 10/10 OK** |
| S4 | Métricas em T=28: acf₁ não-NaN em binária não-constante e NaN em constante; `saltos`≡1,0 (degeneração documentada) e degrau→NaN; boxdim_rank invariante monotona; hurst/higuchi NaN | OK |
| S5 | **Smoke de `analyze()` com `contrast_over_sigma` stubado** — lição r5 | OK |
| S6 | **Determinismo do DRAT** (2 execuções → mesmo comprimento) | OK |
| DISJ | grade × (v2..v6 + τ k↑) = ∅ | OK |
| Equiv | gerador script ≡ sonda (5/5 hash+tag+T) | OK |
| Censuras | varredura completa de4 σ's @6M (0/0/4/3 X) + sonda @20M (>2,2h, inviável) → decisão `6M` + `S=32` | ver §1.1 |

---

## 2. Método (execução)

Coleta com **checkpoint atômico + `--resume`** (crash CaDiCaL
possível): por `(σ, b_rank)` → `gen_tau_at_b` → `solve` (UNSAT exigido)
→ `minref_deep(max_aux=6M, with_info)` → `solve_drat` → linha com
`lb`, `t_testados`, `pares_ultimo`. Análise: séries por σ em ordem de
`b_rank` → H_b1 (contagem), H_b2 (D_σ + bootstrap sobre σ), H_b3
(descritiva), assert, tabelas → `gk_series_b_series.csv` +
`gk_series_b.json` (R6 protege o par).

## 3. Resultados *(pós-execução — run concluído 27/11 21:51 local, exit 0)*

**Execução:** 904/904 instâncias (grade real: T_σ ∈ {28,29,30} —
σ=6013 tem imagem=2 → T=30), `mode=resume+collect+analyze`,
`runtime=41926s` (tentativa2) · coleta 698min · **0 descartes** ·
**ASSERT 0 violações** · selftests **todos OK** no run (S1 0,013 ·
S3 tipo-I **1/40=0,025** + poder **10/10** · S4 contratos NaN · S5
smoke · S6 drat determinístico · DISJ ∅). Artefatos:
`gk_series_b_series.csv` (**sha256 `50ecd215dae321c5…`**) +
`gk_series_b.json` (R6 protege o par).

**Incidente (contido):** TENTATIVA 1 morreu com **`0xC0000005`**
(ACCESS_VIOLATION — classe nativa CaDiCaL conhecida) após **507
linhas**; o checkpoint atômico salvou tudo → TENTATIVA 2 (`--resume`)
retomou das507 e completou as904 + análise. Padrão τ k↑ repetido com
sucesso.

**Censuras:** 60/904 pontos (6,6%) — mas concentradas: **14/32 σ's**
têm ≥1 ponto censurado (~4 X por σ sujo, como as sondas) → excluídos.

### 3.1 H_b1 — VIABILIDADE: **CONFIRMADA**

**16/32 σ's utilizáveis** (gate ≥12 ✓). Decomposição: 18 completos −
2 constantes (σ=6003 e 6021: minref **todo 5** → acf₁ NaN) = 16;
14 censurados (6004-6007, 6009, 6012-6013, 6016-6018, 6020, 6023,
6028, 6030). **Os16 utilizáveis:** 6000, 6001, 6002, 6008, 6010, 6011,
6014, 6015, 6019, 6022, 6024, 6025, 6026, 6027, 6029, 6031.

### 3.2 H_b2 — ESTRUTURA SERIAL EM b (PRIMÁRIA): **CONFIRMADA (OK)**

`D_σ = acf₁(real) − média₁₀₀₀ acf₁(permutações)`; média sobre os
**16 σ's**:

| Estatística | Valor |
|---|---|
| **ponto** | **−0,2431** |
| percentil 95% (PRIMÁRIO) | **[−0,3653, −0,1086]** — exclui 0 |
| BCa (parceiro) | **[−0,3543, −0,0947]** — exclui 0, mesmo sinal → **concordante** |
| veredito interno | `SEPARA` (ponto dentro do IC) → classificação dirn=−1 → **OK** |
| SE / MDE80 | 0,0652 / **0,1827** (|efeito| 0,243 > MDE ✓) |
| z0 / n_boot / n_jack | 0,0527 (saudável) / 1000 / 16 |

**Consistência por σ:** 14/16 D's negativos (extremos: σ=6026 −0,727 ·
σ=6029 −0,531 · σ=6019 −0,528); ≈0 em 6000 (+0,004) e 6025 (−0,003);
**um outlier positivo**: σ=6027 **+0,447** (registrado — ver §5).

**Leitura:** a sequência `minref(b₀), minref(b₁), …` em ordem lex de
`b` (σ fixo) é **anti-persistente**: níveis alternam (5→7→5…) mais do
que o esperado por embaralhamento — **a série ordinal do D4′ indexada
por b carrega estrutura serial real**.

### 3.3 H_b3 (DESCRIPTIVA — sem claim): polaridades opostas

Nos **10 σ's** com ambas as séries utilizáveis: `média D_minref =
−0,225` vs `média D_drat = **+0,796**` — contraste −1,021
(percentil [−1,271; −0,749], BCa [−1,241; −0,695], `SEPARA`).
**minref alterna; drat é persistente** (runs longos de mesmo
comprimento) — padrão de polaridade oposta, **(P)/candidata (C)**,
sem verbo confirmatório (seleção pós-hoc).

### 3.4 Tabelas/diagnóstico

- **minref exato** nos σ's utilizáveis: valores ∈ {5,7,9,11} (alguns
  σ's têm9/11 **exatos** @6M — instâncias de pares pequenos);
- `T_σ` ∈ {28,29,30}; `drat_mean` por σ: 6,2–21,6 (variação grande);
- **`saltos` ≈ 1,0 em todas as séries binárias** (degeneração
  documentada pelo S4 — confirmada nos dados reais) → métrica inútil
  aqui; `boxdim_rank` ∈ 0,57–0,88 varia normalmente;
- `hurts/higuchi` NaN (T<32/36) — contrato S4 cumprido.

## 4. Interpretação *(pós-execução)*

1. **A série ordinal do D4′ existe e é estruturada (P):** o índice lex
   de `b` para σ fixo revela **anti-persistência** em `minref`
   (H_b2 OK, efeito −0,243 > MDE 0,183, 14/16 σ's no sinal) — a
   pergunta original do doc28 §7.3 respondida com dado novo;
2. **Mecanismo plausível:** `minref` ∈ {5,7} alterna porque b's lex
   vizinhos diferem em bits de baixa ordem → o resolvente/propagação
   muda de paridade a cada passo → comprimento mínimo oscila. (Não
   provado — interpretação (C) qualitativa.)
3. **minref × drat com polaridades opostas (P):** a prova do solver
   (drat) agrupa-se em runs (persistência +0,80) enquanto o mínimo
   alterna — o solver "suaviza" a alternância canônica. Candidata (C)
   natural a pré-registro (H de rodada futura: D_drat − D_minref > 0);
4. **Viabilidade de n=7 com σ fixo:** 6M resolve16/32 σ's — a
   exclusão de sujos é o preço do exato (escopo declarado).

## 5. Limitações *(pós-execução)*

- **Escopo do H_b2:** fala **apenas dos σ's sem instância minref≥8**
  (16/32) — exclusão **dirigida pelo resultado** (pré-declarada, mas
  real): se sujos tiverem outra dinâmica, o claim não os cobre;
- **Direção −1** derivada de UMA sonda (σ=5000) — se fosse oposta,
  o resultado seria `CONTRADITA`; deu certo, mas é sorte de desenho
  declarada;
- **n=16** no bootstrap (jackknife16): MDE 0,183 — efeitos < ~0,2
  indetectáveis; **σ=6027 (+0,45)** outlier positivo não explicado;
- **Séries curtas e binárias** (T=28-30, valores5/7/9/11):
  `hurst`(n≥36)/`higuchi`(n≥32) NaN; `saltos` degenerada — só
  `acf₁`/`boxdim*` utilizáveis (contratos S4);
- **Indexação lex é um caminho arbitrário** sobre {0,1}⁵ — a
  anti-persistência pode ser específica da ordem lex (Gray seria
  outra — futuro);
- **H_b3 com10 pares** (séries drat constantes em6 σ's) — descritiva
  por construção;
- **Incidente0xC0000005** contido por checkpoint (507→904) — classe
  nativa conhecida, sem perda.

## 6. Próximos passos *(pós-execução)*

1. **H_b3 → candidata (C) pré-registrável:** `D_drat − D_minref > 0`
   (polaridades opostas) com a máquina desta rodada em grade nova
   DISJ;
2. **Indexação alternativa:** série em **código de Gray** de `b`
   (vizinhos diferem1 bit) — se a anti-persistência é do lex ou de
   `b` em si;
3. **σ's sujos:** tentar `max_aux` intermediário (~8-10M) com
   **teto de wall-clock pré-registrado** (a sonda @20M mostrou que
   minref=11 custa ~2h) para ampliar o escopo além dos16;
4. **Ligar à lacuna τ k↑:** a anti-persistência do minref pode
   explicar por que as médias ficaram planas (alternância cancela em
   média) — nota interpretativa p/ `34_` §4 (sem reabrir veredito).

---

**Referências:** `28_…` §7.3 · `29_…` §3 · `34_TAU_KUP_MINREF.md` ·
`gk_series_b.py` (pré-registro executável, commit `7f45d12`) ·
sondas `probe_series_b*.py`, `probe_variation.py`, `calib_perm.py` ·
`pequalnp/VARREDURA_2026-11-28.md` (rotina da sessão) ·
Efron (1993) BCa · r5/r6 (método percentil+BCa)

---

**Referências:** `28_PONTE_PROVA_FRACTAL_D4.md` §7.3 · `29_…` §3 ·
`34_TAU_KUP_MINREF.md` (τ k↑) · `gk_series_b.py` (pré-registro
executável) · sondas `probe_series_b*.py`, `probe_variation.py`,
`calib_perm.py` · Efron (1993) BCa · r5/r6 (método percentil+BCa)

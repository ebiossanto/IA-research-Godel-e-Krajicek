# 34 — τ k↑: estendendo o `minref` para n>6 (fronteira empírica + série)

**Data:** 21–22/11/2026 · **Classificação:** **(P)** experimento próprio +
**(C)** hipóteses pré-registradas · **Nível Ten-Proofs:** N1 + N2 · **Não** é
lower bound; **não** é claim de EF.

> **PROTOCOLO DE PRIORIDADE TEMPORAL:** hipóteses, grade, regras e orçamentos
> deste documento e do script `gk_tau_kup.py` foram fixados e **commitados
> ANTES de qualquer execução com dados do experimento** — o hash do commit de
> pré-registro prova a ordem (C1). As **sondas de fronteira** (seeds 1700+,
> nunca do experimento) são engenharia de viabilidade, executadas antes e
> registradas aqui; elas não contêm os dados do experimento.

**Linha:** pendência original do D4′ (`ONDE_ESTAMOS` §5-D4): "τ com tamanhos
crescentes (k↑) para curvas τ de maior dinâmica" — bloqueada porque o
`minref` só cobria n≤6. Este documento abre a fronteira.

**Reproduzir:**
```powershell
python -u gk_tau_kup.py --selftest-only    # bateria (~2min)
python -u gk_tau_kup.py [--resume]          # coleta + análise (~3.5h)
python -u gk_tau_kup.py --analyze-only      # re-análise (~1min)
# → gk_tau_kup_series.csv + gk_tau_kup.json
# seed=20261119 · seed_boot=20261127 · B=1000
```

---

## 1. Pré-registro (fixado antes do run)

### 1.1 Fronteira empírica (sondas — engenharia, seeds 1700+)

| Nível | nvars | fecho | DP | pares (dedup) | Exatidão com `minref_deep` |
|---|---|---|---|---|---|
| **k=2** | 5 | ≤211 | — | ~2·10³ | **sempre exato** (t_cap folgado) |
| **k=3** | 7 | 2059 (37s) | 6s, d(∅)=3 | 766k | **exato até minref=7** (max_aux=6M; REF_7 construído+resolvido, 173s); ≥8 censurado |
| **k=4** | 9 | 3551 (124s) | 19s, d(∅)=3 | 2,2M | **exato até minref=5** (max_aux=8M; REF_5 construído+UNSAT, 216s); ≥6 censurado (REF_6 exigiria ~13M auxs — memória impraticável, declarado) |
| **k≥5** | ≥11 | — | — | — | parede do fecho (não testado; projetado inviável) |

**Argumento de correção (pools de profundidade):** `d(C)=1` se `C∈γ`,
senão `min_pares max(d(c₁),d(c₂))+1`. *Toda linha j de uma refutação com
≤ t linhas tem `d ≤ j`* (indução: folha d=1; resolvente de linhas <j tem
d≤max+1≤j) → `d(∅) ≤ t` (**limite inferior testado**) e o pool `{d≤t}` com
pares restritos é **equivalente** ao REF_t sobre o fecho cheio — com
ordens de grandeza menos auxiliares. Pares **deduplicados** (o auxiliar
`a_{j,C,p}` é simétrico nos pais → metade). *Validação:* propriedade
`minref_deep = minref` em n≤6: **17/17 consistentes** no `demo` (que
permanece a suite de regressão do caminho original — byte-idêntico).

### 1.2 Grade (nova, disjunta de r2..r6 — aborta se intersectar)

`tau_tiny`, `depth=1`, `w=k+1`: **k ∈ {2,3,4} × seeds 1536..1667** (32/nível,
**96 total**; nvars 5/7/9). níveis anteriores usaram seeds ≤1535 (r2..r6).

### 1.3 Hipóteses

**H_t1 — VIABILIDADE:** em **k=3**, ≥ **16/32 (50%)** dos seeds têm
`minref` **exato** com `max_aux=6M`. `CONFIRMADA` ≥16 · `REFUTADA` <16.
*Consequência pré-declarada:* pontos censurados são **excluídos da série**
(regra existente das rodadas anteriores) e o censuramento **por nível** é
reportado.

**H_t2 — DINAMICA (crescimento com k):** médias de `minref` exato crescem
com o nível — **2 contrastes adjacentes** (bootstrap IID; percentil
**primário** + BCa parceiro + jackknife delete-one + **Bonferroni 0,05/2**
+ regra de 2 níveis idêntica às rodadas r5/r6):
- (i) média(k=3) − média(k=2) > 0
- (ii) média(k=4) − média(k=3) > 0

`CONFIRMADA` ⟺ 2/2 OK · `PARCIAL` 1/2 · `REFUTADA` 0/2 ·
`REFUTADA_CONTRADITA` se sinal oposto. **Caveat pré-declarado:** censuras
removem instâncias (geralmente as de minref **maior**) → as médias do nível
**subestimam**; uma falha pode ser artefato de censura — as censuras por
nível são reportadas junto.

**ASSERT (teorema, não hipótese):** `minref_exato ≥ d(∅)` em **todas** as
instâncias — violação = bug → o script retorna exit3 com relatório.

### 1.4 Métricas: descritivas (sem hipótese)

`hurst_rs`, `higuchi_D`, `boxdim`, `saltos`, `boxdim_rank` sobre a série
ordinal `(k, seed)` dos **minref exatos** e da série **DRAT dos mesmos
pontos**; CI percentil **estratificado** (estratos = níveis de k, B=1000)
como caracterização — **sem** comparações confirmatórias (boxdim cross-n é
confundido, lição do r4). Tabela de médias por nível (minref exato + DRAT
+ censuras) é o dado central da "dinâmica τ".

### 1.5 Regras de veredito

Idênticas às r5/r6 (2 níveis, exaustivas): ponto dentro → veredito normal;
ponto fora → concordância entre percentil e BCa decide (conta com flag) ou
discordância (não conta); Bonferroni do grupo = **0,05/2** (quantis
0,0125/0,9875). Global de H_t2: CONTRADITA* → REFUTADA_CONTRADITA; 2/2 →
CONFIRMADA; 1/2 → PARCIAL; 0/2 → REFUTADA (ou INDETERMINADO se tudo
discordante).

### 1.6 Selftests (antes do commit; repetidos no run; A8)

| # | Teste | Resultado |
|---|---|---|
| S1 | BCa vs `scipy` (iid) | **OK** diff 0,013 |
| S2 | Métricas n=96 (invariância rank + ordenações) | **OK** |
| S3 | Máquina de contrastes de médias: tipo-I 40 nulos + poder 10 (deslocamento 1σ) | **OK** — 3/40=0,075 · 10/10 |
| S5 | **Smoke de `analyze()` com `mean_contrast()` stubado** (H_t1/H_t2/assert/métricas) — lição r5 | **OK** |
| DISJ | grade × (r2..r6) = ∅ | **OK** |
| Propriedade | `minref_deep = minref` em n≤6 (demo) | **17/17** |

---

## 2. Método (execução)

Coleta com **checkpoint atômico + `--resume`** (crash CaDiCaL possível):
por instância → `gen_tau(1, seed, k, k+1)` → `minref_deep(max_aux por
nível: {2:400k, 3:6M, 4:8M}, with_info)` → `solve_drat` → linha com
`lb`, `t_testados`, `pares_ultimo`. Análise: H_t1 (contagem), H_t2
(2 contrastes), assert, métricas descritivas →
`gk_tau_kup_series.csv` + `gk_tau_kup.json` (R6 protege o par).

## 3. Resultados *(pós-execução)*

## 4. Interpretação *(pós-execução)*

## 5. Limitações *(pós-execução)*

## 6. Próximos passos *(pós-execução)*

---

**Referências:** `28_`–`33_` (linha D4′ + referees) · `gk_minref.py`
(`minref_deep`, `tree_depths` — nova extensão n>6) · `gk_tau_kup.py`
(pré-registro executável) · sondas `probe*_tau*.py` (fronteira) ·
Efron (1993) BCa · Lakens (2017) TOST (não usado aqui — sem eq)

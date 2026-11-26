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

### 2.1 Nota de execução — patch de desempenho da `saturation` (23/11, 06:29)

Durante a coleta de k=4, a instância s=1539 ficou **3h50min em 100% de
CPU dentro de `saturation`** (diagnosticado com py-spy). Causa: o laço
original re-sorta `sorted(derived)` para **cada** c1 → O(N²·N log N) por
passada; o fecho desta instância mediu **19171 cláusulas** (perto do
máximo 3⁹=19683; as 3 instâncias anteriores tinham ~3551).

**Patch (mesmo dia, antes de ver qualquer resultado agregado de k=4):**
`saturation` passa a usar **buckets por literal** (pares (c1 ⊃ l, c2 ⊃ -l)
por l>0). A versão original ficou como `saturation_ref` (só para teste).

**Invariância de dados — validação em 3 camadas (todas antes do
reinício):**
1. **Equivalência direta** `saturation × saturation_ref`: **28/28**
   `order` idêntico (n≤6 + tau k=2 + sondas k=3, incl. fecho 2059);
2. **`demo`**: VALIDACAO OK — novas seções de equivalência **17/17** +
   propriedade `minref_deep` 17/17 intacta;
3. **Dados gravados**: **9/9 `fecho`** do CSV do experimento reproduzidos
   + **1 `minref_deep` completo** (s=1536 k=3, `>7(orcamento…)`) idêntico
   ao registrado.

*Justificativa teórica:* o fecho é ponto fixo de operador monotono
(conteúdo único, independente da ordem) e o resolvente é comutativo
(`res(c1,c2|l) = res(c2,c1|-l)`) → buckets cobrem os mesmos resolventes;
`order` final é sort determinístico sobre o mesmo conteúdo → lista
idêntica. A proveniência `(p1,p2)` muda de ordem de registro, mas os
dois chamadores a descartam (`order, _ = sat`). Nenhuma hipótese, regra,
grade ou orçamento foi alterado — C1 intacto.

**Reinício:** `Stop-Process` no PID antigo → o loop de retry retomou em
5s (**tentativa 2**, PID 9880, 06:29) com `--resume`: **267 linhas do
checkpoint preservadas**, selftests S1–S5+DISJ re-executados OK,
k=2/k=3 marcados completos, k=4 coletando de s=1539 (129 restantes).

## 3. Resultados *(pós-execução — run concluído 26/11/2026, exit 0)*

**Execução:** 396/396 instâncias (132+132+132), `mode=resume+collect+analyze`,
runtime da tentativa final 37 095s · selftests **todos OK** no run (S1 BCa
0,013 · S2 métricas · S3 tipo-I 3/40=0,075 + poder 10/10 · S5 smoke ·
DISJ ∅ r2..r6) · **ASSERT 0 violações** · 0 descartes · UNSAT 132/132 em
cada nível · **0 crash CaDiCaL** (2 reinícios externos de servidor —
checkpoint atômico preservou tudo; nota do patch da `saturation` na §2.1;
s=1655 levou 459min por degradação de estado do processo — `fecho=9061`
**idêntico** à sonda fresca, dado íntegro). Artefatos:
`gk_tau_kup_series.csv` (sha256 `f5d51c570455bb43…`) + `gk_tau_kup.json`
(pare protegido pelo R6 do lint).

**§3.0 Correção de anotação do pré-registro (transparência):** o §1.2 do
commit `eb43a9b` diz "**32/nível, 96 total**" e a H_t1 diz "**16/32**" —
**errado como aritmética**: a grade vinculante é `seeds 1536..1667` =
**132/nível, 396 total** (o *range* de seeds está correto e é o que
define a grade; o código usou 132 e o JSON registra `n_grid_k3=132`).
**O veredito é robusto às duas leituras:** 118 ≥ 66 (50% de 132) **e**
≥16. Nada foi alterado pós-dado — esta nota é um erratum de contagem.

### 3.1 H_t1 — VIABILIDADE: **CONFIRMADA**

**118/132 exatos (89,4%)** em k=3 com `max_aux=6M` (gate: ≥50% = ≥66;
também ≥16 da anotação). Distribuição dos exatos: minref **5→28, 7→84,
9→1, 11→5**; censuras 14. *Leitura:* a fronteira da sonda se confirma —
a maioria das instâncias k=3 tem minref ≤7 e é capturada **exatamente**;
os valores 9/11 aparecem porque o teto `t_cap = max_aux/pares` é
por-instância (pares menores liberam t maior).

### 3.2 H_t2 — DINAMICA (crescimento com k): **REFUTADA** (0/2)

Regra pré-registrada (0/2 OK → REFUTADA; nenhum CONTRADITA — todos os
CIs cruzam 0). Percentil primário + BCa + Bonferroni 0,05/2 + regra de
2 níveis (z0 ≈ 0, saudável):

| Contraste | n | ponto | percentil 95% | BCa | bonf2 (0,0125/0,9875) | SE | MDE80 | veredito |
|---|---|---|---|---|---|---|---|---|
| k3 − k2 | 118/132 | **−0,243** | [−0,606, +0,135] | [−0,615, +0,128] | [−0,649, +0,180] | 0,189 | 0,531 | INCONCLUSIVO → **FALHA_INCONCLUSIVO** |
| k4 − k3 | 55/118 | **+0,106** | [−0,323, +0,526] | [−0,320, +0,533] | [−0,390, +0,569] | 0,211 | 0,592 | INCONCLUSIVO → **FALHA_INCONCLUSIVO** |

### 3.3 ASSERT (teorema): **OK — 0 violações em 396**

`minref_exato ≥ d(∅)` em todas as instâncias (coleta e re-análise).

### 3.4 Tabela por nível (dado central da "dinâmica τ")

| k | nvars | exatos | censuras | % exato | mean_minref (exatos) | min–max | mean_drat (mesmos pontos) | lacuna drat−minref |
|---|---|---|---|---|---|---|---|---|
| 2 | 5 | 132 | 0 | 100% | **6,955** | 5–11 | 8,742 | 1,79 |
| 3 | 7 | 118 | 14 | 89,4% | **6,712** | 5–11 | 10,178 | 3,47 |
| 4 | 9 | 55 | 77 | 41,7% | **6,818** | 5–11 | 11,309 | 4,49 |

Série ordinal exata: n=305, estratos [132, 118, 55], censuras totais 91.

### 3.5 Métricas descritivas (CI percentil estratificado, B=1000 — sem hipótese)

| série | n | D_H (higuchi) | boxdim | saltos | hurst_rs |
|---|---|---|---|---|---|
| minref | 305 | 2,028 [1,955; 2,041] | 0,812 [0,785; 0,825] | 0,804 [0,756; 0,872] | 0,542 [0,500; 0,678] |
| drat | 305 | 1,971 [1,959; 2,032] | 0,937 [0,895; 0,945] | 0,734 [0,652; 0,745] | 0,642 [0,511; 0,698] |

## 4. Interpretação *(pós-execução)*

1. **A extensão n>6 funciona (P):** H_t1 confirma que `minref_deep`
   torna n=7 **viável e exato em 89,4%** das instâncias — a pendência
   original do D4′ (τ k↑ bloqueado em n≤6) está **resolvida** dentro do
   orçamento declarado;
2. **H_t2 refutada — resultado negativo honesto:** o comprimento mínimo
   **não cresce com k** nesta família (médias planas 6,95/6,71/6,82;
   mesmo intervalo 5–11 nos três níveis). A leitura estatística é
   "sem suporte + poder limitado" (os contrastes são INCONCLUSIVOS;
   MDE 0,53/0,59 → crescimento < ~0,5 linhas seria indetectável) — a
   palavra "REFUTADA" é **mecânica da regra pré-registrada** (0/2 OK),
   não prova de efeito nulo; registrar ambas as leituras é obrigatório;
3. **O dinamismo está no DRAT, não no mínimo (P, descritivo):** a lacuna
   `drat − minref` cresce **1,79 → 3,47 → 4,49** com k — as provas dos
   solvers crescem enquanto o mínimo fica estável. Candidata natural a
   hipótese **(C)** pré-registrada em rodada futura;
4. **Parede de exatidão medida:** % exato cai 100% → 89% → 42%
   (censuras 0/11/58%) — o custo do exato em n=9 é quantificado e a
   fronteira empírica da §1.1 se confirma com dado novo (k≥5 segue
   parede declarada);
5. **Caveat pré-declarado em ação:** a média k=4 é **condicional aos55
   exatos** (enviesada para baixo — censuras removem minref altos); mas
   k3−k2, com censura mínima (0% vs 11%), também é levemente negativo —
   o padrão plano **não é só artefato de censura** (é fraque, porém:
   MDE ~0,5).

## 5. Limitações *(pós-execução)*

- **Censura diferencial** (0/10,6/58,3%): médias de minref são
  condicionais à exatidão — em k=4, 58% dos valores verdadeiros não
  são observados (só limites inferiores `>3/>4/>5`);
- **Poder:** MDE80 = 0,53 (k3−k2) e 0,59 (k4−k3) — "REFUTADA" não
  exclui crescimento pequeno; excluiria efeito ≥ ~0,5 com 80% de poder;
- **Família única** (`tau_tiny`, depth=1, w=k+1, seeds 1536..1667):
  generalização desconhecida; k≥5 = parede do fecho (não testado);
- **Métricas descritivas** (sem hipótese); boxdim cross-n confundido
  (licença do r4);
- **max_aux por nível** (400k/6M/8M) é dirigido pela fronteira — não
  altera valores exatos, mas é o canal da censura diferencial;
- **Anotação do pré-registro corrigida** (§3.0: "96 total"/"16/32" →
  396/132; veredito robusto às duas leituras);
- **Execução:** 2 reinícios de servidor (checkpoint preservou 100%),
  patch de desempenho da `saturation` mid-run com invariância provada
  (§2.1), s=1655 com 459min (estado do processo — dado íntegro),
  wall-clock **não** é orçamentado (só auxs) — viabilidade de n=9
  exato custou dias de CPU.

## 6. Próximos passos *(pós-execução)*

1. **Séries em b** — próxima da linha (`ONDE_ESTAMOS`: índice lex da
   série ordinal original do D4′);
2. **Candidata (C) pré-registrável:** `lacuna drat − minref` cresce com
   k (1,79/3,47/4,49) — testar com a máquina de contrastes em rodada
   futura (seleção de métrica = pós-hoc aqui, portanto **não** é claim);
3. k≥5 mantido como **parede declarada** (não testar sem nova
   engenharia de fecho);
4. Opcional: **teto de wall-clock pré-registrado** para n≥9 (a s=1655
   mostra que tempo não é limitado pelo orçamento de auxs);
5. Sincronizar `IA-Research-GK-MinRef` (`minref_deep` + `saturation`
   buckets + `saturation_ref`) e o 2º clone.

---

**Referências:** `28_`–`33_` (linha D4′ + referees) · `gk_minref.py`
(`minref_deep`, `tree_depths` — nova extensão n>6) · `gk_tau_kup.py`
(pré-registro executável) · sondas `probe*_tau*.py` (fronteira) ·
Efron (1993) BCa · Lakens (2017) TOST (não usado aqui — sem eq)

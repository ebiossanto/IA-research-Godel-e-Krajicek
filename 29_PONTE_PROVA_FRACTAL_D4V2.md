# 29 — Ponte Prova → Fractal (D4′ v2 + r2): comprimentos MÍNIMOS canônicos (minref), controle do regime, BCa/TOST

**Data:** 20/11/2026 (v2 + rodada r2) · **Classificação:** **(P)** experimento
próprio + **(C)** hipóteses testadas a priori · **Nível Ten-Proofs:** N1
(script, seed determinística) + N2 (bootstrap nesta máquina). **Não** é lower
bound, **Não** é claim de EF. **Rodadas:** r1 (§1–7) + **r2 BCa/TOST (§8)** —
referee completo em `29_..._referee.md` (r1 e r2, RECOMENDADO).

**Reproduzir:**
```powershell
python -u gk_proof_fractal_v2.py        # v2 (coleta + metricas)
# → gk_proof_fractal_v2_series.csv + gk_proof_fractal_v2.json
# seed=20261119 · B=300 · bloco=8 · 192 instâncias · runtime ~1000–1150s
# CSV sem colunas de tempo (reprodução byte-a-byte entre execuções)
python -u gk_proof_fractal_v2_r2.py     # r2 (BCa + TOST + MDE80)
# → gk_proof_fractal_v2_r2.json + gk_proof_fractal_v2_r2_contrasts.csv
# re-análise do CSV congelado · seed_r2=20261122 · B=1000 · ~40s
```

---

## 1. Pergunta e relação com o 28_ (v1)

O v1 (`28_PONTE_PROVA_FRACTAL_D4.md`) mostrou que métricas fractais (D_H de
Higuchi) **separam** a família `php` (crescimento exponencial de provas DRAT)
das demais — e o referee reinterpreteu isso como *separação de regime de
crescimento*, **não** de dureza (§A1), listando como pendência de r2 (i)
normalização anti-quantização (A2), (ii) teste primário registrado a priori
(A4).

O v2 ataca as duas pendências **e** troca a fonte do comprimento:

| | v1 (28_) | **v2 (este)** |
|---|---|---|
| Comprimento | linhas da prova **DRAT do solver** (artefato do Cadical) | **minref = comprimento mínimo exato** (canônico, `gk_minref`) + DRAT como controle na mesma instância |
| Regime | php exponencial (48 → 935.504) vs quase-linear | **controlado**: escopo n≤6 do minref elimina toda curva exponencial |
| Anti-quantização (A2) | só log1p | log1p + **`relinc`** = incrementos de `log1p` |
| Prioridade (A4) | 4 de 18 marcados a priori | **12 contrastes confirmatórios declarados no código** (D_H, raw+relinc) |
| Famílias | implication, php, tau (k=8) | implication (m=3–6), cadeia+ruído (k=3–6), **tau_tiny** (k=2, w=3, d=1) — todas n≤6 |

**Hipóteses (registradas a priori no script):**

- **H_C3 (controle de regime):** se D_H media *regime de crescimento* (leitura
  A1 do referee) e não identidade de família, então **controlado o regime**
  (sem php exponencial) os pares de famílias **não separam** (IC95 de D_H
  inclui 0, raw e relinc). **REFUTADA** se algum par excluir 0.
- **H_C4 (invariância de fonte):** os contrastes **pareados**
  `D_H(minref) − D_H(drat)` por família incluem 0 → a métrica não é artefato
  do solver. **REFUTADA** se algum excluir 0.

## 2. Método

### 2.1 Famílias (64 pontos cada; 192/192 UNSAT verificados por solver; 0 censuras minref)

| Família | Construção | Grade | minref (faixa) | DRAT médio |
|---|---|---|---|---|
| `implication` | grafo de implicações semeado `[-a,b]` + unidades `[s]`,`[-t]` | m=3..6 ×16 seeds | 5–9 | 5,0 |
| `cadeia` | cadeia unitária `[1],[−1,2]…[−k]` + **ruído binário semeado** (0–6 cláusulas; superset de UNSAT) | k=3..6 ×16 seeds | 5–13 | 11,8 |
| `tau_tiny` | **τ(g)ᵦ de Krajíček** reduzida: k=2 entradas, w=3 saídas, prof.1 (5 vars) — b∉imagem | 64 seeds | 5–11 | 8,3 |

> O ruído binário da `cadeia` é necessário: sem ele `minref=2k+1` seria
> constante por k e a série não teria variação. O ruído ternário foi
> **descartado na sonda** (fecho explodia para 665 → censura `>2`, 8–10s/inst).

### 2.2 Sistemas e variantes

- **`minref`** — comprimento mínimo exato via `REF_t` (fecho + pares
  completos + busca binária; escopo n≤6). É a fonte **canônica**: não
  depende de solver, de ordem de entrada nem de heurística.
- **`drat`** — linhas da prova DRAT real (Cadical195) da **mesma instância**
  (pareamento ponto a ponto; se DRAT falhar, o ponto sai das duas séries).
- **Variantes:** `raw`, `log1p`, **`relinc`** = Δ de `log1p(x)` — remove
  nível, escala e tendência (a mitigação A2). Validação sintética da
  variante: ruído→D_H 2,120 · passeio→2,028 · seno→1,218 (mesma ordem do
  raw; o seno permanece o mais baixo ✓).

### 2.3 Métricas e inferência

Mesma implementação validada do v1 (import direto de `gk_proof_fractal`):
Hurst R/S, Higuchi D_H (k≤8), box-counting. Bootstrap em blocos B=300,
bloco=8, seed fixa. **H_C4 usa resample pareado** (mesmos índices nas duas
fontes); **H_C3 usa independente** (famílias distintas). 12 contrastes
confirmatórios (D_H × {raw, relinc} × 6) + 81 exploratórios.

**Nota de múltiplas comparações (A4):** régua Bonferroni α* = 0,05/12 ≈
0,0042 declarada; com B=300 o percentil resolvível mais extremo é [1,298] —
reporta-se IC95 + contagem, na mesma régua honesta do 28_ §3.3.

## 3. Resultados

### 3.1 Séries (n=64 por célula)

| Família \| sistema | média | faixa | H_RS | **D_H** | D_box | D_H(relinc) |
|---|---|---|---|---|---|---|
| implication \| **minref** | 6,0 | 5–9 | 0,528 | **1,980** | 0,772 | 2,069 |
| implication \| drat | 5,0 | 3–7 | 0,378 | **1,998** | 0,758 | 2,106 |
| cadeia \| **minref** | 7,5 | 5–13 | 0,661 | **1,965** | 0,776 | 2,078 |
| cadeia \| drat | 11,8 | 6–18 | 0,556 | **1,954** | 0,860 | 2,095 |
| tau_tiny \| **minref** | 7,3 | 5–11 | 0,491 | **2,019** | 0,718 | 2,089 |
| tau_tiny \| drat | 8,3 | 3–15 | 0,654 | **1,979** | 0,830 | 2,069 |

Observação imediata: **minref é sistematicamente menor que DRAT** (ex.:
cadeia 7,5 vs 11,8 — o solver não achava provas mínimas), mas as *métricas*
das séries ficam na mesma faixa.

### 3.2 H_C3 — contraste entre famílias (minref, D_H): **6/6 incluem 0**

| Par | raw | relinc |
|---|---|---|
| implication − cadeia | +0,015 [−0,118; +0,211] inclui 0 | −0,009 [−0,109; +0,090] inclui 0 |
| implication − tau_tiny | −0,039 [−0,231; +0,112] inclui 0 | −0,020 [−0,111; +0,080] inclui 0 |
| cadeia − tau_tiny | −0,054 [−0,307; +0,030] inclui 0 | −0,011 [−0,090; +0,060] inclui 0 |

→ **H_C3: CONFIRMADA.** Controlado o regime (nenhuma família exponencial),
**nenhum par separa** — inclusive a variante anti-quantização `relinc`.
Isso sustenta a leitura A1 do referee: no v1, o que D_H separava era o
**regime de crescimento** (curva exponencial do php), não a identidade da
família.

### 3.3 H_C4 — fonte minref vs DRAT (pareado, D_H): 1 exclusão **incoerente**

| Família | raw | relinc |
|---|---|---|
| implication | −0,019 **[+0,011; +0,385] EXCLUI 0** ⚠ | −0,037 [−0,132; +0,072] inclui 0 |
| cadeia | +0,011 [−0,102; +0,224] inclui 0 | −0,017 [−0,078; +0,066] inclui 0 |
| tau_tiny | +0,040 [−0,063; +0,126] inclui 0 | +0,020 [−0,052; +0,074] inclui 0 |

**Veredito pela régua a priori: H_C4 REFUTADA (NOMINAL)** — 1/6 excluiu 0.
**Porém** o teste excluente é **estatisticamente incoerente**: o delta
pontual (−0,019) está **fora do próprio IC95** `[+0,011; +0,385]`.

**Diagnóstico (executado):** na reamostragem, D_H(minref) ≥ 1,99 em **35%**
dos blocos vs 2% para DRAT — o Higuchi **satura no teto D_H≈2** com séries
de inteiros pequenos e a distribuição bootstrap fica deslocada (mediana
+0,174 vs ponto −0,019). O IC percentil não está centrado na estimativa →
a "exclusão" é **artefato do IC**, não de efeito. A flag
`point_outside_ci` marca os **9 contrastes** (de 93) afetados; nenhum
sobrevive à variante `relinc`. **Leitura sustentada: invariância de fonte
mantida, com ressalva declarada.**

### 3.4 Exploratórios (81 contrastes): 8 excluem 0

8/81 ≈ o esperado por chance (α=0,05 → ~4; com correlação entre testes, a
ordem de grandeza é compatível). Sem padrão de sinal consistente (5 em
`boxdim`, 3 em D_H/H, mistura de direções) → **sem evidência exploratória
que justifique promover teste algum.**

## 4. Interpretação

1. **A1 confirmada como controle:** a separação do v1 era do **regime**
   (exponencial vs quase-linear). Retirada a curva exponencial (escopo n≤6),
   **nada separa** — a métrica é sensível à *forma da curva de crescimento*
   da complexidade de prova ao longo do índice ordinal, não à família.
2. **A2 endereçada:** `relinc` (incrementos de log1p) não muda nenhum
   veredito — a anti-quantização **não é o que sustenta** (nem destrói) os
   resultados; mas a **saturação no teto** (§3.3) revela que, em n≤6, D_H
   opera sem dinâmica útil (todas as séries ∈ [1,95; 2,13], perto do nível
   de ruído branco 2,075). **Limitação nova e declarada.**
3. **Comprimento mínimo ≠ comprimento de solver:** minref é menor que DRAT
   em todas as famílias (o Cadical não produz provas mínimas), mas as
   métricas não distinguem as fontes → a "ponte prova→fractal" **não é
   artefato do solver** (com a ressalva da flag de incoerência).
4. **Resultado negativo é resultado:** o v2 **não** reproduz a separação do
   v1 — e é justamente isso que a torna interpretabilizada: separação =
   regime.

## 5. Bugs encontrados e corrigidos nesta rodada (7º e 8º do projeto)

1. **7º bug — `gen_tau` com unidades de saída invertidas** (codificava
   `saída = ¬b`): 10/24 seeds davam SAT na sonda. **Impacto no v1: nenhum
   na validade** (CSV congelado com 188/188 UNSAT verificado por solver —
   as instâncias eram τ com testemunha ¬b). Corrigido para `saída = b`.
2. **8º bug — "seed fixa" não reproduzia entre processos:** os geradores
   usavam `tuple.__hash__()` (randomizado por PYTHONHASHSEED) — verificado:
   3 processos → 3 hashes. Artefatos v1 congelados permanecem válidos
   (gerados num processo único, sha registrado), mas a regeneração exata
   era impossível. Corrigido com `_det_seed()` = CRC32 (verificado
   determinístico entre processos). **Errata adicionada ao 28_ §5.**
3. **Wall-clock no CSV:** a coluna `seconds` (run1/run2) quebrava a
   reprodução byte-a-byte; removida do artefato (só console). **Confirmado:**
   a previsão `b8aecc2d…` (run2 sem a coluna) **bateu** com o sha do run3
   (`b8aecc2dd6cc7b33…`) — determinismo byte-a-byte entre execuções
   demonstrado (run1 vs run2: idênticos em métricas/deltas/ICs; run3:
   idêntico em CSV inteiro). Ver referee §A6.

Referee completo: `29_PONTE_PROVA_FRACTAL_D4V2_referee.md`.

## 6. Limitações

1. **n≤6 (escopo do minref):** sem família exponencial possível → o v2
   **controla** o regime, não o **testa** em escala; a separação do v1 em
   php permanece um achado do v1, não replicável aqui por construção.
2. **Saturação do Higuchi no teto** (§3.3): em séries curtas e quantizadas,
   D_H ≈ 2 para tudo → poder discriminativo limitado; ICs largos. Um
   resultado "não separa" em n≤6 **não** equivale a equivalência demostrada
   (faltaria teste de equivalência com margin declarado).
3. **τ reduzida** (k=2, w=3) — a pendência "τ maior (k↑)" do referee do 28_
   continua **aberta** (k↑ exige n>6, fora do escopo minref).
4. Bootstrap percentil **não confiável perto do teto** (9/93 contrastes com
   ponto fora do IC); recomendação para r2: BCa/studentizado ou margem de
   equivalência.
5. N1+N2 (sem N4 — nada formalizado em Lean); H_C2 (Res vs EF) permanece
   **DEFERIDO**.

## 7. Próximos passos

1. ~~**r2 do v2:** inferência robusta perto do teto (BCa) + teste de
   equivalência com margin~~ → **EXECUTADO — §8** (com achados próprios:
   BCa não resolve a saturação; pendências atualizadas para r3 abaixo).
2. Pendência do 28_ mantida: **τ com k↑** — exige estender o escopo do
   minref (n>6, fecho ≤3ⁿ inviável) ou método alternativo de comprimento
   mínimo (ex.: SAT-based sem fecho completo).
3. Séries em b (índice lex) com minref — a "série ordinal" original do D4′.
4. **Novo (r2):** estatística anti-saturação (rank-based/contagem de
   saltos) ou n↑; delete-d block jackknife; **boxdim pré-registrado**
   como métrica primária; margens ancoradas em efeito prévio documentado
   antes de qualquer série nova (referee r2 §C–D).

## 8. Rodada r2 (20/11/2026): BCa + TOST + MDE80

**Reproduzir:**
```powershell
python -u gk_proof_fractal_v2_r2.py
# → gk_proof_fractal_v2_r2.json + gk_proof_fractal_v2_r2_contrasts.csv
# re-analise do CSV CONGELADO b8aecc2d… (nao regenera instancias)
# seed_r2=20261122 · B=1000 · runtime ~40s
```

**Pendências r1 atacadas:** (i) TOST com margem · (ii) BCa + poder ·
(iii) regra de incoerência declarada · (iv) pista boxdim. Referee da
rodada: `29_..._referee.md` §C–D (RECOMENDADO com correções — incluindo
duas afirmações de robustez que a própria checagem **refutou** e foram
corrigidas no texto).

### 8.1 Método (reguas declaradas antes de rodar)

- **BCa** (Efron): correção de viés `z0` + aceleração `a` (jackknife
  delete-1; pareado nos contrastes de fonte, pooled em duas amostras).
  **Selftest:** implementação confrontada com `scipy.stats.bootstrap
  (method='BCa')` em caso iid → **OK, diff máximo 0,013** (scipy 1.18.1).
- **TOST:** `EQUIVALENTE` ⟺ **IC90 BCa** ⊂ (−Δ, +Δ) (α=0,05 bicaudal).
  **Margens:** Δ=**0,10 primária** (âncora independente: ~1/7 do efeito
  v1 imp−php=0,731) + **0,15/0,20 sensibilidade** — tabela reportada
  inteira, nenhuma margem promovida (referee C1: escolhidas após ver o
  r1; mitigado, não eliminado).
- **MDE80** = 2,8016 × SE_boot (poder 80%, α=0,05) — métrica de
  planejamento, não decide veredito (referee C4).
- **Regra de incoerência (iii):** estimativa fora do IC (percentil ou
  BCa) ⇒ teste `INCOERENTE` — **não conta como refutação nem como
  confirmação**, aplicada automaticamente em `classify()`.
- **Tripla régua por contraste:** `SEPARA` (IC95 BCa exclui 0) ·
  `EQUIVALENTE` (TOST na margem primária) · `INCONCLUSIVO` ·
  `INCOERENTE`.

### 8.2 H_C3 (famílias, minref, D_H) — 0 separações; equivalência depende da margem

| Par | raw BC95 | relinc BC95 | veredito |
|---|---|---|---|
| implication−cadeia | +0,015 [−0,222; +0,165] | −0,009 [−0,121; +0,076] | INC / INC |
| implication−tau_tiny | −0,039 [−0,180; +0,134] | −0,020 [−0,126; +0,065] | INC / INC |
| cadeia−tau_tiny | −0,054 [−0,150; +0,118] | −0,011 [−0,087; +0,068] | INC / **EQUIV** |

**Tally: 0 SEPARA · 1 EQUIVALENTE · 5 INCONCLUSIVO · 0 INCOERENTE.**

**Tabela de sensibilidade (contagem de equivalentes):**

| Margem Δ | 0,08 | **0,10** | 0,12 | 0,15 | 0,18 | 0,20 |
|---|---|---|---|---|---|---|
| H_C3 (6 testes) | 1 | **1** | 3 | 4 | 5 | **6** |
| H_C4 (6 testes) | 0 | **2** | 2 | 3 | 6 | **6** |

→ **Resposta quantitativa à pendência A1:** nenhuma separação detectada
(0/6); **equivalência demonstrada em ±0,20 (6/6)** e ±0,15 (4/6);
**±0,10 inacessível com n=64** (MDE80≈0,19 > 0,10). A leitura corrigida
do r1 (referee C6): "não separam" era ausência de evidência — agora
**há limite quantitativo**: qualquer efeito real de D_H entre essas
famílias é < 0,20 (com a ressalva da saturação §8.5).

### 8.3 H_C4 (fonte pareada) — a exclusão do r1 virou INCOERENTE

| Família | raw BC95 | relinc BC95 | veredito |
|---|---|---|---|
| implication | −0,019 [−0,156; −0,032] ⚠ | −0,037 [−0,172; +0,032] | **INCOERENTE** / INC |
| cadeia | +0,011 [−0,200; +0,105] | −0,017 [−0,095; +0,039] | INC / **EQUIV** |
| tau_tiny | +0,040 [−0,054; +0,140] | +0,020 [−0,031; +0,095] | INC / **EQUIV** |

**Tally: 0 SEPARA · 2 EQUIVALENTE · 3 INCONCLUSIVO · 1 INCOERENTE.**

A exclusão nominal do r1 (`implication` raw) **persiste como exclusão
sob BCa** (`IC95=[−0,156;−0,032]` não contém 0) — **mas o ponto estimado
(−0,019) está fora do IC nos DOIS métodos** → pela regra declarada (iii)
o teste é `INCOERENTE` e **não conta**. Sob as duas margens folgadas o
par é equivalente. **Leitura: invariância de fonte mantida** (0
separações coerentes), com a exclusão r1 explicitamente registrada como
artefato estatístico, não como efeito.

### 8.4 Poder (MDE80) — por que ±0,10 é inacessível

| Grupo | MDE80 médio | faixa |
|---|---|---|
| H_C3 confirmatórios | **0,190** | 0,110–0,272 |
| H_C4 confirmatórios | **0,161** | 0,092–0,281 |
| por variante (todos) | raw **0,232** / relinc **0,120** | — |

A variante `relinc` **dobra o poder** (MDE 0,12 vs 0,23) — a
anti-quantização A2 não muda vereditos mas torna a série mais detectável.
Com MDE≈0,19 na métrica primária, a margem 0,10 está **abaixo do que a
amostra pode certificar** — exatamente o padrão da tabela 8.2.

### 8.5 Achado principal do r2: BCa NÃO resolveu a saturação

**8/81 contrastes continuam com estimativa fora do IC — percentil E BCa**
(mesmos 8 do r1); **2 ICs BCa degenerados** (`lo==hi`, Hurst em
`drat:implication−tau_tiny`). O BCa corrige viés/assimetria da
distribuição bootstrap, mas a patologia aqui é da **estatística**
(Higuchi/Hurst saturando no teto D_H≈2 sob reamostragem de séries
quantizadas) — nenhuma correção de IC conserta estatística colapsada.
Consequências: a **regra de incoerência (iii) é o remédio vigente** (8
testes excluídos dos dois lados); r3 precisa de estatística
anti-saturação (rank/saltos) ou n↑ (referee C2).

### 8.6 Pista boxdim (A4) — sobrevive em 2/3

`drat:implication−cadeia:boxdim`: raw **SEPARA** [−0,201; −0,006] ·
log1p **SEPARA** [−0,213; −0,016] · relinc INC [−0,204; +0,026] — sob
BCa coerente (ponto dentro). **Exploratório, não promovido** (C5): entre
os 69 exploratórios, **18 SEPARA coerentes** (12 boxdim + 6 Hurst) —
acima do nominal, mas séries correlacionadas inflam a contagem; nenhum
toca os confirmatórios (0/12). **Boxdim como métrica primária
pré-registrada é a maior aposta de r3.**

### 8.7 Resultado consolidado (81 contrastes)

`INCONCLUSIVO: 45 · SEPARA: 18 (todos exploratórios) · EQUIVALENTE: 10 ·
INCOERENTE: 8` — autocontidos no CSV (`ce26b53a…`), input congelado
`b8aecc2d…` registrado no JSON.

---

**Referências:** `28_PONTE_PROVA_FRACTAL_D4.md` + referee (§A1, A2, A4, A9–A11) ·
`gk_proof_fractal_v2.py` (hipóteses a priori) · `gk_proof_fractal_v2_r2.py`
(r2: BCa/TOST/MDE80 + selftest scipy) · `gk_minref.py` ·
`ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md` §5-D4 ·
`ferramentas/gk_proof_fractal.md` · `FERRAMENTAS.md` ·
Efron, B. (1987). *Bootstrap methods: another look at the jackknife.* Ann. Statist. ·
Schervish, M. (1996). *Theory of Statistics* (BCa) ·
Lakens, D. (2017). *Equivalence tests: A practical primer…* Soc. Psych. (TOST)

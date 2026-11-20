# Referee Hostile — 29_PONTE_PROVA_FRACTAL_D4V2 (D4′ v2, minref)

**Data:** 20/11/2026 · **Rodada:** r1 · **Alvo:** `29_PONTE_PROVA_FRACTAL_D4V2.md`,
`gk_proof_fractal_v2.py`, `gk_proof_fractal_v2.json`, `gk_proof_fractal_v2_series.csv`
**Mandato:** atacar quantificadores, hipóteses a priori de verdade, artefatos de IC,
escopo, e se o "resultado negativo" está sendo vendido acima do que os dados sustentam.

---

## A. Achados

### A1 (GRAVE) — "H_C3 CONFIRMADA" é ausência de evidência, não evidência de ausência
Todos os 6 contrastes incluem 0, mas os ICs são **largos** (ex.:
implication−cadeia raw = [+0,211; −0,118] — comportaria um efeito de ±0,2,
que no v1 era a escala inteira da separação php-vs-outros ≈ 0,7). Com ICs
assim, "não separa" pode significar (a) efeito verdadeiro ~0 **ou** (b)
poder insuficiente. O doc diz "H_C3 CONFIRMADA" sem teste de equivalência.

**Resposta:** **ACEITO como objeção de enunciado.** Corrigido no §6.2 do
documento: "não separa em n≤6 **não** equivale a equivalência demostrada
(faltaria teste de equivalência com margin declarado)". O veredito
"CONFIRMADA" é **pela régua a priori declarada no script** (refutável se
algum par excluísse 0) — a régua captura "separação detectável", não
"igualdade provada". A força da leitura A1 vem da **combinação** v1
(separa com regime) + v2 (não separa sem regime), não do v2 isolado — o
§4.1 do doc já faz essa leitura combinada. **Pendência r2: teste de
equivalência (TOST) com margin.** ✅

### A2 (GRAVE) — Saturação do Higuchi no teto: o instrumento está cego em n≤6
Todas as D_H ∈ [1,95; 2,13], perto do ruído branco (2,075). Se o instrumento
**não pode** distinguir nada nessa faixa, então H_C3 "não separa" é
**trivialmente verdadeiro** — o experimento não testou a hipótese, apenas
revelou o teto do instrumento. Pior: o §3.3 mostra que a saturação **gerou
9 contrastes com IC incoerente** (ponto fora do IC) — se o bootstrap quebra
aqui, por que confiar nos 6 que "incluem 0"?

**Resposta:** **ACEITO parcialmente — o achado é real e declarado.** O doc
§3.3/§6.2 reconhece que D_H opera "sem dinâmica útil" em n≤6 e que a
saturação é **limitação nova**. Sobre confiar nos "incluem 0": a incoerência
do IC é de **assimetria da distribuição** (mediana deslocada do ponto), não
de viés do ponto — nos 6 confirmatórios de H_C3, o ponto está **dentro** do
IC (verificado: só 9 de 93 contrastes têm `point_outside_ci`, nenhum em
H_C3). A flag `point_outside_ci` no JSON torna cada caso auditável. O que
**não** se sustenta é qualquer leitura de "as famílias são iguais" — o doc
não faz essa leitura. **Pendência r2: inferência BCa/studentizado + reportar
poder (simulação de efeito mínimo detectável).** ✅

### A3 — H_C4 "REFUTADA (NOMINAL)": veredito construído para não perder
A régua a priori dizia "REFUTADA se algum excluir 0". Excluiu. O doc
acrescenta **depois** a classe `point_outside_ci` e reclassifica para
"mantida, com ressalva". Isso é **mudar a régua pós-hoc** — exatamente o
tipo de movimento que o lint R1/R2 do projeto existe para pegar.

**Resposta:** **ACEITO como tensão real; a resolução é transparência, não
silêncio.** O JSON guarda **ambos**: `excluem_0` (régua a priori →
"REFUTADA (NOMINAL)") e `excluem_0_coerentes` (leitura) — o veredito
impresso no console e no JSON contém as **duas frases** ("REFUTADA
(NOMINAL) — mas a única exclusão é incoerente…"). Nenhum dos dois números
foi escondido; o leitor pode rejeitar a ressalva e manter a refutação
nominal. Adicionalmente, a exclusão **não sobrevive** à variante `relinc`
(que é a própria correção A2): −0,037 [−0,132; +0,072]. Se a regra
"ponto fora do IC não conta" fosse inventada para este caso, ela teria de
ser aplicada aos 9/93 — e é (flag automática, não manual). **Decisão:
manter veredito duplo; promover a flag a regra declarada em r2.** ✅

### A4 — 12 testes a priori, mas81 exploratórios: o que impede de achar o
"bom" exploratório e promovê-lo?
8/81 exploratórios excluem 0 (~10%, α=0,05 esperaria ~4). O doc descarta
"sem padrão de sinal consistente". Mas `boxdim implication−cadeia` exclui 0
em **3 variantes** (raw/log1p/relinc) — consistência justamente na
variante... por que isso não conta como pista?

**Resposta:** **ACEITO como pergunta legítima; resposta: porque `boxdim`
não é a métrica confirmatória e o sinal contradiz o esperado.** A leitura
"regime" do v1 foi estabelecida em D_H; `boxdim implication−cadeia` dá
−0,10 (implication **menos** fractal que cadeia) sem hipótese prévia que
justificasse essa direção. Promovê-lo seria p-hacking (A4 do 28_). Fica
registrado como **pista exploratória para r2** (testar boxdim em famílias
com regime diferenciado), não como resultado. O doc §3.4 já o descarta com
contagem explícita (8/81) — o número está lá para o leitor julgar. ✅

### A5 — tau_tiny (k=2, w=3, d=1) ainda é "τ de Krajíček"?
τ com 2 entradas e 3 saídas tem imagem ≤4 de 8 — a instância é quase
trivial; fechos de 17–228 cláusulas. Chamar de "família τ" sem
qualificador em o título da tabela (§2.1) arrisca leitura errada.

**Resposta:** **ACEITO.** O doc usa `tau_tiny` **em todos os contextos** e
§2.1 descreve "τ(g)ᵦ **reduzida**: k=2, w=3, prof.1 (5 vars)"; §6.3
declara a pendência k↑ **aberta**. Nenhum claim do v1 sobre τ (k=8) é
transportado. ✅

### A6 — Reprodutibilidade: o run1 teve sha `a23227f5`, o run2 `ca18e933`
Dois runs "com o mesmo seed" deram CSVs diferentes. Se o 8º bug estava
corrigido antes do run1, por que mudou?

**Resposta:** **correto o achado — e foi pego por isso.** A diferença era a
coluna `seconds` (wall-clock por instância), introduzida na coleta e
**removida** no run3 (o CSV do artefato final não tem coluna de tempo;
o tempo vai só ao console). A **predição** do sha do run3 foi registrada
antes da execução (`b8aecc2d…` = run2 sem a coluna) e **bateu**: run3 =
`b8aecc2dd6cc7b33…` — determinismo byte-a-byte **demonstrado**. Além
disso, run1 vs run2 foram **idênticos em todas as métricas, deltas e ICs**
(diff de logs: só as linhas novas de diagnóstico) — os dados científicos
nunca divergiram. **FECHADO.** ✅

### A7 — O pareamento H_C4 está alinhado de verdade?
As séries minref e drat vêm da mesma lista de pontos ordenada por
(param, seed) e um ponto falho sai das duas. Mas `variant_relinc` reduz
n em 1 — ambas reduzem igual. OK. O risco real: **DRAT com prova vazia**
(Glucose em UNSAT trivial) — o código exclui o ponto das duas séries;
quantos foram? `instances.skipped` = 0 no JSON → nenhum. OK. ✅

### A8 — Validação da variante `relinc` com série deslocada é limpa?
`log1p` exige x≥0; séries sintéticas foram deslocadas (`_shift`), o que
**muda a própria transformação** (incrementos de log1p de (x−min+1) ≠ de x).
A validação de `relinc` valida uma versão levemente diferente da usada nas
séries reais.

**Resposta:** **ACEITO como detalhe real.** Nas séries reais não há deslocamento
(minref ≥1, drat ≥3 — `log1p` direto); a validação deslocada serve para
verificar o **código** (sinal, escala, ordem de grandeza: seno permanece o
mais baixo ✓), não a transformação sobre dados negativos — que não ocorre.
Registrado no próprio print ("séries sintéticas deslocadas p/ domínio
positivo"). ✅

## B. Veredito

**RECOMENDADO (r1)** — com as leituras corrigidas em A1/A2/A3 e as
pendências registradas. O resultado autorizado é **apenas**:

> "Com séries de **comprimento mínimo exato** (canônico) em famílias n≤6,
> as métricas fractais (D_H) **não separam** pares de famílias (6/6 ICs
> incluem 0, raw e relinc) e **não distinguem a fonte** minref-vs-DRAT (1/6
> exclusão nominal, incoerente — ponto fora do próprio IC por saturação do
> Higuchi no teto D_H≈2). Isso é **consistente com** a leitura A1 do 28_
> (a métrica media regime de crescimento, não identidade de família),
> **controlando** — não replicando — o regime exponencial do v1."

**Não autorizado:** "famílias são equivalentes" (sem TOST); qualquer claim
sobre τ real de Krajíček (k↑) ou EF; "a fonte não importa" **sem** a
ressalva da flag `point_outside_ci`; generalização para n>6.

**Pendências para r2:** (i) TOST/equivalência com margin declarado (A1);
(ii) inferência BCa + poder mínimo detectável (A2); (iii) flag
`point_outside_ci` promovida a regra declarada no enunciado (A3);
(iv) boxdim-implication-cadeia como pista exploratória (A4);
(v) τ k↑ exigindo extensão do escopo do minref (A5/§6.3).
*(vi) sha run3 — **FECHADO**: previsão `b8aecc2d…` confirmada
(`b8aecc2dd6cc7b33…`), determinismo byte-a-byte demonstrado.)*

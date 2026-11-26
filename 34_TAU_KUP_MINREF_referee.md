# Referee Hostile — 34_TAU_KUP_MINREF (τ k↑, minref n>6)

**Rodada:** r1 (26/11/2026) · **Alvo:** `34_TAU_KUP_MINREF.md` §3–6 +
`gk_tau_kup.json` (sha CSV `f5d51c570455bb43…`) · **Postura:** atacar
quantificadores, viés de censura, semântica dos vereditos e a
integridade mid-run. Nada é promovido sem resposta.

## A. Achados

### A1 (GRAVE) — Anotação do pré-registro contradiz a grade executada

O commit `eb43a9b` (§1.2) diz "**32/nível, 96 total**" e H_t1 diz
"**16/32 (50%)**", mas a grade executada é `seeds 1536..1667` =
**132/nível, 396 total**. Pior: o **código** usou gate `n3 >= 16` —
muito mais fraco que o "50% do doc" (≥66). Se o resultado tivesse sido
40/132 (30%), o código diria CONFIRMADA e o doc REFUTADA — veredito
divergente entre fontes.

**Resposta (aceita parcialmente):** o *range* de seeds (vinculante,
duplicado em código e doc) está correto; a contagem "96" é erratum de
aritmética, corrigido transparentemente na §3.0 **antes** de qualquer
promoção. O gate real do resultado (118/132 = 89,4%) satisfaz **ambas**
as leituras (≥66 e ≥16) — o veredito é robusto, mas a *divergência de
gate código×doc* é um defeito de processo: nos scripts futuros o gate
deve ser `≥ 50% de len(grid)`, não literal. **Correção obrigatória
registrada; H_t1 permanece CONFIRMADA.**

### A2 (GRAVE) — "REFUTADA" para contrastes estatisticamente INCONCLUSIVOS

Os dois contrastes de H_t2 têm ICs que **cruzam 0**
(k3−k2: [−0,606, +0,135]; k4−k3: [−0,323, +0,526]) — isto é,
*falha em detectar*, não *evidência de ausência*. A regra
pré-registrada (0/2 OK → REFUTADA) converte "inconclusivo" em
"refutado". Chamá-lo de refutado em texto corrido seria overclaim.

**Resposta (aceita com condição):** a §4.2 já obriga a **dupla
leitura** — "REFUTADA" é o veredito *mecânico* da regra
pré-registrada; a leitura estatística correta é **sem suporte, poder
limitado** (MDE80 0,53/0,59 — crescimento < ~0,5 linhas seria
indetectável). Qualquer promoção no `INDICE.md` deve trazer **as duas
frases**. Nenhuma afirmação de "efeito nulo" é permitida.

### A3 (GRAVE) — Censura diferencial: 58% de k=4 não é ruído, é seleção

Censuras 0/10,6/**58,3%** por nível. A média k=4 (6,818) é calculada
sobre **55 exatos** — subamostra selecionada para minref *baixo*
(quem tem minref alto é censurado antes de aparecer). O contraste
k4−k3 é, portanto, média-enviesada-comparada-com-média-limpa. O
"caveat pré-declarado" não elimina o viés, só o declara.

**Resposta (aceita):** limitação explícita na §5 e §4.5; o **peso
probatório** do H_t2 recai sobre k3−k2 (censura 0% vs 11% — limpo),
que também é levemente negativo → o padrão plano não é *só* artefato.
O JSON registra `censuras_total=91` e a tabela por nível traz exatos e
censuras lado a lado — dado disponível para qualquer re-análise com
limite inferior (ex.: tratar censurados como `>cens` em análise de
sensibilidade futura).

### A4 — Poder pré-calibrado para efeitos grandes, não para este

S3 (pré-run): poder 10/10 com deslocamento **1.0σ**. Aqui o efeito
alvo é ~0,5–1,0 unidades de minref com SE 0,19–0,21 → MDE 0,53/0,59.
A calibração não garante poder para o tamanho de efeito plausível
(mínimo que cresce "devagar"). Isso está declarado (§5), mas enfraquece
qualquer leitura forte de H_t2 nos dois sentidos.

**Resposta (aceita):** registrado; futuras rodadas com alvo de poder
(H_D4-style) devem fixar o MDE alvo **antes** do run.

### A5 — Lacuna `drat − minref` crescendo: é pós-hoc?

1,79 → 3,47 → 4,49 é um padrão **observado depois** do run, sem
hipótese pré-registrada — e a subamostra (mesmos305 exatos) também é
seletiva (drat médio de k=4 só dos55 exatos).

**Resposta (aceita):** marcado como **(P) descritivo** na §4.3 e como
candidata **(C)** "não é claim" na §6.2 — explicitamente *seleção de
métrica = pós-hoc*. Só poderá ser testada em rodada futura com
pré-registro próprio (grade nova, DISJ).

### A6 — Patch mid-run da `saturation`: a integridade do run não é auto-certificável?

O patch (commit `1a5a9be`) rodou **no meio** da coleta. Se a
invariância falhasse, dados de antes e depois seriam incomparáveis.

**Resposta (aceita):** §2.1 documenta as 3 camadas de validação
**anteriores** ao reinício: equivalência direta 28/28 (`order`
byte-idêntico), `demo` 17/17, **9/9 `fecho` +1 `minref_deep` completos
reproduzidos do CSV gravado**. Evidência adicional *a posteriori*: a
s=1655 do processo "doente" gravou `fecho=9061` **idêntico** à sonda
fresca — coerência entre processos/versões. Proveniência `(p1,p2)`
muda de ordem de registro e é descartada pelos chamadores (`order, _`).

### A7 — s=1655 com 459min: estado do processo pode ter corrompido algo?

A instância levou ~57× o tempo da sonda fresca (466s) para o mesmo
trabalho (degradação de heap/GC após horas de CNFs). Suspeita de
resultado alterado.

**Resposta (aceita):** `fecho=9061`, `ncl=18`, `lb=3`, censor
`>5(orcamento(t=6,t_cap=1,pares=4891142))` — coerente com a trajetória
da sonda; CSV **não tem colunas de tempo** (byte-reprodutível por
desenho); o valor é função só de (gamma, max_aux). Sem impacto em
veredito. *Wall-clock não-orçamentado* registrado como limitação (§5)
com candidata de teto pré-registrado (§6.4).

### A8 — `max_aux` desigual (400k/6M/8M) entre níveis: compara justos com injustos?

**Resposta (aceita):** o orçamento só decide **censura** (quem entra
na série), nunca o valor exato (REF_t SAT/UNSAT é absoluto). O viés
indireto é real (A3) e está declarado. Nível sem censura (k=2) usa
400k porque lá é folgado — fronteira medida, não escolhida.

### A9 — Conformidades verificadas (sem achado)

- **Temporalidade C1:** pré-registro `eb43a9b` anterior ao run;
  patch `1a5a9be` com invariância provada (A6); sem mudança de
  hipótese/regra/grade pós-dado;
- **DISJ:** interseção grade × r2..r6 = ∅ (aborta se intersectar) —
  OK no run;
- **ASSERT teórico:** 0/396 violações (coleta + re-análise);
- **Múltiplas comparações:** Bonferroni 0,05/2 no grupo H_t2; H_t1 é
  gate de contagem; métricas sem p-valor;
- **z0:** −0,02/−0,00 (saudável, sem degradação da linha);
- **Selftests no run:** S1 0,013 · S3 tipo-I 0,075/poder 10/10 · S5
  smoke · DISJ — todos OK; **0 crash CaDiCaL**; 2 reinícios externos
  com checkpoint atômico (396 linhas íntegras, última linha válida).

### A10 — Anotação "16/32" sobrevive no JSON (`alvo`)

`H_t1.alvo` no JSON ainda diz "≥16/32 (50%) exatos" com
`n_grid_k3=132` ao lado — o artefato carrega a anotação errônea.

**Resposta (aceita):** o JSON é registro de execução (não se edita
pós-hoc); a correção vive na §3.0 do doc e neste referee. Aceitar a
ambiguidade documentada em vez de reescrever histórico.

## B. Veredito

1. **H_t1 (viabilidade): PROMOVIDA — CONFIRMADA (118/132 = 89,4%)**,
   com o erratum da anotação (A1) acoplado *para sempre* à claim;
2. **H_t2 (crescimento com k): PROMOVIDA COMO NEGATIVO QUALIFICADO** —
   no `INDICE.md` constará **duas frases obrigatórias**: "(i) regra
   pré-registrada: REFUTADA (0/2); (ii) estatisticamente: contrastes
   INCONCLUSIVOS com MDE 0,53/0,59 — não detecta crescimento <
   ~0,5 linhas; censura diferencial 0/11/58% compromete k4−k3, o peso
   recai em k3−k2";
3. **ASSERT: OK (0/396)** — teorema, não hipótese;
4. **Lacuna drat−minref:** apenas **(P) descritivo/candidata (C)** —
   proibido qualquer verbo confirmatório nesta rodada;
5. **Nenhuma promessa de EF, de n≥5 ou de generalização** — parede do
   fecho mantida como declarada.

**R1 aprovado com condições** (as 4 condições acima são de *redação*,
não de reexecução — nenhum dado precisa ser refeito). Só após
incorporar as condições ao `INDICE.md`/catálogos o resultado é promovido.

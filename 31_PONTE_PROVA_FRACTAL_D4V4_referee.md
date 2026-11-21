# Referee Hostile — 31_PONTE_PROVA_FRACTAL_D4V4 (D4′ v4, n=384)

**Data:** 21/11/2026 · **Rodada:** r1 · **Alvo:** `31_PONTE_PROVA_FRACTAL_D4V4.md`,
`gk_proof_fractal_v4.py`, `gk_proof_fractal_v4_series.csv` (`c92f0968…`),
`gk_proof_fractal_v4_contrasts.csv` (`8419f25b…`), JSONs
**Mandato:** atacar o veredito `INDETERMINADO` do primário, a execução
em 3 processos, o 3/3 de saltos, e se o diagnóstico de z0 sustenta as
recomendações de r5.

---

## A. Achados

### A1 (GRAVE) — O primário morreu INDETERMINADO; o pré-registro subestimou a incoerência
H_C1 saiu **2/6 contáveis, 4 incoerentes** — o experimento primário
**não respondeu**. O r3 tinha 1/6 incoerente; a calibração do r4 mostrou
o mecanismo (z0=3,29 no construct com tendência) mas **não previu a
incidência** em dados reais-like (4/6). O pré-registro previu a classe
`INDETERMINADO`, mas prever uma classe ≠ prever sua probabilidade.

**Resposta:** **ACEITO como fracasso de previsão, não de regra.** O que
o r4 entregou é o **mecanismo medido** (D1 94%: z0 = viés/SE; escalada
7%→33% com n; D2 confirmada) — é exatamente o que faltava para *porque*
4/6. A classe `INDETERMINADO` funcionou como projetado (não virou
"REFUTADA" falso, como o r3 teria feito com a regra antiga). A lição
está em §6.1/§6.2: o método de IC deve ser escolhido **antes** da série
de r5, com o bloco escalonado/stationary bootstrap testados em
calibração com taxa de incoerência-alvo (<10%). Registrar: **calibrar
também a INCIDÊNCIA de incoerência em dados sintéticos com macroestrutura
de grade (4 blocos de parâmetro), não só tipo-I/poder.** ✅

### A2 (GRAVE) — (a) virou negativo: o r3 era ruído, e o doc r3 disse "OK"
O teste (a) do r3 era `OK` (BC95 excluía) e virou **−0,024 (sinal
invertido, IC inclui 0)**. Se o r3 (a) era1,4σ com percentil incluindo 0,
por que foi contado como OK na rodada anterior — e quantos outros "OK"
de rodadas passadas são ruído?

**Resposta:** **ACEITO — e o próprio r3 já modulou o claim.** O doc do
r3 §3.1 chamou (a) de "evidência moderada" e apontou que o **percentil
incluía 0**; o r4 é a segunda amostra e ela diz: efeito ≈ 0. A régua
(a priori) contou o que a régua manda contar; a **força do claim** foi
rebaixada em ambas as rodadas. Sobre outros "OK" passados: (e)
fonte:τ é o único boxdim que replicou **3× seguidas** (r2/r3/r4);
(a) morreu na 2ª — a taxa de replicação observada (1/3 para boxdim
par-família, 3/3 para saltos) fica registrada como **base empírica para
dimensionar r5** (n e nº de testes). ✅

### A3 — D4 revertido: a justificativa r3 ("fonte não cancela viés") era errada
Mediana |z0|: família **1,54** > fonte **0,82** — exatamente o oposto
do previsto.

**Resposta:** **ACEITO — expectativa falsificada e registrada como tal**
(§3.3/§4.4), não contornada. A hipótese r3 nasceu de **um** caso
(`fonte:cadeia` r3, z0=−2,17) — amostra n=1 disfarçada de padrão. O
fator dominante no r4 é o **par família×parâmetro** (pares com perfis
de m diferentes têm macro desarmônica sob resample). Lição: expectativas
derivadas de casos únicos não vão para o pré-registro sem série de base. ✅

### A4 — O 3/3 de saltos é sólido ou é a mesma ilusão do (a) do r3?
Três testes, 3/3 `OK_BONF`, mas (a) do r3 também foi "OK" e morreu.

**Resposta:** **verificações executadas a favor da solidez:** (1)
**dois métodos concordam** (BC99 Bonferroni **e** percentil excluem,
pontos dentro do IC — o oposto do (a) r3, cujo percentil nunca excluiu);
(2) **z0 saudável** (0,19/0,96/0,06 — viés ≈ 0, como previsto para
estatística local); (3) **MDE < efeito** (razão ≥1,2; detecções 3,4σ–6σ);
(4) **âncoras r3 → r4 com desvio ≤0,012** em 3/3; (5) `saltos` foi a
única métrica 0/27 no r3 e continua melhor (2/27) aqui. Não é
dupla-cicatrização (âncoras r3, teste r4, dados disjuntos). **Ressalva
honesta:** são 3 testes da mesma família de desenho; a replicação
independente real seria r5 com série nova. ✅

### A5 — (d) e (f): ambos os métodos excluem 0 no sinal certo, mas a regra
bloqueia — a regra não está destruindo evidência real?
Em (d): pct [−0,101; −0,055] **e** BCa [−0,110; −0,108] excluem 0
negativo; só o **ponto** cai fora do BCa → INCOERENTE. Idem (f). Dois
métodos concordando é mais forte do que "ponto fora de um deles".

**Resposta:** **ACEITO como tensão real da regra pré-registrada.** A
regra (desde r2) foi desenhada para o caso em que os métodos
**discordam** (ponto fora = distribuição bootstrap não centrada); ela
não distingue "métodos discordam" de "métodos concordam mas o ponto
está fora". Mudar a regra agora seria pós-hoc — **não mudei**; o doc
reporta (d)(f) como "evidência indicativa, não confirmação". **Pendência
r5 (pré-registrar):** regra em 2 níveis — `INCOERENTE_CONCORDANTE`
(ambos excluem no mesmo sinal, ponto fora → conta com flag) vs
`INCOERENTE_DISCORDANTE` (não conta). Não promovo sem pré-registro. ✅

### A6 — Coleta em 3 processos: por que os dados são confiáveis?
Crash ×2, retomada ×3 — o CSV final mistura tentativas. E se o crash
tivesse corrompido algo?

**Resposta:** (1) fix `3d244ab` é **plumbing** (checkpoint/resume),
commitado **separado** do pré-registro `9fe7165` — diff auditável,
hipóteses/margens/regras/grade intactas; (2) escrita **atômica**
(tmp+replace) — nenhum CSV truncado; (3) **determinismo**: geradores
`_det_seed` (CRC32) + minref/solve determinísticos → a mesma instância
produz o mesmo resultado em qualquer processo — as 1152 linhas são
idênticas ao de uma execução única (autochecagem: DISJ+selftests
reexecutados em **cada** tentativa, todos OK); (4) o artefato canônico
é o CSV final com sha `c92f0968…` registrado no JSON da análise
(`input_series_sha256` bate). Bug do `__del__` (0xC0000005) ficou
documentado como **limitação de plataforma** (Windows/python-sat
1.9.dev24), não do experimento. ✅

### A7 — 39% de discordância pct-vs-BCa: a primariedade BCa (A4) está empíricamente errada?
53/135 discordam; o próprio (a) r3 vs r4 mostra BCa oscilando. A
continuidade (BCa primário desde r2) pode estar custando mais que
ganha.

**Resposta:** **ACEITO — quantificado e levado a r5.** O r4 manteve
BCa primário **por continuidade pré-registrada** (A4) e reportou o
percentil em paralelo (flag `discordancia_pct_bca`, 39%) — nada foi
escondido. A recomendação r5 (§6.1) troca o **método** (bloco
escalonado/stationary/percentil-com-nota), não só o rótulo — com
calibração de **incidência** de incoerência (A1). ✅

### A8 — H_C4 "4/6" não é perto-demais de virar propaganda?
(a) perdeu por 0,0009 — "quase atingido" é close call que vira claim?

**Resposta:** o veredito registrado é **`NAO_ATINGIDO (4/6)`** — sem
"quase" no veredito; §3.4 e §5.2 reportam os dois valores exatos
(0,0609 e 0,0684) e a falha de alvo. A previsão √ foi declarada antes e
sua acurácia (4/6, erros −4%…+40%) é reportada como **incerteza da
previsão**, não suavizada. ✅

## B. Veredito

**RECOMENDADO (r4)** — com A1–A8 incorporados. Resultado autorizado:

> "Com n=384/família (1152 instâncias disjuntas de r2+r3; alvo de poder
> declarado): **H_C2 (`saltos`) CONFIRMADA 3/3 com Bonferroni** —
> âncoras r3 replicadas com desvio ≤0,012, z0 saudável, percentil
> concorda; **H_C1 (boxdim) INDETERMINADO** pelas regras exaustivas
> pré-registradas (2/6 contáveis: fonte:τ OK_BONF; imp−τ efeito ≈0 com
> sinal invertido; 4 incoerentes — em (d)(f) ambos os métodos excluem
> no sinal esperado mas o ponto cai fora do BCa → indiciação, não
> confirmação); **H_C3: mecanismo de z0 medido** (D1 94%, D2
> CONFIRMADA, escalada de incoerência 7%→33% com n → viés de bloco
> fixo não encolhe enquanto SE encolhe — **BCa+bloco fixo inadequado
> para n grande**); D4 revertido (família 1,54 > fonte 0,82 —
> expectativa r3 falsificada); **H_C4 NAO_ATINGIDO (4/6)**;
> delete-d vs delete-1 **0/135** (3ª rodada); discordância pct-vs-BCa
> **39%**."

**Não autorizado:** "H_C1 confirmada/refutada" (é INDETERMINADO);
"padrão-τ boxdim replicado" ((a) morreu); "D4 confirmada" (revertida);
"quase atingido" como sucesso (A8); qualquer claim de que a regra de
incoerência foi ajustada (não foi).

**Pendências para r5:** (i) método de IC decidido antes da série +
**calibração de incidência** de incoerência em dados com grade (A1);
(ii) `saltos` primário pré-registrado (3/3); (iii) regra de
incoerência em 2 níveis (concordante/discordante) pré-registrada (A5);
(iv) expectativas só com série-base (A3); (v) n≈512 ou alvo por família
para MDE (A8/§6.5); (vi) τ k↑ inalterada; (vii) limitação de plataforma
`__del__` documentada (A6).

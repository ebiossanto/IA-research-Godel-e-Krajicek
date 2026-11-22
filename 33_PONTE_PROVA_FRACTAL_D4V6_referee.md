# Referee Hostile — 33_PONTE_PROVA_FRACTAL_D4V6 (D4′ v6, n=512)

**Data:** 22/11/2026 · **Rodada:** r1 · **Alvo:** `33_PONTE_PROVA_FRACTAL_D4V6.md`,
`gk_proof_fractal_v6.py`, `gk_proof_fractal_v6_series.csv` (`5571b05f…`),
`gk_proof_fractal_v6_contrasts.csv` (`c567dbfd…`),
`gk_proof_fractal_v6_reanalise_r5.json` (`d3b6b336…`)
**Mandato:** atacar o 6/6 "fácil demais", a salvação por flag de (b), o
TOST de (c), o H_E1 PARCIAL, e se a "consolidação" é vitória ou ruído.

---

## A. Achados

### A1 (GRAVE) — 6/6 no boxdim com previsões derivadas do r5: não é circular?
As6 previsões de H_F2 foram escritas **depois** de ver o r5 (mesmas
chaves, direções tiradas dos pontos r5). Isso é replicação ou é
"prever o que já se viu"?

**Resposta:** **ACEITO a distinção — e o doc a faz.** H_F2 não é
descoberta, é **replicação com método novo em série nova** (seeds
disjuntos r2–r5): os pontos r5 foram a *hipótese*, os r6 são o *teste*.
O que seria circular: escolher chavras/direções **dos próprios dados
r6** — não foi feito (pré-registro `1113bb8` anterior ao run; grade
disjunta verificada por DISJ). E a redefinição de (a) para equivalência
**também** veio do r5, declarada antes. O que H_F2 prova, com honestidade
de escopo: "as previsões derivadas do r5 **replicam** em r6" — que é
exatamente o que o doc §3.3/§4.1 diz. **Não autorizado:** tratar H_F2
como descoberta nova. ✅

### A2 (GRAVE) — (b) do H_F1: o ponto caiu FORA do IC e a flag salvou uma
previsão pré-registrada — a regra não está desenhada para vencer?
O caso: ponto 0,1686 vs IC percentílico [0,064; 0,167] — **0,0012
acima**. Sem a regra de 2 níveis, H_F1 seria 2/3 (PARCIAL). Com ela,
3/3 (CONFIRMADA). Conveniente demais?

**Resposta:** **ACEITO a suspeição; três verificações a respondem.**
(1) A regra foi pré-registrada em r5 (não criada aqui) e o ramo
concordante é **simétrico**: ele também conta `FALHA_INCONCLUSIVO_FLAG`
e `CONTRADITA_FLAG` — não é uma máquina de confirmações. (2) A
salvação não é "ponto fora → conta": exige **concordância total** —
percentil e BCa excluem0 no mesmo sinal e coerente com o ponto; aqui
BCa [0,169; 0,199] e pct [0,064; 0,167] concordam positivo (e o z0=1,98
explica o deslocamento — viés conhecido). (3) O caso é **marginal**
(0,0012) e o flag é **visível** no veredito (`[1 concordantes-com-flag]`)
— o leitor vê que (b) não é limpo como (a)/(c). Decisão: manter; se em
r7 o padrão "perto da borda + flag" se repetir, investigar se o
percentil está sistematicamente estreito para `saltos:drat`. ✅

### A3 — (c) do H_F2: TOST de novo — "exclui 0 e equivalente" não confunde
leitores? E o parceiro BCa discorda (`bca_eq=False`).

**Resposta:** **ACEITO como ambiguidade de apresentação, não de
lógica.** É o mesmo padrão documentado no r5 (A2): TOST pergunta
"|efeito| < Δ"; CI95 pergunta "≠0"; ambos verdadeiros (efeito −0,036
detectável e < 0,05). O doc §3.3 repete a explicação. Sobre o parceiro
discordar: a regra **só exige concordância quando o ponto está fora**
(pré-registrado) — dentro, decide o primário; `bca_eq=False` está no
JSON para auditoria. Ressalva aceita: §5.1 do doc já a declara. ✅

### A4 — H_E1 PARCIAL (2/45 vs alvo ≤1): o fix não é completo — e os2
novos são `higuchi:relinc`. Por que higuchi de novo?

**Resposta:** **ACEITO o veredito PARCIAL (régua pré-registrada,
aplicada).** Os2 novos são chaves **diferentes** das5 do r5 (que
resolveram100%); `higuchi:relinc` em pares minref. Nota: higuchi em
relinc já era o padrão de resto no r4 (12/27 incoerentes de higuchi
lá) — a métrica+variante é a combinação mais frágil, não o estrato.
E H_F3 (dado novo) deu **1/45** — dentro do gate. Fix bom, não
perfeito; os2 ficam discordantes (não contam) — sistema se protege. ✅

### A5 — z0 extremos subiram 12 → 28 (r5 → r6): a linha está degradando?
Mais com os pares `drat:cadeia−τ` (aparece em2 rodadas) e degenerados
4 (r5:2). Progressão r4:61 → r5:12 → r6:28?

**Resposta:** **ACEITO a tendência como monitoramento, não como
degradação concluída.** Fatores: r6 tem `saltos:drat` com z0=+1,98 (o
caso da flag) e4 degenerados em `saltos/hurst` — todos **fora dos
confirmatórios** (boxdim:0 incoerentes; discordância total5,2% vs gate
10%). A progressão61→12→28 não é monótona (r5 foi o mínimo) e cada
rodada tem seeds diferentes — sem teste, "degradação" é leitura de
tendência com n=3. Registrado em §6.2 para r7 (originar no par
`drat:cadeia−τ`). ✅

### A6 — Cochran Q entre rodadas com n/grades diferentes: o teste é
válido ou é ruído com p-valor?

**Resposta:** **ACEITO a limitação — declarada antes do run (§1.3) e
repetida no §5.3.** O Q é o teste padrão de heterogeneidade de
meta-análise; inverso-de-variância lida bem com SEs diferentes (r3
n=64 tinha SE 0,06–0,09; r6 n=512 SE ~0,025 — os pesos já dão mais
valor às rodadas precisas). O que ele **não** separa: variação por
mudança de grade vs variação temporal — por isso o veredito é "SEM
HETEROGENEIDADE" (ausência de heterogeneidade detectável) e **não**
"prova de estabilidade". A leitura do doc §4.3 ("variação = ruído
entre amostras, não tendência") é forte demais? Atenuada aqui: o teste
**não detecta** tendência; com4 pontos e potência baixa para declive
suave, "não detecta" ≠ "não há". ✅ *(registro: refinar a frase do §4.3
para "sem tendência detectável".)*

### A7 — H_F4 DISPAROU (4×): a regra está inflando resultados?
4 flags — um deles é o (b) pré-registrado do H_F1. Se toda rodada tiver
flags, a regra vira padrão e a distinção "limpo vs flag" se perde.

**Resposta:** **ACEITO como tensão de projeto; dados ainda favoráveis.**
4/135 = 3% (r5:0) — minoria; flags são **reportados na string do
veredito** e separados no CSV; nenhum veredito global depende só de
flag sem nota. A alternativa (remover o ramo) foi condicionada a "0/135
de novo" — **não ocorreu**, então o ramo permanece (pré-registrado). Se
r7 ≥4 flags de novo, discutir estreitar a definição de concordância
(ex.: exigir ponto dentro de alguma tolerância, não só mesma direção).
Registrado. ✅

### A8 — Incidentes:3 crashes +1 commit pós-pré-reg (progress print)
Nova rodada, mesmo custo operacional. O protocolo C1 está virando
permeável?

**Resposta:** **ACEITO o custo; a distinção continua nítida.** O único
commit pós-pré-reg (`a2316b9`) é **print de progresso** — diff trivial,
auditável, sem tocar em hipótese/método/regra/dados (o padrão dos3
fixes anteriores: `3d244ab`, `8209433`, `0919e6b`). Os crashes são de
plataforma (CaDiCaL/Windows, documentado como limitação em todos os
docs desde o r4) e o checkpoint garantiu perda zero de dados (1536/1536
verificados). O que C1 protege — decisões científicas — permanece
intocado e provado por diff. ✅

## B. Veredito

**RECOMENDADO (r6)** — com A1–A8 incorporados. Resultado autorizado:

> "Com estratos **exatos** do `relinc` (transformação recalculada por
> réplica) e a consolidação pré-registrada: **H_E1 PARCIAL** (discordância
> relinc 5/45→2/45; todos os5 originais resolvidos); **H_F1 CONFIRMADA
> 3/3** na4ª rodada — com **(b) salvo pelo ramo concordante pela 1ª vez
> em dado real** (flag visível) — e **H_F1b SEM HETEROGENEIDADE** (Cochran
> Q p=0,13–0,71; sem tendência detectável em4 rodadas); **H_F2 boxdim
> CONFIRMADA 6/6** (replicação r5→r6 de previsões pré-registradas; 5/6
> teriam sido bloqueados pelo método do r4); **H_F3 CONFIRMADA** (relinc
> 1/45 em dado novo); **H_F4 DISPAROU 4×** (ramo mantido); **H_F5 ATINGIDO
> 6/6** (MDE 0,014–0,042). z0 extremos 12→28 (monitoramento, §6.2)."

**Não autorizado:** tratar H_F2 como descoberta nova (A1); "prova de
estabilidade" a partir do Q (A6); esconder o flag de (b) (A2); promover
H_E1 a CONFIRMADO (é PARCIAL); afirmar degradação por z0 com n=3 (A5).

**Pendências para a próxima rodada (científica, não de infra):** (i)
**τ k↑** ou **séries em b** — as perguntas originais da linha (§6.1);
(ii) monitorar z0/`drat:cadeia−τ` (A5); (iii) se flags ≥4 de novo,
estreitar concordância (A7); (iv) refinar frase do §4.3 para "sem
tendência detectável" (A6); (v) H_C2 (EF) inalterada.

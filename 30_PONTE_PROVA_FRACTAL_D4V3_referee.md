# Referee Hostile — 30_PONTE_PROVA_FRACTAL_D4V3 (D4′ v3, boxdim pré-registrado)

**Data:** 20/11/2026 · **Rodada:** r1 · **Alvo:** `30_PONTE_PROVA_FRACTAL_D4V3.md`,
`gk_proof_fractal_v3.py`, `gk_proof_fractal_v3_series.csv` (`6d4cbdd1…`),
`gk_proof_fractal_v3_contrasts.csv` (`0cb1dce2…`), JSONs
**Mandato:** atacar o pré-registro (é mesmo pré-registro?), os vereditos,
a correção pós-run, e se o resultado positivo (H_B3) suporta o que o doc diz.

---

## A. Achados

### A1 (GRAVE) — A margem 0,05 era impossível de atingir; a âncora ignorou a precisão
O pré-registro ancorou Δ=0,05 no **menor efeito separador do r2 (0,053)**
— mas a equivalência depende da **largura do IC90**, que no r2 já era
~±0,07 (`bca90=[−0,082; +0,058]`). Qualquer um que lesse o r2 sabia que
(c) **falharia** a 0,05. Ancorar margem só em efeito, sem precisão, é
ancorar sabendo do fracasso?

**Resposta:** **ACEITO como falha de desenho — e é exatamente o tipo de
coisa que o pré-registro existe para expor.** O valor 0,05 foi escolhido
por critério **declarado e independente** (1/3 da amplitude
entre-séries; menor efeito já detectado) — não houve ajuste para
"passar"; e a **sensibilidade pré-declarada (0,03/0,05/0,08)** mostrou o
quadro inteiro: eq a 0,08 ✓. Se a intenção fosse garantir vitória, a
margem seria 0,10 (a do r2) — não foi. **Lição registrada para r4
(§6.1): margem deve ser ancorada também na precisão observada**
(IC90 r3 → margem ≥0,07–0,08). O veredito (c) "FALHA_INCONCLUSIVO" é
verdadeiro e útil: **não se separa, mas não se certifica equivalência
apertada** — a leitura do doc §3.1 diz exatamente isso. ✅

### A2 (GRAVE) — Bug pós-pré-registro + veredito "REFUTADA" a partir de dados vazios
O run1 analisou **séries vazias** (bool vs string) e emitiu
"REFUTADA (0/3)" para hipóteses nunca testadas. Se o mesmo bug
servisse para **fabricar** dados (invertido), teríamos falso positivo
num experimento pré-registrado — qual a garantia de que a correção não
tocou nada além do filtro?

**Resposta:** **ACEITO a gravidade; a garantia é verificável.** (1) O
bug era de **plumbing** (comparação `bool == str`), detectado
**pelas séries = 0** — não havia como passar despercebido; (2) a
corrigida mudou **duas linhas**: `str()` no filtro + `SEM_DADOS` nunca
vira refutação (semântica); (3) **prova de integridade**: o CSV de
coleta congelado tem o **mesmo sha `6d4cbdd1`** registrado no JSON da
análise antes e depois (`input_series_sha256`) — os dados de entrada
são byte-idênticos; (4) hipóteses, margens, sinais, regras e grades do
pré-registro (`66f40ae`) **intocados** — diff limitado ao script de
análise, commitado à parte. (5) O caso "SEM_DADOS → REFUTADA" foi
**corrigido como bug de semântica** (isso é pós-hoc, mas é correção de
um veredito impossível, não de um veredito real). Registrado no §3 do
doc. ✅

### A3 (GRAVE) — H_B2 "REFUTADA" viola a própria regra de incoerência
A regra diz: incoerente **não conta como refutação nem como
confirmação**. H_B2 tem 1 OK + 1 INCOERENTE → o código imprimiu
**REFUTADA** — ou seja, o teste incoerente, direta ou indiretamente,
contou como refutação. O pré-registro falhou em definir o caso.

**Resposta:** **ACEITO — lacuna do pré-registro, não corrigida pós-hoc
no código.** O doc §3.2 reporta as **duas** coisas: veredito do código
(REFUTADA) e a leitura correta pela regra (**não confirmada, 1/2**). Não
mudei `eval_hyp` depois do run para "consertar" o número — isso seria
exatamente o movimento proibido; a correção semântica fica para r4
**declarada** (§6), junto com a definição prévia de todos os casos
possíveis (OK / FALHA / INCOERENTE / SEM_DADOS → veredito global). ✅

### A4 — As separações (a)/(b) são da correção de viés, não do sinal
O IC95 **percentílico** de (a) e (b) **inclui 0** ([−0,036; +0,121],
[−0,034; +0,129]); a exclusão vem do BCa (z0=0,63/0,66 — correção de
viés forte). Com tipo-I calibrado em n=50 (rate 0,04, mas IC amplo),
"OK_BONF" para (b) é frágil?

**Resposta:** **ACEITO — o doc já reporta isso (§3.1) e modula a força
do claim para "evidência moderada".** A régua do pré-registro era "IC95
BCa" (declarada), o BCa está calibrado (S4=0,04), e o percentil foi
reportado ao lado — nada foi escondido. Mas (b) é o único com Bonferroni
sobrevivente e mesmo ele depende de z0; a claim autorizada é
**"replicação moderada"**, não "confirmado fortemente". Para r4:
declarar qual IC (BCa vs percentil) é primário **e** reportar o outro
como robustez — hoje é o inverso (BCa primário por herança do r2). ✅

### A5 — A escolha de boxdim perdeu parte do motivo (H_B4 refutado)
Boxdim foi escolhida por ser a única métrica limpa no r2 (0/27); no r3
ela teve 3/27 incoerentes — o critério de escolha não se manteve.

**Resposta:** **ACEITO o fato; a escolha continua legítima.** Ela foi
**pré-registrada** com o motivo documentado (r2) — não foi refeita após
os dados; H_B4 **existe justamente para testar isso e foi refutada** —
o experimento se auto-corrigiu em vez de esconder. E o achado é
cientificamente útil: a incoerência **muda de métrica entre rodadas**
(higuchi 4/27→0/27; boxdim 0/27→3/27) → é **do par de séries**, não do
instrumento — isso reorienta a pendência C2 para "z0 extremo/IC
degenerado por par" (§6.2), com `saltos` (0/27) como candidata. ✅

### A6 — 9 incoerentes/135 e 2 ICs degenerados (`lo==hi`): a regra esconde quanto?
Aplicar `INCOERENTE` remove 9 testes da contagem. Quanto do resultado
mudaria se fosse todos?

**Resposta:** **parcialmente respondido pelo próprio CSV** — a regra é
**simétrica** (remove dos dois sentidos) e cada caso está com point/ICs
no CSV (auditável). Dos 9: **1 toca pré-registrado** (H_B2 cadeia — que
por isso virou "não confirmada", não "confirmada"; a regra **não**
favoreceu o resultado). Os 2 degenerados (`lo==hi`: hurst relinc;
boxdim_rank drat cadeia−τ) são o alvo do §6.2. Nenhum veredito do doc
depende de esconder um incoerente — H_B1 e H_B3 estão completos. ✅

### A7 — Generalização: "replicou" significa o quê, com os mesmos geradores?
Mesmos geradores, seeds novos — o doc diz "distribuição do gerador"
(§1.1). É suficiente para "a pista A4 confirmada"?

**Resposta:** **ACEITO o escopo e o doc o mantém.** H_B3 é
"pré-registrada e confirmada **para a distribuição do gerador
`gen_implication`/`gen_cadeia` com a grade declarada**" — nada de
"famílias de prova em geral" (§4.1 usa "pré-registrada e confirmada
para `drat:implication−cadeia`"). A extrapolação para outras famílias
ficaria para replicação externa. ✅

## B. Veredito

**RECOMENDADO (r3)** — com A1–A7 incorporados. Resultado autorizado:

> "Com **boxdim pré-registrada** (commit `66f40ae` anterior ao run) em
> **192 instâncias novas disjuntas** do r2: a pista A4
> (`drat:implication−cadeia`) **replicou e sobrevive a Bonferroni**
> (Δ=−0,170, BC97,5% [−0,301; −0,110]); o padrão-τ em `minref`
> **replicou em 2/3** (ambos os pares τ separando, (b) com Bonferroni;
> imp−cadeia **não separa** mas a equivalência a ±0,05 **não é
> certificável** — sensibilidade: eq a ±0,08 ✓); H_B2 **não confirmada**
> (1/2, 1 incoerente); H_B4 **refutada** — incoerência instável entre
> métricas (higuchi 0/27 aqui) → é do par, não do instrumento;
> delete-d vs delete-1 **0/135** discordâncias. Claims de separação
> (a)/(b): **evidência moderada** (percentil inclui 0; correção de viés
> BCa)."

**Não autorizado:** "equivalentes a ±0,05" (A1); "H_B2 refutada"
(leitura: não confirmada — A3); "boxdim imune a saturação" (H_B4
refutado — A5); "confirmado fortemente" para (a)/(b) (A4); generalizar
para fora dos geradores (A7).

**Pendências para r4:** (i) margem ancorada **também** em precisão
(IC90→≥0,08) (A1); (ii) definição prévia do veredito global para cada
classe, incl. INCOERENTE (A3); (iii) primariedade de IC declarada (BCa
vs percentil) (A4); (iv) diagnóstico de z0 extremo/IC degenerado +
`saltos` como candidata (A5/A6); (v) n maior (MDE80 < 0,06) (§6.1);
(vi) τ k↑ inalterada.

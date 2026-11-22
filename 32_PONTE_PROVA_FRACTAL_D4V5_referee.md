# Referee Hostile — 32_PONTE_PROVA_FRACTAL_D4V5 (D4′ v5, n=512)

**Data:** 22/11/2026 · **Rodada:** r1 · **Alvo:** `32_PONTE_PROVA_FRACTAL_D4V5.md`,
`gk_proof_fractal_v5.py`, `gk_proof_fractal_v5_series.csv` (`df3737ce…`),
`gk_proof_fractal_v5_contrasts.csv` (`c30b13f2…`), JSONs
**Mandato:** atacar o 3/3 de saltos (decadência de magnitude?), a "equivalência
com CI95 excluindo 0", o ramo da regra nunca testado, a concentração de
discordantes em `relinc`, e os 2 bugs pós-pré-registro.

---

## A. Achados

### A1 (GRAVE) — `saltos` confirmado 3/3, mas as magnitudes estão caindo
(a) +0,173 → +0,185 → **+0,138**; (b) +0,110 → +0,117 → **+0,080**;
(c) +0,120 → +0,113 → **+0,104**. Queda de ~25–30% em duas rodadas — é
decaimento real (o efeito depende de algo que muda entre grades) ou
flutuação?

**Resposta:** **ACEITO a pergunta; os dados não sustentam decaimento.**
(1) Os ICs95 das três rodadas se **sobrepõem** em todos os testes
(ex.: (b): r4 [+0,082;+0,207] vs r5 [+0,064;+0,165] — sobreposição
total); (2) não há tendência monotônica com significado: (a) subiu do
r3 ao r4 e caiu no r5 — oscilação, não declive; (3) as três rodadas
usam **seeds disjuntos** — cada valor é uma amostra independente da
mesma distribuição do gerador; a dispersão entre rodadas (0,08–0,19)
é a escala natural do efeito. **Leitura autorizada:** "efeito positivo
robusto em 3 amostras independentes, magnitude entre 0,08 e 0,19".
Declínio só seria claim com teste de tendência sobre ≥4 rodadas —
registrado como pergunta para r6, não afirmado aqui. ✅

### A2 (GRAVE) — (c) é "EQUIVALENTE" com CI95 excluindo 0 — contraditório?
O teste (c) tem CI95 = [−0,047; −0,012] (diferente de 0!) mas veredito
`OK = EQUIVALENTE @0,05`. "Diferente e equivalente ao mesmo tempo" é
defensável ou é bug de ordem de classificação?

**Resposta:** **defensável e foi a ordem pré-registrada** (§1.5: "IC90
primário na margem → OK" vem antes de "exclui 0 → FALHA_SEPARA"). É o
resultado canônico do **TOST** (Lakens): a pergunta da equivalência é
"|efeito| < Δ", não "efeito = 0". Aqui: efeito −0,037 é **detectável**
(CI95 exclui 0) e **menor que a margem 0,05** (IC90 ⊂ ±0,05) — "diferente
de zero, mas praticamente irrelevante" é uma conclusão legítima e, de
fato, a mais informativa possível. O doc §3.2 explica explicitamente.
Ressalva registrada: o parceiro BCa discorda da equivalência
(`equiv_bca=False`) — a regra só exige concordância do parceiro quando o
ponto está **fora** do IC; dentro, decide o primário (pré-registrado).
✅

### A3 — O ramo "concordante" da regra de 2 níveis nunca disparou — a
metade nova da regra é cosmética?
0 `*_FLAG` em 135 contrastes: todos os 6 pontos fora eram discordantes.
A regra que o r4 pediu (contar concordantes) não teve nem1 ocorrência.

**Resposta:** **ACEITO como fato e é uma resposta empírica, não cosmética:**
em dados reais com o método novo, **ponto fora ⟹ discordância** (6/6) —
isto é, quando o percentil e o BCa discordam sobre onde o ponto está, eles
também discordam sobre a exclusão. O ramo concordante existe para cobrir o
caso lógico (e foi exercitado no smoke test com fixtures), mas a
frequência observada é **zero** — o que simplifica a leitura: em r5, a
regra de 2 níveis equivale, na prática, a "fora → não conta". Registrado:
se r6 repetir 0/135, o ramo pode ser **removido do pré-registro** (menos
superestrutura). ✅

### A4 — 5 dos 6 discordantes estão em `relinc` — a aproximação de
estratos do `relinc` (1º estrato −1) está causando os próprios falhos?
O `relinc` usa `runs[0] -= 1` (aproximação declarada). Os 6 discordantes:
4 `saltos:relinc`, 1 `hurst:relinc`, 1 `saltos:log1p` — **0 em `raw`**.

**Resposta:** **ACEITO como suspeita principal e levado a r6 (§6.1).**
A evidência circunstancial é forte: a variante com estrato aproximado é
de onde vêm5/6. Mas (1) `log1p` **não** tem a aproximação (mantém
comprimento e estratos exatos) e ainda assim gerou1 discordante — há
alguma residual do método, não só a aproximação; (2) nenhum confirmatório
(`raw`) foi afetado — os vereditos das hipóteses não dependem disso;
(3) a correção (recalcular fronteiras do `relinc` pós-diferença) está
declarada em §6.1 **antes** de qualquer run de r6. ✅

### A5 — (a) do H_D2 errou a direção pela 3ª vez — manter a previsão é
vontade, não ciência?
r3 +0,060 (ok fraco) → r4 −0,024 → r5 −0,012 — três rodadas sem efeito
positivo. O doc mantém (a) como teste direcional `d+1`.

**Resposta:** **ACEITO — a previsão está morta e o doc diz isso** (§3.2:
"fracassou pela 3ª vez", §5.3: "qualquer rodada futura deve redefinir (a)
como equivalência"). Mantê-la **neste** run era obrigação do pré-registro
(mudar depois de ver r4 seria pós-hoc); o veredito `FALHA_INCONCLUSIVO`
está registrado como está. R6 redefine. ✅

### A6 — Dois bugs de código pós-pré-registro: o protocolo C1 está
servindo só para hipóteses, não para o código?
Pre-registro `b6c359f`, depois `8209433` (runs_of) e `0919e6b`
(pre.items()) — o código executado difere do pré-registrado.

**Resposta:** **ACEITO a distinção e a defendo com evidência.** O
pré-registro protege **decisões científicas**: hipóteses, direções,
margens, método, regras, grade — **todas intactas** (diffs auditáveis:
os dois fixes tocam `runs_of`/H_D3-report e nada mais). Os bugs eram de
**plumbing com falha visível** (estrato errado impresso; ValueError) —
não havia como "escolher" um resultado. O custo foi 1,5h + 2 arranques,
pago e registrado. E o processo **melhorou**: o smoke test com stub passou
a ser pré-requisito (executado antes do relançamento) — a lição virou
procedimento. Comparação com r3 (bug de filtro pós-run) e r4 (crash):
três rodadas, três incidentes de execução, **nenhum tocou nas decisões**,
todos documentados nos §3 correspondentes. ✅

### A7 — H_D4 "6/6 ATINGIDO" com (e)=0,052 — folga de 3% não é folga
Os MDE: 0,014–0,052; (e) 0,052 < 0,06 por 0,008. Se o run tivesse dado
0,061, o veredito seria outro — o alvo foi "quase perdido".

**Resposta:** o veredito é binário e **foi atingido como declarado** — sem
"quase" no JSON (`ATINGIDO`, valores exatos no doc §3.4). A previsão
√(384/512) errou para baixo em (e) (previsto ~0,059, real0,052 — na
verdade acertou folgadamente; o caso apertado não se materializou). Sem
pós-hoc. ✅

### A8 — Os 6 discordantes não invalidam a afirmação "incidência 4,4%"?
Se5/6 são artefato do `relinc` (A4), a incidência "real" seria ~1/135 —
o doc reporta 4,4% **sem** subtrair os suspeitos. Não é subestimar o
mérito do método?

**Resposta:** o doc reporta **bruto (6/135)** e **não** subtrai —
subtrair seria pós-hoc em favor do próprio método. O gate (≤10%) passa
com folga **no bruto**; a decomposição por variante (§3.3: 0 em `raw`)
é dada para o leitor julgar. Se a correção do `relinc` (r6) zerar os 5, a
incidência bruta continua sendo o número do gate. ✅

## B. Veredito

**RECOMENDADO (r5)** — com A1–A8 incorporados. Resultado autorizado:

> "Com **`saltos` como métrica primária** e método de IC **selecionado
> pela calibração** (percentil + bootstrap estratificado por parâmetro;
> tipo-I 0,075; calibração S4–S6 pré-run): **H_D1 CONFIRMADA 3/3
> Bonferroni** em 3ª rodada independente (r3→r4→r5, magnitude0,08–0,19,
> ICs sobrepostos — sem evidência de declínio); **H_D2 PARCIAL 5/6**
> (0 discordantes): equivalência **±0,05 certificada** em imp−cadeia,
> pista (d) e fonte (f) limpas pela 1ª vez, (a) sem efeito pela 3ª vez;
> **H_D3 CONFIRMADA**: incidência discordante **4,4%** (r4: 33%), z0
> extremos 61→12, degenerados 16→2, **head-to-head bloco8 bloquearia 4/9
> vs primário 0/9**; **H_D4 ATINGIDO 6/6** (MDE 0,014–0,052). Regra de 2
> níveis aplicada; ramo concordante **0 ocorrências** (resposta empírica,
> A3)."

**Não autorizado:** "saltos com efeito decaindo" (A1: ICs sobrepostos);
"equivalente = igual a zero" (A2: TOST ≠ igualdade); afirmar que o ramo
concordante "funciona em dados reais" (A3: não disparou); culpar só o
`relinc` pelos discordantes (A4: `log1p` também tem); redefinir (a)
neste run (A5: é pós-hoc); subtrair suspeitos da incidência (A8).

**Pendências para r6:** (i) estratos exatos do `relinc` (A4/§6.1);
(ii) redefinir H_D2(a) como equivalência (A5); (iii) decidir sobre o
ramo concordante se r6 repetir 0 ocorrências (A3); (iv) teste de
tendência de magnitude de `saltos` com ≥4 rodadas (A1); (v) τ k↑ e
séries em b como próximas perguntas científicas (§6.3); (vi) H_C2 (EF)
inalterada.

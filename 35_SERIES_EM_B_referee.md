# Referee Hostile — 35_SERIES_EM_B (séries em b, σ fixo)

**Rodada:** r1 (28/11/2026) · **Alvo:** `35_SERIES_EM_B.md` §3–6 +
`gk_series_b.json` (sha CSV `50ecd215dae321c5…`) · **Postura:** atacar
seleção, direção, exclusões e a máquina de duas etapas. Nada promovido
sem resposta.

## A. Achados

### A1 (GRAVE) — Exclusão dirigida pelo resultado: 14/32 σ's fora por censura

H_b2 fala dos **16 σ's sem nenhuma instância minref≥8** (44% dos σ's
excluídos por terem pontos censurados +2 constantes). A exclusão é
**dirigida pelo resultado** (o critério é uma propriedade dos valores
de minref). Se σ's sujos tiverem dinâmica diferente (ex.: anti-
persistência reversa), o claim **não os cobre** — e são quase metade.

**Resposta (aceita com condição de redação):** escopo foi **pré-
declarado** (H_b1/§1.3: "σ's não utilizáveis são EXCLUIDOS… ESCOPO:
H_b2 fala dos σ's sem instância minref≥8"); as sondas mediram a taxa
(~50%) **antes** do run e motivaram S=32 justamente para o gate não
falhar; a alternativa (20M) é **inviável** (sonda: 1,8–2,1h POR
instância minref=11 → ~9 dias). Condição: o `INDICE.md` deve trazer o
escopo **na própria claim** (§B.2). Análise de sensibilidade futura:
tratar censurados como `≥cens` (limite inferior) — registrado no §6.

### A2 (GRAVE) — Direção −1 tirada de UMA sonda

A direção do H_b2 (alternância) baseia-se em **um** σ de engenharia
(σ=5000, D=−0,36). Se a sonda tivesse dado o sinal oposto, a direção
seria +1 e o resultado provável seria `CONTRADITA` — ou, pior, a
direção poderia ter sido escolhida depois de espiar os dados do
experimento (não foi: commit `7f45d12` precede o run; seeds do
experimento6000+ intocados até o run).

**Resposta (aceita com condição):** cadeia de decisões documentada
(doc35 §1.3 nota + §1.4 histórico): sonda → direção, **antes** do
commit; caveat obrigatório no `INDICE.md` ("direção baseada em sonda
única"). O fato de14/16 σ's do experimento caírem no sinal esperado é
**evidência a favor**, não contaminação.

### A3 — Outlier σ=6027 (+0,447) e n=16

Um σ fortemente positivo; n=16 é o menor da linha.

**Resposta (aceita):** sensibilidade leave-one-out **sem** σ=6027:
média ≈ **−0,289** (MAIS negativa) → veredito robusto (o outlier
puxa **contra** a hipótese; removê-lo fortalece). O jackknife
delete-one (n_jack=16) já é parte da máquina (BCa usa o pooled).
MDE80=0,183 com o n real — efeito observado 0,243 > MDE ✓.

### A4 — Máquina de duas etapas (shuffles + bootstrap): calibração fiel?

S3 calibrou tipo-I 1/40 e poder10/10 — mas com sintético `alf=[5,7]`,
T=28 fixo. Dados reais: T∈{28,29,30}, alfabeto {5,7,9,11} (alguns σ's
com9/11).

**Resposta (aceita):** (i) o shuffle-centering remove o viés de
amostragem finita do acf₁ (E[acf₁ de shuffle] ≈ −1/(n−1)) — por isso
D é centrado em0 sob H0 **mesmo** com empates; (ii) alfabeto com mais
níveis só **aumenta** variância de D no nulo (tipo-I conservador —
observado:1/40); (iii) T=29/30 vs28: irrelevante para acf₁. Risco
residual aceito e declarado (§5: "curtas e binárias").

### A5 — Escolha de config após ver alternância na sonda?

(2,5) foi escolhido depois de ver a série de σ=5000 **alternando**
(5,7,5,7…) — seleção indireta pela riqueza/alternância da sonda?

**Resposta (aceita parcialmente):** as razões declaradas de descarte
das outras configs são **legítimas e independente da alternância:**
(1,5)/(1,6) = série **plana** (sem variância não há teste algum);
(3,4) = T=8–11 <16 (boxdim/acf nem nasceriam); (3,5)/(2,6) = **parede
n≥8** (censura). Restou (2,5) como única config viável. A alternância
da sonda só informou a **direção** (A2). Ainda assim: a *riqueza* de
variação é pré-requisito de qualquer potência — aceito como
seleção-de-engenharia documentada, não como p-hacking de veredito.

### A6 — C1 temporalidade: o run precedeu o commit?

**Resposta (verificada):** não. Sequência: sondas (5000–5004) →
selftests OK → lint 10/10 → **commit `7f45d12` + CI verde** → run
lançado (PID14284,15:31). `git log` confirma; grade/direção/máquina
fixadas no commit. O crash `0xC0000005` (tentativa1,507 linhas) e o
retomar (tentativa2 →904) são **incidentes de execução**, não mudanças
de método — checkpoint atômico como no τ k↑.

### A7 — H_b3 "SEPARA" no JSON: não é claim disfarçado?

O JSON registra `veredito: SEPARA` no contraste descritivo — risco de
alguém ler como confirmado.

**Resposta (aceita com condição):** o campo carrega `nota:
"(P)/candidata (C) — DESCRIPTIVA, sem claim"` no próprio objeto; o doc
§3.3/§4.3 marca como pós-hoc; condição: `INDICE.md` **não** pode
usar verbo confirmatório para H_b3 (só "candidata").

### A8 — Conformidades verificadas (sem achado)

- **DISJ:** grade × (v2..v6 + τ k↑) = ∅ (OK no run);
- **ASSERT:** `minref ≥ d(∅)` + `solve=UNSAT` por construção — **0/904**;
- **S6:** drat determinístico (2 execuções idênticas);
- **Gerador:** equivalência sonda×script **5/5** (hash+tag+T);
- **Múltiplas comparações:** H_b2 é a **única** confirmatória
  (α=0,05 sem Bonferroni de grupo — pré-declarado); H_b1 é gate de
  contagem; H_b3 descritiva; métricas sem p-valor;
- **R6:** sha CSV×JSON registrado (`50ecd215…`);
- **Degeneração `saltos`:** descoberta e corrigida **antes** do commit
  (S3 falhou → troca para acf₁) — o selftest cumpriu seu papel; S4
  fixou o contrato (≡1,0 confirmado nos dados reais).

## B. Veredito

1. **H_b1 (viabilidade): PROMOVIDA — CONFIRMADA (16/32 ≥ 12)**;
2. **H_b2 (estrutura serial em b): PROMOVIDA COMO CLAIM (P) —
   "CONFIRMADA (OK): média D = −0,243 [percentil −0,365; −0,109],
   BCa concordante, dirn=−1, n=16, MDE 0,183"**, com **3 condições
   obrigatórias de redação**: (i) **escopo explícito** — "σ's sem
   instância minref≥8 (16/32)"; (ii) **caveat da direção** — "direção
   −1 baseada em sonda única de engenharia"; (iii) **nota de poder** —
   "efeitos < ~0,18 indetectáveis; outlier σ=6027 registrado;
   leave-one-out fortalece";
3. **H_b3:** apenas **candidata (C)** — proibido verbo confirmatório
   (condição A7);
4. **ASSERT:** OK (0/904); **incidente0xC0000005** contido por
   checkpoint — documentado;
5. **Nenhuma** promessa de EF, de n≥8 ou de σ's sujos.

**R1 aprovado com condições de redação** (3 para H_b2 +1 para H_b3 —
nenhuma exige reexecução). Só após incorporar as condições ao
`INDICE.md`/catálogos o resultado é promovido.

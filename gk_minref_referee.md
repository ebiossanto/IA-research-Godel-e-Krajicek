# Referee Hostile — gk_minref (ferramenta de comprimento mínimo de refutação)

**Data:** 19/11/2026 · **Rodada:** r1 · **Alvo:** `gk_minref.py` +
`gk_minref_results.{csv,json}` · **Mandato:** validar a ferramenta, o 6º bug
do projeto e o impacto nos resultados já commitados do teste LP.

---

## A. Achados

### A1 (GRAVE) — Completude do encoder: o bug de SOBREPOSICÃO
A v1 do `res_pairs` só gerava pares **particionados** (S₁∪S₂ = C disjuntos).
A resolução permite **sobreposição**: `(a∨b),(b∨¬a) → (b)` com `{b}` em ambos
os lais. A derivação real do caso `random2sat` (exposta ao vivo: v1 reportava
`>64`) usava exatamente um passo desses → **6º bug do projeto** (após:
off-by-one, filtro de tautologia, AND-vs-OR, condições de sonsidade,
profundidade-vs-linhas).

**Correção (arquitetural):** pool = **fecho de resolução** (saturação sem
tautologias; WLOG qualquer refutação usa só cláusulas do fecho) + pares
enumerados **por força bruta sobre o fecho** (completo por construção).
**Validação:** units=3 ✓ · **ABC=5** (a v1 dizia6 — era artefato do bug;
derivação de5 linhas verificada passo-a-passo: `[1,-2],[1,2],[-1],
res(L1,L2|x2)=[1], res([1],[-1])=∅`) · sat=∞ ✓ · regressão
`random2sat_n5_m12` ✓. ✅

### A2 — Benchmark: estouro anterior e novo escopo
A v1 do benchmark estourou **25min** (timeout): `random3sat` n=5 produz
fechos ~211 com ~19k pares → auxiliares explodem com t. **Correção:**
`MAX_AUX=400k` (orçamento explícito, censura declarada) + famílias de
**fecho pequeno** (2-SAT n=5/6, cadeias, variantes de sobreposição) —
o domínio de projeto declarado do minref. Resultado: **17/17 exatos, todos
<2s**; distribuição `{7:6, 9:4, 11:1, 5:2}`; cadeias `7,9,11` (2k+1) ✓.
Escopo honesto: **n≤6, resolução** (não DRAT/EF), sem lower bound geral. ✅

### A3 (CRÍTICO) — Impacto nos resultados COMMITADOS do teste LP
O `gk_alternating_family.py` (artefatos T1/T2/T3 já pushados) também usava
pares particionados. **Pergunta do referee: T1 foi distorcido?**

**Verificação executada (92/92 — exaustiva, não amostral):** reconstituiu
por replay de RNG exato as92 γ-insat da rodada T1 e testou `REF_6` com o
encoder **completo** (mesmo fecho/pares da ferramenta nova):

> **92/92 REF_6=UNSAT → minref >6 para todas → o `REF_6=UNSAT` do encoder
> antigo estava CORRETO → números de T1 SUSTENTADOS integralmente.**
> (Fecho idêntico em todas:211 cláusulas,19050 pares — random-3SAT denso
> em n=5 satura o mesmo fecho.)

O bug, portanto, **não** alterou as conclusões do `C2_LP_familia_alternante`
(a direção do viés seria p/ mais alternância, mas nenhuma γ-insat tinha
ref ≤6 de qualquer forma). **Nenhum rerun necessário.** ✅

### A4 — Reprodutibilidade
Seed `20261119` fixa; CSV sha256 **normalizado CRLF→LF** (regra do CI);
saídas `gk_minref_results.{csv,json}` com metadados de escopo. ✅

### A5 — Encoder antigo do `gk_alternating_family` permanece particionado
Refatorá-lo mudaria artefatos futuros (shas) — **não feito** (escopo).

**Resposta:** declarado — T1 verificado92/92 (A3); execuções FUTURAS do
script antigo devem preferir o encoder de `gk_minref` (completo) — nota no
próprio script (pendência aplicada). ✅

---

## B. Veredito

**RECOMENDADO (r1)** — ferramenta validada,6º bug documentado, impacto no
trabalho commitado **exaustivamente aferido e nulo** (92/92).

**Limitações declaradas (escopo):** n≤6 · resolução · orçamento MAX_AUX ·
benchmark só de fechos pequenos · nenhum claim de lower bound geral.

**Uso:** `python gk_minref.py demo | dimacs FILE | --benchmark`.

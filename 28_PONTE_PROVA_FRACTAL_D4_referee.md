# Referee Hostile — 28_PONTE_PROVA_FRACTAL_D4 (D4′ v1)

**Data:** 19/11/2026 · **Rodada:** r1 · **Alvo:** `28_PONTE_PROVA_FRACTAL_D4.md`,
`gk_proof_fractal.py`, `gk_proof_complexity_fractal.json`, `gk_proof_fractal_series.csv`
**Mandato:** atacar quantificadores, confundimentos, overfitting numérico, escopo.

---

## A. Achados

### A1 (GRAVE) — O que D_H separa NÃO é "dureza de prova", é tendência × ruído
`php` tem D_H=1,27 (mais suave) e as demais ~2,0 (mais ásperas). A causa óbvia:
a série do php é `exp(m)` domínio-dominado (48→935.504), enquanto `implication`/
`tau` são inteiros pequenos com jitter. **Se a métrica só detecta "curva suave vs
ruidosa", o título "ponte prova→fractal" promete mais do que os dados entregam.**

**Resposta (aplicada):** §4.1 do documento **refuta explicitamente** a hipótese
ingênua e reenuncia o resultado como *separação de regimes de crescimento* — não
como "dureza fractal". A variante **log1p** (que aplaina a exponencial em escala)
mantém a separação (IC exclui 0 em 4/4) → a separação **não** é mero artefato de
escala, mas continua sendo separação de regime, não de dureza. **Nenhum claim de
"hardness fractal" sobrevive ao referee.** ✅

### A2 (GRAVE) — Artefato de quantização nos inteiros pequenos
`implication`/`tau` têm provas de 8–46 linhas (inteiros); quantização inteira
injeta ruído de alta frequência → D_H≈2 artificialmente próximo do máximo.

**Resposta:** **reconhecido como limitação** (§6.4) — o contraste
implication-vs-tau (ambos inteiros) **de fato não separa** (IC inclui 0), o que
**coerente** com o artefato: quando a quantização é igual, não há diferença. A
separação php-vs-outros sobrevive ao log1p mas **não** está imune à objeção em
geral. Mitigação declarada como v2 (incrementos relativos / normalização).
**Nível do resultado: RECOMENDADO com limitação explícita, não "descoberta".** ✅

### A3 — H_RS >1 (1,363) em série não-estacionária
R/S em série com tendência exponencial infla H acima de1 — métrica inválida ali.

**Resposta:** marcado **descritivo apenas** no documento (§3.1 rodapé); H_RS não
entra nos testes confirmatórios (só D_H). ✅

### A4 —18 contrastes (3 pares ×3 métricas ×2 variantes) = p-hacking potencial
**Resposta:** §3.2 define **a priori** como confirmatórios apenas D_H raw+log1p
nos pares envolvendo php (4 testes) — todos excluem 0 com sinal coerente; os
demais marcados exploratórios. Mesmo assim: **sem correção de múltiplas
comparações aplicada** — declarado; com Bonferroni exploratório (α=0,05/4=0,0125)
os ICs de implication−php raw (limite 0,051) **ficariam no limite** → nota honesta:
**evidência forte para php−tau, moderada para implication−php raw.** ✅
(Adicionado: ver §3.3 abaixo.)

### A5 — Séries de tamanhos/grades diferentes por família
m=4..9 vs 8..23 vs 2..9 — o "índice ordinal" não significa a mesma coisa entre
famílias.

**Resposta:** reconhecido (§6.5); a comparação é de **forma estatística da curva**
sobre a grade natural de cada família — aceitável para separação de regimes, não
para igualdade pontual. ✅

### A6 — `z3_proof_nodes` ≠ EF; php|z3 n=50 (10 timeouts de5s)
**Resposta:** H_C2 **DEFERIDO** no JSON e no documento; proxy sempre rotulado;
n=50 reportado. ✅

### A7 — Exit code1 apesar de sucesso; `sat.proof` removido após aviso
**Resposta:** artefato completo (JSON+CSV+sha); causa = teardown z3/atexit;
registrado §6.6. Aviso Z3 eliminado na rodada final (saída limpa). ✅

### A8 — Bug da rodada1 (sinal Higuchi, janelas degeneradas) — como foi pego?
**Resposta:** pela **validação sintética obrigatória** (ruído→2,07, seno→1,20
só após correção). Lição: validação de métrica contra séries de referência é
obrigatória antes de qualquer medição — incorporar ao `diagnostico` de futuros
experimentos gk_*. ✅

---

## B. Veredito

**RECOMENDADO (r1)** — com as correções já aplicadas e limitações explícitas
(A1, A2, A4, A5, A6 no documento). O resultado autorizado é **apenas**:

> "Métricas fractais (D_H de Higuchi) **separam** a família `php` das famílias
> `implication`/`tau` em séries de comprimentos de prova DRAT reais, robusto a
> log1p (IC95 exclui 0), interpretado como **separação de regime de crescimento**
> (exponencial vs quase-linear) — não como dureza fractal, não como lower bound,
> não como Res-vs-EF."

**Não autorizado:** qualquer claim sobre Extended Frege; "provas duras são mais
fractais"; generalização para PA/τ reais além das famílias testadas.

**Pendências para r2 (v2 do experimento):** normalização anti-quantização (A2);
correção de múltiplas comparações ou registro explícito do teste primário (A4);
séries τ maiores (k↑) ligadas a PR10/PR11.

---

## C. Rodadas adicionais — achados do desenvolvimento da v2 (20/11/2026)

### A9 (GRAVE, 7º bug do projeto) — unidades de saída do `gen_tau` invertidas
O gerador `gen_tau` do v1 codificava `saída = ¬b` (cláusula `[o]` quando
`b_i=0`), contradizendo o próprio comentário (`# saida = b`). A família só
era UNSAT quando `¬b ∉ imagem` — em `k=2,w=3`, **10/24 seeds davam SAT**
(sonda da v2). **Impacto no v1: NENHUM na validade dos dados.** O CSV
congelado tem **188/188 UNSAT verificado por solver** (as 64 instâncias τ
do v1 são τ com testemunha `¬b ∉ imagem`, igualmente legítimas); o que
estava errado era a *garantia construtiva* documentada ("b fora da
imagem"). **Corrigido** em `gk_proof_fractal.gen_tau` (unidades passam a
codificar `saída = b` de fato). Artefatos v1 não são regenerados
(frozen + sha registrado). ✅

### A10 (GRAVE, 8º bug do projeto) — "seed fixa" não reproduzia entre processos
Os geradores usavam `random.Random((SEED,"imp",m,seed).__hash__())` — o
`__hash__` de tuplas contendo strings é **randomizado por PYTHONHASHSEED**
e muda a cada processo (verificado: 3 processos → 3 hashes distintos).
Consequência: o v1 (e a primeira execução da v2) **não era regenerável
entre execuções** apesar do seed declarado; o CSV congelado permanece
válido *dentro* do processo que o gerou (sha256 registrado, dados reais),
mas a promessa "Reproduzir: `python -u gk_proof_fractal.py` → mesmo sha"
era **falsa entre máquinas/execuções**. **Corrigido:** `_det_seed()`
(CRC32 de `repr(parts)`) — verificado determinístico entre processos.
Atingia apenas os 4 geradores do fractal; os demais `gk_*` usam
`random.Random(int)` (determinístico). **Efeito colateral honesto:** uma
re-execução pós-correção gera instâncias *diferentes* das congeladas
(mesma distribuição, seed agora real) — por isso os artefatos v1 não são
sobrescritos. ✅

### A11 — O que a v2 (minref) perguntou e o que isso implica para A1/A2
A v2 troca "prova do solver" por **comprimento mínimo exato** (fonte
canônica) e controla o regime (escopo n≤6 elimina o php exponencial).
Isso transforma A1 de *interpretação* em *hipótese testável*: se a
métrica media regime (e não família), **controlado o regime a separação
deve desaparecer** — registrado a priori como H_C3 no
`gk_proof_fractal_v2.py`, com H_C4 (invariância de fonte) como controle.
Veredictos e números: `29_PONTE_PROVA_FRACTAL_D4V2.md`. ✅

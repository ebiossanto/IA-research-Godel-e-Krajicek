# Avaliacao de Novelidade e Resultados Existentes

> **STATUS (22/09/2026 — PR12 + revisao externa):** Seções 2–3 contêm **AFIRMAÇÕES
> REJEITADAS ou NÃO CERTIFICADAS**. Teoremas 4 e 6 **não provados** (09 §33).
> Novidade: **provisória** — não "sem equivalente na literatura".
> Ver `INDICE.md` D1–D8 e `EVOLUCAO_PROJETO.md`.

## 1. O que JA EXISTE na literatura (honestidade intelectual)

### Resultado A — Krajicek (2004/2025): Geradores a partir de incompletude
Krajicek define um gerador g_T a partir de uma teoria T: o bit extra codifica paridade de provas de insatisfiabilidade em T. Mostra que g_T e hard para sistemas que interpretam T.

**Status:** Essencialmente equivalente a nossa construcao G_P^T do Paper 1. Krajicek foca na funcao; nos focamos na tautologia.

### Resultado B — Krajicek (JSL 2025): Incompletude de teorias p-tempo
Prova que qualquer teoria p-tempo T capaz de formalizar sintaxe de logica de 1a ordem deve ser incompleta, usando g_T que estende entrada por 1 bit.

**Status:** Resultado de incompletude para teorias p-tempo. Nosso antigo "Teorema 1" (barreira de interpretabilidade) **está REJEITADO** — enumeração exponencial ≠ polinomial; Krajíček (2023) já faz o mecanismo correto.

### Resultado C — Krajicek (arXiv:2506.2025): Problem DD_P e hipotese (ST)
Estuda busca de provas: dada uma prova de disjuncao com atomos disjuntos, encontrar qual disjuncto e tautologia. Formula hipotese (ST) de que DD_P nao e soluvel no modelo estudante-professor.

**Status:** Sobre busca de provas, nao comprimento. Complementar.

### Resultado D — Beklemishev (2000-2024): Hierarquias de reflexao para PA
Cada nivel ordinal alpha produz uma teoria T_alpha mais forte. A ordem-teorica de PA e epsilon_0.

**Status:** Teorias de 1a ordem, nao sistemas proposicionais. A ponte reflexão↔geradores é **candidata a novidade** (não certificada; exige revisão por especialistas).

### Resultado E — Monroe (2026): Hardness como restricao informacional
Unifica meta-complexidade sob uma assuncao. Conecta MCSP, Kolmogorov, e provabilidade.

**Status:** Framework unificador, nao foca em geradores godelianos especificamente.

### Resultado F — Oliveira (2025): Meta-matematica da complexidade
Survey da formalizacao e independencia de resultados de complexidade em aritmetica delimitada.

**Status:** Survey, nao contribuicao original.

### Resultado G — Saitou & Noguchi (2026): Goedel mecanizado em Lean 4
Mecanizam os 1o e 2o teoremas da incompletude, teorema de completude de Solovay, e logica de provabilidade em Lean 4.

**Status:** Mecanizacao formal. Complementar e util para verificacao futura.

### Resultado H — Fang et al. (2026): K-SAT autorreferencial
Constroem instancias de SAT autorreferenciais e conectam com dureza de busca exaustiva. Argumento: auto-referencia e chave para provar extrema dureza.

**Status:** Diferente do nosso foco (complexidade de provas vs. dureza de SAT). Complementar.

### Resultado I — arXiv:2604.07406 (2026): Indecidiveis de complexidade nondeterministica
Argumenta que a definicao semantica de NP e subjeita a limitacoes godelianas.

**Status:** Argumento filosofico/semantico. Nosso framework fornece formalizacao concreta.

---

## 2. O que PROVAMOS ESTAR REJEITADO / o que permanece em aberto

### ~~Novelidade 1~~ → PROGRAMA (não teorema)
A ponte Beklemishev↔Krajíček **não foi encontrada nas fontes consultadas**;
a alegação de prioridade **permanece provisória** até revisão especializada.

### ~~Novelidade 2: Teorema 4~~ → **REJEITADO (PR12)**
Escala exponencial `s_P ≥ 2^{c|T_α|n}` **sem justificativa** (contagem de provas
não entrega limite inferior; incompletude ≠ dureza computacional).
`|T_α|` ambíguo para ordinais. Enunciado condicional de transferência **aberto**.

### ~~Novelidade 3: Teorema 6~~ → **NÃO PROVADO** (condicional à conjectura de Krajíček)

### ~~Novelidade 4: MCSP~~ → **SKETCH ESPECULATIVO** (03)

### O que permanece (pós-auditoria + núcleo 09)
- **δ, 𝒢, ρ_b, RBT** (definições + Teo. 2, Lema 3, Teo. 4 **no modelo finito**, Lean 0 sorry)
- **PPR / ≼_ppr** (08): R1/R2 provados, R3 aberto
- **Pergunta FP-K** (rebaixada): originalidade não certificada
- **RCS slow-vs-fast** (13/16): confirmada **no modelo estrutural**

---

## 3. Avaliacao honesta (pós-revisão)

| Contribuicao | Novelidade | Status |
|---|---|---|
| Hierarquia ordinal de geradores | CANDIDATA (não certificada) | PROGRAMA |
| Teorema 4 (escala ordinal) | — | **REJEITADO** |
| Teorema 6 (gerador canonico) | — | **NÃO PROVADO** |
| Conexao MCSP | BAIXA (sketch) | ESPECULATIVO |
| Barreira de Interpretabilidade | — | **REJEITADO** (D1) |
| Espectro δ/𝒢 (09, modelo finito) | CANDIDATA | VERIFICADO (Lean) |

**Aviso:** Novidade só se estabelece com busca bibliográfica especializada
e revisão por pares — não com varredura limitada.

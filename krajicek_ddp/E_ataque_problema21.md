# E — Ataque ao Problema 2.1 (Krajíček, arXiv:2506.20221v4)

**Equipe E (lógica de baixa complexidade / análise de ataque).**
Fonte primária: Jan Krajíček, *On NP∩coNP proof complexity generators*,
arXiv:2506.20221v4 (23 Mar 2026), https://arxiv.org/html/2506.20221v4 —
não reconsultada nesta rodada; tudo abaixo deriva de `CONTEXTO_COMUM.md` (itens 11–15)
mais raciocínio próprio.

**Convenção de proveniência (regra 2 da equipe):**
- **(A?)** = extraído do `CONTEXTO_COMUM.md`, ainda **não conferido** no HTML do artigo;
- **(P)** = demonstração / análise própria desta equipe;
- **(C)** = conjectura, ideia de trabalho, especulação explicitada como tal.

---

## 1. Reformulação do problema

### 1.1 Ponto de partida: o Teorema 3 **(A?)**

Seja `M ⊨ T_PV` não-padrão e `φ` uma fórmula proposicional (no sentido do modelo).
Equivalentes:

1. `φ` não tem prova em `M` em nenhum pps;
2. existe extensão `M' ⊇ M` com `M' ⊨ T_PV + (¬φ) ∈ SAT`.

Comentários registrados no artigo **(A?)**: construções com modelos de `S^1_2`
garantem que `M'` preserva propriedades `Σ^b_1(PV)` de elementos de `M` — mas
**usam o esquema BB para fórmulas abertas**; e `Log(M') = Log(M)` pode ser arranjado
via **forcing** ([7] = Krajíček 1995, Thm 9.4.2). Ou seja: **cada ingrediente é
conhecido isoladamente; o que falta é compô-los.**

### 1.2 Enunciado formal do Problema 2.1 **(A?)**

Dados `M ⊨ T_PV` satisfazendo o item (1) do Teorema 3 e `φ` sem prova em `M`,
existem estruturas `L_PV` `M ⊆ M* ⊆ M'` tais que:

- **(i)** `M*` preserva **todas** as propriedades `Σ^b_1(PV)` de elementos de `M`
  (para todo parâmetro `a ∈ M` e toda `Σ^b_1`-fórmula `θ`: `M ⊨ θ(a) ⇒ M* ⊨ θ(a)`);
- **(ii)** `M' ⊨ T_PV + (¬φ) ∈ SAT`;
- **(iii)** `Log(M*) = Log(M')`.

O artigo **assume** resposta afirmativa **(A?)**.

### 1.3 A versão fraca admitida pelo artigo **(A?)** + **(P)**

Basta que `M*` preserve fórmulas da forma

```
∀i ∃y  B(x, i, y)      com i sharply bounded (∀i<t),
                        y bounded, B aberta,
```

com parâmetros `x` de `M`.

**Por que essa versão fraca é a certa para o Teorema 4 (P).** A única sentença de `S`
que o passo (5) da prova do Teorema 4 precisa herdar em `M*` é

```
∀i<m  (¬α_i) ∈ SAT ,
```

que tem **exatamente** o formato `∀i∃y B(x,i,y)` com `i` sharply bounded (índice do
disjunto), `y` bounded (atribuição falsificante) e matriz aberta (`SAT` é `Σ^b_1`,
ou seja, `∃`-matriz aberta). Os parâmetros `α, m, π` pertencem a `M ⊆ M*`. Logo a
versão fraca **cobre** o uso real da preservação. Consequência prática **(P)**:
não atacar (i) em sua plenitude; atacar a versão fraca.

### 1.4 Decomposição útil: o que cada condição realmente exige **(P)**

Analisando o que o passo (5) consome, obtemos uma lista curta de exigências:

| # | Exigência | Natureza lógica | Como obtê-la |
|---|-----------|-----------------|--------------|
| E1 | `M* ⊨ T_PV` | universal | **De graça**: `T_PV` é a teoria universal verdadeira em `L_PV`, e subestrutura de modelo de teoria universal é modelo; logo `M* ⊆ M' ⊨ T_PV` dá `M* ⊨ T_PV`, em particular `M* ⊨ Ref_P` |
| E2 | `M* ⊨ ∀i<m (¬α_i) ∈ SAT` (ou ao menos a instância `i_0`) | `∀i∃y`, matriz aberta | **a tal da preservação fraca** |
| E3 | `σ_{i_0} : P ⊢ α_{i_0}` vale em `M*` | transitivo de cima para baixo **se** escrita na forma `Π` universal (`∀z̃ ¬FalhaPrf`) | transfere de `M'` para `M*` desde que os **parâmetros** `σ_{i_0}, α_{i_0}` estejam em `M*` |
| E4 | os parâmetros usados (`σ`, `i_0`, `α_{i_0}`, e as atribuições) pertencem a `M*` | **membership**, não verdade | exigência de construção (semear `M*` com eles) |
| E5 | `Log(M*) = Log(M')` | conjunto de comprimentos | forcing ([7], Thm 9.4.2) |

Observação-chave **(P)**: `Σ^b_1` (`∃`) transfere **para cima** (`M ⊆ M'`),
sentenças universais `Π` transfere **para baixo** (`M* ⊆ M'`); portanto as duas
transferências "fáceis" já cobrem E1 e E3. O núcleo do problema é **E2 + E4**.

### 1.5 Nota técnica sobre `Log` (ponto a conferir) **(P)/**(A?)**

O item 14 do contexto afirma que no passo (5) "`i_0 ∈ M*` (**mesmos comprimentos**)".
Rigorosamente, `Log(M*) = Log(M')` (igualdade de *conjuntos de comprimentos*) **não**
implica que um elemento *específico* `i_0 ∈ M'` pertença a `M*`: mesma cardinalidade
de níveis não dá pertinência de um indivíduo. Três leituras possíveis:

- **(L1)** `Log` no artigo é mais forte do que "conjunto de comprimentos" (ex.: partes
  canônicas/`Σ^b_1`-definíveis) e aí o passo fecha; **(L2)** `i_0` é `p`-tempo definível
  a partir de parâmetros já em `M*` (`i_0 = f(σ, α)`), de modo que basta `σ ∈ M*`
  (E4); **(L3)** há um argumento comprimido no artigo, não reproduzido no contexto.

**Ação**: conferir no artigo a frase exata de onde se conclui `i_0 ∈ M*`. Este é,
provavelmente, o ponto mais frágil (e mais aproveitável) de toda a cadeia. **(P)**

---

## 2. Por que é difícil

### 2.1 A lacuna exata: (4) `∃x ∀i ∃y_i` vs. (3) `∃x,y ∀i` **(A?)**

Fórmulas de reflexão ausente (`missing reflection`) `τ(g)` têm forma
`γ(p,q) := ⋁_i β_i(p, q^i)` com blocos `q^i` disjuntos. Duas formas aparecem:

- **(3)** — o que é preciso (falsificação de `γ` num modelo):
  `∃x,y ∀i<m ¬A_b(x, i, (y)_i)`;
- **(4)** — o que as construções de [8, 12] entregam:
  `∃x ∀i<m ∃y_i ¬A_b(x, i, y_i)`.

A diferença é **apenas** a permutação `∀i ∃y_i ⟷ ∃y ∀i`: empacotar a família
de testemunhas `y_i` numa única `y` (uma sequência bounded). Para `m` padrão isso é
trivial (escolha finita e concatenação); para `m` **não-padrão** exige um **princípio
de coleção** provável na teoria.

### 2.2 O esquema BB **(A?)**

`BB` = *sharply bounded collection* para **fórmulas abertas**:

```
∀i<m ∃y≤t B(i,y)   ⟹   ∃z ∀i<m B(i, (z)_i)      (B aberta)
```

Trocar (4) por (3) **exige** BB. Sem ela, `M'` construído a partir de um modelo de
`S^1_2` não herda as `Σ^b_1` de `M` em `M*` — a preservação (i) falha exatamente
aqui.

### 2.3 Cook–Thapen: BB não é barato **(A?)** **(P)**

Cook–Thapen (2006, [6] = TOCL 7(4)) mostram que **BB não é provável em `T_PV`**
a menos que **fatoração não seja difícil** (isto é, `BB` provável em `T_PV`
⟹ fatoração fácil). Diagnóstico **(P)**: a afirmação "provar BB em `T_PV`" é,
nessa leitura, *tão forte quanto* um resultado de complexidade que hoje não temos.
Portanto qualquer ataque que passe por "sim, BB vale" **rouba** do problema a
sua força — e é legítimo perguntar se a resposta ao Problema 2.1 não é
condicionalmente "BB-complexidade-Teorema".

### 2.4 Por que acrescentar BB à teoria quebra a análise **(A?)** **(P)**

No passo (2) do Teorema 4 aplica-se o **teorema KPT** (Krajíček–Pudlák–Takeuti,
APAL 52, 1991, [16]) à teoria `S` com os três primeiros axiomas (`T_PV`;
`α = ⋁̇_{i<m} α_i`; `π : P ⊢ α`), para concluir que `S` é consistente. O teorema
KPT vale para **teorias universais**; `T_PV` é a universa verdadeira. Se
adicionarmos `BB` (ou a preservação `Σ^b_1` de cara, formalizada como axioma),
a teoria deixa de ser universal em forma útil e **o KPT não se aplica**
**(A?)**: a conclusão "existe modelo não-padrão `M` de `S`" desaparece.

**Leitura combinada (P):** as duas barreiras são a **mesma** barreira vista por
dois lados. Quem quer preservar `Σ^b_1` (item 1) precisa de BB; quem precisa do
KPT (item 2) precisa que a teoria continue universal. O Problema 2.1 é
precisamente a tentativa de obter o **efeito** de BB numa **extensão** `M*` que
não é axiomatizada por BB — ou seja, de fatorar "teoria que prova BB" em
"`M*` que se comporta *como se* provasse BB, só para os parâmetros de `M`".

---

## 3. Três estratégias de ataque

### 3.(a) Forcing e estruturas pseudofinitas

**Ideia (A?)/(C).** Usar a maquinaria de [7] (Krajíček 1995, Thm 9.4.2: é possível
arranjar `Log(M') = Log(M)` por forcing) somada à técnica de aproximações /
estruturas pseudofinitas de **Ajtai** e ao que [9] (Krajíček, 2016) extraí dessas
construções, para construir `M*` **sem pagar BB**: condições de forcing decidindo
fórmulas `Σ^b_1` sobre parâmetros antigos, com a exigência reduzida a
**preservação de tipos finitos** dos elementos de `M` (cada elemento `a ∈ M`
realiza um tipo `p_a(x)`; exigir que `M*` realize `p_a` é mais fraco e mais
combinatório do que exigir toda `Σ^b_1` sobre `a`).

**O que precisaria ser provado.**
1. Que "realizar o tipo (de certa classe finita/efetiva) de `a`" **implica**
   preservação da classe fraca `∀i∃y B(a,i,y)` — ou, mais fraco ainda, só as
   instâncias do esquema `∀i<m (¬α_i) ∈ SAT`.
2. Que o forcing **não destrói** `M ⊆ M*` como subestrutura `L_PV` (fechamento sob
   funções PV) e que `M* ⊨ T_PV` (isso é livre, por 1.4/E1).
3. Que `Log(M*) = Log(M')` sobrevive à genericidade.

**Obstáculo conhecido (P).** As duas construções conhecidas **não composicionam**:
a de `S^1_2` dá `Σ^b_1` mas usa BB; a de forcing dá `Log` mas não garante `Σ^b_1`.
Pior: decidir `Σ^b_1(a)` para um parâmetro não-padrão `a` em cada condição é
justamente onde a coleta `∀i ∃y_i → ∃y` reaparece — o forcing "esconde" BB dentro
da genericidade. A preservação de tipos finitos só escapa disso se a classe de
tipos exigida for **decidível/efetiva** e pequena.

**Status honesto (P).** Aberto. A variante "só preservar os tipos dos elementos
que **realmente aparecem** na prova do Teorema 4" já é a estratégia (c) — ver
abaixo; a versão "todos os tipos finitos de todos os elementos de `M`" é plausível
mas não está demonstrada e provavelmente **exige mais**, não menos, do que o
problema pede.

---

### 3.(b) Escolher `M` recursivamente saturado no item (2) do Teorema 4

**Ideia (C).** No passo (2) do Teorema 4 escolhemos um modelo `M` de `S`. Em vez de
escolher qualquer modelo, escolher `M` **recursivamente saturado** (o artigo admite
que basta uma classe universal de modelos: contáveis ou recursivamente saturados
**(A?)**), de modo que o axioma

```
∀i<m  (¬α_i) ∈ SAT
```

seja **herdado por `M*` sem preservação `Σ^b_1` geral**: a saturação fornece
testemunhas para todo tipo finito consistente com os dados, e o axioma é uma
única sentença com parâmetros `α, m ∈ M`.

**O que precisaria ser provado.**
1. Uma lemma de **herança**: se `M` é recursivamente saturado e `M ⊆ M* ⊆ M'`
   com `M' ⊨ T_PV`, então `M*` satisfaz o esquema — **ou** pelo menos `M*` satisfaz
   todas as suas instâncias com índice em `M*`.
2. Variantes que dispensam saturação:
   - **(b')** arranjar a extensão **sem novos elementos abaixo de `m`**:
     `M* ∩ m = M ∩ m`. Então toda instância `i < m` é antiga e sua testemunha já
     está em `M ⊆ M*` — BB é contornado por *fechamento*, não por teoria;
   - **(b'')** semear `M*` com as testemunhas de `α_i` para os poucos `i` novos.

**Obstáculo conhecido (P).** Saturação de `M` é propriedade de `M`, mas `M*` é
construída **depois** e pode acrescentar `i < m` inexistentes em `M`; tipos
realizados em `M` não cobrem índices novos. I.e. a saturação sozinha não fecha o
buraco `∀i ∃y_i` quando o domínio cresce. A variante (b') é a única que ataca a
causa (domínio crescente), e ela conflita **possivelmente** com `Log(M*) = Log(M')`
se `m` for grande o suficiente para exigir comprimentos novos em `M*`.

**Status honesto (P).** Conjectura promissora e **testável**: (b') é um enunciado
matemático preciso, sem quantificadores sobre estruturas infinitas além de uma
igualdade de domínios recortados. Se (b') for provável sob as hipóteses do
Teorema 4, o Problema 2.1 é resolvido *para o uso que dele se faz*.

---

### 3.(c) Relaxar `Log(M*) = Log(M')` para "mesmos comprimentos dos elementos envolvidos `(π, α, z)`"

**Ideia (P).** A igualdade global de `Log` é uma exigência **infinita**; mas a prova
do Teorema 4 só usa **finitos** elementos de `M'`. Trocá-la por

```
M* e M' contêm elementos dos mesmos comprimentos para a lista finita
L = (π, α, m, σ, i_0, α_{i_0}, provas e atribuições envolvidas),
```

transforma (iii) numa condição **finita/combinatória**: `|e| ∈ Log(M*)` para cada
`e ∈ L`, ou melhor, `e ∈ M*` para cada `e` da lista (ver 1.5 — "mesmos comprimentos"
precisa ser lido como "os elementos envolvidos estão em `M*`", não apenas "há
elementos de mesma medida").

**O que precisaria ser provado.**
1. **Lema de suficiência finita**: reescrever o passo (5) do Teorema 4 usando
   apenas E1–E5 da tabela 1.4, e observar que E1 e E3 são gratuitas (universal ↑↓),
   E2 é a preservação fraca e E4 é a lista finita. Conclusão: **a versão fraca
   bastaria** para a prova do Teorema 4.
2. Que E4 é realizável: dar `M*` contendo `σ` (com `|σ| = |φ|` ou `≤ |φ|^c` por
   p-boundedness) e fechar sob funções PV para obter `i_0, α_{i_0}` — fechamento é
   barato (subestrutura).
3. Que a condição finita de comprimentos convive com `M* ⊆ M'` e com o forcing de
   [7] (que *já* arranja `Log` igual; exigir só uma parte finita é mais fraco, logo
   herda-se o resultado, **desde** que o forcing possa ser restrito a uma lista de
   medidas finita — trivial se a construção for "medida a medida").

**Obstáculo conhecido (P).** (α) Se `Log` for só o conjunto de *medidas*, o lema de
suficiência falha em E4 (indivíduos vs. níveis) — ver 1.5; é preciso mostrar que o
artigo (ou a versão relaxada) exige membership, não medida. (β) Pode haver um
elemento de `L` que só existe em `M'` *por causa* da extensão que satisfez
`¬φ ∈ SAT`, e cuja inclusão em `M*` seja **incompatível** com `M*` satisfazer
`T_PV + ` a negação de algo — ou seja: semear `M*` com `σ` pode forçar `M*` a
verificar `¬φ ∈ SAT`, o que é justamente E2 aplicada a `φ`. Se `M` já satisfaz
`¬φ ∈ SAT`, isso é de graça (preservação fraca com parâmetro `φ`); se não, é o
verdadeiro ponto duro.

**Status honesto (P).** **Mais promissora das três.** Não resolve o Problema 2.1
em sua plenitude, mas resolve a *pergunta que o artigo precisa* — se o lema de
suficiência finita for escrito e conferido, o Problema 2.1 pode ser reformulado
publicamente numa versão finita, atacável por combinatoria clássica.

---

## 4. Possível refutação: a hipótese é "forte demais"?

### 4.1 O que o artigo afirma **(A?)**

Resposta **negativa** ao Problema 2.1 ⟹ `P ≠ NP` (rodapé 2 do artigo).

### 4.2 Análise das duas direções **(P)**

| Direção | Consequência | Custo de ataque |
|---|---|---|
| **Afirmação** (assumida pelo artigo) + (ST) | `NP ≠ coNP` (Teorema 4) | exige construir `M*` — ver §3 |
| **Negação** | `P ≠ NP` | exige refutar a construção de `M*` **para todo** `M, φ` |

Comentários:

1. **A hipótese afirmativa é "forte mas não descabida" (C).** Os dois ingredientes
   (preservação `Σ^b_1` via `S^1_2`; `Log` via forcing) já existem; falta a
   composição. Hipóteses estruturais sobre modelos não-padrão costumam ser mais
   baratas que separações de complexidade.
2. **A negação é estruturalmente cara (P).** Uma negativa *incondicional* daria
   `P ≠ NP`. Nota: do ponto de vista *condicional*, a consequência é quase
   desinteressante — **(P)** lembre-se de que `OWF` (funções unidirecionais)
   ⟹ `P ≠ NP` é elementar (com `P = NP`, busca em `NP` reduz-se a decisão via
   auto-redução, e `∃x f(x)=y` está em `NP`). Portanto uma refutação *condicional
   a OWF* do Problema 2.1 **não** traria consequência de complexidade nova — só
   traria informação sobre modelos não-padrão, o que continua sendo um resultado
   legítimo, mas bem mais modesto.
3. **Assimetria de valor (P).** A rota afirmativa transforma uma hipótese de
   prova-complexidade plausível ((ST), permutações *one-way* fortes) numa
   separação `NP ≠ coNP` — o "grande prêmio" acessível desta área. A rota negativa
   exige bater de frente com `P` vs `NP`. **Consequência metodológica**: não atacar
   o Problema 2.1 *buscando refutação*; atacá-lo buscando a versão finita (§3c),
   que é "afirmativa por construção".
4. **Possível via intermediária (C).** Uma refutação *relativizada* (oracle `A` com
   `M^A, φ^A` sem `M*`) seria informativa: diria que qualquer prova afirmativa
   precisa usar essencialmente não-relativização (força do `T_PV` verdadeiro /
   de `Log`). Se uma refutação relativizada existir, é forte evidência *contra*
   a plausibilidade ingênua da hipótese.

---

## 5. Síntese: subproblemas, status e plano

### 5.1 Lista de subproblemas

| # | Subproblema | Tipo | Status |
|---|-------------|------|--------|
| S1 | Conferir no artigo a justificativa de `i_0 ∈ M*` e a definição exata de `Log` | leitura | **não feito** — prioridade 1 |
| S2 | Escrever o **lema de suficiência finita** (E1–E5 ⟹ passo (5) do Teorema 4) | prova | **aberto, mais promissor** |
| S3 | Provar que a versão fraca `∀i∃y B` de (i) implica S2 | prova | provavelmente direto (o axioma de `S` já tem esse formato) |
| S4 | `(b')`: extensão com `M* ∩ m = M ∩ m` compatível com `Log` igual | prova/conj. | **conj. (C)**, precisa de teste |
| S5 | Compor forcing (`Log`) com construção `S^1_2` (`Σ^b_1`) sem BB | prova | **aberto, cerne do problema** |
| S6 | Entender exatamente onde Cook–Thapen (`BB ⟹` fatoração fácil) entra: BB é necessária ou só suficiente? | análise | aberto |
| S7 | Refutação relativizada do Problema 2.1 | construção | não explorado |
| S8 | Verificar [9] (Krajíček 2016) e rodapé 2 no artigo | leitura | **não feito** (marcado **(A?)**) |

### 5.2 O mais promissor

**S2 + S3 (a versão finita, §3c)**: é o único caminho que *reduz* a exigência
infinita a uma quantidade finita de dados e, ao mesmo tempo, é exatamente o que o
Teorema 4 consome. Mesmo que S5 permaneça aberto, S2+S3 reformulam o Problema 2.1
numa pergunta atacável.

### 5.3 Plano de 3 passos

1. **Passo 1 (leitura + formalização finita, ~1 rodada).** Conferir no HTML do
   artigo: (a) frase exata de onde sai `i_0 ∈ M*`; (b) definição de `Log`;
   (c) rodapé 2; (d) entrada [9]. Em paralelo, escrever S2 como um lema numerado
   E1–E5, explicitando quais transferências são gratuitas (`Σ^b_1` ↑, `Π` ↓,
   subestrutura de teoria universal).
2. **Passo 2 (o ataque, ~1–2 rodadas).** Tentar **S4** (`M* ∩ m = M ∩ m`): se
   verdadeiro, E2 é satisfeito trivialmente (testemunhas antigas) e BB desaparece.
   Testar contra o obstáculo `Log` (medidas novas exigidas por `M*` perto de `m`);
   se S4 falhar, cair para a versão "semear `M*` com `σ` e fechar sob funções PV"
   (E4) e verificar se isso colide com `¬φ ∈ SAT` em `M*`.
3. **Passo 3 (validação, ~1 rodada).** Registrar tudo sob as marcas (A?)/(P)/(C);
   se S2+S4/S4' fecharem, redigir o enunciado da **versão finita** do Problema 2.1
   como correção/enriquecimento do artigo, e só então discutir consequências
   (Teorema 4 preservado; eventual refutação relativizada, S7).

### 5.4 Riscos principais **(P)**

- **R1**: S2 pode esbarrar no fato de que "mesmos comprimentos" ≠ "mesmos
  elementos" (S1) — daí a prioridade da leitura.
- **R2**: toda variante que exige `M* ⊨ (¬φ) ∈ SAT` pode ser equivalente a BB em
  disfarce (S6): checar sempre se a construção "esconde" coleta.
- **R3**: o artigo **assume** a resposta afirmativa; qualquer "solução" que só
  reprove a hipótese em casos particulais não resolve 2.1 — mas resolve o
  *Teorema 4 para esse caso*, o que já seria publicável se o lema de suficiência
  (S2) for novo.

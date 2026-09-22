# 08 — PROGRAMA: INTERPRETABILIDADE vs. GERADORES
## Definição formal de \(\preceq_{\mathrm{ppr}}\), caso \(T_0=PA\), \(T_1=PA+\mathrm{RFN}(PA)\) e tentativa de prova/refutação

**Projeto:** IA-research-Godel-e-Krajicek  
**Autor:** Euzebio Soares  
**Data:** 22/09/2026  
**Status:** programa matemático em investigação — nenhum resultado novo abaixo é declarado como teorema sem prova completa.

---

## 0. Objetivo

A pergunta central desta etapa é:

\[
\boxed{
T\preceq_{\mathrm{int}}S
\quad\stackrel{?}{\Longrightarrow}\quad
g_T\preceq_{\mathrm{ppr}} g_S
}
\]

onde:

- \(T\preceq_{\mathrm{int}}S\) é uma relação adequada de interpretabilidade entre teorias aritméticas;
- \(g_T\) é o gerador de Krajíček associado a \(T\);
- \(\preceq_{\mathrm{ppr}}\) será uma nova relação operacional, explicitamente definida abaixo, baseada em **range-avoidance tautologies** e transformação polinomial de provas.

O primeiro caso concreto é:

\[
T_0=PA,
\qquad
T_1=PA+\mathrm{RFN}(PA).
\]

A meta desta etapa não é presumir a implicação. É tentar:

1. prová-la sob hipóteses mínimas;
2. descobrir exatamente onde a prova quebra;
3. procurar um contraexemplo;
4. classificar o resultado como teorema, refutação, implicação condicional ou problema aberto.

---

# 1. Correção preliminar: qual é a tautologia associada a um gerador?

Há uma correção importante ao formalismo atual do repositório.

O objeto padrão na teoria de proof complexity generators não é, em geral,

\[
\bigwedge_{x\in\{0,1\}^n}[C_n(x)=g(x)].
\]

Essa expressão é uma afirmação de **correção do circuito que calcula o próprio gerador** e, tomada literalmente, não é a família padrão de tautologias usada para medir hardness do gerador.

Na literatura de Krajíček, para

\[
g_n:\{0,1\}^n\to\{0,1\}^{m(n)},\qquad m(n)>n,
\]

e para cada

\[
b\in\{0,1\}^{m(n)}\setminus\operatorname{rng}(g_n),
\]

usa-se uma \(\tau\)-fórmula

\[
\boxed{\tau(g_n)_b}
\]

que expressa proposicionalmente:

\[
\boxed{
b\notin\operatorname{rng}(g_n)
}
\]

ou, equivalentemente,

\[
\forall x\in\{0,1\}^n,\qquad g_n(x)\neq b.
\]

Krajíček define a família exatamente dessa forma e define a hardness do gerador por meio das \(\tau(g)_b\), para \(b\) fora da imagem. citeturn128981search0turn151226search59

Portanto, daqui em diante:

\[
\boxed{
\mathcal T(g)
=
\left\{
\tau(g_n)_b:
n\ge 1,\;
b\notin\operatorname{rng}(g_n)
\right\}.
}
\]

Essa correção é necessária para que a nova relação \(\preceq_{\mathrm{ppr}}\) seja compatível com a literatura de proof complexity generators.

---

# 2. Geradores \(g_T\) de Krajíček

Para uma teoria \(T\) suficientemente forte, sound e p-time no sentido utilizado por Krajíček, o gerador \(g_T\) é construído assim, em linhas gerais:

- recebe \(u\in\{0,1\}^n\);
- procura um código inicial de fórmula \(\Phi\) de tamanho no máximo \(\log n\);
- considera os padrões \(w\) de tamanho \(O(\log n)\);
- procura \(T\)-provas de comprimento no máximo \(\log n\) para certas sentenças \(\Phi^w\);
- escolhe o primeiro \(w_0\) para o qual tal prova não é encontrada;
- produz uma saída de comprimento \(n+1\).

Krajíček prova que o algoritmo é p-time, que há stretch de um bit e que o complemento da imagem é infinito. A construção usa \(S^1_2\) como teoria-base e requer as propriedades de soundness e p-time formalization usadas no artigo. citeturn655306view0

A questão de saber se algum \(g_T\) é hard para todos os sistemas de prova permanece aberta na formulação de Krajíček. citeturn655306view0turn565792search0

---

# 3. Hipóteses exatas para \(T_0\) e \(T_1\)

## 3.1 \(T_0=PA\)

Temos:

\[
S^1_2\subseteq PA.
\]

Logo \(PA\) possui a força sintática necessária para a construção de \(g_T\).

Também é uma teoria efetivamente axiomatizável.

A utilização de \(g_{PA}\) como gerador correto exige a soundness de \(PA\) no modelo padrão. Esta é uma hipótese metamatemática; não deve ser confundida com um fato provado dentro de PA.

---

## 3.2 \(T_1=PA+\mathrm{RFN}(PA)\)

Aqui é essencial distinguir:

\[
\mathrm{RFN}_\Gamma(PA)
\]

de uma reflexão uniforme sem especificação de classe \(\Gamma\).

Uma versão formal deve fixar a classe de fórmulas e a codificação da reflexão. Em termos esquemáticos:

\[
\mathrm{RFN}_\Gamma(PA)
=
\left\{
\forall \vec x
\left(
\operatorname{Pr}_{PA}(\ulcorner\varphi(\dot{\vec x})\urcorner)
\rightarrow
\varphi(\vec x)
\right):
\varphi\in\Gamma
\right\}.
\]

Não é aceitável escrever simplesmente um predicado externo `True(x)` como se fosse uma fórmula aritmética comum.

Beklemishev trabalha precisamente com versões restritas e uniformes de reflexão, e mostra resultados de equivalência e análise ordinal dependentes da classe de reflexão escolhida. citeturn880383academia1turn565792search34

Neste documento, \(T_1\) significa:

\[
\boxed{
T_1=PA+\mathrm{RFN}_{\Gamma}(PA)
}
\]

com \(\Gamma\) fixada em toda a argumentação.

Quando não for relevante qual classe específica está sendo usada, escreveremos apenas \(\mathrm{RFN}(PA)\).

---

# 4. A relação de interpretabilidade

A notação do repositório atual,

\[
T\preceq_{\mathrm{int}}S,
\]

precisa de uma definição mais precisa.

Para esta etapa, usaremos a relação semântica padrão:

\[
\boxed{
T\preceq_{\mathrm{int}}S
}
\]

quando existe uma interpretação aritmética \(I\) de \(T\) em \(S\).

No caso particular em estudo:

\[
T_0=PA\subseteq T_1,
\]

portanto a inclusão fornece imediatamente uma interpretação trivial de \(PA\) em \(T_1\).

Assim:

\[
\boxed{
T_0\preceq_{\mathrm{int}}T_1.
}
\]

Isso é a parte fácil.

O problema real começa ao passar de teorias para geradores proposicionais.

---

# 5. Definição formal de \(\preceq_{\mathrm{ppr}}\)

A relação proposta aqui será explicitamente uma relação entre **famílias de geradores e suas \(\tau\)-fórmulas**, e não simplesmente entre funções.

## 5.1 Prova em um sistema de prova

Seja \(P\) um sistema de prova proposicional no sentido de Cook–Reckhow.

Para uma tautologia \(\varphi\),

\[
s_P(\varphi)
=
\min\{|\pi|:P(\pi,\varphi)\}.
\]

Um sistema de prova é p-time verificável por definição. Essa é a base padrão da teoria de Cook–Reckhow. citeturn565792search0turn128981search24

---

## 5.2 Dados de uma instância de gerador

Para \(g\), uma instância é um par:

\[
(n,b)
\]

com

\[
b\notin\operatorname{rng}(g_n).
\]

A fórmula associada é

\[
\tau(g_n)_b.
\]

---

## 5.3 Definição

Fixe um sistema de prova \(P\).

Dizemos que

\[
\boxed{
g\preceq_{\mathrm{ppr}}^P h
}
\]

quando existem:

- um polinômio \(p\);
- uma função total p-time
  \[
  R:\{(n,b)\}\to\{(m,\beta)\};
  \]
- uma função total p-time de tradução de provas
  \[
  \Theta;
  \]

tais que, para todo \(n\) e todo

\[
b\notin\operatorname{rng}(g_n),
\]

valem:

### (PPR-1) crescimento de tamanho controlado

Se

\[
R(n,b)=(m,\beta),
\]

então

\[
m\le p(n)
\]

e

\[
|\beta|\le p(n+|b|).
\]

### (PPR-2) preservação semântica da range-avoidance

\[
b\notin\operatorname{rng}(g_n)
\Longrightarrow
\beta\notin\operatorname{rng}(h_m).
\]

Logo:

\[
\tau(g_n)_b,\quad \tau(h_m)_\beta
\in\mathrm{TAUT}.
\]

### (PPR-3) tradução de provas

Para toda prova \(P\)-válida

\[
P(\pi,\tau(h_m)_\beta),
\]

temos

\[
P\left(
\Theta(n,b,\pi),
\tau(g_n)_b
\right),
\]

e existe polinômio \(q\) tal que

\[
\boxed{
|\Theta(n,b,\pi)|
\le
q\!\left(
n+|b|+|\pi|
\right).
}
\]

Essa é a propriedade que justifica o nome:

\[
\boxed{\text{proof-preserving reduction}}
\]

ou **PPR**.

---

# 6. Variante mais forte: equivalência de tautologicidade

Para alguns resultados será útil exigir:

\[
\boxed{
b\in\operatorname{rng}(g_n)
\iff
\beta\in\operatorname{rng}(h_m).
}
\]

Equivalente:

\[
\tau(g_n)_b\in\mathrm{TAUT}
\iff
\tau(h_m)_\beta\in\mathrm{TAUT}.
\]

Chamaremos isto de

\[
g\preceq_{\mathrm{bppr}}^P h
\]

(**bidirectional semantic PPR**).

A definição principal do programa continuará sendo \(\preceq_{\mathrm{ppr}}\), que só exige a direção necessária à transferência de provas.

---

# 7. Lemas elementares sobre \(\preceq_{\mathrm{ppr}}^P\)

## Lema 7.1 — reflexividade

Para todo gerador \(g\),

\[
g\preceq_{\mathrm{ppr}}^P g.
\]

### Prova

Tome:

\[
R(n,b)=(n,b)
\]

e

\[
\Theta(\pi)=\pi.
\]

Todos os três requisitos são imediatos.

\[
\boxed{\square}
\]

---

## Lema 7.2 — transitividade

Se

\[
g\preceq_{\mathrm{ppr}}^P h
\]

e

\[
h\preceq_{\mathrm{ppr}}^P k,
\]

então

\[
g\preceq_{\mathrm{ppr}}^P k.
\]

### Prova

Componha:

\[
R_{g\to h}
\quad\text{e}\quad
R_{h\to k}
\]

e, para provas,

\[
\Theta_{g\leftarrow h}
\circ
\Theta_{h\leftarrow k}.
\]

A composição de funções p-time é p-time, e a composição de polinômios é polinomial.

\[
\boxed{\square}
\]

Portanto, para \(P\) fixo,

\[
\boxed{
\preceq_{\mathrm{ppr}}^P
\text{ é uma pré-ordem.}
}
\]

---

# 8. Consequência fundamental para hardness

## Proposição 8.1

Se

\[
g\preceq_{\mathrm{ppr}}^P h
\]

e a família \(\mathcal T(h)\) possui provas \(P\) de tamanho polinomial para todos os seus elementos, então \(\mathcal T(g)\) também possui provas \(P\) de tamanho polinomial.

### Demonstração

Para cada

\[
\tau(g_n)_b,
\]

a redução produz

\[
\tau(h_m)_\beta
\]

com

\[
m,|\beta|\le\operatorname{poly}(n).
\]

Se a segunda possui prova

\[
|\pi|\le m^c,
\]

então PPR-3 produz prova da primeira com comprimento

\[
\le q(n+|b|+m^c)
=
\operatorname{poly}(n).
\]

\[
\boxed{\square}
\]

---

## Corolário 8.2

Pela contraposição:

\[
\boxed{
g\text{ é hard para }P
\Longrightarrow
h\text{ é hard para }P
}
\]

sempre que

\[
g\preceq_{\mathrm{ppr}}^P h.
\]

Essa é exatamente a direção que torna a relação útil para o projeto.

---

# 9. Tentativa de provar a implicação para \(T_0\) e \(T_1\)

Queremos:

\[
\boxed{
PA\preceq_{\mathrm{int}}
PA+\mathrm{RFN}(PA)
}
\]

e tentar concluir

\[
\boxed{
g_{PA}
\preceq_{\mathrm{ppr}}
g_{PA+\mathrm{RFN}(PA)}.
}
\]

A primeira afirmação é verdadeira.

A segunda não decorre automaticamente.

---

# 10. Por que a inclusão \(T_0\subseteq T_1\) não basta?

A construção de \(g_T\) depende da pergunta:

> existe uma \(T\)-prova curta da sentença \(\Phi^w\)?

Escrevendo:

\[
A_T(n,\Phi,w)
\equiv
\exists\pi
\left(
|\pi|\le\log n
\land
\operatorname{Proof}_T(\pi,\Phi^w)
\right).
\]

Como

\[
PA\subseteq PA+\mathrm{RFN}(PA),
\]

temos a monotonicidade local:

\[
A_{T_0}(n,\Phi,w)
\Longrightarrow
A_{T_1}(n,\Phi,w).
\]

Portanto:

\[
\boxed{
\operatorname{Proof}_{T_0}^{\le\log n}
\subseteq
\operatorname{Proof}_{T_1}^{\le\log n}.
}
\]

Isto é verdadeiro.

---

# 11. Mas o que acontece com o bit \(w_0\)?

O gerador escolhe o primeiro \(w\) sem prova curta.

Defina:

\[
w_0^T(n,\Phi)
=
\min_{\mathrm{lex}}
\{w:
\neg A_T(n,\Phi,w)\}.
\]

Como \(A_{T_0}\Rightarrow A_{T_1}\), temos:

\[
\{w:A_{T_1}(n,\Phi,w)\}
\supseteq
\{w:A_{T_0}(n,\Phi,w)\}.
\]

Logo, quando ambas as coleções de provas deixam algum \(w\) sem prova,

\[
\boxed{
w_0^{T_1}(n,\Phi)
\ge_{\mathrm{lex}}
w_0^{T_0}(n,\Phi).
}
\]

Esta desigualdade local é um resultado real.

### Porém:

\[
w_0^{T_1}
\ge_{\mathrm{lex}}
w_0^{T_0}
\]

**não fornece uma função p-time**

\[
w_0^{T_0}
=
F(w_0^{T_1})
\]

nem produz automaticamente uma relação entre as imagens de \(g_{T_0}\) e \(g_{T_1}\).

Esse é o primeiro ponto onde a prova da implicação quebra.

---

# 12. O bloqueio estrutural

A construção de \(g_T\) não é monotônica como uma função de \(T\).

Ela é monotônica apenas no **predicado auxiliar de existência de prova curta**:

\[
A_{T_0}\Rightarrow A_{T_1}.
\]

A função final envolve uma operação de mínimo lexicográfico:

\[
g_T(u)
=
w_0^T u_0.
\]

A operação

\[
A_T
\mapsto
\min\{w:\neg A_T(w)\}
\]

não é uma operação que preserve uma relação de redução eficiente entre os predicados.

Formalmente:

\[
A\subseteq B
\]

não implica, em geral, a existência de função p-time

\[
\min(\overline A)
\le_p
\min(\overline B).
\]

Portanto a inclusão de teorias não é suficiente.

---

# 13. Por que não podemos simplesmente usar a reflexão

Uma tentativa natural seria:

\[
PA+\mathrm{RFN}(PA)
\]

“conhece” a correção das provas de PA.

Talvez, portanto, um raciocínio em \(T_1\) possa ser convertido em algo que \(g_{PA}\) reconheça.

Mas isso exigiria uma transformação:

\[
\pi_{T_1}
\longmapsto
\pi_{PA}
\]

para as sentenças relevantes.

Isso é impossível em geral se a sentença for genuinamente nova para \(PA\).

Por exemplo, sob hipóteses usuais de consistência/soundness,

\[
T_1\vdash \mathrm{Con}(PA)
\]

enquanto

\[
PA\nvdash\mathrm{Con}(PA).
\]

Logo não existe uma transformação geral que elimine \(\mathrm{RFN}(PA)\) e conserve a prova dentro de PA.

O máximo que podemos esperar é uma **tradução proposicional local para a família específica \(\tau(g_T)\)**, com controle quantitativo de tamanho.

Essa é precisamente a parte que ainda precisa ser demonstrada.

---

# 14. Tentativa de produzir PPR por simulação

Uma segunda estratégia:

1. tomar uma prova de
   \[
   \tau(g_1)_\beta;
   \]
2. interpretar a prova na teoria \(T_1\);
3. eliminar as instâncias de reflexão;
4. obter uma prova de
   \[
   \tau(g_0)_b.
   \]

Problema:

\[
\text{interpretação aritmética}
\neq
\text{p-simulação proposicional}.
\]

Krajíček enfatiza que relações entre sistemas de prova, reflexão e simulações precisam de construções proposicionais explícitas; reflexão é uma das formas clássicas de obter simulações, mas isso não fornece automaticamente uma tradução entre os \(\tau\)-tautologies de dois geradores diferentes. citeturn128981search24turn128981search26

Portanto esta tentativa também falha como prova geral.

---

# 15. Tentativa de refutação

A alternativa seria provar:

\[
g_{PA}
\npreceq_{\mathrm{ppr}}
g_{PA+\mathrm{RFN}(PA)}.
\]

Também não conseguimos provar isso com as ferramentas disponíveis.

Por quê?

Porque uma não-reduzibilidade PPR suficientemente geral já exige uma separação proposicional quantitativa entre duas famílias de tautologias.

Isso se aproxima da fronteira de problemas abertos de proof complexity.

A própria teoria de Krajíček trata como problema fundamental encontrar geradores hard para sistemas fortes e, em particular, um gerador hard para todos os sistemas. citeturn565792search0turn128981search0

Logo uma refutação incondicional forte seria, por si só, um resultado importante de complexidade de provas.

---

# 16. Resultado intermediário rigoroso

Podemos, entretanto, separar três afirmações:

### R1 — verdadeiro

\[
\boxed{
T_0\subseteq T_1
\Longrightarrow
A_{T_0}\subseteq A_{T_1}.
}
\]

### R2 — verdadeiro condicionalmente no ponto de saída

Sempre que a construção produz ambos os mínimos,

\[
\boxed{
w_0^{T_1}\ge_{\mathrm{lex}} w_0^{T_0}.
}
\]

### R3 — não demonstrado

\[
\boxed{
A_{T_0}\subseteq A_{T_1}
\Longrightarrow
g_{T_0}\preceq_{\mathrm{ppr}}g_{T_1}.
}
\]

Portanto:

\[
\boxed{
\text{monotonicidade do predicado de prova}
\not\Rightarrow
\text{monotonicidade PPR do gerador}.
}
\]

Essa distinção é o primeiro resultado estrutural relevante do novo programa.

---

# 17. Formulação do problema aberto correto

Em vez do enunciado antigo:

> interpretabilidade implica aumento de dureza;

formulamos:

## Problema PPR-Reflection-1

Sejam

\[
T_0=PA,
\qquad
T_1=PA+\mathrm{RFN}_\Gamma(PA).
\]

Pergunta:

\[
\boxed{
g_{T_0}
\preceq_{\mathrm{ppr}}^P
g_{T_1}\;?
}
\]

para um sistema de prova \(P\) fixado.

Depois:

\[
\boxed{
g_{T_0}
\preceq_{\mathrm{ppr}}
g_{T_1}\;?
}
\]

em uma noção uniforme sobre uma classe de sistemas de prova.

---

# 18. Uma versão ainda mais forte e potencialmente interessante

Podemos perguntar se a altura de reflexão é refletida por uma pré-ordem operacional.

Considere:

\[
T_0=PA,
\]

\[
T_1=PA+\mathrm{RFN}(PA),
\]

\[
T_2=T_1+\mathrm{RFN}(T_1),
\]

etc.

Defina:

\[
T_\alpha\preceq_{\mathrm{gen}}T_\beta
\]

quando

\[
g_{T_\alpha}
\preceq_{\mathrm{ppr}}
g_{T_\beta}.
\]

A questão geral torna-se:

\[
\boxed{
\alpha<\beta
\quad\stackrel{?}{\Longrightarrow}\quad
T_\alpha\preceq_{\mathrm{gen}}T_\beta.
}
\]

Isso é uma reformulação muito mais precisa da antiga “escala ordinal da dureza”.

Não assumimos que seja verdadeira.

---

# 19. Uma possibilidade de contraexemplo estrutural

Há uma razão para levar a sério a possibilidade de falha.

A hierarquia de reflexão controla uma noção de força aritmética:

\[
T_0
<
T_1
<
T_2
<
\cdots
\]

sob relações proof-theoretic apropriadas.

Mas o gerador \(g_T\) contém uma escolha adicional:

\[
\boxed{
\text{ordenação lexicográfica + limite de prova + codificação sintática}.
}
\]

Essas escolhas podem produzir efeitos que não são invariantes sob interpretabilidade.

Portanto pode existir:

\[
T\preceq_{\mathrm{int}}S
\]

mas

\[
g_T\npreceq_{\mathrm{ppr}}g_S.
\]

Não temos um exemplo concreto ainda.

Mas a possibilidade não é descartável.

---

# 20. Conexão com a literatura de Krajíček

A teoria contemporânea de proof complexity generators já introduz uma diferença importante entre:

1. hardness para um sistema \(P\);
2. search-hardness;
3. \(\bigvee\)-hardness / W-hardness;
4. condições de pseudo-surjectividade.

Krajíček mostrou que essas propriedades se relacionam com proof search, bounded arithmetic, circuit complexity e determinadas classes de geradores. citeturn565792search0turn151226search0

O trabalho de 2026 sobre \(NP\cap coNP\) generators reforça que a análise de geradores está ligada a problemas de busca \(\Sigma^p_2\), modelos student–teacher e hipóteses criptográficas; portanto é importante não reduzir a teoria a uma única noção de “tamanho da prova”. citeturn741325academia24turn151226search58

Isso sugere uma extensão natural do nosso programa:

\[
\preceq_{\mathrm{ppr}}
\quad\longrightarrow\quad
\preceq_{\mathrm{search}}
\quad\longrightarrow\quad
\preceq_{\vee}.
\]

---

# 21. Relação com reflection principles e jump operators

Há uma linha da literatura que trata diretamente da produção de um sistema de prova mais forte \(Q\) a partir de \(P\), com a propriedade de que certas reflection principles de \(Q\) não têm provas polinomiais em \(P\).

Isso é estudado na teoria de **jump operators**. O trabalho de FOCS 2024 descreve exatamente esse tipo de procedimento: dado \(P\), construir \(Q\) mais forte de modo que \(P\) não simule \(Q\) eficientemente. citeturn128981search26

Isso é relevante porque oferece uma alternativa ao nosso caminho:

Em vez de

\[
T_0\to T_1\to g_{T_0}\to g_{T_1},
\]

poderíamos estudar

\[
P\to J(P)
\]

e comparar:

\[
\tau(g_{T_0})
\quad\text{com}\quad
\mathrm{RFN}(J(P)).
\]

Talvez a conexão correta não seja

\[
\text{teoria}\to\text{gerador},
\]

mas

\[
\boxed{
\text{reflexão}
\to
\text{jump proposicional}
\to
\text{gerador}.
}
\]

Esta é uma direção concreta para a segunda fase.

---

# 22. Relação com slow consistency

O programa de slow consistency mostra que pequenas alterações na forma como a consistência é iterada podem mudar drasticamente a viabilidade de provas.

Freund–Pakhomov obtiveram provas polinomiais em PA para determinadas afirmações de slow consistency, apesar de que a progressão “rápida” correspondente apresenta comportamento diferente. citeturn880383academia0

Isso dá uma motivação forte para estudar uma versão:

\[
g_{T^{\mathrm{slow}}_1}
\]

versus

\[
g_{T^{\mathrm{fast}}_1}.
\]

A pergunta é:

\[
\boxed{
T^{\mathrm{slow}}_1
\preceq_{\mathrm{int}}
T^{\mathrm{fast}}_1
\quad\text{implica alguma relação PPR?}
}
\]

Novamente, isso é problema aberto nesta formulação.

---

# 23. Resultado negativo sobre o antigo Teorema 3.3 do repositório

O repositório afirma, em essência:

\[
P\text{ prova }TG_\beta^n\text{ em tamanho polinomial}
\Longrightarrow
P\text{ prova }TG_\alpha^n
\]

porque \(T_\alpha\) é mais fraca que \(T_\beta\). citeturn382456view0

A auditoria atual permite afirmar de modo mais preciso:

\[
\boxed{
\text{isso não segue da interpretação apenas.}
}
\]

Para torná-lo verdadeiro é necessário um lema separado do tipo:

\[
T_\alpha\preceq_{\mathrm{int}}T_\beta
\Longrightarrow
g_{T_\alpha}
\preceq_{\mathrm{ppr}}g_{T_\beta}.
\]

E justamente esse lema é o objeto do presente programa.

Assim, a antiga “prova” circular:

\[
\text{Teorema 3.3}
\Rightarrow
\text{monotonicidade de geradores}
\]

não pode ser usada para provar o próprio Teorema PPR.

---

# 24. O que já podemos afirmar sobre \(T_0,T_1\)

Sob as hipóteses metamatemáticas de soundness apropriadas:

\[
\boxed{
T_0=PA
}
\]

e

\[
\boxed{
T_1=PA+\mathrm{RFN}_\Gamma(PA)
}
\]

são candidatos legítimos à construção de \(g_T\).

Além disso:

\[
T_0\subseteq T_1
\]

e, portanto:

\[
T_0\preceq_{\mathrm{int}}T_1.
\]

Também temos a inclusão dos predicados de prova curta:

\[
A_{T_0}\subseteq A_{T_1}.
\]

E, no caso em que os mínimos são definidos:

\[
w_0^{T_1}\ge_{\mathrm{lex}}w_0^{T_0}.
\]

**Não temos ainda:**

\[
g_{T_0}\preceq_{\mathrm{ppr}}g_{T_1}.
\]

---

# 25. Classificação rigorosa do resultado desta etapa

| Afirmação | Estado |
|---|---|
| \(PA\subseteq PA+\mathrm{RFN}(PA)\) | PROVADO |
| \(T_0\preceq_{\mathrm{int}}T_1\) | PROVADO sob a definição padrão de interpretação |
| Predicados de provas curtas são monotônicos | PROVADO |
| \(w_0^{T_1}\ge_{\rm lex}w_0^{T_0}\) | PROVADO quando ambos os mínimos são definidos na mesma instância |
| \(g_{T_0}\preceq_{\mathrm{ppr}}g_{T_1}\) | ABERTO |
| \(g_{T_0}\npreceq_{\mathrm{ppr}}g_{T_1}\) | ABERTO |
| Interpretabilidade \(\Rightarrow\) PPR para todos \(T,S\) | ABERTO |
| Monotonicidade ordinal da dureza dos \(g_T\) | NÃO PROVADA |
| Escala exponencial do antigo Teorema 4 | REJEITADA |
| Cobertura de todos os geradores por uma hierarquia ordinal | NÃO PROVADA |

---

# 26. Nova conjectura central

Propomos substituir a antiga conjectura informal por:

## Conjectura PPR-Reflection

Para cada classe de reflexão \(\Gamma\), seja

\[
T_{k+1}
=
T_k+\mathrm{RFN}_\Gamma(T_k).
\]

Então:

\[
\boxed{
g_{T_k}
\preceq_{\mathrm{ppr}}
g_{T_{k+1}}
}
\]

para todo \(k\), ou, mais fracamente, existe uma subsequência cofinal de níveis em que essa relação ocorre.

### Importante

Esta conjectura é **nova no âmbito deste projeto e não deve ser atribuída à literatura**.

Isto não significa que seja inédita no sentido bibliográfico absoluto. Uma busca bibliográfica específica de equivalentes em termos de redução de geradores/proof-search seria necessária antes de qualquer reivindicação de prioridade.

---

# 27. Conjectura alternativa de quebra

A outra possibilidade é:

\[
\boxed{
\exists k:
g_{T_k}
\npreceq_{\mathrm{ppr}}
g_{T_{k+1}}.
}
\]

Esta conjectura representaria uma separação conceitual:

\[
\boxed{
\text{força proof-theoretic}
\neq
\text{força operacional do gerador}.
}
\]

Se um contraexemplo concreto puder ser provado, isso seria matematicamente relevante.

---

# 28. Estratégia concreta para decidir entre as duas

O próximo passo não deve ser tentar provar diretamente a conjectura geral.

Fixe:

\[
T_0=PA,
\qquad
T_1=PA+\mathrm{RFN}_\Gamma(PA).
\]

Depois:

### Etapa A — fixar uma apresentação canônica

Escolher uma codificação única de:

- fórmulas \(L\);
- provas;
- comprimento de prova;
- \(\Phi^w\);
- circuitos \(C_n\);
- \(\tau(g_n)_b\).

Sem isso, \(g_T\) não é um objeto único, mas uma família dependente de escolhas de codificação.

### Etapa B — calcular explicitamente instâncias pequenas

Para pequenos \(n\):

\[
n=4,5,6,\ldots
\]

enumerar:

\[
g_{PA,n},
\qquad
g_{T_1,n},
\]

e suas imagens.

Não para “provar” nada assintótico, mas para procurar invariantes.

### Etapa C — testar candidatos \(R\)

Procurar transformações de baixa complexidade:

\[
\beta=R(b,n)
\]

tais que

\[
b\notin Rng(g_0)
\Rightarrow
\beta\notin Rng(g_1).
\]

### Etapa D — testar transformações de prova

Para cada candidato \(R\), investigar se existe:

\[
\Theta:
\mathrm{Proof}_P(\tau(g_1)_\beta)
\to
\mathrm{Proof}_P(\tau(g_0)_b)
\]

com blow-up:

\[
O(s^c).
\]

### Etapa E — somente então generalizar

Se o padrão sobreviver:

\[
PA\to T_1\to T_2,
\]

buscar uma prova por indução no nível.

---

# 29. Uma possível nova invariante

A construção sugere medir a diferença entre teorias por:

\[
\Delta_T(n,\Phi)
=
w_0^T(n,\Phi).
\]

Para \(T_0\subseteq T_1\),

\[
\Delta_{T_0}(n,\Phi)
\le_{\mathrm{lex}}
\Delta_{T_1}(n,\Phi).
\]

Podemos definir:

\[
\boxed{
D_{T_0,T_1}(n,\Phi)
=
\operatorname{rank}_{lex}
\left(
w_0^{T_1}
\right)
-
\operatorname{rank}_{lex}
\left(
w_0^{T_0}
\right).
}
\]

A pergunta:

\[
D_{T_0,T_1}(n,\Phi)
\]

possui crescimento controlável por uma função simples?

Se:

\[
D(n,\Phi)
\]

tiver uma estrutura universal ligada à reflexão, poderemos ter encontrado uma assinatura computacional da subida proof-theoretic.

Isso é apenas uma definição exploratória.

---

# 30. Uma ponte ainda mais forte

A ordem poderia ser estudada em três níveis:

\[
\boxed{
T
\stackrel{\mathrm{int}}{\longrightarrow}
g_T
\stackrel{\mathrm{ppr}}{\longrightarrow}
\tau(g_T)
}
\]

com duas perguntas independentes:

### Ponte I

\[
T\preceq_{\mathrm{int}}S
\stackrel{?}{\Longrightarrow}
g_T\preceq_{\mathrm{ppr}}g_S.
\]

### Ponte II

\[
g_T\preceq_{\mathrm{ppr}}g_S
\stackrel{?}{\Longrightarrow}
\text{alguma relação proof-theoretic entre }T,S.
\]

A Ponte I tenta transportar força aritmética para complexidade proposicional.

A Ponte II tenta recuperar informação da teoria a partir do comportamento do gerador.

A combinação:

\[
\boxed{
T
\longleftrightarrow
[g_T]_{\mathrm{ppr}}
}
\]

seria uma forma de **invariante operacional de teorias**.

Este conceito é um candidato interessante para desenvolvimento posterior.

---

# 31. Relação com o programa de Beklemishev

Beklemishev mostra que iterações de reflexão podem ser organizadas por operadores e notações ordinais; para níveis adequados de reflexão, essas estruturas codificam força proof-theoretic e relações de conservatividade. citeturn565792search34turn565792academia36

O nosso programa não deve afirmar:

\[
\alpha<\beta
\Rightarrow
g_{T_\alpha}\text{ é mais hard}.
\]

A formulação correta é investigar se a ordem ordinal/proof-theoretic deixa uma sombra operacional:

\[
\boxed{
\alpha<\beta
\Rightarrow
[g_{T_\alpha}]_{\mathrm{ppr}}
\preceq
[g_{T_\beta}]_{\mathrm{ppr}}.
}
\]

Essa é a conjectura matemática que vale a pena atacar.

---

# 32. Conclusão desta etapa

O ataque aos casos

\[
T_0=PA,
\qquad
T_1=PA+\mathrm{RFN}(PA)
\]

produziu uma separação nítida:

\[
\boxed{
T_0\preceq_{\mathrm{int}}T_1
}
\]

é simples e estabelecido.

Também estabelecemos:

\[
\boxed{
A_{T_0}\subseteq A_{T_1}
}
\]

e, para as instâncias em que o mecanismo produz ambos os mínimos,

\[
\boxed{
w_0^{T_0}\le_{\mathrm{lex}}w_0^{T_1}.
}
\]

Mas não conseguimos concluir:

\[
\boxed{
g_{T_0}\preceq_{\mathrm{ppr}}g_{T_1}.
}
\]

Nem conseguimos provar a negação.

Portanto, **o problema concreto \(PA\to PA+\mathrm{RFN}(PA)\) permanece aberto nesta formulação**.

Isso não é uma falha do programa. Ao contrário: o problema agora está formulado em uma linguagem suficientemente precisa para ser atacado sem esconder os saltos lógicos.

---

# 33. Resultado novo efetivamente obtido nesta etapa

O resultado que pode ser preservado como contribuição metodológica do projeto é:

\[
\boxed{
\text{Inclusão de teorias}
\Rightarrow
\text{monotonicidade do predicado de prova curta}
}
\]

mas:

\[
\boxed{
\text{monotonicidade do predicado}
\nRightarrow
\text{PPR do gerador}.
}
\]

A razão estrutural é o operador:

\[
A_T
\mapsto
\min_{\mathrm{lex}}(\neg A_T),
\]

que não possui, por si só, uma transformação polinomial inversa/preservadora.

Esta é uma distinção que deve substituir as antigas provas de monotonicidade do repositório.

---

# 34. Agenda imediata

O próximo arquivo deveria ser:

\[
\boxed{
09\_EXPERIMENTO\_PPR\_PA\_RFNPA.md
}
\]

com uma implementação matemática/computacional das versões finitas de \(g_{PA}\) e \(g_{T_1}\).

A prioridade é:

\[
\boxed{
\text{enumerar }g_{PA,n},g_{T_1,n}
\rightarrow
\text{enumerar complementos de imagem}
\rightarrow
\text{buscar }R
\rightarrow
\text{testar PPR}.
}
\]

Só depois devemos tentar uma prova assintótica.

---

# 35. Bibliografia essencial

1. **Krajíček, J.** “A Proof Complexity Conjecture and the Incompleteness Theorem.” *Journal of Symbolic Logic* 90(3), 2025, pp. 1206–1210. Preprint 2023.  
   https://arxiv.org/abs/2303.10637

2. **Krajíček, J.** *Proof Complexity Generators*. Cambridge University Press / LMS Lecture Note Series 497, 2025.  
   https://www.cambridge.org/core/books/proof-complexity-generators/

3. **Krajíček, J.** “On the Existence of Strong Proof Complexity Generators.” *Bulletin of Symbolic Logic*, 2024.  
   https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/on-the-existence-of-strong-proof-complexity-generators/84EA24D938C0775C59BE4D54E5E645B5

4. **Krajíček, J.** “On \(NP\cap coNP\) Proof Complexity Generators.” *Logical Methods in Computer Science* 22(2), 2026.  
   https://lmcs.episciences.org/18158

5. **Beklemishev, L. D.** “Reflection Principles and Provability Algebras in Formal Arithmetic.” *Russian Mathematical Surveys* 60(2), 2005.  
   https://www.mathnet.ru/links/4b1b1c98a0a27ce025c80ebb198e65a1/rm1401_eng.pdf

6. **Beklemishev, L. D.** “Positive Provability Logic for Uniform Reflection Principles.” 2013.  
   https://arxiv.org/abs/1304.4396

7. **Freund, A.; Pakhomov, F.** “Short Proofs for Slow Consistency.” 2017/2020.  
   https://arxiv.org/abs/1712.03251

8. **Jump Operators, Interactive Proofs and Proof Complexity Generators.** FOCS 2024.  
   https://ieee-focs.org/FOCS-2024-Papers/pdfs/FOCS2024-1oojWxXs5YAKfs3z3lBRMF/167400a573/167400a573.pdf

---

## Registro de status

\[
\boxed{
\begin{array}{ll}
\text{Definição PPR} & \text{NOVA / proposta deste projeto}\\
T_0\preceq_{\rm int}T_1 & \text{ESTABELECIDO}\\
A_{T_0}\subseteq A_{T_1} & \text{ESTABELECIDO}\\
w_0^{T_0}\le_{\rm lex}w_0^{T_1} & \text{ESTABELECIDO localmente}\\
g_{T_0}\preceq_{\rm ppr}g_{T_1} & \text{ABERTO}\\
g_{T_0}\npreceq_{\rm ppr}g_{T_1} & \text{ABERTO}\\
\text{interpretabilidade}\Rightarrow\text{PPR} & \text{ABERTO}\\
\text{escala ordinal automática de dureza} & \text{NÃO DEMONSTRADA}
\end{array}
}
\]

**Regra para o repositório:** até que uma redução \(R\) e um transformador \(\Theta\) sejam efetivamente construídos e suas cotas polinomiais provadas, nenhum enunciado de monotonicidade de \(g_T\) deve ser rotulado como teorema.

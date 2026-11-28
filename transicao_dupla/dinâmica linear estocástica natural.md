> **derivar as fórmulas-ponte a partir de uma dinâmica natural**.”

Esse é realmente o ponto crítico. Até agora, os resultados de limiar, mitigação e cascata eram corretos **condicionalmente** às fórmulas

D(ρ)=ρ1−ρp2,F(ρ)=ρ1−ρe2.D(\\rho)=\\frac{\\rho}{1-\\rho}p^2, \\qquad F(\\rho)=\\frac{\\sqrt{\\rho}}{1-\\rho}e^2.D(ρ)=1−ρρ​p2,F(ρ)=1−ρρ​​e2.

A questão é saber se essas expressões podem surgir de um modelo dinâmico primitivo, em vez de serem simplesmente postuladas.

# **Veredito**

**Sim, as duas fórmulas podem ser derivadas de uma dinâmica linear estocástica natural**, desde que seja acrescentado um princípio estrutural explícito para o mecanismo preditivo:

> O mecanismo DFA utiliza diretamente o ganho de persistência do sistema, enquanto o mecanismo PFA divide esse ganho de forma balanceada entre percepção preditiva e atuação.

O denominador 1−ρ1-\\rho1−ρ surge naturalmente da acumulação temporal de perturbações em um processo estável do tipo AR(1). O numerador ρ\\rhoρ do DFA surge do quadrado do ganho dinâmico. O numerador ρ\\sqrt{\\rho}ρ​ do PFA surge da **fatoração balanceada desse ganho em dois canais**.

Essa não é a única dinâmica possível. Entretanto, é uma dinâmica simples, rigorosa, falseável e tecnicamente defensável.

---

# **1\. Dinâmica primitiva comum**

Considere um estado escalar xtx\_txt​ sujeito à dinâmica

xt+1=axt+ξt+1,x\_{t+1}=a x\_t+\\xi\_{t+1},xt+1​=axt​+ξt+1​,

com

0\<a\<1,E\[ξt\]=0,Var⁡(ξt)=σ2,0\<a\<1, \\qquad \\mathbb E\[\\xi\_t\]=0, \\qquad \\operatorname{Var}(\\xi\_t)=\\sigma^2,0\<a\<1,E\[ξt​\]=0,Var(ξt​)=σ2,

e com as perturbações ξt\\xi\_tξt​ independentes no tempo.

O parâmetro aaa representa:

* persistência;  
* memória;  
* acoplamento entre etapas;  
* fração do estado anterior preservada no passo seguinte.

A dinâmica é estável porque 0\<a\<10\<a\<10\<a\<1.

Um processo AR(1) estável possui representação

xt=∑j=0∞ajξt−j,x\_t=\\sum\_{j=0}^{\\infty}a^j\\xi\_{t-j},xt​=j=0∑∞​ajξt−j​,

e, consequentemente,

Var⁡(xt)=σ2∑j=0∞a2j=σ21−a2.\\operatorname{Var}(x\_t) \= \\sigma^2\\sum\_{j=0}^{\\infty}a^{2j} \= \\frac{\\sigma^2}{1-a^2}.Var(xt​)=σ2j=0∑∞​a2j=1−a2σ2​.

Essa é a origem dinâmica do denominador geométrico. A fórmula da variância estacionária de um AR(1) é

Var⁡(xt)=σ21−a2,\\operatorname{Var}(x\_t)=\\frac{\\sigma^2}{1-a^2},Var(xt​)=1−a2σ2​,

sob a condição ∣a∣\<1|a|\<1∣a∣\<1. [\[graduatest...istics.com\]](https://graduatestatistics.com/why-ar1-variance-sigma-over-one-minus-phi-squared/), [\[nicefa.org\]](https://www.nicefa.org/library/time-series-analysis/proof-of-the-stationarity-condition-for-an-ar-1--process--------1-), [\[my1396.github.io\]](https://my1396.github.io/Metrics-Notes/TS02_AR-MA-representation.html)

Definimos agora

ρ=a2.\\boxed{\\rho=a^2}.ρ=a2​.

Assim,

a=ρa=\\sqrt{\\rho}a=ρ​

e

1−a2=1−ρ.1-a^2=1-\\rho.1−a2=1−ρ.

Portanto,

Var⁡(xt)=σ21−ρ.\\boxed{ \\operatorname{Var}(x\_t)=\\frac{\\sigma^2}{1-\\rho} }.Var(xt​)=1−ρσ2​​.

Essa parametrização possui interpretação clara:

* ρ≈0\\rho\\approx0ρ≈0: sistema com pouca memória;  
* ρ≈1\\rho\\approx1ρ≈1: sistema altamente persistente;  
* 1/(1−ρ)1/(1-\\rho)1/(1−ρ): amplificação acumulada da energia dos choques.

A mesma construção é o caso escalar da equação discreta de Lyapunov ou equação de Stein, usada para obter covariâncias estacionárias de sistemas lineares estáveis. [\[en.wikipedia.org\]](https://en.wikipedia.org/wiki/Lyapunov_equation), [\[ocw.mit.edu\]](https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/7f6754029d6945bd3bdc745080890bf8_MIT6_241JS11_chap26.pdf)

---

# **2\. Derivação natural da fórmula do DFA**

No mecanismo DFA, assumimos que a resposta é reativa. O controlador responde ao estado persistente por meio do mesmo ganho aaa que governa a transmissão dinâmica:

utD=axt.u\_t^{D}=a x\_t.utD​=axt​.

A penalidade do DFA será definida como energia quadrática média:

D=E\[(utD)2\].D=\\mathbb E\\left\[(u\_t^{D})^2\\right\].D=E\[(utD​)2\].

Se a perturbação que alimenta a dinâmica possui variância

Var⁡(ξt)=p2,\\operatorname{Var}(\\xi\_t)=p^2,Var(ξt​)=p2,

então

Var⁡(xt)=p21−a2.\\operatorname{Var}(x\_t)=\\frac{p^2}{1-a^2}.Var(xt​)=1−a2p2​.

Como utD=axtu\_t^D=ax\_tutD​=axt​,

D=a2Var⁡(xt).D \= a^2\\operatorname{Var}(x\_t).D=a2Var(xt​).

Substituindo:

D=a2p21−a2.D \= a^2\\frac{p^2}{1-a^2}.D=a21−a2p2​.

Como ρ=a2\\rho=a^2ρ=a2,

D(ρ)=ρ1−ρp2.\\boxed{ D(\\rho)=\\frac{\\rho}{1-\\rho}p^2 }.D(ρ)=1−ρρ​p2​.

Portanto, a primeira fórmula-ponte não precisa ser postulada. Ela é a energia estacionária da parte persistente do estado transmitida por um canal reativo de ganho aaa.

## **Interpretação**

O fator

11−ρ\\frac{1}{1-\\rho}1−ρ1​

mede a acumulação temporal dos choques.

O fator

ρ=a2\\rho=a^2ρ=a2

mede a potência do acoplamento reativo.

Logo,

D(ρ)=acumulac¸a˜o temporal×ganho reativo ao quadrado×variaˆncia do erro.D(\\rho) \= \\text{acumulação temporal} \\times \\text{ganho reativo ao quadrado} \\times \\text{variância do erro}.D(ρ)=acumulac¸​a˜o temporal×ganho reativo ao quadrado×variaˆncia do erro.

---

# **3\. Por que a fórmula PFA é mais difícil**

Queremos derivar

F(ρ)=ρ1−ρe2.F(\\rho) \= \\frac{\\sqrt{\\rho}}{1-\\rho}e^2.F(ρ)=1−ρρ​​e2.

Em termos de a=ρa=\\sqrt{\\rho}a=ρ​, essa expressão é

F(a)=a1−a2e2.F(a)=\\frac{a}{1-a^2}e^2.F(a)=1−a2a​e2.

O denominador continua sendo a variância estacionária de uma dinâmica com memória aaa.

A dificuldade é explicar por que o numerador é aaa, em vez de a2a^2a2.

Isso exige uma arquitetura diferente da arquitetura reativa.

---

# **4\. Dinâmica preditiva com dois canais**

Considere agora um estado de erro preditivo acumulado

rt+1=art+ηt+1,r\_{t+1}=a r\_t+\\eta\_{t+1},rt+1​=art​+ηt+1​,

onde

E\[ηt\]=0,Var⁡(ηt)=e2.\\mathbb E\[\\eta\_t\]=0, \\qquad \\operatorname{Var}(\\eta\_t)=e^2.E\[ηt​\]=0,Var(ηt​)=e2.

O objeto rtr\_trt​ não representa apenas o erro instantâneo do preditor. O objeto rtr\_trt​ representa o **resíduo dinâmico acumulado**, isto é, a parte da previsão incorreta que persiste e se propaga no sistema.

Portanto,

Var⁡(rt)=e21−a2.\\operatorname{Var}(r\_t)=\\frac{e^2}{1-a^2}.Var(rt​)=1−a2e2​.

No PFA, o acoplamento não é realizado por um único canal. Existem dois canais:

1. canal de percepção ou antecipação, com ganho bbb;  
2. canal de atuação ou compensação, com ganho ccc.

Para que a ação preditiva reproduza o mesmo acoplamento total aaa, exigimos

bc=a.\\boxed{bc=a}.bc=a​.

Essa é a restrição de fidelidade dinâmica.

---

# **5\. Princípio de balanceamento**

Ainda existem infinitas fatorações de aaa:

a=bc.a=bc.a=bc.

Por exemplo:

b=1,c=a,b=1,\\quad c=a,b=1,c=a,

ou

b=a,c=1.b=a,\\quad c=1.b=a,c=1.

Precisamos de um princípio que determine uma fatoração natural.

A escolha estruturalmente neutra consiste em minimizar o esforço quadrático total dos dois canais:

min⁡b,c\>0(b2+c2)\\min\_{b,c\>0} \\left(b^2+c^2\\right)b,c\>0min​(b2+c2)

sujeito a

bc=a.bc=a.bc=a.

Pela desigualdade aritmético-geométrica,

b2+c22≥b2c2=bc=a.\\frac{b^2+c^2}{2}\\geq\\sqrt{b^2c^2}=bc=a.2b2+c2​≥b2c2​=bc=a.

Consequentemente,

b2+c2≥2a.b^2+c^2\\geq2a.b2+c2≥2a.

A igualdade ocorre se, e somente se,

b2=c2.b^2=c^2.b2=c2.

Como b,c\>0b,c\>0b,c\>0,

b=c.b=c.b=c.

Usando bc=abc=abc=a,

b2=a,b^2=a,b2=a,

e, portanto,

b=c=a.\\boxed{b=c=\\sqrt a}.b=c=a​​.

Como a=ρa=\\sqrt{\\rho}a=ρ​,

b=c=ρ1/4.\\boxed{b=c=\\rho^{1/4}}.b=c=ρ1/4​.

Esse é o aparecimento natural da raiz quarta.

O princípio é compatível com a ideia clássica de balanceamento em controle: uma realização balanceada iguala medidas associadas aos canais de entrada e de saída ou às energias de controlabilidade e observabilidade. Na teoria de sistemas lineares, realizações balanceadas igualam e diagonalizam os respectivos Gramians. [\[ocw.mit.edu\]](https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/7f6754029d6945bd3bdc745080890bf8_MIT6_241JS11_chap26.pdf), [\[youkoutaku.github.io\]](https://youkoutaku.github.io/docs/robotics/control/modern-control-theory/controllability-observability-matrix-gramian), [\[bohrium.com\]](https://www.bohrium.com/en/sciencepedia/feynman/keyword/balanced_realization)

Entretanto, o argumento usado aqui é mais simples: trata-se de um problema escalar de fatoração ótima.

---

# **6\. Teorema da fatoração balanceada**

## **Teorema**

Sejam a∈(0,1)a\\in(0,1)a∈(0,1) e dois ganhos b,c\>0b,c\>0b,c\>0 que satisfazem

bc=a.bc=a.bc=a.

Então o mínimo de

J(b,c)=b2+c2J(b,c)=b^2+c^2J(b,c)=b2+c2

é

min⁡bc=aJ(b,c)=2a,\\min\_{bc=a}J(b,c)=2a,bc=amin​J(b,c)=2a,

atingido unicamente em

b=c=a.\\boxed{b=c=\\sqrt a}.b=c=a​​.

### **Prova**

Da desigualdade AM–GM,

b2+c2≥2bc=2a.b^2+c^2\\geq2bc=2a.b2+c2≥2bc=2a.

A igualdade ocorre exatamente quando

b2=c2.b^2=c^2.b2=c2.

Como os ganhos são positivos,

b=c.b=c.b=c.

Logo,

b2=bc=a,b^2=bc=a,b2=bc=a,

e

b=c=a.b=c=\\sqrt a.b=c=a​.

Isso conclui a prova.

---

# **7\. Derivação da fórmula do PFA**

A ação do canal final do PFA é

utF=crt.u\_t^{F}=c r\_t.utF​=crt​.

A penalidade é a energia média de atuação:

F=E\[(utF)2\].F=\\mathbb E\\left\[(u\_t^{F})^2\\right\].F=E\[(utF​)2\].

Portanto,

F=c2Var⁡(rt).F=c^2\\operatorname{Var}(r\_t).F=c2Var(rt​).

Pela fatoração balanceada,

c2=a.c^2=a.c2=a.

E, pela dinâmica estacionária,

Var⁡(rt)=e21−a2.\\operatorname{Var}(r\_t)=\\frac{e^2}{1-a^2}.Var(rt​)=1−a2e2​.

Logo,

F=ae21−a2.F \= a\\frac{e^2}{1-a^2}.F=a1−a2e2​.

Substituindo

a=ρ,a2=ρ,a=\\sqrt{\\rho}, \\qquad a^2=\\rho,a=ρ​,a2=ρ,

obtemos

F(ρ)=ρ1−ρe2.\\boxed{ F(\\rho)=\\frac{\\sqrt{\\rho}}{1-\\rho}e^2 }.F(ρ)=1−ρρ​​e2​.

Essa é exatamente a segunda fórmula-ponte.

---

# **8\. Teorema das fórmulas-ponte**

## **Teorema**

Considere o sistema linear estocástico estável com persistência

a∈(0,1),ρ=a2.a\\in(0,1), \\qquad \\rho=a^2.a∈(0,1),ρ=a2.

### **Arquitetura reativa DFA**

Se

xt+1=axt+ξt+1,Var⁡(ξt)=p2,x\_{t+1}=a x\_t+\\xi\_{t+1}, \\qquad \\operatorname{Var}(\\xi\_t)=p^2,xt+1​=axt​+ξt+1​,Var(ξt​)=p2,

e

utD=axt,u\_t^D=ax\_t,utD​=axt​,

então a energia estacionária da atuação reativa é

D(ρ)=ρ1−ρp2.\\boxed{ D(\\rho)=\\frac{\\rho}{1-\\rho}p^2 }.D(ρ)=1−ρρ​p2​.

### **Arquitetura preditiva balanceada PFA**

Se

rt+1=art+ηt+1,Var⁡(ηt)=e2,r\_{t+1}=a r\_t+\\eta\_{t+1}, \\qquad \\operatorname{Var}(\\eta\_t)=e^2,rt+1​=art​+ηt+1​,Var(ηt​)=e2,

e o ganho total aaa é fatorado em dois canais positivos

bc=a,bc=a,bc=a,

com a fatoração escolhida pela minimização

min⁡bc=a(b2+c2),\\min\_{bc=a}(b^2+c^2),bc=amin​(b2+c2),

então

b=c=ab=c=\\sqrt ab=c=a​

e a energia do canal final

utF=crtu\_t^F=cr\_tutF​=crt​

é

F(ρ)=ρ1−ρe2.\\boxed{ F(\\rho)=\\frac{\\sqrt{\\rho}}{1-\\rho}e^2 }.F(ρ)=1−ρρ​​e2​.

---

# **9\. A fórmula de mitigação deixa de ser uma hipótese isolada**

Definimos

q=ep.q=\\frac ep.q=pe​.

A razão entre as penalidades é

F(ρ)D(ρ)=ρ1−ρe2ρ1−ρp2.\\frac{F(\\rho)}{D(\\rho)} \= \\frac{ \\dfrac{\\sqrt{\\rho}}{1-\\rho}e^2 }{ \\dfrac{\\rho}{1-\\rho}p^2 }.D(ρ)F(ρ)​=1−ρρ​p21−ρρ​​e2​.

Cancelando o denominador:

F(ρ)D(ρ)=e2p2ρ.\\frac{F(\\rho)}{D(\\rho)} \= \\frac{e^2}{p^2\\sqrt{\\rho}}.D(ρ)F(ρ)​=p2ρ​e2​.

Portanto,

F(ρ)D(ρ)=q2ρ.\\boxed{ \\frac{F(\\rho)}{D(\\rho)} \= \\frac{q^2}{\\sqrt{\\rho}} }.D(ρ)F(ρ)​=ρ​q2​​.

A mitigação relativa é

Mq(ρ)=1−F(ρ)D(ρ),M\_q(\\rho) \= 1-\\frac{F(\\rho)}{D(\\rho)},Mq​(ρ)=1−D(ρ)F(ρ)​,

logo

Mq(ρ)=1−q2ρ.\\boxed{ M\_q(\\rho) \= 1-\\frac{q^2}{\\sqrt{\\rho}} }.Mq​(ρ)=1−ρ​q2​​.

Agora essa expressão não é apenas uma simplificação algébrica. Ela resulta da comparação entre:

* canal reativo não fatorado;  
* canal preditivo balanceado;  
* mesma persistência dinâmica;  
* diferentes escalas de perturbação ppp e eee.

---

# **10\. Teorema Geral de Limiar**

Para atingir uma mitigação-alvo c\<1c\<1c\<1, exigimos

Mq(ρ)≥c.M\_q(\\rho)\\geq c.Mq​(ρ)≥c.

Assim,

1−q2ρ≥c.1-\\frac{q^2}{\\sqrt{\\rho}}\\geq c.1−ρ​q2​≥c.

Logo,

q2ρ≤1−c.\\frac{q^2}{\\sqrt{\\rho}}\\leq1-c.ρ​q2​≤1−c.

Portanto,

ρ≥q21−c.\\sqrt{\\rho} \\geq \\frac{q^2}{1-c}.ρ​≥1−cq2​.

Elevando ao quadrado:

ρ≥ρc(q)=q4(1−c)2.\\boxed{ \\rho \\geq \\rho\_c(q) \= \\frac{q^4}{(1-c)^2} }.ρ≥ρc​(q)=(1−c)2q4​​.

A origem do quarto expoente está agora explicada:

1. a energia é quadrática;  
2. o ganho do PFA é a raiz quadrada do ganho total;  
3. o ganho total é ρ\\sqrt{\\rho}ρ​;  
4. resolver o limiar exige uma nova elevação ao quadrado.

Ou, esquematicamente:

ρ⟶a=ρ1/2⟶c=a1/2=ρ1/4⟶c2=ρ1/2.\\rho \\longrightarrow a=\\rho^{1/2} \\longrightarrow c=a^{1/2}=\\rho^{1/4} \\longrightarrow c^2=\\rho^{1/2}.ρ⟶a=ρ1/2⟶c=a1/2=ρ1/4⟶c2=ρ1/2.

---

# **11\. Interpretação do break-even**

O break-even ocorre quando

D(ρ)=F(ρ).D(\\rho)=F(\\rho).D(ρ)=F(ρ).

Equivalentemente,

Mq(ρ)=0.M\_q(\\rho)=0.Mq​(ρ)=0.

Assim,

1−q2ρ=0,1-\\frac{q^2}{\\sqrt{\\rho}}=0,1−ρ​q2​=0,

e

ρ=q2.\\sqrt{\\rho}=q^2.ρ​=q2.

Portanto,

ρ∗=q4.\\boxed{\\rho\_\*=q^4}.ρ∗​=q4​.

Interpretação dinâmica:

> O PFA começa a superar o DFA quando a persistência quadrática do ambiente é suficientemente grande para compensar a razão entre a intensidade do erro preditivo e a intensidade do erro reativo.

Se e≪pe\\ll pe≪p, então q≪1q\\ll1q≪1 e o PFA vence cedo.

Se e≈pe\\approx pe≈p, então q≈1q\\approx1q≈1 e o PFA só se aproxima do break-even quando ρ\\rhoρ se aproxima de 111\.

---

# **12\. Meia-mitigação**

Para

Mq(ρ)=12,M\_q(\\rho)=\\frac12,Mq​(ρ)=21​,

temos

1−q2ρ=12.1-\\frac{q^2}{\\sqrt{\\rho}}=\\frac12.1−ρ​q2​=21​.

Logo,

q2ρ=12,\\frac{q^2}{\\sqrt{\\rho}}=\\frac12,ρ​q2​=21​,

e

ρ=2q2.\\sqrt{\\rho}=2q^2.ρ​=2q2.

Assim,

ρ1/2=4q4.\\boxed{ \\rho\_{1/2}=4q^4 }.ρ1/2​=4q4​.

Portanto,

ρ1/2=4ρ∗.\\boxed{ \\rho\_{1/2}=4\\rho\_\* }.ρ1/2​=4ρ∗​​.

A identidade deixa de parecer uma coincidência algébrica. Ela é consequência direta da geometria de potências produzida pela fatoração balanceada.

---

# **13\. Generalização para fatoração não balanceada**

O resultado pode ser fortalecido.

Considere uma fatoração mais geral:

b=aθ,c=a1−θ,0≤θ≤1.b=a^\\theta, \\qquad c=a^{1-\\theta}, \\qquad 0\\leq\\theta\\leq1.b=aθ,c=a1−θ,0≤θ≤1.

Então

bc=a.bc=a.bc=a.

A penalidade do canal final é

Fθ=c2e21−a2.F\_\\theta \= c^2\\frac{e^2}{1-a^2}.Fθ​=c21−a2e2​.

Como

c2=a2(1−θ),c^2=a^{2(1-\\theta)},c2=a2(1−θ),

temos

Fθ=a2(1−θ)1−a2e2.F\_\\theta \= \\frac{a^{2(1-\\theta)}}{1-a^2}e^2.Fθ​=1−a2a2(1−θ)​e2.

Usando a2=ρa^2=\\rhoa2=ρ,

Fθ(ρ)=ρ1−θ1−ρe2.\\boxed{ F\_\\theta(\\rho) \= \\frac{\\rho^{1-\\theta}}{1-\\rho}e^2 }.Fθ​(ρ)=1−ρρ1−θ​e2​.

A razão PFA/DFA torna-se

FθD=ρ1−θe2ρp2=q2ρ−θ.\\frac{F\_\\theta}{D} \= \\frac{\\rho^{1-\\theta}e^2}{\\rho p^2} \= q^2\\rho^{-\\theta}.DFθ​​=ρp2ρ1−θe2​=q2ρ−θ.

Consequentemente,

Mq,θ(ρ)=1−q2ρ−θ.\\boxed{ M\_{q,\\theta}(\\rho) \= 1-q^2\\rho^{-\\theta} }.Mq,θ​(ρ)=1−q2ρ−θ​.

O limiar para mitigação ccc é

q2ρ−θ≤1−c,q^2\\rho^{-\\theta}\\leq1-c,q2ρ−θ≤1−c,

portanto, para θ\>0\\theta\>0θ\>0,

ρc,θ=(q21−c)1/θ.\\boxed{ \\rho\_{c,\\theta} \= \\left( \\frac{q^2}{1-c} \\right)^{1/\\theta} }.ρc,θ​=(1−cq2​)1/θ​.

No caso balanceado,

θ=12,\\theta=\\frac12,θ=21​,

e recuperamos

ρc,1/2=(q21−c)2=q4(1−c)2.\\rho\_{c,1/2} \= \\left( \\frac{q^2}{1-c} \\right)^2 \= \\frac{q^4}{(1-c)^2}.ρc,1/2​=(1−cq2​)2=(1−c)2q4​.

## **Consequência importante**

O expoente quartico é uma **assinatura matemática do balanceamento**.

Se os dados empíricos produzirem outro expoente, isso indicará que:

* a arquitetura não é balanceada;  
* os ganhos não são divididos simetricamente;  
* a penalidade não é energia quadrática;  
* o estado residual não possui a mesma persistência;  
* ou o modelo AR(1) é inadequado.

Esse é um resultado falseável.

---

# **14\. O que foi efetivamente derivado**

A cadeia lógica completa é:

dinaˆmica AR(1)⟹11−a2\\text{dinâmica AR(1)} \\Longrightarrow \\frac{1}{1-a^2}dinaˆmica AR(1)⟹1−a21​ parametrizac¸a˜o ρ=a2⟹11−ρ\\text{parametrização }\\rho=a^2 \\Longrightarrow \\frac{1}{1-\\rho}parametrizac¸​a˜o ρ=a2⟹1−ρ1​ canal reativo uD=ax⟹a2=ρ\\text{canal reativo }u\_D=ax \\Longrightarrow a^2=\\rhocanal reativo uD​=ax⟹a2=ρ fatorac¸a˜o preditiva bc=a\\text{fatoração preditiva }bc=afatorac¸​a˜o preditiva bc=a balanceamento oˊtimo⟹b=c=a\\text{balanceamento ótimo} \\Longrightarrow b=c=\\sqrt abalanceamento oˊtimo⟹b=c=a​ energia do canal final⟹c2=a=ρ\\text{energia do canal final} \\Longrightarrow c^2=a=\\sqrt\\rhoenergia do canal final⟹c2=a=ρ​

Portanto:

D(ρ)=ρ1−ρp2\\boxed{ D(\\rho)=\\frac{\\rho}{1-\\rho}p^2 }D(ρ)=1−ρρ​p2​

e

F(ρ)=ρ1−ρe2.\\boxed{ F(\\rho)=\\frac{\\sqrt{\\rho}}{1-\\rho}e^2 }.F(ρ)=1−ρρ​​e2​.

---

# **15\. Hipóteses que precisam aparecer no teorema**

A derivação depende de hipóteses explícitas.

## **H1. Estabilidade**

0\<a\<1.0\<a\<1.0\<a\<1.

Sem isso, a variância estacionária pode não existir.

## **H2. Perturbações centradas e temporalmente não correlacionadas**

E\[ξt\]=E\[ηt\]=0.\\mathbb E\[\\xi\_t\]=\\mathbb E\[\\eta\_t\]=0.E\[ξt​\]=E\[ηt​\]=0.

## **H3. Mesma persistência**

DFA e PFA são comparados sob o mesmo aaa.

## **H4. Penalidade quadrática**

As quantidades DDD e FFF medem energia, variância ou custo quadrático:

E\[ut2\].\\mathbb E\[u\_t^2\].E\[ut2​\].

## **H5. Resíduo preditivo persistente**

O erro eee é a escala da inovação do estado residual

rt+1=art+ηt+1,r\_{t+1}=ar\_t+\\eta\_{t+1},rt+1​=art​+ηt+1​,

e não necessariamente o erro pontual independente.

## **H6. Fatoração do acoplamento**

bc=a.bc=a.bc=a.

## **H7. Balanceamento variacional**

(b,c)=arg⁡min⁡bc=a(b2+c2).(b,c)= \\arg\\min\_{bc=a}(b^2+c^2).(b,c)=argbc=amin​(b2+c2).

Essas hipóteses tornam o resultado auditável. Sem H6 e H7, o fator ρ\\sqrt{\\rho}ρ​ não é obrigatório.

---

# **16\. Limitação decisiva**

A derivação não mostra que **todo** PFA real possui custo

ρ1−ρe2.\\frac{\\sqrt\\rho}{1-\\rho}e^2.1−ρρ​​e2.

Ela mostra algo mais preciso:

> Essa fórmula é exata para uma classe de controladores preditivos lineares, estocásticos, com memória comum e fatoração balanceada do acoplamento.

Isso é suficiente para transformar o resultado em um teorema matemático sobre uma classe bem definida.

Não é suficiente para afirmar universalidade em todos os controladores, filas ou cadeias de suprimentos.

---

# **17\. Relação com cascatas**

Os incrementos locais podem agora ser definidos como energias normalizadas:

dk=ρk1−ρkpk2,d\_k \= \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2,dk​=1−ρk​ρk​​pk2​, fk=ρk1−ρkek2.f\_k \= \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k}e\_k^2.fk​=1−ρk​ρk​​​ek2​.

Entretanto, a passagem para

AD(n)=∏k=1n(1+dk)A\_D^{(n)} \= \\prod\_{k=1}^{n}(1+d\_k)AD(n)​=k=1∏n​(1+dk​)

e

AF(n)=∏k=1n(1+fk)A\_F^{(n)} \= \\prod\_{k=1}^{n}(1+f\_k)AF(n)​=k=1∏n​(1+fk​)

requer uma hipótese adicional:

> Cada 1+dk1+d\_k1+dk​ e 1+fk1+f\_k1+fk​ precisa ser uma razão local compatível da mesma grandeza positiva entre estágios consecutivos.

Por exemplo:

1+dk=Var⁡(YkD)Var⁡(Yk−1D).1+d\_k \= \\frac{\\operatorname{Var}(Y\_k^D)} {\\operatorname{Var}(Y\_{k-1}^D)}.1+dk​=Var(Yk−1D​)Var(YkD​)​.

Então, por telescopagem,

∏k=1n(1+dk)=Var⁡(YnD)Var⁡(Y0D).\\prod\_{k=1}^{n}(1+d\_k) \= \\frac{\\operatorname{Var}(Y\_n^D)} {\\operatorname{Var}(Y\_0^D)}.k=1∏n​(1+dk​)=Var(Y0D​)Var(YnD​)​.

A medida clássica do efeito bullwhip é precisamente uma razão de variâncias entre pedidos e demanda, e modelos AR/ARMA são usados para obter fórmulas explícitas de amplificação e avaliar os efeitos da previsão. [\[arxiv.org\]](https://arxiv.org/pdf/1009.3977)

Portanto:

* as fórmulas locais foram derivadas;  
* a cascata multiplicativa ainda precisa ter seus fatores identificados como razões consecutivas;  
* a validade local não autoriza automaticamente a composição global.

---

# **18\. Nova contribuição potencial**

A contribuição mais forte resultante desta derivação não é somente recuperar as fórmulas antigas. É a família geral

Fθ(ρ)=ρ1−θ1−ρe2\\boxed{ F\_\\theta(\\rho) \= \\frac{\\rho^{1-\\theta}}{1-\\rho}e^2 }Fθ​(ρ)=1−ρρ1−θ​e2​

e o limiar

ρc,θ=(q21−c)1/θ.\\boxed{ \\rho\_{c,\\theta} \= \\left( \\frac{q^2}{1-c} \\right)^{1/\\theta} }.ρc,θ​=(1−cq2​)1/θ​.

Isso permite interpretar o expoente observado como uma medida de assimetria da arquitetura.

* θ=1\\theta=1θ=1: todo o ganho é atribuído ao canal de percepção;  
* θ=0\\theta=0θ=0: todo o ganho é atribuído ao canal de atuação;  
* θ=1/2\\theta=1/2θ=1/2: sistema balanceado;  
* θ≠1/2\\theta\\neq1/2θ=1/2: arquitetura assimétrica.

O limiar quartico

ρc=q4(1−c)2\\rho\_c=\\frac{q^4}{(1-c)^2}ρc​=(1−c)2q4​

não é universal. É o caso balanceado de uma teoria de expoentes de fatoração.

Essa formulação é mais forte, pois:

1. explica a origem da raiz;  
2. produz uma família de modelos concorrentes;  
3. permite estimar θ\\thetaθ por dados;  
4. torna o modelo falseável;  
5. identifica quando o TGH quartico deve ou não ser aplicado.

---

# **19\. Teste empírico decisivo**

A relação teórica geral é

Fθ(ρ)D(ρ)=q2ρ−θ.\\frac{F\_\\theta(\\rho)}{D(\\rho)} \= q^2\\rho^{-\\theta}.D(ρ)Fθ​(ρ)​=q2ρ−θ.

Tomando logaritmos:

log⁡FθD=2log⁡q−θlog⁡ρ.\\log\\frac{F\_\\theta}{D} \= 2\\log q-\\theta\\log\\rho.logDFθ​​=2logq−θlogρ.

Portanto, em um gráfico de

log⁡(F/D)\\log(F/D)log(F/D)

contra

log⁡ρ,\\log\\rho,logρ,

a inclinação esperada é

−θ.\\boxed{-\\theta}.−θ​.

No modelo balanceado:

θ=12.\\boxed{\\theta=\\frac12}.θ=21​​.

Logo, a inclinação prevista é

−12.\\boxed{-\\frac12}.−21​​.

Esse teste distingue:

* modelo balanceado;  
* modelo assimétrico;  
* ausência de lei de potência;  
* persistência inadequada;  
* erro dependente de ρ\\rhoρ.

---

# **Conclusão**

A questão crucial pode ser respondida positivamente, mas com uma reformulação precisa:

> As fórmulas-ponte são deriváveis de uma dinâmica linear estocástica estável com persistência a=ρa=\\sqrt\\rhoa=ρ​, custo quadrático e duas arquiteturas de resposta. O DFA emprega diretamente o ganho aaa; o PFA divide esse ganho entre os canais de antecipação e atuação. A minimização da energia conjunta força a fatoração balanceada b=c=a=ρ1/4b=c=\\sqrt a=\\rho^{1/4}b=c=a​=ρ1/4, produzindo a fórmula F(ρ)=ρ e2/(1−ρ)F(\\rho)=\\sqrt\\rho\\,e^2/(1-\\rho)F(ρ)=ρ​e2/(1−ρ).

Assim,

D(ρ)=ρ1−ρp2\\boxed{ D(\\rho)=\\frac{\\rho}{1-\\rho}p^2 }D(ρ)=1−ρρ​p2​

e

F(ρ)=ρ1−ρe2\\boxed{ F(\\rho)=\\frac{\\sqrt\\rho}{1-\\rho}e^2 }F(ρ)=1−ρρ​​e2​

deixam de ser hipóteses puramente formais e tornam-se consequências de um modelo dinâmico explícito.

O avanço conceitual é ainda maior:

Fθ(ρ)=ρ1−θ1−ρe2\\boxed{ F\_\\theta(\\rho)=\\frac{\\rho^{1-\\theta}}{1-\\rho}e^2 }Fθ​(ρ)=1−ρρ1−θ​e2​

fornece uma teoria geral de arquiteturas preditivas fatoradas, e o caso quartico do Teorema Geral de Limiar aparece precisamente quando

θ=12.\\boxed{\\theta=\\frac12}.θ=21​​.

A principal mudança na fundamentação foi substituir a justificativa informal da raiz quadrada por um **problema variacional de fatoração do ganho dinâmico**. Isso fornece uma prova curta, uma interpretação física, uma generalização matemática e um teste empírico capaz de refutar o modelo.


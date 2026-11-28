# 

# Teorema da Transição Dupla (TD) \+ Lower Bounds LB1/LB2 — Doc. de desenvolvimento

# **Data: 15/10/2026 · Status: T1/LB1/LB2 (P) — provados aqui \+ checados por máquina (**teorema\_transicao\_dupla\_check.py**, sympy 1.14 \+ grade \+ seed 11;** out\_teorema\_td.json**, TUDO\_OK=True) · Nível 4:** pending **(sem auditor externo). Condicional a (A): fórmulas-ponte dos Eixos 1/2 (**FCT\_REFINAMENTO\_PREDITIVO.md **§1).**

# **O que se pretende provar: (i) que break-even e meia-mitigaç��o PFA×DFA têm forma fechada para qualquer razão de erro** q \= E\_pfa/p**, com a identidade de razão** ρ\_1/2 \= 4·ρ\***; (ii) um lower bound de mitigação (LB1) que reabilita o 0.25 com o significado correto; (iii) um lower bound de cascata (LB2): amplificação bullwhip cresce pelo menos linearmente em n. Nada aqui é lower bound de complexidade — ver §7 (non-claims).**

## 1\. Análise do projeto (vários ângulos)

1. # **Algébrico:** M(ρ) \= 1 − q²/√ρ **— toda a fenomenologia (dois modelos, três números 0.0625/0.25/0.706) colapsa num único parâmetro** q**. A forma** 1 − C/√ρ **explica *por que* a confusão era inevitável sem parametrizar.**

2. # **Analítico:** M′ \> 0**,** M → −∞ **em 0⁺ — unicidade de cada travessia é gratuita; o conteúdo real está nas condições de existência em \[0,1).**

3. # **Operacional:** ρ\_global \= 0.272 **cai exatamente na faixa onde os modelos discordam (A: \>50% mitigação; B: DFA suficiente) — a ambiguidade morde na prática.**

4. # **Estatístico: calibração ADV-003 mostrou estimadores com viés sistemático; este teorema não depende de estimação — é dedutivo a partir de (A).**

5. # **Complexidade: ponte L2→L3 segue aberta; nenhum lower bound aqui transfere para** Res(k)**/P-vs-NP. Qualquer leitura nesse sentido é proibida (§7).**

## 2\. Definições

# **Fixados** p \> 0 **(erro DFA),** e ≥ 0 **(erro PFA),** ρ ∈ (0,1)**:**

* # D(ρ) \= ρ/(1−ρ)·p² **(inflação DFA, Eixo 1),** F(ρ) \= √ρ/(1−ρ)·e² **(PFA, Eixo 4),**

* # M(ρ) \= (D−F)/D \= 1 − q²/√ρ**,** q \= e/p **(fator de mitigação, §2.3),**

* # **cascata (Eixo 2):** P⁽ⁿ⁾/P⁽⁰⁾ \= ∏\_{k=1}^{n}(1+a\_k)**,** a\_k \= ρ\_k/(1−ρ\_k)·p\_k² ≥ 0**.**

## 3\. Teorema TD (transição dupla parametrizada)

# **Teorema T1 (P). Seja** q ∈ (0,1)**. Então: (a) existe único break-even** ρ\* \= q⁴ **com** M(ρ\*) \= 0**; (b) existe único ponto de meia-mitigaç��o** ρ\_1/2 \= 4q⁴ **com** M \= 1/2**; (c) identidade de razão** ρ\_1/2 \= 4·ρ\***; (d)** 0 \< ρ\* \< ρ\_1/2 \< 1 ⟺ q \< 1/√2**; se** 1/√2 ≤ q \< 1**, o break-even existe mas a meia-mitigaç��o é inatingível em** \[0,1)**; se** q ≥ 1**, nem break-even há (PFA nunca vence).**

# **Prova.** M′(ρ) \= q²/(2ρ^{3/2}) \> 0 **(derivada checada no sympy), logo** M **estritamente crescente,** lim\_{ρ→0⁺} M \= −∞**,** M(1⁻) \= 1−q²**. Cada equação** M \= c \< 1−q² **tem no máximo uma solução;** M \= 0 ⟺ √ρ \= q² ⟺ ρ \= q⁴ **(única);** M \= 1/2 ⟺ q²/√ρ \= 1/2 ⟺ √ρ \= 2q² ⟺ ρ \= 4q⁴ **(única). (c) é imediato. (d):** 4q⁴ \< 1 ⟺ q⁴ \< 1/4 ⟺ q \< (1/4)^{1/4} \= 1/√2**; e** q⁴ ≥ 1 ⟺ q ≥ 1 **mata o break-even pois** M(1⁻) \= 1−q² ≤ 0 **com** M **crescente. ∎**

# **Corolário C1 (instâncias, P). Modelo A (**q \= 1/2**):** ρ\* \= 1/16 \= 0.0625**,** ρ\_1/2 \= 1/4 \= 0.25 **(o "ρ\_c do doc", agora com o nome certo). Modelo B (**q \= 1−r \= 11/12 ≈ 0.917 \> 1/√2**):** ρ\* \= (11/12)⁴ ≈ 0.7063 **existe, mas** ρ\_1/2 \= 4(11/12)⁴ ≈ 2.82 **é inatingível.**

# **Corolário C2 — cap assintótico (novo, P).** lim\_{ρ→1⁻} M \= 1−q²**: Modelo A tende a 75%; Modelo B a** 1−(11/12)² \= 23/144 ≈ 0.16**. Sob o Modelo B o PFA jamais passa de \~16% de mitigação — nem em saturação total.**

## 4\. Lower bound LB1 (mitigação mínima)

# **LB1 (P). Para** ρ ≥ ρ₀**:** M(ρ) ≥ 1 − q²/√ρ₀**.**

# **Prova. Monotonicidade de T1. ∎ Instância: Modelo A,** ρ ≥ 0.25 ⟹ M ≥ 0.5 **— o 0.25 do doc reabilitado com o significado correto: limiar de garantia (lower bound), não break-even.**

## 5\. Lower bound LB2 (cascata bullwhip aditiva)

# **LB2 (P). Para** a\_k ≥ 0**:** ∏\_{k=1}^{n}(1+a\_k) ≥ 1 \+ Σ\_{k=1}^{n} a\_k**.**

# **Prova (indução). Base** n=1 **igualdade. Passo: supondo para** n**,** ∏\_{k=1}^{n+1}(1+a\_k) ≥ (1+S\_n)(1+a\_{n+1}) \= 1+S\_n+a\_{n+1}+S\_n·a\_{n+1} ≥ 1+S\_{n+1}**, pois** S\_n·a\_{n+1} ≥ 0**. ∎ (Caso** n=3**: resto** ab+bc+ac+abc ≥ 0**, checado simbolicamente.)**

# **Corolário C3 (P).** P⁽ⁿ⁾/P⁽⁰⁾ ≥ 1 \+ Σ\_k ρ\_k/(1−ρ\_k)·p\_k²**; caso uniforme** ≥ 1 \+ n·ρ/(1−ρ)·p² **— a cascata cresce pelo menos linearmente em** n**. Ex.:** ρ \= 0.8**,** p \= 1/6**,** n \= 5 **⟹ inflação** ≥ 1+5·(4/36) ≈ 1.56 **(lower bound; o relato 2.07× é consistente, acima do piso).**

## 6\. Verificação por máquina

# teorema\_transicao\_dupla\_check.py**: derivada/resolução/razão/instâncias no sympy (exato); LB1 em grade 2000 pontos × 2 modelos × 6 âncoras (pior violação 0); LB2 em 3000 grades aleatórias (seed 11, pior 0.0) \+ forma exata** n=3**.** out\_teorema\_td.json**: TUDO\_OK=True. Teste** test\_teorema\_td.py **(5 testes).**

## 7\. Non-claims (proibido inferir)

* # **Nada aqui é lower bound de complexidade (**Res(k)**, DD\_P, P-vs-NP).**

* # **T1/LB1 condicionais às fórmulas-ponte (A) dos Eixos 1/4; LB2/C3 condicionais ao Eixo 2 (A). Se a ponte cair, o teorema cai junto (marcado, não escondido).**

* # **Nível 4** pending**: sem auditor externo; Lean formal futuro, não presente.**

## 8\. Próximos passos (estudo)

1. # **Conjectura (C): cascata PFA (Eixo 4 em** n **estágios com** √ρ\_k**) — lower bound análogo com** Σ √ρ\_k/(1−ρ\_k)·e\_k²**? Prova segue se a forma por estágio for** (1+b\_k) **com** b\_k ≥ 0 **(checar definição do estágio PFA).**

2. # **Formalizar T1/LB2 em Lean 4 (**lean/ **futuro).**

3. # **Auditoria externa do pacote (nível 4).**

4. # **Q-estendida:** q ≥ 1 **(PFA pior que DFA em toda carga) — caracterizar controladores degenerados; e sensibilidade** dρ\*/dq \= 4q³**.**

# **\=================================**

# **Avaliação científica do Teorema da Transição Dupla**

O trabalho está matematicamente coerente no núcleo algébrico e apresenta uma boa disciplina epistemológica ao separar resultados condicionais, verificações computacionais e *non-claims*. Porém, na forma atual, **T1, LB1 e LB2 ainda não sustentam, sozinhos, uma reivindicação forte de “novo teorema matemático”**. O caminho mais promissor é transformar o resultado em uma contribuição sobre o **modelo estrutural PFA×DFA**, provar rigorosamente as fórmulas-ponte e substituir a “transição dupla” por uma teoria completa de níveis de mitigação.

Minha conclusão preliminar é:

> **O conteúdo é correto como resultado dedutivo condicional. A originalidade potencial não está na álgebra de M(ρ)M(\\rho)M(ρ), nem na desigualdade LB2 isolada, mas na derivação e interpretação das fórmulas-ponte, na identificação do parâmetro adimensional q=e/pq=e/pq=e/p, na classificação completa dos regimes e, possivelmente, em uma extensão dinâmica/estocástica validada.**

---

## **1\. Parecer sintético**

### **O que já está sólido**

1. A redução  
    M(ρ)=D(ρ)−F(ρ)D(ρ)=1−q2ρ,q=epM(\\rho)=\\frac{D(\\rho)-F(\\rho)}{D(\\rho)} \=1-\\frac{q^2}{\\sqrt{\\rho}}, \\qquad q=\\frac epM(ρ)=D(ρ)D(ρ)−F(ρ)​=1−ρ​q2​,q=pe​  
    está correta.

2. A monotonicidade está correta:  
    M′(ρ)=q22ρ3/2\>0para q\>0,  ρ\>0.M'(\\rho)=\\frac{q^2}{2\\rho^{3/2}}\>0 \\quad\\text{para }q\>0,\\;\\rho\>0.M′(ρ)=2ρ3/2q2​\>0para q\>0,ρ\>0.  
3. O break-even  
    ρ∗=q4\\rho\_\*=q^4ρ∗​=q4  
    está correto quando 0\<q\<10\<q\<10\<q\<1.

4. O ponto de meia-mitigação  
    ρ1/2=4q4\\rho\_{1/2}=4q^4ρ1/2​=4q4  
    e a identidade  
    ρ1/2=4ρ∗\\rho\_{1/2}=4\\rho\_\*ρ1/2​=4ρ∗​  
    estão corretos.

5. A condição  
    ρ1/2\<1  ⟺  q\<12\\rho\_{1/2}\<1 \\iff q\<\\frac1{\\sqrt 2}ρ1/2​\<1⟺q\<2​1​  
    está correta.

6. LB1 é correto e, mais do que isso, é um **lower bound exato e ótimo**.

7. LB2 é correto para ak≥0a\_k\\geq 0ak​≥0.

8. Os *non-claims* estão adequados e devem ser mantidos.

---

## **2\. Correções e aprimoramentos necessários**

## **2.1 O domínio deve ser declarado com absoluta precisão**

Você usa simultaneamente:

ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1)

e expressões como “em \[0,1)\[0,1)\[0,1)”. Isso precisa ser uniformizado.

As funções originais

D(ρ)=ρ1−ρp2,F(ρ)=ρ1−ρe2D(\\rho)=\\frac{\\rho}{1-\\rho}p^2, \\qquad F(\\rho)=\\frac{\\sqrt\\rho}{1-\\rho}e^2D(ρ)=1−ρρ​p2,F(ρ)=1−ρρ​​e2

são naturalmente definidas em (0,1)(0,1)(0,1). Em ρ=0\\rho=0ρ=0, ambas valem formalmente zero se estendidas por continuidade, mas o quociente

M(ρ)=D−FDM(\\rho)=\\frac{D-F}{D}M(ρ)=DD−F​

não está definido porque D(0)=0D(0)=0D(0)=0.

Portanto, a formulação recomendada é:

> Para p\>0p\>0p\>0, e≥0e\\geq 0e≥0 e ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1), definimos D,FD,FD,F e MMM. Eventuais afirmações em ρ=0\\rho=0ρ=0 ou ρ=1\\rho=1ρ=1 referem-se exclusivamente a limites laterais.

---

## **2.2 Há um caso degenerado importante: q=0q=0q=0**

O teorema assume q∈(0,1)q\\in(0,1)q∈(0,1), o que exclui e=0e=0e=0. Isso é aceitável, mas o caso deve ser classificado.

Se q=0q=0q=0, então

F(ρ)=0,M(ρ)=1F(\\rho)=0,\\qquad M(\\rho)=1F(ρ)=0,M(ρ)=1

para todo ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1).

Logo:

* não há break-even interior;  
* o PFA elimina integralmente o custo modelado por FFF;  
* qualquer alvo c\<1c\<1c\<1 é satisfeito para toda carga admissível.

Esse caso deve aparecer como regime degenerado ou perfeito.

---

## **2.3 O caso q=1q=1q=1 merece formulação separada**

No texto atual:

> “se q≥1q\\geq1q≥1, nem break-even há”.

Isto está correto **para break-even interior em(0,1)(0,1)(0,1)**. Mas em q=1q=1q=1,

ρ∗=q4=1\\rho\_\*=q^4=1ρ∗​=q4=1

é uma solução apenas na fronteira formal, onde DDD e FFF divergem. Além disso,

M(ρ)=1−1ρ\<0M(\\rho)=1-\\frac1{\\sqrt\\rho}\<0M(ρ)=1−ρ​1​\<0

para todo ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1), embora

lim⁡ρ→1−M(ρ)=0.\\lim\_{\\rho\\to1^-}M(\\rho)=0.ρ→1−lim​M(ρ)=0.

A formulação mais precisa seria:

* se q=1q=1q=1, não existe break-even interior; há somente empate assintótico na fronteira ρ→1−\\rho\\to1^-ρ→1−;  
* se q\>1q\>1q\>1, o PFA é estritamente pior que o DFA em todo (0,1)(0,1)(0,1), inclusive no limite, pois lim⁡ρ→1−M(ρ)=1−q2\<0.\\lim\_{\\rho\\to1^-}M(\\rho)=1-q^2\<0.ρ→1−lim​M(ρ)=1−q2\<0.

---

## **2.4 Um pequeno ajuste lógico na prova de T1**

Você escreve:

> Cada equação M=c\<1−q2M=c\<1-q^2M=c\<1−q2 tem no máximo uma solução.

A monotonicidade fornece “no máximo uma”. Para garantir existência em (0,1)(0,1)(0,1), o intervalo correto da imagem é:

M((0,1))=(−∞,1−q2).M((0,1))=(-\\infty,1-q^2).M((0,1))=(−∞,1−q2).

Logo, a afirmação completa é:

M(ρ)=cM(\\rho)=cM(ρ)=c

tem exatamente uma solução em (0,1)(0,1)(0,1) se, e somente se,

c\<1−q2.c\<1-q^2.c\<1−q2.

Se c=1−q2c=1-q^2c=1−q2, o valor é apenas atingido no limite ρ→1−\\rho\\to1^-ρ→1−, não no domínio.

Essa observação conduz diretamente a uma generalização muito mais forte.

---

# **3\. Principal avanço recomendado: Teorema Geral de Limiar**

A “transição dupla” é, na realidade, uma instância de uma família contínua de transições. Isso permite substituir dois pontos especiais por uma caracterização completa.

## **Teorema TG, transição em nível arbitrário**

Sejam q\>0q\>0q\>0, ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1) e

Mq(ρ)=1−q2ρ.M\_q(\\rho)=1-\\frac{q^2}{\\sqrt\\rho}.Mq​(ρ)=1−ρ​q2​.

Para qualquer nível de mitigação c\<1c\<1c\<1, a equação

Mq(ρ)=cM\_q(\\rho)=cMq​(ρ)=c

possui solução formal única

ρc(q)=q4(1−c)2.\\boxed{\\rho\_c(q)=\\frac{q^4}{(1-c)^2}}.ρc​(q)=(1−c)2q4​​.

Essa solução pertence a (0,1)(0,1)(0,1) se, e somente se,

q\<1−c.\\boxed{q\<\\sqrt{1-c}}.q\<1−c​​.

### **Prova**

Mq(ρ)=c  ⟺  1−q2ρ=cM\_q(\\rho)=c \\iff 1-\\frac{q^2}{\\sqrt\\rho}=cMq​(ρ)=c⟺1−ρ​q2​=c   ⟺  q2ρ=1−c  ⟺  ρ=q21−c.\\iff \\frac{q^2}{\\sqrt\\rho}=1-c \\iff \\sqrt\\rho=\\frac{q^2}{1-c}.⟺ρ​q2​=1−c⟺ρ​=1−cq2​.

Como c\<1c\<1c\<1, o denominador é positivo. Elevando ao quadrado:

ρ=q4(1−c)2.\\rho=\\frac{q^4}{(1-c)^2}.ρ=(1−c)2q4​.

A unicidade decorre da monotonicidade estrita de MqM\_qMq​. Finalmente,

ρc(q)\<1  ⟺  q4(1−c)2\<1  ⟺  q2\<1−c  ⟺  q\<1−c.\\rho\_c(q)\<1 \\iff \\frac{q^4}{(1-c)^2}\<1 \\iff q^2\<1-c \\iff q\<\\sqrt{1-c}.ρc​(q)\<1⟺(1−c)2q4​\<1⟺q2\<1−c⟺q\<1−c​.

∎

---

## **3.1 T1 passa a ser corolário**

* Para c=0c=0c=0:  
   ρ0=q4=ρ∗.\\rho\_0=q^4=\\rho\_\*.ρ0​=q4=ρ∗​.  
* Para c=12c=\\frac12c=21​:  
   ρ1/2=q4(1/2)2=4q4.\\rho\_{1/2} \=\\frac{q^4}{(1/2)^2} \=4q^4.ρ1/2​=(1/2)2q4​=4q4.  
* Portanto:  
   ρcρ∗=1(1−c)2.\\frac{\\rho\_c}{\\rho\_\*} \=\\frac1{(1-c)^2}.ρ∗​ρc​​=(1−c)21​.

A identidade 444 deixa de parecer um fato isolado e passa a ser o caso c=1/2c=1/2c=1/2 da lei universal

ρcρ∗=1(1−c)2.\\boxed{\\frac{\\rho\_c}{\\rho\_\*}=\\frac1{(1-c)^2}}.ρ∗​ρc​​=(1−c)21​​.

Essa é uma apresentação matematicamente muito melhor.

---

## **3.2 Classificação completa dos regimes**

Para um alvo c∈\[0,1)c\\in\[0,1)c∈\[0,1):

### **Regime I: alcançável**

0≤q\<1−c.0\\le q\<\\sqrt{1-c}.0≤q\<1−c​.

Existe ρc∈(0,1)\\rho\_c\\in(0,1)ρc​∈(0,1) e:

Mq(ρ)≥c  ⟺  ρ≥ρc(q).M\_q(\\rho)\\ge c \\iff \\rho\\ge\\rho\_c(q).Mq​(ρ)≥c⟺ρ≥ρc​(q).

### **Regime II: crítico assintótico**

q=1−c.q=\\sqrt{1-c}.q=1−c​.

Então:

ρc=1,\\rho\_c=1,ρc​=1,

mas o alvo não é atingido em (0,1)(0,1)(0,1). Apenas:

lim⁡ρ→1−Mq(ρ)=c.\\lim\_{\\rho\\to1^-}M\_q(\\rho)=c.ρ→1−lim​Mq​(ρ)=c.

### **Regime III: inalcançável**

q\>1−c.q\>\\sqrt{1-c}.q\>1−c​.

Nesse caso:

Mq(ρ)\<cM\_q(\\rho)\<cMq​(ρ)\<c

para todo ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1).

Isso proporciona uma verdadeira **classificação de fase do modelo**, mesmo que a palavra “fase” deva ser usada com cautela para não sugerir uma transição física.

---

# **4\. Uma formulação ainda mais geral**

A estrutura não depende especificamente dos expoentes 111 e 1/21/21/2.

Considere:

D(ρ)=Aρα1−ρ,F(ρ)=Bρβ1−ρ,D(\\rho)=A\\frac{\\rho^\\alpha}{1-\\rho}, \\qquad F(\\rho)=B\\frac{\\rho^\\beta}{1-\\rho},D(ρ)=A1−ρρα​,F(ρ)=B1−ρρβ​,

com A,B\>0A,B\>0A,B\>0 e α\>β\\alpha\>\\betaα\>β. Então:

M(ρ)=1−BAρβ−α.M(\\rho) \= 1-\\frac BA\\rho^{\\beta-\\alpha}.M(ρ)=1−AB​ρβ−α.

Definindo

δ=α−β\>0,κ=BA,\\delta=\\alpha-\\beta\>0, \\qquad \\kappa=\\frac BA,δ=α−β\>0,κ=AB​,

obtemos

M(ρ)=1−κρ−δ.M(\\rho)=1-\\kappa\\rho^{-\\delta}.M(ρ)=1−κρ−δ.

Para um alvo c\<1c\<1c\<1:

M(ρ)=c  ⟺  ρc=(κ1−c)1/δ.M(\\rho)=c \\iff \\rho\_c= \\left(\\frac{\\kappa}{1-c}\\right)^{1/\\delta}.M(ρ)=c⟺ρc​=(1−cκ​)1/δ.

No seu modelo:

A=p2,B=e2,α=1,β=12,A=p^2,\\quad B=e^2,\\quad \\alpha=1,\\quad\\beta=\\frac12,A=p2,B=e2,α=1,β=21​,

logo:

δ=12,κ=q2,\\delta=\\frac12,\\qquad \\kappa=q^2,δ=21​,κ=q2,

e, consequentemente,

ρc=(q21−c)2=q4(1−c)2.\\rho\_c \= \\left(\\frac{q^2}{1-c}\\right)^2 \= \\frac{q^4}{(1-c)^2}.ρc​=(1−cq2​)2=(1−c)2q4​.

## **Por que essa extensão é importante**

Ela mostra que:

* o expoente 444 vem da diferença de escala α−β=12;\\alpha-\\beta=\\frac12;α−β=21​;  
* o fator 444 da meia-mitigação vem do nível c=1/2c=1/2c=1/2;  
* a geometria do limiar depende da diferença entre os expoentes de carga;  
* o cancelamento de 1−ρ1-\\rho1−ρ é estrutural e deve ser explicitamente justificado pela modelagem.

Esta extensão tem mais potencial de originalidade do que T1 isolado.

---

# **5\. Avaliação de LB1**

Seu LB1 diz:

ρ≥ρ0⟹M(ρ)≥1−q2ρ0.\\rho\\ge\\rho\_0 \\Longrightarrow M(\\rho)\\ge 1-\\frac{q^2}{\\sqrt{\\rho\_0}}.ρ≥ρ0​⟹M(ρ)≥1−ρ0​​q2​.

Está correto. Mas pode ser fortalecido na apresentação.

## **Proposição LB1, forma ótima**

Para todo q≥0q\\ge0q≥0 e ρ0∈(0,1)\\rho\_0\\in(0,1)ρ0​∈(0,1),

inf⁡ρ∈\[ρ0,1)Mq(ρ)=Mq(ρ0)=1−q2ρ0.\\inf\_{\\rho\\in\[\\rho\_0,1)} M\_q(\\rho) \= M\_q(\\rho\_0) \= 1-\\frac{q^2}{\\sqrt{\\rho\_0}}.ρ∈\[ρ0​,1)inf​Mq​(ρ)=Mq​(ρ0​)=1−ρ0​​q2​.

Portanto:

Mq(ρ)≥1−q2ρ0\\boxed{ M\_q(\\rho)\\ge 1-\\frac{q^2}{\\sqrt{\\rho\_0}} }Mq​(ρ)≥1−ρ0​​q2​​

é o melhor lower bound uniforme possível para ρ≥ρ0\\rho\\ge\\rho\_0ρ≥ρ0​.

### **Observação importante**

O bound pode ser negativo. Assim, “lower bound de mitigação” não significa automaticamente “garantia de mitigação positiva”.

A garantia é positiva se:

1−q2ρ0\>0  ⟺  ρ0\>q4.1-\\frac{q^2}{\\sqrt{\\rho\_0}}\>0 \\iff \\rho\_0\>q^4.1−ρ0​​q2​\>0⟺ρ0​\>q4.

E garante pelo menos ccc se:

ρ0≥q4(1−c)2.\\rho\_0\\ge\\frac{q^4}{(1-c)^2}.ρ0​≥(1−c)2q4​.

Isso integra LB1 diretamente ao Teorema Geral de Limiar.

---

# **6\. Avaliação de LB2**

A desigualdade

∏k=1n(1+ak)≥1+∑k=1nak\\prod\_{k=1}^n(1+a\_k) \\ge 1+\\sum\_{k=1}^n a\_kk=1∏n​(1+ak​)≥1+k=1∑n​ak​

para ak≥0a\_k\\ge0ak​≥0 é correta. Entretanto, trata-se de uma desigualdade elementar da família de Bernoulli e das expansões por polinômios simétricos não negativos; não deve ser apresentada como novidade matemática isolada. A desigualdade clássica de Bernoulli já fornece, no caso uniforme, (1+a)n≥1+na(1+a)^n\\ge1+na(1+a)n≥1+na, e existem generalizações amplamente estudadas. [\[en.wikipedia.org\]](https://en.wikipedia.org/wiki/Bernoulli%27s_inequality), [\[faculty.fiu.edu\]](https://faculty.fiu.edu/~decarlil/Preprints/FinalBern1.pdf), [\[files.ele-math.com\]](https://files.ele-math.com/articles/jmi-02-10.pdf)

Na literatura de bullwhip, já existem lower bounds associados a previsão, lead time e cadeias multiestágio. O artigo de Frank Chen, Zvi Drezner, Jennifer K. Ryan e David Simchi-Levi quantifica o efeito em cadeias simples e estende a análise para múltiplos estágios. Portanto, qualquer reivindicação de originalidade para LB2 precisa ser comparada explicitamente com essa linha de trabalhos. [\[jstor.org\]](https://www.jstor.org/stable/2634741), [\[dsl.mit.edu\]](https://dsl.mit.edu/biblio/quantifying-bullwhip-effect-simple-supply-chain-impact-forecasting-lead-times-and-information/), [\[scholars.c...tyu.edu.hk\]](https://scholars.cityu.edu.hk/en/publications/quantifying-the-bullwhip-effect-in-a-simple-supply-chain-the-impa/)

O efeito bullwhip é normalmente definido por uma razão de variâncias, não simplesmente por um produto abstrato de fatores. Essa distinção conceitual precisa ser resolvida na fórmula-ponte do Eixo 2\. [\[arxiv.org\]](https://arxiv.org/pdf/1009.3977), [\[link.springer.com\]](https://link.springer.com/content/pdf/10.1007/978-3-319-32441-8_1.pdf)

---

## **6.1 Forma exata de LB2**

A expansão completa é:

∏k=1n(1+ak)=1+∑iai+∑i\<jaiaj+∑i\<j\<ℓaiajaℓ+⋯+∏i=1nai.\\prod\_{k=1}^n(1+a\_k) \= 1+ \\sum\_i a\_i+ \\sum\_{i\<j}a\_i a\_j+ \\sum\_{i\<j\<\\ell}a\_i a\_j a\_\\ell+ \\cdots+ \\prod\_{i=1}^n a\_i.k=1∏n​(1+ak​)=1+i∑​ai​+i\<j∑​ai​aj​+i\<j\<ℓ∑​ai​aj​aℓ​+⋯+i=1∏n​ai​.

Assim:

∏k=1n(1+ak)−(1+∑k=1nak)=∑r=2ner(a1,…,an),\\prod\_{k=1}^n(1+a\_k) \- \\left(1+\\sum\_{k=1}^n a\_k\\right) \= \\sum\_{r=2}^n e\_r(a\_1,\\ldots,a\_n),k=1∏n​(1+ak​)−(1+k=1∑n​ak​)=r=2∑n​er​(a1​,…,an​),

onde ere\_rer​ é o polinômio simétrico elementar de grau rrr.

Como todos os ak≥0a\_k\\ge0ak​≥0,

er(a1,…,an)≥0.e\_r(a\_1,\\ldots,a\_n)\\ge0.er​(a1​,…,an​)≥0.

Isso fornece uma prova mais informativa que a indução, pois identifica exatamente o termo descartado.

---

## **6.2 Condição de igualdade**

A igualdade em LB2 ocorre se, e somente se, não há dois índices distintos com valores positivos:

∏k=1n(1+ak)=1+∑k=1nak\\prod\_{k=1}^n(1+a\_k) \= 1+\\sum\_{k=1}^n a\_kk=1∏n​(1+ak​)=1+k=1∑n​ak​

se, e somente se,

aiaj=0para todo i≠j.a\_i a\_j=0 \\quad\\text{para todo }i\\ne j.ai​aj​=0para todo i=j.

Equivalentemente, no máximo um dos aka\_kak​ é não nulo.

Esse critério deve ser acrescentado.

---

## **6.3 “Pelo menos linear” exige cuidado**

Para uma família arbitrária ak≥0a\_k\\ge0ak​≥0, LB2 fornece:

P(n)P(0)≥1+∑k=1nak.\\frac{P^{(n)}}{P^{(0)}}\\ge1+\\sum\_{k=1}^n a\_k.P(0)P(n)​≥1+k=1∑n​ak​.

Mas isso **não implica crescimento linear em nnn** sem uma hipótese adicional.

Por exemplo, se:

ak=1k2,a\_k=\\frac1{k^2},ak​=k21​,

então:

∑k=1nak\\sum\_{k=1}^n a\_kk=1∑n​ak​

permanece limitada quando n→∞n\\to\\inftyn→∞. Portanto, nesse caso, LB2 não fornece um lower bound linear em nnn.

A afirmação correta é uma destas:

### **Caso uniforme**

Se ak=a\>0a\_k=a\>0ak​=a\>0, então:

∏k=1n(1+ak)=(1+a)n≥1+na.\\prod\_{k=1}^n(1+a\_k) \=(1+a)^n \\ge1+na.k=1∏n​(1+ak​)=(1+a)n≥1+na.

### **Piso uniforme**

Se existe a‾\>0\\underline a\>0a​\>0 tal que:

ak≥a‾a\_k\\ge\\underline aak​≥a​

para todo kkk, então:

∏k=1n(1+ak)≥(1+a‾)n≥1+na‾.\\prod\_{k=1}^n(1+a\_k) \\ge (1+\\underline a)^n \\ge 1+n\\underline a.k=1∏n​(1+ak​)≥(1+a​)n≥1+na​.

Esse resultado é, na verdade, exponencial, não apenas linear.

### **Média inferior**

Se:

1n∑k=1nak≥aˉ\>0,\\frac1n\\sum\_{k=1}^n a\_k\\ge\\bar a\>0,n1​k=1∑n​ak​≥aˉ\>0,

então:

∏k=1n(1+ak)≥1+naˉ.\\prod\_{k=1}^n(1+a\_k) \\ge 1+n\\bar a.k=1∏n​(1+ak​)≥1+naˉ.

Portanto, recomendo substituir:

> “a cascata cresce pelo menos linearmente em nnn”

por:

> “no caso uniforme, ou mais geralmente quando a média dos incrementos possui piso positivo independente de nnn, o fator de cascata admite um lower bound linear em nnn. Sob um piso estágio a estágio estritamente positivo, obtém-se o lower bound exponencial (1+a‾)n(1+\\underline a)^n(1+a​)n.”

---

# **7\. Checagem do exemplo numérico**

Para

ρ=0.8,p=16,\\rho=0.8,\\qquad p=\\frac16,ρ=0.8,p=61​,

temos:

a=0.80.2136=4⋅136=19.a=\\frac{0.8}{0.2}\\frac1{36} \=4\\cdot\\frac1{36} \=\\frac19.a=0.20.8​361​=4⋅361​=91​.

Para n=5n=5n=5:

1+na=1+59=149≈1.5556.1+na \= 1+\\frac59 \= \\frac{14}{9} \\approx1.5556.1+na=1+95​=914​≈1.5556.

O fator exato do modelo multiplicativo uniforme é:

(1+a)5=(109)5≈1.6935.(1+a)^5 \= \\left(\\frac{10}{9}\\right)^5 \\approx1.6935.(1+a)5=(910​)5≈1.6935.

Assim:

* lower bound aditivo: 1.55561.55561.5556;  
* valor exato do modelo apresentado: 1.69351.69351.6935;  
* relato externo: 2.072.072.07.

O valor 2.072.072.07 é consistente apenas no sentido de estar acima do lower bound. Mas ele **não é produzido pelo modelo multiplicativo uniforme com esses parâmetros**. Isso deve ser declarado.

Se o relato 2.072.072.07 é uma observação ou simulação, há um excesso de amplificação de aproximadamente:

2.071.6935−1≈22.2%.\\frac{2.07}{1.6935}-1 \\approx22.2\\%.1.69352.07​−1≈22.2%.

Isso sugere fatores adicionais ausentes de aka\_kak​, como heterogeneidade, correlação, realimentação, lead time ou estimação dinâmica.

---

# **8\. Robustez sob incerteza paramétrica**

Como o projeto reporta viés de estimação, uma extensão útil é produzir bounds robustos.

Suponha:

q∈\[q−,q+\],ρ∈\[ρ−,ρ+\].q\\in\[q\_-,q\_+\], \\qquad \\rho\\in\[\\rho\_-,\\rho\_+\].q∈\[q−​,q+​\],ρ∈\[ρ−​,ρ+​\].

Como MMM é decrescente em qqq e crescente em ρ\\rhoρ,

∂M∂q=−2qρ\<0,\\frac{\\partial M}{\\partial q} \= \-\\frac{2q}{\\sqrt\\rho}\<0,∂q∂M​=−ρ​2q​\<0,

temos:

1−q+2ρ−≤M(q,ρ)≤1−q−2ρ+.\\boxed{ 1-\\frac{q\_+^2}{\\sqrt{\\rho\_-}} \\le M(q,\\rho) \\le 1-\\frac{q\_-^2}{\\sqrt{\\rho\_+}} }.1−ρ−​​q+2​​≤M(q,ρ)≤1−ρ+​​q−2​​​.

Esse é um certificado robusto muito mais relevante operacionalmente do que testar uma grade de valores pontuais.

## **Garantia robusta de alvo ccc**

Para garantir:

M(q,ρ)≥cM(q,\\rho)\\ge cM(q,ρ)≥c

para todo q≤q+q\\le q\_+q≤q+​, basta impor:

ρ≥q+4(1−c)2.\\rho\\ge \\frac{q\_+^4}{(1-c)^2}.ρ≥(1−c)2q+4​​.

Isso converte incerteza de calibração em requisito operacional verificável.

---

# **9\. Sensibilidade**

Você já propôs:

dρ∗dq=4q3.\\frac{d\\rho\_\*}{dq}=4q^3.dqdρ∗​​=4q3.

Para o alvo geral ccc:

ρc(q)=q4(1−c)2.\\rho\_c(q)=\\frac{q^4}{(1-c)^2}.ρc​(q)=(1−c)2q4​.

Portanto:

∂ρc∂q=4q3(1−c)2,\\frac{\\partial\\rho\_c}{\\partial q} \= \\frac{4q^3}{(1-c)^2},∂q∂ρc​​=(1−c)24q3​,

e

∂ρc∂c=2q4(1−c)3.\\frac{\\partial\\rho\_c}{\\partial c} \= \\frac{2q^4}{(1-c)^3}.∂c∂ρc​​=(1−c)32q4​.

A segunda derivada em ccc é:

∂2ρc∂c2=6q4(1−c)4\>0.\\frac{\\partial^2\\rho\_c}{\\partial c^2} \= \\frac{6q^4}{(1-c)^4}\>0.∂c2∂2ρc​​=(1−c)46q4​\>0.

Isso mostra que o custo em carga para buscar níveis mais altos de mitigação cresce de maneira convexa e diverge quando c→1−c\\to1^-c→1−.

Uma propriedade especialmente elegante é a elasticidade:

qρc∂ρc∂q=4.\\frac{q}{\\rho\_c}\\frac{\\partial\\rho\_c}{\\partial q}=4.ρc​q​∂q∂ρc​​=4.

Logo:

> Um aumento relativo de 1%1\\%1% em qqq produz aproximadamente 4%4\\%4% de aumento no limiar ρc\\rho\_cρc​, independentemente do nível ccc.

Essa é uma interpretação forte e comunicável.

---

# **10\. Potencial de originalidade**

## **10.1 O que provavelmente não é novo isoladamente**

* resolver 1−q2/ρ=c1-q^2/\\sqrt\\rho=c1−q2/ρ​=c;  
* demonstrar monotonicidade;  
* provar ∏(1+ak)≥1+∑ak;\\prod(1+a\_k)\\ge1+\\sum a\_k;∏(1+ak​)≥1+∑ak​;  
* verificar casos em SymPy;  
* observar que um produto uniforme possui lower bound linear.

A própria literatura de bullwhip já contém quantificações, modelos multiestágio e lower bounds associados a previsões e lead times. [\[jstor.org\]](https://www.jstor.org/stable/2634741), [\[scholars.c...tyu.edu.hk\]](https://scholars.cityu.edu.hk/en/publications/quantifying-the-bullwhip-effect-in-a-simple-supply-chain-the-impa/), [\[arxiv.org\]](https://arxiv.org/pdf/2604.13478)

Além disso, a literatura ressalta que fórmulas explícitas de bullwhip dependem fortemente do processo de demanda, da política de previsão e das hipóteses do modelo; em modelos ARMA, por exemplo, fórmulas fechadas podem ser difíceis e específicas. [\[arxiv.org\]](https://arxiv.org/pdf/1009.3977)

## **10.2 Onde pode existir contribuição original**

### **A. Derivação das pontes**

Se for possível demonstrar, a partir de um sistema bem definido, que:

D(ρ)=ρ1−ρp2D(\\rho)=\\frac{\\rho}{1-\\rho}p^2D(ρ)=1−ρρ​p2

e

F(ρ)=ρ1−ρe2,F(\\rho)=\\frac{\\sqrt\\rho}{1-\\rho}e^2,F(ρ)=1−ρρ​​e2,

então a redução para q=e/pq=e/pq=e/p pode constituir uma contribuição estrutural.

### **B. Lei universal de níveis**

A formulação

ρc(q)=q4(1−c)2\\rho\_c(q)=\\frac{q^4}{(1-c)^2}ρc​(q)=(1−c)2q4​

e a classificação alcançável/crítico/inalcançável são mais fortes que a transição dupla.

### **C. Teorema geral por expoentes**

A família:

D=Aρα1−ρ,F=Bρβ1−ρD=A\\frac{\\rho^\\alpha}{1-\\rho}, \\qquad F=B\\frac{\\rho^\\beta}{1-\\rho}D=A1−ρρα​,F=B1−ρρβ​

com classificação por α−β\\alpha-\\betaα−β pode ter valor como resultado abstrato de comparação de controladores.

### **D. Teoria robusta**

Bounds sob incerteza em qqq, ρ\\rhoρ, correlações e erros de calibração podem produzir uma contribuição nova e aplicável.

### **E. Cascatas heterogêneas**

Uma extensão com qk,ρk,pk,ekq\_k,\\rho\_k,p\_k,e\_kqk​,ρk​,pk​,ek​ por estágio e critérios globais de dominância pode ser substancialmente mais interessante.

---

# **11\. O maior risco científico: as fórmulas-ponte**

Atualmente, T1 é essencialmente uma consequência imediata das definições. Portanto, a pergunta científica determinante não é:

> “A álgebra de T1 está correta?”

Ela está.

A pergunta central é:

> “Por que os custos ou erros reais de DFA e PFA obedecem exatamente às leis ρ/(1−ρ)\\rho/(1-\\rho)ρ/(1−ρ) e ρ/(1−ρ)\\sqrt\\rho/(1-\\rho)ρ​/(1−ρ)?”

É preciso provar ou justificar:

1. o significado operacional de ρ\\rhoρ;  
2. as unidades de DDD e FFF;  
3. por que p2p^2p2 e e2e^2e2 aparecem;  
4. por que ambos compartilham o denominador 1−ρ1-\\rho1−ρ;  
5. por que o PFA escala como ρ\\sqrt\\rhoρ​;  
6. se eee e ppp permanecem constantes quando ρ\\rhoρ varia;  
7. se os estágios são independentes;  
8. por que a cascata é multiplicativa;  
9. se os fatores aka\_kak​ agem sobre variância, erro quadrático, probabilidade ou custo;  
10. como a grandeza se relaciona com a definição padrão de bullwhip como razão de variâncias.

A literatura consolidada trata o bullwhip como amplificação da variabilidade de demanda ou de pedidos ao longo da cadeia, e modelos clássicos dependem de políticas de reposição, previsão e lead time. [\[jstor.org\]](https://www.jstor.org/stable/2634741), [\[link.springer.com\]](https://link.springer.com/content/pdf/10.1007/978-3-319-32441-8_1.pdf)

Sem essa ponte, o trabalho permanece um teorema correto sobre uma função definida ad hoc.

---

# **12\. Verificação computacional: o que ela prova e o que não prova**

Os testes relatados são úteis para:

* detectar erros de implementação;  
* conferir derivadas simbólicas;  
* comparar expressões exatas;  
* testar exemplos;  
* prevenir regressões.

Mas:

* grade de 2.000 pontos não prova LB1;  
* 3.000 amostras aleatórias não provam LB2;  
* `TUDO_OK=True` não estabelece validade matemática;  
* seed fixa garante reprodutibilidade, não completude.

Como já há provas analíticas, recomendo classificar os artefatos assim:

Plain Text  
proof\_status:  
analytic\_proof: complete  
symbolic\_cross\_check: passed  
numerical\_regression\_tests: passed  
formal\_proof\_assistant: pending  
external\_audit: pending

Isso evita dizer “provado por máquina” antes da formalização em Lean.

A expressão mais adequada seria:

> “Provado analiticamente e verificado simbolicamente/computacionalmente.”

---

# **13\. Plano de desenvolvimento recomendado**

## **P0: corrigir o documento atual**

1. Fixar o domínio em ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1).  
2. Separar q=0q=0q=0, 0\<q\<10\<q\<10\<q\<1, q=1q=1q=1 e q\>1q\>1q\>1.  
3. Trocar T1 pelo Teorema Geral de Limiar.  
4. Rebaixar TD a corolário para c=0c=0c=0 e c=1/2c=1/2c=1/2.  
5. Declarar LB1 como bound ótimo.  
6. Acrescentar a condição de igualdade de LB2.  
7. Corrigir “linear em nnn” mediante hipótese de piso ou média positiva.  
8. Distinguir o lower bound 1.55561.55561.5556 do valor exato 1.69351.69351.6935.

## **P1: provar as fórmulas-ponte**

Criar um documento separado:

Plain Text  
AXIOMAS\_E\_DERIVACAO\_DAS\_PONTES.md

Com:

* variáveis primitivas;  
* unidades;  
* hipóteses probabilísticas;  
* processo gerador;  
* definição dos erros;  
* derivação de DDD;  
* derivação de FFF;  
* derivação do produto da cascata;  
* condições de validade;  
* regimes em que a aproximação falha.

## **P2: formalização**

Formalizar primeiro o núcleo abstrato:

Lean  
def mitigation (q ρ : ℝ) : ℝ :=  
1 \- q^2 / Real.sqrt ρ

Ordem sugerida:

1. positividade da raiz;  
2. monotonicidade em ρ\\rhoρ;  
3. solução de `mitigation q ρ = c`;  
4. condição ρc∈(0,1)\\rho\_c\\in(0,1)ρc​∈(0,1);  
5. T1 como corolário;  
6. LB1;  
7. expansão/prova indutiva de LB2;  
8. condição de igualdade;  
9. resultado para piso uniforme.

## **P3: pesquisa de anterioridade**

Executar buscas por:

* comparação de leis de escala ρ\\rhoρ versus ρ\\sqrt\\rhoρ​;  
* limiares de mitigação em controladores;  
* modelos multiplicativos multiestágio;  
* lower bounds de bullwhip;  
* efeitos de previsão e lead time;  
* classificação paramétrica de controladores.

A busca inicial já mostra que lower bounds de bullwhip e extensões multiestágio são uma área estabelecida. [\[jstor.org\]](https://www.jstor.org/stable/2634741), [\[scholars.c...tyu.edu.hk\]](https://scholars.cityu.edu.hk/en/publications/quantifying-the-bullwhip-effect-in-a-simple-supply-chain-the-impa/), [\[link.springer.com\]](https://link.springer.com/content/pdf/10.1007/978-3-319-32441-8_1.pdf)

## **P4: validação**

Comparar o modelo contra:

* simulação Monte Carlo;  
* cadeias heterogêneas;  
* processos AR(1), ARMA e demanda não estacionária;  
* erros correlacionados;  
* lead times variáveis;  
* parâmetros estimados;  
* dados observacionais, se existirem.

Trabalhos recentes continuam apontando a importância de benchmarks multiestágio, múltiplas métricas e comparação com dados reais, o que reforça a necessidade de validação além de uma fórmula fechada. [\[arxiv.org\]](https://arxiv.org/pdf/2604.13478)

---

# **14\. Formulação recomendada da contribuição**

Uma reivindicação cientificamente defensável seria:

> Introduzimos uma redução adimensional para uma classe de modelos comparativos PFA×DFA cujas penalidades compartilham uma singularidade de saturação, mas possuem diferentes expoentes de carga. Provamos uma lei fechada para o limiar de qualquer nível de mitigação, classificamos os regimes alcançável, crítico e inalcançável, derivamos certificados robustos sob incerteza paramétrica e estabelecemos limites de cascata sob hipóteses explícitas de composição multiplicativa.

Essa formulação é mais forte e mais segura que:

> “Descobrimos um novo lower bound bullwhip.”

---

# **15\. Veredito final**

## **Estado matemático**

**Correto, com pequenos ajustes de domínio e formulação.**

## **Estado de originalidade**

**Ainda não demonstrado.**

## **Elementos provavelmente elementares ou conhecidos**

* T1 na forma atual;  
* LB1 como monotonicidade;  
* LB2 como inequação de produto/Bernoulli.

## **Elementos com potencial real**

* derivação das fórmulas-ponte;  
* redução adimensional por qqq;  
* teorema para nível arbitrário ccc;  
* generalização por expoentes α,β\\alpha,\\betaα,β;  
* robustez sob incerteza;  
* cascata heterogênea ligada a uma definição operacional verificável.

## **Decisão científica recomendada**

> **Continuar o projeto, mas reposicionar a novidade.** O próximo esforço não deve ser criar mais testes numéricos para T1/LB2. Deve ser provar a ponte do modelo, generalizar T1 para níveis arbitrários, fortalecer as hipóteses da cascata e realizar uma pesquisa de anterioridade focada.

A principal mudança foi separar rigorosamente três camadas que estavam parcialmente misturadas: **álgebra correta**, **validade do modelo** e **originalidade científica**. Também transformei a transição dupla em uma lei geral de limiares, corrigi a interpretação assintótica de q=1q=1q=1 e delimitei quando LB2 realmente implica crescimento linear.

\===========================================================================

# **Teorema Geral de Limiar e Lower Bounds de Cascata**

## **Documento de desenvolvimento e auditoria das fórmulas-ponte dos Eixos 1/2**

**Data:** 15/10/2026  
 **Status matemático:** núcleo algébrico provado analiticamente; verificações simbólicas e numéricas disponíveis  
 **Status das fórmulas-ponte:** Eixo 1 plausível sob hipóteses explícitas, mas ainda não derivado de um modelo primitivo; Eixo 2 correto como identidade de composição somente se os fatores locais forem razões compatíveis da mesma grandeza  
 **Status de originalidade:** em investigação  
 **Formalização Lean 4:** pendente  
 **Auditoria externa:** pendente

---

## **Resumo executivo**

Este documento estuda a comparação entre dois mecanismos, denominados DFA e PFA, sob uma variável de carga

ρ∈(0,1).\\rho\\in(0,1).ρ∈(0,1).

Adotam-se, condicionalmente, as fórmulas

D(ρ)=ρ1−ρp2,F(ρ)=ρ1−ρe2,D(\\rho)=\\frac{\\rho}{1-\\rho}p^2, \\qquad F(\\rho)=\\frac{\\sqrt\\rho}{1-\\rho}e^2,D(ρ)=1−ρρ​p2,F(ρ)=1−ρρ​​e2,

em que:

* D(ρ)D(\\rho)D(ρ) é a penalidade atribuída ao DFA;  
* F(ρ)F(\\rho)F(ρ) é a penalidade atribuída ao PFA;  
* p\>0p\>0p\>0 é uma escala de erro do DFA;  
* e≥0e\\ge 0e≥0 é uma escala de erro do PFA.

Introduzindo o parâmetro adimensional

q=ep,q=\\frac ep,q=pe​,

o fator relativo de mitigação torna-se

Mq(ρ)=D(ρ)−F(ρ)D(ρ)=1−q2ρ.M\_q(\\rho) \= \\frac{D(\\rho)-F(\\rho)}{D(\\rho)} \= 1-\\frac{q^2}{\\sqrt\\rho}.Mq​(ρ)=D(ρ)D(ρ)−F(ρ)​=1−ρ​q2​.

O antigo “Teorema da Transição Dupla” é substituído por um resultado mais geral: para qualquer nível-alvo c\<1c\<1c\<1, a carga necessária para atingir mitigação ccc é

ρc(q)=q4(1−c)2.\\boxed{\\rho\_c(q)=\\frac{q^4}{(1-c)^2}}.ρc​(q)=(1−c)2q4​​.

O alvo é atingível no domínio (0,1)(0,1)(0,1) se, e somente se,

q\<1−c.\\boxed{q\<\\sqrt{1-c}}.q\<1−c​​.

O break-even e a meia-mitigação surgem como casos particulares:

ρ∗=ρ0=q4,ρ1/2=4q4,\\rho\_\*=\\rho\_0=q^4, \\qquad \\rho\_{1/2}=4q^4,ρ∗​=ρ0​=q4,ρ1/2​=4q4,

de modo que

ρ1/2=4ρ∗.\\rho\_{1/2}=4\\rho\_\*.ρ1/2​=4ρ∗​.

O documento também formaliza dois lower bounds:

1. **LB1:** melhor garantia uniforme de mitigação acima de uma carga mínima;  
2. **LB2:** lower bound aditivo para uma cascata multiplicativa de fatores não negativos.

A auditoria das fórmulas-ponte mostra, entretanto, que a validade matemática desses resultados não prova automaticamente sua validade operacional. O fator ρ/(1−ρ)\\rho/(1-\\rho)ρ/(1−ρ) é compatível com formas clássicas de saturação em filas, nas quais quantidades como comprimento médio e espera divergem quando ρ→1−\\rho\\to1^-ρ→1−, mas isso não basta para derivar o Eixo 1 sem definir o processo estocástico e a grandeza medida. [\[jstor.org\]](https://www.jstor.org/stable/3010415), [\[web.mit.edu\]](https://web.mit.edu/1.041/spring2023/lectures/L8-queuing-models-2023sp.pdf), [\[en.wikipedia.org\]](https://en.wikipedia.org/wiki/Heavy_traffic_approximation)

No Eixo 2, a composição por produto é exata quando cada fator é uma razão consecutiva da mesma grandeza positiva, como razões de variância entre estágios. A análise usual do bullwhip emprega razões de variâncias ou de coeficientes de variação, e a razão cumulativa pode telescopar como produto das razões locais quando numeradores e denominadores são compatíveis e as séries estão alinhadas. [\[metricgate.com\]](https://metricgate.com/docs/bullwhip-effect-quantification/), [\[researchpo...ulisboa.pt\]](https://researchportal.ulisboa.pt/en/publications/effective-bullwhip-metrics-for-multi-echelon-distribution-systems/)

---

# **1\. Escopo, camada lógica e non-claims**

O trabalho possui três camadas que devem permanecer separadas.

## **1.1 Camada algébrica**

Partindo das fórmulas de DDD e FFF, deduzem-se exatamente:

* a redução adimensional por q=e/pq=e/pq=e/p;  
* a monotonicidade de MqM\_qMq​;  
* os limiares ρc(q)\\rho\_c(q)ρc​(q);  
* a classificação de atingibilidade;  
* LB1;  
* LB2 sob hipóteses de não negatividade.

Essa camada está provada.

## **1.2 Camada de modelagem**

É necessário justificar por que o sistema real ou abstrato estudado satisfaz:

D(ρ)=ρ1−ρp2,F(ρ)=ρ1−ρe2,D(\\rho)=\\frac{\\rho}{1-\\rho}p^2, \\qquad F(\\rho)=\\frac{\\sqrt\\rho}{1-\\rho}e^2,D(ρ)=1−ρρ​p2,F(ρ)=1−ρρ​​e2,

e por que os fatores locais de cascata assumem a forma

1+ak,ak=ρk1−ρkpk2.1+a\_k, \\qquad a\_k=\\frac{\\rho\_k}{1-\\rho\_k}p\_k^2.1+ak​,ak​=1−ρk​ρk​​pk2​.

Essa camada ainda é condicional.

## **1.3 Camada de originalidade**

Mesmo um teorema correto pode ser uma consequência elementar de hipóteses escolhidas. A contribuição original, se confirmada, deverá estar em pelo menos um dos seguintes pontos:

1. derivação não trivial das fórmulas-ponte;  
2. identificação de uma classe natural de sistemas que produz essas fórmulas;  
3. classificação universal de níveis de mitigação;  
4. extensão robusta a parâmetros estimados ou intervalares;  
5. conexão rigorosa com cascatas dinâmicas, bullwhip ou outro fenômeno operacional;  
6. evidência de que a redução por q=e/pq=e/pq=e/p revela comportamento antes não identificado.

## **1.4 Non-claims**

Não se afirma neste documento que:

* LB1 ou LB2 sejam lower bounds de complexidade computacional;  
* os resultados impliquem algo sobre PPP versus NPNPNP, sistemas de prova ou Res⁡(k)\\operatorname{Res}(k)Res(k);  
* testes em grade constituam prova matemática;  
* o uso da palavra “bullwhip” esteja justificado sem identificar a grandeza propagada;  
* as fórmulas-ponte sejam universais;  
* TGL, LB1 ou LB2 sejam inéditos sem pesquisa de anterioridade;  
* o modelo descreva automaticamente dados reais.

---

# **2\. Definições básicas**

Sejam:

p\>0,e≥0,ρ∈(0,1).p\>0,\\qquad e\\ge0,\\qquad \\rho\\in(0,1).p\>0,e≥0,ρ∈(0,1).

Definem-se, condicionalmente:

D(ρ)=ρ1−ρp2D(\\rho)=\\frac{\\rho}{1-\\rho}p^2D(ρ)=1−ρρ​p2

e

F(ρ)=ρ1−ρe2.F(\\rho)=\\frac{\\sqrt\\rho}{1-\\rho}e^2.F(ρ)=1−ρρ​​e2.

Como p\>0p\>0p\>0, define-se a razão adimensional de erros:

q=ep≥0.q=\\frac ep\\ge0.q=pe​≥0.

O fator relativo de mitigação do PFA contra o DFA é

Mq(ρ)=D(ρ)−F(ρ)D(ρ).M\_q(\\rho) \= \\frac{D(\\rho)-F(\\rho)}{D(\\rho)}.Mq​(ρ)=D(ρ)D(ρ)−F(ρ)​.

Para ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1), temos D(ρ)\>0D(\\rho)\>0D(ρ)\>0, de modo que esse quociente está bem definido.

Substituindo DDD e FFF:

Mq(ρ)=1−F(ρ)D(ρ)=1−ρ1−ρe2ρ1−ρp2=1−e2p2ρ=1−q2ρ.\\begin{aligned} M\_q(\\rho) &= 1-\\frac{F(\\rho)}{D(\\rho)}\\\\ &= 1- \\frac{\\frac{\\sqrt\\rho}{1-\\rho}e^2} {\\frac{\\rho}{1-\\rho}p^2}\\\\ &= 1-\\frac{e^2}{p^2\\sqrt\\rho}\\\\ &= \\boxed{1-\\frac{q^2}{\\sqrt\\rho}}. \\end{aligned}Mq​(ρ)​=1−D(ρ)F(ρ)​=1−1−ρρ​p21−ρρ​​e2​=1−p2ρ​e2​=1−ρ​q2​​.​

A singularidade comum 1/(1−ρ)1/(1-\\rho)1/(1−ρ) cancela-se na comparação relativa, mas permanece nas penalidades absolutas.

---

# **3\. Interpretação de MqM\_qMq​**

A interpretação correta depende do sinal e do valor de Mq(ρ)M\_q(\\rho)Mq​(ρ).

## **3.1 PFA pior que DFA**

Se

Mq(ρ)\<0,M\_q(\\rho)\<0,Mq​(ρ)\<0,

então

F(ρ)\>D(ρ).F(\\rho)\>D(\\rho).F(ρ)\>D(ρ).

O PFA possui penalidade maior.

## **3.2 Break-even**

Se

Mq(ρ)=0,M\_q(\\rho)=0,Mq​(ρ)=0,

então

F(ρ)=D(ρ).F(\\rho)=D(\\rho).F(ρ)=D(ρ).

## **3.3 PFA melhor que DFA**

Se

0\<Mq(ρ)\<1,0\<M\_q(\\rho)\<1,0\<Mq​(ρ)\<1,

então

0\<F(ρ)\<D(ρ).0\<F(\\rho)\<D(\\rho).0\<F(ρ)\<D(ρ).

O valor Mq(ρ)M\_q(\\rho)Mq​(ρ) mede a redução relativa:

F(ρ)=(1−Mq(ρ))D(ρ).F(\\rho)=(1-M\_q(\\rho))D(\\rho).F(ρ)=(1−Mq​(ρ))D(ρ).

Por exemplo,

Mq(ρ)=12M\_q(\\rho)=\\frac12Mq​(ρ)=21​

significa

F(ρ)=12D(ρ),F(\\rho)=\\frac12D(\\rho),F(ρ)=21​D(ρ),

isto é, redução de 50% em relação à penalidade DFA.

## **3.4 Caso perfeito**

Se q=0q=0q=0, então e=0e=0e=0 e

F(ρ)=0,M0(ρ)=1.F(\\rho)=0, \\qquad M\_0(\\rho)=1.F(ρ)=0,M0​(ρ)=1.

Esse é um caso degenerado de mitigação total no modelo.

---

# **4\. Propriedades analíticas**

Para q\>0q\>0q\>0,

Mq(ρ)=1−q2ρ−1/2.M\_q(\\rho)=1-q^2\\rho^{-1/2}.Mq​(ρ)=1−q2ρ−1/2.

Sua derivada em relação a ρ\\rhoρ é

Mq′(ρ)=q22ρ3/2\>0.M\_q'(\\rho) \= \\frac{q^2}{2\\rho^{3/2}}\>0.Mq′​(ρ)=2ρ3/2q2​\>0.

Portanto, MqM\_qMq​ é estritamente crescente em (0,1)(0,1)(0,1).

A segunda derivada é

Mq′′(ρ)=−3q24ρ5/2\<0.M\_q''(\\rho) \= \-\\frac{3q^2}{4\\rho^{5/2}}\<0.Mq′′​(ρ)=−4ρ5/23q2​\<0.

Logo, além de crescente, MqM\_qMq​ é estritamente côncava em ρ\\rhoρ.

Os limites laterais são:

lim⁡ρ→0+Mq(ρ)=−∞\\lim\_{\\rho\\to0^+}M\_q(\\rho)=-\\inftyρ→0+lim​Mq​(ρ)=−∞

e

lim⁡ρ→1−Mq(ρ)=1−q2.\\lim\_{\\rho\\to1^-}M\_q(\\rho)=1-q^2.ρ→1−lim​Mq​(ρ)=1−q2.

Consequentemente, para q\>0q\>0q\>0,

Mq((0,1))=(−∞,1−q2).M\_q((0,1))=(-\\infty,1-q^2).Mq​((0,1))=(−∞,1−q2).

O limite superior não é atingido porque ρ=1\\rho=1ρ=1 não pertence ao domínio.

---

# **5\. Teorema Geral de Limiar**

## **Teorema TGL**

Sejam q\>0q\>0q\>0, c\<1c\<1c\<1 e

Mq(ρ)=1−q2ρ,ρ∈(0,1).M\_q(\\rho)=1-\\frac{q^2}{\\sqrt\\rho}, \\qquad \\rho\\in(0,1).Mq​(ρ)=1−ρ​q2​,ρ∈(0,1).

Então:

1. a equação  
    Mq(ρ)=cM\_q(\\rho)=cMq​(ρ)=c  
    possui no máximo uma solução em (0,1)(0,1)(0,1);

2. sua solução formal é  
    ρc(q)=q4(1−c)2;\\boxed{\\rho\_c(q)=\\frac{q^4}{(1-c)^2}};ρc​(q)=(1−c)2q4​​;  
3. essa solução pertence a (0,1)(0,1)(0,1) se, e somente se,  
    q\<1−c;\\boxed{q\<\\sqrt{1-c}};q\<1−c​​;  
4. quando a solução existe,  
    Mq(ρ)≥c  ⟺  ρ≥ρc(q);M\_q(\\rho)\\ge c \\iff \\rho\\ge\\rho\_c(q);Mq​(ρ)≥c⟺ρ≥ρc​(q);  
5. se  
    q=1−c,q=\\sqrt{1-c},q=1−c​,  
    então ccc é atingido apenas assintoticamente:  
    Mq(ρ)\<cpara todo ρ∈(0,1),M\_q(\\rho)\<c \\quad\\text{para todo }\\rho\\in(0,1),Mq​(ρ)\<cpara todo ρ∈(0,1),  
    mas  
    lim⁡ρ→1−Mq(ρ)=c;\\lim\_{\\rho\\to1^-}M\_q(\\rho)=c;ρ→1−lim​Mq​(ρ)=c;  
6. se  
    q\>1−c,q\>\\sqrt{1-c},q\>1−c​,  
    então  
    Mq(ρ)\<cM\_q(\\rho)\<cMq​(ρ)\<c  
    para todo ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1).

## **Prova**

Como Mq′(ρ)\>0M\_q'(\\rho)\>0Mq′​(ρ)\>0, a função é estritamente crescente. Portanto, a equação Mq(ρ)=cM\_q(\\rho)=cMq​(ρ)=c possui no máximo uma solução.

Resolvendo:

1−q2ρ=c1-\\frac{q^2}{\\sqrt\\rho}=c1−ρ​q2​=c

se, e somente se,

q2ρ=1−c.\\frac{q^2}{\\sqrt\\rho}=1-c.ρ​q2​=1−c.

Como c\<1c\<1c\<1, temos 1−c\>01-c\>01−c\>0. Assim,

ρ=q21−c\\sqrt\\rho=\\frac{q^2}{1-c}ρ​=1−cq2​

e, portanto,

ρ=q4(1−c)2.\\rho=\\frac{q^4}{(1-c)^2}.ρ=(1−c)2q4​.

A solução pertence a (0,1)(0,1)(0,1) precisamente quando

q4(1−c)2\<1.\\frac{q^4}{(1-c)^2}\<1.(1−c)2q4​\<1.

Como ambos os lados relevantes são positivos,

q4\<(1−c)2  ⟺  q2\<1−c  ⟺  q\<1−c.q^4\<(1-c)^2 \\iff q^2\<1-c \\iff q\<\\sqrt{1-c}.q4\<(1−c)2⟺q2\<1−c⟺q\<1−c​.

Quando a solução existe, a monotonicidade estrita fornece:

Mq(ρ)≥c  ⟺  ρ≥ρc(q).M\_q(\\rho)\\ge c \\iff \\rho\\ge\\rho\_c(q).Mq​(ρ)≥c⟺ρ≥ρc​(q).

Se q=1−cq=\\sqrt{1-c}q=1−c​, então

ρc(q)=1,\\rho\_c(q)=1,ρc​(q)=1,

que está fora do domínio. Nesse caso,

lim⁡ρ→1−Mq(ρ)=1−q2=c.\\lim\_{\\rho\\to1^-}M\_q(\\rho) \= 1-q^2 \= c.ρ→1−lim​Mq​(ρ)=1−q2=c.

Se q\>1−cq\>\\sqrt{1-c}q\>1−c​, então

1−q2\<c.1-q^2\<c.1−q2\<c.

Como 1−q21-q^21−q2 é o supremo da imagem de MqM\_qMq​ em (0,1)(0,1)(0,1), conclui-se que Mq(ρ)\<cM\_q(\\rho)\<cMq​(ρ)\<c para todo ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1). ∎

---

# **6\. Classificação dos regimes**

Para um nível desejado c∈\[0,1)c\\in\[0,1)c∈\[0,1), existem três regimes.

## **6.1 Regime alcançável**

Se

q\<1−c,q\<\\sqrt{1-c},q\<1−c​,

há um limiar interior

ρc(q)=q4(1−c)2∈(0,1).\\rho\_c(q)=\\frac{q^4}{(1-c)^2}\\in(0,1).ρc​(q)=(1−c)2q4​∈(0,1).

O alvo é garantido para:

ρ≥ρc(q).\\rho\\ge\\rho\_c(q).ρ≥ρc​(q).

## **6.2 Regime crítico assintótico**

Se

q=1−c,q=\\sqrt{1-c},q=1−c​,

o alvo não é atingido para nenhuma carga estritamente inferior a 111, mas é aproximado quando

ρ→1−.\\rho\\to1^-.ρ→1−.

## **6.3 Regime inalcançável**

Se

q\>1−c,q\>\\sqrt{1-c},q\>1−c​,

nem mesmo o limite de saturação alcança o alvo ccc.

---

# **7\. Corolários da antiga Transição Dupla**

## **Corolário C1: break-even**

Tomando c=0c=0c=0, obtemos:

ρ∗=ρ0=q4.\\boxed{\\rho\_\*=\\rho\_0=q^4}.ρ∗​=ρ0​=q4​.

O break-even interior existe se, e somente se,

q\<1.q\<1.q\<1.

Assim:

* se 0\<q\<10\<q\<10\<q\<1, existe um único break-even em (0,1)(0,1)(0,1);  
* se q=1q=1q=1, há apenas empate assintótico quando ρ→1−\\rho\\to1^-ρ→1−;  
* se q\>1q\>1q\>1, o PFA é pior que o DFA em todo o domínio;  
* se q=0q=0q=0, o PFA é perfeito no modelo e não há break-even interior.

## **Corolário C2: meia-mitigação**

Tomando

c=12,c=\\frac12,c=21​,

obtemos:

ρ1/2=4q4.\\boxed{\\rho\_{1/2}=4q^4}.ρ1/2​=4q4​.

A meia-mitigação é atingível se, e somente se,

q\<12.q\<\\frac1{\\sqrt2}.q\<2​1​.

## **Corolário C3: identidade de razão**

Sempre que os limiares forem considerados formalmente,

ρcρ∗=1(1−c)2.\\boxed{\\frac{\\rho\_c}{\\rho\_\*}=\\frac1{(1-c)^2}}.ρ∗​ρc​​=(1−c)21​​.

Em particular:

ρ1/2=4ρ∗.\\boxed{\\rho\_{1/2}=4\\rho\_\*}.ρ1/2​=4ρ∗​​.

O fator 444 não é um fenômeno isolado. Ele é o caso c=1/2c=1/2c=1/2 de uma lei contínua de níveis.

---

# **8\. Instâncias**

## **8.1 Modelo A**

Se

q=12,q=\\frac12,q=21​,

então:

ρ∗=(12)4=116=0.0625\\rho\_\*=\\left(\\frac12\\right)^4=\\frac1{16}=0.0625ρ∗​=(21​)4=161​=0.0625

e

ρ1/2=4(12)4=14=0.25.\\rho\_{1/2} \= 4\\left(\\frac12\\right)^4 \= \\frac14=0.25.ρ1/2​=4(21​)4=41​=0.25.

O cap assintótico é:

lim⁡ρ→1−M1/2(ρ)=1−14=34.\\lim\_{\\rho\\to1^-}M\_{1/2}(\\rho) \= 1-\\frac14 \= \\frac34.ρ→1−lim​M1/2​(ρ)=1−41​=43​.

Logo, o modelo permite no máximo 75% de mitigação, no sentido de limite.

## **8.2 Modelo B**

Se

q=1112,q=\\frac{11}{12},q=1211​,

então:

ρ∗=(1112)4=1464120736≈0.7061.\\rho\_\*= \\left(\\frac{11}{12}\\right)^4 \= \\frac{14641}{20736} \\approx0.7061.ρ∗​=(1211​)4=2073614641​≈0.7061.

A meia-mitigação exigiria:

ρ1/2=4(1112)4≈2.824.\\rho\_{1/2} \= 4\\left(\\frac{11}{12}\\right)^4 \\approx2.824.ρ1/2​=4(1211​)4≈2.824.

Como esse valor excede 111, a meia-mitigação é inalcançável.

O cap assintótico é:

1−(1112)2=1−121144=23144≈0.1597.1-\\left(\\frac{11}{12}\\right)^2 \= 1-\\frac{121}{144} \= \\frac{23}{144} \\approx0.1597.1−(1211​)2=1−144121​=14423​≈0.1597.

Assim, dentro do modelo, nenhuma carga admissível oferece 16% completos de mitigação. Esse valor é apenas o supremo assintótico.

---

# **9\. Sensibilidade dos limiares**

Como

ρc(q)=q4(1−c)2,\\rho\_c(q)=\\frac{q^4}{(1-c)^2},ρc​(q)=(1−c)2q4​,

temos:

∂ρc∂q=4q3(1−c)2\>0\\frac{\\partial\\rho\_c}{\\partial q} \= \\frac{4q^3}{(1-c)^2}\>0∂q∂ρc​​=(1−c)24q3​\>0

e

∂ρc∂c=2q4(1−c)3\>0.\\frac{\\partial\\rho\_c}{\\partial c} \= \\frac{2q^4}{(1-c)^3}\>0.∂c∂ρc​​=(1−c)32q4​\>0.

A segunda derivada em relação ao alvo é

∂2ρc∂c2=6q4(1−c)4\>0.\\frac{\\partial^2\\rho\_c}{\\partial c^2} \= \\frac{6q^4}{(1-c)^4}\>0.∂c2∂2ρc​​=(1−c)46q4​\>0.

Portanto:

* erros relativos maiores tornam o limiar mais difícil;  
* metas mais altas exigem cargas maiores;  
* o custo de elevar a meta cresce de forma convexa;  
* ρc\\rho\_cρc​ diverge quando c→1−c\\to1^-c→1−.

A elasticidade do limiar em relação a qqq é constante:

qρc∂ρc∂q=4.\\frac{q}{\\rho\_c} \\frac{\\partial\\rho\_c}{\\partial q} \=4.ρc​q​∂q∂ρc​​=4.

Assim, pequenas perturbações relativas satisfazem aproximadamente:

Δρcρc≈4Δqq.\\frac{\\Delta\\rho\_c}{\\rho\_c} \\approx 4\\frac{\\Delta q}{q}.ρc​Δρc​​≈4qΔq​.

Uma incerteza relativa de 1% em qqq pode produzir aproximadamente 4% de incerteza relativa no limiar.

---

# **10\. LB1: lower bound ótimo de mitigação**

## **Teorema LB1**

Sejam q≥0q\\ge0q≥0 e ρ0∈(0,1)\\rho\_0\\in(0,1)ρ0​∈(0,1). Para todo

ρ∈\[ρ0,1),\\rho\\in\[\\rho\_0,1),ρ∈\[ρ0​,1),

vale:

Mq(ρ)≥1−q2ρ0.\\boxed{ M\_q(\\rho) \\ge 1-\\frac{q^2}{\\sqrt{\\rho\_0}} }.Mq​(ρ)≥1−ρ0​​q2​​.

Além disso,

inf⁡ρ∈\[ρ0,1)Mq(ρ)=Mq(ρ0).\\inf\_{\\rho\\in\[\\rho\_0,1)}M\_q(\\rho) \= M\_q(\\rho\_0).ρ∈\[ρ0​,1)inf​Mq​(ρ)=Mq​(ρ0​).

Portanto, o bound é ótimo.

## **Prova**

Como MqM\_qMq​ é não decrescente em ρ\\rhoρ,

ρ≥ρ0⟹Mq(ρ)≥Mq(ρ0).\\rho\\ge\\rho\_0 \\Longrightarrow M\_q(\\rho)\\ge M\_q(\\rho\_0).ρ≥ρ0​⟹Mq​(ρ)≥Mq​(ρ0​).

Logo:

Mq(ρ)≥1−q2ρ0.M\_q(\\rho) \\ge 1-\\frac{q^2}{\\sqrt{\\rho\_0}}.Mq​(ρ)≥1−ρ0​​q2​.

A igualdade ocorre em ρ=ρ0\\rho=\\rho\_0ρ=ρ0​, de modo que nenhum lower bound uniforme maior pode valer no mesmo intervalo. ∎

## **Consequência para um alvo geral**

Para garantir

Mq(ρ)≥cM\_q(\\rho)\\ge cMq​(ρ)≥c

para toda ρ≥ρ0\\rho\\ge\\rho\_0ρ≥ρ0​, é necessário e suficiente que

ρ0≥q4(1−c)2.\\rho\_0\\ge\\frac{q^4}{(1-c)^2}.ρ0​≥(1−c)2q4​.

## **Instância do Modelo A**

Para

q=12,ρ0=14,q=\\frac12, \\qquad \\rho\_0=\\frac14,q=21​,ρ0​=41​,

temos:

Mq(ρ)≥1−1/41/2=12.M\_q(\\rho) \\ge 1-\\frac{1/4}{1/2} \= \\frac12.Mq​(ρ)≥1−1/21/4​=21​.

Assim:

ρ≥0.25⟹Mq(ρ)≥0.5.\\rho\\ge0.25 \\Longrightarrow M\_q(\\rho)\\ge0.5.ρ≥0.25⟹Mq​(ρ)≥0.5.

O valor 0.250.250.25 é um limiar de garantia de meia-mitigação, não um break-even.

---

# **11\. Certificados sob incerteza paramétrica**

Suponha que qqq e ρ\\rhoρ não sejam conhecidos exatamente, mas satisfaçam:

q∈\[q−,q+\],ρ∈\[ρ−,ρ+\],q\\in\[q\_-,q\_+\], \\qquad \\rho\\in\[\\rho\_-,\\rho\_+\],q∈\[q−​,q+​\],ρ∈\[ρ−​,ρ+​\],

com 0\<ρ−≤ρ+\<10\<\\rho\_-\\le\\rho\_+\<10\<ρ−​≤ρ+​\<1.

Como

∂M∂q=−2qρ≤0\\frac{\\partial M}{\\partial q} \= \-\\frac{2q}{\\sqrt\\rho}\\le0∂q∂M​=−ρ​2q​≤0

e

∂M∂ρ=q22ρ3/2≥0,\\frac{\\partial M}{\\partial\\rho} \= \\frac{q^2}{2\\rho^{3/2}}\\ge0,∂ρ∂M​=2ρ3/2q2​≥0,

segue que:

1−q+2ρ−≤Mq(ρ)≤1−q−2ρ+.\\boxed{ 1-\\frac{q\_+^2}{\\sqrt{\\rho\_-}} \\le M\_q(\\rho) \\le 1-\\frac{q\_-^2}{\\sqrt{\\rho\_+}} }.1−ρ−​​q+2​​≤Mq​(ρ)≤1−ρ+​​q−2​​​.

Para garantir robustamente um alvo ccc, basta verificar:

ρ−≥q+4(1−c)2.\\boxed{ \\rho\_-\\ge \\frac{q\_+^4}{(1-c)^2} }.ρ−​≥(1−c)2q+4​​​.

Esse resultado deve substituir, sempre que possível, verificações baseadas apenas em grades finitas.

---

# **12\. Auditoria da fórmula-ponte do Eixo 1**

A fórmula analisada é:

D(ρ)=ρ1−ρp2.\\boxed{ D(\\rho)=\\frac{\\rho}{1-\\rho}p^2 }.D(ρ)=1−ρρ​p2​.

## **12.1 O que a fórmula afirma estruturalmente**

Ela decompõe a penalidade DFA em:

D(ρ)=g(ρ)p2,g(ρ)=ρ1−ρ.D(\\rho)=g(\\rho)p^2, \\qquad g(\\rho)=\\frac{\\rho}{1-\\rho}.D(ρ)=g(ρ)p2,g(ρ)=1−ρρ​.

Isso impõe quatro propriedades:

1. separabilidade entre carga e erro;  
2. crescimento quadrático na escala ppp;  
3. crescimento aproximadamente linear para cargas pequenas;  
4. divergência hiperbólica quando ρ→1−\\rho\\to1^-ρ→1−.

De fato,

g(ρ)=ρ+ρ2+ρ3+⋯g(\\rho) \= \\rho+\\rho^2+\\rho^3+\\cdotsg(ρ)=ρ+ρ2+ρ3+⋯

para ∣ρ∣\<1|\\rho|\<1∣ρ∣\<1.

Portanto:

D(ρ)=p2∑j=1∞ρj.D(\\rho) \= p^2\\sum\_{j=1}^{\\infty}\\rho^j.D(ρ)=p2j=1∑∞​ρj.

Essa representação sugere uma interpretação como soma de contribuições recorrentes, mas, por si só, não identifica o mecanismo que gera os termos ρj\\rho^jρj.

---

## **12.2 Plausibilidade por analogia com filas**

Em modelos de fila com utilização ρ\<1\\rho\<1ρ\<1, é comum que comprimentos médios, tempos de espera ou aproximações de tráfego pesado cresçam rapidamente e eventualmente divirjam à medida que ρ→1−\\rho\\to1^-ρ→1−. A utilização próxima de 111 é justamente o regime de tráfego pesado. [\[jstor.org\]](https://www.jstor.org/stable/3010415), [\[web.mit.edu\]](https://web.mit.edu/1.041/spring2023/lectures/L8-queuing-models-2023sp.pdf), [\[en.wikipedia.org\]](https://en.wikipedia.org/wiki/Heavy_traffic_approximation)

Em uma fila M/M/1M/M/1M/M/1, por exemplo, aparecem formas relacionadas a:

ρ1−ρeρ21−ρ,\\frac{\\rho}{1-\\rho} \\quad\\text{e}\\quad \\frac{\\rho^2}{1-\\rho},1−ρρ​e1−ρρ2​,

dependendo de a grandeza considerada incluir ou excluir o cliente em serviço.

Isso torna a forma do Eixo 1 **plausível**, mas não prova que ela descreve o DFA.

A analogia só é válida se:

* ρ\\rhoρ for efetivamente uma utilização ou parâmetro de carga equivalente;  
* existir um regime estável com ρ\<1\\rho\<1ρ\<1;  
* a penalidade for proporcional à grandeza de fila apropriada;  
* p2p^2p2 puder ser separado da dinâmica;  
* a distribuição e a política do sistema forem compatíveis com a fórmula.

---

## **12.3 Problema de identificação**

A forma

ρ1−ρ\\frac{\\rho}{1-\\rho}1−ρρ​

não identifica unicamente o mecanismo gerador.

Ela pode surgir de:

* soma geométrica;  
* ocupação média de um sistema Markoviano;  
* repetição de tentativas;  
* propagação recursiva;  
* aproximação de saturação;  
* função escolhida fenomenologicamente.

Consequentemente, observar empiricamente algo parecido com ρ/(1−ρ)\\rho/(1-\\rho)ρ/(1−ρ) não permite concluir, sem hipóteses adicionais, que o sistema obedece a um modelo específico de fila ou recursão.

---

## **12.4 Análise dimensional**

Como ρ\\rhoρ é adimensional,

ρ1−ρ\\frac{\\rho}{1-\\rho}1−ρρ​

também é adimensional.

Logo:

\[D\]=\[p2\].\[D\]=\[p^2\].\[D\]=\[p2\].

Se ppp é um erro medido na unidade UUU, então:

\[D\]=U2.\[D\]=U^2.\[D\]=U2.

Isso é coerente se DDD representar:

* erro quadrático;  
* variância;  
* energia de erro;  
* perda quadrática.

Não é automaticamente coerente se DDD representar:

* probabilidade;  
* latência;  
* quantidade de itens;  
* custo monetário;  
* taxa de falha.

Nesses casos, seria necessário um coeficiente dimensional:

D(ρ)=κDρ1−ρp2,D(\\rho)=\\kappa\_D\\frac{\\rho}{1-\\rho}p^2,D(ρ)=κD​1−ρρ​p2,

em que κD\\kappa\_DκD​ converta p2p^2p2 para a unidade de DDD.

---

## **12.5 O significado de ppp**

É necessário distinguir pelo menos três possibilidades.

### **Caso A: ppp é um erro determinístico**

Então p2p^2p2 é apenas o quadrado de uma magnitude.

### **Caso B: ppp é RMSE**

Nesse caso:

p2=MSE⁡,p^2=\\operatorname{MSE},p2=MSE,

o que torna natural uma penalidade quadrática. Métricas de previsão como MSE e RMSE não são intercambiáveis em unidade: MSE usa a unidade ao quadrado, enquanto RMSE retorna à unidade original. [\[en.wikipedia.org\]](https://en.wikipedia.org/wiki/Forecast_error), [\[openforecast.org\]](https://openforecast.org/adam/errorMeasures.html), [\[datacamp.com\]](https://www.datacamp.com/tutorial/rmse)

### **Caso C: p2p^2p2 é variância**

Então é necessário demonstrar que o erro é centrado ou separar viés e variância:

MSE⁡=Var⁡(ε)+Bias⁡(ε)2.\\operatorname{MSE} \= \\operatorname{Var}(\\varepsilon) \+ \\operatorname{Bias}(\\varepsilon)^2.MSE=Var(ε)+Bias(ε)2.

Se houver viés sistemático, tratar p2p^2p2 simplesmente como variância perde informação.

---

## **12.6 Hipótese de separabilidade**

A fórmula supõe que ppp não depende de ρ\\rhoρ:

D(ρ)=g(ρ)p2.D(\\rho)=g(\\rho)p^2.D(ρ)=g(ρ)p2.

Em sistemas adaptativos, essa hipótese pode falhar. Pode ocorrer:

p=p(ρ),p=p(\\rho),p=p(ρ),

levando a:

D(ρ)=ρ1−ρp(ρ)2.D(\\rho)=\\frac{\\rho}{1-\\rho}p(\\rho)^2.D(ρ)=1−ρρ​p(ρ)2.

Nesse caso, a razão q=e/pq=e/pq=e/p também pode depender da carga:

q=q(ρ).q=q(\\rho).q=q(ρ).

A fórmula reduzida passaria a ser:

M(ρ)=1−q(ρ)2ρ,M(\\rho) \= 1-\\frac{q(\\rho)^2}{\\sqrt\\rho},M(ρ)=1−ρ​q(ρ)2​,

e a monotonicidade deixaria de ser automática. Sua derivada seria:

M′(ρ)=−2q(ρ)q′(ρ)ρ−1/2+q(ρ)22ρ3/2.M'(\\rho) \= \-2q(\\rho)q'(\\rho)\\rho^{-1/2} \+ \\frac{q(\\rho)^2}{2\\rho^{3/2}}.M′(ρ)=−2q(ρ)q′(ρ)ρ−1/2+2ρ3/2q(ρ)2​.

Logo,

M′(ρ)\>0M'(\\rho)\>0M′(ρ)\>0

exigiria:

q(ρ)−4ρq′(ρ)\>0q(\\rho)-4\\rho q'(\\rho)\>0q(ρ)−4ρq′(ρ)\>0

quando q(ρ)\>0q(\\rho)\>0q(ρ)\>0.

A hipótese de qqq constante é, portanto, estrutural, não apenas notacional.

---

## **12.7 Derivação mínima admissível para o Eixo 1**

Uma derivação rigorosa pode começar de uma recursão abstrata de propagação de energia:

Xj+1=ρXj+ρp2,X0=0.X\_{j+1}=\\rho X\_j+\\rho p^2, \\qquad X\_0=0.Xj+1​=ρXj​+ρp2,X0​=0.

Então:

X1=ρp2,X\_1=\\rho p^2,X1​=ρp2, X2=(ρ+ρ2)p2,X\_2=(\\rho+\\rho^2)p^2,X2​=(ρ+ρ2)p2,

e, em geral,

Xn=p2∑j=1nρj.X\_n=p^2\\sum\_{j=1}^{n}\\rho^j.Xn​=p2j=1∑n​ρj.

Como 0\<ρ\<10\<\\rho\<10\<ρ\<1,

lim⁡n→∞Xn=p2ρ1−ρ.\\lim\_{n\\to\\infty}X\_n \= p^2\\frac{\\rho}{1-\\rho}.n→∞lim​Xn​=p21−ρρ​.

Portanto:

D(ρ)=ρ1−ρp2.D(\\rho) \= \\frac{\\rho}{1-\\rho}p^2.D(ρ)=1−ρρ​p2.

Essa derivação é válida se for possível justificar operacionalmente que:

* cada rodada retém a fração ρ\\rhoρ da energia anterior;  
* cada rodada injeta ρp2\\rho p^2ρp2;  
* os termos podem ser somados sem covariâncias cruzadas;  
* o sistema atinge um regime estacionário;  
* ppp permanece constante entre rodadas.

A recursão não deve ser adotada apenas para reproduzir a fórmula. Ela precisa ser derivada da dinâmica do sistema.

---

## **12.8 Veredito sobre o Eixo 1**

### **Resultado**

A fórmula é:

* matematicamente bem definida para 0\<ρ\<10\<\\rho\<10\<ρ\<1;  
* dimensionalmente coerente se DDD e p2p^2p2 tiverem a mesma unidade;  
* compatível com uma soma geométrica ou uma lei de saturação;  
* qualitativamente compatível com comportamentos de tráfego pesado.

### **Lacuna**

Ainda falta provar que o DFA estudado satisfaz a recursão ou o modelo probabilístico que produz exatamente:

D(ρ)=ρ1−ρp2.D(\\rho)=\\frac{\\rho}{1-\\rho}p^2.D(ρ)=1−ρρ​p2.

### **Classificação epistemológica**

Eixo 1: hipoˊtese estrutural plausıˊvel, ainda na˜o derivada.\\boxed{\\text{Eixo 1: hipótese estrutural plausível, ainda não derivada.}}Eixo 1: hipoˊtese estrutural plausıˊvel, ainda na˜o derivada.​

---

# **13\. Auditoria da fórmula PFA associada**

Embora o pedido principal se concentre nos Eixos 1 e 2, o Teorema Geral de Limiar depende também de:

F(ρ)=ρ1−ρe2.F(\\rho)=\\frac{\\sqrt\\rho}{1-\\rho}e^2.F(ρ)=1−ρρ​​e2.

A diferença decisiva é o numerador ρ\\sqrt\\rhoρ​.

## **13.1 Consequência estrutural**

Temos:

F(ρ)D(ρ)=e2p2ρ=q2ρ.\\frac{F(\\rho)}{D(\\rho)} \= \\frac{e^2}{p^2\\sqrt\\rho} \= \\frac{q^2}{\\sqrt\\rho}.D(ρ)F(ρ)​=p2ρ​e2​=ρ​q2​.

Para cargas pequenas:

ρ\>ρ.\\sqrt\\rho\>\\rho.ρ​\>ρ.

Portanto, mesmo compartilhando o denominador, o PFA pode ser relativamente pior em cargas pequenas.

Para cargas altas:

ρ→1,ρ→1,\\sqrt\\rho\\to1, \\qquad \\rho\\to1,ρ​→1,ρ→1,

e a comparação passa a depender principalmente de q2q^2q2.

---

## **13.2 Uma recursão que produziria a fórmula**

A forma de FFF poderia resultar de:

Yj+1=ρYj+ρ e2,Y0=0.Y\_{j+1}=\\rho Y\_j+\\sqrt\\rho\\,e^2, \\qquad Y\_0=0.Yj+1​=ρYj​+ρ​e2,Y0​=0.

Então:

Yn=e2ρ∑j=0n−1ρj,Y\_n \= e^2\\sqrt\\rho \\sum\_{j=0}^{n-1}\\rho^j,Yn​=e2ρ​j=0∑n−1​ρj,

e:

lim⁡n→∞Yn=ρ1−ρe2.\\lim\_{n\\to\\infty}Y\_n \= \\frac{\\sqrt\\rho}{1-\\rho}e^2.n→∞lim​Yn​=1−ρρ​​e2.

Novamente, isso apenas desloca a obrigação de prova. É preciso justificar por que a injeção por rodada é ρ e2\\sqrt\\rho\\,e^2ρ​e2, e não ρe2\\rho e^2ρe2, e2e^2e2, ou outra função.

## **13.3 Questão científica central**

O expoente 1/21/21/2 não deve aparecer como escolha de ajuste sem suporte. Ele precisa derivar de algo como:

* transformação entre amplitude e energia;  
* norma L2L^2L2;  
* desvio-padrão associado a uma variância proporcional a ρ\\rhoρ;  
* concentração estatística;  
* geometria de projeção;  
* agregação de contribuições independentes;  
* processo difusivo.

Sem essa derivação, o expoente 1/21/21/2 é um postulado.

---

# **14\. Auditoria da fórmula-ponte do Eixo 2**

A fórmula proposta é:

P(n)P(0)=∏k=1n(1+ak)\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \= \\prod\_{k=1}^{n}(1+a\_k) }P(0)P(n)​=k=1∏n​(1+ak​)​

com

ak=ρk1−ρkpk2≥0.a\_k= \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2 \\ge0.ak​=1−ρk​ρk​​pk2​≥0.

Essa ponte contém duas afirmações distintas:

1. a composição global é multiplicativa;  
2. o fator local é exatamente 1+ak1+a\_k1+ak​.

Ambas exigem justificação separada.

---

## **14.1 Quando o produto é uma identidade exata**

Suponha que P(k)\>0P^{(k)}\>0P(k)\>0 e defina o fator local por:

Bk=P(k)P(k−1).B\_k=\\frac{P^{(k)}}{P^{(k-1)}}.Bk​=P(k−1)P(k)​.

Então:

∏k=1nBk=∏k=1nP(k)P(k−1).\\prod\_{k=1}^{n}B\_k \= \\prod\_{k=1}^{n} \\frac{P^{(k)}}{P^{(k-1)}}.k=1∏n​Bk​=k=1∏n​P(k−1)P(k)​.

O produto telescopa:

∏k=1nP(k)P(k−1)=P(n)P(0).\\prod\_{k=1}^{n} \\frac{P^{(k)}}{P^{(k-1)}} \= \\frac{P^{(n)}}{P^{(0)}}.k=1∏n​P(k−1)P(k)​=P(0)P(n)​.

Se for demonstrado que:

Bk=1+ak,B\_k=1+a\_k,Bk​=1+ak​,

segue exatamente que:

P(n)P(0)=∏k=1n(1+ak).\\frac{P^{(n)}}{P^{(0)}} \= \\prod\_{k=1}^{n}(1+a\_k).P(0)P(n)​=k=1∏n​(1+ak​).

Portanto, nenhuma hipótese de independência é necessária para a telescopagem. O que é necessário é que cada fator seja realmente uma razão consecutiva da mesma grandeza.

---

## **14.2 Interpretação como razão de variâncias**

No contexto bullwhip, uma escolha natural seria:

P(k)=Var⁡(Ok),P^{(k)} \= \\operatorname{Var}(O\_k),P(k)=Var(Ok​),

em que OkO\_kOk​ é o processo de pedidos no estágio kkk.

Então:

Bk=Var⁡(Ok)Var⁡(Ok−1).B\_k \= \\frac{\\operatorname{Var}(O\_k)} {\\operatorname{Var}(O\_{k-1})}.Bk​=Var(Ok−1​)Var(Ok​)​.

A razão cumulativa é:

∏k=1nBk=Var⁡(On)Var⁡(O0).\\prod\_{k=1}^n B\_k \= \\frac{\\operatorname{Var}(O\_n)} {\\operatorname{Var}(O\_0)}.k=1∏n​Bk​=Var(O0​)Var(On​)​.

Essa forma é compatível com a definição usual do bullwhip como amplificação da variabilidade ao longo de estágios. A literatura emprega múltiplas métricas, incluindo razões de variância, coeficientes de variação e medidas de estoque, de modo que a métrica precisa ser declarada explicitamente. [\[arxiv.org\]](https://arxiv.org/pdf/2604.13478), [\[arxiv.org\]](https://arxiv.org/html/2604.13478), [\[researchpo...ulisboa.pt\]](https://researchportal.ulisboa.pt/en/publications/effective-bullwhip-metrics-for-multi-echelon-distribution-systems/)

Também é necessário alinhar corretamente as séries e os períodos. Uma razão cumulativa só representa a amplificação total se cada denominador intermediário corresponder ao numerador do estágio anterior. [\[metricgate.com\]](https://metricgate.com/docs/bullwhip-effect-quantification/)

---

## **14.3 O símbolo P(k)P^{(k)}P(k) está subespecificado**

Antes de aceitar o Eixo 2, deve-se declarar se P(k)P^{(k)}P(k) é:

* variância;  
* MSE;  
* potência de sinal;  
* energia acumulada;  
* custo;  
* probabilidade;  
* inventário;  
* taxa de pedidos;  
* coeficiente de variação ao quadrado.

Se P(k)P^{(k)}P(k) representar variância, a multiplicação de razões é natural.

Se representar erro absoluto, custo ou probabilidade, a mesma forma pode ser inadequada.

---

## **14.4 Análise dimensional de aka\_kak​**

Como 1+ak1+a\_k1+ak​ aparece como fator multiplicativo, aka\_kak​ precisa ser adimensional.

Mas:

ak=ρk1−ρkpk2.a\_k= \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2.ak​=1−ρk​ρk​​pk2​.

O fator

ρk1−ρk\\frac{\\rho\_k}{1-\\rho\_k}1−ρk​ρk​​

é adimensional. Assim, aka\_kak​ tem a unidade de pk2p\_k^2pk2​.

Logo, aka\_kak​ só é adimensional se:

* pkp\_kpk​ já for adimensional; ou  
* pkp\_kpk​ tiver sido normalizado por uma escala de referência.

Se pkp\_kpk​ possui unidade física UUU, então pk2p\_k^2pk2​ possui unidade U2U^2U2, e a soma

1+ak1+a\_k1+ak​

é dimensionalmente inválida.

Esse é um problema central.

## **Correção necessária**

Deve-se introduzir uma escala sk\>0s\_k\>0sk​\>0 com a mesma unidade de pkp\_kpk​:

p\~k=pksk.\\widetilde p\_k=\\frac{p\_k}{s\_k}.p​k​=sk​pk​​.

Então:

ak=ρk1−ρkp\~k2a\_k \= \\frac{\\rho\_k}{1-\\rho\_k}\\widetilde p\_k^2ak​=1−ρk​ρk​​p​k2​

é adimensional.

Alternativamente, usar:

ak=κkρk1−ρkpk2,a\_k \= \\kappa\_k \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2,ak​=κk​1−ρk​ρk​​pk2​,

com:

\[κk\]=\[pk\]−2.\[\\kappa\_k\]=\[p\_k\]^{-2}.\[κk​\]=\[pk​\]−2.

Sem essa normalização, o Eixo 2 não é dimensionalmente bem formado.

---

## **14.5 Derivação local necessária**

O produto global exige que cada estágio satisfaça:

P(k)=(1+ak)P(k−1).P^{(k)} \= (1+a\_k)P^{(k-1)}.P(k)=(1+ak​)P(k−1).

Isso equivale a:

P(k)−P(k−1)=akP(k−1).P^{(k)}-P^{(k-1)} \= a\_kP^{(k-1)}.P(k)−P(k−1)=ak​P(k−1).

Portanto, o modelo afirma que o acréscimo no estágio kkk é proporcional à grandeza de entrada P(k−1)P^{(k-1)}P(k−1).

Uma fórmula aditiva diferente, como:

P(k)=P(k−1)+ak,P^{(k)} \= P^{(k-1)}+a\_k,P(k)=P(k−1)+ak​,

não produz o mesmo produto. Nesse caso:

P(n)=P(0)+∑k=1nak.P^{(n)} \= P^{(0)}+\\sum\_{k=1}^{n}a\_k.P(n)=P(0)+k=1∑n​ak​.

Logo, antes de usar LB2, é preciso provar que aka\_kak​ é uma **taxa relativa de amplificação**, e não um incremento absoluto.

---

## **14.6 Covariâncias e sistemas lineares**

Suponha que o sinal no estágio kkk seja modelado por:

Ok=Ok−1+εk.O\_k=O\_{k-1}+\\varepsilon\_k.Ok​=Ok−1​+εk​.

Então:

Var⁡(Ok)=Var⁡(Ok−1)+Var⁡(εk)+2Cov⁡(Ok−1,εk).\\operatorname{Var}(O\_k) \= \\operatorname{Var}(O\_{k-1}) \+ \\operatorname{Var}(\\varepsilon\_k) \+ 2\\operatorname{Cov}(O\_{k-1},\\varepsilon\_k).Var(Ok​)=Var(Ok−1​)+Var(εk​)+2Cov(Ok−1​,εk​).

Para obter:

Var⁡(Ok)=(1+ak)Var⁡(Ok−1),\\operatorname{Var}(O\_k) \= (1+a\_k)\\operatorname{Var}(O\_{k-1}),Var(Ok​)=(1+ak​)Var(Ok−1​),

é necessário que:

Var⁡(εk)+2Cov⁡(Ok−1,εk)=akVar⁡(Ok−1).\\operatorname{Var}(\\varepsilon\_k) \+ 2\\operatorname{Cov}(O\_{k-1},\\varepsilon\_k) \= a\_k\\operatorname{Var}(O\_{k-1}).Var(εk​)+2Cov(Ok−1​,εk​)=ak​Var(Ok−1​).

Se εk\\varepsilon\_kεk​ for não correlacionado com Ok−1O\_{k-1}Ok−1​, reduz-se a:

Var⁡(εk)=akVar⁡(Ok−1).\\operatorname{Var}(\\varepsilon\_k) \= a\_k\\operatorname{Var}(O\_{k-1}).Var(εk​)=ak​Var(Ok−1​).

Portanto, independência ou ausência de correlação não é necessária para a telescopagem das razões, mas pode ser necessária para derivar a fórmula local 1+ak1+a\_k1+ak​ a partir de uma dinâmica aditiva.

Modelos reais de bullwhip dependem de previsão, políticas de reposição, lead time, batching, backorders e dependências temporais. Simulações multiestágio mostram que diferentes escolhas desses mecanismos podem alterar fortemente a amplificação observada. [\[arxiv.org\]](https://arxiv.org/pdf/2604.13478), [\[arxiv.org\]](https://arxiv.org/html/2604.13478), [\[jurnal-tmit.com\]](https://jurnal-tmit.com/index.php/home/article/view/1980)

---

## **14.7 Condição de não negatividade**

Se

0\<ρk\<10\<\\rho\_k\<10\<ρk​\<1

e

pk2≥0,p\_k^2\\ge0,pk2​≥0,

então:

ak≥0.a\_k\\ge0.ak​≥0.

Consequentemente:

1+ak≥1.1+a\_k\\ge1.1+ak​≥1.

O modelo exclui, por construção, estágios atenuadores.

Isso pode ser excessivamente restritivo. Certos estágios podem suavizar a variabilidade, dando:

0\<Bk\<1.0\<B\_k\<1.0\<Bk​\<1.

Nesse caso:

ak=Bk−1∈(−1,0).a\_k=B\_k-1\\in(-1,0).ak​=Bk​−1∈(−1,0).

O LB2 baseado em todos os ak≥0a\_k\\ge0ak​≥0 deixa de se aplicar. Portanto, a hipótese implica que cada estágio é individualmente não atenuador.

---

## **14.8 Veredito sobre o Eixo 2**

### **A parte correta**

Se:

1+ak=P(k)P(k−1),1+a\_k \= \\frac{P^{(k)}}{P^{(k-1)}},1+ak​=P(k−1)P(k)​,

então:

P(n)P(0)=∏k=1n(1+ak)\\frac{P^{(n)}}{P^{(0)}} \= \\prod\_{k=1}^n(1+a\_k)P(0)P(n)​=k=1∏n​(1+ak​)

é uma identidade telescópica.

### **Pontos ainda não provados**

É necessário demonstrar:

1. o significado de P(k)P^{(k)}P(k);  
2. sua positividade;  
3. a compatibilidade entre estágios;  
4. a adimensionalidade de aka\_kak​;  
5. a lei local P(k)=(1+ak)P(k−1);P^{(k)}=(1+a\_k)P^{(k-1)};P(k)=(1+ak​)P(k−1);  
6. por que ak=ρk1−ρkpk2;a\_k=\\frac{\\rho\_k}{1-\\rho\_k}p\_k^2;ak​=1−ρk​ρk​​pk2​;  
7. se cada estágio é necessariamente amplificador;  
8. como correlações temporais e entre estágios entram no modelo.

### **Classificação epistemológica**

Eixo 2: composic¸a˜o correta condicionalmente; fator local ainda na˜o derivado.\\boxed{ \\text{Eixo 2: composição correta condicionalmente; fator local ainda não derivado.} }Eixo 2: composic¸​a˜o correta condicionalmente; fator local ainda na˜o derivado.​

---

# **15\. LB2: lower bound de cascata**

## **Teorema LB2**

Se

a1,…,an≥0,a\_1,\\ldots,a\_n\\ge0,a1​,…,an​≥0,

então:

∏k=1n(1+ak)≥1+∑k=1nak.\\boxed{ \\prod\_{k=1}^{n}(1+a\_k) \\ge 1+\\sum\_{k=1}^{n}a\_k }.k=1∏n​(1+ak​)≥1+k=1∑n​ak​​.

## **Prova por expansão**

Temos:

∏k=1n(1+ak)=1+∑iai+∑i\<jaiaj+∑i\<j\<ℓaiajaℓ+⋯+∏iai.\\prod\_{k=1}^{n}(1+a\_k) \= 1+ \\sum\_i a\_i+ \\sum\_{i\<j}a\_i a\_j+ \\sum\_{i\<j\<\\ell}a\_i a\_j a\_\\ell+ \\cdots+ \\prod\_i a\_i.k=1∏n​(1+ak​)=1+i∑​ai​+i\<j∑​ai​aj​+i\<j\<ℓ∑​ai​aj​aℓ​+⋯+i∏​ai​.

Como todos os ak≥0a\_k\\ge0ak​≥0, todos os termos de grau pelo menos dois são não negativos. Portanto:

∏k=1n(1+ak)≥1+∑k=1nak.\\prod\_{k=1}^{n}(1+a\_k) \\ge 1+\\sum\_{k=1}^{n}a\_k.k=1∏n​(1+ak​)≥1+k=1∑n​ak​.

∎

A desigualdade é uma extensão elementar da mesma estrutura que, no caso uniforme, aparece na desigualdade clássica de Bernoulli:

(1+a)n≥1+na(1+a)^n\\ge1+na(1+a)n≥1+na

para a≥0a\\ge0a≥0. Ela não deve ser reivindicada como nova isoladamente. [\[en.wikipedia.org\]](https://en.wikipedia.org/wiki/Bernoulli%27s_inequality), [\[faculty.fiu.edu\]](https://faculty.fiu.edu/~decarlil/Preprints/FinalBern1.pdf), [\[files.ele-math.com\]](https://files.ele-math.com/articles/jmi-02-10.pdf)

---

## **15.1 Condição de igualdade**

A igualdade ocorre se, e somente se,

aiaj=0a\_i a\_j=0ai​aj​=0

para todos os índices distintos i,ji,ji,j.

Equivalentemente, no máximo um dos aka\_kak​ é estritamente positivo.

---

## **15.2 Corolário condicionado ao Eixo 2**

Se:

P(n)P(0)=∏k=1n(1+ak)\\frac{P^{(n)}}{P^{(0)}} \= \\prod\_{k=1}^n(1+a\_k)P(0)P(n)​=k=1∏n​(1+ak​)

e

ak=ρk1−ρkp\~k2≥0,a\_k= \\frac{\\rho\_k}{1-\\rho\_k}\\widetilde p\_k^2\\ge0,ak​=1−ρk​ρk​​p​k2​≥0,

com p\~k\\widetilde p\_kp​k​ adimensional, então:

P(n)P(0)≥1+∑k=1nρk1−ρkp\~k2.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge 1+ \\sum\_{k=1}^{n} \\frac{\\rho\_k}{1-\\rho\_k}\\widetilde p\_k^2 }.P(0)P(n)​≥1+k=1∑n​1−ρk​ρk​​p​k2​​.

---

# **16\. Quando a cascata cresce linearmente**

LB2, sozinho, não implica crescimento linear em nnn para sequências arbitrárias.

Se, por exemploA seção 16 precisa deixar explícita a diferença entre **o lower bound aditivo**, **crescimento linear uniforme** e **crescimento exponencial da cascata multiplicativa**. Abaixo está a versão revisada, já corrigindo o erro de formatação “nnnnnnnnn” para nnn.

---

# **16\. Quando a cascata possui crescimento linear**

O teorema LB2 estabelece que, para ak≥0a\_k\\ge 0ak​≥0,

∏k=1n(1+ak)≥1+∑k=1nak.\\prod\_{k=1}^{n}(1+a\_k) \\ge 1+\\sum\_{k=1}^{n}a\_k.k=1∏n​(1+ak​)≥1+k=1∑n​ak​.

Esse resultado, isoladamente, **não implica que a cascata cresça pelo menos linearmente em nnn**. Para obter um lower bound linear uniforme, é necessário controlar como a soma

Sn=∑k=1nakS\_n=\\sum\_{k=1}^{n}a\_kSn​=k=1∑n​ak​

cresce com nnn.

## **16.1 Contraexemplo à afirmação linear sem hipóteses adicionais**

Considere:

ak=1k2.a\_k=\\frac{1}{k^2}.ak​=k21​.

Temos ak≥0a\_k\\ge 0ak​≥0, de modo que LB2 se aplica:

∏k=1n(1+1k2)≥1+∑k=1n1k2.\\prod\_{k=1}^{n} \\left(1+\\frac1{k^2}\\right) \\ge 1+\\sum\_{k=1}^{n}\\frac1{k^2}.k=1∏n​(1+k21​)≥1+k=1∑n​k21​.

Entretanto, a série

∑k=1∞1k2\\sum\_{k=1}^{\\infty}\\frac1{k^2}k=1∑∞​k21​

é convergente. Consequentemente, as somas parciais

∑k=1n1k2\\sum\_{k=1}^{n}\\frac1{k^2}k=1∑n​k21​

permanecem limitadas quando n→∞n\\to\\inftyn→∞.

Logo, LB2 fornece nesse caso apenas um lower bound limitado. Ele não fornece uma constante c\>0c\>0c\>0, independente de nnn, tal que

∏k=1n(1+ak)≥1+cn\\prod\_{k=1}^{n}(1+a\_k)\\ge 1+cnk=1∏n​(1+ak​)≥1+cn

para todo nnn.

Portanto, a afirmação

> “A cascata cresce pelo menos linearmente em nnn”

é falsa para sequências arbitrárias de incrementos não negativos.

A conclusão correta de LB2, sem hipóteses adicionais, é apenas:

P(n)P(0)≥1+Sn\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge 1+S\_n }P(0)P(n)​≥1+Sn​​

onde

Sn=∑k=1nak.S\_n=\\sum\_{k=1}^{n}a\_k.Sn​=k=1∑n​ak​.

O comportamento assintótico do lower bound depende do comportamento de SnS\_nSn​.

---

## **16.2 Critério necessário e suficiente para o lower bound linear**

Suponha que:

P(n)P(0)=∏k=1n(1+ak),ak≥0.\\frac{P^{(n)}}{P^{(0)}} \= \\prod\_{k=1}^{n}(1+a\_k), \\qquad a\_k\\ge0.P(0)P(n)​=k=1∏n​(1+ak​),ak​≥0.

LB2 fornece um lower bound linear da forma

P(n)P(0)≥1+cn\\frac{P^{(n)}}{P^{(0)}} \\ge 1+cnP(0)P(n)​≥1+cn

para alguma constante c\>0c\>0c\>0, se:

∑k=1nak≥cn.\\sum\_{k=1}^{n}a\_k\\ge cn.k=1∑n​ak​≥cn.

Essa condição pode ser reescrita como:

1n∑k=1nak≥c.\\frac1n\\sum\_{k=1}^{n}a\_k\\ge c.n1​k=1∑n​ak​≥c.

Assim, uma condição suficiente e essencial para obter o crescimento linear através de LB2 é a existência de um piso positivo para a média acumulada dos incrementos:

inf⁡n≥11n∑k=1nak\>0.\\boxed{ \\inf\_{n\\ge1} \\frac1n\\sum\_{k=1}^{n}a\_k \>0. }n≥1inf​n1​k=1∑n​ak​\>0.​

Mais precisamente, definindo

a‾n=1n∑k=1nak,\\overline a\_n \= \\frac1n\\sum\_{k=1}^{n}a\_k,an​=n1​k=1∑n​ak​,

temos a identidade:

1+∑k=1nak=1+na‾n.1+\\sum\_{k=1}^{n}a\_k \= 1+n\\overline a\_n.1+k=1∑n​ak​=1+nan​.

Portanto, LB2 pode ser escrito como:

P(n)P(0)≥1+na‾n.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge 1+n\\overline a\_n. }P(0)P(n)​≥1+nan​.​

Se existe a‾\>0\\underline a\>0a​\>0 tal que

a‾n≥a‾\\overline a\_n\\ge\\underline aan​≥a​

para todo nnn, então:

P(n)P(0)≥1+na‾.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge 1+n\\underline a. }P(0)P(n)​≥1+na​.​

Esse é o enunciado rigoroso do lower bound linear.

---

## **16.3 Caso uniforme**

Suponha que todos os estágios possuam o mesmo incremento relativo:

ak=a≥0.a\_k=a\\ge0.ak​=a≥0.

Então:

P(n)P(0)=∏k=1n(1+a)=(1+a)n.\\frac{P^{(n)}}{P^{(0)}} \= \\prod\_{k=1}^{n}(1+a) \= (1+a)^n.P(0)P(n)​=k=1∏n​(1+a)=(1+a)n.

Por LB2:

(1+a)n≥1+na.(1+a)^n\\ge1+na.(1+a)n≥1+na.

Logo:

P(n)P(0)≥1+na.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge 1+na. }P(0)P(n)​≥1+na.​

Se

a=ρ1−ρp\~ 2,a= \\frac{\\rho}{1-\\rho}\\widetilde p^{\\,2},a=1−ρρ​p​2,

com 0\<ρ\<10\<\\rho\<10\<ρ\<1 e p\~\\widetilde pp​ adimensional, então:

P(n)P(0)≥1+nρ1−ρp\~ 2.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge 1+ n\\frac{\\rho}{1-\\rho}\\widetilde p^{\\,2}. }P(0)P(n)​≥1+n1−ρρ​p​2.​

Essa é a versão correta do corolário uniforme.

### **Observação importante**

Quando a\>0a\>0a\>0, o crescimento exato é exponencial:

P(n)P(0)=(1+a)n.\\frac{P^{(n)}}{P^{(0)}}=(1+a)^n.P(0)P(n)​=(1+a)n.

O termo

1+na1+na1+na

é apenas um lower bound linear de primeira ordem.

Portanto, deve-se distinguir:

* **comportamento exato:** exponencial;  
* **lower bound elementar:** linear;  
* **interpretação:** a cascata cresce ao menos tão rapidamente quanto 1+na1+na1+na, mas normalmente cresce mais rapidamente.

---

## **16.4 Piso estágio a estágio**

Suponha que exista uma constante a‾\>0\\underline a\>0a​\>0 tal que:

ak≥a‾a\_k\\ge\\underline aak​≥a​

para todo estágio kkk.

Então:

1+ak≥1+a‾.1+a\_k\\ge1+\\underline a.1+ak​≥1+a​.

Multiplicando as desigualdades:

∏k=1n(1+ak)≥(1+a‾)n.\\prod\_{k=1}^{n}(1+a\_k) \\ge (1+\\underline a)^n.k=1∏n​(1+ak​)≥(1+a​)n.

Portanto:

P(n)P(0)≥(1+a‾)n.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge (1+\\underline a)^n. }P(0)P(n)​≥(1+a​)n.​

Aplicando a desigualdade de Bernoulli:

(1+a‾)n≥1+na‾,(1+\\underline a)^n \\ge 1+n\\underline a,(1+a​)n≥1+na​,

obtemos:

P(n)P(0)≥(1+a‾)n≥1+na‾.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge (1+\\underline a)^n \\ge 1+n\\underline a. }P(0)P(n)​≥(1+a​)n≥1+na​.​

Este resultado é mais forte que LB2: um piso positivo em cada estágio fornece um lower bound exponencial e, como consequência, também um lower bound linear.

---

## **16.5 Piso médio**

Exigir que todos os estágios satisfaçam

ak≥a‾a\_k\\ge\\underline aak​≥a​

pode ser excessivamente restritivo. Alguns estágios podem ter amplificação pequena ou até nula.

Uma condição mais fraca é exigir apenas que a média acumulada possua um piso positivo:

1n∑k=1nak≥a‾\>0.\\frac1n\\sum\_{k=1}^{n}a\_k\\ge\\overline a\>0.n1​k=1∑n​ak​≥a\>0.

Então:

∑k=1nak≥na‾.\\sum\_{k=1}^{n}a\_k\\ge n\\overline a.k=1∑n​ak​≥na.

Por LB2:

P(n)P(0)≥1+na‾.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge 1+n\\overline a. }P(0)P(n)​≥1+na.​

Essa hipótese permite que alguns aka\_kak​ sejam zero, desde que os demais mantenham uma média positiva.

---

## **16.6 Condição assintótica**

Para estudar apenas o comportamento quando n→∞n\\to\\inftyn→∞, basta uma condição mais fraca:

lim inf⁡n→∞1n∑k=1nak=μ\>0.\\liminf\_{n\\to\\infty} \\frac1n\\sum\_{k=1}^{n}a\_k \= \\mu\>0.n→∞liminf​n1​k=1∑n​ak​=μ\>0.

Pela definição de limite inferior, para todo ε∈(0,μ)\\varepsilon\\in(0,\\mu)ε∈(0,μ), existe NεN\_\\varepsilonNε​ tal que, para n≥Nεn\\ge N\_\\varepsilonn≥Nε​,

1n∑k=1nak≥μ−ε.\\frac1n\\sum\_{k=1}^{n}a\_k \\ge \\mu-\\varepsilon.n1​k=1∑n​ak​≥μ−ε.

Consequentemente:

∑k=1nak≥n(μ−ε).\\sum\_{k=1}^{n}a\_k \\ge n(\\mu-\\varepsilon).k=1∑n​ak​≥n(μ−ε).

Por LB2:

P(n)P(0)≥1+n(μ−ε),n≥Nε.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge 1+n(\\mu-\\varepsilon), \\qquad n\\ge N\_\\varepsilon. }P(0)P(n)​≥1+n(μ−ε),n≥Nε​.​

Assim, a cascata possui lower bound assintoticamente linear sempre que a média assintótica inferior dos incrementos for positiva.

---

## **16.7 Classificação segundo a soma acumulada**

Defina:

Sn=∑k=1nak.S\_n=\\sum\_{k=1}^{n}a\_k.Sn​=k=1∑n​ak​.

Então:

P(n)P(0)≥1+Sn.\\frac{P^{(n)}}{P^{(0)}}\\ge1+S\_n.P(0)P(n)​≥1+Sn​.

O lower bound pode ser classificado pelo comportamento de SnS\_nSn​.

### **Caso A: soma limitada**

Se:

sup⁡nSn\<∞,\\sup\_n S\_n\<\\infty,nsup​Sn​\<∞,

LB2 não implica crescimento ilimitado.

Exemplo:

ak=1k2.a\_k=\\frac1{k^2}.ak​=k21​.

### **Caso B: crescimento sublinear**

Se:

Sn→∞eSnn→0,S\_n\\to\\infty \\quad\\text{e}\\quad \\frac{S\_n}{n}\\to0,Sn​→∞enSn​​→0,

o lower bound diverge, mas de forma sublinear.

Exemplo:

ak=1k.a\_k=\\frac1k.ak​=k1​.

Nesse caso:

Sn∼log⁡n,S\_n\\sim\\log n,Sn​∼logn,

de modo que:

P(n)P(0)≥1+O(log⁡n).\\frac{P^{(n)}}{P^{(0)}} \\ge 1+O(\\log n).P(0)P(n)​≥1+O(logn).

### **Caso C: crescimento linear**

Se:

Sn≥cnS\_n\\ge cnSn​≥cn

para alguma constante c\>0c\>0c\>0, então:

P(n)P(0)≥1+cn.\\frac{P^{(n)}}{P^{(0)}} \\ge 1+cn.P(0)P(n)​≥1+cn.

### **Caso D: crescimento superlinear**

Se:

Snn→∞,\\frac{S\_n}{n}\\to\\infty,nSn​​→∞,

o lower bound aditivo é superlinear.

Por exemplo, se:

ak=k,a\_k=k,ak​=k,

então:

Sn=n(n+1)2,S\_n=\\frac{n(n+1)}2,Sn​=2n(n+1)​,

e:

P(n)P(0)≥1+n(n+1)2.\\frac{P^{(n)}}{P^{(0)}} \\ge 1+\\frac{n(n+1)}2.P(0)P(n)​≥1+2n(n+1)​.

---

## **16.8 O produto pode crescer mesmo quando LB2 é pouco informativo**

LB2 considera apenas o termo de primeira ordem:

1+∑k=1nak.1+\\sum\_{k=1}^{n}a\_k.1+k=1∑n​ak​.

Mas o produto contém termos de ordem superior:

∏k=1n(1+ak)=1+∑iai+∑i\<jaiaj+⋯ .\\prod\_{k=1}^{n}(1+a\_k) \= 1+ \\sum\_i a\_i+ \\sum\_{i\<j}a\_i a\_j+ \\cdots.k=1∏n​(1+ak​)=1+i∑​ai​+i\<j∑​ai​aj​+⋯.

Por isso, o lower bound aditivo pode ser bastante conservador.

Uma análise assintótica mais precisa utiliza logaritmos:

log⁡(P(n)P(0))=∑k=1nlog⁡(1+ak).\\log \\left( \\frac{P^{(n)}}{P^{(0)}} \\right) \= \\sum\_{k=1}^{n}\\log(1+a\_k).log(P(0)P(n)​)=k=1∑n​log(1+ak​).

Se existir A\<∞A\<\\inftyA\<∞ tal que

0≤ak≤A,0\\le a\_k\\le A,0≤ak​≤A,

então:

log⁡(1+ak)≥log⁡(1+A)Aak,\\log(1+a\_k) \\ge \\frac{\\log(1+A)}{A}a\_k,log(1+ak​)≥Alog(1+A)​ak​,

com a interpretação contínua usual quando A=0A=0A=0.

Logo:

log⁡(P(n)P(0))≥log⁡(1+A)A∑k=1nak.\\log \\left( \\frac{P^{(n)}}{P^{(0)}} \\right) \\ge \\frac{\\log(1+A)}{A} \\sum\_{k=1}^{n}a\_k.log(P(0)P(n)​)≥Alog(1+A)​k=1∑n​ak​.

Portanto:

P(n)P(0)≥exp⁡(log⁡(1+A)A∑k=1nak).\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge \\exp\\left( \\frac{\\log(1+A)}{A} \\sum\_{k=1}^{n}a\_k \\right). }P(0)P(n)​≥exp(Alog(1+A)​k=1∑n​ak​).​

Se:

∑k=1nak≥cn,\\sum\_{k=1}^{n}a\_k\\ge cn,k=1∑n​ak​≥cn,

então:

P(n)P(0)≥exp⁡(clog⁡(1+A)An).\\frac{P^{(n)}}{P^{(0)}} \\ge \\exp\\left( \\frac{c\\log(1+A)}{A}n \\right).P(0)P(n)​≥exp(Aclog(1+A)​n).

Assim, sob limitação superior e média inferior positiva dos incrementos, o crescimento multiplicativo não é apenas linear: ele possui lower bound exponencial.

---

## **16.9 Aplicação à parametrização do Eixo 2**

Considere:

ak=ρk1−ρkp\~k 2,a\_k \= \\frac{\\rho\_k}{1-\\rho\_k}\\widetilde p\_k^{\\,2},ak​=1−ρk​ρk​​p​k2​,

com:

0\<ρk\<10\<\\rho\_k\<10\<ρk​\<1

e p\~k\\widetilde p\_kp​k​ adimensional.

Para garantir um piso estágio a estágio, suponha:

ρk≥ρ‾\>0\\rho\_k\\ge\\underline\\rho\>0ρk​≥ρ​\>0

e

p\~k≥p‾\>0.\\widetilde p\_k\\ge\\underline p\>0.p​k​≥p​\>0.

A função

g(ρ)=ρ1−ρg(\\rho)=\\frac{\\rho}{1-\\rho}g(ρ)=1−ρρ​

é estritamente crescente em (0,1)(0,1)(0,1), pois:

g′(ρ)=1(1−ρ)2\>0.g'(\\rho)=\\frac1{(1-\\rho)^2}\>0.g′(ρ)=(1−ρ)21​\>0.

Logo:

ρk1−ρk≥ρ‾1−ρ‾.\\frac{\\rho\_k}{1-\\rho\_k} \\ge \\frac{\\underline\\rho}{1-\\underline\\rho}.1−ρk​ρk​​≥1−ρ​ρ​​.

Além disso:

p\~k 2≥p‾ 2.\\widetilde p\_k^{\\,2}\\ge\\underline p^{\\,2}.p​k2​≥p​2.

Portanto:

ak≥ρ‾1−ρ‾p‾ 2.a\_k \\ge \\frac{\\underline\\rho}{1-\\underline\\rho} \\underline p^{\\,2}.ak​≥1−ρ​ρ​​p​2.

Definindo:

a‾=ρ‾1−ρ‾p‾ 2,\\underline a \= \\frac{\\underline\\rho}{1-\\underline\\rho} \\underline p^{\\,2},a​=1−ρ​ρ​​p​2,

obtemos:

P(n)P(0)≥(1+a‾)n≥1+na‾.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge (1+\\underline a)^n \\ge 1+n\\underline a. }P(0)P(n)​≥(1+a​)n≥1+na​.​

Explicitamente:

P(n)P(0)≥(1+ρ‾1−ρ‾p‾ 2)n\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge \\left( 1+ \\frac{\\underline\\rho}{1-\\underline\\rho} \\underline p^{\\,2} \\right)^n }P(0)P(n)​≥(1+1−ρ​ρ​​p​2)n​

e, consequentemente,

P(n)P(0)≥1+nρ‾1−ρ‾p‾ 2.\\boxed{ \\frac{P^{(n)}}{P^{(0)}} \\ge 1+ n \\frac{\\underline\\rho}{1-\\underline\\rho} \\underline p^{\\,2}. }P(0)P(n)​≥1+n1−ρ​ρ​​p​2.​

Esse é o corolário adequado para sustentar uma afirmação de crescimento pelo menos linear.

---

## **16.10 Teorema revisado de crescimento da cascata**

### **Teorema LC**

Seja:

Cn=∏k=1n(1+ak),ak≥0.C\_n=\\prod\_{k=1}^{n}(1+a\_k), \\qquad a\_k\\ge0.Cn​=k=1∏n​(1+ak​),ak​≥0.

Então:

1. para toda sequência não negativa,  
    Cn≥1+∑k=1nak;C\_n\\ge1+\\sum\_{k=1}^{n}a\_k;Cn​≥1+k=1∑n​ak​;  
2. se existe a‾\>0\\overline a\>0a\>0 tal que  
    1n∑k=1nak≥a‾\\frac1n\\sum\_{k=1}^{n}a\_k\\ge\\overline an1​k=1∑n​ak​≥a  
    para todo nnn, então  
    Cn≥1+na‾;C\_n\\ge1+n\\overline a;Cn​≥1+na;  
3. se existe a‾\>0\\underline a\>0a​\>0 tal que  
    ak≥a‾a\_k\\ge\\underline aak​≥a​  
    para todo kkk, então  
    Cn≥(1+a‾)n≥1+na‾;C\_n\\ge(1+\\underline a)^n\\ge1+n\\underline a;Cn​≥(1+a​)n≥1+na​;  
4. sem uma hipótese de piso médio positivo, LB2 não implica crescimento linear uniforme em nnn.

### **Prova**

A primeira afirmação é LB2.

Para a segunda, a hipótese fornece:

∑k=1nak≥na‾.\\sum\_{k=1}^{n}a\_k\\ge n\\overline a.k=1∑n​ak​≥na.

Aplicando LB2:

Cn≥1+∑k=1nak≥1+na‾.C\_n \\ge 1+\\sum\_{k=1}^{n}a\_k \\ge 1+n\\overline a.Cn​≥1+k=1∑n​ak​≥1+na.

Para a terceira, de ak≥a‾a\_k\\ge\\underline aak​≥a​ segue:

1+ak≥1+a‾.1+a\_k\\ge1+\\underline a.1+ak​≥1+a​.

Logo:

Cn=∏k=1n(1+ak)≥(1+a‾)n.C\_n \= \\prod\_{k=1}^{n}(1+a\_k) \\ge (1+\\underline a)^n.Cn​=k=1∏n​(1+ak​)≥(1+a​)n.

A desigualdade

(1+a‾)n≥1+na‾(1+\\underline a)^n\\ge1+n\\underline a(1+a​)n≥1+na​

decorre da desigualdade de Bernoulli.

A quarta afirmação é demonstrada pelo contraexemplo:

ak=1k2,a\_k=\\frac1{k^2},ak​=k21​,

para o qual as somas parciais permanecem limitadas. ∎

---

## **16.11 Formulação recomendada para o resumo do trabalho**

Substituir:

> “LB2 prova que a amplificação bullwhip cresce pelo menos linearmente em nnn.”

por:

> **“LB2 fornece o lower bound geral**

> P(n)P(0)≥1+∑k=1nak.\\frac{P^{(n)}}{P^{(0)}} \\ge 1+\\sum\_{k=1}^{n}a\_k.P(0)P(n)​≥1+k=1∑n​ak​.

> **A partir dele, obtém-se crescimento pelo menos linear em nnn quando a média acumulada dos incrementos locais possui um piso positivo independente de nnn. No caso uniforme, ou sob um piso positivo estágio a estágio, o modelo multiplicativo possui de fato crescimento exponencial, do qual o bound linear é uma consequência.”**

Essa formulação é rigorosa, evita uma generalização falsa e fortalece o resultado nos casos em que existem hipóteses quantitativas uniformes.

**Principais mudanças:** corrigi a notação, introduzi a condição exata para o lower bound linear, distingui crescimento do bound e crescimento do produto, acrescentei contraexemplos e formulei um novo Teorema LC pronto para integrar ao documento.


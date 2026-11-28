# **Desenvolvimento ampliado do TGH**

## **Teorema da Transição Global Heterogênea, limiares globais, compensação entre estágios e robustez**

A direção mais fértil é transformar o resultado local em uma teoria comparativa de cascatas. O avanço central consiste em passar da comparação de incrementos isolados para uma comparação exata entre **produtos acumulados**, usando o domínio logarítmico para obter critérios aditivos, certificados robustos e regras de intervenção.

Os resultados abaixo estão provados dentro do modelo proposto. A possível originalidade está na **combinação específica** entre as pontes PFA×DFA, o limiar quartico local, a composição heterogênea e os limiares globais fechados. As ferramentas matemáticas subjacentes, como produtos multiplicativos, logaritmos, AM–GM e taxas de crescimento, são clássicas. A literatura sobre bullwhip também já inclui cadeias multiestágio, várias métricas e lower bounds dependentes de políticas e lead times, portanto a reivindicação de novidade deverá ser feita somente após pesquisa bibliográfica direcionada. [\[arxiv.org\]](https://arxiv.org/pdf/2604.13478), [\[arxiv.org\]](https://arxiv.org/html/2604.13478), [\[researchpo...ulisboa.pt\]](https://researchportal.ulisboa.pt/en/publications/effective-bullwhip-metrics-for-multi-echelon-distribution-systems/)

---

# **1\. Estrutura formal da cascata**

Considere uma cadeia com n≥1n\\ge1n≥1 estágios.

Para cada estágio k∈{1,…,n}k\\in\\{1,\\ldots,n\\}k∈{1,…,n}, sejam:

0\<ρk\<1,pk\>0,ek≥0.0\<\\rho\_k\<1, \\qquad p\_k\>0, \\qquad e\_k\\ge0.0\<ρk​\<1,pk​\>0,ek​≥0.

Assumimos que pkp\_kpk​ e eke\_kek​ já foram normalizados e são adimensionais. Caso possuam unidade física, devem ser substituídos por:

p\~k=pksk,e\~k=eksk,\\widetilde p\_k=\\frac{p\_k}{s\_k}, \\qquad \\widetilde e\_k=\\frac{e\_k}{s\_k},p​k​=sk​pk​​,ek​=sk​ek​​,

para alguma escala de referência sk\>0s\_k\>0sk​\>0.

Definimos os incrementos locais:

dk=ρk1−ρkpk2d\_k \= \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2dk​=1−ρk​ρk​​pk2​

e

fk=ρk1−ρkek2.f\_k \= \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k}e\_k^2.fk​=1−ρk​ρk​​​ek2​.

Por construção:

dk\>0,fk≥0.d\_k\>0, \\qquad f\_k\\ge0.dk​\>0,fk​≥0.

Os fatores locais completos são:

Dk=1+dk,Fk=1+fk.D\_k=1+d\_k, \\qquad F\_k=1+f\_k.Dk​=1+dk​,Fk​=1+fk​.

As cascatas acumuladas são:

AD(n)=∏k=1nDk=∏k=1n(1+dk)A\_D^{(n)} \= \\prod\_{k=1}^{n}D\_k \= \\prod\_{k=1}^{n}(1+d\_k)AD(n)​=k=1∏n​Dk​=k=1∏n​(1+dk​)

e

AF(n)=∏k=1nFk=∏k=1n(1+fk).A\_F^{(n)} \= \\prod\_{k=1}^{n}F\_k \= \\prod\_{k=1}^{n}(1+f\_k).AF(n)​=k=1∏n​Fk​=k=1∏n​(1+fk​).

A interpretação é que AD(n)A\_D^{(n)}AD(n)​ e AF(n)A\_F^{(n)}AF(n)​ medem a amplificação acumulada da mesma grandeza positiva sob os mecanismos DFA e PFA.

Isso é particularmente natural quando cada fator é uma razão consecutiva:

Dk=PD(k)PD(k−1),Fk=PF(k)PF(k−1).D\_k=\\frac{P\_D^{(k)}}{P\_D^{(k-1)}}, \\qquad F\_k=\\frac{P\_F^{(k)}}{P\_F^{(k-1)}}.Dk​=PD(k−1)​PD(k)​​,Fk​=PF(k−1)​PF(k)​​.

Nesse caso, os produtos telescopam:

AD(n)=PD(n)PD(0),AF(n)=PF(n)PF(0).A\_D^{(n)} \= \\frac{P\_D^{(n)}}{P\_D^{(0)}}, \\qquad A\_F^{(n)} \= \\frac{P\_F^{(n)}}{P\_F^{(0)}}.AD(n)​=PD(0)​PD(n)​​,AF(n)​=PF(0)​PF(n)​​.

Em aplicações bullwhip, produtos de razões locais podem representar razões cumulativas de variância, desde que numeradores, denominadores, janelas temporais e escalas sejam compatíveis. A literatura também utiliza razões de coeficientes de variação, estoque médio e variância de pedidos, por isso a métrica concreta deve ser declarada antes da aplicação. [\[researchpo...ulisboa.pt\]](https://researchportal.ulisboa.pt/en/publications/effective-bullwhip-metrics-for-multi-echelon-distribution-systems/), [\[metricgate.com\]](https://metricgate.com/docs/bullwhip-effect-quantification/)

---

# **2\. Mitigação global**

## **Definição 2.1**

A mitigação global do PFA em relação ao DFA é:

Mn=AD(n)−AF(n)AD(n).\\mathcal M\_n \= \\frac{A\_D^{(n)}-A\_F^{(n)}}{A\_D^{(n)}}.Mn​=AD(n)​AD(n)​−AF(n)​​.

Como:

AD(n)\>0,A\_D^{(n)}\>0,AD(n)​\>0,

a definição é bem formada.

Simplificando:

Mn=1−AF(n)AD(n).\\mathcal M\_n \= 1-\\frac{A\_F^{(n)}}{A\_D^{(n)}}.Mn​=1−AD(n)​AF(n)​​.

Portanto:

Mn=1−∏k=1n1+fk1+dk.\\boxed{ \\mathcal M\_n \= 1- \\prod\_{k=1}^{n} \\frac{1+f\_k}{1+d\_k} }.Mn​=1−k=1∏n​1+dk​1+fk​​​.

Defina a razão comparativa local:

rk=1+fk1+dk\>0.r\_k \= \\frac{1+f\_k}{1+d\_k}\>0.rk​=1+dk​1+fk​​\>0.

Então:

Mn=1−∏k=1nrk.\\boxed{ \\mathcal M\_n=1-\\prod\_{k=1}^{n}r\_k. }Mn​=1−k=1∏n​rk​.​

---

## **2.1 Interpretação do sinal**

Temos:

Mn\>0  ⟺  AF(n)\<AD(n).\\mathcal M\_n\>0 \\iff A\_F^{(n)}\<A\_D^{(n)}.Mn​\>0⟺AF(n)​\<AD(n)​.

Assim:

* Mn\>0\\mathcal M\_n\>0Mn​\>0: PFA vence globalmente;  
* Mn=0\\mathcal M\_n=0Mn​=0: break-even global;  
* Mn\<0\\mathcal M\_n\<0Mn​\<0: PFA perde globalmente;  
* Mn≥c\\mathcal M\_n\\ge cMn​≥c: PFA reduz pelo menos a fração ccc da amplificação DFA.

Observe que:

Mn\<1,\\mathcal M\_n\<1,Mn​\<1,

pois o produto dos rkr\_krk​ é estritamente positivo.

Quando fk≥0f\_k\\ge0fk​≥0, também temos:

AF(n)≥1.A\_F^{(n)}\\ge1.AF(n)​≥1.

Logo, para parâmetros finitos, a mitigação total Mn=1\\mathcal M\_n=1Mn​=1 nunca é atingida. Ela pode surgir apenas como limite assintótico.

---

# **3\. Distinção entre três noções de mitigação**

É importante separar:

1. mitigação do incremento;  
2. mitigação do fator local completo;  
3. mitigação global da cascata.

## **3.1 Mitigação incremental**

Para dk\>0d\_k\>0dk​\>0, define-se:

Mk=dk−fkdk=1−fkdk.M\_k \= \\frac{d\_k-f\_k}{d\_k} \= 1-\\frac{f\_k}{d\_k}.Mk​=dk​dk​−fk​​=1−dk​fk​​.

Usando as pontes:

Mk=1−qk2ρk,qk=ekpk.M\_k \= 1-\\frac{q\_k^2}{\\sqrt{\\rho\_k}}, \\qquad q\_k=\\frac{e\_k}{p\_k}.Mk​=1−ρk​​qk2​​,qk​=pk​ek​​.

## **3.2 Mitigação local completa**

Define-se:

μk=1−1+fk1+dk.\\mu\_k \= 1-\\frac{1+f\_k}{1+d\_k}.μk​=1−1+dk​1+fk​​.

Então:

μk=dk−fk1+dk.\\mu\_k \= \\frac{d\_k-f\_k}{1+d\_k}.μk​=1+dk​dk​−fk​​.

Como:

dk−fk=dkMk,d\_k-f\_k=d\_kM\_k,dk​−fk​=dk​Mk​,

obtemos:

μk=dk1+dkMk.\\boxed{ \\mu\_k \= \\frac{d\_k}{1+d\_k}M\_k. }μk​=1+dk​dk​​Mk​.​

Portanto:

∣μk∣≤∣Mk∣,|\\mu\_k|\\le |M\_k|,∣μk​∣≤∣Mk​∣,

pois:

0\<dk1+dk\<1.0\<\\frac{d\_k}{1+d\_k}\<1.0\<1+dk​dk​​\<1.

A mitigação incremental pode parecer elevada, mas sua ação sobre o fator completo é amortecida pelo termo basal 111\.

## **3.3 Mitigação global**

Como:

rk=1−μk,r\_k=1-\\mu\_k,rk​=1−μk​,

temos:

Mn=1−∏k=1n(1−μk).\\boxed{ \\mathcal M\_n \= 1-\\prod\_{k=1}^{n}(1-\\mu\_k). }Mn​=1−k=1∏n​(1−μk​).​

Essa identidade conecta diretamente mitigação local e mitigação global.

---

# **4\. Teorema da Transição Global Heterogênea**

## **Teorema TGH**

Sejam n≥1n\\ge1n≥1, dk\>−1d\_k\>-1dk​\>−1 e fk\>−1f\_k\>-1fk​\>−1, de forma que:

1+dk\>0,1+fk\>0.1+d\_k\>0, \\qquad 1+f\_k\>0.1+dk​\>0,1+fk​\>0.

Defina:

AD(n)=∏k=1n(1+dk),A\_D^{(n)} \= \\prod\_{k=1}^{n}(1+d\_k),AD(n)​=k=1∏n​(1+dk​), AF(n)=∏k=1n(1+fk),A\_F^{(n)} \= \\prod\_{k=1}^{n}(1+f\_k),AF(n)​=k=1∏n​(1+fk​),

e:

Mn=1−AF(n)AD(n).\\mathcal M\_n \= 1-\\frac{A\_F^{(n)}}{A\_D^{(n)}}.Mn​=1−AD(n)​AF(n)​​.

Então, para todo c\<1c\<1c\<1, são equivalentes:

(i)Mn≥c;\\mathrm{(i)} \\qquad \\mathcal M\_n\\ge c;(i)Mn​≥c; (ii)∏k=1n1+fk1+dk≤1−c;\\mathrm{(ii)} \\qquad \\prod\_{k=1}^{n} \\frac{1+f\_k}{1+d\_k} \\le1-c;(ii)k=1∏n​1+dk​1+fk​​≤1−c; (iii)∑k=1nlog⁡(1+fk1+dk)≤log⁡(1−c);\\mathrm{(iii)} \\qquad \\sum\_{k=1}^{n} \\log\\left(\\frac{1+f\_k}{1+d\_k}\\right) \\le\\log(1-c);(iii)k=1∑n​log(1+dk​1+fk​​)≤log(1−c); (iv)∑k=1n\[log⁡(1+dk)−log⁡(1+fk)\]≥−log⁡(1−c).\\mathrm{(iv)} \\qquad \\sum\_{k=1}^{n} \\left\[ \\log(1+d\_k)-\\log(1+f\_k) \\right\] \\ge-\\log(1-c).(iv)k=1∑n​\[log(1+dk​)−log(1+fk​)\]≥−log(1−c).

Em particular:

Mn\>0  ⟺  ∑k=1nlog⁡(1+dk1+fk)\>0\\boxed{ \\mathcal M\_n\>0 \\iff \\sum\_{k=1}^{n} \\log\\left(\\frac{1+d\_k}{1+f\_k}\\right)\>0 }Mn​\>0⟺k=1∑n​log(1+fk​1+dk​​)\>0​

e:

Mn=0  ⟺  ∑k=1nlog⁡(1+dk)=∑k=1nlog⁡(1+fk).\\boxed{ \\mathcal M\_n=0 \\iff \\sum\_{k=1}^{n} \\log(1+d\_k) \= \\sum\_{k=1}^{n} \\log(1+f\_k). }Mn​=0⟺k=1∑n​log(1+dk​)=k=1∑n​log(1+fk​).​

---

## **Prova completa**

Pela definição:

Mn=1−AF(n)AD(n).\\mathcal M\_n \= 1-\\frac{A\_F^{(n)}}{A\_D^{(n)}}.Mn​=1−AD(n)​AF(n)​​.

Como AD(n)\>0A\_D^{(n)}\>0AD(n)​\>0, temos:

Mn≥c\\mathcal M\_n\\ge cMn​≥c

se, e somente se,

1−AF(n)AD(n)≥c.1-\\frac{A\_F^{(n)}}{A\_D^{(n)}}\\ge c.1−AD(n)​AF(n)​​≥c.

Subtraindo 111 dos dois lados:

−AF(n)AD(n)≥c−1.-\\frac{A\_F^{(n)}}{A\_D^{(n)}}\\ge c-1.−AD(n)​AF(n)​​≥c−1.

Multiplicando por −1-1−1, o sentido da desigualdade é invertido:

AF(n)AD(n)≤1−c.\\frac{A\_F^{(n)}}{A\_D^{(n)}}\\le1-c.AD(n)​AF(n)​​≤1−c.

Como c\<1c\<1c\<1, temos:

1−c\>0.1-c\>0.1−c\>0.

Além disso:

AF(n)AD(n)=∏k=1n(1+fk)∏k=1n(1+dk).\\frac{A\_F^{(n)}}{A\_D^{(n)}} \= \\frac{ \\prod\_{k=1}^{n}(1+f\_k) }{ \\prod\_{k=1}^{n}(1+d\_k) }.AD(n)​AF(n)​​=∏k=1n​(1+dk​)∏k=1n​(1+fk​)​.

Pela positividade dos fatores:

∏k=1n(1+fk)∏k=1n(1+dk)=∏k=1n1+fk1+dk.\\frac{ \\prod\_{k=1}^{n}(1+f\_k) }{ \\prod\_{k=1}^{n}(1+d\_k) } \= \\prod\_{k=1}^{n} \\frac{1+f\_k}{1+d\_k}.∏k=1n​(1+dk​)∏k=1n​(1+fk​)​=k=1∏n​1+dk​1+fk​​.

Logo:

Mn≥c\\mathcal M\_n\\ge cMn​≥c

se, e somente se,

∏k=1n1+fk1+dk≤1−c.\\prod\_{k=1}^{n} \\frac{1+f\_k}{1+d\_k} \\le1-c.k=1∏n​1+dk​1+fk​​≤1−c.

Isso prova a equivalência entre (i) e (ii).

Como cada razão é estritamente positiva, o logaritmo natural pode ser aplicado. Como log⁡\\loglog é estritamente crescente:

∏k=1n1+fk1+dk≤1−c\\prod\_{k=1}^{n} \\frac{1+f\_k}{1+d\_k} \\le1-ck=1∏n​1+dk​1+fk​​≤1−c

se, e somente se,

log⁡\[∏k=1n1+fk1+dk\]≤log⁡(1−c).\\log\\left\[ \\prod\_{k=1}^{n} \\frac{1+f\_k}{1+d\_k} \\right\] \\le \\log(1-c).log\[k=1∏n​1+dk​1+fk​​\]≤log(1−c).

Pela propriedade logarítmica do produto:

log⁡\[∏k=1n1+fk1+dk\]=∑k=1nlog⁡(1+fk1+dk).\\log\\left\[ \\prod\_{k=1}^{n} \\frac{1+f\_k}{1+d\_k} \\right\] \= \\sum\_{k=1}^{n} \\log\\left(\\frac{1+f\_k}{1+d\_k}\\right).log\[k=1∏n​1+dk​1+fk​​\]=k=1∑n​log(1+dk​1+fk​​).

Logo:

∑k=1nlog⁡(1+fk1+dk)≤log⁡(1−c).\\sum\_{k=1}^{n} \\log\\left(\\frac{1+f\_k}{1+d\_k}\\right) \\le \\log(1-c).k=1∑n​log(1+dk​1+fk​​)≤log(1−c).

Isso prova a equivalência entre (ii) e (iii).

Finalmente:

log⁡(1+fk1+dk)=log⁡(1+fk)−log⁡(1+dk).\\log\\left(\\frac{1+f\_k}{1+d\_k}\\right) \= \\log(1+f\_k)-\\log(1+d\_k).log(1+dk​1+fk​​)=log(1+fk​)−log(1+dk​).

Multiplicando a desigualdade por −1-1−1:

∑k=1n\[log⁡(1+dk)−log⁡(1+fk)\]≥−log⁡(1−c).\\sum\_{k=1}^{n} \\left\[ \\log(1+d\_k)-\\log(1+f\_k) \\right\] \\ge \-\\log(1-c).k=1∑n​\[log(1+dk​)−log(1+fk​)\]≥−log(1−c).

Isso prova a equivalência entre (iii) e (iv).

Para c=0c=0c=0, temos:

−log⁡(1−c)=0.-\\log(1-c)=0.−log(1−c)=0.

Consequentemente:

Mn≥0  ⟺  ∑k=1nlog⁡(1+dk1+fk)≥0.\\mathcal M\_n\\ge0 \\iff \\sum\_{k=1}^{n} \\log\\left(\\frac{1+d\_k}{1+f\_k}\\right)\\ge0.Mn​≥0⟺k=1∑n​log(1+fk​1+dk​​)≥0.

A versão estrita segue da estrita monotonicidade das operações utilizadas:

Mn\>0  ⟺  ∑k=1nlog⁡(1+dk1+fk)\>0.\\mathcal M\_n\>0 \\iff \\sum\_{k=1}^{n} \\log\\left(\\frac{1+d\_k}{1+f\_k}\\right)\>0.Mn​\>0⟺k=1∑n​log(1+fk​1+dk​​)\>0.

A igualdade fornece o break-even global. ∎

---

# **5\. Margem logarítmica global**

## **Definição 5.1**

Defina a vantagem logarítmica local:

gk=log⁡(1+dk1+fk).g\_k \= \\log\\left(\\frac{1+d\_k}{1+f\_k}\\right).gk​=log(1+fk​1+dk​​).

Defina a margem global:

Gn=∑k=1ngk.G\_n \= \\sum\_{k=1}^{n}g\_k.Gn​=k=1∑n​gk​.

Então:

AD(n)AF(n)=eGn,\\frac{A\_D^{(n)}}{A\_F^{(n)}}=e^{G\_n},AF(n)​AD(n)​​=eGn​,

ou, equivalentemente:

AF(n)AD(n)=e−Gn.\\frac{A\_F^{(n)}}{A\_D^{(n)}}=e^{-G\_n}.AD(n)​AF(n)​​=e−Gn​.

Portanto:

Mn=1−e−Gn.\\boxed{ \\mathcal M\_n=1-e^{-G\_n}. }Mn​=1−e−Gn​.​

Essa identidade é a forma normal do TGH.

---

## **5.1 Classificação completa**

Como a função

h(G)=1−e−Gh(G)=1-e^{-G}h(G)=1−e−G

é estritamente crescente, temos:

Gn\>0  ⟺  Mn\>0,G\_n\>0 \\iff \\mathcal M\_n\>0,Gn​\>0⟺Mn​\>0, Gn=0  ⟺  Mn=0,G\_n=0 \\iff \\mathcal M\_n=0,Gn​=0⟺Mn​=0, Gn\<0  ⟺  Mn\<0.G\_n\<0 \\iff \\mathcal M\_n\<0.Gn​\<0⟺Mn​\<0.

Além disso:

Mn≥c  ⟺  Gn≥−log⁡(1−c).\\mathcal M\_n\\ge c \\iff G\_n\\ge-\\log(1-c).Mn​≥c⟺Gn​≥−log(1−c).

Defina o orçamento logarítmico necessário para o alvo ccc:

B(c)=−log⁡(1−c).B(c)=-\\log(1-c).B(c)=−log(1−c).

Então:

Mn≥c  ⟺  Gn≥B(c).\\boxed{ \\mathcal M\_n\\ge c \\iff G\_n\\ge B(c). }Mn​≥c⟺Gn​≥B(c).​

A meta de mitigação torna-se um problema de acumulação aditiva de margem.

---

# **6\. Composição exata das mitigações locais**

Como:

1−μk=1+fk1+dk,1-\\mu\_k \= \\frac{1+f\_k}{1+d\_k},1−μk​=1+dk​1+fk​​,

temos:

Mn=1−∏k=1n(1−μk).\\mathcal M\_n \= 1-\\prod\_{k=1}^{n}(1-\\mu\_k).Mn​=1−k=1∏n​(1−μk​).

Expandindo:

Mn=∑iμi−∑i\<jμiμj+∑i\<j\<ℓμiμjμℓ−⋯ .\\mathcal M\_n \= \\sum\_i\\mu\_i \- \\sum\_{i\<j}\\mu\_i\\mu\_j \+ \\sum\_{i\<j\<\\ell}\\mu\_i\\mu\_j\\mu\_\\ell \-\\cdots.Mn​=i∑​μi​−i\<j∑​μi​μj​+i\<j\<ℓ∑​μi​μj​μℓ​−⋯.

No caso n=2n=2n=2:

M2=μ1+μ2−μ1μ2.\\mathcal M\_2 \= \\mu\_1+\\mu\_2-\\mu\_1\\mu\_2.M2​=μ1​+μ2​−μ1​μ2​.

No caso n=3n=3n=3:

M3=μ1+μ2+μ3−μ1μ2−μ1μ3−μ2μ3+μ1μ2μ3.\\mathcal M\_3 \= \\mu\_1+\\mu\_2+\\mu\_3 \- \\mu\_1\\mu\_2-\\mu\_1\\mu\_3-\\mu\_2\\mu\_3 \+ \\mu\_1\\mu\_2\\mu\_3.M3​=μ1​+μ2​+μ3​−μ1​μ2​−μ1​μ3​−μ2​μ3​+μ1​μ2​μ3​.

---

## **6.1 Caso em que todos os estágios favorecem PFA**

Se:

0≤μk\<10\\le\\mu\_k\<10≤μk​\<1

para todo kkk, então:

0≤1−μk≤1.0\\le1-\\mu\_k\\le1.0≤1−μk​≤1.

Logo:

0≤∏k=1n(1−μk)≤10\\le\\prod\_{k=1}^{n}(1-\\mu\_k)\\le10≤k=1∏n​(1−μk​)≤1

e:

0≤Mn\<1.0\\le\\mathcal M\_n\<1.0≤Mn​\<1.

Além disso, como:

1−∏k=1n(1−μk)≥μj1-\\prod\_{k=1}^{n}(1-\\mu\_k) \\ge\\mu\_j1−k=1∏n​(1−μk​)≥μj​

para cada jjj, temos:

Mn≥max⁡kμk.\\boxed{ \\mathcal M\_n\\ge\\max\_k\\mu\_k. }Mn​≥kmax​μk​.​

Por outro lado, pela desigualdade da união:

1−∏k=1n(1−μk)≤∑k=1nμk.1-\\prod\_{k=1}^{n}(1-\\mu\_k) \\le \\sum\_{k=1}^{n}\\mu\_k.1−k=1∏n​(1−μk​)≤k=1∑n​μk​.

Assim:

max⁡kμk≤Mn≤min⁡{1,∑k=1nμk}.\\boxed{ \\max\_k\\mu\_k \\le \\mathcal M\_n \\le \\min\\left\\{1,\\sum\_{k=1}^{n}\\mu\_k\\right\\}. }kmax​μk​≤Mn​≤min{1,k=1∑n​μk​}.​

Esses bounds mostram que:

* a mitigação global nunca é menor que a melhor mitigação local;  
* a soma das mitigações locais é um upper bound;  
* há retornos marginais decrescentes quando muitas mitigações positivas são combinadas.

---

# **7\. Teorema de compensação entre estágios**

## **Teorema TC**

Divida os estágios nos conjuntos:

I+={k:gk\>0},I\_+ \= \\{k:g\_k\>0\\},I+​={k:gk​\>0}, I0={k:gk=0},I\_0 \= \\{k:g\_k=0\\},I0​={k:gk​=0}, I−={k:gk\<0}.I\_- \= \\{k:g\_k\<0\\}.I−​={k:gk​\<0}.

Então:

Mn\>0\\mathcal M\_n\>0Mn​\>0

se, e somente se,

∑k∈I+gk\>∑k∈I−∣gk∣.\\boxed{ \\sum\_{k\\in I\_+}g\_k \> \\sum\_{k\\in I\_-}|g\_k|. }k∈I+​∑​gk​\>k∈I−​∑​∣gk​∣.​

Mais geralmente:

Mn≥c\\mathcal M\_n\\ge cMn​≥c

se, e somente se,

∑k∈I+gk−∑k∈I−∣gk∣≥−log⁡(1−c).\\boxed{ \\sum\_{k\\in I\_+}g\_k \- \\sum\_{k\\in I\_-}|g\_k| \\ge \-\\log(1-c). }k∈I+​∑​gk​−k∈I−​∑​∣gk​∣≥−log(1−c).​

## **Prova**

Por definição:

Gn=∑k=1ngk.G\_n \= \\sum\_{k=1}^{n}g\_k.Gn​=k=1∑n​gk​.

Os termos com índice em I0I\_0I0​ são nulos. Para k∈I−k\\in I\_-k∈I−​:

gk=−∣gk∣.g\_k=-|g\_k|.gk​=−∣gk​∣.

Assim:

Gn=∑k∈I+gk−∑k∈I−∣gk∣.G\_n \= \\sum\_{k\\in I\_+}g\_k \- \\sum\_{k\\in I\_-}|g\_k|.Gn​=k∈I+​∑​gk​−k∈I−​∑​∣gk​∣.

Pelo TGH:

Mn\>0  ⟺  Gn\>0.\\mathcal M\_n\>0 \\iff G\_n\>0.Mn​\>0⟺Gn​\>0.

Substituindo a decomposição de GnG\_nGn​, obtemos a primeira equivalência.

Para o alvo ccc:

Mn≥c  ⟺  Gn≥−log⁡(1−c),\\mathcal M\_n\\ge c \\iff G\_n\\ge-\\log(1-c),Mn​≥c⟺Gn​≥−log(1−c),

o que produz a segunda equivalência. ∎

---

## **7.1 Consequência conceitual**

O PFA não precisa vencer em todos os estágios.

Ele pode perder fortemente em alguns estágios e ainda vencer globalmente se a soma das vantagens logarítmicas superar a soma das desvantagens.

Isso é mais informativo que exigir:

fk≤dkf\_k\\le d\_kfk​≤dk​

para todo kkk.

A condição estágio a estágio é suficiente, mas não necessária.

---

# **8\. Critério local em termos do limiar quartico**

Para cada estágio:

dk=ρk1−ρkpk2,d\_k \= \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2,dk​=1−ρk​ρk​​pk2​, fk=ρk1−ρkek2.f\_k \= \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k}e\_k^2.fk​=1−ρk​ρk​​​ek2​.

Temos:

dk\>fkd\_k\>f\_kdk​\>fk​

se, e somente se,

ρkpk2\>ρkek2.\\rho\_kp\_k^2\>\\sqrt{\\rho\_k}e\_k^2.ρk​pk2​\>ρk​​ek2​.

Como ρk\>0\\sqrt{\\rho\_k}\>0ρk​​\>0:

ρkpk2\>ek2.\\sqrt{\\rho\_k}p\_k^2\>e\_k^2.ρk​​pk2​\>ek2​.

Dividindo por pk2\>0p\_k^2\>0pk2​\>0:

ρk\>ek2pk2=qk2.\\sqrt{\\rho\_k}\>\\frac{e\_k^2}{p\_k^2}=q\_k^2.ρk​​\>pk2​ek2​​=qk2​.

Elevando ao quadrado:

dk\>fk  ⟺  ρk\>qk4.\\boxed{ d\_k\>f\_k \\iff \\rho\_k\>q\_k^4. }dk​\>fk​⟺ρk​\>qk4​.​

Além disso:

gk\>0  ⟺  1+dk\>1+fk  ⟺  dk\>fk.g\_k\>0 \\iff 1+d\_k\>1+f\_k \\iff d\_k\>f\_k.gk​\>0⟺1+dk​\>1+fk​⟺dk​\>fk​.

Portanto:

gk\>0  ⟺  ρk\>qk4.\\boxed{ g\_k\>0 \\iff \\rho\_k\>q\_k^4. }gk​\>0⟺ρk​\>qk4​.​

O limiar quartico local é exatamente o ponto de mudança de sinal da contribuição logarítmica ao resultado global.

---

# **9\. Caso homogêneo**

Suponha:

ρk=ρ,pk=p,ek=e\\rho\_k=\\rho, \\qquad p\_k=p, \\qquad e\_k=eρk​=ρ,pk​=p,ek​=e

para todos os estágios.

Defina:

d(ρ)=ρ1−ρp2,d(\\rho) \= \\frac{\\rho}{1-\\rho}p^2,d(ρ)=1−ρρ​p2, f(ρ)=ρ1−ρe2.f(\\rho) \= \\frac{\\sqrt\\rho}{1-\\rho}e^2.f(ρ)=1−ρρ​​e2.

Então:

AD(n)=(1+d)n,A\_D^{(n)}=(1+d)^n,AD(n)​=(1+d)n, AF(n)=(1+f)n.A\_F^{(n)}=(1+f)^n.AF(n)​=(1+f)n.

A mitigação global é:

Mn(ρ)=1−(1+f(ρ)1+d(ρ))n.\\boxed{ \\mathcal M\_n(\\rho) \= 1- \\left( \\frac{1+f(\\rho)}{1+d(\\rho)} \\right)^n. }Mn​(ρ)=1−(1+d(ρ)1+f(ρ)​)n.​

Defina:

r(ρ)=1+f(ρ)1+d(ρ).r(\\rho) \= \\frac{1+f(\\rho)}{1+d(\\rho)}.r(ρ)=1+d(ρ)1+f(ρ)​.

Então:

Mn(ρ)=1−r(ρ)n.\\mathcal M\_n(\\rho)=1-r(\\rho)^n.Mn​(ρ)=1−r(ρ)n.

---

# **10\. Break-even global homogêneo**

## **Teorema BEG**

Para qualquer n≥1n\\ge1n≥1,

Mn(ρ)=0\\mathcal M\_n(\\rho)=0Mn​(ρ)=0

se, e somente se,

ρ=q4,q=ep,\\rho=q^4, \\qquad q=\\frac ep,ρ=q4,q=pe​,

desde que 0\<q\<10\<q\<10\<q\<1.

Portanto, o break-even global homogêneo é independente do número de estágios.

## **Prova**

Temos:

Mn(ρ)=0\\mathcal M\_n(\\rho)=0Mn​(ρ)=0

se, e somente se,

r(ρ)n=1.r(\\rho)^n=1.r(ρ)n=1.

Como r(ρ)\>0r(\\rho)\>0r(ρ)\>0:

r(ρ)=1.r(\\rho)=1.r(ρ)=1.

Logo:

1+f(ρ)1+d(ρ)=1.\\frac{1+f(\\rho)}{1+d(\\rho)}=1.1+d(ρ)1+f(ρ)​=1.

Portanto:

f(ρ)=d(ρ).f(\\rho)=d(\\rho).f(ρ)=d(ρ).

Pela teoria local:

f(ρ)=d(ρ)  ⟺  ρ=q4.f(\\rho)=d(\\rho) \\iff \\rho=q^4.f(ρ)=d(ρ)⟺ρ=q4.

A condição ρ∈(0,1)\\rho\\in(0,1)ρ∈(0,1) exige 0\<q\<10\<q\<10\<q\<1. ∎

---

# **11\. Teorema do Limiar Global Homogêneo**

Este resultado fornece uma forma fechada para qualquer meta global ccc.

## **Teorema TLGH**

Sejam:

n≥1,p\>0,e≥0,c∈\[0,1).n\\ge1, \\qquad p\>0, \\qquad e\\ge0, \\qquad c\\in\[0,1).n≥1,p\>0,e≥0,c∈\[0,1).

Defina:

tn,c=(1−c)1/nt\_{n,c}=(1-c)^{1/n}tn,c​=(1−c)1/n

e:

An,c=1+tn,c(p2−1).A\_{n,c} \= 1+t\_{n,c}(p^2-1).An,c​=1+tn,c​(p2−1).

Então:

An,c\>0.A\_{n,c}\>0.An,c​\>0.

Defina:

xn,c=e2+e4+4An,c(1−tn,c)2An,c.x\_{n,c} \= \\frac{ e^2+ \\sqrt{ e^4+4A\_{n,c}(1-t\_{n,c}) } }{ 2A\_{n,c} }.xn,c​=2An,c​e2+e4+4An,c​(1−tn,c​)​​.

A condição:

Mn(ρ)≥c\\mathcal M\_n(\\rho)\\ge cMn​(ρ)≥c

é equivalente a:

ρ≥xn,c.\\sqrt\\rho\\ge x\_{n,c}.ρ​≥xn,c​.

Consequentemente, o limiar global é:

ρn,c=\[e2+e4+4An,c(1−tn,c)2An,c\]2.\\boxed{ \\rho\_{n,c} \= \\left\[ \\frac{ e^2+ \\sqrt{ e^4+4A\_{n,c}(1-t\_{n,c}) } }{ 2A\_{n,c} } \\right\]^2. }ρn,c​=\[2An,c​e2+e4+4An,c​(1−tn,c​)​​\]2.​

O alvo é atingível em (0,1)(0,1)(0,1) se, e somente se:

q2n\<1−c.\\boxed{ q^{2n}\<1-c. }q2n\<1−c.​

Equivalentemente:

q\<(1−c)1/(2n).\\boxed{ q\<(1-c)^{1/(2n)}. }q\<(1−c)1/(2n).​

---

## **Prova completa**

Temos:

Mn(ρ)≥c\\mathcal M\_n(\\rho)\\ge cMn​(ρ)≥c

se, e somente se,

1−r(ρ)n≥c.1-r(\\rho)^n\\ge c.1−r(ρ)n≥c.

Logo:

r(ρ)n≤1−c.r(\\rho)^n\\le1-c.r(ρ)n≤1−c.

Como r(ρ)\>0r(\\rho)\>0r(ρ)\>0:

r(ρ)≤(1−c)1/n=tn,c.r(\\rho)\\le(1-c)^{1/n}=t\_{n,c}.r(ρ)≤(1−c)1/n=tn,c​.

Defina:

x=ρ.x=\\sqrt\\rho.x=ρ​.

Como 0\<ρ\<10\<\\rho\<10\<ρ\<1, temos:

0\<x\<1.0\<x\<1.0\<x\<1.

Além disso:

ρ=x2.\\rho=x^2.ρ=x2.

Substituindo:

d(ρ)=x2p21−x2d(\\rho) \= \\frac{x^2p^2}{1-x^2}d(ρ)=1−x2x2p2​

e:

f(ρ)=xe21−x2.f(\\rho) \= \\frac{xe^2}{1-x^2}.f(ρ)=1−x2xe2​.

Assim:

1+f(ρ)=1+xe21−x2=1−x2+xe21−x2,1+f(\\rho) \= 1+\\frac{xe^2}{1-x^2} \= \\frac{1-x^2+xe^2}{1-x^2},1+f(ρ)=1+1−x2xe2​=1−x21−x2+xe2​,

e:

1+d(ρ)=1+x2p21−x2=1−x2+x2p21−x2.1+d(\\rho) \= 1+\\frac{x^2p^2}{1-x^2} \= \\frac{1-x^2+x^2p^2}{1-x^2}.1+d(ρ)=1+1−x2x2p2​=1−x21−x2+x2p2​.

Portanto:

r(x)=1+e2x−x21+(p2−1)x2.r(x) \= \\frac{1+e^2x-x^2} {1+(p^2-1)x^2}.r(x)=1+(p2−1)x21+e2x−x2​.

O denominador é positivo em 0\<x\<10\<x\<10\<x\<1, pois:

1+(p2−1)x2=1−x2+p2x2\>0.1+(p^2-1)x^2 \= 1-x^2+p^2x^2\>0.1+(p2−1)x2=1−x2+p2x2\>0.

A condição:

r(x)≤tn,cr(x)\\le t\_{n,c}r(x)≤tn,c​

equivale a:

1+e2x−x2≤tn,c\[1+(p2−1)x2\].1+e^2x-x^2 \\le t\_{n,c} \\left\[ 1+(p^2-1)x^2 \\right\].1+e2x−x2≤tn,c​\[1+(p2−1)x2\].

Expandindo o lado direito:

1+e2x−x2≤tn,c+tn,c(p2−1)x2.1+e^2x-x^2 \\le t\_{n,c} \+ t\_{n,c}(p^2-1)x^2.1+e2x−x2≤tn,c​+tn,c​(p2−1)x2.

Reorganizando:

1−tn,c+e2x−\[1+tn,c(p2−1)\]x2≤0.1-t\_{n,c}+e^2x \- \\left\[ 1+t\_{n,c}(p^2-1) \\right\]x^2 \\le0.1−tn,c​+e2x−\[1+tn,c​(p2−1)\]x2≤0.

Pela definição de An,cA\_{n,c}An,c​:

1−tn,c+e2x−An,cx2≤0.1-t\_{n,c}+e^2x-A\_{n,c}x^2\\le0.1−tn,c​+e2x−An,c​x2≤0.

Equivalentemente:

An,cx2−e2x−(1−tn,c)≥0.A\_{n,c}x^2-e^2x-(1-t\_{n,c})\\ge0.An,c​x2−e2x−(1−tn,c​)≥0.

Agora:

An,c=1−tn,c+tn,cp2.A\_{n,c} \= 1-t\_{n,c}+t\_{n,c}p^2.An,c​=1−tn,c​+tn,c​p2.

Como p\>0p\>0p\>0, tn,c\>0t\_{n,c}\>0tn,c​\>0 e 1−tn,c≥01-t\_{n,c}\\ge01−tn,c​≥0:

An,c\>0.A\_{n,c}\>0.An,c​\>0.

O polinômio:

P(x)=An,cx2−e2x−(1−tn,c)P(x) \= A\_{n,c}x^2-e^2x-(1-t\_{n,c})P(x)=An,c​x2−e2x−(1−tn,c​)

é uma parábola voltada para cima.

Seu discriminante é:

Δ=e4+4An,c(1−tn,c)≥0.\\Delta \= e^4+4A\_{n,c}(1-t\_{n,c})\\ge0.Δ=e4+4An,c​(1−tn,c​)≥0.

As raízes são:

x±=e2±Δ2An,c.x\_{\\pm} \= \\frac{ e^2\\pm\\sqrt\\Delta }{ 2A\_{n,c} }.x±​=2An,c​e2±Δ​​.

Como:

Δ≥e2,\\sqrt\\Delta\\ge e^2,Δ​≥e2,

temos:

x−≤0x\_-\\le0x−​≤0

e:

x+≥0.x\_+\\ge0.x+​≥0.

Para x\>0x\>0x\>0, a desigualdade P(x)≥0P(x)\\ge0P(x)≥0 vale precisamente quando:

x≥x+.x\\ge x\_+.x≥x+​.

Logo:

x≥e2+e4+4An,c(1−tn,c)2An,c.x\\ge \\frac{ e^2+\\sqrt{ e^4+4A\_{n,c}(1-t\_{n,c}) } }{ 2A\_{n,c} }.x≥2An,c​e2+e4+4An,c​(1−tn,c​)​​.

Como x=ρx=\\sqrt\\rhox=ρ​, obtemos a fórmula de ρn,c\\rho\_{n,c}ρn,c​.

Resta demonstrar a condição de atingibilidade. O alvo é atingível em (0,1)(0,1)(0,1) se, e somente se:

xn,c\<1.x\_{n,c}\<1.xn,c​\<1.

Como P(x)P(x)P(x) muda do sinal negativo para o positivo em xn,cx\_{n,c}xn,c​, temos:

xn,c\<1  ⟺  P(1)\>0.x\_{n,c}\<1 \\iff P(1)\>0.xn,c​\<1⟺P(1)\>0.

Calculando:

P(1)=An,c−e2−(1−tn,c).P(1) \= A\_{n,c}-e^2-(1-t\_{n,c}).P(1)=An,c​−e2−(1−tn,c​).

Substituindo An,cA\_{n,c}An,c​:

P(1)=1+tn,c(p2−1)−e2−1+tn,c.P(1) \= 1+t\_{n,c}(p^2-1)-e^2-1+t\_{n,c}.P(1)=1+tn,c​(p2−1)−e2−1+tn,c​.

Logo:

P(1)=tn,cp2−e2.P(1) \= t\_{n,c}p^2-e^2.P(1)=tn,c​p2−e2.

Portanto:

xn,c\<1  ⟺  tn,cp2\>e2.x\_{n,c}\<1 \\iff t\_{n,c}p^2\>e^2.xn,c​\<1⟺tn,c​p2\>e2.

Dividindo por p2\>0p^2\>0p2\>0:

tn,c\>q2.t\_{n,c}\>q^2.tn,c​\>q2.

Como:

tn,c=(1−c)1/n,t\_{n,c}=(1-c)^{1/n},tn,c​=(1−c)1/n,

temos:

q2\<(1−c)1/n.q^2\<(1-c)^{1/n}.q2\<(1−c)1/n.

Elevando à potência nnn:

q2n\<1−c.q^{2n}\<1-c.q2n\<1−c.

Equivalentemente:

q\<(1−c)1/(2n).q\<(1-c)^{1/(2n)}.q\<(1−c)1/(2n).

Isso conclui a prova. ∎

---

# **12\. Cap global de mitigação**

O caso homogêneo produz um resultado particularmente simples.

Quando:

ρ→1−,\\rho\\to1^-,ρ→1−,

temos:

d(ρ)∼p21−ρ,d(\\rho)\\sim\\frac{p^2}{1-\\rho},d(ρ)∼1−ρp2​, f(ρ)∼e21−ρ.f(\\rho)\\sim\\frac{e^2}{1-\\rho}.f(ρ)∼1−ρe2​.

Logo:

lim⁡ρ→1−1+f(ρ)1+d(ρ)=e2p2=q2.\\lim\_{\\rho\\to1^-} \\frac{1+f(\\rho)}{1+d(\\rho)} \= \\frac{e^2}{p^2} \= q^2.ρ→1−lim​1+d(ρ)1+f(ρ)​=p2e2​=q2.

Consequentemente:

lim⁡ρ→1−Mn(ρ)=1−q2n.\\boxed{ \\lim\_{\\rho\\to1^-}\\mathcal M\_n(\\rho) \= 1-q^{2n}. }ρ→1−lim​Mn​(ρ)=1−q2n.​

Esse é o cap global assintótico da cascata homogênea.

---

## **12.1 Comparação com o cap local**

Para um estágio:

lim⁡ρ→1−M1(ρ)=1−q2.\\lim\_{\\rho\\to1^-}\\mathcal M\_1(\\rho) \= 1-q^2.ρ→1−lim​M1​(ρ)=1−q2.

Para nnn estágios:

lim⁡ρ→1−Mn(ρ)=1−q2n.\\lim\_{\\rho\\to1^-}\\mathcal M\_n(\\rho) \= 1-q^{2n}.ρ→1−lim​Mn​(ρ)=1−q2n.

Se:

0\<q\<1,0\<q\<1,0\<q\<1,

então:

q2n→0.q^{2n}\\to0.q2n→0.

Portanto:

1−q2n→1.1-q^{2n}\\to1.1−q2n→1.

Uma vantagem relativa imperfeita em cada estágio pode produzir mitigação global próxima de 100% quando repetida por muitos estágios.

Isso não significa que a penalidade PFA absoluta tende a zero. Significa somente que ela se torna pequena **em relação à cascata DFA**.

---

# **13\. Número mínimo de estágios para atingir uma meta**

A condição de atingibilidade global é:

q2n\<1−c.q^{2n}\<1-c.q2n\<1−c.

Suponha:

0\<q\<1,0\<c\<1.0\<q\<1, \\qquad 0\<c\<1.0\<q\<1,0\<c\<1.

Tomando logaritmos:

2nlog⁡q\<log⁡(1−c).2n\\log q\<\\log(1-c).2nlogq\<log(1−c).

Como log⁡q\<0\\log q\<0logq\<0, ao dividir por 2log⁡q2\\log q2logq, o sentido da desigualdade é invertido:

n\>log⁡(1−c)2log⁡q.n\> \\frac{\\log(1-c)}{2\\log q}.n\>2logqlog(1−c)​.

Assim, o menor número inteiro de estágios que torna o alvo assintoticamente atingível é:

ncap(q,c)=⌊log⁡(1−c)2log⁡q⌋+1.\\boxed{ n\_{\\mathrm{cap}}(q,c) \= \\left\\lfloor \\frac{\\log(1-c)}{2\\log q} \\right\\rfloor+1. }ncap​(q,c)=⌊2logqlog(1−c)​⌋+1.​

Se a igualdade:

q2n=1−cq^{2n}=1-cq2n=1−c

ocorrer, o alvo é apenas assintótico em ρ→1−\\rho\\to1^-ρ→1−, não atingido em (0,1)(0,1)(0,1). Isso explica o uso da desigualdade estrita.

---

## **13.1 Número de estágios para carga fixa**

Para uma carga fixa com:

0\<r(ρ)\<1,0\<r(\\rho)\<1,0\<r(ρ)\<1,

temos:

Mn=1−r(ρ)n.\\mathcal M\_n=1-r(\\rho)^n.Mn​=1−r(ρ)n.

A condição:

Mn≥c\\mathcal M\_n\\ge cMn​≥c

equivale a:

r(ρ)n≤1−c.r(\\rho)^n\\le1-c.r(ρ)n≤1−c.

Logo:

nlog⁡r(ρ)≤log⁡(1−c).n\\log r(\\rho)\\le\\log(1-c).nlogr(ρ)≤log(1−c).

Como log⁡r(ρ)\<0\\log r(\\rho)\<0logr(ρ)\<0:

n≥log⁡(1−c)log⁡r(ρ).n \\ge \\frac{\\log(1-c)}{\\log r(\\rho)}.n≥logr(ρ)log(1−c)​.

Portanto:

nmin⁡(ρ,c)=⌈log⁡(1−c)log⁡r(ρ)⌉.\\boxed{ n\_{\\min}(\\rho,c) \= \\left\\lceil \\frac{\\log(1-c)} {\\log r(\\rho)} \\right\\rceil. }nmin​(ρ,c)=⌈logr(ρ)log(1−c)​⌉.​

---

# **14\. Convergência dos limiares globais ao break-even**

## **Teorema CL**

Se:

0\<q\<10\<q\<10\<q\<1

e:

0\<c\<1,0\<c\<1,0\<c\<1,

então, para nnn suficientemente grande, o limiar ρn,c\\rho\_{n,c}ρn,c​ existe e:

lim⁡n→∞ρn,c=q4.\\boxed{ \\lim\_{n\\to\\infty}\\rho\_{n,c}=q^4. }n→∞lim​ρn,c​=q4.​

## **Prova**

Temos:

tn,c=(1−c)1/n.t\_{n,c}=(1-c)^{1/n}.tn,c​=(1−c)1/n.

Como 0\<1−c\<10\<1-c\<10\<1−c\<1:

lim⁡n→∞tn,c=1.\\lim\_{n\\to\\infty}t\_{n,c}=1.n→∞lim​tn,c​=1.

Também:

An,c=1+tn,c(p2−1).A\_{n,c} \= 1+t\_{n,c}(p^2-1).An,c​=1+tn,c​(p2−1).

Logo:

lim⁡n→∞An,c=p2.\\lim\_{n\\to\\infty}A\_{n,c}=p^2.n→∞lim​An,c​=p2.

Na fórmula da raiz:

xn,c=e2+e4+4An,c(1−tn,c)2An,c,x\_{n,c} \= \\frac{ e^2+\\sqrt{ e^4+4A\_{n,c}(1-t\_{n,c}) } }{ 2A\_{n,c} },xn,c​=2An,c​e2+e4+4An,c​(1−tn,c​)​​,

temos:

1−tn,c→0.1-t\_{n,c}\\to0.1−tn,c​→0.

Portanto:

e4+4An,c(1−tn,c)→e2.\\sqrt{ e^4+4A\_{n,c}(1-t\_{n,c}) } \\to e^2.e4+4An,c​(1−tn,c​)​→e2.

Assim:

xn,c→e2+e22p2=e2p2=q2.x\_{n,c} \\to \\frac{e^2+e^2}{2p^2} \= \\frac{e^2}{p^2} \= q^2.xn,c​→2p2e2+e2​=p2e2​=q2.

Como:

ρn,c=xn,c2,\\rho\_{n,c}=x\_{n,c}^2,ρn,c​=xn,c2​,

segue que:

ρn,c→q4.\\rho\_{n,c}\\to q^4.ρn,c​→q4.

∎

---

# **15\. Monotonicidade no número de estágios**

## **Teorema MN**

Suponha que, para determinada ρ\\rhoρ,

0\<r(ρ)\<1.0\<r(\\rho)\<1.0\<r(ρ)\<1.

Então:

Mn+1(ρ)\>Mn(ρ)\\mathcal M\_{n+1}(\\rho)\>\\mathcal M\_n(\\rho)Mn+1​(ρ)\>Mn​(ρ)

para todo n≥1n\\ge1n≥1.

Além disso, para um alvo fixo c∈(0,1)c\\in(0,1)c∈(0,1), os limiares homogêneos satisfazem:

ρn+1,c\<ρn,c\\boxed{ \\rho\_{n+1,c}\<\\rho\_{n,c} }ρn+1,c​\<ρn,c​​

sempre que ambos existirem.

## **Prova**

Como:

Mn=1−rn\\mathcal M\_n=1-r^nMn​=1−rn

e 0\<r\<10\<r\<10\<r\<1, temos:

rn+1\<rn.r^{n+1}\<r^n.rn+1\<rn.

Logo:

1−rn+1\>1−rn.1-r^{n+1}\>1-r^n.1−rn+1\>1−rn.

Portanto:

Mn+1\>Mn.\\mathcal M\_{n+1}\>\\mathcal M\_n.Mn+1​\>Mn​.

Agora, ρn,c\\rho\_{n,c}ρn,c​ é a menor carga que permite:

Mn(ρ)≥c.\\mathcal M\_n(\\rho)\\ge c.Mn​(ρ)≥c.

Se uma carga ρ\\rhoρ satisfaz:

Mn(ρ)≥c,\\mathcal M\_n(\\rho)\\ge c,Mn​(ρ)≥c,

então:

Mn+1(ρ)\>Mn(ρ)≥c.\\mathcal M\_{n+1}(\\rho)\> \\mathcal M\_n(\\rho)\\ge c.Mn+1​(ρ)\>Mn​(ρ)≥c.

Assim, o conjunto de cargas admissíveis para n+1n+1n+1 contém estritamente o conjunto admissível para nnn, e o limiar diminui. ∎

---

# **16\. Expansão assintótica do limiar para cascatas longas**

O limite ρn,c→q4\\rho\_{n,c}\\to q^4ρn,c​→q4 pode ser refinado.

Defina:

L=−log⁡(1−c)\>0.L=-\\log(1-c)\>0.L=−log(1−c)\>0.

Então:

tn,c=e−L/n=1−Ln+O(n−2).t\_{n,c} \= e^{-L/n} \= 1-\\frac Ln+O(n^{-2}).tn,c​=e−L/n=1−nL​+O(n−2).

Queremos resolver:

r(xn,c)=tn,c,x=ρ.r(x\_{n,c})=t\_{n,c}, \\qquad x=\\sqrt\\rho.r(xn,c​)=tn,c​,x=ρ​.

No break-even:

x∗=q2x\_\*=q^2x∗​=q2

e:

r(x∗)=1.r(x\_\*)=1.r(x∗​)=1.

A derivada de rrr no break-even pode ser calculada convenientemente pela diferença entre denominador e numerador.

Temos:

r(x)=1+e2x−x21+(p2−1)x2.r(x) \= \\frac{1+e^2x-x^2} {1+(p^2-1)x^2}.r(x)=1+(p2−1)x21+e2x−x2​.

Seja:

N(x)=1+e2x−x2,N(x)=1+e^2x-x^2,N(x)=1+e2x−x2, D(x)=1+(p2−1)x2.D(x)=1+(p^2-1)x^2.D(x)=1+(p2−1)x2.

No break-even, N(x∗)=D(x∗)N(x\_\*)=D(x\_\*)N(x∗​)=D(x∗​).

Além disso:

D(x)−N(x)=p2x2−e2x=x(p2x−e2).D(x)-N(x)=p^2x^2-e^2x=x(p^2x-e^2).D(x)−N(x)=p2x2−e2x=x(p2x−e2).

Derivando:

(D−N)′(x)=2p2x−e2.(D-N)'(x)=2p^2x-e^2.(D−N)′(x)=2p2x−e2.

Em:

x∗=e2p2,x\_\*=\\frac{e^2}{p^2},x∗​=p2e2​,

obtemos:

(D−N)′(x∗)=e2.(D-N)'(x\_\*)=e^2.(D−N)′(x∗​)=e2.

Como r=N/Dr=N/Dr=N/D, segue que:

r′(x∗)=−e2D(x∗).r'(x\_\*) \= \-\\frac{e^2}{D(x\_\*)}.r′(x∗​)=−D(x∗​)e2​.

Agora:

D(x∗)=1+(p2−1)q4.D(x\_\*) \= 1+(p^2-1)q^4.D(x∗​)=1+(p2−1)q4.

Defina:

B∗=1+(p2−1)q4\>0.B\_\*=1+(p^2-1)q^4\>0.B∗​=1+(p2−1)q4\>0.

Então:

r′(x∗)=−e2B∗.r'(x\_\*)=-\\frac{e^2}{B\_\*}.r′(x∗​)=−B∗​e2​.

Por expansão de primeira ordem:

r(xn,c)=1+r′(x∗)(xn,c−q2)+O((xn,c−q2)2).r(x\_{n,c}) \= 1+r'(x\_\*)(x\_{n,c}-q^2) \+ O((x\_{n,c}-q^2)^2).r(xn,c​)=1+r′(x∗​)(xn,c​−q2)+O((xn,c​−q2)2).

Como:

r(xn,c)=1−Ln+O(n−2),r(x\_{n,c}) \= 1-\\frac Ln+O(n^{-2}),r(xn,c​)=1−nL​+O(n−2),

temos:

−e2B∗(xn,c−q2)=−Ln+O(n−2).-\\frac{e^2}{B\_\*}(x\_{n,c}-q^2) \= \-\\frac Ln+O(n^{-2}).−B∗​e2​(xn,c​−q2)=−nL​+O(n−2).

Logo:

xn,c=q2+B∗Le2n+O(n−2).\\boxed{ x\_{n,c} \= q^2+ \\frac{B\_\*L}{e^2n} \+ O(n^{-2}). }xn,c​=q2+e2nB∗​L​+O(n−2).​

Como:

ρn,c=xn,c2,\\rho\_{n,c}=x\_{n,c}^2,ρn,c​=xn,c2​,

obtemos:

ρn,c=q4+2q2B∗Le2n+O(n−2).\\boxed{ \\rho\_{n,c} \= q^4+ \\frac{2q^2B\_\*L}{e^2n} \+ O(n^{-2}). }ρn,c​=q4+e2n2q2B∗​L​+O(n−2).​

Usando e2=q2p2e^2=q^2p^2e2=q2p2:

ρn,c=q4+2\[1+(p2−1)q4\]\[−log⁡(1−c)\]p2n+O(n−2).\\boxed{ \\rho\_{n,c} \= q^4+ \\frac{ 2\\left\[1+(p^2-1)q^4\\right\] \[-\\log(1-c)\] }{ p^2n } \+ O(n^{-2}). }ρn,c​=q4+p2n2\[1+(p2−1)q4\]\[−log(1−c)\]​+O(n−2).​

Esse resultado quantifica a velocidade com que o limiar global se aproxima do break-even:

ρn,c−q4=O(n−1).\\rho\_{n,c}-q^4=O(n^{-1}).ρn,c​−q4=O(n−1).

---

# **17\. Resultado de concentração e distribuição do esforço**

A margem global é:

Gn=∑k=1ngk.G\_n=\\sum\_{k=1}^{n}g\_k.Gn​=k=1∑n​gk​.

Mas, para uma cascata isolada:

Cn=∏k=1n(1+ak),ak≥0,C\_n=\\prod\_{k=1}^{n}(1+a\_k), \\qquad a\_k\\ge0,Cn​=k=1∏n​(1+ak​),ak​≥0,

é útil estudar como a distribuição dos aka\_kak​ afeta o produto.

Fixe:

S=∑k=1nak.S=\\sum\_{k=1}^{n}a\_k.S=k=1∑n​ak​.

## **Teorema EXT**

Sob:

ak≥0,∑k=1nak=S,a\_k\\ge0, \\qquad \\sum\_{k=1}^{n}a\_k=S,ak​≥0,k=1∑n​ak​=S,

temos:

1+S≤∏k=1n(1+ak)≤(1+Sn)n.\\boxed{ 1+S \\le \\prod\_{k=1}^{n}(1+a\_k) \\le \\left(1+\\frac Sn\\right)^n. }1+S≤k=1∏n​(1+ak​)≤(1+nS​)n.​

A igualdade inferior ocorre se, e somente se, no máximo um aka\_kak​ é não nulo.

A igualdade superior ocorre se, e somente se:

a1=⋯=an=Sn.a\_1=\\cdots=a\_n=\\frac Sn.a1​=⋯=an​=nS​.

## **Prova do lower bound**

Por LB2:

∏k=1n(1+ak)≥1+∑k=1nak=1+S.\\prod\_{k=1}^{n}(1+a\_k) \\ge 1+\\sum\_{k=1}^{n}a\_k \= 1+S.k=1∏n​(1+ak​)≥1+k=1∑n​ak​=1+S.

A igualdade ocorre quando todos os produtos envolvendo dois ou mais índices distintos são nulos. Isso equivale a dizer que no máximo um aka\_kak​ é positivo.

## **Prova do upper bound**

A soma dos fatores 1+ak1+a\_k1+ak​ é:

∑k=1n(1+ak)=n+S.\\sum\_{k=1}^{n}(1+a\_k)=n+S.k=1∑n​(1+ak​)=n+S.

Pela desigualdade AM–GM:

\[∏k=1n(1+ak)\]1/n≤n+Sn=1+Sn.\\left\[ \\prod\_{k=1}^{n}(1+a\_k) \\right\]^{1/n} \\le \\frac{n+S}{n} \= 1+\\frac Sn.\[k=1∏n​(1+ak​)\]1/n≤nn+S​=1+nS​.

Elevando à potência nnn:

∏k=1n(1+ak)≤(1+Sn)n.\\prod\_{k=1}^{n}(1+a\_k) \\le \\left(1+\\frac Sn\\right)^n.k=1∏n​(1+ak​)≤(1+nS​)n.

A igualdade em AM–GM ocorre se, e somente se, todos os fatores forem iguais:

1+a1=⋯=1+an.1+a\_1=\\cdots=1+a\_n.1+a1​=⋯=1+an​.

Portanto:

a1=⋯=an=Sn.a\_1=\\cdots=a\_n=\\frac Sn.a1​=⋯=an​=nS​.

∎

O fato de um produto com soma fixa ser maximizado pela distribuição uniforme é uma consequência clássica de AM–GM, não uma novidade isolada. [\[en.wikipedia.org\]](https://en.wikipedia.org/wiki/AM%E2%80%93GM_inequality), [\[rmi.tsu.ge\]](https://rmi.tsu.ge/transactions/TRMI-volumes/177-3/v177%283%29-2.pdf)

---

# **18\. Índice estrutural de interação**

Defina:

Sn=∑k=1nak.S\_n=\\sum\_{k=1}^{n}a\_k.Sn​=k=1∑n​ak​.

Defina o índice:

Hn=log⁡(∏k=1n(1+ak)1+Sn).H\_n \= \\log\\left( \\frac{ \\prod\_{k=1}^{n}(1+a\_k) }{ 1+S\_n } \\right).Hn​=log(1+Sn​∏k=1n​(1+ak​)​).

Por LB2:

Hn≥0.H\_n\\ge0.Hn​≥0.

Além disso:

∏k=1n(1+ak)=(1+Sn)eHn.\\boxed{ \\prod\_{k=1}^{n}(1+a\_k) \= (1+S\_n)e^{H\_n}. }k=1∏n​(1+ak​)=(1+Sn​)eHn​.​

Essa é uma decomposição exata em:

* componente aditiva mínima:  
   1+Sn;1+S\_n;1+Sn​;  
* multiplicador estrutural:  
   eHn.e^{H\_n}.eHn​.

Se Hn=0H\_n=0Hn​=0, a carga está concentrada em no máximo um estágio.

Se Hn\>0H\_n\>0Hn​\>0, existem interações multiplicativas entre estágios.

Pelo teorema extremal:

0≤Hn≤nlog⁡(1+Snn)−log⁡(1+Sn).0 \\le H\_n \\le n\\log\\left(1+\\frac{S\_n}{n}\\right) \-\\log(1+S\_n).0≤Hn​≤nlog(1+nSn​​)−log(1+Sn​).

Para n→∞n\\to\\inftyn→∞ com Sn=SS\_n=SSn​=S fixo:

(1+Sn)n→eS.\\left(1+\\frac Sn\\right)^n\\to e^S.(1+nS​)n→eS.

Portanto:

Hn≤S−log⁡(1+S)+o(1).H\_n \\le S-\\log(1+S)+o(1).Hn​≤S−log(1+S)+o(1).

---

# **19\. Sensibilidade exata da mitigação global**

Como:

Mn=1−e−Gn,\\mathcal M\_n=1-e^{-G\_n},Mn​=1−e−Gn​,

temos:

∂Mn∂Gn=e−Gn=1−Mn.\\frac{\\partial\\mathcal M\_n}{\\partial G\_n} \= e^{-G\_n} \= 1-\\mathcal M\_n.∂Gn​∂Mn​​=e−Gn​=1−Mn​.

Assim:

dMn=(1−Mn)dGn.\\boxed{ d\\mathcal M\_n \= (1-\\mathcal M\_n)dG\_n. }dMn​=(1−Mn​)dGn​.​

Isso revela retornos decrescentes:

* quando Mn\\mathcal M\_nMn​ é pequena, aumentar GnG\_nGn​ tem efeito quase integral;  
* quando Mn\\mathcal M\_nMn​ está próxima de 111, o ganho marginal diminui.

Para o estágio jjj:

gj=log⁡(1+dj)−log⁡(1+fj).g\_j=\\log(1+d\_j)-\\log(1+f\_j).gj​=log(1+dj​)−log(1+fj​).

Logo:

∂Gn∂dj=11+dj,\\frac{\\partial G\_n}{\\partial d\_j} \= \\frac1{1+d\_j},∂dj​∂Gn​​=1+dj​1​, ∂Gn∂fj=−11+fj.\\frac{\\partial G\_n}{\\partial f\_j} \= \-\\frac1{1+f\_j}.∂fj​∂Gn​​=−1+fj​1​.

Portanto:

∂Mn∂dj=1−Mn1+dj\>0\\boxed{ \\frac{\\partial\\mathcal M\_n}{\\partial d\_j} \= \\frac{1-\\mathcal M\_n}{1+d\_j}\>0 }∂dj​∂Mn​​=1+dj​1−Mn​​\>0​

e:

∂Mn∂fj=−1−Mn1+fj\<0.\\boxed{ \\frac{\\partial\\mathcal M\_n}{\\partial f\_j} \= \-\\frac{1-\\mathcal M\_n}{1+f\_j}\<0. }∂fj​∂Mn​​=−1+fj​1−Mn​​\<0.​

Um aumento de djd\_jdj​ torna o PFA relativamente mais vantajoso; um aumento de fjf\_jfj​ reduz sua vantagem.

Isso é uma afirmação comparativa, não uma recomendação para aumentar a penalidade DFA.

---

## **19.1 Sensibilidade ao erro PFA**

Como:

fj=ρj1−ρjej2,f\_j \= \\frac{\\sqrt{\\rho\_j}}{1-\\rho\_j}e\_j^2,fj​=1−ρj​ρj​​​ej2​,

temos:

∂fj∂ej=2ejρj1−ρj.\\frac{\\partial f\_j}{\\partial e\_j} \= 2e\_j \\frac{\\sqrt{\\rho\_j}}{1-\\rho\_j}.∂ej​∂fj​​=2ej​1−ρj​ρj​​​.

Então:

∂Mn∂ej=−(1−Mn)2ejρj1−ρj+ρjej2.\\boxed{ \\frac{\\partial\\mathcal M\_n}{\\partial e\_j} \= \- (1-\\mathcal M\_n) \\frac{ 2e\_j\\sqrt{\\rho\_j} }{ 1-\\rho\_j+\\sqrt{\\rho\_j}e\_j^2 }. }∂ej​∂Mn​​=−(1−Mn​)1−ρj​+ρj​​ej2​2ej​ρj​​​.​

A magnitude:

Jj=2ejρj1−ρj+ρjej2J\_j \= \\frac{ 2e\_j\\sqrt{\\rho\_j} }{ 1-\\rho\_j+\\sqrt{\\rho\_j}e\_j^2 }Jj​=1−ρj​+ρj​​ej2​2ej​ρj​​​

mede a sensibilidade logarítmica da cascata ao erro PFA do estágio jjj.

---

# **20\. Certificado robusto do TGH**

Suponha que os parâmetros não sejam conhecidos exatamente.

Para cada estágio, suponha:

dk≥d‾kd\_k\\ge\\underline d\_kdk​≥d​k​

e:

fk≤f‾k.f\_k\\le\\overline f\_k.fk​≤f​k​.

Então:

1+fk1+dk≤1+f‾k1+d‾k=:r‾k.\\frac{1+f\_k}{1+d\_k} \\le \\frac{1+\\overline f\_k}{1+\\underline d\_k} \=:\\overline r\_k.1+dk​1+fk​​≤1+d​k​1+f​k​​=:rk​.

Consequentemente:

AF(n)AD(n)≤∏k=1nr‾k.\\frac{A\_F^{(n)}}{A\_D^{(n)}} \\le \\prod\_{k=1}^{n}\\overline r\_k.AD(n)​AF(n)​​≤k=1∏n​rk​.

Logo:

Mn≥1−∏k=1nr‾k.\\boxed{ \\mathcal M\_n \\ge 1-\\prod\_{k=1}^{n}\\overline r\_k. }Mn​≥1−k=1∏n​rk​.​

Em forma logarítmica:

Mn≥1−exp⁡(∑k=1nlog⁡r‾k).\\boxed{ \\mathcal M\_n \\ge 1- \\exp\\left( \\sum\_{k=1}^{n}\\log\\overline r\_k \\right). }Mn​≥1−exp(k=1∑n​logrk​).​

Um certificado suficiente para:

Mn≥c\\mathcal M\_n\\ge cMn​≥c

é:

∑k=1nlog⁡(1+f‾k1+d‾k)≤log⁡(1−c).\\boxed{ \\sum\_{k=1}^{n} \\log\\left( \\frac{1+\\overline f\_k} {1+\\underline d\_k} \\right) \\le \\log(1-c). }k=1∑n​log(1+d​k​1+f​k​​)≤log(1−c).​

Esse tipo de certificado é compatível com a perspectiva da otimização robusta, na qual uma solução deve permanecer válida para todas as realizações de parâmetros dentro de um conjunto de incerteza. [\[leclere.github.io\]](https://leclere.github.io/files/teaching/Saclay/Saclay-7.pdf), [\[mit.edu\]](https://www.mit.edu/~dbertsim/papers/Robust%20Optimization/Theory%20and%20applications%20of%20robust%20optimization.pdf)

---

# **21\. Intervalos nos parâmetros primitivos**

Suponha:

ρk∈\[ρk−,ρk+\],\\rho\_k\\in\[\\rho\_k^-,\\rho\_k^+\],ρk​∈\[ρk−​,ρk+​\], pk∈\[pk−,pk+\],p\_k\\in\[p\_k^-,p\_k^+\],pk​∈\[pk−​,pk+​\], ek∈\[ek−,ek+\].e\_k\\in\[e\_k^-,e\_k^+\].ek​∈\[ek−​,ek+​\].

Como:

dk(ρ,p)=ρ1−ρp2d\_k(\\rho,p) \= \\frac{\\rho}{1-\\rho}p^2dk​(ρ,p)=1−ρρ​p2

é crescente em ρ\\rhoρ e ppp, temos:

d‾k=ρk−1−ρk−(pk−)2.\\underline d\_k \= \\frac{\\rho\_k^-}{1-\\rho\_k^-}(p\_k^-)^2.d​k​=1−ρk−​ρk−​​(pk−​)2.

Como:

fk(ρ,e)=ρ1−ρe2f\_k(\\rho,e) \= \\frac{\\sqrt\\rho}{1-\\rho}e^2fk​(ρ,e)=1−ρρ​​e2

é crescente em ρ\\rhoρ e eee, temos:

f‾k=ρk+1−ρk+(ek+)2.\\overline f\_k \= \\frac{\\sqrt{\\rho\_k^+}}{1-\\rho\_k^+}(e\_k^+)^2.f​k​=1−ρk+​ρk+​​​(ek+​)2.

Portanto:

Mn≥1−∏k=1n1+ρk+1−ρk+(ek+)21+ρk−1−ρk−(pk−)2.\\boxed{ \\mathcal M\_n \\ge 1- \\prod\_{k=1}^{n} \\frac{ 1+ \\frac{\\sqrt{\\rho\_k^+}}{1-\\rho\_k^+}(e\_k^+)^2 }{ 1+ \\frac{\\rho\_k^-}{1-\\rho\_k^-}(p\_k^-)^2 }. }Mn​≥1−k=1∏n​1+1−ρk−​ρk−​​(pk−​)21+1−ρk+​ρk+​​​(ek+​)2​.​

Esse certificado é conservador. Ele pode ser melhorado se houver informação sobre dependência entre os parâmetros, porque a combinação simultânea de todos os piores extremos pode ser impossível no sistema real.

---

# **22\. Robustez a erro de modelagem das pontes**

As fórmulas-ponte podem ser apenas aproximações. Considere:

dkreal=dk+δkDd\_k^{\\mathrm{real}} \= d\_k+\\delta\_k^Ddkreal​=dk​+δkD​

e:

fkreal=fk+δkF.f\_k^{\\mathrm{real}} \= f\_k+\\delta\_k^F.fkreal​=fk​+δkF​.

Suponha:

∣δkD∣≤εkD,∣δkF∣≤εkF,|\\delta\_k^D|\\le\\varepsilon\_k^D, \\qquad |\\delta\_k^F|\\le\\varepsilon\_k^F,∣δkD​∣≤εkD​,∣δkF​∣≤εkF​,

e que todos os fatores permaneçam positivos.

A margem real é:

Gnreal=∑k=1n\[log⁡(1+dk+δkD)−log⁡(1+fk+δkF)\].G\_n^{\\mathrm{real}} \= \\sum\_{k=1}^{n} \\left\[ \\log(1+d\_k+\\delta\_k^D) \- \\log(1+f\_k+\\delta\_k^F) \\right\].Gnreal​=k=1∑n​\[log(1+dk​+δkD​)−log(1+fk​+δkF​)\].

Pelo teorema do valor médio, se:

1+dk−εkD\>01+d\_k-\\varepsilon\_k^D\>01+dk​−εkD​\>0

e:

1+fk−εkF\>0,1+f\_k-\\varepsilon\_k^F\>0,1+fk​−εkF​\>0,

então:

∣log⁡(1+dk+δkD)−log⁡(1+dk)∣≤εkD1+dk−εkD,\\left| \\log(1+d\_k+\\delta\_k^D) \- \\log(1+d\_k) \\right| \\le \\frac{\\varepsilon\_k^D} {1+d\_k-\\varepsilon\_k^D},​log(1+dk​+δkD​)−log(1+dk​)​≤1+dk​−εkD​εkD​​,

e:

∣log⁡(1+fk+δkF)−log⁡(1+fk)∣≤εkF1+fk−εkF.\\left| \\log(1+f\_k+\\delta\_k^F) \- \\log(1+f\_k) \\right| \\le \\frac{\\varepsilon\_k^F} {1+f\_k-\\varepsilon\_k^F}.​log(1+fk​+δkF​)−log(1+fk​)​≤1+fk​−εkF​εkF​​.

Portanto:

∣Gnreal−Gn∣≤En,\\boxed{ |G\_n^{\\mathrm{real}}-G\_n| \\le E\_n, }∣Gnreal​−Gn​∣≤En​,​

onde:

En=∑k=1n\[εkD1+dk−εkD+εkF1+fk−εkF\].E\_n \= \\sum\_{k=1}^{n} \\left\[ \\frac{\\varepsilon\_k^D} {1+d\_k-\\varepsilon\_k^D} \+ \\frac{\\varepsilon\_k^F} {1+f\_k-\\varepsilon\_k^F} \\right\].En​=k=1∑n​\[1+dk​−εkD​εkD​​+1+fk​−εkF​εkF​​\].

Assim, se:

Gn−En≥−log⁡(1−c),\\boxed{ G\_n-E\_n \\ge \-\\log(1-c), }Gn​−En​≥−log(1−c),​

então:

Mnreal≥c\\mathcal M\_n^{\\mathrm{real}}\\ge cMnreal​≥c

para toda perturbação admissível.

Esse resultado é importante porque desloca a confiança das fórmulas exatas para uma **margem formal de tolerância ao erro de modelagem**.

---

# **23\. Versão estocástica**

Considere agora fatores aleatórios:

Rk=1+Fk1+Dk\>0.R\_k \= \\frac{1+F\_k}{1+D\_k}\>0.Rk​=1+Dk​1+Fk​​\>0.

A razão acumulada é:

R(n)=∏k=1nRk.R^{(n)} \= \\prod\_{k=1}^{n}R\_k.R(n)=k=1∏n​Rk​.

Defina:

Xk=log⁡Rk.X\_k=\\log R\_k.Xk​=logRk​.

Então:

log⁡R(n)=∑k=1nXk.\\log R^{(n)} \= \\sum\_{k=1}^{n}X\_k.logR(n)=k=1∑n​Xk​.

A mitigação aleatória é:

Mn=1−R(n)=1−exp⁡(∑k=1nXk).\\mathcal M\_n \= 1-R^{(n)} \= 1-\\exp\\left(\\sum\_{k=1}^{n}X\_k\\right).Mn​=1−R(n)=1−exp(k=1∑n​Xk​).

---

## **Teorema estocástico no caso i.i.d.**

Suponha que X1,X2,…X\_1,X\_2,\\ldotsX1​,X2​,… sejam independentes e identicamente distribuídos e:

E\[∣X1∣\]\<∞.\\mathbb E\[|X\_1|\]\<\\infty.E\[∣X1​∣\]\<∞.

Então, pela lei forte dos grandes números:

1nlog⁡R(n)=1n∑k=1nXk⟶E\[X1\]\\frac1n \\log R^{(n)} \= \\frac1n\\sum\_{k=1}^{n}X\_k \\longrightarrow \\mathbb E\[X\_1\]n1​logR(n)=n1​k=1∑n​Xk​⟶E\[X1​\]

quase certamente.

Defina:

λ=E\[log⁡(1+F11+D1)\].\\lambda \= \\mathbb E\\left\[ \\log\\left(\\frac{1+F\_1}{1+D\_1}\\right) \\right\].λ=E\[log(1+D1​1+F1​​)\].

Então:

### **Se λ\<0\\lambda\<0λ\<0**

R(n)→0R^{(n)}\\to0R(n)→0

exponencialmente quase certamente, e:

Mn→1.\\mathcal M\_n\\to1.Mn​→1.

### **Se λ\>0\\lambda\>0λ\>0**

R(n)→∞R^{(n)}\\to\\inftyR(n)→∞

exponencialmente quase certamente, e:

Mn→−∞.\\mathcal M\_n\\to-\\infty.Mn​→−∞.

### **Se λ=0\\lambda=0λ=0**

O termo exponencial dominante desaparece. Flutuações, variância e dependência de ordem superior tornam-se decisivas.

Produtos aleatórios e taxas exponenciais são tradicionalmente estudados por expoentes de Lyapunov e teoremas ergódicos multiplicativos. A extensão do modelo escalar para matrizes ou operadores exigiria ferramentas mais fortes, como cociclos subaditivos e o teorema ergódico multiplicativo. [\[w3.impa.br\]](https://w3.impa.br/~viana/out/lle.pdf), [\[perso.univ...rennes1.fr\]](https://perso.univ-rennes1.fr/sebastien.gouezel/articles/SubMult.pdf), [\[hal.science\]](https://hal.science/hal-02996811v1/file/SubMult.pdf)

---

# **24\. Um ponto sutil: média aritmética versus média geométrica**

A condição correta para vantagem assintótica é:

E\[log⁡R\]\<0,\\mathbb E\[\\log R\]\<0,E\[logR\]\<0,

não necessariamente:

E\[R\]\<1.\\mathbb E\[R\]\<1.E\[R\]\<1.

Como log⁡\\loglog é côncava, Jensen fornece:

E\[log⁡R\]≤log⁡E\[R\].\\mathbb E\[\\log R\] \\le \\log\\mathbb E\[R\].E\[logR\]≤logE\[R\].

Portanto:

E\[R\]\<1\\mathbb E\[R\]\<1E\[R\]\<1

é condição suficiente para:

E\[log⁡R\]\<0.\\mathbb E\[\\log R\]\<0.E\[logR\]\<0.

Mas não é necessária.

Pode ocorrer:

E\[R\]\>1\\mathbb E\[R\]\>1E\[R\]\>1

e ainda:

E\[log⁡R\]\<0.\\mathbb E\[\\log R\]\<0.E\[logR\]\<0.

Isso acontece quando ganhos raros e muito grandes elevam a média aritmética, enquanto a trajetória típica ainda decai multiplicativamente.

Quantidades que se combinam por produto são naturalmente resumidas pela média geométrica, equivalendo à média aritmética dos logaritmos. [\[en.wikipedia.org\]](https://en.wikipedia.org/wiki/Geometric_mean)

Essa distinção pode ser uma contribuição interpretativa importante nas aplicações: avaliar a média simples do fator local pode produzir a decisão errada sobre o comportamento acumulado típico.

---

# **25\. Otimização de intervenção**

Suponha que seja possível investir uk≥0u\_k\\ge0uk​≥0 para reduzir eke\_kek​:

ek=ek(uk),ek′(uk)≤0.e\_k=e\_k(u\_k), \\qquad e\_k'(u\_k)\\le0.ek​=ek​(uk​),ek′​(uk​)≤0.

Com orçamento:

∑k=1nuk≤B.\\sum\_{k=1}^{n}u\_k\\le B.k=1∑n​uk​≤B.

Como:

Gn=∑k=1n\[log⁡(1+dk)−log⁡(1+fk(uk))\],G\_n \= \\sum\_{k=1}^{n} \\left\[ \\log(1+d\_k)-\\log(1+f\_k(u\_k)) \\right\],Gn​=k=1∑n​\[log(1+dk​)−log(1+fk​(uk​))\],

maximizar a mitigação equivale a maximizar GnG\_nGn​, porque:

Mn=1−e−Gn\\mathcal M\_n=1-e^{-G\_n}Mn​=1−e−Gn​

é crescente em GnG\_nGn​.

Portanto, o problema é:

max⁡u1,…,un∑k=1n\[−log⁡(1+ρk1−ρkek(uk)2)\]\\max\_{u\_1,\\ldots,u\_n} \\sum\_{k=1}^{n} \\left\[ \-\\log \\left( 1+ \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k} e\_k(u\_k)^2 \\right) \\right\]u1​,…,un​max​k=1∑n​\[−log(1+1−ρk​ρk​​​ek​(uk​)2)\]

sujeito a:

uk≥0,∑k=1nuk≤B.u\_k\\ge0, \\qquad \\sum\_{k=1}^{n}u\_k\\le B.uk​≥0,k=1∑n​uk​≤B.

Equivalentemente:

min⁡u1,…,un∑k=1nlog⁡(1+ρk1−ρkek(uk)2).\\min\_{u\_1,\\ldots,u\_n} \\sum\_{k=1}^{n} \\log \\left( 1+ \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k} e\_k(u\_k)^2 \\right).u1​,…,un​min​k=1∑n​log(1+1−ρk​ρk​​​ek​(uk​)2).

Para estágios internos ativos, a condição de primeira ordem é:

2αkek(uk)ek′(uk)1+αkek(uk)2=−λ,\\frac{ 2\\alpha\_ke\_k(u\_k)e\_k'(u\_k) }{ 1+\\alpha\_ke\_k(u\_k)^2 } \= \-\\lambda,1+αk​ek​(uk​)22αk​ek​(uk​)ek′​(uk​)​=−λ,

onde:

αk=ρk1−ρk\\alpha\_k=\\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k}αk​=1−ρk​ρk​​​

e λ≥0\\lambda\\ge0λ≥0 é o multiplicador do orçamento.

Isso significa:

> O investimento ótimo tende a equalizar o ganho marginal logarítmico entre os estágios financiados.

A otimização completa dependerá da forma de ek(uk)e\_k(u\_k)ek​(uk​), dos custos e de eventuais restrições operacionais.

---

# **26\. Possível contribuição original: princípio de orçamento logarítmico**

O TGH sugere um princípio geral.

## **Princípio OL**

Em qualquer comparação entre duas cascatas escalares positivas:

A=∏k=1nAk,B=∏k=1nBk,A=\\prod\_{k=1}^{n}A\_k, \\qquad B=\\prod\_{k=1}^{n}B\_k,A=k=1∏n​Ak​,B=k=1∏n​Bk​,

a garantia relativa:

1−BA≥c1-\\frac BA\\ge c1−AB​≥c

equivale a:

∑k=1nlog⁡AkBk≥−log⁡(1−c).\\sum\_{k=1}^{n}\\log\\frac{A\_k}{B\_k} \\ge \-\\log(1-c).k=1∑n​logBk​Ak​​≥−log(1−c).

A contribuição específica do projeto não seria essa identidade elementar isolada, mas sua integração com:

1. pontes de saturação distintas;  
2. limiar quartico local;  
3. metas globais dependentes de nnn;  
4. compensação entre estágios;  
5. certificados robustos;  
6. alocação ótima de intervenção;  
7. possível extensão estocástica.

A terminologia “orçamento logarítmico” pode ser útil, mas deve ser tratada inicialmente como uma nomenclatura do projeto, não como reivindicação de conceito inédito.

---

# **27\. Aspecto realmente não trivial do modelo**

A passagem ao logaritmo, por si só, é clássica. O conteúdo específico aparece quando substituímos:

dk=ρk1−ρkpk2,d\_k \= \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2,dk​=1−ρk​ρk​​pk2​, fk=ρk1−ρkek2.f\_k \= \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k}e\_k^2.fk​=1−ρk​ρk​​​ek2​.

A margem local torna-se:

gk=log⁡\[1+ρk1−ρkpk2\]−log⁡\[1+ρk1−ρkek2\].g\_k \= \\log \\left\[ 1+ \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2 \\right\] \- \\log \\left\[ 1+ \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k}e\_k^2 \\right\].gk​=log\[1+1−ρk​ρk​​pk2​\]−log\[1+1−ρk​ρk​​​ek2​\].

Multiplicando numerador e denominador internos por 1−ρk1-\\rho\_k1−ρk​:

gk=log⁡(1−ρk+ρkpk21−ρk+ρkek2).\\boxed{ g\_k \= \\log \\left( \\frac{ 1-\\rho\_k+\\rho\_kp\_k^2 }{ 1-\\rho\_k+\\sqrt{\\rho\_k}e\_k^2 } \\right). }gk​=log(1−ρk​+ρk​​ek2​1−ρk​+ρk​pk2​​).​

A condição global exata é:

∑k=1nlog⁡(1−ρk+ρkpk21−ρk+ρkek2)≥−log⁡(1−c).\\boxed{ \\sum\_{k=1}^{n} \\log \\left( \\frac{ 1-\\rho\_k+\\rho\_kp\_k^2 }{ 1-\\rho\_k+\\sqrt{\\rho\_k}e\_k^2 } \\right) \\ge \-\\log(1-c). }k=1∑n​log(1−ρk​+ρk​​ek2​1−ρk​+ρk​pk2​​)≥−log(1−c).​

Essa é a forma operacional principal do TGH para o modelo PFA×DFA.

---

# **28\. Nova definição: carga efetiva de transição**

Em uma cascata heterogênea, não há necessariamente uma única carga ρ\\rhoρ. Porém, podemos definir uma carga homogênea equivalente.

Suponha p,e,np,e,np,e,n fixos e uma cascata heterogênea com margem:

Gnhet=∑k=1ngk.G\_n^{\\mathrm{het}} \= \\sum\_{k=1}^{n}g\_k.Gnhet​=k=1∑n​gk​.

Defina ρeq\\rho\_{\\mathrm{eq}}ρeq​, quando existir, como a solução de:

n g(ρeq;p,e)=Gnhet,n\\,g(\\rho\_{\\mathrm{eq}};p,e) \= G\_n^{\\mathrm{het}},ng(ρeq​;p,e)=Gnhet​,

isto é:

g(ρeq;p,e)=1nGnhet.g(\\rho\_{\\mathrm{eq}};p,e) \= \\frac1nG\_n^{\\mathrm{het}}.g(ρeq​;p,e)=n1​Gnhet​.

Então:

Mnhet=1−e−Gnhet=1−e−ng(ρeq;p,e).\\mathcal M\_n^{\\mathrm{het}} \= 1-e^{-G\_n^{\\mathrm{het}}} \= 1-e^{-ng(\\rho\_{\\mathrm{eq}};p,e)}.Mnhet​=1−e−Gnhet​=1−e−ng(ρeq​;p,e).

Assim, ρeq\\rho\_{\\mathrm{eq}}ρeq​ resume a cascata heterogênea em uma carga homogênea que produz a mesma mitigação global.

A existência e unicidade dependem da monotonicidade de g(ρ;p,e)g(\\rho;p,e)g(ρ;p,e) no intervalo analisado. Isso deve ser estudado antes de usar ρeq\\rho\_{\\mathrm{eq}}ρeq​ como métrica universal.

---

# **29\. Novos teoremas candidatos**

O programa matemático pode ser organizado em quatro resultados adicionais.

## **Candidato A: teorema de monotonicidade da margem local**

Determinar condições em p,ep,ep,e sob as quais:

g′(ρ)\>0g'(\\rho)\>0g′(ρ)\>0

em todo (0,1)(0,1)(0,1).

Isso garantiria que a carga efetiva equivalente é única.

## **Candidato B: teorema de concentração finita**

Se os gkg\_kgk​ forem independentes e limitados:

gk∈\[ak,bk\],g\_k\\in\[a\_k,b\_k\],gk​∈\[ak​,bk​\],

aplicar uma desigualdade de concentração a:

Gn=∑gkG\_n=\\sum g\_kGn​=∑gk​

para obter:

Pr⁡(Mn\<c)=Pr⁡(Gn\<−log⁡(1−c)).\\Pr(\\mathcal M\_n\<c) \= \\Pr(G\_n\<-\\log(1-c)).Pr(Mn​\<c)=Pr(Gn​\<−log(1−c)).

Isso converteria o TGH em certificado probabilístico.

## **Candidato C: transição crítica**

No regime:

E\[gk\]=0,\\mathbb E\[g\_k\]=0,E\[gk​\]=0,

estudar a escala:

Gn=O(n)G\_n=O(\\sqrt n)Gn​=O(n​)

e a distribuição da mitigação:

Mn=1−e−Gn.\\mathcal M\_n=1-e^{-G\_n}.Mn​=1−e−Gn​.

O regime crítico provavelmente apresentará forte assimetria devido à transformação exponencial.

## **Candidato D: extensão matricial**

Substituir os fatores escalares por operadores positivos:

AD(n)=Dn⋯D1,AF(n)=Fn⋯F1.A\_D^{(n)} \= D\_n\\cdots D\_1, \\qquad A\_F^{(n)} \= F\_n\\cdots F\_1.AD(n)​=Dn​⋯D1​,AF(n)​=Fn​⋯F1​.

A comparação passaria a depender de normas, raios espectrais e expoentes de Lyapunov. Nesse cenário, a comutatividade desaparece e o TGH escalar deixa de valer diretamente. Produtos de matrizes e expoentes de Lyapunov possuem uma teoria extensa, portanto a extensão exigirá uma contribuição verdadeiramente estrutural para ser original. [\[arxiv.org\]](https://arxiv.org/html/2501.11941v1), [\[arxiv.org\]](https://arxiv.org/html/2509.18944v1), [\[w3.impa.br\]](https://w3.impa.br/~viana/out/lle.pdf)

---

# **30\. O que pode ser reivindicado agora**

## **Provado dentro do modelo**

1. fórmula exata da mitigação global;  
2. TGH e todas as suas equivalências;  
3. decomposição em margem logarítmica;  
4. teorema de compensação;  
5. persistência do break-even q4q^4q4 no caso homogêneo;  
6. limiar global fechado ρn,c\\rho\_{n,c}ρn,c​;  
7. condição de atingibilidade: q2n\<1−c;q^{2n}\<1-c;q2n\<1−c;  
8. cap global: 1−q2n;1-q^{2n};1−q2n;  
9. convergência: ρn,c→q4;\\rho\_{n,c}\\to q^4;ρn,c​→q4;  
10. taxa: ρn,c−q4=O(1/n);\\rho\_{n,c}-q^4=O(1/n);ρn,c​−q4=O(1/n);  
11. certificados robustos;  
12. limites extremalmente concentrado e uniforme;  
13. decomposição da amplificação pelo índice HnH\_nHn​.

## **Ainda não provado como modelo aplicado**

1. que as pontes dk,fkd\_k,f\_kdk​,fk​ descrevem um sistema físico ou operacional real;  
2. que os fatores locais são realmente multiplicativos;  
3. que pk,ekp\_k,e\_kpk​,ek​ permanecem constantes ao variar ρk\\rho\_kρk​;  
4. que não há covariâncias ou realimentações ausentes;  
5. que a mesma métrica é preservada em todos os estágios;  
6. que a configuração PFA não altera os parâmetros dos estágios posteriores.

---

# **31\. Avaliação de originalidade**

## **Provavelmente não original isoladamente**

* transformar produto em soma por logaritmo;  
* AM–GM;  
* produtos de razões consecutivas;  
* uso de taxa logarítmica em processos multiplicativos;  
* expoentes de Lyapunov em produtos aleatórios;  
* lower bound de Bernoulli;  
* conceito geral de mitigação bullwhip.

Produtos multiplicativos, médias geométricas e taxas logarítmicas são ferramentas clássicas. Teoremas ergódicos multiplicativos e expoentes de Lyapunov já tratam crescimento assintótico de produtos em contextos muito mais gerais. [\[w3.impa.br\]](https://w3.impa.br/~viana/out/lle.pdf), [\[en.wikipedia.org\]](https://en.wikipedia.org/wiki/Geometric_mean), [\[perso.univ...rennes1.fr\]](https://perso.univ-rennes1.fr/sebastien.gouezel/articles/SubMult.pdf)

Além disso, a literatura bullwhip já considera cadeias multiestágio, várias métricas, políticas de pedido, forecasting, lead times e benchmarks computacionais. [\[arxiv.org\]](https://arxiv.org/pdf/2604.13478), [\[arxiv.org\]](https://arxiv.org/html/2604.13478), [\[researchpo...ulisboa.pt\]](https://researchportal.ulisboa.pt/en/publications/effective-bullwhip-metrics-for-multi-echelon-distribution-systems/)

## **Candidato real a avanço**

O pacote potencialmente novo é:

> Uma teoria fechada de transição entre duas cascatas cujos incrementos compartilham a mesma singularidade de saturação, mas possuem expoentes distintos de carga, produzindo limiar quartico local, cap global 1−q2n1-q^{2n}1−q2n, condição de atingibilidade q2n\<1−cq^{2n}\<1-cq2n\<1−c, limiar global explícito e compensação logarítmica em cascatas heterogêneas.

Essa formulação é específica e testável.

Ainda assim, deve ser apresentada inicialmente como:

> “Resultado candidato a contribuição original, sujeito a auditoria bibliográfica e validação das fórmulas-ponte.”

---

# **32\. Próxima decisão científica**

A melhor sequência de desenvolvimento é:

## **Fase 1: fechar o núcleo matemático**

1. provar condições para monotonicidade global de g(ρ)g(\\rho)g(ρ);  
2. formalizar TGH e TLGH em Lean 4;  
3. verificar simbolicamente a fórmula ρn,c\\rho\_{n,c}ρn,c​;  
4. produzir testes de propriedades, não apenas exemplos;  
5. implementar certificados intervalares;  
6. estudar o regime crítico estocástico.

## **Fase 2: derivar um modelo primitivo**

Construir uma dinâmica que gere:

dk=ρk1−ρkpk2d\_k \= \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2dk​=1−ρk​ρk​​pk2​

e:

fk=ρk1−ρkek2.f\_k \= \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k}e\_k^2.fk​=1−ρk​ρk​​​ek2​.

A derivação deverá esclarecer:

* por que surge 1/(1−ρk)1/(1-\\rho\_k)1/(1−ρk​);  
* por que DFA injeta ρkpk2\\rho\_kp\_k^2ρk​pk2​;  
* por que PFA injeta ρkek2\\sqrt{\\rho\_k}e\_k^2ρk​​ek2​;  
* quais covariâncias são anuladas;  
* quais aproximações são usadas.

## **Fase 3: escolher domínio de aplicação**

O domínio mais adequado será aquele no qual:

* a grandeza propagada é positiva;  
* razões consecutivas são naturais;  
* há vários estágios;  
* erros locais podem ser medidos;  
* saturação possui interpretação clara;  
* intervenções por estágio são possíveis.

## **Fase 4: pesquisa de anterioridade**

Buscar especificamente:

* threshold comparison of multiplicative cascades;  
* heterogeneous cumulative mitigation theorem;  
* saturation exponents in multi-echelon amplification;  
* log-budget control of cascades;  
* global mitigation threshold under stagewise ratios;  
* predictive versus reactive cascade error;  
* multi-stage variance-ratio controller comparison.

---

# **33\. Formulação recomendada do novo resultado principal**

> **Teorema da Transição Global Heterogênea.**  
>  Considere duas cascatas positivas com fatores locais 1+dk1+d\_k1+dk​ e 1+fk1+f\_k1+fk​. A mitigação global do segundo mecanismo em relação ao primeiro é

> Mn=1−∏k=1n1+fk1+dk.\\mathcal M\_n \= 1- \\prod\_{k=1}^{n} \\frac{1+f\_k}{1+d\_k}.Mn​=1−k=1∏n​1+dk​1+fk​​.

> Para qualquer meta c\<1c\<1c\<1,

> Mn≥c\\mathcal M\_n\\ge cMn​≥c

> se, e somente se,

> ∑k=1nlog⁡(1+dk1+fk)≥−log⁡(1−c).\\sum\_{k=1}^{n} \\log\\left(\\frac{1+d\_k}{1+f\_k}\\right) \\ge \-\\log(1-c).k=1∑n​log(1+fk​1+dk​​)≥−log(1−c).

> Assim, vantagens e desvantagens locais compensam-se aditivamente no domínio logarítmico. No modelo homogêneo PFA×DFA, o break-even global permanece q4q^4q4, o cap assintótico após nnn estágios é 1−q2n1-q^{2n}1−q2n, e uma meta ccc é atingível se, e somente se,

> q2n\<1−c.q^{2n}\<1-c.q2n\<1−c.  
---

# **Conclusão**

O TGH está agora provado integralmente, com hipóteses, equivalências, condições de sinal e interpretação operacional.

O avanço mais significativo não é apenas a transformação logarítmica. É a estrutura completa que ela revela:

Mn=1−e−Gn,Gn=∑k=1nlog⁡(1+dk1+fk).\\boxed{ \\mathcal M\_n=1-e^{-G\_n}, \\qquad G\_n= \\sum\_{k=1}^{n} \\log\\left(\\frac{1+d\_k}{1+f\_k}\\right). }Mn​=1−e−Gn​,Gn​=k=1∑n​log(1+fk​1+dk​​).​

Essa estrutura produz:

* compensação exata entre estágios;  
* metas expressas como orçamento logarítmico;  
* limiar global fechado;  
* cap global 1−q2n1-q^{2n}1−q2n;  
* condição de atingibilidade q2n\<1−cq^{2n}\<1-cq2n\<1−c;  
* convergência dos limiares a q4q^4q4;  
* taxa de convergência O(1/n)O(1/n)O(1/n);  
* certificados robustos a incerteza e erro das pontes;  
* um problema natural de alocação ótima de intervenção;  
* uma extensão estocástica governada pela média de log⁡Rk\\log R\_klogRk​.

O ponto científico decisivo permanece o mesmo: **derivar as fórmulas-ponte a partir de uma dinâmica natural**. Se essa derivação for obtida em um domínio relevante, o conjunto TGL \+ TGH \+ TLGH poderá constituir uma contribuição coerente, aplicável e potencialmente original.


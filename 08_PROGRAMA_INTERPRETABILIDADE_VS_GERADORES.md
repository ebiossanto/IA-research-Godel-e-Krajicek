# Programa de Pesquisa: Interpretabilidade vs. Geradores

**Status:** PROGRAMA DE PESQUISA (nenhum resultado e' teorema ate' cada hipotese estar especificada)
**Data:** Setembro 2026
**Origem:** Auditoria rigorosa (22/09/2026) + reconstrucao propria
**Aviso:** Nenhum resultado abaixo e' chamado de teorema sem especificacao formal completa de hipoteses, dominio, codificacao, reducao e medida de tamanho.

---

## 1. Principio de Research

> Nenhum resultado sera' chamado de teorema ate' que cada hipotese, dominio, codificacao, reducao e medida de tamanho esteja formalmente especificada.

---

## 2. Definicoes Formais

### 2.1. Gerador g_T

**Definicao (baseada em Krajicek 2023/2025).** Seja T uma teoria r.e. consistente com axiomas recursivamente enumeraveis. O gerador g_T : {0,1}* -> {0,1} e' definido como segue:

Para entrada x com |x| = n:
1. Achar a primeira formula Phi com |Phi| <= b(n) tal que... (construcao de Krajicek)
2. Para cada w, verificar se existe T-prova de tamanho <= b(n) de ...
3. O bit de saida e' definido pela primeira w sem prova

**Restricoes:**
- b(n) = log n (ou qualquer funcao omega(1) time-constructible, ver Krajicek rodape 3)
- g_T e' computavel em tempo polinomial
- stretch de um bit

**Nota:** A observacao b(n) -> omega(1) JA EXISTE em Krajicek (2023), rodape 3, Secao 3. NAO e' contribuicao original.

### 2.2. Tautologia TG_T^n

**Definicao.** Para cada n, a tautologia TG_T^n afirma que g_T e' computavel por um circuito/maquina C_n especificada.

- |TG_T^n| = 2^n + O(n) (comprimento exponencial na entrada)
- TG_T^n e' tautologia (por construcao do gerador)

### 2.3. Tamanho de Prova s_P

**Definicao.** Seja P um sistema de prova Cook-Reckhow. Para tautologia phi:

s_P(phi) = min{|pi| : pi e' P-prova de phi}

se existe; caso contrario s_P(phi) = infinity.

s_P(TG_T^n) = max{|x|=n} s_P(TG_T^n para a entrada x) -- ou outro maximo conveniente.

---

## 3. A Ordem Operacional ≼_ppr

### 3.1. Definicao

Defina T ≼_ppr S se e' somente se existe uma familia de transformacoes {R_n} tal que:

1. **R_n e' polinomial:** R_n e' computavel em tempo polinomial
2. **Preserva tautologia:** R_n mapeia tautologias em tautologias
3. **Reducao de prova:** existe transformacao pi_S |-> pi_T tal que:
   - Se pi_S e' S-prova de R_n(TG_S^{p(n)}), entao pi_T e' T-prova de TG_T^n
   - |pi_T| <= |pi_S|^{O(1)} (blow-up polinomial)

### 3.2. Interpretacao

T ≼_ppr S significa: **"TG_T^n e' polinomialmente redutivel a TG_S"** no sentido de proof complexity.

Isto e' uma ordem de dificuldade **operacional**, observavel no mundo proposicional.

### 3.3. Propriedades

- ≼_ppr e' uma pre-ordem (reflexiva e transitiva) -- **a ser verificado formalmente**
- Composicao de reducoes preserva ≼_ppr -- **a ser provado como lema**

---

## 4. A Ordem de Interpretabilidade ≼_int

### 4.1. Definicao (classica)

T ≼_int S se e' somente se T e' interpretavel em S (traducao uniforme de teoremas de T para teoremas de S).

### 4.2. Hierarquia de Reflexao

T_0 = T
T_{alpha+1} = T_alpha + RFN(T_alpha)
T_lambda = union_{alpha<lambda} T_alpha

**Nota:** RFN precisa de especificacao formal:
- classe de formulas
- representacao aritmetica de verdade
- reflexao uniforme vs. local
- fragmento utilizado

Ver audit: definicao informal "Pr_T(x) -> True(x)" NAO e' aceitavel literalmente.

---

## 5. A Pergunta Central

### 5.1. Enunciado

$$T \preceq_{int} S \stackrel{?}{\Longrightarrow} g_T \preceq_{ppr} g_S$$

### 5.2. Tres Possibilidades

**Caso A (preservacao):**
T ≼_int S => T ≼_ppr S
Teriamos um teorema de transferencia.

**Caso B (restricao):**
A implicacao vale apenas para T, S em alguma classe C.
Isto produziria uma nova classe de teorias.

**Caso C (quebra):**
Existe contraexemplo: T ≼_int S mas T NÃO ≼_ppr S.
Isto revelaria uma **quebra entre hierarquia proof-theoretic e hierarquia proposicional**.

### 5.3. Por que Caso C seria Interessante

Se precequiv_ppr NAO e' redutivel a precequiv_int, entao:
- A hierarquia de reflexao e a hierarquia de complexidade de geradores sao **estruturalmente diferentes**
- Isto e' uma contribuicao conceitual importante

---

## 6. Medida Operacional Gamma_P

### 6.1. Definicao

$$\Gamma_P(T, n) = \log s_P(TG_T^n)$$

quando s_P e' finito.

### 6.2. Diferenca

$$\Delta_P(T, S; n) = \Gamma_P(S, n) - \Gamma_P(T, n)$$

### 6.3. Hipotese de Pesquisa

A diferenca Delta_P pode carregar informacao sobre a progressao de reflexao T -> T + RFN(T).

**Pergunta testavel:** "A transformacao por reflexao produz uma assinatura mensuravel na complexidade proposicional?"

---

## 7. Programa Experimental

### Fase 1: Niveis Finitos

- T_0 = PA
- T_1 = PA + RFN(PA)
- NAO usar ordinais gerais ainda
- Construir explicitamente g_0, g_1
- Construir TG_0^n, TG_1^n

### Fase 2: Sistema de Prova Fixado

Escolher UM sistema:
- Resolution, OU
- Cutting Planes, OU
- Frege, OU
- Extended Frege

NAO falar em "qualquer P" inicialmente.

### Fase 3: Reducao

Tentar provar:
$$TG_0^n \le_{ppr} TG_1^{p(n)}$$

ou a direcao inversa.

### Fase 4: Lower Bound

SO DEPOIS procurar:
$$s_P(TG_1^n) \ge L(n)$$

Aqui podem entrar tecnicas reais de Krajicek:
- interpolation
- communication complexity
- circuit lower bounds
- proof search
- bounded arithmetic

---

## 8. Resultado Negativo Importante

$$\boxed{\text{"ordem ordinal" NAO pode ser identificada automaticamente com "complexidade de prova"."}}$$

A nova formulação e':

$$\boxed{\text{ordem de reflexao} \stackrel{?}{\longrightarrow} \text{ordem operacional de geradores} \stackrel{?}{\longrightarrow} \text{separacao de prova}}$$

Esta formulação e' mais defensavel e abre espaco real para um resultado novo.

---

## 9. Estado dos Resultados Anteriores (apos auditoria)

| Resultado | Estado |
|-----------|--------|
| Mecanismo g_T de Krajicek | EXISTENTE NA LITERATURA |
| Substituicao log n -> omega(1) | EXISTENTE EM KRAJICEK (rodape 3) |
| Teorema 4: 2^{c|T_alpha|n} | **REJEITADO COMO PROVADO** |
| Teorema 5: cortes estritos | **NAO PROVADO** |
| Teorema 6(a)(b)(c) | **NAO PROVADO** |
| Pergunta slow consistency x g_T | **PERGUNTA DE PESQUISA** |
| Relacao interpretabilidade x dificuldade de gerador | **CANDIDATO A NOVO PROBLEMA FORMAL** |
| Assinatura Gamma_P(T,n) | **NOVA DEFINICAO PROPOSTA; NAO RESULTADO** |

---

## 10. Erros Identificados (para nao repetir)

### Teorema 4
1. "N candidatos => tempo minimo Omega(N)" e' FALSO em geral
2. Segundo Teorema de Goedel NAO produz lower bound quantitativo
3. |T_alpha| e' ambiguo para ordinais
4. Gerador nao especificado no nivel necessario

### Teorema 5
1. T_alpha subseteq T_beta NAO implica C(alpha) proper subset C(beta)
2. Interpretabilidade e' entre teorias; sistemas de prova sao proposicionais -- falta traducao

### Teorema 6
1. T_* = union{r.e., consistente, supseteq PA} NAO e' r.e.
2. "Conter informacao inacessivel" NAO e' prova de hardness
3. Universal hardness NAO cria completude automaticamente

---

## 11. Proximo Passo Concreto

Criar arquivo formal contendo SOMENTE:
1. definicao formal de g_T
2. definicao formal de TG_T^n
3. definicao de precequiv_ppr
4. lema de composicao de reducoes
5. casos T_0=PA e T_1=PA+RFN(PA)
6. tentativa de provar T_0 ≼_int T_1 => g_0 ≼_ppr g_1
7. tentativa de construir contraexemplo
8. SOMENTE DEPOIS, lower bounds

---

## Referencias Centrais (verificadas)

1. Krajicek, J. "A Proof Complexity Conjecture and the Incompleteness Theorem." JSL 90(3), 2025, pp. 1206-1210. arXiv:2303.10637
2. Krajicek, J. "Proof Complexity Generators." Cambridge UP, LMS Lecture Notes 497, 2025.
3. Beklemishev, L.D. "Reflection principles and provability algebras in formal arithmetic." Russian Math. Surveys 60(2), 2005, pp. 197-268.
4. Freund, A. & Pakhomov, F. "Short proofs for slow consistency." Notre Dame J. Formal Logic 61(1), 2020, pp. 31-49.
5. Krajicek, J. "Interpolation theorems, lower bounds for proof systems, and independence results for bounded arithmetic." JSL 62(2), 1997, pp. 457-486.
6. Cook, S. & Reckhow, R. "Propositional proof systems." JCSS, 1979.

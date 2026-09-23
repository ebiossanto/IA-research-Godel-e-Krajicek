# Hierarquia Ordinal e Consistencia Lenta: Notas Exploratorias

**Status:** Notas Exploratorias (nao submetido)
**Data:** Setembro 2026
**Aviso:** Este documento contem conjecturas e argumentos informalos. Nao e um paper comprovado.

---

## Resumo

Exploramos a conexao entre a hierarquia de reflexao ordinal de Beklemishev e o programa de slow consistency. Apresentamos uma pergunta de pesquisa (nao respondida): existe um analogo do fenomeno Freund-Pakhomov dentro do esquema g_T de Krajicek? A tabela anterior de bounds exponenciais foi descartada por falta de derivação.

**Aviso importante:** Este documento e exploratorio. A unica contribuicao potencial e a pergunta de pesquisa na Secao 4.

---

## 1. O Que Ja Existe (referencias criticas)

### 1.1. Krajicek (2023) - O Mecanismo Correto

**Referencia central:** Krajicek, J. (2023). "A proof complexity conjecture and the Incompleteness theorem." arXiv:2303.10637. JSL 90(3), 2025, pp. 1206-1210.

Krajicek constroi g_T que diagonaliza contra T usando log n como limite. O mecanismo e:
- Dado u com |u| = n, acha formula Phi com |Phi| <= log n
- Para cada w, procura T-prova de tamanho <= log n
- A primeira w sem prova define a saida
- Total: 2^{O(log n)} = poly(n) candidatos

### 1.2. Slow Consistency - A Literatura Certa

A intuicao de "hierarquia ordinal" tem um nome certo na literatura:

**Pudlak (2020):** T prova Con(T)↾n com provas de tamanho polinomial. Conjectura que isso quebra ao subir um nivel ingenuo.

**Friedman-Rathjen-Weiermann (2013):** Definem consistencia "lenta" Con*(PA):
- Usam hierarquia de rapido crescimento no ordinal epsilon_0
- Mostram PA ⊊ PA+Con* ⊊ PA+Con (estritamente entre)

**Henk-Pakhomov (2016):** Variantes de "provabilidade lenta":
- Fazem progressao de Turing-Feferman alcancar PA+Con em epsilon_0, omega, ou outros numeros de passos
- Depende da variante

**Freund-Pakhomov (2020):** Resultado surpreendente:
- PA tem provas polinomiais de Con(PA+Con*(PA))↾n
- "Subir devagar" (versao lenta) preserva viabilidade que "subir rapido" destroi

### 1.3. O Que Nossa Tabela Anterior Errava

A tabela anterior dizia:

| Nivel alpha | s_P(TG_alpha) |
|-------------|---------------|
| 0 | 2^{Omega(n)} |
| 1 | 2^{2^{Omega(n)}} |
| 2 | 2^{2^{2^{Omega(n)}}} |

**Erro:** Estes limites nao tinham derivacao. Eram especulativos.

**Correcao:** Removemos a tabela. A literatura correta e slow consistency.

---

## 2. O Que Esta Bem Estabelecido

### 2.1. Hierarquia de Beklemishev (2003)

A hierarquia de reflexao sobre PA e bem-definida:
- T_0 = PA
- T_{alpha+1} = T_alpha + RFN(T_alpha)
- T_lambda = union_{alpha < lambda} T_alpha

**Propriedade:** A progressao e estritamente crescente para alpha < epsilon_0.

**Status:** PROVADO. Resultado classico.

### 2.2. Geradores de Krajicek (2023-2025)

Krajicek desenvolveu geradores que:
- Constroem g_T que diagonaliza contra T
- Provam o 1o Teorema de Goedel
- Conectam incompletude com complexidade de provas

**Status:** PROVADO. Resultados de Krajicek.

### 2.3. Slow Consistency (2013-2020)

O programa de slow consistency:
- Define variantes "lentas" de Con(T)
- Mostra que subir devagar preserva polinomialidade
- Conecta analise ordinal com complexidade de provas

**Status:** PROVADO. Resultados de Friedman, Pakhomov, Freund, etc.

---

## 3. Nossas Conjecturas (nao provadas)

### 3.1. Conexao entre Slow Consistency e Geradores

**Conjectura 1:** A hierarquia de consistencia lenta (Friedman-Rathjen-Weiermann) induz uma hierarquia de geradores g_T com propriedades de complexidade.

**Argumento (sketch):**
1. Cada nivel da hierarquia de consistencia lenta produz uma teoria T_alpha
2. Cada T_alpha produz um gerador g_{T_alpha}
3. A complexidade de g_{T_alpha} escala com o nivel alpha

**Problema:** Nao sabemos se a complexidade realmente escala. Isto depende de conjecturas.

**Status:** CONJECTURA. Plausivel mas nao provada.

### 3.2. Separacao via Slow Consistency

**Conjectura 2:** Slow consistency pode ser usado para separar sistemas de prova de forma mais precisa que fast consistency.

**Argumento (sketch):**
1. Fast consistency (Con(T)) e "rapida" mas pode colapsar
2. Slow consistency (Con*(T)) e "lenta" mas preserva estrutura
3. Portanto slow consistency deve produzir separacoes mais finas

**Problema:** Nao sabemos se isto e verdade. E uma intuicao.

**Status:** CONJECTURA. Intuicao.

---

## 4. A Pergunta Certa (contribuicao potencial)

### 4.1. Enunciado

**Pergunta de pesquisa:** Existe um analogo do fenomeno Freund-Pakhomov dentro do proprio esquema g_T de Krajicek?

**Formalizacao:**
- Seja g_T^(b) o gerador de Krajicek com parametro b(n)
- Seja T_alpha a hierarquia de consistencia lenta
- Pergunta: quantas iteracoes de reflexao limitada (na hierarquia T_alpha) sao necessarias pra recuperar o poder de diagonalizacao da versao "rapida" (inviavel)?

### 4.2. Por que e importante

1. **Conecta dois programas:** Slow consistency (Beklemishev, Friedman) e geradores de Krajicek
2. **Novidade provisória:** não encontramos esta conexão nas fontes consultadas — **não** "genuinamente nova" sem revisão (auditoria + revisão externa §10)
3. **E respondivel:** A pergunta e precisa o bastante pra ser investigada

### 4.3. Por que e uma pergunta (nao teorema)

1. **Nao sei a resposta:** E uma pergunta em aberto
2. **Pode ja ter sido investigada:** O livro de Krajicek (2025) tem generalizacoes que nao revimos
3. **Precisa de especialista:** Logica/teoria da prova e mais delicado que combinatoria

---

## 5. O Que Foi Descartado

### 5.1. Tabela de Bounds Exponenciais

A tabela anterior:

| Nivel alpha | s_P(TG_alpha) |
|-------------|---------------|
| 0 | 2^{Omega(n)} |
| 1 | 2^{2^{Omega(n)}} |
| 2 | 2^{2^{2^{Omega(n)}}} |

**Foi descartada** por falta de derivacao. Sao limites especulativos.

### 5.2. Teorema 4.1 (Escala Ordinal)

O "Teorema 4.1" anterior:

> s_P(TG_alpha^n) >= 2^{c * |T_alpha| * n}

**Foi descartado** por dependencia de argumentos invalidos (enumeracao exponencial).

### 5.3. Cortes Ordinais

A hierarquia de cortes C(alpha) = {P : ist(P) >= [T_alpha]}:

**Foi descartada** por ser especulativa.

---

## 6. Status Atual

| Item | Status |
|------|--------|
| Krajicek (2023) | **CITADO** (referencia central) |
| Slow consistency | **CITADO** (literatura correta) |
| Tabela de bounds | **DESCARTADA** |
| Teorema 4.1 | **DESCARTADO** |
| Pergunta de pesquisa | **FORMULADA** (nao respondida) |

---

## 7. Conclusao Honesta

Este documento e exploratorio. O que fizemos foi:

1. **Citar Krajicek (2023)** como referencia central
2. **Citar slow consistency** como literatura correta
3. **Descartar** tabelas e teoremas sem derivacao
4. **Formular** uma pergunta de pesquisa genuina

**Recomendacao:** Levar a pergunta de pesquisa a um especialista (MathOverflow, tag proof-theory).

---

## Referencias

1. **Krajicek, J. (2023). "A proof complexity conjecture and the Incompleteness theorem." arXiv:2303.10637. JSL 90(3), 2025, pp. 1206-1210.**
2. Krajicek, J. (2025). "Proof Complexity Generators." Cambridge University Press.
3. Beklemishev, L.D. (2003). "Proof-theoretic analysis by iterated reflection."
4. Friedman, S., Rathjen, M., and Weiermann, A. (2013). "Slow consistency." Annals of Pure and Applied Logic.
5. Freund, A. and Pakhomov, F. (2020). "Short Proofs for Slow Consistency." Notre Dame J. Formal Logic 61(1), pp. 31-49. arXiv:1712.03251.
6. Henk, P. and Pakhomov, F. (2016). "Slow and ordinary provability for PA." arXiv:1602.01822.
7. Pudlak, P. (2020). "Reflection principles in propositional proof complexity."

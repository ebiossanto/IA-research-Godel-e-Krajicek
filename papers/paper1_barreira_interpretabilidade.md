# Barateando a Diagonalizacao: Uma Observacao sobre o Mecanismo de Krajicek

**Status:** Nota curta (observacao, nao teorema estabelecido)
**Data:** Setembro 2026
**Aviso:** Trate como observacao pequena, nao teorema estabelecido. Expliquei no fim por que.

---

## Resumo

Notamos que o limite log n na construcao de Krajicek (2023) pode ser substituido por qualquer funcao computavel b(n) -> infinito, sem alterar a correcao do argumento. Especificamente, com b(n) = log log n, o algoritmo de diagonalizacao roda em tempo linear (dominado por ler a entrada), nao apenas polinomial. Isto separa duas coisas que "barreira de interpretabilidade" estava tentando capturar e confundindo: a diagonalizacao crua de Goedel e barata; o que e caro e ligado a problemas em aberto so aparece quando se tenta empurrar o argumento pra forma proposicional.

---

## 1. Contexto: O Paper de Krajicek (2023)

**Referencia central:** Krajicek, J. (2023). "A proof complexity conjecture and the Incompleteness theorem." arXiv:2303.10637. JSL 90(3), 2025, pp. 1206-1210.

Krajicek constroi uma funcao g_T que diagonaliza contra uma teoria T e usa isso pra provar o 1o Teorema de Goedel. O mecanismo e:

**Dado u com |u| = n:**

1. Acha a formula Phi, prefixo de u, com |Phi| <= log n
2. Para cada string w de um alfabeto pequeno (determinado por |Phi|), procura uma T-prova de tamanho <= log n de uma senteca Phi_w especifica
3. A primeira w sem prova encontrada define a saida

**O truque decisivo:** Os dois limites sao log n. O numero de strings candidatas a prova de tamanho <= b e da ordem de 2^b:

- Se b = log n -> 2^{O(log n)} = poly(n) -> dentro de P
- Se b = p(n) com p polinomial -> 2^{Theta(n^e)}, genuinamente exponencial

---

## 2. Nossa Observacao: Barateando a Diagonalizacao

### 2.1. Enunciado

**Proposicao.** Seja b(n) qualquer funcao computavel em tempo, nao decrescente, com b(n) -> infinito (por mais devagar que seja - log log n, log* n, o que for). Troque "log n" por "b(n)" nos dois lugares da construcao de Krajicek, sem mexer em mais nada. Entao:

(a) A funcao resultante g_T^(b) ainda estica a entrada, ainda tem imagem co-infinita, e satisfaz o mesmo teorema de intersecao condicional de Krajicek (logo o mesmo Corolario = 1o Teorema de Goedel), trocando "n >= 2^l" por "n grande o bastante para que b(n) >= l";

(b) A demonstracao e literalmente a dele, palavra por palavra - nada nela usa a taxa de crescimento especifica de log n, so que ela tende a infinito;

(c) O que muda e so o tempo de execucao: o passo 2 faz uma busca dupla (aprox 2^{O(b(n))} valores de w, e para cada um aprox 2^{O(b(n))} candidatas a prova), entao o tempo total e O(n + 2^{O(b(n))}).

### 2.2. Status: JA EXISTE NA LITERATURA

**Descoberta importante:** Krajicek (2023) ja faz essa observacao no **rodape 3 da Secao 3**:

> "Note that the function log log n bounding ℓ can be replaced by any ω(1) time-constructible function, making the time needed to compute function h closer to quasi-polynomial."

Portanto, a observacao NAO e nova. Ja esta publicada no paper de referencia.

### 2.2. Exemplos

| b(n) | Candidatas por busca | Tempo total | Em P? |
|------|---------------------|-------------|-------|
| log n | 2^{O(log n)} = poly(n) | O(n + poly(n)) | Sim (escolha de Krajicek) |
| log log n | 2^{O(log log n)} = (log n)^O(1) | O(n + (log n)^O(1)) | Sim (linear) |
| log* n | 2^{O(log* n)} = constante | O(n + c) | Sim (linear) |

**Tabela de exemplos praticos:**

| n | log n | log log n (2^isso) | log* n (2^isso) |
|---|-------|-------------------|-----------------|
| 2^10 | 10 | 3,3 (~10) | 4 (16) |
| 2^20 | 20 | 4,3 (~20) | 5 (32) |
| 2^40 | 40 | 5,3 (~40) | 5 (32) |
| 2^80 | 80 | 6,3 (~80) | 5 (32) |

### 2.3. O Ponto Conceitual

Isto separa duas coisas que "barreira de interpretabilidade" estava tentando capturar e confundindo:

**Diagonalizacao crua de Goedel e barata** - quase de graça computacionalmente. Com b(n) = log log n, temos uma testemunha computavel do 1o Teorema de Goedel rodando em tempo linear.

**O que e caro e ligado a problemas em aberto** so aparece no Teorema 3.1 de Krajicek (2023), um andar acima, quando se tenta empurrar o argumento pra forma proposicional. A barreira real nao esta em provar incompletude; esta em extrair dela informacao sobre classes de complexidade.

---

## 3. O Que Ja Existia (e que erramos nao citar)

### 3.1. Krajicek (2023) - O Paper Central

Krajicek faz corretamente o que nosso "Teorema 1" tentava fazer (e errava):
- Constroi g_T que diagonaliza contra T
- Usa log n como limite (nao p(n))
- Prova o 1o Teorema de Goedel via geradores

**Nosso erro:** Nao citamos este paper. Sem esta referencia, o trabalho parecia estar tentando reinventar (e errando) algo que ja existe, correto, publicado.

### 3.2. Krajicek (2024-2025) - Livro e Developments

O livro "Proof Complexity Generators" (CUP, 2025, 134 paginas) tem generalizacoes que nao vimos de perto. A observacao pode ja ter sido notada por outros.

---

## 4. Honestidade sobre a Observacao

### 4.1. Por que e observacao (nao teorema)

1. **E pequena:** A mudanca de log n para b(n) e direta
2. **E verificavel:** A demonstracao e "literalmente a dele, palavra por palavra"
3. **Pode ja ter sido notada:** O livro de 2025 tem generalizacoes que nao revimos

### 4.2. O que falta para tornar teorema

1. **Verificar** se a generalizacao ja aparece em Krajicek (2025)
2. **Publicar** como nota curta (se nao existir)
3. **Formalizar** em Lean 4

---

## 5. Conexao com Slow Consistency

### 5.1. A Literatura Certa

A tabela de bounds duplamente-a-quadruplamente exponenciais que tínhamos nao tinha onde se apoiar. Mas a intuicao por tras - uma hierarquia ordinal ligada a quanto uma teoria precisa "subir" pra provar o que a de baixo nao prova, e o preco disso em tamanho de prova - tem um nome certo e uma literatura rica:

**Pudlak:** T prova Con(T)↾n com provas de tamanho polinomial em n. Conjectura que isso quebra ao subir um nivel ingenuo.

**Friedman-Rathjen-Weiermann (2013):** Definem consistencia "lenta" Con*(PA) via hierarquia de rapido crescimento no ordinal epsilon_0. Mostram PA ⊊ PA+Con* ⊊ PA+Con.

**Henk-Pakhomov (2016):** Variantes de "provabilidade lenta" fazem progressao de Turing-Feferman alcancar PA+Con em epsilon_0, omega, ou outros numeros de passos.

**Freund-Pakhomov (2020):** PA tem provas polinomiais de Con(PA+Con*(PA))↾n. Subir devagar preserva viabilidade que subir rapido destroi.

### 5.2. A Pergunta Certa

**Pergunta de pesquisa (genuina, ate onde sei nao respondida):** Existe um analogo do fenomeno Freund-Pakhomov dentro do proprio esquema g_T de Krajicek? Ou seja: em vez de indexar por um b(n) qualquer, indexar por uma hierarquia genuinamente ordinal (a la Friedman-Rathjen-Weiermann) e perguntar quantas iteracoes de reflexao limitada sao necessarias pra recuperar o poder de diagonalizacao da versao "rapida" (inviavel) da construcao.

Isto e uma ponte real entre dois programas que nao vi conectados - mas e uma pergunta em aberto, nao um resultado.

---

## 6. Status

| Item | Status |
|------|--------|
| Krajicek (2023) | **CITADO** (referencia central) |
| Observacao (b(n) generico) | **JA EXISTE** (rodape 3, Secao 3 do paper) |
| Conexao com slow consistency | **PERGUNTA EM ABERTO** |
| Nosso "Teorema 1" anterior | **DESCARTADO** (invalido) |

---

## 7. Conclusao Honesta

Este documento e exploratorio. O que descobrimos foi:

1. **Krajicek (2023)** ja faz corretamente o que nosso Teorema 1 tentava fazer
2. **Nossa observacao** ja existe no rodape 3 da Secao 3 do paper
3. **Nao temos contribuicao nova** neste ponto

**Recomendacao:** Nao publicar esta observacao como contribuicao, pois ja existe. Focar na conexao com slow consistency (pergunta em aberto).

---

## Referencias

1. **Krajicek, J. (2023). "A proof complexity conjecture and the Incompleteness theorem." arXiv:2303.10637. JSL 90(3), 2025, pp. 1206-1210.**
2. Krajicek, J. (2025). "Proof Complexity Generators." Cambridge University Press, 134 pp.
3. Friedman, S., Rathjen, M., and Weiermann, A. (2013). "Slow consistency." Annals of Pure and Applied Logic.
4. Freund, A. and Pakhomov, F. (2020). "Short Proofs for Slow Consistency." Notre Dame J. Formal Logic 61(1), pp. 31-49. arXiv:1712.03251.
5. Henk, P. and Pakhomov, F. (2016). "Slow and ordinary provability for PA." arXiv:1602.01822.
6. Pudlak, P. (2020). "Reflection principles in propositional proof complexity."

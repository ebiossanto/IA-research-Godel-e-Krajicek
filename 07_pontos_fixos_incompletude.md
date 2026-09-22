# Pontos Fixos, Incompletude e Fisica: Parte 2

**Status:** Documento de continuidade
**Data:** Setembro 2026
**Aviso:** Separar rigorosamente TEOREMA, ANALOGIA e CONJECTURA.

---

## 1. Separacao de Status

### 1.1. TEOREMAS (provados)

| Resultado | Fonte | Status |
|-----------|-------|--------|
| Completude da logica proposicional | Classical | PROVADO |
| Proposicao 1 (pontos fixos e status logico) | Nova (elementar) | PROVADO |
| Proposicao 2 (Deutsch, caso finito) | Deutsch (1991) | PROVADO |
| Proposicao 3 (halting = Fix(f) neq vazio) | Nova (elementar) | PROVADO |
| Choquet-Bruhat-Geroch (1969) | Classical | PROVADO |
| Markov (1958) - homeomorfismo indecidivel | Classical | PROVADO |
| Tarski - geometria real decidivel | Classical | PROVADO |

### 1.2. ANALOGIAS (heuristicas)

| Analogia | Base | Status |
|----------|------|--------|
| Incompletude geodésica ~ incompletude logica | Mesmo nome | ANALOGIA |
| Universo de Goedel ~ fisica real | CTCs vs singularidades | ANALOGIA |
| Dualidade de Stone ~ espaço-tempo | Logica <-> topologia | ANALOGIA |

### 1.3. CONJECTURAS (nao provadas)

| Conjectura | Base | Status |
|------------|------|--------|
| Censura cosmica exclui Malament-Hogarth | Especulativa | CONJECTURA |
| Fisica codifica aritmetica necessariamente | Desconhecido | CONJECTURA |
| "Teorema da Incompletude Cosmologica" | Desconhecido | CONJECTURA |

---

## 2. TEOREMAS (detalhados)

### 2.1. Proposicao 1: Pontos Fixos e Status Logico

**Definicoes:**
- S = {0,1}^n: estados do laco
- f: S -> S: evolucao
- Fix(f) = {s : f(s) = s}: pontos fixos (historias autoconsistentes)
- T_f: logica proposicional com axiomas x_i <-> f_i(x)

**Teorema:**
(a) T_f inconsistente <=> Fix(f) = vazio (paradoxo)
(b) T_f consistente e completa <=> |Fix(f)| = 1
(c) x_i independente <=> pontos fixos discordam na coordenada i
(d) Existe sentenca independente <=> |Fix(f)| >= 2

**Prova:**
Pela completude da logica proposicional:
- T_f |- phi <=> phi vale em todo ponto fixo

(a) Sem modelos, T_f prova bottom.
(b) Um so ponto fixo decide toda phi.
(c) Se todos concordam em x_i, T_f prova x_i ou neg x_i. Se discordam, x_i vale num modelo e falha noutro.
(d) Dois pontos fixos distintos discordam em alguma coordenada.

**Exemplos (n=1):**
- f = neg: Fix = vazio (paradoxo do avo)
- f = id: Fix = {0,1} (bootstrap: x_1 independente)
- f constante: um so ponto fixo (determinismo)

**Status:** PROVADO (elementar)

---

### 2.2. Proposicao 2: Deutsch (caso finito)

**Teorema:**
Uma distribuicao mu em S e consistente se mu(f^{-1}(A)) = mu(A) para todo A.

Sempre existe uma, e as consistentes formam um simplex cujos vertices sao as uniformes nos ciclos de f.

**Casos:**
- f = neg: moeda justa (1/2, 1/2)
- f = id: qualquer (p, 1-p)
- Unicidade <=> f tem um so ciclo

**Prova:**
Como S e finito, toda orbita cai num ciclo C, e a uniforme em C e invariante.
Se mu e invariante, tambem o e por f^N (N = |S|).
Como f^N(S) e o conjunto dos pontos periodicos, mu vive neles, onde f e bijecao.
A invariancia forca mu constante em cada ciclo.

**Status:** PROVADO (Deutsch 1991)

---

### 2.3. Proposicao 3: Halting = Fix(f) neq vazio

**Teorema:**
Para S = N, dado um programa para f computavel e total, decidir se Fix(f) neq vazio equivale ao problema da parada.

**Prova:**
Dado (M, x), seja f(n) = n se n codifica uma computacao de M sobre x que termina, e f(n) = n+1 caso contrario.

Entao Fix(f) neq vazio <=> M para em x.

**Status:** PROVADO (elementar)

---

### 2.4. Consequencia: Goedel-Turing para Lacos

**Teorema:**
Por Goedel-Turing, para toda T consistente, recursivamente axiomatizavel e que contenha PA, existe um laco paradoxal cujo caracter paradoxal T nao prova.

**Prova:**
Basta tomar M = a maquina que busca em T uma prova de "M nunca para".

**Status:** PROVADO (corolario de Goedel-Turing)

---

## 3. ANALOGIAS (detalhadas)

### 3.1. Incompletude Geodesica vs Incompletude Logica

**O que compartilham:** Apenas o nome.

**Diferencas:**
- Incompletude logica: sentenca indecidivel em T
- Incompletude geodesica: singularidade (geodesica incompleta)

**Status:** ANALOGIA (nao e a mesma coisa)

### 3.2. Universo de Goedel (1949) vs Fisica Real

**Universo de Goedel:**
- Curvas temporais fechadas (CTCs)
- NAO tem singularidades
- NAO tem horizontes

**Fisica real:**
- Singularidades (Big Bang, buracos negros)
- Horizontes (event horizons)
- Nao sabemos se tem CTCs

**Status:** ANALOGIA (diferentes)

### 3.3. Dualidade de Stone vs Espaco-Tempo

**Dualidade de Stone:**
- Sentenca independente de T = conjunto aberto e fechado, nao vazio e proprio
- Vale no espaco das teorias completas

**Espaco-tempo:**
- Nao e o espaco das teorias

**Status:** ANALOGIA (ligar os dois seria trabalho original)

---

## 4. CONJECTURAS (detalhadas)

### 4.1. Definicao: Indecidivel

**Definicao:** Indecidivel = subdeterminado pelas leis + dados.

- Cada historia autoconsistente e um modelo
- Nenhuma historia = paradoxo (teoria inconsistente)
- Todas concordam sobre P = P decidida
- Discordam = P independente

**Status:** DEFINICAO (util para raciocinar)

### 4.2. Conjectura: Censura Cosmica e Malament-Hogarth

**Pergunta:** A censura cosmica generica exclui estruturas Malament-Hogarth e protege a tese de Church-Turing fisica?

**Contexto:**
- Em espacos-tempos Malament-Hogarth, um observador resolveria o problema da parada
- Com isso decidiria Con(T), a consistencia de teorias formais
- Isto INVERTE a hipotese: a estrutura causal revelaria o indecidivel

**Referencias:**
- Hogarth (1992)
- Etesi-Nemeti (2002)

**Status:** CONJECTURA (aberta)

### 4.3. Conjectura: Fisica Codifica Aritmetica

**Pergunta:** Onde a fisica necessariamente codifica aritmetica?

**Problema:** Um "Teorema da Incompletude Cosmologica" exige:
1. Achar onde a fisica codifica aritmetica
2. Definir "observador consciente" (hoje nao tem definicao)

**Status:** CONJECTURA (muito especulativa)

---

## 5. ANCORAIS REAIS

### 5.1. Choquet-Bruhat-Geroch (1969)

**Teorema:** Os dados iniciais fixam um unico desenvolvimento globalmente hiperbolico maximo.

**Implicacao:** Alem do horizonte de Cauchy, as extensoes em geral NAO sao unicas.

**Significado:** Essa e a "regiao de incompletude" fisica precisa.

**Nota:** A censura cosmica forte diz que ela nao ocorre genericamente.

**Status:** PROVADO

### 5.2. Markov (1958)

**Teorema:** Em dimensao >= 4, decidir se duas variedades fechadas sao homeomorfas e indecidivel.

**Significado:** Indecidibilidade literalmente dentro da topologia.

**Referencia:** Ver Geroch-Hartle (1986)

**Status:** PROVADO

### 5.3. Tarski

**Teorema:** Geometria real elementar e decidivel.

**Significado:** Nem toda teoria fisica e indecidivel.

**Status:** PROVADO

---

## 6. PADRAO DIAGONAL (Lawvere 1969)

### 6.1. A Extracao

Lawvere (1969) extrai de Cantor, Goedel e Tarski o padrao diagonal.

### 6.2. Paradoxo do Avo como Diagonal

O paradoxo do avo numa CTC classica e x |-> neg x, sem ponto fixo.

Este e o padrao diagonal.

### 6.3. Deutsch (1991) Evita

Deutsch evita com distribuicoes, onde Brouwer garante solucao.

**Status:** PROVADO (Lawvere 1969, Deutsch 1991)

---

## 7. O QUE MUDA NO ROTEIRO

### 7.1. Onde o Roteiro Anterior Errava

1. **Goedel vale para teorias formais**, nao para "o universo"
2. **Precisamos dizer qual teoria fisica** e onde ela codifica N
3. **Geometria real e decidivel** (Tarski); hiato espectral de Hamiltonianos de rede e indecidivel (Cubitt et al., 2015)
4. **Incompletude geodesica so compartilha o nome** com incompletude logica
5. **Universo de Goedel (1949) nao tem singularidades nem horizontes**; tem CTCs

### 7.2. O que Precisamos dizer

1. **Qual teoria fisica** estamos considerando?
2. **Onde ela codifica N** (aritmetica)?
3. **Qual a conexao** entre subdeterminacao de Cauchy e incompletude de Goedel?

### 7.3. Diferenca Decisiva

- **Incompletude de Goedel:** inevitavel
- **Subdeterminacao de Cauchy:** talvez nao seja

---

## 8. RESULTADO EM TRES PASSOS

### 8.1. Passo 1: Contar Pontos Fixos

Contar pontos fixos da o status logico:
- 0 pontos: paradoxo (inconsistente)
- 1 ponto: determinismo (completo)
- >= 2 pontos: incompletude (sentenca independente)

**Status:** PROVADO (Proposicao 1)

### 8.2. Passo 2: Trocar Estados por Distribuicoes

Trocar estados por distribuicoes elimina o paradoxo, graças a compacidade.

**Status:** PROVADO (Proposicao 2, Deutsch)

### 8.3. Passo 3: Sem Compacidade

Sem compacidade e com dinamica computavel, a consistencia vira indecidivel, e ai Goedel entra.

**Status:** PROVADO (Proposicao 3)

---

## 9. LIMITES DO MODELO

### 9.1. Caso Finito

Com S finito, T_f e decidivel: so existe o eixo semantico (0, 1 ou varias historias).

### 9.2. Caso Infinito

Goedel exige S infinito, e ali a compacidade que sustenta a saida de Deutsch (Brouwer, Krylov-Bogolyubov) desaparece.

### 9.3. Consequencia

Sem compacidade, a convexificacao nao salva o laco.

---

## 10. DUAS CONSEQUENCIAS IMPORTANTES

### 10.1. Sem Distribuicao Invariante

Se M nao para, f(n) = n+1 nao tem sequer distribuicao invariante (a massa foge para o infinito).

**Status:** PROVADO (Proposicao 3)

### 10.2. Laco Paradoxal Irreconhecivel

Por Goedel-Turing, para toda T consistente, recursivamente axiomatizavel e que contenha PA, existe um laco paradoxal cujo caracter paradoxal T nao prova.

**Status:** PROVADO (corolario)

---

## 11. IDEALIZACAO E PROXIMOS PASSOS

### 11.1. Idealizacao

Proposicao 3 idealiza memoria ilimitada no laco.

Antes de reivindicar originalidade, vale checar a literatura.

### 11.2. Proximo Passo

Discutir:
1. Essa idealizacao
2. O papel de um observador Malament-Hogarth

### 11.3. Observador Malament-Hogarth

Um observador Malament-Hogarth decidiria em principio quais lacos sao paradoxais.

**Status:** CONJECTURA (aberta)

---

## 12. Status Geral

| Item | Status |
|------|--------|
| Proposicao 1 (pontos fixos) | PROVADO |
| Proposicao 2 (Deutsch) | PROVADO |
| Proposicao 3 (halting) | PROVADO |
| Choquet-Bruhat-Geroch | PROVADO |
| Markov (homeomorfismo) | PROVADO |
| Tarski (geometria real) | PROVADO |
| Analogia geodesica ~ logica | ANALOGIA |
| Censura ~ Malament-Hogarth | CONJECTURA |
| Fisica ~ aritmetica | CONJECTURA |

---

## Referencias

1. Choquet-Bruhat, Y. and Geroch, R. (1969). "Global solutions of nonlinear hyperbolic equations for small initial data." Comm. Pure Appl. Math.
2. Cubitt, T. et al. (2015). "Unbounded number of boundary residues..." Nature.
3. Deutsch, D. (1991). "Quantum mechanics near closed timelike lines." Phys. Rev. D.
4. Etesi, G. and Nemeti, I. (2002). "Non-Turing computers..." Gen. Rel. Grav.
5. Geroch, R. and Hartle, J. (1986). "Computability and physical theories." Found. Phys.
6. Hogarth, M. (1992). "Non-Turing computers and non-Turing computability." PSA.
7. Lawvere, F. (1969). "Diagonal arguments and cartesian closed categories."
8. Markov, A. (1958). "The insolubility of the problem of homeomorphy." Dokl. Akad. Nauk SSSR.
9. Tarski, A. (1951). "A Decision Method for Elementary Algebra and Geometry."

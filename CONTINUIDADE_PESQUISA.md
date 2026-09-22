# Documento de Continuidade: Pesquisa Godel-Krajicek

**Data:** Setembro 2026
**Status:** Para continuidade pelo autor
**Aviso:** Este documento resume TUDO o que foi feito, descoberto, e o que resta fazer.

---

## 1. Resumo da Jornada

### 1.1. Objetivo Inicial

Conectar:
- Incompletude de Goedel (1931)
- Complexidade de provas de Krajicek (2004-2025)
- Hierarquia ordinal de Beklemishev (2003-2024)

### 1.2. O Que Foi Descoberto

1. **Krajicek (2023)** ja faz corretamente o que tentavamos fazer
2. **Nossa observacao** ja existe no rodape 3 do paper dele
3. **Tabelas de bounds** eram especulativas (sem derivacao)
4. **Provas** continham erros (enumeracao exponencial)

### 1.3. O Que Sobrou

A **unica contribuicao potencial** e uma pergunta de pesquisa:

> Existe um analogo do fenomeno Freund-Pakhomov dentro do esquema g_T de Krajicek?

---

## 2. Referencias Criticas (obrigatorias)

### 2.1. Paper Central

**Krajicek, J. (2023). "A proof complexity conjecture and the Incompleteness theorem."**
- arXiv:2303.10637
- JSL 90(3), 2025, pp. 1206-1210
- **Leer COMPLETO** - e curto (6 paginas)

**O que faz:**
- Constroi g_T que diagonaliza contra T
- Prova 1o Teorema de Goedel via geradores
- Mostra que log n pode ser trocado por ω(1) (rodape 3)

### 2.2. Livro de Referencia

**Krajicek, J. (2025). "Proof Complexity Generators."**
- Cambridge University Press, 134 paginas
- LMS Lecture Note Series, No. 497
- **Leer capítulos 3 e 9**

### 2.3. Slow Consistency (linha correta para "hierarquia ordinal")

| Paper | O que faz | Status |
|-------|-----------|--------|
| Friedman-Rathjen-Weiermann (2013) | Definem Con*(PA) | PROVADO |
| Henk-Pakhomov (2016) | Progressao lenta | PROVADO |
| Freund-Pakhomov (2020) | PA tem provas polinomiais de Con(PA+Con(PA))↾n* | PROVADO |
| Pakhomov-Walsh | Reflection ranks e analise ordinal | PROVADO |

### 2.4. Outras Referencias

- Beklemishev (2003): Hierarquia de reflexao
- Cook-Reckhow (1979): NP=coNP iff existe sistema polinomico
- Pudlak (2020): Reflexao proposicional

---

## 3. O Que Ja Existe (nao inventamos nada novo)

### 3.1. Mecanismo de Krajicek (2023)

**Dado u com |u| = n:**

1. Acha formula Φ com |Φ| ≤ log n
2. Para cada w, procura T-prova de tamanho ≤ log n
3. A primeira w sem prova define a saida

**Por que funciona:**
- 2^{O(log n)} = poly(n) candidatos
- Cada candidato verificado em tempo polinomial
- Total: tempo polinomial

**Generalizacao (ja em Krajicek):**
- log n pode ser trocado por qualquer ω(1)
- Com log log n: tempo linear

### 3.2. Conexao com Slow Consistency

A "hierarquia ordinal" que tentavamos criar ja existe como **slow consistency**:
- Friedman-Rathjen-Weiermann (2013)
- Henk-Pakhomov (2016)
- Freund-Pakhomov (2020)

---

## 4. O Que NAO Funcionou (erros que cometemos)

### 4.1. Teorema 1 (invalido)

**Dizia:** "Enumerar todas as provas de ate p(n) e polinomial"

**Erro:** 2^{p(n)} e exponencial, nao polinomial

**Correcao:** Krajicek usa log n (nao p(n))

### 4.2. Tabela de Bounds (especulativa)

**Dizia:**
| Nivel | s_P(TG_alpha) |
|-------|---------------|
| 0 | 2^{Omega(n)} |
| 1 | 2^{2^{Omega(n)}} |
| 2 | 2^{2^{2^{Omega(n)}}} |

**Problema:** Sem derivacao. Eram conjecturas.

**Correcao:** Removida.

### 4.3. Cortes Ordinais (especulativos)

**Dizia:** C(alpha) = {P : ist(P) >= [T_alpha]}

**Problema:** Nao sabemos se a hierarquia de interpretabilidade e "suficiente"

**Correcao:** Removido.

---

## 5. O Que Pode Ser Explorado (perguntas em aberto)

### 5.1. Pergunta Principal

> Existe um analogo do fenomeno Freund-Pakhomov dentro do esquema g_T de Krajicek?

**Formalizacao:**
- Seja g_T^(b) o gerador de Krajicek com parametro b(n)
- Seja T_alpha a hierarquia de consistencia lenta
- Pergunta: quantas iteracoes de reflexao limitada sao necessarias pra recuperar o poder de diagonalizacao da versao "rapida"?

**Status atual:** Formalizada como **Conjectura FP-K** em `CONJECTURA_FP_K.md`.

**Por que e importante:**
1. Conecta dois programas (slow consistency e geradores)
2. E genuinamente nova (nao vi na literatura)
3. E respondivel (pergunta precisa)

**Por que e uma pergunta (nao teorema):**
1. Nao sei a resposta
2. Pode ja ter sido investigada
3. Precisa de especialista

### 5.2. Perguntas Secundarias

1. **Tightness:** O limite de Krajicek e otimo?
2. **Formalizacao:** Os resultados podem ser mecanizados em Lean 4?
3. **Aplicacoes:** Slow consistency pode separar sistemas de prova?

---

## 6. Proximos Passos Concretos

### 6.1. Imediatos (1-2 semanas)

1. **Ler Krajicek (2023) COMPLETO** (6 paginas)
2. **Ler Krajicek (2025) capitulos 3 e 9**
3. **Ler Freund-Pakhomov (2020)** sobre slow consistency

### 6.2. Curto prazo (1-3 meses)

1. **Formular** a pergunta de pesquisa formalmente
2. **Verificar** se ja existe na literatura
3. **Postar** no MathOverflow (tag proof-theory)

### 6.3. Medio prazo (3-6 meses)

1. **Investigar** a pergunta de pesquisa
2. **Colaborar** com especialista (se possivel)
3. **Publicar** como nota curta (se houver resultado)

---

## 7. Contatos

### 7.1. Jan Krajicek

- Email: jan.krajicek@protonmail.com
- Affiliation: Charles University, Prague
- Status: Contato publico (via paper)

### 7.2. MathOverflow

- Tag: proof-theory
- Formato: Pergunta formal com contexto
- Incluir: Referencias, o que ja existe, o que se pergunta

---

## 8. Arquivos no Repositorio

### 8.1. Papers (em `papers/`)

| Arquivo | Status |
|---------|--------|
| paper1_barreira_interpretabilidade.md | Atualizado com Krajicek (2023) |
| paper2_hierarquia_ordinal.md | Atualizado com slow consistency |

### 8.2. Documentos de Apoio (em `support/`)

| Arquivo | Conteudo |
|---------|----------|
| 00_avaliacao_novelidade.md | O que ja existe vs. o que e novo |
| 01_framework_estendido.md | Framework anterior (descartado) |
| 02_teoremas_principais.md | Teoremas anteriores (descartados) |
| 03_meta_complexidade_aplicacoes.md | Aplicacoes (especulativas) |
| 04_questoes_abertas_referencias.md | Questoes abertas e referencias |
| 05_verificacao_lean4.md | Verificacao e plano Lean 4 |

### 8.3. Arquivos Raiz

| Arquivo | Status |
|---------|--------|
| README.md | Atualizado |
| INDICE.md | Atualizado (v4.0) |
| CONTINUIDADE_PESQUISA.md | Este arquivo |
| CONJECTURA_FP_K.md | Conjectura FP-K formalizada |
| 07_pontos_fixos_incompletude.md | Parte 2: pontos fixos, física, analogias |

---

## 9. Citacoes Obrigatorias

Se este trabalho for publicado, CITAR:

1. **Krajicek (2023)** - paper central
2. **Krajicek (2025)** - livro de referencia
3. **Friedman-Rathjen-Weiermann (2013)** - slow consistency
4. **Freund-Pakhomov (2020)** - resultado sobre PA
5. **Beklemishev (2003)** - hierarquia de reflexao

---

## 10. Nota Final

Este projeto comecou tentando criar algo novo, mas descobriu que:

1. **Krajicek (2023)** ja faz corretamente o que tentavamos fazer
2. **Nossa observacao** ja existe no paper dele (rodape 3)
3. **A unica contribuicao potencial** e a Conjectura FP-K

**Honestidade:** Nao inventamos nada novo no eixo Krajicek. O que fizemos foi:
- Entender o trabalho de Krajicek
- Conectar com slow consistency
- Formalizar a Conjectura FP-K (`CONJECTURA_FP_K.md`)
- Separar rigorosamente teorema/analogueia/conjectura na Parte 2 (`07_pontos_fixos_incompletude.md`)

**Proximo passo real:** Levar a Conjectura FP-K a um especialista (MathOverflow ou Krajicek).

---

## 11. Parte 2: Pontos Fixos e Fisica (adicionado)

Nova linha de trabalho separada da Parte 1:

| Status | Itens |
|--------|-------|
| **TEOREMAS** | Prop. 1-3, Choquet-Bruhat-Geroch, Markov, Tarski, corolario Goedel-Turing |
| **ANALOGIAS** | Incompletude geodesica ~ logica; universo de Goedel ~ fisica real; Stone ~ espaco-tempo |
| **CONJECTURAS** | Censura ~ Malament-Hogarth; fisica ~ aritmetica; Teorema da Incompletude Cosmologica |

**Documento:** `07_pontos_fixos_incompletude.md`

**Proximo passo da Parte 2:** Checar a idealizacao de memoria ilimitada na Proposicao 3 na literatura; discutir papel do observador Malament-Hogarth.

---

**Autor do documento:** Euzebio Santos
**Data:** Setembro 2026
**Contato:** ebiossanto (GitHub)

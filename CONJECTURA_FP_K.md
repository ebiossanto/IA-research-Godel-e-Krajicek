# Conjectura FP-K: Fenomeno Freund-Pakhomov para Geradores de Krajicek

**Status:** PERGUNTA DE PESQUISA — originalidade ainda NAO estabelecida (apos auditoria 22/09/2026)
**Data:** Setembro 2026
**Aviso:** Este documento formaliza uma pergunta de pesquisa. NAO e um teorema, NAO e uma conjectura comprovadamente nova. Rebaixado de "conjectura" para "pergunta de pesquisa" apos auditoria rigorosa.

> **Correcao pos-auditoria:** A afirmacao de que a pergunta e' "genuinamente nova" NAO esta certificada. A literatura de geradores, reflexao e slow consistency e' suficientemente proxima para exigir busca bibliografica especializada antes de qualquer prioridade de descoberta.

---

## 1. A Pergunta

> Existe um analogo do fenomeno Freund-Pakhomov dentro do esquema g_T de Krajicek?

---

## 2. Por que a Pergunta e Natural

### 2.1. O Fenomeno Freund-Pakhomov

De forma simplificada: versoes "lentas" da consistencia ou da reflexao podem eventualmente recuperar a forca da consistencia ordinaria apos uma quantidade suficiente de iteracoes transfinita ou ordinalmente controlada.

### 2.2. O Esquema de Krajicek

Os geradores g_T dependem da capacidade do sistema T de formalizar argumentos de diagonalizacao e extrair dureza proposicional.

### 2.3. A Correspondencia

```
forca de reflexao <-> qualidade da diagonalizacao <-> forca do gerador g_T
```

### 2.4. As Duas Correntes Conectam

- **Consistencia e reflexao** (Freund-Pakhomov)
- **Diagonalizacao e incompletude** (Krajicek)

Ambas compartilham raizes em Goedel.

---

## 3. A Conjectura FP-K

### 3.1. Enunciado

Seja T_alpha a hierarquia de consistencia lenta de Freund-Pakhomov e g_{T_alpha}^{(b)} o gerador correspondente. Entao existe um ordinal critico alpha_* tal que:

- Para alpha < alpha_*: g_{T_alpha}^{(b)} NAO recupera totalmente o comportamento diagonalizador de g_T
- Para alpha >= alpha_*: g_{T_alpha}^{(b)} recupera o comportamento diagonalizador

Ou seja:

```
alpha_* = min{alpha : g_{T_alpha}^{(b)} equiv g_T em forca de diagonalizacao}
```

### 3.2. Por que Parece Verdadeiro

1. **Diagonalizacao de Goedel exige** que o sistema consiga verificar propriedades sintaticas dos proprios codigos
2. **Reflexao limitada adiciona** precisamente essa capacidade
3. **Na pratica:**
   - Pouca reflexao -> diagonalizacao incompleta
   - Mais reflexao -> mais autoverificacao
   - Reflexao suficiente -> recuperacao da diagonalizacao completa

### 3.3. Filosofia Matematica

O mecanismo conceitual ja aparece em resultados de:
- Beklemishev
- Schmerl
- Freund
- Pakhomov

O que mudaria seria o objeto observado:
- **Antes:** consistencia
- **Agora:** geradores de Krajicek

---

## 4. Teorema Intermediario Candidato

### 4.1. Objetivo

Antes da pergunta principal, tentar provar algo mais fraco.

### 4.2. Enunciado

Existe uma funcao monotonica D(alpha) medindo a profundidade formal de diagonalizacao disponivel em T_alpha, tal que:

```
D(alpha+1) > D(alpha)
```

E mostrar que:

```
sup_{alpha < alpha_*} D(alpha) < D(T)
```

```
D(alpha_*) = D(T)
```

### 4.3. Por que e Mais Atacavel

- Nao requer resolver a pergunta completa
- Fornece ferramentas para atacar o problema
- Pode ser formalizavel em Lean 4

---

## 5. Sobre a Quantidade de Reflexao Necessaria

### 5.1. Previsao Heuristica

O parametro critico NAO e um numero finito de iteracoes.

Na literatura de consistencia lenta, quase sempre acontece:
- Cada passo adiciona pouco
- O salto real surge proximo de algum ordinal canonico

### 5.2. Ordinais Candidatos

```
omega, epsilon_0, Gamma_0
```

Ou outro ordinal de prova associado a T.

### 5.3. Nao Esperar

```
5 iteracoes
```

### 5.4. Esperar

```
omega ou epsilon_0
```

---

## 6. A Questao de Tightness

### 6.1. Pergunta

O limite de Krajicek e otimo?

### 6.2. Duas Possibilidades

**Cenario A:** alpha_* e exatamente o limite previsto pelos argumentos conhecidos
- A teoria e tight

**Cenario B:** A recuperacao ocorre mais cedo
- Os argumentos atuais deixam espaco e nao sao otimos

### 6.3. Dificuldade

Esta pergunta e provavelmente tao dificil quanto a principal.

---

## 7. Mecanizacao em Lean 4

### 7.1. Ingredientes Disponiveis

- Aritmetica de primeira ordem (ja formalizada)
- Codificacao de provas (ja formalizada)
- Sintaxe de Goedel (ja formalizada)
- Hierarquias ordinais (parcialmente formalizada)

### 7.2. Obstaculo

Nao e conceitual. E engenharia formal.

### 7.3. Classificacao

**Dificil, mas plausivelmente realizavel.**

---

## 8. Aplicacoes a Sistemas de Prova

### 8.1. Novo Invariante

Se houver um ordinal ordinal medindo recuperacao de diagonalizacao, ele fornece um novo invariante:

```
rho(T) = ordinal minimo que recupera g_T
```

### 8.2. Comparacao de Sistemas

Dois sistemas podem ser distinguidos por:

```
rho(T_1) != rho(T_2)
```

### 8.3. Diferenca do que Existe

Hoje comparamos sistemas por:
- Forca de consistencia
- Ordinais de prova
- Classes de funcoes

O novo invariante seria baseado em:
- "Velocidade de recuperacao da diagonalizacao"

### 8.4. Novidade Conceitual

Se existir, seria conceitualmente novo -- MAS A NOVELIDADE NAO FOI CERTIFICADA (ver Secao 9).

---

## 9. Veredicto Honesto (apos auditoria 22/09/2026)

### 9.1. Sobre a Pergunta

A pergunta e' boa e bem motivada. Nao reconheco nenhum resultado classico que faca explicitamente a ponte:

```
Freund-Pakhomov <-> g_T de Krajicek
```

### 9.2. Sobre a Novidade (CORRIGIDO)

**STATUS REBAIXADO:** A originalidade NAO esta estabelecida.

A literatura de geradores, reflexao e slow consistency e' suficientemente proxima para exigir busca bibliografica especializada antes de qualquer prioridade de descoberta.

$$\boxed{\text{PERGUNTA DE PESQUISA - originalidade ainda nao estabelecida}}$$

### 9.3. A Aposta Matematica (heuristica, nao teorema)

E' plausivel que exista um analogo do fenomeno Freund-Pakhomov para os geradores g_T, manifestando-se como um ordinal critico de reflexao. Mas isto e' uma aposta, nao um resultado.

### 9.4. Status

Nao e' teorema. Nao e' conjectura comprovadamente nova. E' uma pergunta de pesquisa razoavel baseada na arquitetura comum dos dois programas.

---

## 10. Proximos Passos (revisados)

### 10.1. Imediatos

1. **BUSCA BIBLIOGRAFICA ESPECIALIZADA** antes de qualquer reivindicacao de prioridade
2. Verificar se a interacao Freund-Pakhomov x g_T ja foi estudada
3. Postar no MathOverflow (tag proof-theory) -- como PERGUNTA, nao como conjectura nova

### 10.2. Alternativa (recomendada pela auditoria)

Em vez de insistir na FP-K como "nova", seguir o programa de:
`08_PROGRAMA_INTERPRETABILIDADE_VS_GERADORES.md`

que formula um problema formal mais preciso:

$$T \preceq_{int} S \stackrel{?}{\Longrightarrow} g_T \preceq_{ppr} g_S$$

### 10.3. NAO fazer ainda

- Nao adicionar mais conjecturas ao repositorio
- Nao reivindicar prioridade sem busca bibliografica
- Nao tratar teoremas 4-6 como provados

---

## Referencias (corrigidas pos-auditoria)

1. Krajicek, J. (2025). "A Proof Complexity Conjecture and the Incompleteness Theorem." JSL 90(3), 2025, pp. 1206-1210. arXiv:2303.10637. https://doi.org/10.1017/jsl.2023.69
2. Freund, A. and Pakhomov, F. (2020). "Short proofs for slow consistency." Notre Dame Journal of Formal Logic 61(1), pp. 31-49. https://doi.org/10.1215/00294527-2019-0031
3. Friedman, S., Rathjen, M., and Weiermann, A. (2013). "Slow complexity." Archive for Mathematical Logic.
4. Beklemishev, L.D. (2005). "Reflection principles and provability algebras in formal arithmetic." Russian Mathematical Surveys 60(2), pp. 197-268.
5. Krajicek, J. (2025). "Proof Complexity Generators." Cambridge University Press, LMS Lecture Note Series 497.

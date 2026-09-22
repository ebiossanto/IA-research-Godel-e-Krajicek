# Hierarquia Ordinal de Geradores Godelianos: Notas Exploratorias

**Status:** Notas Exploratorias (nao submetido)
**Data:** Setembro 2026
**Aviso:** Este documento contem conjecturas e argumentos informalos. Nao e um paper comprovado.

---

## Resumo

Exploramos a conexao entre a hierarquia de reflexao ordinal de Beklemishev e os geradores de complexidade de provas de Krajicek. Apresentamos conjecturas (nao provadas) sobre como a hierarquia ordinal pode indexar geradores de tautologias duras. Muitos resultados dependem da hipotese P != NP e da conjectura de Krajicek.

**Aviso importante:** Este documento e exploratorio. Os "teoremas" sao na verdade conjecturas ou sketches de prova que precisam de rigorizacao.

---

## 1. O Que Esta Bem Estabelecido (nao e nosso)

### 1.1. Hierarquia de Beklemishev (2003)

A hierarquia de reflexao sobre PA e bem-definida:
- T_0 = PA
- T_{alpha+1} = T_alpha + RFN(T_alpha)
- T_lambda = union_{alpha < lambda} T_alpha

**Propriedade:** A progressao e estritamente crescente para alpha < epsilon_0.

**Status:** PROVADO. Resultado classico.

### 1.2. Geradores de Krajicek (2004-2025)

Geradores de complexidade de provas produzem familias de tautologias:
- C_n: {0,1}^n -> {0,1}^{n+1} (computavel em tempo polinomial)
- TG_g^n = AND_{x in {0,1}^n} [C_n(x) = g(x)]

**Propriedade:** Se g e pseudo-aleatorio, TG_g^n e hard para sistemas que nao resolvem g.

**Status:** PROVADO. Resultado classico.

### 1.3. Gerador Godeliano (Krajicek 2023)

** referencia fundamental:** Krajicek, J. (2023). "A proof complexity conjecture and the Incompleteness theorem." arXiv:2303.10637. JSL 90(3), 2025, pp. 1206-1210.

Seja T uma teoria r.e. consistente. Krajicek (2023) prova que existe um gerador g_T computavel em tempo polinomial tal que:
- g_T e hard para qualquer sistema P que interpreta T
- A tautologia TG_{g_T}^n requer provas super-polinomiais em P

**Mecanismo (log n):** O truque decisivo e usar log n como limite de tamanho de prova:
1. Dado u com |u| = n, acha formula Phi com |Phi| <= log n
2. Para cada string w, procura T-prova de tamanho <= log n
3. A primeira w sem prova define a saida
4. Total: 2^{O(log n)} = poly(n) candidatos (POLINOMIAL)

**Status:** PROVADO. Resultado de Krajicek.

---

## 2. Nossas Conjecturas (nao provadas)

### 2.1. Geradores Indexados por Ordinais

**Conjectura 1:** Para cada nivel alpha da hierarquia de Beklemishev, o gerador g_{T_alpha} produz tautologias TG_{alpha}^n cuja complexidade escala com |T_alpha|.

**Argumento (sketch):**
1. T_alpha e mais forte que T_beta para alpha > beta
2. Portanto g_{T_alpha} codifica mais informacao que g_{T_beta}
3. Logo TG_{alpha}^n deve ser mais dificil que TG_{beta}^n

**Problema:** Nao sabemos se "mais informacao" implica "mais dificil". Isto depende de P != NP.

**Status:** CONJECTURA. Argumento informal.

### 2.2. Escala Ordinal da Dureza

**Conjectura 2:** s_P(TG_alpha^n) >= 2^{c * |T_alpha| * n} para algum c > 0.

**Argumento (sketch):**
1. Se s_P(TG_alpha^n) <= p(n), podemos decidir g_alpha(x) em tempo polinomial
2. Mas decidir g_alpha(x) implica decidir provabilidade em T_alpha
3. Isto contradiz G2

**Problema:** O passo 2 nao e direto. Decidir g_alpha(x) nao implica decidir provabilidade em T_alpha. A conexao precisa de mais trabalho.

**Status:** CONJECTURA. Argumento incompleto.

### 2.3. Cortes Ordinais

**Conjectura 3:** A hierarquia de Beklemishev induz uma hierarquia estrita de sistemas de prova.

**Argumento (sketch):**
1. C(alpha) = {P : ist(P) >= [T_alpha]}
2. Se alpha < beta, C(alpha) subset C(beta)
3. Se alpha != beta, C(alpha) != C(beta)

**Problema:** Nao sabemos se a hierarquia de interpretabilidade e "suficiente" para distinguir sistemas. Pode haver colapsos.

**Status:** CONJECTURA. Plausivel mas nao provada.

---

## 3. O Que NAO E Provable (erros no paper anterior)

### 3.1. Erro na Prova do Teorema 4.1

O paper anterior dizia:

> "Decidir g_alpha(x) em tempo polinomial implica decidir provabilidade em T_alpha, contradizendo G2."

**Erro:** G2 diz que T nao prova Con(T). Nao diz que um algoritmo nao pode decidir Con(T). A conexao entre incompletude e decidibilidade e sutil.

**Correcao:** O argumento correto seria:
- Se P = coNP, entao TAUT ∈ P
- Se TAUT ∈ P, podemos decidir tautologias em tempo polinomial
- Mas isto nao contradiz G2 diretamente

### 3.2. Tabela de s_P(TG_alpha) e Especulativa

O paper anterior dizia:

| Nivel alpha | s_P(TG_alpha) |
|-------------|---------------|
| 0 | 2^{Omega(n)} |
| 1 | 2^{2^{Omega(n)}} |
| 2 | 2^{2^{2^{Omega(n)}}} |

**Problema:** Estes limites sao ESPECULATIVOS. Nao existem provas na literatura para estes limites especificos.

**Correcao:** A tabela deve ser marcada como "conjectural" ou removida.

### 3.3. Corolarios Prematuros

O paper anterior dizia:

> "Se P interpreta PA mas nao PA + RFN(PA), entao s_P(TG_0^n) e polinomial mas s_P(TG_1^n) e super-polinomial."

**Problema:** Isto depende de P != NP e de conjecturas nao provadas.

**Correcao:** Marcar como "condicional a P != NP".

---

## 4. Resultados Validos (com ressalvas)

### 4.1. Monotonicidade e Solida

**Lema 4.1 (Monotonicidade):** Se alpha < beta e P interpreta T_beta, entao P interpreta T_alpha.

**Prova:** T_alpha <= T_beta (por definicao da hierarquia). Portanto se P interpreta T_beta, P interpreta T_alpha.

**Status:** PROVADO. E trivial pela definicao.

### 4.2. Conexao com Krajicek e Plausivel

A conexao entre geradores godelianos e a hierarquia ordinal e plausivel:
1. Cada nivel ordinal produz um gerador
2. Geradores de niveis mais altos devem ser mais dificeis
3. Mas isto depende de conjecturas

**Status:** CONJECTURA. Plausivel mas nao provada.

---

## 5. O Que Precisa de Trabalho

### 5.1. Rigorizar a Conexao Ordinal-Complexidade

A conexao precisa de:
1. Definicao precisa de "forca de gerador" para niveis ordinais
2. Prova rigorosa de que geradores de niveis mais altos sao mais dificeis
3. Limite inferior explicito para TG_alpha^n

### 5.2. Evitar Presuncoes

Nao devemos presumir:
1. Que decidir g_alpha(x) e equivalente a decidir provabilidade
2. Que limites exponenciais sao "provados"
3. Que tabelas sao fatos

### 5.3. Marcar Conjecturas

Todo resultado que depende de P != NP deve ser marcado como:
- "Condicional a P != NP"
- "Conjectura"
- "Sketch de prova"

---

## 6. Formalizacao Lean 4

### 6.1. O Que Pode Ser Formalizado

Alguns resultados podem ser formalizados:
1. Definicao de hierarquia de Beklemishev
2. Monotonicidade (Lema 4.1)
3. Definicao de geradores

### 6.2. O Que NAO Pode Ser Formalizado

Resultados que dependem de conjecturas:
1. Escala ordinal (depende de P != NP)
2. Cortes ordinais (depende de conjecturas)
3. Separacao TG_0 vs TG_1 (depende de P != NP)

### 6.3. Esqueleto (com sorry)

```lean
-- Hierarquia de Beklemishev
def ReflectionHierarchy : Nat → FirstOrder.Theory
  | 0     => PA
  | n + 1 => (ReflectionHierarchy n).addAxiom (RFN (ReflectionHierarchy n))

-- Monotonicidade (PROVADO)
theorem monotonicity (α β : Nat) (h : α < β) :
    (ReflectionHierarchy α) ≤ (ReflectionHierarchy β) :=
  by
    -- Prova trivial por inducao
    sorry

-- Escala ordinal (CONJECTURA - depende de P != NP)
theorem scaling (α : Nat) :
    ∃ c > 0, ∀ n,
      proofLength P (TG (godelGenerator (ReflectionHierarchy α)) n)
        ≥ 2 ^ (c * α * n) :=
  by
    sorry -- Depende de conjecturas nao provadas
```

---

## 7. Status Atual

| Item | Status |
|------|--------|
| Hierarquia de Beklemishev | PROVADO (classico) |
| Geradores de Krajicek | PROVADO (classico) |
| Monotonicidade ordinal | PROVADO (trivial) |
| Escala ordinal da dureza | CONJECTURA |
| Cortes ordinais | CONJECTURA |
| Separacao TG_0 vs TG_1 | CONDICIONAL a P != NP |

---

## 8. Conclusao Honesta

Este documento e exploratorio. Nao provamos nenhuma nova barreira. O que temos e:
1. Uma conexao plausivel entre ordinais e geradores
2. Conjecturas que precisam de rigorizacao
3. Um programa de pesquisa para investigar a conexao

**Recomendacao:** Rebaixar este documento para "notas exploratorias" e nao submeter como paper.

---

## Referencias

1. Beklemishev, L.D. (2003). "Proof-theoretic analysis by iterated reflection."
2. Cook, S.A. and Reckhow, R.A. (1979). "The relative efficiency of propositional proof systems."
3. Krajicek, J. (2004). "Diagonalization in proof complexity."
4. **Krajicek, J. (2023). "A proof complexity conjecture and the Incompleteness theorem." arXiv:2303.10637. JSL 90(3), 2025, pp. 1206-1210.**
5. Krajicek, J. (2024). "Proof complexity generators."
6. Pudlak, P. (2020). "Reflection principles in propositional proof complexity."

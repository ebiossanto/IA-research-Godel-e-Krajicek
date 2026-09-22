# 10 — EXPERIMENTO: Instâncias Finitas dos Geradores g_T^{a,b}

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** EXPERIMENTO/METODOLOGIA — não prova resultados assintóticos; busca invariantes e candidatos R.

---

## 0. Objetivo

Calcular explicitamente, para n pequeno:

1. as imagens g_{PA,n} e g_{T_1,n} (T_1 = PA + RFN_{Π_1}(PA));
2. os complementos de imagem (candidatos a b para τ(g)_b);
3. o déficit de cobertura δ_T(Φ, b) para orçamentos b crescentes;
4. candidatos a redução R: (n, b) ↦ (m, β) testando PPR.

**Não fazemos:** prova assintótica, lower bound, reivindicação de prioridade.

---

## 1. Varredura bibliográfica (resultados desta data)

### 1.1. δ (déficit de cobertura) vs. literatura

| Fonte | O que faz | Sobreposição com δ? |
|-------|-----------|---------------------|
| Krajíček (2023/2025) | τ(g)_b = "b ∉ rng(g)"; hardness de τ individuais | **NÃO** — ele estuda τ pontuais, não conta obrigações não cobertas |
| Krajíček BSL 2024 | Conjectura: rng(g) ∩ NP infinito ≠ ∅ | **NÃO** — about range, not coverage budget |
| Pudlák (2020) arXiv:2007.14835 | "finer scale" de reflexão; comprimento de provas de Con(T)↾n | **NÃO** — mede comprimento de prova de princípios fixos, não déficit |
| Krajíček–Pudlák (1989) | Consistência e complexidade de computação | **NÃO** — contexto clássico diferente |

**Conclusão parcial:** δ como "número de obrigações verdadeiras sem prova dentro do orçamento b para fórmula Φ fixa" **não aparece** nas buscas realizadas.

**Ressalva:** busca especializada (MathOverflow, revisão por pares) ainda necessária antes de reivindicar prioridade.

### 1.2. RBT (Transição de Ramo por Reflexão) vs. literatura

| Fonte | Conceito próximo | Igual a RBT? |
|-------|------------------|--------------|
| Krajíček (ECCC TR10-054, "missing reflection") | Reflexão ausente na tradução proposicional | **NÃO** — é sobre fidelidade da tradução, não mudança de ramo do gerador |
| Krajíček (2023) §construção | Primeiro w sem prova curta | **MECANISMO** — RBT nomeia a *mudança* desse ramo sob RFN |
| Pudlák (2020) | Reflexão local vs. global | **NÃO** |

**Conclusão parcial:** o fenômeno "T → T+RFN muda o primeiro ramo não coberto de w* para all-covered" **não tem nome encontrado**.

**Ressalva:** "Reflection Branch Transition" é nome **proposto**, não estabelecido.

### 1.3. ρ_b (rank de cobertura) vs. literatura

| Fonte | Conceito | Relação com ρ_b |
|-------|----------|-----------------|
| **Pakhomov–Walsh (JSL 2021)** "Reflection ranks" | reflection rank of T = ordinal de prova de T (para Π¹₁-sound ext. de ACA₀⁺) | **PRÓXIMO mas DIFERENTE** — eles: força de reflexão/ordinal; nós: primeiro nível com δ=0 para Φ, b fixos |
| Beklemishev (2003) | Hierarquia de reflexão e ordinais | **DIFERENTE** — não usa déficit de cobertura |
| Schmerl (1979) | Fine structure de reflection formulas | **DIFERENTE** |

**Conclusão:** ρ_b **não é** o reflection rank de Pakhomov–Walsh; precisa ser posicionado explicitamente como noção distinta (cobertura finita vs. força proof-theoretic).

### 1.4. Slow consistency (conexão δ)

| Fonte | Resultado | Conexão com δ |
|-------|-----------|---------------|
| Friedman–Rathjen–Weiermann (2013) | Con*(PA), PA ⊊ PA+Con_s ⊊ PA+Con | Base para "slow vs fast em δ" |
| Freund–Pakhomov (2020) | PA tem provas polinomiais de Con(PA+Con*(PA))↾n | **ABERTO:** isso aparece em δ_T(Φ,b)? |
| Henk–Pakhomov (2016) | 3 variantes; Turing–Feferman: ε₀, ω, 2 passos | **ABERTO:** assinatura em δ? |

**Pergunta concreta gerada:**

> Para Φ que codifica Con, δ_{PA+Con_s}(Φ, b) vs. δ_{PA+Con}(Φ, b) — há diferença mensurável?

---

## 2. Setup experimental

### 2.1. Teorias (nível finito, sem ordinais)

- **T₀ = PA** (axiomatização fixa, ex.: PEANO padrão com codificação de Gödel fixada)
- **T₁ = PA + RFN_{Π₁}(PA)** (esquema Π₁ sobre fórmulas Π₁ de tamanho ≤ L)

**Fixar L** (ex.: L = 20) para o experimento finito — não é a teoria completa, é uma truncagem.

### 2.2. Parâmetros do gerador

| Parâmetro | Função | Valores testados |
|-----------|--------|------------------|
| a(n) | orçamento de descrição | a(n) = ⌊log₂ n⌋ (ou constante c ∈ {3,4,5}) |
| b(n) | orçamento de prova | b ∈ {4, 8, 16, 32, 64} bits |

### 2.3. Codificação (Etapa A — canônica)

Fixar UMA vez:

1. Codificação de fórmulas L (prefix-free, tipo Gödel);
2. Codificação de provas (sequência de fórmulas + regra);
3. Comprimento = número de símbolos (ou bits — escolher e documentar);
4. Φ ⊆_e u = Φ é prefixo de u como strings binárias;
5. w ∈ {0,1}^{|Φ|+1}; Φ^w como em 09 §4 Passo C.

**Sem essa fixação, g_T não é um objeto único.**

### 2.4. Fórmula Φ de teste (Lema 3 finito)

Para n com prefixo Φ_PA (codificação fixa de):

```
Φ_PA(x) := ∃p,z [ Prf_PA(p, ⊥) ∧ x = pad(w*, p, z) ]
```

- w* = prefixo fixo de Φ_PA;
- Para n ≥ |Φ_PA|: entrada u = Φ_PA u₀ com |u₀| = n − |Φ_PA|.

**V de verdade (finito):** para w ∈ W_Φ, decidir ℕ ⊨ Φ^w é decidível para Φ limitada (verificar se existe x grande o suficiente com Φ(x) ∧ prefixo w — na prática: se Prf_PA(p,⊥) não existe para p < 2^k, então Φ é falso em todo x, logo todos Φ^w são verdadeiros no ramo "fundo vazio").

---

## 3. Algoritmo de enumeração

### 3.1. Para cada n ∈ {8, 9, 10, 11, 12, 13, 14, 15, 16}

```
1. Listar todos u ∈ {0,1}^n com prefixo Φ_PA (se n ≥ |Φ_PA|):
   u = Φ_PA · u₀,  u₀ ∈ {0,1}^{n−|Φ_PA|}

2. Para cada u:
   a. Extrair Φ (prefixo ≤ a(n) bits)
   b. Se Φ inválida ou |Φ| > a(n): saída = 0^{n+1}
   c. W_Φ = {0,1}^{|Φ|+1}
   d. Para cada w ∈ W_Φ (ordem lex):
      - Se Φ^w falso em ℕ: pular (não conta em W^true)
      - Se Φ^w verdadeiro:
          procurar prova π de Φ^w com |π| ≤ b
          se existe: marcar COBERTO
          senão: marcar NÃO COBERTO
   e. w₀ = primeiro w não coberto (lex)
      se existe: saída = w₀ · u₀
      senão: saída = 0^{n+1}

3. Registrar: g_{T,n}(u) para cada u; imagem; complemento
4. Calcular δ_T(Φ_PA, b) = |{w ∈ W^true : não coberto}|
```

### 3.2. Busca de provas (limitada)

Para b ≤ 64: enumeração exaustiva de sequências de axiomas/inferências até comprimento b.
Para PA: usar um sistema fixo (ex.: FSTQ ou codificação de sequências Dedekind).
**Nota:** busca completa é 2^{O(b)}; para b=64 ainda viável com otimizações (hash de subprovas).

---

## 4. Tabela de coleta (esqueleto)

### 4.1. Imagens e δ

| n | \|Φ_PA\| | \|W^true\| | b | δ_{T₀} | δ_{T₁} | 𝒢 = δ₀−δ₁ | w₀(T₀) | w₀(T₁) |
|---|----------|------------|---|--------|--------|------------|---------|---------|
| 8 | | | 4 | | | | | |
| 8 | | | 8 | | | | | |
| … | | | … | | | | | |
| 16 | | | 64 | | | | | |

### 4.2. Complemento de imagem (candidatos a τ)

| n | \|rng(g_{T₀,n})\| | \|{0,1}^{n+1} \ rng\| | amostra b ∉ rng |
|---|-------------------|----------------------|-----------------|
| 8 | | | |
| … | | | |

### 4.3. Transição de Ramo (RBT)

| n | b | primeiro ramo não coberto T₀ | primeiro ramo não coberto T₁ | RBT ocorre? |
|---|---|------------------------------|------------------------------|-------------|
| | | | | SIM/NÃO |

**RBT = SIM** iff w₀(T₀) ≠ w₀(T₁) ou (w₀(T₀) existe e w₀(T₁) = all-covered).

---

## 5. Busca por R (candidatos a PPR)

### 5.1. Espaço de busca (inicial)

Para cada par (n, b) com τ(g_{T₁})_β e τ(g_{T₀})_b:

1. Enumerar β ∉ rng(g_{T₁,m}) para m ≤ p(n) (p linear: m = n, n+1, 2n);
2. Testar: β = R(n, b) com R de forma simples:
   - R₁: identidade (se domínios coincidem);
   - R₂: extensão de prefixo (β = b ‖ 0^k);
   - R₃: XOR com constante;
   - R₄: máscara dependente de n.
3. Verificar PPR-2: b ∉ rng(g₀) ⟹ R(n,b) ∉ rng(g₁)
4. Se PPR-2 vale em todas as amostras: tentar Θ (tradução de provas)

### 5.2. Critério de sucesso parcial

- **R candidate:** PPR-2 vale para todos os n testados (n = 8..16);
- **R validated:** PPR-3 com Θ explícito e cota q verificada para amostras;
- **R refuted:** contraexemplo a PPR-2 encontrado.

---

## 6. Pseudocódigo (Python-like)

```python
# FIX CODING ONCE
ENC_FORMULA = ...  # prefix-free
ENC_PROOF = ...
def Phi_prefix(n): return ENC_FORMULA("Con_PA_encoding")  # fixa

def generator(T, u, a, b, proof_search):
    n = len(u)
    phi = longest_valid_prefix(u, max_len=a(n))
    if phi is None: return "0" * (n+1)
    r = len(phi) + 1
    u0 = u[len(phi):]
    for w in lex_order(r):  # {0,1}^r
        if not true_PHI_w(phi, w): continue
        if not proof_search(T, PHI_w(phi, w), max_len=b):
            return w + u0
    return "0" * (n+1)

def delta(T, phi, b, proof_search):
    r = len(phi) + 1
    W_true = [w for w in lex_order(r) if true_PHI_w(phi, w)]
    covered = [w for w in W_true if proof_search(T, PHI_w(phi, w), max_len=b)]
    return len(W_true) - len(covered)
```

---

## 7. Resultados esperados vs. possíveis

### 7.1. Se RBT aparece (RBT = SIM para algum n, b)

- Evidência de que reflexão muda o ramo do gerador em instâncias finitas;
- Não prova o Teorema 4 assintótico, mas **corrobora** a construção Φ_T;
- Candidato a nota curta se generalizável.

### 7.2. Se δ_{T₁} < δ_{T₀} sistematicamente

- Corrobora Teorema 2 em instâncias;
- Mede 𝒢 empiricamente;
- Permite traçar curvas δ(b) para cada T.

### 7.3. Se R candidate é encontrado

- Primeiro passo concreto para R3 (PPR entre T₀ e T₁);
- Permite tentar Θ.

### 7.4. Se R refutado

- Contraexemplo a candidatos simples;
- Informa que PPR (se existe) não é trivial;
- Ainda é resultado útil (direciona busca).

---

## 8. Limitações declaradas

1. **n ≤ 16** — nada assintótico;
2. **RFN truncada em L** — não é PA+RFN(PA) completo;
3. **Sistema de prova fixo** — resultados dependem da codificação;
4. **Busca de provas limitada por b** — não decide verdade aritmética completa;
5. **Sem reivindicação de originalidade** — ver §1.

---

## 9. Próximos passos (após este experimento)

1. Rodar enumeração e preencher §4;
2. Classificar RBT: ocorre/não ocorre;
3. Se R candidate: construir Θ e testar PPR-3;
4. Se resultados estáveis: posicionar vs. Pudlák/Krajíček com cuidado;
5. Atualizar `EVOLUCAO_PROJETO.md` com achados;
6. Decidir: nota curta vs. continuar como programa.

---

## Referências da varredura

1. Krajíček, J. (2025). JSL 90(3), 1206–1210. arXiv:2303.10637.
2. Krajíček, J. (2024). "On the Existence of Strong Proof Complexity Generators." BSL 30(1), 20–40. arXiv:2208.11642.
3. Krajíček, J. (2025). *Proof Complexity Generators*. Cambridge UP.
4. Krajíček, J. (2026). "On NP∩coNP Proof Complexity Generators." LMCS 22(2). arXiv:2506.20221.
5. Pudlák, P. (2020). "Reflection principles, propositional proof systems, and theories." arXiv:2007.14835.
6. Krajíček, J. & Pudlák, P. (1989). JSL 54(3), 1063–1079.
7. Pakhomov, F. & Walsh, J. (2021). "Reflection Ranks and Ordinal Analysis." JSL 86(4), 1350–1375. arXiv:1805.02095.
8. Freund, A. & Pakhomov, F. (2020). "Short Proofs for Slow Consistency." NDJFL 61(1), 31–49. arXiv:1712.03251.
9. Henk, P. & Pakhomov, F. (2016). "Slow and Ordinary Provability for PA." arXiv:1602.01822.
10. Friedman, S., Rathjen, M., Weiermann, A. (2013). "Slow complexity." APAL.
11. Beklemishev, L.D. (2003). "Proof-theoretic analysis by iterated reflection." APAL.
12. Krajíček, J. (2011). ECCC TR10-054 (missing reflection).

# Nota Curta — Déficit de Cobertura δ e Transição de Ramo RBT vs. Literatura

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** NOTA DE POSICIONAMENTO BIBLIOGRÁFICO — não é artigo de resultados
**Classificação honesta:** candidatos a novidade (busca inicial); não certificados por pares

---

## 1. Objetivo

Posicionar duas noções introduzidas neste projeto — **δ (déficit de cobertura)** e
**RBT (Reflection Branch Transition)** — em relação à literatura de proof complexity
e ordinal analysis mais próxima. Também esclarecer a relação de **ρ_b** com o
"reflection rank" de Pakhomov–Walsh.

---

## 2. Noções do projeto (definições operacionais)

### 2.1. δ — déficit de cobertura

Para teoria T, fórmula Φ e orçamento de prova b:

> **δ_T(Φ, b) := |W^true| − |{w ∈ W^true : T prova Φ^w com prova ≤ b}|**

Conta **quantas obrigações verdadeiras ficam sem prova curta** sob orçamento b.

### 2.2. RBT — Reflection Branch Transition

Dizemos que **RBT ocorre** em b se o primeiro ramo (obrigação) não coberto muda
ao passar de T para T' = T + RFN, ou se T' cobre tudo enquanto T não:

> w₀(T, b) ≠ w₀(T', b)  (incluindo ALL_COV como valor sentinela)

### 2.3. ρ_b — rank de cobertura

> **ρ_b(Φ) :=** primeiro nível/índice onde δ_T(Φ, b) = 0.

---

## 3. Literatura mais próxima — comparação

### 3.1. Pudlák (2020), arXiv:2007.14835

**"Reflection principles, propositional proof systems, and theories."**

- Mede **comprimento de provas** de princípios de reflexão/consistência fixos
  (Con(T)↾n, RFN(T)↾n) em sistemas proposicionais.
- Escala "mais fina" (finer scale) de reflexão por tamanhos de prova.

| Aspecto | Pudlák | Este projeto (δ) |
|---------|--------|------------------|
| O que mede | comprimento mínimo de prova de princípio fixo | nº de obrigações **sem** prova ≤ b |
| Variável | tamanho n do princípio | orçamento b **e** fórmula Φ |
| Sobreposição | parcial: δ usa comprimento implicitamente | δ é **complementar** (conta falhas, não sucessos) |

**Conclusão:** δ **não é** Pudlák (2020); é observável dual/complementar.
Busca inicial não encontrou δ definido explicitamente.

### 3.2. Krajíček (2023/2024/2025)

- **τ(g)_b**: fórmula "b ∉ rng(g)" — individuais, por gerador.
- **Footnote 3 / Seção 3 (2023):** b(n)→ω(1) — **já existe** (D7).
- **Hardness de rng(g)**: conjectura rng(g) ∩ NP infinito ≠ ∅ (BSL 2024).

| Aspecto | Krajíček | Este projeto (δ, RBT) |
|---------|----------|----------------------|
| Unidade | τ pontual (uma fórmula por b) | **conjunto** de obrigações Φ^w |
| Orçamento | b no tamanho de τ/prova de τ | b no tamanho de prova de **cada** Φ^w |
| Reflexão | não estuda muda de ramo em T→T+RFN | **RBT** nomeia exatamente isso |

**Conclusão:** δ agregado e RBT **não aparecem** em Krajíček (busca inicial).

### 3.3. Pakhomov–Walsh (JSL 2021), arXiv:1805.02095

**"Reflection Ranks and Ordinal Analysis."**

- **Reflection rank of T** = ordinal de prova de T para extensões Π¹₁-sound de ACA₀⁺.
- Mede **força proof-theórica** (ordinais), não cobertura finita.

| Aspecto | Pakhomov–Walsh | ρ_b (este projeto) |
|---------|----------------|---------------------|
| Natureza | ordinal (proof-theoretic) | **primeiro nível com δ=0** (finito/combinatório) |
| Depende de b? | não (é ordinal) | **sim** (ρ_b indexado por orçamento) |
| Depende de Φ? | não | **sim** |

**Conclusão:** ρ_b **≠** reflection rank; posicionamento explícito necessário em qualquer texto.

### 3.4. Outros

- **Krajíček (ECCC TR10-054):** "missing reflection" — fidelidade de tradução,
  não muda de ramo do gerador. Próximo mas distinto de RBT.
- **Beklemishev (2003):** hierarquia de reflexão por ordinais — sem δ.
- **Freund–Pakhomov (2020) / Henk–Pakhomov (2016):** slow consistency —
  geram pergunta PR7 (Con*(PA) em δ?), não definem δ.

---

## 4. Veredito de prioridade (busca inicial 22/09/2026)

| Noção | Encontrada? | Status declarado |
|-------|-------------|------------------|
| δ (déficit de cobertura) | **NÃO** | **candidata a novidade** (não certificada) |
| RBT (transição de ramo) | **NÃO** | **candidata a novidade**; nome proposto |
| ρ_b (rank de cobertura) | **PRÓXIMO: P–W** | **distinta**; posicionar sempre |
| suffix0 como R | teste: **vácuo** | **abandonado** como R final (11 §4.3) |

---

## 5. Ressalvas metodológicas (obrigatórias)

1. **Busca inicial** (web/arXiv/Google Scholar) — não substitui revisão por pares
   nem consulta a especialistas (Pudlák, Krajíček, Pakhomov, Freund).
2. **Experimentos 10/11/reimplementação** são **proposicionais/estruturais** —
   capturam a mecânica, não certificam PA real.
3. **suffix0** mostrou-se vácuo — honestidade: não é resultado positivo de PPR-3.
4. Nada aqui é "teorema" no sentido do projeto (hipóteses/domínios/codificações
   não totalmente formalizados em um assistente de provas).

---

## 6. O que tornaria sólido

- Especialista revisar §3 (δ vs Pudlák; ρ_b vs P–W);
- Reimplementação em Lean/Isabelle com PA (ou IΣ₁) real;
- Provar ou refutar a condição CC-Θ (11 §3.3) para algum R não-vácuo;
- Nota de 2–4 páginas só com §2–§4 se δ/RBT resistirem a consulta.

---

## Referências

1. Pudlák, P. (2020). arXiv:2007.14835.
2. Krajíček, J. (2023/2025). arXiv:2303.10637; JSL 90(3).
3. Krajíček, J. (2024). BSL 30(1). arXiv:2208.11642.
4. Krajíček, J. (2011). ECCC TR10-054.
5. Pakhomov, F. & Walsh, J. (2021). JSL 86(4). arXiv:1805.02095.
6. Freund, A. & Pakhomov, F. (2020). arXiv:1712.03251.
7. Henk, P. & Pakhomov, F. (2016). arXiv:1602.01822.
8. Beklemishev, L.D. (2003). APAL.

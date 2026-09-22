# Indice da Pesquisa Gödel–Krajíček

**Versão:** 4.0 (Setembro 2026)
**Status:** Honestidade intelectual — teoremas descartados, conjecturas separadas

---

## Estrutura dos Documentos

### Papers Reescritos (estado atual honesto)

| Arquivo | Conteúdo | Status |
|---------|----------|--------|
| `papers/paper1_barreira_interpretabilidade.md` | "Barateando a Diagonalização" — extensão de Krajíček (2023) | Nota exploratória |
| `papers/paper2_hierarquia_ordinal.md` | Hierarquia ordinal e consistência lenta | Nota exploratória |

### Conjecturas e Continuidade

| Arquivo | Conteúdo | Status |
|---------|----------|--------|
| `CONJECTURA_FP_K.md` | Conjectura FP-K: análogo Freund–Pakhomov para geradores g_T | **Conjectura** (não provada) |
| `07_pontos_fixos_incompletude.md` | Pontos fixos, incompletude e física — Parte 2 | Teoremas + analogias + conjecturas separados |
| `CONTINUIDADE_PESQUISA.md` | Documento de continuidade completo | Ativo |

### Documentos de Apoio (em `support/`) — CONTÊM AFIRMAÇÕES DESATUALIZADAS

| Arquivo | Status |
|---------|--------|
| `00_avaliacao_novelidade.md` | Parcialmente válido |
| `01_framework_estendido.md` | **DESCARTADO** (framework anterior) |
| `02_teoremas_principais.md` | **DESCARTADO** (teoremas 4-6 inválidos/especulativos) |
| `03_meta_complexidade_aplicacoes.md` | **DESCARTADO** (especulativo) |
| `04_questoes_abertas_referencias.md` | Desatualizado |
| `05_verificacao_lean4.md` | Plano Lean 4 ainda útil |

### Documentos Originais (raiz) — DESATUALIZADOS

| Arquivo | Status |
|---------|--------|
| `goedel_complexity_paper pnp.md` | **DESCARTADO** (Teorema 1 inválido) |
| `06_paper2_hierarquia_ordinal.md` | Substituído por `papers/paper2_...` |
| `goedel_complexity_original_contributions.md` | Desatualizado |

---

## Status dos Resultados (versão honesta)

### TEOREMAS (provados, na literatura ou elementares)

| # | Resultado | Status | Fonte |
|---|-----------|--------|-------|
| T1 | Completude da lógica proposicional | PROVADO | Clássico |
| T2 | Proposição 1: pontos fixos ↔ status lógico | PROVADO | Elementar, novo |
| T3 | Proposição 2: distribuições invariantes (caso finito) | PROVADO | Deutsch (1991) |
| T4 | Proposição 3: Fix(f) ≠ ∅ ≡ problema da parada | PROVADO | Elementar, novo |
| T5 | Choquet-Bruhat–Geroch (1969) | PROVADO | Clássico |
| T6 | Markov (1958): homeomorfismo indecidível (dim ≥ 4) | PROVADO | Clássico |
| T7 | Tarski: geometria real decidível | PROVADO | Clássico |
| T8 | Corolário Gödel–Turing: laco paradoxal irreconhecível | PROVADO | Corolário |

### CONJECTURAS (não provadas)

| # | Conjectura | Status | Documento |
|---|------------|--------|-----------|
| C1 | **FP-K**: análogo Freund–Pakhomov para g_T com ordinal crítico α_* | ABERTA | `CONJECTURA_FP_K.md` |
| C2 | Censura cósmica exclui estruturas Malament–Hogarth | ABERTA | `07_...` |
| C3 | Física necessariamente codifica aritmética | ESPECULATIVA | `07_...` |
| C4 | Teorema da Incompletude Cosmológica | ESPECULATIVA | `07_...` |

### DESCARTADOS (não usar)

| # | Resultado antigo | Motivo |
|---|------------------|--------|
| D1 | Teorema 1 original (barreira de interpretabilidade) | Enumeração exponencial ≠ polinomial; Krajíček (2023) já faz |
| D2 | Tabela de bounds duplamente exponenciais | Especulativa, sem derivação |
| D3 | Cortes ordinais C(α) | Não sabemos se hierarquia é suficiente |
| D4 | Teoremas 4–6 (framework estendido) | Descartados na reescrita |
| D5 | Observação b(n) genérico | **JÁ EXISTE** — Krajíček (2023), rodapé 3, Seção 3 |

---

## Pergunta de Pesquisa Principal

> **Conjectura FP-K:** Existe um análogo do fenômeno Freund–Pakhomov dentro do esquema g_T de Krajíček? Isto é, existe ordinal crítico α_* tal que g_{T_α}^{(b)} recupera a força diagonalizadora de g_T?

**Status:** Conjectura plausível, não provada, não encontrada na literatura.
**Próximo passo:** Verificar literatura + MathOverflow (tag proof-theory).

---

## Referências Obrigatórias

1. **Krajíček, J. (2023).** "A proof complexity conjecture and the Incompleteness theorem." arXiv:2303.10637; JSL 90(3), 2025, 1206–1210.
2. **Krajíček, J. (2025).** *Proof Complexity Generators.* Cambridge UP (LMS Lecture Notes 497).
3. **Friedman–Rathjen–Weiermann (2013).** Slow consistency. APAL.
4. **Freund–Pakhomov (2020).** Provability algebras. NDJFL.
5. **Beklemishev (2003).** Proof-theoretic analysis by iterated reflection.
6. **Deutsch (1991).** Quantum mechanics near closed timelike lines.
7. **Choquet-Bruhat–Geroch (1969).** Global solutions of nonlinear hyperbolic equations.
8. **Markov (1958).** The insolubility of the problem of homeomorphy.
9. **Lawvere (1969).** Diagonal arguments and cartesian closed categories.
10. **Hogarth (1992); Etesi–Németi (2002).** Malament–Hogarth spacetimes.

---

## Contato

- **Autor:** Euzebio Santos (ebiossanto)
- **Repositório:** https://github.com/ebiossanto/IA-research-Godel-e-Krajicek

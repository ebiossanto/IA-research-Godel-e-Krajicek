# Indice da Pesquisa Gödel–Krajíček

**Versão:** 5.0 (Setembro 2026, pós-auditoria)
**Status:** Honestidade intelectual — teoremas 4-6 rejeitados, FP-K rebaixada, novo programa ≼_ppr

---

## Estrutura dos Documentos

### Papers Reescritos (estado atual honesto)

| Arquivo | Conteúdo | Status |
|---------|----------|--------|
| `papers/paper1_barreira_interpretabilidade.md` | "Barateando a Diagonalização" — extensão de Krajíček (2023) | Nota exploratória |
| `papers/paper2_hierarquia_ordinal.md` | Hierarquia ordinal e consistência lenta | Nota exploratória |

### Conjecturas, Programa e Continuidade

| Arquivo | Conteúdo | Status |
|---------|----------|--------|
| `08_PROGRAMA_INTERPRETABILIDADE_VS_GERADORES.md` | **NOVO: programa ≼_int vs ≼_ppr (pós-auditoria)** | **PROGRAMA ATIVO** |
| `CONJECTURA_FP_K.md` | FP-K: análogo Freund–Pakhomov para geradores | **PERGUNTA DE PESQUISA** (rebaixada) |
| `07_pontos_fixos_incompletude.md` | Pontos fixos, incompletude e física — Parte 2 | Teoremas + analogias + conjecturas separados |
| `CONTINUIDADE_PESQUISA.md` | Documento de continuidade completo | Atualizado pós-auditoria |

### Documentos de Apoio (em `support/`) — CONTÊM AFIRMAÇÕES DESATUALIZADAS/REJEITADAS

| Arquivo | Status |
|---------|--------|
| `00_avaliacao_novelidade.md` | Parcialmente válido |
| `01_framework_estendido.md` | **DESCARTADO** (framework anterior) |
| `02_teoremas_principais.md` | **REJEITADO** (Teoremas 4-6 não provados — auditoria 22/09/2026) |
| `03_meta_complexidade_aplicacoes.md` | **DESCARTADO** (especulativo) |
| `04_questoes_abertas_referencias.md` | Desatualizado (Q1 usa premissa rejeitada) |
| `05_verificacao_lean4.md` | Plano Lean 4 ainda útil (não certifica T4-6) |

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

### CONJECTURAS / PERGUNTAS (não provadas)

| # | Item | Status | Documento |
|---|------|--------|-----------|
| P1 | **FP-K**: análogo Freund–Pakhomov para g_T | **PERGUNTA DE PESQUISA** (rebaixada, originalidade não certificada) | `CONJECTURA_FP_K.md` |
| C2 | Censura cósmica exclui estruturas Malament–Hogarth | CONJECTURA ABERTA | `07_...` |
| C3 | Física necessariamente codifica aritmética | ESPECULATIVA | `07_...` |
| C4 | Teorema da Incompletude Cosmológica | ESPECULATIVA | `07_...` |

### PROGRAMA ATIVO (pós-auditoria)

| # | Problema | Status | Documento |
|---|----------|--------|-----------|
| **PR1** | **T ≼_int S ⟹? g_T ≼_ppr g_S** | **PROBLEMA FORMAL ABERTO** | `08_PROGRAMA_...` |
| PR2 | Γ_P(T,n) = log s_P(TG_T^n): assinatura da reflexão? | DEFINIÇÃO PROPOSTA | `08_PROGRAMA_...` |

### DESCARTADOS / REJEITADOS (não usar)

| # | Resultado antigo | Motivo |
|---|------------------|--------|
| D1 | Teorema 1 original (barreira de interpretabilidade) | Enumeração exponencial ≠ polinomial; Krajíček (2023) já faz |
| D2 | Tabela de bounds duplamente exponenciais | Especulativa, sem derivação |
| D3 | Cortes ordinais C(α) | Não sabemos se hierarquia é suficiente |
| D4 | **Teorema 4: s_P ≥ 2^{c|T_α|n}** | **REJEITADO** (auditoria): contagem ≠ lower bound; \|T_α\| ambíguo |
| D5 | **Teorema 5: cortes estritos** | **NÃO PROVADO** (auditoria): falta ponte teorias↔sistemas |
| D6 | **Teorema 6(a)(b)(c)** | **NÃO PROVADO** (auditoria): T_* não é r.e.; hardness ≠ completude |
| D7 | Observação b(n) genérico | **JÁ EXISTE** — Krajíček (2023), rodapé 3, Seção 3 |

---

## Pergunta de Pesquisa Principal (pós-auditoria)

**ANTES (rebaixada):**
> ~~Conjectura FP-K~~ → **PERGUNTA DE PESQUISA** — originalidade não estabelecida.

**AGORA (mais promissora):**

$$T \preceq_{int} S \stackrel{?}{\Longrightarrow} g_T \preceq_{ppr} g_S$$

A ordem proof-theoretic de interpretabilidade é refletida pela ordem operacional de dificuldade de geradores?

**Três casos:** (A) teorema de transferência · (B) classe restrita · (C) contraexemplo = quebra entre hierarquias.

**Documento:** `08_PROGRAMA_INTERPRETABILIDADE_VS_GERADORES.md`

---

## Referências Obrigatórias (corrigidas)

1. **Krajíček, J. (2025).** "A Proof Complexity Conjecture and the Incompleteness Theorem." JSL 90(3), 1206–1210. arXiv:2303.10637. doi:10.1017/jsl.2023.69
2. **Krajíček, J. (2025).** *Proof Complexity Generators.* Cambridge UP (LMS Lecture Notes 497).
3. **Beklemishev, L.D. (2005).** "Reflection principles and provability algebras in formal arithmetic." Russian Math. Surveys 60(2), 197–268.
4. **Freund, A. & Pakhomov, F. (2020).** "Short proofs for slow consistency." Notre Dame J. Formal Logic 61(1), 31–49. doi:10.1215/00294527-2019-0031
5. **Krajíček, J. (1997).** "Interpolation theorems, lower bounds for proof systems..." JSL 62(2), 457–486.
6. **Deutsch (1991).** Quantum mechanics near closed timelike lines.
7. **Choquet-Bruhat–Geroch (1969).** Global solutions of nonlinear hyperbolic equations.
8. **Markov (1958).** The insolubility of the problem of homeomorphy.
9. **Lawvere (1969).** Diagonal arguments and cartesian closed categories.
10. **Hogarth (1992); Etesi–Németi (2002).** Malament–Hogarth spacetimes.

---

## Contato

- **Autor:** Euzebio Santos (ebiossanto)
- **Repositório:** https://github.com/ebiossanto/IA-research-Godel-e-Krajicek

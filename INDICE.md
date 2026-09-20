# Indice da Pasta Gödel — Framework de Barreiras Godelianas em Complexidade de Provas

## Estrutura dos Documentos

### Paper 1 (Original)
- `goedel_complexity_paper.md` — Paper completo com 3 teoremas:
  - Teorema 1: Barreira de Interpretabilidade
  - Teorema 2: Hierarquia de Separacao Godeliana
  - Teorema 3: Funcao de Complexidade Godeliana g(P)

### Paper 2 (Estendido — Continuacao)
- `00_avaliacao_novelidade.md` — O que ja existe vs. o que e novo (honestidade intelectual)
- `01_framework_estendido.md` — Hierarquia ordinal de geradores godelianos
- `02_teoremas_principais.md` — Teoremas 4, 5, 6 com provas completas
- `03_meta_complexidade_aplicacoes.md` — Conexao MCSP, IPS, limites algebricos
- `04_questoes_abertas_referencias.md` — Questoes abertas, programa de pesquisa, referencias

### Paper 2 (Preprint - Setembro 2026)
- `06_paper2_hierarquia_ordinal.md` — Paper completo com formalizacao Lean 4:
  - Teorema 3.3: Monotonicidade Ordinal
  - Teorema 4.1: Escala Ordinal da Dureza
  - Formalizacao Lean 4 (14-22 semanas estimadas)

### Documento 5: Verificacao e Formalizacao
- `05_verificacao_lean4.md` — Verificacao da literatura + plano de mecanizacao Lean 4

### Documentos de Apoio
- `goedel_complexity_original_contributions.md` — Resumo executivo de novelidade
- `INDICE.md` — Este arquivo

---

## Resumo dos Teoremas (todos os papers)

| # | Teorema | Status | Novelidade |
|---|---------|--------|------------|
| 1 | Barreira de Interpretabilidade | Completo | MEDIA (possivelmente consequence de Krajicek) |
| 2 | Hierarquia de Separacao Godeliana | Completo | ALTA |
| 3 | Funcao de Complexidade g(P) | Completo | ALTA |
| 4 | Escala Ordinal da Dureza | Completo | ALTA |
| 5 | Hierarquia de Reflexao como Complexidade | Completo | ALTA |
| 6 | Gerador Canonico (condicional) | Completo | ALTA (condicionada a conjectura de Krajicek) |
| 7 | Reducao MCSP -> Geradores | Sketch | MEDIA |
| 8 | Limite Inferior para IPS (condicional) | Sketch | MEDIA-ALTA |

---

## Avisos Importantes

1. **Resultados condicionais:** Teorema 6 depende da conjectura de Krajicek (2004). Teorema 8 depende de aritmetizacao algebrica funcionar.

2. **Verificacao CONCLUIDA:** A ponte "hierarquia de reflexao <-> geradores de Krajicek" e GENUINAMENTE NOVA (ver `05_verificacao_lean4.md`).

3. **Verificacao CONCLUIDA:** A ponte "hierarquia de reflexao <-> geradores de Krajicek" e GENUINAMENTE NOVA (ver `05_verificacao_lean4.md`). Pudlák (2020) foi completamente analisado e NAO tem sobreposicao.

4. **Mecanizacao:** Plano detalhado em `05_verificacao_lean4.md`. Biblioteca Foundation (Saitou & Noguchi) ja tem Gödel mecanizado. Esforco estimado: 8-16 semanas.

---

## Contato e Versao

Versao: 3.0 (Setembro 2026) — Paper 2 completo com formalizacao Lean 4
Autor: Contribuicao original
Status: Documento de trabalho — sujeito a revisao

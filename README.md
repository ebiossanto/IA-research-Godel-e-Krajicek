# IA Research: Godel e Krajicek

**Status:** Notas Exploratorias (nao submetido)
**Ultima atualizacao:** Setembro 2026

## Sobre Este Projeto

> **Nota:** Estes trabalhos sao estudos de ideias desenvolvidos com ferramentas de inteligencia artificial. O autor e um estudante, entusiasta e pesquisador com um brinquedo nas maos.

**Ferramentas utilizadas:** Gemini MiMo V2.5, GPT 5.6 Copilot, Opencode

**Autor:** Euzebio Santos — Estudante, entusiasta e pesquisador

## Aviso Importante

Este repositorio contem **notas exploratorias**, nao papers comprovados. Os resultados sao conjecturas ou observacoes que precisam de verificacao por especialistas.

**Referencia central:** Krajicek, J. (2023). "A proof complexity conjecture and the Incompleteness theorem." arXiv:2303.10637. JSL 90(3), 2025, pp. 1206-1210.

## Resumo

Este repositorio contem dois documentos que exploram a conexao entre:

1. **O mecanismo de Krajicek (2023)** para provar o 1o Teorema de Goedel via geradores
2. **O programa de slow consistency** (Friedman, Pakhomov, Freund)
3. **Uma observacao** sobre baratear a diagonalizacao

## Documentos

### Paper 1: Barateando a Diagonalizacao

**Arquivo:** `papers/paper1_barreira_interpretabilidade.md`

Observacao de que o limite log n na construcao de Krajicek pode ser substituido por qualquer funcao b(n) -> infinito. Com b(n) = log log n, o algoritmo roda em tempo linear.

**Contribuicao:** Separa diagonalizacao crua (barata) de proposicionalizacao (cara).

### Paper 2: Hierarquia Ordinal e Consistencia Lenta

**Arquivo:** `papers/paper2_hierarquia_ordinal.md`

Explora conexao entre hierarquia de Beklemishev e slow consistency. Formula pergunta de pesquisa: existe analogo do fenomeno Freund-Pakhomov dentro do esquema g_T de Krajicek?

**Contribuicao:** Pergunta de pesquisa (nao respondida).

## Status

| Item | Status |
|------|--------|
| Krajicek (2023) | CITADO |
| Slow consistency | CITADO |
| Observacao (b(n)) | CORRETA (mas pode ja existir) |
| Pergunta de pesquisa | FORMULADA |
| Tabela de bounds | DESCARTADA |
| Teorema 4.1 | DESCARTADO |

## Proximos Passos

1. Verificar se observacao ja aparece em Krajicek (2025)
2. Levar pergunta a especialista (MathOverflow)
3. Formalizar em Lean 4

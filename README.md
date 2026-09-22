# IA Research: Godel e Krajicek

**Status:** Notas Exploratorias (nao submetido)

Papers sobre conexao entre incompletude de Godel, complexidade de provas de Krajicek, e hierarquia ordinal de Beklemishev.

## Aviso Importante

Este repositorio contem **notas exploratorias**, nao papers comprovados. Os resultados sao conjecturas ou sketches de prova que precisam de rigorizacao. Muitos resultados dependem da hipotese P != NP.

## Resumo

Este repositorio contem dois papers que estabelecem uma ponte formal entre:

1. **A incompletude de Godel** (teoremas classicos de 1931)
2. **A complexidade de provas de Krajicek** (geradores de tautologias duras)
3. **A hierarquia ordinal de Beklemishev** (analise ordinal de teorias)

## Papers

### Paper 1: Barreira de Interpretabilidade

**Arquivo:** `papers/paper1_barreira_interpretabilidade.md`

Mostra que todo sistema de prova que interpreta PA enfrenta uma "barreira" - existem problemas que ele pode fazer mas nao pode resolver. Quanto mais forte o sistema, mais dificeis sao esses problemas.

**Teoremas principais:**
- Teorema 1 (Barreira): Sistema forte nao e completo E polinomico
- Teorema 2 (Separacao): Sistemas mais fortes resolvem problemas que sistemas mais fracos nao resolvem
- Teorema 3 (Funcao g(P)): Funcao que mede a dificuldade godeliana de cada sistema

### Paper 2: Hierarquia Ordinal de Geradores Godelianos

**Arquivo:** `papers/paper2_hierarquia_ordinal.md`

Conecta a hierarquia de Beklemishev (que indexa teorias por ordinais) com os geradores de Krajicek (que produzem tautologias duras). Mostra que a dificuldade escala exponencialmente com a posicao na hierarquia ordinal.

**Teoremas principais:**
- Teorema 3.3 (Monotonicidade): Se alpha < beta, sistemas que provam TG_beta tambem provam TG_alpha
- Teorema 4.1 (Escala Ordinal): s_P(TG_alpha^n) >= 2^{c * |T_alpha| * n}

## Estrutura

```
IA-research-Godel-e-Krajicek/
├── README.md                    # Este arquivo
├── papers/                      # Papers principais
│   ├── paper1_barreira_interpretabilidade.md
│   └── paper2_hierarquia_ordinal.md
├── support/                     # Documentos de apoio
│   ├── 00_avaliacao_novelidade.md
│   ├── 01_framework_estendido.md
│   ├── 02_teoremas_principais.md
│   ├── 03_meta_complexidade_aplicacoes.md
│   ├── 04_questoes_abertas_referencias.md
│   └── 05_verificacao_lean4.md
├── lean4/                       # Formalizacao Lean 4
│   └── Gothic_Generators/
│       └── OrdinalHierarchy.lean
└── INDICE.md                    # Indice geral
```

## Conceitos Chave

### Geradores Godelianos

Um gerador godeliano g_T produz tautologias TG_g^n que sao dificeis para qualquer sistema que interpreta T. A construcao usa o Lema do Ponto Fixo de Godel.

### Hierarquia de Beklemishev

Uma progressao de teorias indexadas por ordinais:
- T_0 = PA
- T_{alpha+1} = T_alpha + RFN(T_alpha)
- T_lambda = union_{alpha < lambda} T_alpha

### A Ponte

Cada nivel alpha da hierarquia produz um gerador g_alpha. A dificuldade de provar TG_alpha^n escala com a ordem-teorica |T_alpha|.

## Status

| Item | Status |
|------|--------|
| Paper 1 (Barreira) | Notas Exploratorias |
| Paper 2 (Hierarquia) | Notas Exploratorias |
| Verificacao de novelidade | Concluida |
| Formalizacao Lean 4 | Esqueleto (com sorry) |
| Tightness (limite otimo) | ABERTO |

## Referencias

- Beklemishev, L.D. (2003). "Proof-theoretic analysis by iterated reflection."
- Krajicek, J. (2024). "Proof complexity generators."
- Krajicek, J. (2025). "A proof complexity conjecture and the incompleteness theorem."
- Saitou, S. and Noguchi, M. (2026). "Mechanizing Godel's Incompleteness Theorems."

## Contato

Autor: ebiossanto
GitHub: https://github.com/ebiossanto

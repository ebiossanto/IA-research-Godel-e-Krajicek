# transicao_dupla — extração do repo `transicao-dupla-krajicek`

**Proveniência:** extração de **<https://github.com/ebiossanto/transicao-dupla-krajicek>**
(público; criado e finalizado em15/10/2026,6 commits; clone analisado em
28/11/2026). Repo **híbrido matemática+produto** da vertente **FCT** — o
nome "krajicek" é *branding* do workspace; **nada de DD_P/proof
complexity aqui** (o próprio §7 do Teorema proíbe essa leitura).

## Conteúdo migrado (math)

| Arquivo | Conteúdo |
|---|---|
| `Teorema da Transição Dupla.md` (92KB) | **Núcleo:** **T1** (break-even único `ρ*` + meia-mitigação `ρ_{1/2}=4√ρ*`, identidade de razão), **LB1** (piso de mitigação), **LB2** (cascata bullwhip `∏(1+a_k) ≥ 1+Σa_k` → ≥ linear), Corolários C1–C3, **§7 non-claims** (nenhum lower bound de complexidade; L2→L3 aberta) — condicionais a **(A)** (FCT_REFINAMENTO §1, em `motor_fractal_rea/`) |
| `Transição Global em Cascatas Heterogâneas.md` + `…2.md` | **TGH:** teorema global de cascatas heterogêneas — produtos acumulados em domínio log, critérios aditivos, AM-GM, limiares globais fechados, compensação entre estágios, robustez — **caveat de novidade honesto** (reivindicar só após busca bibliográfica; lit. bullwhip citada) |
| `dinâmica linear estocástica natural.md` | Fundação estocástica (substitui justificativa informal da raiz quadrada por problema de dinâmica linear) |
| `docs/` (8) | formalization, development, tests, certificates, continuity, measurement, rastreability, reproducible_tests |

## ⚠️ Flags de integridade (registradas na análise de28/11)

1. **`lean4/krajicek/transition.lean` NÃO foi migrado — e não vale como
   N2:** sintaxe Mathlib3 (`begin/end`, `import data.fintype`), lema
   inexistente (`eq_unique`), unicode corrompido e "provas" que não
   fecham → **não compila** no Lean4 do projeto
   (`leanprover/lean4:v4.34`). Não conta como formalização;
2. **Artefatos de máquina ausentes no repo:** o Teorema cita
   `teorema_transicao_dupla_check.py` + `out_teorema_td.json`
   (TUDO_OK=True, sympy1.14, grade2000, seed11) — **não estão no
   repositório** → a checagem sympy **não é reprodutível** a partir do
   repo-fonte. Status real: **(P) com checagem a recuperar** (se os
   artefatos surgirem, migrar aqui);
3. `docs/formalization.md` é esboço incompleto ("demonstrar para
   |X|=n+1…" sem fechar).

## Classificação (A)/(P)/(C)

- **(P) condicionais a (A):** T1, LB1, LB2, TGH (provados no repo;
  sympy citado mas artefato ausente → N2 parcial);
- **(C):** novidade do TGH (o doc exige busca bibliográfica antes de
  reivindicar);
- **Não verificado:** formalização Lean (flag1).

## Impacto no projeto (por que migrou)

**Correção do item D1** (`ONDE_ESTAMOS` §5): a fórmula `ρ_c=0.25`
**não é** "quantização da taxa de transição" — pelo T1 (Modelo A,
q=1/2) é **`ρ_{1/2}`** (meia-mitigação) e, pelo LB1, **piso de
garantia**; o break-even é `ρ*=0,0625`. O experimento D1 precisa dessa
interpretação **antes** de rodar (atualizado no D1).

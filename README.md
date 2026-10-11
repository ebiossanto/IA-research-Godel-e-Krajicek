# IA Research: Gödel e Krajíček

**Status:** Notas exploratórias + campanha de verificação referee-processada (não submetido)
**Última atualização:** 11 de outubro de 2026

> **Nota:** Estes trabalhos são estudos de ideias desenvolvidos com ferramentas de
> inteligência artificial. O autor é um estudante, entusiasta e pesquisador com um
> brinquedo nas mãos.

**Ferramentas utilizadas:** Gemini MiMo, GPT Copilot, OpenCode

**Autor:** Euzébio Soares dos Santos — estudante, entusiasta e pesquisador
(Contato: euambiente@gmail.com · github.com/ebiossanto)

## Aviso importante

Este repositório contém **notas exploratórias e verificações próprias**, não papers
comprovados. Resultados novos são marcados **(P)** (próprios), **(A)** (fonte/artigo)
ou **(C)** (conjectura) e passam por **referee hostile** antes de virarem estado do
projeto. **Índice canônico: [`INDICE.md`](INDICE.md).**

## Os dois eixos do repositório

### Eixo 1 — Programa exploratório (setembro/2026)

Explora a conexão entre o mecanismo de geradores de Krajíček (2023), a hierarquia de
reflexão de Beklemishev e o programa de *slow consistency* (Friedman–Pakhomov–Freund).

- `papers/paper1_barreira_interpretabilidade.md` — observação: o limite `log n` da
  construção de Krajíček admite qualquer `b(n) → ∞` (observação, não teorema).
- `papers/paper2_hierarquia_ordinal.md` — pergunta de pesquisa (não respondida):
  existe análogo do fenômeno Freund–Pakhomov dentro do esquema `g_T`?

**Resultados fortes deste eixo foram RETRAÍDOS por auditoria interna** (ver
`INDICE.md`, seção DESCARTADOS D1–D6): a "barreira de interpretabilidade" (Teorema 1),
a escala exponencial `s_P ≥ 2^{c|T_α|n}` (Teorema 4/4.1), a tabela de bounds e os
teoremas 5 e 6. **Não usar como resultado.** Banner de retração no topo de
`02_teoremas_principais.md`.

### Eixo 2 — Campanha DD_P sobre Krajíček (outubro/2026) — **linha atual**

Verificação própria, com referee hostile por entrega, sobre
**Krajíček, J., arXiv:2506.20221v4/v5 (LMCS 22(2:14)2026)**: pasta
[`krajicek_ddp/`](krajicek_ddp/) — 14 frentes (A–N), todas com referee processado.
Resultados principais (todos (P), com logs):

1. **Lacuna verbatim** no passo (5) da prova do Teorema 4 (v4) / Teorema 3 (v5),
   em **ambas** as versões (F1).
2. `Log(M[G]) = Log(M)` no forcing de Kra95/98 — **`(F-b')` refutado** (G1);
   obstrução ZFC à correção via Problema 2.1 (G2).
3. **Teorema K** (J1): coleção interna impossível; `T_PV+BB+(S2)(S3)(S4)` inconsistente.
4. **`T_PV+(S4) ⊢ ∀rφ(r)`** (L1): `¬φ` internamente insatisfatível; **C.3 negativa**.
5. **Canto adversarial decidido** (M): `C_{N_s} ≡ ⊥` construído (2ª fonte de
   não-compactude).
6. **Redução da refutação interna de `{C_{N_s}}`** (N): existe ⟺ `Taut(α)` tem prova
   EF interna em `M_0` — dicotomia honesta (C1′).
7. **`DD_Res ∈ P`** com refutação pura ≤ |π| (C) — formalizado em Lean 4.
8. **✅ Nota editorial enviada a Krajíček em 11/10/2026**
   (`krajicek_ddp/CARTA_FINAL_ENVIO.md`; jan.krajicek@protonmail.com) —
   **aguardando resposta**.

Consolidação: `krajicek_ddp/RELATORIO_CONSOLIDADO.md` · contexto:
`krajicek_ddp/CONTEXTO_COMUM.md` · evolução: `EVOLUCAO_PROJETO.md`.

## Formalização (Lean 4)

- `lean4/Gothic_Generators/DDP.lean` — `DD_P` (totalidade, solubilidade, lema de
  união) — **compila** (2 `sorry`s documentados e permanentes).
- `FoundationBridge/GodelSecond.lean` — rota B (`phiWStarB`); `lake build` verificado
  **verde, 0 `sorry`** (PR27/PR28).

## Estrutura

```
INDICE.md                  ← índice canônico (auditável)
EVOLUCAO_PROJETO.md        ← cronologia + próximos passos
CONTINUIDADE_PESQUISA.md   ← continuidade entre fases
00_… a 27_…                ← documentos de apoio numerados (canônicos)
papers/                    ← os 2 documentos exploratórios (set/2026)
krajicek_ddp/              ← campanha DD_P completa (out/2026) — linha atual
lean4/  FoundationBridge/  ← formalização
archive/                   ← snapshots antigos (não canônicos; ver archive/README.md)
CRITICA_EXTERNA_2026-10-11.md ← resposta pontual à crítica externa recebida
```

## Próximos passos

1. **Aguardar/registrar a resposta de Krajíček** (perguntas Q1–Q4 da carta).
2. Residuais da frente N: R-α (omitting types) e R-β (compressão P→EF).
3. `DD_Res ∈ P` → `Res(k)`; instâncias `(τ_n, q)` concretas para a pergunta Q.
4. MathOverflow post — **só com confirmação do autor**.

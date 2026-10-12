# IA Research: Gödel e Krajíček

**Status:** Notas exploratórias + campanha DD_P com **revisão interna estruturada** (não submetido; não peer review)
**Última atualização:** 12 de outubro de 2026

> **Nota:** Estes trabalhos são estudos de ideias desenvolvidos com ferramentas de
> inteligência artificial. O autor é um estudante, entusiasta e pesquisador com um
> brinquedo nas mãos.

**Ferramentas utilizadas:** Gemini MiMo, GPT Copilot, OpenCode

**Autor:** Euzébio Soares dos Santos — estudante, entusiasta e pesquisador
(Contato: euambiente@gmail.com · github.com/ebiossanto)

## Aviso importante

Este repositório contém **notas exploratórias e verificações próprias**, não papers
comprovados. Resultados novos são marcados **(P)** (próprios), **(A)** (fonte/artigo)
ou **(C)** (conjectura) e passam por **referee hostile interno** antes de virarem
estado do projeto. **"RECOMENDADO" = aprovado por rodada interna de crítica
estruturada (logs `*_referee.md`) — NÃO é peer review nem validação da
comunidade.** Os resultados (P) de K, L, M, N são **argumentos próprios
condicionais**; nenhum item aqui é lower bound; a ponte de modelos não-padrão
para consequências de complexidade está **aberta** (ver
`krajicek_ddp/RELATORIO_CONSOLIDADO.md` §9.1 — **três níveis de resultado**).
**Auditoria externa independente pendente** →
`krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md`. **Índice canônico: [`INDICE.md`](INDICE.md).**

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

Verificação própria, com referee hostile **interno** por entrega, sobre
**Krajíček, J., arXiv:2506.20221v4/v5 (LMCS 22(2:14)2026)**: pasta
[`krajicek_ddp/`](krajicek_ddp/) — 14 frentes (A–N) + 3 entregas da terceira
onda (N2, C2, Q2), todas com rodadas internas de crítica processadas.
Resultados principais (todos (P), com logs):

1. **Lacuna verbatim** no passo (5) da prova do Teorema 4 (v4) / Teorema 3 (v5),
   em **ambas** as versões (F1).
2. `Log(M[G]) = Log(M)` no forcing de Kra95/98 — **`(F-b')` refutado** (G1);
   obstrução ZFC à correção via Problema 2.1 (G2).
3. **Teorema K** (J1): coleção interna impossível; `T_PV+BB+(S2)(S3)(S4)` inconsistente.
4. **`T_PV+(S4) ⊢ ∀rφ(r)`** (L1): `¬φ` internamente insatisfatível; **C.3 negativa**.
5. **Canto adversarial** (M): `m` sempre não-padrão (M.0); sem falsificador global
   (M.1); **`C_{N_s} ≡ ⊥` CONDICIONAL** (M.2 — **sob `q` total**; sob `q` parcial
   com merge pode falhar → pergunta **Q1** da carta decide; 2ª fonte de
   não-compactude **se o condicional fechar**).
6. **Redução da refutação interna de `{C_{N_s}}`** (N): existe ⟺ `Taut(α)` tem prova
   EF interna em `M_0` — dicotomia honesta (C1′).
7. **`DD_Res ∈ P`** com refutação pura ≤ |π| (C) — resultado próprio **com
   auditoria externa pendente** (`krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md`
   §A: checklist recorte/DAG/pureza); o núcleo proposicional de `DD_P` é o que
   está formalizado em Lean 4 (o teorema em si é prova escrita).
8. **✅ Nota editorial enviada a Krajíček em 11/10/2026**
   (`krajicek_ddp/CARTA_FINAL_ENVIO.md`; jan.krajicek@protonmail.com) —
   **aguardando resposta**.

Consolidação: `krajicek_ddp/RELATORIO_CONSOLIDADO.md` · contexto:
`krajicek_ddp/CONTEXTO_COMUM.md` · evolução: `EVOLUCAO_PROJETO.md` ·
**avaliação externa de 12/10 + resposta**: `CRITICA_EXTERNA_2026-10-12.md`
(a 1ª: `CRITICA_EXTERNA_2026-10-11.md`).

## Formalização (Lean 4)

**O que está formalizado** (nível proposicional — honestidade de escopo):

- `lean4/Gothic_Generators/DDP.lean` — `DD_P` (totalidade, solubilidade, lema de
  união) — **compila** (2 `sorry`s documentados e permanentes).
- `FoundationBridge/GodelSecond.lean` — rota B (`phiWStarB`); `lake build` verificado
  **verde, 0 `sorry`** (PR27/PR28).

**O que NÃO está formalizado:** p-time, `O(1)` rodadas, p-boundedness, NP≠coNP,
o Problema 2.1, modelos não-padrão, o Teorema 4.3 (`DD_Res ∈ P`) — este é prova
escrita com auditoria externa pendente. O Lean **não** é evidência de
consequências de complexidade.

**Reproduzir a compilação (instalação limpa):** (1) instalar `elan`
(`<https://elan.lean-lang.org>`; no Windows: `winget install elan`); (2) clonar
o repositório; (3) `lake build` na **raiz** — o `lean-toolchain`
(`leanprover/lean4:v4.34.0`) baixa a versão correta sozinho. **Reproduzido em
12/10/2026**: saída `Build completed successfully (4 jobs)` com exatamente 2
warnings de `sorry` (`DDP.lean:628` e `:690`).

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
CRITICA_EXTERNA_2026-10-12.md ← 2ª onda da avaliação externa + ações aplicadas
```

## Próximos passos

1. **Aguardar/registrar a resposta de Krajíček** (perguntas Q1–Q4 da carta) —
   Q1 decide o condicional de M.2 e o escopo de N.
2. **Obter auditoria externa independente** de `DD_Res ∈ P` e das frentes G–N —
   o dossiê está pronto em `krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md`
   (prioridade segundo a avaliação de 12/10; vias em §E; MathOverflow só com
   confirmação do autor).
3. Frente **N3**: construir `(∗′)` por compacidade (canto χ≡⊤); depois
   [K19 5.7] + família alternante (C2) e a fonte Σ₁ (Q2.4).
4. MathOverflow post — **só com confirmação do autor**.

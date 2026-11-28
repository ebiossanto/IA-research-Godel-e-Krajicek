# VARREDURA WEB PROFUNDA — 27/11/2026

**Escopo:** fontes confiáveis e verificáveis apenas (arXiv + API arXiv, OpenAlex, Semantic
Scholar, páginas de autor/periódico, INI Cambridge, talks.cam, websearch). **Fases P1–P7.**
**Caveats de ferramenta:** Semantic Scholar respondeu 429 (rate-limit de IP compartilhado) e o
OpenAlex tem **metadado errado** (o DOI `10.46298/lmcs-22(2:14)2026` está attached ao trabalho
errado `W4386850379`) → contagem de citações do alvo **não obtida** (registrado, não mascarado).

---

## P1 — Nosso artigo-alvo: status primário

- **arXiv:2506.20221** — última versão é **v5 (05/05/2026)**; **publicado**: LMCS 22(2:14),
  06/05/2026 (aceito 17/03/2026; página `lmcs.episciences.org/18158`). **Sem v6, sem corrigenda**
  → nossa análise da lacuna (v4 **e** v5) continua valendo; nenhuma correção do autor.
- **Nenhuma discussão pública da lacuna** encontrada (busca MO/blogs/artigos) → a candidata ①
  (nota de errata) **segue sem duplicata pública**.

## P2 — Prior art do `DD_Res`/FDP (API arXiv: 6 resultados)

| Paper | Status no nosso corpus |
|---|---|
| **Papamakarios, "Feasible disjunction for random resolution"** (arXiv:2609.10602, set/2026) | ✅ **já citado** — `[Pap26]`, `C_disjuncao_viavel.md` (ECCC TR26-154, "verif. integral") — nossa vanguarda confirmada |
| **Krajíček, "Failure of the strong feasible disjunction property"** (arXiv:**2604.04830** v3, 10/2026) | ❌ **NOVO p/ nós** — combina Ilango (2025) + Ren et al. (2025) + gadget generator (K.2007); **condiciona** a remark final do artigo-alvo ("strong FDP falha para strong pps, cf. [12]") |
| Maxa, "Effective Disjunction and Effective Interpolation…" (2601.02821) | ❌ novo (com errata autoral no comentário do arXiv — higiene exemplar) |
| Tabatabai, "Exponential Gaps… Linear Extended Frege" (2609.00422) | ❌ novo — variante de FDP para L-Frege |
| Garlík, "Failure of FDP for k-DNF Resolution…" (2003.10230) | contexto C2/Gar24 já nosso |

> **Ação recomendada (A)-nc:** adicionar `2604.04830` e `2607.13540` (P3) às referências de
> `C_disjuncao_viavel.md`/contexto D **via rodada referee** (não editado aqui de propósito).

## P3 — Preprints 2026 do próprio Krajíček (23 no total; 4 novos p/ nós)

1. **2604.04830** — falha da **FDP forte** (ver P2) — posiciona nosso `DD_Res ∈ P` (FDP **fraca**
   construtiva para Resolução) contra a falha **condicional** da forte.
2. **2607.13540** — "A proof complexity perspective on effectively zero-knowledge proofs"
   (jul/2026): Ilango FOCS 2025 + teoria de geradores — relevante à **frente D (geradores)**.
3. **2606.13367** — "Extended Frege proofs, circuits and rewriting" (v2, out/2026).
4. **2609.35927** — "Pseudo-solutions… AC⁰[p]-Frege lower bound problem" (set/2026) — continuação
   da linha de reduções (contexto C2/L-clb).
- `2303.10637` (JSL 2025) já é **central** no nosso corpus (13 referências) ✓.

## P4 — Posicionamento do D4′ (dimensão fractal de provas)

- Query arXiv (`fractal dimension × proof`, `Higuchi × proof complexity`, `geometry of
  resolution proofs`): **nenhum trabalho aplicado a DAGs de refutação** → **nicho vazio** —
  a originalidade do D4′ permanece.
- **Mas a ponte "dimensão fractal × lógica" existe e DEVE ser citada**: Lutz (point-to-set
  principle), Mayordomo–Nies "Fractal dimensions and profinite groups" (math.LO+math.MG),
  Lutz–Qi–Yu (bases de Hamel via dimensão fractal efetiva). Não citar essa linha = risco de
  "descoberta da roda" no referee.

## P5 — Contexto vivo (o achado estratégico)

**Programa INI Cambridge "Logical foundations of complexity theory" (LFC), 1 set – 18 dez 2026** —
organizado por **Sam Buss e Jan Krajíček** (página oficial newton.ac.uk/event/lfc):
- **Pavel Pudlák** = Rothschild DVF (palestra pública 01/10/2026, "Complexity of computations
  and proofs") — **o autor do candidato A à fonte Σ₁ do nosso Q2.4** (Pudlák §6–§7).
- Workshops: LFCW01 *Frontiers in complexity lower bounds* (set) · LFCW02 *Logical foundations*
  (out; palestrantes: Atserias, **Garlík**, **Jeřábek**, Pudlák, Ren, Thapen, Tzameret…) ·
  **LFCW03 *Bridges between proofs, communication, and computation* (30 nov – 4 dez — começa em
  3 dias)**.
- Grade (talks.cam.ac.uk) — temas batendo nos nossos eixos: **"ETH is False"** (23/11 — o claim
  do openai/math em escrutínio), **"The complexity of Range Avoidance" (Hanlin Ren, 24/11)**
  (= complemento de geradores; Ren é o "Ren et al. 2025" do paper da FDP forte), **"Forcing
  Reading Group"** (Krejčí, Charles U — forcing!), "Recent Progress on Unprovability of
  Complexity Bounds" (Atserias), "Proof Complexity meets Computational Complexity" (09/12),
  "Prospects for mechanising feasible mathematics" (09/12).
- O INI **grava e arquiva** palestras (recordings archive) → recurso verificável futuro.
> **Ações:** (i) audiência certa e **autor acessível** p/ nossa nota de errata ① (Krajíček é
> organizador); (ii) assistir/monitorar LFCW03 (30/11–04/12) e os reading groups; (iii) usar a
> linha de crédito do INI em publicações futuras se derivadas do programa; (iv) range avoidance
> ↔ nossa frente D (geradores) — palestra de Ren é leitura direta.

## P6 — Citações do artigo-alvo

Não obtidas (S2: 429; OpenAlex: DOI com metadado errado). **Pendência:** repetir com chave
OpenAlex própria ou S2 mais tarde; alternativa: Google Scholar manual.

## P7 — Verificação de duplicata do erratum

Busca (MO + blogs + "gap step (5) Log(M"): **nada** — nenhum terceiro reportou a lacuna.
**Nossa candidata ① é a única nota pública conhecida sobre o passo (5).**

---

## Síntese de acções

| # | Ação | Class. | Prioridade |
|---|---|---|---|
| A1 | Referenciar **arXiv:2604.04830** (FDP forte falha) e **2607.13540** (ZK efetiva) no corpus (via referee) | (A)-nc | **ALTA** — prior art direto do `DD_Res`/geradores |
| A2 | Nota de errata ①: reforço — sem duplicata pública, autor acessível via INI | (P) | **ALTA** |
| A3 | D4′: citar a linha **point-to-set/Lutz–Mayordomo–Nies** na futura submissão experimental | (A) | ALTA (evitar "roda") |
| A4 | Monitorar **LFCW03 (30/11–04/12)** + talks do LFC (INI grava) | — | MÉDIA |
| A5 | Ler palestra de **Ren sobre Range Avoidance** ↔ frente D | (A) | MÉDIA |
| A6 | Repetir contagem de citações (chave própria) | — | BAIXA |

*Fontes primárias usadas: arxiv.org/abs/2506.20221 · lmcs.episciences.org/18158 ·
export.arxiv.org/api · api.openalex.org · newton.ac.uk/event/lfc · talks.cam.ac.uk ·
karlin.mff.cuni.cz/~krajicek · websearch (MO/blogs). Todas consultadas em 27/11/2026.*

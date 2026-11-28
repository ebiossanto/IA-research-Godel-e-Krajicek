# VARREDURA github.com/openai/math — 27/11/2026

**Alvo:** `openai/math` (repositório de **estudos matemáticos produzidos por IA** — modelo
interno não-publicado, Apache-2.0; 730 manuscritos / 375 famílias / biblioteca Lean ~42%
formalizado; lançado 06/10/2026) + repositório irmão `openai/ten-proofs` + revisor
independente **MathVet** (mathvet/mathvet).
**Evidências em `openai_math/`:** `README.md`, `CONTENTS.md` (649 KB, mapa de manuscritos),
`lean_formalization.yaml` (catálogo de formalizações), `history.md`, `fidelity-table.csv`
(MathVet, 245 famílias revisadas) + `_extract_fidelity.py`.

---

## 1. Resultado da triagem dirigida aos nossos eixos

**Varredura-chave (2 grep's):** `proof complexity | resolution refutation | bounded
arithmetic | propositional proof | Frege | pigeonhole | refutation | Gödel | Krajíček |
student-teacher | feasible disjunction | MCSP | tautology | Cook-Reckhow | proof length |
cutting planes` → **ZERO ocorrências**.

> **Conclusão negativa honesta:** o repositório **não toca** nosso eixo central (complexidade
> de provas / aritmética limitada / Gödel / `DD_P`). Nada a importar para `krajicek_ddp/`.

## 2. O que É relevante (com classificação do protocolo)

| # | Família / item | Veredito MathVet | Class. | Uso para nós |
|---|---|---|---|---|
| **O1** 🔴 | **#108 "A cubic permanent–determinant lower bound"** — Ω(n³) na complexidade determinantal de borda do permanente sobre ℂ (challenges `PermanentCubic`+`SmoothInitialForm`, 20.739 linhas) | **`full`**, `comparator-sandboxed-pass` | **(A)-nc** (máquina-sim, **sem referee** — MathVet "pre-referee") | **✅ FONTE CONFIRMADA do `L-gct-026` do pequalnp** (registro do lemma + citação literal em arXiv:2610.40484) — ver §4 |
| **O2** 🔴 | **#112 "Beyond the square-root exponent for depth-three circuits"** — linguagem explícita em DPTIME exigindo 2^{ω(√n)} portões em OR–AND–OR | **`full`** (nota: sem expoente fixo n^{1/2+ε}; máquina `FiniteMultiTapeMachine` = definição a conferir) | **(A)-nc** | Lower bound Booleano explícito p/ profundidade 3 — relevante ao eixo de circuitos (padrão que adotamos) e ao muro `L-clb-036` |
| **O3** 🔴 | **#378 "Disproof of the ETH"** — contagem exata de k-CNF em tempo 2^{n/(log n)^{1/2+o(1)}} ⇒ lower bounds superblineares p/ linguagem em **E^NP** (challenge `SubexponentialSAT`, 547k linhas) | **`full`** (mas `machine_check=none` no commit revisado — desafio de 26/10, na fila do MathVet) | **(A)-nc** com auditoria **em curso**: grupo **Impagliazzo–Paturi–Williams** examinando o problema (history.md 26/10) | Contexto p/ nossos condicionais; adjacente a `p_eq_np_search` do pequalnp (algoritmo rápido p/ SAT); **cuidado**: é E^NP, **não** resolve `L-clb-036` (SAT em NP) |
| **O4** 🟡 | **#379 (24/11, NOVA)** — limites exp(c(log N)²/(loglog N)²) p/ circuitos aritméticos do Hamiltoniano direcionado e do permanente (fora car. 2); **VP≠VNP** (state sum n^{Ω((log n)^{1/12})}); expoente de multiplicação = 9/4 com limite n^{9/4}/2; | no `formalization.yaml` (Lean incluído) — **fora da revisão MathVet** (upstream drift) | **(A)-nc** (fidelidade **pendente**) | Atualização do piso de conhecimento em complexidade algébrica — mesma família de alvos do `L-gct-*` do pequalnp |
| **O5** 🟡 | **`openai/ten-proofs` (ago/2026)** — `Permanent.lean`: limites novos p/ permanentes com circuitos/fórmulas aritméticas (fórmula n⁴/log n) + mais 9 provas com **certificado Lean** | certificado por construção | **(A)-nc** | Mesma família do O1/O4; certificate pattern |
| **O6** 🟢 | **Lógica (6 famílias)**: #241 rigidez dos graus de Turing (`full`), #242 representações diofanticas single-fold (`full`), #243 contagem choiceless ≠ P (`full`), #245 normalização de sistemas de tipos (`full`), #240/244 (`partial`) | 4 full / 2 partial | **(A)-nc** | #242 é adjacente a MRDP/H10 (nossa T4 ≡ parada) — leitura opcional; **nada de incompletude/aritmética limitada** |

## 3. Metodologia a copiar (propostas **(P)**)

1. **`Comparator`** (github.com/leanprover/comparator): "challenge file" + solução; o kernel
   Lean verifica contra o enunciado **só com os 3 axiomas padrão**, em sandbox Landlock.
   → Padrão natural para o nosso futuro `CircuitCore`/`DD_Res` formalizado: **arquivo-debate
   + configuração de axiomas** (espelha nosso `gk_dd_cert.py`, que já recusa adulteração).
2. **MathVet (revisão independente de fidelidade)** — **exatamente a pergunta do nosso §A.3**:
   *o enunciado formal diz o que a manchete/prosa afirma?* Vereditos `full/partial/weaker-
   statement/supporting-only/no-Lean`, **protocolo pré-registrado** (amostra de 40 congelada,
   taxa de erro com IC de Wilson, linhas de decisão fixadas: ≤0.10 = "referee-verified";
   ≥0.20 = "first-pass map"), publicado como `formalization-review.yaml` no padrão da Mathlib
   Initiative. → **Modelo para a auditoria externa de `DD_Res ∈ P`**: um "fidelity table"
   linha×linha do dossiê (§A.1–A.5) × prova escrita.
3. **Governança**: 3 manuscritos **retirados** com aviso (erro de sinal), 14 revisados,
   histórico versionado, "raw research data, não artigos" + crédito deferido à comunidade —
   espelho do nosso protocolo de retrações (D1–D6) + `claims_lint`.
4. **Transparência de processo**: 10 resumos de raciocínio, compute (~3h ChatGPT Pro por
   resultado), ~4.000 problemas tentados — análogo ao nosso registro de rodadas/sessões.

## 4. Fechamento do loop com o pequalnp (o achado mais valioso) — ✅ CONFIRMADO em 27/11

O `plan.json` do pequalnp diz, no alvo GCT (`L-gct-026`): *"a cubic bound that **unrefereed
2026 reports** claim; this project has not verified it and has no proof route"*.

**Cadeia de confirmação (3 elos, todos com fonte primária):**
1. **Registro público do lemma** (`data/lemma/L-gct-026.d43713ec6215.json`, salvo em
   `pequalnp/lemma_L-gct-026.json`): *"Source: **the manuscript of 24 September 2026 cited by
   arXiv:2610.40484**. The manuscript states c = 5529600e and m at least 1408."*
2. **arXiv:2610.40484** (K. Sheshadri, 29/10/2026, "Cubic lower bounds for the permanent in
   odd characteristic…", submetido à IMRN; HTML salvo em `openai_math/arxiv_2610.40484.html`)
   — abstract: *"Over the complex numbers, the best known lower bound grows cubically"*;
   **referência literal**: *"OpenAI. A cubic lower bound for border determinantal complexity
   of the permanent. Preprint, 24 September 2026.
   `github.com/openai/math/blob/fd4aeeb2…/preprints/A-cubic-lower-bound…`"*
3. ⇒ **Fonte = `openai/math` família #108** (preprint de 24/09/2026 — data exata), veredito
   MathVet **`full`**, challenge `PermanentCubic` aceito pelo Comparator (20.739 linhas).

- Classificação atualizada: **(A)-nc nomeada** (máquina-sim, sem referee — como o nosso
  próprio dossiê) em vez de "unrefereed 2026 reports" anônimo. A rota `letters` não foi
  necessária (o registro público deles já declarava a fonte).
- Nota de rigor: constantes divergem (`5529600e` no manuscrito × `8.8·10⁶e` em Sheshadri —
  o dele é pior, provavelmente p/ sua redução `k=⌊n/11⌋`); `m ≥ 1408` confere nos dois.
- Efeito: o hard link `L-gct-026` agora tem **fonte rastreável** — e `openai/math #108` ganha
  um *citação de terceiro* (Sheshadri) além do certificado de máquina.

## 5. O que NÃO encontramos (para não prometer)

- Sem proof complexity / aritmética limitada / Gödel / MCSP / student-teacher (2 varreduras).
- Sem nada sobre ponte L2→L3 ou `DD_Res` — nosso eixo segue **exclusivamente nosso**.
- Contagens do repositório mudam por sessão (722→730 manuscritos); sempre citar o commit.

## 6. Ações desta varredura

1. Evidências salvas em `openai_math/` (inclui `fidelity-table.csv` do MathVet).
2. **`pequalnp/PEQUALNP_MAPA.md` §7**: linha nova — fonte candidata do `L-gct-026` (O1).
3. `INDICE.md`: esta varredura indexada (Estudos de Fontes Externas).
4. **Não** adotamos nada no código — propostas O1–O6 são (A)-nc/((P)) e ficam como leitura.

**Monitoramento futuro (opcional):** `history.md` do openai/math (mudanças) + changelog do
MathVet (`upstream-drift/`) — o MathVet já assiste o upstream à noite; citar o review deles
evita re-fazer a leitura de fidelidade.

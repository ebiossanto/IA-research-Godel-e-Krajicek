# CONTRIBUIÇÕES DO PROJETO — Gödel · Krajíček · Sistemas Complexos

**Data:** 19/11/2026 · **Autor:** Euzebio Soares (ebiossanto) · **Status:**
síntese das descobertas e contribuições do projeto para as áreas estudadas.
**Documento vivo** — atualizar a cada nova entrega.

> **Taxonomia (AGENTS.md §2):** **(A)** = literatura · **(P)** = próprio ·
> **(C)** = conjectura/programa · **retr** = retraído.
> **"RECOMENDADO" = aprovado em rodadas internas de crítica estruturada
> (referee hostile; logs `*_referee.md`) — NÃO é peer review nem validação
> da comunidade.** Nenhum item deste documento é lower bound; nenhuma
> afirmação de `P≠NP`/`NP≠coNP`; a ponte L2→L3 está **aberta**
> (`krajicek_ddp/RELATORIO_CONSOLIDADO.md` §9.1). Auditoria externa pendente:
> `krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md`.

**Índice canônico:** [`INDICE.md`](INDICE.md) · **histórico:**
[`EVOLUCAO_PROJETO.md`](EVOLUCAO_PROJETO.md) · **plano:**
[`PLANO_PESQUISA_E_DESENVOLVIMENTO.md`](PLANO_PESQUISA_E_DESENVOLVIMENTO.md)

---

## 1. Complexidade de provas (campo central)

| # | Contribuição | Tipo | Estado |
|---|---|---|---|
| 1.1 | **`DD_Res ∈ P` com refutação pura ≤ \|π\|** — algoritmo construtivo que devolve um lado tautológico com **FDP ótima `p(t)=t`** para Resolução; lemas de recorte + pureza autocontidos (3000/3000 exp.) | **(P)** | RECOMENDADO — **auditoria externa pendente** |
| 1.2 | **Lacuna *verbatim*** na prova do Teorema 4 (v4) / Teorema 3 (v5) de Krajíček, arXiv:2506.20221 — confirmada em **ambas** as versões (LMCS 22(2:14)) | **(P)** | Enviada ao autor; **resposta parcial recebida 12/10/2026** |
| 1.3 | **Texto exato de `Res(k)` recuperado** (Garlík CCC 2024 §2 ↔ [K19] ch5.7 ↔ Kra01 Def 1.1) + **correção de atribuição** ("Lema 4.1" é nosso, não de Krajíček) | **(A)+(P)** | Feito (19/11) — destravou a frente C2 |
| 1.4 | **Contraexemplo à projeção por subconjunto** sob a promessa fraca de C2.2 (15 linhas, verificado por máquina): bloqueio real de **retenção parcial** de blocos — candidato anterior **retraído** | **(P)** | r2 RECOMENDADO |
| 1.5 | **Teorema Nec**: família alternante + π polinomial + lado difícil para `Res(k)` ⟹ **π necessariamente impuro** → via LP do reductio **retraída** | **(P)** | 19/11 — retração honesta |
| 1.6 | **Ponte prova→fractal (D4′)**: D_H de Higuchi **separa** séries reais de comprimentos de prova por **regime de crescimento** (exponencial vs quase-linear; 4/4 IC95 exclui 0, robusto a log1p) — e **refutou** a leitura "prova dura = mais fractal" | **(P)+(C)** | N1+N2, referee r1 — primeira medição fractal de refutações `Res(k)`/τ reais |
| 1.7 | **Primeiras refutações reais da família `τ(g)ᵦ` medidas** (DRAT via Cadical195) | **(P)** | N2 (19/11) |
| 1.8 | **`Log(M[G]) = Log(M)`** no forcing de Kra95/98 → **`(F-b')` refutado**; errata 9.4.2; **obstrução ZFC** (`T_PV`+falsificador+`(F-sent)` é falso → correção `2.1→(F-sent)` é alvo de reductio) | **(P)** | RECOMENDADO |

---

## 2. Aritmética limitada / prova de teorias

| # | Contribuição | Tipo | Estado |
|---|---|---|---|
| 2.1 | **Teorema K**: coleção interna impossível; `T_PV+BB+(S2)(S3)(S4)` **inconsistente** | **(P)** | RECOMENDADO |
| 2.2 | **`T_PV+(S4) ⊢ ∀rφ(r)`** — `¬φ` internamente insatisfatível; **C.3 negativa incondicional** | **(P)** | RECOMENDADO |
| 2.3 | **K-FP′**: ponto fixo padrão existe; `(Hjoint)` falsa em todo modelo | **(P)** | RECOMENDADO |
| 2.4 | **Canto adversarial M.0–M.5**: `m` sempre não-padrão; **`C_{N_s} ≡ ⊥`** (condicional a `q` total — **Q1 respondido pelo autor**: `i₀` = comprimento ∈ `Log(M')` → leitura (A)) | **(P)** | RECOMENDADO + autoridade do autor |
| 2.5 | **Refutação interna de `{C_{N_s}}` reduzida a `EF ⊢ Taut(α)`**; dicotomia honesta (C1′) | **(P)** | RECOMENDADO |
| 2.6 | **Fonte Σ₁ para limites inferiores** — candidatas **A** = `Con_T(f(n))` (Pudlák ch.VIII **Thm 6.2.3**/§7.2.2: hierarquia de velocidade real) e **B** = `i-RFN` ∀Σ^b_i (**KP90** Lemma 1.3/Thm 5.1 — texto integral obtido do autor) | **(A)+(C)** | Varredura executada (19/11); pendências A1/A2/A5 |
| 2.7 | **Três correções aos enunciados** do artigo-alvo (nº de rodadas; classe Σ₂ᵖ; totalidade sem BB) | **(P)** | Verificado |

---

## 3. Hierarquias de reflexão / slow consistency (linha Beklemishev–Freund–Pakhomov)

| # | Contribuição | Tipo | Estado |
|---|---|---|---|
| 3.1 | **Framework do Espectro de Reflexão**: déficit de cobertura **δ**, ganho **𝒢** (telescoping `δ_{T₀}−δ_{T_m}=Σ𝒢`), rank **ρ_b**, transição de ramo **RBT** — nível intermediário observável entre inclusão de teorias e PPR de geradores | **(P)** | Núcleo do Eixo 1; **δ/RBT = candidatos a novidade** (busca inicial; profundização pendente) |
| 3.2 | **Monotonicidade** `δ_S ≤ δ_T` (T⊆S) · **Lema 3** `Φ_T^{w*} ↔ Con(T)` · **Teorema 4** reflexão dá `δ_T=1→δ_T'=0` (ganho unitário) | **(P)** | Provados; Lema 3 e Teo. 4 **formalizados em Lean (0 sorry)** |
| 3.3 | **RCS** (separação slow vs fast com Φ fixa): confirmada e **robusta 4/4** (κ, razão, \|W\|) — primeiro observável que separa progressões lentas/rápidas; **ponte empírica** slow consistency ↔ geradores | **(C)→N2** | Verificado no modelo finito (Caixa PPR) |
| 3.4 | **Obstrução estrutural**: `min_lex` **não preserva redução** → o salto `T≼_int S ⟹ g_T≼_ppr g_S` é bloqueado — explica por que o programa PPR precisa de δ | **(P)** | Provado (Fase 3/4) |
| 3.5 | Posicionamento de **ρ_b vs Pakhomov–Walsh** (reflection rank ordinal): **distintos** (nós = primeiro nível com δ=0) | **(A)/(P)** | Busca inicial |

---

## 4. Interpretabilidade vs. geradores (programa `g_T` de Krajíček)

| # | Contribuição | Tipo | Estado |
|---|---|---|---|
| 4.1 | **≼_ppr formalizado** com τ-fórmulas corrigidas; **pré-ordem** (Lemas 7.1–7.2); **transferência de hardness** (Prop 8.1/Cor 8.2) | **(P)** | Provados |
| 4.2 | **Q2.1 decidido**: instância *full-range* é **inócua** — moral: `(τ,q)` é só metade da hipótese; a outra é a fonte | **(P)** | RECOMENDADO |
| 4.3 | Instância `(Q)\|_{Σ₁}` com `τ_n` total e cutoff de testemunha corrigida | **(P)** | RECOMENDADO (Q2.2) |

---

## 5. Resultados negativos e retrações (contribuições de delimitação)

1. **Retrações transparentes da tese inicial** (D1–D6: barreira de
   interpretabilidade, escala exponencial `s_P≥2^{c|T_α|n}`, T\*, observação
   b(n)) — banners + motivações preservados (`INDICE.md` §DESCARTADOS).
2. **Via LP do reductio fechada** (19/11): candidato `(γ, REF_t)` **não
   alterna** para t poli (0/92 γ-insat; só o lado SAT) + **Teorema Nec**.
3. **SemΣ₁ "pronta"** na literatura para o transfer (Q2.4): a hierarquia de
   velocidade dá famílias **Π₁-ish** (`Con_T`), não Σ₁ com testemunhas
   curtas — fronteira precisa do que falta (candidatas A/B em §2.6).
4. **Contagem ≠ lower bound** (D4) e **prova ingênua rejeitada** — lições
   incorporadas ao método.
5. **Contraexemplo à promessa fraca de C2.2** (§1.4) — fecha o caminho
   "ingênuo" da projeção.

---

## 6. Metodologia (contribuição transversal)

1. **Triangulação obrigatória**: Simbólico (Z3/SymPy) → Numérico
   (Julia/Python) → Formal (Lean 4); **validação sintética obrigatória** antes
   de medir (pegou5 bugs no encoder de19/11; fronteira exata REF_5/REF_6).
2. **Taxonomia (A)/(P)/(C) + referee hostile por entrega + níveis
   Ten-Proofs N0–N4** (não executado = `pending`) — ~15 rodadas internas,
   várias produzindo **contraexemplos e teoremas** em vez de "✓" prematuros.
3. **Formalização Lean com escopo honesto**: núcleo proposicional provado
   (`delta_mono`, `theorem4_strict`, `rcs_exists`, `lemma3_con` — verificado
   por `#print axioms`, sem `sorryAx`); **nunca** reivindicado como prova de
   p-time/NP≠coNP; 2 `sorry`s permanentes documentados em `DDP.lean`.
4. **Engagement científico real**: carta com errata a **Jan Krajíček** →
   **resposta do autor** (Q1 fechado);2 avaliações externas respondidas
   ponto-a-ponto; pacote de auditoria pronto.
5. **Retrações como resultado de primeira classe** — o que não funciona fica
   documentado e fechado, não escondido.

---

## 7. Fronteira — o que **NÃO** é claim

- **Nenhum** lower bound; **nenhuma** afirmação de `P≠NP`/`NP≠coNP`;
  ponte **L2→L3 aberta**.
- PPR/RBT/RCS = programa experimental **no modelo finito escolhido**
  (não evidência para geradores de provas reais).
- `DD_Res∈P`, Teorema K, L.1, M.2 etc. = argumentos **próprios
  condicionais**, RECOMENDADO (interno) — **auditoria externa = próximo
  passo de credibilidade**.
- Resultados D1–D6 do Eixo 1 permanecem **retraídos**.
- MathOverflow: rascunho **não publicado** sem confirmação do autor.

---

## 8. Maior alavanca de valor (hoje)

> **Externa:** (i) auditoria de `DD_Res∈P` + frentes G–N (dossiê pronto);
> (ii) follow-up Q2–Q4 a Krajíček (janela de 2–4 semanas vencida há 5+).
> É o que transforma "RECOMENDADO" em credibilidade de campo — e é o
> horizonte **H0/H1** do `PLANO_PESQUISA_E_DESENVOLVIMENTO.md`.

---

*Documento vivo — atualizar a cada nova entrega. Gerado em19/11/2026 a partir
de `INDICE.md` v6.24, `EVOLUCAO_PROJETO.md` (Fases1–13.8) e os relatórios de
referee das frentes C2/DD_P/Frontier.*

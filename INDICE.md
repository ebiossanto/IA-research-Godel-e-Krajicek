# Indice da Pesquisa Gödel–Krajíček

**Versão:** 6.15 (Setembro 2026 — PR27 Q + Gödel II rota A + bridge δ + MO)
**Status:** Teorema Q condicional em Core; wStarObl/δ≥1; Φw*:=T.consistent; rascunho MO (não postado)

---

## Estrutura dos Documentos

### NÚCLEO ATUAL (começar por aqui)

| Arquivo | Conteúdo | Status |
|---------|----------|--------|
| `EVOLUCAO_PROJETO.md` | **HISTÓRICO VIVO** | **ATUALIZAR A CADA PASSO** |
| `09_EVOLUCAO_PERFIL_REFLEXAO_GERADORES.md` | **NÚCLEO: g^{a,b}, δ, 𝒢, ρ_b, RBT + §35–40** | **ATIVO** |
| `08_PROGRAMA_INTERPRETABILIDADE_VS_GERADORES.md` | PPR, ≼_ppr, R1/R2, R3 aberto | ATIVO |
| `10_EXPERIMENTO_GERADORES_FINITOS.md` | RBT=SIM, suffix0 (depois: vácuo) | EXECUTADO |
| `11_PPR3_THETA_SUFFIX0.md` | suffix0 VÁCUO; CC-Θ aberta | EXECUTADO |
| `12_NOTA_CURTA_POSICIONAMENTO_DELTA_RBT.md` | δ/RBT vs Pudlák/Krajíček; ρ_b vs P–W | NOTA |
| **`13_EXPERIMENTO_SLOW_VS_FAST_DELTA.md`** | **RCS CONFIRMADA** | **EXECUTADO** |
| **`14_R_RAMOS_RBT_PPR.md`** | **R_w design + testado (PPR-2)** | **TESTADO** |
| **`15_FORMALIZACAO_LEAN_PR15.md`** | **Lean VERIFICADO (lake build limpo); lemma3=teorema (interface)** | **ATIVO** |
| **`16_EXTENSAO_EXPERIMENTO13_RCS.md`** | **RCS ROBUSTA 4/4** | **EXECUTADO** |
| **`17_R_RAMOS_PPR2_TESTE.md`** | **PPR-2 refinado 3/3 (cond. C)** | **EXECUTADO** |
| **`18_R_W_E0_E3_PPR2.md`** | **R_w PPR-2 em E0–E3: 4/4 PASSA** | **EXECUTADO** |
| **`19_PPR3_THETA_RAMOS.md`** | **Θ ramos: CC-Θ 32/32, polinomial** | **EXECUTADO** |
| **`23_COND_B_RBT_EXPLICITO.md`** | **cond. (B) NÃO-VÁCIA: 10 disparos, PPR-2 20/20, CC-Θ 20/20** | **EXECUTADO** |
| **`24_FOUNDATION_LEMMA3_ALLCOV.md`** | **lemma3 PROVADO; (C) ALL_COV ⇔ δ=0 (limiar maxκ)** | **EXECUTADO** |
| **`25_FOUNDATION_INSTANCE_FP_DELTA.md`** | **Foundation instância Lemma3Hyp; PR7 comprimento vs δ SIM (modelo)** | **EXECUTADO** |
| **`26_REVISAO_EXTERNA_PONTUAL.md`** | **Revisão externa: só banners/orig./esqueleto — sem redesenhar programa** | **EXECUTADO** |
| **`27_TEOREMA_Q_GODEL2_BRIDGE_MO.md`** | **PR27: Q condicional; bridge δ; Gödel II rota A; agenda antes de LB** | **EXECUTADO** |
| **`27_MATHOVERFLOW_PERGUNTA.md`** | **Rascunho MO (EN) — NÃO publicado sem confirmação** | **RASCUNHO** |
| `00/02/04/05`, `support/*`, `paper2` | **PR26: REJEITADO + novidade provisória + pseudocódigo** | **CORRIGIDO** |
| `01/06/03` | **PR12: banners REJEITADO/histórico** | **CORRIGIDO** |
| Scripts | exp10, ppr3, reimpl, slow_vs_fast, **_ext**, test_Rw, **_E0E3**, **ppr3_ramos**, **_RBT_B**, **_allcov**, **fp_length_vs_delta** | SCRIPTS |
| `lean4/Gothic_Generators/Core.lean` | **VERIFICADO `lake build` (0 sorry, 0 axiom; lemma3=teorema)**; Lean 4.34.0 | **OK** |
| `lean4/Gothic_Generators/FoundationInstance.lean` | **moved → `FoundationBridge/`** | **OK** |
| **`FoundationBridge/`** | **instância Foundation isolada; 0 sorry no fonte; `GodelSecond` rota A** | **OK (build Mathlib pendente)** |
| `lean-toolchain`, `lakefile.toml` | Toolchain Lean 4.34 + Lake | **OK** |

### Papers e Conjecturas

| Arquivo | Conteúdo | Status |
|---------|----------|--------|
| `papers/paper1_barreira_interpretabilidade.md` | "Barateando a Diagonalização" | Nota exploratória |
| `papers/paper2_hierarquia_ordinal.md` | Hierarquia ordinal e consistência lenta | Nota exploratória |
| `CONJECTURA_FP_K.md` | FP-K | **PERGUNTA DE PESQUISA** (rebaixada; ver 09 §18 para versão δ) |
| `07_pontos_fixos_incompletude.md` | Parte 2: pontos fixos, física | Teoremas+analogias+conjecturas separados |
| `CONTINUIDADE_PESQUISA.md` | Documento de continuidade | Atualizado |

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
| **T9** | **Prop. 1 (09): \|g_T^{a,b}(u)\|=\|u\|+1** | **PROVADO** | **Novo, elementar** |
| **T10** | **Teo. 2 (09): δ_S ≤ δ_T se T⊆S** | **PROVADO** | **Novo, elementar** |
| **T11** | **Telescoping (09 §10): δ_{T_0}−δ_{T_m}=Σ𝒢** | **PROVADO** | **Novo, elementar** |
| **T12** | **Lema 3 (09): Φ_T^{w*}↔Con(T)** | **PROVADO** | **Novo, sob formalização** |
| **T13** | **Teo. 4 (09): δ_T=1, δ_{T'}=0** | **PROVADO** | **Novo, sob hipóteses** |
| **T14** | **08 Lemas 7.1-7.2: ≼_ppr é pré-ordem** | **PROVADO** | **Novo, elementar** |
| **T15** | **08 Prop 8.1/Cor 8.2: transferência de hardness** | **PROVADO** | **Novo, elementar** |

### CONJECTURAS / PERGUNTAS (não provadas)

| # | Item | Status | Documento |
|---|------|--------|-----------|
| P1 | **FP-K**: análogo Freund–Pakhomov para g_T | **PERGUNTA DE PESQUISA** (rebaixada, originalidade não certificada) | `CONJECTURA_FP_K.md` |
| C2 | Censura cósmica exclui estruturas Malament–Hogarth | CONJECTURA ABERTA | `07_...` |
| C3 | Física necessariamente codifica aritmética | ESPECULATIVA | `07_...` |
| C4 | Teorema da Incompletude Cosmológica | ESPECULATIVA | `07_...` |

### PROGRAMA ATIVO (pós-auditoria + núcleo 09)

| # | Problema | Status | Documento |
|---|----------|--------|-----------|
| **PR0** | **Espectro de Reflexão: δ, 𝒢, ρ_b, RBT** | **NÚCLEO — Teo. 2, Lema 3, Teo. 4 PROVADOS** | `09_...` |
| **PR1** | **g_PA ≼_ppr g_{PA+RFN(PA)}?** (PPR-Reflection-1) | **ABERTO** — R1/R2 provados, R3 aberto | `08_...` §17, §25 |
| PR2 | Conjectura PPR-Reflection: g_{T_k} ≼_ppr g_{T_{k+1}} | CONJECTURA (nova no projeto) | `08_...` §26 |
| PR3 | Conjectura de quebra: ∃k tal que g_{T_k} ⋠_ppr g_{T_{k+1}} | CONJECTURA alternativa | `08_...` §27 |
| PR4 | Hipótese RCS: α ↦ δ_{T_α}(Φ,b) contém info não ordinal? | HIPÓTESE falsificável | `09_...` §28 |
| PR5 | ρ_b: independente de codificação? | ABERTO | `09_...` §32 |
| PR6 | Transferência: δ_S ≤ δ_T ⟹? g_T ≼_ppr g_S | ABERTO | `09_...` §23 |
| PR7 | Freund–Pakhomov: Con*(PA) aparece em δ? | **PERGUNTA GERADA** (varredura) | `10_...` §1.4 |
| PR8 | δ/RBT: prioridade vs. Pudlák/Krajíček | **NOTA 12: busca inicial NÃO**; profundizar | `12_...` |
| PR9 | PPR-3: Θ para `suffix0` | **FALHOU: suffix0 vácuo** — abandonado | `11_...` §4.3 |
| PR10 | R não-vácuo (índices w ou códigos π) | **ABERTO** | `11_...` §7 |
| PR11 | CC-Θ: Θ polinomial | **ABERTO** | `11_...` §3.3 |
| PR12 | Aplicar correções 01/06/03 (09 §33) | **APLICADAS** (PR12) | `01/06/03` |
| PR13 | Plano 09 §35: prova formal Φ_PA↔Con(PA) | **ABERTO** (plano) | `09_...` §35 |
| PR14 | Iteração 09 §36: mesma Φ em T_0,T_1,... | **ABERTO** (plano) | `09_...` §36 |
| PR15 | Formalização Lean Lema 3+Teo 4+RCS | **ESQUELETO** (sorry) | `15_...` |
| PR16 | Estender 13 (κ, razão, \|W\|) | **FEITO — RCS ROBUSTA 4/4** | `16_...` |
| PR17 | Testar R_w (índices) PPR-2 | **FEITO — PPR-2 3/3 (cond. A∨B∨C)** | `14_...`, `17_...` |
| PR18 | Fechar sorry delta_mono em Lean | **FEITO — prova completa (sem sorry)** | `Core.lean` |
| PR19 | PPR-3: Θ sobre provas de ramos | **FEITO — CC-Θ 32/32, polinomial** | `19_...` |
| PR20 | Testar R_w nos cenários E0–E3 (RCS) | **FEITO — 4/4 PASSA PPR-2** | `18_...` |
| PR21 | Fechar sorries theorem4/rcs em Lean | **FEITO — provas completas sem sorry** (lake build pendente) | `Core.lean`, `15_...` |

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
| D8 | "g_T hard para sistemas que interpretam T" | **NÃO AFIRMADO** por Krajíček — hardness universal é aberta |

---

## Varredura Bibliográfica (22/09/2026) — resumo

| Conceito nosso | Encontrado? | Posicionamento |
|----------------|-------------|----------------|
| δ (déficit de cobertura) | **NÃO** (busca inicial) | Candidato a novidade; profundizar |
| RBT (transição de ramo) | **NÃO** (busca inicial) | Nome proposto; candidato |
| ρ_b (rank de cobertura) | **PRÓXIMO: Pakhomov–Walsh reflection rank** | DISTINTO: eles=ordinal; nós=δ=0 |
| g^{a,b} (dois orçamentos) | **NÃO explícito** em Krajíček | Refinamento; verificar livro 2025 |

---

## Experimento 10 — Resultados (22/09/2026)

| Pergunta | Resultado |
|----------|-----------|
| δ diminui T₀→T₁? | **SIM** (𝒢=4, b≥20) |
| RBT ocorre? | **SIM** (5/9 b: `0000→ALL_COV`) |
| Candidato R? | ~~`suffix0`~~ **VÁCUO/abandonado** (11 §4.3) |
| δ decresce com b? | **SIM** [16,16,16,5,4,4,4,4,4] |
| Teo. 4 (δ₀=1,δ₁=0)? | **Parcial** (δ₀=4, δ₁=0, b≥20) |

## Reimplementação (busca real, resolução) — 22/09/2026

| Verificação | Resultado |
|-------------|-----------|
| δ_T0, δ_T1, G | 4, 0, **4** (estável) |
| RBT | **SIM** |
| Con T0 / Con T1 | False / True ✓ |
| Natureza | **proposicional** (não PA aritmética) |

## Experimento 13 — Slow vs Fast (RCS) — 22/09/2026

| Verificação | Resultado |
|-------------|-----------|
| Mesma Φ, hierarquias lenta/rápida | **SIM** |
| ∃α,b: δ_F ≠ δ_S | **SIM** — 3–4/30 pares (α=1, b≥3) |
| **RCS** | **CONFIRMADA no modelo** |

## PR16 — Extensão RCS (robustez) — 22/09/2026

| Config | Pares δ_F≠δ_S | RCS |
|--------|---------------|-----|
| E0 base | 4/42 | **SIM** |
| E1 κ rich | 7/42 | **SIM** |
| E2 3:1 | 4/42 | **SIM** |
| E3 \|W\|=64 | 4/42 | **SIM** |

**Veredito: RCS ROBUSTA 4/4.**

---

## Pergunta de Pesquisa Principal (núcleo 09)

**ANTECESSORES (superados/rebaixados):**
> ~~Ordinal ⟹ escala exponencial~~ → REJEITADO (auditoria)
> ~~Conjectura FP-K como "nova"~~ → REBAIXADA (originalidade não certificada)
> ~~PPR-Reflection-1 como única saída~~ → bloqueio estrutural identificado (min_lex)

**NÚCLEO ATUAL — Espectro de Reflexão:**

Como evolui o déficit de cobertura diagonal

$$\delta_{T_\alpha}(\Phi,b)$$

ao longo de uma hierarquia de reflexão $T_0 \subseteq T_1 \subseteq \cdots$?

**O que já é PROVADO (09):**
- δ é monotônico (Teo. 2)
- 𝒢 ≥ 0 e telescopa (§10)
- Φ_T^{w*} ↔ Con(T) (Lema 3)
- Reflexão dá δ_T=1 → δ_{T'}=0 (Teorema 4)
- Ganho unitário 𝒢=1 (corolário)

**O que está ABERTO:**
- g_PA ≼_ppr g_{PA+RFN(PA)}? (R3)
- Hipótese RCS (informação além do ordinal?)
- ρ_b independente de codificação?
- Transferência δ ⟹ PPR?

**Documentos:** 09 (núcleo), 08 (PPR), 10–26 (exp+**RCS**+Lean+**Foundation**+**FP-δ**+**revisão externa**), 01/06/03/00/02/04/05 **corrigidos**, EVOLUCAO

**Próximo passo:** Φw* Gödel II; bridge δ; teorema de transferência Q (antes de limite inferior); MathOverflow como pergunta

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

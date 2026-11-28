# Indice da Pesquisa Gödel–Krajíček

**Versão:** 6.45 (28/11/2026 — **séries em b EXECUTADO** (`35_SERIES_EM_B.md`
+ referee R1 com4 condições de redação): **H_b1 CONFIRMADA 16/32 σ's
utilizáveis** · **H_b2 CONFIRMADA (OK): média D = −0,243 [percentil
−0,365; −0,109], BCa concordante, dirn=−1, n=16, MDE 0,183** —
**minref(lex b) é ANTI-PERSISTENTE para σ fixo** (14/16 σ's no sinal;
outlier σ=6027 +0,45 registrado; leave-one-out fortalece) · **escopo
obrigatório na claim: σ's sem instância minref≥8 (16/32)** · direção −1
baseada em sonda única (caveat) · **H_b3 = candidata (C)** (minref
alterna −0,23 vs drat persistente +0,80 — sem verbo confirmatório) ·
ASSERT **0/904** · crash0xC0000005 contido por checkpoint (507→904) ·
**varredura pequalnp da sessão executada** (`pequalnp/VARREDURA_
2026-11-28.md`: checked +5.872, proof_complexity +219,24 artigos);
v6.44: séries em b pré-registrado; …)
**Status:** ✅ **Carta ENVIADA 11/10/2026 18:14 → RESPOSTA PARCIAL RECEBIDA 12/10/2026
(Q1 respondido; Q2–Q4 pendentes — follow-up devido; `CARTA_FINAL_RECEBIDA.md`)**;
Teorema K, K-FP′, `¬φ` insatisfatível, `C_{N_s}≡⊥` **(condicional a `q` total —
Q1 respondido → leitura (A), interpretação (P) no dossiê)**;
`DD_Res ∈ P` **(auditoria externa pendente)**; Teorema Q condicional
em Core; rascunho MO (não postado)

> **Terminologia (fixada em 12/10/2026 — ver `CRITICA_EXTERNA_2026-10-12.md`):**
> **"RECOMENDADO (rn)" = aprovado em `n` rodadas internas de crítica estruturada
> (referee hostile interno; logs `*_referee.md`) — NÃO é peer review nem
> validação da comunidade.** Os itens (P) de K/L/M/N são argumentos próprios
> **condicionais**; a ponte modelos não-padrão → complexidade (L2→L3) está
> **aberta** (`krajicek_ddp/RELATORIO_CONSOLIDADO.md` §9.1). PPR/RBT/RCS =
> programa experimental **no modelo finito escolhido**. Auditoria externa
> pendente: `krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md`.

---

## Estrutura dos Documentos

### NÚCLEO ATUAL (começar por aqui)

| Arquivo | Conteúdo | Status |
|---------|----------|--------|
| `CONTRIBUICOES_DO_PROJETO.md` | **SÍNTESE das descobertas/contribuições por área** (complexidade de provas, aritmética limitada, reflexão/slow, geradores, negativas, metodologia) + fronteira de claims | **ATIVO — começar por aqui (visão externa)** |
| **`FERRAMENTAS.md` + `ferramentas/`** | **Catálogo das ferramentas executáveis** (minref, dd-cert, claims-lint, proof-fractal, alternating-family, c2-sim) — cada uma como extensão do projeto, com README, arcabouço matemático, aplicações, uso e citação | **ATIVO** |
| `PLANO_PESQUISA_E_DESENVOLVIMENTO.md` | **PLANO-MESTRE: desenvolvimento + questões respondidas/a responder + P&D priorizado** (19/11/2026) | **ATIVO — começar por aqui** |
| `AMBIENTE_E_FERRAMENTAS.md` | **Estado das ferramentas/permissões + incidente sympy + reidratação** (19/11/2026) | **ATIVO** |
| `diagnostico_ambiente.ps1` | Script ✅/❌ de verificação do ambiente (`-Build` inclui `lake build`) | SCRIPT |
| **`gk_claims_lint.py` + `.github/workflows/ci.yml`** | **Sistema imunológico**: lint de claims (10 regras: retrações, status obsoletos, disclaimer, links, sha256, lean JSON, DESCARTADOS, indexação) + **CI** (lint · `lake build` · smoke do simulador C2) | **ATIVO — rodar a cada entrega** |
| **`gk_prosa_lean_lint.py`** | **Leitura adversarial prosa×Lean** (modelo red team pequalnp): P1 refs de `sorry` × warning real do Lean · P2 contagem · **P3 tokens + P3b diff dos 3 quotes A.1 + P3c fragmento F1 × 3 transcrições** · P4 reprodução `3000/3000` (`--replay`: + 5 taxas + médias) · P5/P6 guardas §9.1 · **P7 manifesto de 15 entradas (§B + E + Q2.4)** · **P8 rodadas §D.2** · **P9 cross-refs do §9.2 (4 condicionais τ_N + terminologia)** · **P10 fonte primária arXiv v4+v5 (lacuna nas duas; Thm 4→3)**. r1–r5: ver `PROSA_VS_LEAN_r*_referee.md` | **ATIVO — NO CI ao lado do `claims_lint`** (job `claims-lint`, sem `--replay`) |
| **`gk_minref.py` (+ `gk_minref_referee.md`, `gk_minref_results.*`)** | **Comprimento MÍNIMO exato de refutação** via REF_t (fecho + pares completos); validação (units=3, ABC=5, sat=∞); benchmark17/17 exatos `{7:6,9:4,11:1,5:2}`; **6º bug (sobreposição)** encontrado; **T1 do teste LP verificado92/92** | **ATIVO — RECOMENDADO r1** |
| **`gk_dd_cert.py` (+ teste/referee/demo)** | **EXTRATOR DE CERTIFICADOS DD** — Teorema 4.3 executável: saturação/DAG/**DRAT→DAG** (UP com rastreio) → certificado da sub-derivação pura + **verificador independente** (recusa adulteração); motor Res(k) com **detecção automática de violação (G1)**; teste7/7 no CI | **ATIVO — RECOMENDADO r1 · peça da auditoria externa** |
| `EVOLUCAO_PROJETO.md` | **HISTÓRICO VIVO** | **ATUALIZAR A CADA PASSO** |
| `ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md` | Estado honesto (Level 0→4) + descobertas possíveis D1–D6 (13/10) + gaps | ATIVO (indexado em 19/11 pelo claims-lint) |
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
| **`27_TEOREMA_Q_GODEL2_BRIDGE_MO.md`** | **PR27: Q condicional; bridge δ; Gödel II rota A; FoundationBridge BUILD VERDE (0 sorry)** | **EXECUTADO** |
| **`27_MATHOVERFLOW_PERGUNTA.md`** | **Rascunho MO (EN) — NÃO publicado sem confirmação** | **RASCUNHO** |
| **`28_PONTE_PROVA_FRACTAL_D4.md`** (+ `_referee.md`) | **D4′ v1: ponte prova→fractal — 188 UNSAT reais (Cadical195 DRAT + Z3); D_H separa `php` (4/4 IC95 exclui0, raw+log1p) = regime de crescimento; refutada leitura "dura=mais fractal"; H_C2 deferido** | **EXECUTADO — RECOMENDADO r1** |
| **`29_PONTE_PROVA_FRACTAL_D4V2.md`** (+ `_referee.md`) | **D4′ v2+r2: comprimentos MÍNIMOS canônicos (minref) vs DRAT pareado, famílias n≤6 (controle do regime), 12 testes a priori — H_C3/H_C4 sem separação; r2: BCa+TOST+MDE80 → equivalência ±0,20=6/6 (±0,10 inacessível, MDE≈0,19), exclusão r1 → INCOERENTE, BCa não resolve saturação (8/81), pista boxdim 2/3; 7º/8º bugs (tau invertido; seed não-determinístico)** | **EXECUTADO (2 rodadas) — RECOMENDADO r2** |
| **`30_PONTE_PROVA_FRACTAL_D4V3.md`** (+ `_referee.md`) | **D4′ v3/r3: boxdim PRÉ-REGISTRADO (commit `66f40ae` anterior ao run) em 192 instâncias novas disjuntas do r2 — H_B3 pista A4 CONFIRMADA (Δ=−0,170, Bonferroni ✓); H_B1 padrão-τ PARCIAL 2/3 (τ separa, (b) Bonferroni; imp−cadeia não separa, eq±0,05 não certificável → sensibilidade 0,08✓); H_B2 1/2 (1 incoerente); H_B4 refutada (incoerência é do par, não da métrica — higuchi 0/27 aqui); delete-d vs delete-1 0/135; tipo-I 0,04; poder 9/10; bug de filtragem pós-run corrigido sem tocar pré-registro** | **EXECUTADO — RECOMENDADO r3** |
| **`31_PONTE_PROVA_FRACTAL_D4V4.md`** (+ `_referee.md`) | **D4′ v4/r4: n=384/família (1152 instâncias disjuntas r2+r3; crash nativo CaDiCaL ×2 → checkpoint+retry `3d244ab`, 3 processos, plumbing separado do pré-registro `9fe7165`) — H_C2 `saltos` CONFIRMADA 3/3 Bonferroni (âncoras r3±0,012, z0 saudável); H_C1 boxdim INDETERMINADO (2/6 contáveis, 4 incoerentes — régua exaustiva A3; (a) efeito≈0 sinal invertido; (d)(f) dois métodos excluem mas ponto fora → indiciação); H_C3 mecanismo z0 MEDIDO (D1 94%, D2 CONFIRMADA, incoerência 7%→33% com n → BCa+bloco fixo inadequado p/ n grande); D4 revertido; H_C4 NAO_ATINGIDO 4/6; delete-d 0/135; discordância pct-vs-BCa 39%** | **EXECUTADO — RECOMENDADO r4** |
| **`32_PONTE_PROVA_FRACTAL_D4V5.md`** (+ `_referee.md`) | **D4′ v5/r5: `saltos` PRIMÁRIO — H_D1 CONFIRMADA 3/3 Bonferroni (3ª rodada: r3→r4→r5, magnitude 0,08–0,19, ICs sobrepostos); método de IC novo SELECIONADO PELA CALIBRAÇÃO (percentil+estratificado: tipo-I 0,075 vs BCa 0,325; S4–S6 pré-run) — H_D3 incidência real 4,4% (r4:33%), z0 extremos 61→12, degenerados 16→2, head-to-head bloco8 4/9 bloqueado vs primário 0/9; H_D2 PARCIAL 5/6 (eq±0,05 certificada, pista (d) e fonte (f) limpas pela 1ª vez, (a) sem efeito 3ª vez); H_D4 ATINGIDO 6/6 (MDE 0,014–0,052); regra 2 níveis (ramo concordante 0 ocorrências); 2 bugs de plumbing pós-pré-reg + smoke test; n=512 disjunto r2–r4** | **EXECUTADO — RECOMENDADO r5** |
| **`33_PONTE_PROVA_FRACTAL_D4V6.md`** (+ `_referee.md`) | **D4′ v6/r6 CONSOLIDAÇÃO: estratos EXATOS do `relinc` (transformação recalculada por réplica) — H_E1 PARCIAL (5/45→2/45, todos os5 originais resolvidos) + H_F3 CONFIRMADA (1/45 em dado novo); H_F1 saltos **CONFIRMADA 3/3 na4ª rodada** com (b) salvo pelo ramo concordante **pela1ª vez em dado real** (flag visível) + H_F1b Cochran Q **SEM HETEROGENEIDADE** (p=0,13–0,71, sem tendência em4 rodadas); H_F2 boxdim **CONFIRMADA 6/6** (5/6 teriam sido bloqueados pelo método r4); H_F4 DISPAROU 4× (ramo mantido); H_F5 **6/6** (MDE 0,014–0,042); z0 extremos 12→28 (monitoramento); S7 smoke em toda execução; n=512 disjunto r2–r5** | **EXECUTADO — RECOMENDADO r6** |
| **`34_TAU_KUP_MINREF.md`** (+ `_referee.md`) | **τ k↑ (pendência original do D4′): `minref_deep` estende o minref para n>6** (pools de profundidade `d≤t`, pares deduplicados, propriedade17/17) — **EXECUTADO (396/396,26/11)**: **H_t1 CONFIRMADA 118/132 = 89,4%** (n=7 exato dentro de max_aux=6M) · **H_t2 REFUTADA (0/2) pela regra — leitura obrigatória dupla: contrastes INCONCLUSIVOS (MDE 0,53/0,59; censura 0/11/58%; peso em k3−k2 = −0,243 [−0,606,+0,135])** · **ASSERT 0/396** · médias minref **planas** 6,95/6,71/6,82 vs **drat crescente** 8,74/10,18/11,31 → **lacuna1,79→3,47→4,49 = (P) descritivo, candidata (C) não-claim** · fronteira %exato 100/89/42 · erratum anotação pré-reg ("96/16-32"→396/132) · patch `saturation` mid-run invariante (3 camadas) · CSV sha `f5d51c57…` | **EXECUTADO — R1 aprovado com4 condições de redação** |
| **`35_SERIES_EM_B.md`** (+ `_referee.md`) | **séries em b (índice lex de b para σ fixo — a série ordinal do D4′, docs 28 §7.3 / 29 §3 "com minref") — EXECUTADO (904/904,27/11):** gerador `gen_tau_at_b` (namespace `tau_b`, DISJ) · grade k=2,w=5 (n=7, T=28-30) × σ 6000..6031 (S=32), max_aux=6M · **H_b1 CONFIRMADA (16/32 σ's utilizáveis)** · **H_b2 CONFIRMADA: média D=acf₁(real)−média₁₀₀₀ acf₁(permutações) = −0,243 [−0,365;−0,109] percentil, BCa [−0,354;−0,095] concordante, dirn=−1, n=16, MDE 0,183, z0 0,05 — minref(lex b) ANTI-PERSISTENTE (14/16 σ's no sinal)** · **3 condições do referee: escopo "σ's sem minref≥8" na claim + caveat direção (sonda única) + nota de poder/outlier** · H_b3 **candidata (C)**: D_minref −0,23 vs D_drat **+0,80** (polaridades opostas; sem verbo confirmatório) · ASSERT 0/904 · S3 pego degeneração `saltos`→acf₁ pré-commit · crash0xC0000005 contido (507→904) · CSV sha `50ecd215…` | **EXECUTADO — R1 aprovado com4 condições de redação** |
| `00/02/04/05`, `support/*`, `paper2` | **PR26: REJEITADO + novidade provisória + pseudocódigo** | **CORRIGIDO** |
| `01/06/03` | **PR12: banners REJEITADO/histórico** | **CORRIGIDO** |
| Scripts | exp10, ppr3, reimpl, slow_vs_fast, **_ext**, test_Rw, **_E0E3**, **ppr3_ramos**, **_RBT_B**, **_allcov**, **fp_length_vs_delta** | SCRIPTS |
| `lean4/Gothic_Generators/Core.lean` | **VERIFICADO `lake build` (0 sorry, 0 axiom; lemma3=teorema)**; Lean 4.34.0 | **OK** |
| `lean4/Gothic_Generators/FoundationInstance.lean` | **moved → `FoundationBridge/`** | **OK** |
| **`FoundationBridge/`** | **instância Foundation isolada; 0 sorry no fonte; `GodelSecond` rota A** | **OK (build Mathlib pendente)** |
| `lean-toolchain`, `lakefile.toml` | Toolchain Lean 4.34 + Lake | **OK** |

### CAMPANHA DD_P (Krajíček 2025, arXiv:2506.20221) — pasta `krajicek_ddp/`

| Arquivo | Conteúdo | Status |
|---------|----------|--------|
| **`krajicek_ddp/RELATORIO_CONSOLIDADO.md`** | **Consolidação de TUDO (rodadas A–M)** | **ATIVO** |
| `krajicek_ddp/CONTEXTO_COMUM.md` | Contexto centralizado (estado das frentes 11/10) | **ATIVO** |
| `krajicek_ddp/A_teoremas_exatos.md` | Teoremas exatos do artigo (L21–22, L190/375, L341, L442, L513–518) | VERIFICADO |
| `krajicek_ddp/B_lean_relatorio.md` + `lean4/Gothic_Generators/DDP.lean` | `DD_P` em Lean 4 — **compila** (2 `sorry`s permanentes) | **OK** |
| `krajicek_ddp/C_disjuncao_viavel.md` | **`DD_Res ∈ P`** + refutação pura ≤ \|π\|; 3000/3000 exp. | **RECOMENDADO** |
| `krajicek_ddp/D_geradores_consequencias.md` | NW/[8] reconstruído; `(K)⟹(ST)`; Lema 2 | VERIFICADO |
| `krajicek_ddp/E_ataque_problema21.md` | Decomposição E1–E5 do passo (5); ponto frágil | VERIFICADO |
| `krajicek_ddp/F1_verificacao_passo7.md` | **Lacuna verbatim em v4 e v5/LMCS** (referee 10/10) | **RECOMENDADO** |
| `krajicek_ddp/F2_versao_finita.md` / `F3_...` | Lema de suficiência finita; obstáculos O1–O8 | RECOMENDADO |
| `krajicek_ddp/G1_log_forcing.md` | **`Log(M[G])=Log(M)`**; **`(F-b')` refutado** (Thm 4.3) | RECOMENDADO |
| `krajicek_ddp/G2_semente_Fsent.md` | **Obstrução ZFC** (Thm 2.1); correção `2.1→(F-sent)` | RECOMENDADO |
| `krajicek_ddp/H1_colecao_refutacao.md` | **Thm 1.1 "no-G"**; redução (A)/(B) | RECOMENDADO |
| `krajicek_ddp/I1_Qcompactness_ultrapoderes.md` | Ultrapoderes fora de `S`; B.1 (nenhuma instância padrão); venue `M_0⊨S` viva | **RECOMENDADO (v5)** |
| `krajicek_ddp/J1_Qcompactness_M0.md` | **Teorema K**; K.2 (`T_PV+BB+(S2)(S3)(S4)` inconsistente); `(Hjoint)`; J.6 | **RECOMENDADO (v4)** |
| `krajicek_ddp/J2_ponto_fixo.md` | **K-FP′**; J.6-a′; semântica `τ_N` aberta | **RECOMENDADO (v3)** |
| `krajicek_ddp/L1_phi_insatisfativel.md` | **L.1** (`T_PV+(S4)⊢∀rφ(r)`); **L.3′** (C.3 negativa); L.3a; L.4 | **RECOMENDADO (v4)** |
| `krajicek_ddp/M_canto_adversarial.md` | **M.0–M.5**: `m` não-padrão; **`C_{N_s}≡⊥`** — adversarial `(C)` decidido | **RECOMENDADO (v4)** |
| `krajicek_ddp/N1_refutacao_interna_CN_s.md` | **N.1**: refutação interna de `{C_{N_s}}` ⟺ `EF⊢Taut(α)` interna; N.2 dicotomia (C1′); N.3 R-α/R-β | **RECOMENDADO (v3)** |
| **`krajicek_ddp/NOTA_EDITORIAL_Krajicek.md`** | **Nota a Krajíček (errata + dicotomia + perguntas + carta EN)** | **RASCUNHO — aguardando autor** |
| `krajicek_ddp/*_referee.md` | Referees hostile preservados (F–N, NOTA, L1, J1, J2, I1, H1, G2) | AUDIT |
| **`krajicek_ddp/PROSA_VS_LEAN_piloto_referee.md`** | **Piloto prosa×Lean sobre §9.1 + dossiê `DD_Res ∈ P`**: 9 achados (F1–F9) — `sorry` 628:8/690:8 = warning real do Lean ✓ · Lean não contém Teorema 4.3 ✓ · **`3000/3000` reproduzido byte a byte** ✓ · 3 omissões do rótulo "verbatim" **CORRIGIDAS** em §A.1 · nota de custo `O(\|Π\|²+\|Π\|·m)` adicionada à fonte §2.3 · guardas P5/P6 da regra §9.1 verdes | **EXECUTADO — RECOMENDADO r1** |
| **`krajicek_ddp/PROSA_VS_LEAN_r2_frentes_G-N_referee.md`** | **r2 sobre as 13 frentes (§B)**: R2-1 linha **H1** com cross-ref desatualizado (§1.3 ≠ "convenção de abertas") **CORRIGIDA** · R2-2 ponteiro v5 adicionado à linha F1 · R2-3 "(N1 §0.3)" · rodadas §D.2 5/5/3/2 confirmadas (4/4) · G1/G2/I1/J1/J2/L1/M/N2/C2/Q2 marcadores confirmados · **P7+P8 codificados; r2 limpo → PROMOVIDO AO CI** | **EXECUTADO — RECOMENDADO r2** |
| **`krajicek_ddp/PROSA_VS_LEAN_r3_p3b_E_Q24_referee.md`** | **r3**: **P3b diff normalizado completo** dos 3 quotes A.1 × fonte (sanidade do extrator auto-testada: 385/332/425 chars, iguais) **fecha a objeção R3 de r1** · P7 → **15 entradas** (+E `E1–E5`/`passo (5)`/`frágil`; +Q2.4 `Pudlák`/`i-RFN`/`K19`/`(C)` + referee obrigatório) · **P4 --replay confere 5 taxas + médias** (fecha R4) · **r3 limpo, exit 0** | **EXECUTADO — RECOMENDADO r3** |
| **`krajicek_ddp/PROSA_VS_LEAN_r4_fonte_primaria_referee.md`** | **r4 com FONTE PRIMÁRIA**: HTML do arXiv v5 baixado (`fontes/arxiv_2506.20221v5.html`, 158.449 bytes, sha256 `E7282222…FC49`) → o artigo escreve **`i_o` (letra `o`)** na lacuna → transcrição de `A_teoremas_exatos.md` **CORRIGIDA com nota *sic*** · linha F1 confirmada contra a v5 (Theorem 3, eqs (7)/(8), lacuna presente) → nota no §B · cross-ref §9.2 "`§7.6`" (inexistente) → **§7 item 6** · **P3c (fragmento × 3 fontes) + P9 (4 condicionais τ_N + 3 terminologias) codificados; r4 limpo, exit 0** | **EXECUTADO — RECOMENDADO r4** |
| **`krajicek_ddp/PROSA_VS_LEAN_r5_arxiv_v4_referee.md`** | **r5 fecha B1**: HTML da **v4** salvo (`fontes/arxiv_2506.20221v4.html`, sha256 `C1781BE1…C63E`) → **lacuna presente nas DUAS versões** (texto idêntico `But by (7) io… already in M*`) · `Theorem 4` só na v4 × `Theorem 3` só na v5 = **renumeração confirmada com fonte primária** · coluna "O que o auditor checa" da linha F1 virou **RESPONDIDO** · **P10 codificado (normalização sem espaços p/ dupla renderização MathML); r5 limpo, P1–P10 exit 0** | **EXECUTADO — RECOMENDADO r5** |
| **`krajicek_ddp/NOVAS_REFERENCIAS_2026_referee.md`** | **A1 (da varredura web)**: +4 referências — `[Kra26-fdp]` arXiv:2604.04830 (Krajíček, *Failure of the strong FDP*, out/2026) e `[RWZ26]` Ren–Wang–Zhong ITCS 2026 em `C_disjuncao` §9; `[Kra26-zk]` arXiv:2607.13540 (ZK efetiva) e `[RWZ26]` em `D_geradores` §8 — **corpos intocados**; verificação por varredura do HTML (`_verify_refs.py`): **nenhum dos dois cita `DD_P`/2506.20221 nem discute Resolução/enfraquecimento** → escopo do Lema 4.1 segue sem cobertura (prior-art via `letters` pendente, §A.3) | **EXECUTADO — RECOMENDADO r1** |

### Papers e Conjecturas

| Arquivo | Conteúdo | Status |
|---------|----------|--------|
| `papers/paper1_barreira_interpretabilidade.md` | "Barateando a Diagonalização" | Nota exploratória |
| `papers/paper2_hierarquia_ordinal.md` | Hierarquia ordinal e consistência lenta | Nota exploratória |
| `CONJECTURA_FP_K.md` | FP-K | **PERGUNTA DE PESQUISA** (rebaixada; ver 09 §18 para versão δ) |
| `07_pontos_fixos_incompletude.md` | Parte 2: pontos fixos, física | Teoremas+analogias+conjecturas separados |
| `CONTINUIDADE_PESQUISA.md` | Documento de continuidade | Atualizado |

### Estudos de Fontes Externas

| Arquivo | Conteúdo | Status |
|---------|----------|--------|
| **`pequalnp/MAPEAMENTO_DDP_vs_PEqualNP.md`** (+ `_referee.md`) | Site **pequalnp.com** (fleet de agentes atacando P vs NP, lemmas verificados em Lean 4): snapshot `overview.json`/`plan.json` (sha256 no doc) + clone `open-goat/pequalnp-proofs@89a01cd` (Apache-2.0) em `pequalnp/`; mapeamento `Defs/{CircuitLowerBounds,MetaComplexity,ProofComplexity}` × `lean4/Gothic_Generators/DDP.lean`; **DECISÃO (P): modelo de circuito deles (`GateOp`/`Gate`/`Circuit`/`FanInTwo`/`HasCircuitSize`) adotado como PADRÃO de circuito do projeto**, com vendorização testada sem Mathlib (`_r4_test_circuitcore.lean`, `lake env lean` EXIT=0 em v4.34.0, adaptação `Set`→disjunção); **`DDP.lean` intocado** (2 `sorry`s preservados); cross-checks minref×`IsRefutation` propostos como **(C)** | **EXECUTADO — RECOMENDADO r1** |
| **`pequalnp/PEQUALNP_MAPA.md`** (+ `extract_ids.py`, `papers.json`) | **MAPA DE IDs** L-pcx/L-clb/L-meta/L-lib/L-alg extraídos dos 3 snapshots (regenerável por script): 21 L-pcx (Res(+) bit-PHP etc.), 2 L-clb, cadeia partial-MCSP, 10 rows do Note 1 com run-IDs, linhas de ataque vivas/mortas e registros negativos (`L-alg-004` refutado por "regra adivinhadora" = caso de teste p/ `gk_dd_cert.py`) — **cada linha classificada (A)/(A)-nc/(C)** com notação documentada (§1); conexões com nossos eixos em §6; **§7 = deltas da varredura 27/11** | **EXECUTADO — RECOMENDADO r1** (†rows de `attack.rows`: status individual PENDENTE no ledger) |
| **`pequalnp/VARREDURA_2026-11-27.md`** (+ `_varredura_diff.py`, `_news_letters.py`, snapshots `*_novo.json`, artigos A-054/A-056) | **Varredura diária 26→27/11**: deltas por programa (+399 meta checked), `L-clb-036`→conjecture, `proof-complexity`→support (**`L-pcx-203/204`**), **`L-pcx-205` novo (anel ≤48n+1 linhas)**, `clean-ands` morto (L-meta-25474), `candidate-family` = first line (201 portões), **plan_v2** (BET/RULED_OUT/DECISIONS/WOULD_CHANGE), **letters LT-003 replied** (|E\|+τ−1), custos exatos novos em modelo **one-a-side** (≠ Note 1), relançamento "open lab", **sem Note 2**; 7 itens usáveis U1–U7 | **EXECUTADO — RECOMENDADO r1** |
| **`pequalnp/VARREDURA_2026-11-28.md`** (+ diffs `overview`/`news` sobre `daily/2026-11-28_*`) | **Varredura 27→28/11 (rotina AGENTS §4 executada na sessão)**: contadores **checked 18.710 (+5.872)**, **refuted +4.477 > conjecture +3.761** (frota absorvendo backlog) · **meta_complexity +5.003 checked/+4.475 refuted**, **proof_complexity +219 checked/+9 retired** (eixo minref em movimento) · **linhas de ataque SEM MUDANÇA** (diff exaustivo 33 linhas) · **24 artigos novos** (A-067…A-075, A-084…A-098) — destaques **(A)-nc**: A-084/A-089 (proof_complexity — paridade/red-mismatch, o mais próximo de minref), A-074/075 (13 impossibilidades + 493 grafos em Lean), **A-085** (201→6 portões com NOT — mesmo motivo da família τ), A-067/068 (lower bounds de anel) · letras/plan_v2/papers **inalterados** (sem Note 2) · **limitação registrada:** script imprimiu só8/24 artigos (corte `[:8]`) — **CORRIGIDO** (`diff_news` completa, teste offline24/24) | **EXECUTADO — ROTINA DIÁRIA** |
| **`motor_fractal_rea/`** (+ zip gitignorado na raiz) | **Extração documental da vertente FCT/REA** (`github.com/ebiossanto/Motor-Fractal-REA`, snapshot06/11; mesma árvore `formal-certification/` + skill ten-proofs do workspace IA-RESEARCH): **`RELATORIO_FINAL_INTEGRACAO.md`** = refutação do paper ponte original em **5 erros** (4/24≠1/12; **E_dyn\*=0 p/ m≥2 — teorema de bipartido**; P₉₉ incompatível com M/M/1; regime instável; oráculo inválido) + **Teorema de Rigidez Dinâmica** (força bruta) + correção wavelet H 0,7041→0,5967 · `FCT_REFINAMENTO_PREDITIVO.md` (4 eixos + correções de4 papers + PFA) · `RELATORIO_INTEGRACAO_TEN_PROOFS.md` (N0–N2 ✔, N3/N4 pendentes) · `validation_report.json` (H=0,7686; **espectro violado** β>γ honesto) · **`cpu_timeseries.csv` (301 pts) = dado do item D3 pendente** · classificação: refutações+rigidez = **(P) da vertente**, fórmulas = (A)-nc · **segurança:** `.github_token.txt` (PAT) extraído **NUNCA versionado aqui**; removido do repo público (`Motor-Fractal-REA` `ad22a35`,404 confirmado) — **rotação do PAT pendente com o autor** | **EXECUTADO — extração + indexação** |
| **`lab_sistemas_complexos/`** + `docs/` +5 na raiz | **Migração do ancestral** `-Laboratorio-Sistemas-Complexos` (privado, HEAD15/10 = doador do ONDE_ESTAMOS;281 arquivos →182 idênticos/30 pré-referee descartados/38 falsos-únicos/**31 únicos,25 migrados**): **raiz** ← `gk_hardness_separation_real.*` (**artefatos PPR-3 §2.2 que faltavam**: s_Res=21,2/s_EFrege=17,0) + `entropy_calc.py`/`collect_and_plot.py` (ferramentas do **D6**) · **`docs/`** (13) = **única documentação do toolchain FCT** (Z3/CVC5/Julia/LTspice/FreeFEM/SageMath/GeoGebra + guias; suporte H2.13/P₉₉; ver `docs/PROVENIENCIA.md`) · **`lab_sistemas_complexos/`** (13) = doc-mestre + launchers + **`rea_bridge.ps1/bat`** (série longa do **D3**) + saída `sistema_complexo_entropia.csv` · segredo varrido = limpo | **EXECUTADO — migração com proveniência** |
| **`transicao_dupla/`** | **Extração do repo público `transicao-dupla-krajicek`** (15/10,6 commits; vertente FCT — nome "krajicek" é branding, **nada de DD_P**): **T1** (break-even único `ρ*` + meia-mitigação `ρ_{1/2}=4√ρ*`), **LB1** (piso de garantia), **LB2** (bullwhip `∏≥1+Σ` → ≥ linear) + **TGH** (2 docs: transição global em cascatas heterogêneas, log/AM-GM/limiares globais, **caveat de novidade honesto**) + dinâmica estocástica + `docs/`8 · **§7 non-claims** = disciplina idêntica à nossa (nenhum LB de complexidade; L2→L3 aberta) · **impacto: corrige o D1** — `ρ_c=0,25` = **`ρ_{1/2}`** (meia-mitigação, Modelo A q=1/2) e piso LB1, **não** break-even (esse `ρ*=0,0625`); D1 reescrito com os dois alvos empíricos · **3 flags:** Lean **não compila** (Mathlib3/`eq_unique` — não é N2); artefatos sympy **ausentes** no repo (checagem não reprodutível); formalization.md incompleto · classificação: T1/LB/TGH = **(P) condicionais a (A)**, novidade TGH = **(C)** | **EXECUTADO — extração + D1 corrigido** |
| **`espectro_limiares/`** | **Extração da linha irmã `IA-RESEARCH-Logica`** (público,26/09–01/10; **não referenciada no INDICE até agora** — lacuna fechada): **espectro de limiares dos geradores de Krajíček** (`ρ_T,B_T,C_T,R_T,g_T^[b]`) — verificação exaustiva **no repo-fonte** (**410.155 perfis,7.737.331 pares — TODOS OS TESTES PASSARAM**) · extraídos: **`04_CONTINUIDADE.md`** = **Tabela1 normativa de notação** (`ρ_b`≠`ρ_T` sufixos obrigatórios; `g^{a,b}`⊃`g_T^[b]`; `RBT/PPR` vs `R_T` só com revisão de `09_EVOLUCAO`) + **Lema3↔gadget** (`lemma3_con` Lean-provado = instância α=⊤ do padding; mesmo esqueleto `α^w`/`Prf` → **material reaproveitável**) + **convergência do problema aberto** (mãe ↔ ECCC TR23-030 ↔ Etapa15 → citar a mesma formulação) · `STATUS_MAPA_ESPECTRO` (estado por resultado: `ρ` **limiar exato** = fortalecimento vs fonte; `M_T` novo; ponte `C_T→ω` **não existe**; lei de crescimento = clássico Gödel1936; achados A1–A44) + `01_NUCLEO_DURO` · **fora:** `paper/main.pdf` (18pp — candidato H3) e `verifica_espectro.py` (N2) por URL · classificação: núcleo+`ρ`+`M_T` = **(P) verificado**, Q3/Conj-F = **(C)** condicionado, níveis A–D ≠ N0–N4 (**mapeamento pendente**) | **EXECUTADO — extração + ponte de notação** |
| **`pequalnp/varredura.py`** (+ `last_state.json`, `daily/`) | **ROTINA AGENDADA (AGENTS.md §4)**: rodar `python pequalnp/varredura.py` **no início de cada sessão** — baixa `head.json`, diff contra última execução, baixa só o que mudou p/ `daily/`, imprime deltas/alertas (**novo paper**, plan_v2, letters replied) com integridade (hash embutido no nome). Testada: baseline + "sem mudanças" (exit 0) | **ATIVO — ROTINA POR SESSÃO** |
| **`openai_math/VARREDURA_2026-11-27.md`** (+ `README/CONTENTS/formalization.yaml/history`, `fidelity-table.csv` do MathVet) | **Varredura de `github.com/openai/math`** (730 manuscritos gerados por IA + Lean): triagem dirigida = **ZERO** proof complexity/aritmética limitada/Gödel/Krajíček (nosso eixo segue exclusivo) · relevantes: **#108 claim cúbico perm-det = FONTE CONFIRMADA do `L-gct-026`** (registro do lemma declara "manuscript of 24 Sep 2026 cited by arXiv:2610.40484" → citação literal aponta p/ `openai/math` #108; MathVet `full`, Comparator) · #112 depth-3 2^{ω(√n)} · #378 **ETH falso** (grupo Impagliazzo–Paturi–Williams examinando; E^NP, não resolve `L-clb-036`) · #379 (24/11) VP≠VNP+Hamiltoniano aritmético (fidelidade pendente) · `ten-proofs` Permanent.lean · **metodologia a copiar**: Comparator (challenge+3 axiomas) e **MathVet fidelity table/protocolo pré-registrado** = modelo p/ auditoria `DD_Res` (§A.3) · evidências: `lemma_L-gct-026.json`, `arxiv_2610.40484.html` | **EXECUTADO — RECOMENDADO r1 (loop confirmado r2)** |
| **`varredura_web/VARREDURA_WEB_2026-11-27.md`** | **Varredura web profunda (fontes primárias, fases P1–P7)**: alvo = **v5 última, LMCS publicado 06/05/2026, sem corrigenda, sem discussão pública da lacuna** (erratum ① segue único) · prior art FDP: **`arXiv:2604.04830` Krajíček "Failure of the strong FDP" (out/2026) = NOVO p/ nós** + `2607.13540` ZK efetiva + `2606.13367`/`2609.35927` (Pap26 já nosso ✓) · D4′: nicho "fractal de provas" **vazio**, mas citar linha **point-to-set/Lutz–Mayordomo–Nies** · **INI Cambridge LFC (set–dez/2026, Buss+Krajíček organizando; Pudlák DVF; LFCW03 30/11–04/12; talks "ETH is False", Range Avoidance/Ren, Forcing RG)** = audiência/autor p/ erratum e contexto vivo · caveats: S2 429 + OpenAlex com DOI mal-attached (citações pendentes) | **EXECUTADO — RECOMENDADO r1** |

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
| `goedel_complexity_paper_pnp.md` | **DESCARTADO** (Teorema 1 inválido) |
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
| **DD1** | **Campanha DD_P: teoremas exatos (A)** | **FEITO** — 3 correções aos enunciados | `krajicek_ddp/A_...` |
| **DD2** | **`DD_Res ∈ P` + refutação pura (C)** | **FEITO — RECOMENDADO** | `krajicek_ddp/C_...` |
| **DD3** | **Lacuna do Problema 2.1 (F1)** | **FEITO — verbatim em v4 e v5; referee 10/10** | `krajicek_ddp/F1_...` |
| **DD4** | **Obstrução ZFC + correção (G1/G2)** | **FEITO — `Log(M[G])=Log(M)`; `(F-b')` refutado; `2.1→(F-sent)`** | `krajicek_ddp/G1/G2` |
| **DD5** | **Teorema K + K-FP′ (J1/J2)** | **FEITO — coleção impossível; ponto fixo padrão** | `krajicek_ddp/J1/J2` |
| **DD6** | **`¬φ` insatisfatível + C.3 negativa (L)** | **FEITO — `T_PV+(S4)⊢∀rφ(r)`** | `krajicek_ddp/L1_...` |
| **DD7** | **Canto adversarial `(C)` (M)** | **FEITO CONDICIONAL — `C_{N_s}≡⊥` sob `q` total; sob `q` parcial com merge pode falhar → Q1 da carta decide** | `krajicek_ddp/M_...` |
| **DD8** | **Nota editorial a Krajíček** | **✅ ENVIADA 11/10/2026 18:14** (protonmail + karlin); **📨 RESPOSTA PARCIAL 12/10/2026 14:48 UTC** — **Q1 respondido** (`i₀` = comprimento de elemento de `M'` ∈ `Log(M')` → leitura (A)); **Q2–Q4 pendentes** (follow-up devido) | `krajicek_ddp/CARTA_FINAL_ENVIO.md`, **`CARTA_FINAL_RECEBIDA.md`** |
| **DD9** | **Refutação interna de `{C_{N_s}}` (N)** | **FEITO — reduzida a `EF⊢Taut(α)` (N.1); dicotomia (C1′)** | `krajicek_ddp/N1_...` |
| **DD10** | **Residuais R-α/R-β (N2)** | **FEITO (RECOMENDADO r5)** — R-α=(∗′) com 4 formas da ameaça **(C)**→N3; N2.3′ no escopo efetivo; R-β: compressão necessária≠suficiente; **N3 rodada2 (20/11): movimento (ii) EXECUTADO** — H-separ mecanismo **(P) executável**, acoplamento C2 desacoplado, lema de constantes (P), regressão commitada; lift §2.4 + Q4 seguem (C)/(H) | `krajicek_ddp/N2_residuals_RA_RB.md`, **`krajicek_ddp/N3_construction_compactness_chi_top.md` §7** (+`N3_rodada2_referee.md`, `n3_hsepar_*`) |
| **DD11** | **`DD_{Res(k)}` (C2)** | **PARCIAL (RECOMENDADO r5)** — C2.1 **teorema**; **r1:** regras exatas [K19 5.7] (A) + "Lema 4.1"=nosso; **r2: contraexemplo (G1)** (candidato retraído) → **C2.2′ teorema (P) linha-puro**; **r3/LP: critério DECIDIDO — via LP RETRAÍDA** (candidato `(γ,REF_t)` não alterna p/ t poli + **Nec**); **C2.2 = única via (C)** | `krajicek_ddp/C2_r2_G1_contraexemplo.md`, **`krajicek_ddp/C2_LP_familia_alternante.md`** (+referees), `gk_alternating_family.py`, `gk_c2_projection_sim.py` |
| **DD12** | **Instâncias `(τ_n,q)` (Q2)** | **FEITO (RECOMENDADO r3)**; **fonte Σ₁ varrida 19/11 (C→candidata)**: A=`Con_T(f(n))` (Pudlák §6–§7) · B=`i-RFN(G_i)` (KP90); K19 caps.9/17=setup/FI; pendências A1/A2/A5 | `krajicek_ddp/Q2_instancias_tau_n_q.md`, **`krajicek_ddp/Q2.4_fonte_SIGMA1_K19_KP90.md`** (+referee) |
| **DD13** | **Avaliação externa 2ª onda + resposta** | **APLICADA (P1–P5, P10)** — terminologia de status; M.2 condicional; build reproduzido; PPR reclassificado; três níveis L1/L2/L3 | `CRITICA_EXTERNA_2026-10-12.md` |
| **DD14** | **Pacote de auditoria externa (G–N + `DD_Res`)** | **PRONTO** — checklist (a)–(e) do T4.3; tabela G–N com o que checar; §C não-reivindicado; §E vias (MO congelado) | `krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md` |

### 

## Dados Frontier (13/10/2026)

Artefatos gerados por python gk_frontier_integration.py:
- gk_F1_analytic.csv, gk_F1_rho_c_sweep.csv — varredura ρ_c(r)=(1−r)^4
- gk_F2_nonabelian_filters.csv, gk_F2_summary.csv — filtros Donoho/EMA, separação H
- gk_F3_tau_real.csv, gk_F3_tau_real.json — 4 configs Z3, H=0.297 estável
- gk_F4_telemetry_real_filtered.csv, gk_F4_telemetry_result.json — telemetria real n=300
- gk_F5_d4_reframe.json — H vs fração-small, decoupled (ρ=0.016, p=0.78)
- gk_frontier_resultados.json — relatório mestre

Consulte DESCOBERTAS_FRONTIER_2026-10-13.md para análise completa.

DESCARTADOS / REJEITADOS (não usar)

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

**Documentos:** 09 (núcleo), 08 (PPR), 10–26 (exp+**RCS**+Lean+**Foundation**+**FP-δ**+**revisão externa**), 01/06/03/00/02/04/05 **corrigidos**, EVOLUCAO, **`krajicek_ddp/` (campanha DD_P — consolidado em `RELATORIO_CONSOLIDADO.md`)**

**Próximo passo:** ~~enviar a nota editorial~~ **✅ FEITO (11/10 18:14)** ·
~~aguardar a resposta~~ **✅ RESPOSTA PARCIAL 12/10/2026 — Q1 respondido**
(`i₀` ∈ `Log(M')`; leitura (A); `CARTA_FINAL_RECEBIDA.md`); **Q2–Q4 pendentes →
follow-up curto devido** (recomendação de 2–4 semanas já vencida); em paralelo: Φw* rota B
(definability); (τ_n,q) concretas para Q (antes de limite inferior); MathOverflow
como pergunta

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
11. **Krajíček, J. (2026).** "On NP∩coNP proof complexity generators." arXiv:2506.20221 (v4 Mar 2026; **LMCS 22(2:14)**) — **alvo da campanha DD_P** (`krajicek_ddp/`).
12. **Krajíček, J. (2020).** "A limitation on the KPT interpolation." LMCS 16(3) — [11] do artigo DD_P (Lema 2).

---

## Contato

- **Autor:** Euzebio Santos (ebiossanto)
- **Repositório:** https://github.com/ebiossanto/IA-research-Godel-e-Krajicek

# PLANO DE PESQUISA E DESENVOLVIMENTO — Gödel · Krajíček · Sistemas Complexos

**Data:** 19/11/2026 · **Autor:** Euzebio Soares (ebiossanto)
**Propósito:** documento-mestre único que (1) resume o desenvolvimento do trabalho,
(2) lista as **questões respondidas** e as **a responder**, (3) organiza o **plano de
P&D** priorizado, e (4) aponta o estado do ambiente (detalhes em
`AMBIENTE_E_FERRAMENTAS.md`).

> **Taxonomia obrigatória (AGENTS.md §2):** todo item é classificado **(A)** literatura,
> **(P)** próprio, **(C)** conjectura. **"RECOMENDADO" = revisão interna (referee
> hostile), NÃO é peer review.** Nenhum item é lower bound; a ponte L2→L3
> (modelos não-padrão → complexidade) está **aberta**.
>
> **Documento canônico de índice:** [`INDICE.md`](INDICE.md) · **histórico vivo:**
> [`EVOLUCAO_PROJETO.md`](EVOLUCAO_PROJETO.md) · **consolidação DD_P:**
> [`krajicek_ddp/RELATORIO_CONSOLIDADO.md`](krajicek_ddp/RELATORIO_CONSOLIDADO.md).
> Este plano **não duplica** esses documentos — sintetiza, prioriza e aponta.

---

## 1. Mapa do programa (visão única)

| Eixo | Pergunta central | Estado | Documento-síntese |
|---|---|---|---|
| **Eixo 1 — Espectro de Reflexão (set/2026)** | Como evolui o déficit de cobertura diagonal δ_{T_α}(Φ,b) numa hierarquia de reflexão? | **Núcleo ativo** — T9–T15 provados; abertos R3/RCS/transferência | `09_...` (núcleo), `08_...` (PPR) |
| **Eixo 2 — Campanha DD_P (out/2026)** | A prova do Problema 2.1/Teorema 3–4 de Krajíček (arXiv:2506.20221) fecha? | **Lacuna confirmada em v4+v5; carta ENVIADA 11/10; aguardando autor; auditoria externa pendente** | `krajicek_ddp/RELATORIO_CONSOLIDADO.md` |
| **Eixo 3 — FCT / Motor Fractal (out/2026)** | Obstruções algébricas → latência de cauda em filas; métricas fractais de séries | **5/5 PASS; 6 descobertas D1–D6 geradas (13/10)** | `ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md`, `DESCOBERTAS_FRONTIER_2026-10-13.md` |

**Método comum (AGENTS.md §3):** triangulação **Simbólico (Z3/SymPy) → Numérico
(Julia/Python) → Formal (Lean 4)**, com *referee hostile* interno por entrega e
honestidade de escopo (nível Ten-Proofs N0–N4).

---

## 2. Desenvolvimento — síntese cronológica

| Fase | Data | O que aconteceu | Mudança de rumo? |
|---|---|---|---|
| 1 | Ago–Set/2026 | Ideia original: "ordinal ⟹ escala exponencial de provas" | — |
| 2 | 22/09/2026 | Auditoria rejeita Teoremas 4–6 (D1–D6 retraídos) | **SIM** — abandona escala exponencial |
| 3 | 22/09/2026 | Programa PPR (`08`): ≼_ppr, Lemas 7.1–7.2, transferência | **SIM** — foco em ordem operacional |
| 4 | 22/09/2026 | Núcleo `09`: δ, 𝒢, ρ_b, RBT — nível intermediário observável | **SIM** — núcleo atual |
| 5–10 | 22/09–12/10/2026 | Experimentos 10/13, RCS confirmada+robusta, PPR-2/CC-Θ, Lean PR15–PR27, revisões externas | evolução incremental |
| 11 | 10–12/10/2026 | **Campanha DD_P** — frentes A–N + N2/C2/Q2; lacuna verbatim; Teorema K; `C_{N_s}≡⊥` (cond.); nota editorial **ENVIADA 11/10 18:14** → **resposta parcial 12/10 (Q1: `i₀` ∈ `Log(M')`; Q2–Q4 pendentes)** | **SIM** — foco no Problema 2.1 |
| 12 | 13/10/2026 | **Frontier/FCT** — motor fractal 5/5; descobertas D1–D6; frentes N3/C2-O1-O5 iniciadas; commits `317886d`…`f12e324` | ampliação experimental |
| 13 | **19/11/2026 (hoje)** | Reanálise + **restauração do ambiente** (ver §6): Git, sympy, Julia, Lean, PATH; `lake build` **VERDE** reproduzido | — |

**Lacunas de documentação conhecidas (a fechar):** `INDICE.md` ainda marca v6.17
(não indexa a campanha frontier/Z3/DRAT/ω); `EVOLUCAO_PROJETO.md` encerra na Fase 11.8
(fases 12–13 ausentes). Ambas entram no horizonte Imediato do §5.

---

## 3. Questões RESPONDIDAS (estado honesto)

### 3.1 Teoremas e proposições provados (Eixo 1)

| # | Resultado | Status |
|---|---|---|
| T1 | Completude da lógica proposicional | **(A)** clássico |
| T2/T4/T9–T13 | Pontos fixos↔status; δ monotônico (Teo. 2); telescoping 𝒢; Lema 3 Φ↔Con(T); Teo. 4 δ_T=1→δ_T'=0 | **(P)** provados, elementares/sob hipóteses |
| T3/T5/T6/T7 | Deutsch; Choquet-Bruhat–Geroch; Markov; Tarski | **(A)** clássicos |
| T14/T15 | ≼_ppr é pré-ordem; transferência de hardness | **(P)** provados |
| Lema 3 / `(C)` | `lemma3_con` **PROVADO** em Lean; `allCovered ⇔ δ=0` (limiar maxκ) | **(P)** — PR24, `lake build` verde |

### 3.2 Experimentos e verificações de máquina (nível N2)

| Item | Resultado |
|---|---|
| Exp. 10 + reimplementação | δ 4→0, 𝒢=4, RBT=SIM, Con(T₀)=F / Con(T₁)=T — **proposicional** |
| RCS slow vs fast (Exp. 13 + PR16) | **CONFIRMADA e ROBUSTA 4/4** (κ, razão, \|W\|) |
| PPR-2 de R_w (PR17/PR20/PR23) | **PASSA** 3/3, 4/4, 20/20 (modelo finito escolhido — ver Caixa PPR) |
| CC-Θ sobre provas de ramos (PR19) | **32/32**, cota polinomial \|Θ(π)\|=\|π\|+O(log\|W\|) |
| Lean `Core.lean` | `delta_mono`, `theorem4_strict`, `rcs_exists` **provados sem sorry**; build verde |
| `DDP.lean` (campanha) | compila — 2 `sorry`s **permanentes por natureza** (628/690) |
| `FoundationBridge` | rota A `GodelSecond.lean` — build **VERDE 0 sorry** |
| Z3 real (12–13/10) | PPR-3 **216/216**, DRAT **216/216**, hardness `s_Res=21.2` vs `s_EF=17.0` |
| Cadeia ordinal ω | `T_ω=PA+RFN^ω`, δ→0 uniforme — convergência SIM |
| Motor fractal (FCT) | **5/5 PASS**; 24 records; **19/11: `lake build` reproduzido (4 jobs)** |

### 3.3 Campanha DD_P (Eixo 2) — DD1–DD14

| # | Resultado | Status |
|---|---|---|
| DD1 | Teoremas exatos do artigo + 3 correções de enunciado | **(A/P)** VERIFICADO |
| DD2 | **`DD_Res ∈ P`** com refutação pura ≤ \|π\| (3000/3000) | **(P)** RECOMENDADO — **auditoria externa pendente** |
| DD3 | Lacuna do passo (5) **verbatim em v4 e v5** | **(P)** RECOMENDADO |
| DD4 | `Log(M[G])=Log(M)`; `(F-b')` refutado; obstrução ZFC | **(P)** RECOMENDADO |
| DD5 | **Teorema K** (coleção interna impossível); K-FP′ | **(P)** RECOMENDADO |
| DD6 | `T_PV+(S4) ⊢ ∀rφ(r)`; C.3 negativa | **(P)** RECOMENDADO |
| DD7 | Canto adversarial: `C_{N_s}≡⊥` | **(P)** **CONDICIONAL a `q` total (Q1 da carta)** |
| DD8 | **Nota editorial ENVIADA 11/10/2026 18:14** | ✅ — **📨 resposta parcial 12/10/2026** (Q1 respondido; Q2–Q4 pendentes) |
| DD9/DD10 | Refutação interna reduzida a `EF⊢Taut(α)`; residuais R-α/R-β | **(P)** RECOMENDADO |
| DD11 | `DD_{Res(k)}`: C2.1 teorema; C2.2 = programa (O1)–(O5) | **(P)** PARCIAL |
| DD12 | Instâncias `(τ_n,q)`: Q2.1 decidido; `(Q)\|_{Σ₁}` vale | **(P)** RECOMENDADO |
| DD13/DD14 | Avaliação externa 2ª onda aplicada; **pacote de auditoria pronto** | ✅ |

### 3.4 Descobertas Frontier/FCT (13/10/2026, nível N2)

| # | Descoberta | Status |
|---|---|---|
| D1 | `ρ_c = 0.706` (não 0.25) — quantização do PFA refutada/enhancada | **(C) testada** — dado novo commitado |
| D2 | Separação não-abeliana via H: `p = 3.6e-21` | **(C) testada** |
| D4 | `H = 0.307` (fractalidade de prova) | **(C) testada** |
| D5 | Série ω **persistente** (H alto) | **(C) testada** |
| D6 | Ruído/observador **piora** a métrica | **(C) testada** |

> **Os resultados retraídos D1–D6 do Eixo 1 (tabela `DESCARTADOS` do `INDICE.md`)
> continuam retraídos — não confundir com as descobertas D1–D6 Frontier de 13/10.**

---

## 4. Questões A RESPONDER (priorizadas)

### P0 — bloqueios externos (não dependem de nós)

| # | Questão | Bloqueia | Via |
|---|---|---|---|
| **P0.1a** | ✅ **Q1 RESPONDIDO (12/10/2026):** `i₀` é comprimento de elemento de `M'` → `i₀ ∈ Log(M')` (leitura **(A)**) | remove o "blocked on Q1" de **M.2** (leitura (P) do dossiê) e fecha o escopo de **N** via (A); Q2–Q4 seguem decidindo leitura (i)/(iii), convenção de código e Condition 1 | `CARTA_FINAL_RECEBIDA.md` (e-mail de 12/10/2026 14:48 UTC) |
| **P0.1b** | **Q2–Q4 PENDENTES** — range de `τ_N` (condiciona **C2**), divergência hip, container H3 | C2/DD_{Res(k)} e leituras restantes | **follow-up curto devido** — janela de 2–4 semanas **vencida** (5+ semanas em 19/11) |
| **P0.2** | **Auditoria externa independente** de `DD_Res ∈ P` e frentes G–N | credibilidade (N4 Ten-Proofs); prioridade nº 1 da avaliação 12/10 | dossiê pronto: `krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md` |

### P1 — frentes internas em andamento (próximo passo ativo)

| # | Questão | Status atual | Próximo passo concreto |
|---|---|---|---|
| **P1.1** | **N3:** construir `(∗′)` por compacidade (canto `χ≡⊤`) | aberta (origem N2.3′) | lema de omissão **não-elementar**; omitting types; excluir ultrapoder (I1 A.7/B.2) |
| **P1.2** | **C2:** fechar o algoritmo `DD_{Res(k)}` — obrigações **(O1)–(O5)** | **r2 (19/11): (G1) CONTRAEXEMPLO verificado** (candidato r1 retraído) → **C2.2′ TEOREMA (P) linha-puro**; C2.2 original segue **(C)** com evidência negativa; próximo: **critério-LP na família alternante** (`gk_alternating_family.py`) | `krajicek_ddp/C2_r2_G1_contraexemplo.md`, `gk_c2_projection_sim.py` |
| **P1.3** | **C2.3:** família **alternante** (exatamente 1 lado insat, alternando com γ) | **(C)** | atacar via reflexão com lado "espectador" satisfatível |
| **P1.4** | **Q2.4:** fonte **Σ₁** para a hierarquia de velocidade | ✅ **VARREDURA EXECUTADA (19/11)** — `(C)` → **candidatas A/B qualificadas** (`Q2.4_fonte_SIGMA1_K19_KP90.md` + referee r1); K19 caps.9/17 = setup/FI; fonte real = Pudlák §6–§7; **pendências A1/A2/A5 bloqueiam o 1º limite inferior** |
| **P1.5** | **Rota B:** Φw* com padding w* (definability + FGH) | aberta | `FoundationBridge/` — especificar Φ e provar pad-Prf |

### P2 — programa δ/𝒢 (Eixo 1, matemática pura)

| # | Questão | Status |
|---|---|---|
| P2.1 | **PR1/R3:** `g_PA ≼_ppr g_{PA+RFN(PA)}?` | ABERTO (R1/R2 provados) |
| P2.2 | **PR4/RCS:** perfil α↦δ contém informação não-ordinal? | hipótese falsificável — RCS confirmada no modelo; generalização aberta |
| P2.3 | **PR6:** transferência `δ_S ≤ δ_T ⟹ g_T ≼_ppr g_S?` | ABERTO |
| P2.4 | **PR5:** `ρ_b` independente de codificação? | ABERTO (posicionar vs Pakhomov–Walsh) |
| P2.5 | **PR10/PR11:** R não-vácuo geral; Θ polinomial CC-Θ em PA | aberto no modelo real (finições: 32/32 no modelo) |
| P2.6 | **PR13/PR14:** prova formal Φ_PA↔Con(PA); iteração T_k com mesma Φ | planos em `09 §35–36` |

### P3 — FCT / experimentos (Eixo 3)

| # | Experimento (ver `ONDE_ESTAMOS` §5) | Critério |
|---|---|---|
| P3.1 | **D1′** quantização PFA: varrer m∈{2..7}, n∈{4,8,16}, bootstrap de ρ_c empírico | coincidir com 1/4? → dado `gk_fractal_phase_transition.csv` |
| P3.2 | **D2′** detector ordem de grupo (abeliano vs não) via cross-validation | acurácia + β, ρ |
| P3.3 | **D3′** predição de colapso em `cpu_timeseries` reais | H ajustado vs colapso 24h seguintes |
| P3.4 | **D4′** ponte prova→fractal | ✅ **EXECUTADO v1 (19/11)** — `28_PONTE_PROVA_FRACTAL_D4.md`: 188 UNSAT reais; **D_H separa `php` (4/4 IC exclui0, raw+log1p)** = regime de crescimento; Res-vs-EF **deferido**; v2: anti-quantização, séries τ maiores |
| P3.5 | **D5′** perfil fractal da cadeia ω (η_n → H) | H→1 (persistência transfinite)? |
| P3.6 | Validar `P₉₉ = P^ideal(1+ρ/(1−ρ)·p²)` contra telemetria real | erro relativo |

### P4 — metaciência e divulgação

| # | Item | Regra |
|---|---|---|
| P4.1 | Atualizar `INDICE.md` → v6.18+ (indexar frontier/Z3/DRAT/ω/N3/C2) | gap declarado em `ONDE_ESTAMOS` §2.4 |
| P4.2 | Atualizar `EVOLUCAO_PROJETO.md` → Fases 12–13 | idem |
| P4.3 | Regenerar `gk_lean_bridge.py` (JSON stale diz False; build real é verde) | substituir por verificador baseado no output do lake |
| P4.4 | MathOverflow — **só com confirmação do autor** | rascunho `27_MATHOVERFLOW_PERGUNTA.md` |
| P4.5 | Busca bibliográfica especializada de δ/RBT/ρ_b/FP-K | antes de qualquer claim de novidade |
| P4.6 | Publicar apenas com resultado formal verificado + auditoria externa | `CONTINUIDADE` §6.4 |

---

## 5. Plano de P&D — horizontes

### H0 — Imediato (esta semana, alto sinal/baixo custo)

1. ✅ **Ambiente restaurado** (19/11): Git (safe.directory), sympy (adulterado→oficial),
   Julia 1.10.2, Lean 4.34/Lake, PATH, pysat — ver `AMBIENTE_E_FERRAMENTAS.md`.
2. ✅ **`lake build` reproduzido** (4 jobs, 2 sorry documentados).
3. ~~Verificar resposta de Krajíček~~ ✅ **propagado em 19/11** (P0.1a: Q1
   respondido 12/10; P0.1b: Q2–Q4 pendentes) — **próximo: follow-up curto
   para Q2–Q4** (janela de 2–4 semanas vencida).
4. **Fechar lacunas de documentação:** INDICE v6.18, EVOLUCAO Fase 12–13 (P4.1/P4.2).
5. **Regenerar `gk_lean_bridge.py`** (P4.3).
6. **Commit seletivo** dos artefatos novos (separar fixes de ambiente vs pesquisa).

### H1 — Curto prazo (1–3 semanas)

7. **Enviar 1ª via da auditoria externa** (P0.2) — parar de acumular conjecturas   (determinação da avaliação 12/10: *obter auditoria, não adicionar resultados*).
8. **Frente N3** — `(∗′)` por compacidade (P1.1).
9. ~~Varredura [K19 5.7] + K19 caps 9/17 + KP90 (P1.2/P1.4)~~ — **P1.4 FEITO
   em 19/11** (`Q2.4_fonte_SIGMA1_K19_KP90.md`: candidatas A/B, K19 caps.9/17 =
   setup/FI); **P1.2 TEXTO EXATO OBTIDO em 19/11** (`C2_K19_5_7_TEXTO_EXATO.md`:
   regras de `Res(k)` via Garlík CCC2024 §2) — **resta r2: (G1) conflito de
   demandas + (G2) pureza `Res(k)`**.
10. ~~Rodar D4′ (ponte prova→fractal, P3.4)~~ ✅ **FEITO em 19/11** —
    `28_PONTE_PROVA_FRACTAL_D4.md` (+referee r1): seed+hash+comando congelados;
    H_C1 confirmada como separação de regime; pendências v2 no referee §B.

### H2 — Médio prazo (1–3 meses)

11. Fechar **C2 (O1)–(O5)** e família alternante (P1.2/P1.3).
12. **Rota B** Φw* (P1.5) + avançar Foundation/Mathlib.
13. Datasets institucionais do motor fractal (Bridge/Bullwhip/Nonabelian/Stochastic/Entropy)
    + validação P₉₉ (P3.6).
14. Busca bibliográfica de novidade (P4.5); só então rascunho de submissão.

### H3 — Largo prazo (3–6+ meses)

15. Responder às frentes P2 (R3, transferência, ρ_b, RCS generalizada) — exigem PA real
    ou novo modelo.
16. Submissão condicionada: auditoria externa ✓ + resultado formal verificado ✓.
17. Manter cadência de *referee hostile* interno por entrega (invariante do método).

### Critérios de sucesso por entrega (Ten-Proofs)

Toda entrega nova deve nascer com **N0 proposição → N1 prova escrita → N2 verificação
de máquina → N3 meta-verificação → N4 externa**; nível não executado = `pending`.

---

## 6. Ambiente — resumo (detalhe em `AMBIENTE_E_FERRAMENTAS.md`)

| Ferramenta | Estado (19/11/2026) | Nota |
|---|---|---|
| Git 2.56 | ✅ | `safe.directory` **corrigido hoje**; remoto = GitHub oficial |
| Python 3.15.2 | ✅ | z3 5.4.1, sympy 1.14.0 (**restaurado**), numpy/pandas/scipy/matplotlib, psutil, **pysat (instalado hoje)** |
| Julia 1.10.2 | ✅ | **restaurada hoje** (`julia.exe` faltava); no PATH |
| Lean 4.34 + elan + Lake 5.0 | ✅ | toolchain baixada hoje; **`lake build` verde** |
| Node 22.23 / GitHub CLI / choco | ✅ | presentes |
| winget | ❌ indisponível | usar **choco** ou zips manuais |
| cvc5, LTspice, FreeFEM, Sage, GeoGebra | ❌ não instalados | **opcionais** (FCT/hardware) — instalar sob demanda |
| Junction `C:\Lab` | desnecessária | caminho atual é ASCII puro (sem acentos) |

**Permissões:** apenas ajustes de **PATH/usuário** foram necessários (sem admin);
Git configurado com exceção de diretório seguro.

---

## 7. Disciplina de pesquisa (invariantes — não violar)

1. **Não** apresentar Z3/PPR-3 como lower bound de complexidade de provas (verifica a *tradução*, não a ausência de prova curta).
2. **Não** chamar RECOMENDADO de peer review; **não** tratar M.2 como incondicional.
3. **Não** empurrar o motor fractal para claims de complexidade computacional.
4. **Não** committar experimentos sem seed+hash+comando.
5. **Não** usar os resultados retraídos D1–D6 do Eixo 1; manter banners de retração.
6. **Não** adicionar conjecturas novas sem necessidade (determinação da avaliação externa);
   priorizar **auditoria externa**.
7. Toda descoberta nova entra **aditivamente** — não alterar a essência dos resultados existentes.

---

## 8. Referências obrigatórias (recorte — lista completa em `INDICE.md`)

1. Krajíček, J. (2025). *A Proof Complexity Conjecture and the Incompleteness Theorem.* JSL 90(3).
2. Krajíček, J. (2025). *Proof Complexity Generators.* Cambridge UP (LMS LN 497).
3. Krajíček, J. (2026). *On NP∩coNP proof complexity generators.* arXiv:2506.20221 — **alvo da campanha DD_P**.
4. Beklemishev, L.D. (2005). *Reflection principles and provability algebras.* RMS 60(2).
5. Freund & Pakhomov (2020). *Short proofs for slow consistency.* NDJFL 61(1).

---

*Documento vivo — atualizar a cada mudança de horizonte. Índice canônico: `INDICE.md`.*

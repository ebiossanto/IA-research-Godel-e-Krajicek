# Evolução do Projeto: Gödel–Krajíček

**Documento vivo:** atualizado a cada novo passo.
**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data da primeira versão:** Setembro 2026
**Última atualização:** 22/09/2026

---

## Propósito deste documento

Registrar, de forma honesta e cronológica:

1. a ideia original;
2. as pesquisas e provas que conseguimos;
3. o que está em aberto;
4. onde mudamos de rumo e o porquê.

---

## Fase 1 — Ideia original (agosto/setembro 2026)

### O que queríamos fazer

Conectar três programas:

- **Gödel (1931):** incompletude de teorias formais;
- **Krajíček (2004–2025):** geradores de complexidade de provas;
- **Beklemishev (2003–2024):** hierarquia ordinal de reflexão.

### A tese informal

> "A força proof-theoretic de uma teoria T determina a hardness do gerador g_T, e uma hierarquia ordinal de reflexão induz uma escala exponencial de comprimentos de prova."

### Status desta fase

**DESCARTADA.** Motivos:

1. Krajíček (2023/2025) já constrói g_T corretamente — não era novo;
2. a observação b(n)→ω(1) já está no rodapé 3 do paper dele;
3. as tabelas exponenciais (2^Ω(n), 2^{2^Ω(n)}, …) não tinham derivação;
4. a prova do "Teorema 1" confundia enumeração exponencial com tempo polinomial;
5. "hard para sistemas que interpretam T" não é afirmado por Krajíček — hardness universal é problema aberto.

---

## Fase 2 — Auditoria e reclassificação (22/09/2026)

### O que aconteceu

Uma auditoria rigorosa (`AUDITORIA_RIGOROSA_GODEL_KRAJICEK.md`) reconstruiu os Teoremas 4, 5 e 6 e os rejeitou:

| Resultado antigo | Veredito |
|------------------|----------|
| Teorema 4: s_P ≥ 2^{c\|T_α\|n} | **REJEITADO** — contagem ≠ lower bound |
| Teorema 5: cortes estritos C(α) | **NÃO PROVADO** — falta ponte teorias↔sistemas |
| Teorema 6: gerador universal T_* | **NÃO PROVADO** — T_* não é r.e. |
| Conjectura FP-K como "nova" | **REBAIXADA** — originalidade não certificada |

### Mudança de rumo

Em vez de tentar provar uma escala exponencial, passamos a estudar a **ordem operacional** de geradores:

$$T \preceq_{int} S \stackrel{?}{\Longrightarrow} g_T \preceq_{ppr} g_S$$

---

## Fase 3 — Programa PPR (22/09/2026)

### O que fizemos (`08_PROGRAMA_...`)

1. **Corrigimos** a tautologia associada: em vez de ⋀[C_n(x)=g(x)], usamos as τ-fórmulas de range-avoidance τ(g_n)_b (compatível com Krajíček);
2. **Definimos** formalmente ≼_ppr (PPR-1 tamanho, PPR-2 semântica, PPR-3 provas);
3. **Provamos** que ≼_ppr é pré-ordem (Lemas 7.1–7.2);
4. **Provamos** a transferência de hardness (Prop 8.1, Cor 8.2).

### O caso concreto T₀=PA, T₁=PA+RFN(PA)

| Afirmação | Estado |
|-----------|--------|
| T₀ ⊆ T₁ | PROVADO |
| T₀ ≼_int T₁ | PROVADO |
| A_{T₀} ⊆ A_{T₁} (provas curtas) | PROVADO |
| w₀^{T₁} ≥_lex w₀^{T₀} | PROVADO (local) |
| g_{T₀} ≼_ppr g_{T₁} | **ABERTO** |
| g_{T₀} ⋠_ppr g_{T₁} | **ABERTO** |

### Resultado metodológico novo (§33 do 08)

$$\text{Inclusão de teorias} \Rightarrow \text{monotonicidade do predicado de prova}$$

mas

$$\text{monotonicidade do predicado} \nRightarrow \text{PPR do gerador}$$

**Razão:** o operador $A_T \mapsto \min_{lex}(\neg A_T)$ não preserva redução polinomial.

---

## Fase 4 — Espectro de Reflexão (22/09/2026, núcleo atual)

### Por que mudamos de rumo

O salto direto T ≼_int S ⟹ g_T ≼_ppr g_S era **bloqueado estruturalmente** (min_lex não preserva redução). Precisávamos de um **nível intermediário** observável.

### A ideia nova (`09_EVOLUCAO_...`)

Separar dois orçamentos no gerador:

- **a(n):** orçamento de descrição (tamanho de Φ);
- **b(n):** orçamento de prova (comprimento da prova procurada);

produzindo a família **g_T^{a,b}**.

Isso permite definir:

1. **Déficit de cobertura diagonal** δ_T(Φ,b) — quantas obrigações verdadeiras estão sem prova dentro do orçamento;
2. **Ganho de reflexão** 𝒢_Γ(T,Φ,b) = δ_T − δ_{T+RFN(T)} ≥ 0;
3. **Rank de cobertura** ρ_b(Φ;H) = min{α : δ_{T_α}(Φ,b)=0};
4. **Transição de Ramo por Reflexão (RBT):** mudança discreta no ramo escolhido pelo gerador após um passo de reflexão.

### Provas obtidas nesta fase

| # | Resultado | Status |
|---|-----------|--------|
| Prop. 1 | \|g_T^{a,b}(u)\| = \|u\|+1 (alongamento) | **PROVADO** |
| Teo. 2 | δ_S(Φ,b) ≤ δ_T(Φ,b) se T ⊆ S (monotonicidade) | **PROVADO** |
| §10 | Telescoping: δ_{T_0} − δ_{T_m} = Σ 𝒢 | **PROVADO** |
| Lema 3 | Φ_T^{w*} ↔ Con(T) (obrigação codifica consistência) | **PROVADO** (sob formalização) |
| Teo. 4 | δ_T=1, δ_{T'}=0 (ressposta estrita à reflexão) | **PROVADO** (sob hipóteses) |
| Cor. | 𝒢_{Π_1}(T,Φ_T,b)=1 (ganho unitário) | **PROVADO** (corolário) |

### O que isso melhora

A antiga FP-K usava "força de diagonalização" (vago). Agora:

$$\text{recuperação} \iff \delta_{T_\alpha}(\Phi,b)=0$$

e a pergunta slow vs. fast torna-se:

$$\delta_{S_\alpha}(\Phi,b) \stackrel{?}{=} \delta_{F_\alpha}(\Phi,b)$$

---

## Fase 5 — Varredura bibliográfica e experimento (22/09/2026)

### Busca δ vs. Pudlák/Krajíček

| Conceito | Encontrado? | Detalhe |
|----------|-------------|---------|
| δ (déficit de cobertura) | **NÃO** | Krajíček: τ pontuais; Pudlák: comprimento de provas de princípios fixos — não contam obrigações não cobertas com orçamento b |
| RBT (transição de ramo) | **NÃO** | Nome proposto; "missing reflection" (Kra11) é conceito próximo mas diferente |
| ρ_b (rank de cobertura) | **PRÓXIMO: Pakhomov–Walsh "reflection rank"** | DIFERENTES: eles = ordinal de prova; nós = primeiro nível com δ=0 |

**Status:** δ e RBT são **candidatos a novidade** (busca especializada pendente). ρ_b precisa de posicionamento explícito vs. Pakhomov–Walsh.

### Perguntas geradas pela varredura

1. Freund–Pakhomov: PA prova polinomialmente Con(PA+Con*(PA))↾n — **isso aparece em δ?**
2. Henk–Pakhomov: 3 variantes com ε₀, ω, 2 passos — **assinatura em δ?**

### Experimento criado

**`10_EXPERIMENTO_GERADORES_FINITOS.md`:**
- Setup: T₀=PA, T₁=PA+RFN_{Π₁}(PA) truncada em L
- Enumeração n=8..16, b∈{4,...,64}
- Tabelas: imagens, δ, 𝒢, RBT, candidatos R
- Pseudocódigo Python-like
- Critérios de sucesso/refutação

---

## Fase 6 — Experimento 10 EXECUTADO (22/09/2026)

### Script: `experimento_10.py` (simulação estrutural)

**Setup:** |Φ|=12, r=4, W^true=16, w*=00 (4 obrigações ∞ em T₀), s_{T₁}(Con)=20

### Resultados (tabelas §4 preenchidas)

| Pergunta | Resultado |
|----------|-----------|
| δ diminui T₀→T₁? | **SIM** — 𝒢=4 para b≥20 |
| RBT ocorre? | **SIM** — 5/9 valores b (b≥20): `0000 → ALL_COV` |
| Candidato R? | **SIM — `suffix0`** (s‖'0') passa PPR-2 em n=12,14,16 |
| δ decresce com b? | **SIM** — [16,16,16,5,4,4,4,4,4] |
| Teo. 4 (δ₀=1,δ₁=0)? | **Parcial** — δ₀=4(=n_wstar), δ₁=0 para b≥20 |

### Verificações teóricas executadas

- 𝒢 ≥ 0 sempre ✓
- δ_{T₁} ≤ δ_{T₀} (Teo. 2) ✓
- δ_{T₀} não-crescente em b ✓

### Ressalva

Simulação estrutural (complexidades de prova fixadas), não busca real em PA.
Captura mecânica (δ, RBT, PPR) fielmente; não certifica PA real.

---

## Fase 7 — PPR-3 + reimplementação real + nota (22/09/2026)

### 7.1 PPR-3 para suffix0 (`11_PPR3_THETA_SUFFIX0.md` + `ppr3_suffix0.py`)

- Θ de enumeração: **OK** mas cota O(2^n) (fraca)
- **DESCOBERTA: suffix0 VÁCUO** — |R(b)|=n+2 vs |rng|=n+1 ⇒ PPR-2 trivial
- **suffix0 ABANDONADO** como R final; R real deve operar em índices/obrigações
- Θ polinomial (§3.2): proposto, CC-Θ **não provada**

### 7.2 Reimplementação com busca real (`reimplementacao_provas_reais.py`)

- Busca por **resolução proposicional** (não valores fixos)
- T0: axiomas de obrigações genéricas; Con não-unitário (indemonstrável)
- T1: T0 + axioma unitário Con (RFN proposicional)
- **Resultados (estáveis em max_steps 500–2000):**
  - δ_T0=4, δ_T1=0, **G=4**
  - **RBT=SIM** (w0: 0000 → ALL_COV)
  - Con em T0: False ✓; Con em T1: True ✓
  - G≥0 ✓; δ_T1≤δ_T0 ✓
- **Limite honesto:** proposicional, não PA aritmética

### 7.3 Nota de posicionamento (`12_NOTA_CURTA_POSICIONAMENTO_DELTA_RBT.md`)

- δ vs Pudlák (2020): complementar (falhas vs. sucessos) — não encontrada
- δ/RBT vs Krajíček: agregado/reflexão não aparecem — candidatos
- ρ_b vs Pakhomov–Walsh: **distintos** (finito-combinatório vs. ordinal)
- Ressalvas: busca inicial, proposicional, suffix0 vácuo

### 7.4 Mesclagem de conteúdo em 09 (§35–40)

Adicionado ao núcleo 09 o que era novo/correto no documento fornecido:
- **§35 Plano concreto PA→RFN** (metas formais δ_PA=1, δ_T1=0)
- **§36 Iteração** T_{k+1} com mesma família Φ
- **§37 Meta científica** (reflexão ↔ transição de cobertura)
- **§38 Tabela de classificação** de todos os objetos
- **§39 Veredicto**
- **§40 Referências** expandidas
- Status de correções §33 marcado como **PENDENTES**

---

## Fase 8 — Experimento 13: Slow vs Fast, RCS CONFIRMADA (22/09/2026)

### Setup
- **Φ fixa** (Φ_PA^{w*} ↔ Con(PA)), mesma para ambas hierarquias
- Rápida F_α: +2σ/pass (Con); Lenta S_α: +1σ/pass (Con_s < Con)
- |W|=16, w* = 4 obrigações κ=2; genéricas κ∈{0,1}
- Script: `slow_vs_fast_delta.py`

### Resultado

| α=1, b≥3 | δ_F | δ_S | Diferença |
|-----------|-----|-----|-----------|
| | **0** | **4** | **−4** |

- **3/30 pares (α,b) com δ_F ≠ δ_S**
- Rápida cobre tudo em α=1; lenta ainda com w* descoberto (κ=2>σ=1)
- Lenta alcança em α=2

### VEREDITO

\[\boxed{\text{RCS CONFIRMADA no modelo (slow vs fast, Φ fixa)} }\]

- **Nomeável:** primeiro observável de cobertura que separa progressões lentas/rápidas
- **Ponte:** slow consistency (FRW/Freund–Pakhomov) ↔ proof complexity generators (Krajíček) via δ
- **Ressalva:** modelo estrutural (σ,κ fixados), não PA real — formalização Lean/Isabelle pendente (PR15)

---

## Fase 9 — O que está em aberto (agora)

### Aberto matemático

1. **PPR-Reflection-1:** g_PA ≼_ppr g_{PA+RFN(PA)}? (e a negação)
2. **Hipótese RCS:** o perfil α ↦ δ_{T_α}(Φ,b) contém informação não recuperável do ordinal?
3. **Transferência:** δ_S ≤ δ_T + hipóteses ⟹ g_T ≼_ppr g_S?
4. **ρ_b:** é independente das escolhas de codificação?

### Aberto bibliográfico (após varredura 22/09)

1. ~~δ vs Pudlák/Krajíček?~~ → **busca inicial: NÃO encontrado** (profundizar com especialistas)
2. ~~RBT já existe?~~ → **busca inicial: NÃO encontrado**
3. ρ_b vs Pakhomov–Walsh → **PRÓXIMO mas DISTINTO** — posicionar explicitamente
4. FP-K equivalente publicado? → **ainda não verificado**

### Aberto experimental (pós-13)

- ~~PPR-3 suffix0~~ → **vácuo; abandonado** (11 §4.3)
- ~~RCS slow vs fast~~ → **CONFIRMADA no modelo** (13) — formalizar em Lean/Isabelle
- **R não-vácuo:** índices w ou códigos π
- **CC-Θ:** Θ polinomial (11 §3.3)
- **PA real:** Lema 3 + Teo 4 + resultado 13 em Lean/Isabelle (PR15)
- **Correções 01/06/03:** aplicar (09 §33, PENDENTE)
- **Estender 13:** mais κ variado, Φ mais rica, comparar com Freund–Pakhomov (comprimento vs δ)

---

## Cronologia resumida

| Data | Evento | Mudança de rumo? |
|------|--------|------------------|
| Ago/Set 2026 | Ideia original: ordinal ⟹ escala exponencial | — |
| 22/09/2026 | Auditoria rejeita Teoremas 4-6 | **SIM** — abandona escala exponencial |
| 22/09/2026 | Programa PPR (08): ≼_ppr definido, R1/R2 provados | **SIM** — foco em ordem operacional |
| 22/09/2026 | Núcleo 09: δ, 𝒢, ρ_b, RBT | **SIM** — nível intermediário observável |
| 22/09/2026 | Varredura bib. + 10_EXPERIMENTO | δ/RBT não encontrados; ρ_b ≠ Pakhomov–Walsh |
| 22/09/2026 | **Experimento 10 executado** | RBT=SIM(5/9), R=`suffix0`, δ/T2 confirmados |
| 22/09/2026 | **PPR-3 suffix0: VÁCUO; abandonado** | R real = índices/obrigações |
| 22/09/2026 | **Reimplementação resolução real** | confirma δ/G/RBT; proposicional |
| 22/09/2026 | **Nota 12 posicionamento** | δ/RBT não encontrados; ρ_b≠P–W |
| 22/09/2026 | **Exp.13 slow vs fast** | **RCS CONFIRMADA** (δ_F≠δ_S em α=1) |
| Próximo | Lean/Isabelle (PR15); estender 13; R não-vácuo | — |

---

## Lições aprendidas

1. **Separar teorema, analogia e conjectura** desde o início (Parte 2 / pontos fixos ensinou isso).
2. **Nunca confundir contagem com lower bound** (erro do Teorema 1/4).
3. **b(n)→ω(1) já existe** — sempre verificar rodapés.
4. **Hardness universal é problema aberto** — não assumir.
5. **min_lex não preserva redução** — inclusão de teorias não dá PPR automaticamente.
6. **Buscar nível intermediário** quando o salto direto falha (δ foi esse nível).

---

## Próximo passo (a atualizar)

> **Próximo:** (a) Buscar **R não-vácuo** (sobre índices w ou códigos de prova π — ligação com RBT); (b) Provar/refutar **CC-Θ** para Θ polinomial; (c) **Lean/Isabelle** com PA real (sair do proposicional); (d) Consultar especialista sobre nota 12. Depois: atualizar este documento.

---

**Este documento deve ser atualizado a cada novo resultado, mudança de rumo ou descoberta bibliográfica.**

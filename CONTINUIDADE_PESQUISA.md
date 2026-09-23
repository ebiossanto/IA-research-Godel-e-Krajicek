# Documento de Continuidade: Pesquisa Godel-Krajicek

**Data:** Setembro 2026
**Status:** Para continuidade pelo autor
**Aviso:** Este documento resume TUDO o que foi feito, descoberto, e o que resta fazer.

---

## 1. Resumo da Jornada

### 1.1. Objetivo Inicial

Conectar:
- Incompletude de Goedel (1931)
- Complexidade de provas de Krajicek (2004-2025)
- Hierarquia ordinal de Beklemishev (2003-2024)

### 1.2. O Que Foi Descoberto

1. **Krajicek (2023)** ja faz corretamente o que tentavamos fazer
2. **Nossa observacao** ja existe no rodape 3 do paper dele
3. **Tabelas de bounds** eram especulativas (sem derivacao)
4. **Provas** continham erros (enumeracao exponencial)
5. **Teoremas 4, 5, 6** NAO estao provados na forma escrita (auditoria 22/09/2026)

### 1.3. O Que Sobrou (apos auditoria + nucleo 09)

A **pergunta de pesquisa FP-K** foi REBAIXADA (originalidade nao estabelecida).

A **nova linha mais promissora** evoluiu em duas camadas:

1. **08 (PPR):** T ≼_int S ⟹? g_T ≼_ppr g_S — bloqueio estrutural identificado (min_lex nao preserva reducao)
2. **09 (Espectro de Reflexao) — NUCLEO ATUAL:** nivel intermediario observavel:
   - deficit delta_T(Φ,b) (monotonico, Teo. 2)
   - ganho de reflexao 𝒢 ≥ 0 (telescoping)
   - rank rho_b, transicao RBT
   - Lema 3: Φ_T^{w*} ↔ Con(T)
   - Teorema 4: reflexao da δ_T=1 → δ_T'=0

**Documentos:** `09_EVOLUCAO_...` (nucleo), `08_PROGRAMA_...` (PPR), `EVOLUCAO_PROJETO.md` (historico vivo).

---

## 2. Referencias Criticas (obrigatorias)

### 2.1. Paper Central

**Krajicek, J. (2023). "A proof complexity conjecture and the Incompleteness theorem."**
- arXiv:2303.10637
- JSL 90(3), 2025, pp. 1206-1210
- **Leer COMPLETO** - e curto (6 paginas)

**O que faz:**
- Constroi g_T que diagonaliza contra T
- Prova 1o Teorema de Goedel via geradores
- Mostra que log n pode ser trocado por ω(1) (rodape 3)

### 2.2. Livro de Referencia

**Krajicek, J. (2025). "Proof Complexity Generators."**
- Cambridge University Press, 134 paginas
- LMS Lecture Note Series, No. 497
- **Leer capítulos 3 e 9**

### 2.3. Slow Consistency (linha correta para "hierarquia ordinal")

| Paper | O que faz | Status |
|-------|-----------|--------|
| Friedman-Rathjen-Weiermann (2013) | Definem Con*(PA) | PROVADO |
| Henk-Pakhomov (2016) | Progressao lenta | PROVADO |
| Freund-Pakhomov (2020) | PA tem provas polinomiais de Con(PA+Con(PA))↾n* | PROVADO |
| Pakhomov-Walsh | Reflection ranks e analise ordinal | PROVADO |

### 2.4. Outras Referencias

- Beklemishev (2003): Hierarquia de reflexao
- Cook-Reckhow (1979): NP=coNP iff existe sistema polinomico
- Pudlak (2020): Reflexao proposicional

---

## 3. O Que Ja Existe (nao inventamos nada novo)

### 3.1. Mecanismo de Krajicek (2023)

**Dado u com |u| = n:**

1. Acha formula Φ com |Φ| ≤ log n
2. Para cada w, procura T-prova de tamanho ≤ log n
3. A primeira w sem prova define a saida

**Por que funciona:**
- 2^{O(log n)} = poly(n) candidatos
- Cada candidato verificado em tempo polinomial
- Total: tempo polinomial

**Generalizacao (ja em Krajicek):**
- log n pode ser trocado por qualquer ω(1)
- Com log log n: tempo linear

### 3.2. Conexao com Slow Consistency

A "hierarquia ordinal" que tentavamos criar ja existe como **slow consistency**:
- Friedman-Rathjen-Weiermann (2013)
- Henk-Pakhomov (2016)
- Freund-Pakhomov (2020)

---

## 4. O Que NAO Funcionou (erros que cometemos)

### 4.1. Teorema 1 (invalido)

**Dizia:** "Enumerar todas as provas de ate p(n) e polinomial"

**Erro:** 2^{p(n)} e exponencial, nao polinomial

**Correcao:** Krajicek usa log n (nao p(n))

### 4.2. Tabela de Bounds (especulativa)

**Dizia:**
| Nivel | s_P(TG_alpha) |
|-------|---------------|
| 0 | 2^{Omega(n)} |
| 1 | 2^{2^{Omega(n)}} |
| 2 | 2^{2^{2^{Omega(n)}}} |

**Problema:** Sem derivacao. Eram conjecturas.

**Correcao:** Removida.

### 4.3. Cortes Ordinais (especulativos)

**Dizia:** C(alpha) = {P : ist(P) >= [T_alpha]}

**Problema:** Nao sabemos se a hierarquia de interpretabilidade e "suficiente"

**Correcao:** Removido.

### 4.4. Teoremas 4, 5, 6 (auditoria 22/09/2026)

**Teorema 4 (s_P >= 2^{c|T_alpha|n}):**
- "N candidatos => tempo minimo Omega(N)" e' FALSO em geral
- 2o Teorema de Goedel NAO produz lower bound quantitativo
- |T_alpha| e' ambiguo para ordinais
- **STATUS: NAO PROVADO / REJEITADO**

**Teorema 5 (cortes estritos C(alpha)):**
- T_alpha subseteq T_beta NAO implica C(alpha) proper subset C(beta)
- Interpretabilidade e' entre teorias; sistemas de prova sao proposicionais -- falta traducao
- **STATUS: NAO PROVADO**

**Teorema 6 (gerador universal T_*):**
- T_* = union{r.e., consistente, supseteq PA} NAO e' r.e.
- "Conter informacao inacessivel" NAO e' prova de hardness
- Universal hardness NAO cria completude automaticamente
- **STATUS: NAO PROVADO**

**Leitor completo:** `AUDITORIA_RIGOROSA_GODEL_KRAJICEK.md` (downloads) ou verificacao propria.

---

## 5. O Que Pode Ser Explorado (perguntas em aberto)

### 5.1. Pergunta Principal (STATUS REBAIXADO)

> Existe um analogo do fenomeno Freund-Pakhomov dentro do esquema g_T de Krajicek?

**Status atual:** **PERGUNTA DE PESQUISA** — originalidade NAO estabelecida (auditoria 22/09/2026). Formalizada em `CONJECTURA_FP_K.md`.

**Antes se dizia:** "e genuinamente nova" — **CORRIGIDO:** nao certificado; exige busca bibliografica especializada.

**Por que e' importante:**
1. Conecta dois programas (slow consistency e geradores)
2. E' respondivel (pergunta precisa)
3. NAO ha confirmacao de que seja nova

### 5.2. NOVA Pergunta Principal (apos auditoria)

**Mais promissora e formalmente mais precisa:**

$$T \preceq_{int} S \stackrel{?}{\Longrightarrow} g_T \preceq_{ppr} g_S$$

A interpretacao proof-theoretic preserva a ordem operacional de geradores?

**Tres casos:**
- **A:** implicacao vale -> teorema de transferencia
- **B:** vale sob restricoes -> nova classe de teorias
- **C:** contraexemplo -> quebra entre hierarquias (interessante!)

**Documento:** `08_PROGRAMA_INTERPRETABILIDADE_VS_GERADORES.md`

### 5.3. Medida Operacional (nova)

$$\Gamma_P(T, n) = \log s_P(TG_T^n)$$

Pergunta testavel: "A reflexao produz assinatura mensuravel na complexidade proposicional?"

### 5.4. Perguntas Secundarias

1. **Tightness:** O limite de Krajicek e' otimo?
2. **Formalizacao:** Podem ser mecanizados em Lean 4?
3. **Aplicacoes:** Slow consistency pode separar sistemas de prova?

---

## 6. Proximos Passos Concretos (revisados pos-auditoria)

### 6.1. PRINCIPIO

> Nenhum resultado sera' chamado de teorema ate' que cada hipotese, dominio, codificacao, reducao e medida de tamanho esteja formalmente especificada.

### 6.2. Imediatos (1-2 semanas)

1. **Ler Krajicek (2023) COMPLETO** (6 paginas)
2. **Ler Krajicek (2025) capitulos 3 e 9**
3. **Ler Freund-Pakhomov (2020)** "Short proofs for slow consistency" NDJFL 61(1)
4. **NAO adicionar mais conjecturas** ao repositorio

### 6.3. Curto prazo (1-3 meses) — seguir 09 (nucleo) + 08 (PPR)

1. ~~Definir formalmente g_T, TG_T^n, precequiv_ppr~~ **FEITO** (08: τ-fórmulas, PPR)
2. ~~Provar lema de composicao~~ **FEITO** (08: Lemas 7.1-7.2)
3. ~~Casos T_0=PA e T_1=PA+RFN(PA)~~ **ANALISADO** (08: R1/R2 provados, R3 aberto)
4. ~~Nivel intermediario delta~~ **FEITO** (09: Teo. 2, Lema 3, Teo. 4, telescoping)
5. **ETAPA A:** fixar apresentacao canonica (codificacao de formulas, provas, tau)
6. **ETAPA B:** calcular explicitamente g_{PA,n}, g_{T_1,n} para n pequeno
7. **ETAPA C-D:** buscar R e Theta candidatos; testar PPR
8. **ETAPA E:** so depois generalizar / tentar prova assintotica
9. **`10_EXPERIMENTO` + `experimento_10.py` EXECUTADOS:** RBT=SIM, suffix0 proposto, tabelas §4
10. **`11_PPR3` + `ppr3_suffix0.py`:** suffix0 **VÁCUO/abandonado**; Θ enum OK; CC-Θ aberta
11. **`reimplementacao_provas_reais.py`:** resolução real confirma δ=4/0, G=4, RBT, Con T0/T1
12. **`12_NOTA_CURTA_...`:** δ/RBT=NR busca inicial; ρ_b≠P–W; ressalvas explícitas
13. **`13_...`:** **RCS CONFIRMADA** — δ_F≠δ_S, Φ fixa, slow vs fast
14. **PR12:** correções 01/06/03 **APLICADAS** (banners REJEITADO, Paper2=histórico)
15. **PR16 `16_...`:** RCS **ROBUSTA 4/4** (κ rich, razão 3:1, |W|=64)
16. **PR15 `15_...` + `lean4/.../Core.lean`:** esqueleto Lean — defs OK, sorries
17. **`14_...`:** R_w sobre **índices** (pós-suffix0); design
18. **PR17 `17_...` + `test_Rw_ppr2.py`:** PPR-2 **refinado (A∨B∨C)**; R_w identidade+sentinela **PASSA 3/3**
19. **PR18 `Core.lean`:** `delta_mono` **PROVADO** (sem sorry); `lemma3_con` → **axiom**; theorem4/rcs ainda sorry (fechados em PR21)
20. **PR20 `18_...` + `test_Rw_ppr2_E0E3.py`:** R_w + PPR-2 **PASSA 4/4** cenários E0–E3 (κ/razão/\|W\|)
21. **PR19 `19_...` + `ppr3_ramos_theta.py`:** Θ sobre provas de ramos; **CC-Θ 32/32**; \|Θ(π)\|=\|π\|+O(log\|W\|)
22. **PR21 `Core.lean`:** `theorem4_strict` e `rcs_exists` **PROVADOS sem sorry** (h1–h8; α=⌈κ/fastStep⌉, b=κ+1)
23. **PR22 toolchain + `lake build` LIMPO:** Lean 4.34.0 instalado; `delta_mono`/`theorem4_strict`/`rcs_exists`/`native_decide` **VERIFICADOS**; 0 sorry; lemma3=axiom
24. **PR23 cond. (B) RBT explícita:** w*='1000' ≠ w₀'; 10 disparos (6 puros B); PPR-2 20/20; CC-Θ 20/20 (`23_...` + `test_Rw_ppr2_RBT_B.py`)
25. **PR24 Foundation lemma3 + (C) ALL_COV:** `Lemma3Hyp` + **`lemma3_con` PROVADO** (0 axiom); `allCovered ⇔ δ=0`; limiar σ*=maxκ, b*=maxκ+1 (Lean+Python 4 perfis, EXIT=0) (`24_...` + `test_allcov_threshold.py`)
26. **PR25 Foundation instância + PR7:** clone Foundation; `FoundationBridge/FoundationInstance.lean` `lemma3Hyp` 0 sorry (Con/Prf/pad local); `fp_length_vs_delta.py` EXIT=0 — **PR7 SIM no modelo**; papers título FP+Con* corrigidos (`25_...`)
27. **PR26 revisão externa:** banners REJEITADO/orig. provisória/pseudocódigo aplicados sem redesenhar programa (`26_...`)
28. **PR27 Q+Gödel II+bridge+MO:** `TransferQ`/`transfer_lower_bound` em Core; `wStarObl`+`delta_ge_one` (lake EXIT=0); `GodelSecond.lean` Φw*:=T.consistent (build Mathlib pendente); rascunho `27_MATHOVERFLOW_PERGUNTA.md` **não postado** (`27_TEOREMA_Q_...`)
29. **PRÓXIMO:** `lake build` Foundation/FoundationBridge; rota B padding w*; (τ_n,q) concretos antes de qualquer LB; postar MO só com confirmação

### 6.4. Medio prazo (3-6 meses)

1. **Busca bibliografica especializada** sobre FP-K antes de reivindicar prioridade
2. **Postar** no MathOverflow (tag proof-theory) — como PERGUNTA
3. **Colaborar** com especialista (se possivel)
4. **Publicar** apenas se houver resultado formal verificado

### 6.5. NAO fazer

- Nao tratar Teoremas 4-6 como provados
- Nao reivindicar originalidade da FP-K sem busca
- Nao adicionar conjecturas novas sem necessidade

---

## 7. Contatos

### 7.1. Jan Krajicek

- Email: jan.krajicek@protonmail.com
- Affiliation: Charles University, Prague
- Status: Contato publico (via paper)

### 7.2. MathOverflow

- Tag: proof-theory
- Formato: Pergunta formal com contexto
- Incluir: Referencias, o que ja existe, o que se pergunta

---

## 8. Arquivos no Repositorio

### 8.1. Papers (em `papers/`)

| Arquivo | Status |
|---------|--------|
| paper1_barreira_interpretabilidade.md | Atualizado com Krajicek (2023) |
| paper2_hierarquia_ordinal.md | Atualizado com slow consistency |

### 8.2. Documentos de Apoio (em `support/`)

| Arquivo | Conteudo |
|---------|----------|
| 00_avaliacao_novelidade.md | O que ja existe vs. o que e novo |
| 01_framework_estendido.md | Framework anterior (descartado) |
| 02_teoremas_principais.md | Teoremas anteriores (descartados) |
| 03_meta_complexidade_aplicacoes.md | Aplicacoes (especulativas) |
| 04_questoes_abertas_referencias.md | Questoes abertas e referencias |
| 05_verificacao_lean4.md | Verificacao e plano Lean 4 |

### 8.3. Arquivos Raiz

| Arquivo | Status |
|---------|--------|
| README.md | Atualizado |
| INDICE.md | Atualizado (v6.15) |
| **EVOLUCAO_PROJETO.md** | **NOVO: histórico vivo (ideia→provas→aberto→mudanças de rumo)** |
| CONTINUIDADE_PESQUISA.md | Este arquivo |
| CONJECTURA_FP_K.md | Rebaixada para PERGUNTA DE PESQUISA |
| 07_pontos_fixos_incompletude.md | Parte 2: pontos fixos, física, analogias |
| 08_PROGRAMA_INTERPRETABILIDADE_VS_GERADORES.md | PPR: τ-corrigido, R1/R2 provados, R3 aberto |
| **09_EVOLUCAO_PERFIL_REFLEXAO_GERADORES.md** | **NÚCLEO ATUAL: g^{a,b}, δ, 𝒢, ρ_b, RBT (Teo. 2, Lema 3, Teo. 4)** |
| **10_EXPERIMENTO_GERADORES_FINITOS.md** | **EXPERIMENTO: enumeração n=8..16, δ/𝒢/RBT, busca R; varredura bib. δ/RBT=Não encontrado** |
| **14–19, 23–25** | **R_w, PPR-2, E0–E3, Θ ramos, cond.(B) RBT, Foundation+(C), inst.FP** |
| **lean4/** + toolchain | **lake build LIMPO (PR24); 0 sorry; 0 axiom; lemma3=teorema; FoundationInstance 0 sorry** |
| **Foundation/** | **clone Saitou–Noguchi (c69c68c); path require** |
| **fp_length_vs_delta.py** | **PR7 EXIT=0 — separação FP visível em δ (modelo)** |

---

## 9. Citacoes Obrigatorias (corrigidas pos-auditoria)

Se este trabalho for publicado, CITAR:

1. **Krajicek, J. (2025).** "A Proof Complexity Conjecture and the Incompleteness Theorem." JSL 90(3), pp. 1206-1210. arXiv:2303.10637
2. **Krajicek, J. (2025).** "Proof Complexity Generators." Cambridge UP, LMS Lecture Notes 497
3. **Beklemishev, L.D. (2005).** "Reflection principles and provability algebras..." Russian Math. Surveys 60(2), pp. 197-268
4. **Freund, A. & Pakhomov, F. (2020).** "Short proofs for slow consistency." Notre Dame J. Formal Logic 61(1), pp. 31-49
5. **Krajicek, J. (1997).** "Interpolation theorems, lower bounds..." JSL 62(2), pp. 457-486

---

## 10. Nota Final (apos auditoria + nucleo 09)

Este projeto percorreu 4 fases:

1. **Ideia original** (ordinal ⟹ escala exponencial) — DESCARTADA
2. **Auditoria** (22/09) — Teoremas 4-6 rejeitados, FP-K rebaixada
3. **Programa PPR** (08) — ≼_ppr definido; bloqueio min_lex identificado; R1/R2 provados
4. **Espectro de Reflexao** (09) — nivel intermediario: δ, 𝒢, ρ_b, RBT; Teo. 2, Lema 3, Teo. 4 provados

**Honestidade:** Temos provas elementares novas (T9-T15 no INDICE), nao um teorema grandioso. O nucleo atual e falsificavel e verificavel.

**Proximo passo real:** `10_EXPERIMENTO_...` + busca bibliografica sobre δ/RBT.

**Historico vivo:** `EVOLUCAO_PROJETO.md` (atualizar a cada passo).

**Principio:** Nenhum resultado sera' teorema sem especificacao formal completa.

---

## 11. Parte 2: Pontos Fixos e Fisica (adicionado)

Nova linha de trabalho separada da Parte 1:

| Status | Itens |
|--------|-------|
| **TEOREMAS** | Prop. 1-3, Choquet-Bruhat-Geroch, Markov, Tarski, corolario Goedel-Turing |
| **ANALOGIAS** | Incompletude geodesica ~ logica; universo de Goedel ~ fisica real; Stone ~ espaco-tempo |
| **CONJECTURAS** | Censura ~ Malament-Hogarth; fisica ~ aritmetica; Teorema da Incompletude Cosmologica |

**Documento:** `07_pontos_fixos_incompletude.md`

**Proximo passo da Parte 2:** Checar a idealizacao de memoria ilimitada na Proposicao 3 na literatura; discutir papel do observador Malament-Hogarth.

---

**Autor do documento:** Euzebio Santos
**Data:** Setembro 2026
**Contato:** ebiossanto (GitHub)

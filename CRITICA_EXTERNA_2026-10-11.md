# Crítica externa de 11/10/2026 — análise pontual e resposta

> Documento próprio **(P)**, 11 Out 2026. Recebemos via autor uma **análise crítica
> externa** do repositório (revisão de estrutura + confronto das alegações com
> Krajíček, Pudlák e Beklemishev). Este documento registra o veredito ponto a ponto:
> **o que a crítica acerta e foi aplicado**, **o que já estava internalizado**,
> **o que está desatualizado/inexato**, e **as ações executadas**. Idioma: português
> (a crítica veio em português).

## §1. Veredito sumário

1. **A análise matemática da crítica é correta em essência** — e, o mais importante,
   **não nos pegou de surpresa**: os "teoremas que precisam cair" (Teoremas 1, 3, 3.3,
   4/4.1, 5, 6; g(P) canônica; MCSP/IPS) foram **retraídos pela própria auditoria
   interna em 22/09/2026** — tabela **DESCARTADOS D1–D6** do `INDICE.md` e banner de
   retração no topo de `02_teoremas_principais.md`. A crítica revisou o **Eixo 1**
   (programa exploratório, set/2026) e **desconhece o Eixo 2** (campanha DD_P,
   out/2026 — a linha atual), que já opera exatamente no "modo programa de pesquisa"
   que a crítica recomenda (referee hostile, marcação (A)/(P)/(C), afirmações
   condicionais, residuais marcados, carta ao especialista **enviada**).
2. **A crítica acerta em 3 problemas reais de higiene**, todos aplicados hoje
   (§4): README desatualizado; arquivo com espaço no nome; duplicação raiz↔`support/`.
3. **Algumas afirmações factuais da crítica estão desatualizadas ou inexatas**
   (§3): o README atual **não** declara papers completos nem "80% provado"; não
   menciona `OrdinalHierarchy.lean`; os `papers/` atuais já se declaram observações.

## §2. Tabela ponto a ponto

| # | Ponto da crítica | Veredito | Evidência / ação |
|---|---|---|---|
| 1 | §3.1 incompletude ≠ lower bound de prova | **CORRETO — já internalizado** | `INDICE.md` D4 (22/09): "contagem ≠ lower bound"; banner `02_teoremas_principais.md` L3–6; o Eixo 2 nunca dependeu disso |
| 2 | §3.2 `\|T_α\|` ambíguo (ordinal vs tamanho) | **CORRETO — já internalizado** | `INDICE.md` D4: "`\|T_α\|` ambíguo"; Teorema 4 REJEITADO |
| 3 | §3.3 "P interpreta PA" indefinido; mistura de categorias | **CORRETO — já internalizado** | `INDICE.md` D1 (Teorema 1 retraído) e D5 ("falta ponte teorias↔sistemas") |
| 4 | §3.4 "não completo e polinomial" (Cook–Reckhow embute completude; p-bounded ⟺ NP=coNP) | **CORRETO — já refletido** | README atual: "notas exploratórias, não papers comprovados"; nenhuma alegação de completude restou |
| 5 | §3.5 monotonicidade de provabilidade ≠ monotonicidade de dificuldade | **CORRETO — já internalizado** | `INDICE.md` D5/D6 |
| 6 | §4 "verificação de novidade concluída" é overclaim | **PARCIALMENTE DESATUALIZADO** | README atual: "CORRETA (mas pode já existir)"; `00_avaliacao_novelidade.md`; e a **carta a Krajíček (11/10)** é exatamente a "consulta ao especialista" que a crítica recomenda — **enviada** |
| 7 | §5 arquivo com espaço no nome | **CORRETO — APLICADO** | `git mv` → `goedel_complexity_paper_pnp.md`; ref corrigida em `INDICE.md` L93 |
| 8 | §5 duplicação raiz↔`support/`; qual é canônico | **CORRETO — APLICADO** | raiz (22/09) é mais nova que `support/` (20/09) e é a referenciada; snapshots movidos → `archive/support_2026-09-20/` + `archive/README.md`; `CONTEXTO_COMUM.md` corrigido |
| 9 | §5 README desatualizado / identidade trocada | **CORRETO — APLICADO** | README reescrito (§4): eixos 1 e 2, retrações D1–D6, estado DD_P, estrutura, ponteiros canônicos |
| 10 | §6 "reconstruir em 4 níveis (definições → fatos seguros → conjecturas → especialistas)" | **JÁ ADOPTADO na prática** | O método da campanha DD_P é isto: frentes A–N com referee hostile, marcação (A)/(P)/(C), resultados modestos e verificados (`DD_Res ∈ P`, Teorema K, L.1, M.2, N.1), **carta ao autor enviada** |
| 11 | §7 "rebaixar Teoremas 1–8 a conjecturas/condicionais" | **JÁ FEITO em 22/09** | D1–D6; `07`/`08` marcados sketch; MCSP/IPS = sketch/questão aberta |
| 12 | "README declara papers completos, 80% provado, verificação concluída" | **INEXATO (para o estado atual)** | README de set/2026 já dizia o contrário (L3, L16, L54–55); a crítica parece basear-se em snapshot anterior ou nos docs profundos |
| 13 | "`OrdinalHierarchy.lean` mencionado mas ausente" | **DESATUALIZADO** | README atual não o menciona; `lean4/Gothic_Generators/` tem `Core.lean`, `DDP.lean`, `DDP_Experiments.lean` |
| 14 | §"Teorema 3": separar gerador `g_T` / tamanho sintático / `s_P(τ)` | **CORRETO — e já a convenção do Eixo 2** | O Eixo 2 não usa `g(P)`; usa `δ_T(Φ,b)` (Krajíček, (A)) e mede tamanho de prova por `s_P`/refutação; a **convenção de código** é pergunta **Q3** da carta enviada |
| 15 | Proximidade com Pudlák maior que o admitido | **ACERTA em espírito** | `00_avaliacao_novelidade.md` já marcava originalidade "provisória"; o Eixo 2 evita a alegação ao trabalhar sobre um **artigo específico** e enviar as dúvidas ao próprio autor |

## §3. Onde empurramos de volta (afirmações inexatas)

- A crítica afirma que "o README declara os papers como completos… tightness 80%
  provado". **Isto não está no README vigente** (nem no de setembro): ele diz
  "Notas Exploratórias (não submetido)", "não papers comprovados", "Tabela de bounds:
  DESCARTADA", "Teorema 4.1: DESCARTADO". A crítica provavelmente leu um snapshot
  anterior (ou os documentos de suporte profundos, que carregam os rascunhos com os
  teoremas — hoje todos com banner de retração).
- A crítica avalia **apenas o Eixo 1**. O Eixo 2 (campanha DD_P, 14 frentes,
  referee por entrega, lacuna verbatim no artigo de 2026, nota enviada ao autor)
  **não é mencionado** — porque nasceu depois (out/2026). Qualquer avaliação de
  "prontidão para submissão" deve ser refeita sobre o Eixo 2, que é a linha viva.

## §4. Ações executadas hoje (higiene — as que a crítica acerta)

1. `goedel_complexity_paper pnp.md` → **`goedel_complexity_paper_pnp.md`** (referência
   corrigida em `INDICE.md`).
2. `support/` (snapshots de 20/09, duplicados e mais velhos que a raiz) →
   **`archive/support_2026-09-20/`** + `archive/README.md` explicando a canonicidade
   da raiz.
3. **`README.md` reescrito**: identidade correta do repositório (dois eixos),
   retrações D1–D6 explícitas, estado atual da campanha DD_P, estrutura canônica,
   ponteiro para este documento.
4. `CONTEXTO_COMUM.md`: linha de infraestrutura corrigida (docs canônicos na raiz).

## §5. Lições que ficam (adotadas)

1. **A crítica confirma a saúde do processo**: as retrações internas anteciparam-se
   ~3 semanas à crítica externa — o referee hostile interno cumpriu o papel.
2. **README é a capa pública** — deve ser atualizado a cada fase (agora: Eixo 2).
3. **Separação de noções** (independência / força teórica / demonstrabilidade /
   tamanho mínimo de prova) — já a disciplina do Eixo 2; manter.
4. Pendência: versão LaTeX consolidada + BibTeX continua **aberta** (a crítica tem
   razão) — relevante só quando houver submissão; o Eixo 2 é nota curta + carta,
   não paper.

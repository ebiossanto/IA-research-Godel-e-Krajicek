# Crítica externa de 12/10/2026 — análise pontual e resposta (2ª onda)

> Documento próprio **(P)**, 12 Out 2026. Recebemos uma **avaliação independente do
> repositório** (2ª onda; a 1ª está em `CRITICA_EXTERNA_2026-10-11.md`). A avaliação
> reconhece a melhoria metodológica e aponta **5 reservas principais** + um veredito
> final com direcionamento: *"o próximo passo decisivo não é adicionar mais
> conjecturas, mas obter uma auditoria externa independente da prova de
> `DD_Res ∈ P` e das frentes G–N, além de tornar a compilação Lean reproduzível
> em uma instalação limpa."* Este documento registra o veredito ponto a ponto e as
> **ações executadas em 12/10/2026**.

## §1. Veredito sumário

1. **A avaliação acerta nas 5 reservas** — todas aplicadas hoje (§3): a linguagem
   "RECOMENDADO" passa a ser explicitada como **revisão interna estruturada** (não
   peer review); `M.2` é **condicional à semântica de `τ_N`** em todo resumo; a
   compilação Lean foi **reproduzida nesta sessão** (§4) + instruções de build;
   os resultados PPR/RBT/CC-Θ são **reclassificados** como "verificados no modelo
   finito escolhido"; e os **três níveis de resultado** ganham seção própria
   (a ponte L2→L3 permanece **aberta e declarada**).
2. **A avaliação confirma os positivos**: retrações coerentes; estrutura séria da
   campanha DD_P; lacuna verbatim concreta; honestidade da frente N; `DD_Res ∈ P`
   "promissor, mas precisa de verificação externa".
3. **A ação decisiva gerada é uma só e foi executada**: o **pacote de auditoria
   externa** `AUDITORIA_EXTERNA_DDRES_G-N.md` — dossiê autossuficiente para um
   auditor independente verificar `DD_Res ∈ P` e as frentes G–N, com o que exatamente
   checar, o que é (A)/(P)/(C) e o que **não** é reivindicado.

## §2. Tabela ponto a ponto

### 2.1 O que a avaliação reconheceu (mantido, não alterado)

| # | Reconhecimento | Status |
|---|---|---|
| P0a | README reescrito corretamente (eixos, retrações, arquivamento) | mantido |
| P0b | Resultados antigos explicitamente retraídos (coerente com auditoria 22/09) | mantido |
| P0c | Campanha DD_P com estrutura séria (transcrição/reconstrução/conjecturas/abertos/referee) | mantido |
| P0d | `DDP.lean` formaliza corretamente, **no nível abstrato**, o núcleo proposicional | mantido |
| P0e | Lacuna `Log(M*)=Log(M')` → `i₀ ∈ M*` é concreta e relevante | mantido |
| P0f | Frente N: distingue `α` aberta / `Taut(α)` fechada / redução condicional / compressão aberta; **não afirma ter resolvido** | mantido |

### 2.2 As 5 reservas — veredito e ação

| # | Reserva da avaliação | Veredito | Ação executada (12/10) |
|---|---|---|---|
| **P1** | "RECOMENDADO"/"referee hostile" = revisão **interna**, não peer review; descrever como "aprovado por rodada interna de crítica estruturada" | **CORRETO — APLICADA** | Nota de status no topo de `RELATORIO_CONSOLIDADO.md` (§0), no `README.md` (§Aviso) e no `INDICE.md`; fórmula padronizada "**RECOMENDADO (revisão interna; não validado externamente)**" |
| **P2** | `M.2` (`C_{N_s} ≡ ⊥`) não deve ser resumido incondicionalmente: fecha sob `q` total, pode falhar sob `q` parcial com merge — enunciado correto é **condicional à semântica de `τ_N`** | **CORRETO — APLICADA** | Resumos corrigidos em `README.md` (item 5), `INDICE.md` (DD7), `RELATORIO_CONSOLIDADO.md` (§6.4 e §7): condicionalidade **Q1** (pergunta já enviada à carta) explicitada em todos |
| **P3** | Lean formaliza o núcleo **proposicional**, não complexidade (p-time, O(1) rodadas, NP≠coNP, Problema 2.1, modelos não-padrão **não** formalizados); compilação **não reproduzida na sessão do avaliador** (`lake` ausente no ambiente dele) | **CORRETO — APLICADA** | (a) lista do que **não** está formalizado, explícita, no `README.md`; (b) **compilação reproduzida em 12/10/2026 nesta sessão** (§4); (c) instruções de reprodução (`README.md` §Formalização) — basta `elan` (o `lean-toolchain` pin `v4.34.0` baixa sozinho) |
| **P4** | Testes PPR permissivos (`cond_C = (w0_Tp is None)`; `R_W=4`; `W_STAR='00'`; ramos de 4 bits); PPR-2/RBT/CC-Θ devem ser classificados como **"verificados no modelo finito escolhido"**, não como evidência de redução entre geradores reais | **CORRETO — APLICADA** | Caixa de classificação permanente em `EVOLUCAO_PROJETO.md` (§Caixa PPR — modelo finito) + nota no §Aberto experimental; a ampliação `w0_Tp is None` é **propriedade do modelo finito**, registrada como tal |
| **P5** | A campanha mistura 3 níveis: (L1) teoremas sobre fórmulas/resolução · (L2) resultados internos sobre modelos não-padrão de `T_PV` · (L3) consequências p/ NP/coNP/geradores/complexidade; **a ponte L2→L3 precisa ser demonstrada separadamente** | **CORRETO — APLICADA** | Seção **"Três níveis de resultado"** (`RELATORIO_CONSOLIDADO.md` §9.1 + `CONTEXTO_COMUM.md` §Regras): nenhuma afirmação do repositório vale como lower bound computacional sem a ponte; **a ponte está aberta e é o aberto de maior peso** |

### 2.3 Demais pontos

| # | Ponto | Veredito | Ação |
|---|---|---|---|
| P6 | `DD_Res ∈ P` "promissor, mas tratar como resultado próprio a submeter a verificação independente — a passagem do lema de recorte para a extração da sub-refutação merece leitura formal em **todas** as variantes de resolução, especialmente com **enfraquecimento** e **representações DAG**" | **CORRETO — REGISTRADO** | É exatamente o escopo da auditoria externa: `AUDITORIA_EXTERNA_DDRES_G-N.md` §A (checklist (a)–(d)); a frente C2 já isolou o mesmo ponto no `Res(k)` (obrigações (O1)–(O5), `C2_ddres_k.md` — referee 5 rodadas) |
| P7 | Teoremas K, L, M, N: "interessantes como argumentos próprios **condicionais**, ainda não estabelecidos externamente" | **CORRETO — REGISTRADO** | Fórmula padronizada em §0 do relatório e §Aviso do README; cada frente com seus condicionais no pacote de auditoria §B |
| P8 | Consequências para lower bounds e P≠NP: **ainda não demonstradas** | **CORRETO — JÁ DECLARADO** | `RELATORIO_CONSOLIDADO.md` §7 (condicional explícito: `(2.1)+(ST)⟹NP≠coNP`; `¬2.1⟹P≠NP`) — nenhuma delas é afirmada incondicionalmente; §9.1 reforça |
| P9 | PPR/RBT/RCS: **programa experimental**, não resultado de complexidade | **CORRETO — APLICADA** | Caixa PPR (P4 acima) |
| P10 | Próximo passo decisivo = auditoria externa de `DD_Res ∈ P` + G–N, e build reproduzível | **ACEITO E EXECUTADO** (o que depende de nós) | `AUDITORIA_EXTERNA_DDRES_G-N.md` criado; build reproduzido (§4); **a auditoria em si exige um externo** — vias possíveis listadas no próprio pacote (MO segue **congelado** até confirmação do autor) |

## §3. Fórmula de status padronizada (P1, P7)

A partir de 12/10/2026, em todo resumo de resultado do repositório:

> **"RECOMENDADO (revisão interna; não validado externamente)"** — a entrega
> sobreviveu a N rodadas de crítica estruturada adversarial **interna** (logs em
> `*_referee.md`). **Não** equivale a peer review nem a validação da comunidade.
> Resultados (P) condicionais continuam condicionais; nada aqui é lower bound.

## §4. Reprodução da compilação Lean (P3)

- **Ambiente**: Windows; `elan 4.2.4` (toolchain default **não** configurada — é
  o caso do avaliador quando `lake` "não está instalado": na realidade falta o
  `elan`, que é o instalador); `lean-toolchain` fixa `leanprover/lean4:v4.34.0`.
- **Reproduzido em 12/10/2026, nesta sessão**: `lake build` na raiz do repositório →
  `Build completed successfully (4 jobs)`, com **exatamente os 2 `sorry`s
  documentados**: `lean4/Gothic_Generators/DDP.lean:628` e `:690`. Nenhum `sorry`
  em `FoundationBridge/` (coerente com o "0 sorry" do PR27/PR28).
- **Como reproduzir (instalação limpa)**: (1) instalar `elan`
  (`https://elan.lean-lang.org` — no Windows, `winget install elan`); (2) clonar o
  repositório; (3) `lake build` **na raiz** (o `lean-toolchain` baixa a versão
  correta automaticamente; nenhum `elan default` é necessário por diretório).
  Esperado: sucesso com 2 warnings de `sorry` (DDP.lean 628/690).
- **O que isso NÃO prova** (P3): a compilação cobre o **núcleo proposicional**
  (`DD_P`: totalidade, solubilidade em `m` rodadas, lema de união) — **não**
  formaliza p-time, O(1) rodadas, p-boundedness, NP≠coNP, o Problema 2.1 nem
  modelos não-padrão.

## §5. Ação decisiva — pacote de auditoria externa

Seguindo o direcionamento da avaliação ("não adicionar mais conjecturas; obter
auditoria externa"), foi criado **`krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md`**:

- **§A — `DD_Res ∈ P`**: enunciado + prova em 4 passos + **checklist exato do
  que um auditor deve checar** (recorte/enfraquecimento em todas as variantes,
  DAG, pureza, extração da sub-refutação, bound) — os mesmos pontos que a
  avaliação nomeou.
- **§B — Frentes G–N**: cada frente com uma linha de enunciado, status
  (condicional/(C)/retraído) e **o que checar** — incluindo o condicional de `M.2`
  à semântica de `τ_N` (Q1) e o fato de `N2.3′` ser escopo-efetivo.
- **§C — O que NÃO é reivindicado**: nenhum lower bound; nenhum P≠NP; ponte
  L2→L3 aberta.
- **§D — Logística**: reprodução do build, logs de referee, contato.

**Vias de auditoria externa** (a cargo do autor): (1) resposta de Krajíček
(aguardando — Q1–Q4); (2) MathOverflow (**congelado** até confirmação);
(3) especialistas indicados pelo autor. O pacote existe para que qualquer uma
delas possa ser usada sem reescrever nada.

## §6. Status desta resposta

- Aplicadas: P1, P2, P3(a–c), P4, P5, P10(pacote+build).
- Registradas como escopo externo: P6, P7, P8 (já declarado), P9 (=P4).
- Nenhum resultado foi **alterado** — apenas sua **apresentação** ficou mais
  precisa (condicionais explícitos; níveis separados; revisão interna nomeada).

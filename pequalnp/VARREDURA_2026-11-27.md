# VARREDURA pequalnp.com — 27/11/2026 (26/11 → 27/11)

**Fonte:** `head.json` (ponto de entrada dinâmico) + snapshots baixados · **Método:** diff
programático (`pequalnp/_varredura_diff.py`, `pequalnp/_news_letters.py`) + artigos individuais.
**Snapshots novos (sha256 16):** `overview_novo 124A0B784E1CDDB6` · `plan_novo FC7529DB36718FC3`
· `graveyard_novo 65AD7A0AA7D8F30C` · `news_novo 3BFC747B5DF5B5CE` · `letters_novo 57590F761C030A16`
· `head_novo 358197D23D03DF48` · `plan_v2 95B8A1E85377` (nome do arquivo) · `eliminated 04F970F63533`.
**Papers:** hash `a2e9f3f7dded` **inalterado** → **sem Note 2** ainda.

---

## 1. O que mudou (deltas verificados)

### 1.1 Contadores (head.json, 27/11 13:14Z)
`checked 12.776` (≈ +464 vs 26/11; **60/hora**) · `conjecture 6.223` · `refuted 5.205` ·
`lemmas 24.589` · `outside: 962 contribuidores` · `kills: 10 hoje, mediana de vida 2 min`.
**Relançamento do site:** "The open lab for frontier problems" (menu **Causes** novo; P vs NP
virou "uma causa" entre outras — matemática/medicina além). `plan_v2` apareceu como export novo.

### 1.2 Programas (overview 26→27/11)
| Programa | Δ checked | Δ conjecture | Δ refuted | Nota |
|---|---|---|---|---|
| meta_complexity | **+399** | **−191** | +10 | varredura pesada (conjecturas virando refutação/check) |
| library | **+42** | **+117** | — | biblioteca em expansão |
| circuit_lower_bounds | **+15** | **+33** | — | **target `L-clb-036` `in_work → conjecture`** ("no seat on it today") |
| proof_complexity | **+8** | **+28** | — | linha `proof-complexity` `dormant → support` |
| p_eq_np_search | 0 | 0 | 0 | parado |

### 1.3 Linhas de ataque (overview)
- **`candidate-family` → `first line`** (prioridade máxima agora): regra de 5 bits ligada à
  tabela 32×32 com circuito aceito de **≤201 portões AND/OR** (artigo A-062: alvo publicado
  09:07, batido às **09:59**); +10 rows (L-meta-25483…25498, L-lib-372).
- **`proof-complexity` → `support`** com rows novos **`L-pcx-203`, `L-pcx-204`** — "como uma
  restrição em arestas afeta a contagem de linhas de uma refutação; uma simulação geral
  compararia fórmulas de pombal **sparse × complete**".
- **`clean-ands` → `stopped`**: `L-meta-25474` mostrou grafo (lados ≤6) onde acender aresta
  ausente com AND **reduz** portões → **a simplificação proposta morreu para todo grafo**.
- **`small-circuits-found` → `stopped`**; `several-outputs-product` → `support`.
- `not-gates-on-the-promise` +3 rows (**L-meta-19361, 19158, 19159**); `above-three-a-vertex`
  +6; `gates-removed-one-input-at-a-time` +5; `candidate-family` +10.

### 1.4 `plan_v2` (export novo — plano estratégico versionado, 27/11 07:03Z)
- **BET** (apostas duais): lado "not equal" = grafo explícito caro em **inputs "one-a-side"**
  (uma linha + uma coluna ligadas) + conta exata do que NOT economiza; lado "equal" = famílias
  onde NOT **diminui** muito o circuito.
- **RULED_OUT** (com data e rows): argumentos de contagem na coroa (circuito de ~3n checado,
  `L-meta-19062`; piso 4n−6 **refutado**, `L-meta-18140`) — 26/11 · tabelas exatas ≤9 inputs
  paradas · "overhead da conversão" parado.
- **DECISIONS**: cada linha deve justificar em 1 frase o que dá *acima de linear* ou *com NOT*,
  senão é retirada (26/11).
- **WOULD_CHANGE** (gatilhos de vigilância): grafo >4 portões/vértice → linha N1; NOT
  economizando > 2n−5 (`L-meta-19158` refutado) → linha N2; circuitos do candidato N4
  continuando a encolher.

### 1.5 News (16 artigos 26–27/11 — `news_novo.json`)
| Artigo | Data | Conteúdo |
|---|---|---|
| **A-064** | 27/11 | **`L-pcx-205`**: cláusulas em 3 switches consecutivos de um anel ⇒ **refutação Res ≤ 48n+1 linhas** (upper bound de comprimento!) |
| A-065 | 27/11 | cutoff exato 5/8 (economia exponencial abaixo dele) |
| A-063/A-062 | 27/11 | candidato: 1.024 questões → 201 portões; chaves >10²¹ |
| **A-060/A-052** | 26–27/11 | **4 famílias**: sem NOT exatamente `2n−1`; com NOT **≤4 portões** (economia gigante) |
| **A-056** | 26/11 | **complemento do matching N×N: ≥2N portões MESMO com NOT**, N≥3 (em N=5: nenhum circuito ≤9) |
| A-057 | 26/11 | piso `n+m−2` vale também **com** NOT (grafos sem linhas/colunas repetidas) |
| **A-054/A-053** | 26/11 | **custo EXATO** de grafos escada (chain graphs): piso = teto, chequeado em Lean em todo tamanho |
| A-059 | 26/11 | **"quatro pontes entre formas de contar portões"** (medidas/vocabulário) |
| A-055 | 26/11 | 3 regras de monotonicidade (cortar grafo nunca encarece) |
| A-051 | 26/11 | contribuidores acharam circuitos menores que os "grafos duros" da estratégia |

⚠️ **Ressalva de modelo:** todos os novos resultados de custo exato são no modelo
**"one-a-side inputs"** (uma linha + uma coluna ligadas) — **diferente** do Note 1 (inputs
completos). Calibração D4′/minref deve tratar como classe separada.

### 1.6 Letters (export novo)
- **LT-002/003 — `|E| + τ(G) − 1` (função aresta) enviado a especialista → `replied`** (nosso
  campo de citação (A) ganhou potencial resposta de especialista!).
- LT-004 (`hardness of deciding circuit acyclicity`) — `replied`.
- LT-001 (algebraic complexity) e LT-005 (formal verification) — `sent`.
→ **Modelo exato para o nosso follow-up Q2–Q4 da carta a Krajíček.**

### 1.7 Novos exports de dados (todos baixados)
`graveyard` (**5.209 refutados**, 22–27/11: L-meta 5.143 · **L-pcx 40** · L-gct 21 · L-alg 3 ·
L-lib 2 — formato `[id,'r',null,epoch,hash]`), `eliminated` (vazio), `news`, `letters`,
`plan_v2`, `atlas`, `vocabulary`.

---

## 2. O que é USÁVEL no nosso trabalho

| # | Info nova | Uso no projeto | Prioridade |
|---|---|---|---|
| **U1** | **`L-pcx-205`** (anel: refutação ≤ `48n+1`) + **`L-pcx-203/204`** (restrição→linhas; sparse×complete PHP) | **Eixo minref/DD**: candidatos (A)-nc para comparar com `gk_minref` em fórmulas de anel; possível fonte de hipótese (C) sobre comprimento vs estrutura | **ALTA** |
| **U2** | Custos **exatos** novos: escada (A-053/054), complemento do matching ≥2N com NOT (A-056), `2n−1` vs `≤4` (A-052/A-060) | **Ground truth** para D4′/pontes — **com a ressalva do modelo one-a-side** (classe nova, Note 1 é full-input) | **ALTA** |
| **U3** | **`plan_v2`** (BET/RULED_OUT/DECISIONS/WOULD_CHANGE) | Modelo de **graveyard estratégico** p/ nossos D1–D6 + **watchlist de gatilhos** (o que faria a linha mudar) | **ALTA** |
| **U4** | Letters LT-002/003 **replied** sobre `|E\|+τ−1` | (a) citar a resposta quando publicada; (b) **modelo de carta** para Q2–Q4 (formato: why/redacted/outcome/next) | MÉDIA |
| **U5** | `L-clb-036` `in_work→conjecture`; `clean-ands` morto por `L-meta-25474`; `small-circuits-found` parado | Atualizar status no `PEQUALNP_MAPA.md` (§ abaixo) | MÉDIA |
| **U6** | Endpoints de monitoramento: `head.json` (contadores+mapa de arquivos), índice de `news` (artigos com `covers`), `plan_v2`, `letters`, `graveyard`, `eliminated` | **Varredura futura vira script** (estes 2 scripts já rodam nos snapshots) | MÉDIA |
| **U7** | Relançamento ("open lab", Causes) | Muda o contexto de citação do site (não é mais "só P vs NP") — registrar na citação | BAIXA |

## 3. O que NÃO há (para não prometer)

- **Sem Note 2** (hash de papers inalterado) — Note 1 segue único.
- **Sem mudança nos alvos grandes**: `L-pcx-071` (hard link Res(+) dag-like) segue `conjecture`;
  `L-clb-036` segue aberto (agora `conjecture`, sem agente).
- **Sem P≠NP/NP≠coNP** alegado em lugar nenhum (guarda P5/P6 continua verde).

## 4. Ações tomadas nesta varredura

1. Snapshots novos + artigos A-054/A-056 salvos em `pequalnp/` (evidência com sha256 §topo).
2. Scripts `pequalnp/_varredura_diff.py` e `pequalnp/_news_letters.py` mantidos (reexecutáveis).
3. **`PEQUALNP_MAPA.md` §7**: status de `L-clb-036`, morte do `clean-ands` e linha `proof-complexity`
   atualizados (abaixo).
4. Próxima varredura sugerida: `head.json` → comparar `files.map/plan/papers` — se `papers.*`
   mudar de hash = **saída de novo paper** (alerta automático candidato a CI noturno).

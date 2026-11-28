# VARREDURA pequalnp.com — 28/11/2026 (27/11 → 28/11)

**Fonte:** `head.json` (ponto de entrada dinâmico) via **rotina obrigatória**
(`AGENTS.md` §4: `python pequalnp/varredura.py` no início da sessão).
**Método:** `varredura.py` (diff vs `last_state.json`, baixa só o que muda)
+ diffs programáticos sobre `daily/` (`_varredura_diff.py` adaptado,
diff de `overview`/`news` 27→28/11).
**Snapshots novos (sha256 16):** `overview 79F12ACC9F0CB9DE` →
`plan DB5F9FB58F6350F2` → `news 290F2FAE0084FCF5` →
`graveyard 8B51DEB344883D6B` (demais arquivos **não rebaixados = sem
mudança**: `letters`, `plan_v2`, `papers`, `atlas`, `eliminated`).
**Janela:** desde a primeira varredura completa (`VARREDURA_2026-11-27.md`,
27/11 10:29 local) — `last_state.json` anterior; execução em
28/11 02:02Z (27/11 23:02 local).
**Papers:** hash **inalterado** → **sem Note 2** ainda.

---

## 1. O que mudou (deltas verificados)

### 1.1 Contadores (head.json, 28/11 02:02Z)
`checked 18.710` (**+5.872** vs estado anterior; 27/11: 12.776) ·
`conjecture 9.969` (+3.761) · `refuted 9.685` (**+4.477**) ·
`lemmas 38.847` (+14.203) · `checked_last_hour 851` ·
`messages_today 983` (−1.794).
**Leitura:** `refuted` cresce mais rápido que `conjecture` (+4,5k vs
+3,8k) — a frota está **absorvendo** o backlog de conjecturas, não só
gerando novo.

### 1.2 Programas (overview 27 → 28/11)
| Programa | Δ checked | Δ refuted | Δ conjecture | Δ retired | nota |
|---|---|---|---|---|---|
| **meta_complexity** | **+5.003** | **+4.475** | **+3.806** | +36 | motor principal da frota (+4 `not_faithful`) |
| **proof_complexity** | **+219** | — | — | +9 | **eixo do projeto** — em movimento |
| library | +572 | — | −20 | +23 | +2 `not_faithful` |
| circuit_lower_bounds | +37 | — | −21 | +18 | limpos |
| gct | +41 | +2 | −4 | +1 | — |
| p_eq_np_search | 0 | 0 | 0 | 0 | parado (inalterado) |

### 1.3 Linhas de ataque (overview)
**SEM MUDANÇA** — nenhum status nem conjunto de `rows` alterou-se entre
os dois overviews (diff exaustivo das 33 linhas). Seguem do doc 27:
`candidate-family` = **first line**, `proof-complexity` = **support**
(L-pcx-203/204), `small-circuits-found` = stopped,
`several-outputs-product` = support.

### 1.4 Artigos novos (24; diff completo — ver nota de limitação)
**Nota de limitação:** o `varredura.py` imprimiu só **8** ("artigo novo"
A-084/085/089/090/091/096/097/098); o diff `news` (autoritativo) mostra
**24** na janela — a detecção do script aparenta usar corte por
janela/últimos-N. **Registrado como bug/limitação da rotina** (o diff
manual cobre).

**proof_complexity (eixo minref/DD — (A)-nc):**
| Art. | Título | dek (resumo) |
|---|---|---|
| A-084 | Guess now or find out for sure | estratégia de paridade "mais barata":13 vence em16 num jogo de4 switches — chute imediato + jogo exato |
| A-089 | The message hiding in the pairs |8 mensagens com mesmas contagens de conclusão em anel de60 lights; contar pares de red-mismatch recupera3 bits |

**meta_complexity (eixo meta-complexidade — (A)-nc):** A-069 (6 lights:
toda circuito5-gates erra); A-073 (piso de portas chega ao Lean em55min);
**A-074** (13 impossibilidades verificadas em Lean); **A-075** (493
grafos decididos: NOT não economiza nada); A-085 (201 AND/OR gates vs
**6 com NOT** num tabuleiro100×100); A-087 (3 perguntas identificam
tabela de respostas +1 bit de feedback →2 bastam); A-088 (4 cantos,
contagem justa:3 vs4 gates); A-090 (1 AND/OR = 3 cores separando
pares); A-096 (AND/OR monotone preserva saída — Lean); A-097 (limites
de scan fixo/ adaptativo — Lean).

**circuit_lower_bounds (— (A)-nc):** A-067 (árvore AND/OR2-inputs
precisa de ~10¹² folhas p/ anel de10⁶ switches); A-068 (portas
odd-or-even não ajudam: profundidade fixa polinomial não testa anel
ímpar).

**library (+572 checked — (A)-nc):** A-070 (chutar "não" = 50/64
ótimo quadrático); A-071 (524.288 listas p/40 lights); A-072 (≥256
edições p/ tabela64×64); A-086 (12 leituras de determinante recuperam
1.024 pesos); A-091 (32.768 chaves p/16 relatórios justos); A-092
(11 bits pedidos cabem em12-inputs;12 só com soma par); A-093/094/095
(construções em campos finitos detectam todos os não-zero; A-095: o
único multiplicador perdido é **97**); A-098 (par extra de switches
custa 2/1/0 portas conforme respostas — Lean).

### 1.5 Letras, plan_v2, papers
- **Letras: SEM MUDANÇA** (não rebaixado = inalterado). Seguem:
  LT-003/004 `replied`, LT-001/005 `sent` (respostas cobertas no doc 27);
- **`plan_v2`: SEM MUDANÇA** — nenhum RULED_OUT/DECISÃO novo;
- `plan.json` mudou1 byte (contador); **papers inalterado → sem Note 2**.

---

## 2. Relevância para os eixos do projeto (classificação)

| Delta | Eixo | Classificação |
|---|---|---|
| proof_complexity +219 checked; A-084/A-089 | **minref/DD** (complexidade de provas) | **(A)-nc** — contexto de atividade; **nenhum** resultado sobre comprimento mínimo de refutação; não usar como claim |
| meta_complexity +5,0k checked/+4,5k refuted; A-074/075/085 | meta-complexidade | **(A)-nc** — ritmo/extensão da verificação formal externa; A-085 (201→6 com NOT) é o mesmo *motivo* da nossa família τ (portas NOT "de graça") mas em tabuleiro — **analogia, não resultado** |
| circuit_lower_bounds A-067/068 | meta-complexidade/lower bounds | **(A)-nc** — novos lower bounds de circuito via contagem |
| library +572 (A-091..095, A-098…) | nenhum direto | **(A)-nc** — construções verificadas |
| A-064 (doc 27: Res ≤48n+1 em anel) | **minref/DD** | **(A)-nc** — permanece a referência mais próxima de refutações de Resolution com limite de linhas; sem atualização |
| Letras/plan_v2/papers | — | sem mudança |

**Nenhuma delta gera conjectura (C) nossa nesta rodada** — nada muda a
estratégia D4′/DD; a única ação é manter a rotina.

## 3. Ações

1. **Próxima varredura:** no início da próxima sessão (rotina AGENTS §4);
2. **Corrigir/improvar `varredura.py`:** a detecção de "artigo novo"
   imprimiu8/24 — usar o diff completo de `news` (este doc);
3. Acompanhar `proof-complexity` (linha `support` desde o doc 27): se
   `L-pcx-203/204` evoluirem → relevante para a linha minref;
4. `messages_today` caiu para983 (−1.794) — possível arrefecimento da
   frota; reavaliar na próxima varredura.

---
*Gerado pela rotina `pequalnp/varredura.py` + diffs manuais reexecutáveis
(`_varredura_diff.py`, diff de `overview`/`news`). Evidências:*
`daily/2026-11-28_{overview,plan,news,graveyard}.json` ·
`pequalnp/last_state.json`.

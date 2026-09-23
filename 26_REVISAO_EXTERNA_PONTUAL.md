# 26 — Revisão externa: incorporação pontual

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** **REVISÃO EXTERNA RECEBIDA — só o pertinente aplicado (PR26)**
**Tipo:** parecer crítico (não é teorema do projeto)

---

## 1. Veredicto da revisão vs. estado do repo

A revisão externa **coincide em substance** com a auditoria interna de 22/09/2026
(`09 §33`, PR12). Não redesenhamos o programa; apenas fechamos inconsistências
editoriais que ainda sobravam.

| Crítica (§) | Já feito? | Ação PR26 |
|-------------|-----------|-----------|
| Teoremas 1–6 tratados como completos | Parcial (INDICE D1–D8; 01/06/03 PR12) | **Banners** em `00`, `02`, `04`, `05`, `support/*` |
| Limite exponencial sem justificativa | **REJEITADO** (PR12, 06, README) | Reforçado; Q1→teorema de transferência |
| Barreira de interpretabilidade = NP coNP? | **REJEITADO** (D1) | README já DESCARTADO; `00` corrigido |
| Gerador `Set.card` infinito / não computável | Marcado REJEITADO em `01` | Esqueleto Lean = **PSEUDOCÓDIGO** |
| TG sem parâmetro C_n | — | Anotado no esqueleto `05`/`support/05` |
| Monotonicidade ordinal não decorre de T⊆S | Resultado negativo em `08 §23` | Já registrado |
| RFN como 1 axioma / Nat ≠ ordinais | Anotado no esqueleto | Esqueleto = plano |
| `proofLength` Nat.find quebra | Anotado | Esqueleto = plano |
| Originalidade absoluta | FP-K rebaixada; **faltava** 00/05/paper2 | **CORRIGIDO** |
| Status inflado / sorry ≠ formalizado | Core.lean 0 sorry (finito) | Distinguir **modelo finito** vs PA |

---

## 2. O que a revisão pede e o que **não** fazemos agora

### 2.1. Aplicado (só pertinente)

1. Banners **REJEITADO/NÃO PROVADO** em `00_avaliacao_novelidade`, `02_teoremas_principais`;
2. `04_...`: Q1 reformulada (transferência Q, não tightness de T4); Fase 1 não "publicar barreira";
3. Originalidade → **provisória** em `05`, `support/05`, `paper2`, `06`;
4. Esqueleto Lean legado rotulado **pseudocódigo** (não "formalização");
5. Classificação: δ/𝒢/Lema 3/Teo 4 = **modelo finito verificado**; PA real = aberto.

### 2.2. **Não** fazemos (fora do escopo imediato / já é programa futuro)

- Reescrever todo o programa no núcleo da §12 da revisão (Ref_{T_k,P});
  — **coerente** com `09` + `08`, mas é redesign, não correção editorial;
- Provar teorema de transferência Q (ficou Q1 explícito);
- Submeter paper de limites inferiores (revisão: não publicável como teoremas);
- Eliminar Foundation/mathlib build (pesado, independente da crítica).

---

## 3. Núcleo que a revisão **não** descarta (e nós mantemos)

| Item | Classe |
|------|--------|
| Conexão conceitual reflexão↔geradores | Ideia de pesquisa |
| δ, 𝒢, ρ_b, RBT + Teo. 2 / Lema 3 / Teo. 4 | **No modelo finito** (Lean 0 sorry) |
| PPR R1/R2 | Provas elementares |
| RCS slow-vs-fast | Confirmada **no modelo** |
| FP 2020 (comprimento poly de Con\*) | **Teorema da literatura** |
| PR7: δ captura poly vs exp | **Verificado no modelo** (`fp_length_vs_delta.py`) |

**Confusão central da revisão (§14)** — adotamos como regra:
independência lógica ≠ não demonstrabilidade ≠ dureza computacional ≠ comprimento de prova.

---

## 4. Núcleo recomendado (alinhado à revisão §12) — STATUS

A revisão propõe progressão **finita** `T_{k+1}=T_k+RFN_Γ(T_k)` + famílias
`Ref_{T_k,P}(n)` + custo de tradução. Isso **já é a direção** de:

- `08` (PPR, transferência de hardness);
- `09` (δ/𝒢 sobre obrigações; Lema 3 Con);
- `15`/`24`/`25` (Lean + Foundation).

**Não é necessário abandonar** o núcleo; é necessário **não** reviver T4–T6.

---

## 5. Próximos passos (após revisão)

1. ~~Banners/originalidade~~ **FEITO (PR26)**
2. Foundation: sentença reificada Φw* (Gödel II) — **ABERTO**
3. Bridge Φ^{w*} ↔ obrigação δ — **ABERTO**
4. Escrever teorema de transferência Q (Q1) antes de qualquer limite inferior
5. MathOverflow: **pergunta** FP-K / δ, não "novo teorema"

---

## 6. Referências da revisão

- Cook–Reckhow (1979); NP=coNP e provas polinomiais
- Krajíček (2023/2025) — geradores, não barreira de interpretabilidade
- Freund–Pakhomov (2020) — comprimento, não δ
- Foundation / Saitou–Noguchi — 1º/2º IT em Lean (já clonado)

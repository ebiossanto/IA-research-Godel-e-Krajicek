# REFEREE — r4 do piloto prosa×Lean: fonte primária (arXiv v5) + cross-refs §9.2

**Rodada:** r4 · **Data:** 26/11/2026 · **Sucessor:** `PROSA_VS_LEAN_r3_p3b_E_Q24_referee.md`.
**Escopo previsto em r3:** diff das demais citações verbatim (§B-F1) contra a **fonte
primária** + verificações das cross-references do §9.2 (resumos com condicional τ_N).

## 1. Achados

| # | Achado | Evidência | Ação |
|---|---|---|---|
| **R4-1** ⚠️ | **Transcrição "verbatim" corrigida silenciosamente**: o artigo escreve **`i_o` (letra `o`)** em "But by (7) `io` is also already in M*", logo após usar `i_0` (zero) em "for some `i_0 < m`". O dossiê (§B-F1), `F_CONTEXTO_ATAQUE`, `G_CONTEXTO_FORCING` e a `CARTA_FINAL_ENVIO` usam `i_o` ✓ — mas **`A_teoremas_exatos.md:226` transcrevia `i_0`**, normalizando o original | **Fonte primária baixada**: `arXiv:2506.20221v5` HTML §3 (`fontes/arxiv_2506.20221v5.html`, 158.449 bytes, sha256 `E7282222…FC49`, 26/11/2026): `alttext="i_{0}<m"` e "But by (7) io is also already in M*" | ✅ **CORRIGIDO** em `A_teoremas_exatos.md` (`i_o` + nota *sic* datada) |
| **R4-2** ✅ | Contra a fonte primária, **toda a linha F1 se confirma**: v5 = **Theorem 3** (não 4), eqs. (7)/(8), Problem 2.1, "the negative answer implies P≠NP" (rodapé 2), Theorem 3: (ST) ⟹ NP≠coNP — e **a lacuna está no v5** | HTML v5 §3 | 🔧 **Nota de verificação adicionada à linha §B-F1** (fecha o item "O que o auditor checa" da própria linha) |
| **R4-3** ⚠️ | `RELATORIO §9.2(2)` citava "**§7.6**" como um dos resumos com o condicional τ_N — **§7 não tem subsections** (cross-ref quebrada); o condicional está no **§7 item 6** (linhas 324–327) | grep `^#{2,3} 7` = só `## 7.` | ✅ **CORRIGIDO**: "(§6.4, §7 item 6, README item 5, INDICE DD7)" |
| **R4-4** ✅ | §9.2(2) "todos os resumos": §6.4 ("CONDICIONAL à semântica de τ_N"), §7 item 6 ("parcial com merge pode falhar"), README item 5 ("sob `q` parcial com merge"), INDICE DD7 ("pode falhar → Q1") — **4/4 presentes** | P9 (novo) | ✅ Codificado como **P9** |
| **R4-5** ✅ | §9.2(1) "terminologia padronizada no §0, README e INDICE": marcador "peer review" nos **3** | P9 | ✅ Codificado |
| **R4-6** ✅ | Fragmento F1 nas 3 transcrições do repo (`F_CONTEXTO`, `G_CONTEXTO`, `A_teoremas` pós-correção), com normalização `∗≡*` | P3c (novo) | ✅ Codificado |

## 2. Correções aplicadas (r4)

1. `krajicek_ddp/A_teoremas_exatos.md` — `i_0` → **`i_o` (sic)** no trecho verbatim + nota
   datada do referee (a fonte primária manda).
2. `krajicek_ddp/RELATORIO_CONSOLIDADO.md` §9.2(2) — `§7.6` → **`§7 item 6`**.
3. `krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md` §B-F1 — nota de conferência contra o
   HTML v5 (fecha o checklist da própria linha).
4. `krajicek_ddp/fontes/arxiv_2506.20221v5.html` — **prova primária preservada** no repo
   (sha256 registrado acima).
5. `gk_prosa_lean_lint.py` — **P3c** (fragmento × 3 fontes) e **P9** (4 condicionais +
   3 terminologias); `norm()` agora trata `∗≡*`.

## 3. Autocrítica (r4)

- **(B1)** ~~o HTML da **v4** não foi baixado~~ → **RESOLVIDO em r5**: `fontes/arxiv_2506.20221v4.html`
  (156.939 bytes, sha256 `C1781BE1…C63E`) + **P10** do lint cobre as duas versões.
- **(B2)** P9 depende de **formatos de heading/lista** (`### 6.4`, `5. **Canto…`, `**DD7**`);
  uma renumeração futura do RELATORIO/INDICE **quebra alto** (fail) — é o desejado, mas exige
  atualizar o lint junto.
- **(B3)** O `i_o` do artigo é quase certamente **typo do autor** (i naught = `i_0`); não
  "consertamos" o artigo — registramos *sic*. Se o autor confirmar na errata, atualizar.
- **(B4)** P3c usa um fragmento hardcoded; uma mudança de redação do dossiê exige atualizar
  `F1_FRAGMENT` — aceitável (é literalmente a citação em disputa).

## 4. Veredito

**r4 LIMPO — P1–P9 todos OK (exit 0).** Registro de honestidade: esta foi a primeira rodada
com **fonte primária externa** no loop (arXiv HTML), e ela pagou: achou uma normalização
silenciosa numa transcrição rotulada verbatim.

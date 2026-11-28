# REFEREE — r3 do piloto prosa×Lean: P3b (diff completo) + frentes E/Q2.4 + taxas

**Rodada:** r3 · **Data:** 26/11/2026 · **Sucessor:** `PROSA_VS_LEAN_r2_frentes_G-N_referee.md`.
**Escopo (fecha as objeções abertas de r1/r2):**

1. **P3b — fecha a objeção R3 de r1** ("a transcrição verbatim foi conferida só pelos tokens").
   Implementado `_quote_blocks()`: extrai os 3 blocos de blockquote de `AUDITORIA` §A.1 e os
   3 blocos-fonte de `C_disjuncao_viavel.md` §2.2–§2.3, normaliza (sem `` ` ``/`*`/`>`, espaço
   único) e exige **igualdade total**, com localização da primeira divergência em caso de falha.
   **Sanidade do extrator auto-testada** (não passa por vazio): 385/332/425 caracteres,
   `igual: True` nos 3 pares. Resultado: **OK** — a transcrição de r1 é literal.
2. **P7 estendido** às frentes fora da §B: **E** (`E1–E5` + `passo (5)` + `frágil` — fecha o
   resumo do `INDICE.md` linha VERIFICADO) e **Q2.4** (`Pudlák` + `i-RFN` + `K19` + `(C)`,
   + **existência obrigatória do referee** `Q2.4_fonte_SIGMA1_referee.md`). Marcadores lidos
   antes de codificar (regra r2). Manifesto agora: **15 frentes/entradas**.
3. **P4 estendido** (objeção R4 de r1): `--replay` confronta além do `3000/3000` as **5 taxas**
   (847/436/289/1566/1485 sobre 3000) e as médias (`media |pi| = 7.0, max = 20`) do bloco §7.
   Resultado: **IDÊNTICOS**.

**Veredito: r3 LIMPO — P1–P8 (com P3b) todos OK, exit 0, com `--replay`.**

**Ainda aberto (fora do escopo desta r3):**
- **(A4 de r2)** CI roda sem `--replay` (P4 estendido é manual/sob demanda).
- **(R6 de r1)** `EVOLUCAO_PROJETO.md` não atualizado — decisão do autor.
- r4 previsto: aplicar P3-style diff às demais citações verbatim do dossiê (F1–Q2) e
  eventualmente ao `RELATORIO` §6–§8.

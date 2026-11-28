# REFEREE — r5 do piloto prosa×Lean: fonte primária v4 + v4↔v5 (fecha B1)

**Rodada:** r5 · **Data:** 27/11/2026 · **Sucessor:** `PROSA_VS_LEAN_r4_fonte_primaria_referee.md`.
**Escopo:** fechar a pendência **B1** da r4 (v4 do arXiv não baixada) e transformar a
conferência v4↔v5 em regra permanente.

## 1. Achados

| # | Achado | Evidência | Ação |
|---|---|---|---|
| **R5-1** ✅ | **A lacuna do passo (5) existe nas DUAS versões**: `But by (7) io i_{o} is also already in M* and hence by (8) we get:` — idêntica em v4 e v5 | HTMLs salvos: `fontes/arxiv_2506.20221v4.html` (156.939 bytes, sha256 `C1781BE1…C63E`) e `…v5.html` (158.449, sha256 `E7282222…FC49`) | ✅ **Linha §B-F1 agora RESPOSTA**: "é a mesma lacuna nas duas versões" (o item "O que o auditor checa" da linha foi respondido com fonte primária) |
| **R5-2** ✅ | **Renumeração confirmada**: v4 contém `Theorem 4`; v5 **não** contém e contém `Theorem 3` (o teorema principal com (ST) ⟹ NP≠coNP) | mesmo HTML, extração de texto visível | ✅ Confirma `CONTEXTO_COMUM` §11/10 ("em v5/LMCS o Teorema 4 da v4 é o Teorema 3") |
| **R5-3** ✅ | `Problem 2.1` presente nas duas (âncora do dossiê §B-F1/G2/rodapé 2) | idem | ✅ |
| **R5-4** 🔧 | A extração bruta de tags introduz espaços (`But by ( 7 )`, `i o i_{o}`, `M ∗ {\mathbf{M}}^{*}` — o HTML tem **dupla renderização**: itálico + MathML) — a checagem ingênua falhava | depuração da r5 | ✅ P10 usa comparação **sem espaços** (`Butby(7)`, `isalsoalreadyin`) — robusta à dupla renderização |

**Nota sobre o `i_o`:** o HTML confirma a dupla forma no próprio artigo — itálico `io` **e**
math `i_{o}` — na mesma frase (`i_{0}<m` no passo anterior com zero). O *sic* do r4 em
`A_teoremas_exatos.md` está corretamente ancorado.

## 2. Correções/aplicações (r5)

1. `krajicek_ddp/fontes/arxiv_2506.20221v4.html` — **prova primária v4 preservada** (sha256 acima).
2. `gk_prosa_lean_lint.py` — **P10** (`_visible_arxiv` + normalização sem espaços): lacuna
   nas duas versões, `Theorem 4` (v4) × `Theorem 3` (v5), `Problem 2.1` em ambas.
3. `AUDITORIA` §B-F1 — coluna "O que o auditor checa" virou **"RESPONDIDO"** com a evidência.
4. `PROSA_VS_LEAN_r4_..._referee.md` — pendência **B1 marcada como RESOLVIDA**.
5. Sonda descartável `_verify_arxiv.py` removida (P10 é a versão versionada).

## 3. Autocrítica (r5)

- **(C1)** P10 é **presença/ausência** — não valida que o *resto* do texto v4/v5 bate com as
  transcrições do repo (seria diff completo contra `A_teoremas_exatos.md`; tamanho/malha
  LaTeX inviabilizam sem alinhamento de frases — deixado explícito).
- **(C2)** Os arquivos HTML são evidência local; se o arXiv re-renderizar, sha muda. *Mitigação:*
  sha256 registrados nos referees r4/r5 — rebaixar exige nova rodada.
- **(C3)** `Theorem4` spaceless pode casar `Theorem 40` (não observado; risco aceito e
  registrado).

## 4. Veredito

**r5 LIMPO — P1–P10 todos OK (exit 0).** Pendência B1 do r4 fechada com evidência primária
dupla (v4+v5). **Estado do CI:** `claims-lint` roda `gk_claims_lint` + `gk_prosa_lean_lint`
(P1–P10) a cada push.

# REFEREE — r2 do piloto prosa×Lean: frentes G–N (AUDITORIA §B)

**Rodada:** r2 · **Data:** 26/11/2026 · **Sucessor:** `PROSA_VS_LEAN_piloto_referee.md` (r1).
**Alvo desta rodada:** tabela §B de `AUDITORIA_EXTERNA_DDRES_G-N.md` (13 frentes: F1, G1, G2,
H1, I1, J1, J2, L1, M, N1, N2, C2, Q2) + §D.2 (contagens de rodadas).
**Método:** sonda de marcadores (`_probe_frentes.py`, descartável) → calibragem → manifesto
`FRONT_MANIFEST` codificado no `gk_prosa_lean_lint.py` como **P7/P8** → leitura semântica dos
desvios.

---

## 1. Achados (frentes)

| # | Frente | Achado | Veredito/Ação |
|---|---|---|---|
| **R2-1** | **H1** | Linha §B dizia "Sem coleção sharply-bounded disponível; **convenção de abertas (§1.3)** (P)". O `H1_colecao_refutacao.md` (v2 pós-referee S1) **não contém** "convenção de abertas": seu §1.3 é a **retração da finitude → Questão Q-compactness aberta**; a indisponibilidade de BB é declarada em **`G2 §2.3` ("`R3 ≡ BB`")**. Cross-reference desatualizado (a v1 do H1 foi reestruturada pelo referee S1) | ⚠️→✅ **LINHA §B CORRIGIDA** (atribuição: retração/Q-compactness §1.3 + BB via `G2 §2.3`). É exatamente a classe de erro que o red team do pequalnp chama de "prosa diz mais que o artefato" |
| **R2-2** | **F1** | §B afirma "vale em v4 **e** v5/LMCS", mas `F1_verificacao_passo7.md` não cita v5/LMCS (é anterior). Suporte real: `CONTEXTO_COMUM.md:102–104` ("está em **ambas** as versões"; renumeração Thm 4→3) + `G_CONTEXTO_FORCING.md` §1.1 | ✅→🔧 **PONTEIRO ADICIONADO** na linha §B; P7 agora cobre `{F1: verbatim} ∪ {CONTEXTO: v5}` |
| **R2-3** | **N1** | §B pedia auditoria da "convenção aberta→fechada" sem ponteiro; a convenção vive em **N1 §0.3** (`Taut(α)` fechada × `α` aberta, FATAL-1). Literal `aberta→fechada` não existe em N1 (só em N2/CONTEXTO/RELATORIO) | 🔧 **PONTEIRO "(N1 §0.3)" ADICIONADO**; marcador P7 = `["N.1","N.2","fechada","§0.3"]` |
| **R2-4** | **Q2** | `Q2.1/Q2.2` não estão no arquivo raiz `27_TEOREMA_Q_...md` (que só existe como alvo de comparação) — os rótulos estão em `krajicek_ddp/Q2_instancias_tau_n_q.md` (§§2, 180) | ✅ **CONFIRMADO** (não é erro: §B aponta ambos, implícito); P7 cobre os dois arquivos |
| **R2-5** | **M** | Substantivo "condicional" ausente do `M_canto_adversarial.md`, **porém** a condição está explícita: "Ressalva de semântica (P)" (L108), "`q` **parcial** (merge) → o trap **pode abrir**" (L110/167), tabela L184 "Semântica de τ_N (q total vs parcial) — **aberta** — referee nº 1" | ✅ **CONFIRMADO** — honestidade presente; marcador P7 calibrado no **conteúdo** (`Ressalva`/`parcial`), não na palavra-chave do §B |
| **R2-6** | **§D.2** | "N2 = 5, C2 = 5, Q2 = 3, N1 = 2 rodadas" vs cabeçalhos reais: `N2_residuals_referee` "(rodada 5)" ✓ · `C2_ddres_k_referee` "rodada 5" ✓ · `Q2_instancias_referee` "rodada 3" ✓ · `N1_referee` "Veredito da rodada 2" (L272) ✓ | ✅ **CONFIRMADO** (4/4) — virou **P8** |
| **R2-7** | G1, G2, I1, J1, J2, L1, N2, C2 | marcadores todos presentes (`R3 ≡ BB`, `Teorema 2.1`+ZFC, `A.7`+ultrapoder, `Teorema K`+`K.2`, `K-FP`, `L.1/L.3/L.4`, `(C)`+omitente+`G_eff`+global, `(O1)–(O5)`+alternante+C2.3) | ✅ **CONFIRMADOS** |

**Nenhum achado altera uma claim matemática** — os 2 achados (R2-1, R2-2/R2-3) são de
**referência/attribution**, corrigidos na própria linha da tabela §B.

## 2. Correções aplicadas (r2)

1. `AUDITORIA` §B: linha **H1** reescrita (Q-compactness §1.3 + `G2 §2.3` para BB).
2. `AUDITORIA` §B: linha **F1** ganhou ponteiro da verificação v5 (`CONTEXTO_COMUM` + `G_CONTEXTO` §1.1).
3. `AUDITORIA` §B: linha **N1** ganhou "(N1 §0.3)".
4. `gk_prosa_lean_lint.py`: + **P7** (manifesto de 13 frentes × marcadores lidos) e
   **P8** (4 contagens de rodadas); docstring atualizada.
5. Marcador `**ambas**` (markdown bold) — lição de engenharia: marcadores devem ser colados
   do texto lido, nunca reconstruídos.

## 3. Autocrítica (objeções à r2)

- **(A1)** O manifesto P7 foi calibrado **por sondagem iterativa** — risco de *overfitting*
  (marcadores escolhidos depois de ver os arquivos). *Mitigação:* cada marcador é um conteúdo
  exigido pela linha §B; um marcador só entra se a §B o exige E o artefato o contém; nada foi
  afrouxado para esconder divergência (R2-1 foi **corrigido na prosa**, não no marcador).
- **(A2)** P7 checa presença, não verdade. A **matemática** das 13 frentes continua a cargo do
  auditor externo (§A.3/§B mantêm-se o contrato) e dos `*_referee.md` internos.
- **(A3)** Sonda descartável (`_probe_frentes.py`) **removida** após a calibragem — o manifesto
  codificado no lint é a fonte única e versionada.
- **(A4)** `--replay` (P4) **não** rodará no CI (custo + determinismo já verificado à mão em r1);
  mantido como verificação manual/sob demanda.

## 4. Veredito e promoção (decisão)

**r2 LIMPO — P1–P8 todos OK (exit 0).** Promovido, nesta entrega, ao **CI ao lado do
`gk_claims_lint`** (job `claims-lint`, step `gk_prosa_lean_lint`, sem `--replay`).
Reavaliação: qualquer FALHA de P1–P8 bloqueia o CI como o claims-lint já faz; extensões
previstas (r3): diff normalizado de P3 (objeção R3 de r1) e frentes restantes (C, E, Q2.4).

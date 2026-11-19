# Referee Hostile — C2_K19_5_7_TEXTO_EXATO

**Data:** 19/11/2026 · **Rodada:** r1 · **Alvo:** `C2_K19_5_7_TEXTO_EXATO.md`
(+ fontes `garlik_ccc2024.pdf`, `kra01_wphp.pdf`)
**Mandato:** atacar a transcrição das regras, a correção de atribuição, o
fechamento candidato de (O1)–(O4) e o ataque à família alternante.

---

## A. Achados

### A1 (GRAVE) — Transcrição das regras via OCR/layout pode ter errado a Weakening
A regra (3) `A ⟹ A∨B` foi reconstruída de um layout degradado. Se o original
for `A∨B ⟹ A∨(termo)` (insólida — descartada) ou outra, toda a §3 muda.

**Resposta:** **parcialmente respondida**: (i) a versão reconstruída é a
**única sólida** (demonstrado na §2); (ii) o layout extraído em modo *layout*
do PDF mostra `A` acima e `A∨B` abaixo do rótulo Weakening; (iii) **risco
residual declarado (G4)** — conferir no livro K19 ch5.7 quando houver acesso.
**Não promover a (A) definitiva sem o livro.** ✅ mantido como pendência.

### A2 — A correção "Lema 4.1 é nosso" pode ser errada: e se K19 ch5.7 tiver
*um* lema de projeção com outra numeração?
A §1 afirma que nunca houve lema de projeção em Krajíček. Mas não lemos o
livro — talvez ch5.7 contenha um lema (ex.: projeção de `R(f)` para FI) com
número diferente, e o autor da frente C2 o viu.

**Resposta:** **ACEITO com qualificação** — a §1 está ancorada em (i)
`C_disjuncao` linha283 ("não é discutido nas fontes que consultamos") e
(ii) Kra01 não tem "Lemma 4.x" (busca exaustiva no PDF: só Theorem 4.1).
Mas **a prova negativa é sobre as fontes lidas, não sobre o livro**.
**Correção aplicada:** §1 restringe a afirmação a "nas fontes obtidas"
(G4 cobre o livro). ✅

### A3 (GRAVE) — A passada reversa de demanda pode ser circular ou inconsistente
`(G1)` está declarado, mas a §3a afirma "toda demanda é satisfatível" com um
argumento informal. Contraexemplo candidato: linha `v` = ∧-intro cujo pai `u₁`
é **Cut** cujo `E` exigido para reter `termo(t)` conflita com a exigência de
**perda total** imposta por outro consumidor de `u₂`... (demandas conflitantes
em `u` de consumidores distintos).

**Resposta:** **ACEITO — é o achado central desta rodada.** Demandas de
consumidores distintos **podem** conflitar (um exige retenção, outro exige
perda-total para reuso). A §3 como escrita **não resolve conflito**.
**Estado real: (O1)–(O4) NÃO fecharam** — a §4 é *candidata* com esta
lacuna explícita. **Correção aplicada:** título da §4 alterado para
"Status candidato" (já era) e **(G1) reescrito** como *conflito de demandas*
não apenas satisfatibilidade. **Próxima rodada exige: ou política de
prioridade de demanda (consumidor mais próximo da raiz?) com prova, ou
contraexemplo computacional.** ✅ (registrado como bloqueante r2)

### A4 — Weakening com adição de termos exigidos pode violar pureza?
§3(b): `E(v) := E(u) ∪ {termos de B exigidos}`. Se `B` tem variáveis do lado
`j ≠ w(u)`?

**Resposta:** argumento na §4/G2: consumidores exigem pivôs que são
compartilhados entre os dois pais do consumidor → mesmo lado (Lema 4.2(2)
adaptado). Mas isso está **pressuposto**, não provado para `Res(k)`
(pivô = termo vs cláusula). **Bloqueante r2 junto com A3.** ✅

### A5 — Família alternante: a §5 não produz construção verificável ainda
Marcada como plano com teste N2 futuro — nenhum claim de sucesso. A
conjectura "promessa por construção" está marcada (C) e é falsificável.

**Resposta:** OK — nenhum abuso de escopo. O script `gk_alternating_family.py`
entra como pendência. ✅

### A6 — "Fecha" demais na tabela da §4
Várias células dizem "Fecha" sendo na verdade "fecha SE (G1)–(G3) fecharem".

**Resposta:** **ACEITO** — a tabela é "Status **candidato**" (título corrigido
em A3), mas o veredito executivo do documento deve espelhar isso. **Correção
exigida no corpo:** nenhum lugar pode dizer "C2.2 fechado" — conferido: §6
passo1 submete a referee antes de virar v6. ✅

---

## B. Veredito

**NÃO RECOMENDADO para fechamento (r1)** — mas **RECOMENDADO como avanço**:
a rodada entregou (i) **texto exato das regras (A)** com dupla citação;
(ii) **correção de atribuição** (Lema 4.1 = nosso); (iii) definição (P) de `E`
com passada de demanda; (iv) **identificação do bloqueante real**: *conflito
de demandas entre consumidores* (A3/G1) + pureza em `Res(k)` (A4/G2) — antes
não formalizados.

**Para r2 (fechamento):** resolver A3 (política de demanda com prova ou
contraexemplo exaustivo pequeno) e A4 (pureza `Res(k)`); conferir G4 no livro.
**Para a família alternante:** script N2 (§5).

**Regra de ouro mantida:** C2.2 continua **(C)** — nada de "teorema" até r2+.

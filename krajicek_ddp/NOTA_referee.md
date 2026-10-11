# Revisão da v3 (rodada 3) — NOTA_EDITORIAL_Krajicek.md (v3, §6 reescrito)

**Veredito da v3: REVISION (micro)** — fecharam **C1′, M2′, M4b, REG-1, REG-2/§6 e os
13 menores**; resta **1 MAIOR** (a *forma lógica* do fecho da dicotomia §1 — item 3 do pedido)
+ **1 regressão nova (REG-3)** + 5 nitpicks. Rodadas 2 e 1 preservadas abaixo.

Itens 1–7 do pedido, em tabela; depois o detalhe.

## 1. Quadro de fechamento da v3

| Pedido | Status | Evidência |
|---|---|---|
| **1. C1′** | **FECHADO** | §2(i) L74–79: "não refuta (ii) *per se* — refuta **(ii) junto de `(8)`/`(F-sent)` em `M′`** … (`G2` Cor 2.2)" + "nenhum método pode gerar `(F-sent)` junto do falsificador" + ressalva `G2 §2.5.1` (reductio sob `NP=coNP`) ✓ fiel a `G2` 2.1(a)/(b)/(a′)/Cor 2.2/§2.5.1; base `M⊨(S1)–(S4)` restaurada ✓ |
| **2. M2′** | **FECHADO** | §2(iii) L87–90: "(**(A)** L442: BB invalida a análise de `(1)` — perda de universalidade do KPT)" + "**(P)** `J1` K.2: `T_PV+BB+(S2)+(S3)+(S4)` é inconsistente — a segunda razão" ✓ separação (A)/(P) e escopo exatos |
| **3a. M4a** (leitura forte) | **FECHADO na definição; FALHA no fecho lógico (ver §2 abaixo)** | L42–47: leitura forte = "(i) sobre `M′` (verbatim *'preserves all Σ^b_1 properties…'*) **ou** (iii) = `M′∩m=M∩m` (`F1 (H)`)" — exatamente o pedido; cadeia contém um salto inválido (MAIOR-3) |
| **3b. M4b** (rótulos) | **FECHADO** | L43/45/46/51–53 + §4.3 L141 + §5 L159: itens **(i)(ii)(iii)** do Problema 2.1; "`(1)`…`(8)` = equações, com `(1)` = condição da análise KPT" ✓ = `A_...` L513–518/L442; escopo pendente declarado **em §1** ✓ |
| **4. REG-1** | **FECHADO** | L34–36: "(a)→`G1` Thm 4.3, (b)→`G2` Thm 2.1(b) — ambos impossíveis junto de (ii); a rota **por coleção** é a que `J1` K mata; **(c) é o único vivo**" ✓ (+ `(C→P)` na featura, L33) |
| **5. REG-2 + §6** | **FECHADO** | §6 L169–172 confessa "o §6 da v2 superestimou os fechamentos de C1 e M4"; L173–187 descreve v2→v3 com alvos e correções reais; nenhum fechamento infiel restou (1 omissão inocente: M2-partial da v2 não listado em v1→v2) |
| **6. Menores 1–13** | **13 de 13 aplicados** (2 com ressalva) | ver §3 abaixo |
| **7. Carta EN** | **PRONTA** (1 nit de inglês) | ver §4 |

## 2. MAIOR-3 (único bloqueio) — a cadeia de fecho da dicotomia **não está bem formada**

Texto (§1 L48–50): *"a leitura forte tornaria o Problema 2.1 negativo para esta instância ⟹
`P≠NP`. **Não reivindicamos `P≠NP`: a conclusão honesta é que a leitura forte não é a pretendida**
— daí a errata."*

O primeiro passo está certo (`leitura forte ⟹ ¬2.1(instância) ⟹ P≠NP`, rodapé 2; escopo com
hedge ✓). O segundo é **modus tollens sobre premissa epistêmica**: de "nós não reivindicamos
`P≠NP`" não se segue "a leitura forte não é pretendida" — isso exigiria **¬(P≠NP)**, que ninguém
tem (se `P≠NP` for verdadeiro, o silogismo não fecha). O `L1 §2` trata isso como **disjunção de
chifres** ("o artigo não pode ter ambas"), e é assim que precisa ser escrito.
**Correção (1 frase):** "**Ou** a leitura forte é a pretendida — e então, pelo rodapé 2, 2.1 é
negativo para esta instância e `P≠NP` se seguiria (consequência que o artigo não afirma e que
nós, sem uma prova, não reivindicamos); **ou** ela não é a pretendida — e então a direção da
errata é enfraquecer (i)/(iii) e o passo (5) é lacuna real. **Qual das duas você endossa? (§4.3)**"
+ manter o hedge de escopo. Com isso a dicotomia fica válida e vira pergunta, que é o tom do resto.

**NB de fidelidade (vinculado):** em "a configuração que o **item (5)** exige, `(ii)+(8)/(F-sent)`
**em `M′`**" — o item (5) exige `(8)` **em `M*`** com `i_0 ∈ M*` (`G2` 2.1(c)/Cor 2.2); `(F-sent)` em
`M′` é a forma (b), mais forte. E na leitura (iii) o refutador exato é **`G1` Thm 4.3** (não
`G2` 2.1). Corrigir a citação para "(G2 Thm 2.1(b)/(c); na leitura (iii), `G1` Thm 4.3)".

## 3. Regressão nova + menores

- **REG-3 (MENOR-MAIOR) — §2(ii) L82–83**: "`ν_G` leva `𝒯` a `M[G] ⊨ PV` **com `¬φ` satisfeito** —
  contradizendo `G2` 2.1(a′)". A contradição com 2.1(a′) exige **(1)+(2)** do `H1` Thm 1.1: `¬φ`
  **e `(F-sent)`** (vindo de `δ_N→τ_N`). Como está, repete em miniatura o erro de classe C1
  (falsificador sozinho ⟹ contradição). **Fix:** "… com `¬φ` satisfeito **e `(F-sent)`**
  (ramos `δ_N→τ_N`) — contradizendo `G2` 2.1(a′)".
- **M1..M13 (rodada 2): todos aplicados** ✓ — 1 §2(v) sem quantificador órfão; 2 escopo de `G`;
  3 base `M⊨(S1)–(S4)`; 4 rótulo do teorema (= `G2` Thm 4.1 restaurado); 5 `(L1)` teorema em
  [Kra98 §4] / `(C)`-livro; 6 citação `G2` Thm 2.1/Cor 2.2; 7 "K-FP′ + J.6-a′"; 8 verbatim
  integral com reticências; 9 §5 "lacuna é (A)"; 10 lacunas G2-R3; 11 ponteiro `L1 §5` nº 4;
  12 carta (a)✓ ancorada em v4 /(b) `M∗` só na citação, `M*` na prosa = aceitável /(c)✓;
  13 sem regressão em §3.3.
- **Nitpicks restantes:** (n1) §6 v1→v2 omite M2-partial (inocente); (n2) carta: "Theorem 4 **of
  the** v4" → "Theorem 4 **in arXiv v4** (renumbered as Theorem 3 in v5/LMCS)"; (n3) §1 L42 "i.e."
  → "i.e.,"; (n4) §2(iii) "padrão-muitos… o que morre" é lição do `J2` (fonte a nomear); (n5)
  §5(2) mantém "traduzir §§1–4" enquanto só há carta de §1 — prever o que entra da §2 (obstáculos)
  na carta final.

## 4. Carta EN (§1 L57–65)

**Pronta para envio após a revisão do usuário**, desde que MAIOR-3 seja aplicado ao **texto PT**
que a carta resume (a caixa EN não contém a dicotomia — não afirma `P≠NP` ✓). Conferido: numeração
✓ (ancorada em v4 + renumeração v5), tom ✓ (hedged, sem acusação, "Am I missing an argument?"),
sem backticks ✓, sem artefatos ✓, `(7)`/`Log` fiéis ao verbatim ✓. Só o nit (n2).

## 5. Veredito da rodada 3

**REVISION (micro)** — não REJECT (9 dos 11 itens das rodadas 1–2 fecharam de fato; o §6 é agora
honesto) e não APROVADO (resta **1 frase logicamente inválida no núcleo da errata** + 1 regressão
de classe-C1 em miniatura). Esforço restante: **1 reescrita (MAIOR-3) + 6 linhas (REG-3, n1–n5)**
→ então **APROVADO PARA REVISÃO DO USUÁRIO**.

---

# Revisão da v2 (rodada 2) — NOTA_EDITORIAL_Krajicek.md (v2, com §6 log)

**Veredito da v2: REVISION** (progresso real: C2, C3, M2′-parcial, M3, M5-partial, M6 fechados;
mas **C1 reabre como C1′**, **M2 vira M2′ (nova troca de autoria)**, **M4 não foi de fato
fechado** e o **§6 log superestima os fechamentos**). Rodada 1 preservada abaixo (título
"# NOTA_REFERE — … (rodada 1 — v1)").

Fontes (re)lidas: `G2` (Thm 2.1/4.1, §2.5), `G1` (Thm 4.3, Advert. 2.4), `H1` Thm 1.1,
`I1` (A.4–A.6, B.1–B.4, C.1), `J1` (K, K.2), `J2` (K-FP′, J.6-a′), `L1` (L.1, L.3′, L.3″),
`A_...` L442/L513–518 (Problema 2.1 = itens **(i)(ii)(iii)**), `G_CONTEXTO` §1.1 (v5 = Thm 3).

## 1. Quadro de fechamento (item a item do pedido)

| Pedido | Status | Evidência / resto |
|---|---|---|
| **C1** trio `T_PV`+falsificador+`(F-sent)` | **PARCIAL — reabre como C1′** | o trio está certo (G2 2.1(a)/(b)) ✓, mas a mesma frase acrescenta "**o que refuta a hipótese (ii) do artigo**" — falsa (ver C1′) |
| **C2** numeração 3(v5)/4(v4) | **FECHADO** | §0 L13–14, título §1 L19, carta L51–52 ("proof of Theorem 3") ✓ = `G_CONTEXTO §1.1` |
| **C3** I1 escopo+mecanismo | **FECHADO (1 resíduo)** | "ultrapoder de `ℕ` só" ✓, "venue `M_0⊨S` vivo (C.1)" ✓, A.4–A.6 × B.2/B.3 separados ✓; resíduo: "Em todo `M_0`" (ver MENORES) |
| **M1** no-G = `G2 2.1(a′)` | **FECHADO (escopo resta)** | §2(ii) ✓; ainda "qualquer `G`" sem "genérico/fechado sob EF" |
| **M2** K "coerente com, não idêntica à" | **FECHADO + REGRESSÃO (M2′)** | fórmula ✓, mas o corolário **nossо** foi etiquetado como L442 (ver M2′) |
| **M3** §3.1 (renumeração, (F-b'), (C)-livro, ZFC-falsa) | **FECHADO** | L89–95 ✓ todos os 4 |
| **M4** dicotomia §1 | **NÃO FECHADO (2 de 4)** | perna `⟹P≠NP` ✓, escopo em §1+§4 ✓; **definição da convenção** e **rótulos (i)(ii)(iii)** ✗ |
| **M5** K-FP′ "sem ¬φ" + `M_0⊨T_S` | **FECHADO (naming resta)** | L96–99 ✓; ainda rotulado só "K-FP′" (família = J.6-a′) |
| **M6** L.3″ + adversarial (C) | **FECHADO** | L105–107 ✓ |
| **M7** marcação (C) | **FECHADO** | `(C)`: featura de (c) implícita? — `(C)` explícito em §3.1 (livro), §3.3 (adversarial), §5(d) ✓ |
| **N1–N9** menores | **6 de 9** | N2 ✓, N4 ✓, N5 ✓, N7-partial ✓, N9 n/a; N1 trocado por link errado (ver REG-1), N3 parcial, N6 parcial, N8 ausente |

## 2. CRÍTICO (bloqueia o envio)

### C1′ — §2(i) L66–67: ainda afirma que **a hipótese (ii) do artigo é refutada**
> "A configuração `M' ⊨ T_PV` com `¬φ` satisfatível e `M' ⊨ (F-sent)` é falsa em ZFC — **o que
> refuta a hipótese (ii) do artigo** (2.1 com falsificador interno da semente enviada)."

A primeira metade está **correta** (= `G2` Thm 2.1(a)/(b)) ✓ — mas a segunda é falsa: a hipótese
**(ii)** do Problema 2.1 é só "`M' ⊨ T_PV` + `(¬φ) ∈ SAT`", e ela **não** é refutável (é o que o
`G2` Thm 1.1/`H1` **construem**; `G2 §2.5.3` diz que até `(F-sent)` nua é consistente). O que G2
refuta é **(ii)+(8)`/`(F-sent)` em `M'`** — e, no cenário em que o artigo aplica 2.1, a
**configuração que a prova do Teorema 3/4 exige** (`G2` Cor 2.2). Como está, a frase reaproveita o
erro da v1 por outro caminho e **implicaria `P≠NP` como teorema** (¬(ii) ⟹ ¬2.1 ⟹ rodapé 2) — o
over-claim que o §1 supostamente evita.
**Correção (sugestão):** "…é falsa em ZFC (`G2` Thm 2.1). Isto **não** refuta a hipótese (ii) *per
se*; refuta **(ii) junto de `(8)`/`(F-sent)` em `M'`** — exatamente a configuração que o item (5)
da prova precisa (`G2` Cor 2.2)."

## 3. MAIOR (corrigir antes do envio)

### M2′ — §2(iii) L76–77: **nosso** corolário etiquetado como `(A)` (L442)
> "(L442: **`T_PV+BB` é inconsistente com a semente**) — K exige `+(S2)(S3)(S4)` a mais."

Duas coisas trocadas: (1) **L442 não diz isso** — o artigo diz que BB *não é provável* em `T_PV`
"a menos que fatoração não seja difícil" e que *acrescentá-lo a `T_PV` invalida a análise de (1)*
por perda de universalidade do KPT; (2) a inconsistência `T_PV+BB+(S2)+(S3)+(S4)` é **K.2 =
nosso (P)** — e a frase seguinte a trata como acréscimo a uma base `T_PV+BB` já inconsistente.
Resultado: **(P) apresentado como (A)**, exatamente o que §5 L132–133 promete evitar.
**Correção:** "…coerente com, não idêntica à a remark do artigo (**(A)** L442: BB invalida a
análise de (1) — perda de universalidade do KPT). **(P)** `G1/J1` K.2: `T_PV+BB+(S2)+(S3)+(S4)`
é **inconsistente** — a segunda razão, ao nível da semente."

### M4a — §1 L40–41: a "convenção" **não foi definida** (objeção da rodada 1 mantida)
"sob a convenção **fechamento+`Log`+`(3)`** (com `(1)` entregando `(8)`)" é a redação da v1
rerotulada. O buraco é o mesmo: **`F1 §2` prova que (3)/`Log` sozinho não dá `i_0 ∈ M*`** — logo,
sob essa convenção literal, (1)+(2)+(3) **não** são inconsistentes e a dicotomia não se sustenta
(é o próprio objeto da errata). Falta dizer **qual leitura** torna-a forte, i.e.: ou
**(1) lida sobre `M′`** ("M′ preserves all Σ^b_1 properties of elements of M" — verbatim do §2 do
artigo, `F1 §6(c)` ⟹ `(8)` em `M′`, instanciável no `i_0 ∈ M′` — aí (3) fica **inocente**), ou
**(3) lida como `M′∩m = M∩m`** (F1 (H)) — em qualquer caso: "a leitura que faria o **passo (5)**
valer". Sem isto, o autor responde com a sua própria errata.
*NB:* com a leitura sobre `M′`, a inconsistência é **(1′)+(2)** (aí `Log`/(3) não entra) — decidam
qual das duas cadeias escrevem e coerenciem o "(3)" do enunciado.

### M4b — §1 L40–41: **rótulos não alinhados** com o artigo (o §6 afirma que sim)
O Problema 2.1 do artigo tem itens **(i), (ii), (iii)** (`A_...` L513–518); o rascunho escreve
"os itens **(1), (2), (3), (8)** da configuração do artigo" e o §6 L159 declara "rótulos
alinhados aos itens do artigo". No artigo, **(1) é a condição da análise KPT de [8,12]** (é ela
que L442 diz ser invalidada por BB) — num documento de errata, "(1)+(2)+(3)" será lido como as
equações/itens dele, não como (i)(ii)(iii). **Correção:** "(i)+(ii)+(iii) do Problema 2.1 (com
`(1)`… `(8)` = equações)" e alinhar §4.3.

### REG-1 — §1 L32–34: ligação reparos↔teorema aponta para o teorema errado (nova regressão)
A nota da rodada 1 diz: "os reparos que exigem coleção interna de falsificadores … são refutados
pelo **Teorema K**". Mas **(a)** `M′∩m = M∩m` é refutado por **`G1` Thm 4.3** e **(b)** `(8)` em
`M′` por **`G2` Thm 2.1(b)** — nenhum dos dois *exige coleção interna* (K proíbe um **função**
`F ∈ M_0`; (8) é um `∀∃`). A ligação que a rodada 1 pediu (N1) era **reparo (a)→G1 4.3, reparo
(b)→G2 2.1(b)**; "o reparo (c) é o único vivo" está certo, mas a causa citada é outra.
**Correção:** "(a) é refutado por `G1` Thm 4.3 e (b) por `G2` Thm 2.1(b) — ambos impossíveis junto
de (ii); a rota *por coleção* de falsificadores é o que `J1` K mata."

### REG-2 — §6 L146–161: o log declara fechamentos que não ocorreram
"C1 … corrigido" (é C1′), "MAIOR-6 … convenção definida … rótulos alinhados" (não; M4a/M4b),
"ligação reparos↔Teorema K" (REG-1). Um log de correções infiel é o mesmo defeito que o documento
combate. **Correção:** ajustar o §6 ao estado real (C1 **parcial**, MAIOR-6 **parcial**).

## 4. MENORES (nitpicks + pendências da rodada 1)

1. **§2(v) L82**: "Em todo `M_0`, nenhum ultrapoder de `ℕ`…" — quantificador órfão: B.2 não
   quantifica base alguma. Escrever "**Nenhum** ultrapoder `ℕ^ω/U` modela `S` (B.2)".
2. **§2(ii)**: "irrealizável por qualquer `G`" → "por qualquer `G` **genérico** (fechado sob
   EF-provability in `M`, contendo constantes-1)" (M1, escopo, ainda pendente).
3. **§2(i)**: hipótese de base omitida — `G2` 2.1 exige `M ⊨ (S1)–(S4)`; acrescentar
   "para a semente do artigo (`M ⊨ (S1)–(S4)`)" (a v1 tinha; a v2 caiu).
4. **§3.1 L89**: rótulo "**Teorema principal da §3**" é confuso → "o Teorema **4** do artigo (v4) =
   **3** (v5/LMCS)".
5. **§3.1 L95**: "`Log(M[G])=Log(M)` … **não afirmamos como teorema**" — subdeclara: é **teorema**
   na construção booleana de `[Kra98 §4]` (`G1` Thm 2.1) e **(C)** só **para a versão do livro**
   (`G1` Advert. 2.4). Sugerir: "(C) **para o livro**; teorema em [Kra98 §4] — mas é o livro que o
   artigo cita".
6. **§3.1 L92**: citação "ZFC-falsa (**G2 §2.5.1**)" → a falsidade é **Thm 2.1/Cor 2.2**; §2.5.1 dá
   só a legitimidade da reductio sob `NP=coNP`.
7. **§3.2 L96**: escopos ✓, mas o enunciado de família é **J.6-a′** (K-FP′ é por nome; "sem `¬φ`"
   só a família entra). Rotular "K-FP′ + J.6-a′".
8. **§3.4 L109**: aspas com reticências + paráfrase ("… **but always sound**" vs verbatim "but it
   will always be sound") — ou cita literal ou troca aspas por semicódigo.
9. **§5 L130**: "a **errata** … é produto da nossa equipe" — a lacuna é **(A)**; produto nosso é a
   **identificação** (a frase seguinte mitiga, mas a primeira mantém a confusão que §5 L132 critica).
10. **§5 lacunas**: continua sem os gaps declarados do **G2** (espelhamento `α_i↦α̃_i` não-padrão;
    passagem a semente infinita — referee R3) — N7 da rodada 1 só pela metade.
11. **§4.2** sem o ponteiro de localização do verbatim ("bits of α" = constantes, `L1 §5` nº 4) — N8
    não aplicado.
12. **Carta EN**: pronta no essencial (numeração ✓, tom ✓, sem backticks ✓, sem `P≠NP` ✓).
    Antes de enviar: (a) conferir no v5 que ainda é "**§3**, item (5)" (`G_CONTEXTO` confirma a
    citação literal, não o número da seção); (b) padronizar `M∗` (verbatim) vs `M*`; (c) opcional
    "(Theorem 4 in arXiv v4)".
13. **§3.3 / L.3″ / adversarial (C)**: fechado ✓ (sem regressão).

## 5. Veredito da rodada 2

**REVISION.** Motivo: os três críticos da v1 viraram **dois fechados + um reaberto em forma nova
(C1′)**; há **uma troca de autoria nova (M2′: K.2 dentro do parêntese do L442)**; **M4 (o núcleo
lógico da dicotomia) não foi fechado** — só ganhou escopo e perna `P≠NP`; e o §6 log **afirma
fechamentos inexistentes**. Nada exige reescrita: são **2 correções críticas + 3 médias + ~10
nitpicks**. Depois disso: carta EN (12) → envio.

**Ordem:** C1′ → M2′ → M4a → M4b → REG-1 → REG-2 → §6 honesto → menores 1–13 → revisão final.

---


# NOTA_REFERE — revisão hostil do rascunho `NOTA_EDITORIAL_Krajicek.md` (rodada 1 — v1)

**Veredito: REVISION** (não APPROVADO — há erro factual no teorema central; não REJECT —
estrutura, honestidade de processo e tom são salvos).

Arquivos-fonte lidos para conferência: `F1_verificacao_passo7.md` (§1–§6), `G2_semente_Fsent.md`
(Thm 1.1, 2.1, 4.1, §2.5, §5, §7), `G1_log_forcing.md` (Thm 2.1/(L1), Advertência 2.4, Thm 4.3,
Cor 4.4), `H1_colecao_refutacao.md` (Thm 1.1, §1.3), `I1_Qcompactness_ultrapoderes.md` (§0, §1
A.1–A.7, §2 B.1–B.4, C.3), `J1_Qcompactness_M0.md` (Thm K, K.2, J.2′, J′), `J2_ponto_fixo.md`
(K-FP′, J.6-a′, §1), `L1_phi_insatisfativel.md` (L.1, L.1′, L.3′, L.3a, L.3″, L.4, §2, §7c),
`A_teoremas_exatos.md` (L18–27, L151, L190, L341, L374–380, L442, L513–518),
`G_CONTEXTO_FORCING.md` (§1.1: renumeração v5), `F2`/`F_CONTEXTO` ((F-b')), `RELATORIO_CONSOLIDADO.md`.

---

## 0. Quadro-resposta aos cinco pontos de ataque

| # | Ponto | Veredito |
|---|---|---|
| 1 | Fidelidade dos teoremas por frente | **3 erros + 1 exagero + 3 escopos** — G2 (parêntese ERRADO), H1.1 (mecanismo ERRADO), I1 (escopo+MECANISMO ERRADOS), K ("reproduz a remark" = exagero); escopos: L.1 ("todo modelo"), K-FP′ ("famílias"/"todo M_0"), L.3′ (falta L.3″) |
| 2 | §1 errata / dicotomia / carta EN | **Dicotomia não reivindica P≠NP** (usa "implicaria" e deixa alternativas) ✓, mas "convenção forte" indefinida e parece autocontradizer a errata; **carta EN aponta "Theorem 4" no v5, onde o teorema é o 3** — errata de numeração fatal num e-mail |
| 3 | §3 item 1 | "troca 2.1→(F-sent)" **fiel a G2 §5.1/§6.3** ✓; "(F-b') refutado (G1 4.3)" ✓; **faltam 4 ressalvas** (hipótese corrigida é ela-mesma ZFC-falsa; reductio sob NP=coNP segue legítima; "Teorema 4.1" ambíguo; gloss "finito-bounded" errado; (L1) não provado p/ o livro) |
| 4 | Tom e riscos | **Colaborativo** ✓; **marcação (C) ausente no documento todo** (deveria marcar ≥ 4 lugares); claims derrubáveis: os do quadro 1 + §3.1 + a frase "referee interno hostil" |
| 5 | §5 autoria/próximos passos | **Honesto em geral** ✓ (lacunas declaradas), mas "a errata … é produto da nossa equipe / nada disso é do artigo" impreciso, e 3 lacunas conhecidas omitidas |

---

## 1. CRÍTICO (derruba o envio; corrigir antes de qualquer revisão)

### C1 — §2(i) L61–63: o parêntese sobre o G2 está **matematicamente invertido**
> Redação atual: "…é **falsa em ZFC** para a semente do artigo (**falsificador + `M' ⊨ T_PV`
> contradizem-se**; a construção precisa de `(F-sent)`, não de completude)."

Isso **não** é o G2. `G2`, Thm 2.1: a impossibilidade é **`M' ⊨ T_PV` + `(¬φ) ∈ SAT` +
`(F-sent)`** (item (b)); sozinhos, falsificador + `T_PV` são perfeitamente consistentes (é a
hipótese (2)/`(ii)` do artigo, que ele obtém; `G2 §2.5.3` diz explicitamente que `(F-sent)` nua
também é consistente). Como está escrito, o rascunho afirma que a própria hipótese (ii) do
Problema 2.1 é refutável — o que (a) um referee externo derruba em duas linhas, (b) contradiz a
própria dicotomia do §1 (que precisa de (2) como perna), (c) contradiz `L1 §2`/`G1 Cor 4.4`.
A frase "não de completude" é obscura (sem correspondente claro em `G2`).
**Correção:** "…é falsa em ZFC: `M' ⊨ T_PV` + falsificador + `(F-sent)` contradizem-se (`G2`
Thm 2.1(a)/(b); hipótese mínima: `M' ⊨ PV`, Thm 2.1(a′)) — ou seja, o forcing (ou qualquer
método) **não pode gerar** `(F-sent)` junto do falsificador (`G2` Cor 2.2)." + acrescentar a
ressalva honesta do próprio `G2 §2.5.1`: "construção sob `NP=coNP` permanece legítima (e já
provaria `NP≠coNP`)".

### C2 — Carta EN (L46) e §0/§1: **numeração errada na versão enviada**
`G_CONTEXTO_FORCING.md §1.1` (releitura integral do v5/LMCS): a lacuna está literalmente lá, **mas
em v5/LMCS o teorema é o Teorema 3** ("Teorema 3 = antigo Teorema 4"; Problema 2.1, (7), (8),
`Log` inalterados). A carta abre "I am reading arXiv:2506.20221**v5** … In §3, item (5) of the
proof of **Theorem 4**" — aponta o teorema errado para o destinatário. Idem §0 L14 ("errata … no
Teorema 4 (v4 **e** v5/LMCS)") e §1 L21–22.
**Correção:** em toda parte: "**Theorem 4 of arXiv v4 = Theorem 3 of v5/LMCS**" (e conferir em v5
que ainda é "§3, item (5)"). Sugestão de redação EN: *"in §3, item (5) of the proof of Theorem 4
(v4; renumbered Theorem 3 in v5/LMCS)"*.

### C3 — §2(v) L73–74: escopo **e** mecanismo do I1 errados
> "nenhum **ultrapoder** modela `S` (o mecanismo: `T_f` padrão é internamente refutável por EF ⟺
> insatisfatibilidade real)."

`I1`, B.2 + Cor. B.4: "**nenhum ultrapoder `ℕ^ω/U`** modela `S`" — só ultrapoderes **de `ℕ`**;
`C.1` mantém explicitamente vivo o venue `M = M_0^ω/U` sobre `M_0 ⊨ S` não-padrão. E o mecanismo
de B.2/B.3, segundo o próprio `I1 §0` item 2, é "**`Ref_P` soundness interna + impossibilidade de
seletor p-tempo**" (via Łoś + Lema B.1: nenhuma instância **padrão** de (S2)–(S4) com `P` sounde).
A equivalência "refutabilidade interna ⟺ insatisfatibilidade real para `T_f` padrão" é o **A.4 +
A.5 + Cor. A.6** — resultado diferente, com escopo diferente ("`T_f` padrão", "todo `M ⊨ T_PV`").
**Correção:** "(v) **I1 B.2/B.3**: nenhum **ultrapoder de `ℕ`** modela `S` (Łoś + Lema B.1:
nenhuma instância padrão de (S2)–(S4); B.3: sem falsificador comum + sem seletor p-tempo) — o
venue `M_0 ⊨ S` não-padrão permanece vivo (`C.1`)". Se quiserem manter a frase da equivalência,
citá-la como **I1 A.4–A.6** à parte.

---

## 2. MAIOR (referee externo derruba; corrigir antes do envio)

### M1 — §2(ii) L64–65: mecanismo atribuído ao **H1.1 (no-G) está errado**
Redação: "irrealizável por qualquer `G` (**amálgama + `(S3)` + Condition 1**)". A prova de `H1`
Thm 1.1 é: `ν_G(¬φ)=1` + `ν_G(δ_N→τ_N)=1` ∀N ⟹ `M[G] ⊨ (¬φ)∈SAT` + `∀i<m(¬α_i)∈SAT`, com
`M[G] ⊨ PV` (Kra98 Thm 4.1) ⟹ **contradiz `G2` Thm 2.1(a′)**. Nem amálgama, nem `(S3)`, nem
Condition 1 entram nessa prova (Condition 1 só na *consistência* da semente — `G2` Thm 1.1;
`(S2)` só na consistência de subconjuntos finitos — `G2 §2.3`). Escopo: `G` = ultrafiltro em
`B(p)` **fechado sob EF-provability in `M` e contendo constantes-1** ("universal"), não "qualquer
`G`". **Correção:** "(amalgama/`(S3)`/Condition 1 são da *semente*; a refutação é por
`G2` 2.1(a′))".

### M2 — §2(iii) L66–70: "o mecanismo **reproduz a própria remark** do artigo (L442)"
`J1` K.2 diz literalmente o contrário do verbo usado: K é "**coerente com, mas não idêntica à**,
razão do artigo" — o artigo dá como razão a **perda de universalidade do KPT**; K acrescenta uma
**segunda** razão, **ao nível da semente** (`J1 §0` item 1 e K.2). Escopo do corolário:
`T_PV + BB + (S2)+(S3)+(S4)` é **inconsistente** ("incompatível com a semente" é atalho aceitável,
mas escreva os axiomas). **Correção:** "…dá uma segunda razão, ao nível da semente, **coerente com
(não idêntica à)** a remark do artigo (L442: `T_PV+BB` invalida a análise de (1) por perda de
universalidade do KPT); `T_PV+BB+(S2)+(S3)+(S4)` é inconsistente."

### M3 — §3.1 L78–81: quatro problemas numa linha
1. **"Teorema 4.1"** — o artigo não tem Teorema 4.1 (e em v5 o Teorema 4 virou 3). É o
   **Teorema 4.1 do `G2`** (versão corrigida do Teorema 4 do artigo). Escreva: "**Teorema 4 do
   artigo (v4; = Thm 3 em v5/LMCS) — correção proposta: `G2` Teorema 4.1**".
2. **"a obstrução G2 vira teorema com essa hipótese"** é verdade, mas **omite o golpe que o autor
   vai dar**: a hipótese corrigida é ela-mesma refutável em ZFC (`G2` Thm 2.1) — logo o teorema
   corrigido, tal como está, é **vazio/vacuoamente verdadeiro** como entrega verificável. Sem esta
   frase, o "correção" parece um troco benigno. Acrescente: "a hipótese trocada é o **conteúdo de
   BB** (`G2 §6.3`) — irrealizável em ZFC junto do falsificador, o que faz do Teorema corrigido um
   **alvo de reductio** (`G2 §2.5.1`: construção sob `NP=coNP` segue legítima), não uma entrega
   verificável."
3. **"`(F-b')` (finito-bounded)"** — gloss errado: `(F-b')` = "versão **membership/domínio**:
   `M'∩m = M∩m`" (`F_CONTEXTO_ATAQUE` L76, `F2` §(F-b')). Troque por "(domínio: `M'∩m = M∩m`)".
   ("`(F-b')` é refutado — `G1` Thm 4.3" está **correto** ✓; inclua `G1 Cor 4.4` para o passo (5).)
4. **"`(L1)` `Log(M[G]) = Log(M)` vale (G1)"** — **falta o escopo**: `G1` prova (L1) na construção
   booleana de `[Kra95 §9.4]/[Kra98 §4]`; para a **versão do livro** (`[Kra95, Thm 9.4.2]`, que é
   exatamente o que o artigo cita) `G1 Advertência 2.4` declara **"(C): plausível mas não provado
   aqui"**. Como está, é uma superestimação flagrante — o autor responderá "vocês provaram só para
   a versão que eu não citei".

### M4 — §1 L38–42: a dicotomia (1)+(2)+(3) via (8) precisa de andaime
- **"convenção forte (fechamento+Log, condição (3)…)"** não está definida — e é o ponto todo:
  `F1 §2` prova que **(3) sozinha não dá `i_0 ∈ M*`**. Se a "convenção forte" = só fechamento+Log,
  a dicotomia é **falsa** e o autor rebate com a própria errata do rascunho. A dicotomia só fecha
  com a leitura **forte** de (3)/(1): aquela em que o artigo já teria `i_0 ∈ M*` (ou `(8)` em `M'`,
  cf. `F1 §6(c)`: "M′ preserves all Σ^b_1 properties of elements of M").
  **Correção:** definir explicitamente "convenção forte = (3) **lida como** 'nenhum elemento novo
  abaixo de `m`' (ou `(8)` exigido em `M'`)" — i.e., exatamente a leitura que faria o passo (5)
  valer —, e então afirmar a inconsistência.
- **Falta a 3ª perna explícita** (`L1 §2` tem; o rascunho só insinua): "(1)+(2)+(3) valem ⟹ 2.1
  negativo ⟹ **`P≠NP`** (rodapé 2) — o que você não reivindica — **ou** a convenção forte não é a
  pretendida (direção da errata)". Hoje "isto implicaria `P≠NP`" aparece solto, antes das duas
  alternativas que não incluem `P≠NP`.
- **Hedge de escopo só em §5**: `L1 §2/§6` marca o alcance como **pendente de verbatim de
  (1)–(3)/(8)**. Ponha "(escopo: depende do verbatim — ver §5)" **dentro** do §1.
- **Rótulos**: o artigo usa **(i)(ii)(iii)** no Problema 2.1 (`A_...` L513–517); o rascunho usa
  (1)(2)(3). Num documento que vai ao autor, mapeie.

### M5 — §3.2 L82–84: K-FP′ mistura escopo de dois enunciados
`J2` **K-FP′** é **por nome padrão `N` com `R(N)⊆m`** ("o ponto fixo existe em `M_0`");
"**famílias finitas-padrão**" é a **J.6-a′** (construtor-joint), que exige adicionalmente **`sem ¬φ`**
e conclui `(Hjoint)`/C.3 nesse alcance. E "em todo `M_0`" = "em todo **`M_0 ⊨ T_S`**".
**Correção:** "(ii) **K-FP′ (J2)** — para **todo nome padrão `N` com `R(N)⊆m`** … existe em todo
`M_0 ⊨ T_S`; **J.6-a′** estende a famílias finitas-padrão **sem `¬φ`**". (A ressalva de semântica
de `τ_N` já está em §4.1 e §5 ✓.)

### M6 — §3.3 L85–89: falta a ressalva `L.3″`
"C.3 decidida: negativa" ✓ e "para refutações **genuínas**" ✓ (fiel a `L1 §3`, incondicional,
com Lema L.3a e carregador corrigido). Mas `L1 §3` (`L.3″`) mantém **aberta** a pergunta original
do `H1 §1.3`: refutação **interna** com testemunha **não-padrão** (é a não-compactude interna).
Sem isto, o autor (ou um referee) dirá "vocês fecharam a Q-compactness, mas o `H1 §1.3` continua
aberto — e vocês mesmos dizem isso". **Correção:** acrescentar "(refutações **internas** com
testemunha não-padrão permanecem abertas — `L.3″`; só o ramo padrão está decidido)".

### M7 — marcação **(C)**: ausente no documento inteiro
O rascunho usa (A)/(P) e **nunca (C)**, embora pelo menos quatro assertivas dependam de material
interno marcado (C)/pendente: (a) `(L1)` para a versão do livro (M3.4); (b) a "featura oculta de
[7, Thm 9.4.2]" do §1 item (c) — `F1 §2.2` a marca `(C→P)` e declara a conferência página-a-página
**pendente**; (c) o alcance da dicotomia (M4); (d) qualquer extensão de B.2 além de ultrapoderes
de `ℕ` (`I1 B.4` = `(C)`). **Correção:** marcar esses quatro pontos com **(C)** — é o que o cabeçalho
promete e é o que protege o dossiê.

---

## 3. MENOR (qualidade e cortesia editorial)

- **N1 — §1 L29–32**: os "reparos mínimos (a)/(b)" são listados como propostas, mas **(a) é
  refutado por `G1` Thm 4.3** e **(b) por `G2` Thm 2.1(b)** (ambos impossíveis *junto de* (2)).
  A estrutura "proponho → mostro que é impossível → troco a hipótese" é legítima, mas ligue as
  pontas: acrescentar após (c): *"nota: (a) e (b) são exatamente o que os teoremas §2 bloqueiam —
  daí a correção efetiva em §3.1"*. Sem isto, a carta parece oferecer reparos que a própria carta
  derruba.
- **N2 — §2(iv) L71–72**: "`¬φ` é internamente insatisfatível **em todo modelo**" → "em **todo
  modelo de `T_PV+(S4)`** (com `α,m` nomeados)" (`L1 §1`, escopo restrito na rodada 1).
- **N3 — §3.4 L90–91**: citação truncada sem reticências: o verbatim (`A_...` L21–22) continua
  "**but it will always be sound** as that is expressible by a universal `L_PV`-formula". Citar a
  metade sem "…" num documento que discute *incompletude* convida a acusação de citação seletiva
  — e a parte omitida (soundness) é justamente o que `L.1` usa.
- **N4 — Carta EN L46–54**: remove os crases/backticks literais (`` `i_0 ∈ M*` ``), use símbolos
  limpos; caso contrário o texto está **fiel** ao PT e sem exageros ✓ (bem-hedged: "seems to",
  "appears compatible", "Am I missing an argument?" — nada de `P≠NP`, nada de "fatal"). Bom.
- **N5 — §2 cabeçalho L58 / §5 L113**: "referee **interno hostil**" → sugira "revisão cruzada por
  pares interna (logs em `*_referee.md`)". Autodescrição como "referee" num documento externo soa
  a auto-referência e enfraquece o apelo de autoridade.
- **N6 — §5 L112–114**: "a **errata** … é produto da nossa equipe … **nada disso é do artigo**"
  — impreciso: a lacuna **é** do artigo **(A)**; o que é `(P)` é a **identificação/análise**.
  Reduzir para: "a identificação da lacuna e a análise §1–§3 são nossas; as citações verbatim são
  do artigo".
- **N7 — §5 lacunas (L119–122)**: acrescentar três lacunas já declaradas nas fontes e ausentes
  aqui: (i) `(L1)` não provado para a versão do livro (M3.4); (ii) `L.3″` aberta (M6); (iii) gaps
  do `G2` (espelhamento `α_i ↦ α̃_i` para `i` não-padrão e passagem a semente infinita — `G2 §2.3`
 /`§6`, referee R3) — hoje o §5 diz só "os teoremas §2 são nossos; se o autor apontar erro, cai em
  parte", o que é honesto mas genérico.
- **N8 — §4.2 L102–103**: "conferido no artigo por nós — confirma?" ✓ honesto; sugiro explicitar
  **onde** (`"bits of α"` = constantes — `L1 §5` nº 4, `(A✔)`) para o autor conferir em um passo.
- **N9 — §0 L13–17**: "(iii) o que **sobrevive**" — bom resumo; apenas tom: "sobrevive" +
  "obstáculos" + "lacuna" é denso. Não é bloqueante.

---

## 4. Veredito

**REVISION.** Motivo resumido: o esqueleto é sólido, o tom é colaborativo, a marcação (A)/(P) e a
transparência de processo (§5) são bons, e a carta em inglês é politicamente bem calibrada — mas o
documento **contém um erro factual no teorema central (C1)**, uma **referência de teorema errada
na versão que será enviada (C2)** e um **escopo+Mecanismo errados no I1 (C3)**; além disso a
marcação (C) não aparece onde as próprias fontes a exigem (M7) e §3.1 superestima `(L1)` e
silencia sobre a vacuidade da hipótese trocada (M3). Nada disso exige reescrever a nota — exige
sete correções cirúrgicas + quatro menores.

**Ordem sugerida de aplicação:** C1 → C2 → C3 → M1 → M2 → M3 → M4 → M5 → M6 → M7 → N1–N9 →
nova rodada de revisão → tradução EN (§1–§4) → envio.

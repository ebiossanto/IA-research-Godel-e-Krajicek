# Referee HOSTILE — `N1_refutacao_interna_CN_s.md` (v1)

> Referee independente, **rodada 1 — 11 Out 2026**. Esqueleto (cabeçalho + veredito
> pendente) gravado **antes** da análise longa — procedimento cumprido; este é o texto
> final. Marcação: **(A)** = fonte, **(P)** = próprio, **(C)** = conjectura.
> Fontes conferidas: `F2_versao_finita.md` (§0 L26–34), `M_canto_adversarial.md`
> (M.0/M.1/M.2/M.4, §2 ressalva, §8b), `G2_semente_Fsent.md` (§1.2, §2.3, §2.5),
> `L1_phi_insatisfativel.md` (L.1, L.3a, L.3′, L.3″, L.4), `A_teoremas_exatos.md`
> (L19–28, §1.2, §1.12, L341–344), `H1_colecao_refutacao.md` (§1.1, §1.3, §2.2),
> `I1_Qcompactness_ultrapoderes.md` (A.4–A.7, B.2, B.3, C.1).

## VEREDITO: **NÃO RECOMENDADO** (refaço necessário nas formulações; o núcleo §3 é salvável)

**1 FATAL, 4 MAIOR, 5 MENOR.** O FATAL não está na ideia — está no **enunciado do
resultado**: o Teorema N.1 é provado, na §3, com o alvo **`Taut(α)`** (sentença
**fechada**, big-and sobre as ~`2^{|at(α)|}` atribuições), mas §0 item 1, Corolário
N.1′, Dicotomia N.2 (chifre (α)), §4 e §7 trocam `Taut(α)` por **`α`** (fórmula
**aberta**, tamanho `|α|`) — e a direção `EF ⊢ α ⟹ EF ⊢ σ_s` **não é provada**, não
é verdade por completude, e o arranjo que a salvaria é **exatamente uma coleção
sharply-bounded (tipo BB)** — o princípio que o próprio projeto classifica como
indisponível (`G2 §2.3` "R3 ≡ BB"; `F2 §4.2`). O chifre (α) da dicotomia — a metade
"refutável internamente" que dá conteúdo ao Corolário "π comprime-se" — fica sem
prova. Somam-se uma **contabilidade de tamanho falsa** (Lema N.0 "poly(|α|)" para
sentenças com `∀v` — MAJOR-1), o escopo semântico (R1/`q`-total) **não propagado** dos
enunciados-resumo (MAJOR-3), o gloss "compressão de π" e a marcação "(A)" de "P não
simulável" (MAIOR-4 — a fonte diz o contrário) e citações trocadas ao I1 (MAJOR-2).

Com as correções da §"Forma corrigida" abaixo — que **reestraa** N.1/N.1′/N.2/§7 em
termos de `Taut(α)` e **rebaixa** "EF ⊢ α ⟹ refutação interna" a hipótese aberta — a
frente N entregaria um resultado correto e útil. Enquanto isso, v1 **não** pode virar
v2 por correções pontuais: o §0 (a parte que será citada na nota editorial e na
resposta a Krajíček) enuncia um teorema não demonstrado.

---

## FATAL

### FATAL-1 — A troca `Taut(α)` ↔ `α` é ilícita e derruba o chifre (α) de N.2, o Corolário N.1′ e §7

**Locais:** §0 item 1 (L17–22: "`M_0 ⊨ EF ⊢ σ_s` ⟺ `M_0 ⊨ EF ⊢ α`"); §3 enunciado
(L67: "⟺ `M_0 ⊨ EF ⊢ Taut(α)`" — **este** é o que a prova trata); Corolário N.1′
(L90–94: "`π` comprime-se: tem uma 'irmã' EF"); §4 N.2 chifre (α) (L99–102: "`M_0 ⊨
EF ⊢ α`: então `{C_{N_s}}` **tem** refutação EF interna"); §7 (L163–168).

**O que a prova da §3 realmente entrega (e eu CERTIFICO, com a correção de MAJOR-1):**

> **(T1)** `M_0 ⊨ EF ⊢ σ_s` ⟺ `M_0 ⊨ EF ⊢ Taut(α)`, onde `Taut(α) = ⋀_v (eval(v,α)=1)`
> é **fechada** (α hardwirado como constante) e tem tamanho `≥ 2^{|at(α)|}`.

- **(⇒) de (T1)**: ok — o argumento por-`v` (L82–88) fecha **porque o carregador `e`
  já paga a conta**: toda derivação EF de `σ_s` contém `σ_s` ⟹ `|e| ≥ |τ_{N_s}| ≥
  2^{|at(α)|}` (`τ` é um big-or com um disjunto por atribuição — `H1 §1.1` L32–35);
  montar o big-and custa `2^{|at(α)|}·poly(|α|) ≤ poly(|e|+|α|)` ⟹ programa PV
  legítimo, saída ∈ `M_0` por fechamento de `T_PV`. **O arquivo não escreve esta
  contabilidade** — vê MAJOR-1.
- **(⇐) de (T1)**: ok, mesma contabilidade, com `|e| ≥ |Taut(α)| ≥ 2^{|at(α)|}`.

**O que NÃO é entregue:** `M_0 ⊨ EF ⊢ α ⟹ M_0 ⊨ EF ⊢ σ_s` (o chifre (α) de N.2, que é
o que a §0 declara ser o Teorema N.1). Argumento do referee:

1. `α` é **aberta** (`|α|` bits, `|at(α)| ≤ |α|`); uma prova EF interna `e_α` de `α`
   pode ter tamanho `poly(|α|)` — **muito menor** que `2^{|at(α)|}`.
2. **Toda** prova EF de `σ_s` tem tamanho `≥ |σ_s| ≥ 2^{|at(α)|}` (conclusão contida
   na derivação; `τ_{N_s}` tem `2^{|p|}` disjuntos, `p ⊇ at(α)` — `H1 §1.1`).
3. Logo nenhum programa PV, dado `(e_α, α)`, **produz** uma prova de `σ_s` (nem
   consegue *escrever* a saída quando `2^{|at(α)|} ≫ poly(|e_α|+|α|)`).
4. A montagem honesta — para cada `v`, derivar `eval(v,α)=1` de `e_α` por
   substituição, deduzir `¬Fals(v, α_{s(v)})` pelo laço desenrolado, e **juntar as
   `2^{|at(α)|}` derivações** — é literalmente uma **coleção sharply-bounded**
   (`q < 2^{|at(α)|}` é sharply bounded), i.e. uma instância do tipo de princípio que
   `G2 §2.3` (L116–129) mostra ser **indisponível em `T_PV`** ("R3 ≡ BB") e que `F2 §4.2`
   coloca no coração do problema. Usá-la aqui de graça seria inconsistente com o
   próprio programa da campanha.
5. A completude externa de EF **não** conserta: externamente `α` padrão tem prova, mas
   aqui `α` é **não-padrão** (Lema L.3a, `L1 §3`) e a incompletude interna de pps em
   modelos de `T_PV` é justamente o **aviso L21–22** (`A L21–22`) que o projeto invoca
   em L.4. `EF ⊢ Taut(α) ⟹ EF ⊢ α` **é** provável (restricção + `α ≡ ⋁_v(α|_v∧χ_v)`,
   carregador `e_T` grande) — mas a **recíproca** (`EF ⊢ α ⟹ EF ⊢ Taut(α)`) é o passo
   que exige carregador grande ou coleção, e **não está no arquivo**.

**Consequências exigidas:** (i) §0.1, N.1′, N.2(α), §4, §7 devem ser reescritos com
`Taut(α)`; (ii) "EF ⊢ α ⟹ refutação interna de `{C_{N_s}}`" deve passar a figurar como
**hipótese aberta (C1′-α)** — mais forte que o (C1′) atual, que (no chifre (β)) está
correto; (iii) a identificação "`EF ⊢ α` = `EF ⊢ Taut(α)`" deve ser explicitada como
convenção **ou** removida — hoje o arquivo oscila entre as duas leituras em três
formulações diferentes do mesmo "teorema".

---

## MAIORES

### MAIOR-1 — Lema N.0: a afirmação "provas de tamanho `poly(|α|)`" é **falsa** para (a)/(b) como estão escritas

**Local:** §2 (L49–61, em especial L56–58: "`m` passos × provas locais de
`poly(|α|)` = `poly(|α|)` no total"); §6 checklist nº 5 (L153).

**Argumento.** As sentenças (a) e (b) dizem "**para todo v**" (L51–53). `v` percorre as
atribuições — `2^{|at(α)|}` delas — e pela convenção do projeto (`§5.3` L138–139:
"big-and/or como circuitos") a sentença fechada é um big-and com `2^{|at(α)|}`
conjunções. Toda derivação EF **contém** sua conclusão ⟹ `|prova| ≥ 2^{|at(α)|}`. E
`2^{k} > k^{c}` para **todo** `c` padrão **também dentro de `M_0`**: para cada `c` padrão,
`∀k(k ≥ N_c → 2^k > k^c)` é sentença **universal verdadeira** de `L_PV` (com `exp`), logo
`∈ T_PV` (`A §1.0` L19–28), logo vale em `M_0 ⊨ T_PV` para o `k = |at(α)|` não-padrão.
Portanto `poly(|α|)` **não** cobre o big-and, por mais que cubra o unrolling.

**O que o unrolling de fato cobre (e está certo):** a dimensão `i<m` — `m ≤ |α|` **é
(A✔)** verbatim (`A §1.2` L50–57: "*`m` is bounded by the size of the formula*") — e aí
`m·poly(|α|) ≤ poly(|α|)` ✓. A dimensão `v` foi **silenciosamente omitida** da conta.

**Correção:** enunciar N.0 como **esquema** (com `v` livre), tamanho `poly(|α|)` ✓;
a versão fechada custa `2^{|at(α)|}·poly(|α|)`. E, crucialmente, **a prova da §3 tem de
escrever** a contabilidade que a salva: em ambas as direções o carregador `e` tem
`|e| ≥ 2^{|at(α)|}` (≥ `|τ_{N_s}|` ou ≥ `|Taut(α)|`), logo a montagem é p-tempo em
`(|e|,|α|)` — sem isto, a frase "Concatenação de derivações em `M_0` é p-tempo ⟹ prova
EF de `σ_s` ∈ `M_0` ✓" (L80–81) é um **non sequitur**: concatenar `k` derivações é
p-tempo no **tamanho somado**, e o arquivo nunca limita esse tamanho pelos dados.

**Registro de consistência:** §5.5 (L142–143) já nota que provas de `σ_s` são de
comprimento não-padrão — ou seja, o arquivo *pressente* o `2^{k}` mas não o paga na
conta do Lema N.0 nem na §3.

### MAJOR-2 — N.3 e checklist nº 10: citações trocadas ao I1 (A.4–A.6 não cobrem este caso; a barreira é B.2)

**Local:** §4 R-α (L112–114: "ultrapoderes **não** servem — sentenças transferem por
Łoś, `I1` A.4–A.6"); §6 checklist nº 10 (L158).

**Conferido no `I1`:** A.4/A.5/A.6 (L58–89) valem para `T_f` **padrão** — e o próprio
I1 traz a **Limite de escopo A.7** (L91–97): "`T_f ⊆ 𝒯` do H1 tem fórmulas **não-padrão**
(`δ_N → τ_N` com `N` não-padrão) … Logo A.3–A.6 **não se aplicam**". Aqui o objeto é
`α` **não-padrão** (Lema L.3a, `L1 §3` L94–102) e `C_{N_s}` não-padrão — logo A.4–A.6
ficam **fora de alcance por decisão do próprio I1**. A razão correta pela qual
ultrapoderes "não servem" para construir `M_0 ⊨ T_S` é o **Teorema B.2** (`I1` L120–128:
nenhum `ℕ^ω/U` modela (S1)–(S4)); a transferência Łoś é o **Teorema C.1** (`I1` L166).
Corrigir as duas citações; o argumento de R-α sobrevive, mas **muda de fonte**.

### MAIOR-3 — Escopo semântico: a hipótese "R1 ou alternativa com `q` total" some dos enunciados-resumo

**Locais:** enunciado de N.1 em §0 (L17–22 — sem a hipótese; o §3 L65–66 **tem**: "sob a
semântica de `τ_N` em que M.2 vale — R1 ou alternativa com `q` total"); §1 L41–42
("`code(N_s,v) = s(v)`" enunciado incondicionalmente); Corolário N.1′ (L90–94); N.2
(L98–108); §7 (L163–169).

**Por que importa:** sob a alternativa **`q`-par**, a ressalva herdada de `M §2`
(L108–112) permite que `σ_s` seja **falsa**. Aí a sonoridade de EF em `M_0` (`Ref_EF ∈
T_PV` — `G2 §2.3` L112; `I1` Nota A.5) dá `EF ⊬ σ_s`, mas `EF ⊢ α` pode valer — a
equivação **sem-condicionamento** de §0 e o chifre (α) de N.2 seriam **simplesmente
falsos**. A §5.1 (L131–135) admite o ponto ("toda a frente presume …"), mas o resumo do
§0, o Corolário, a Dicotomia e o Veredito §7 **não** o repetem — e é o resumo que será
citado. Propagar a hipótese para todos os enunciados (e para `code(N_s,·)=s(·)` do §1).

### MAIOR-4 — Gloss "compressão de π" é falso como equivalência; e a marcação "(A)" de "P não simulável" contradiz a fonte

**Locais:** §0.1 (L21–22: "a prova `π` comprime-se para EF dentro de `M_0`"); N.1′
(L90–94); §4 (L103–108: "(C1′) é **literalmente**: 'a prova `π` de `P` não comprime para
EF em `M_0`'"); §6 checklist nº 8 (L156, marcação "(A)"); §7 (L164–166).

**Argumento.** "Compressão" em prova-complexidade é `|EF proof| ≤ poly(|π|)` (p-simulação).
O que N.1 (mesmo corrigido) entrega é **existência** de *alguma* prova EF interna de
`Taut(α)`, de tamanho não-padrão **≥ `2^{|at(α)|}`** — não há cota em `|π|`, e a
distinção existência vs. limitação polinomial é exatamente a que `I1` Cor. A.6 marca
(L87–89: "a equivalência usa EF completo mas **não** polinomialmente limitado … ⇔
`NP = coNP` (aberto)"). Pior: "(C1′) **literalmente** = π não comprime" (L105–106) é o
**contrário** do sentido forte: "EF ⊬ α" diz que **nenhuma** prova EF de `α` **existe**
em `M_0` — muito mais forte que "todas as provas são superpolis". E quanto à
justificativa "`P` é extensão de EF, **não simulável** por ele; (ST) pressupõe `P`
forte" (L93–94) com marcação "(A)": a fonte (`A §1.6` L112–115, verbatim) diz "**Every
pps can be p-simulated by a strong one**" — i.e., forte simula os outros; **não** diz
que EF não simula `P`. "Não simulável" é, no máximo, **(C)** (consequência esperada de
(ST), não teorema). Além disso, a premissa "`P ⊢ α` não dá `EF ⊢ α`" é externamente
**falsa como implicação** (completude de EF para `α` padrão); o que falha é a passagem
**interna** — e a justificativa correta é o aviso L21–22, não a "não-simulabilidade".
Reescrever N.1′ como: "`EF ⊬_{M_0} Taut(α)` ⟹ nenhuma prova EF interna de `Taut(α)`
existe; isto é, internamente, `P` provando o que `EF` não prova — a incompletude
exemplificada de L.4, com `(C1′)` no lugar de Condition 1".

---

## MENORES

- **M-1 (§1, L42–43):** "`σ_s` … **verdadeira** em `M_0`" é a conclusão de **M.2**, cuja
  prova usa **M.1** ("totalidade do seletor — M.1", `M` L100–101), que usa o **Teorema
  K** (`M` L62–67). Não há **circularidade** para N.1 (a prova de §3 não usa M.1/M.2/Teorema
  K — ver §"Certificados" nº 6 abaixo), mas a hipótese de trabalho "sentença verdadeira"
  é **herdada** e deve ser registrada como tal no checklist.
- **M-2 (§4 N.4, L124–127):** "Sonoridade de EF em `M_0` (`Ref_P ∈ T_PV`) garante: em (β)
  a sentença `σ_s` é **verdadeira** sem prova" — a sonoridade dá só "prova ⟹ verdade";
  a verdade de `σ_s` vem de M.2 (M-1). E a citação "`Ref_P ∈ T_PV` ⟹ EF sonoro"
  (`F2` L26–27/A L341) trata de `Ref_P`; para `Ref_EF` a fonte explícita é `G2 §2.3`
  (L112) e `I1` Nota A.5 (L72–83) — citar.
- **M-3 (§2, L54, N.0(c)):** "`code(N_s,v) = s(v)` (definicional)" — não é definicional:
  `code` **avalia os circuitos** de `N_s` (`H1 §1.1` L29–31). A identidade vale **por
  construção** (os bits de `s` são o laço unrolled, `M §2` L78–81) e é EF-provável em
  `poly(|α|)` via extension variables (rastro do laço, `m ≤ |α|` passos) — escrever isto;
  senão parece que a semântica de `code` é livre, e é justamente aí que entra a ressalva
  R1/`q`-total (MAJOR-3).
- **M-4 (§5.3, L138–139):** a convenção "prova EF em `M_0`" é citada a "`G2 L2, L.3″`" —
  "`G2 L2`" não designa nada identificável (G2 L2 é nota de autoria). A fonte **exata**
  da convenção (derivação interna = elemento de `M_0`, comprimento possivelmente
  não-padrão) é `H1 §1.3` (L59–64); o uso correspondente em G2 está em §1.2 (L62–69).
- **M-5 (§4 L100–102, §7 L166):** "a única não-compactude genuína **restante** é `¬φ`
  sob Condition 1" — correto só **no escopo das duas condições canônicas** de M.4
  (`¬φ`, `C_{N_s}`). A pergunta Q-compactness de `H1 §1.3` (L66–70) é mais ampla e
  permanece aberta; restringir a frase a esse escopo.

---

## O que o referee CERTIFICA (OK)

1. **(S3) = `π : P ⊢ α`** — verbatim `F2 §0` L33 (e `A §1.12` L202–204); `Ref_P ∈ T_PV`
   ∈ `F2` L26–27 = `A` L341–344 ✓. §6 checklist nº 1–2 corretos.
2. **`m ≤ |α|` é (A✔)** verbatim (`A §1.2` L50–57: "*`m` is bounded by the size of the
   formula*") — e N1 cita a fonte **certa** (`A §1.2`), sem repetir o erro de citação
   da v1 de M (`G2 §2.2`) — `M §8b` MAJOR-3. O unrolling `i<m` de N.0 é legítimo
   (tamanho `poly(|α|)` **na dimensão `i`**) — salva a MAJOR-1.
3. **`m ≥ 1` por (S3)+sonoridade** (§1, L43–45): correto e coincide com `A §3(a)` item 4
   (L352–353: "`m = 0` ⟹ `α = ⊥` ⟹ `Ref_P` refuta"). O default `0 < m` fecha.
4. **Lema N.0(b) como disjunção** ("ou check passou em `s(v)`, ou `∀i<m Fals(v,α_i)`"):
   **correto** — o caso default dispara só quando o laço esgotou `i<m` com todos os
   checks falhando; o caso retorno dá `¬Fals(v,α_{s(v)})`; os dois casos cobrem o código
   (L59–61). Uso em (⇐) (L74–78): a instância de `Taut(α)` em `v` dá `∃i<m ¬Fals(v,α_i)`
   (identidade proposicional do big-or de `α = ⋁̇_{i<m} α_i`, com `Fals ↔ eval=0`) e mata
   o ramo-default — **correto**. Em particular N.0(b) **não** precisa de M.1 (o ramo
   default é morto por `Taut(α)`, não pela inexistência de falsificador global).
5. **Direções individuais da §3 com `Taut(α)`** — (⇐) L74–81 e (⇒) L82–88: o
   raciocínio por-`v` é proposicionalmente correto (identidade big-or; `¬Fals ↔ eval=1`);
   o "salto para todo v" **é legítimo** em convenção EF **com a contabilidade de
   carregador `|e| ≥ 2^{|at(α)|}`** que falta escrever (MAJOR-1). **Sem circularidade**
   com M.1/M.2/Teorema K: N.1 usa só fatos locais do laço; `δ_{N_s} ≡ 1` sai de N.0(a)+
   `code=s`, não de M.2 (`M` L100–101 usa M.1; N.1 não).
6. **§5.1 (ressalva `q`-par) e §5.5** — herança honesta de `M §2` (L108–112); o
   condicionamento existe (falta propagar — MAJOR-3).
7. **Chifre (β) de N.2 e N.4** — `EF ⊬ α ⟹ EF ⊬ Taut(α) ⟹ EF ⊬ σ_s` é **proveniente**
   da corrente (⇒) de (T1) (toda prova de `α` vem de uma de `Taut(α)`, que tem carregador
   grande); a comparação com `¬φ`/Condition 1 (`L1` L.3″ L117–123; L.4 L130–134) é fiel.
8. **N.3 como honestidade** (nenhum chifre decidido; `(C)` marcado; `G2 §2.5.1` = `G2`
   §2.5 item 1, L178–187 ✓) — a única falha é a fonte dos ultrapoderes (MAJOR-2).

---

## Forma corrigida proposta (para orientar a v2 — não reescrevo o arquivo da frente)

> **Teorema N.1′ (certificado nesta rodada, com contabilidade de carregador).** Em todo
> `M_0 ⊨ T_S`, sob a semântica de `τ_N` em que M.2 vale (R1 ou alternativa com `q`
> total): **`M_0 ⊨ EF ⊢ σ_s` ⟺ `M_0 ⊨ EF ⊢ Taut(α)`**, e ainda `EF ⊢ Taut(α) ⟹ EF ⊢ α`.
> As duas direções construem a derivação-alvo num tempo p-tempo em `(|e|,|α|)`,
> **legítimo porque `|e| ≥ 2^{|at(α)|}`** (`|σ_s|`, `|Taut(α)| ≥ |τ_{N_s}| ≥ 2^{|p|}`,
> `p ⊇ at(α)` — `H1 §1.1`).
>
> **Aberto (C1′-α) (C):** `EF ⊢_{M_0} α ⟹ EF ⊢_{M_0} σ_s`? A montagem exigiria coleção
> de `2^{|at(α)|}` derivações (sharply bounded — tipo BB, `G2 §2.3`) ou uma prova EF de
> `α` já grande (`≥ 2^{|at(α)|}`); nenhum dos dois está garantido. **Enquanto (C1′-α)
> não for resolvido, o Corolário "π comprime-se" e o chifre (α) de N.2 permanecem (C).**

**Checklist da v2 (obrigatório para novo referee):** (1) reescrever §0.1, N.1′, N.2(α),
§4, §7 com `Taut(α)` e com (C1′-α) explicitamente aberto; (2) N.0 como esquema + nota de
tamanho da versão fechada (MAJOR-1), e a contabilidade de carregador escrita na §3;
(3) propagar "R1/`q`-total" a todos os enunciados (MAJOR-3); (4) corrigir gloss
"compressão" e marcação "(A)" de "não simulável" → (C) (MAIOR-4); (5) trocar `I1 A.4–A.6`
por `I1 B.2` (+`C.1`), com nota de que A.7 exclui fórmulas não-padrões (MAJOR-2);
(6) aplicar M-1…M-5.

**Veredito: NÃO RECOMENDADO** — a v1 enuncia, na parte que será citada externamente, um
teorema (e um corolário) mais fortes que a sua própria prova; o refaço é de
**formulação**, não de ideia — o núcleo `EF ⊢ σ_s ⟺ EF ⊢ Taut(α)` (com contabilidade
corrigida) está **certificado acima** e pode ser aproveitado integralmente na v2.

---

# Rodada 2 — referee da v2 (11 Out 2026)

> **Estado:** análise concluída. Fonte revisada:
> `N1_refutacao_interna_CN_s.md` **v2** (201 linhas). Veredito da rodada 2: **RECOMENDADO
> (condicionado a 4 correções locais obrigatórias antes da consolidação)**.
> Procedimento: APPEND (a rodada 1 acima permanece intacta).

## VEREDITO RODADA 2: **RECOMENDADO** — 0 FATAL, 2 NOVO-MAIOR, 1 correção da rodada 1 NÃO aplicada, 2 nits

O FATAL-1 está **fechado**: o teorema foi reescrito com `Taut(α)` **fechada** em §0.1
(L20–26), N.1 (L73–78), N.2 (L104–113) e §7 (L173–179); a leitura "π comprime-se" foi
rebaixada a residual R-β e N.1′ (L100) diz explicitamente "**não** é equivalência" ✓.
O núcleo `EF ⊢ σ_s ⟺ EF ⊢ Taut(α)` está agora **corretamente enunciado e certificável**.
Mas a v2 **trocou um overclaim por outro** (NOVO-1) e **emagreceu a justificativa da
direção (⇒)** até atribuí-la à fonte errada (NOVO-2); além disso o menor M-2 **não foi
aplicado**. Todos reparáveis em uma passada de texto — não reestração.

## Verificação item a item das correções da rodada 1

| Rodada 1 | Estado | Evidência (v2) |
|---|---|---|
| FATAL-1 (`Taut(α)` fechada; π-rebaixada) | **APLICADO** | §0.1 L20–26; N.1 L73–78; N.2 L104–113; §7 L173–179; N.1′ L97–100 ("não é equivalência"; R-β) |
| MAIOR-1 (N.0 por-`v`; fechado `≥2^{at(α)}`; contabilidade §3) | **APLICADO** (nit N1 abaixo) | §2 L56–64 (esquema, `poly(‖α‖,‖v‖)`) + L66–69 (fechado `≥2^{at(α)}`, transferência interna); §3 L80–82 (preamble de tamanhos); §5.4 L142–144 |
| MAIOR-2 (I1 `A.7`/`B.2`/`C.1`) | **APLICADO** | N.3 L118–121; checklist nº 9 (L166) |
| MAIOR-3 (escopo R1/`q`-total) | **APLICADO PARCIAL** | §0.1 L20–21 ✓; N.1 L73–74 ✓; N.2 L104 ✓; §5.1 L134–137 ✓; §7 L173 ✓; **falhou em N.1′** (L96–100: título promete "escopo exato", o enunciado não declara R1/`q`-total) — e §5.1/§6 nº 10 **alegam falsamente** "propagado a … N.1′" |
| MAIOR-4 ("não simulável" → (C)) | **APLICADO** | §5.6 L147–150 (cita `A §1.6` verbatim); checklist nº 12 |
| M-1 (cadeia M.2⟸M.1⟸K) | **APLICADO** | §0 L16–18; §5.5 L145–146; nº 11 |
| M-2 (sonoridade ≠ verdade de `σ_s`; fonte `Ref_EF`) | **NÃO APLICADO** | N.4 L128–129 ainda diz "**Sonoridade** … dá: em (β) `σ_s` é **verdadeira sem prova**" — a sonoridade só dá "`σ_s` falsa ⟹ não provável"; a verdade vem de M.2 (cadeia §5.5). E `Ref_P ∈ T_PV` segue citado como base da sonoridade de **EF** em §1 L45 e N.4 L128, sem a fonte exata (`G2 §2.3` L112 / `I1` Nota A.5) |
| M-3 (`code=s` "por construção") | **APLICADO** | §1 L48–49 ("pela construção dos circuitos do nome (sob R1/`q`-total)"); N.0(c) §2 L59 |
| M-4 (convenção = `H1 §1.3`) | **APLICADO** | §5.3 L139–141; cabeçalho L9–10 |
| M-5 (escopo de "sobrevive só `¬φ`") | **APLICADO** (nit N2 abaixo) | N.2(α) L106–108 ("escopo restrito ao que L.3″ efetivamente fecha") |

## NOVOS buracos da v2

### NOVO-1 (MAJOR) — "comprimir π é **estritamente mais forte** que `EF ⊢ Taut(α)`" é falso/ não provado — e contradiz a própria §0.3

**Locais:** §0.3 L33–36 ("comprimir a aberta `π : P ⊢ α` para EF é **estritamente mais
forte** que `EF ⊢ Taut(α)`"); N.1′ L99–100 ("Comprimir π … é **mais forte**"); N.3 R-β
L121–122 ("mais forte que (α)"); checklist nº 7 (L164, marcado "(C)" mas afirmado
declarativamente nos três textos).

**Argumento.** Seja `A := EF ⊢_{M_0} Taut(α)` e `B := EF ⊢_{M_0} α` (ou `B'` = `B` com
prova `≤ poly(|π|)`). "B é estritamente mais forte que A" exige `B ⟹ A` e `¬(A ⟹ B)`:
1. **`A ⟹ B` é provável** (carregador `e_T` grande: instanciar o big-and fechado por
   `v` + `α ≡ ⋁_v(α|_v ∧ χ_v)`, tudo `poly(2^{at(α)}) ≤ poly(|e_T|)`) — logo a
   **estritude** `¬(A⟹B)` é **falsa** se a compressão = `B`.
2. **`B ⟹ A` (ou `B' ⟹ A`) é exatamente a direção bloqueada** — a montagem exigiria
   colher `2^{at(α)}` derivações por-`v` (coleção sharply-bounded) ou carregador
   `≥ 2^{at(α)}`, que uma prova `poly(|π|)` não fornece. A **própria justificativa
   parenética da v2** ("exigiria colher `2^{at(α)}` derivações — coleção
   sharply-bounded **(C)**; `G2 §2.3` declara-a indisponível") argumenta que a
   implicação **não é demonstrável** no arcabouço — o que **não** serve de prova de
   que ela vale, muito menos *estritamente*. `G2 §2.3` (L116–129) é sobre
   indisponibilidade de coleção, não sobre ordem de força entre as duas noções.
3. **Autocontradição textual:** a mesma §0.3 (L32–33) chama a leitura de "**mais fraca**
   do que a redução" e dois period depois "estritamente **mais forte** que
   `EF ⊢ Taut(α)`" — a redução tem por-alvo justamente `EF ⊢ Taut(α)`; as duas frases
   não podem estar ambas certificadas.

**Correção:** reescrever como **relação ABERTA**: "`EF ⊢ α` (ou compressão polinomial
de π) e `EF ⊢ Taut(α)` são **incomparáveis no que se provou**: `Taut(α)-prova ⟹
α-prova` é provável; `α-prova ⟹ Taut(α)-prova` é o passo bloqueado por coleção
sharply-bounded (C1′-α, da rodada 1). R-β é residual de **status indeterminado**, não
'dois níveis'". O mérito da v2 (rebaixar π-compressão de corolário a residual) **fica
de pé**; o que cai é a ordem estrita.

### NOVO-2 (MAJOR, local) — direção (⇒): `¬Fals(v,α_{s(v)})` foi atribuída à fonte errada

**Local:** §3 L89–91: "Por N.0(a) **e a definição do seletor**: para cada `v`,
`¬Fals(v,α_{s(v)})` ∧ `s(v)<m` ⟹ …".

**Problema.** A definição do seletor **não** dá `¬Fals(v,α_{s(v)})` sem condição: no caso
**default** (`∀i<m Fals(v,α_i)`), `s(v)=0` e `Fals(v,α_0)` vale — é o próprio N.0(b)
(L57–58) que expõe o ramo. O passo é verdadeiro **só porque `e` prova `¬τ_{N_s}`**: a
instância do big-and fechado `¬τ` em `v`, junto de N.0(c) (`code(N_s,v)=s(v)`), dá
`¬Fals(v,α_{s(v)})`. A v1 pelo menos omitia a fonte; a v2 **trocou-a pela errada**.
**Correção (1 frase):** "de `e`: `¬τ_{N_s}`; instanciando o big-and fechado em `v` e
usando N.0(c) (`code(N_s,v)=s(v)`, §1 L48) obtém-se `¬Fals(v,α_{s(v)})`; com N.0(a) e a
identidade do big-or, `eval(v,α)=1`". *(O tratamento do big-and fechado da direção (⇒)
— L91–94, "as provas por-`v` têm tamanho `poly`; a derivação fechada tem tamanho
compatível com `2^{at(α)}`" — está **aceitável** como esboço (P), ver nit N1.)*

### Nits (MENORES novos)

- **N1 (contabilidade):** §3 L80–82/L93–94 nunca escreve a desigualdade que paga a
  montagem: `2^{at(α)} ≤ |τ_{N_s}| ≤ |σ_s| ≤ |e|` (direção (⇒)) e `2^{at(α)} ≤
  |Taut(α)| ≤ |e|` (direção (⇐)) — é ela que torna `2^{at(α)}·poly(|α|) ≤ poly(|e|+|α|)`.
  Uma linha explicitando-a elimina a ambiguidade de "compatível com `2^{at(α)}`".
- **N2 (escopo residual):** §7 L175–176 repete "não-compactude genuína restante:
  `¬φ`+Condition 1" sem o escopo que N.2(α) L107–108 agora impõe ("restrito ao que
  L.3″ efetivamente fecha") — alinhar.
- **N3 (typo):** §5.4 L143 "Concatenção" → "Concatenação".

## O que a v2 CERTIFICOU (OK confirmados nesta rodada)

1. N.0 (§2) como **esquema por-`v`** com tamanho `poly(|α|,|v|)` + contabilidade honesta
   da versão fechada (L66–69) — exatamente a forma corrigida pedida; `2^k > k^c`
   internamente em `M_0` alegado corretamente por transferência de universais
   verdadeiros (`A §1.0`).
2. (⇐) da §3 (L83–88): default morto pela instância `∃i<m ¬Fals(v,α_i)` de `Taut(α)`;
   `¬τ` por `code=s` sob R1/`q`-total; `δ` por N.0(a) — correto.
3. Dicotomia N.2 (L104–113): ambos os chifres em `Taut(α)`, `(C1′)` marcado (C),
   escopo declarado — correto (chifre (β) provado pela direção (⇒) de N.1; chifre (α)
   é simples contrapositiva).
4. N.3 (L115–124): residuais R-α/R-β honestos; `I1 A.7` ("caso do H1 fica fora",
   L91–97 do I1) corretamente aplicado a `α`/`C_{N_s}` não-padrões.
5. Sem circularidade: N.1 continua sem usar M.1/M.2/Teorema K na prova (só a
   dependência de "σ_s verdadeira" é registrada, §0/§5.5) ✓.

## Diretrizes para a v3 (condições do RECOMENDADO)

(1) **NOVO-1**: reescrever §0.3, N.1′ e N.3(R-β) como **relação aberta** (tabela acima);
checklist nº 7 reescrito; eliminar "estritamente mais forte" e a autocontradição
"mais fraca/mais forte" do mesmo parágrafo. (2) **NOVO-2**: 1 frase na direção (⇒)
com a fonte correta (`e`/`¬τ` + N.0(c)). (3) **M-2**: N.4 — separar "verdadeira" (M.2,
cadeia §5.5) de "sem prova" ((β)) e citar `Ref_EF ∈ T_PV` (`G2 §2.3`/`I1` A.5) em §1
L45/N.4 L128. (4) **Escopo em N.1′** (L96–100): acrescentar "(escopo R1/`q`-total, como
em N.1)" — e corrigir a alegação de §5.1/§6 nº 10 de que já foi propagado. (5) Nits
N1–N3.

**Com as cinco: a v2 vira v3 e vai a consolidação.** O teorema central, a dicotomia e a
cadeia de dependências estão, nesta rodada, **matematicamente de pé** — o que restou são
camadas de interpretação (π-compressão) e de redação.

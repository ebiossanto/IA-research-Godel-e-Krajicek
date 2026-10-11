# J1 — Q-compactness-over-M_0: anatomia da semente, decisão de C.3 e o Teorema K

> Frente J, **v4 (FINAL — referee RECOMENDADO, rodadas 1–4)**, 11 Out 2026.
> Marcação: **(A)** = fonte/artigo; **(P)** = próprio; **(C)** = conjectura. Contexto:
> `H1_colecao_refutacao.md` §1.1 (semente `𝒯`, verbatim), `I1_Qcompactness_ultrapoderes.md`
> (A.5 rota (α), B.3, A.7, C.3), `A_teoremas_exatos.md` (`T_PV` = universal verdadeira:
> §1.0/L18–27; **pps pode ser incompleto em modelo de `T_PV`, mas sempre sound**: L21–22;
> Condition 1 do Teorema 3: L190/L375; linha BB/Cook–Thapen: L442), `J1_referee.md`
> (rodadas 1–4; log de correções em §7). Veredito do referee: **RECOMENDADO** (v4).

## §0. Caso concreto e resultados

Caso concreto **universal**: `M_0` = qualquer modelo de `T_PV + (S2)+(S3)+(S4)` com
`Ref_P ∈ T_PV` (Condition 1 do Teorema 3 entra só em J.4, hoje **aberta** — ver §1).
Resultados:

1. **Teorema K (novo, incondicional)**: em **nenhum** tal `M_0` existe coleção interna
   `F` para a multifunção de falsificadores `∀i<m ∃y Fals(y, α_i)`. Corolário: **`T_PV +
   BB` é inconsistente com (S2)–(S4)** (a forma coletada de BB fornece o `F` proibido) —
   **(P)** coerente com o remark do artigo de que BB "invalida a análise de (1)"
   (`A_teoremas_exatos.md` L442 **(A)**; a razão dada pelo artigo é a *perda de
   universalidade do KPT* — K acrescenta o **mecanismo** ao nível da semente, mas não é
   idêntico a ele). **Isto decide a Questão J.5 da v1: negativa, em todo modelo.**
2. **Teorema J′ (C.3)**: negativa **sob (Hjoint)** (hipótese exata, §2). A análise de
   (Hjoint) colapsa, para as partes sem `¬φ`, na questão do **ponto fixo local** — a
   mesma estrutura do item 2 (a redução é de (Hjoint) ⟹ C.3; a recíproca **não** é
   reivindicada — §4).
3. **Anatomia (J.2′)**: `¬φ` não é satisfeito por **nenhuma atribuição padrão**. Se
   `M_0 ⊨ ∃r ¬φ(r)` é **aberto** (v1/v2 usavam completude interna de EF, **retraída**:
   o artigo avisa que pps pode ser incompleto em modelo de `T_PV` — L21–22 **(A)**).

## §1. Lemas

> **Lema J.0(a) (tamanho; confirmado pelo referee) (P).** `d* ∈ ℕ` codificando derivação
> EF real tem linhas — inclusive premissas — de tamanho **padrão**, e a verificação
> interna `Ref_EF(d*, ψ)` com `d*`, `ψ` de tamanho padrão é absoluta (cálculo padrão).

**Prova.** Decodificação p-tempo: entrada padrão ⟹ saída padrão. ∎
*(A v1 tinha um falso Lema J.0(b) "monotonia de tamanho de p-tempo" — contraexemplo
`f≡0` — **retirado**; a v2/v3 dispensa qualquer classificação de tamanhos, ver §2.)*

> **Lema J.2′ (`¬φ` falha em toda atribuição padrão) (P).** Para `r` padrão (numeral),
> `M_0 ⊭ ¬φ(r)`: para todo `i<m`, `(r)_i` não é derivação `P` de `(α)_i`.

**Prova.** `i` padrão: `(r)_i` é padrão — sua última linha tem tamanho padrão, enquanto
`(α)_i` pode ser de tamanho não-padrão (**descompasso de tamanhos** mata `Ref_P`;
comparação padrão é absoluta); se `(α)_i` fosse padrão, `Ref_P(r_i,(α)_i)` falso por
soundness real de `P` + `(S4)` (avaliação de circuito padrão é absoluta ⟹ falsificador
interno de `(α)_i` é real). `i` não-padrão: `(r)_i = 0` (slicing de numeral fora do
suporte — cálculo padrão). ∎

> **Retração (v2 → v3): Lema J.0′ (completude interna de EF) RETIRADO (A).**
> Verbatim L21–22: "a pps `P` may be **incomplete** in a model of `T_PV` but it will
> always be **sound** as that is expressible by a universal `L_PV`-formula". A
> completude interna **não** vale em geral; só a **soundness** (rota (α): sentenças
> universais verdadeiras ⟹ ∈ `T_PV`). Consequência: a **Condição J.4** da v2
> ("`M_0 ⊨ ∃r ¬φ(r)`") cai para **aberta** — ver §2(ii) e §6.

> **Lema J.5-sound (soundness interna de EF e de `P`) (A)+(P).** As sentenças
> `Ref_EF(d,ψ) → ∀v (v ⊨ ψ → v ⊨ ⊥)` e `Ref_P(d,β) → ∀v v ⊨ β` são **universais
> verdadeiras** de `L_PV` (prensificação padrão dos `∀∃` limitados; matriz via funções
> p-tempo de avaliação) ⟹ ∈ `T_PV` ⟹ valem em todo `M_0 ⊨ T_PV`.
> *Para listas de premissas (J′): aplicar a fórmula única à **conjunção** `ψ = ψ_1∧…∧ψ_k`
> (tamanho padrão, pois `d*` e as linhas são padrão — J.0(a)) — mesma sentença.*

## §2. Teorema J′ (C.3) e a hipótese exata (Hjoint)

> **Hipótese (Hjoint).** Toda subfamília **interna**-mente finita `L ⊆ 𝒯_{M_0}` é
> **satisfatível internamente** em `M_0`.

> **Teorema J′ (P).** Sob (Hjoint): **nenhuma** sublista internamente finita `L ⊆ 𝒯_{M_0}`
> tem refutação EF **genuína** (testemunha padrão) — C.3 é **negativa**.

**Prova.** Se `d* ∈ ℕ` genuinamente refuta `L`: por J.0(a), as premissas usadas têm
tamanho padrão; a verificação `M_0 ⊨ Ref_EF(d*, premissas, ⊥)` é absoluta; por J.5-sound
(`Ref_EF ∈ T_PV`), `M_0 ⊨ "nenhuma atribuição interna satisfaz as premissas"` —
contradiz (Hjoint). ∎

> **Análise de (Hjoint) — casos (P):**
> (i) constantes-1: satisfatíveis trivialmente ✓.
> (ii) subfamílias **contendo `¬φ`**: `¬φ` é falso em toda atribuição **padrão** (J.2′);
> sua satisfatibilidade **interna** em `M_0` é **aberta**. A pergunta aberta é feita **com
> Condition 1 do Teorema 3 como hipótese** (a hipótese do artigo): sob Condition 1,
> `M_0 ⊭ ∃d Ref_EF(d,φ)` — mas a v2 deduzia `M_0 ⊨ ∃r ¬φ(r)` por completude interna de EF,
> **retraída** (L21–22: pps pode ser incompleto em `T_PV`). Sem completude, "insatisfatível"
> nem dá refutação interna — o caso (ii) fica **em aberto**.
> (iii) subfamílias **sem `¬φ`**: compostas de `δ_N → τ_N` e constantes. A satisfação
> conjunta depende de **pontos fixos**: como circuito, `τ_N(v)` vale sse
> `∃q (q` codifica atribuição ∧ `Fals(q, (α)_{code(N,q)}) = 1)` (verbatim H1 §1.1) —
> um **ponto fixo** `q*` falsificando o disjunct que `N` escolhe **em `q*`**. *(Nota: a
> semântica em generic de H1 §1.1 diz `ν_G(τ_N)=1 ⟺ M[G] ⊨ (¬(α)_{ν_G(N)}) ∈ SAT` —
> índice `ν_G(N)`, sem a circularidade `code(N,q)`; a leitura de circuito acima é a que
> (Hjoint) exige para avaliação interna em `v` arbitrária — a correspondência nas
> duas leituras é **ponto de referee**, marcada.)*
> **(Hjoint) não está decidida** — e decidí-la é decidir C.3.

> **Dicotomia residual (P).** Ou (Hjoint) vale (⟹ C.3 negativa: Teorema J′), ou existe
> subfamília internamente insatisfatível — aí a **rota (A)** de `H1 §3.3` (refutação
> interna finita) fica viva **só se** completude interna valer para essa subfamília
> (aberto, L21–22) — e a genuinidade permanece em aberto nesse ramo.

## §3. Teorema K — a coleção interna é impossível (incondicional)

> **Teorema K (P).** Em **todo** `M_0 ⊨ T_PV + (S2)+(S3)+(S4)` (com `Ref_P ∈ T_PV`):
> **não existe** `F ∈ M_0` com `M_0 ⊨ ∀i<m Fals(F(i), α_i)`. **(A Questão J.5 da v1 é
> decidida: negativa.)**

**Prova (fundação v3: funções PV + sentenças universais verdadeiras; sem compreensão).**

Seja `G` o **símbolo de função PV** do amalgam: `G(F,α,m)` é o candidato a amalgam, e `H` o
localizador do **menor** testemunho (ambos símbololo PV, **totais por construção** —
programa p-tempo: o laço em `i<m` custa `O(m·|α|)`, pois `|α| ≥ m`). Declare-se
`p ∈ at(α_i)` como "`p` é posição de átomo da projeção PV `(α)_i`" (predicado p-tempo).
A **correção** de `G`,`H` é a sentença

> `∀m,F,α,p,i [ m = m(α) ∧ i = H(F,α,p,m) → ( (G(F,α,m))_p = 1 ↔ ( i < m ∧ p ∈ at(α_i) ∧ (F(i))_p = 1 ) ) ]`

(com `m` **guardado** por `m = m(α)` — sem a guarda a sentença é falsa para `m < m(α)`;
`at` declarada acima). Esta sentença é **verdadeira** (definição
de `G`,`H`) e, após prensificação dos `∀∃` limitados, **universal** — logo **∈ `T_PV`**
(§1.0: `T_PV` = toda sentença universal verdadeira) ⟹ vale em `M_0`, inclusive com dados
não-padrões. *(Se `H` não encontra testemunho, o lado direito é falso para todo `i` —
bicondicional com `i = H(...)` faz o que precisa.)* **(Substitui a "compreensão limitada"
da v2 — MAJOR-1 do referee.)**

1. **Localidade (lema, universal ∈ `T_PV`):** `Fals(q,β)` depende só de `q ↾ at(β)` —
   sentença universal verdadeira (avaliação de circuito lê só os átomos). Logo, para
   todo `i<m`: `σ* := G(F,α,m)` coincide com `F(i)` em `at(α_i)` (por **(S2)**, `at(α_i)`
   são par-a-par disjuntos — nada de `F(j)`, `j≠i`, escreve ali) ⟹ `Fals(σ*, α_i)`.
   *(Bits de `F(i)` fora de `at(α_i)` não atrapalham: localidade.)*
2. **Composição via localizador (MAJOR-R3: predicado de shape + sentenças universais).**
   Declare `S(α,m)` = "`α` é o circuito da forma `⋁_{i<m} (α)_i`" (o shape da disjunção —
   **de graça** para o `α` do artigo: **(S2)** o garante em `M_0`). Defina dois
   símbolos PV (totais por construção, laço `i<m` p-tempo):
   `Winv(α,σ*,i)` := avaliação da projeção `(α)_i` em `σ*`; e `Widx(α,σ*)` := **menor**
   `i<m` com `Winv(α,σ*,i)=1`, senão `m`. Quatro sentenças **universais verdadeiras**
   (∈ `T_PV` por §1.0, para `α` de shape `S`):
   > (i) `∀α,σ* [ S(α,m) → Widx(α,σ*) ≤ m ]`;
   > (ii) `∀α,σ* [ S(α,m) ∧ Widx(α,σ*) < m → Winv(α,σ*,Widx(α,σ*)) = 1 ]`;
   > (iii) `∀α,σ*,i [ S(α,m) ∧ i < m ∧ Winv(α,σ*,i) = 1 → Widx(α,σ*) ≤ i ]`;
   > (iv) `∀α,σ* [ S(α,m) ∧ Widx(α,σ*) = m → Eval(α,σ*) = 0 ]`
   — (iv) **é** a composicionalidade do `big-or` para o shape `S` (todos os disjunctos
   avaliam `0` ⟹ o `OR` avalia `0`; o localizador `Widx` evita `∀i<m` no antecedente,
   que quebraria a universalidade). Dedução **em `M_0`** (instanciação de sentenças
   universais, sem apelo a "avaliação `Δ^b_0` com dados não-padrões" — é o limite A.7):
   por §1, `M_0 ⊨ ∀i<m Fals(σ*,(α)_i)`, i.e., `Winv(α,σ*,i)=0` para todo `i<m`. Se
   `Widx < m`, (ii) dá `Winv(...)=1`, contradizendo a instância em `i = Widx` — logo
   com (i): `Widx = m`; por (iv): `M_0 ⊨ Eval(α,σ*) = 0`, i.e., `Fals(σ*, α)` ✓.
3. **Contradição:** `(S3)` (`π : P ⊢ α`, `π` interno) + soundness interna de `P` via
   `Ref_P ∈ T_PV` (**rota (α)**, universal — J.5-sound; a indução `Δ^b_0` da Nota A.5(β)
   **não** é usada e não transfere, conforme referee) ⟹ `M_0 ⊨ ∀v (v ⊨ α)` — com `Fals(σ*,α)`,
   contradição. ∎

> **Corolário K.2 (BB é inconsistente com a semente) (P)+(A).** `T_PV + BB + (S2)+(S3)+
> (S4)` é **inconsistente**: BB converte `∀i<m ∃y A_b(α,i,y)` na forma coletada
> `∃(y)_i ∀i<m A_b(α,i,(y)_i)` — matriz aberta `Δ^b_0`, `i` sharply bounded (verbatim
> L442: BB "troca `∃y_i` e `∀i`"; **legítimo** para `Fals(y,(α)_i)`, confirmado pelo
> referee) — e a forma coletada entrega exatamente o `F` proibido por K. **Relação com
> o artigo (A):** o artigo afirma que "acrescentá-lo [BB] a `T_PV` invalida a análise de
> (1)" (L442), dando como razão a **perda de universalidade do KPT**; K fornece uma
> segunda razão, **ao nível da semente** (BB amalgama os falsificadores e contradiz
> `(S3)+Ref_P`) — **coerente com, mas não idêntica à**, razão do artigo **(P)**.

> **Observação K.3 (relação com B.3 do I1) (P).** B.3(ii) proibia **seletores p-tempo**;
> K proíbe **coleções internas arbitrárias** — a escolha exigida pela amalgamação é
> impossível **em qualquer forma**. A sobrevivência de `(S4)` em `M_0` é exatamente a
> ausência dessa coleção: sem escolha, a amalgamação feita "à mão" (compreensão pura
> sobre `∃y`) falha, pois falsificadores distintos do mesmo `α_i` podem discordar —
> só o amalgam **por escolha `F`** funcionaria, e é ele que K proíbe.

## §4. O que destravou do item 2

A v1 propunha J.5 ("`M_0` adota a coleção?") como pergunta nítida. **K decide-a: não.**
O que resta do item 2 é **uma pergunta**, e ela governa C.3:

> **Questão J.6 (forma final) (P).** Para toda subfamília **interna**-mente finita sem
> `¬φ` (`N_1,…,N_k` internos): existe atribuição interna `v*` satisfazendo todos os
> `C_{N_j}` — o que (caso iii de §2) é a existência de pontos fixos `q*` com `q*`
> falsificando `(α)_{code(N_j,q*)}` para cada `j`? E para as subfamílias com `¬φ`:
> `M_0 ⊨ ∃r ¬φ(r)`? (§2(ii), aberto.)

**Redução honesta (P):** **(Hjoint) ⟹ C.3 negativa** (J′) — direção provada. A análise
de (Hjoint) **para as partes sem `¬φ`** é a questão do ponto fixo J.6(i); a recíproca
não é reivindicada (C.3 negativa não implica (Hjoint)). **Leitura:** o item 2 ficou
**sem rota de coleção** (K: morta incondicionalmente — mais forte que a barreira de
fatoração de Cook–Thapen, que restringe só a *provabilidade* de BB) e **reduzido ao
ponto-fixo J.6**, que **governa** C.3. O que Cook–Thapen restringe é a coleção (morta
mesmo sem ele); o que permanece — o ponto fixo — Cook–Thapen **não** aborda: a
instância local sobreviveu e ficou isolada com precisão cirúrgica.

## §5. Certificados para humanos (checklist)

| # | Afirmação | Verificação | Onde |
|---|---|---|---|
| 1 | Semente `𝒯 = {¬φ} ∪ {δ_N→τ_N} ∪ {C≡1}` e `τ_N = ⋁_q(q cod. atrib. ∧ Fals(q,(α)_{code(N,q)})=1)` | verbatim | `H1_colecao_refutacao.md` §1.1 |
| 2 | `T_PV` = teoria universal verdadeira de `L_PV` (fundação de K: sentenças universais) | verbatim | `A_teoremas_exatos.md` §1.0 (L18–27) |
| 3 | **pps pode ser incompleto em modelo de `T_PV`; soundness sempre** (retração de J.0′) | verbatim | `A_teoremas_exatos.md` L21–22 |
| 4 | Condition 1 do Teorema 3 ("`φ` não tem prova em `M` em nenhum pps") | verbatim | `A_teoremas_exatos.md` L190/L375/L514 |
| 5 | `Ref_P ∈ T_PV` + soundness interna universal de `P` e de EF (J.5-sound) | verbatim + prensificação | §1; I1 A.5 rota (α) |
| 6 | Funções PV `G`,`H`,`Widx`,`Winv` (amalgam, menor testemunho, localizadores) + correção universal | padrão | §3 |
| 7 | Localidade de `Fals` (só lê `at(β)`) e composicionalidade do big-or — sentenças universais | padrão (referee confirma) | §3 passos 1–2 |
| 8 | BB coleta `∀i<m∃y` (matriz aberta `Δ^b_0`); "invalida a análise de (1)" + razão KPT | verbatim | `A_teoremas_exatos.md` L442; `CONTEXTO_COMUM.md` item 11 |
| 9 | Cook–Thapen: BB não em `T_PV` a menos que fatoração difícil (não usado em K) | verbatim | L442 |
| 10 | Descompasso de tamanhos em J.2′ | 1 linha | §1 |
| 11 | Leitura de circuito vs leitura-em-generic de `τ_N` (ponto de referee) | conferir | §2(iii) |

## §6. Veredito e próximos passos

**Veredito (P):** o "caso concreto" produziu um teorema **incondicional** (K: nenhuma
coleção interna para os falsificadores, em todo modelo do artigo; corolário: `BB`
inconsistente com a semente — mecanismo ao nível da semente, coerente com o remark do
artigo) e **decisão parcial de C.3** (J′: negativa sob (Hjoint); a análise de (Hjoint)
colapsa no ponto-fixo J.6, que **governa** C.3 e é a mesma estrutura do item 2 — rotas
de coleção mortas por K). A anatomia `J.2′` mostra `¬φ` insatisfatível por atribuições
padrão; a satisfatibilidade interna ficou **aberta** (completeness retraiada).

**Próximos passos:** (1) ~~referee hostile~~ **concluído: RECOMENDADO (rodada 4)**;
(2) com K, atacar J.6 num `M_0` concreto — rota
promissora: modelo recursamente saturado de `S` (tipos recursos podem dar ou negar os
pontos fixos — decide (Hjoint) e, com ela, C.3); (3) nota editorial a Krajíček: K +
J.2′ (+ a errata da lacuna do Teorema 4, já consolidada).

**Lacunas honestas:** (Hjoint)/J.6 **aberta** (é a próxima missão); caso (ii) de §2
depende da completude interna que o artigo **não garante** (L21–22); a correspondência
entre a leitura de circuito e a leitura-em-generic de `τ_N` é ponto de referee; K.2
pressupõe a aplicabilidade de BB a `Fals(y,(α)_i)` (confirmada em rodada 2, reconfirmar);
a recíproca de J′ não vale provada (C.3 negativa ⇏ (Hjoint)).

## §7. Registro de correções (v1→v2→v3; referees rodadas 1–2)

**v1→v2 (rodada 1: 3 FATAL, 5 MAIOR):**
- FATAL-1 (J.0(b) falso `f≡0`; classificação de tamanhos não provada): J.0(b) **retirado**;
  v2/v3 dispensam tamanhos (J′ usa só J.0(a) + (Hjoint) + `Ref_EF ∈ T_PV`).
- FATAL-2 ("`C_N` tautologia real" não provada; avaliação `Δ^b_0` não-absoluta): Lema J.1
  **retirado**; substituído por **(Hjoint)** explícita + análise de casos (§2).
- FATAL-3 (caso constantes-1 só afirmado): linha própria em §2(i) ✓.
- M1–M5: soundness interna citada (A.5); §4 reescrita; J.2′ com descompasso de tamanhos;
  citação L442 corrigida; nomenclatura "Condition 1 do Teorema 3" unificada.

**v2→v3 (rodada 2: 0 FATAL, 3 MAIOR):**
- **MAJOR-1 (fundação de K)**: "compreensão limitada em `T_PV`" **trocada** por funções
  PV `G`,`H` + correção como **sentença universal verdadeira** (§1.0) — a instância de
  compreensão não é universal; Cook–Nguyen cobre `PV`, não modelos arbitrários.
- Localidade e composicionalidade **enunciadas como lemas universais** (eram apelo a
  "interno/padrão" — insuficiente com dados não-padrões, é o A.7).
- Indução `Δ^b_0` (A.5(β)) **removida** da prova de K — rota (α) (universal) basta.
- **MAJOR-2 (J.0′)**: completude interna de EF **retraída** (artigo: pps pode ser
  incompleto em `T_PV` — L21–22); **Condição J.4 → aberta**; §0.3, §2(ii), §6 ajustados.
- **MAJOR-3**: quantificadores de (Hjoint) e J.6 unificados ("interna-mente finita");
  "C.3 ≡ J.6" suavizado para **(Hjoint) ⟹ C.3** (recíproca não reivindicada); leitura
  de `τ_N` marcada como ponto de referee (código `code(N,q)` vs índice `ν_G(N)`).
- K.2 reescrito: coerência com (não identidade à) razão do artigo (perda de
  universalidade do KPT).

**v3→v3b (rodada 3: 0 FATAL, 1 MAIOR):**
- **MAJOR-R3 (passo 2 de K)**: a sentença de composição era (i) **falsa** para `α`
  malformado (falta de predicado de shape) e (ii) **não universal** (`∀i<m` no
  antecedente ⟹ `Σ_2`; a negação não prensifica). **Reescrito** com predicado
  `S(α,m)`, localizadores PV `Widx`/`Winv` e quatro sentenças universais verdadeiras
  (i)–(iv) ∈ `T_PV`; a dedução em `M_0` roda por instanciação de sentenças universais
  (`Widx ≤ m`, `Widx < m →` testemunho, minimalidade, `Widx = m → Eval = 0`) — a tese
  de K **não muda**.
- MENORES da rodada 3: `m` ligado e `at` declarada na correção de `G`/`H`; totalidade
  de `H` justificada (`O(m·|α|)`); J.5-sound reduzido a listas via **conjunção**;
  coerência de Condition 1 em §2(ii); typo.

**v3b→v4 (rodada 4: RECOMENDADO; 2 micro-correções):**
- Passo 2 de K **validado**: (iv) verdadeira para o shape `S`; as quatro sentenças são
  universais; a dedução em `M_0` está **correta, sem lacuna** (trichotomia da ordem ∈
  `T_PV` fecha `Widx = m`).
- Micro-correção (a): guarda `m = m(α)` na correção de `G`/`H` (sem ela a sentença é
  falsa para `m < m(α)`) — **aplicada**; `G(F,α,m)` unificado no texto.
- Micro-correção (b): o shape `S(α,m)` é garantido por **(S2)** (não `(S4)`/`(S1)`) —
  **aplicada**.
- Notas cosméticas do referee: `(iii)` não usada na dedução (mantida por completude do
  quadro de localizadores) e nº 6 do §5 ampliado com `Widx`/`Winv` — aplicadas.

**Confirmados pelos referees (rodadas 1–3):** J.0(a); tese de J.2′; J.4-condicional
(v2, agora retraiado); composição sem circularidade de J′; não-uso de completude de `P`;
fidelidade a C.3 e a C.1–C.3 do I1; marcação (C); **tese central de K: "CORRETA — é o
achado da v2"** (rodada 2); **passo 0 de K (correção de `G`/`H`): "sólido"**, K.2: "escopo
honesto", J.2′: "correto" (rodada 3) — restando só o refazer do passo 2.

**Autoria:** v1–v4 pelo orquestrador, guiados estritamente pelos referees
(`J1_referee.md`, rodadas 1–4 completas; veredito final **RECOMENDADO**). O Teorema K é
**descoberta da revisão**: o referee derrubou a análise de tamanhos da v1; o refúgio
((Hjoint)+ponto fixo) revelou que a coleção é impossível incondicionalmente — mais
forte que tudo que a v1 pretendia — e as rodadas 2–4 firmaram a fundação (universalidade
via `G`/`H`/`Widx`/`Winv`), retrairam a completude interna (L21–22) e fecharam o passo 2.

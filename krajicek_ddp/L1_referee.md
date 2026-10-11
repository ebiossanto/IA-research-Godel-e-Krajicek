# L1 — Relatório do referee hostile (rodada 1) — `L1_phi_insatisfativel.md`

> Referee hostile de lógica (proof complexity / modelos não-padrões). 11 Out 2026.
> Fontes conferidas: `L1_phi_insatisfativel.md`; `A_teoremas_exatos.md`; `J1_Qcompactness_M0.md`;
> `J2_ponto_fixo.md`; `H1_colecao_refutacao.md`; `I1_Qcompactness_ultrapoderes.md` (C.3);
> `CONTEXTO_COMUM.md`; **e o artigo verbatim** (arXiv:2506.20221v4, HTML integral —
> conferido nesta rodada, incl. Thm 3/4, Ref_P, passos (2)–(5), rodapé 2).

## Veredito: **REVISION** — **0 FATAL no Teorema L.1**; 3 MAIOR, 5 MENOR (escopo/justificação/encaminhamento)

A tese central (**L.1: `T_PV+(S4) ⊢ ∀r φ(r)`**) está **CORRETA** — a prova é sólida em
todos os passos atacados. Os corolários L.2/L.4 chegam a conclusões corretas. O que trava
o RECOMENDADO são três problemas de **escopo e justificação**: (M1) a nota subestima a
consequência de L.1 para o **próprio artigo** (L.1 localiza com precisão cirúrgica onde o
passo (5) do Teorema 4 precisa quebrar — a nota não o diz e chega a afirmar "consistente
com todo o artigo" de forma enganosa); (M2) **C.3 é negativa incondicionalmente por um
argumento trivial de standardness** que a nota não vê — o que invalida o desenho da tabela
§3 (linha 3 "aberto (C)") e o "exceto o canto adversarial" do §5 *para C.3*; (M3) a Nota
L.1′ exige elementaridade `Σ^b_1` **em dois sentidos** e o rotula mal como "caso especial
do no-G".

---

## §1. Teorema L.1 — ataques e veredito: **CORRETO (sem lacuna)**

### (a) Instantância de (S4) em `i<m` com `i` arbitrário de `M_0` — **OK**
`(S4)` é o axioma `∀i<m (¬α_i) ∈ SAT` = `∀i<m ∃y Fals(y,(α)_i)` (verbatim artigo, passo (2);
`F2_versao_finita.md` L34). Instanciar em `i ∈ M_0`, `i<m`, é instância legítima de sentença
da teoria. A prova usa **só** `(S4)` + `T_PV` — a afirmação "`(S2)`/`(S3)` não são precisas"
está **correta** (a fatia `(α)_i` é termo PV do corte, definível sem disjunção disjunta).
*Reserva menor (MENOR-4):* o enunciado do teorema deve dizer `T_PV+(S4)+` **dados `(α,m)`**
com `m=m(α)` — "`(S4)`" sozinho é incompleto sem os parâmetros; e "todo modelo" no cabeçalho
de L.2 deve ler "todo modelo de `T_S`".

### (b) Soundness interna de `P` — rota (α) — **OK, e mais forte do que a nota afirma**
A sentença `Ref_P(d,β) → ∀v eval(β,v)=1` prensifica para `∀d,β,v[...]` — **universal**;
é **verdadeira** porque `P` é relação CR (`∃xP(x,y)` define TAUT ⟹ `P` rejeita códigos
malformados; para β tautologia, `∀v` verdadeiro); logo ∈ `T_PV` (teoria universal verdadeira,
§1.0/A L18–27). **Importante (MENOR-2):** isto é **(A✔) verbatim**, não só "referee-validada":
o artigo diz literally "**Let `Ref_P` be the universal valid `L_PV` formula `x:P⊢y → (¬y)∉SAT`**"
(abertura da Seção 3). Upgrade o checklist nº 3 para (A✔). A instância em `v:=y` (com `y`
falsificador de (S4)) é instância legítima; a incompatibilidade `Fals(y,β)∧(y⊨β)→⊥` é
quantifier-free, universal verdadeira, ∈ `T_PV` ✓.

### (c) O salto `∀r φ(r)` — **OK, parêntese confuso**
De `∀d ∀i<m ¬Ref_P(d,(α)_i)` segue `∀r ⋀_{i<m} ¬Ref_P((r)_i,(α)_i)` por **instanciação**
`d:=(r)_i` — válido. O parêntese "(a disjunção `∀r∃i` é trivial: `φ` é a conjunção das
negações)" (L1 L34) é **gambiarra de redação** (MENOR-1): não há disjunção alguma; escrever
apenas "instanciando `d:=(r)_i`, para todo `r` e `i<m` vale `¬Ref_P((r)_i,(α)_i)`; logo a
conjunção". A direção inversa (surjetividade do corte) não é necessária e não é usada ✓.

### (d) Tipagem de `(r)_i` — **OK, verbatim no artigo**
O artigo (passo (3)): "the symbols `(y)_i` and `(z)_i` denote the **i-th string in the list
coded by y,z**" — logo `(r)_i` é a i-ésima **string** candidata a prova, e `Ref_P` (relação
em strings) está bem tipado. A prova de L.1 usa `d:=(r)_i` **arbitrário** — funciona exatamente
porque `∀d` é sobre strings arbitrárias ✓. `φ(r) = ⋀_{i<m} ¬Ref_P((r)_i,(α)_i)` corresponde
ao `||∀i<len(y)(z)_i : P ⊬* (y)_i||(r,q)` do artigo com `q` substituído pelos **bits de `α`**
(isto é: **constantes** — conferi no verbatim: "substituting the bits of α for atoms q";
**não há espelho/mirror**) — portanto `(α)_i` é o **disjuncto real** e a identificação da
nota com "o φ do artigo" está **correta**. ✓

---

## §2. MAIOR-1 — L.1 **não** é "consistente com todo o artigo" sem qualificação: ela
**localiza o gap exato do passo (5)** do Teorema 4 (a nota subestima o próprio resultado)

A Nota L.1′ (L1 L37–46) afirma que `M ⊨ ∀rφ(r)` "é consistente com todo o artigo" porque o
artigo cria o falsificador "só em `M'`". **Isto é enganoso.** Pelo verbatim do artigo:
`M' ⊨ T_PV + ¬φ ∈ SAT` (item (2) de 2.1), e `M* ⊨ ∀i<m (¬α_i)∈SAT` **(8)** por preservação
`Σ^b_1` (a sentença é `Δ^b_0`-com-parâmetros, hence `Σ^b_1(PV)`, com parâmetros `α,m ∈ M` ✓).
A prova de L.1 corre **verbatim em qualquer `M' ⊨ T_PV` em que `∀i<m ∃y Fals(y,(α)_i)` valha
para todos `i<m ∈ M'`**. Logo:

> **Corolário omitted pela nota (deve ser acrescentado):** se `M' ⊨ T_PV + ∃r¬φ(r)`, então
> existe `i_0 < m` em `M'` tal que **`(α)_{i_0}` não tem falsificador em `M'`** — o testemunho
> `σ` de `¬φ` só pode viver num **índice novo** `i_0 ∈ M'∖M`, onde `(S4)`/`(8)` **falha**.

Ou seja: L.1 **fixa com precisão cirúrgica onde o artigo precisa quebrar** — é exatamente o
passo "`by (7) i_0 is also already in M*`" (a lacuna já flagrada em `A_teoremas_exatos.md`
L242–247: `Log`-equality ≠ pertinência, sem a convenção de fechamento para strings mais
curtas). E mais forte: **sob a convenção forte** (estruturas `L_PV` contendo todas as strings
de comprimento ≤ comprimentos presentes), `Log(M')=Log(M*)` ⟹ `i_0 ∈ M*` ⟹ `(8)` dá o
falsificador de `(α)_{i_0}` em `M'` ⟹ contradição com `Ref_P` — logo **as hipóteses (2)+(3)
de 2.1 são inconsistentes com L.1 para esta instância**: o Problema 2.1 teria resposta
**negativa** para `(M,φ)` do artigo ⟹ (rodapé 2, verbatim) `P ≠ NP`. A nota precisa declarar
isto: L.1 **não** deixa o artigo "iles"; ela mostra que a única saída de `M'` é falhar em
`i_0` novo, i.e., o artigo sobrevive **exatamente se** o fechamento/`Log` falhar — a mesma
lacuna já registrada. Redação atual ("consistente com todo o artigo", §0/§5) → **reescrita
obrigatória**. *(Item (ii) da Nota: "K-FP′ dá falsificadores; L.1 proíbe só provas" — correto
✓. Item (iii): Teorema K sem conflito ✓.)*

---

## §3. MAIOR-2 — C.3 é negativa **incondicionalmente** por argumento trivial de standardness;
a tabela §3 e o "canto adversarial" estão mal desenhados **para C.3**

C.3 (verbatim `I1` L188–201): existe `L ∈ M_0` internamente-finita, sublista de `𝒯_{M_0}`, com
**refutação genuína**: `d* ∈ ℕ` derivação EF **real** e `M_0 ⊨` "toda premissa de `d*` pertence
a `L`". Argumento que a nota não vê:

1. `d*` real ⟹ (J.0(a), L1–J1) **todas as linhas, inclusive premissas, são padrão**.
2. A pertinência é igualdade de strings (absoluta) ⟹ cada premissa é **literalmente** uma
   entrada de `L ⊆ 𝒯` — i.e., um **membro padrão da semente**.
3. Pela construção da semente (H1 §1.1): `¬φ` tem tamanho `poly(|α|)` (**não-padrão**);
   `δ_N→τ_N` tem tamanho `poly(|N|+|m|)` com `m` não-padrão (**não-padrão**, para **todo**
   `N`); logo os **únicos membros padrão de `𝒯` são constantes-1** — e `C ≡ 1 em M_0` com
   `C` padrão ⟹ `C` é tautologia **real** (avaliação absoluta; `∀v` interno contém todo `v`
   padrão).
4. Derivação EF **real** de `⊥` de premissas que são tautologias reais: impossível pela
   **soundness real de EF**. ∎

Consequências para o L1:
- **L.3 está concluído corretamente, mas a justificativa citada não é a vinculante.** Um `d*`
  padrão **nem pode mencionar** `¬φ` (premissa não-padrão) — a rota "dobra ⟹ `M_0 ⊨ Ref_EF(d*,φ)`
  ⟹ proibido por Condition 1" (L1 L57–60) é **desnecessária e ligeiramente mal-posta**: com `φ`
  não-padrão, `Ref_EF(d*,φ)` com `d*` padrão é **falso trivialmente** (igualdade de linhas), não
  "proibido por Condition 1". Condition 1 continua **correta e necessária** para a outra metade
  de L.3 — a **refutação interna** (`d ∈ M_0` não-padrão; dobra interna via teorema da dedução
  de EF — citar, MENOR-3) — aí o argumento fecha ✓.
- **Tabela §3 linha 1**: "contém `¬φ` ⟹ decidido negativo (Condition 1 ⟹ L.3)" — conclusão
  certa, justificativa trocada: nenhuma premissa padrão pode ser `¬φ` nem `δ_N→τ_N` (tamanho);
  Condition 1 nem entra.
- **Tabela §3 linha 3 e §5 ("negativa em todo alcance exceto o canto adversarial `(C)`") —
  ERRADOS para C.3**: pelo argumento acima, **nenhuma** sublista (contenha ou não `¬φ`;
  ramo vazio/adversarial incluído) tem refutação genuína — C.3 é **negativa incondicionalmente
  e trivialmente**, sem Condition 1, sem L.1, sem (Hjoint). O canto `(C)` de J2 §3 pertence a
  **satisfatibilidade interna / Q-compactness (refutação interna)** — pergunta **diferente**
  (H1 §1.3; J.6). A nota (e, de passagem, a J1 — Theorem J′ dependia de (Hjoint) sem necessidade)
  superdimensionou C.3. **Correção**: reescrever §3/§5: C.3 = negativo tout court; o `(C)`
  residual = Q-compactness/refutação **interna** e pontos fixos não-padrões.
- *(Veredito de L.2 permanece certo: `(Hjoint)` falsa em todo modelo de `T_S` ✓; J′ vácuo ✓;
  "sobrevivência" da negativa de C.3 ✓ — mas pela rota trivial, não (só) por L.3+J.6-a′.)*

---

## §4. Corolário L.4 — **CORRETO e fiel** (supera, não contradiz)

Artigo verbatim (antes do Thm 3): "a pps `P` **may be incomplete** in a model of `T_PV` but it
will always be **sound** as that is expressible by a universal `L_PV`-formula". O artigo postula
**possibilidade**; L.4 mostra, **sob as hipóteses do próprio artigo** (Condition 1 é hipótese do
Problema 2.1; o artigo a verifica para o `(M,φ)` do Teorema 4 no passo (4), sob `NP=coNP` via
p-boundedness), que `φ` é **instância real**: `M ⊨ ∀rφ(r)` (L.1) e `M ⊭ ∃d Ref_Q(d,φ)` para todo
pps `Q` (Condition 1). **Supera o "may" — não contradiz nada** (o artigo nunca alega completude).
Marcação (A)+(P) honesta ✓. *Escopo (MENOR-5):* a testemunha vale no `M` **onde Condition 1 vale**
(não "em todo modelo") — a redação "sob suas hipóteses" já mitiga, mas convém fixar.

---

## §5. Nota L.1′ — Claim 2/KPT e no-G: **condicionalmente correta; rotulação errada (MAJOR-3)**

- `∃r ¬φ(r)` é `Σ^b_1` com parâmetros `α,m ∈ M` ✓ (existencial não-limitado + matriz `Δ^b_0`
  — `⋁_{i<m}` sharply bounded). A transferência de `M[G]` para `M` exige a direção
  **`M[G] ⊨ σ ⟹ M ⊨ σ`** — i.e., elementaridade `Σ^b_1` **dois sentidos**. A **preservação**
  `M→M[G]` (sentenças `Σ^b_1` verdadeiras em `M` continuam verdadeiras em `M[G]`) **não basta**.
  A nota deve explicitar: o no-G/H1 (L46: "[Kra98, Thm 4.1] … `Σ^b_1`-elementar **(A)**") pressupõe
  os dois sentidos — **conferir no [Kra98] que a direção reversa está incluída**; se só houver
  preservação, a rota válida é a do próprio no-G (G2 Thm 2.1(a′)), não "L.1 + elementaridade".
- "caso especial do no-G do H1 Thm 1.1" — **má rotulagem**: no-G cobre `G` universais fechados sob
  EF-provability + constantes-1; a afirmação da nota ("generics **cofinais `Σ^b_1`-elementares**")
  é uma classe **possivelmente maior** — é rota **paralela/independente**, não caso especial.
  Corrigir para "rota paralela, coerente com o no-G".
- Itens (ii)/(iii) (K-FP′, Teorema K — sem conflito): **corretos** ✓ (L.1 proíbe provas, não
  falsificadores; (S4) é exatamente a ausência da coleção que K proíbe).

---

## §6. §3–§5 (tabela e veredito) — demais saltos

- §3 linha 2 (J.6-a′: satisfatível ⟹ sem refutação) — correto ✓ (refutação interna/genuína
  contradiz satisfatibilidade interna por soundness de EF).
- §4 checklist: item 3 → (A✔) verbatim (MAJOR/MENOR-2 acima); itens 1,2,5,9 conferidos ✓;
  item 6: adicionar citação do **teorema da dedução de EF** (dobra `ψ⊢⊥ ⟺ ⊢¬ψ`, overhead
  polinomial; internamente a derivação dobrada pode ter tamanho não-padrão — legítimo em `M_0`).
- §5 "Próximos passos" e "Lacunas honestas": a lacuna `i_0∈M*` já citada deve ser **promovida
  a item central** (MAJOR-1) — é ela que decide se a incompatibilidade de L.1 com (2)+(3) de 2.1
  é real ou contornável.

## §7. Registro de correções esperadas (v1 → v2)

- **MAJOR-1**: acrescentar o corolário "falsificador de `φ` em `M'` ⟹ índice novo `i_0` com
  `(α)_{i_0}` infalsificável" + redigir a relação exata com o passo (5)/lacuna `i_0∈M*` +
  consequência (2.1 negativa para a instância sob convenção forte ⟹ rodapé 2). Substituir
  "consistente com todo o artigo" por análise qualificada.
- **MAIOR-2**: §3/§5 reescritas — C.3 negativa **incondicional** (argumento de standardness;
  escrevê-lo); `(C)` residual = Q-compactness/refutação **interna**; Condition 1 reescopada para
  a refutação **interna** de `{¬φ}`.
- **MAIOR-3**: Nota L.1′ — elementaridade em dois sentidos explícita; "caso especial" → "rota
  paralela".
- **MENOR-1..5**: parêntese do salto; checklist (A✔) de `Ref_P`; dedução de EF citada; escopo
  `T_PV+(S4)+(α,m)`/"todo modelo de `T_S`"; escopo de L.4 ao `M` com Condition 1.

**Veredito final: REVISION.** Com as correções acima (em particular MAJOR-1 e MAIOR-2), a
frente L entrega um resultado forte e honesto: L.1 é um teorema correto e não-trivial que
isola a fratura exata do Teorema 4.

---

# Revisão da v2 — veredito: **REVISION** (quase-recomendado: 1 MAJOR-leve, 3 MENOR, 0 FATAL)

> Referee hostile — rodada 2, 11 Out 2026. Arquivo conferido: `L1_phi_insatisfativel.md` (v2,
> 159 linhas), contra a rodada 1 deste relatório e o artigo verbatim (arXiv:2506.20221v4).
> **L.1 permanece CORRETA (não tocada, só limpa).** Das 3 correções MAJOR: MAJOR-3 e os
> MENORES estão **aplicados integralmente**; MAJOR-2 está **aplicado com uma peça em falta**;
> MAJOR-1 está **aplicado pela metade** (o pinçamento está certo; a dicotomia da convenção
> forte, não escrita). Duas correções pontuais + uma adição recomendada separam a v2 de
> RECOMENDADO.

## §1. MAJOR-1 (§2, Proposição L.1′) — **correto; identificação do `i_0` certificada; falta 1 consequência**

- **"`M' ⊨ ∃r¬φ(r)` ⟹ `M' ⊭ (S4)`" — CORRETO.** Contrapositiva da prova de L.1 dentro de
  `M'` (hipótese `M' ⊨ T_PV` declarada ✓). A afirmação forte ("o testemunho aponta `i_0<m` com
  `α_{i_0}` infalsificável em `M'`") é também correta: o testemunho `σ` dá `Ref_P((σ)_{i_0},(α)_{i_0})`
  e a soundness em `M'` (`Ref_P ∈ T_PV`) torna `(α)_{i_0}` tautologia interna — sem falsificador. ✓
- **Identificação `i_0`(L.1′) ≡ `i_0`(passo (7)) — honestamente marcada como (P), e o referee
  AGORA A CERTIFICA no verbatim:** o artigo (passo (5)) define `i_0` exatamente como o índice do
  falsificador de `φ` ("σ falsifies φ … Hence σ=(σ_i)_{i<m} and we have `M' ⊨ σ_{i_0}:P⊢α_{i_0}`
  for some `i_0<m`"). Logo a correspondência é **(A✔)+(P)** — promover na lacuna honesta.
- **Restricção "`i_0 ∈ M*` com `(S4)` lá ⟹ contradição" — CORRETO** (o falsificador em `M*`
  persiste em `M'` por absolutidade de avaliação p-tempo em dados internos). A redação "o que o
  artigo obtém por forçamento" é imprecisa (o `M'` vem da **hipótese 2.1AF**, não do forçamento —
  MENOR-1).
- **FALTA (MAJOR-leve):** a v2 não escreve a dicotomia da rodada 1: **sob a convenção forte**
  (estruturas `L_PV` fechadas em todas as strings de comprimentos presentes + `Log(M')=Log(M*)`),
  `i_0 ∈ M*` seguiria automaticamente ⟹ (2)+(3) de 2.1 seriam **inconsistentes** com L.1 para
  esta instância ⟹ **Problema 2.1 negativo para `(M,φ)` ⟹ `P ≠ NP`** (rodapé 2, verbatim). A v2
  pinça a lacuna mas não escreve o fork — é ele que transforma o "pinçamento" em consequência
  sobre o artigo. Acrescentar 3 linhas em §2.

## §2. MAJOR-2 (§3, Teorema L.3′) — **essencialmente correto; uma peça não demonstrada + uma sobreafirmação**

- **(a) J.0(a) (premissas padrão de `d*` padrão): ok ✓** — citada corretamente.
- **(b) "todo membro padrão de `𝒯` = só constantes-1": conclusão CORRETA, prova com duas
  pendências:**
  1. **Peça carga não escrita: `α` é não-padrão.** O argumento "embutem os parâmetros
     não-padrões" pressupõe `α` (e `m`) não-padrões; `m` não é excluído de ser padrão a priori,
     mas `α` **é** não-padrão — e isto tem prova de 1 linha que o arquivo deve incluir: se `α`
     fosse padrão, `Ref_P(π,α)` (axioma (S3), soundness ∈ `T_PV`) daria `α` tautologia **real**;
     `(S4)` dá `(α)_i` falsificável internamente ⟹ (autualidade de avaliação p-tempo p/ circuito
     padrão) realmente falsificável para `i<m`; `m` padrão (determinado por `α`); `(S2)`
     disjuntude ⟹ união real dos falsificadores falsifica `α` — **contradição**. Logo `α`
     não-padrão, `|α|` não-padrão. Sem este lema, o "≥ |α|" flutua.
  2. **Sobreafirmação "`≥ |α|` ou `≥ |m|`"**: a parte "`≥ |m|`" é **desnecessária** (e invulnerável
     se `m` fosse padrão). O-carregador correto é: `τ_N` (espelho de `α` sobre ~`|α|` átomos,
     pela projeção PV `D`) e `¬φ` (`⋀_{i<m}` sobre os bits de `α` como **constantes** — verbatim
     conferido, sem espelho livre) têm códigos de tamanho `poly(|α|)` — **não-padrão**, e o
     disjuntivo `δ_N→τ_N` herda não-padrão de `τ_N` **mesmo se `δ_N` fosse padrão**. Reescrever
     a frase de tamanho nesses termos; aí o ramo `δ_N→τ_N` está coberto para **todo** `N`,
     padrão ou não. ✓ (Conclusão do teorema preservada.)
- **(c) Fecho por soundness real de EF: ok ✓** (derivação real, axiomas = tautologias reais
  `C≡1 em M_0` com `C` padrão — inclusão interna ⟹ real — regras preservam verdade).
- **(d) L.3″ (escopo limpo): CORRETO ✓** — C.3 decidida sem Condition 1; não-compactude máxima
  no plano interno sob Condition 1; adversarial restrito ao plano interno. É a correção exata do
  MAJOR-2.
- **MENOR-2 (enunciação):** o parêntese de L.3′ "(nem **internamente**, com verificação absoluta)"
  é ambíguo: a prova cobre só `d* ∈ ℕ`; com `d*` padrão a verificação interna é absoluta e o
  argumento fecha ✓, mas a refutação interna com `d` **não-padrão** é a Q-compactness **aberta**
  (corretamente preservada em L.3″). Reescrever para "nenhum `d* ∈ ℕ` refuta — genuinamente nem
  por verificação interna absoluta; refutação interna com testemunha não-padrão permanece
  (Q-compactness)". Hoje o parêntese emenda com L.3″ de forma tensa.

## §3. MAJOR-3 — **aplicado integralmente ✓**
§2: elementaridade `Σ^b_1` **dois sentidos**, direção `M[G]→M` explícita, "só a preservação
`M→M[G]` não basta", Claim 2/KPT como **rota paralela** ao no-G (não caso especial). Correto:
`∃r¬φ(r)` é `Σ^b_1` com parâmetros `α,m ∈ M` — a direção reversa transfere. ✓

## §4. MENORES — **todos aplicados ✓**
- Escopo `T_PV+(S4)+` **dados `(α,m)`** nomeados: §1 ✓ (regra "escopo da sentença").
- Parêntese-gambiarra "∀r∃i" retirado, com nota explícita (L46–47) ✓; a prova fecha direto pela
  conjunção ✓.
- Escopo de L.4 a `M` com Condition 1: §4 ✓ ("may" → "é, nesta instância; supersede sem
  contradizer" — fiel ao verbatim L21–22) ✓.

## §5. Regressão e consistência (§0/§4/§6/§7)
- §0/§4/§6/§7 **consistentes** entre si e com o corpo ✓; §7 registra fielmente a rodada 1 ✓.
- **Nada substancial da v1 se perdeu**: L.2 mantido (+ observação correta de que J′ é
  **desnecessário** — antecipa a rodada 1); a tabela §3 v1 foi substituída por L.3′+L.3″
  (melhor); checklist ampliado ✓; "lacunas honestas" atualizadas ✓.
- Único item da v1 a recuperar: a menção de que `(S2)`/`(S3)` são **desnecessárias** para L.1
  sobrevive no §0 item 1 ✓ — ok, nada a recuperar.

## §6. Registro de correções esperadas (v2 → v3)
1. **(MAJOR-leve, obrigatório)** L.3′ §3: incluir o lema "`α` é não-padrão" (1 linha: §2(b)1) e
   reescrever a análise de tamanhos só com o carregador `τ_N`/`¬φ` ⊇ bits de `α` (`≥ poly(|α|)`);
   retirar "`≥ |m|`".
2. **(MENOR, obrigatório)** L.3′ enunciação: escopar o parêntese "(nem internamente…)" a
   verificação **absoluta** (testemunha padrão); refutação interna não-padrão = Q-compactness
   (aberta, como L.3″ já diz).
3. **(recomendado)** §2: acrescentar a dicotomia da convenção forte (fork 2.1AF ⟹ 2.1 negativa
   para a instância ⟹ `P≠NP` via rodapé 2) e corrigir "obtém por forçamento" → "por hipótese 2.1AF";
   promover a identificação `i_0` para **(A✔)+(P)** (certificada nesta rodada).

**Veredito: REVISION.** Com os itens 1–2 aplicados (e o 3 recomendado), **RECOMENDADO** — a v2
aplicou o essencial da rodada 1 sem tocar no núcleo corretíssimo de L.1.

---

# Revisão da v3 — veredito: **REVISION** (micro: 4 erratas pontuais; 0 FATAL; nada substancial resta)

> Referee hostile — rodada 3, 11 Out 2026. Conferido: `L1_phi_insatisfativel.md` (v3, 206
> linhas) vs. rodadas 1–2 deste relatório; L.1 intacta. **Os três MAJOR estão fechados no
> essencial**; restam quatro micro-defeitos, um deles de direção de seta numa implicação —
> tem de ser corrigido antes de RECOMENDADO.

## §1. MAJOR-1 (§2) — fechado, com 2 micro-defeitos de redação

- **(a) `i_0` = (P)+(A✔) com certificação: ok ✓** — a promoção reproduz fielmente a minha
  certificação da rodada 2 (o artigo define `i_0` como índice do falsificador de `φ`). Nit:
  "o `i_0` do passo (7)" — (7) é a equação `Log(M*)=Log(M')`; o `i_0` aparece no passo (5)
  invocando (7). Ler "do passo (5) que invoca (7)".
- **(b) "obtido por hipótese (2.1AF)": ok ✓** (substitui corretamente "por forçamento").
- **(c) DICOTOMIA — honesta ✓, mas com dois defeitos:**
  1. **ERRATA OBRIGATÓRIA (direção de seta):** "(2)+(3) valem e 2.1 falha para a instância
     **(⟸ P≠NP)**" — o rodapé 2 diz **`¬2.1 ⟹ P≠NP`** (e a própria frase anterior escreve-o
     corretamente). "⟸" inverte a implicação — trocar por **`⟹`** (ou apagar o parêntese).
  2. **ERRATA OBRIGATÓRIA (rótulo):** "as condições **(2)+(3)** do Problema 2.1" como se
     fossem a convenção — mas **(2) é a existência do falsificador**, não convenção; a
     convenção forte é **fechamento + (3)**, e **(1)** (preservação) entrega **(8)**. A frase
     correta: "sob fechamento+(3), (8)+(L.1′) tornam **(1)+(2)+(3) mutuamente inconsistentes**
     para esta instância". O conteúdo (fork honesto, sem reivindicar `P≠NP`; "o artigo não
     pode ter ambas"; alcance marcado) está certo ✓.

## §2. MAJOR-2 (§3) — fechado; L.3a está CORRETA (inclusive a absolutidade)

- **(a) Lema L.3a: correto ✓.** A instanciação `v := σ*` é legítima: `σ*` é **padrão**
  (amalgama de falsificadores de partes padrão, `m` padrão — elementos `≤ |α|` padrão são
  padrão) ⟹ `σ* ∈ M_0` ✓. A absolutidade de `Fals` está **correta como escrita**: a
  testemunha de `(¬α_i) ∈ SAT` é **limitada** (`y < 2^{|α_i|}`, com `|α_i|` padrão) — sentença
  `Δ^b_0` com parâmetros padrão ⟹ absoluta ⟹ o falsificador pode ser tomado **padrão** mesmo
  partindo de `(S4)` interno ✓. `(S3)`+soundness interna dão `eval(α,σ*)=1`; avaliação real
  absoluta (α, σ* padrão) dá `=0` — contradição ✓. **Nenhuma correção necessária.**
- **(b) Carregador corrigido: ok ✓** — "`≥ |m|` retirado; `τ_N`/`¬φ` ⊇ bits de `α` como
  constantes, tamanho `≥ |α|` não-padrão (L.3a); cobre o ramo mesmo se `δ_N` fosse padrão"
  — exatamente a correção da rodada 2 ✓.
- **(c) Reescopo de L.3′: ok ✓** — só refutações **genuínas**; parêntese ambíguo retirado;
  internas não-padrão = Q-compactude (L.3″ preservada verbatim ✓).

## §3. MENORES / regressões — 2 inconsistências de texto

1. **§0 item 2 (L20–21) desatualizado:** continua dizendo "`δ_N` embute `m` … **todos de
   tamanho não-padrão**" — contradiz o §3 corrigido (`m` pode ser padrão; o ramo `δ_N→τ_N`
   é descartado por `τ_N`, não por `δ_N`). Corrigir a linha-resumo do §0.
2. **§7b mente:** afirma "§5 checklist ampliado **(Lema L.3a)**", mas a tabela §5 (9 linhas)
   **não contém** linha de L.3a — acrescentar a linha 10 ou corrigir §7b.
3. §6/§7/§7b: consistentes ✓; nenhuma regressão substantiva — L.1, L.2, L.4, L.3″ intactos;
   nada da v1/v2 bom se perdeu ✓.
4. **Caracteres CJK: corpo limpo ✓** — o único `\p{Han}` no arquivo é a própria citação do
   typo na linha de log da §7b ("排除ada" → "já é descartado") — aceitável; opcionalmente
   reescrever a citação sem os caracteres.

## §4. Registro de correções esperadas (v3 → v4)
1. §2: "(⟸ P≠NP)" → "**(⟹ P≠NP)**".
2. §2: "(2)+(3) … convenção forte" → "fechamento+(3) tornam (1)+(2)+(3) inconsistentes (via (8))".
3. §0 item 2: alinhar ao §3 (carregador = `τ_N`/`¬φ`; `δ_N` irrelevante).
4. §5: acrescentar linha do Lema L.3a (ou corrigir §7b).

**Veredito: REVISION (micro).** Substância fechada: L.1 correta e intacta; L.1′ + dicotomia
(certificada; só seta e rótulo); L.3a correta; L.3′ reescopada; L.3″ preservada. Com as quatro
erratas acima aplicadas: **RECOMENDADO**.

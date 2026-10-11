# Referee I1 — relatório completo sobre `I1_Qcompactness_ultrapoderes.md`

**Referee hostile (lógica: proof complexity / teoria dos modelos / ultrapoderes). 11 Out 2026.**
Fontes conferidas: `I1_Qcompactness_ultrapoderes.md` (alvo), `CONTEXTO_COMUM.md`,
`A_teoremas_exatos.md` §1.0–§1.3, `H1_colecao_refutacao.md` §0, §1.1, §1.3, §2.2,
`G2_semente_Fsent.md` §§1–2, `F2_versao_finita.md` §0, §2.
Marcação: **(A)** = fonte/artigo; **(P)** = próprio; **(C)** = conjectura.

---

## 0. Quadro-resumo

| # | Item | Veredito | Severidade |
|---|------|----------|------------|
| 1 | Lema A.1 (sub-interno de `[0,k]`) | **PARCIAL** — enunciado correto, prova falha no caso geral; cláusula extra não provada | **MAIOR** |
| 2 | Teorema A.2 (trivialidade) | **FALHA** — a passagem central é inválida; conclusão iluminada só sob restrição | **FATAL** |
| 3 | Lema B.1 (totalidade padrão) | **CORRETO** (duas ressalvas técnicas) | MENOR/ESTILO |
| 4 | Teorema B.2 (barreira do ultrapoder) | **CORRETO no núcleo**; generalização mal formada | MENOR (bem sinalizado pelo próprio texto) |
| 5 | Observação B.3 (sharpness) | **PARCIAL** — conclusão qualitativa defensável, frase central errada e distinção não feita | **MAIOR** |
| 6 | Corolário B.4 | **FALHA** — texto corrompido + sobreafirmação sobre o Problema 2.1 | **MAIOR** |
| 7 | Teorema C.1 (transferência Łoś) | **PARCIAL** — estratégia Łoś correta, enunciado ambíguo e RHS mal definido para `M_0` não-padrão | **MAIOR** |
| 8 | Prop. C.3 e §4 ("fechado") | **FALHA** — "decidido/fechado" não segue; redução ≠ decisão | **FATAL** |

**Veredito global: REVISION** (não REJECT: B.1/B.2 são corretos e têm valor; não RECOMENDADO:
A.2 e a §4 são o eixo do documento e não passam como estão).

---

## 1. Lema A.1 — **PARCIAL**, severidade MAIOR

**Local:** §1, Lema A.1, enunciado + parênteses finais da prova.

**O que está correto (declarado explicitamente):**
- A *conclusão* é verdadeira para `M ⊨ T_PV`: se `k ∈ ℕ` é padrão e `M ⊨ ∀x (x ∈ A → x ≤ k)`,
  então `A ⊆ {0,…,k}` externamente, logo `A` é externamente finito. **CORRETO.**
- O passo "i ≤ k com `i` não-padrão exige `k` não-padrão" **é válido em modelos arbitrários de
  `T_PV`**, desde que se escreva o argumento: a sentença
  `σ_k := ∀x (x ≤ k → x = 0 ∨ x = 1 ∨ … ∨ x = k)` é universal (matriz quantifier-free, com `≤`
  primitivo) e **verdadeira em `ℕ`**, logo `σ_k ∈ T_PV` (teoria universal verdadeira, `A`
  §1.0/`F2` §0), logo vale em **todo** `M ⊨ T_PV` — com `k` padrão, todo `i ∈ M` com `i ≤ k` é
  um numeral padrão. A prova do arquivo **não** faz isso; ela só o afirma entre parênteses.

**Falhas:**
1. **(MAIOR)** A prova é dada **só para ultrapoderes** (`ℕ^ω/U`, Łoś ponto a ponto). O caso geral
   é "coberto" pelo parêntese *"(o caso geral: quase-isomorfismo / representação de `A` por uma
   sequência `A_n ⊆ [0,k_n]`)"* — que é **irrelevante/sem sentido** para um `M` arbitrário (um
   `M` qualquer não é ultrapoder nem tem tal representação). O enunciado não restringe `M`.
   **Correção sugerida:** reescrever a prova geral via `σ_k ∈ T_PV` (2–3 linhas, acima); manter a
   prova ultrapoder como ilustração. Conferir antes que `≤` é símbolo primitivo de `L_PV` (se
   `x ≤ y` for abreviatura `∃z (x+z=y)`, `σ_k` não é universal e o argumento precisa ser reformulado).
2. **(MAIOR)** A cláusula *"todo `i ∈ A` é padrão-computável a partir da descrição de `A`"* é
   **não provada e provavelmente falsa como está escrita**: se a descrição de `A` é um código
   não-padrão de `M`, "computar" a partir dela exige uma apresentação efetiva de `M` — num
   ultrapoder com `U` não-computável, `A ∩ ℕ = {i ≤ k : {n : i ∈ A_n} ∈ U}` **não** é
   computável a partir de `A = [(A_n)]`. A parte *correta* e suficiente é só "é subconjunto
   genuíno de `{0,…,k}` (tabela finita de `k+1` bits, bem definida)". **Correção:** restringir a
   "determinado como subconjunto de `{0,…,k}`" ou apontar o que "padrão-computável" significa
   (relativamente a `U`? a uma apresentação de `M`?) e marcar **(C)**.
3. **(ESTILO)** "`A ∈ M` … `M ⊨ ∀x (x ∈ A → x ≤ k)`" usa `∈` de conjunto numa linguagem
   `L_PV` sem símbolo de pertinência; convém explicitar a convenção (características/circuitos,
   como em `G2` §1.1 e `H1` §1.1: `A` é um predicado definido com parâmetro em `M`).

---

## 2. Teorema A.2 — **FALHA**, severidade FATAL

**Local:** §1, Teorema A.2, prova ("`Ref` é p-tempo, logo **absoluto** … comprimento real
`ℓ(d)`, finito como número real … Soundness **real** …") e Corolário A.3.

**Por que a passagem não é rigorosa (três problemas encadeados):**

1. **(FATAL) "`ℓ(d)` finito como número real" é falso/no-op para `M` não-padrão.** `d ∈ M` e
   `ℓ(d) ∈ M`; em um modelo **não-padrão** (exatamente a configuração de `H1` §0) `ℓ(d)` pode ser
   **não-padrão**. Nesse caso `d` codifica uma derivação de comprimento não-padrão — **não** é um
   objeto derivação EF finito no metalível, e a indução de soundness **externa** (sobre derivações
   finitas reais, "qualquer comprimento real") **não se aplica**. Isto é precisamente o que o
   referee S1 forçou a retractar em `H1` §1.3: *"uma refutação é um elemento de `M` codificando
   uma derivação EF cujo comprimento é possivelmente não-padrão"* — A.2 reabre a ferida sem nota.
2. **(FATAL) "Absolutude de `Ref` p-tempo" não produz o que se quer.** Para entradas padrão,
   `Ref` é absoluto ✓; para `d` não-padrão não existe "computação externa" com a qual `M` possa
   "coincidir" — `f^M(d)` é a computação **interna** de `M`. O que se tem direito a afirmar é
   **soundness interna**: `Ref_EF` (versão de comprimento padrão `k`, matriz quantifier-free com
   `k` desdobrado) é sentença universal verdadeira ⇒ `∈ T_PV` ⇒ vale em `M` **com quaisquer
   parâmetros** (inclusive `d` não-padrão) ⇒ `M ⊨ "nenhum y ∈ M satisfaz todas as premissas"`.
   Isso é **insatisfatibilidade interna**, não externa.
3. **(FATAL) "Nenhuma atribuição booleana *real* satisfaz as condições de `T_f`" está mal
   definida nas hipóteses dadas.** O enunciado permite condições com `código ∈ M`
   **não-padrão**: os átomos podem ser elementos não-padrões de `M`; avaliar um circuito
   não-padrão sob uma atribuição externa não é um processo bem definido em `V` (a ordem interna
   dos gates é externamente não-bem-fundada: modelos de `PA`/`T_PV` têm cadeias descendentes
   externas). E insatisfatibilidade interna ("nenhum `y ∈ M`") é **mais fraca** que "nenhuma
   atribuição real" — mais funções existem em `V` do que em `M`.

**A correção possível (a tese sobrevive com hipótese extra):**
- **(a)** Restringir `T_f` a **condições padrão** (fórmulas reais, átomos padrão, finitos). Aí:
  soundness interna (`Ref_EF ∈ T_PV`, instanciada) ⇒ nenhum `y ∈ M` falsifica as premissas; e
  **toda atribuição real sobre os (finitos, padrão) átomos tem código padrão ∈ `M`** ⇒
  insatisfatibilidade **real** ✓ — *sem* precisar que `ℓ(d)` seja padrão. Conclusão salva,
  prova nova.
- **(b)** Se condições não-padrão forem permitidas, a conclusão honesta é só
  `M ⊨ ¬∃y ⋀ Prem` (interna), e o Corolário A.3 perde "o modelo `M` não acrescenta poder algum".
- **(c)** `Corolário A.3` afirma **"equivale"**; A.2 prova só `⟸`... na verdade só
  `(refutação interna) ⟹ (insatisfatibilidade)`. A volta `(insatisfatibilidade) ⟹ (refutação
  interna)` é **completude de EF**, que (i) para condições padrão vale (fato padrão: cite), e
  (ii) para condições/componentes não-padrões **não** é sentença universal e não está em `T_PV` —
  **não provada**. Corrigir "equivale" → "implica", ou provar a volta com a hipótese de padrão.

---

## 3. Lema B.1 — **CORRETO**, severidade MENOR/ESTILO

**Local:** §2, Lema B.1. **Veredito explícito: o lema está correto.**

- **Caso `m = 0`:** `α = ⊥` (disjunção vazia); `(S3)` dá `π : P ⊢ ⊥`, contradiz soundness real
  de `P` **(A)** ✓. **CORRETO.**
- **Caso `m ≥ 1`:** `(S3)` + soundness real (instância padrão: `π` padrão, teste p-tempo
  absoluto) ⇒ `α` tautologia real; `(S4)` dá falsificadores reais `y_i` para cada `i < m`
  (`m` padrão ⇒ `k+1` escolhas, objeto real de suporte finito padrão); `(S2)` (átomos disjuntos
  ⇒ sem conflito) ⇒ a união `y` é atribuição bem definida e falsifica cada `α_i` e logo a
  disjunção (disjunção falsa exige **todos** os disjunctos falsos) ⇒ contradição ✓.
  **CORRETO.**
- **Alegação (A) verificada:** `CONTEXTO_COMUM.md` L16–17 diz literalmente *"Totalidade: se cada
  `α_i` tivesse atribuição falsificante, a união dessas atribuições (átomos disjuntos ⇒ sem
  conflito) falsificaria a disjunção inteira, contradizendo `P ⊢`"*, e `A_teoremas_exatos.md`
  §1.3 a transcreve como **(A✔)**. **A alegação de que o artigo afirma exatamente este lema
  está CORRETA.** Matiz menor: o artigo formula a totalidade como propriedade de *entradas de
  `DD_P`*; `B.1` a formula como "nenhuma instância **padrão** de `(S2)–(S4)` com `P` sounde" — a
  equivalência é imediata (contrapositiva), mas convém dizê-lo.
- **(MENOR)** Antes de unir, cada `y_i` deve ser **restrito aos átomos de `α_i`**: um falsificador
  arbitrário pode atribuir valores a átomos fora de `supp(α_i)` e a união crua conflitaria fora
  do domínio relevante. Uma linha resolve (`y_i ↾ atoms(α_i)`).
- **(MENOR)** O trecho *"teste p-tempo absoluto — cobre objetos padrões e não-padrões"* é
  irrelevante num lema de instâncias **padrões** e reforça a confusão de nível do item 2.
- **(MENOR)** Explicitar: `(¬α_i) ∈ SAT` para `α_i` **padrão** ⇒ falsificador real (absolutidade
  de `Fals` + restrição de `y ∈ M` aos átomos padrão de `α_i`).

---

## 4. Teorema B.2 — **CORRETO no núcleo**, severidade MENOR

**Local:** §2, Teorema B.2.

**O que está correto (declarado explicitamente):**
- **A aplicação de Łoś está correta.** `M = ℕ^ω/U` é o ultrapoder **primeira-ordem** da estrutura
  `L_PV`-padrão; `(S2)`, `(S3)`, `(S4)` são sentenças de 1ªª ordem com parâmetros:
  `(S3)` = `Prf_P(π,α)` (p-tempo ⇒ fórmula quantifier-free via símbolos de função PV, para o
  `P` **fixo** — verificabilidade p-tempo não é "compartilhada" entre componentes, é a mesma
  fórmula); `(S2)` = checagem sintática p-tempo de "disjunção disjunta com `m` determinado por
  `α`" ✓; `(S4)` = `∀i<m ∃y Fals(y,(α)_i)` ✓ (projeção `(α)_i` = função PV `D`). Logo
  `M ⊨ ψ(π,α,m) ⟺ {n : ℕ ⊨ ψ(π_n,α_n,m_n)} ∈ U`, e o conjunto é não-vazio ⇒ existe `n` com
  `ℕ ⊨ (S2)∧(S3)∧(S4)` ⇒ **instância padrão** (todo componente de um ultrapoder de `ℕ` é objeto
  padrão) com `P` sound **(A)** ⇒ **Lema B.1** ⇒ contradição ✓.
- **Soundness uniforme dos componentes ✓** (a soundness de `P` é propriedade externa de `P`, não
  depende de `n`).
- **O salto "ultrapoder = Łoś" está ok:** modelos de `T_PV` são estruturas de 1ªª ordem em
  `L_PV` (com `exp`/`|·|` se presentes); Łoś vale para **qualquer** linguagem de 1ªª ordem, então
  "objetos/fórmulas não-padrão" **não** criam sutileza: Łoś cobre parâmetros não-padrões de `M`
  diretamente. **CORRETO.**
- **(MENOR)** A generalização *"nenhum `M` com a propriedade de Łoś para `(S2),(S3),(S4)` com
  parâmetros (i.e. `M ⊨ ψ ⟺` quase-todo componente `⊨ ψ`)"* não está bem formada: "componente"
  não está definido para um `M` qualquer (ultrapoder de quê? quais componentes?). O próprio
  arquivo reconhece nas **Lacunas honestas** (§6) que isso é **(C)** — **mas o enunciado do
  teorema está rotulado (P)**. Corrigir: enunciar `B.2` só para `ℕ^ω/U` **(P)**, e a
  generalização como **(C)** com definição explícita (ex.: "para `M ≅ ∏_{i∈I} ℕ/U`, ou `M`
  elementar-no-falso sobre a família de componentes").
- **(MENOR)** Convém escrever explicitamente: "(S1) não é usado na prova (o que se prova é mais
  forte: `(S2)–(S4)` já são inmodéis)".

---

## 5. Observação B.3 — **PARCIAL**, severidade MAIOR

**Local:** §2, Observação B.3.

**Correto:**
- `m` não-padrão ⇒ `M ∩ m` contém **todos** os numerais padrão ⇒ é externamente infinito ✓ — a
  alegação de que a "união" de todos os falsificadores tem suporte externamente infinito está
  **CORRETA**.
- A coerência com (i) `M ⊨ S` existindo: **conferido** — `F2` §2(3) diz literalmente *"Sendo
  consistente, `S` tem modelo"* (com (2): consistência **sob (ST)** via KPT). A citação está
  certa, mas **deve** notar a condicionalidade em `(ST)` (o arquivo não nota — MENOR).
- A direção "`S` apoia-se na assimetria interna/externa de finitude" é qualitativamente
  defensável e coerente com `H1` §1.3 e `G2` §2.3.

**Falhas:**
1. **(MAIOR)** *"a 'união' … externamente infinita — **não é número real algum** — logo não
   falsifica nada"*: **erro de categoria**. (a) A união **existe em `V`** como função
   conjunta (Replacement/união de pares ordenados — `V` não tem problema com isso); o que **não
   existe** é **código em `M`** (não é elemento do universo de `M`). (b) Um falsificador é
   **atribuição**, não número — "não é número real algum" não é a frase certa.
2. **(MAIOR) A distinção pedida ("união" vs. 'atribuição em `M` que falsifica toda a
   disjunção') NÃO está bem feita — e a resposta é mais forte do que o texto sugere.** Um
   `y ∈ M` falsificando a disjunção `⋁_{i<m} α_i` é **exatamente** um `y` que falsifica
   **todos** os `α_i` (`i<m`) — e, por `(S2)`, "fusão" e "atribuição comum" são o **mesmo**
   objeto (restringir `y` aos átomos de `α_i` dá falsificadores `y_i`; fusão dos `y_i` dá `y`).
  E esse `y` **é proibido internamente**: `(S3)` + `Ref_P ∈ T_PV` **(A)** dão
  `M ⊨ "α é tautologia"`, i.e. `∀y ∈ M eval(α,y)=1` — logo **nenhum** `y ∈ M` falsifica a
   disjunção, com ou sem formato de união. Portanto a fricção `(S3)∧(S4)` em `m` não-padrão é
   **exatamente a sentença coletada `∃z ∀i<m Fals((z)_i,(α)_i)` = conteúdo de `BB`**, como
   `G2` §2.3 já provou (**(A+P)** lá) — `B.3` deveria citar `G2 §2.3 (R3 ≡ BB)` em vez de
   presentear a exterioridade da união como a razão. **Correção sugerida:** reescrever a
   Observação dizendo: (1) internamente, `(S3)+Ref_P` já excluem qualquer falsificador comum em
   `M`; (2) externamente, a fusão existe em `V` mas não é elemento de `M`; (3) a sentença que
   faria existir o objeto coletado em `M` é literalmente `BB` (Cook–Thapen indisponível) — e é
   isso que `S` "explora". A frase "`S` é a teoria que se apoia na assimetria interna/externa"
   pode ficar, agora justificada.
3. **(MENOR)** "`|M ∩ m|`-muitos blocos" — a indexação é por `i ∈ M∩m` (índices), e os blocos só
   são "disjuntos" pelo `(S2)` **interno**; dizer que a validade da fusão transfere para o
   exterior exige absolutidade de `(S2)` para fórmulas não-padrão (p-tempo, plausível, mas
   declarar).

---

## 6. Corolário B.4 — **FALHA**, severidade MAIOR

**Local:** §2, Corolário B.4.

1. **(MAIOR — texto) Frase truncada/corrompida:** *"exclui a classe dos ultrapoderes e**它的**
   iterações sobre `ℕ`"* — caractere chinês `它的` (="seus/suas") no meio do português;
   provável intenção: *"e **suas** iterações"*. A frase inteira é um parêntese auto-interruptor
   (*"(que inclui construções tipo-ultrapoder sobre `ℕ`? — …)"*) que não fecha sintaticamente.
   **Correção:** reescrever: *"a menção do autor a 'countable or recursively saturated' **(A✔)**
   refere-se a uma classe universal de modelos para o Problema 2.1; contáveis têm tamanho
   `ℵ_0` e ultrapoderes de `ℕ` por `ω` têm `2^{ℵ_0}`, logo **a barreira B.2 não exclui** esses
   modelos — ela exclui apenas a classe dos ultrapoderes (e suas iterações) sobre `ℕ`."*
2. **(MAIOR — conteúdo) Sobreafirmação:** *"Nenhum modelo candidato ao **Problema 2.1**/à
   aplicação do artigo pode ser ultrapoder sobre `ℕ`"* — **só a segunda metade é provada.**
   `B.2` exclui ultrapoderes de `ℕ` como **modelos de `S`** (i.e. como `M` da aplicação do
   Teorema 4 / de `H1` §0). Para o **Problema 2.1** em geral (`M ⊨ T_PV` + Condition 1),
   ultrapoderes de `ℕ` **não** são excluídos por `B.2` — são modelos de `Th(ℕ)` perfeitamente
   elegíveis. **Correção:** apagar "/ao Problema 2.1" ou restringir a "candidato **à aplicação do
   Teorema 4** (i.e. modelo de `S`)".
3. **(MENOR)** "e suas iterações sobre `ℕ`" **não é provado no arquivo** — `B.2` cobre
   ultrapoderes; iterações `ℕ^ω/U` iterado satisfazem Łoś em cada estágio e o argumento se
   repete, mas isso é **(P) novo, uma linha a escrever** (ou apagar).
4. **Correto (declarado):** o raciocínio de cardinalidade (contáveis não são ultrapoderes de `ℕ`)
   está **CERTO**, e a honestidade ("a barreira é restrição de classe, não elimina os modelos que
   o artigo sugere") é acertada.

---

## 7. Teorema C.1 — **PARCIAL**, severidade MAIOR

**Local:** §3, Teorema C.1.

**Correto:**
- A **estratégia** está correta: a afirmação `∃d (Ref(d, L) ∧ L sublistasub-interna de 𝒯)` é
  sentença **de 1ªª ordem com parâmetros** — `Ref` p-tempo ⇒ fórmula quantifier-free via
  símbolos de função PV; `L` é uma lista codificada em `M` (`p(d) ⊑ 𝒯` = `∀j<|p(d)| p(d)_j ∈ 𝒯`,
  com "∈ 𝒯" definido por fórmula — ver abaixo); e Łoś aplica-se ✓. **CORRETO.**
- Caso `M_0 = ℕ`: componentes padrão, "refutação EF real (finita)" com premissas sublista de
  `𝒯_n` está bem definido ✓.

**Falhas:**
1. **(MAIOR) "`𝒯` é internamente um objeto `∈ M`" é impreciso.** Pela construção de `H1` §1.1,
  `𝒯 := {¬φ} ∪ {δ_N → τ_N : N ∈ Names} ∪ {C : C ≡ 1 em M}` — a parte `{C : C ≡ 1 em M}` é uma
  **classe definível** (`M ⊨ EF ⊢ C`, i.e. `∃d' Ref(d',C)`), não um conjunto codificado em `M`,
  e `Names` é um predicado/objeto com parâmetros. **Correção:** "família **definível por fórmula
  de 1ªª ordem com parâmetros `∈ M`" — a conclusão (1ªª ordem com parâmetros) **sobrevive**, mas a
  frase atual é falsa como está.
2. **(MAIOR) Ambiguidade grave no enunciado:** *"`M ⊨ '∃ refutação EF interna de **toda** a
  semente 𝒯'` (premissas internamente `⊆ 𝒯`)"* — "**de toda a semente**" sugere refutar
  `𝒯` inteira; "**premissas ⊆ 𝒯**" (e a Questão de `H1` §1.3, "`T_f ⊆ 𝒯`") é **sublista**. São
  sentenças diferentes. **Correção:** escrever uma vez
  `∃d ∃L (L é lista ∧ L ⊑_int 𝒯 ∧ Ref(d,L))` e usá-la igualmente no RHS.
3. **(MAIOR) RHS mal definido para `M_0` não-padrão.** *"Nos componentes, 'refutação EF real' =
   derivação finita real"* — se `M_0 ⊨ S` é **não-padrão** (o venue da §4!), um `d ∈ M_0` com
  `M_0 ⊨ Ref(d,L)` pode ter comprimento não-padrão — exatamente o erro **FATAL** do item 2
  repetido. **Correção:** ou (a) restringir `C.1` a `M_0` **padrão** (`ℕ`), ou (b) escrever o RHS
  como interno: `{n : M_0 ⊨ ∃d Ref(d, L_n)} ∈ U` com o `L_n` definido a partir dos parâmetros
 -componente. Também definir `𝒯_n` (semente construída com os parâmetros componentes
  `(φ_n, α_n, m_n, Names_n, …)`).
4. **(ESTILO)** "comprimento interno, suporte" etc. ok; marcar a parte "compreensível apenas sob
  a convenção de `H1` §1.1" com referência cruzada.

---

## 8. Proposição C.3 e §4 — **FALHA (sobreafirmação)**, severidade FATAL

**Local:** §3 Proposição C.3; §4 itens 1–3; §6 Veredito ("a pergunta … **decide** … **fechada**").

1. **(FATAL) "`A pergunta herdada do H1` está **fechada** / **decidida**" não segue.** O que os
   teoremas davam é: **(B.2)** o sub-caso "ultrapoder sobre `ℕ` na configuração de `H1` (que
   exige `M ⊨ S`)" é **vazio** — isso **CORRETO** (e `Cor. C.2` está certo nisso); e **(A.2)**
   uma **redução condicional** `(refutação interna de `T_f` externamente finito) ⟹
   (insatisfatibilidade)`. Redução **não é decisão**: `H1` §1.3 distingue dois casos —
   *(A)* existe `T_f` finito refutado internamente, *(B)* toda parte finita é EF-consistente
   mesmo assim sem `G` universal — e **I1 não distingue nenhum dos dois**. A existência (ou
   não) de `T_f` insatisfatível dentro de `𝒯` permanece **exatamente a pergunta aberta de `H1`**.
   **Correção:** trocar "decidido/fechado" por "**reduzido**: para ultrapoderes de `ℕ`, vazio
   (B.2); para finitude externa, reduzido a insatisfatibilidade real (A.2 em sua forma corrigida);
   a pergunta de existência continua **aberta** — é o caso (A)/(B) de `H1` §3.3".
2. **(MAIOR) `(i) "trivial para finitude externa"`** herda o FATAL do item 2 (a prova de A.2) e
   subestima o conteúdo: mostrar que `𝒯` tem uma parte **realmente** insatisfatível **é** o
   problema (não é trivial).
3. **(MAIOR) Corolário A.3 "equivale"** — não provado (só `⟹`; a volta é completude de EF, ver
   item 2(c)). Como `§4.1(i)` e `C.3` ("a resposta **não** depende de `M_0` … colapsa a real")
   se apoiam nisso, arrastam o mesmo furo.
4. **(MAIOR) Proposição C.3:** *"sublista interna `L ∈ M_0` (internamente finita, externamente
   possivelmente infinita) … com **refutação EF real**"* — **contradição terminológica**: uma
   derivação **real** tem premissas finitas externamente; para `L` externamente infinita só
   faz sentido "**refutação EF interna**". Trocar "real" → "interna" (e aí a Proposição fica
   como pergunta bem formulada).
5. **(MENOR) `§4.3`:** "a sublista interna-finita insatisfatível … é **exatamente** a porta do
   item 2 (instância local de `∀i<m ∃y`)" — a igualdade "exata" é **(C)**, não **(P)**; rotular.
6. **(MENOR) `§6`:** "B.2 … é **novo**" — hedge sugerido ("novidade a verificar contra a
   literatura"); "auto-certificado pelo próprio remark de totalidade" exagera: `B.1` é o remark
   **(A)**, o conteúdo de `B.2` é a aplicação de Łoś **(P)**.

---

## Veredito global: **REVISION**

**Por que não REJECT:** o Teorema **B.2** (barreira do ultrapoder) está **correto** com
argumento limpo (Łoś + instâncias padrão + `B.1`), o **Lema B.1** reproduz fielmente a
totalidade do artigo **(A✔, conferido em `CONTEXTO_COMUM.md` L16–17 e `A` §1.3)**, e a direção
geral (barreira de classe + venue `M_0 ⊨ S`) é produtiva. **Por que não RECOMENDADO:** o eixo
§1 (`A.1`/`A.2`/`A.3`) tem uma **falha FATAL** na passagem central, `B.3` e `B.4` contêm frases
erradas/corrompidas, `C.1`/`C.3` têm ambiguidades que tornam os enunciados mal formados, e a
§4/§6 declara "**decidido/fechado**" o que só foi **reduzido**.

**Correções obrigatórias (para passar a RECOMENDADO):**
1. Reescrever a prova de `A.2` via soundness interna + restrição a condições padrão (ou rebaixar
   a conclusão a insatisfatibilidade interna); corrigir `A.3` ("equivale" → "implica", com
   completude de EF citada onde aplicável).
2. Corrigir a prova de `A.1` no caso geral (`σ_k ∈ T_PV`) e remover/reformular
   "padrão-computável".
3. Reescrever `B.3` (erro de categoria; citar `G2 §2.3 (R3 ≡ BB)`; a proibição do falsificador
   comum vem de `(S3)+Ref_P`, não da cardinalidade da união).
4. Sanear `B.4` (caractere chinês, parêntese truncado; apagar "/ao Problema 2.1"; "iterações" =
   (P) com uma linha de prova ou apagar).
5. Reformular `C.1` (sentença única explícita; `𝒯` = família definível; RHS interno ou `M_0`
   padrão) e `C.3` ("real" → "interna").
6. Trocar "decidido/fechado" por "reduzido/parcialmente decidido" em §4.1 e §6, declarando
   aberto o caso `(A)/(B)` de `H1` §3.3.

**Itens explicitamente CORRETOS (registro obrigatório):** Lema `B.1` (casos `m=0` e `m≥1`, e a
alegação de que o artigo o afirma); núcleo do Teorema `B.2` (Łoś com parâmetros, uniformidade de
soundness, componentes padrão); raciocínio de cardinalidade do `B.4` (ultrapoderes de `ℕ` são de
tamanho `2^{ℵ_0}`, logo não excluem os modelos contáveis citados pelo autor); estratégia de
Łoś do `C.1` (a afirmação é de fato sentença de 1ªª ordem com parâmetros, uma vez que `𝒯` é
família definível); `Cor. C.2` ("a pergunta é **vazia** para ultrapoderes do artigo") — segue de
`B.2` + a exigência de `M ⊨ S` em `H1` §0.

---
---

# Revisão da v2 (pós-correções)

**Alvo:** `I1_Qcompactness_ultrapoderes.md`, **v2 (pós-referee)** — lida integralmente.
Acima permanece o registro completo da v1 (veredito **REVISION**: 2 FATAL, 5 MAIOR).

## A. Status das 7 correções listadas na §7 da v2

| # | Correção (§7 da v2) | Status | Frase |
|---|---|---|---|
| 1 | **FATAL 1** — A.2→Lema A.2 (soundness interna) + absolutidade só para dados padrão; "A.3 equivale"→A.4 só com `⟹` | **PARCIAL** | A mecânica de `A.3` ficou correta para dados padrão e a "equivale" virou só `⟹`, mas a prova de `A.2` invoca indução Δ^b_0 "provável em `T_PV`" (indisponível na convenção universal-verdadeira do próprio corpus) e a restrição a **fórmulas-padrão** torna `A.3` **inaplicável** às condições da semente `𝒯` — ver FATAL-R1 abaixo. |
| 2 | **FATAL 2** — escopo rebaixado ("vazia no subcaso ultrapoder; reduzida, não decidida") | **RESOLVIDA** | §4.2 e §6 declaram explicitamente "reduzida, **não** decidida", mantêm abertos os casos (A)/(B) de `H1` §1.3, e "fechado" ficou restrito ao subcaso ultrapoder-de-`ℕ` (que `B.2` torna vazio). |
| 3 | **MAIOR 1** — `A.1` prova geral + remoção de "padrão-computável" | **PARCIAL** | "padrão-computável" foi removido ✓ e ultrapoderes foram dispensados ✓, mas a nova justificativa "por definição de números não-padrões: todo `x ∉ ℕ` excede todo padrão" é handwave: em modelo arbitrário ela depende de `σ_k = ∀x (x ≤ k → x = 0 ∨ … ∨ x = k)` ser sentença **universal verdadeira** ⇒ `∈ T_PV` (o argumento pedido na v1), e o §5 item 6 ainda diz "indução fraca" (`T_PV` não tem esquema de indução). |
| 4 | **MAIOR 2** — `B.3` erro de categoria → mecanismo correto (soundness interna + escolha) | **PARCIAL** | O erro de categoria sumiu e o novo mecanismo está certo, mas o "fato padrão **(A)**" que sustenta a peça central (`T_PV ⊬ Σ^b_1-choice` via "PV ≈ IΣ₁+exp no qual Σ₁-choice não é provável") é **duvidoso/trocado** — ver ataque (b). |
| 5 | **MAIOR 3** — `B.4` texto corrompido, escopo "Problema 2.1"→"modelos de `S`", "iterações" rebaixada | **PARCIAL** | No enunciado de `B.4` tudo foi corrigido ✓ (caractere chinês ausente; escopo = modelos de `S`; "iterações" removida), mas a **§6 regrediu**: "restrição de classe nova sobre os modelos do **Problema 2.1**" repete o erro corrigido, e o novo parêntese "recursamente saturados (não coincidem com ultrapoderes de `ℕ`)" é falso (ultrapoderes de `ℕ` são ℵ₁-saturados, logo recursamente saturados). |
| 6 | **MAIOR 4** — `C.1` "objeto ∈ M"→"família definida"; "refutação real"→"interna" | **PARCIAL** | Ambos os reparos foram feitos ✓ e o RHS para `M_0` não-padrão ficou coerente, mas a lista de parâmetros está incompleta (`(π,α,m,P)` — faltam `φ`, `p`/`Names`, espelhos), `𝒯^{list}` e `𝒯_n` nunca são definidos e a sentença única `∃d∃L (…)` permanece apenas implícita. |
| 7 | **MAIOR 5** — `C.3` "refutação real"→"interna" + limite A.4 embutido | **PARCIAL** | A contradição terminológica foi removida ✓ e a pergunta da `A.4` foi embutida ✓, mas "realmente não-satisfatível" continua **sem definição** para `L` externamente infinita com fórmulas não-padrões (o caso que `A.3`/`A.4` não cobrem) e a "Proposição" contém pergunta retórica no enunciado formal. |

## B. Os 3 pontos novos

### (a) Lema A.2 + Teorema A.3 — **PARCIAL** (quase correto; 1 FALHA de prova, 1 FATAL de escopo)

- **CORRETO (o resultado de A.2):** a sentença universal fechada `∀d,T,v (Ref_EF(d,T) → v`
  falsifica `conj(T)`) é **universal e verdadeira em `ℕ`** (`Ref_EF` p-tempo ⇒ quantifier-free
  via símbolos de função PV; soundness real no metalível) ⇒ `∈ T_PV` ⇒ vale em **todo**
  `M ⊨ T_PV` com **quaisquer parâmetros**, inclusive `d` de comprimento não-padrão. Esse é o
  caminho rigoroso e ele fecha a soundness **interna**.
- **FALHA (a prova escrita):** "a indução sobre os passos `< ℓ(d)` é limitada (Δ^b_0) —
  **provável em `T_PV`**" é **falso** na convenção do corpus (`T_PV` = teoria universal
  verdadeira, `A` §1.0 / `F2` §0): instâncias de indução Δ^b_0 não são sentenças universais e
  não pertencem a `T_PV`. **Correção:** trocar a rota pela sentença universal verdadeira acima
  (uma linha) e enunciar a forma **com premissas** (`premissas(d) ⊆_int T_f` + `conj(T_f)`),
  que é o que `A.3` usa e o enunciado atual omite.
- **CORRETO (a mecânica de A.3 para dados padrão):** "v real ⇒ v padrão ⇒ v ∈ M ⇒ M avalia
  corretamente" **passa** em `M` arbitrário: (i) todo objeto padrão pertence a todo `M ⊨ T_PV`
  (a subestrutura gerada por 0 satisfaz as verdades universais de `ℕ` e é `≅ ℕ`); (ii) funções
  p-tempo **concordam em entradas padrão** (`f^M(n) = (f(n))^M`, sentença universal verdadeira) —
  nenhuma sutileza quebra aqui. Só a terminologia "Δ^b_0-completude para parâmetros padrão" é
  imprecisa (dizer: absolutidade de funções p-tempo em entradas padrão; `§5` item 7).
- **FATAL-R1 (escopo, novo):** `A.3` exige **fórmulas-padrão**, mas as condições da semente
  `𝒯` são **códigos não-padrões** (`¬φ`, `δ_N → τ_N` dependem de `m`, `α` não-padrões) — logo
  `A.3` **não se aplica a nenhum `T_f ⊆ 𝒯` não-trivial**, enquanto **§0.1, §4.1(i) e
  `C.2(ii)`** o vendem como resposta ao caso de finitude externa da pergunta de `H1`. Para
  `T_f ⊆ 𝒯` só se obtém insatisfatibilidade **interna** (`A.2`). A `A.4` ainda justifica a
  inaplicabilidade por uma razão incompleta ("a semente inteira é externamente infinita"),
  sem notar a razão certa (fórmulas não-padrões). **Correção:** reescroner §0.1/§4.1(i)/`C.2(ii)`
  como "para `T_f` de fórmulas-padrão, `A.3`; para `T_f ⊆ 𝒯`, só insatisfatibilidade interna —
  lacuna declarada".

### (b) Observação B.3 — **PARCIAL** (mecanismo CORRETO, fundamentação FALHA)

- **CORRETO:** (1) falsificador comum `σ ∈ M` de `α` é proibido por `(S3)` + `Ref_P ∈ T_PV`
  (`M ⊨ ∀v (v ⊨ α)`) — argumento correto e é o mecanismo do artigo; (2) para `k < m` padrão a
  escolha é finita — é o que derruba os componentes (`B.1`) ✓; (3) a **conclusão** "a
  amalgamação sobre `i<m` não-padrão não se conclui em `T_PV`" é **verdadeira**: é literalmente
  a sentença coletada `∃z ∀i<m Fals((z)_i,(α)_i)` = conteúdo de `BB` (`G2` §2.3, "R3 ≡ BB";
  Cook–Thapen).
- **FALHA (o fato (A) invocado):** "`T_PV` não prova Σ^b_1-choice (**fato padrão**: … PV ≈
  `IΣ₁+exp` no qual Σ₁-choice não é provável)" é, no mínimo, **inverossímil e em tensão com a
  própria referência citada**: o witnessing de Buss (`§5` item 8!) é precisamente um teorema de
  **funções escolha Σ^b_1** em `S^1_2`, e `S^1_2 ⊆ IΣ₁+exp ≈ PV`. **Correção:** fundamentar a
  não-provabilidade **em `T_PV`** por **Cook–Thapen (`BB` não é provável em `T_PV`) (A)** +
  `G2 §2.3`, que já estão no corpus; reescrever `§5` item 8.
- **Ligação com KPT — legítima mas precisa de condicionalidade:** a implicação rigorosa é
  "amalgamação ∈ `T_PV` ⟹ `S` inconsistente ⟹ KPT derruba `(ST)`", logo "**sob `(ST)`**,
  a consistência de `S` via KPT ⟹ amalgamação ∉ `T_PV`" — a redação atual ("o que **confirma**
  que nenhuma amalgamação … pode ser válida") soa incondicional, e a `§4.3` ("depende
  **exatamente** da falta de Σ^b_1-choice") exagera: é condição **necessária** (sob `(ST)`),
  não "exatamente" (a existência de `M ⊨ S` continua dependendo de KPT/`(ST)`).

### (c) Teorema C.1 + Proposição C.3 — **PARCIAL**

- **C.1 — transferência Łoś CORRETA:** a sentença `∃d∃L (L ⊑_int 𝒯 ∧ Ref_EF(d,L))` é de 1ªª
  ordem com parâmetros (família definível ✓ — reparo "objeto ∈ M" aplicado), e Łoś com parâmetros
  dá a equivalência; ambos os lados agora dizem "**refutação EF interna**", o que conserta o RHS
  para `M_0` não-padrão (para `M_0 = ℕ` degenera corretamente a refutação real finita). Resíduos
  **MENOR**: parâmetros incompletos (faltam `φ`, `p`/`Names`, espelhos), `𝒯^{list}`/`𝒯_n` não
  definidos, notação "⊥ ∈ d'" errada — nada disso derruba o teorema.
- **C.3 — incorpora o limite A.4 conceitualmente certo, formalmente incompleto:** pedir
  "refutação interna **+** captura de insatisfatibilidade genuína" é a consequência certa da
  `A.4`, mas "realmente não-satisfatível" **não está definido** para `L` internamente
  finita/externamente infinita com fórmulas não-padrões (exatamente o caso que `A.3`/`A.4` não
  cobrem — ver FATAL-R1), e o enunciado é uma pergunta retórica ("?") dentro de uma
  "Proposição" — convertê-la em Definição/Pergunta com a noção explicitada.

## C. Demais verificações (§5, §6, §7)

- **§5 item 8:** contém a alegação falha do item (b) — **reescrever** (Cook–Thapen BB).
- **§5 item 6 / `A.1`:** "indução fraca" — usar a rota `σ_k ∈ T_PV` (universal-verdadeira).
- **§5 item 4, 5, 7, 9, 10:** citações adequadas ✓ (Chang–Keisler §4.4 para Łoś; Buss para
  soundness real; exemplo `PA + ¬Con(PA)` para não-absolutitude com dados não-padrões é bom ✓).
- **§5 "Lean … `A.1` (num modelo finito/`DLO` trivial)":** inadequado — modelos de `T_PV` são
  discretamente ordenados, não `DLO`; especificar os axiomas a formalizar (ESTILO).
- **§6:** mantém **"restrição de classe nova sobre os modelos do Problema 2.1"** — regressão do
  MAIOR 3 (corrigir para "modelos de `S` / da aplicação do Teorema 4").
- **§4.1** ainda diz "(i) **trivial** para partes externamente-finitas (A.3)" — arrasta o
  FATAL-R1; **§4.3** "depende exatamente" — condicionar a `(ST)`.
- **§4/§6 — honestidade:** o rebaixamento exigido está presente e é claro ✓; a `§7` mapeia as 7
  correções fielmente ao relatório da v1 ✓, mas erra a contagem ("**6** itens declarados
  corretos" — a lista tem **5**) e a nota de autoria é coerente com o processo observado ✓.

## D. Veredito da v2: **REVISION**

**Progresso real (por que não REJECT):** o FATAL 2 da v1 está **resolvido** (escopo honesto:
"vazia" só para ultrapoder-de-`ℕ`, "reduzida, não decidida" no venue geral); `B.1`/`B.2`
continuam corretos e intactos; `B.3` trocou o erro de categoria pelo mecanismo **certo**
(soundness interna + escolha/coleção); `A.3` está mecanicamente rigoroso para dados padrão;
`C.1`/`C.3` perderam as contradições terminológicas.

**O que ainda impede RECOMENDADO:**
1. **FATAL-R1 (escopo):** `A.3` só cobre fórmulas-padrão, logo **não decide** o caso de
   finitude externa da pergunta de `H1` (as condições de `𝒯` são não-padrões) — §0.1, §4.1(i),
   `C.2(ii)` precisam ser reescritos com a lacuna declarada.
2. **MAIOR-R2:** prova do Lema `A.2` invoca indução Δ^b_0 "provável em `T_PV`" (falso) — trocar
   pela rota da sentença universal verdadeira e enunciar a forma com premissas (`conj(T_f)`).
3. **MAIOR-R3:** `B.3`/`§5` item 8 — sustentar `T_PV ⊬ Σ^b_1-choice` por **Cook–Thapen (BB) +
   `G2 §2.3`**, não por "IΣ₁+exp sem Σ₁-choice" (em tensão com o witnessing de Buss); condicionar
   a coerência KPT a `(ST)`.
4. **MAIOR-R4:** `§6` — remover "modelos do **Problema 2.1**" (regra de escopo do `B.4`).
5. **MAIOR-R5:** `A.4` — para instâncias **padrão** a completude de EF é **clássica** (não
   "aberta, tipo P vs NP"); o que é aberto é a **limitação de tamanho** (⇔ `NP vs coNP`), e para
   condições não-padrões a noção de insatisfatibilidade real nem está definida.
6. **MENOR:** `A.1` via `σ_k ∈ T_PV`; `B.4` parêntese "recursamente saturados ≠ ultrapoderes"
   (falso: ultrapoderes de `ℕ` são ℵ₁-saturados); `C.1` parâmetros/`𝒯_n` definidos; `C.3`
   pergunta formal; contagem da `§7` (5, não 6).

---
---

# Revisão da v3 (final)

**Alvo:** `I1_Qcompactness_ultrapoderes.md`, **v3 (pós-referee, 2 rodadas)** — foco nos 4 blocos
novos solicitados. Acima permanecem os registros completos da v1 (REVISION: 2 FATAL + 5 MAIOR) e
da v2 (REVISION: FATAL-R1 + MAIOR R2–R5).

## Item 1 — §1: A.3, A.4, A.5, A.6, A.7

| Item | Veredito | Severidade |
|---|---|---|
| Lema A.2 (completude clássica de EF) | **CORRETO** | — (MENOR de rótulo: é fato padrão de proof complexity (Buss), não vem do artigo; rotular "(A)-padrão/citação externa") |
| Proposição A.3 (⟸ em qualquer `M`) | **CORRETO** | — |
| Teorema A.4 (⟹ em `M` Σ₁-sound) | **CORRETO como teorema, mas superhipotetizado** | MAIOR |
| Contraexemplo A.5 | **FALSO** | **FATAL** |
| Corolário A.6 | **VERDADEIRO, mas com gloss falso** | MAIOR |
| A.7 (limite: fórmulas não-padrão) | **CORRETO** | — |

- **A.3 ✓:** `d*` real existe por completude de EF; `Ref_EF(d*,T_f)` é cálculo finito padrão e
  correto em todo `M ⊨ T_PV` (absolutidade de função p-tempo em entradas padrão). Fecha.
- **A.5 ✗ FATAL — refutação direta.** `Con(EF) = ∀d ¬Ref_EF(d,∅)` é **sentença universal
  verdadeira em `ℕ`** (`Ref_EF` p-tempo ⇒ matriz quantifier-free via símbolos de função PV;
  soundness real: nenhum `d` deriva `⊥` sem premissas) ⇒ `Con(EF) ∈ T_PV` ⇒ **todo**
  `M ⊨ T_PV` satisfaz `¬∃d Ref_EF(d,∅)`, com `d` padrão ou não. Logo `T_PV + ¬Con(EF)` é
  **inconsistente** — a hipótese "se `T_PV` é consistente" não ajuda. A invocação de Gödel II
  falha em dois pontos: (i) `T_PV` **não é r.e.** (é a teoria de *todas* as verdades universais),
  e Gödel II exige axiomatizabilidade efetiva; (ii) `Con(EF)` é ela mesma axiomática em `T_PV`.
  `∅` é lista de fórmulas-padrão e realmente satisfatível — isso está certo, mas não salva o
  contraexemplo: ele não existe. O "mecanismo" descrito (passos não-padrões validados
  internamente) só ocorre em teorias fracas demais para induzir sobre derivações; `T_PV` não é
  uma delas (contém a soundness universal de EF).
- **Consequência — o "quadro exato" da §0/§4 está invertido.** Para `T_f` padrão, o `⟹` vale em
  **todo** `M ⊨ T_PV`, sem Σ₁-soundness: de `M ⊨ Ref_EF(d,T_f)`, a sentença universal verdadeira
  `U := ∀d,Γ,v (Ref_EF(d,Γ) → Eval(conj(Γ),v)=0)` (soundness de EF com premissas; `conj`,`Eval`
  p-tempo) pertence a `T_PV`, logo `M ⊨ ∀v Eval(conj(T_f),v)=0`; um candidato real `v*` é
  padrão, tem código padrão `∈ M`, e a avaliação é absoluta (dado padrão) `⇒ =1` — contradição.
  **Isto é exatamente o caminho que a revisão da v2 prescreveu** e que a §7 (log R2) diz ter sido
  abandonado por A.5.
- **A.4:** a hipótese está **bem formulada e é suficiente** (Σ₁-sound para parâmetros padrão;
  exemplos — ultrapoder por Łoś, `M ⊨ Th(ℕ)` — **corretos**; prova `∃d Ref` Σ₁ ⇒ `d` padrão ⇒
  soundness real ⇒ insatisfatível ✓), mas é **desnecessária** (acima). Torná-la condição do
  teorema só se sustenta pela falsidade de A.5.
- **A.6:** o enunciado é **verdadeiro** (`⟸`=A.3, `⟹`=A.4, completude clássica ✓; nota
  P-vs-coNP sobre *tamanho* correta e bem usada), mas o gloss "com contraexemplo mostrando a
  necessidade de Σ₁-soundness (**A.5**)" é **falso**, e a versão real é mais forte: a
  equivalência vale para **todo** `M ⊨ T_PV` (com `T_f` padrão).
- **A.7 ✓:** honesto e essencialmente certo (não-absolutude de avaliação com dados não-padrões;
  `A.3`/`A.4` são restringidos por definição a fórmulas-padrão). Reserva (MENOR): o motivo mais
  preciso é que "insatisfatibilidade **real**" de fórmulas não-padrão é **indefinido** — não só
  "não-absoluto"; declarar assim.
- **Rastros do FATAL (todos a corrigir junto):** §0.1 ("falha para `M` arbitrário: Contraexemplo
  A.5"), §4.1(i) ("com contraexemplo mostrando a necessidade"), §5 item 7
  (`M ⊨ T_PV + ¬Con(EF)`), §6, e `C.3` premissa (a).

## Item 2 — §2: B.3(ii) (seletor p-tempo) — **CORRETO**

- **A prova de 3 linhas fecha:** se `f` é PV com `M ⊨ ∀i<m Fals(f(i),(α)_i)`, o amalgamador
  `σ* = ⋃_{i<m} f(i)` é computável em tempo `p(m,|α|)` — exige **`m ≤ |α|`** (artigo `A` §1.2;
  **citar**); `(S2)` (suportes disjuntos) garante fusão sem conflito, logo `σ*` bem definida
  `∈ M`; `σ*` falsifica todo disjunto ⇒ falsifica `α = ⋁_{i<m} α_i` ⇒ contraria `(i)`
  (`(S3)` + `Ref_P ∈ T_PV`). **Sem circularidade:** `(i)` é independente (não usa B.1/B.2);
  `(ii) → (iii)` ok, e `(iii)` pressupõe que até escolha **interna arbitrária** falha — o que é
  verdade e cabe em uma linha: de `z` que empacota os falsificadores, um *flatten* p-tempo de
  `z` produz `σ* ∈ M` falsificando `α` — mesmo `(i)`.
- **MENOR:** formalizar os quantificadores ("não existe `f` PV tal que `M ⊨ ∀i<m …`", com
  escopo em `M`); nota que sem `(S4)` o item é vazio-facilmente (sem falsificadores, não há
  seletor) — o caso interessante é `M ⊨ (S1)–(S4)`, já o contexto.
- **KPT:** escopo marcado ("sob as hipóteses da prova (NP=coNP e (ST))") ✓ — mas a frase
  seguinte "Isto **confirma** que nenhuma amalgamação ingênua pode ser válida em `T_PV`" ainda
  soa incondicional: manter "**sob (ST)`**" ou sustentar a versão incondicional em Cook–Thapen
  (BB) (MENOR residual do MAIOR-R3).

## Item 3 — §3: C.1 e C.3

- **C.1 — CORRETO.** Parâmetros `(π,α,m)` com `P` **fixo e definido uniformemente** estão
  **corretos**: `P` é um sistema fixo, `Prf_P` é fórmula fixa (não parâmetro) ✓; `φ`, `p`/`Names`,
  espelhos e átomos são sintaticamente determinados por `(α,m)` ✓; `𝒯_n` **definido** ("semente
  avaliada nos parâmetros componentes `(π_n,α_n,m_n)`") ✓; Łoś com parâmetros ✓. Reservas
  (MENOR): `π` não entra na semente (parâmetro inofensivo, mas declarar por que é listado);
  "cópia correspondente de `M_0`" = cada coordenada é `M_0` — esclarecer.
- **C.3 — PARCIAL.** Avanço real: a contradição terminológica sumiu e o qualifier
  "**não-espúria**" está explicitado como o cerne ✓. Porém: (a) a premissa "(a) refutações
  espúrias existem para `M` arbitrário (**A.5**)" é **falsa** (item 1); (b) "a **crença**
  `M_0 ⊨ 'L tem refutação'` é Σ₁-sound **para este `L`" segue **sem definição**: Σ₁-soundness é
  propriedade de teoria/modelo, não de crença única, e com `L` não-padrão a referência externa
  (`∃d Ref` "de verdade") nem sequer tipifica (`d`, `L` ∉ `ℕ`) — a única noção disponível é a da
  lacuna `A.7`; (c) **internamente** não há distinção espúria/genuína (a soundness interna com
  parâmetros é garantida por `U ∈ T_PV`). **Correção:** ou definir "não-espúria" operacionalmente
  (declarando o que é "verdadeiro" para parâmetros não-padrão), ou apagar o qualifier e
  declarar a lacuna `A.7`; converter a "Proposição" em Definição/Pergunta.

## Item 4 — §7 (log v2→v3) — **PARCIAL: fiel em 4/5, infiel em R2**

- **FATAL-R1 → A.7 + ajustes: fiel ✓** ao pedido da v2 (declarar a lacuna das fórmulas
  não-padrões).
- **R2: INFIEL/FALSO (MAJOR).** O log afirma "`indução Δ^b_0 provável em `T_PV`` estava errada —
  soundness interna **NÃO** é provável em `T_PV` (espúries: A.5)". A revisão da v2 disse o
  **contrário**: o resultado de soundness interna é correto e a rota corrigida é a sentença
  universal verdadeira (`U`) — o que eu prescrevi; a v3 inverteu a orientação com base em A.5,
  que é falso (item 1). Reescrever o log e o §5 item correspondente.
- **R3: fiel ✓** (argumento direto de B.3(ii) substituiu o fato duvidoso "IΣ₁+exp sem
  Σ₁-choice"; escopo KPT marcado — resquício MENOR acima).
- **R4: fiel ✓** (§6 agora diz "restrição de classe nova sobre os `M` do Teorema 4" — o erro
  "modelos do Problema 2.1" foi removido).
- **R5: fiel ✓** (completude é clássica; aberto é só tamanho ⇔ `NP` vs `coNP`).
- **Má-atribuição (MAJOR):** a nota final da §7 diz que "**o referee v1** classificava a
  recíproca de `A.2` como 'aberta tipo P vs NP'". **Errado:** quem escreveu isso foi a **v2 do
  autor** (`Cor. A.4`); o referee v1 registrou que, *para condições padrão*, a completude é
  fato padrão disponível. Corrigir a atribuição (a autocrítica é boa, a autoria está trocada).
- **MENOR não tratados (§7 não os promete, mas registre-se):** `A.1` continua "Indução trivial
  sobre `k`" sem `σ_k ∈ T_PV`; o parêntese de `B.4` "recursamente saturados (não coincidem com
  ultrapoderes de `ℕ`)" está **inalterado** e é falso (ultrapoderes de `ℕ` são ℵ₁-saturados).

## Veredito final: **REVISION**

**Por que não REJECT:** `A.3` está correto; `A.6` é verdadeiro (de fato mais forte do que
enunciado); `B.1`/`B.2` permanecem intactos e corretos; `B.3(i)–(iv)` e a nova `(ii)` estão
corretos com prova que fecha; `C.1` ficou limpo (parâmetros, `𝒯_n`, Łoś); `A.7` declara
honestamente o limite `FATAL-R1`; `R4`/`R5` foram reparados de verdade.

**Por que não RECOMENDADO:**
1. **FATAL:** `A.5` é **falso** (`Con(EF) ∈ T_PV` ⇒ `T_PV + ¬Con(EF)` inconsistente; Gödel II
   não se aplica a `T_PV` não-r.e.) e é o alicerce de §0.1, §4.1(i), §5 item 7, §6, `C.3(a)` e
   do log `R2` — junto com ele cai a alegação de que a Σ₁-soundness é **necessária** (o `⟹` vale
   em todo `M ⊨ T_PV` para `T_f` padrão).
2. **MAIOR:** `C.3` "não-espúria" indefinido (e premissa falsa); §7 `R2` inverte o apontamento
   da v2; má-atribuição do "referee v1" na nota final; `A.4` superhipotetizado (hipótese
   suficiente mas desnecessária).
3. **MENOR:** `A.1` sem `σ_k ∈ T_PV`; parêntese falso de `B.4`; `(ii)` com quantificadores a
   formalizar e `m ≤ |α|` a citar; "Δ^b_0-completude" → absolutidade p-tempo; KPT "confirma" →
   "sob (ST)".

**Correções obrigatórias (mínimo para RECOMENDADO):** (1) apagar `A.5` e reescrever
§0.1/§4.1(i)/§5.7/§6 com o teorema real (⟹ vale em todo `M ⊨ T_PV` para `T_f` padrão, via
`U ∈ T_PV` + absolutidade em dado padrão); `A.4` vira observação "hipótese suficiente, não
necessária"; (2) `C.3`: remover a premissa (a) e definir (ou declarar indefinido) "não-espúria";
(3) §7: reescrever `R2` fielmente e corrigir a atribuição ao referee v1; (4) menores: `σ_k ∈
T_PV`, parêntese de `B.4`, quantificadores de `(ii)`.

---
---

# Revisão da v4

**Alvo:** `I1_Qcompactness_ultrapoderes.md`, **v4 (pós-referee, 3 rodadas)** — os 5 pontos
solicitados. Fonte verbatim conferida antes do veredito: `A_teoremas_exatos.md` §1.0 ("the
**true universal** `L_PV`-theory `T_PV`"; tradução do corpus: "todo sentença universal
verdadeira de `L_PV` está em `T_PV`") e §3(a) (`Ref_P ∈ T_PV` *por ser verdadeira e universal*).

## (a) Nota A.5 — **forma honesta, substância indevida (MAIOR-R6)**

- **Forma ✓:** nenhum contraexemplo é afirmado; a nota é rotulada **(C)**, explicita as duas
  rotas, e §6 a registra como lacuna — o pedido da v3 (apagar A.5 e parar de afirmar) foi
  cumprido na forma.
- **Porém a questão não é aberta — é decidível afirmativamente, e a §7 caracteriza mal o
  referee v3, em dois erros:**
  1. **Na convenção do artigo (§1.0, verbatim acima): `Con(EF) ∈ T_PV` trivialmente.**
     `Con(EF) = ∀d ¬Ref_EF(d,∅)` é sentença **universal** (`Ref_EF` p-tempo ⇒ matriz
     quantifier-free via símbolos de função PV) e **verdadeira em `ℕ`** (soundness real de
     EF: nenhum `d` real deriva `⊥` sem premissas) — logo é **axioma** de `T_PV` pela própria
     definição (mesmíssimo argumento, já verbatim, pelo qual `Ref_P ∈ T_PV` em §3(a)). Não há
     "verificar no artigo/literatura" (item 7′): é uma linha.
  2. **"`T_PV` é r.e." (§7, coluna v3→v4) contradiz §1.0:** a teoria universal **verdadeira**
     não é r.e. (sua parte Π₁ é o conjunto de verdades Π₁, co-r.e.-completo). E a
     caracterização "referee alegou não-provabilidade (tipo Gödel)" **inverte** o argumento do
     referee v3: ele foi de **provabilidade trivial** (acima) e afirmou explicitamente que
     Gödel II **não se aplica** (não-r.e.; e `Con(EF)` ≠ `Con(T)`).
  3. **Mesmo na leitura "crua" PV (a que a Nota quer proteger): `PV ⊢ Con(EF)` também.**
     `IΔ_0+exp` (logo `PV`) prova soundness de EF por indução Δ^b_0 sobre os passos da
     derivação (os axiomas de EF são **instâncias proposicionais** — sem axiomas de indução
     aritmética no sistema; é exatamente essa ausência que faz o obstáculo gödeliano não
     aplicar, ao contrário de `Con(PA)`) — Δ^b_0-completude de `Ref_EF` dá o resto.
- **Consequência:** (h1) vale em **todo** `M ⊨ T_PV`; o `Cor. A.6` é **universal** para `T_f`
  padrão; "espúrias por construção" (`C.3`) perde a última ancora. A Nota vira observação
  "suficiência de (h1)/(h2); na convenção do artigo (h1) é satisfeita por todo `M`".

## (b) A.4 (h1)/(h2) — **CORRETO**

- **(h1):** "se `d` refuta `T_f` (premissas ⊆ `T_f`), então `d'` (p-tempo, teorema da
  dedução para EF) deriva `¬⋀T_f`; `Ref_EF` dá `M ⊨ ∀v (v ⊨ ⋀T_f → ⊥)`; atribuição real `v*`
  é padrão ∈ `M` e a avaliação é absoluta — contradição" ✓. **MENOR:** a passagem `d ↦ d'`
  (descarregar premissas) está **implícita** — escrever uma linha; e "Δ^b_0-completude" →
  "absolutidade de função p-tempo em dado padrão".
- **(h2):** inalterado e correto ✓ (suficiência; exemplos Łoś/`Th(ℕ)` ✓). Enunciados
  **bem hipotetizados**: ambos os caminhos declarados, nenhum depende da (falsa) premissa de
  A.5 — só a leitura "hipótese (h1) possivelmente dispensável" é que dependia dela.

## (c) C.3 "testemunha padrão" — **PARCIAL (MAIOR-R7)**

- A noção substituta é a direção certa e evita a vagueza de "não-espúria" ✓.
- **Mas a justificativa escrita é falsa:** *"avaliação real de `d*` contra `L` é um cálculo
  finito real"* — **não**: `L` tem código **não-padrão** (externamente infinito); ler `L`
  não é cálculo real-finito. O que é real-finito: (i) a validade de `d*` (axiomas/regras) e
  (ii) a insatisfatibilidade **real** das premissas `p_1..p_k` citadas (soundness de EF).
  A pertinência `p_i ∈ L` é computação **interna** em `M_0` (`∃j < ℓ(L) (L)_j = c`), não
  externa — e sem `L` externo não há "avaliação real" a divergir.
- **Reparo (uma linha):** "testemunha padrão = existe `d*` **real** tal que `d*` é derivação
  EF **real** de `⊥` citando premissas `p_1..p_k` **com `M_0 ⊨ p_i ∈ L`**" — aí a noção é
  bem definida mesmo para `L` não-padrão (mistura objeto externo finito + pertinência
  interna) e captura "contém sublista realmente insatisfatível reconhecida por `M_0`".
  Resíduo MENOR: "espúrias por construção" é prosa sem ancora (sem A.5).

## (d) B.4 — **CORRIGIDO ✓**

- "Alguns [ultrapoderes de `ℕ`] **são** r.s. (fato clássico)" ✓ — na verdade **todo**
  `ℕ^ω/U` com `U` não-principal é ℵ₁-saturado (contável-incompleto) ⇒ r.s. em linguagem
  contável; "alguns" é fraco mas verdadeiro; a consequência ("desses, `B.2` impede modelar
  `S`") ✓; não-ultrapoder r.s. de `S` rotulado **(C)** ✓ honesto.
- KPT `(iv)` "compatível" ✓; `A.1` "proVável em `T_PV`" ✓ (verdadeiro: `σ_k` é universal-
  verdadeira ⇒ axioma; manter "indução sobre `k"` só como justificativa externa, não interna);
  §5 itens 7′/8/10 coerentes ✓.

## (e) §7 — **PARCIAL: linhas v1→v2 e v2→v3 fiéis ✓; linha v3→v4 INFIEL (MAIOR-R6)**

- A linha v3→v4 inverte o apontamento do referee v3 (ver (a): argumento de provabilidade
  trivial, não "tipo Gödel") e afirma "`T_PV` é r.e." contra o §1.0 que o próprio arquivo
  cita. É o **terceiro** rodada-seguida com o log caracterizando mal o referee (R2 na v3,
  atribuição ao "referee v1" na v3, agora A.5). Padrão a quebrar: quando a divergência for
  real, citar a frase exata do relatório anterior (`I1_referee.md` é o arquivo-fonte).

## Veredito final: **REVISION**

**Progresso real (por que não REJECT):** nenhum contraexemplo indevido permanece; as rotas
(h1)/(h2) estão bem hipotetizadas e corretas; `B.4`/KPT/`A.1` reparados de verdade; `C.3` ganhou
noção substituta na direção certa; `B.1`/`B.2`/`B.3`/`C.1` seguem intactos e corretos.

**O que impede RECOMENDADO:**
1. **MAIOR-R6:** `Nota A.5` trata como **aberta** uma questão decidível afirmativamente na
   própria convenção do artigo (`Con(EF)` universal-verdadeira ⇒ axioma de `T_PV`; §1.0), e a
   `§7` **inverte** o argumento do referee v3 + afirma "`T_PV` é r.e." contra §1.0.
2. **MAIOR-R7:** `C.3` — a justificativa da "testemunha padrão" ("avaliação real de `d*` contra
   `L` é cálculo finito real") é falsa para `L` não-padrão; reparo de uma linha disponível.
3. **MENOR:** passo `d ↦ d'` em (h1); "Δ^b_0-completude" → absolutidade p-tempo; "espúrias por
   construção" sem ancora.

**Correções mínimas (→ RECOMENDADO):** (1) `Nota A.5`: substituir "não é decidido aqui" por
"`Con(EF) ∈ T_PV` na convenção do artigo (universal-verdadeira; §1.0/§3(a)); além disso
`PV ⊢ Con(EF)` por Δ^b_0-indução sobre derivações EF (axiomas proposicionais) — logo (h1) vale
em todo `M ⊨ T_PV` e `A.6` é universal para `T_f` padrão; apagar item 7′"; (2) `§7` linha
v3→v4 corrigida (sem "`T_PV` é r.e."; sem "tipo Gödel" atribuído ao referee v3); (3) `C.3` com
o reparo "`d*` real + `M_0 ⊨ p_i ∈ L`"; (4) menores listados.

---
---

# Confirmação da v5

As 3 correções mínimas exigidas na v4 foram aplicadas corretamente, sem erro novo.
**(1) Nota A.5 → resolução ✓:** `Ref_EF ∈ T_PV` pela definição do artigo (verbatim §1.0
L19/L25/L341 — "the true universal `L_PV`-theory `T_PV`"; o mesmo truque que o artigo usa
para `Ref_P`, L341–344) e a rota alternativa `PV ⊢ Con(EF)` por indução Δ^b_0 sobre passos
de derivações EF; consequência aplicada: `A.4`/`A.6` estão corretamente **universais** (todo
`M ⊨ T_PV`), a nota de rotas alternativas (Σ₁-sound) ficou bem escopada em "teorias-base que
não contenham `Ref_EF`", e o item 7′ foi marcado resolvido no §5.
**(2) C.3 ✓:** aplica o reparo pedido ao pé da letra — testemunha padrão = `d*` **real** +
`M_0 ⊨` "toda premissa de `d*` pertence a `L`" (pertinência como computação **interna**),
com disavowal explícito de legibilidade externa de fórmulas não-padrões e sem "espúrias por
construção". **(3) §7 ✓:** a linha v3→v4 agora cita o argumento real do referee (verbatim
"true universal" + Δ^b_0 em `PV`) e reconhece a substância; a linha v4→v5 mapeia fielmente o
relatório da v4 (inclusive o reparo de `C.3`). **Resíduos NÃO-bloqueantes (registro):** o
parágrafo final de autoria ainda diz "referee v2 e v3 estavam errados na substância" — impreciso:
o relatório v2 (`I1_referee.md` §B(a)) adotou exatamente a rota vencedora (sentença universal-
verdadeira ⇒ soundness interna) e **concorda** com v3, e "citou `T_PV` 'não r.e.', erro" rotula
como erro uma observação verdadeira sob §1.0 (a teoria universal verdadeira não é r.e.);
§4.1(i)/`C.2`(ii) mantêm o ponteiro desatualizado "com hipótese explícita `Ref_EF`/Σ₁-sound";
o (β) de `A.5` diz "sem indução aritmética" onde quer dizer "sem axiomas de indução *no sistema
EF verificado*". Nenhuma dessas peças afeta teorema algum.

## Veredito final: **RECOMENDADO**

Os blocos (A), (B) e (C) estão com enunciados corretos, hipóteses verdadeiras e explícitas,
limite de escopo (`A.7`) honesto, lacunas rotuladas **(C)** onde são genuínas e log de rodadas
substancialmente fiel — os FATAL/MAIOR das rodadas v1–v4 estão resolvidos. Recomendação:
arquivar como versão final da Frente I; os próximos passos (`Q-compactness-over-M_0`, item 2
local-BB vs Cook–Thapen, Lean) são bem direcionados.

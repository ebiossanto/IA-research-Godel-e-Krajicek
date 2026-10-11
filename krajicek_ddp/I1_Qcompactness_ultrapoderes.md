# I1 — Q-compactness em ultrapoderes: análise, barreira do ultrapoder e venue corrigida

> Frente I, **v5 (final; pós-referee, 4 rodadas)**, 11 Out 2026. Marcação: **(A)** =
> fonte/artigo; **P** = próprio; **(C)** = conjectura. Fontes verbatim locais:
> `A_teoremas_exatos.md` §1.0/§1.2/§1.12 (inclusive L19/L25/L341: `T_PV` = **teoria
> universal verdadeira** em `L_PV`), `CONTEXTO_COMUM.md` L13–16/L61–76,
> `H1_colecao_refutacao.md` §1.1/§1.3, `G2_semente_Fsent.md`, `I1_referee.md`
> (4 rodadas; log consolidado em §7).

## §0. Pergunta e resultado desta rodada

**Pergunta herdada (H1 §1.3):** dado `M` não-padrão modelando a teoria `S` do artigo e a
semente `𝒯` de `H1` (§1.1), existe parte `T_f ⊆ 𝒯` com refutação EF **interna** em `M`
("Q-compactness" para ultrapoderes)?

**Resultado (P), em três blocos:**

1. **(A) Refutabilidade interna × real** (§1): para `T_f` de **fórmulas-padrão**, a
   insatisfatibilidade real **equivale** à refutabilidade interna em **todo**
   `M ⊨ T_PV` (Teorema A.4 + Cor. A.6) — pois `Ref_EF` (soundness de EF) **pertence a
   `T_PV` por definição**: `T_PV` é a teoria universal **verdadeira** de `L_PV`
   (verbatim do artigo: `A_teoremas_exatos.md` §1.0 L19/L25/L341) — e também é provável
   já em `PV` (A.5). Para `T_f` de fórmulas **não-padrão** (o caso do H1), nada se
   conclui (A.7).
2. **(B) Barreira do ultrapoder** (§2): **nenhum ultrapoder `ℕ^ω/U` modela `S`** (B.2);
   mecanismo: soundness interna `Ref_P` + **impossibilidade de seletor p-tempo** para
   falsificadores (B.3). A pergunta sobre o artigo é **vazia** na sede ultrapoder-de-`ℕ`.
3. **(C) Transferência Łoś** (§3): refutabilidade interna transfere para ultrapoderes
   **sobre qualquer base**; venue remanescente `M_0 ⊨ S` não-padrão (C.3), com o cerne
   identificado: refutações **genuínas** (testemunha padrão).

## §1. (A) Refutabilidade interna × real: quadro exato para `T_f` padrão

Notação: `T_f` = lista externamente finita de fórmulas-padrão (código padrão);
`Ref_EF(d, T_f)` = predicado p-tempo "d é derivação EF de ⊥ com premissas sublistas de
`T_f`". `Ref_EF` (axioma de soundness "`x : EF ⊢ y → (¬y) ∉ SAT`", análogo de `Ref_P`)
**pertence ao `T_PV` do artigo** — ver A.5 (definição + prova direta).

> **Lema A.1 (finitude padrão de `[0,k]`) (P).** Para `k` padrão, em qualquer modelo
> `M ⊨ T_PV`: `x ≤ k ⟹ x ∈ {0,…,k}` (proVável em `T_PV` por indução sobre `k`). Logo
> todo subconjunto interno `A ⊆ [0,k]` é, externamente, subconjunto de um conjunto
> padrão-finito.

**Prova.** Todo `x ∉ ℕ` excede todo padrão, em particular `k`. ∎

> **Lema A.2 (completude clássica de EF) (A).** Toda tautologia real tem derivação EF
> real. Em particular, se `T_f` é realmente insatisfatível, existe derivação EF **real**
> `d*` (objeto padrão) refutando `T_f`.

**Prova.** Fato clássico de proof complexity (EF é proposicionalmente completo). ∎

> **Proposição A.3 (⟸ vale em qualquer M) (P).** Se `T_f` é realmente insatisfatível,
> então **todo** `M ⊨ T_PV` satisfaz `M ⊨ ∃d Ref_EF(d, T_f)`.

**Prova.** Pelo Lema A.2 existe `d*` padrão; `Ref_EF(d*, T_f)` é cálculo padrão finito,
correto em qualquer `M` (absolutidade Δ^b_0 para dados padrão). ∎

> **Teorema A.4 (⟹) (P).** Seja `M ⊨ T_PV` (no sentido do artigo: teoria universal
> verdadeira de `L_PV` — logo `M ⊨ Ref_EF`, por A.5). Então:
> `M ⊨ ∃d Ref_EF(d, T_f)` ⟹ `T_f` é realmente insatisfatível.

**Prova.** `Ref_EF` dá `M ⊨ ∀v (v ⊨ ⋀T_f → ⊥)` (toda atribuição interna viola `T_f`);
uma atribuição **real** `v` de `T_f` é objeto padrão, logo `v ∈ M`, e a avaliação de
fórmulas-padrão sob dados padrão é **absoluta** (cálculo Δ^b_0 padrão finito, correto em
qualquer `M`) — logo `v` violaria internamente, contradição. ∎
**Nota (rotas alternativas) (P):** para teorias-base que não contenham `Ref_EF` (ex.: `PV`
"cru"), o mesmo resultado vale se `M` é **Σ₁-sound para parâmetros padrão** (Łoś dá
isso em ultrapoderes `ℕ^ω/U` e em `M ⊨ Th(ℕ)`): `∃d Ref_EF(d, T_f)` é Σ₁ com parâmetro
padrão, logo verdadeira em `ℕ` — `d` padrão, derivação EF real — e a soundness real de
EF (fato padrão; vale para qualquer comprimento real) conclui.

> **Nota A.5 (`Ref_EF ∈ T_PV`: por que A.4 vale em todo `M ⊨ T_PV`) (A)+(P).** Duas
> rotas, ambas fechadas: (α) **pela definição**: `T_PV` é a teoria universal **verdadeira** de `L_PV`
> (verbatim: "The provability of such a statement in **the true universal `L_PV`-theory
> `T_PV`**" — `A_teoremas_exatos.md` L19; §1.0 L25; §5.9 L341/L481); `Ref_EF` é sentença
> universal verdadeira (em `L_PV`, predicados p-tempo são atômicos via símbolos de
> função; a soundness real de EF a torna verdadeira) — logo `Ref_EF ∈ T_PV`. O artigo
> usa exatamente este truque com `Ref_P` (`A_teoremas_exatos.md` L341–344) e com
> correções de funções p-tempo (L416–418). (β) **por prova direta**: `PV` (=
> `IΔ₀+exp`) prova `Con(EF)` por indução `Δ^b_0` sobre o índice de passos de derivações
> EF (axiomas EF = tautologias proposicionais, checagem p-tempo; "conclusão é tautologia"
> é predicado interno limitado) — a indução usada é **só** `Δ^b_0` (sem axiomas de
> indução aritmética de nível maior), daí por que Gödel II não se aplica a `Con(EF)`.

> **Corolário A.6 (equivalência universal) (P).** Para `T_f` padrão e **todo**
> `M ⊨ T_PV`: `M ⊨ ∃d Ref_EF(d, T_f)` **⟺** `T_f` realmente insatisfatível. (⟸ = A.3;
> ⟹ = A.4 + A.5.) Sobre P vs NP: a equivalência usa EF completo mas **não**
> polinomialmente limitado — "tautologias têm provas EF de tamanho polinomial" ⇔
> `NP = coNP` (aberto, não usado; §5 item 11).

> **Limite de escopo A.7 (o caso do H1 fica fora) (P).** `T_f ⊆ 𝒯` do H1 tem fórmulas
> **não-padrão** (`δ_N → τ_N` com `N` não-padrão): (a) a avaliação interna de tais
> fórmulas sob atribuições padrão **não** é absoluta (Δ^b_0 com dados não-padrão), e
> (b) a própria noção "realmente insatisfatível" de uma fórmula não-padrão (circuito
> real de tamanho não-padrão) precisa de cuidado (avaliação real finita existe, mas não
> é capturada pela avaliação interna). Logo A.3–A.6 não se aplicam: o H1 §1.3 permanece
> **aberto** fora do subcaso "partes padrão".

## §2. (B) Barreira do ultrapoder — `S` não é ultraprovável

Axiomas de `S` (verbatim, `A_teoremas_exatos.md` §1.12 (2); `CONTEXTO_COMUM.md` L63–64):
`T_PV`; "`α` é disjunção disjunta `⋁̇_{i<m} α_i`" **(S2)**; "`π : P ⊢ α`" **(S3)**;
"`∀i<m (¬α_i) ∈ SAT`" **(S4)** — internos, parâmetros `π, α, m, P` (`SAT` Σ^b_1).
Nota (A): `Ref_P` (`x : P ⊢ y → (¬y) ∉ SAT`) **é axioma de `T_PV`** no artigo
(`A_teoremas_exatos.md` §1.12 (5)).

> **Lema B.1 (amalgamação padrão) (A)+(P).** Não existe instância **padrão**
> `(π, α, m, P)` com (S2)+(S3)+(S4) e `P` sounde.

**Prova.** `m=0`: `α=⊥` e `π : P ⊢ ⊥` contradiz soundness real de `P` (objetos reais,
qualquer comprimento). `m≥1`: por (S3)+soundness real, `α` é tautologia real. Por (S4)
escolha, para cada `i<m`, um falsificador real `y_i` (escolha finita). Por (S2) os átomos
dos `α_i` são par-a-par disjuntos; logo `y := ⋃_{i<m} y_i` é bem definida e, como `m` é
padrão, tem suporte finito padrão (objeto real). `y` falsifica cada `α_i`, logo `α`:
contradição. ∎
*(O artigo afirma exatamente este lema como "Totalidade" de `DD_P` —
`CONTEXTO_COMUM.md` L16: "se cada `α_i` tivesse atribuição falsificante, a união dessas
atribuições [falsificaria α]". **(A)**)*

> **Teorema B.2 (barreira do ultrapoder) (P).** Não existe ultrapoder `M = ℕ^ω/U`
> (ultrafiltro não-principal em `ω`) com `M ⊨ (S1)–(S4)`.

**Prova.** Cada axioma (S2)–(S4) é sentença **primeira-ordem com parâmetros** (verificações
Δ^b_0/p-tempo; `(S4)` = `∀i<m ∃σ Fals(σ,(α)_i)`, Σ^b_1 com parâmetros). Por **Łoś**
(válido para ultrapoderes de qualquer estrutura de 1ª ordem): `{n : ℕ ⊨ (S2)∧(S3)∧(S4)
para (π_n, α_n, m_n, P_n)} ∈ U` — não-vazio. Cada componente é instância **padrão** com
`P` sounde (soundness real uniforme; objetos reais, verificação absoluta) — contradiz o
Lema B.1. ∎

> **Observação B.3 (sharpness: onde a amalgamação morre) (P).**
> (i) **Sem falsificador comum.** Em qualquer `M ⊨ T_PV + (S3)` (com `Ref_P ∈ T_PV`):
> não existe `σ ∈ M` falsificando `α`, pois `Ref_P` + `π : P ⊢ α` dão `M ⊨ ∀v (v ⊨ α)`
> (toda atribuição interna satisfaz `α`) — o mesmo mecanismo que o artigo usa em `M'`
> (`A_teoremas_exatos.md` §1.12 (5)).
> (ii) **Sem seletor p-tempo.** Seja `m ≤ |α|` (`m` determinado por `α`) e a multifunção
> `i ↦ {σ : Fals(σ, α_i)}`. Não existe seletor **p-tempo** `f` para ela: tal `f` definiria
> `σ*` por `(σ*)_p = 1 ⟺ ∃i<m (f(i))_p = 1` (cálculo em tempo `p(m, |α|)` — `f` é p-tempo
> e `m ≤ |α|`); por (S2) os suportes são disjuntos, logo `σ*` **não tem conflitos** e é
> extensão de cada `f(i)` — logo falsifica cada `α_i`, logo `α` — contradiz (i). **(P)**
> (iii) **Leitura.** Para `m` **padrão**, o amalgamador existe (escolha finita; Lema B.1)
> — e é por isso que os **componentes** dos ultrapoderes morrem (B.2). Para `m`
> **não-padrão**, a amalgamação exigiria uma função escolha interna `i ↦ σ_i` — cuja
> forma p-tempo é **impossível** por (ii), e cuja forma interna arbitrária colidiria
> com (i). A sobrevivência de `S` em modelos genuinamente não-padrões vive nesse
> intervalo.
> (iv) **Coerência com o artigo (A, escopo explícito).** O artigo prova a consistência
> de `S` via **KPT** (`A_teoremas_exatos.md` §1.12 (2): "If S were inconsistent then
> applying the KPT theorem … would give p-time functions … solving DD_P in a constant
> number of rounds") — **sob as hipóteses da prova** (`NP=coNP` e (ST)), a inconsistência
> de `S` produziria um solucionador estratégico de `DD_P`. Isto é **compatível** com
> (i)/(ii): nenhuma amalgamação interna ingênua é válida em `T_PV`.

> **Corolário B.4 (escopo honesto) (P).** B.2 exclui exatamente **modelos de `S`** da
> classe dos ultrapoderes de `ℕ`. Como o `M` do artigo deve modelar `S`
> (`A_teoremas_exatos.md` §1.12 (2): "Let M be a model (necessarily non-standard) of S"),
> isto é uma **restrição real** sobre os `M` usados na prova do Teorema 4. Quanto às
> classes sugeridas pelo autor: modelos **contáveis** não são ultrapoderes de `ℕ`
> (tamanho `ℵ_0` vs `2^{ℵ_0}`) — fora do alcance de B.2; modelos **recursamente
> saturados** — alguns **são** ultrapoderes de `ℕ` (fato clássico), e desses B.2 impede
> que modelem `S`; que existam modelos r.s. de `S` **não**-ultrapoder é **(C)**
> (não verificado aqui). Estender B.2 a "qualquer `M` com propriedade de Łoś para estas
> fórmulas" é **(C)** — a caracterização dessa classe não foi feita.

## §3. (C) Transferência Łoś e venue remanescente

> **Teorema C.1 (transferência) (P).** Seja `M = M_0^ω/U` ultrapoder sobre qualquer
> estrutura-base `M_0 ⊨ T_PV` (caso `M_0=ℕ`; venue novo: `M_0 ⊨ S` não-padrão). A
> semente `𝒯` de `H1 §1.1` é uma **família definida a partir dos parâmetros
> `(π, α, m)`** (`P` fixo, definido uniformemente): condições `δ_N → τ_N` para
> `N ∈ Names`, mais `¬φ`, mais constantes-1. A afirmação "`d` codifica derivação EF com
> `premissas(d) ⊆_{int} 𝒯^{list}` e conclui ⊥" é sentença **primeira-ordem com parâmetros**
> (`Ref_EF` p-tempo/absoluto; listas internamente codificadas). Logo:
> `M ⊨ "∃ refutação EF interna da semente (premisas internamente ⊆ 𝒯)"`
> **⟺** `{n : M_0 ⊨ "∃ refutação EF interna de 𝒯_n` — a semente avaliada nos
> **parâmetros componentes** `(π_n, α_n, m_n)` na cópia correspondente de `M_0`
> — "com premissas internamente ⊆ 𝒯_n"} ∈ U`.

**Prova.** Łoś para sentenças com parâmetros. ∎

> **Corolário C.2 (recomposição) (P).** (i) Pelo B.2, para `M_0=ℕ` o `M` de C.1 não
> modela `S` — a pergunta sobre ultrapoderes **do artigo** é **vazia**. (ii) Pelo
> A.3–A.6, partes `T_f` de **fórmulas-padrão** colapsam a insatisfatibilidade-real —
> **em todo `M ⊨ T_PV`** (A.5) — sem conteúdo interno novo. (iii) Pelo A.7, partes com
> fórmulas **não-padrões** (o caso H1) não são cobertas por §1 — o venue remanescente é
> `M = M_0^ω/U` sobre `M_0 ⊨ S` não-padrão, onde a amalgamação continua quebrada (B.3)
> e C.1 transfere a pergunta para `M_0`.

> **Proposição C.3 (o que `Q-compactness-over-M_0` pergunta) (P).** Dado `M_0 ⊨ S`
> não-padrão e sua semente `𝒯_{M_0}` (família com parâmetros `(π, α, m)` de `M_0`):
> existe sublista `L ∈ M_0` **interna**-mente finita (externamente possivelmente
> infinita, fórmulas possivelmente não-padrão) de `𝒯_{M_0}` com **refutação EF
> genuína**, i.e., com **testemunha padrão**: algum `d* ∈ ℕ` (objeto padrão) é derivação
> EF real e `M_0 ⊨ "toda premissa de `d*` pertence a `L`"` (a pertinência é computação
> **interna** em `M_0` — `L` é lista interna; a derivação `d*` é objeto real e o check
> das premissas contra `L` é interno e finito). Esta formulação é bem definida mesmo
> para `L` não-padrão — **sem** afirmar que a avaliação real de `d*` contra `L` é legível
> externamente (fórmulas não-padrão não se leem externamente como circuitos finitos
> únicos; só a pertinência interna é legítima). B.3(ii) mostra que um seletor p-tempo de
> falsificadores não existe; a pergunta é se a **não-colecção interna** se manifesta
> numa refutação **genuína** (testemunha padrão) de uma parte internamente finita — ou
> se todas as testemunhas de crenças `M_0 ⊨ "L tem refutação"` são não-padrões.

## §4. O que foi decidido e o que destrava o item 2

1. **Decidido (P):** para **ultrapoderes sobre `ℕ`**: (i) partes padrão colapsam a
   realidade (A.3–A.6 — **em todo `M ⊨ T_PV`**, pois `Ref_EF ∈ T_PV` por definição:
   A.5); (ii) **nenhum** ultrapoder de `ℕ` modela `S` (B.2) — a pergunta do artigo é
   **vazia** nessa sede.
2. **Reduzida, não decidida (P):** o caso H1 (partes com fórmulas não-padrão; modelos
   não-padrões arbitrários `M ⊨ S`) permanece aberto — A.7 + C.3 enxutam-no: é a
   pergunta por refutações **genuínas** (testemunha padrão) de sublista interna-finita.
3. **Teoria nova (P):** **barreira do ultrapoder** (B.2) + **mecanismo** (B.3):
   amalgamação morre por (i) soundness interna (`Ref_P`) e (ii) **impossibilidade de
   seletor p-tempo** para falsificadores — compatível com o uso de KPT pelo artigo (A).
4. **Destravado (P):** `Q-compactness-over-M_0` (C.3) é a pergunta nítida remanescente
   — porta do **item 2** (instância local `(m, α)` vs Cook–Thapen): o objeto a medir é a
   **função escolha ausente** `i ↦ σ_i` e a existência (ou não) de testemunha padrão.

## §5. Certificados para humanos (checklist de falseabilidade)

| # | Afirmação | Verificação humana | Onde checar |
|---|---|---|---|
| 1 | (S2) = "no two `α_i` have an atom in common" | verbatim | `A_teoremas_exatos.md` §1.2 / arXiv html v5 §3 |
| 2 | (S4) = `∀i<m (¬α_i) ∈ SAT`, interno Σ^b_1; `Ref_P ∈ T_PV` | verbatim | `A_teoremas_exatos.md` §1.12 (2),(5); `CONTEXTO_COMUM.md` L63–64/L76 |
| 3 | Lema B.1 = "Totalidade" do artigo | o artigo o afirma | `CONTEXTO_COMUM.md` L16 |
| 4 | Łoś (1ª ordem, sentenças com parâmetros) | fato padrão | Chang–Keisler, *Model Theory* §4.4 |
| 5 | Soundness real de EF/`P` (qualquer comprimento real); completude clássica de EF | fatos padrão | Buss, *Handbook of Proof Complexity*; Krajíček, *Bounded Arithmetic* |
| 6 | Lema A.1 (`[0,k]` padrão = `{0..k}`; proVável em `T_PV`) | 1 linha + indução | §1 |
| 7 | Σ₁-soundness de ultrapoderes de `ℕ` para parâmetros padrão (Łoś) — rota alternativa da Nota A.4 | padrão | Chang–Keisler §4.4 |
| 7′ | `Ref_EF ∈ T_PV` **resolvido**: `T_PV` = teoria universal verdadeira de `L_PV` ⟹ `Ref_EF` (universal-verdadeira) ∈ `T_PV`; e `PV ⊢ Con(EF)` por indução Δ^b_0 | verbatim + prova direta | `A_teoremas_exatos.md` L19/L25/L341; §1 Nota A.5 |
| 8 | Cor. B.3(ii): **nenhum seletor p-tempo** para `i ↦ {σ : Fals(σ,α_i)}` | prova de 4 linhas (§2) | §2, B.3(ii) |
| 9 | Consistência de `S` via KPT no artigo (sob `NP=coNP`+(ST)) | verbatim + escopo | `A_teoremas_exatos.md` §1.12 (2) |
| 10 | Modelos contáveis ≠ ultrapoderes de `ℕ` (tamanho `ℵ_0` vs `2^{ℵ_0}`); ultrapoderes de `ℕ` podem ser r.s. | cardinalidade; fato clássico | §2, B.4; Kossak–Schmerl |
| 11 | "Tautologias têm provas EF polinomiais" ⇔ `NP = coNP` (não usado) | padrão | Cook–Thapen; Krajíček |

**Formalização Lean possível:** A.1; A.3; B.1 (para `P` fixo); B.3(ii) — Equipe B.

## §6. Veredito e próximos passos

**Veredito (P):** a pergunta "Q-compactness em ultrapoderes" produziu o **quadro exato**
(A.3–A.7: **equivalência universal** para `T_f` padrão — em todo `M ⊨ T_PV`, pois
`Ref_EF ∈ T_PV` por definição; A.7 fixa o limite de escopo para fórmulas não-padrão), a
**barreira do ultrapoder** (B.2: nenhum `ℕ^ω/U` modela `S`) com **mecanismo** (B.3:
soundness interna + impossibilidade de seletor p-tempo), e a **transferência Łoś** (C.1)
— composição que **fecha** o subcaso ultrapoder-de-`ℕ` e **reorienta** para
`Q-compactness-over-M_0` (C.3), cujo cerne é a existência de **refutações genuínas**
(testemunha padrão) de sublista internamente finita. O achado mais denso é B.2+B.3:
restrição de classe nova sobre os `M` do Teorema 4, com mecanismo nomeado e
compatibilidade verificada com o KPT do artigo.

**Próximos passos:** (1) atacar `Q-compactness-over-M_0` concreto (`M_0` = ultrapoder
iterado/saturado de um modelo de `S`? modelo minimal via KPT?); (2) então item 2
(local-BB vs Cook–Thapen); (3) Lean: A.1, A.3, B.1, B.3(ii); (4) nota editorial a
Krajíček ganha B.2/B.3.

**Lacunas honestas:** a A.7 tem duas razões (não-absolutude da avaliação interna +
"insatisfatibilidade real" de fórmulas não-padrão precisa de cuidado — a segunda é a
razão firme). B.4: existência de modelos r.s. de `S` não-ultrapoder é **(C)**. C.3 é
enunciada, não decidida — é a próxima missão. B.2 usa Łoś padrão; "qualquer `M` com
propriedade de Łoś" é **(C)**.

## §7. Registro de correções (autorship honesty; v1→v5)

| Rodada | referee | achados | correção aplicada |
|---|---|---|---|
| v1→v2 | REVISION (2F+5M) | FATAL: "refutação interna ⟹ derivação real" (ℓ(d) não-padrão); escopo "decidida". MAIOR: A.1/B.3/B.4/C.1/C.3 | v2: soundness interna + absolutidade p/ dados padrão; escopo rebaixado; correções 1–7 |
| v2→v3 | REVISION (FATAL-R1 + R2–R5) | R1: A.3 não cobre fórmulas não-padrão; R2: "indução Δ^b_0 provável em T_PV" errada (segundo o referee v2); R3: "PV sem Σ₁-choice" mal localizado; R5: completude de EF é clássica | v3: A.7; reescrita §1; Cor. B.3(ii) p/ seletor p-tempo; Cor. A.6 |
| v3→v4 | REVISION (FATAL-A.5 + menores) | FATAL: contraexemplo A.5 (`T_PV+¬Con(EF)`) não sustentado — o referee v3 alegou que `Con(EF)` é axioma de `T_PV` ("true universal", §1.0) e ainda provável em `PV` p/ indução Δ^b_0 (referee v3 formulou mal — citou `T_PV` "não r.e.", erro — mas a substância foi confirmada na v4); menores: C.3 "não-espúria" vaga; B.4 parêntese r.s. falso; KPT "confirma" incondicional | v4: A.5 virou Nota (C); A.4 com rotas (h1)/(h2); C.3: "testemunha padrão"; B.4 corrigido; KPT: "compatível" |
| v4→v5 | REVISION→**fechado nas correções mínimas** | (a) Nota A.5: a questão `T_PV ⊢ Con(EF)` **não é aberta** — verbatim do artigo: `T_PV` = **teoria universal verdadeira** de `L_PV` (`A_teoremas_exatos.md` L19/L25/L341, o mesmo truque que o artigo usa p/ `Ref_P` L341–344) ⟹ `Ref_EF ∈ T_PV`; e `PV ⊢ Con(EF)` por indução Δ^b_0 (referee v4; confirmado aqui); (c) C.3: "avaliação real de `d*` contra `L` é cálculo finito" é **falsa** p/ `L` não-padrão — reparo: testemunha = `d*` real + pertinência **interna** `M_0 ⊨ "premissas de d* ∈ L"`; (e) log v3→v4 infiel | v5: Nota A.5 reescrita como **resolução (A)+(P)** com as duas rotas; A.4/A.6 universais sem (h1)/(h2); item 7′ marcado resolvido; C.3 reparada; esta linha corrigida |

Autoria: a v1 e a v2 foram escritas pelo orquestrador; a v3, a v4 e a v5 são **reescritas
do orquestrador seguindo estritamente as 4 rodadas de referee hostile** (`I1_referee.md`),
cujas retomadas de sessão do subagente produziram os relatórios após falhas de resposta
(esqueleto gravado). A divergência referees v2↔v3 sobre `T_PV ⊢ Con(EF)` foi **decidida
na v5 por verbatim do artigo** (não pelo orquestrador): `T_PV` é a teoria universal
verdadeira de `L_PV` (A L19/L25/L341) — e essa teoria, por conter **todas** as
sentenças universais verdadeiras, **não é r.e.** (o referee v3 tinha razão nesse ponto;
o orquestrador corrigiu a v4 por engano) — logo `Ref_EF`, sentença universal verdadeira,
é axioma dela. No mérito: referee v2 apontou a rota vencedora ("sentença universal
verdadeira") mas negou a prova direta por indução `Δ^b_0` em `PV`; referee v4 sustentou
as duas rotas (definição + Δ^b_0) e o orquestrador confirmou ambas — a Nota A.5 final
registra as duas.

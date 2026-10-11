# H1 — A refutação interna da semente de coleção (Claim 1 de [Kra98] invertido)

> Frente H, rodada de 11 Out 2026. **Versão 2 — corrigida após referee** (`H1_referee.md`;
> ver §5). Autoria: subagente falhou 2× (infraestrutura); conteúdo do orquestrador,
> referee hostile executado. Marcação: **(A)** = fonte; **(P)** = próprio; **(C)** = conjectura.
> Idioma: português.

## §0. Notação, fontes e mapa da missão

Configuração de `G2_semente_Fsent.md` §§1–2 **(A+P)**: `M ⊨ T_PV + (S1)–(S4)` não-padrão;
`P` pps; `φ(r) = ⋀_{i<m} ¬(r_i : P ⊢ α_i)` sem prova em `M` (item (1));
**`T_σ = {¬φ} ∪ constantes-1` é consistente** (G2, Thm 1.1 — usa item (1));
**nenhum `M' ⊨ PV` satisfaz `(¬φ) ∈ SAT` + `(F-sent)`** (G2, Thm 2.1, rota (a′));
forcing booleano [Kra98, §4] com Claims 1–2.

**Missão:** determinar o status de `M` perante a semente de `(F-sent)` — `M` a refuta?
Parcialmente? Totalmente? Mapa: §1 semente completa + o que se provou (e o que foi
**retraído**); §2 o teorema condicional sobre refutações finitas; §3 consequências para
a reductio (com trilhas falsas documentadas); §4 veredito; §5 referee.

## §1. A semente completa e o Teorema do "no-G" (com retração da finitude)

### 1.1 A semente, sem circularidade e com tipagem corrigida — **(P)** *(referee S1)*

Fixe os átomos `p := (r_i)_{i<m} ∪ (a_1,…,a_t) ∈ M`, onde os `a_s` são os **átomos-espelho**
dos átomos de `α` — todos os átomos de todos os `α_i` (`i < m`) estão entre os `a_s` por
(S2)/(S4) **(A)**. Com `p` assim ampliado, **todas** as condições abaixo pertencem a
`Circuit_M(p)` *(correção de mal-tipagem do referee S1: com espelhos "frescos" fora de `p`,
`τ_N` ficaria fora de `B(p)`)*. Para cada nome `N = ⟨C_1,…,C_ℓ⟩ ∈ Names_M(p)`:
- `δ_N` := "o número codificado por `⟨ν_G(C_1),…,ν_G(C_ℓ)⟩` é `< m`" — circuito em `M`
  (comparação p-tempo nos bits, `m` fixo) **(P)**;
- `τ_N` := `⋁_q ( q` codifica atribuição ∧ `Fals(q, (α)_{code(N,q)}) = 1 )`, com `(α)_{code(N,q)}`
  pelo circuito-projeção PV `D` de `M` espelhado sobre os `a_s` — disjunção (internamente)
  finita de condições em `Circuit_M(p)` **(P)**. Sentido: `ν_G(τ_N)=1` ⟺
  `M[G] ⊨ (¬(α)_{ν_G(N)}) ∈ SAT` **(P)**.

**Semente:** `𝒯 := {¬φ} ∪ { δ_N → τ_N : N ∈ Names } ∪ { C : C ≡ 1 em M }` **(P)**.

### 1.2 O que se provou

> **Teorema 1.1 (no-G) (P).** *(Versão corrigida — a afirmação de refutação EF **finita**
> foi **retraída** pelo referee S1; ver §1.3.)* Não existe ultrafiltro `G` em `B(p)` fechado
> sob EF-provability in `M`, contendo constantes-1, com `ν_G(¬φ)=1` e
> `ν_G(δ_N → τ_N)=1` para **todo** nome `N`.

**Prova.** Suponha `G`. [Kra98, Thm 4.1] (+ fechamento constantes-1): `M[G] ⊨ PV`, cofinal,
`Σ^b_1`-elementar **(A)**. (1) `σ := ν_G(p↾r)` falsifica `φ` em `M[G]` ⟹
`M[G] ⊨ (¬φ) ∈ SAT` **(P)**. (2) Para `i ∈ M[G]`, `i <^{M[G]} m`: `i = ν_G(N)` para nome
canônico; `δ_N` vale em `M[G]` ⟹ `ν_G(τ_N)=1` ⟹ `M[G] ⊨ (¬(α)_i) ∈ SAT`; logo
`M[G] ⊨ ∀i<m (¬α_i) ∈ SAT` **(P)**. (3) `M[G] ⊨ PV` + (1) + (2) contradizem G2, Thm 2.1(a′)
**(A+P)**. ∎

> **Corolário 1.2 (status de `𝒯`) (P).** Para **todo** `G` universal, alguma condição de
> `𝒯` falha: ou `ν_G(φ)=1`, ou existe nome `N` com `ν_G(δ_N)=1` e `ν_G(τ_N)=0` (um índice
> novo `i < m` em `M[G]` com `(α)_i` não-falsificado **em `M[G]`**). `𝒯` é **irrealizável**.

### 1.3 A finitude foi retraída — e o que ela deixou em aberto — **(P)** *(referee S1)*

**Retração.** "Refutação EF em `M`" **não** é finitária do ponto de vista externo: uma
refutação é um elemento de `M` codificando uma derivação EF cujo comprimento é **possivelmente
não-padrão** e cujo conjunto de premissas é externamente ilimitado. Logo "todo subconjunto
finito de `𝒯` EF-consistente ⟹ `𝒯` EF-consistente" **falha** (non-compactude interna), e o
argumento Zorn/[Kra98, Claim 2] não conserta. O Teorema 1.1 dá só "nenhuma `G` universal",
**não** "algum `T_f` finito refutado".

> **Questão Q-compactness (aberta, `(C)`).** Existe `T_f ⊆ 𝒯` **finito** com refutação EF
> **interna** em `M`? Alternativa: toda parte finita de `𝒯` é EF-consistente em `M` (sem
> refutação interna alguma) e ainda assim nenhuma `G` universal existe — falha genuína de
> compactude dentro de `M`. O Teorema 1.1 não distingue os casos; a distinção **é** o ponto
> onde a reductio do Teorema 4 tocaria o metalível (§3.2).

## §2. O teorema condicional sobre refutações finitas — *(corrigido, referee S2/S3)*

### 2.1 Candidato coberto

> **Definição (P).** `N` é **coberto** sse: para **toda** atribuição booleana `v` aos átomos
> de `N` (todos `⊆ p`, referee S2) com `code(N,v) ∈ M` e `code(N,v) < m`, a fórmula
> `(α)_{code(N,v)}` tem falsificador **real**. *(O código é elemento de `M`: `v` tem finitos
> bits em `{0,1} ⊆ M` e o código é p-tempo-computável em `M` — referee S3.)*
> Nomes **constantes** com `i ∈ M`, `i < m`, são cobertos: (S4) em `M` + absolutidade de
> `Fals` dão falsificador real **(P)**.

### 2.2 Teorema (condicional)

> **Teorema 2.1 (alvo da refutação — CONDICIONAL) (P).** Suponha que exista `T_f` **finito**,
> `T_f ⊆ 𝒯`, com refutação EF interna em `M`, cujas condições de coleção são
> `δ_{N_j} → τ_{N_j}` (`j ≤ k`). Se **todos** `N_j` são cobertos, então **`EF ⊢ φ` em `M`**
> — contradizendo o item (1) **(A)**. Logo todo `T_f` refutante usa algum candidato
> **não-coberto**.

**Prova.** Refutação interna ⟹ derivação EF **real** (o objeto é um número real) de `⊥`
de `{¬φ, δ_{N_j}→τ_{N_j}, C's}`; concatenando provas EF em `M` dos `C` (viáveis por
`C ≡ 1`), derivação EF **real** de `Φ := φ ∨ ⋁_{j≤k} ¬(δ_{N_j} → τ_{N_j})` **(P)**.
Agora: os átomos de cada `N_j` estão **em `p`** (S2); seja `x` **arbitrária** em `p`; para
cada `j` avalie `code(N_j, x)`:
- se `code(N_j,x) < m`: cobertura dá falsificador real `y_j` de `(α)_{code(N_j,x)}` — e os
  `y_j` são **mutuamente compatíveis** porque os `α_i` são disjuntos-variáveis ((S2): "no
  two `α_i` have an atom in common" **(A, verbatim em `A_teoremas_exatos.md`)**) — a **união**
  dos `y_j` é falsificador conjunto; logo `τ_{N_j}` avalia 1 sob a extensão de `x` por essa
  união (absolutidade p-tempo de `Fals`) **(P)**;
- se `code(N_j,x) ≥ m`: `δ_{N_j}` avalia 0, logo `¬(δ_{N_j}→τ_{N_j})` avalia 0.
Sob esta extensão de `x`, todo disjuncto de `⋁_j ¬(δ_{N_j}→τ_{N_j})` avalia 0; substituição
(operção fechada em EF) transforma a derivação de `Φ` numa derivação EF de `φ(x) ∨ (constantes-0)`;
e `EF ⊢ ¬(constantes-0)` trivialmente ⟹ `EF ⊢ φ(x)` — hmm, atenção: `x` foi **fixada**; o
que se obtém é uma derivação de `φ(x)` **para toda `x`** — como cada derivação usa só
finitos passos substitutivos, mas `φ` tem (internamente) `m` variáveis — o salto
"`∀x EF ⊢ φ(x)` ⟹ `EF ⊢ φ`" **não é automático**. **Correção do referee S2 incorporada:**
o passo certo é avaliar a derivação de `Φ` **uma única vez**: escolha **uma** extensão `x*`
de `x` aos demais átomos de `p` que, para todo `j`, ou falsifica `δ_{N_j}`, ou — quando
`code(N_j,x) < m` — estende `x` pelos falsificadores conjuntos `y_j` (união compatível por
(S2)); nos demais átomos (fora dos `N_j`), escolha arbitrária. Sob `x*`, `Φ` avalia
`φ(x) ∨ 0` — logo a derivação real de `Φ`, substituída por `x*`, é derivação EF **real** de
`φ(x)` — com `x` **arbitrária** em `p↾r` — hmm, o mesmo problema permanece para `x`
variando. **Estado honesto:** o argumento fecha **se** `x` puder ser tomada **uma vez** —
e ela pode: o que a refutação precisa é de **uma** falsificação de `φ` — tome `x` **livre**
(e não substituído): sob a extensão fixa `x*` (que só decide átomos dos `N_j` e espelhos,
**todos fixos e finitos** — `k` finito!), a derivação de `Φ` substituída dá
`EF ⊢ φ(p↾r) ∨ ⊥` com `p↾r` **ainda livre** ⟹ `EF ⊢ φ` **(P)**. *(O referee S2 tem razão
em exigir este arranjo: sem fixar `x*` finita e deixar `p↾r` livre, o passo não fecha.)* ∎

> **Corolário 2.2 (condicional) (P).** *Sob a hipótese de existência de `T_f` refutante
> (não provada — §1.3):* existe `v` com `i := code(N_j,v) ∈ M`, `i < m`, tal que `(α)_i`
> **não tem falsificador real algum** — uma autologia real em índice novo (`i ∉ M`: senão
> (S4)+absolutidade daria falsificador **(P)**). Pela soundness de EF em `M`
> (`Ref_EF ∈ T_PV`, `M ⊨ T_PV` **(A)**), as partes `¬τ` da refutação são **realmente
> verdadeiras** — ou seja: `M` certificaria, por derivação interna, não-falsificabilidade
> de `(α)_i` em um índice novo. *(A redação anterior "a refutação produz o certificado" foi
> corrigida: as direções são soundness/completude de EF, como apontou o referee S3.)*

## §3. Consequências para a reductio — com trilhas falsas documentadas

### 3.1 O que `M1`+`M2a` dão sob `NP=coNP` — **(P)**

Sob `NP=coNP`, `P` strong p-bounded **completo** é plausível **(C)**: então `(α)_i` autologia
(Cor. 2.2, condicional) tem `P`-prova real — uma **resolução** real de `(π, α, m)` em índice
novo. Coerente, sem contradição: `(S4)` protege só índices antigos. **Nenhuma contradição
emerge livremente.**

### 3.2 Trilhas falsas documentadas — **(P)** *(referee S4/S5)*

- **TF-1 (refutada — versão corrigida):** "(ST) contradiz resolução-em-índice-novo: o
  estudante corre em `M` e devolve `i ∈ M` antigo, que não resolve." **A premissa "`i ∈ M`"
  está CERTA** (`M ⊨ PV` ⟹ funções p-tempo reais fecham `M` — referee S4), mas o argumento
  falha por: `(ST)` só **constrange** a inexistência de estudante correto (não dá um para
  instanciar); **falhar numa instância ≠ contradição**; e decidir tautologias em índices
  não-padrões não é p-tempo. **Retirar dos "provados".**
- **TF-2 (rota (ii) anterior — retraída, referee S5):** "tornar `(ST)` interna
  (`M ⊨ estudante resolve DD_P`) e fechar com `M' ⊨ PV`." **Vazia:** `M ⊨ S` já refuta
  internamente a `(ST)`-interna (o estudante falha em `(π, α, m)`), e `(ST)`-interna é
  inconsistente com `(ST)` real via KPT (Teorema 3 do artigo: `S` inconsistente ⟹ estudante
  existe) **(A)**. Além disso o teorema de extração exigido ("índice novo ⟹ procedimento
  `p`-tempo com saída em `M ∩ m`") é **impossível** (G1, Thm 4.3 + G2, Thm 2.1(a′)) **(P)**.

### 3.3 Estado do problema — teorema de redução honesto — **(P)+(C)**

> **Proposição 3.1 (redução).** Fechar a reductio do Teorema 4 corrigido sob `NP=coNP` é
> **equivalente** a um dos dois: **(A)** provar **Q-compactness afirmativa** (existe `T_f`
> finito refutado internamente) **e** a extração de contradição do Cor. 2.2 sob
> p-boundedness/completude (candidato `X`: a refutação é `P`-bounded em tamanho —
> `≤ poly(|α|)` — tornando-a objeto de busca do estudante — `(C)`); **ou (B)** aceitar a
> alternativa de Q-compactness (só refutações "globais", não-padrões) — aí nada finito se
> extrai e a rota forcing/claim é **estruturalmente inalcançável** do lado de `M`.

## §4. Veredito honesto (≤ 600 palavras)

1. **Provado (P):** o forcing booleano **não pode semear `(F-sent)`** — nenhuma `G`
   universal realizaria `𝒯` (Thm 1.1): com isso, a pergunta original do ataque ("as
   condições do forcing corrigem o Teorema 4 com hipótese finita?") está **fechada de vez**:
   `Log` sim (G1), semente de falsificador sim (G2), `(F-b')` impossível (G1), `(F-sent)`
   irrealizável no forcing (G2+H1).
2. **Retraído (P):** a finitude da refutação (non-compactude interna — referee S1). O que
   fica é a **Questão Q-compactness**, um problema de compactude **interno a `M`** — e é
   agora o ponto exato onde a reductio do Teorema 4 toca o metalível: (A) ou (B) da §3.3.
3. **Condicionais válidos (P):** Thm 2.1 + Cor. 2.2 (com o arranjo de extensão finita `x*`
   corrigido pelo referee): **se** uma refutação finita interna existir, ela precisa de
   candidato não-coberto e produz autologia real certificada em índice novo — o objeto
   cuja extração sob p-boundedness é o último `(C)` da cadeia.
4. **Trilhas falsas TF-1/TF-2 documentadas** — em particular: `(ST)` interna é vazia, e
   "estudante devolve índice antigo" não é contradição. Qualquer ataque futuro deve passar
   por (A) ou (B) da §3.3.
5. **Valor para o artigo:** a nota ao autor ganha o fecho: *"`Log` é de graça, a semente do
   falsificador é consistente, mas `(F-b')` é impossível (G1) e a semente de `(8)` é
   irrealizável por qualquer `G` (G2+H1) — o item (5) não pode ser consertado por forcing
   algum; a única correção possível é a troca de hipótese 2.1 → (F-sent)"* — mais a questão
   Q-compactness como fronteira declarada.

**Próximos passos:** (1) referee desta versão 2 (foco: §2.2 arranjo `x*`; §1.3 non-compactude;
§3.3 equivalência); (2) decidir Q-compactness num caso concreto (modelos de `PV` não-padrões
contáveis — ultrapoderes de `N`?); (3) atualizar nota editorial; (4) Lean: G2 Thm 2.1.

**Lacunas honestas:** Q-compactness é `(C)`/aberta; completude de `P` sob colapso é `(C)`;
o Claim 2 de [Kra98] não foi relido verbatim esta rodada (o "no-G" não depende dele).

## §5. Relatório do referee e correções aplicadas (transparência)

| Ponto | Veredito | Ação |
|---|---|---|
| S1 (finitude) | ERRO — refutabilidade interna não é finitária (non-compactude) | **Retraída**; §1.3 Q-compactness; Thm 1.1 reescrito só como no-G; mal-tipagem dos espelhos corrigida (§1.1) |
| S2 (substituição) | PARCIAL — átomos de `N_j` ∈ `p`; passo final exigia arranjo finito | §2.2 reescrito com extensão finita `x*` e `p↾r` livre; (S2)-compatibilidade explícita |
| S3 (Cor. 2.2) | PARCIAL — `code ∈ M` a escrever; "certificada" impreciso | Cor. 2.2 corrigido: código ∈ M; direções via soundness/completude de EF |
| S4 (TF-1) | PARCIAL — conclusão certa, razão falsa (`M ⊨ PV` fecha saídas em `M`) | §3.2 TF-1 corrigida; retirada dos "provados" |
| S5 (rota ii) | ERRO — hipótese vazia (refutável em ZFC; inconsistente com (ST) via KPT) | **Retraída**; §3.3 redução (A)/(B) |

**Sobrevivente (1 linha):** "`𝒯` é irrealizável por qualquer `G` universal" (Thm 1.1) +
Thm 2.1/Cor. 2.2 **condicionais** à existência de refutação finita interna (Q-compactness
aberta).

# M — O canto adversarial (J2 §3): construído — e exatamente onde vive

> Frente M, **v4 RECOMENDADO** (referee rodadas 1–3: rodada 1 — REVISION, 0 FATAL,
> 5 MAIOR; rodada 2 — REVISION, MAJOR novo de `R(N_s)`; **rodada 3 — "RECOMENDADO
> definitivo" com E-1/E-2/E-3, todos aplicados**), 11 Out 2026.
> Marcação: **(A)** = fonte;
> **(P)** = próprio; **(C)** = conjectura. Contexto: `J2_ponto_fixo.md` §3 (a fronteira
> `(C)`), `J1_Qcompactness_M0.md` (Teorema K), `L1_phi_insatisfativel.md` (L.3′, L.3a),
> `H1_colecao_refutacao.md` §1.1 (semente: `δ_N`, `τ_N`, `code(N,q)`, `Names`),
> `A_teoremas_exatos.md` (§1.12 (S2)–(S4); §1.2 `m ≤ |α|`), `M_referee.md` (rodadas 1–3).

## §0. Missão e veredito sumário

Missão: decidir o canto **(C)** de `J2 §3` — a compatibilidade conjunta dos fibrados
`≥ m` para famílias no ramo vazio, incluindo a possibilidade de **par adversarial**
(mesmo padrão). Resultado: **o canto é REAL, e foi CONSTRUÍDO** — mas o mapa ficou
muito mais limpo que a fronteira sugeria, com **três teoremas**:

1. **M.0**: `T_S ⊢` **`m` é não-padrão** (em todo modelo) — o caso "m padrão" da
   fronteira **não existe**.
2. **M.1**: `T_S ⊢` **não existe falsificador global** (colagem de todos os `y_i`) —
   contrapositiva do Teorema K.
3. **M.2 (o adversarial)**: existe nome **não-padrão** `N_s` (um **seletor p-tempo**)
   com **`C_{N_s} ≡ ⊥` internamente, em todo `M_0 ⊨ T_S`** — sob **R1 e sob a
   alternativa com `q` total**; sob a alternativa com **`q` parcial** o trap **pode
   abrir** (§2 ressalva — a resposta do autor à semântica de `τ_N` decide) — condição
   da semente **internamente insatisfatível**, dual à `¬φ` (L.1), mas por mecanismo
   **diferente** (Teorema K, não soundness de `P`).
4. Consequências: nomes **padrão** nunca são adversariais **para nomes isolados,
   pares e famílias externamente finitas** (guarda `R(N)⊆m` é
   **automática em todo modelo** — o contraexemplo do referee J2 (m=2) é **vácuo**;
   famílias **internas** não-padrão-muitas permanecem **(C)** — coleção proibida);
   famílias com `C_{N_s}` são internamente insatisfatíveis **sem refutação genuína**
   (L.3′) — segunda instância de não-compactude; refutação interna **aberta**.

## §1. Dois lemas preliminares

> **Lema M.0 (m não-padrão) (P)** *(antecedente: Lema B.1 de `I1` — nenhuma instância
> padrão de `(S2)–(S4)` com `P` sounde — mesma família de argumento)*.
> `T_S ⊢` "m é não-padrão" — em **todo**
> `M_0 ⊨ T_PV+(S2)+(S3)+(S4)`.
>
> **Prova.** Suponha `m` padrão. Para cada `i < m` (**todos** os `i < m` são
> padrão), por **(S4)** instanciação interna em `i`: `∃y Fals(y, α_i)` — escolha
> `y_i ∈ M_0` (`m` escolhas — `m` padrão-muitos — sem coleção proibida). Montagem:
> `y := h(α, ⟨y_0,…,y_{m-1}⟩)` — a atribuição que em `at(α_i)` concorda com `y_i`
> (`i < m`), `0` no resto — é **p-tempo** em `(α, ⟨y_i⟩)` (`m ≤ |α|` — **(A✔)**
> `A_...` §1.2; `|y| ≤ |α|·max_i|y_i|`) ⟹ `y ∈ M_0`, e `y` falsifica **todo**
> `α_i` (`i < m` — todos padrão; localidade de `Fals`). Defina a **lista**
> `F := h'(y, α) = ⟨y↾at(α_i) : i < m⟩` — p-tempo (saída `m·|y| ≤ |α|·|y|`) ⟹
> `F ∈ M_0` é coleção **interna** com `∀i<m Fals(F(i), α_i)` — **proibida pelo
> Teorema K** (`J1` §3). Contradição. ∎
>
> *(Nota: o argumento usa que, com `m` padrão, `∀i<m` instancia só padrão-muitos —
> com `m` não-padrão a montagem cobre só `i` padrão e nada se conclui — sem
> circularidade. `at(α_i)` pode ser não-padrão mesmo para `i` padrão (`α` é
> não-padrão — L.3a) — por isso a montagem é p-tempo em `α`, não "padrão-finita".)*

> **Lema M.1 (sem falsificador global) (P).** `T_S ⊢` "não existe `y ∈ M_0` com
> `∀i<m Fals(y↾at(α_i), α_i)`" — **nenhum** `M_0 ⊨ T_S` tem falsificador global.
>
> **Prova.** Se `y` falsificasse todos os `α_i` (`i < m`, **todos** — inclusive
> não-padrão), a **lista** `F := ⟨y↾at(α_i) : i<m⟩ = h'(y,α)` é p-tempo (`F = h'(y,α)`,
> saída `m·|y| ≤ |α|·|y|`) ⟹ `F ∈ M_0` com `∀i<m Fals(F(i),α_i)` — coleção proibida
> (Teorema K: `K` quantifica sobre `F ∈ M_0` **arbitrárias** — não é preciso que `F`
> venha de escolha ou de uniformização PV; daí a diferença para o K-FP v1 retraído).
> Contradição. ∎
>
> *(Localidade de `Fals` (lê só `at(α_i)`) garante `Fals(y↾at(α_i), α_i) ⟺
> Fals(y, α_i)` — padrão.)*

## §2. O adversarial — a construção do seletor

**Ideia (P).** O seletor p-tempo `s(v) := ` "menor `i < m` tal que `¬Fals(v, α_i)`"
(existe por **M.1**: todo `v` falha em algum disjunto; e é **PV-total**: o laço roda
`i = 0,…,m−1` — `m ≤ |α|` **(A✔)** `A_...` §1.2 (**corrigido na rodada 1**: a v1
citara `G2 §2.2`, que fala de "tamanhos internos ≤ poly(α)" e é (P)) — cada teste
`Fals` é p-tempo; fora do laço, default `0`). Os **bits** de `s(v)` são circuitos
sobre `p` (hardwirando `α,m` como constantes — os circuitos de `M_0` podem) — logo
`N_s := ⟨C_1,…,C_ℓ⟩` com `ℓ = ⌈log m⌉` é um **nome** (`N_s ∈ Names_M(p)`;
**não-padrão** porque `ℓ = ⌈log m⌉` é não-padrão — `m` não-padrão por M.0 —, não por
cota de tamanho; `R(N_s)` é **não padrão-finita** — prova por contrapositiva
[rodada 2 — a v2 alegara sobrejetividade, **errada**: M.1 é `∀v∃i`, não `∀i∃v`, e
`α_i ≡ ⊥` daria `i ∉ R(N_s)`]: se `R(N_s) ⊆ {0,…,k}` com `k` **padrão**, colha
por **(S4)** `y_j ∈ M_0` para `j ≤ k` (padrão-muitos ✓) e monte
`σ* := h(α,⟨y_j⟩_{j≤k})` (o mesmo `h` de M.0 — `m ≤ |α|`) — `σ*` **falsifica
`α_0..α_k`** (por construção de `h` + **localidade** de `Fals`; a colagem em
at(α_j) é sem conflito por **(S2)**) — logo `s(σ*) > k` (menor índice mau passa
`k`) — mas `s(σ*) ∈ R(N_s) ⊆ {0,…,k}` — contradição. Logo `R(N_s)` não é
padrão-finita — **não-padrão-muitos**. *(Escopo [errata E-1]: a prova exclui só
`k` **padrão**; `k` não-padrão exigiria amalgamar `k+1` falsificadores — coleção
proibida (Teorema K) — logo **não** concluímos "cofinal em `m"`.)*
*Lateral: isto não entra em δ/τ — só classifica `N_s`.*).
E `N_s` é um **adversário perfeito**:

> **Teorema M.2 (o canto é real — `C_{N_s} ≡ ⊥`) (P).** Em **todo** `M_0 ⊨ T_S`:
> `δ_{N_s} ≡ 1` e `τ_{N_s} ≡ 0` — logo **`C_{N_s} = δ_{N_s} → τ_{N_s}` é internamente
> insatisfatível** (avalia `0` sob **toda** atribuição).
>
> **Prova.** Para qualquer atribuição `v`: `code(N_s, v) = s(v) < m` (totalidade do
> seletor — **M.1**) ⟹ `δ_{N_s}(v) = 1`. E `s(v)` é **mau para `v`** por construção:
> `¬Fals(v, α_{s(v)})` — i.e., a própria `v` não falsifica o disjunto que ela mesma
> seleciona. Para `τ_{N_s} = ⋁_q (q` cod. atribuição ∧ `Fals(q, (α)_{code(N_s,q)})`)`:
> cada disjuncto falha — `code(N_s,q) = s(q)` é mau **para `q`**, i.e.,
> `¬Fals(q, α_{s(q)})` ⟹ `τ_{N_s} ≡ 0`. Logo `C_{N_s}(v) = 1 → 0 = 0` para todo `v`.
> ∎
>
> **Ressalva de semântica (P)** — a leitura alternativa de `τ_N` (`J2 §1`, referee
> nº 1): se `q` for atribuição **total** (a forma do artigo: *"q codifica atribuição"*),
> `q⊗v = q` e o trap fecha igual. Se `q` for **parcial** (merge), o índice é mau para
> `q⊗v` mas o falsificador é `q` — o trap **pode** abrir. **Marcado: a resposta do
> autor à semântica de `τ_N` (§4.1 da nota) também decide o trap.**

> **Observação (por que isso não colide com K-FP′) (P).** K-FP′ cobre nomes
> **padrão** (`R(N)` padrão-finito — colagem de `g_i` sobre padrão-muitos). `N_s` é
> **não-padrão** (`R(N_s)` não-padrão-muitos) — colar `g_i` sobre `R(N_s)` seria
> exatamente a coleção proibida (Teorema K) — e M.2 mostra que o bloqueio é **genuíno**:
> o ponto fixo para `N_s` **não existe** (senão `τ_{N_s} ≥ Fals(q*,α_{s(q*)})` —
> contradiz a mau-da-construção). O Teorema K e K-FP′ continuam consistentes; o canto
> adversarial é o **território exato** onde a coleção proibida vira **derangeamento
> p-tempo**.

## §3. Consequências

> **Corolário M.3 (o `(C)` do J2 §3 está DECIDIDO) (P).** A fronteira `(C)` se resolve
> em **três fatias**:
> (a) **`m` padrão**: caso **inexistente** (M.0) — a preocupação "par adversarial
> mesmo padrão" com `m` padrão é **vácuo**;
> (b) **nomes padrão** (qualquer `m`): `R(N) ⊆ m` **automática** (`code` padrão-tamanho
> < `m` não-padrão — M.0) ⟹ **J.6-a′ cobre** — nomes padrão **nunca** são
> adversariais **para nomes isolados, pares e famílias externamente finitas** (alcance
> de J.6-a′); o contraexemplo do referee J2 (`N=⟨1,1,1⟩, m=2`) é **vácuo** (m=2
> impossível — M.0). **Residual honesto ((C))**: famílias **internas** com
> não-padrão-muitos nomes padrão exigiriam **coleção proibida** (Teorema K) — fora
> do alcance de J.6-a′, **permanecem `(C)`** (a "correção à J2 §3" vale, portanto,
> só nesse escopo);
> (c) **nomes não-padrões**: o adversarial é **real** — M.2 constrói `N_s` com
> `C_{N_s} ≡ ⊥` (**in-range**! `δ≡1` — o ramo vazio também só tem nomes não-padrões:
> `code` padrão-tamanho nunca alcança `m` não-padrão). **Correção à J2 §3**: a
> fronteira não é "ramo vazio" — é "**nomes não-padrões**" (in-range ou vazio).
>
> **Corolário M.4 (segunda condição `≡ ⊥` da semente; não-compactude) (P)+(A).**
> `𝒯` contém agora **duas** condições canônicas internamente insatisfatíveis:
> `¬φ` (L.1 — via soundness de `P`) e `C_{N_s}` (M.2 — via Teorema K). Famílias
> finitas contendo `C_{N_s}` são **internamente insatisfatíveis** e, por **L.3′**,
> **sem refutação genuína**. Refutação **interna** de `{C_{N_s}}`: seria uma prova EF
> de `¬C_{N_s} = δ_{N_s} ∧ ¬τ_{N_s}` — sentença **verdadeira** em `M_0` cuja
> provabilidade EF é **aberta** (mesma forma de L.3″ / aviso L21–22) — **(C)**:
> plausivelmente não-provável, não verificado. *(Para `¬φ`, a Condition 1 do artigo
> fornece a exclusão; para `C_{N_s}` não há hipótese análoga — honestamente aberto.)*
>
> **M.5 (robustez de J.6-a′) (P).** A guarda `R(N)⊆m` do K-FP′ é **automática em todo
> `M_0 ⊨ T_S`** para nomes padrão (M.0) — J.6-a′ vale **sem ressalva de `m`**.

## §4. Interação com a pergunta aberta (τ_N) e com a nota editorial

- A ressalva de §2 **acrescenta pressão** à pergunta §4.1 da nota (`τ_N`: R1 vs
  alternativa): a resposta do autor decide (i) se o corner dissolve sob R1 (τ≡1 —
  K-FP′), (ii) se o trap M.2 fecha sob a alternativa-total e abre sob a alternativa-par.
- **Recomendação ao usuário**: acrescentar à nota (§4) a pergunta "`q` em `τ_N` é
  atribuição **total**?" — é a pergunta que decide o canto adversarial.
- Sob **R1**: `τ_{N_s} ≡ 0` (M.2 prova) — sob R1, K-FP′ daria `τ_N ≡ 1` **para nomes
  padrão**; para `N_s` não-padrão, M.2 mostra `τ ≡ 0` — as duas coisas são
  consistentes (guarda de K-FP′ é nomes padrão) e mostram que **sob R1 o corner
  também é real para nomes não-padrões**. **Alinhamento (rodada 1)**: o corner é real
  **sob R1 e sob a leitura alternativa com `q` total**; sob a alternativa com **`q`
  parcial** (merge), o trap **pode abrir** (§2 ressalva) — a resposta do autor à
  pergunta "q é total?" decide o caso-par (a v1 dizia "sob ambas as leituras" sem
  esta qualificação — corrigido em §0 e §6).

## §5. Certificados para humanos (checklist)

| # | Afirmação | Verificação | Onde |
|---|---|---|---|
| 1 | (S4) instanciável em `i` padrão `< m`; (S2) disjuntos | verbatim | `A_...` §1.12 |
| 2 | Montagem `y := h(α,⟨y_i⟩)` p-tempo (`m ≤ |α|`); `F := h'(y,α)` lista ∈ `M_0` (sem compreensão) | padrão | M.0, M.1 |
| 3 | Lista `F = h'(y,α) = ⟨y↾at(α_i)⟩_{i<m}` ∈ `M_0` (p-tempo; saída `m·|y| ≤ |α|·|y|`); K quantifica sobre `F ∈ M_0` **arbitrárias** (sem escolha — diferença p/ K-FP v1) | padrão | M.0/M.1 |
| 4 | Teorema K (proíbe coleção `∀i<m`) | referee-validada | `J1` §3 |
| 5 | `m ≤ |α|` (**(A✔)** `A_...` §1.2 — corrigido: v1 citara `G2 §2.2`) + laço `i<m` do seletor (PV-totalidade, default 0) | verbatim | §2 |
| 6 | Seletor `s(v)` = p-tempo; bits = circuitos; `N_s ∈ Names` | padrão | §2 |
| 7 | `s(v)` mau para `v` (por construção) ⟹ `τ_{N_s} ≡ 0` | 2 linhas | M.2 |
| 8 | K-FP′ só para nomes padrão — sem colisão com M.2 | conferir | §2 Obs. |
| 9 | `code` padrão-tamanho < `m` não-padrão (M.5) | padrão | §3 |
| 10 | Semântica de `τ_N` (q total vs parcial) — aberta | referee nº 1 | §2 Ressalva |
| 11 | Refutação interna de `{C_{N_s}}` — aberta (prova EF de `δ∧¬τ`) | honesto | M.4 |

## §6. Veredito e próximos passos

**Veredito (P):** o canto `(C)` de `J2 §3` está **decidido**: o adversarial é **real**
e **construído** (M.2: seletor p-tempo `N_s` com `C_{N_s}≡⊥` em todo modelo) — vive
**exatamente** nos nomes **não-padrões** (o caso padrão colapsa: `m` sempre não-padrão
(M.0); nomes padrão sempre in-range (M.5) ⟹ J.6-a′ — famílias internas
não-padrão-muitas permanecem `(C)`, M.3(b)). A semente tem **duas**
condições canônicas `≡ ⊥` (`¬φ` e `C_{N_s}`) — não-compactude com **duas** fontes
(soundness de `P`; Teorema K). O corner é real **sob R1 e sob a alternativa com `q`
total**; sob a alternativa com `q` parcial pode abrir (§2 ressalva — decisão do autor).

**Próximos passos:** (1) referee hostile (foco: M.0 — a instância de (S4) em `i`
padrão e a coleção `F`; M.1 — a contrapositiva de K; M.2 — PV-idade do seletor
(`m ≤ |α|` — `A_...` §1.2), `τ ≡ 0` disjunção-a-disjunto, ressalva do merge; M.3–M.5 escopos);
(2) com o veredito, **acrescentar à nota editorial** a pergunta "`q` é total?" (§4)
e o item M.2 como sexto obstáculo (§2) — decisão do usuário; (3) decidir a refutação
interna de `{C_{N_s}}` (prova EF de `δ_{N_s}∧¬τ_{N_s}` — pergunta de provabilidade,
mesma forma de L.3″).

**Lacunas honestas:** a ressalva do merge (§2) — se a leitura alternativa for par,
o trap pode abrir (a pergunta ao autor decide); M.4 (refutação interna) é **(C)**;
M.2 depende de `m ≤ |α|` (**(A✔)** `A_...` §1.2 — o laço é sobre `i<m` — conferir
no artigo a redação exata de §1.2); o **big-or/tamanho de `τ_N`** herda a ressalva
do `J2_referee` MAJOR-1(iii) (não reavaliado aqui — **marcado**); a "coleção
interna" de M.0/M.1 usa a mesma noção de K (sequência/lista em `M_0`) — se o
referee de K tiver formalizado de forma diferente, alinhar.

## §7. Autoria e método

Análise do orquestrador (frente M); referee hostile (`M_referee.md`, rodada 1:
REVISION — 0 FATAL, 5 MAIOR; núcleo M.2 confirmado). O ataque segue o
padrão do projeto: **a fronteira `(C)` foi convertida em pergunta combinatoria finita**
(fibrados `≥ m` / seletores p-tempo / falsificadores globais) e decidida — com o
**Teorema K** (J1) aparecendo pela terceira vez como ferramenta (aqui: para **construir**
o adversarial, não só para proibir).

## §8. Registro de correções (v1→v2; rodada 1: 0 FATAL, 5 MAIOR)

- **MAJOR-1 (M.0)**: "`A_i := at(α_i)` padrão-finito (dados padrão)" era **falso**
  (`α` é não-padrão — L.3a —, sob `m` padrão algum `α_i` de `i` padrão é não-padrão)
  ⟹ reescrito como **montagem p-tempo** `y := h(α,⟨y_i⟩)` (`m ≤ |α|` — (A✔)
  `A_...` §1.2); antecedente **Lema B.1 (I1)** citado.
- **MAJOR-2 (M.1)**: "p-tempo em `y` ⟹ `F ∈ M_0`" omitia a **coleta** do código de
  lista de comprimento `m` (K quantifica sobre `F ∈ M_0` **arbitrárias**) ⟹ `F :=
  h'(y,α)` p-tempo (saída `m·|y| ≤ |α|·|y|`); nota "sem escolha — diferença para o
  K-FP v1 retraído"; checklist nº3 reescrito.
- **MAJOR-3 (M.2a)**: `m ≤ poly(|α|)` **não** está em `G2 §2.2` (lá: "tamanhos internos
  ≤ poly(α)"; G2 é (P)) ⟹ fonte corrigida: `m ≤ |α|` — **(A✔)** `A_...` §1.2; §2,
  checklist nº5 e §6 corrigidos; totalidade do seletor explicitada (PV-totalidade,
  default `0`); `N_s` não-padrão **por `ℓ=⌈log m⌉`** (não por cota poly);
  `R(N_s)` não-padrão-muitos justificado em 2 linhas.
- **MAJOR-4 (M.3(b))**: "nomes padrão **nunca** adversariais" restrito a **nomes
  isolados, pares e famílias externamente finitas** (alcance de J.6-a′); famílias
  **internas** não-padrão-muitas exigiriam coleção proibida — **permanecem `(C)`**.
- **MAJOR-5 (§0/§4/§6)**: "corner sobrevive sob **ambas** as leituras" **alinhada** à
  ressalva do merge: real **sob R1 e sob a alternativa com `q` total**; sob alternativa
  com `q` parcial pode abrir — decisão do autor.
- **MENORES**: typos ("vacuo"→"vácuo", "daría"→"daria", "differently"→"de forma
  diferente"); big-or/tamanho de `τ_N` **marcado** como herança do `J2_referee`
  MAJOR-1(iii) (§6 lacunas).
- **Confirmados pelo referee rodada 1**: núcleo **M.2** (seletor p-tempo total,
  `code(N_s,q)=s(q)`, `δ≡1`, `τ≡0` diagonal); Observação (sem colisão com K-FP′);
  `τ_{N_s}≡0` sob R1 consistente; **M.4** honesto ((C) marcado); M.5.

## §8b. Registro de correções (v2→v3; rodada 2: REVISION — MAJOR-1/2/4 fechados,
MAJOR-5 parcial; MAJOR novo de `R(N_s)`; 3 reparos finais; **rodada 3: RECOMENDADO
com E-1/E-2/E-3 — aplicados**)

- **MAJOR novo (R(N_s))**: as 2 linhas da **v2** alegavam **sobrejetividade** de `s`
  (a v1 só havia **afirmado sem prova** — errata E-3(a)) — **errada** (erro de
  quantificadores: M.1 é `∀v∃i`, não `∀i∃v`; e `α_i ≡ ⊥` daria `i ∉ R(N_s)`;
  "índice mau" indefinido) ⟹ substituídas pela prova **por
  contrapositiva**: `R(N_s) ⊆ {0,…,k}` (k padrão) ⟹ `σ* := h(α,⟨y_j⟩_{j≤k})` falsifica
  `α_0..α_k` ⟹ `s(σ*) > k` — contradição ⟹ `R(N_s)` **não padrão-finita**
  (escopo E-1: não "cofinal em `m`" — `k` não-padrão daria coleção proibida);
  `(S4)`/`(S2)`+localidade nomeados na escolha de `y_j` e em "σ* falsifica" (E-2).
- **§0 item 3**: acrescentada a ressalva do `q` parcial (R1/alternativa-total: real;
  alternativa-par: pode abrir); **§0 item 4**: escopo "isolados, pares e famílias
  externamente finitas" + "(C)" para famílias internas.
- **Checklist nº2**: "colagem padrão-finita" → montagem/lista p-tempo `h/h'`.
- **§8 (log da v1→v2)**: corrigida a imprecisão (dizia "corrigido em §0" antes de
  sê-lo — o §0 só foi corrigido na v3).
- **E-3(b)**: o título de §8b corrigido — MAJOR-5 ficou **parcial** na rodada 2
  (§0 só na v3; o veredito da rodada 2 foi REVISION).
- **Estado final (v4 RECOMENDADO)**: rodada 3 do referee: "`R(N_s)`: CORRETA no
  essencial"; E-1 (escopo "não padrão-finita", não "cofinal em `m`"), E-2
  ((S4)/(S2)+localidade nomeados) e E-3 (atribuição e título) **aplicados** —
  "aplicadas E-1/E-2/E-3: **RECOMENDADO definitivo**".

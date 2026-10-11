# L1 — `¬φ` insatisfatível em todo modelo; **C.3 decidida: negativa incondicional**

> Frente L, **v4 RECOMENDADO** (referee rodada 3 pre-comprometeu: "Com as 4 erratas
> da §4 aplicadas: RECOMENDADO" — rodadas 1–2: L.1 CORRETA, 0 FATAL, 3 MAIOR fechados;
> 4 erratas da rodada 3 aplicadas em v4), 11 Out 2026. Marcação: **(A)** = fonte;
> **(P)** = próprio; **(C)** = conjectura. Contexto:
> `A_teoremas_exatos.md` ((S4): §1.12; `Ref_P ∈ T_PV`: L341; Condition 1: L190/L375/L514;
> aviso L21–22; Claim 2/KPT: L341), `J1_...` (J.5-sound, J.0(a)), `J2_...` (K-FP′,
> §3 adversarial), `H1_...` (no-G), `L1_referee.md` (rodadas 1–3).

## §0. Missão e resultado (v4)

Missão: decidir `T_S ⊢ ∃r ¬φ(r)?` (`J2 §4`). Resultados — **três**:

1. **Teorema L.1 (CORRETO, referee rodada 1)**: `T_PV + (S4) ⊢ ∀r φ(r)` — `¬φ` é
   **internamente insatisfatível em todo modelo** (só `(S4)` + soundness interna de `P`;
   `(S2)`/`(S3)` desnecessárias).
2. **Teorema L.3′ (NOVO — referee MAJOR-2)**: **C.3 é negativa INCONDICIONALMENTE** —
   nenhum `d*` padrão refuta qualquer subfamília internamente finita da semente, **sem**
   Condition 1, **sem** (Hjoint), **sem** o canto adversarial: membros **padrão** da
   semente = **só as constantes-1** (carregador corrigido [rodada 2]: `τ_N`/`¬φ`
   embutem os bits de `α` como **constantes** — códigos de tamanho `≥ |α|`, não-padrão
   pelo **Lema L.3a**; cobre o ramo mesmo se `δ_N` fosse padrão) ⟹
   premissas de `d*` são tautologias reais ⟹ soundness real de EF.
3. **Gap do artigo PINCADO (referee MAJOR-1)**: L.1 aplicada em `M'` força o falsificador
   de `φ` a viver num **índice `i_0` onde `(S4)` falha em `M'`** — exatamente o ponto
   da lacuna `i_0 ∈ M*` do Teorema 4 (errata F1) — a Nota L.1′ (v1: "consistente com
   todo o artigo") foi **reescrita** em §2.

## §1. Teorema L.1

> **Teorema L.1 (P; referee: "CORRETA", "(A✔) verbatim" para a rota (α)).**
> `T_PV + (S4) ⊢ ∀r φ(r)` — em **todo** `M_0 ⊨ T_PV+(S4)` (com `α,m` nomeados —
> escopo da sentença, MENOR da rodada 1): `M_0 ⊨ ∀r∀i<m ¬Ref_P((r)_i,(α)_i)`.

**Prova (todos os passos ∈ `T_PV` por sentenças universais verdadeiras).** Seja `r`
arbitrário, `i<m`, `d := (r)_i` (a `i`-ésima string da lista codificada por `r` —
tipagem conferida: verbatim "i-th string in the list coded by z"). Suponha
`Ref_P(d, α_i)`.
1. **(S4)** instanciada em `i<m`: `∃y Fals(y, α_i)`.
2. **Soundness interna de `P`**: `Ref_P ∈ T_PV` (verbatim L341 — o artigo chama
   `Ref_P` de "the universal valid `L_PV` formula" — **(A✔)**) e a sentença
   `Ref_P(d,β) → ∀v v⊨β` é universal verdadeira ⟹ `M_0 ⊨ ∀v v⊨α_i` — instancie
   `v := y`: `eval(α_i,y)=1`.
3. `Fals(y,α_i)` dá `eval(α_i,y)=0` — incompatibilidade (∈ `T_PV`) — contradição.
Logo `¬Ref_P(d,α_i)` para todo `d`, `i<m`; `φ(r)` é a conjunção das negações
`(r)_i : P ⊬* (α)_i` sobre `i<m` ⟹ `∀r φ(r)`. ∎

*(O parêntese v1 "∀r∃i trivial" foi retirado — gambiarra, conforme referee: a forma
correta é a conjunção sobre `i<m` das negações, direta.)*

## §2. Pinçamento do gap do artigo (referee MAJOR-1; Nota L.1′ reescrita)

> **Proposição L.1′ (P)+(A✔) [referee rodada 2: "eu a certifico no verbatim — o artigo
> define `i_0` exatamente como índice do falsificador de `φ`"].** Seja `M'` qualquer
> extensão com `M' ⊨ T_PV` e `M' ⊨ ∃r¬φ(r)` (obtido **por hipótese (2.1AF)** do artigo —
> a afirmação do Problema 2.1 — não "por forçamento" em abstrato). Então, por L.1:
> **`M' ⊭ (S4)`** — o testemunho de `¬φ` em `M'` aponta um índice `i_0 < m` tal que
> **`α_{i_0}` não tem falsificador em `M'`**. I.e., o falsificador de `φ` vive
> **necessariamente num índice onde `(S4)` falha na extensão** — e este `i_0` **é** o
> `i_0` do passo (5) do artigo, que invoca (7) **(A✔)**.

**Consequência para a errata — DICOTOMIA CONVENÇÃO-FORTE (P)+(A) [referee rodadas 2–3].**
Sob a **convenção forte** (fechamento + `Log` — a condição **(3)** do Problema 2.1,
com **(1)** entregando **(8)**), L.1′ mostra **(1)+(2)+(3) mutuamente inconsistentes
via (8)** — com **(2)** sendo justamente a existência do falsificador — i.e., **o
Problema 2.1 é negativo para esta instância** — e, pelo **rodapé 2** do artigo
(`¬2.1 ⟹ P≠NP` **(A)**), isto implicaria `P≠NP`. A alternativa: a convenção forte
**não** é a que o artigo precisa — a análise de (1) sobrevive só numa versão
**enfraquecida** (a direção da errata). O artigo não pode ter ambas: ou (1)+(2)+(3)
valem e 2.1 falha para a instância (⟹ `P≠NP`), ou a análise é reenquadrada. **Isto
estreita a errata: a lacuna `i_0 ∈ M*` não é só infundada — sob a convenção forte,
é contraditória com L.1.** *(O alcance exato desta dicotomia depende do verbatim de
(1)–(3) e (8) — marcado para referee final.)*

**Retratação da v1**: a Nota L.1′ v1 ("`M ⊨ ∀rφ(r)` é consistente com todo o artigo")
era **fraca demais** (MAJOR-1): o resultado correto é o pinçamento acima — L.1 não é
só compatível, é **a chave** que fixa onde o falsificador precisa morar. O Claim 2/KPT
(L341) permanece: para generics **não-elementares**, `¬φ` pode ser realizado num índice
com `(S4)` falhando; para generics **cofinais `Σ^b_1`-elementares com a direção
`M[G]→M`** (MAJOR-3: só a preservação `M→M[G]` não basta), `∃r¬φ(r)` transfere de
`M[G]` para `M` — **rota paralela** ao no-G do `H1 Thm 1.1`, não caso especial.

## §3. Teorema L.3′ — C.3 decidida: negativa incondicional (referee MAJOR-2)

> **Teorema L.3′ (P; inspirado no MAJOR-2 do referee).** Nenhum `d* ∈ ℕ` refuta
> **genuinamente** qualquer subfamília internamente finita `L ⊆ 𝒯_{M_0}` —
> **incondicionalmente** (sem Condition 1, sem (Hjoint), sem o canto adversarial).
> **C.3: NEGATIVA.** *(Reescopo [rodada 2]: L.3′ fala só de refutações **genuínas**
> (testemunha padrão). Refutações **internas** com testemunha **não-padrão** são a
> pergunta de Q-compactude — ver L.3″ abaixo; o parêntese v2 "nem internamente, com
> verificação absoluta" era ambíguo e foi retirado.)*

**Lema L.3a (α não-padrão) (P)+(A).** `α` tem tamanho não-padrão em todo
`M_0 ⊨ T_PV+(S2)+(S3)+(S4)`. *Prova:* se `α` fosse de tamanho padrão, seus
partes `(α)_i` seriam padrão para `i` padrão, e `m ≤ |α|` seria padrão; por
**(S4) + absolutidade** (dados padrão: verificação `Fals` é `Δ^b_0` absoluta —
J1 J.0(a)) cada parte teria **falsificador real**; por **(S2)** (átomos disjuntos)
as amalgamações são compatíveis e a amalgama real `σ*` falsifica **todas** as
partes; mas por **(S3)** `M_0 ⊨ Ref_P(π,α)` e soundness interna dão
`M_0 ⊨ ∀v v⊨α` — instanciando em `v := σ*` (objeto padrão): `eval(α,σ*)=1`, e a
avaliação é absoluta (dados padrão) ⟹ `eval(α,σ*)=0` — contradição. ∎

**Prova de L.3′.** Se `d*` padrão refuta `L` (genuinamente: `M_0 ⊨ Ref_EF(d*, L, ⊥)`):
por J.0(a) (J1), as premissas usadas são de tamanho **padrão**. Membros padrão de
`𝒯_{M_0}`: **só as constantes-1** — carga correta do carregamento não-padrão
**(corrigido na rodada 2 — o `≥ |m|` da v2 foi retirado: `m` não é excluído de ser
padrão)**: `τ_N` e `¬φ` **embutem os bits de `α` como constantes** (verbatim —
referee conferiu no artigo: "bits of α for atoms q" = constantes, sem espelhamento
livre) ⟹ códigos de tamanho `≥ |α|` — e `|α|` é **não-padrão pelo Lema L.3a** —
o que cobre o ramo **mesmo se `δ_N` fosse padrão**. (`δ_N` embute `m` — irrelevante
para a conclusão: o ramo já é descartado por `τ_N`/`¬φ`.) Logo as premissas de `d*` são
**constantes-1** — tautologias **reais** — e por **soundness real de EF** (derivação
real, axiomas verdadeiros, regras preservam verdade sob atribuições reais), `⊥` não
é conclusão. Contradição. ∎

> **Corolário L.3″ (escopo limpo) (P).** A pergunta original de `H1 §1.3` (refutação
> **interna** finita) permanece: L.1 mostra `{¬φ}` insatisfatível internamente, e sob
> **Condition 1** (L.3 da v1, aqui preservada como **condicional**) ele não tem
> refutação interna — máxima não-compactude **no plano interno**. Mas a pergunta de
> **C.3** (testemunha **padrão**) está decidida **sem** Condition 1 (L.3′). O canto
> **adversarial** (`J2 §3`) só toca o plano **interno** ((Hjoint)/satisfatibilidade) —
> **não** C.3 (MAJOR-2: a v1 estava errada ao enfiá-lo na tabela de C.3).

## §4. Corolários L.2 e L.4 (mantidos; escopo ajustado)

> **L.2 (P)**: `{¬φ}` é internamente insatisfatível em todo modelo ⟹ `(Hjoint)` falsa
> em todo modelo; o Teorema J′ (J1) é vácuo como hipótese — mas **desnecessário**: a
> resposta negativa de C.3 vem de L.3′ (incondicional).
> **L.4 (P)+(A; escopo: `M` com Condition 1)**: Condition 1 + L.1 ⟹ `φ` é
> **internamente válida** e **internamente não-provável** em `M` — o aviso verbatim
> L21–22 ("a pps may be **incomplete** in a model of `T_PV`") é **exemplificado pelo
> próprio `φ` do artigo** sob suas hipóteses — o artigo diz "may"; L.4 diz "**é**,
> nesta instância" — supersede sem contradizer (referee).

## §5. Certificados (checklist; ampliado)

| # | Afirmação | Verificação | Onde |
|---|---|---|---|
| 1 | (S4) + instanciação em `i<m` arbitrário | verbatim | `A_...` §1.12 |
| 2 | `Ref_P ∈ T_PV` ("the universal valid L_PV formula") | verbatim **(A✔)** | `A_...` L341 |
| 3 | `(r)_i` = i-ésima string da lista codificada (tipagem) | verbatim | `A_...` (referee) |
| 4 | Bits de α entram como **constantes** (tamanho não-padrão dos códigos) | verbatim **(A✔)** | artigo (referee rodada 1) |
| 4b | **Lema L.3a**: `α` não-padrão (absolutidade de `Fals` (testemunha **limitada**) + `(S2)` + soundness + `v:=σ*` — referee rodada 3: "correto"; `σ*` padrão, `m` padrão ⟹ `σ*∈M_0`) | referee-validada | §3 |
| 5 | J.0(a): premissas de `d*` padrão | referee-validada | J1 §1 |
| 6 | Soundness real de EF (derivações reais) | padrão | I1 §5; L.3′ |
| 7 | Condition 1 (só para o plano interno — L.3″) | verbatim | `A_...` L190/L375 |
| 8 | Elementaridade `Σ^b_1` **dois sentidos** para transferir `∃r¬φ(r)` (`M[G]→M`) | referee MAJOR-3 | §2 |
| 9 | Aviso L21–22 | verbatim | `A_...` L21–22 |

## §6. Veredito e próximos passos

**Veredito (P):** a pergunta-chave está decidida **duas vezes**: **L.1** (`¬φ`
insatisfatível internamente em todo modelo — o falsificador do artigo precisa morar
num índice onde `(S4)` falha — pinçando a lacuna `i_0∈M*` do Teorema 4; **`i_0`
certificado como o do artigo pelo referee rodada 2**) e **L.3′** (**C.3 negativa
incondicionalmente** — argumento trivial de tamanhos, com o Lema L.3a e o carregamento
corrigido). A não-compactude interna (`{¬φ}` insatisfatível + não-refutável sob
Condition 1) e a incompletude exemplificada (L.4) completam o quadro.

**Próximos passos:** (1) referee da v3 (foco: Lema L.3a — a absolutidade de `Fals`
em dados padrão e o encaixe do `σ*` amalgamado pela instância `v := σ*`; a dicotomia
convenção-forte de §2 — o rodapé 2); (2) **montar a nota editorial a Krajíček**
com: errata (lacuna verbatim + L.1′-pinçamento + dicotomia), Teorema K (J1, mecanismo
de BB), K-FP′ (J2), L.1+L.3′+L.4 (frente L); (3) canto adversarial `(C)` — só como
pergunta interna (não toca mais C.3).

**Lacunas honestas:** o alcance da dicotomia convenção-forte (§2) depende do verbatim
de (2)+(3) — pendente; a convenção "bits de α = constantes" está (A✔) pelo referee
rodada 1 (conferido no artigo); L.4 tem escopo condicionado a Condition 1; a
classificação "membros padrão = só constantes-1" cobre os ramos `τ_N`/`¬φ` via
L.3a (o ramo `δ_N` é irrelevante — ver §3).

## §7. Registro de correções (v1→v2; rodada 1: 0 FATAL, 3 MAIOR)

- **MAJOR-1**: Nota L.1′ ("consistente com todo o artigo") → **Proposição L.1′** de
  pinçamento (`M' ⊭ (S4)`; o falsificador vive onde `(S4)` falha; ligação à errata
  `i_0∈M*` — §2). Claim 2/KPT reescrito com elementaridade **dois sentidos** e como
  **rota paralela** (MAJOR-3).
- **MAIOR-2**: **Teorema L.3′** adicionado — C.3 negativa **incondicional** (membros
  padrão da semente = só constantes-1; verbatim "bits de α = constantes"); a tabela
  §3 v1 ("aberto (C)" para C.3) foi **corrigida** — o adversarial só toca o plano
  interno (L.3″); nota de que **J′ não precisava de (Hjoint)** para o ramo genuíno.
- **MAJOR-3**: elementaridade dois sentidos explicitada em §2.
- **MENORES**: escopo `T_PV+(S4)+(α,m)` nomeado (§1); parêntese-gambiarra "∀r∃i"
  retirado; escopo de L.4 a `M` com Condition 1.
- **Confirmados**: L.1 (CORRETA; rota (α) = "(A✔) verbatim"); L.2; L.4 (fiel —
  "may" → "é", supersede); tipagem de `(r)_i`.

## §7b. Registro de correções (v2→v3; rodada 2: REVISION "quase-recomendado", 0 FATAL)

- **MAJOR-1 (fechado)**: (a) `i_0` **certificado no verbatim pelo referee** —
  "o artigo define `i_0` exatamente como índice do falsificador de `φ`" ⟹ promovido
  de (P) a **(P)+(A✔)** (§2); (b) "obtém por forçamento" → **"obtido por hipótese
  (2.1AF)"**; (c) **Dicotomia convenção-forte** escrita em §2: sob (2)+(3) [v4: rótulo
  corrigido — ver §7c], L.1′ ⟹
  2.1 negativa para a instância ⟹ (rodapé 2) `P≠NP`; alternativa: convenção forte
  enfraquecida (a direção da errata) — o artigo não tem ambas.
- **MAJOR-2 (fechado)**: (a) **Lema L.3a** adicionado (`α` não-padrão: 1 linha —
  absolutidade de `Fals` + `(S2)` + soundness + `v := σ*`); (b) carregamento
  corrigido: **`≥ |m|` retirado** (`m` não é excluído de ser padrão) — o carregador
  é `τ_N`/`¬φ` ⊇ bits de `α` como constantes, tamanho `≥ |α|` não-padrão (L.3a),
  cobrindo o ramo mesmo se `δ_N` fosse padrão; (c) **reescopo de L.3′**: só
  refutações **genuínas** — o parêntese ambíguo "nem internamente, com verificação
  absoluta" foi retirado (as internas não-padrão são a pergunta de Q-compactude —
  L.3″ preservada).
- **MENORES**: typo "排除ada" → "já é descartado" (§3); §5 checklist ampliado
  (Lema L.3a); §6 lacunas atualizadas.
- **Confirmados pelo referee rodada 2**: Proposição L.1′ (correta); L.3″ (ok);
  J.0(a)/soundness real (ok); Claim 2 como rota paralela (ok); MENORES da v2
  aplicados.

## §7c. Registro de correções (v3→v4; rodada 3: REVISION micro, "com as 4 erratas: RECOMENDADO")

- **Errata 1 (MAJOR-1)**: seta invertida no rodapé 2 — "(⟸ `P≠NP`)" → **"(⟹ `P≠NP`)"**
  (o rodapé diz `¬2.1 ⟹ P≠NP`; logo 2.1 falha ⟹ `P≠NP`).
- **Errata 2 (MAJOR-1)**: rótulo trocado — "(2)+(3) = convenção forte" era errado
  ((2) **é** a existência do falsificador; a convenção é fechamento+(3), com (1)
  entregando (8)) ⟹ reescrito como **"(1)+(2)+(3) mutuamente inconsistentes via (8)"**;
  também `i_0` = o do **passo (5) que invoca (7)** (nit do referee).
- **Errata 3 (MENORES)**: §0 item 2 corrigido — "`δ_N` embute `m`; … todos de tamanho
  não-padrão" (contradizia o §3 corrigido) → carregador correto (`τ_N`/`¬φ` ⊇ bits de
  `α`, `≥ |α|` não-padrão via Lema L.3a); §5: **linha 4b** do Lema L.3a efetivamente
  adicionada (§7b afirmava "ampliado" antes de a linha existir).
- **Confirmados pela rodada 3**: Lema L.3a **correto** (testemunha limitada —
  `y < 2^{|α_i|}`, `|α_i|` padrão ⟹ falsificador real; `σ*` padrão, `m` padrão ⟹
  `σ*∈M_0`); carregador corrigido; reescopo de L.3′; dicotomia honesta; CJK limpo
  (só a citação do typo no log).

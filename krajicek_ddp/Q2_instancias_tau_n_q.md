# Q2 — Instâncias `(τ_n, q)` para o Teorema Q: full-range (com a correção de Gödel II), Σ₁ e o residual

> Frente Q2, **v3 — v2 corrigida pela rodada 2** (`Q2_instancias_referee.md`:
> NÃO RECOMENDADO; os 7 fatais da v1 auditados como corrigidos; FATAL-1/r2 =
> equivalência falsa §4 → **patch de v3** + MINOR-1..7), 11 Out 2026. Marcação: **(A)** = fonte; **(P)** =
> próprio; **(C)** = residual; **(R)** = retraído. Contexto: `27_TEOREMA_Q_...md`
> ((Q) e corolário verbatim), `27_MATHOVERFLOW_PERGUNTA.md` (rascunho MO — não
> publicar sem confirmação), `INDICE.md` (item congelado "(τ_n,q) concretas").
> Referências: **[Bus97]** Buss, *Handbook of Proof Theory* ch. 2 (verificação
> poli de provas EF em `IΔ₀+exp`/PA); **[K97]**/[K19] Krajíček, *Proof
> Complexity* cap. 2 (sonoridade/verificação); tradução de Cook/Buss para Σ₁/Π₁
> (**correção**: τ(φ) tautológica ⟺ φ verdadeira, no range adequado).

## §0. Missão e veredito sumário (v2)

1. **Q2.1 (decidido, enunciado corrigido) (P)+(A)**: **(Q) full-range com
   `τ_n(Con(T)) ∈ TAUT` para algum n é impossível** para `T` r.e., consistente,
   `T ⊇ Q` (Gödel II explícito — FATAL-1 corrigido) e `P` **completo** (FATAL-7:
   "sonoro" era hipótese morta — removida). **Mas** — correção do C2 da v1
   (FATAL-7): existem instâncias full-range **computáveis não-degeneradas**
   (exemplo canônico §2.2) — o que Q2.1 prova é só `τ_n(Con T) ∉ TAUT`; tais
   instâncias **transfere trivialmente** (q = n). O item congelado não morre no
   full-range — ele **perde a motivação**: ranges restringidos são os
   candidatos a transferir **não-trivialmente** (heurística **(C)**).
2. **Q2.2 (proposta corrigida) (P)**: **(Q)|_{Σ₁}** com `τ_n` **total** (⊥
   fora do range; cutoff de testemunha `n^{O(1)}` — FATAL-2), tamanho honesto
   `|τ_n(φ)| = 2^{p(n)}` (**não** `n^{O(1)}` — FATAL-3), verificação/sonoridade
   **citadas** [Bus97]/[K19] (MINOR-1), ponte como **implicação única**
   `PA ⊢ τ(φ)→φ` (MINOR-2). Vale `(Q)|_{Σ₁}` com `q(n,m) = (n·m)^c`.
3. **Q2.2′ (corolário com hipótese necessária) (P)**: a hipótese primária é
   **`τ_n(φ_n) ∈ TAUT`** (patch v3 — a v2 escrevia uma equivalência **falsa**,
   FATAL-1/r2: testemunha curta sozinha não basta se `⌢φ_n⌝ > n`, pois o
   cutoff dá `τ_n(φ_n)=⊥`; a decomposição correta é
   `τ_n(φ_n) ∈ TAUT ⟺ ⌢φ_n⌝ ≤ n ∧ ∃w(|w|≤n^{c₀} ∧ θ(w))`). Sem a hipótese,
   **três modalidades** de não-contente, todas declaradas (§4): (1) cutoff de
   Gödel (`⌢φ_n⌝>n` ⟹ ⊥); (2) testemunha longa (disjunctos não-tautológicos);
   (3) bound trivial `m ≥ |τ_n(φ_n)| = 2^{p(n)}`.
4. **Q2.3 (sanity check corrigido) (P)**: `τ` = identidade **sintática** sobre
   fórmulas proposicionais (computável — FATAL-5); transfere zero (sem fonte
   aritmética) — explica por que "Q sozinho" não basta.
5. **Q2.4 (residual, mecanismo corrigido) (C)**: PH/Goodstein violam a
   **provabilidade** (independência) — **não** a ponte (que vale para todo φ)
   (FATAL-6); contagem não dá limites **superpolinomiais** para PA em Σ₁
   (corrigido). Rota mais promessora: versões `IΣ_k` de Q2.2.

## §1. (Q) — recap verbatim (`27 §1.1–1.2`)

`(Q)`: ∀n∀φ∀m [π é P-prova de `τ_n(φ)` ∧ |π|=m ⟹ ∃π' (π' é T-prova de φ ∧
|π'|≤q(n,m))], `τ_n : Sent(T)→Form_prop` **uniforme** (computável — total),
`q` limitante. Corolário: `L(n)` ⟹ lower bound P se q poli em m. **(A)**:
sem instância concreta, nenhum limite inferior exponencial decorre da
incompletude (razão do congelamento).

## §2. Q2.1 — o teorema, corrigido, e o que ele realmente prova

> **Teorema Q2.1 (P)+(A: Gödel II).** Seja `T` r.e. **com `T ⊬ Con(T)`**
> (ex.: `T ⊇ Q` — condição suficiente, não equivalente), e
> `(τ_n,q)` satisfazendo **(Q) full-range**.
> Então **para todo n: `τ_n(Con(T)) ∉ TAUT`**.
>
> **Prova.** `Con(T)` é Π₁-verdadeira (T consistente) e `T ⊬ Con(T)` (Gödel II
> para `T ⊇ Q` r.e. consistente). Se `τ_n(Con T) ∈ TAUT` para algum n: por
> completude de `P`, ∃π: `P ⊢ τ_n(Con T)`; por (Q): `T ⊢ Con(T)` — **contradição
> com Gödel II**. ∎

### 2.1 Corolários corretos (substituem os C1–C3 da v1)

- **(C1′)** a tradução de Cook/Buss de Π₁-verdadeiras (que leva `Con(T)` a
  tautologia pela **correção da tradução**) **não** é instância full-range.
- **(C2′) (P) — correção do falso C2 da v1 (FATAL-7)**: existem instâncias
  full-range **computáveis e não-degeneradas**. Exemplo canônico: `τ_n(φ) := ⊤`
  sse `PA` tem prova de `φ` de tamanho ≤ `n` (decidível por busca finita),
  `⊥` caso contrário; `q(n,m) := n`. **(Q) vale**: dado π de `τ_n(φ)`: se
  `τ_n(φ)=⊤`, a busca encontra alguma prova PA de tamanho **≤ n** — é o π'
  exigido (|π'| ≤ n = q) ✓; se `⊥`, EF é sonoro ⟹ sem π (hipótese vazia) ✓.
  (Sanity check com Q2.1: `τ_n(Con PA)=⊥` para todo n, pois PA ⊬ Con PA.)
  **Mas transfere trivialmente**: `L(n) > n` força `τ_n(φ_n)=⊥` — não-tautologia
  — sem π — vacuidade. **Moral (C)**: o full-range não é "impossível" — é
  **inócuo** para os exemplos canônicos; a inexistência de instância full-range
  não-trivial é **heurística (C)**, não teorema.
- **(C3′)** o item congelado pede **range restrito** — a pergunta certa está
  em §3. **(R)**: a v1 dizia "só sobrevivem degeneradas" — falso; corrigido.

## §3. Q2.2 — a proposta Σ₁, corrigida

### 3.1 Definição corrigida de `τ_n` (resposta a FATAL-2/3)

`τ_n` **total**: `τ_n(φ) := ⊥` se `⌢φ⌝ > n`; senão, para `φ = Q̄x̄ ∃x θ(x)` (Σ₁;
`θ` limitada; `Q̄` limitados):

> `τ_n(φ) := (⋁_{w: |w| ≤ n^{c₀}} θ^{τ}(w))` — big-or sobre testemunhas de
> tamanho ≤ `n^{c₀}` (c₀ fixo; cutoff — **não** o ∃ ilimitado); e `τ_n(φ) := ⊥`
> para φ **não-Σ₁** com `⌢φ⌝ ≤ n` também (totalidade plena de `27 §1.1` —
> MINOR-1).

**Tamanho honesto (FATAL-3)**: `|τ_n(φ)| = 2^{p(n)}` (**exponencial** no pior
caso — o big-or tem `2^{n^{O(1)}}` disjunctos). A v1 pedia `n^{O(1)}`: **falso**
— retractado; o teste denunciador (famílias triviais de tempos de parada
transferirem limite inferior exponencial "sensação inexistente") é **exatamente**
por `τ_n` não ser polinomial quando a testemunha é grande: nesse caso
`τ_n(φ_n)` **não é tautologia** (§4).

### 3.2 (Q)|_{Σ₁} vale (com predicado de range — MINOR-4)

> **(Q)|_{Σ₁}(τ,q)**: ∀n∀φ∀m [(Σ₁(φ) ∧ ⌢φ⌝ ≤ n ∧ π: `EF ⊢ τ_n(φ)` ∧ |π|=m)
> ⟹ ∃π' (`PA ⊢ φ` ∧ |π'| ≤ (n·m)^c)].

**Prova (sketch, fontes citadas).** Dado π: (1) `PA` verifica π — fato
computável com provas poli(m) ([Bus97] ch. 2; [K19] cap. 2) — `PA ⊢ "π é
derivação EF de τ_n(φ)"`; (2) sonoridade instanciada de EF (formalizável;
[Bus97]/[K19]; instanciação em numerais `π̄,φ̄` de custo O(m+n) por passo)
⟹ `PA ⊢ τ_n(φ)` é tautologia; (3) **ponte** — via o **lema de correção
limitada** (uniforme, poli): `PA ⊢ (eval(v,θ^{τ}(w))=1 → θ(w))` para cada
disjuncto — daí a implicação única `PA ⊢ τ_n(φ) → φ` (MINOR-2/3: "coincide
com o ∃" era falso; o passo (2)+(3) comprime este lema — explicitado aqui);
concatenação com sobre-custo `c`. Para φ **falso**: todo `θ(w)` falso ⟹
todo `θ^{τ}(w)` não-tautológico (o mesmo lema na direção semântica — correção
da tradução por disjuncto) ⟹ `τ_n(φ)` não-tautologia ⟹ sem π (hipótese
vazia). ∎

## §4. Q2.2′ — o corolário COM a hipótese necessária (resposta a FATAL-4)

> **Corolário Q2.2′ (P).** Seja `(φ_n)` Σ₁-verdadeira com **`τ_n(φ_n) ∈
> TAUT`** — hipótese primária (patch v3; decomposta:
> `τ_n(φ_n) ∈ TAUT ⟺ ⌢φ_n⌝ ≤ n ∧ ∃w(|w| ≤ n^{c₀} ∧ θ(w))` — **testemunha
> curta sozinha não basta**, FATAL-1/r2) — e com toda prova PA de comprimento
> `≥ L(n)`. Então toda prova EF de `τ_n(φ_n)` tem comprimento `m` com
> `(n·m)^c ≥ L(n)`, i.e. `m ≥ L(n)^{1/c}/n`.
>
> **Sem a hipótese, TRÊS modalidades de não-contente, todas declaradas**:
> (1) `⌢φ_n⌝ > n` ⟹ `τ_n(φ_n)=⊥` (cutoff de Gödel — a modalidade que a v2
> não declarava); (2) testemunha longa ⟹ todo disjuncto de tamanho ≤ n^{c₀} é
> não-tautológico ⟹
> `τ_n(φ_n)` não-tautologia — "toda prova EF ≥ …" é **vacuidade**; (3) bound
> `m ≥ |τ_n(φ_n)| = 2^{p(n)}` seria **trivial** (tamanho da fórmula). ∎

**Algebra** (aceita na rodada 1): `(n·m)^c ≥ L ⟹ m ≥ L^{1/c}/n` ✓.

## §5. Q2.3 — o sanity check (corrigido: FATAL-5)

`T := T_PV`; `P := EF`; `τ_n(φ) := φ` se φ é fórmula **proposicional sintática**
(computável — sem decidir TAUT), `⊥` caso contrário. φ proposicional é lida
como **sentença de `L_PV`** (ponte identidade declarada — MINOR-4). (Q) vale
com `q(n,m) := m^{O(1)}`: verificação de π em `T_PV` (parte universal + unrolling
de indução limitada — poli em m) + ponte trivial. **Não transfere**: não há
fonte aritmética `L(n)`. **Moral (P)**:
`(τ,q)` é metade daHipótese; a outra é a fonte — e §2 mostra que o full-range
só produz a metade um inócua.

## §6. Q2.4 — residual (mecanismo corrigido — FATAL-6)

- **(P) excluído, com razão corrigida**: (a) PH/Goodstein: classificação Π₂ ✓
  (aceito); **o que violam é a provabilidade de φ em PA** (independência) —
  **não** a ponte (a ponte `PA ⊢ τ(φ)→φ` vale para φ arbitrário — cada
  disjuncto limitado implica φ) — a v1 dizia "a ponte Σ_1 é o que elas
  violam": **falso, retractado**; (b) contagem: dá limites Ω(n)-tipo, **não
  superpolinomiais**, para PA em Σ₁ (a justificativa da v1 — "PA prova todas"
  — era non sequitur; retractada).
- **(C) o que pode existir**: famílias Σ₁-verdadeiras com testemunhas curtas
  (§4) e limites PA superpolinomiais — via **hierarquia de velocidade**
  (Krajíček, *Proof Complexity*; Krajíček–Pudlák) ou **fragmentos**: as versões
  `IΣ_k` de §3 (o sketch vale com `T := IΣ_k`, k fixo) — lower bounds para
  fragmentos são mais acessíveis. **Próximo passo**: revisar K19 caps. 9/17 e
  KP90; se achadas: primeiro limite inferior do projeto com `(τ,q)` concretos.

## §7. Escopo, conexões (atualizados)

1. **Q2.2**: `c` fixo; convenção de abertas: não usada (a ponte é para φ
   fechada Σ₁ — melhor que a v1). `τ_n` total — `27 §1.1` satisfeito.
2. **Q2.1 não toca o artigo** — é o `(τ_n,q)` do projeto (27); não confundir
   com Q1 da carta.
3. **MO**: rascunho mantido; adendo factual sugerido (full-range inócuo;
   range restrito é o candidato) — **publicar só com confirmação**.
4. **Lean** (`Core.lean` `TransferQ`): se Q2.2 for adotado, acrescentar
   `IsSigma1 φ` + `SmallWitness φ n` aos campos (2 linhas, futuro).

## §8. Checklist (honesto — status)

| # | Afirmação | Status | Onde |
|---|---|---|---|
| 1 | (Q)/corolário verbatim; predicado de range formal | (A)+(P) | §1, §3.2 |
| 2 | Q2.1: enunciado **com** `T ⊇ Q` (Gödel II); P completo (não "sonoro") | corrigido | §2 |
| 3 | (C2′): instância full-range computável com q=n; transfere trivialmente | (P) — corrige C2 v1 | §2.1 |
| 4 | `τ_n` total com cutoff; `|τ|=2^{p(n)}` honesto | (P) corr. FATAL-2/3 | §3.1 |
| 5 | verificação/sonoridade citadas [Bus97]/[K19]; ponte = implicação | (A)+(P) | §3.2 |
| 6 | Q2.2′: hipótese `τ_n(φ_n)∈TAUT` (patch v3); **três** modalidades de não-contente | corr. FATAL-1/r2 | §4 |
| 7 | τ sintática (computável) | corr. FATAL-5 | §5 |
| 8 | PH/Goodstein: independência (não ponte); contagem: só Ω(n) | corr. FATAL-6 | §6 |

## §9. Veredito e próximos passos (v2)

**Veredito (honesto)**: a v1 teve 7 fatais — **auditados como corrigidos** na
rodada 2; a v2 tinha **um** falso remanescente (equivalência "testemunha curta
⟺ tautologia" sem o cutoff de Gödel — FATAL-1/r2) — **corrigido no patch v3**
(hipótese primária `τ_n(φ_n) ∈ TAUT`, com as **três** modalidades de
não-contente declaradas) + os 7 menores da rodada 2. O que sobra: a instância
Σ₁ (§3) **corrigida e citada**; a fonte Σ₁ (§6) permanece **(C)** — o residual
real; a moral "full-range inócuo" é **(C)** (heurística, não teorema).

**Próximos passos:** (1) referee rodada 2 (foco: §3.2 — sonoridade instanciada
com sobre-custo poli está bem citada?; (C2′) — a instância canônica satisfaz
mesmo (Q) full-range?; §4 — equivalência "testemunha curta ⟺ τ autologia" está
correta?); (2) revisão K19/KP90 para a fonte Σ₁; (3) se achada: primeiro limite
inferior com `(τ,q)` concretos — só então submissão/MO.

**Lacunas honestas**: §3.2 sketch (fontes citadas, referee julga); fonte Σ₁
**(C)**; `c` não otimizado; MO em rascunho; v1 tinha 7 fatais — documentados e
corrigidos.

Referee rodada 1: `Q2_instancias_referee.md` (NÃO RECOMENDADO) — v2 responde.

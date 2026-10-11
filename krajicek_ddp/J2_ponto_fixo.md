# J2 — Ponto fixo para a multifunção de falsificadores (K-FP′) e o destino de J.6

> Frente K, **v3 (pós-referee — rodadas 1–2)**, 11 Out 2026.
> **Pendente de referee (v3 — guarda restaurada; referee antecipou RECOMENDADO).**
> Marcação: **(A)** = fonte; **(P)** = próprio; **(C)** =
> conjectura. Contexto: `J1_Qcompactness_M0.md` (Teorema K, (Hjoint), J.6, J.2′),
> `H1_colecao_refutacao.md` §1.1 (semente verbatim), `A_teoremas_exatos.md` (§1.0;
> L21–22; §1.12), `J2_referee.md` (REJECT v1; rota factível §7).

## §0. Missão e veredito sumário (v3 — referee RECOMENDADO)

Missão do usuário: *atacar J.6 num `M_0` concreto — modelo recursamente saturado de
`S`*. Resultados (v2, após a retração da v1 — §8):

1. **Teorema K-FP′ (corrigido, menor, real)**: para todo nome **padrão** `N` com
   `R(N) ⊆ m` (guarda — **automática só para `m` não-padrão**, o caso de aplicação;
   contraexemplo do referee para `m` padrão: `N=⟨1,1,1⟩`, `m=2`, code `7 ≥ m`), o
   **ponto fixo existe** em `M_0` (existencial interno; prova metateórica com
   **falsificadores indexados `g_i`** — escolha padrão, **sem** uniformização PV).
   Consequência: **`C_N ≡ ⊤` para nomes padrão nesse alcance** ⟹ `(Hjoint)` vale em
   **todo** `M_0 ⊨ T_S` para **famílias finitas-padrão** sem `¬φ` (construtor-joint
   `⋃_j`, §3) ⟹ **C.3 negativa nesse alcance**, independente do modelo.
2. **Retração da v1 (FATAL-1/2/3 do referee)**: a versão v1 (símbolo PV `Q` +
   correção universal) é **falsa** — instanciada em nomes **constantes** `N_i`, ela
   entrega `F(i) := Q(α,N_i,·)` com `∀i<m Fals(F(α,i),α_i)` — **a coleção proibida pelo
   Teorema K da própria J1** (§8 log). O referee matou K-FP com o Teorema K — o projeto
   se auditou.
3. **Veredito sobre r.s.: CONFIRMADO pelo referee** (§4): saturação recursativa realiza
   **tipos**, não existenciais `Σ^b_1` — a rota r.s. **não destrava** o residuo de J.6;
   o que destrava é a pergunta de **provabilidade** de §4.
4. **Casos restantes**: `¬φ` (pergunta de teoria, §4) e o caso **misto/adversarial** —
   `(C)`, honestamente delimitado (§3).

## §1. Semântica de `τ_N` — **NÃO DECIDIDA** (referee MAJOR-1/2 da v1)

A v1 adotou a leitura **R1** (quantificadores todos ligados; `a_s` placeholders; `τ_N`
independente de `v`). O referee **rejeitou R1** com três pressões: (i) sob R1, `τ_N`
fica **sem átomos livres**, tornando vazia a correção S1 do H1 (que pressupõe `a_s`
livres); (ii) R1 falsificaria a nota "Sentido" de H1 §1.1 e o passo (2) do no-G;
(iii) R1 é incompatível com o tamanho `poly(|α|)` de G2 §2.2. Sob a **alternativa**
(`a_s` carregam valores da atribuição a `α`; `q` é o falsificador ligado), `τ_N` passa
a depender de `v` — e aí "J.6-a: qualquer `v*`" **colapsa** e o caso adversarial
engole todo o alcance. **Estado: aberto — ponto de referee nº 1.** As consequências
§2–§3 estão formuladas para sobreviver **sob qualquer das duas leituras**, com a
ressalva explicitada (§2 nota, §3).

## §2. Teorema K-FP′ — o ponto fixo existe para nomes **padrão**

> **Notação (P).** `N` **padrão** := `N ∈ Names_M(p)` de tamanho padrão (suporte
> `B = sup(N)` finito-padrão, metateóricamente finito). `R(N) := {code(N,v) : v`
> atribuição interna`}` — padrão-finito para `N` padrão; e `R(N) ⊆ m` é **automática
> só quando `m` é não-padrão** (o caso do artigo) — **para `m` padrão é falsa**
> (referee: `N=⟨1,1,1⟩`, `m=2` ⟹ `code = 7 ≥ m`) ⟹ a guarda `R(N) ⊆ m` permanece
> **explícita** no teorema. `F(i) := {q : Fals(q,α_i)}`; `D_i := at(α_i) ∩ B` —
> par-a-par disjuntos por **(S2)**.

> **Teorema K-FP′ (P).** Para todo nome **padrão** `N` com **`R(N) ⊆ m`** (guarda
> explícita — ver Notação): `M_0 ⊨ ∃q* ( q*` codifica atribuição ∧
> `Fals(q*, (α)_{code(N,q*)}) )` — o **ponto fixo existe** em `M_0`.

**Prova (metateórica; sem uniformização PV — é o que a v1 fez de errado).**
1. `R(N)` é **padrão-finito** (valores de um circuito padrão). Para cada `i ∈ R(N)`:
   por **(S4)** instanciada em `i` (padrão — instanciação interna legítima), escolha
   **um** falsificador `g_i ∈ F(i)` — elemento de `M_0` (a escolha é sobre
   **padrão-muitos** índices — escolha metateórica finita; **sem coleção proibida**,
   que exigiria não-padrão-muitos).
2. `b` := o padrão em `B` com `b ↾ D_i := g_i ↾ D_i` para `i ∈ R(N)` (os `D_i` são
   **disjuntos** por (S2) — colagem sem conflito), `0` no resto de `B`. `b` é um
   objeto de dados padrão-finitos ⟹ **`b ∈ M_0`** (montagem finita — sem compreensão).
3. `i* := code(N, b)` — `< m` **por hipótese (a guarda `R(N) ⊆ m`)** — *não* por
   `N` padrão isoladamente (contraexemplo do referee para `m` padrão) ⟹ `i* ∈ R(N)`.
4. `q* := ` a fusão: `g_{i*}` em `at(α_{i*})`, `b` em `B ∖ at(α_{i*})`, `0` fora.
   **Bem-definido**: em `D_{i*} = B ∩ at(α_{i*})`, `b ↾ D_{i*} = g_{i*} ↾ D_{i*}` (passo 2,
   com o **mesmo** `g_{i*}` — sem circularidade: os `g_i` são fixados **antes** de `b`).
   `q* ∈ M_0` (dados padrão-finitos + um elemento de `M_0`) ✓.
5. Verificações: `code(N,q*) = code(N,b) = i*` (`N` lê só `B` ✓); `Fals(q*, α_{i*})` por
   **localidade** de `Fals` (lê só `at(α_{i*})`, onde `q* = g_{i*}` ∈ `F(i*)` ✓). ∎

> **Nota (sobrevivência frente à §1) (P).** K-FP′ prova o **existencial interno** (a
> disjunção de `τ_N` tem testemunha). A passagem "`τ_N`'s circuito avalia 1 (em todo
> `v`, ou no `v` relevante)" depende da leitura de §1: sob R1, `τ_N = 1` (constante);
> sob a alternativa, `τ_N(v)` pode exigir compatibilidade de `g_{i*}` com a parte-`a`
> de `v` — aí K-FP′ só garante o ponto fixo "para a atribuição certa". **Marcado.**

> **Retração (v1 → v2) — por que K-FP′ não é a v1 (P).** A v1 construía o ponto fixo
> por **símbolos PV uniformes** (`leastF`,`BuildPat`,`Merge`) com sentença-correção
> universal. **Falsa**: (FATAL-2) `leastF` busca sobre `2^{#átomos}` atribuições —
> **não** é PV (FNP-difícil; `|α| ≥ m` só polinomializa varreduras em `i<m`);
> (FATAL-1) ainda que fosse, instantiando nos nomes **constantes** `N_i` ela entregaria
> `F(i) := Q(α,N_i,…)` com `∀i<m Fals(F(i),α_i)` — **a coleção que o Teorema K (J1 §3)
> proíbe em todo `M_0 ⊨ (S2)+(S3)+(S4)`** — contradição; (FATAL-3) a guarda `(S4)` é
> `∀∃` — não prensifica para universal — fora de `T_PV`. **Lições**: escolha sobre
> padrão-muitos é inofensiva; uniformização não-padrão é exatamente o que K mata.

## §3. Consequências para (Hjoint) e C.3 (escopo rebaixado — MAJOR-3 da v1)

> **Proposição J.6-a′ (com construtor-joint; P).** Seja `L` uma **família finita-padrão**
> (externamente finita) de nomes **padrão** com `R(N_j) ⊆ m`, **sem `¬φ`**. Então `L`
> é satisfatível internamente em **todo** `M_0 ⊨ T_S`. **Prova (joint):** `B_joint :=
> ⋃_j sup(N_j)` e `R_joint := ⋃_j R(N_j)` — ambos **padrão-finitos**; os
> `D_i := at(α_i) ∩ B_joint` seguem disjuntos ((S2)); colar `b` sobre `B_joint` com os
> `g_i` (`i ∈ R_joint` — padrão-muitos ✓); para cada `j`: `i_j* := code(N_j, b) ∈
> R_joint ⊆ m` e `q_j* :=` fusão com `g_{i_j*}` (mesmo acordo em `D_{i_j*}`) ⟹
> ponto fixo para **cada** `j`. Sob R1: todos os `C_{N_j}` ≡ ⊤ (qualquer `v*`);
> sob a alternativa: o construtor-joint fecha **ambas as leituras** (referee MAJOR-4) —
> `v* := q† := ` a fusão comum (estendida pelos `g_i` sobre `at(α_{i_j*})` — `q†` ∈
> `M_0`, testemunha certa) serve de testemunha comum. Constantes-1 ✓.
> ⟹ **C.3 é negativa nesse alcance**, independente do modelo. *(Alcance: famílias
> finitas-padrão — para famílias internas com nomes não-padrões, §3 fronteira `(C)`.)*

> **Proposição J.6-b (ramo vazio; confirmada pelo referee) (P).** Para nome `N` com
> `R(N) ⊄ m`: `C_N` é satisfatível **vazamente** (existe `v` com `code(N,v) ≥ m`).

> **Fronteira honesta (C)** — permanece: (i) no ramo vazio (`R(N) ⊄ m`), nomes
> **padrão ou não**, com **compatibilidade conjunta** dos fibrados `≥ m` entre vários
> `N_j` (a v1 marcava corretamente: fibrados podem ser incompatíveis; a existência de
> par adversarial com (S2)+(S4) — **mesmo padrão** — é **(C)**); (ii) sob a alternativa de §1, o alcance de J.6-a′ recai sobre
> o construtor-joint (famílias finitas-padrão); (iii) índices **genéricos novos**
> `ν_G(N)` (lado `M[G]`): `R(N) ⊆ m` não os cobre — a transferência para `M[G]` usa a
> **maquinaria de forcing do artigo** (cofinalidade + preservação `Σ^b_1` dos
> universais), **não** K-FP′ — tratamento fora do escopo de J2 (MENOR-1 do referee:
> a menção anterior a "elementaridade `Σ^b_1`" era vaga para parâmetro novo).

## §4. `¬φ` e o destino da rota "modelo recursamente saturado" — **CONFIRMADO**

- **Caso (ii)** (subfamílias **com `¬φ`**) colapsa na pergunta de teoria:
  **`T_S ⊢ ∃r ¬φ(r)`?** — aberta (completude interna **retraída**, verbatim L21–22 **(A)**).
- **Veredito sobre r.s. (P) — confirmado pelo referee**: r.s. **realiza tipos recursivos
  sobre parâmetros**; as questões de J.6 são **existenciais `Σ^b_1` internos** — sua
  verdade é matéria de **provabilidade em `T_S`**, não de saturação (modelos r.s. podem
  satisfazê-los ou não). **A rota r.s. não destrava o residuo** — a rota que destrava é
  decidir a provabilidade de §4 (e, se independente, aí modelos concretos — ex. r.s.
  de `T_S + ∀rφ(r)`, se consistente — dariam o caso de não-colecção total).
- **Existência do `M_0` r.s.**: sob a consistência de `T_S` (KPT, **(A)**), modelo r.s.
  contável existe (teoria padrão) — irrelevante para o que foi decidido (alcance de
  J.6-a′ vale em **todo** modelo).

## §5. Certificados para humanos (checklist)

| # | Afirmação | Verificação | Onde |
|---|---|---|---|
| 1 | **Semântica de `τ_N`: ABERTA** (R1 vs alternativa) | referee nº 1 | §1 |
| 2 | (S2) disjunto; (S4) instanciável em índices padrão | verbatim | `A_teoremas_exatos.md` §1.12 |
| 3 | Escolha `g_i` sobre padrão-muitos ≠ coleção proibida (não-padrão-muitos) | 2 linhas | §2 passo 1; §8 |
| 4 | `b`, `q*` ∈ `M_0` por montagem de dados padrão-finitos (sem compreensão) | padrão | §2 passos 2,4 |
| 5 | Localidade de `Fals` | padrão | J1 §3 passo 1 |
| 6 | K-FP′ sobrevive sob qualquer leitura de §1 (com ressalva) | conferir | §2 Nota |
| 7 | `R(N) ⊆ m` **automática só para `m` não-padrão** (guarda explícita no teorema) | contraexemplo do referee | §2 Notação |
| 8 | Caso misto/adversarial: `(C)` | honestidade | §3 |
| 9 | r.s. não decide `Σ^b_1` | padrão | §4 |
| 10 | L21–22 (incompletude de pps em `T_PV`) | verbatim | `A_teoremas_exatos.md` L21–22 |
| 11 | `leastF` não é PV (FNP); K-FP v1 = coleção proibida | referee | §2 Retração; §8 |

## §6. Veredito e próximos passos

**Veredito (P):** J.6 está decidida **para famílias finitas-padrão de nomes com
`R(N)⊆m`, sem `¬φ`** (K-FP′ + construtor-joint: ponto fixo existe em todo modelo;
C.3 negativa nesse alcance); a **rota r.s. foi avaliada e
descartada** com razão confirmada pelo referee (tipos ≠ existenciais `Σ^b_1`); o
residuo é **duas perguntas delimitadas**: a semântica de `τ_N` (referee nº 1) e a
provabilidade de `∃r ¬φ(r)` em `T_S` (§4), mais o caso adversarial **(C)**.

**Próximos passos:** (1) referee hostile da v2 (foco: K-FP′ — escolha `g_i` e montagem
de `b`/`q*`; sobrevivência sob as duas leituras de §1; escopo rebaixado de §3);
(2) decidir §4 (`T_S` vs `∃r¬φ(r)`): a rota mais promissora — se `T_PV` prova a
completude **para a sentença `φ` só** (mais fraca que a completude geral — L21–22 não
a exclui!), então `T_S ⊢ ∃r¬φ(r)` e `(Hjoint)` fica **total** ⟹ **C.3 negativa inteira**;
(3) decidir a semântica de `τ_N` (§1) consultando G2 §2.2 (tamanho `poly(|α|)`) e o
passo (2) do no-G; (4) com K (J1) + K-FP′ + J.2′, montar a **nota editorial a Krajíček**.

**Lacunas honestas:** §1 em aberto (as leituras divergem no alcance); K-FP′ cobre só
nomes **padrão**; o caso misto/adversarial é **(C)**; §4 é pergunta única, não decisão;
a completude "para `φ` só" em (2) é **(C)** plausível mas não verificada.

## §7. Autoria e método

Análise do orquestrador; referee hostile (`J2_referee.md`) — **REJECT da v1** com 3
FATAIS resolvidos por retração + K-FP′ (a "rota factível" do próprio referee). O
episódio é o melhor exemplo do protocolo do projeto: **o Teorema K da J1 matou o
K-FP da v1** (uniformização PV = coleção proibida) — auditoria cruzada entre frentes.

## §8. Registro de correções (v1→v2; REJECT: 3 FATAL, 4 MAIOR)

- **FATAL-1 (K-FP v1 contradiz o Teorema K)**: instantes em nomes **constantes** `N_i`
  davam a coleção proibida ⟹ **K-FP v1 retraído**; substituído por K-FP′ (existencial
  interno; escolha padrão; sem símbolo PV uniforme).
- **FATAL-2 (`leastF` não é PV — FNP)**: a busca do menor falsificador explora
  `2^{#átomos}` atribuições; `|α|≥m` só polinomializa varreduras em `i<m`. Retirado.
- **FATAL-3 (guarda `(S4)` é `∀∃` — não universal)**: irrelevante em K-FP′ (a prova é
  metateórica de um existencial interno em `M_0` — não usa sentença-correção universal).
- **MAIOR-1/2 (R1 não decidida)**: §1 reescrita como **aberta**, com as três pressões
  do referee registradas e a Nota de sobrevivência de K-FP′.
- **MAIOR-3 (superestimação do alcance)**: "C.3 negativa em quase todo alcance" → só
  "famílias sem `¬φ` com nomes **padrão**" (J.6-a′).
- **MAIOR-4 (`ν_G(N)` fora de `R(N)⊆m`)**: nota em §3(iii) — transferência a `M[G]` é
  por elementaridade `Σ^b_1`, não por K-FP′.
- **Confirmados pelo referee**: `BuildPat`/`Merge` PV; o padrão do acordo em `D_{i*}` +
  localidade (condicionado); ramo vazio de J.6-b; fronteira `(C)` e o salto
  "(Hjoint) falsa ⇏ C.3 positiva"; **veredito sobre r.s.** (tipos, não existenciais
  `Σ^b_1`).

**v2→v3 (referee da v2: REVISION — 2 MAIOR de escopo; "com a guarda restaurada,
RECOMENDADO"):**
- **MAJOR-1**: "`R(N)⊆m` automática para `N` padrão" **falsa** para `m` padrão
  (contraexemplo `N=⟨1,1,1⟩`, `m=2`, code `7`) ⟹ **guarda `R(N) ⊆ m` restaurada** no
  Teorema, Notação, K-FP′ passo 3, §0 ato 1 e checklist nº 7 ("automática só para `m`
  não-padrão" — o caso do artigo).
- **MAJOR-4**: J.6-a′ reescrita com **construtor-joint** (`B_joint := ⋃_j sup(N_j)`,
  `R_joint := ⋃_j R(N_j)`, ambos padrão-finitos; colagem sobre `D_i` disjuntos ((S2));
  ponto fixo para cada `j` com os `g_i` pré-fixados) — **fecha sob ambas as leituras**
  de §1 e restringe o alcance a **famílias finitas-padrão** (o caso com nomes
  não-padrões permanece na fronteira `(C)`).
- **MENORES**: §3(iii) reescrita (transferência a `M[G]` = maquinaria de forcing do
  artigo, fora do escopo de J2 — a menção a "elementaridade `Σ^b_1`" era vaga para
  parâmetro novo `ν_G(N)`); Notação de `R(N)` explicitada.

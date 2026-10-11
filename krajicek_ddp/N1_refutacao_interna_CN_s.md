# N — A refutação interna de `{C_{N_s}}` reduz-se a `Taut(α)` interna

> Frente N, **v3**, 11 Out 2026 — **após referee hostile rodadas 1–2** (`N1_referee.md`:
> r1 NÃO RECOMENDADO → r2 **RECOMENDADO** com 4 correções locais, aqui aplicadas:
> NOVO-1 π-compressão reescrita como **relação aberta**; NOVO-2 suporte da direção
> (⇒); MAJOR-3 escopo em N.1′; M-2 verdade-vs-sonoridade; nits).
> Marcação: **(A)** = fonte; **(P)** = próprio; **(C)** = conjectura. Contexto:
> `M_canto_adversarial.md` (M.1, M.2, M.4 — o aberto), `F2_versao_finita.md` §0
> ((S1)–(S4) verbatim; `(S3)`: `π : P ⊢ α`; `Ref_P ∈ T_PV` L26–27), `G2_semente_Fsent.md`
> (semântica de `τ_N`), `L1_phi_insatisfativel.md` (L.3″/L.4 — o caso `¬φ`),
> `A_teoremas_exatos.md` (L21–22; L341; §1.2 `m ≤ |α|`; §1.6), `H1_colecao_refutacao.md`
> (§1.1, §1.3 — semente; convenção de prova EF).

## §0. Missão e veredito sumário

Aberto herdado de `M` (M.4): `{C_{N_s}}` é internamente insatisfatível em todo
`M_0 ⊨ T_S` (M.2), sem refutação **genuína** (L.3′); falta a refutação **interna** —
uma prova EF em `M_0` de `σ_s := ¬C_{N_s} = δ_{N_s} ∧ ¬τ_{N_s}` (sentença **verdadeira**
em `M_0` por M.2 — cuja cadeia é `σ_s` verdadeira ⟸ M.2 ⟸ M.1 ⟸ Teorema K (J1);
**registrada, sem circularidade na prova de N.1** — referee conferiu). Resultado:

1. **Teorema N.1 (redução exata) (P)** — *escopo: semântica de `τ_N` em que M.2
   vale, i.e. R1 **ou** alternativa com `q` **total** (§5.1)*: em `M_0`,
   **`M_0 ⊨ EF ⊢ σ_s` ⟺ `M_0 ⊨ EF ⊢ Taut(α)`** — onde **`Taut(α) := ⋀_{v}` (eval(v,α)=1)**
   é a **sentença fechada** (big-and interno sobre as `2^{at(α)}` atribuições; tamanho
   `≥ 2^{at(α)}`). I.e., **`{C_{N_s}}` tem refutação EF interna ⟺ a tautologia fechada
   de `α` tem prova EF interna em `M_0`** — *apesar de* **(S3)** garantir uma **prova
   de `α` (fórmula aberta) em `P`**.
2. **Dicotomia N.2 (P)**: `EF ⊢_{M_0} Taut(α)` → refutação interna **existe**;
   `EF ⊬_{M_0} Taut(α)` **((C1′))** → **sem** refutação interna — 2ª instância
   genuína de não-compactude, sombra interna do aviso L21–22 (o mesmo fenômeno que
   L.4 exemplificou com `φ`).
3. **Honestidade (P)**: (C1′) é **(C)** — ambos os chifres são consistentes com
   `T_S` ao que tudo indica, mas **nenhum foi decidido** (§4 N.3). A leitura
   "compressão de `π` (P→EF)" é **interpretativa**, e a relação entre ela e
   `EF ⊢ Taut(α)` é **aberta (R-β, status indeterminado)** — **não** afirmamos
   estritude em nenhuma direção: `Taut(α)`-prova ⟹ `α`-prova é **plausível**
   (carregador `e_T`, (C)); `α`-prova ⟹ `Taut(α)`-prova é **exatamente a bloqueada**
   pela indisponibilidade de coleção sharply-bounded (`G2 §2.3`) — logo a
   implicação não é demonstrável em nenhuma das duas direções com o que temos.

## §1. Setup recolhido (verbatim das fontes)

`M_0 ⊨ T_S`, `T_S = T_PV + (S1)–(S4)` **(A, F2 §0 L30–34)**: (S1) axiomas de `T_PV`;
**(S2)** `α = ⋁̇_{i<m} α_i` disjunção **disjunta**; **(S3) `π : P ⊢ α`** (`π ∈ M_0`
derivação **P** de `α` — **fórmula aberta**, `|α|` bits); **(S4)** `∀i<m (¬α_i) ∈ SAT`.
`α` **não-padrão** (L.3a); `m` **não-padrão** (M.0); **`m ≤ |α|` (A✔, `A §1.2` —
conferido pelo referee)**. `Ref_P ∈ T_PV` (`F2` L26–27; `A` L341) ⟹ **EF sonoro em
`M_0`** (usado em N.4). `m ≥ 1` (senão `α = ⊥` e (S3) contradiz a sonoridade de `P`).
Seletor (M.2): `s(v)` = "menor `i<m` com `¬Fals(v,α_i)`", PV-total, **default `0`**;
`N_s = ⟨bits de s⟩`; `code(N_s,v) = s(v)` **pela construção dos circuitos do nome**
(sob R1/`q`-total — §5.1); `τ_{N_s} = ⋁_q (q` cod. atribuição ∧ `Fals(q,(α)_{code(N_s,q)}))`
— big-or sobre `q` ⟹ tamanho `≥ 2^{at(α)}` (referee, FATAL-1); `δ_{N_s}` ≡ 1;
`σ_s := δ_{N_s} ∧ ¬τ_{N_s}` verdadeira em `M_0`. *(Convenção `Fals(q,α_i)` = `α_i`
avaliada 0 sob `q`; `¬Fals` = `q` **satisfaz** `α_i` — alinhada M.1/M.2.)*

## §2. Fatos locais do seletor (N.0) — tamanhos corrigidos

> **Lema N.0 (P).** Para **`v` fixo** (atribuição de tamanho `≤ poly(|α|)`), os
> fatos **(a)** `s(v) < m`; **(b)** **ou** o laço retornou índice que passou no
> check — `¬Fals(v, α_{s(v)})` — **ou** o default disparou — `∀i<m Fals(v,α_i)`;
> **(c)** `code(N_s,v) = s(v)` — são prováveis em EF com derivações de tamanho
> **`poly(|α|, |v|)`**.
>
> **Prova (P).** O laço roda `i = 0,…,m−1`; `m ≤ |α|` (A✔) é **constante**
> (não-padrão, fixo) ⟹ unrolling: `m` passos × `poly` locais = `poly(|α|)`; cada
> passo é implicação proposicional entre avaliações de circuitos. ∎
>
> **Contabilidade honesta (referee MAIOR-1)**: as versões **fechadas** ("para todo
> `v`") do big-and têm tamanho `≥ 2^{at(α)}` — **não** `poly(|α|)`; `2^k > k^c`
> vale **internamente** em `M_0 ⊨ T_PV` (transferência de sentenças universais
> verdadeiras). O unrolling cobre só a dimensão `i<m`.

## §3. O Teorema de redução

> **Teorema N.1 (P).** Em qualquer `M_0 ⊨ T_S` (**sob a semântica de `τ_N` em que
> M.2 vale — R1 ou alternativa `q`-total**): **`M_0 ⊨ EF ⊢ σ_s` ⟺ `M_0 ⊨ EF ⊢ Taut(α)`**,
> com `Taut(α)` a **sentença fechada** `⋀_{v}(eval(v,α)=1)`. *(Equivalências
> intermediárias: `Taut(α) ⟺` sentença interna de M.1 `∀v∃i<m ¬Fals(v,α_i)` —
> identidades proposicionais do big-or, ambas fechadas; e `σ_s ⟺` [N.0, por-`v`] ∧
> [sentença interna de M.1].)*

**Prova (P).** *(Ambas as direções operam com **sentenças fechadas**; concatenação
de derivações de tamanho `≤ t` é `poly(t)`-computável — com os tamanhos corretos
`≥ 2^{at(α)}` do lado de `σ_s` — referee MAJOR-1 corrigido.)*
**(⇐)** `e` = prova EF de `Taut(α)`. Por N.0(b), dado `v`: o default (`∀i Fals(v,α_i)`)
contradiz a instância `∃i<m ¬Fals(v,α_i)` de `Taut(α)` em `v` (identidade
proposicional); logo o check passou em `s(v)` e `¬Fals(v,α_{s(v)})`. Logo
`⋀_q (q` cod → `¬Fals(q,α_{s(q)}))` — `¬τ_{N_s}` (sob R1/`q`-total); com `δ_{N_s}`
(N.0(a)) obtém-se `σ_s`. Concatenação em `M_0` é p-tempo nos tamanhos ⟹ prova EF
de `σ_s` ∈ `M_0` ✓.
**(⇒)** `e` = prova EF de `σ_s`. Por N.0(a) e **`e` (a instância de `¬τ_{N_s}` que
`e` encerra, ligada por N.0(c) `code=s`)**: para cada `v`, `¬Fals(v,α_{s(v)})` ∧
`s(v)<m` ⟹ `eval(v,α_{s(v)})=1` ⟹ `eval(v,α)=1` (identidade do big-or). *(Suporte
corrigido, referee NOVO-2: no **default**, `Fals(v,α_0)` valeria — logo
`¬Fals(v,α_{s(v)})` vem de `e` + N.0(c), **não** "da definição do seletor".)* A
derivação de `Taut(α)` = `e` + N.0 + essas identidades — o "para cada `v`" é o
**big-and fechado** da sentença-destino (as provas por-`v` de N.0 têm tamanho
`poly`; a derivação fechada resultante satisfaz `2^{at(α)} ≤ |τ_{N_s}| ≤ |e|`)
✓. ∎

> **Corolário N.1′ (a pergunta em uma linha, com o escopo exato) (P)** *(escopo:
> R1/`q`-total, como N.1)*. `{C_{N_s}}` tem refutação EF interna em `M_0` ⟺
> **`Taut(α)` (fechada) tem prova EF interna em `M_0`**. *(Leitura: **(S3)** dá
> `π : P ⊢ α` — `α` **aberta**; a pergunta é se a tautologia correspondente tem
> prova EF interna. A relação "comprimir `π` (aberta) para EF" ↔ `EF ⊢ Taut(α)`
> é **aberta** — residual **R-β**, status indeterminado (§0.3, §4 R-β);
> **não** é equivalência nem estritude.)*

## §4. A dicotomia e o que cada chifre entrega

> **Dicotomia N.2 (P)** *(escopo R1/`q`-total)*. Em todo `M_0 ⊨ T_S`, um dos dois:
> **(α)** `M_0 ⊨ EF ⊢ Taut(α)`: `{C_{N_s}}` **tem** refutação EF interna — a 2ª
> fonte de não-compactude de M.4 **colapsa no plano interno**; a não-compactude
> genuína restante é a de `¬φ` sob **Condition 1 (A)** (L.3″) — *escopo restrito ao
> que L.3″ efetivamente fecha*.
> **(β)** `M_0 ⊨ EF ⊬ Taut(α)` — **hipótese (C1′) (C)**: `{C_{N_s}}` **não tem**
> refutação interna — 2ª instância genuína — e (C1′) é a **sombra interna** do
> aviso L21–22 ("pps pode ser incompleto **num modelo de `T_PV`**") aplicada à
> tautologia de `α`. *(M.4 marcava "plausivelmente não-provável"; N.1 refina: o que
> é plausível é exatamente (C1′).)*

> **Proposição N.3 (honestidade de escopo) (C).** Ambos os chifres são consistentes
> com `T_S` ao que tudo indica, mas **não construímos** `M_0` com (C1′) nem provamos
> `T_S ⊨ EF ⊢ Taut(α)`. Residuais: **(R-α)** construir `M_0 ⊨ T_S` com (C1′)
> (rota: instância do aviso L21–22 aplicada a `Taut(α)` — omitting types; **ultrapoderes
> não servem**: `α`/`C_{N_s}` são **não-padrões**, caso **excluído** por `I1 A.7`;
> a barreira de ultrapoderes é `I1 B.2` e a transferência Łoś `I1 C.1` — **citação
> corrigida, referee MAIOR-2**); **(R-β)** comprimir `π` (aberta) para EF —
> **(C)**; a **relação R-β ↔ `EF ⊢ Taut(α)` é aberta, status indeterminado**
> (§0.3; sem estritude em nenhuma direção — referee NOVO-1) (`G2 §2.3`: a coleção
> sharply-bounded envolvida é indisponível; sob `NP=coNP` a compressão **externa**
> existe, mas a interna em `M_0` segue aberta — `G2 §2.5.1`). **I1 C.1 permanece
> intocado** (venue viva).

> **N.4 (contraste com `¬φ`) (P)+(A).** Para `{¬φ}` a hipótese que fecha o plano
> interno é **Condition 1 (A)** (do artigo). Para `{C_{N_s}}` a hipótese análoga
> **(C1′)** é **nossa e aberta**. *(Papéis separados, referee M-2: a **verdade**
> de `σ_s` vem de **M.2**; a **sonoridade** (`Ref_EF ∈ T_PV` — `G2 §2.3`; `I1 A.5`)
> só dá "`σ_s` **falsa** não é provável" — juntas, os chifres de N.2 são mutuamente
> exclusivos e exaustivos.)*

## §5. Ressalvas (herdadas, novas e de referee)

1. **Semântica de `τ_N`**: toda a frente presume **R1 ou `q`-total** (onde M.2 vale
   e `code(N_s,q)=s(q)`). Sob `q`-**par**, o trap M.2 pode abrir, `σ_s` pode ser
   **falsa** e a equivalência de N.1 não se aplica (pergunta Q1 da carta já enviada) —
   **escopo em §0.1, N.1, N.1′, N.2, §7** (em N.1′ acrescentado na v3, referee MAJOR-3).
2. **Convenção `Fals`** (`eval=0` sob falsificação) — alinhada M.1/M.2.
3. **"Prova EF em `M_0`"**: convenção do projeto (**fonte exata: `H1 §1.3`**;
   corrigida, referee menor) — derivação EF interna; sentenças com quantificadores
   internos (big-and/or) como circuitos.
4. **Tamanhos**: `σ_s` e `Taut(α)` têm tamanho `≥ 2^{at(α)}`; o unrolling de N.0
   cobre só a dimensão `i<m` (`m ≤ |α|`, A✔). "Concatenação p-tempo" vale **nos
   tamanhos**, não em `|α|` (MAJOR-1 corrigido).
5. **Cadeia de dependência** de "σ_s verdadeira": M.2 ⟸ M.1 ⟸ Teorema K (J1) —
   **sem circularidade** com N.1 (referee conferiu; registrado).
6. **`P` extensão de `EF`**: `P ⊢ α` não dá `EF ⊢ α`; **"não simulável" é (C)**,
   não (A) — `A §1.6` ("every pps can be p-simulated by a strong one") não sustenta
   não-simulabilidade (**MAIOR-4 corrigido**); a leitura "compressão de π" é
   interpretativa, e sua relação com `EF ⊢ Taut(α)` é **aberta** (R-β;
   §0.3 — sem estritude).
7. **Provas de `σ_s`**, se existirem, têm comprimento **não-padrão** (`N_s` é
   não-padrão) — legítimo, só registrar.

## §6. Certificados para humanos (checklist v3)

| # | Afirmação | Verificação | Onde |
|---|---|---|---|
| 1 | (S1)–(S4), (S3)=`π:P⊢α` (**aberta**) | verbatim (referee) | `F2` §0 L30–34 |
| 2 | `Ref_P ∈ T_PV` ⟹ EF sonoro em `M_0` | verbatim | `F2` L26–27; `A` L341 |
| 3 | `m ≤ \|α\|` | (A✔) referee | `A` §1.2 |
| 4 | N.0 por-`v`: `poly(\\|α\\|,\\|v\\|)`; fechado `≥ 2^{at(α)}` | MAJOR-1 corrigido | §2 |
| 5 | N.1 (⇐): default contradiz instância de `Taut(v)` | 6 linhas | §3 |
| 6 | N.1 (⇒): big-or identity; big-and fechado do destino | 2 linhas | §3 |
| 7 | Relação R-β ↔ `EF⊢Taut(α)` **indeterminada** | (C); NOVO-1 | §0.3, §3, §4 |
| 8 | N.2 chifres exclusivos/exaustivos + sonoridade | padrão | §4 N.4 |
| 9 | Ultrapoderes: `I1 A.7` (não-padrão excluído), `B.2`, `C.1` | MAIOR-2 corrigido | §4 R-α |
| 10 | Escopo R1/`q`-total em §0.1, N.1, **N.1′**, N.2, §5.1, §7 | MAJOR-3 fechado (v3) | §5.1 |
| 11 | Cadeia M.2⟸M.1⟸K sem circularidade | referee | §0.1, §5.5 |
| 12 | "P não simulável" re-marcado (C) | MAIOR-4 corrigido | §5.6 |

## §7. Veredito e próximos passos

**Veredito (P, v3):** o aberto de M.4 está **reduzido com exatidão** (escopo
R1/`q`-total): refutação interna de `{C_{N_s}}` ⟺ **`Taut(α)` fechada tem prova EF
interna em `M_0`** — com dicotomia honesta: (α) refutável internamente (a
não-compactude genuína restante no plano interno é a de `¬φ` sob Condition 1, no
escopo em que L.3″ a fecha) ou (β) **(C1′)** — 2ª instância genuína, sombra de
L21–22. Decisão plena = residuais R-α (construir `M_0` com (C1′)) ou R-β
(comprimir `π`; relação a `EF⊢Taut(α)` indeterminada); ambos abertos e marcados.
A leitura "π comprime-se" ficou **interpretativa**, com relação **aberta** à
redução, não corolário (FATAL-1 + NOVO-1 corrigidos).

**Próximos passos:** (1) ~~referee rodada 2~~ **feito** — RECOMENDADO (correções
aplicadas nesta v3); (2) registrar o desfecho na resposta da carta quando Krajíček
responder (Q1 → se `q` total, N.1 firme); (3) residual R-α: instância L21–22
aplicada a `Taut(α)` via omitting types (ultrapoder excluído — `I1 A.7`/`B.2`);
(4) consolidar a frente N no `RELATORIO_CONSOLIDADO.md` (§6/§7) e no `INDICE.md`.

**Lacunas honestas:** N.3 **(C)** (nenhum chifre decidido em ZFC para todo modelo);
`q`-total herdada (Q1); "prova EF" pela convenção do projeto (`H1 §1.3`) — pode
divergir da convenção do autor; omiting types não construído.

## §8. Autoria, referee e método

Análise do orquestrador (frente N). **Rodada 1** (`N1_referee.md`): NÃO RECOMENDADO
— FATAL-1 (`Taut(α)` fechada vs `α` aberta; trocada em §0.1/N.1′/N.2/§7), MAIOR-1
(tamanho N.0), MAIOR-2 (citação I1), MAIOR-3 (escopo `q`-total), MAIOR-4 (gloss
π + marcação (A)); 5 menores. **v2** corrige todos. **Rodada 2** (mesma sessão do
referee): **RECOMENDADO** com 4 correções locais — NOVO-1 (π-compressão: estritude
não provada, reescrita como relação **aberta**), NOVO-2 (suporte da direção (⇒):
`e` + N.0(c), não "definição do seletor"), MAIOR-3-parcial (escopo em N.1′),
M-2 (verdade ⟸ M.2 ≠ sonoridade) — **aplicadas nesta v3**, com o teorema central,
a dicotomia e a cadeia M.2⟸M.1⟸K declarados "matematicamente de pé" pelo referee.
A frente fecha o último residual
J.6 na forma de pergunta interna decidida por redução: o Teorema K (J1) deu o
adversarial (M.2); aqui a pergunta dele (refutação interna) colapsa numa pergunta
de **prova interna da tautologia de `α`** — a mesma tensão EF-vs-P do artigo, por
dentro.

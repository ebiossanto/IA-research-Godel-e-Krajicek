# NOTA EDITORIAL a Krajíček — rascunho consolidado (v4)

> **Status: RASCUNHO para revisão do usuário — não enviar sem aprovação.** 11 Out 2026.
> **v4 (referee rodadas 1–3: todos os CRÍTICOS/MAIOR aplicados; referee pre-comprometeu
> APROVADO após as correções desta versão — ver §6).** Destinatário:
> Jan Krajíček (arXiv:2506.20221v5 / LMCS 22(2:14)2026). Marcação:
> **(A)** = fonte/artigo; **(P)** = resultado próprio da equipe (sujeito a crítica —
> é o que pedimos ao autor); **(C)** = conjectura. Fontes internas (mesma pasta):
> `F1`, `G2`, `G1`, `H1`, `I1`, `J1`, `J2`, `L1`, `A_teoremas_exatos.md`,
> `G_CONTEXTO_FORCING.md`.

## §0. Propósito

Reunir, em texto único e curto, tudo que nossa verificação do artigo produziu,
para envio ao autor: (i) a **errata** da lacuna no **Teorema 4** (v4; = **Teorema 3**
em v5/LMCS); (ii) os **obstáculos estruturais** a reparos naturais (nossos teoremas);
(iii) o que **sobrevive** e propomos como correção; (iv) **perguntas** ao autor.
Tom: colaborativo — a lacuna é local e pedimos ao autor que nos mostre o argumento
oculto, se houver.

## §1. A errata (A) — lacuna no Teorema 4 (v4) / Teorema 3 (v5/LMCS)

**Local exato.** §3, item (5) da prova (presente em v4, v5 e LMCS; conferido em
`G_CONTEXTO_FORCING.md` §1.1): *"But by (7) i_o is also already in M∗"*.

**Por que não segue.** `(7)` diz `Log(M*) = Log(M′)`. `Log(M) = {|m| : m ∈ M}` registra
apenas **medidas**; um índice novo `j < m` tem `|j| ≤ |m|` — medida **já** em `Log(M)`.
Logo `(7)` é compatível com `M′` contendo índices abaixo de `m` fora de `M∗`.
`Log` guarda comprimentos, não elementos.

**Reparos mínimos (A)+(P) — e por que dois deles já caem.** (a) exigir `M′ ∩ m = M ∩ m`
como condição de domínio; (b) exigir `(8)` diretamente em `M′`; (c) um argumento oculto
— ex.: uma featura do forçamento de [7, Thm 9.4.2] que **também** impede elementos novos
de medida velha abaixo de `m` **(C→P — conferência página-a-página do [7] pendente)**.
*Nota: (a) é refutado por `G1` Thm 4.3 e (b) por `G2` Thm 2.1(b) — ambos impossíveis
junto de (ii); a rota **por coleção** de falsificadores (a forma natural de fechar a
conta) é a que `J1` K mata. **(c) é o único vivo.***

**Nova evidência (P) — o `i_0` é pinçado.** Nosso Teorema L.1 (`T_PV+(S4) ⊢ ∀rφ(r)`;
todo `M ⊨ T_PV+(S4)` com `α,m` nomeados — §2(iv)) mostra que o falsificador de `φ`
obtido em `M′` aponta **necessariamente** um índice `i_0 < m` **onde `(S4)` falha em
`M′`** — e este `i_0` é o mesmo do passo (5) que invoca `(7)` (conferido no verbatim).
**Dicotomia (P) — dois chifres** (a v3 tentava *modus tollens* sobre premissa
epistêmica — reescrita). A **leitura forte** é aquela em que o **passo (5) valeria**:
ou o item **(i)** do Problema 2.1 lido sobre `M′` (*"M′ preserves all Σ^b_1 properties
of elements of M"* — verbatim do §2 do artigo, cf. `F1 §6(c)`), o que dá `(8)`
instanciável no `i_0 ∈ M′` — e o item (5) exige `(8)` **em `M*`** com `i_0 ∈ M*`
(`G2` 2.1(c)/Cor 2.2; `(F-sent)` em `M′` é a forma (b), mais forte); ou o item
**(iii)** lido como `M′∩m = M∩m` (`F1 (H)`). **Chifre (α)**: se a leitura forte
**for** a pretendida, a configuração que o item (5) exige — **(ii)+(8)/(F-sent)**
com `T_PV` — é **refutada** (`G2` Thm 2.1(b)/(c); na leitura (iii), `G1` Thm 4.3;
e `L.1` diz onde o falsificador precisa morrer), o Problema 2.1 é **negativo para
esta instância** e o **rodapé 2** (`¬2.1 ⟹ P≠NP`) entrega **`P≠NP`**.
**Chifre (β)**: se a leitura forte **não for** a pretendida, o passo (5) carece do
argumento que o sustente — a direção da errata. **Perguntamos: qual das leituras
(i)/(iii) é a pretendida — e, no chifre (α), a perna `P≠NP` é aceita?**
*(Escopo desta dicotomia: depende do verbatim dos itens (i)–(iii) e da equação (8) —
perguntado em §4.3. Labels: no Problema 2.1 os itens são (i)(ii)(iii) (`A_...`
L513–518); `(1)`…`(8)` são equações do artigo, com `(1)` = condição da análise KPT.)*

**Carta em inglês (base — F1 §5, revisada).**

> Dear Dr. Krajíček, I am reading arXiv:2506.20221v5 with great interest. In §3, item (5)
> of the proof of Theorem 4 in arXiv v4 (renumbered as Theorem 3 in v5/LMCS), the sentence
> "But by (7) i_o is also already in M∗" seems to derive i_0 ∈ M* from Log(M*) = Log(M′).
> Since Log(M) = {|m| : m ∈ M} records only measures, and any new element j < m has
> |j| ≤ |m| (a measure already in Log(M)), condition (7) appears compatible with M′
> containing indices below m outside M*. The step would follow from the additional
> domain condition M′ ∩ m = M ∩ m; alternatively the axiom (8) could be required
> directly in M′. Am I missing an argument — e.g., a feature of the forcing in
> [7, Thm 9.4.2] that also prevents new elements of old measure below m? Best regards.

## §2. Obstáculos estruturais a reparos naturais (P) — nossos teoremas

Pedimos ao autor que os verifique; passaram por revisão cruzada por pares interna
(logs em `*_referee.md`).

> **(i) Teorema G2 (obstrução) (P).** Para a semente do artigo (`M ⊨ (S1)–(S4)`), a
> configuração `M' ⊨ T_PV` com `¬φ` **satisfatível** e `M' ⊨ (F-sent)` é **falsa em ZFC**
> (`G2` Thm 2.1(a)/(b); hipótese mínima `M' ⊨ PV`, Thm 2.1(a′)). Isto **não** refuta a
> hipótese (ii) do artigo *per se* — refuta **(ii) junto de `(8)`/`(F-sent)` em `M'`** —
> exatamente a configuração que o item (5) da prova do Teorema 3/4 precisa (`G2`
> Cor 2.2). I.e., **nenhum método** (forcing ou outro) pode gerar `(F-sent)` junto do
> falsificador. *(Ressalva honesta do próprio `G2 §2.5.1`: a construção sob `NP=coNP`
> permanece legítima — e já provaria `NP≠coNP`.)*
> **(ii) Teorema H1.1 (no-G) (P).** A semente `𝒯 = {¬φ} ∪ {δ_N→τ_N} ∪ {C≡1}` é
> **irrealizável por qualquer `G` genérico** (ultrafiltro em `B(p)` fechado sob
> EF-provability in `M` e contendo constantes-1): `ν_G` leva `𝒯` a `M[G] ⊨ PV` com
> `¬φ` satisfeito **e `(F-sent)`** (ramos `δ_N→τ_N`) — contradizendo `G2` 2.1(a′). *(Amálgama/`(S3)`/Condition 1 são da
> *semente* — `G2` Thm 1.1/§2.3 — não desta refutação.)*
> **(iii) Teorema K (J1 §3; incondicional) (P).** Em nenhum `M_0 ⊨ T_PV+(S2)+(S3)+(S4)`
> existe **coleção interna** `F` com `∀i<m Fals(F(i),α_i)`: colher falsificadores um a
> um e juntar é proibido. K é **coerente com, não idêntica à** a remark do artigo
> (**(A)** L442: BB invalida a análise de `(1)` — perda de universalidade do KPT).
> **(P)** `J1` K.2: `T_PV+BB+(S2)+(S3)+(S4)` é **inconsistente** — a **segunda** razão,
> ao nível da semente. Escolha **padrão-muitos** é inofensiva; **uniformização não-padrão**
> é o que morre (lição do `J2`: uniformização que entregaria coleção é proibida).
> **(iv) Teorema L.1 (L1 §1) (P).** `T_PV+(S4) ⊢ ∀rφ(r)`: `¬φ` é internamente
> **insatisfatível em todo modelo de `T_PV+(S4)`** (com `α,m` nomeados) — o falsificador
> só pode viver onde `(S4)` falha (§1 acima).
> **(v) I1 B.2/B.3 (P).** **Nenhum ultrapoder `ℕ^ω/U`** modela `S` (Łoś + Lema B.1:
> nenhuma instância **padrão** de `(S2)–(S4)` com `P` sounde; B.3: sem falsificador
> comum + sem seletor p-tempo). **O venue `M_0 ⊨ S` não-padrão permanece vivo** (C.1 —
> não afirmamos que `S` é refutável). À parte: `I1` A.4–A.6 — para `T_f` padrão,
> refutabilidade interna por EF ⟺ insatisfatibilidade real em todo `M ⊨ T_PV`.
> **(C)**: extensão de B.2 além de ultrapoderes de `ℕ` (`I1` B.4).

## §3. O que sobrevive — correções que propomos (P)

1. **Teorema 4 do artigo (v4; = Teorema 3 em v5/LMCS) — correção proposta: `G2`
   Teorema 4.1.** A correção é a **troca da hipótese 2.1 → `(F-sent)`** (falsificador
   com semente **enviada**, não gerada): com ela o teorema torna-se **correto como
   condicional** — **mas a hipótese trocada é ela-mesma ZFC-falsa** para a semente
   (`G2` Thm 2.1/Cor 2.2; `§2.5.1` dá a legitimidade da reductio sob `NP=coNP`) — o
   teorema corrigido é um **alvo de reductio**, não uma entrega verificável.
   **(F-b')** (= exigir `M′∩m = M∩m`, versão domínio) é **refutado** (`G1` Thm 4.3;
   ver `G1` Cor 4.4 para o passo (5)). A featura `Log(M[G]) = Log(M)` é **teorema em
   [Kra98 §4]** (`G1` Thm 2.1), mas **(C) para a versão do livro** (`[Kra95, Thm 9.4.2]` —
   `G1` Advert. 2.4) — e é o livro que o artigo cita.
2. **K-FP′ (J2; por nome) + J.6-a′ (famílias) (P)** — para **todo nome padrão `N` com
   `R(N)⊆m`**, o ponto fixo `∃q*: Fals(q*, (α)_{code(N,q*)})` **existe em todo
   `M_0 ⊨ T_S`** (colagem sobre disjuntos `(S2)`; escolha padrão-muitos, **sem** a
   coleção proibida pelo Teorema K); **J.6-a′** estende a **famílias finitas-padrão
   sem `¬φ`**.
3. **L.3′ (L1 §3) (P)** — **Q-compactness de `𝒯` para refutações genuínas: negativa
   incondicionalmente**: qualquer `d*` padrão refutando subfamília internamente finita
   usaria premissas de tamanho padrão — e os **únicos** membros padrão de `𝒯` são as
   constantes-1 (os demais embutem os bits de `α` como constantes; `α` é não-padrão —
   Lema L.3a) — tautologias reais; soundness real de EF fecha. **C.3 decidida:
   negativa.** **Residual (L.3″)**: refutações **internas** com testemunha **não-padrão**
   seguem **abertas** — é a pergunta de Q-compactude; o canto **adversarial** de `J2 §3`
   é uma pergunta **interna** marcada **(C)** (não toca C.3).
4. **L.4 (L1 §4) (P)+(A)** — o aviso do artigo (L21–22: *"a pps `P` may be **incomplete**
   in a model of `T_PV` … but it will always be sound as that is expressible by a
   universal `L_PV`-formula"*) é **exemplificado pelo próprio `φ`**: sob Condition 1 +
   L.1, `φ` é internamente válida e internamente não-provável — instância canônica de
   incompletude **dentro** do artigo.
5. **J.2′ (J1) (P)** — `¬φ` falha em toda atribuição **padrão** (subsumido por L.1).

## §4. Perguntas ao autor (A) — delimitam o residual

1. **Semântica de `τ_N`**: a leitura (R1) — `τ_N = ⋁_q (q` cod. atribuição ∧
   `Fals(q,(α)_{code(N,q)}) = 1)` — é a pretendida? Há alternativa? (`J2 §1`;
   consequências escritas para sobreviver às duas.)
2. **Convenção de código**: os bits de `α` entram como **constantes** nas fórmulas
   (conferido no artigo por nós — `L1 §5` nº 4; confirma?) — é o que sustenta L.3′.
3. **`(8)` em `M′`**: era exigido? A leitura dos itens (i)–(iii) do Problema 2.1:
   quais condições exatamente (para fechar o escopo da dicotomia §1)? E a featura de
   [7, Thm 9.4.2] que você imaginou ao escrever o passo (5) — qual é?
4. **Condition 1** (φ sem prova em `M` em nenhum pps): pretendida como hipótese
   **sobre** o modelo, ou era para ser **derivada**? (L.4 mostra que, como hipótese,
   ela instancia a própria incompletude que você avisa.)

## §5. Autoria, processo e próximos passos (interno)

- **Autoria honesta (A)+(P)**: a **lacuna** do Teorema 3/4 é **do artigo (A)**; o que
  é **nosso (P)** é a **identificação**, a análise §§1–3 e os teoremas §2 — as citações
  verbatim são do artigo e estão separadas em cada item. Processo: revisão cruzada por
  pares interna por entrega (logs em `*_referee.md`).
- **Próximos passos**: (1) revisar este rascunho (usuário); (2) traduzir para o inglês:
  a **carta de §1** (curta — ~1 página) e **decidir** se o §2 (obstáculos) entra como
  **apêndice de uma página** (recomendado: só 2–3 itens resumidos — G2, K, L.1 — para
  não diluir a errata; o texto em PT completo fica como dossiê de apoio); (3) revisão
  final do dossiê consolidado; (4) envio a
  `www.karlin.mff.cuni.cz/~krajicek/` após aprovação.
- **Lacunas honestas**: (a) os teoremas §2 são nossos — se o autor apontar erro, este
  documento cai em parte; (b) o escopo da dicotomia §1 pende do verbatim de (i)–(iii)/(8);
  (c) a semântica de `τ_N` (§4.1) pode alterar J2 (nem K, nem L); (d) `(C)` permanece:
  canto adversarial interno (`J2 §3`), `Log(M[G])=Log(M)` para o livro (`G1` Advert.
  2.4), featura de [7] (`F1 §2.2`), extensão de B.2 além de `ℕ` (`I1` B.4); (e) o venue
  `M_0 ⊨ S` (I1 C.1) segue **aberto** — §2(v) não o fecha; (f) gaps declarados do `G2`:
  espelhamento `α_i ↦ α̃_i` para `i` não-padrão e passagem a semente infinita (`G2`
  §2.3/§6, referee R3).

## §6. Registro de correções (v1→v2→v3→v4; referee rodadas 1–3)

- **v1→v2 (rodada 1: 3 CRÍTICOS + 4 MAIOR)**: C2 (numeração 3 v5/4 v4), C3 (I1 escopo
  ultrapoder de `ℕ` + mecanismo), M3 (renumeração, `(F-b')`, `(C)`-livro, ZFC-falsa),
  M6 (L.3″ + adversarial `(C)`), M2-partial ("coerente com, não idêntica à"), M5-partial
  (K-FP′ escopos), M1-partial (no-G
  mecanismo). *(O §6 da v2 superestimou os fechamentos de C1 e M4 — corrigido abaixo.)*
- **v2→v3 (rodada 2)**: **C1′** — §2(i): a refutada é **(ii)+(8)/(F-sent) em `M′`**,
  não (ii) *per se* (a v2 reabria o over-claim `⟹P≠NP`); ressalva `G2 §2.5.1` (reductio
  sob `NP=coNP`) acrescentada. **M2′** — §2(iii): `T_PV+BB+(S2)(S3)(S4)` inconsistente é
  **K.2 = (P)** (a v2 etiquetara como L442 = (A)); L442 = perda de universalidade do KPT.
  **M4a** — leitura forte **definida**: "(i) sobre `M′` (verbatim 'preserves all
  Σ^b_1 properties…') ou (iii) = `M′∩m=M∩m`" — a que faria o passo (5) valer; cadeia
  coerenciada. **M4b** — rótulos alinhados: itens **(i)(ii)(iii)** do Problema 2.1;
  `(1)…(8)` = equações. **REG-1** — §1: reparos (a)→`G1` 4.3, (b)→`G2` 2.1(b) (a v1
  atribuira à K). **REG-2** — este log é reescrito para o estado real. **Menores 1–13**:
  §2(v) sem quantificador órfão; §2(ii) escopo de `G`; §2(i) base `M⊨(S1)–(S4)`;
  §3.1 rótulo do teorema + `(L1)` [Kra98 §4]/(C)-livro + `G2` Thm 2.1/Cor 2.2;
  §3.2 "K-FP′+J.6-a′"; §3.4 verbatim integral; §4.2 ponteiro `L1 §5` nº 4; §5
  "lacuna é (A)"; §5 lacunas G2 (espelhamento/semente infinita); carta EN "(Theorem 4
  of the v4; renumbered Theorem 3 in v5/LMCS)"; marcação `(C)` nos 4 pontos exigidos
  (§1 (c), §2(v), §3.1 livro, §3.3 adversarial).
- **v3→v4 (rodada 3)**: **M4a (MAIOR)** — a dicotomia foi **reescrita como disjunção
  de dois chifres** (α: leitura forte pretendida ⟹ refutação via `G2` 2.1(b)/(c) —
  na leitura (iii), `G1` Thm 4.3 — ⟹ 2.1 negativa para a instância ⟹ perna `P≠NP`
  via rodapé 2; β: leitura forte não pretendida ⟹ passo (5) sem argumento — direção
  da errata) + **pergunta explícita ao autor** (§4.3) — a v3 fazia *modus tollens*
  sobre premissa epistêmica. **REG-3** — §2(ii): acrescentado **`(F-sent)`** (ramos
  `δ_N→τ_N`) — sem ele, a contradição com 2.1(a′) repetia o erro C1 em miniatura.
  **Nits**: n1 (M2-partial no log v1→v2); n2 (carta: "Theorem 4 in arXiv v4");
  n3 ("i.e."→"i.e.," — absorvido pela reescrita de M4a); n4 (fonte `J2` para
  "padrão-muitos"); n5 (§5(2) com a decisão carta↔apêndice de §2).
- **Estado final (v4)**: todos os CRÍTICOS e MAIOR das rodadas 1–3 aplicados;
  13/13 menores da rodada 2 confirmados pelo referee; o referee pre-comprometeu
  APROVADO após "1 reescrita (MAIOR-3) + 6 linhas (REG-3, n1–n5)" — ambas
  aplicadas; pendente: apenas a decisão do **usuário**.

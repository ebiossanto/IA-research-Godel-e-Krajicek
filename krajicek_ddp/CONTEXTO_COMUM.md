# Contexto comum da equipe — Problema DD_P (Krajíček, arXiv:2506.20221v4)

**Idioma de trabalho: português.** Fonte primária: Jan Krajíček, *On NP∩coNP proof complexity
generators*, arXiv:2506.20221v4 (23 Mar 2026) — https://arxiv.org/html/2506.20221v4
(pode usar `webfetch`/`websearch`; confirme no artigo antes de citar literalmente).

## Extração fiel do artigo (usar como fonte primária; marcar divergências)

1. **pps (propositional proof system)**: relação binária `P(x,y)` decidível em tempo polinomial
   tal que `∃x P(x,y)` define TAUT. Notação sugerida: `σ : P ⊢ β`.
   *Obs.: a formalização do usuário "P : {0,1}* → TAUT, p-time e sobrejetora" é a versão
   função; o artigo usa a relação binária de Cook–Reckhow.*
2. **Disjunção disjunta** (disjoint disjunction) `⋁̇_{i<m} α_i`: nenhum par `α_i, α_j`
   compartilha átomo.
3. **DD_P**: entrada `(π, ⋁̇_i α_i)` com `π : P ⊢ ⋁̇_i α_i`; saída: `i` com `α_i ∈ TAUT`.
   Totalidade: se cada `α_i` tivesse atribuição falsificante, a união dessas atribuições
   (átomos disjuntos ⇒ sem conflito) falsificaria a disjunção inteira, contradizendo `P ⊢`.
4. **D_P** (generalização): entrada `(π, ⋁_i β_i(p,q^i), a)` com **apenas** os átomos `p`
   podendo ocorrer em mais de um `β_i`, e `a` uma atribuição de verdade para os `p`;
   saída: `i` com `β_i(a,q^i) ∈ TAUT`.
5. **Modelo aluno-professor (S-T)**: S recebe a entrada e propõe candidato `i_1`;
   se correto, T reconhece e a computação termina; senão T envia um contra-exemplo
   (atribuição falsificando `α_{i_1}`); S propõe `i_2` usando o contra-exemplo, etc.
   `ST[F, t(n)]`: classe dos problemas de busca totais Σ₂ᵖ solúveis em `t(n)` rodadas com
   um estudante cujos movimentos são computados por algoritmo de `F` (com `T` arbitrária).
6. **strong pps**: extensão de EF (Extended Frege) por um conjunto p-time de tautologias
   como axiomas extras. Todo pps é p-simulado por um strong.
7. O artigo afirma que **DD_P é soluvel no modelo S-T** — *conferir no artigo o número
   exato de rodadas e os limites* (a hipótese (ST) fala em O(1) rodadas; a provável realidade
   é até `m` rodadas, `m` = nº de disjunctos, que é polinomial mas NÃO constante).
8. **Lema 1**: `DD_P ∉ ST[P, O(1)] ⇔ D_P ∉ ST[P, O(1)]`.
9. **Hipótese (ST)**: existe strong pps `P` com `DD_P ∉ ST[P, O(1)]` (`P` aqui denota também
   a classe de algoritmos p-time). Krajíček acredita que vale para **todo** strong pps
   (equivalente a valer para EF).
10. **Lema 2** ([11] = Krajíček, *A limitation on the KPT interpolation*, LMCS 16(3), 2020):
    (ST) é verdadeira se existe uma permutação one-way **forte** (nenhum circuito p-size
    a inverte com vantagem não-negligível).
11. **Missing reflection / BB**: fórmulas τ(g) têm forma `γ(p,q) := ⋁_i β_i(p,q^i)` com
    `q^i` disjuntos. Falsificação de γ em modelo equivale a (3) `∃x,y ∀i<m ¬A_b(x,i,(y)_i)`,
    enquanto as construções de [8,12] dão (4) `∃x ∀i<m ∃y_i ¬A_b(x,i,y_i)`.
    Trocar os dois quantificadores internos exige o esquema **BB** (sharply bounded
    collection) para fórmulas abertas; Cook–Thapen (2006, [6]) mostram que BB **não** é
    provável em `T_PV` (a menos que fatoração não seja difícil), e acrescentar BB invalida
    a análise KPT (a teorema KPT de [16] não se aplica em forma útil a teoria não-universal).
12. **Teorema 3** (após Krajíček–Pudlák 1990, Thm.1): `M ⊨ T_PV` não-padrão, `φ` fórmula
    proposicional (no sentido do modelo): equivalentes:
    (1) `φ` não tem prova em `M` em nenhum pps;
    (2) existe extensão `M' ⊇ M` com `M' ⊨ T_PV + (¬φ) ∈ SAT`.
    Comentários: construções com modelos de `S^1_2` garantem que `M'` preserva propriedades
    Σ^b_1 de elementos de `M` (usa BB para fórmulas abertas); pode-se arranjar
    `Log(M') = Log(M)` via forcing ([7], Thm 9.4.2).
13. **Problema 2.1 (EM ABERTO — é o coração do paper)**: suponha `M ⊨ T_PV` satisfazendo o
    item (1) do Teorema 3. Existem estruturas `L_PV` `M ⊆ M* ⊆ M'` tais que
    (1) `M*` preserva **todas** as propriedades `Σ^b_1(PV)` de elementos de `M`;
    (2) `M' ⊨ T_PV + (¬φ) ∈ SAT`;
    (3) `Log(M*) = Log(M')`?
    O artigo **assume** resposta afirmativa. Observações do artigo: resposta **negativa**
    implicaria `P ≠ NP` (rodapé 2); basta uma classe universal de modelos (ex.: contáveis ou
    recursamente saturados); basta que `M*` preserve propriedades `∀i∃y B(x,i,y)` com `i`
    sharply bounded, `y` bounded, `B` aberta.
14. **Teorema 4**: (Problema 2.1 com resposta afirmativa) + (ST) ⟹ `NP ≠ coNP`.
    Esquema da prova: (1) sob `NP = coNP`, escolher strong pps `P` satis fazendo (ST) e
    também **p-bounded**; (2) teoria `S` com constantes `π, α` e axiomas: `T_PV`;
    `α` é disjunção disjunta `⋁̇_{i<m} α_i`; `π : P ⊢ α`; `∀i<m (¬α_i) ∈ SAT`.
    Se `S` fosse inconsistente, o **teorema KPT** aplicado aos três primeiros axiomas daria
    funções p-time dos movimentos de um estudante que resolve `DD_P` em O(1) rodadas,
    violando (ST); logo existe modelo `M` (não-padrão) de `S`; (3) por p-boundedness existe
    `c` com toda tautologia `β` tendo prova `P` de tamanho `≤ |β|^c`; notação `σ : P ⊢* β`;
    a fórmula universal `A_Q`: `x : P ⊢ ⋁̇_i (y)_i → Q ⊬ ||∀i<len(y) (z)_i : P ⊬* (y)_i||`
    é verdadeira (portanto está em `T_PV`) porque alguma `(y)_i` é tautologia e, pela
    p-boundedness, tem prova `P` curta; (4) em `M`, substituindo `x:=π, y:=α`, obtem-se
    `M ⊨ Q ⊬ φ(r)`; (5) o Problema 2.1 dá `M ⊆ M* ⊆ M'` com `Log` iguais e
    `M' ⊨ T_PV ∧ ¬φ ∈ SAT`; `M*` satisfaz `∀i<m (¬α_i) ∈ SAT` por preservação Σ^b_1;
    um `σ` falsificando `φ` em `M'` fornece `i_0` com `M' ⊨ σ_{i_0} : P ⊢ α_{i_0}`;
    `i_0 ∈ M*` (mesmos comprimentos) e `(¬α_{i_0}) ∈ SAT`, contradizendo `Ref_P`
    (`x : P ⊢ y → (¬y) ∉ SAT`), que vale em `M'` por `T_PV`.
15. **Observação final do artigo**: a prova mostra algo mais forte — em **nenhum** strong `P`
    uma prova de algum disjuncto numa disjunção disjunta é polinomialmente limitada em
    função do tamanho de uma prova da disjunção (a **strong feasible disjunction property**
    **falha** para strong proof systems).
16. **Referências-chave**: [8] Krajíček, *J. Math. Logic* 11(1), 2011 (gerador NW sobre
    função NP∩coNP dura; análise S-T mostrou que (1) não pode ser testemunhado em
    `ST[P/poly, O(1)]` se existir permutação one-way dura para circuitos p-size);
    [11] Krajíček, LMCS 16(3), 2020; [12] Krajíček, *Proof complexity generators*,
    LMS Lecture Note Series 497, CUP 2025 (gerador de gadget, hipótese (K), Sec 8.6);
    [17] Pich–Santhanam, STOC 2021; [6] Cook–Thapen, TOCL 7(4), 2006;
    [16] Krajíček–Pudlák–Takeuti, APAL 52, 1991 (KPT);
    [15] Krajíček–Pudlák–Sgall, MFCS 1990 (modelo S-T);
    [14] Krajíček–Pudlák, CSL 1990; [7] Krajíček 1995 (livro);
    [10] Krajíček, *Proof Complexity*, CUP 2019; [5] Cook–Reckhow 1979; [3] Buss 1986.

## Problema relacionado (2023)

arXiv:2303.10637 (Krajíček): dado um teorema `T` p-time, sólido, que formaliza a sintaxe,
constrói-se `g_T` que estica a entrada em 1 bit e que formaliza a incompletude de `T`.
Em aberto: se, para **algum** `T`, a imagem de `g_T` intersecta **todo** conjunto NP infinito
(ou seja, se `g_T` é um gerador difícil para todos os sistemas de prova).
Verificar o enunciado exato no artigo antes de afirmar qualquer coisa.

## Estado das frentes (11 Out 2026 — após as rodadas A–M)

- **Numeração**: em **v5/LMCS** o "Teorema 4" da v4 é o **Teorema 3** (Problema 2.1,
  `(7)`, `(8)`, `Log` inalterados) — ver `G_CONTEXTO_FORCING.md` §1.1. A lacuna
  "But by (7) i_o is also already in M∗" está em **ambas** as versões.
- **Veredito consolidado sobre o Teorema 4/3**: (1) a lacuna do passo (5) é **real**
  (`F1`, referee 10/10); (2) a configuração natural de reparo é **ZFC-falsa**
  (`G2` Thm 2.1: `T_PV`+falsificador+`(F-sent)`); (3) a correção é a **troca
  2.1→`(F-sent)`** — teorema correto como condicional, mas **alvo de reductio**
  (hipótese trocada ZFC-falsa para a semente); `(F-b')` refutado (`G1` 4.3).
- **Frente L (nova, 11/10; `L1_phi_insatisfativel.md` v4 RECOMENDADO)**:
  **L.1**: `T_PV+(S4) ⊢ ∀rφ(r)` — `¬φ` internamente insatisfatível em todo modelo;
  pinça o `i_0` (falsificador vive onde `(S4)` falha). **L.3′**: **C.3 negativa
  incondicionalmente** (membros padrão de `𝒯` = só constantes-1; `α` não-padrão —
  Lema L.3a). **L.4**: Condition 1 + L.1 ⟹ o próprio `φ` exemplifica o aviso
  L21–22 (pps pode ser incompleto em modelo de `T_PV`).
- **`NOTA_EDITORIAL_Krajicek.md` v4 + `CARTA_FINAL_ENVIO.md`**: nota ao autor
  (errata + obstáculos G2/H1/K/L.1 + o que sobrevive + perguntas), referee-processado
  3 rodadas (`NOTA_referee.md`) — **APROVADA PELO USUÁRIO (11/10)**. **Carta final
  EN pronta** (`CARTA_FINAL_ENVIO.md`): errata + dicotomia (dois chifres) + 3
  obstáculos resumidos + 4 perguntas (Q1 = "`q` em `τ_N` é **total**?") +
  **apresentação do autor** (pesquisador independente/entusiasta; pesquisa com
  OpenCode + MIMO + IAs gratuitas; GitHub `github.com/ebiossanto`; e-mail
  `euambiente@gmail.com`). **✅ ENVIADA em 11/10/2026 18:14** para
  jan.krajicek@protonmail.com e krajicek@karlin.mff.cuni.cz — **aguardando resposta**.
- **Residual J.6**: semântica de `τ_N` (R1 vs alternativa) e pergunta (i)/(iii) da
  dicotomia — perguntas ao autor (§4 da nota).
- **Frente M (nova, 11/10; `M_canto_adversarial.md` v4 RECOMENDADO, referee 3
  rodadas — `M_referee.md`)**: o **canto adversarial (C)** de `J2 §3` foi **decidido**:
  **M.0**: `T_S ⊢` `m` é **não-padrão** (Teorema K + (S4) + montagem p-tempo) —
  o caso "m padrão" não existe; **M.1**: não existe **falsificador global** em
  nenhum modelo (contrapositiva de K); **M.2**: nome **não-padrão** `N_s` (**seletor
  p-tempo** "menor índice `i<m` com `¬Fals(v,α_i)`", total por M.1) satisfaz
  **`C_{N_s} ≡ ⊥` internamente em todo `M_0 ⊨ T_S`** (sob R1 e sob a alternativa
  com `q` total; sob `q` parcial pode abrir — a pergunta ao autor decide) — 2ª
  condição `≡ ⊥` da semente (dual de `¬φ`, mecanismo Teorema K); **M.3**: nomes
  **padrão** nunca são adversariais (guarda `R(N)⊆m` automática — contraexemplo
  `m=2` do referee J2 é vácuo; famílias internas não-padrão-muitas = `(C)`);
  **M.4**: famílias com `C_{N_s}` sem refutação genuína (L.3′), refutação interna
  **aberta**; **M.5**: J.6-a′ sem ressalva de `m`. Novo item de pergunta para a
  nota: **"`q` em `τ_N` é atribuição total?"** (decide o trap M.2).

## Infraestrutura local

- Repositório: `C:\Users\Euzébio Soares\Downloads\zero\IA-research-Godel-e-Krajicek`
- Projeto Lean 4: pasta `lean4/`, lib `Gothic_Generators` (`lakefile.toml` com
  `srcDir = "lean4"` e `roots = ["Gothic_Generators.Core"]`, `lean-toolchain`).
  Estilo de referência: `lean4/Gothic_Generators/Core.lean` (namespace, comentários `/-! -`
  e docstrings em português, `import Init` apenas — sem dependências externas).
- Documentos de apoio existentes em `support/` e numerados (`01_...` a `27_...`).

## Regras da equipe

1. Escrever entregáveis **apenas** nos arquivos indicados na própria missão (não editar
   arquivos de outras equipes).
2. Distinguir sempre: **(A)** o que está no artigo; **(B)** o que é demonstração própria;
   **(C)** conjectura/ideia de trabalho.
3. Rigor técnico; nada de afirmação sem fonte ou sem prova.
4. Terminar a resposta com um resumo de até ~600 palavras com os achados principais e os
   caminhos mais promissores.

# Relatório consolidado — Equipe multidisciplinar sobre o problema DD_P de Krajíček

**Fonte primária:** Jan Krajíček, *On NP∩coNP proof complexity generators*,
arXiv:2506.20221 (v4, 23 Mar 2026 — https://arxiv.org/html/2506.20221v4;
**v5/LMCS 22(2:14)2026** — https://arxiv.org/html/2506.20221v5).
**Numeração:** o "Teorema 4" da v4 é o **Teorema 3** na v5/LMCS (`G_CONTEXTO_FORCING.md` §1.1);
a lacuna está em **ambas** as versões.
**Data do relatório:** 10–12 Out 2026 (atualizado com a terceira onda N2/C2/Q2 + avaliação externa de 12/10 — §9).
**Equipes/frentes:** A (teoria exata), B (Lean 4), C (casos/disjunção viável), D (geradores),
E (ataque ao Problema 2.1); **segunda onda:** F (verificação do passo 7/5), G (forcing/`Log`),
H (coleção/refutação), I (Q-compactness), J (`M_0`/ponto fixo), L (`¬φ`), M (canto adversarial),
Nota editorial.

> **§0. Nota de status (padrão fixado em 12/10/2026 — ver §9).** Todo veredito
> "**RECOMENDADO**" deste relatório significa: **aprovado por rodada interna de
> crítica estruturada (referee hostile interno; logs `*_referee.md`)** — **não**
> equivale a peer review nem a validação pela comunidade. Os resultados **(P)** de
> K, L, M, N são **argumentos próprios condicionais** (os condicionais estão em
> cada frente). **Nenhum** item deste relatório é um lower bound computacional;
> a ponte L2→L3 está **aberta** (§9.1). A auditoria **externa** de `DD_Res ∈ P` e
> das frentes G–N está **pendente** — dossiê pronto em
> `AUDITORIA_EXTERNA_DDRES_G-N.md`.

Entregáveis individuais (não duplicar aqui; este relatório só consolida):

| Equipe/Frente | Arquivo |
|---|---|
| Contexto | `krajicek_ddp/CONTEXTO_COMUM.md` |
| A — teoria | `krajicek_ddp/A_teoremas_exatos.md` |
| B — Lean 4 | `lean4/Gothic_Generators/DDP.lean`, `DDP_Experiments.lean`, `krajicek_ddp/B_lean_relatorio.md` |
| C — casos | `krajicek_ddp/C_disjuncao_viavel.md`, `krajicek_ddp/experimentos_disjuncao.py` |
| D — geradores | `krajicek_ddp/D_geradores_consequencias.md` |
| E — ataque | `krajicek_ddp/E_ataque_problema21.md` |
| F — verificação | `F_CONTEXTO_ATAQUE.md`, `F1_verificacao_passo7.md`, `F2_versao_finita.md`, `F3_ataque_construtivo.md`, `F_RELATORIO_ATAQUE_FINITO.md` |
| G — forcing | `G_CONTEXTO_FORCING.md`, `G1_log_forcing.md` (+`G2_referee.md`), `G2_semente_Fsent.md` |
| H — coleção | `H1_colecao_refutacao.md` (+`H1_referee.md`) |
| I — Q-compact | `I1_Qcompactness_ultrapoderes.md` (+`I1_referee.md`) |
| J — `M_0`/PF | `J1_Qcompactness_M0.md` (+`J1_referee.md`), `J2_ponto_fixo.md` (+`J2_referee.md`) |
| L — `¬φ` | `L1_phi_insatisfativel.md` (+`L1_referee.md`) |
| M — adversarial | `M_canto_adversarial.md` (+`M_referee.md`) |
| Nota editorial | `NOTA_EDITORIAL_Krajicek.md` (+`NOTA_referee.md`) |

---

## 1. O que o artigo diz (extração exata — Equipe A)

- **pps**: relação binária Cook–Reckhow `P(x,y)` p-time com `∃x P(x,y) ⇔ TAUT`
  (a versão "função sobrejetora" dada pelo usuário é só a variante função).
- **DD_P**: entrada `(π, ⋁̇_i α_i)` com `π : P ⊢ ⋁̇_i α_i` (disjunção disjunta); saída `i`
  com `α_i ∈ TAUT`.
- **D_P**: generalização com átomos compartilhados `p` fixados por uma atribuição `a`.
- **Lema 1**: `DD_P ∉ ST[P,O(1)] ⇔ D_P ∉ ST[P,O(1)]`.
- **Hipótese (ST)**: existe strong pps `P` (extensão de EF por axiomas p-time) com
  `DD_P ∉ ST[P,O(1)]`. Krajíček acredita que vale para todo strong pps (equivalente: EF).
- **Lema 2** ([11], LMCS 2020): (ST) é verdadeira se existe permutação one-way forte.
- **Problema 2.1** (ABERTO — o coração): para `M ⊨ T_PV` sem prova de `φ`, existem
  `M ⊆ M* ⊆ M'` com (i) `M*` preservando Σ^b_1(PV) de elementos de `M`,
  (ii) `M' ⊨ T_PV + (¬φ) ∈ SAT`, (iii) `Log(M*) = Log(M')`?
- **Teorema 4**: (Problema 2.1 afirmativo) + (ST) ⟹ `NP ≠ coNP`.
- **Rodapé 2**: resposta **negativa** ao Problema 2.1 ⟹ `P ≠ NP`.
- **Observação final**: a strong feasible disjunction property **falha** para strong pps
  (sob as mesmas hipóteses do Teorema 4).

### Correções aos enunciados do usuário (Equipe A)

1. **Número de rodadas S-T**: o artigo **não** escreve número algum ("some number of rounds").
   A cota `≤ m` (m = nº de disjunctos) é derivação própria: cada contra-exemplo elimina
   exatamente um índice (átomos disjuntos ⇒ o contra-exemplo não informa sobre os demais).
   Logo `DD_P ∈ ST[P, O(n)]` — polinomial, mas **não** constante; e é exatamente a
   não-constância que (ST) postula ser insuperável.
2. **Classe de complexidade**: o rótulo "busca total Σ₂ᵖ" coincide com o artigo (abstract:
   "the Σ₂ᵖ search problem DD_P"), **mas a justificativa do usuário está errada**: o
   critério de aceitação `∀y ¬A(x,i,y)` tem um único bloco universal = `coNP`
   (coNP-completo em entradas válidas). Os dois blocos `∃i<m ∀y` existem apenas na
   **sentença de totalidade** (Σ^b_2), não na verificação. DD_P **não** é Σ₂ᵖ-complete.
3. **Totalidade não exige BB**: `Ref_P` é sentença universal verdadeira, logo ∈ `T_PV`;
   a redução de testemunha usa uma só extensão de atribuição. BB é preciso noutro sítio:
   no swap (3)↔(4) e no preservamento Σ^b_1.

---

## 2. Formalização Lean 4 (Equipe B) — COMPILANDO

Projeto existente estendido: `lean4/Gothic_Generators/DDP.lean` (695 linhas) +
`DDP_Experiments.lean` (138 linhas) + root acrescentado ao `lakefile.toml`.
Toolchain `v4.34.0` instalada via elan. **`lake build` = sucesso (exit 0), 2 `sorry`s intencionais.**

Provado integralmente (sem `sorry`):
- Sintaxe/semântica: `Formula`, `atoms`, `DisjointDisjunction` (via `List.Pairwise`), `orAll`,
  `Eval`, `Tautology`, `eval_congr`, decidibilidade de TAUT por enumeração de valorações.
- `PropProofSystem` (Cook–Reckhow: `Valid : List Formula → Formula → Bool` + sonoridade),
  `DDInstance`/`DDTask`.
- **Lema de totalidade de DD_P por indução real**: `dd_counterexample_exists` constrói
  explicitamente a valoração `v = ⋃ vᵢ` (com lemas de consistência `unionVal_mem/not_mem`),
  total e falsificando `⋁̇αᵢ`; contrapositiva e `dd_task_total` (toda entrada tem solução).
- Modelo aluno–professor completo (`Student`, `professor`, `play`) com `play_correct` ⟹
  **`dd_solvable_in_m_rounds`**: DD_P soluvel em m rodadas.

Os 2 `sorry`s são permanentes por natureza (não são lacunas de trabalho):
`dd_solvable_in_ST_O1` (é exatamente o que (ST) postula falso) e
`pbounded_implies_feasible` (falta só o limite de tempo; a semântica já está em
`pbounded_spec`).

---

## 3. Disjunção viável sistema a sistema (Equipe C) — o resultado mais forte

**Teorema próprio (B): `DD_Res ∈ P` para resolução em qualquer apresentação usual**
(tree/dag-like, com ou sem enfraquecimento), com garantia ótima: o algoritmo devolve `i*`
com `α_{i*} ∈ TAUT` **e uma refutação pura desse lado com ≤ |π| linhas** — ou seja,
a FDP vale para Res com `p(t) = t`. Prova em duas etapas:
(1) **lema de recorte** que elimina enfraquecimentos preservando derivação pura de tamanho
≤ |π| (o ponto sutil — herdar o pai correto quando o literal resolvido sobrevive num só lado);
(2) **lema da pureza** (toda linha é pura; os pais do último passo são puros do mesmo lado),
da qual segue o algoritmo de projeção.

Corolários: `D_Res ∈ P` (pela restrição pela atribuição `a`); "interpolação viável ⟹
`DD_P ∈ P`" (interpolante constante no caso disjunto; `m−1` chamadas).

**Correção importante à premissa da missão**: resolução **tem** interpolação viável
(Krajíček, JSL 62 (1997); Pudlák 1997 na versão monotônica). A FI **falha** para strong pps
(sob OWP fortes) — é a razão pela qual [17] Pich–Santhanam é refutado.

**Refutação da regra ingênua**: "p-bounded ⟹ DD_P ∈ P" **não** se sustenta como algoritmo —
enumerar provas de tamanho ≤ |β|^c custa `2^{|β|^c+1}`, exponencial. A implicação ficou
**aberta**; e a recíproca é **falsa** (Res tem `DD ∈ P` mas não é p-bounded, Haken 1985).
Ademais, p-bounded de qualquer P implica `NP = coNP`, então sob as hipóteses do Teorema 4 a
questão é vazia.

**Experimentos** (3000 instâncias + enumeração exaustiva): algoritmo de projeção 3000/3000
corretos; heurísticas só-sintáticas falham em 9,6%–52% (contra-exemplos mínimos de 4 literais).
Heurística ≠ algoritmo — só a estrutura da prova dá resposta garantida.

**Status dos demais**: `Res(k)` (k ≥ 2), random-res, Frege: `DD ∉ P` **aberto** (conjectura
`∉ P` sob `P≠NP`). As instâncias de Garlík (CCC 2024) têm **ambos** os disjunctos
tautológicos — boas para cotas de prova, inúteis para separar `DD_{Res(k)}`.

---

## 4. Geradores e consequências (Equipe D)

- **NW ([8], JML 2011)**: "(1) não pode ser testemunhada em `ST[P/poly,O(1)]` se existir OWP
  forte para circuitos p-size". O problema de [8] **não** tem prova na entrada — a função do
  NW não é p-tempo (requer inverter a OWP) —, então o estudante só pode ser não-uniforme.
  **DD_P resolve exatamente isso**: a prova `π` na entrada permite aplicar KPT à teoria
  universal `{T_PV; π:P⊢α; …}`, gerando estudante **p-tempo uniforme** — é por isso que (ST)
  pode ser enunciada em `ST[P,O(1)]`.
- **(K) ⟹ (ST)** reconstruído: a forma de `K(c,P)` ([12, §8.6]) é a de DD_P (prova na
  entrada; disjunção disjunta de tautologias por contagem/PHP).
- **Lema 2** derivado de [11]: a "KPT interpolation" de Pich–Santhanam é literalmente um
  estudante de O(1) rodadas com prova na entrada (= `D_P`); [11, Thm 2] mostra que ela falha
  para sistemas fortes via bit difícil de OWP forte.
- **Gargalo identificado**: é o **Problema 2.1**, não (ST). (ST) deriva-se de hipótese
  criptográfica aceita; a extensão de modelos não tem suporte independente.
- **Observação final do artigo** reconstruída como **versão do Teorema 4 sem `NP=coNP`**
  (trocar p-boundedness por strong fdp na fórmula universal `A'_Q`), fechando a ponte
  dureza ⟹ W-duro de [12, Lema 4.2.3]: para sistemas fortes, a noção certa de dureza de
  gerador é a de **busca**.
- **Problema de 2023** (arXiv:2303.10637v2): enunciados `g_T`, Lema 2.1, Teorema 2.2,
  Corolário 2.3, Problema 2.4, Teorema 3.1 extraídos literalmente; **confirmada contra o
  HTML do arXiv a discrepância `n+2` vs `n+1`** já detectada no arquivo local `09_…`
  (validação independente). Comparação: busca-de-disjuncto (DD_P) vs cobertura-da-imagem
  (2023); o contato é que DD_P + Problema 2.1 destravaria a conversão dos resultados de
  consistência de [8,12] em lower bounds de provas.

---

## 5. Ataque ao Problema 2.1 (Equipe E)

- A **versão fraca** admitida pelo artigo (`∀i∃y B`, i sharply bounded, y bounded, B aberta)
  é *exatamente* o formato do axioma `∀i<m (¬α_i) ∈ SAT` — logo é a versão certa.
- Decomposição do passo (5) em E1–E5: E1 (`M* ⊨ T_PV`) é grátis (subestrutura de modelo de
  teoria universal verdadeira); E3 (`σ_{i_0}:P⊢α_{i_0}`) transfere na forma universal; o
  núcleo é **E2** (preservação fraca) + **E4** (pertinência dos parâmetros).
- **Ponto frágil levantado**: `Log(M*) = Log(M')` por si só **não** dá `i_0 ∈ M*` —
  "mesmos comprimentos" ≠ "mesmos elementos"; a ser conferido no artigo.
- As duas barreiras (BB e KPT) são **a mesma barreira por dois lados**: fatorar "teoria que
  prova BB" em "`M*` que se comporta como se provasse BB, só para parâmetros de `M`".
- Três estratégias mapeadas com obstáculos honestos: (a) forcing + pseudofinitas com
  preservação de tipos finitos; (b) `M` recursivamente saturado, variante (b')
  `M*∩m = M∩m` (contorno por fechamento, não por teoria); (c) **relaxar `Log` para lista
  finita** `(π, α, z, σ, i_0, …)` → exigência finita/combinatória (**lema de suficiência
  finita** a provar).
- Refutação: uma versão condicional a OWF não traria consequência nova (OWF ⟹ P≠NP é
  elementar); a rota afirmativa é a assimetricamente mais acessível.

**Submais promissor (Equipe E)**: S2+S3 — a versão finita do problema, plano em 3 passos:
(1) conferir no artigo `i_0 ∈ M*`, `Log`, rodapé 2 e [9] e escrever E1–E5 formalmente;
(2) atacar `M*∩m = M∩m`; (3) redigir a versão finita e verificar que o Teorema 4 passa.

---

## 6. Segunda onda — rodadas F–M (10–11 Out 2026)

Metodologia da segunda onda: **frete curto por agente + referee hostile** (todas as
rodadas preservadas em `*_referee.md`); contexto centralizado (`CONTEXTO_COMUM.md`)
para agentes de contexto limpo; cada resultado marcado (A)=fonte/(P)=próprio/
(C)=conjectura; subagentes falhavam com frequência → mitigação: "grave primeiro" +
retomada da mesma sessão (quando falhavam, o orquestrador completava).

### 6.1 A lacuna é real e está em ambas as versões (F, G)

- **F1** (referee 10/10): a lacuna do passo (5) — *"But by (7) i_o is also already
  in M\*"* — está **verbatim** na v4 **e** na v5/LMCS (Teorema 4 → **Teorema 3**).
  A configuração natural de reparo é ZFC-falsa.
- **F2**: lema de suficiência finita (a exigência `Log(M*)=Log(M')` se reduz a uma
  lista finita de comprimentos — versão combinatória do Problema 2.1).
- **F3**: mapeamento de obstáculos O1–O8 para as três rotas de reparo.
- **G1**: **`Log(M[G]) = Log(M)`** (teorema em [Kra98, §4]; (C) para o livro) —
  o forcing booleano **não** cria novos comprimentos de prova; **`(F-b')` refutado**
  (Thm 4.3); errata 9.4.2 do arquivo `09_...`.
- **G2** (obstrução central): `T_PV` + falsificador de `¬φ` + `(F-sent)` é
  **ZFC-falso** (Thm 2.1, rotas (a)/(a′)/(b)/(c); Cor 2.2). Consequência: a correção
  do Teorema 3/4 é a **troca** `2.1 → (F-sent)` — o teorema corrigido é correto como
  condicional, mas sua hipótese trocada é **falsa para a semente** (alvo de reductio).

### 6.2 Q-compactness: o mapa inteiro (H, I, J)

- **H1**: **Thm 1.1 "no-G"** — nenhum `G` do artigo sobrevive ao mecanismo de G2
  (`ν_G` levando `¬φ` **e** `(F-sent)`); redução do problema às variantes (A)/(B).
- **I1** (v5): **A.4–A.6**: nenhum ultrapoder `ℕ^ω/U` modela `S`; **B.1–B.4**: nenhuma
  instância **padrão** de `(S2)–(S4)` com `P` sounde; a venue `M_0 ⊨ S` permanece
  **viva** em C.1; C.2–C.3.
- **J1** (v4): **Teorema K** (incondicional): coleção interna `F` com
  `∀i<m Fals(F(i),α_i)` é **impossível** em todo `M_0` — coerente com, não idêntica
  à remark L442; **K.2**: `T_PV + BB + (S2)(S3)(S4)` é **inconsistente**;
  **J.2′**; **`(Hjoint)`**; **J.6**.
- **J2** (v3): **K-FP′** — o ponto fixo **padrão** existe em todo `M_0 ⊨ T_S`
  (nomes padrão com `R(N)⊆m`); **J.6-a′**: famílias sem `¬φ`; a semântica de `τ_N`
  (R1 vs alternativa) fica **aberta** (pergunta ao autor).

### 6.3 `¬φ` internamente insatisfatível e o destino de C.3 (L)

- **L.1**: **`T_PV+(S4) ⊢ ∀rφ(r)`** — `¬φ` é **internamente insatisfatível** em
  todo modelo (só `(S4)` + sonoridade de `P`; `(r)_i` = i-ésima string da lista).
- **L.1′**: o falsificador de `φ` em `M'` aponta um índice `i_0` onde `(S4)` **falha**
  (`i_0` certificado no verbatim) — **dicotomia de dois chifres**: leitura forte
  ((i) sobre `M'` ou (iii) `M'∩m=M∩m`) ⟹ configuração refutada (G2 2.1(b)/(c); na
  (iii), G1 4.3) ⟹ resposta **negativa** ao Problema 2.1 para a instância ⟹
  `P ≠ NP` (rodapé 2); senão, o passo (5) carece de argumento.
- **L.3′**: **C.3 negativa incondicionalmente** — membros padrão de `𝒯` = só
  constantes-1 (carregador: `τ_N`/`¬φ` ⊇ bits de `α` como constantes, `≥|α|` não-padrão);
  **Lema L.3a**: `α` é não-padrão; **L.3″**: refutações internas não-padrão seguem
  abertas (o adversarial só toca o plano interno).
- **L.4**: Condition 1 + L.1 ⟹ `φ` é internamente válida e **não-provável** — o aviso
  L21–22 (pps pode ser incompleto num modelo de `T_PV`) é **exemplificado pelo próprio
  `φ` do artigo**.

### 6.4 Canto adversarial decidido (M)

- **M.0**: `T_S ⊢` **`m` é não-padrão** (Teorema K + `(S4)` + montagem p-tempo `h`);
  o caso "m padrão" não existe e o contraexemplo `m=2` do referee J2 é **vácuo**.
- **M.1**: **nenhum** `M_0 ⊨ T_S` tem falsificador **global** (contrapositiva de K).
- **M.2 (CONDICIONAL à semântica de `τ_N` — avaliação externa 12/10, P2)**: o
  **seletor p-tempo** `s(v)` = "menor `i<m` com `¬Fals(v,α_i)`" define um
  nome **não-padrão** `N_s`; **`C_{N_s} ≡ ⊥` internamente em todo modelo
  SOB `q` total** (R1 e a alternativa com `q` total) — sob a leitura parcial
  com **merge** o argumento **pode falhar** e o adversarial `(C)` do `J2 §3`
  **abre** (dual de `¬φ`, mecanismo Teorema K). **Enunciado correto:
  condicional à semântica escolhida para `τ_N`** — a pergunta **Q1** da carta
  (enviada 11/10) decide. **Não resumir M.2 sem esta ressalva.**
- **M.3–M.5**: nomes **padrão** nunca são adversariais (guarda `R(N)⊆m` automática
  em todo modelo ⟹ J.6-a′ sem ressalva; famílias internas não-padrão-muitas = `(C)`);
  **duas** condições canônicas `≡ ⊥` na semente (`¬φ` e `C_{N_s}`) = **duas fontes
  independentes de não-compactude**, ambas sem refutação genuína (L.3′).

### 6.5 Nota editorial a Krajíček (`NOTA_EDITORIAL_Krajicek.md` v4)

Rascunho pronto: errata (lacuna em v4 **e** v5; renumeração), **disjunção de dois
chifres** (não modus tollens — G2 refuta (ii)+(8)/(F-sent) em `M'`, não (ii) per se),
obstáculos (G2, K, L.1; §2 como apêndice de 1 página — decisão do usuário), o que
sobrevive (`DD_Res ∈ P`, K-FP′, …), perguntas ao autor (semântica de `τ_N` — **`q`
total?** —; leitura (i)/(iii); convenção de código; Condition 1) e a **carta EN**
curta. Referee 3 rodadas (`NOTA_referee.md`): **pre-comprometeu APROVADO**;
**aguardando revisão do usuário** antes de traduzir/enviar. *(Status: **✅ ENVIADA**
em 11/10/2026 18:14 — ver §7.7.)*

### 6.6 Refutação interna de `{C_{N_s}}` decidida por redução (N)

- **N.1 (redução exata, escopo R1/`q`-total)**: `M_0 ⊨ EF ⊢ σ_s` (com
  `σ_s = δ_{N_s} ∧ ¬τ_{N_s}`) ⟺ `M_0 ⊨ EF ⊢ Taut(α)` — a **sentença fechada**
  `⋀_v(eval(v,α)=1)`. Logo **`{C_{N_s}}` tem refutação EF interna ⟺ a tautologia
  fechada de `α` tem prova EF interna em `M_0`** — *apesar de* **(S3)** dar só
  uma prova de `α` (aberta) em `P`. (Lema N.0: fatos do laço do seletor por-`v`,
  `poly(|α|,|v|)`; fechados `≥ 2^{at(α)}`.)
- **N.2 (dicotomia honesta)**: (α) `EF ⊢ Taut(α)` → refutação interna **existe**
  (2ª fonte de não-compactude colapsa no plano interno; sobrevive a de `¬φ` sob
  Condition 1, no escopo de L.3″) · (β) **(C1′)** `EF ⊬ Taut(α)` → **sem**
  refutação interna — 2ª instância genuína, **sombra interna do aviso L21–22**.
- **N.3**: nenhum chifre decidido em ZFC para todo modelo **(C)** — residuais
  **R-α** (construir `M_0` com (C1′) via omitting types; ultrapoder excluído —
  `I1 A.7`/`B.2`) e **R-β** (comprimir `π` para EF; relação a `EF⊢Taut(α)`
  **indeterminada**). Leitura "π comprime-se" = interpretativa, **não** corolário.
- **Referee** (`N1_referee.md`, 2 rodadas): r1 NÃO RECOMENDADO (FATAL-1: troca
  `Taut(α)`/`α`) → r2 **RECOMENDADO** (teorema, dicotomia e cadeia
  M.2⟸M.1⟸K "matematicamente de pé") com 4 correções aplicadas em **v3**.

---

## 7. Síntese executiva (atualizada com a segunda onda)

**Condicional:** `(Problema 2.1 afirmativo) + (ST) ⟹ NP ≠ coNP` · `¬(Problema 2.1) ⟹ P ≠ NP`
· `(ST)` segue de OWP forte. Gargalo único e real: **Problema 2.1** (equivalente, em espírito,
a obter coleta de testemunhas BB só para parâmetros de um modelo, sem pagar fatoração).

**Incondicional (novo nesta rodada):** `DD_Res ∈ P` com extração de refutação pura de
tamanho ≤ |π| — a propriedade de disjunção viável vale para resolução com `p(t)=t`.

**Formalizado:** totalidade de DD_P, solubilidade em m rodadas e o lema de união de
valorações falsificantes, todos provados em Lean 4 (`lake build` limpo).

**Segunda onda (F–M, referee-processada):**

1. **A lacuna do passo (5) é real** em v4 **e** v5/LMCS; a configuração de reparo é
   ZFC-falsa (G2); a correção certa é a troca `2.1→(F-sent)` — teorema condicional
   correto, **hipótese trocada falsa para a semente**.
2. **O forcing não adianta**: `Log(M[G])=Log(M)` (G1) refuta `(F-b')`; a rota de
   `M` recursivamente saturado descartada (K, v1 retraída).
3. **Teorema K** (J1): coleção interna impossível; `T_PV+BB+(S2)(S3)(S4)` inconsistente.
4. **`T_PV+(S4) ⊢ ∀rφ(r)`** (L.1): `¬φ` internamente insatisfatível — o falsificador
   de `φ` pinça o `i_0` onde `(S4)` falha; **dicotomia de dois chifres** entregue ao autor.
5. **C.3 negativa incondicionalmente** (L.3′); `α` não-padrão (L.3a); `φ` exemplifica
   a incompletude de pps em modelos de `T_PV` (L.4).
6. **Canto adversarial decidido** (M): `m` sempre não-padrão (M.0); sem falsificador
   global (M.1); **`C_{N_s} ≡ ⊥` condicional** (M.2 — **sob `q` total**; sob `q`
   parcial com merge pode falhar → **Q1** da carta) — 2ª fonte de não-compactude
   **se o condicional fechar**; nomes padrão inofensivos (M.3–M.5).
7. **Nota editorial a Krajíček — ✅ ENVIADA em 11/10/2026 18:14**
   (`CARTA_FINAL_ENVIO.md`; para jan.krajicek@protonmail.com e
   krajicek@karlin.mff.cuni.cz) — **aguardando resposta do autor**.
8. **Refutação interna de `{C_{N_s}}` decidida por redução** (N, v3): existe
   ⟺ `Taut(α)` fechada tem prova EF interna em `M_0` (N.1); dicotomia (α)/(C1′)
   (N.2); residuais R-α/R-β **(C)** (N.3). Sombra interna de L21–22 — a mesma
   tensão EF-vs-P do artigo, por dentro.

**Próximos passos recomendados (ordem):**
1. **Aguardar a resposta de Krajíček** (as 4 perguntas da carta delimitam o residual:
   semântica de `τ_N`/`q` total, leitura (i)/(iii), `(8)` em `M′`, Condition 1);
   registrar a resposta no dossiê quando chegar — **com o desfecho de N**: se `q`
   total, a redução N.1 fica firme; se par, o trap M.2 abre e a pergunta cai.
2. Conferir no artigo o ponto frágil `i_0 ∈ M*` (Equipe E, §3(c)) — barato e decisório.
3. ~~Decidir a refutação interna de `{C_{N_s}}`~~ **feito (N)** — ~~pendências
   viraram residuais: R-α e R-β~~ **feito (N2, §8.1)**: R-α = **(∗′)** → frente
   `N3` (compacidade + χ≡⊤); R-β: compressão necessária≠suficiente.
4. ~~Estender `DD_Res ∈ P` para `Res(k)` ou provar `∉ P` sob P≠NP~~ **parcial
   (C2, §8.2)**: C2.1 **teorema** (largura-k); C2.2 = **programa (O1)–(O5)**;
   ingrediente negativo = **família alternante (C)**. Fonte `Res(k)`:
   conferir [K19 5.7].
5. Transferir a análise S-T de [8] para DD_P via estudante P/poly (rota D-(c)).

## 8. Terceira onda — residuais N2, extensão C2 e instâncias Q2 (11/10/2026)

Três entregas derivadas dos abertos da segunda onda, **referee-processadas até
RECOMENDADO** (logs `*_referee.md`):

### 8.1 N2 — residuais R-α e R-β (`N2_residuals_RA_RB.md` v5; referee 5 rodadas)

- **R-α**: a pergunta **é o lema (∗′)** — consistência de `T_S^¬` (compacidade
  é trivial e declarada como tal). A ameaça a `¬∃e Der(e, Taut(α̂))` está
  **classificada em quatro formas** (sem `Der` / conclusão `ValidDer` /
  conclusão `Der` / antecedente vazialmente falso), com slot **`Taut(α̂)`** e
  tuplas de termos; suficência da omissão de `ValidDer` via **(U1)** `Der→ValidDer`
  (universal por construção). **(C)**: (∗′) — construção **não-elementar**
  (extensões elementares forçam o testemunho, `I1 A.7`), rota honesta =
  **compacidade** (`N3`), com o **canto χ≡⊤** (coincidência denotacional
  `g(t̄)^{M_0}=Taut(α̂)`) registrado como exigência.
- **R-β**: compressão `P→EF` dá `EF ⊢ α` (**aberta**) — o passo aberta→fechada
  é **o mesmo bloqueio** de N1 §0.3; logo compressão é necessária (só em
  derivações com (S3)) mas **não suficiente** — todo chifre passa pela montagem.
  `K.2` mata só o **esquema global** `BB`; montagem **particular** = **(C)**.
- **N2.3′** (escopo honesto): sob (∗′) + Σ₁-sonoridade de ZFC: **(i)** modelo
  omitente existe (chifre (β) realizável); **(ii)** o global **efetivo** `G_eff`
  (sobre `T_S^eff` r.e. — `T_PV` é co-r.e. **e Π₁-completo**, logo não r.e.)
  não é demonstrável em ZFC, via completude formalizada + `∃p Proof_{T_S^eff}(σ)`
  (Σ₁) + Σ₁-sonoridade. **Não provado** (declarado): global sobre `T_S` completo;
  o lado **(β)-global não foi excluído** — a dicotomia N.2 segue aberta, com a
  rota "ZFC decide pelo global" bloqueada no escopo efetivo.

### 8.2 C2 — `DD` para `Res(k)` (`C2_ddres_k.md` v5; referee 5 rodadas)

- **C2.1 (teorema, aceito)**: o algoritmo do Teorema 4.3 é **agnóstico de
  largura** — vale para resolução de **largura-k**, preservando-a (`E_i⊆D_i`);
  bound `O(|Π|²+|Π|·m)`; `DD_{Res^{≤k}} ∈ P`; FDP fraca `p(t)=t`. Distinção
  largura-`Res(k)` provada **só para FDP**; `DD` de `Res(k)` segue **aberto**.
- **C2.2 = PROGRAMA (C)** — **rebaixamento honesto** após 4 rodadas de fato
  novo na mecânica do recorte: as 4 objeções do referee viraram **obrigações
  abertas (O1)–(O5)**: pai correto no fallback do pivô-perdido (fim em `∅`),
  fechamento do passo final na promessa, dependentes de linhas eliminadas
  (corte e ∧-intro, inclusive (r5) com ambos os pais), estricidade do
  truncamento, objeto/ordem únicos. `Res(1)`: só **sob promessa (C)**.
- **C2.3 (ingrediente corrigido + redução)**: a v1 tinha ingrediente
  **logicamente impossível** (Λ₂ sempre sat ⟹ Λ₁ sempre insat) e espantalho
  DNF/CNF trocado (`TAUT_DNF` é coNP-completa). Corrigido: **família
  alternante** — exatamente **um** lado insat, alternando com `γ`, união com
  refutação pequena — decide `UNSAT_CNF` via solver de `DD` (decodificação
  total). [Gar24] dá dois lados insat — a alternância é **o problema exato (C)**.

### 8.3 Q2 — instâncias `(τ_n,q)` para o Teorema Q (`Q2_instancias_tau_n_q.md` v3; referee 3 rodadas)

- **Q2.1 (decidido; enunciado com Gödel II)**: **(Q) full-range + `τ_n(Con(T))∈TAUT`
  é impossível** para `T` r.e. com `T ⊬ Con(T)` (ex.: `T ⊇ Q`) e `P` completo —
  Gödel II em 1 linha. **Mas** o C2 da v1 ("só degeneradas") era **falso**:
  existe instância full-range **computável não-degenerada** (`τ_n(φ)=⊤` sse PA
  tem prova ≤ n; `q=n`) que satisfaz (Q) e **transfere trivialmente** —
  diagnóstico correto: full-range não é impossível, é **inócuo**.
- **Q2.2 (instância Σ₁ corrigida)**: `(Q)|_{Σ₁}` vale com `τ_n` **total**
  (⊥ fora do range; cutoff de testemunha `n^{c₀}`), tamanho honesto
  `|τ_n(φ)| = 2^{p(n)}` (não poli — a v1 era falsa), verificação/sonoridade
  citadas [Bus97]/[K19], ponte = implicação única via lema de correção
  limitada. `q(n,m)=(n·m)^c`.
- **Q2.2′**: corolário **só com** a hipótese `τ_n(φ_n)∈TAUT` (testemunhas
  curtas + `⌢φ_n⌝≤n`); **três modalidades** de não-contente declaradas (cutoff
  de Gödel; testemunha longa ⟹ vacuidade; bound trivial `2^{p(n)}`).
- **Q2.3** (sanity check): τ sintática computável, transfere zero. **Q2.4**:
  PH/Goodstein violam **provabilidade** (não a ponte); contagem não dá limites
  superpolinomiais — rota viva = versões `IΣ_k` (**(C)**: fonte Σ₁ não
  localizada; revisão K19/KP90 pendente).

### 8.4 Balanço das três

| Entrega | Veredito | Fecho | Residual |
|---|---|---|---|
| N2 | RECOMENDADO (r5) | classificação da ameaça; (U1); N2.3′ no escopo efetivo | (∗′)=R-α **(C)** → `N3` |
| C2 | RECOMENDADO (r5) | C2.1 teorema; C2.3 redução+ingrediente | C2.2 **programa (O1)–(O5)**; alternância **(C)** |
| Q2 | RECOMENDADO (r3) | Q2.1 decidido; Q2.2 corrigida e citada | fonte Σ₁ **(C)** (K19/KP90) |

## 9. Avaliação externa de 12/10/2026 — resposta e regime de apresentação

> Resposta pontual completa: `CRITICA_EXTERNA_2026-10-12.md` (2ª onda; a 1ª em
> `CRITICA_EXTERNA_2026-10-11.md`). A avaliação **reconhece** a melhoria
> metodológica (README, retrações, estrutura DD_P, lacuna concreta, honestidade
> da frente N) e dá o direcionamento: *não adicionar mais conjecturas; obter
> **auditoria externa independente** de `DD_Res ∈ P` e das frentes G–N, além de
> **compilação Lean reproduzível***.

### 9.1 Três níveis de resultado (avaliação P5 — regra de leitura obrigatória)

| Nível | O quê | Exemplos | Status |
|---|---|---|---|
| **L1** | Teoremas sobre **fórmulas/resolução** (proposicionais) | `DD_Res ∈ P` (T4.3); C2.1 largura-k; tautologia/dicotomia de `α` | prova escrita; **`DD_Res` com auditoria externa pendente** |
| **L2** | Resultados **internos a modelos não-padrão** de `T_PV` | K, K.2, L.1, L.3′, M.0–M.5, N.1, (∗′), `G_eff` | argumentos próprios **condicionais** |
| **L3** | Consequências p/ **NP, coNP, geradores, complexidade** | `NP≠coNP`, `P≠NP`, lower bounds, p-boundedness | **só condicionais explícitas** (`(2.1)+(ST)⟹NP≠coNP`; `¬(2.1)⟹P≠NP`) |

**A ponte L2→L3 NÃO foi demonstrada.** Uma fórmula internamente insatisfatível
ou uma coleção impossível num modelo **não** produz lower bound computacional.
Esta ponte é o **aberto de maior peso** do projeto e nenhuma leitura do
repositório pode saltá-la.

### 9.2 O que foi aplicado hoje (12/10)

1. **Terminologia (P1)**: "RECOMENDADO" = **revisão interna estruturada**, nunca
   validação externa — fórmula padronizada no §0 acima, no `README.md` e no
   `INDICE.md`.
2. **M.2 condicional (P2)**: condicionalidade à semântica de `τ_N` (`q` total ×
   `q` parcial com merge) explicitada em **todos** os resumos (§6.4, §7.6, README
   item 5, INDICE DD7) — **Q1** da carta decide.
3. **Compilação reproduzida (P3)**: `lake build` na raiz **em 12/10/2026** →
   `Build completed successfully (4 jobs)`, com exatamente os **2 `sorry`s**
   documentados (`lean4/Gothic_Generators/DDP.lean:628` e `:690`); nenhum `sorry`
   em `FoundationBridge/`. Instruções de reprodução em `README.md`
   (§Formalização) — basta `elan` (a toolchain `v4.34.0` baixa sozinha).
   **Escopo honesto**: o Lean cobre o **núcleo proposicional** de `DD_P` —
   **não** formaliza p-time, O(1) rodadas, p-boundedness, NP≠coNP, o Problema 2.1
   nem modelos não-padrão.
4. **PPR reclassificado (P4)**: PPR-2/RBT/CC-Θ = **verificados no modelo finito
   escolhido** (`R_W=4`, `W_STAR='00'`, ramos artificiais; `cond_C =
   (w0_Tp is None)` é propriedade **do modelo finito**) — **não** evidência de
   redução entre geradores de provas reais. Caixa permanente em
   `EVOLUCAO_PROJETO.md`.
5. **Pacote de auditoria (P6/P10)**: `AUDITORIA_EXTERNA_DDRES_G-N.md` — dossiê
   autossuficiente com o enunciado (T4.3/L4.1/L4.2), a **prova em 5 passos**, o
   **checklist exato** (recorte×enfraquecimento em todas as variantes; DAG;
   pureza; **tensão `O(|Π|·m)` × `O(|Π|²)` reconhecida**), a tabela das frentes
   G–N com o que checar em cada uma, o que **não** é reivindicado, e a logística.

### 9.3 O que a avaliação NÃO altera

- Nenhum resultado foi **alterado** — apenas a **apresentação** ficou mais
  precisa (condicionais explícitos; níveis separados; revisão interna nomeada).
- As **retrações** do Eixo 1 permanecem; os positivos reconhecidos permanecem.
- **Próximo passo decisivo** = auditoria externa (vias em
  `AUDITORIA_EXTERNA_DDRES_G-N.md` §E; MathOverflow segue **congelado** até
  confirmação) + avançar os abertos internos na ordem: resposta de Krajíček →
  `N3` → [K19 5.7]/família alternante → fonte Σ₁ (Q2.4).

# Pacote de auditoria externa — `DD_Res ∈ P` e frentes G–N

> Documento próprio **(P)**, 12 Out 2026. Dossiê **autossuficiente** para um
> auditor independente (externo ao projeto) verificar os principais resultados da
> campanha DD_P sobre **Krajíček, arXiv:2506.20221v4/v5 (LMCS 22(2:14)2026)**.
> Gerado pela avaliação externa de 12/10/2026 (`CRITICA_EXTERNA_2026-10-12.md`,
> P6/P10): *"o próximo passo decisivo é obter uma auditoria externa independente
> da prova de `DD_Res ∈ P` e das frentes G–N"*. **Status de todos os itens
> abaixo: revisão interna estruturada (logs `*_referee.md`); NENHUM é
> validado externamente.** Marcação: **(A)** = artigo/fonte, **(P)** = prova
> própria, **(C)** = conjectura/aberto.

## §A. `DD_Res ∈ P` — Teorema 4.3 (`C_disjuncao_viavel.md` §2)

### A.1 Enunciado (verbatim, citado da fonte)

> **Lema 4.1 (B) — recorte.** Para refutação `Π` de `Λ` por resolução **com
> enfraquecimento**, algoritmo calcula `E_i ⊆ D_i` tal que: (a) inclusão; (b)
> `(E_1,…,E_s)` é derivação de `Λ` por **resolução pura** com `E_s = ∅`;
> (c) `|E_i| ≤ |D_i|` e custo `O(|Π|²)` no pior caso.
>
> **Lema 4.2 (B) — pureza.** Se `Λ = Λ_1 ⊎ ⋯ ⊎ Λ_m` com `Λ_i` sobre átomos
> disjuntos `X_i` e `(E_1,…,E_t)` derivação **pura** de `Λ` com `E_t = ∅`,
> então (1) toda linha é **pura** (variáveis de um único `X_i`); (2) os pais
> de `E_t = ∅` são puros sobre o **mesmo** lado `i*`.
>
> **Teorema 4.3 (B) — `DD_Res ∈ P`, sub-prova ótima.** Dado `Λ = ⨄_{i<m} Λ_i`
> puro e `Π` refutação de `Λ` (com/s enfraquecimento, tree/dag), devolve em
> `O(|Π|·m)` um `i*` com `Λ_{i*}` insatisfatível **e** refutação pura de
> `Λ_{i*}` com ≤ `|Π|` linhas — logo FDP com `p(t) = t`.

### A.2 Prova em 5 passos (para auditor)

1. Lema 4.1 → refutaçãopura `E` de `Λ`; 2. caso `∅` = linha-axioma → devolve o
lado; 3. senão `∅` = resolvente de `E_a ∋ l`, `E_b ∋ ¬l` → ambos puros sobre
`i*` (Lema 4.2); 4. restringe às linhas **acessíveis** a partir de `∅` (pais de
resolução + linha-fonte no caso cópia/DAG) — indução retroativa mantém pureza e
folhas ∈ `Λ_{i*}`; 5. linhas acessíveis deduplicadas = refutação pura de
`Λ_{i*}` terminando em `∅` (≤ |Π| linhas).

### A.3 CHECKLIST — o que o auditor deve checar (os pontos nomeados pela avaliação)

- **(a) Recorte × enfraquecimento, em TODAS as variantes.** O Lema 4.1 cobre
  `de C derive C ∨ D` (apresentação de [Pap26]). Verificar: a regra de
  enfraquecimento usada no artigo/na literatura é exatamente esta? Há variantes
  (enfraquecimento em DAG com reuso; cláusulas-duplicatas; resolução
  "à la Davis–Putnam") que escapam? **O próprio texto reconhece** (§2.2
  comentários): *"o ponto delicado (enfraquecimento) é resolvido pelo Lema 4.1,
  que não é discutido nas fontes que consultamos"* — **é este o ponto de maior
  peso**.
- **(b) DAG.** O passo 4 reconstrói dependências incluindo "cópias" (reuso).
  Verificar: em DAG com reuso múltiplo, a restrição às acessíveis preserva
  **cada** inferência e o deduplicamento não corrompe justificações?
- **(c) Pureza (Lema 4.2).** Indução padrão — conferir o caso `(2)` para o
  resolvente final `∅` e a indução retroativa do passo 4 (folhas acessíveis
  pertencem mesmo só a `Λ_{i*}`?).
- **(d) Complexidade (tensão a resolver).** O **Teorema 4.3** afirma
  `O(|Π|·m)`, mas o **Lema 4.1(c)** declara custo `O(|Π|²)` no pior caso —
  o total honesto é `O(|Π|² + |Π|·m)` (é o bound usado em `C2_ddres_k.md`).
  **Tensão interna reconhecida — o auditor deve arbitrar.**
- **(e) Limite honesto já declarado**: o algoritmo garante **um** lado (`i*`);
  lado insatisfatível **não** precisa ter refutação dentro de `Π` (exemplo no
  §2.3 comentarios da fonte).

### A.4 O que NÃO se reivindica aqui

`DD_Res ∈ P` é um teorema sobre **resolução proposicional** (nível L1, §C). **Não**
é um lower bound, não decide `DD_P` (o problema geral segue **aberto**), não
toca NP≠coNP. A extensão `Res(k)` (k-DNF [Gar24]) **não** está provada — virou
**programa** com obrigações (O1)–(O5) (`C2_ddres_k.md`, referee 5 rodadas).

### A.5 Sanidade computacional (não é prova)

Teste do algoritmo de projeção em 3000 instâncias sintéticas: 3000/3000
corretos (`C_disjuncao_viavel.md` §experimentos). **Sanity check apenas** — o
texto já declara: "os experimentos não provam nada".

## §B. Frentes G–N — uma linha por frente, status e o que checar

| Frente | Enunciado (status) | O que o auditor checa |
|---|---|---|
| **F1** | Lacuna **verbatim** no passo (5): "But by (7) `i_o` is also already in M∗" — igualdade de comprimentos de `Log` não implica `i₀ ∈ M*` **(A)+leitura**; vale em v4 **e** v5/LMCS | Confrontar com arXiv:2506.20221v4 e v5; é a mesma lacuna? |
| **G1** | `Log(M[G]) = Log(M)` no forcing de Kra95/98 → **`(F-b')` refutado (P)** | O argumento de filtragem do forcing transfere mesmo com o predicado de observabilidade? |
| **G2** | Configuração de reparo `T_PV`+falsificador+`(F-sent)` é **ZFC-falsa** (reductio, "Teorema 2.1"); `R3 ≡ BB` (§2.3) **(P)** | A reductio usa só o que a semente de fato tem? |
| **H1** | Sem coleção sharply-bounded disponível para a refutação; convenção de abertas (§1.3) **(P)** | A indisponibilidade de BB é mesmo necessária? |
| **I1** | Ultrapoderes **não servem** — Łoś transfere sentenças (`A.7`) **(A)+(P)** | A aplicação de Łoś está correta no nosso uso? |
| **J1** | **Teorema K**: em todo `M_0 ⊨ T_PV+(S2)(S3)(S4)` não existe `F` com `∀i<m Fals(F(i),α_i)` (⇒ `m` não-padrão); **K.2**: `T_PV+BB+(S2)(S3)(S4)` **inconsistente** **(P)** | Núcleo do projeto — verificar a diagonalização de K e a montagem/coleta morta de K.2 |
| **J2** | **K-FP′** (consequência formal de K) **(P)** | Corolário formal corretamente derivado? |
| **L1** | **L.1**: `T_PV+(S4) ⊢ ∀rφ(r)` (`¬φ` internamente insatisfatível); **L.3′**: C.3 negativa incondicionalmente; **L.3a**: `α` não-padrão; **L.4**: `φ` exemplifica a incompletude de pps **(P)** | A prova de L.1 (pinça do `i_0`) e o alcance de L.3′ |
| **M** | **M.0**: `m` não-padrão; **M.1**: sem falsificador global; **M.2**: `C_{N_s} ≡ ⊥` **condicional à semântica de `τ_N`** (fecha sob `q` total (R1 e alternativa); **pode falhar** sob `q` parcial com merge — Q1 da carta); **M.3**: nomes padrão inofensivos **(P), condicionais** | **M.2 NÃO é incondicional** — checar o condicional; Q1 da carta decide |
| **N1** | **N.1**: refutação interna de `{C_{N_s}}` ⟺ `M_0 ⊨ EF ⊢ Taut(α)` (**sentença fechada**; escopo R1/`q`-total); **N.2**: dicotomia (α)/(C1′); **N.3**: residuais **(P)**, condicionais | A redução N.1 (seletor `s(v)`, `σ_s`); convenção aberta→fechada |
| **N2** | **R-α = lema (∗′)** — construção **não-elementar**, rota compacidade **(C)**; ameaça a `¬∃e Der(e,Taut(α̂))` em 4 formas; **N2.3′**: modelo omitente + `G_eff` não-demonstrável **sobre `T_S^eff`** (Σ₁-sonoridade); lado (β)-global **não excluído** **(P)+(C)** | (∗′) é o aberto; a rota Σ₁ (completude formalizada) — e a ressalva co-r.e. de `T_PV` |
| **C2** | **C2.1** (teorema, subclass de largura-k); **C2.2** = **programa** (obrigações (O1)–(O5)); **C2.3**: família **alternante (C)** | Ver §A (a mesma auditoria cobre C2.1); (O1)–(O5) estão no `C2_ddres_k.md` |
| **Q2** | **Q2.1**: (Q) full-range + `τ_n(Con T)∈TAUT` ⟹ `T ⊢ Con(T)` — **impossível** (Gödel II); instância full-range computável transfere **trivialmente**; **Q2.2**: `(Q)|_{Σ₁}` vale (τ total, cutoff, `|τ|=2^{p(n)}`) **(P)** | O enunciado de (Q) em `27_TEOREMA_Q_...md` vs Q2.1; a ponte Σ₁ |

**Condicionalidade geral (avaliação P7)**: K, L, M, N são **argumentos próprios
condicionais** — nenhum é "estabelecido externamente"; os condicionais estão
tabela acima e em cada arquivo de frente.

## §C. O que NÃO é reivindicado (nível de resultado — avaliação P5)

- **(L1) teoremas sobre fórmulas/resolução**: `DD_Res ∈ P` (§A), corolários de
  largura-k, tautologia/dicotomia de `α`.
- **(L2) resultados internos sobre modelos não-padrão de `T_PV`**: K, L, M, N,
  (∗′), `G_eff` — valem **dentro** dos modelos da semente.
- **(L3) consequências p/ NP, coNP, geradores, complexidade**: **a ponte L2→L3
  NÃO foi demonstrada**. Uma fórmula internamente insatisfatível ou uma coleção
  impossível num modelo **não** produz lower bound computacional. As únicas
  consequências de complexidade afirmadas são **condicionais e explícitas**:
  `(Problema 2.1)+(ST) ⟹ NP ≠ coNP`; `¬(Problema 2.1) ⟹ P ≠ NP`
  (`RELATORIO_CONSOLIDADO.md` §7).
- **Nenhum** lower bound provado; **nenhum** P≠NP afirmado; **PPR/RBT/RCS** =
  programa experimental **no modelo finito escolhido** (R_W=4, `W_STAR='00'`);
  **Lean** formaliza só o núcleo proposicional (não p-time, não NP≠coNP).

## §D. Logística para o auditor

1. **Build (reproduzido em 12/10/2026)**: instalar `elan` → `lake build` na
   raiz (`lean-toolchain` pin `leanprover/lean4:v4.34.0`); esperado: sucesso com
   **2 `sorry`s** documentados (`lean4/Gothic_Generators/DDP.lean:628` e `:690`).
   O Lean cobre o **núcleo proposicional** de `DD_P` (totalidade, `m` rodadas,
   lema de união) — **não** o Teorema 4.3, que é prova escrita (§A).
2. **Logs de crítica interna**: `krajicek_ddp/*_referee.md` (uma por entrega;
   N2 = 5 rodadas, C2 = 5, Q2 = 3, N1 = 2…). São **revisão interna** —
   não substituem esta auditoria.
3. **Fontes primárias**: `krajicek_ddp/C_disjuncao_viavel.md` (§A),
   `RELATORIO_CONSOLIDADO.md` (§6–8), as frentes G–N (tabela §B),
   `INDICE.md` (DD1–DD12 + DESCARTADOS D1–D6).
4. **Retrações**: os resultados do Eixo 1 (escala exponencial, teoremas 1–6,
   MCSP/IPS) estão **retraídos** (`INDICE.md` DESCARTADOS; banners) — não
   auditar como válidos.
5. **Contato**: euambiente@gmail.com · github.com/ebiossanto. Carta a Krajíček
   **enviada 11/10/2026** (Q1–Q4), resposta aguardada. MathOverflow segue
   **congelado** até confirmação do autor.

## §E. Vias sugeridas de auditoria externa (a cargo do autor)

1. **Krajíček** (aguardando — Q1 decide o condicional de M.2/Q1 e o escopo de N).
2. **Especialista indicado** (lógica/proof complexity) com este dossiê como
   ponto de partida — §A.3 é o contrato de auditoria.
3. **MathOverflow** (rascunho `27_MATHOVERFLOW_PERGUNTA.md` — **só com
   confirmação do autor**; a avaliação sugere adendo factual).

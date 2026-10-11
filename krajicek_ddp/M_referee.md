# Referee hostile — `M_canto_adversarial.md` (texto final)

> Referee independente, 11 Out 2026. Esqueleto gravado **antes** da leitura (procedimento
> cumprido); este é o texto final. Marcação: **(A)** = fonte, **(P)** = próprio, **(C)** = conjetura.
> Fontes conferidas: `J2_ponto_fixo.md` (§1, §3, K-FP′, §5), `J1_Qcompactness_M0.md` (§3 Teorema K,
> K.2, §7), `L1_phi_insatisfativel.md` (L.1, L.3′, L.3a, L.3″), `H1_colecao_refutacao.md` §1.1,
> `G2_semente_Fsent.md` §2.2, `A_teoremas_exatos.md` (§1.0, §1.2, §1.12, L341), `I1_...` (Lema B.1,
> B.3), `J2_referee.md`, `F2_versao_finita.md` (§0: axiomas (S1)–(S4)).

## VEREDITO: **REVISION** (0 FATAL, 5 MAIOR, 8 MENORES)

O núcleo está **correto**: M.0 (m não-padrão), M.1 (sem falsificador global) e M.2
(`C_{N_s} ≡ ⊥` via seletor p-tempo) resistem ao ataque — **com três passos de justificativa
errados ou omitidos que precisam ser reescritos** (M-1, M-2, M-3), um escopo superestimado
(M-4) e uma conclusão §6 mais forte que a ressalva §2 (M-5). Nada derruba a tese; tudo é
reparável no lugar. Com as 5 correções: **RECOMENDADO**.

---

## FATAIS

**Nenhum.** Justificativa (procurado com cuidado):
- M.0 **não** é falsa: a colagem é legítima — a correção é por **montagem p-tempo** a partir de
  `α` e da tupla padrão-finita `⟨y_i⟩_{i<m}` (custo `O(|y|·m·poly(|α|))`, `m ≤ |α|` **(A)** §1.2),
  não por "montagem finita" — ver M-1. O lema é **verdadeiro**, a frase de suporte é falsa.
- M.1 **não** viola o Teorema K (é o inverso: deriva `F ∈ M_0` para **contradizer** K): a coleção
  aqui é **p-tempo** (`i ↦ y↾A_i` deriva-se de um **único** `y`), ao contrário da coleção
  `∀i<m∃y` (escolha) que a v1 do K-FP ilegitimamente prensificava (J2 FATAL-1/2).
- M.2 **não** colide com K-FP′ (hipótese: `N` **padrão**; `N_s` não-padrão — §2 Obs., correta) nem
  com G2 Thm 2.1 (`τ_{N_s} ≡ 0` é coerente: para o índice `ν_G(N_s)` (novo) não há proteção
  `(S4)` — G2 §2.3 diz literalmente isso).
- `m ≤ |α|` é **(A✔)** verbatim (`A_...` §1.2: "*`m` is bounded by the size of the formula*") —
  o laço do seletor é p-tempo legítimo; só a **citação** está trocada (M-3).

---

## MAIORES

### MAIOR-1 — M.0(b): "`A_i := at(α_i)` é padrão-finito (dados padrão)" é **falso**
**Local:** M.0, linha 36 (também linha 40 "dado `i`, `at(α_i)` é calculável p-tempo" — essa está
certa; o erro é o parêntese "(dados padrão)").

**Argumento.** `i` padrão não dá dado padrão: `α` é **não-padrão** (Lema L.3a **(A+P)**). Sob a
hipótese `m` padrão, `|α|` não-padrão força (soma de padrão-muitos termos) algum `α_i` com `i < m`
**padrão** e `|α_i|` **não-padrão** ⟹ `at(α_i)` **não** padrão-finito. É exatamente a aplicação
proibida de J.0(a) ("entrada padrão ⟹ saída padrão"): aqui a entrada `(α,i)` **não** é padrão.
A frase "união padrão-finita de elementos de `M_0` ⟹ `y ∈ M_0` (montagem finita)" não se sustenta.

**Correção (a prova fecha):** reescrever o passo como montagem **p-tempo**: `y := h(α, ⟨y_i⟩_{i<m})`,
com `h` varrendo `x` e testando `x ∈ at(α_i)` para `i < m` (predicado p-tempo declarado em J1 §3);
`tupla ⟨y_i⟩_{i<m}` padrão-finita (`m` padrão) ⟹ ∈ `M_0`; custo `O(|y|·m·poly(|α|)) ≤ poly` porque
`m ≤ |α|` **(A)** §1.2; `(S2)` garante não-conflito. O restante da prova (escolha metateórica sobre
`i` padrão, localidade, nota de não-circularidade, linhas 44–45) está **correto**.

**Nota de mérito:** M.0 é **forte** e **novo** (generaliza o Lema B.1 do I1, que é só para
**instância padrão**, ao caso `α,π` não-padrões com `m` padrão; e é mais forte que L.3a: `m`
não-padrão, não só `|α|`). **Falta citar B.1/I1 como antecedente** (prior art não referenciado).

### MAIOR-2 — M.1: o passo "`F(i) := y↾A_i` p-tempo em `y` ⟹ `F ∈ M_0`" omite a coleta
**Local:** M.1, linha 51.

**Argumento.** `F` precisa ser **um código de lista de comprimento `m`** (é assim que o Teorema K
quantifica: `F ∈ M_0` com `(F)_i`, ver J1 §3 — K não põe restrição p-tempo sobre `F`; portanto a
"restrição p-tempo" citada em M.0(c)/checklist nº 3 é **irrelevante**, não é a hipótese de K —
corrigir a redação: o que se exige é só `F ∈ M_0`). "Função p-tempo em `i`" **não** dá sozinha a
existência do **código** da grafia sobre domínio não-padrão `i<m` — é exatamente o tipo de passo
que foi retratado aqui (J1 v2 "compreensão limitada" → MAJOR-R3) e o tipo que matou o K-FP v1.

**Correção (o passo é verdadeiro — escrevê-lo):** `F := h(y,α)` com `h` p-tempo montando
`⟨y↾at(α_i) : i<m⟩`; tamanho de saída `m·|y| ≤ |α|·|y|` (**polinomial**) e custo `m·poly(|α|+|y|)`
— logo `h` é p-tempo e `F ∈ M_0` por fechamento de `M_0 ⊨ PV`. A diferença crucial para com o
FATAL-2 da J2 deve ser dita: aqui **não há escolha** (`∀i∃y`); todos os membros derivam de **um
único** `y` — daí a coleção ser p-tempo e legítima. O resto de M.1 (contrapositiva de K,
localidade `Fals(y↾A_i,α_i) ⟺ Fals(y,α_i)`, linhas 54–56) está **correto**.

### MAIOR-3 — M.2(a): `m ≤ poly(|α|)` **não** está em G2 §2.2, e a marcação **(A)** é trocada
**Local:** §2 linha 62; checklist nº 5 (linha 143); §6 linha 170.

**Conferido:** `G2 §2.2` (linha 104) diz "**tamanhos internos ≤ `poly(|α|)`**" das condições `τ_N` —
**não** `m ≤ poly(|α|)`; e G2 é **(P)** (sua própria nota de autoria), jamais **(A)**. A fonte certa
é `A_teoremas_exatos.md` **§1.2 (A✔)**: "*`m` is bounded by the size of the formula*" ⟹ `m ≤ |α|`
(usado assim em J1 §3 `O(m·|α|)`, I1 B.3(ii), A §2.1). A afirmação é **verdadeira** (até mais forte);
é a **citação** que é falsa.

**Correção:** "`m ≤ |α|` por `A_... §1.2` **(A✔)**" nas três ocorrências. Corrigir também nº 5 da
checklist ("Onde"). **Consequência:** o laço `i<m` é p-tempo **legítimo** (verificado: `m(α)`
calculável p-tempo pela estrutura de `α`; cada teste `Fals` p-tempo; totalidade com default —
explicitar o default, senão `s` não é PV-total e `δ_{N_s}` não está definido como circuito).

### MAIOR-4 — M.3(b)/M.3(c): escopo de J.6-a′ superestimado — famílias **internas** ficam de fora
**Local:** linhas 100–107 (e §0 item 4, linha 24–27: "nomes padrão **nunca** são adversariais").

**Argumento.** J.6-a′ cobre "**família finita-padrão (externamente finita)** de nomes padrão"
(J2 §3). A fronteira `(C)` de J2 §3 (i) é sobre **compatibilidade conjunta entre vários `N_j`**, e
`(Hjoint)`/J.6 quantificam sobre famílias **interna**-mente finitas. Uma família **interna** de
comprimento **não-padrão** com nomes **padrão** (ex.: lista `⟨N_j : j<k⟩`, `k` não-padrão, em `M_0`)
**não** é coberta: o construtor-joint juntaria `g_i` sobre `R_joint` **não-padrão-finito** —
literalmente a coleção proibida por K. Logo: (i) "par adversarial **mesmo padrão**" está
**decidido** (impossível ✓ — é o que J2 §3 pedia); (ii) "nomes padrão **nunca** são adversariais"
é **verdadeiro** para nomes isolados/pares e famílias externamente finitas, e **aberto** para
famílias internas não-finitas-padrão.

**Correção de M.3(c):** manter "**o ramo vazio exige nomes não-padrões**" — essa parte está
**correta** e é um ganho real (`code` padrão-tamanho é padrão; `m` não-padrão por M.0 ⟹
`R(N) ⊆ m` sempre; logo `R(N) ⊄ m` é impossível para `N` padrão ✓ — o referee concorda, e o
contraexemplo `m=2` fica **vácuo** ✓). Mas escrever a fronteira como: "*ramo vazio ⟺ nomes
não-padrões; compatibilidade conjunta de famílias **internas** não-finitas-padrão permanece (C)*".
A frase "a fronteira não é ramo vazio, é nomes não-padrões" **parcialmente** corriges J2 §3 — ela
resolve o ramo vazio e **silencia** o lado "entre vários `N_j`".

### MAIOR-5 — §6/§0: "o corner sobrevive sob **ambas** as leituras" derruba a própria ressalva §2
**Local:** §6 linha 158; §0 item 3 (linhas 20–23, `C_{N_s} ≡ ⊥` afirmado **sem** ressalva).

**Argumento.** §2 (linhas 79–83) marca corretamente que, na leitura alternativa com `q` **parcial**
(merge), "o trap **pode** abrir". §4 repete com "(com a ressalva parcial de §2)" ✓, mas §6 e §0
afirmam incondicionalmente. O veredito não pode ser mais forte que a ressalva.

**Correção:** em §0.3 e §6: "`C_{N_s} ≡ ⊥` **sob R1 e sob a alternativa com `q` total**; na
alternativa com merge parcial, **pendente** da pergunta ao autor (`q` é atribuição total?)".

---

## MENORES

1. **M.2(b) — não-padrão de `N_s` justificado errado** (linhas 64–65): "tamanho `poly(|α|)`" é
   **cota superior** — cota superior não força não-padrão (pode ser0). Razão correta: `ℓ = ⌈log m⌉`
   com `m` **não-padrão** (M.0) ⟹ `ℓ` não-padrão ⟹ `N_s` não-padrão. Acrescentar: `N_s ∈ M_0`
   (construção p-tempo de `α`: unrolling do laço `m·poly(|α|)` dá circuito de tamanho `poly(|α|)`;
   hardwiring de `α` não-padrão é legítimo — circuito interno pode ter tamanho não-padrão; as
   entradas são os átomos de `p` ⊇ átomos de `α` por H1 §1.1/S2 — os "circuitos sobre `p`" estão
   corretos).
2. **M.2(d) — composicionalidade da big-or** (linha 75): "cada disjuncto falha ⟹ `τ ≡ 0`" é correto
   para o **circuito-OR construído**, mas J1 §3 passo 2 precisou do item (iv) para o mesmo passo —
   citar avaliação p-tempo absoluta (G2 §2.4(a′)) e dizer que `τ_{N_s}` é OR **construído**.
3. **M.2 herda o impasse de tamanho de `τ_N`** (J2_referee MAIOR-1(iii): disjunção sobre
   `2^{|p|}` `q`'s vs cota `poly(|α|)` de G2 §2.2): **não afeta** a verdade de `τ ≡ 0` (cada
   disjuncto falha, seja qual for o limite), mas **afeta** se `C_{N_s}` é condição de forcing
   "legítima" no sentido de G2 §2.2 — **não marcado em M**; acrescentar em "Lacunas honestas".
4. **§2 Obs. — "`R(N_s)` não-padrão-muitos"** (linha 87) afirmado sem prova. É **verdadeiro**:
   se `R(N_s) ⊆ {0,…,k}` (`k` padrão), colha `y_0,…,y_k` por `(S4)`, amalgame `σ*` por `(S2)`
   (padrão-finito ⟹ ∈ `M_0`) — `σ*` falsifica `α_0..α_k` ⟹ `s(σ*) > k`, contradição. Inserir as 2
   linhas. O resto da Obs. (sem colisão com K-FP′; ponto fixo para `N_s` não existe: `code(N_s,q*)=s(q*)`
   e `¬Fals(q*,α_{s(q*)})`) está **correto**.
5. **M.2(e) — ressalva do merge: marcada honestamente** ✓ (linhas 79–83). Só §6/§0 não a guardam
   (MAIOR-5).
6. **Checklist §5:** nº 1 — (S2)/(S4) verbatim em `A_...` §1.12(2) ✓; nº 4 — K em `J1` §3 ✓; nº 3
   — "restrição p-tempo" não é o que K exige (ver MAIOR-2); nº 5 — fonte trocada (MAIOR-3);
   nº 8/10/11 honestos ✓.
7. **Typos/idioma:** "vacuo" → **vácuo** (linha 25); "daría" → **daria** (linha 129);
   "formalizado differently" → **"formalizado de modo diferente"** (linha 172); "krajicek" →
   **Krajíček** (linha 163).
8. **§7** diz "referee hostile pendente" — atualizar para concluído.

---

## O QUE ESTÁ CORRETO (declarado)

- **M.0 (conclusão): CORRETO** — `T_S ⊢ "m é não-padrão"`; escolha sobre `i` padrão legítima
  (mesma forma de K-FP′ passo 1); localidade de `Fals` universal ∈ `T_PV` (J1 §3 passo 1);
  nota de não-circularidade (linhas 44–45) **correta**: com `m` não-padrão a colagem cobre só `i`
  padrão e nada se conclui. **Novo e forte** — provar com a correção M-1.
- **M.1: CORRETO** — contrapositiva de K; `F` arbitrário ∈ `M_0` (K não restringe `F` a p-tempo);
  localidade `⟺` ✓.
- **M.2 (núcleo): CORRETO** — seletor total (M.1) e p-tempo (`m ≤ |α|` **(A)**); `code(N_s,v)=s(v)`
  para **todo** `q` interno (mesma convenção de leitura-além-como-0 em `Fals` e nos circuitos);
  `δ ≡ 1` ✓; `τ ≡ 0` disjunção-a-disjunto sob a leitura diagonal (R1 / alternativa-total) ✓;
  ressalva do merge marcada ✓; Observação sem colisão com K-FP′ **correta**.
- **M.3(a): CORRETO** (depende de M.0). **M.3(b) para nomes isolados/pares e famílias externamente
  finitas: CORRETO** (`code` padrão-tamanho < `m` não-padrão ⟹ guarda automática; contraexemplo
  `m=2` vácuo ✓). **M.3(c) quanto ao ramo vazio: CORRETO**; incompleto só no lado "várias famílias"
  (MAJOR-4). **M.5: CORRETO** dado M.0.
- **M.4: CORRETO e honesto** — duas condições `≡ ⊥` (`¬φ` por L.1; `C_{N_s}` por M.2); uso de L.3′
  (sem refutação **genuína**) legítimo — L.3′ é incondicional e vale para qualquer subfamília
  internamente finita; refutação interna marcada **(C)** com "plausivelmente não-provável, não
  verificado" — **sem over-claim** (a única honestidade pendente é que `¬C_{N_s}` é tautologia
  interna e a completude de EF não prensifica para dentro — dito em "mesma forma de L.3″" ✓).
- **§4: CORRETO e consistente** — sob R1, K-FP′ + R1 dão `τ_N ≡ 1` **só** para nomes padrão com a
  guarda (Nota do K-FP′), e M.2 dá `τ_{N_s} ≡ 0` para o nome não-padrão: hipóteses distintas, **sem
  colisão**; `τ_{N_s} ≡ 0` vale mesmo sob R1 (a prova é exatamente a leitura diagonal de R1) —
  logo "corner real para nomes não-padrões sob R1" ✓. Recomendação da pergunta "`q` é total?" ✓.

## Condições para RECOMENDADO

Aplicar M-1 (passo de montagem p-tempo + apagar "(dados padrão)"), M-2 (escrever a coleta p-tempo
de `F` e a distinção escolha-vs-derivação), M-3 (citação `A §1.2`, default do seletor), M-4
(escopo das famílias internas em M.3), M-5 (ressalva do merge em §0/§6) + os MENORES 1, 4 e typos.

---

# Revisão da v2 (rodada 2) — texto final

> Referee, 11 Out 2026. Esqueleto gravado antes da leitura (procedimento cumprido). Alvo: v2 de
> `M_canto_adversarial.md` (§8 = log do autor). Rodada 1 preservada acima.

## VEREDITO v2: **REVISION** — 0 FATAL; 3 dos 5 MAIOR fechados; MAIOR-5 parcial; **1 MAIOR novo**

O núcleo (M.0 conclusão, M.1, M.2: `δ≡1`, `τ≡0` diagonal) permanece confirmado e **todas as
correções de substância da rodada 1 entraram** (M-1 ✓, M-2 ✓, M-3 ✓, M-4 ✓ no corpo). Faltam:
(a) a **nova** justificativa de `R(N_s)` está **errada** (sobrejetividade não se segue de M.1);
(b) **§0** não recebeu as qualificações de MAJOR-4/5, embora o §8 diga que recebeu.

## Item a item

**1. MAJOR-1 (M.0) — FECHADO.** Linhas 40–52: `y := h(α,⟨y_0,…,y_{m-1}⟩)` p-tempo com
`m ≤ |α|` **(A✔)** `A_...` §1.2 e cota `|y| ≤ |α|·max_i|y_i|` ✓; escolha "`m` padrão-muitos — sem
coleção proibida" explícita ✓; `F := h'(y,α) = ⟨y↾at(α_i)⟩` com saída `m·|y| ≤ |α|·|y|` ✓; nota
linhas 51–52 reconhece que `at(α_i)` **pode ser não-padrão** (L.3a) e por isso a montagem é
p-tempo, não "padrão-finita" ✓; antecedente **Lema B.1 (I1)** citado (33–34) ✓.
*Resíduo (MENOR-1):* **checklist nº2 (linha 162) ficou velho** — "Colagem padrão-finita ∈ `M_0`
(sem compreensão) | M.0, M.1" reproduz exatamente o passo retratado (e em M.1 a lista tem
comprimento `m` **não-padrão**) ⟹ reescrever: "montagem p-tempo (M.0); lista de comprimento `m`
p-tempo (M.1)".

**2. MAJOR-2 (M.1) — FECHADO.** Linhas 57–61: `F := h'(y,α)` com cota de saída `m·|y| ≤ |α|·|y|` ✓;
"Teorema K quantifica sobre `F ∈ M_0` **arbitrárias** — não é preciso escolha/uniformização PV;
daí a diferença para o K-FP v1 retraído" ✓ (correto: em J1 §3 `F` é parâmetro arbitrário da
correção de `G/H`, sem restrição de forma); checklist nº3 reescrito ✓.

**3. MAJOR-3 (M.2a) — FECHADO no essencial; `R(N_s)` ERRADO (MAJOR NOVO).**
- Fonte `m ≤ |α|` **(A✔)** `A_...` §1.2 ✓ em §2 (71–72), checklist nº5 (165), §6 lacunas (194);
  nota honesta sobre a v1 ter citado `G2 §2.2` ✓.
- PV-totalidade com **default 0** ✓ (70–73) — inofensivo (M.1 garante testemunha; e `m ≥ 1` em
  todo `M_0`: `m=0` daria `α=⊥` contradizendo (S3)+`Ref_P` — caso do I1 B.1) ✓.
- `N_s` **não-padrão por `ℓ = ⌈log m⌉`** (`m` não-padrão por M.0) ✓ (76) — correto, substitui a
  cota `poly(|α|)` da v1 ✓.
- **`R(N_s)` (linhas 77–79): a justificativa está INCORRETA.** As "2 linhas" alegam
  **sobrejetividade** — "`s` é sobrejetivo nos índices maus", "`∀v ¬Fals(v,α_{s(v)})` + M.1 ⟹
  todo `i` mau é atingível para `v` mau adequado" — e isso é **erro de ordem de quantificadores**:
  M.1 dá `∀v ∃i<m` (toda `v` atinge **algum** `i`), que **não** implica `∀i ∃v` (todo `i` é
  atingido). Pior: a sobrejetividade é **falsa** — se algum `α_i ≡ ⊥` ((S2)+(S4) não excluem;
  (S3) exige só `⋁α_i` tautologia), então `¬Fals(v,α_i)` nunca vale ⟹ `i ∉ R(N_s)`. E "índice
  mau" nem está definido (só "mau **para `v**`", linhas 87–88).
  **Substituição correta (a conclusão é VERDADEIRA):** se `R(N_s) ⊆ {0,…,k}` com `k` padrão,
  colha `y_0,…,y_k` por (S4) (padrão-muitos), monte `σ* := h(α,⟨y_j⟩_{j≤k})` (p-tempo; `(S2)`
  ⟹ sem conflito; ⟹ `σ* ∈ M_0`); `σ*` falsifica `α_0..α_k` (localidade) e, por M.1, `s(σ*)<m`
  existe ⟹ `s(σ*) > k` ⟹ `s(σ*) ∈ R(N_s)\{0,…,k}` — contradição ⟹ `R(N_s)` não é padrão-finita.
  *Sem dano no resto:* a Observação (101–103) usa o fato só de forma decorativa (a hipótese de
  K-FP′ é "`N` padrão"), e `δ≡1`/`τ≡0` não dependem dele — mas a frase falsa deve sair.

**4. MAJOR-4 (M.3(b)) — FECHADO no corpo.** Linhas 115–122: alcance restrito a "nomes isolados,
pares e famílias **externamente finitas** (alcance de J.6-a′)"; residual explícito: famílias
**internas** não-padrão-muitas exigiriam coleção proibida ⟹ **permanecem `(C)`**, e "a correção à
J2 §3 vale só nesse escopo" ✓; §6 (177–179) repete o residual ✓.
*Resíduo (MENOR-2):* **§0 item 4 (linha 26)** ainda diz nomes padrão "**nunca** são adversariais"
sem o escopo.

**5. MAJOR-5 (§0/§4/§6) — PARCIAL.** §4 **fechado** (151–155: "Alinhamento (rodada 1)" exato: real
sob R1 e alternativa-com-`q`-total; `q` parcial pode abrir) ✓; §6 **fechado** (181–182) ✓.
**§0 item 3 (22–25) NÃO foi alterado** — continua "`C_{N_s} ≡ ⊥` … em todo `M_0 ⊨ T_S`" **sem**
a qualificação do `q` parcial — e o **§8 (linha 227–229) registra "corrigido em §0 e §6"**, o que
não corresponde ao texto (**registro impreciso do log**). Falta uma frase em §0.

**6. MENORES / regressões.** Typos ✓ ("vácuo" 27, "daria" 148, "de forma diferente" 198);
big-or/tamanho de `τ_N` **marcado** em §6 lacunas (195–196) ✓ herança `J2_referee` MAJOR-1(iii) ✓.
*Regressões novas:* (a) checklist nº2 velho (MENOR-1); (b) §0 sem as duas qualificações
(MENOR-2 + item 5); (c) §8 afirma em §0 o que não foi feito; (d) §6 "Próximos passos (1)" ainda
convoca o referee (cosmético); (e) nit linha 65 termina "— padrão." (sobra de estilo da v1).

**7. Veredito final: REVISION.** 0 FATAL (o erro de `R(N_s)` é lateral: não entra em `δ`, `τ`, M.0,
M.1). **Para RECOMENDADO:** (i) trocar as 2 linhas de `R(N_s)` (linhas 77–79) pela versão acima;
(ii) frase de ressalva em §0.3 e escopo em §0.4; (iii) reescrever checklist nº2; (iv) corrigir o
§8 ("§0" → feito só em §4/§6). Feito isso: **RECOMENDADO** (MAIOR-1/2/3-substantivo/4 já
cumpridos).

---

# Revisão da v3 (rodada 3) — texto final

> Referee, 11 Out 2026. Esqueleto gravado antes da leitura (procedimento cumprido). Alvo: v3 de
> `M_canto_adversarial.md`. Rodadas 1–2 preservadas acima.

## VEREDITO v3: **RECOMENDADO** (com 3 erratas menores obrigatórias — E-1/E-2/E-3)

As **4 condições da rodada 2 foram cumpridas** (R(N_s) por contrapositiva; ressalva + escopo em
§0; checklist nº2; §8/§8b). 0 FATAL; corpo de M.0–M.5 **intacto e idêntico ao da v2** (já
confirmado nas rodadas 1–2) — nenhuma regressão teorema. Restam 3 erratas de formulação/log,
nenhuma das quais atinge δ, τ, M.0, M.1 ou o escopo de M.3/M.4.

## Item a item

**1. As 2 linhas de `R(N_s)` (§2, l.83–89) — CORRETAS no essencial; 1 sobrestimativa (E-1).**
- `σ* ∈ M_0` ✓: `k` **padrão** ⟹ `⟨y_j⟩_{j≤k}` padrão-finita ⟹ `σ* := h(α,·)` é o **mesmo** `h`
  p-tempo de M.0 (mesma `h`, `m ≤ |α|` **(A✔)**) ⟹ `σ* ∈ M_0`, sem compreensão ✓.
- `s(σ*)` bem-definido ✓: `σ* ∈ M_0` + M.1 (`∀v ∃i<m`) dá o menor `i<m` com `¬Fals(σ*,α_i)`
  (e `m≥1`: `m=0` ⟹ `α=⊥` contradiz (S3)+`Ref_P`) ✓; `σ*` falsifica `α_0..α_k` ⟹ `s(σ*) > k` ✓;
  `s(σ*) ∈ R(N_s)` ✓ ⟹ contradição com `R(N_s) ⊆ {0,…,k}` ✓.
- Conclusão correta: **`R(N_s)` não é padrão-finita** ("não-padrão-muitos") ✓ — para **todo `k`
  padrão**.
- **E-1 (errata): "cofinal em `m`" NÃO segue.** A prova só exclui `k` **padrão`; para `k`
  **não-padrão** seria preciso amalgamar `k+1` falsificadores — a coleção proibida por K. (Uma
  forma equivalente: `R(N_s) ⊆ {0,…,k}` ⟺ `⋁_{j≤k} α_j` é tautologia; para `k` padrão, (S4)+(S2)
  derrubam; para `k` não-padrão, (S1)–(S4) **não** derrubam.) ⟹ trocar "cofinal em `m`" por
  "**não padrão-finita** (não cabe em `{0,…,k}` nenhum com `k` **padrão**)". *Lateral* (a frase já
  está marcada "não entra em δ/τ"; a Observação só precisa de "não padrão-finita", que está provada).
- **E-2 (errata):** nomear em uma linha a origem dos `y_j` (**(S4)**, escolha padrão-muitos) e o
  passo **(S2)**-sem-conflito + **localidade** em "`σ*` falsifica `α_0..α_k`" — hoje implícitos
  (são os de M.0; o "(padrão-muitos ✓)" remete, mas não declara).

**2. §0 itens 3 e 4 — FECHADOS.** Item 3 (l.24–29): "`C_{N_s} ≡ ⊥` … **sob R1 e sob a alternativa
com `q` total**; sob a alternativa com **`q` parcial** o trap **pode abrir** (§2 ressalva — a
resposta do autor … decide)" ✓. Item 4 (l.30–35): escopo "**nomes isolados, pares e famílias
externamente finitas**" + "famílias **internas** não-padrão-muitas permanecem **(C)** — coleção
proibida" ✓. Idêntico ao §6 (l.185–192) e ao §4 (l.161–165) — os três agora coerentes ✓.

**3. Checklist nº2 — OK.** l.172: "Montagem `y := h(α,⟨y_i⟩)` p-tempo (`m ≤ |α|`); `F := h'(y,α)`
lista ∈ `M_0` (sem compreensão)" ✓ (nº3 repete a parte de `F` — redundância inofensiva).

**4. §8/§8b — log fiel no essencial; 1 errata (E-3).** §8b anota a imprecisão ✓ (l.258–259:
"dizia 'corrigido em §0' antes de sê-lo — o §0 só foi corrigido na v3") e registra os 4 reparos ✓;
§4 l.164–165 ("corrigido em §0 e §6") passou a ser verdadeiro na v3 ✓.
- **E-3:** (a) §8b, 1º bullet: "as 2 linhas da **v1** alegavam sobrejetividade" — **impreciso**: a
  v1 **afirmou `R(N_s)` sem prova** (rodada 1, MENOR-4); a sobrejetividade foi a tentativa da
  **v2** (rodada 2) ⟹ "as 2 linhas **da v2**"; (b) cabeçalho do §8b "rodada 2: MAJOR-1/2/4/5
  **fechados**" — na rodada 2 o MAJOR-5 ficou **parcial** (§0 só na v3; veredito da rodada 2 =
  REVISION) ⟹ "MAJOR-1/2/4 fechados, MAJOR-5 parcial (§0 na v3)".

**5. Regressões novas: NENHUMA de substância.** Corpo M.0–M.5 idêntico ao v2 ✓; §5, §6, §7 sem
mudança problemática (o "referee hostile" do §6 Próximos passos é cosmético e já estava lá);
typos mantidos corrigidos ✓; big-or/tamanho de `τ_N` segue marcado (§6 lacunas) ✓.

## Erratas para aplicar (fecham a frente)

- **E-1**: §2 — "cofinal em `m`" → "não padrão-finita (`k` padrão)".
- **E-2**: §2 — nomear `(S4)` na escolha dos `y_j` e `(S2)`+localidade em "`σ*` falsifica".
- **E-3**: §8b — atribuição "v1"→"v2" e cabeçalho "5 fechados"→"MAJOR-5 parcial (§0 na v3)".

**Com E-1/E-2/E-3 aplicadas: RECOMENDADO definitivo** (rodada 1: 5 MAIOR — fechados; rodada 2:
MAJOR novo de `R(N_s)` + 3 reparos — fechados; rodada 3: verificado).

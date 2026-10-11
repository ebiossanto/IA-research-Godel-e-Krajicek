# Referee hostile — `J2_ponto_fixo.md` (rodada completa)

> Referee independente, 11 Out 2026. Esqueleto gravado **antes** da leitura (procedimento
> cumprido); este é o texto final. Marcação: **(A)** = fonte, **(P)** = próprio, **(C)** = conjetura.
> Fontes conferidas: `H1_colecao_refutacao.md` §1.1, `G2_semente_Fsent.md` §§1–2,
> `J1_Qcompactness_M0.md` §§2–4 (+§7), `A_teoremas_exatos.md` §1.0/L21–22/§1.12,
> `CONTEXTO_COMUM.md`.

## VEREDITO: **REJECT** (na forma atual)

O resultado central (Teorema K-FP com símbolo de função PV `Q` e rota "sentença universal
verdadeira ∈ `T_PV`") **é incompatível com o Teorema K da J1** (FATAL-1), sua construção
usa uma busca NP-dificil apresentada como PV (FATAL-2) e suas guardas não prensificam em
sentença universal (FATAL-3). A leitura R1 (§1) **não está decidida** e é justamente o que
sustenta `C_N ≡ ⊤` (MAIOR-1/2). As §§3–4 contêm matéria correta e honesta; uma reescrita
como **resultado parcial** (existência condicional, sem `Q` PV, com alcance reduzido) é
factível — ver "Correções exigidas".

---

## FATAIS

### FATAL-1 — K-FP (com `Q` PV e correção universal verdadeira) contradiz o Teorema K (J1 §3)
**Local:** §2, linhas 48–54 (enunciado: "existe **símbolo de função PV** `Q` … a sentença
`∀α,N,B,m[R(N)⊆m ∧ (S2)∧(S4) → Fals(Q(...))]` é universal verdadeira ⟹ ∈ `T_PV` ⟹ vale em
todo `M_0` sob as guardas"); §7 linhas 163–167 (autor não detectou o conflito).

**Argumento.** Tome, para `i<m`, o **nome constante** `N_i := ⟨C_1,…,C_ℓ⟩` cujos componentes
são constantes 0/1 com `⟨ν(C_1),…⟩ = i` (expansão binária de `i` existe em `M_0` pois
`M_0 ⊨ PV` é fechada p-tempo). Então `code(N_i,v) = i` para toda `v`, logo
`R(N_i) = {i} ⊆ m` ✓; `(S2)` ✓; `(S4)` vale em `M_0` ✓. A instância da sentença reivindicada
em `(α,m,N_i,B_i)` dá, **em `M_0`**:
`Fals( Q(α,N_i,B_i,m), (α)_{code(N_i,Q(...))} )`, i.e. `Fals(F(α,i), α_i)` com
`F(α,i) := Q(α,N_i,B_i,m)` — um **símbolo de função PV**, interpretado em `M_0` como
`F ∈ M_0`. Logo `M_0 ⊨ ∀i<m Fals(F(α,i), α_i)` — **exatamente o `F` proibido pelo Teorema K**
(J1 §3, referee RECOMENDADO v4). "Testemunha por nome, sem escolha uniforme" **não** basta:
a quantificação `∀N` inclui **nomes constantes**, e esses já fornecem a coleção uniforme.

**Consequência:** a hipótese "dá testemunha por nome — sem escolha uniforme — sem conflito
com K" (pedido 5 da missão) é **falsa**. K-FP como está enunciado **não pode ser verdadeiro**
(a menos que K esteja errado — não é o caso; K foi fechado na rodada 4 da J1). Caem: §0
atos 1–2, §2 inteiro na forma atual, Corolário K-FP1, J.6-a, e o §6 ("decidida em quase
todo o alcance").

**Correção exigida:** reenunciar K-FP **sem** função `Q` PV — como afirmação existencial
`∃q*` (Σ^b_1) — e reavaliar o alcance (ver FATAL-2): a tese existencial só é provável, pela
rota daqui, para `B` de tamanho **padrão** (número **metateórico** finito de ∃-eliminações);
para `B` não-padrão a montagem de `b` é a coleção que K proíbe.

### FATAL-2 — `leastF` não é PV; "laço limitado ✓" confunde limitado com polinomialmente limitado
**Local:** §2 passo 1, linhas 58–59; checklist §5 nº 3, linhas 127 e 133.

**Argumento.** `leastF(α,i) := o menor q com Fals(q,α_i)` percorre **todas as atribuições**
(`2^{#átomos}` candidatos) — custo exponencial, não p-tempo. A garantia `|α| ≥ m` só
polinomializa as varreduras sobre `i<m` (padrão bem usado em J1: `G`,`H`,`Widx`, `O(m·|α|)`);
ela **não** cobre a busca sobre `q`. Achar o menor falsificador de um circuito é busca
FNP-difícil; com a promessa "(S4) garante existência", resolver `SAT` sob promessa em p-tempo
ainda decide `SAT` (verificar a saída) ⟹ **P=NP**. `BuildPat` (varredura `i<m`, unicidade de
`i(p)` por (S2)) e `Merge` **são** PV ✓ — o defeito é só `leastF` (e o que dele depende:
`b`, `i*`, `q*`, `Q`). Além disso: montar `b` exige **uma testemunha por `p ∈ B`** —
`|B|` ∃-eliminações; para `B` não-padrão com `image(p ↦ i(p))` cobrindo `m` isso é
literalmente a coleção `∀i<m ∃y` que K proíbe (J1, Observação K.3).

**Correção exigida:** remover `leastF` dos "símbolos PV"; explicitar que a existência de `b`
é um passo de **coleta** e está **disponível apenas** para `|B|` padrão (ou sob hipótese
adicional); rebaixar o alcance de K-FP/J.6-a em conformidade.

### FATAL-3 — as guardas não prensificam em sentença universal; o fallback "teorema de `T_S`" não salva §3
**Local:** §2 linhas 52–54; §6 "Lacunas honestas", linhas 156–159 (o ponto estava flagged,
mas a consequência está errada).

**Argumento.** `(S4) = ∀i<m ∃y Fals(y,α_i)` é `Π^b_2`; a matriz
`[ (S2)∧(S4)∧R(N)⊆m → Fals(q*,…) ]` prensifica para **`∀∃`**, não para universal — logo a
sentença **não** ∈ `T_PV` como afirmado. A saída canônica (trocar `(S4)` por função de
Skolem PV + correção universal) é **exatamente** a coleção proibida por K. E o fallback
("se falhar, K-FP vira teorema de `T_S`, o que basta para §3") **não basta**: a **prova** de
K-FP falha por FATAL-2 (não é a formalização que quebra, é a construção). `R(N)⊆m` e `(S2)`
sim são universais ✓ (p-tempo na matriz).

---

## MAIORES

### MAIOR-1 — R1 (§1) não está decidida; a alternativa **não** é descartável
**Local:** §1, linhas 29–39.

(i) Sob R1, `τ_N` fica **sem átomos livres** — o que torna **vazia** a correção do referee S1
do H1 §5 ("com espelhos frescos fora de `p`, `τ_N` ficaria fora de `B(p)`", H1 §1.1): essa
correção **pressupõe átomos livres `a_s`** em `τ_N`. (ii) Sob R1, a nota "Sentido" de H1 §1.1
(`ν_G(τ_N)=1 ⟺ M[G] ⊨ (¬(α)_{ν_G(N)}) ∈ SAT`) — e o **passo (2) da prova do no-G**
(H1, Teorema 1.1) — fica **falsa em geral** (ex.: `code(N,·)` com imagem em índices `≥ m`).
(iii) `G2 §2.2` exige `τ_N` de **tamanho interno ≤ poly(|α|)**, incompatível com uma disjunção
sobre `2^{|p|}` atribuições. (iv) O parágrafo de reconciliação ("elementaridade `Σ^b_1`…")
é um **non sequitur**: `ν_G(N)` é parâmetro **novo** de `M[G]`; sentenças `Σ^b_1` com esse
parâmetro **não** transfere de `M`. **R1 é uma leitura possível, não a leitura fiel**; a
alternativa (diagonal em `v`, `a_s` livres) é a que faz verdadeira a nota Sentido, o fixo de
S1 e o tamanho poly de G2. `J1 §2(iii)` tinha razão em marcar isto; J2 não o resolveu.

### MAIOR-2 — K-FP1 e J.6-a dependem inteiramente de R1; sob a alternativa, o caso adversarial engole o alcance todo
**Local:** §2 K-FP1 (linhas 70–72); §3 J.6-a (linhas 82–84); §0 ato 2 (linhas 17–20);
§6 (linhas 138–144).

Sob a leitura alternativa, `τ_N(v)` é diagonal em `v`; K-FP daria apenas **`τ_N` satisfatível**
(`q*` é atribuição **satisfatória**, não tautologia) → `C_N` satisfatível, **não** `≡ ⊤` →
"**qualquer** `v*` a satisfaz" (J.6-a) **colapsa**, e a compatibilidade entre nomes (mesmo
todos com `R(N)⊆m`) vira o caso a decidir — o "fibrado incompatível" de §3 passa a valer
para o alcance **inteiro**, não só para o ramo misto. `K-FP1` ("verdadeiro em todo `M_0`,
sem restrição de `v`") é portanto **condicional a MAIOR-1** e deve ser reescrito como
"sob `R(N)⊆m`, `C_N` é satisfatível" no máximo.

### MAIOR-3 — superestimativa de alcance: "C.3 negativa em quase todo alcance"
**Local:** §0 ato 2 (linha 19–20) e §6 (linha 143–144).

O resultado condicional cobre só famílias **sem `¬φ`** e **todos** os nomes com `R(N)⊆m`.
Famílias com **qualquer** nome de `R(N)⊄m` (já com dois nomes) podem ser **insatisfatíveis
conjuntamente** (a própria §3 o admite: `code(N_1,v) ≥ m` e `code(N_2,v) ≥ m` podem ser
regiões disjuntas). Logo "quase todo o alcance" não está justificado; escreva: "negativa no
alcance de nomes todos com `R(N)⊆m` (e só aí), condicionado a K-FP"; o restante é `(C)`.

### MAIOR-4 — a "transferência para `M[G]`" de §1 falha também pela hipótese de `R(N)`
**Local:** §1, linhas 36–37.

`R(N) = {code(N,v) : v ∈ M_0}` cobre só atribuições **internas**; `ν_G(N) = code(N,ν_G)` usa
`ν_G ∉ M_0`, logo `ν_G(N)` pode **não** pertencer a `R(N)`. K-FP (sob `R(N)⊆m`) não entrega
ponto fixo para o índice **genérico novo** — que é justamente o que o no-G (H1 Thm 1.1,
passo (2)) precisa. A frase "a verdade interna de τ_N transfere para `M[G]`" deve ser
**retirada** ou reformulada com a condição exata (`δ_N` em `M[G]`, índices novos).

---

## MENORES

- **M1** §2 Notation (linhas 43–46): especificar se `v` em `R(N)` percorre atribuições sobre
  `B` ou sobre `p` (imagem idêntica por "N lê só `B`", mas a guarda deve ser uniforme).
- **M2** §2 passo 2 (linha 61): "`b_p := (leastF(α,i(p)))_p` **se existe**, senão `0`" —
  ambíguo; escrever "se `i(p)` existe".
- **M3** §3 (linhas 96–99): "(Hjoint) falsa ⟹ C.3 **pode ainda** ser negativa" — **correto**
  (C.3 positiva exige refutação **genuína**; insatisfatível interno ≠ refutável, coerente com
  a "Dicotomia residual" da J1 e com L21–22); convém citar J1 §2 explicitamente.
- **M4** §4 (linhas 117–119): o "modelo r.s. de `T_S + ∀rφ(r)`" dá não-compactude máxima só
  se o modelo também satisfizer o **item (1)** (`φ` sem prova em `M` em qualquer pps) — o item
  (1) **não** é axioma de `T_S`; a existência de modelo r.s. contável está correta (teoria padrão).
- **ESTILO** linha 78: "brigiriam" → "brigar(i)am"; §5 nº 3 (linha 133) deve passar a dizer
  "`BuildPat`,`Merge` PV; `leastF` **não** (FATAL-2)".

---

## O QUE ESTÁ CORRETO (declarado explicitamente)

1. **`BuildPat` e `Merge` são PV** (varredura `i<m` com `m ≤ |α|` ⟹ `O(m·|α|)`; unicidade de
   `i(p)` por (S2); merge de duas atribuições explícitas) — item 2(a) parcialmente **confirmado**.
2. **Passo 4, o padrão do acordo em `D_{i*}`** (linhas 64–68): **correto como argumento
   condicionado** — para `p ∈ B∩at(α_{i*})`, `i(p)=i*` por unicidade (S2); `q*↾B = b`;
   `code(N,q*) = code(N,b) = i*` por "N lê só `B`"; `Fals(q*,α_{i*})` por **localidade** de
   `Fals` (sentença universal ∈ `T_PV`, herdada de J1 §3 passo 1). Só falta a **disponibilidade**
   dos falsificadores (FATAL-1/2).
3. **`i* := code(N,b) < m` sob `R(N) ⊆ m`**: hipótese **interna correta** para essa
   construção (reserva: não cobre índices genéricos — MAIOR-4). Item 2(c) **confirmado**.
4. **Ram `R(N) ⊄ m` de J.6-b**: `C_N(v)` vale **vazivamente** para algum `v` interno —
   **correto** (definição de `δ_N`).
5. **Fronteira do caso misto (§3) está honestamente marcada `(C)`** e o exemplo dos fibrados
   incompatíveis é interno coerente; o "salto" `(Hjoint)` falsa → C.3 ainda negativa é
   **legítimo** (M3).
6. **§4 (veredito sobre r.s.) está certo em substância**: r.s. realiza **tipos recursivos**,
   não decide existenciais `Σ^b_1`; para a pergunta `∀M_0`, "verdade em todo modelo" ⟺
   "provabilidade em `T_S`" (completude de 1ª ordem). A auto-crítica ("rota do orquestrador
   anterior: ferramenta errada") é correta e bem-vinda.
7. **Marcação (P)/(C)/(A) e as lacunas declaradas** são adequadas; o erro não é de
   honestidade de marcação, é de **conteúdo** (o conflito com K passou despercebido).
8. **Consistência com o no-G (H1)**: a **tese existencial** de K-FP não contradiz o no-G;
   o que contradiz é a versão com `Q` PV (FATAL-1) e a "transferência" (MAIOR-4).

## Correções exigidas para re-submissão (rota factível de resultado parcial)

1. K-FP reescrito como **existencial** `∃q*` (sem `Q` PV), com prova **para `|B|` padrão**
   (número finito metateórico de ∃-eliminações, usando (S2)+(S4)+localidade) — alcance
   declarado; **ou** como condicional sob hipótese explícita de coleção limitada sobre `B`.
2. Remover "∈ `T_PV`" e a guarda `(S4)` da sentença; manter `(S2)`, `R(N)⊆m` como guardas
   universais.
3. Retirar K-FP1/J.6-a na forma "≡ ⊤ / qualquer `v*`"; substituir por "satisfatível" até que
   a leitura de `τ_N` seja **decidida** (MAIOR-1 é o ponto de partida obrigatório: reler H1
   §1.1 com o referee S1, a nota Sentido e G2 §2.2).
4. Reescrever §0 atos 1–2, §3 J.6-a, §6 e o checklist §5 (nº 3) conforme acima.

**Salvável em 1 linha:** "para nomes cujo sup é finito **padrão**, o ponto fixo de `τ_N`
existe (prova finita, sem coleção) — o residuo de J.6 é uma pergunta de provabilidade `Σ^b_1`
em `T_S`, e a saturação recursiva é ferramenta errada." É um resultado real, mas **muito**
menor que o reivindicado.

---

# Revisão da v2 (rodada 2 — esqueleto gravado antes da leitura; texto final abaixo)

## VEREDITO v2: **REVISION** (correções locais; o mecanismo central está bom)

Os 3 FATAIS da v1 estão **resolvidos de fato** por retração + K-FP′ (escolha sobre
padrão-muitos, sem uniformização PV, sem sentença-correção universal). Restam 2 MAIOR,
ambos de **escopo**: a guarda `R(N) ⊆ m` foi **removida sob uma justificativa falsa**
("automática para `N` padrão") e os enunciados de §0 ato 1 e J.6-a′ ficaram **falsos** na
forma; a correção é local (restaurar a guarda e restringir a famílias finitas-padrão).
Mais 3 MENORES.

## 1. Aplicação das 7 correções da rodada 1

| Correção (rodada 1) | Status |
|---|---|
| K-FP existencial sem `Q` PV, `\|B\|` padrão | **PARCIAL** — prova correta, mas a guarda `R(N)⊆m` foi dropada (MAIOR-1) |
| Remover "∈ `T_PV`" e guarda `(S4)` da sentença | **RESOLVIDA** (K-FP′ não usa sentença-correção) |
| Retrair K-FP1/J.6-a "≡ ⊤/qualquer `v*`" até decidir §1 | **PARCIAL** — §0 ato 1 ainda afirma "`C_N` ≡ ⊤ para nomes padrão" e J.6-a′ conclui "C.3 negativa nesse alcance" incondicionalmente (MAIOR-2) |
| Reescrever §0/§3/§6/checklist | **PARCIAL** — checklist nº 7 repete a falsidade "R(N)⊆m automático" |

## 2. Ataque ao Teorema K-FP′ (§2)

**(a) Escolha `g_i` — PARCIALMENTE LEGÍTIMA.** A escolha sobre `i ∈ R(N)` é legítima
**se** `R(N)` é padrão-finito **e** `R(N) ⊆ m`. `R(N)` padrão-finito para `N` padrão está
**CERTO** (imagem de um circuito padrão sobre `B` padrão: ≤ `2^{|B|}` códigos padrão).
Mas "`R(N) ⊆ m` **automaticamente**" (linha 48; checklist nº 7) é **FALSO** para `m`
padrão: nome constante padrão `N=⟨1,1,1⟩` com `m=2` dá `code=7 ≥ m`. (A versão correta é:
automática para `m` **não-padrão** — registre essa versão.) `K-FP′` **sem** a guarda é
**falso** (contranexemplo acima: se `(α)_7` não tem falsificador, o existencial falha).
**Correção:** restaurar a guarda `R(N)⊆m` no Teorema, na Notação, em J.6-a′, §0 ato 1 e
checklist nº 7 — era exatamente a guarda da "rota factível" do referee.

**(b) `b ∈ M_0` sem compreensão — CORRETO.** `M_0 ⊨ PV` é fechada sob funções p-tempo;
montagem de bits padrão-finitos de elementos `g_i ∈ M_0` é aplicação p-tempo ✓;
`b ↾ D_i := g_i ↾ D_i` sem conflito por (S2) ✓; "0 no resto de `B`" ✓.

**(c) Acordo em `D_{i*}` — CORRETO, sem circularidade.** Os `g_i` são fixados no passo 1
(antes de `b`), `i* = code(N,b)` no passo 3, e `b ↾ D_{i*} = g_{i*} ↾ D_{i*}` pelo passo 2
com o **mesmo** `g_{i*}` ✓; `q*↾B = b` (em `B∖at(α_{i*})` por construção; em `D_{i*}` por
acordo; em `B∩at(α_j)`, `j≠i*`, `j∈R(N)`, por disjointude (S2); fora dos `D_j` por construção)
⟹ `code(N,q*) = code(N,b)`; `Fals(q*,α_{i*})` por localidade ✓ — **condicionado à guarda
de (a)**.

**(d) Nota de sobrevivência — HONESTA e correta.** K-FP′ entrega o **existencial interno**;
o valor do circuito `τ_N` depende da leitura de §1 (sob R1: `τ_N = 1` constante; sob a
alternativa: "para a atribuição certa") — marcado, sem extrapolação ✓.

## 3. §1 (semântica aberta) — tratamento CORRETO

Manter **aberto** com as 3 pressões registradas (correção S1 do H1 pressupõe `a_s` livres;
nota Sentido + passo (2) do no-G; tamanho `poly(|α|)` de G2 §2.2) é o tratamento correto:
**o referee também não decide** a leitura — as pressões puxam para a alternativa, mas a
redação literal de H1 §1.1 admite R1. Se a alternativa vier a ser adotada, cai J.6-a na
forma "qualquer `v*`" e o caso adversarial engola o alcance (o v2 §1 reconhece isso).
**Nada a corrigir.**

**Reforço opcional (não exigido):** para **famílias finitas-padrão** de nomes padrão com
`R(N_j)⊆m`, a satisfatibilidade **conjunta** vale sob **ambas** as leituras: escolha `g_i`
para `i ∈ ⋃_j R(N_j)` (padrão-finito), monte `b` sobre `⋃_j B_j`, e seja `q* :=` fusão de
`g_{code(N_j,b)}` sobre `j` — disjointa por (S2) ⟹ `τ_{N_j}(q*)=1` para **todo** `j`.

## 4. §3 e §4 — coerência com a rodada 1

- **J.6-b (ramo vazio)** — confirmado ✓. **Fronteira `(C)`** — honesta ✓ (fibrados `≥m`
  incompatíveis; "(Hjoint) falsa ⇏ C.3 positiva" mantido ✓; caso misto segue **(C)** ✓).
- **J.6-a′** — precisa das correções MAJOR-1/2: sem a guarda `R(N)⊆m` é **falso mesmo sob
  R1** (dois nomes padrão com `m=2` e fibrados `≥m` incompatíveis formam família padrão
  insatisfatível); sob a alternativa de §1, "interna-mente finita" deve virar **finita-
  padrão** (o construtor-joint acima fecha nesse alcance; para `k` não-padrão a escolha de
  `g`'s seria coleção proibida — K).
- **§3(iii) — MENOR-1**: "a transferência para `M[G]` usa elementaridade `Σ^b_1`" é
  **vaga/errada**: elementaridade não transfere sentenças com parâmetro **novo** `ν_G(N)`;
  sob R1 a transferência **não existe**; sob a alternativa é **direta** (`ν_G(τ_N)` entrega
  o falsificador genérico). Reformular ou retirar.
- **§4 (r.s.)** — **CONFIRMADO**, correto ✓ (tipos ≠ existenciais `Σ^b_1`; para a pergunta
  `∀M_0`, "verdade em todo modelo" ⟺ "provabilidade em `T_S`"). A rota "completude para
  `φ` só" está bem marcada `(C)` ✓.

## MENORES v2

- **M1**: checklist nº 7 — corrigir para "`R(N)⊆m` é automática só para `m` não-padrão".
- **M2**: Notação `R(N)` — explicitar `v` sobre `B` vs sobre `p` (mesma imagem; ressalva M1
  da rodada 1 não endereçada).
- **M3**: §0 ato 1 — retirar "`C_N` ≡ ⊤ para nomes padrão" como consequência incondicional
  (depende da guarda e da leitura de §1).

## O QUE ESTÁ CORRETO NA v2 (declarado)

1. Mecanismo de K-FP′: escolha padrão, montagem sem compreensão, sem circularidade,
   localidade — **correto sob a guarda `R(N)⊆m`**; é a "rota factível" da rodada 1
   executada com fidelidade.
2. Retração da v1 e log §8 — **fiel e honesto** aos 3 FATAL/4 MAIOR; o diagnóstico
   "escolha padrão-muitos ≠ coleção proibida (não-padrão-muitos)" está **correto**.
3. FATAL-1/2/3: **resolvidos de fato** (sem `Q` PV, sem `leastF`, sem prensificação de
   `(S4)`; nenhum vestígio de uniformização não-padrão).
4. §1 aberto com as 3 pressões — tratamento correto; §3 fronteira `(C)` honesta;
   §4 r.s. correto; marcação (P)/(C)/(A) adequada.

**Em 1 linha:** K-FP′ está **quase** certo — resta restaurar a guarda `R(N)⊆m` (que o v2
removeu por engano) e rebaixar J.6-a′ a famílias finitas-padrão com todos os nomes sob a
guarda; com isso, **RECOMENDADO**.

---

# Rodada 3 — v3 (esqueleto gravado antes da leitura; texto final abaixo)

## VEREDITO v3: **RECOMENDADO**

MAJOR-1 **resolvida** (guarda restaurada em todos os pontos exigidos + contraexemplo
registrado); MAJOR-2/J.6-a′ **resolvida** (construtor-joint correto, fecha sob ambas as
leituras); MENORES endereçados. Restam 3 notas **não-bloqueantes** e cosméticos.

## 1. MAJOR-1 — RESOLVIDA ✓

- Teorema K-FP′ (L57–59): "todo nome **padrão** `N` com **`R(N) ⊆ m`** (guarda explícita)"
  ✓; Notação (L50–54): "automática **só** quando `m` é não-padrão… para `m` padrão é
  **falsa** (`N=⟨1,1,1⟩`, `m=2`, `code=7 ≥ m`) ⟹ guarda permanece explícita" ✓
  (a afirmação "só quando" está **correta**: para `m` padrão sempre há nome padrão padrão
  violando; para `m` não-padrão todo código padrão é `< m` ✓); passo 3 (L70–71): "`i* < m`
  **por hipótese (a guarda)** — *não* por `N` padrão isoladamente" ✓; §0 ato 1 (L15–17) ✓;
  checklist nº 7 (L147) ✓. `i* ∈ R(N)` segue porque `b` é atribuição interna ✓.

## 2. MAJOR-4 / J.6-a′ (construtor-joint) — RESOLVIDO ✓

`B_joint := ⋃_j sup(N_j)`, `R_joint := ⋃_j R(N_j)` padrão-finitos ✓; `D_i := at(α_i)∩B_joint`
disjuntos por (S2) ✓; escolha de `g_i` sobre `i ∈ R_joint` (padrão-muitos, (S4) instanciável
em índices padrão `< m`) ✓; `i_j* := code(N_j,b) ∈ R(N_j) ⊆ m` ✓; `q_j*` com o **mesmo**
`g_{i_j*}` e acordo em `D_{i_j*}` ✓ — **sem circularidade** (`R_joint` é prévia a `b`) ✓.
**Fecha sob ambas as leituras**: sob R1 cada `C_{N_j} ≡ ⊤`; sob a alternativa, a testemunha
comum é a **fusão** `q† := ⋃_j g_{i_j*}` sobre `at(α_{i_j*})` (disjuntas por (S2)) ∪ `b` sobre
`B_joint` ⟹ `code(N_j,q†)=i_j*` e `Fals(q†,α_{i_j*})` por localidade ⟹ `C_{N_j}(q†)` ✓.
**Nota MENOR-r1 (não-bloqueante):** "`v* := b` estendida" precisa dizer "**estendida pelos
`g_i` sobre `at(α_{i_j*})`**" — `b` crua **não** falsifica `α_{i_j*}` fora de `B_joint`
(sob a alternativa os bits zero conflitariam); a fusão `q†` acima é a testemunha certa e
ela existe — o resultado não muda.

## 3. MENORES — ENDEREÇADOS

- **§3(iii) reescrita ✓**: transferência a `M[G]` atribuída à maquinaria de forcing do
  artigo, fora do escopo de J2; a vaga "elementaridade `Σ^b_1`" foi removida e reconhecida
  ✓. (Cosmético: rotulada "MAJOR-5"; era MENOR-1 da rodada 2.)
- **Notação de `R(N)` — PARCIAL**: ganhou "padrão-finito para `N` padrão" ✓, mas ainda não
  explicita `v` sobre `B` vs sobre `p` (imagem idêntica — **imaterial**, M2 residual).

## 4. Regressão — SEM PROBLEMAS DE FUNDO

- §0/§3 coerentes com o alcance rebaixado (guarda + famílias finitas-padrão + fronteira
  `(C)` para internas) ✓; §8 registra a rodada 2 (L200–213) ✓.
- **Nota MENOR-r2 (não-bloqueante):** fronteira (i) atribui o par adversarial a "nomes
  **não-padrões**" — o contraexemplo de dois nomes **padrão** com `m=2` e fibrados `≥m`
  incompatíveis é igualmente possível; escrever "famílias com nomes **no ramo vazio**
  (padrão ou não)".
- **Cosméticos**: título §0 ainda "(v2)" (L10); §6 resumo sem a guarda (`"nomes padrão sem
  ¬φ"` → "…com `R(N)⊆m`"); §6 próximo passo (1) ainda "referee da v2".

## O QUE ESTÁ CORRETO NA v3 (declarado)

1. Guarda `R(N)⊆m` integralmente restaurada e justificada com contraexemplo — MAJOR-1 **fechada**.
2. K-FP′ (escolha `g_i`, montagem de `b`/`q*` sem compreensão, acordo sem circularidade,
   localidade) — **correto sob a guarda**.
3. Construtor-joint de J.6-a′ — **correto e fecha sob ambas as leituras** (com a fusão `q†`
   como testemunha comum; nota MENOR-r1 apenas explicita isso).
4. Escopo rebaixado e honesto (famílias finitas-padrão; ramo vazio e `ν_G` fora de escopo;
   §1 em aberto; caso misto `(C)`); §4 (r.s.) mantido e correto; log §8 completo.

**Com a nota MENOR-r1 incorporada a J.6-a′ (e opcionalmente r2/cosméticos), o documento
está em condições de publicação no estado atual de resultados.**

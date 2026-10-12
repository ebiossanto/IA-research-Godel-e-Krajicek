# C2 — `DD` para `Res(k)` (k-DNF resolution): largura-k (teorema), programa sob promessa e o ingrediente correto

> Frente C2, **v5 — rebaixamento honesto após 4 rodadas de referee**; **rodada
> 5: RECOMENDADO** (menores r5 — (O5), (O3)-amplo, marcador (C) em `Res(1)`,
> §7 restrito — aplicados neste texto).
> (`C2_ddres_k_referee.md`: a cada rodada, fato novo na mecânica do recorte —
> (r4) reusava o pai errado; (r6)-final escapava à promessa; (r2) sem regra
> para dependentes ∧-intro). A **prova de C2.2 não se fecha nesta entrega**
> sem a leitura exata de [K19 5.7]/Lema 4.1 — rebaixa-se a **Programa** com as
> obrigações exatas (O1)–(O4) que o referee enumerou. O que permanece **teorema**:
> **C2.1** (largura-k) e **C2.3** (ingrediente corrigido + redução). 11 Out 2026.
> Marcação: **(A)** = fonte; **(P)** = próprio; **(C)** = conjectura/programa;
> **(H)** = leitura a conferir. Contexto: `C_disjuncao_viavel.md` (Teorema 4.3;
> Lema 4.1 recorte; Lema 4.2 pureza; §3.2 `Res(k)` [Gar24]: FDP fraca falsa,
> `DD` aberto; §0: noções (i)/(ii)/(iii)).

## §0. Veredito sumário (v5 — honesto)

1. **C2.1 (teorema) (P)**: `DD ∈ P` para **resolução de largura-k**; sub-prova
   preserva largura; FDP fraca `p(t)=t` (nº de linhas; k constante). Distinção
   provada: só **FDP** (largura-k vale; [Gar24] falha para `Res(k)` — sistemas
   diferentes); `DD_{Res(k)}` **aberto**.
2. **C2.2 (PROGRAMA — não teorema nesta entrega) (C)**: a proposição
   "`DD_{Res(k)} ∈ P` sob promessa puro-respeitadora" é **plausível** (o
   referee, na rodada 3, verificou que "a adaptação deve funcionar" com os
   fallbacks), mas **quatro obrigações de prova** estão **abertas** (O1)–(O4),
>   exatamente as que o referee enumerou nas rodadas 3–4. Status: **em aberto**
   até prova completa ou contraexemplo.
3. **C2.3 (ingrediente corrigido + redução) (C)+(P)**: família **alternante**
   (exatamente um lado insat, alternando com `γ`) decide `UNSAT_CNF` via
   `DD`-solver (decodificação total) — a rota negativa reduz-se a este objeto.
4. **`Res(1)`**: `DD ∈ P` **sob a promessa** — **(C)/condicional a C2.2**
   (o programa §3); sem ela, **aberto** (retraída a versão incondicional da v3).

## §1. `Res(k)` — leitura formal

**(A)**: linhas k-DNFs; axioma `x∨¬x`; corte; ∧-introdução; enfraquecimento;
`Res(1)` ≈ resolução+enfraquecimento; `Res(k)` p-simula `Res`. **(H) a
conferir em [K19 5.7]**: **(H-corte)** corte = literal-pivô; **(H-and)**
∧-introdução truncada a k literais/termo; **(H-weakening)** `F ⟹ F∨G`.
Entrada: `Λ = ⨄_{i<m}Λ_i`, `Λ_i` CNF sobre átomos disjuntos `X_i`; linhas
k-DNF. `D ⊇ E`: inclusão de termos. DAG: uma justificação por linha.

## §2. C2.1 — Largura-k (TEOREMA, aceito nas 4 rodadas)

> **Teorema C2.1 (P).** Seja `Π` refutação de `Λ` por resolução de largura-k
> (k constante; medida = nº de linhas). O algoritmo do Teorema 4.3 devolve um
> lado `i*` com refutação de largura-**k** de `Λ_{i*}` com ≤ |Π| linhas, em
> `O(|Π|² + |Π|·m)`. Logo `DD_{Res^{≤k}} ∈ P` e FDP fraca `p(t)=t`.

**Prova.** O algoritmo é agnóstico de largura; o Lema 4.1 produz `E_i ⊆ D_i`
⟹ `|E_i| ≤ k`; pureza (Lema 4.2) e restrição são agnósticas. ∎ (Corolário do
Teorema 4.3 — conteúdo novo: a **largura** da sub-prova extraída. Nenhuma
conclusão sobre a causa da falha de FDP de [Gar24] — retraída na v2.)

## §3. C2.2 — o PROGRAMA (não teorema — v5)

### 3.1 A proposição conjecturada

> **Conjectura C2.2 (C).** Seja `Π` refutação `Res(k)` de `Λ` **puro-respeitadora**
> (promessa verificável em `O(|Π|·m)` — **objeto: `Π` ou `E`, a ser fixado
> conforme (O4)** —: toda ∧-introdução tem resultado
> estritamente `i`-puro e pais estritamente `i`-puros do mesmo lado). Então
> existe algoritmo p-time que devolve `i*` com refutação `Res(k)` de `Λ_{i*}`
> — i.e. `DD_{Res(k)} ∈ P` sob a promessa.

### 3.2 As OBRIGAÇÕES ABERTAS (as do referee, rodadas 3–4)

A prova tentada (v3/v4) falhou em pontos exatos; registram-se como programa:

> **(O1) Fallback do pivô perdido — pai correto.** Num corte `A∨l, B∨¬l ⟹
> A∨B` cujo pai perdeu o termo-pivô no recorte (caso alcançável: o `l` injetado
> por enfraquecimento e derrubado pelo reuso), a reutilização deve **preservar
> o fim em `∅`** — a v4 reusava o pai que **manteve** o pivô e o `E` podia não
> terminar em ∅ (contraexemplo do referee, rodada 4). Obrigação: caracterizar
> a direção correta do reuso (e provar que `E` termina em `∅` quando `Π` refuta).
>
> **(O2) Fechamento do passo final.** A promessa "usada como justificante"
> deixa a ∧-introdução **final** escapar (contraexemplo do referee: `(r6)`-final
> com resultado neutro acessível a lado satisfatível). Obrigação: promessa
> fechada no passo final (ou traçar retroativamente ancestrais não-neutros —
> as duas rotas apontadas pelo referee na rodada 3).
>
> **(O3) Dependentes de linhas eliminadas.** Enfraquecimento eliminado:
> dependentes de linhas eliminadas precisam de regra — **corte e
> ∧-introdução** (a v4 só tratava cortes) — **inclusive (r5) quando ambos os
> pais foram eliminados** (`E(pai₂)` inexistente: não há reuso possível).
> Obrigação: caso-análise completa dos dependentes.
>
> **(O4) Estricidade do truncamento.** `E(F)∧E(G)` pode zerar a linha
> ((H-and)) — a promessa precisa da estricidade herdada ou da remoção da linha.
> Obrigação: provar que a estricidade sobrevive ao recorte, ou redefinir a
> promessa sobre `E` pós-recorte.
>
> **(O5) Objeto e ordem únicos (ensinamento do FATAL-2/r3).** Antes de
> escrever a prova: definir **um** objeto e **uma** ordem únicos (pré-varredura
> → recorte → retro-indução), com os lemas declarados sobre o mesmo objeto —
> sem isso, a reescrita recai na contradição da v3 (\"recorte após si mesmo\").

**Por que é programa e não teorema (v5)**: a fonte exata das regras de
`Res(k)` e do Lema 4.1 não está verificada nesta frente (as leituras (H) são
minhas); 4 rodadas de referee acharam fato novo a cada tentativa de escrita —
a honestidade exige **obrigações enumeradas**, não "✓" prematuro. Se (H-*)
e (O1)–(O4) fecharem: `DD_{Res(k)} ∈ P` sob promessa (e o resto do mapa
segue); se um (O) falhar com contraexemplo: a promessa foi a errada.

### 3.3 `Res(1)` (retração mantida; **(C)** — condicional a C2.2)

`DD_{Res(1)} ∈ P` **sob a promessa** (mesma proposição — **status (C)**:
condicional ao programa C2.2, que não é teorema nesta entrega); sem ela,
**aberto** (`∧-intro(∅,F)→∅` viola a promessa — referee, rodada 3). A versão
incondicional da v3 foi **retraída**.

## §4. C2.3 — o ingrediente da rota negativa (aceito; entrada declarada)

> **(C) Família alternante de Garlík**: p-tempo, de `γ` (CNF): `(Λ₁,Λ₂)`
> disjuntos + refutação `Res(k)` pequena de `Λ₁⊎Λ₂`, **exatamente um** lado
> insat, `Λ₁` insat ⟺ `γ ∈ UNSAT`. Entrada DD: `α₁ := ¬γ` (DNF `O(|γ|)`),
> `α₂` fresca.

**Redução (P)**: solver p-time de `DD` devolve o lado insat: `γ∈UNSAT ⟹ 1`;
`γ∈SAT ⟹ 2` (decodificação **total**) ⟹ `UNSAT ∈ P` ⟹ P=NP. **Por que
[Gar24] não entrega**: reflexão k× (Dantchev–Ris) produz a refutação pequena
da união fazendo **dois** lados insat — a alternância é **o problema exato**,
em aberto **(C)**. (`TAUT_DNF` coNP-completa — fonte; `UNSAT_CNF` é a fonte
dura correta — retratações da v1 mantidas.)

## §5. Ressalvas

1. **Classe `Res(k)` inteira: aberta** — nenhum fato novo sobre ela.
2. **(H-corte)/(H-and)/(H-weakening)**: leituras a conferir em [K19 5.7];
   divergência ⟹ reescrita.
3. **C2.2 = programa (C)**; **C2.1** e **C2.3** são o que esta entrega
   **entrega como fechado** (C2.1 teorema; C2.3 redução + ingrediente).
4. **Res(1)**: só sob promessa.

## §6. Checklist (status neutro)

| # | Afirmação | Status | Onde |
|---|---|---|---|
| 1 | `Res(k)` com (H-corte)/(H-and)/(H-weakening) | (A)+(H) | §1 |
| 2 | C2.1: teorema (largura preservada; bound; FDP `p(t)=t`) | **(P) fechado** | §2 |
| 3 | C2.2: conjectura + obrigações (O1)–(O4) do referee | **(C) programa** | §3.1–3.2 |
| 4 | (O1) pivô-perdido: pai correto; fim em ∅ | aberta | §3.2 |
| 5 | (O2) passo final fechado na promessa | aberta | §3.2 |
| 6 | (O3) dependentes ∧-intro; (O4) estricidade | abertas | §3.2 |
| 7 | `Res(1)`: só sob promessa **(C)**, condicional a C2.2; incondicional retractada | retratação+(C) | §3.3 |
| 8 | alternância: redução total; [Gar24] não entrega | (C)+(P) | §4 |

## §7. Veredito e próximos passos (v5)

**Veredito (honesto)**: a entrega **não** fecha `DD_{Res(k)}` — nem positiva
nem negativamente — e **não** apresenta como teorema uma prova que o referee
derrubou quatro vezes com fato novo cada vez. O que ela entrega como
**fechado**: **C2.1** (teorema: largura-k — e a distinção largura-`Res(k)`
provada matematicamente para FDP); **C2.3** — fechada a **redução**\n(ingrediente corrigido + decodificação total); a **família alternante é o\nproblema nomeado, em aberto (C)**; e **C2.2 como
programa com as obrigações exatas** (O1)–(O5) — que são, elas mesmas, o
resultado das 4 rodadas de referee: o mapa do que falta.

**Próximos passos**: (1) referee rodada 5 (foco: o rebaixamento é aceitável?
as (O1)–(O4) cobrem tudo o que os fatais pediram?); (2) obter o texto exato
de [K19 5.7] e do Lema 4.1 (`C §2.2`) e reescrever §3 com as regras reais —
aí (O1)–(O4) ou fecham ou viram contraexemplo; (3) atacar a família
alternante (§4).

**Lacunas honestas**: C2.2 **(C)** — 4 obrigações abertas; (H-*) **(H)**;
classe `Res(k)` **aberta**.

Referee rodadas 1–4: `C2_ddres_k_referee.md` — **rodada 5: RECOMENDADO**
(v5 responde: rebaixamento + menores da r5 aplicados).

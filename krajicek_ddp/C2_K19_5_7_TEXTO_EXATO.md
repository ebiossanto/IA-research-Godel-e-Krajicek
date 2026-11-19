# C2 — Texto exato de [K19 §5.7], regras de `Res(k)` e fechamento candidato de (O1)–(O4)

**Data:** 19/11/2026 · **Frente:** C2 · **Classificação:** **(A)** texto fonte obtido +
**(P)** definições/fechamento candidato · **Status:** submetido a referee
(`C2_K19_5_7_referee.md`) · **Mandato:** `C2_O1_O5_K19_5_7.md` §4 (passos 1–3) +
ataque à família alternante (C2.3).

**Fontes obtidas nesta rodada (todas abertas/legítimas):**
- `fontes/garlik_ccc2024.pdf` — Garlík, *Failure of FDP for k-DNF Resolution*,
  LIPIcs CCC 2024 (CC-BY) — **§2 contém as regras exatas de `Res(k)`** com a
  nota "introduced by Krajíček [13] … see also **Chapter 5.7 in [15]**" ✓
- `fontes/kra01_wphp.pdf` — Krajíček, *On the weak pigeonhole principle*,
  Fund. Math. **170** (2001) 123–140 (download IMPAN) — **Def. 1.1** = sistema
  `R(f)` original (regras 1–2)
- `fontes/kraj_err.txt` — errata oficial do K19 (já no repo)
- **K19 livro texto integral: NÃO obtido** (CUP) — mas a *via* ch5.7 está
  confirmada por duas citações independentes (Garlík §2 + rodapé 1)

---

## 1. Correção de atribuição (achado metodológico importante)

> **"Lema 4.1" NÃO é de Krajíček.** O `C2_O1_O5_K19_5_7.md` §1/§1.1 tratava
> "(H-corte)/(H-and)/(H-weakening)" como *leituras de um lema de [K19] §5.7*.
> O próprio `C_disjuncao_viavel.md` (Lema 4.1 **(B)** — recorte) declara na
> linha 283: *"o Lema 4.1 … **não é discutido nas fontes que consultamos**"*.
> Portanto:
> - **[K19 §5.7] = as REGRAS de `Res(k)`/R(f)** (definição) — **(A), agora
>   obtido** (Garlík §2, citando ch5.7; original Kra01 Def. 1.1);
> - **Lema 4.1 (recorte/projeção) = nosso (B)** — nunca houve leitura-alvo de
>   Krajíček a conferir; o que se precisa era o **texto das regras**, e ele
>   está agora em mãos.
>
> Consequência: os passos 1–2 do plano de verificação do `C2_O1_O5` estão
> **EXECUTADOS**; os passos 3–5 viram a §3–§4 deste documento.

---

## 2. Texto exato — as regras de `Res(k)` **(A)**

**Referência:** Garlík, CCC 2024, §2 (p. 33:8 do artigo; layout conferido na
extração em modo *layout* do PDF): *"The lines in `Res(k)` consist of k-DNFs.
The inference rules of `Res(k)` are the following (**A,B são k-DNFs, j ∈ [k],
l, l₁,…,lⱼ literais**):"*

```
(1) Axiom:           x ∨ ¬x

(2) ∧-introduction:  A ∨ l₁        B ∨ (l₂ ∧ ··· ∧ lⱼ)
                     ─────────────────────────────────  (j ∈ [k])
                        A ∨ B ∨ (l₁ ∧ ··· ∧ lⱼ)

(3) Weakening:       A
                     ─────────
                        A ∨ B

(4) Cut:             A ∨ (l₁ ∧ ··· ∧ lⱼ)      B ∨ ¬l₁ ∨ ··· ∨ ¬lⱼ
                     ─────────────────────────────────────────────
                                    A ∨ B
```

**Verificações de solidez (P):** (2) `(A∨l₁)∧(B∨l₂…lⱼ) ⊨ A∨B∨(l₁…lⱼ)` ✓;
(3) `A ⊨ A∨B` ✓; (4) se `A,B` falsos: primeiro premissa força todos `lᵢ`
verdadeiros, segunda força algum `lᵢ` falso → contradição ✓. **Nota (A):**
a leitura "Weakening = `A ⟹ A∨B`" é a única sólida (a alternativa
`A∨B ⟹ A∨(termo)` seria **insólida** — descartada; Garlík confirma a versão
sólida no layout).

**Cruzamento com Kra01 Def. 1.1 (sistema `R(f)` original) (A):**
- Regra 1 de Kra01: `(C₁ ∪ {⋀ⱼ lⱼ}) , (C₂ ∪ {¬l₁,…,¬l_k}) ⟹ C₁ ∪ C₂`
  (lᵢ entre os lⱼ, k≥1) = **o Cut (4)** ✓ (com `j=1` é resolução clássica).
- Regra 2 de Kra01: `(C₁ ∪ {termo u}) , (C₂ ∪ {termo v}) ⟹ C₁ ∪ C₂ ∪ {termo u+v}`
  = **a ∧-introdução (2)** no caso `u=1` (iterável para `u,v ≥ 1` com
  intermediários ≤ k) ✓.
- **`R(f)`**: f não-decrescente; prova de `R(f)`-tamanho s = linhas são
  f(s)-DNFs e `|Π| ≤ s`; **`Res(k)` = `R(f)` com f ≡ k** (Garlík rodapé 1,
  citando ch5.7) ✓.

---

## 3. Regras de projeção `E` para `Res(k)` — definição **(P)** (objeto/ordem de (O5))

**Objeto único (O5, já definido em `C2_O1_O5` §2.5):** `O = (V, E_dag, λ, w)`
— vértices/arestas/rótulos fixos; `w : V → {1,2,0}` computado na pré-varredura;
**ordem única `≺`** = ordem topológica lexicográfica. Duas passagens:

**(a) Passada reversa de DEMANDA** `R(v)` = estruturas-pivô que os consumidores
de `v` exigem que `E(v)` retenha:
- consumidor **Cut (4)** com premissas `u₁,u₂`: exige `termo(l₁…lⱼ)` em `E(u₁)`
  e **o conjunto completo** `{¬l₁,…,¬lⱼ}` em `E(u₂)` (all-or-nothing);
- consumidor **∧-intro (2)**: exige `l₁` em `E(u₁)` e `termo(l₂…lⱼ)` em `E(u₂)`;
- decomposição recursiva: demanda sobre linha **∧-intro** decompõe
  (pivô combinado → demandas nos pais); sobre **Weakening** repassa para `E(u)`
  **e** registra os termos novos de `B`; sobre **Cut** repassa aos pais via
  `A∨B`; folhas/axiomas: demanda ⊆ termos disponíveis (singleton — CNF).
- Invariante-chave (a provar): **toda demanda é satisfatível** — termos
  multi-lit só nascem em ∧-intro (demanda decompõe) ou entram por Weakening
  (adicionáveis); singletons só vêm de folhas/weakening ✓.

**(b) Passada direta de `E`** (em `≺`):
- **Folha** `C ∈ Λ`: `E(v) := C`. **Axiom**: `E(v) := x∨¬x`.
- **Weakening** `u ⟹ v = A∨B`: **`E(v) := E(u) ∪ {termos de B exigidos por R(v)}`**
  (descartar o não-exigido; adicionar os exigidos — derivável pela própria
  regra, `⊆ λ(v)` ✓, pureza preservada: termos exigidos são do mesmo lado,
  §4 abaixo).
- **Cut** `u₁,u₂ ⟹ v = A∨B`: **se** `termo(t) ∈ E(u₁)` **e** `{¬lᵢ} ⊆ E(u₂)`
  **(retención total):** `E(v) := corte(E(u₁), E(u₂)) = A'∨B'` (regra (4)
  aplicada — largura preservada: termo de tamanho j≤k);
  **senão:** reuso — `E(v) := E(u₁)` se `E(u₁) ⊆ A` (i.e. perdeu o termo),
  senão `E(v) := E(u₂)` se `E(u₂) ⊆ B` (nenhum `¬lᵢ` retido), senão
  **ambos os pais perdidos-parcialmente** → ver §4 (caso (O1′)).
- **∧-intro** `u₁,u₂ ⟹ v`: **se** `l₁ ∈ E(u₁)` **e** `termo(l₂…lⱼ) ∈ E(u₂)`:
  `E(v) := ∧-intro(E(u₁), E(u₂))` (regra (2) — largura `j ≤ k` ✓);
  **senão:** reuso do pai cujo `E ⊆ λ(v)` (pai que perdeu a peça: `E(u₁)=A'⊆A⊆λ(v)`
  ou `E(u₂)=B'⊆B⊆λ(v)`); se **ambos retiveram peça incompleta** → caso (O4′).

**Diferença estrutural vs. Lema 4.1 (resolução clássica) (P):** em resolução
clássica o pivô é um literal e "perder o pivô" implica `E ⊆ resolvente`
(fallback sempre disponível). Em `Res(k)` o pivô do Cut-premissa-1 é um
**termo** e o da premissa-2 é um **conjunto de singletons** — "perda parcial"
é possível (algumas demandas satisfeitas, outras não) e **nem todo pai
degradado é reusável**. É a razão exata pela qual (O1)/(O3)/(O4) existem.

---

## 4. Status de (O1)–(O4) contra as regras exatas (análise (P))

| Obrigação | Status candidato | Argumento |
|---|---|---|
| **(O1)** fallback do pivô perdido | **Fecha com a passada de demanda** | A demanda all-or-nothing garante: no Cut, ou ambos os pivôs estão retidos (corte próprio) ou `E(u₁)` perdeu o termo inteiro (`E(u₁)=A'⊆A⊆λ(v)` → reuso válido) ou `E(u₂)` perdeu **todos** os `¬lᵢ` (`E(u₂)=B'⊆B⊆λ(v)` → reuso). A "perda mista" (alguns `¬lᵢ` retidos) é **eliminada pela política all-or-nothing**: `R(u₂)` exige o conjunto completo ou nenhum. **A direção correta do reuso = o pai cuja perda foi total**, não o que "manteve o pivô" (erro da v4). |
| **(O2)** fechamento do passo final | **Fecha — rota 1** | A promessa "∧-intro com resultado e pais i-puros" + a folha `∅` (cláusula vazia é `k`-puro para qualquer lado, convenção `w(∅)=0`) + retro-indução `w(v) := w(ancestral não-neutro)` (definida em (O5)) cobrem o `(r6)`-final: a linha final só é neutra se toda ascendência for — mas toda raiz de refutação acessível é `∅`/axioma, e `x∨¬x` é puro. **Rota 2** (retro-indução) fica como alternativa se a promessa de folhas for alargada. |
| **(O3)** dependentes de linhas eliminadas | **Fecha (caso-análise completa)** | A passada direta define `E` para **todo** vértice (não "recalcula filhos"): Cut e ∧-intro têm ramo próprio (retención) **e** ramo de reuso; Weakening adiciona demandas; **ambos-pais-mortos** = reuso de qualquer pai com `E ⊆ λ(v)` — existe sempre que a perda foi total nos dois (demanda all-or-nothing impede mista). |
| **(O4)** estricidade `E(F)∧E(G) ≠ ∅` | **Fecha com a convenção de linha vazia; caso (O4′) declarado** | Em `Res(k)`, `E = ∅` só como **cláusula vazia** (fim da refutação) — ∧-intro nunca produz `∅` (conclusão tem `A∨B` e ao menos o termo exigido). O perigo "zerar a linha" era da leitura pós-hoc com truncamento — **não existe** na definição (P): não há truncamento, há retenção demandada. Resta **(O4′)**: ambos os pais com retenção incompleta **incompatível com reuso** — **eliminado** pela passada de demanda (a demanda foi feita *antes*, na passada reversa). |
| **(O5)** objeto/ordem únicos | **(P) — já feito** | `O` e `≺` fixados; as duas passagens operam sobre o mesmo `O` (nada de "recorte após si mesmo"). |

**Teorema candidato C2.2′ (P) — a ser submetido ao referee:** sob a promessa
puro-respeitadora, o algoritmo de duas passagens devolve `i*` com refutação
`Res(k)` de `Λ_{i*}` com `≤ |Π|` linhas e largura `k` — i.e.
`DD_{Res(k)} ∈ P` sob a promessa. **Prova:** indução em `≺` com o invariante
*"`E(v) ⊆ λ(v)`, `E(v)` é puro sobre `w(v)`, e `E(v)` retém todas as demandas
`R(v)`"*; folhas base; os quatro casos da §3; pureza por compartilhamento de
variáveis-pivô (Lema 4.2 adaptado: pivôs de um consumidor são variáveis de
ambos os pais → mesmo lado); fim: `E(raiz) = ∅` ⇒ extração retroativa pura
(Lema 4.2(2) + acessibilidade), `≤ |Π|` linhas, largura preservada.

**Lacunas honestas (para o referee):**
1. **(G1) BLOQUEANTE — conflito de demandas** (referee r1-A3): consumidores
   distintos de uma mesma linha podem exigir políticas **incompatíveis** (um
   exige retenção de pivô; outro exige perda-total para permitir reuso). A §3a
   como escrita **não resolve conflito** — a passada reversa precisa de uma
   **política de prioridade** (ex.: demanda do consumidor mais próximo da raiz
   vence; ou retenção sempre que possível e fallback de reuso provado
   compatível) **com prova de consistência**, ou de um **contraexemplo
   exaustivo** em instâncias pequenas (enumeração de DAGs Res(k) ≤6 linhas).
   **Enquanto (G1) não fechar: (O1)–(O4) permanecem (C).**
2. **(G2) BLOQUEANTE — pureza em `Res(k)`** (referee r1-A4): a adaptação da
   Lema 4.2(2) (pivô compartilhado ⇒ mesmo lado) está **pressuposta**, não
   provada, para pivô = **termo** (Cut premissa-1) vs pivô = **conjunto de
   singletons** (premissa-2); e a pureza da regra Weakening com adição de
   termos exigidos (§3b) depende dela.
3. **(G3)** Custo: passada reversa é linear no DAG; total `O(|Π|²+|Π|·m)` —
   confirmar com o Teorema 4.3.
4. **(G4)** K19 livro integral continua não lido (ch5.7) — a regra (3)
   Weakening `A⟹A∨B` é a reconstrução sólida do layout de Garlík; **conferir
   no livro** quando houver acesso (a única leitura com risco residual);
   bem como a prova negativa "Lema 4.1 é nosso" vale **para as fontes
   obtidas** (Garlík, Kra01, errata) — não para o livro não lido (r1-A2).

---

## 5. Família alternante (C2.3) — ataque via reflexão com lado "espectador"

**Objetivo (C):** decidir `UNSAT_CNF` via `DD`-solver sobre a família alternante
(exatamente um lado insat, alternando com `γ`): a rota negativa reduz-se a
`DD_{Res(k)} ∈ P` **sem promessa** — ou seja, precisamos que a promessa
puro-respeitadora **se cumpra por construção** nas instâncias da família.

**Construção candidata (P) — reflexão com espectador satisfatível:**
1. **Base (A):** Garlík Thm 1: `Aₙ ∧ B_{n,k}` tem refutação `Res(2)` pequena
   (`O(k2n^{7k+7})`), `Aₙ` insat com prova longa, `B_{n,k}` insat com prova
   exponencial — o par **não é alternante** (ambos insat). A família alternante
   exige **exatamente um** lado insat.
2. **Engenharia (P):** dado `γ` (3-CNF), tomar
   `Λ₁ := CNF(¬γ)` (insat ⟺ `γ ∈ UNSAT` — nota: `α₁ := ¬γ` como DNF, entrada
   DD) e **`Λ₂ :=` espectador SAT** construído para "esconder" a insatisfação:
   `Λ₂ :=` cláusulas tautológicas/ satisfatíveis sobre variáveis frescas `Z`
   **mais** a codificação da refutação pequena de `Λ₁ ⊎ Λ₂` que usa `Z` como
   *variáveis de trabalho* — o truque da reflexão de Garlík: a fórmula
   `SAT ∧ R^kREF` tem refutação pequena porque um lado "espectador" fornece a
   estrutura de refutação **satisfatível** quando a atribuição-testemunha existe.
3. **Promessa por construção (C):** conjectura testável: nas instâncias
   (2), toda ∧-intro do DAG tem pais do mesmo lado — **falsificável** por
   enumeração de pequenas `γ` (Z3/geração de DAGs).

**Próximo passo concreto (N2):** script `gk_alternating_family.py` — gerar
`(Λ₁, Λ₂)` para `γ` aleatórios pequenos (n≤8), construir a refutação
`Res(2)` via Garlík-Thm1 (ou busca), testar a promessa puro-respeitadora
por inspeção do DAG. **Se a promessa falhar:** a rota negativa fecha como
**retração** de `DD_{Res(k)} ∈ P` sem promessa (resultado negativo honesto).
**Se passar:** alimenta o Teorema candidato da §4 para a família.

---

## 6. Próximos passos

1. **Referee** (obrigatório) — foco: §4 (G1) satisfatibilidade de demanda,
   (G2) pureza em `Res(k)`, (G4) conferência do livro.
2. Se (G1)–(G3) fecharem: re-submeter `C2_ddres_k.md` §3 como **v6 (teorema
   sob promessa)** — a promessa passa a ter verificação `O(|Π|·m)`.
3. Script da §5 (N2) — teste da promessa por construção na família alternante.
4. K19 livro (acesso) → conferir regra Weakening (G4) e fechar a última (H).

---

*Referências:* Garlík CCC 2024 DOI 10.4230/LIPIcs.CCC.2024.33 (§2, rodapé 1) ·
Kra01 Fund. Math. 170 (2001) Def. 1.1 · K19 = Krajíček, *Proof Complexity*,
CUP 2019, ch5.7 (DOI 10.1017/9781108242066) · `C_disjuncao_viavel.md`
(Lema 4.1/4.2, Teorema 4.3) · `C2_O1_O5_K19_5_7.md` (obrigações)

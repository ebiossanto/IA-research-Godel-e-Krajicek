# 01 — Núcleo duro do espectro de limiares de prova

Status: **verificado** (definições + teoremas locais) / **condicionado** (gadget de transferência e grau de Turing).
Classificação editorial (níveis da Etapa 18 da organização): A = definição, B = lema elementar provado, C = teorema condicionado, D = conjectura.

Este documento reúne apenas o que resiste à verificação. Os artefatos de formatação, lacunas e vereditos bibliográficos estão em `02_REVISAO_CRITICA.md`.

---

## 1. A pergunta central

> A distribuição dos comprimentos mínimos de prova induz uma geometria espectral capaz de controlar a complexidade dos geradores de Krajíček?

Cadeia proposta: `ℓ_T → B_T → C_T → g_T^[b] → τ`.

O que é novo em relação à literatura: não a parametrização por `b(n)` (Nível B, ver 02), mas o **objeto espectral** `Φ ↦ L_T(Φ) ↦ ρ_T(Φ) ↦ C_T(L) ↦ R_T(L)` — uma formulação que não foi encontrada nas buscas realizadas (com as ressalvas de método registradas em 02, §3).

---

## 2. Definições (Nível A)

Convenções: linguagem L; teoria T; codificação binária de fórmulas/sentenças/provas; comprimento |·|; relação `Prf_T(π,θ)`; ordem lexicográfica; prefixo `w ⪯_e x`. **Todas essas convenções estão fixadas, com decisões D1–D11 e provas, em `01_ambiente_formal_e_codificacoes.md` (Etapa 1) — em caso de conflito, vale aquele documento.**

**Sentença gerada.** Para Φ(x) com uma variável livre e palavra binária w:

    Φ^w := ∃y ∀x>y ( Φ(x) → ¬(w ⪯_e x) ).

**Candidatos.** `W_Φ = {0,1}^{q(Φ)} = {w_0 <_lex … < w_{k_Φ−1}}`, `k_Φ = 2^{q(Φ)}`. **`q(Φ) = |Φ| + 1`** — fixado em `01_ambiente_formal_e_codificacoes.md` §3 (D7): a aritmética do stretch de `g_T` (`|w₀u₀| = n+1`) mais as três ocorrências concordantes do paper original e dos fontes da linha; lá está registrado também o erratum aparente no passo 2 de `[K23]`. A escolha não afeta os teoremas locais (dependem só do seletor), mas é necessária para o gadget (§5).

**Comprimento mínimo (Nível A).**

    ℓ_T(Φ,w) := min{|π| : Prf_T(π, Φ^w)},   ℓ_T(Φ,w) := ∞ se T ⊬ Φ^w.

**Seletor (núcleo do gerador, Nível A).**

    J_{T,Φ}(c) := min { j < k_Φ : ℓ_T(Φ,w_j) > c }   (= k_Φ se vazio).

O gerador limitado é `g_T^[b](u) = Out(u, w_{J_{T,Φ}(b(n))})`. Todos os teoremas locais dependem apenas de `Φ, c ↦ J_{T,Φ}(c)`, não dos detalhes de `Out`.

**Perfil (Nível A).** `L_T(Φ) = (ℓ_T(Φ,w_0), …, ℓ_T(Φ,w_{k_Φ−1})) ∈ (ℕ∪{∞})^{k_Φ}` — determina completamente `c ↦ J_{T,Φ}(c)`.

**Primeiro não demonstrável (Nível A).** `j*_T(Φ) := min{j : ℓ_T(Φ,w_j)=∞}` (= k_Φ se vazio).

**Limiar final (Nível A).** `ρ_T(Φ) := max_{j < j*_T(Φ)} ℓ_T(Φ,w_j)` (max vazio = 0). Sempre finito: o máximo é tomado só sobre coordenadas finitas.

**Escada de limiares (Nível A).** Índices de recorde:

    I_T(Φ) := { j < j* : ℓ_j > max_{i<j} ℓ_i },   max_∅ := −1
    B_T(Φ) := { ℓ_j : j ∈ I_T(Φ) }   — estritamente crescente.

**Espectros globais (Nível A).**

    S_T(L)  := { ρ_T(Φ) : Φ admissível, |Φ| ≤ L }          (limiares finais)
    C_T(L)  := ⋃_{|Φ|≤L} B_T(Φ)                            (todas as transições)
    R_T(L)  := max S_T(L) = max C_T(L)                     (envelope; conjuntos não vazios)

Versões operacionais: `F_n = {Φ : ∃u∈{0,1}^n, Form_n(u)=Φ}`; `S^op_T(n)`, `C^op_T(n)`. Transporte do orçamento: `B_b(L) := b(2^L)`. Comparação correta: `C_T(L)` versus `B_b(L)`.

**Diferença importante (Nível A):** `S_T(L) ≠ C_T(L)` em geral — `S_T` guarda só o último limiar de cada fórmula; `C_T` guarda todas as transições efetivas.

---

## 3. Teoremas locais (Nível B — provados e verificados por enumeração)

As provas estão no `Núcleo formal mínimo` (§5–7). A verificação exaustiva por script (`src/python/verifica_espectro.py`) testou **410.155 perfis** (k = 1,…,6,8; valores {0,1,2,3,∞}) e **7.737.331 pares (c₁,c₂)**, com todos os testes passando (`src/python/resultado_verificacao.txt`).

**Teorema 5.1 (estabilização local).** `c ≥ ρ_T(Φ) ⟹ J(c) = j*`.
**Fortalecimento (iff — incorporar ao texto):** `J_{T,Φ}(c) = j*_T(Φ) ⟺ c ≥ ρ_T(Φ)`.
Prova da direção inversa (faltava no fonte): se `c < ρ`, existe `j₁ < j*` com `ℓ_{j₁} = ρ > c`; logo `J(c) ≤ j₁ < j*`, logo `J(c) ≠ j*`. **ρ é o limiar exato**, não apenas uma suficiência. (Verificado em T5.1b do script.)

**Lema 6.1 (monotonicidade).** `c₁ ≤ c₂ ⟹ J(c₁) ≤ J(c₂)`.

**Teorema 6.2 (transições unitárias).** Para todo `r ≥ 1`:

    J(r−1) ≠ J(r)  ⟺  r ∈ B_T(Φ).

**Teorema 6.3 (intervalos).** Para `c₁ ≤ c₂`:

    J(c₁) ≠ J(c₂)  ⟺  B_T(Φ) ∩ (c₁, c₂] ≠ ∅.

**T4.1.** `j* = 0 ⟺ B_T = ∅ ∧ ρ = 0`; e `j* > 0 ⟹ ρ = max B_T`.

**Corolários 7.1–7.3.** Comparação exata entre dois orçamentos `b₁ ≤ b₂`: `J(b₁(n)) ≠ J(b₂(n)) ⟺ B_T(Φ) ∩ (b₁(n), b₂(n)] ≠ ∅`; consequência para `g_T^[b₁] ≠ g_T^[b₂]` **sob injetividade de Out**; e a condição necessária para diferença infinita (sequência de fórmulas com limiares atravessando a janela). Coincidência eventual para fórmula fixa e `b₁,b₂ → ∞`.

**Observação verificada (novo no fonte).** O salto `|J(r)−J(r−1)|` pode ser maior que 1 na transição (exemplo documentado `(2,10,7,∞)`: `J(9)=1`, `J(10)=3`; salto máximo observado na enumeração: 8). A caracterização é sobre `≠`, não sobre o tamanho do salto.

**Exemplo-padrão.** `L = (2,10,7,∞)` ⟹ `j*=3`, `B_T={2,10}`, `ρ=10`; o valor 7 não produz transição (o candidato de comprimento 10 já bloqueia antes).

**Realização.** Toda escada finita estritamente crescente (inclusive vazia) é `B_T` de algum perfil: dado `b₀<…<b_r`, o perfil `(b₀,…,b_r,∞)` funciona (57 escadas sobre {0..5}, comprimento ≤ 4, verificadas). Portanto `C_T(L)` pode ser arbitrariamente esparsa ou arbitrariamente densa **do ponto de vista puramente combinatório** — o conteúdo real da pergunta é o que as teorias T concretas produzem.

---

## 4. Onde o gerador vive: hipóteses (resumo do §9 do núcleo)

| Nível | Hipóteses necessárias |
|---|---|
| Definições (`ℓ, ρ, B, S, C`) | noção finita de prova; `Prf` bem definida; `W_Φ` finito; `Φ^w` efetivamente construível. **Sem** consistência, correção ou decidibilidade. |
| `g_T^[b]` computável | `Prf` decidível; enumeração `|π| ≤ b(n)`; `b`, `Out`, extração de `Form` computáveis. `Thm(T)` **não** precisa ser decidível (busca limitada). |
| tempo polinomial | `Prf` verificável em ptime; `|W_Φ| ≤ n^{O(1)}`; `|Φ^w| ≤ n^{O(1)}`; custo de enumeração `2^{O(b(n))}`; `b(n) = O(log n)` ⟹ `2^{O(b(n))} = n^{O(1)}`. |
| interpretação semântica | correção (`T ⊢ θ ⟹ ℕ ⊨ θ`) ou apenas Σ₁/Π₁-correção — **não pode ficar escondida dentro das definições sintáticas**. |
| versão Σ^b₁ | demonstrar que `w ⪯_e x` é definível na classe; `(Φ,w) ↦ Φ^w` preserva a classe; formalização em `S^1_2`; gadget `θ ↦ Φ_θ` preserva a classe. |

Os teoremas da §3 são **sintáticos**: valem mesmo para T inconsistente (nesse caso `j* = k_Φ` e a estabilização continua valendo).

---

## 5. Gadget de transferência `θ ↦ Φ_θ` (Nível C — condicionado)

Status: **padronizado na versão bloco (D11 de `01_ambiente_formal_e_codificacoes.md`); esboço de prova completo; obrigações 1–7 não formalizadas linha a linha.** É a auditoria da Etapa 7 do plano — nada aqui deve ser citado como teorema fechado. A versão "timeout" (busca de provas) fica registrada como alternativa em `01_ambiente` §7.4.

**Correção registrada (26/09/2026).** A versão anterior deste §5 misturava a construção "timeout" com uma análise de blocos que só vale para a versão bloco (a conclusão "`j*` = primeira palavra do bloco 11" é falsa para timeout — lá `j* = k_Φ` quando `T ⊢ θ`). Padrão agora: **bloco**.

**Construção padrão (versão bloco; `[DK]` linha 1330).** Para sentença `θ`:

    Φ_θ(x) := (11 ⊆_e x) ∨ ( ¬θ ∧ (10 ⊆_e x) )
    w*_θ   := 10^{|Φ_θ|}     (primeira palavra de comprimento q = |Φ_θ|+1 que começa por 1;
                              primeiro candidato do bloco 10; |w*| = |Φ_θ|+1 vale por D7)

`|Φ_θ| ≤ a|θ| + b` é imediato (código de `¬θ` tem comprimento `|θ|+O(1)`), sem circularidade `|Φ_θ|` vs `|w|` (o candidato não é embutido em `Φ_θ`).

**Análise dos quatro blocos** (candidatos de comprimento `q = |Φ_θ|+1`, particionados pelos dois primeiros bits):

- **Blocos `00…`/`01…`:** `Φ_θ(x)` exige prefixo `10`/`11`, logo nenhum `x ≥ 1` do cilindro satisfaz `Φ_θ` (cilindros com prefixo `0` são vazios para `x ≥ 1` — binário sem zeros à esquerda) ⟹ `Φ^w` verdadeira trivial, prova `≤ a(|θ|+q)+c` **(P6)**;
- **Bloco `10…`:** no cilindro `Φ_θ(x) ⟺ ¬θ` (constante) ⟹ `T ⊢ (Φ^w ↔ θ)` com prova `≤ a(|θ|+q)+c` **(P7)** — direções puramente sintáticas, **sem correção**;
- **Bloco `11…`:** cilindro infinito e cofinal, `Φ_θ(x)` vale nele todo ⟹ `Φ^w` é **falsa em ℕ**; usar **correção/soundness** **(P5)** para concluir `T ⊬ Φ^w`.

**Localização de `j*` e cotas de `ρ` (Nível C, se as obrigações forem provadas):**

- se `T ⊢ θ`: `j*` = primeiro candidato do bloco 11 (`= 11·0^{|Φ_θ|−1}`) e `s_T(θ) − a(|θ|+q) − c ≤ ρ_T(Φ_θ) ≤ s_T(θ) + a(|θ|+q) + c` (o máximo é sobre os blocos 00/01/10);
- se `T ⊬ θ`: bloco 10 falso ⟹ `j* = índice de w*_θ` e `ρ_T(Φ_θ) ≤ a(|θ|+q)+c` (só blocos 00/01).

**Consequência (Nível C, se as obrigações acima forem provadas):**

    R_T(L) ≥ ρ_T(Φ_θ) ≥ s_T(θ) − a(|θ|+q) − c    para T ⊢ θ,
    M_T(m) ≤ R_T(a·m + b) + c                     — transferência quantitativa com escala linear (P8);
    R_T ≡_T Thm(T) ≡_T ∅'   para T ∈ {S^1_2, PA}   (direções: ver §6; versão Σ^b_1: ver 01_ambiente §4.3).

**Obrigações (Etapa 7 — lista fechada em `01_ambiente` §7.3):** 1. linearidade `|Φ_θ| ≤ a|θ|+b` (já imediata aqui); 2. uniformidade p-tempo de `(θ,w) ↦ Φ_θ^w` e `|Φ_θ^w| ≤ a'|Φ_θ|+|w|+b'`; 3. Lema dos blocos 00/01 formalizado (P6); 4. equivalência do bloco 10 com custo linear (P7) — núcleo; 5. falsidade do bloco 11 com (H-som) isolada; 6. classe sintática: `Φ_θ ∈ Σ^b_1 ⟺ θ ∈ Π^b_1`; 7. combinar na transferência.

**Advertência (da organização, mantida):** a passagem `T ⊬ Φ^w` (blocos 11) usa correção de T **(P5)** e não pode ser tratada como puramente sintática; as equivalências do bloco 10, não. Separar em cada direção exatamente onde entram consistência, correção, Σ₁-correção e reflexão externa.

**Polaridade alternativa (relação com o projeto Gödel).** O gadget "padding" do projeto Gödel, `Φ_θ(x) := ∃p,z[Prf_T(p,θ) ∧ x = pad(w*,p,z)]`, satisfaz `Φ^{w*} ↔ T ⊬ θ` (polaridade invertida); o caso `θ = ⊥` é exatamente o **Lema 3** (`Φ_T^{w*} ↔ Con(T)`), já provado em Lean (`Gödel/lean4/Gothic_Generators/Core.lean`, `lemma3_con`). O gadget bloco acima tem polaridade positiva (`ρ` grande ↔ `T ⊢ θ`), que é o que o espectro precisa. Ver `04_CONTINUIDADE.md`.

---

## 6. Grau de Turing (Nível C — um lado elementar, outro condicionado)

Sejam `M_T(m) := max{ s_T(θ) : T ⊢ θ, |θ| ≤ m }` e `s_T(θ) := ℓ mínimo de prova de θ`.

**(i) `M_T ≡_T Thm(T)` — elemento novo, prova elementar (ver 02, §3.2).**
- `M_T ≤_T Thm(T)`: perguntar ao oráculo quais θ são teoremas; para cada um, achar a prova mais curta por enumeração (para).
- `Thm(T) ≤_T M_T`: para decidir `T ⊢ θ`, calcular `M_T(|θ|)` no oráculo e buscar provas de θ com `|π| ≤ M_T(|θ|)` (busca finita). Se θ é teorema, `s_T(θ) ≤ M_T(|θ|)` por definição do máximo — acha; se não é, não acha.

**Consequência:** `M_T` é ∅'-completo para `T = PA, S^1_2` (pois `Thm(T)` é Σ⁰₁-completo). Logo **a alegação "o envelope não tem majorante computável" é equivalente, em grau, a uma verdade clássica** — o conteúdo não está no grau de Turing.

**(ii) `R_T ≤_T Thm(T)` (e `R_T^Σ ≤_T Thm(T)`) — direção fácil.** Com oráculo para `Thm(T)`: para cada Φ de tamanho ≤ L, determinar `j*` (pertinência de `Φ^w` a Thm), achar cada comprimento mínimo por enumeração, calcular `ρ` e o máximo. Vale para ambas as versões de classe (a enumeração não usa nada da classe).

**(iii) `Thm(T) ≤_T R_T` — condicionada ao gadget (Nível C).** Procedimento limpo (01_ambiente §7.2): dado θ, calcular `Φ_θ` e `L = |Φ_θ|`, pedir `R_T(L)`, e buscar prova de `Φ_θ^{w*}` de tamanho `≤ R_T(L)`. Se `T ⊢ θ`: `ℓ_T(Φ_θ,w*) ≤ ρ_T(Φ_θ) ≤ R_T(L)` (o candidato `w*` precede o bloco 11) → acha; se `T ⊬ θ`: `Φ_θ^{w*}` é falsa → por correção de T não há prova → não acha. Para a **versão `Σ^b_1`** o mesmo vale com `R_T^Σ` **condicionado** a `θ ∈ Π^b_1` (o gadget bloco tem `Φ_θ ∈ Σ^b_1 ⟺ θ ∈ Π^b_1`) — ver a questão aberta de 01_ambiente §4.3.

**Conclusão (Nível C):** `R_T ≡_T Thm(T) ≡_T ∅'`, condicionado a (iii) — e `R_T^Σ ≡_T Thm(T)` com a ressalva de classe do parágrafo anterior. E, em qualquer caso, `R_T` **não possui majorante computável** (pois caso contrário `R_T` seria computável e, por (iii), `Thm(T)` também). A "lei de crescimento" `∀f computável, R_T(L) > f(L)` para infinitos L é exatamente essa — e seu ancestral clássico é o **teorema de speed-up de Gödel (1936)** para `s_T`. Ver 02, §3.2.

---

## 7. O que este núcleo NÃO estabelece

1. **Não** estabelece hierarquia `b₁ < b₂ ⟹ g_T^[b₁] ≺ g_T^[b₂]` (o orçamento modifica o próprio gerador).
2. **Não** trata diferença de **imagem**: `g^[b₁](u) ≠ g^[b₂](u)` não implica `rng(g^[b₁]) ≠ rng(g^[b₂])` (Corolário 7.3 admite isso explicitamente).
3. **Não** há ponte quantitativa com `τ(g_T^[b])` — é a principal lacuna científica (Etapa 14).
4. **Não** há informação sobre a geometria de `C_T(L)` além da realizabilidade combinatória — é onde está o maior potencial de originalidade (Etapa 9).
5. **Não** reivindica novidade para a parametrização `log n → b(n)` (Nível B; Krajíček tem prioridade, ver 02 §3.1).
6. **Não** estabelece o custo p-tempo de `Form`/`Tail`/`Out` (Etapa 2). Obs.: a acessibilidade `F_n` — antes em aberto — agora é **igualdade** `F_n = {Φ admissível : |Φ| ≤ ⌊log n⌋}` (`n ≥ 1`), com `Form_n` fixada em `01_ambiente` §5.1 (Lema 5.2, prova elementar).

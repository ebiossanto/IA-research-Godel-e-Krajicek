# gk_alternating_family — Codificação REF_t e teste da família alternante

**Origem:** extensão do repositório
[IA-research-Godel-e-Krajicek](https://github.com/ebiossanto/IA-research-Godel-e-Krajicek)
(MIT) — núcleo: frente **C2.3** (família alternante) e o **critério-LP**
do r2 (`krajicek_ddp/C2_LP_familia_alternante.md` + referee).
**Código:** `gk_alternating_family.py` · **Dados:**
`gk_alternating_family_t{6,2}_n5.{csv,json}` · **Auditoria:**
`krajicek_ddp/C2_LP_referee.md`

## Como citar

> Soares dos Santos, E. (2026). *gk_alternating_family — REF_t encoding
> and line-purity (LP) criterion test* [Software]. Em:
> IA-research-Godel-e-Krajicek.
> <https://github.com/ebiossanto/IA-research-Godel-e-Krajicek>. MIT.

---

## 1. O que é

Teste N2 do **critério-LP** para a *família alternante* (C2.3): dado γ,
constrói o par `(Λ₁, Λ₂) = (γ, REF_t(γ))` — `REF_t(γ)` = CNF que decide
*"existe refutação Res(γ) com ≤ t **linhas**"* — e mede: **T1** taxa de
alternância, **T2** linhas mistas em provas da união, **T3** controle.
Base para `gk_minref` (mesma codificação, encoder corrigido).

## 2. Para que serve (aplicações)

1. **Decidir o destino da rota negativa** `DD∈P ⟹ P=NP` do projeto:
   o critério-LP pergunta se as refutações da família são linha-puras;
2. **Ferramenta de alternância**: "para t≥t₀, γ tem refutação ≤ t linhas?"
   (fronteira exata — validada);
3. Fonte do **6º bug do projeto** (sobreposição) e da verificação
   **exaustiva92/92** que salvou os resultados do teste LP.

## 3. Como usar

```bash
python gk_alternating_family.py --n 5 --t 6 --samples 100 --m-min 25 --m-max 45
# → gk_alternating_family_t6_n5.{json,csv} (sha normalizado CRLF→LF)
# saída: T1 alternância | T2 mistas | T3 controle
```

## 4. Arcabouço matemático

### 4.1 Codificação `REF_t(γ)` (semântica de linhas)

Variáveis `y_{j,C}` (`C` ∈ fecho/`pool`, `j ∈ [1..t]`):
(1) `y_{t,∅}`; (2a) `⋁_C y_{j,C}`; (2b) **exatamente-um** por posição —
AMO sequencial (aux `r_{j,i}`) **ou** pairwise `¬y_{j,C₁} ∨ ¬y_{j,C₂}`;
(3) `y_{j,C} → [C∈γ] ∨ cópia_{<j}(C) ∨ ⋁_{pares} (copia_{<j}(c₁) ∧ copia_{<j}(c₂))`.

> **Teorema (semântica).** `REF_t(γ)` SAT ⟺ ∃ refutação ≤ t linhas.
> *(a "exatamente-um" é o que distingue LINHAS de profundidade — a v1
> contava profundidade e passava p/ SAT cedo demais.)*

**Fronteira validada:** `γ={[1],[−1]}`: `REF_1`=UNSAT, `REF_2`=SAT (min=3);
ABC: `REF_5`=UNSAT, `REF_6`=SAT sob o encoder particionado — **corrigido
para min=5** com pares completos (sobreposição).

### 4.2 Pares completos (o6º bug)

Par `(c₁,c₂)` para alvo `C`: `l ∈ c₁`, `¬l ∈ c₂`, `(c₁∖{l}) ∪ (c₂∖{¬l}) = C`
com condições de sonsidade (`l,¬l ∉ s₁` e `∉ s₂` sobre `s₁,s₂ ⊆ C`).
A v1 exigia **partição** (`s₂ = C∖s₁`) e perdia `(a∨b),(b∨¬a) → (b)`
(sobreposição com `{b}` em ambos) → minrefs inflados (`>64` onde o real
era13). Correção: enumeração exaustiva sobre o fecho.

### 4.3 Resultados do teste LP (seed20261119, n=5, m∈[25,45])

- **T1:** `8/100` alternam = **exatamente os γ-SAT**; **0/92 γ-insat** em
  t=6 **e** t=2 → candidato `(γ, REF_t)` **só alterna pelo lado trivial**;
  `t` precisa ≥ `ref-length(γ)` (ilimitado) → **retraído como construção
  p-tempo**;
- **T2:** `0/100` mistas (48.945 adições) — coerente: γ pequenos têm prova
  pura curta; os difíceis são governados pelo **Teorema Nec**;
- **T3:** `0/100` (calibrado).

### 4.4 Teorema Nec (P) — por que a via LP morre

> Família alternante + π polinomial + lado insat **difícil para Res(k)**
> ⟹ **π necessariamente impura**.
> *Prova:* por linha-pureza + acessibilidade (C2.2′), a parte acessível de
> π é refutação `Res(k)` de `Λ_{i*}` com ≤ |π| linhas; alternância ⟹
> `i*=1` ⟹ refutação polinomial do lado difícil — contradição. ∎

→ **critério-LP = MISTO → RETRAÇÃO da via LP para a rota negativa**
(escopo: incondicional para o candidato testado; condicional via Nec para
famílias com lados difíceis).

## 5. Validação e limitações

- Encoder validado na fronteira exata +6 bugs corrigidos e documentados
  (off-by-one, filtro de tautologia, AND-vs-OR, sonsidade,
  profundidade-vs-linhas, sobreposição); **impacto no LP:92/92 sustentado**
  (`gk_minref_referee.md` §A3);
- **Limitações:** n≤6 · t poli (orçamento) · random3SAT de n=5 fora
  (fecho~211) · γ aleatórios não uniformes (gerador declarado).

## 6. Referências

- **Origem:** IA-research-Godel-e-Krajicek —
  `krajicek_ddp/C2_LP_familia_alternante.md` (T1/T2/T3 + Nec + referee),
  `krajicek_ddp/C2_r2_G1_contraexemplo.md` (C2.2′), `gk_minref_referee.md`.
- Garlík, M. CCC 2024 (Thm 1/18 — famílias difíceis; DOI
  10.4230/LIPIcs.CCC.2024.33).
- Krajíček, J. *Proof Complexity*, CUP 2019, cap. 5.7.

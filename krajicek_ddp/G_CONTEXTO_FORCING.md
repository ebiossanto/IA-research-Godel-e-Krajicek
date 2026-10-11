# Contexto de ataque — as condições do forcing de [Kra95, Thm 9.4.2]

**Missão da rodada:** determinar se as condições do forcing de [Kra95, Thm 9.4.2] são
"medida a medida" e aceitam **semente de elementos novos de medida velha**; se sim,
(F-b') é construível e o Teorema 4 fica corrigido com hipótese finita.

## 1. Evidências coletadas (rodada de 11 Out 2026)

### 1.1 A lacuna persiste na versão PUBLICADA (confirmado)

Existe **arXiv:2506.20221v5 (05 Mai 2026)** = versão publicada em **LMCS 22(2:14)2026**
(aceito 17 Mar 2026). Releitura integral do v5: o passo frágil está lá **literalmente**:

> "But by (7) i_o is also already in M∗ and hence by (8) we get: M′ ⊨ (¬α_{i_0}) ∈ SAT."

(Numeracão no v5: Teorema 2 = antigo Teorema 3; Teorema 3 = antigo Teorema 4;
Problema 2.1 inalterado; (7) e (8) inalterados; `Log(M) = {|m| | m ∈ M}` inalterado.)
⇒ A lacuna detectada em v4 **não foi corrigida** em v5/LMCS.

### 1.2 O que é a seção 9.4 do livro [Kra95] (cadeia de evidências)

- O prefácio do livro (kniha-obsah.html) aponta o framework de **valorações booleanas**
  nas "sections 3.1, **9.4**, 12.7 and 13.3".
- Krajíček, **"Extensions of models of PV"** (Logic Colloquium'95, LNL 11, 1998, pp.104–114),
  Seção 4 ("A Boolean-valued extension"), diz literalmente:
  > "Boolean-valued extensions of S^1_2 were defined in [5], see also **[4, Chpt. 9.4]**"
  onde [4] = livro Kra95. E: "The following is a special case of [5, Thm 5.1]. See also
  [7] or [5, Sec. 9.4] for another treatment of the construction."
  ([5] = "On Frege and Extended Frege Proof Systems" (1995); [7] = Krajíček–Pudlák 1990.)
- ⇒ **§9.4 de [Kra95] = extensões booleano-valoradas de modelos**, e o "forcing
  construction underlying [Kra95, Thm.9.4.2]" citado pelo artigo-alvo é **essa construção**.
  O "additional requirement on M" do artigo-alvo é a hipótese extra do Teorema 9.4.2
  (a localizar — provavelmente ligada a "SAT_n(M) não reconhecível por circuito" / enumerabilidade).

### 1.3 A construção (verbatim essencial de [Kra98], Seção 4 — texto extraído em `fontes/`)

Seja `M ⊨ PV`, `p = (p_1,…,p_n) ∈ M` uma sequência de átomos proposicionais:
- `Circuit_M(p)`: circuitos com uma saída formados a partir dos átomos `p_i` (elementos de `M`);
- `B(p)` = álgebra de Booleanos obtida de `Circuit_M(p)` por `C₁ ~ C₂` sse existe
  **prova EF em M** de `C₁ ↔ C₂`;
- `G` = ultrafiltro em `B(p)` **fechado sob EF-provability in M**;
- `ν_G(C)` = 1 sse `[C] ∈ G`;
- `Names_M(p)` = sequências `⟨C₁,…,C_ℓ⟩ ∈ M` de circuitos (**os nomes são elementos de M**);
- elementos de `M[G]`: tuplas `⟨ν_G(C₁),…,ν_G(C_ℓ)⟩` — um para cada nome em `M`;
- `f(w₁,…,w_k)` calculado "bit a bit" via circuitos `D_{f,ℓ}` de `M`.

**Teorema 4.1** ([Kra98]): se `G` é fechado sob EF-provability, `M[G]` é extensão **cofinal**
de `M` e **modelo de PV**. E se `ν_G(C)=1` para todo `C` que em `M` computa constantemente 1,
então `M[G]` é extensão **`Σ^b_1`-elementar** e cofinal.

**Semente (Claim 1–2 de [Kra98]):** dado um conjunto `T` de condições proposicionais
**sem refutação EF em M**, existe ultrafiltro `G` estendendo o filtro gerado por `T`
(com as condições de fechamento). O artigo de 1998 usa isso para forçar
`¬(⟨W⟩ |= p) ∧ φ'(p,⟨Z⟩)` — i.e., **a semente é exatamente o mecanismo do forcing**.

### 1.4 O final de [Kra16] (o que o artigo-alvo aponta como direção)

Trecho extraído (`fontes/kra16_boolean_excerpt.txt`), literal:

> "In light of Claim 4 it seems natural to try to extend model M′ by adding a satisfying
> assignment for ⋀_i ψ(A,y_i). The existence of a satisfying assignment … would follow if
> M′ would satisfy a collection scheme for Σ^b_1 formulas on A_W. But that is unlikely as
> the argument of Cook and Thapen [7] implies that the true ∀Π^b_1 theory does not prove
> the scheme (unless factoring is not hard), and the same argument implies that **one
> cannot argue just using the ∀Π^b_1 theory of M′ that it has an extension where the
> collection holds (we would also need that it adds no new elements into [n])**."
>
> "The use of the property that **we add no new elements into [n]** in Claims 1–3 was solely
> to preserve the first order theory of A_W … There is an alternative for arranging that.
> **In the forcing from [17,15] one naturally adds many new elements into [n]** (and, in
> fact, does not include all of [n] from M into M′) but the first order theory of A_W is
> nevertheless often preserved."

Leitura: **"no new elements into [n]" é literalmente o nosso (F-b')** (com `[n] = m`),
"adding a satisfying assignment for ⋀_i" é o nosso **(F-sent)**, e Krajíček já distingue as
duas rotas: (b') é limpo mas as construções de forcing **"naturalmente adicionam muitos
elementos novos em [n]"**; a alternativa é preservar a teoria de primeira ordem de `A_W`.

## 2. Análise própria da organização (a verificar/provar pelas frentes) — **(P)**

**(L1) Lema de Log (a provar).** `Log(M[G]) = Log(M)` deve ser **imediato** da construção:
todo elemento de `M[G]` é indexado por um nome `⟨C₁,…,C_ℓ⟩ ∈ M`, e `|w|` é calculado (via PV)
a partir do nome — logo `|w| ∈ Log(M)`. Se `L1` for provado, ele **é** o conteúdo de
[Kra95, Thm 9.4.2] sobre `Log` — confirmando que a construção é **"medida a medida"** no
sentido de que **todas as medidas vêm de `M`** (nomes ∈ `M`).

**(L2) Semente de medida velha (a provar).** Um falsificador `σ` de `φ(r)` é uma tupla
`⟨ν_G(C_i)⟩` indexada por um nome ∈ `M` — portanto **elemento novo de medida velha**.
A condição de existência: `T ∪ {condições que fazem σ falsificar φ}` sem refutação EF em `M`.
Conjectura: isso segue do item (1) do Teorema 2 do artigo ("φ não tem prova em M em nenhum
pps") — uma refutação EF das condições de falsificação daria prova EF de φ em M.
**Atenção:** precisamos `M[G] ⊨ T_PV` (ou ao menos `Ref_P` com **todos** os parâmetros,
inclusive `σ ∈ M[G]`), mas o Teorema 4.1 de [Kra98] só garante **modelo de PV** —
`Ref_P ∈ T_PV` não é necessariamente consequence de PV. Este é um ponto crítico a resolver
(ver (C3) abaixo).

**(L3) Elementos novos abaixo de m (o ponto duro de (F-b')).** Pela construção, um elemento
`w = ⟨ν_G(C₁),…,ν_G(C_ℓ)⟩` representa um número `≤ 2^ℓ`. Para `w < m` basta `ℓ < |m|`
(nome curto) — e nomes curtos existem em `M`. Logo **`M[G]` contém tipicamente elementos
novos abaixo de `m`** (medida velha, valor novo) — `M[G] ∩ m = M ∩ m` **falha em geral**.
Hipóteses de reparo a examinar:
- **(R1)** Fixar (via `T`) todas as tuplas de nomes com `ℓ < |m|` aos valores em `M`
  (pinning) — mas "o valor em M" de um nome não é intrínseco (os átomos `p_i` são genéricos);
  e `σ` usa átomos `p` — consistência do pinning com a semente de `σ` a verificar;
- **(R2)** Escolher os átomos `p` e a medida `n` de modo que toda tupla genérica tenha
  valor `≥ m` (impossível para nomes curtos — refutado?);
- **(R3)** aceitar `(F-sent)` puro e verificar **(8) em `M[G]`**: para `i ∈ M ∩ m` as
  testemunhas de `M` sobem (`Σ^b_1`); para `i` novo em `[m]`, `(α)_i` é novo e **não há
  garantia de falsificador** — é aqui que `∀i∃y → ∃z∀i` (BB) ressuscita;
- **(R4)** rota alternativa de [Kra16]: **preservar a teoria de primeira ordem** de `A_W`
  em vez de "sem novos elementos em [n]" (o que exige saturação `ℵ_1` + contagem aproximada).

**(C3) O problema `T_PV` vs `PV`.** O Teorema 4 exige `M′ ⊨ T_PV` (todas as universais
verdadeiras, com quaisquer parâmetros — em particular `Ref_P` com parâmetros novos como `σ`).
O forcing booleano dá `M[G] ⊨ PV` (+ `Σ^b_1`-elementaridade sobre `M`). Averiguar:
(a) `M[G] ⊨ T_PV`? (b) `PV ⊢ Ref_P` para `P` forte? (c) ou basta `Ref_P` com os parâmetros
usados, obtido por transferência? Se (a)/(b) falharem, (F-sent) via forcing booleano precisa
de um aditivo.

## 3. Fontes baixadas (pasta `fontes/`)

- `krajicek_extensions_PV_1998.pdf` + extração integral (Seção 4 = construção booleana;
  Teorema 4.1; Claims 1–2 de semente; §3 = argumento de compactness com `N*` = subestrutura
  gerada — atenção ao **paralelo exato** com o que queremos para `M*`!)
- `krajicek_pseudofinite_2016.pdf` + `kra16_boolean_excerpt.txt` (fim do artigo = direção
  endossada pelo artigo-alvo; frases "no new elements into [n]").
- `krajicek_nw_2011.pdf` + `nw2011_full.txt` (não contém "no new elements"; a frase de
  [Kra16] refere-se aos Claims do próprio [Kra16]/[14]).
- Sumário do livro: `https://www.karlin.mff.cuni.cz/~krajicek/kniha-obsah.html`.
- **Não obtido:** o texto de [Kra95] §9.4/Thm 9.4.2 (livro em archive.org, acesso
  restrito). `https://archive.org/details/boundedarithmeti0000kraj` — se um agente
  conseguir material sobre §9.4 (errata, citações, Google Books), é ouro.

## 4. Pergunta central a responder (o brief original)

> "se elas são 'medida a medida' e aceitam semente de elementos novos de medida velha,
> (F-b') é construível e o Teorema 4 fica corrigido com hipótese finita."

Resposta preliminar (a provar/refutar): **medida a medida = SIM (L1); semente = SIM (L2);
mas (F-b') não segue só disso (L3)** — porque o forcing booleano adiciona elementos novos
abaixo de `m` via nomes curtos. A questão decisiva é (R1)/(R3)/(R4): ou fixar os nomes
curtos, ou provar (8) diretamente em `M[G]` para índices novos, ou usar a rota de
preservação de teoria de primeira ordem.

## 5. Regras

Português; marcar **(A)** artigo/fonte, **(P)** demonstração própria, **(C)** conjectura;
entregável apenas no arquivo indicado; resumo final ≤ 600 palavras.

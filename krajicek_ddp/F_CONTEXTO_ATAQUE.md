# Contexto de ataque — versão finita/combinatória do Problema 2.1

**Missão da rodada:** atacar a versão finita do Problema 2.1 (Equipe E, estratégia 3(c)/S2+S3):
relaxar `Log(M*) = Log(M')` para uma exigência finita sobre a lista de parâmetros envolvidos.

## 1. Texto verbatim do artigo (arXiv:2506.20221v4, §3, item (5) da prova do Teorema 4)

Transcrição literal (extraída do HTML do arXiv em 10 Out 2026):

> "Now we conclude the proof by using the assumption that Problem 2.1 has the affirmative
> solution. This gives us M ⊆ M* ⊆ M′ such that
>
> Log(M*) = Log(M′), (7)
>
> and M′ ⊨ T_PV ∧ ¬φ ∈ SAT. Note that M* satisfies the last axiom of S:
>
> M* ⊨ ∀i<m (¬α_i) ∈ SAT (8)
>
> as it preserves the Σ^b_1(PV)-properties from M.
>
> Let σ ∈ M′ be an assignment to the atoms r that falsifies the formula φ in M′.
> Hence σ = (σ_i)_{i<m} and we have M′ ⊨ σ_{i_0}:P ⊢ α_{i_0} for some i_0 < m.
> **But by (7) i_o is also already in M∗** and hence by (8) we get:
>
> M′ ⊨ (¬α_{i_0}) ∈ SAT.
>
> That contradicts Ref_P which holds in M′ as it models T_PV."

E a definição de Log (§2 do artigo, verbatim):

> "where Log(M) = {|m| | m ∈ M}" — ou seja, **Log(M) é o conjunto dos comprimentos (medidas)
> padrono dos elementos de M**, não um conjunto de elementos.

## 2. O ponto crítico identificado (Equipe E §1.5, a confirmar nesta rodada)

A afirmação "**by (7) i_o is also already in M***" deduz a pertinência `i_0 ∈ M*` a partir de
`Log(M*) = Log(M')`. Análise preliminar:

- `i_0 < m` com `m ∈ M ⊆ M*`, e `i_0 ∈ M'` (pois `σ ∈ M'` e a decodificação `(σ)_{i_0}` é PV).
- `Log(M*) = Log(M')` diz que os dois modelos têm **os mesmos comprimentos padrono** — mas
  **não** impede que `M'` tenha **elementos novos abaixo de `m`** com comprimentos antigos.
  (Um elemento novo `j ∈ M'\M*` com `j < m` tem `|j| ≤ |m|`, comprimento já presente em
  `Log(M) = Log(M*) = Log(M')` — logo a igualdade de Log é satisfeita com folga.)
- Consequência provisória: **(7) sozinha não parece dar `i_0 ∈ M*`** — ou há um argumento
  comprimido no artigo (leitura (L1)/(L2)/(L3) da Equipe E §1.5), ou há uma lacuna em v4.

**Três leituras a examinar (Equipe E §1.5):**
- (L1) `Log` no artigo é mais forte que "conjunto de medidas" (ex.: medidas com partes
  canônicas/`Σ^b_1`-definíveis), e aí o passo fecha;
- (L2) `i_0` é `p`-tempo definível a partir de parâmetros já em `M*` — mas atenção: `σ`
  (que define `i_0`) está em `M'`, e se `σ ∈ M*` a prova colapsaria (ver §4 abaixo);
- (L3) há um argumento comprimido não reproduzido no contexto.

## 3. O que o passo (5) realmente consome (Equipe E §1.4, tabela E1–E5)

| # | Exigência | Como obtê-la |
|---|-----------|--------------|
| E1 | `M* ⊨ T_PV` | **Grátis**: `T_PV` é a teoria universal verdadeira em `L_PV`; subestrutura de modelo de teoria universal é modelo; `M* ⊆ M' ⊨ T_PV` ⟹ `M* ⊨ T_PV`, em particular `M* ⊨ Ref_P` |
| E2 | `M* ⊨ ∀i<m (¬α_i) ∈ SAT` (ao menos em `i_0`) | **a preservação fraca Σ^b_1** |
| E3 | `σ_{i_0}:P ⊢ α_{i_0}` em `M'` (só precisa valer em `M'`) | já vem do falsificador de `φ` |
| E4 | `i_0 ∈ M*` | **o passo frágil** ("by (7)") |
| E5 | `Log(M*) = Log(M')` | forcing ([7], Thm 9.4.2) |

Fato: `Σ^b_1` (`∃`-matriz aberta) transfere **para cima** (`M ⊆ M'`); sentenças universais
`Π` transfere **para baixo** (`M* ⊆ M'`). `Ref_P` (`x:P⊢y → (¬y)∉SAT`) é universal verdadeira,
logo vale em `M'` com **todos** os parâmetros de `M'` — logo a contradição final precisa de:
(1) `M' ⊨ σ_{i_0}:P⊢α_{i_0}` (vem do falsificador) e (2) `M' ⊨ (¬α_{i_0}) ∈ SAT` (precisa de E2+E4).

## 4. Análise própria da organização (a verificar pelas equipes) — ideias centrais do ataque

**(A) Duas formulações finitas candidatas.** Toda a máquina `M*` + preservação `Σ^b_1` +
`Log` existe para transportar a sentença (8) de `M` (onde ela é axioma de `S`) até `M'` no
índice `i_0`. Se conseguirmos uma das condições finitas abaixo, `M*` e `Log` tornam-se
desnecessários:

- **(F-b') — versão membership (Equipe E, variante (b')):** exigir `M' ∩ m = M ∩ m`
  ("nenhum elemento novo abaixo de `m`"). Então `i_0 < m, i_0 ∈ M'` ⟹ `i_0 ∈ M ⊆ M*`;
  `M ⊨ (8)` instancia em `i_0`: `M ⊨ (¬α_{i_0}) ∈ SAT`; `Σ^b_1` sobe `M ⊆ M'`:
  `M' ⊨ (¬α_{i_0}) ∈ SAT`; `Ref_P` em `M'` dá a contradição. **(F-b') ⟹ (F-sent).**
- **(F-sent) — versão sentença (o alvo minimalista):** exigir diretamente
  `M' ⊨ T_PV + (¬φ) ∈ SAT + ∀i<m (¬α_i) ∈ SAT`. A contradição fecha com `i_0 ∈ M'` qualquer
  (sem pertinência a `M*`): `M' ⊨ (8)` instancia em `i_0` e `Ref_P` em `M'` fecha.
  Note que **ambas as exigências extras de `M'` são sentenças com parâmetros em `M`**
  (`¬φ ∈ SAT` é `Σ^b_1`; (8) é `Π^b_2`).

**(B) Observação importante (a verificar).** A forma "colecionada" de (8) é
`∃z ∀i<m F(i, (z)_i)` (`z` codificando a lista de atribuições falsificantes) — essa é
**`Σ^b_1`** (∃z + matriz decidível + `∀i<m` sharply bounded), e portanto **sobe** de `M` para
`M'` automaticamente **se valer em `M`**. Mas `M ⊨ (8) ⟹ M ⊨ ∃z∀i<m F(...)` é exatamente
o esquema **BB** — não disponível. Contudo, para a versão finita basta que a extensão
**contenha** tal `z` (ou tais testemunhas), o que é um requisito de construção, não de teoria.
Isto é o "missing reflection" em forma pura:BB escondido na genericidade do forcing.

**(C) Colapso a evitar (importante).** Se `σ` (falsificador de `φ` em `M'`) pertencesse a
`M*`, então `i_0` = índice-p-tempo-decodificável-de-σ entraria em `M*` por fechamento PV, e
com `α_{i_0} ∈ M*` teríamos dentro de `M*`: `(8)` dá `(¬α_{i_0}) ∈ SAT`, enquanto
`σ_{i_0}:P⊢α_{i_0}`... a contradição apareceria já em `M*`, mostrando que **`σ ∉ M*` é
obrigatório**. Logo toda formulação finita deve exigir membership de `i_0` (ou (8) em `M'`)
**sem** exigir que o falsificador inteiro caiba no submodelo. Qualquer "correção" que exija
`σ ∈ M*` é **refutada por esse colapso**.

**(D) Ideia de construção (a explorar).** Em vez de estender `M` e depois preservar,
**construir** `M'` "medida a medida" (à la [7], Thm 9.4.2, forcing) semeando explicitamente:
(a) um falsificador `σ` de `φ` (comprimento `≤ |φ|^c` — medida **antiga**, logo compatível
com `Log` igual); (b) as testemunhas de (8) para os índices `i < m` que aparecerem. A
dificuldade é que `m` é não-padrão e o forcing decide "medida a medida" — cobrir `∀i<m` é
infinito do ponto de vista das condições. Duas saídas: (F-b') evita novos `i` (nenhum `i`
novo a cobrir); (F-sent) exige cobrir todos, incluindo novos.

## 5. Referências locais e externas

- [7] Krajíček 1995, *Bounded arithmetic, propositional logic, and complexity theory*,
  Thm 9.4.2 (forcing com `Log(M') = Log(M)`).
- [9] Krajíček 2016, *Expansions of pseudofinite structures and circuit and proof complexity*.
- [10] Krajíček 2019, *Proof Complexity*, Cap. 20.
- [14] Krajíček–Pudlák 1990 (Teorema 3 do artigo).
- [6] Cook–Thapen 2006 (BB e fatoração).
- Trabalho local: `krajicek_ddp/A_teoremas_exatos.md` (equipe A), `E_ataque_problema21.md`
  (equipe E, §1.5 e §3c), `D_geradores_consequencias.md`.

## 6. Regras (iguais às anteriores)

Português; separar **(A)** artigo, **(P)** demonstração própria, **(C)** conjectura;
entregável apenas no arquivo indicado; resumo final ≤ 600 palavras.

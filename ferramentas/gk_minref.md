# gk_minref — Comprimento mínimo exato de refutação (Resolução)

**Origem:** extensão do repositório
[IA-research-Godel-e-Krajicek](https://github.com/ebiossanto/IA-research-Godel-e-Krajicek)
(MIT) — núcleo teórico das frentes **C2/LP** (encoder `REF_t` de
`gk_alternating_family.py`) e do catálogo de gadgets de complexidade de
provâs do projeto.
**Código:** `gk_minref.py` (raiz) · **Teste:** `python gk_minref.py demo` ·
**Dados:** `gk_minref_results.{csv,json}` · **Auditoria:**
[`gk_minref_referee.md`](../gk_minref_referee.md) (r1 RECOMENDADO)

## Como citar

> Soares dos Santos, E. (2026). *gk_minref — exact minimum refutation
> length* [Software]. Em: IA-research-Godel-e-Krajicek.
> <https://github.com/ebiossanto/IA-research-Godel-e-Krajicek>. Licença MIT.
> (ou use o `CITATION.cff` da raiz)

---

## 1. O que é

Ferramenta que calcula o **comprimento mínimo exato** de uma refutação por
**resolução** de uma CNF γ (ou decide "γ satisfatível → sem refutação"),
via codificação SAT `REF_t(γ)` + busca em *t*. Escopo declarado:
**n ≤ 6 variáveis efetivas** (pool = 3ⁿ), **resolução** (não DRAT/EF),
sem claims de lower bound geral.

## 2. Para que serve (aplicações)

1. **Medir complexidade de prova finita**: comprimento mínimo de refutação
   é o objeto central da complexidade de provas — a ferramenta dá o valor
   *exato* para instâncias pequenas (referência para calibrar outras
   medições, ex.: D4′ com provas mínimas em vez de provas de solver);
2. **Validar encoders REF_t**: regressão de fronteira (unidades=3, ABC=5);
3. **Bug-hunting**: foi ela que revelou o *6º bug do projeto* (pares
   particionados perdiam passos com sobreposição) e verificou
   **exaustivamente (92/92)** que os resultados do teste LP não foram
   distorcidos;
4. **Calibrar a família alternante** (C2.3): decidir se `REF_t` alterna.

## 3. Como usar

```bash
python gk_minref.py demo                 # suite de validação (deve dizer VALIDACAO OK)
python gk_minref.py dimacs inst.cnf      # instância DIMACS (n ≤ 6)
python gk_minref.py --benchmark --seed 20261119   # → gk_minref_results.{csv,json}
```

**Saída (exemplo do benchmark):** `random2sat_n5_m12 ... minref=9 fecho=51`;
`cadeia_k5 ... minref=11` — distribuição `{7:6, 9:4, 11:1, 5:2}` (17/17
exatos, todos <2 s).

## 4. Arcabouço matemático

### 4.1 Definições

- **Refutação Res(γ)**: sequência `π = (C₁,…,C_t)` onde cada `C_i ∈ γ`
  (folha) ou deriva de `C_a, C_b` (a,b < i) por **resolução**:
  `C_a = S₁∪{l}`, `C_b = S₂∪{¬l}`, resolvente `(S₁∪S₂)`; e `C_t = ∅`.
  **Comprimento mínimo** `minref(γ) := min t` sobre tais sequências
  (∞ se γ satisfatível).
- **Fecho de resolução** `Cl(γ)`: menor conjunto fechado sob resolução
  contendo γ (sem tautologias — tautologia nunca é necessária numa
  refutação). **Propriedade (A)** (completude da resolução):
  `γ ∈ UNSAT ⟺ ∅ ∈ Cl(γ)`; toda refutação usa só cláusulas de `Cl(γ)`
  (WLOG) → pool = fecho (|Cl| ≤ 3ⁿ).

### 4.2 Codificação `REF_t` (semântica de LINHAS)

Variáveis `y_{j,C}` = *"a linha j da sequência é a cláusula C"*, para
`C ∈ Cl(γ)`, `j ∈ {1,…,t}`. Restrições:

1. **Raiz:** `y_{t,∅}`.
2. **Exatamente-um por posição:**
   - (2a) `⋁_C y_{j,C}` (ao menos uma);
   - (2b) **AMO sequencial** com auxiliares `r_{j,i}` (O(|Cl|)):
     `(¬y_{j,C₁} ∨ r_{j,1})`, `(¬y_{j,C_i} ∨ r_{j,i})`, `(¬r_{j,i-1} ∨ r_{j,i})`,
     `(¬y_{j,C_i} ∨ ¬r_{j,i-1})` — codificação "r_{j,i} ⇔ ∃k≤i: y_{j,C_k}".
3. **Justificativa** para `C ∉ γ`:
   `y_{j,C} → [C ∈ γ] ∨ ⋁_{j'<j} y_{j',C}` (cópia)
   `∨ ⋁_{(c₁,c₂) ∈ P(C)} ( ⋁_{j'<j} y_{j',c₁} ∧ ⋁_{j'<j} y_{j',c₂} )`
   (corte; implementado com auxiliar `a_{j,C,p}` por par).

**Pares completos** `P(C)`: todo `(c₁,c₂)` com literal `l ∈ c₁`, `¬l ∈ c₂`
e `(c₁∖{l}) ∪ (c₂∖{¬l}) = C`, sujeito às condições de **sonsidade**
`l, ¬l ∉ s₁` e `l, ¬l ∉ s₂` (os "subconjuntos" `s₁,s₂ ⊆ C`). A versão
anterior exigia `s₁ ⊊ s₂` **partição** — **perdia passos com sobreposição**
(ex.: `(a∨b),(b∨¬a) → (b)` com `{b}` em ambos os lados) — **6º bug do
projeto**, corrigido por enumeração exaustiva sobre o fecho.

> **Teorema (semântica).** `REF_t(γ)` é satisfatível ⟺ existe refutação
> Res(γ) com **≤ t linhas**.
> *Prova (→):* a atribuição dá, por posição, exatamente uma cláusula; as
> restrições (3) fornecem folha/cópia/corte com premissas em posições
> anteriores → sequência válida. *(←):* dada a sequência, atribua
> `y_{j,C_j} = ⊤` e escolha auxiliares conforme a justificativa de cada
> linha; sem repetição WLOG (repetir uma linha só desperdiça posições). ∎

### 4.3 Busca e complexidade

- Pré-condição: `solve(γ)`; se SAT → `None`.
- **Busca exponencial** `t = 1,2,4,…` até `REF_t` satisfatível + **binária**
  em `(t_lo UNSAT, t_hi SAT]` → `t*` exato em `O(log t*)` solves.
- **Orçamento:** auxiliares ≈ `t · |P|` onde `|P| = Σ_{C∉γ} |P(C)|`;
  `t_cap = MAX_AUX/|P|` com `MAX_AUX = 400·10³` (cláusulas ~2×) — evita
  estouro (a causa do timeout da v1 do benchmark).
- Custo do fecho: saturação `O(|Cl|²·n)` por varredura; pares
  `O(|Cl|²·n)` — para n=5 típico: |Cl|≈50–211, pares≈19·10³ (medido).

### 4.4 Cálculos trabalhados (validação)

| Instância | minref | Derivação |
|---|---|---|
| `γ = {[1],[−1]}` | **3** | folhas `1`,`−1` +1 corte (não pode ser2: `∅` exige duas premissas) |
| `γ = {[1,2],[1,−2],[−1]}` (ABC) | **5** | `L₁=[1,−2]`, `L₂=[1,2]`, `L₃=[−1]`, `L₄ = res(L₁,L₂ | x₂) = [1]` (sobreposição!), `L₅ = res(L₄,L₃) = ∅` — a v1 particionada dizia6 |
| `γ = {[1,2]}` (SAT) | `None` | `∅ ∉ fecho` |
| cadeia_k∈{3,4,5} | 7, 9, 11 | padrão `2k+1` (propagação unitária + cortes) |
| `random2sat_n5_m12` | 9 (fecho51) | a v1 dizia `>64` (bug de sobreposição) |

**Verificação exaustiva de impacto (92/92):** todas as γ-insat da rodada T1
de `gk_alternating_family` têm `minref > 6` no encoder completo → os
números do teste LP se sustentam (detalhes: `gk_minref_referee.md` §A3).

### 4.7 `minref_deep` — extensão para n>6 (fronteira do τ k↑)

O `minref` original enumera **todos** os pares do fecho no `REF_t` — para
n≥7 o fecho de Tseitin fica denso (n=7: 2059 cláusulas,766k pares
deduplicados) e `t × pares` estoura o orçamento. `minref_deep(gamma,
max_aux=…, with_info=True)` usa duas observações:

- **(L) Limite inferior:** `d(C)` = profundidade **mínima de árvore**
  (`d=1` em γ; senão `min_pares max(d(c₁),d(c₂))+1`, fixpoint). Toda
  linha `j` de uma refutação com `≤ t` linhas tem `d ≤ j` (indução:
  folha d=1; resolvente de linhas <j tem d≤max+1≤j) → **`d(∅) ≤ t`** —
  a busca começa em `t = LB = d(∅)`, não em1.
- **(S) Pool sonoro:** `pool_t = {C : d(C) ≤ t}` com pares restritos
  (ambos os pais **e** alvo no pool) é **suficiente e necessário** para
  `REF_t` (argumento acima) — ordens de grandeza menos auxiliares.
- **Dedup de pares** (`closure_pairs(both_orders=False)`): o auxiliar
  `a_{j,C,p}` é **simétrico** nos pais → metade dos auxiliares. O
  caminho original (`minref`) mantém o default `True` — byte-idêntico.

**Fronteira empírica** (sondas, doc `34_TAU_KUP_MINREF.md` §1.1):

| níveis | nvars | exatidão com `minref_deep` |
|---|---|---|
| k=2 | 5 | sempre exato |
| k=3 | 7 | exato até **minref=7** (max_aux=6M; REF_7 provado:173s) |
| k=4 | 9 | exato até **minref=5** (max_aux=8M; REF_5 provado) |
| k≥5 | ≥11 | parede do fecho (não testado — projetado inviável) |

**Propriedade (no `demo`):** em n≤6, onde o `minref` original é exato,
`minref_deep` devolve o **mesmo valor** — `17/17 consistentes` (deep
censurado onde o original é exato = falha; deep exato onde o original
censurou = aceito — é o motivo da extensão). Retorno idêntico a
`minref(…, with_sat_len=True)` + `info` opcional (`lb`, `t_testados`,
`pares_testados`, `fecho`, `iter_dp`).

### 4.8 `saturation` por buckets (patch de desempenho, 23/11/2026)

O fecho original re-sortava `sorted(derived)` para **cada** c1 do duplo
laço → O(N²·N log N) por passada — gargalo de horas em fechos n=9 com
~19k cláusulas (medido: instância τ k=4 s=1539, fecho **19171**, 3h50min
em 100% CPU antes do patch; versão nova: **25min**). A implementação
atual varre pares (c1 ⊃ l, c2 ⊃ -l) **por literal l>0** (buckets).

**Por que os dados não mudam:** o fecho é ponto fixo de operador
monotono (conteúdo único) e o resolvente é comutativo → mesmos
resolventes; `order` final é sort determinístico sobre o mesmo conteúdo
→ **lista idêntica**. A versão original ficou como `saturation_ref`
(apenas o teste de equivalência do `demo` usa). *Validação (3 camadas,
doc `34_TAU_KUP_MINREF.md` §2.1):* equivalência direta **28/28** ·
`demo` **17/17** · **9/9 `fecho`** + 1 `minref_deep` completo
reproduzidos do CSV gravado do τ k↑.

## 5. Validação e limitações

- **Validação:** `demo` (fronteiras conhecidas + regressão + equivalência
  AMO seq≡pairwise) — deve retornar `VALIDACAO OK`;
- **Limitações (declaradas):** n≤6 · resolução (não DRAT/EF) ·
  `MAX_AUX` (censura `>` declarada) · benchmark só de fechos pequenos
  (`random3sat` n=5 produz fecho ~211 — estoura orçamento) · sem
  lower bound geral.

## 6. Referências

- **Origem:** repositório IA-research-Godel-e-Krajicek (fre­ntes C2/LP;
  docs `krajicek_ddp/C2_LP_familia_alternante.md`, `gk_minref_referee.md`).
- Krajíček, J. *Proof Complexity*, CUP 2019, **cap. 5.7** (fragmentos R(f)
  de resolução-DNF) — DOI 10.1017/9781108242066.
- Krajíček, J. *On the weak pigeonhole principle*, Fund. Math. **170**
  (2001), Def. 1.1 (sistema R(f)).
- Garlík, M. *Failure of Feasible Disjunction Property for k-DNF
  Resolution…*, CCC 2024, §2 (regras de `Res(k)`; DOI
  10.4230/LIPIcs.CCC.2024.33).
- Completude da resolução: estándar (Chang–Lee / Davis–Putnam).

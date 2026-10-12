# Referee Q2 — `Q2_instancias_tau_n_q.md` (v3 — rodada 3)

# RECOMENDADO

> FATAL-1/r2 **corrigido corretamente**; 7/7 MINOR da rodada 2 **respondidos**;
> caça a fatais novos: **nenhum**. Restam 3 menores cosméticos/de precisão
> (MINOR-1..3/r3), nenhum bloqueante. As três rodadas fecham o ciclo pedido em
> rodada 2 ("one-line patch + menores → RECOMENDADO").

## (a) Auditoria do FATAL-1/r2 (§4 + §0.3) — CORRIGIDO ✓

- **Hipótese primária do corolário é agora `τ_n(φ_n) ∈ TAUT`** ✓ — exatamente a
  formulação suficiente/correta que eu apontei como salvadora.
- **Decomposição verificada nas DUAS direções**: `τ_n(φ_n) ∈ TAUT ⟺ ⌢φ_n⌝ ≤ n ∧
  ∃w(|w| ≤ n^{c₀} ∧ θ(w))`. ⇐: cutoff satisfeito + correção limitada (θ(w) verdadeira
  ⟹ θ^τ(w) tautologia) ⟹ disjunção tautologia ✓. ⇒: `τ_n(φ_n) ≠ ⊥` força
  `⌢φ_n⌝ ≤ n` e Σ₁; alguma disjuncto tautológico + direção semântica da correção
  ⟹ testemunha curta ✓. **Correto.**
- **TRÊS modalidades de não-contente declaradas** (§4 e §0.3): (1) cutoff de Gödel
  (`⌢φ_n⌝ > n` ⟹ ⊥); (2) testemunha longa (disjunctos não-tautológicos ⟹ vacuidade);
  (3) bound trivial `m ≥ |τ_n(φ_n)| = 2^{p(n)}` ✓. A terceira modalidade — a que faltava
  — está explícita e rastreada ao FATAL-1/r2 no checklist §8. ✓

## (b) Auditoria dos MINOR-1..7 da rodada 2 — TODOS RESPONDIDOS ✓

1. **MINOR-1 ✓**: §3.1 acrescentou `τ_n(φ) := ⊥` para φ não-Σ₁ com `⌢φ⌝ ≤ n` —
   totalidade plena de `27 §1.1`.
2. **MINOR-2 ✓**: §2 trocou "ou equivalente" por "ou, mais genericamente — condição
   **suficiente**, não equivalente" (exemplo incluso; ver MINOR-2/r3 sobre o exemplo).
3. **MINOR-3 ✓**: §3.2 passo (3) agora explicita o **lema de correção limitada**
   uniforme `PA ⊢ (eval(v,θ^τ(w))=1 → θ(w))` como a ponte entre "τ_n(φ) é tautologia"
   (aritmético) e φ — a composição (2)+(3) está correta (fixar v₀: `∃w` disjuncto
   avaliando 1 ⟹ θ(w) ⟹ φ; custo de instanciação poly ✓).
4. **MINOR-4 ✓**: §5 declara `q(n,m) := m^{O(1)}` e a leitura de φ proposicional como
   sentença `L_PV` (ponte identidade).
5. **MINOR-5 ✓**: §2.1: `|π'| ≤ n = q` (não "= n").
6. **MINOR-6 ✓**: §2.1/§0.1 marcam a moral como **(C)** ("inexistência de instância
   full-range não-trivial é heurística, não teorema") e restringem "inócuo" aos
   exemplos canônicos.
7. **MINOR-7 ✓**: §9 substitui "todos corrigidos" pela auditoria honesta ("os 7 da v1
   auditados; um falso remanescente na v2; patch v3"); checklist §8 linha 6 atualizado.

## (c) Caça a fatais novos — NENHUM

Pontos varridos sem achado: (Q)|_{Σ₁} formal ( predicado de range no antecedente ✓ );
sketch §3.2 (verificação/sonoridade citadas e corretas; φ falso ⟹ atribuição-padrão
falsifica todos os disjunctos — argumento correto já presente); (C2′) intacta e
consistente com Q2.1 (nota nova do §2.1 — `τ_n(Con PA)=⊥` — **correta** e bem-vinda);
álgebra do corolário ✓; §5 e §6 inalterados e corretos; morais marcadas (C) ✓.

## Menores remanescentes (rodada 3 — não bloqueiam)

**MINOR-1/r3.** §4, modalidade (2): "testemunha longa ⟹ **algum** disjuncto
não-tautológico ⟹ τ_n(φ_n) não-tautologia" — a inferência como escrita é inválida
("algum disjuncto não-tautológico" não força a disjunção a não-tautologia). Correto:
**todo** disjuncto é não-tautológico (nenhuma testemunha ≤ cutoff) **e** os disjunctos
são falsificáveis **simultaneamente** pela atribuição-padrão (cada variável
proposicional := verdade da instância aritmética correspondente — todas falsas).
O argumento correto já existe em §3.2 para φ falso; replicar em uma linha. Troca de
uma palavra + uma cláusula.

**MINOR-2/r3.** §2: o exemplo "Presburger" para "T ⊇ Q não é necessário" é arriscado:
`Con(Pr)` não é expressível na linguagem de Presburger (sem codificação de sequências),
e com aritmetização padrão "Presburger ⊬ Con(Pr)" é resultado **não trivial** que
precisaria de citação. Substituir por exemplo incontroverso (ex.: T = verdades Δ₀, ou
teoria r.e. consistente sem axiomas aritméticos) — o ponto do exemplo sobrevive.

**MINOR-3/r3.** Rótulos stale de versão: título do §0 e do §9 ainda dizem "(v2)",
§9 "Próximos passos (1)" ainda pede "referee rodada 2", e a última linha diz "v2
responde" — atualizar para v3/rodada 3 (cosmético; o conteúdo já está correto).

## Veredito

O corolário central está agora **correto e honesto** (hipótese `τ_n(φ_n) ∈ TAUT`
equivalente à decomposição certa; três modalidades de não-contente declaradas); a
instância Σ₁ `(τ_n,q)` está definida, total, citada e com sobre-custos defensáveis;
(C2′) satisfaz (Q) full-range e diagnostica o full-range como inócuo sem superclaim;
as retratações da v1 estão todas rastreadas. Os remanescentes são de precisão
linguística e exemplo, não de matemática. **RECOMENDADO** para adoção como frente
fechada; para a submissão futura do primeiro limite inferior, o residual real segue
sendo a fonte Σ₁ (§6, marcada (C)) — fora do escopo desta entrega.

Referee Q2 — rodada 3 — RECOMENDADO — 11/10/2026

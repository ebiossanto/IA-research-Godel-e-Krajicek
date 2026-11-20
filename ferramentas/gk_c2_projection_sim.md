# gk_c2_projection_sim — Simulador da projeção em Res(k) + contraexemplo G1

**Origem:** extensão do repositório
[IA-research-Godel-e-Krajicek](https://github.com/ebiossanto/IA-research-Godel-e-Krajicek)
(MIT) — núcleo: frente **C2** (`krajicek_ddp/C2_K19_5_7_TEXTO_EXATO.md`,
`C2_r2_G1_contraexemplo.md` + referees r1/r2).
**Código:** `gk_c2_projection_sim.py` · **Teste (CI):**
`python gk_c2_projection_sim.py --n 400` · **Dados:** implícitos nos docs.

## Como citar

> Soares dos Santos, E. (2026). *gk_c2_projection_sim — Res(k) projection
> simulator and G1 counterexample* [Software]. Em:
> IA-research-Godel-e-Krajicek.
> <https://github.com/ebiossanto/IA-research-Godel-e-Krajicek>. MIT.

---

## 1. O que é

Simulador executável do **algoritmo de projeção `E`** para refutações
`Res(k)` (k-DNFs), com **verificação de invariantes** e **contraexemplo
automático**: dado um DAG de refutação com regras de Garlík, computa
`E(v) ⊆ λ(v)` (sub-linha "pura") e ou (i) extrai a certificação de um
lado, ou (ii) **localiza a violação** (ex.: `G1: retenção parcial de
bloco`).

## 2. Para que serve (aplicações)

1. **Detector automático de contraexemplos** para promessas de projeção
   (era manual na rodada r2 do referee);
2. **Caixa de ensaio** das obrigações (O1)–(O5) da frente C2;
3. Regressão do CI: invariantes + contraexemplo fixo = comportamento
   esperado (exit0) vs violação nova (exit1);
4. Base do motor `Res(k)` de `gk_dd_cert`.

## 3. Como usar

```bash
python gk_c2_projection_sim.py --n 400 --seed 20261119
# saída esperada:
#   CONTRAEXEMPLO r2: run_projection -> G1 VIOLADO: retencao parcial do bloco em 4
#   DAGs validos: N | FALHAS: (G1-only = esperado)
#   exit 0 (violacoes fora da classe G1 => exit 1)
```

Entradas programáticas: `Dag` + `run_projection(dag, promise)` +
`check_soundness` (regras) — reusados por `gk_dd_cert.py`.

## 4. Arcabouço matemático

### 4.1 Regras de `Res(k)` (Garlík CCC 2024 §2 — (A))

Linhas são **k-DNFs** (disjunções de termos com ≤ k literais):
`(1)` Axiom `x∨¬x`; `(2)` ∧-intro `A∨l₁, B∨(l₂…lⱼ) ⟹ A∨B∨(l₁…lⱼ)` (j≤k);
`(3)` Weakening `A ⟹ A∨B`; `(4)` Cut `A∨(l₁…lⱼ), B∨¬l₁…∨¬lⱼ ⟹ A∨B`.

### 4.2 Algoritmo `E` (r2) e invariantes

Por linha (ordem topológica): folha → `E := λ`; enfraquecimento →
`E := E(pai)` (descarta acrescimo); corte → **R1** retenção total
(`t ∈ E(p₁) ∧ bloco ⊆ E(p₂)` → corte próprio) | **R2** (`t ∉ E(p₁)` →
reusa `E(p₁)`) | **R3** (`t ∈ E(p₁) ∧ bloco ausente` → reusa `E(p₂)`,
exigindo **all-or-none** do bloco); ∧-intro → **A1** combina
(`l₁ ∈ E(p₁) ∧ s ∈ E(p₂)`) | **A2/A3** reuso do pai sem a peça.

**Invariantes verificados por linha (I1–I5):**
- **I1** `E(v) ⊆ λ(v)`; **I2** pureza (`E(v)` só com variáveis de `w(v)`);
- **I3** derivabilidade (regra aplicada aos E-pais, ou reuso = `E(pai)`);
- **I4** **all-or-none de blocos** (nunca retenção parcial — o coração de G1);
- **I5** extração: primeiro `∅` → lados iguais nos acessíveis, folhas do lado.

### 4.3 O contraexemplo G1 (15 linhas, determinístico)

`build_counterexample()`: folhas todas no lado1 (`Λ₁` UNSAT:
`+1=F, +2=T` falsifica `{-2,+1}`), **único ∧-intro puro** (promessa OK);
o corte intermediário **L10 consome `{+1}` como pivô do próprio bloco** →
em L4 o bloco `{{+1},{+2}}` chega **parcial** (`E(L9) = {{+2},{-2}}`) →
`G1 VIOLADO`. A análise exaustiva (3 ramos de L10) mostra que **nenhuma
atribuição E válida existe** — a resposta `i*=1` existe mas a projeção
gulosa não a extrai → **candidato r1 RETRACTADO**.

### 4.4 Busca aleatória (metodologia)

Gerador reverso a partir de `∅` (corte-tras/enfraquecimento-tras/and-tras)
com folhas singleton validadas por `check_soundness`; seed fixa;
**1602 DAGs válidos passam I1–I5**; falhas G1 aleatórias = classe conhecida
(comportamento esperado no CI).

## 5. Validação e limitações

- Contraexemplo fixo = teste de regressão (se o algoritmo mudar, ele
  acusa); `check_soundness` em todo DAG (referee r2-A1);
- **Limitações:** n≤5 no gerador (VAR_SIDE fixo `{1,2→1; 3,4→2}`) ·
  violação reportada no **primeiro** ponto (não multiponto — pendência r3)
  · motor `Res(k)` é **condicional** à promessa (violação = saída legítima).

## 6. Referências

- **Origem:** IA-research-Godel-e-Krajicek —
  `krajicek_ddp/C2_K19_5_7_TEXTO_EXATO.md` (regras exatas),
  `krajicek_ddp/C2_r2_G1_contraexemplo.md` (contraexemplo + Teorema C2.2′),
  `krajicek_ddp/C2_K19_5_7_referee.md`.
- Garlík, M. CCC 2024, §2 — DOI 10.4230/LIPIcs.CCC.2024.33.
- Krajíček, J. *Proof Complexity*, CUP 2019, cap. 5.7.

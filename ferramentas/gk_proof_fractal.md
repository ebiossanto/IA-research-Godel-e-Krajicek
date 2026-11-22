# gk_proof_fractal — Ponte prova→fractal (D4′): métricas de séries de provas

**Origem:** extensão do repositório
[IA-research-Godel-e-Krajicek](https://github.com/ebiossanto/IA-research-Godel-e-Krajicek)
(MIT) — núcleo: experimento **D4′** (`ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md`
§5-D4; Eixo FCT — Fractal Control Theory).
**Código:** `gk_proof_fractal.py` (v1) + `gk_proof_fractal_v2.py` (v2) +
`gk_proof_fractal_v2_r2.py` (r2: BCa/TOST/MDE80) ·
**Dados:** `gk_proof_complexity_fractal.json` + `gk_proof_fractal_series.csv`
(v1); `gk_proof_fractal_v2.json` + `gk_proof_fractal_v2_series.csv` (v2);
`gk_proof_fractal_v2_r2.json` + `gk_proof_fractal_v2_r2_contrasts.csv` (r2) ·
**Auditoria:** [`28_PONTE_PROVA_FRACTAL_D4.md`](../28_PONTE_PROVA_FRACTAL_D4.md)
e [`29_PONTE_PROVA_FRACTAL_D4V2.md`](../29_PONTE_PROVA_FRACTAL_D4V2.md)
(cada um + referee)

## Como citar

> Soares dos Santos, E. (2026). *gk_proof_fractal — proof-to-fractal
> bridge* [Software]. Em: IA-research-Godel-e-Krajicek.
> <https://github.com/ebiossanto/IA-research-Godel-e-Krajicek>. MIT.

---

## 1. O que é

Mede **assinaturas fractais de séries temporais de comprimentos de prova
reais**: famílias de instâncias UNSAT (`implication`, `php`, `tau` —
família τ(g)ᵦ de Krajíček) → provas DRAT (Cadical195) e Z3 → série
ordinal de comprimentos por (tamanho, semente) → métricas **Hurst R/S**,
**Higuchi D_H**, **box-counting D_box** + **bootstrap em blocos**.

## 2. Para que serve (aplicações)

1. **Discriminar regimes de crescimento** de complexidade de prova
   (exponencial vs quase-linear) por métricas fractais — primeira medição
   desse tipo em refutações reais;
2. Calibrar a leitura "prova dura = mais fractal" — **refutada** no projeto
   (resultado negativo documentado);
3. **D4′ v2 executado** (`gk_proof_fractal_v2.py`): provas *mínimas*
   canônicas (via `gk_minref`) vs DRAT pareado, famílias n≤6 (controle de
   regime), variante anti-quantização `relinc`, hipóteses a priori —
   H_C3 confirmada / H_C4 nominal com ressalva (ver §4.5);
4. Ferramenta interdisciplinar: prova de complexidade ↔ sistemas complexos.

## 3. Como usar

```bash
python gk_proof_fractal.py                    # v1: seed20261119, 3 famílias
# → gk_proof_fractal_series.csv + gk_proof_complexity_fractal.json
python gk_proof_fractal_v2.py                 # v2: minref canônico + DRAT
# → gk_proof_fractal_v2_series.csv + gk_proof_fractal_v2.json
python gk_proof_fractal_v2_r2.py              # r2: BCa + TOST + MDE80
# → gk_proof_fractal_v2_r2.json + gk_proof_fractal_v2_r2_contrasts.csv
# (sha256 normalizado CRLF→LF registrado no JSON; CSV sem colunas de
#  tempo → reprodução byte-a-byte entre execuções)
```

## 4. Arcabouço matemático

### 4.1 Séries

Para cada família `F` e sistema `S`: `x_m = comprimento da prova S da
instância m` ordenada por `(m, semente)` — série ordinal de ~64 pontos.

### 4.2 Métricas

- **Hurst (R/S):** para janelas `n ∈ [8, N/4]`, média
  `R(n)/σ(n)` onde `R` = amplitude do desvio acumulado
  (`max_{i≤n} S_i − min_{i≤n} S_i`) e `S_i = Σ_{k≤i}(x_k − x̄)`;
  regressão `log(R/S) = H·log(n) + c` → **H**.
  `H > ½` = persistente; `H < ½` = anti-persistente.
- **Higuchi D_H:** comprimento da curva na escala `k`:
  `L(k) = (n−1)/(k²·(#pts−1)) · Σ|X_{m+k} − X_m|`;
  regressão `log L(k) = −D_H·log k + c` (equiv. `log L` vs `log(1/k)`
  → slope `= D_H`). `D_H ∈ [1,2]`; validação: ruído→2,075 · passeio→1,725 ·
  seno→1,199.
- **Box-counting D_box:** embutir a série como curva `(t, x_t)`; contar
  caixas de lado `ε = 2^{−j}`; regressão `log N(ε) = −D_box·log ε + c`.

### 4.3 Inferência: bootstrap em blocos

Reamostragem de **blocos consecutivos** (bloco=8, B=300, seed fixa)
preservando autocorrelação → IC95 percentílico de cada métrica e dos
**contrastes** `Δ = métrica(Família_A) − métrica(Família_B)`;
**variante `log1p`** paralela (robustez à escala — anti-overfitting).
Critério confirmatório (a priori): contrastes `D_H` em pares com `php`,
raw+log1p (4 testes).

### 4.4 Resultados (19/11/2026, seed20261119)

| Família | n | prova média | H | **D_H** | D_box |
|---|---|---|---|---|---|
| implication |64 |12,9 |0,703 |**2,000** |0,863 |
| **php** (exponencial) |60 |**183.250** |1,363* |**1,269** |0,783 |
| tau (τ(g)ᵦ) |64 |34,6 |0,707 |**1,983** |0,804 |

Contrastes `D_H`: `imp−php = +0,731 IC[0,051;0,732]` · `php−τ = −0,715
IC[−0,873;−0,192]` — **4/4 confirmatórios excluem0 (raw e log1p)**;
`imp≈τ` (inclui0). \*H>1 em série tendenciosa = descritivo.

**Interpretação honesta:** separação por **regime de crescimento**
(exponencial vs quase-linear) — **não** "dura=mais fractal" (refutado).

### 4.5 D4′ v2 (20/11/2026): comprimentos MÍNIMOS canônicos + controle de regime

O v2 (`gk_proof_fractal_v2.py`) troca a fonte e controla o regime:

- **Fonte canônica:** em vez de provas do solver, mede **`minref`**
  (comprimento mínimo exato, `gk_minref`) na **mesma instância** em que
  mede DRAT — contraste **pareado** minref-vs-DRAT por família;
- **Famílias n≤6** (escopo do minref): `implication` (m=3–6), `cadeia`+
  ruído binário (k=3–6), `tau_tiny` (τ com k=2, w=3, prof.1) — 64 pontos
  cada, 192/192 UNSAT verificados, 0 censuras;
- **Anti-quantização (pendência A2 do referee):** variante **`relinc`** =
  Δ de `log1p(x)` (remove nível/escala/tendência), além de raw/log1p;
- **Hipóteses a priori (pendência A4):** 12 contrastes confirmatórios
  declarados no código (D_H × raw+relinc) — **H_C3** (famílias não separam
  quando o regime é controlado) e **H_C4** (fonte não distingue).

**Resultados:** H_C3 **CONFIRMADA** (6/6 incluem 0) — sustenta a leitura
A1: no v1 a métrica media **regime**, não família. H_C4 **REFUTADA
(NOMINAL)** (1/6 exclui) **mas incoerente** — o ponto está fora do próprio
IC95 (saturação do Higuchi no teto D_H≈2; flag `point_outside_ci` marca
9/93 contrastes) → leitura sustentada: invariance de fonte mantida com
ressalva. minref é sistematicamente **menor** que DRAT (cadeia 7,5 vs
11,8) sem que as métricas distingam. Detalhes, diagnóstico e pendências
r2 (TOST, BCa, τ k↑): `29_PONTE_PROVA_FRACTAL_D4V2.md` + referee.

**Rodada r2 (`gk_proof_fractal_v2_r2.py`, §8 do doc 29):** re-análise do
CSV congelado com **BCa** (selftest vs scipy: OK, diff 0,013), **TOST**
(margens 0,10 primária — âncora ~1/7 do efeito v1 — + 0,15/0,20
sensibilidade) e **MDE80** (poder). Achados: **0 separações** em ambas
as hipóteses; **equivalência ±0,20 = 6/6** (±0,10 inacessível —
MDE80≈0,19); a exclusão r1 do H_C4 virou **INCOERENTE** (ponto fora do IC
nos dois métodos); **BCa não resolveu a saturação** (8/81 incoerentes
persistem, 2 ICs degenerados) — a regra de incoerência é o remédio;
pista **boxdim** sobrevive em 2/3 variantes (candidata pré-registrada a
r3). Artefatos: `gk_proof_fractal_v2_r2.json` +
`gk_proof_fractal_v2_r2_contrasts.csv`.

**Rodada r3 (`gk_proof_fractal_v3.py`, doc `30_`):** **boxdim
pré-registrado** (commit anterior ao run — prioridade temporal) em **192
instâncias novas disjuntas** do r2. Resultados: **pista A4 CONFIRMADA**
(`drat:implication−cadeia`, Δ=−0,170, sobrevive Bonferroni); padrão-τ em
`minref` **2/3** (τ separa ambos; imp−cadeia não separa, mas equivalência
a ±0,05 não certificável → sensibilidade pré-declarada: eq a ±0,08 ✓);
H_B2 1/2 (1 incoerente); **H_B4 refutada** — incoerência instável entre
métricas (higuchi 0/27 aqui) → é **do par de séries**, não do
instrumento; **delete-d vs delete-1: 0/135** discordâncias; tipo-I 0,04 ·
poder 9/10. Métricas novas `boxdim_rank` (invariante monotona) e `saltos`
(0/27 incoerentes). Artefatos: `gk_proof_fractal_v3_series.csv`
(`6d4cbdd1…`) + `gk_proof_fractal_v3_contrasts.csv` (`0cb1dce2…`) + JSONs.

**Rodada r4 (`gk_proof_fractal_v4.py`, doc `31_`):** **n=384/família**
(1152 instâncias disjuntas de r2+r3; alvo MDE80<0,06) + **margem 0,08
ancorada em precisão** (meia-largura IC90 do r3) + **regras exaustivas
de veredito** + **diagnóstico de z0**. Resultados: **`saltos` CONFIRMADA
3/3 com Bonferroni** (âncoras r3 replicadas com desvio ≤0,012, z0
saudável, percentil concorda — métrica local preservada pelo resample);
boxdim **INDETERMINADO** (2/6 contáveis, 4 incoerentes — imp−τ virou
efeito≈0; (d)(f) com ambos os métodos excluindo mas ponto fora do BCa);
**mecanismo de z0 medido**: z0≈viés/SE (94%), incoerência 7%→33% com n
→ **BCa+bloco fixo inadequado para n grande** (viés não encolhe, SE
encolhe); H_C4 **4/6** (falha de alvo declarada); delete-d 0/135 (3ª
rodada); discordância pct-vs-BCa 39%. Incidente: crash nativo
`Cadical195.__del__` (Windows) contido por **checkpoint atômico +
retry** (`3d244ab`, 3 tentativas). Artefatos: `gk_proof_fractal_v4_*
(`c92f0968…` / `8419f25b…`).

**Rodada r5 (`gk_proof_fractal_v5.py`, doc `32_`):** os 3 itens pedidos —
**`saltos` como métrica primária**, **método de IC novo com calibração de
incidência** e **regra de 2 níveis**. Método **selecionado pela calibração
pré-run** (S4–S6): percentil + **bootstrap estratificado por parâmetro**
(DGP real: instâncias iid dentro do estrato; tipo-I 0,075 vs BCa-estrat
0,325 → BCa virou parceiro da regra). Resultados: **H_D1 `saltos`
CONFIRMADA 3/3 Bonferroni** (3ª rodada: r3→r4→r5); **H_D2 boxdim PARCIAL
5/6** (equivalência ±0,05 certificada, pista (d) e fonte (f) limpas pela
1ª vez, (a) sem efeito 3ª vez); **H_D3 incidência 4,4%** (r4: 33%;
head-to-head: bloco8 bloquearia 4/9 vs primário 0/9); **H_D4 6/6 ATINGIDO**
(MDE 0,014–0,052). Ramo concordante da regra: 0 ocorrências em dados
reais (resposta empírica registrada). Incidentes: 3 crashes CaDiCaL +
2 bugs de plumbing pós-pré-reg (corrigidos, smoke test virou
procedimento). Artefatos: `gk_proof_fractal_v5_*` (`df3737ce…` /
`c30b13f2…`).

> **Bugs corrigidos na rodada (7º e 8º do projeto):** `gen_tau` com
> unidades de saída invertidas (v1 permanece válido: 188/188 UNSAT por
> solver) e geradores usando `tuple.__hash__()` — seed não reproduzia
> entre processos; corrigido com `_det_seed()` (CRC32). Errata no 28_ §5.

## 5. Validação e limitações

- Métricas **validadas antes de medir** em séries sintéticas (a validação
  pegou5 bugs do encoder nesta série de trabalho);
- **Limitações:** séries50–64 pontos (ICs largos) · Higuchi k≤8 ·
  provas de solver (não mínimas — v2 com `gk_minref`) · confundimento
  tendência×ruído declarado · H_C2 (Res-vs-EF) **deferido** (EF não
  mensurável) · nível N1+N2 (sem N4).

## 6. Referências

- **Origem:** IA-research-Godel-e-Krajicek —
  `28_PONTE_PROVA_FRACTAL_D4.md` (resultados+referee),
  `ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md` §5-D4, `DESCOBERTAS_FRONTIER_2026-10-13.md`.
- Higuchi, T. (1988). *A new method for the measurement of fractal
  dimension of time series.* Physica D.
- Hurst, H.E. (1951). *Long-term storage capacity of reservoirs.* Trans. ASCE.
- Mandelbrot, B. B. (1982). *The Fractal Geometry of Nature.* (box-counting).
- Garlík, M. CCC 2024 (família τ/refs — contexto).

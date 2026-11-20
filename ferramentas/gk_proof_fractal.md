# gk_proof_fractal — Ponte prova→fractal (D4′): métricas de séries de provas

**Origem:** extensão do repositório
[IA-research-Godel-e-Krajicek](https://github.com/ebiossanto/IA-research-Godel-e-Krajicek)
(MIT) — núcleo: experimento **D4′** (`ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md`
§5-D4; Eixo FCT — Fractal Control Theory).
**Código:** `gk_proof_fractal.py` · **Dados:** `gk_proof_complexity_fractal.json`
+ `gk_proof_fractal_series.csv` · **Auditoria:**
[`28_PONTE_PROVA_FRACTAL_D4.md`](../28_PONTE_PROVA_FRACTAL_D4.md) (+referee)

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
3. Base para **D4′ v2**: provas *mínimas* (via `gk_minref`) em vez de
   provas de solver; normalização anti-quantização (pendência do referee);
4. Ferramenta interdisciplinar: prova de complexidade ↔ sistemas complexos.

## 3. Como usar

```bash
python gk_proof_fractal.py                    # seed20261119, n=4 famílias
# → gk_proof_fractal_series.csv + gk_proof_complexity_fractal.json
# (sha256 normalizado CRLF→LF registrado no JSON)
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

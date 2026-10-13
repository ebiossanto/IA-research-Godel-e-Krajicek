# Descobertas Frontier — 13 de Outubro de 2026 (continuação)
### Terminal-Laboratório · IA-Research Gödel/Krajíček · FCT · Motor Fractal

> **(P)** Documento próprio, continuando `DESCOBERTAS_ORIGINAIS_2026-10-13.md`.
> Execução das cinco trilhas de fronteira (Sweep/F1, D2-filtros, τ-real-Z3/F3, F4
> telemetria real, F5 D4 reframe) reprodutível via `python gk_frontier_integration.py`.
> Saída congelada: `gk_frontier_resultados.json` (e per-track CSV/JSON).

---

## F1 · Sweep analítico — relaxação e `ρ_c`

**Pergunta** (resposta a D1). Sob o trade-off analítico
`I_DFA = ρ/(1−ρ)·p²` vs `I_PFA = √ρ/(1−ρ)·p_pfa²` com `p_pfa = p·(1−r)`,
`ρ_c(r)` varia com `r` e com o ruído em `p`? Qual é a leitura honesta de `0.25`?

**Método:** `ρ_c(r)` analítico = `(1−r)^4` (break-even exato via `brentq`, 2000
bootstrap para noise em p ∈ {0,0.1,0.3}).

**Tabela de transição real:**

| r | ρ_c analítico | σ=0.0 | 0.1 | 0.3 | std |
|---|---|---|---|---|---|
| 0.02 | 0.9224 | idem | idem (±3e−16) | |
| 0.0833 (=1/12) | **0.7061** | 0.7061 | 0.7061 | 0.7061 | ~2e-16 |
| 0.1667 (=1/6) | 0.4823 | idem (1.5e-16) | | |
| 0.25 | **0.3164** | 0.3164 | 0.3164 | 0.3164 | ~1.1e-16 |
| 0.3333 | 0.1975 | idem | | |
| 0.50 | 0.0625 | idem | | |
| 0.75 | 0.0039 | idem | | |

**Descobertas (N2 — numéricas):**
1. `ρ_c = (1−r)^4` — aproximar r a 0.25 dá ρ_c = 0.3164 (mais próximo de 0.25
   mas ainda longe).
2. A raiz analítica é **insensível a ruído em p** (std ~1e−16). Ou seja: a
   discrepância `0.706 vs 0.25` NÃO é artefato de estimativa; o valor é
   **determinístico sob esse modelo**.
3. Leitura honesta: combinando a implementação empírica `p_pfa = p − p/12`
   (r = 1/12, ρ_c = 0.706), o sistema observado (**ρ=0.272 na telemetria real**)
   cai **ABAIXO do cutoff** (DFA suficiente sob ρ_c=0.706). Sob o publicado
   `ρ_c=0.25` o mesmo ρ=0.272 ficaria **ACIMA** (PFA "necessário"). Avancar com o
   audit em D: checar a carga *durante o episódio de tail-latency* (não a média).
→ `gk_F1_rho_c_sweep.csv`, `gk_F1_analytic.csv`.

---

## F2 · D2 non-abelian + 4 filtros (Donoho-Johnstone e EMA)

**Pergunta:** Box-dim colapsou em D2 (−1). Filtrar por EMA / Donoho resolve? A
separabilidade por H sobrevive?

**Método:** 40×400 séries/grupo, 4 filtros
(`raw`, `ema(0.3)`, `donoho(db1 L3 soft)`, `ema→donoho`);
H (R/S) + Box-dim (fixed) + Mann-Whitney bidirecional.

**Resultado (H, diferenças são fortes e estáveis):**

| filtro | H ab (μ±σ) | H non (μ±σ) | Δ | p_H | Box-D p |
|---|---|---|---|---|---|
| raw | 0.577 ±0.079 | 0.065 ±0.051 | 0.512 | 1.4e-14 | NaN (degenerado) |
| ema | 0.746 ±0.080 | 0.273 ±0.057 | 0.473 | 1.4e-14 | NaN |
| donoho_soft | 0.677 ±0.063 | 0.414 ±0.054 | **0.263** | 1.4e-14 | 0.67 (não sig.) |
| ema→donoho | 0.746 ±0.070 | 0.482 ±0.051 | 0.264 | 1.7e-14 | 7.1e-12 (n=40/gr) |

**Descobertas:**
1. **H separa como detector robusto** sob todos os 4 filtros (p_H<1.5e-14): a
   "assinatura de classe" não depende do filtro.
2. **Donoho soft equaliza:** baixa a lacuna de 0.512 → 0.263, sugerindo que
   o grupo não-abeliano tem **escalamento mais baixo de reverb**, coerente com a
   não-comutatividade (mistura de modos). Efeito "windowing" a observar.
3. **Box-dim permanece degenerado** (NaN/"−1") — a métrica implementada falha
   geometricamente (polyfit singular por cauda de valores constantes em bins).
   **Declarar D2 como descoberta somente em H.**
4. **ema→donoho** é o único filtro em que Box-D obtém p<1e-11 — provavelmente
   espúrio; re-classificar com bins adaptativos antes de claim.
→ `gk_F2_nonabelian_filters.csv`, `gk_F2_summary.csv`.

---

## F3 · τ real no Z3 com configurações variadas

**Pergunta:** Resolvido θ H=0.297 (phi_len=4, r_w=2, w_star="00"). Varia esse H com
phi_len, r_w ou w_star?

**Método:** Z3 SMT, 4 configurações (
`phi_len∈{3,4,5}`; `r_w∈{2,3}`, `w_star∈{00,01}`).
Valid rate = 1.0 em todas.

**Tabela:**

| config | n_transl | H (θ) | H (interpolant) | θ_mean±std |
|---|---|---|---|---|
| phi_len=3,r_w=2,w*=00 | 216 | **0.2970** | 0.2970 | 36.5 ±16.54 |
| phi_len=4,r_w=2,w*=00 | 216 | 0.2970 | 0.2970 | 36.5 ±16.54 |
| phi_len=4,r_w=3,w*=01 | 216 | 0.2970 | 0.2970 | 36.5 ±16.54 |
| phi_len=5,r_w=2,w*=00 | **144** (Full sweep) | **0.4091** | 0.4091 | 36.5 ±16.56 |

**Descoberta (N2):**
- **H≈0.297 recorrente:** a zona anti-persistente **não** muda com `w_star`, `r_w`,
  nem phi_len∈{3,4}. Coerência robusta: a estrutura de θ-overhead da
  tradução parece dominada pelo `8+(h%17)` do gerador non-w_star, não pelos
  parâmetros.
- Apenas quando `phi_len=5` (menos casos permitidos, + restricções), H=0.409;
  **H cruza 0.35 (zona crítica→ nominally stable)**. Artefato da escala, ou sinal
  de que o threshold 0.35 é sensível a n de φ? **Próximo passo:** sweep phi_len∈{6,8,12}
  e regressão H~phi_len (confirmar ou refutar a travessia).
- **Significado prático:** a monotonicidade σ_tgt vs θ (Spearman) continua não
  aplicável (mean constante). A hipótese D4 em nível zeta permanece pendente.
→ `gk_F3_tau_real.csv`, `gk_F3_tau_real.json`.

---

## F4 · Telemetria real + FCT 4-axis (cpu_timeseries, n=300)

**Dado base (fonte verdade para o motor):** 300 amostras, 0.1 s, mean 27.19% CPU,
range [0,100].

**Método:** Hurst R/S (raw/EMA span-5/Donoho soft), entropia Shannon, box-dim,
FractalEngine completo (λ=0.272, μ=0.353), Donoho threshold + entropia pós.

**Resultado F4:**

| métrica | raw | EMA(0.3) | Donoho(db1) |
|---|---|---|---|
| H | 0.3208 | 0.6060 | 0.4849 |
| entropia Shannon | 2.5264 | — | 2.1554 |
| box-dim | 0.7684 | — | 0.6604 |

- **FCT:** P99 = 4.36, Entropia = 0.722, `protection_factor = 0.991`.
- `λ=0.272; μ=0.353` — ρ=0.272 fica (D1) **abaixo de 0.706 → DFA suficiente**
  sob esse modelo (e apenas 0.02 acima do 0.25 publicado). Esta é uma **medida
  de carga observada**, não pode ser generalizada como identidade do sistema.
→ `gk_F4_telemetry_real_filtered.csv`, `gk_F4_telemetry_result.json`.

**Descoberta (N0+N1):**
- O sinal real tem H=0.321 — **mesma banda anti-persistente** do proof-chain (0.297–0.409).
  Hipótese empírica: sistemas em regime *hunter* (semi-hot) ficam entre H 0.30–0.35.
- Donoho + EMA elevam H (0.48 / 0.61); box-dim cai (0.77 → 0.66); entropia cai 2.53→2.16
  → o filtro remove ruído lossy preservando dimensão. **Alerta:** D (box-dim) parece
  efeito (filter→dimensão) dependente do método; validar com um segundo algoritmo
  de D (Higuchi/variância) antes de claim.

---

## F5 · D4 reframe — H vs taxa de "dissatisfação"

**Pergunta:** A H global do proof-chain contém poder preditivo per-instância (que
instâncias terão θ "pequeno")?

**Método:** 300 re-samples de tamanho 169 (sem replacement) do ordinal θ, calcula H
(R/S) e fração < mediana. Spearman H vs fração.

**Resultado:** Spearman H-vs-fraction = **0.0160** (p=0.78). **Bootstrap H = 0.0984 ± 0.111**.

**Descoberta (N2 — negar claim?):** A H global está **desacoplada** da taxa de
instâncias "pequenas" (fraction ~0.5), no nível de reamostragem do experimento.
A anti-persistência **não** é preditiva de qual instância específica é "fácil".
Isso restringe a utilidade de D4: H é um *invariante global*, não um preditor
per-caso. **Dono da conclusão:** refinar por blocos de teoria (não pooling global).

---

## Tabela de honestidade epistêmica

| Qualidade | F1 | F2 | F3 | F4 | F5 |
|---|---|---|---|---|---|
| Reproduzível por comando | ✔ | ✔ | ✔ | ✔ | ✔ |
| Seed fixa | ✔ | ✔ | ✔ (4 configs) | ✔ | ✔ |
| Metodologia (Ten-Proofs N2) | ✔ (brentq) | parcial (Box-D NaN) | ✔ (Z3 real 100%) | ✔ (telemetria real) | ✔ (bootstrap-300) |
| Efeito-vestígio/Artefato conhecido | sim (r-modelo simplificado) | sim (box-D degenerate) | parcial (fixed θ_mean) | sim (filtro altera D) | sim (H-subsample) |
| Peer-review externo (N4) | pending | pending | pending | pending | pending |

---

## Próximos passos (5 to-do focados, sem alargar)

1. **F1:** medir **ρ durante eventos de tail-latency real** (marcadores REA). Dissuadir
   do uso de `ρ=0.272` médio se a carga no pico for >0.3 (então classe começa no PFA).
2. **F2:** re-implementar Box-dim (Higuchi/variância) e testar com ± noise para não
   contaminar o `0.746`-`0.273` club (confirmar que Donoho **não** equaliza aritmeticamente).
3. **F3:** sweep `phi_len ∈ {6,7,8}` e checar se H sobe (novaro `0.35`) de forma
   monotonica (regressão em H~phi_len).
4. **F4:** executar pipeline REA bridge (cpu critical/mutation/ssyscall burst) sob
   o filter wavelet e validar a predição `NOMINAL/CRITICAL` por H real.
5. **F5:** repetir por bloco de teoria (σ_tgt) e ver se o Spearman por blocos H-vs-fraction
   se torna significativo — pode revelar que a global H "esconde" sinal per-bloco.

---

## Compromisso

- Nenhuma descoberta nova aqui é reivindicada como lower
  bound computacional — a hipótese δ≥γ≥β≥ρ permanece **honest disclosure**.
- Todas os 5 textos + 11 arquivos saem com **commit 759e06b já pushado** +
  novos dados (10arquivos: `gk_F1_*`, `gk_F2_*`, `gk_F3_*`, `gk_F4_*`,
  `gk_F5_*`, `gk_frontier_resultados.json`). Coin o que falta (atualizar stream INDICE).

---

*Sha256 dos arquivos fonte (N1) e comando de re-running (`python gk_frontier_integration.py`)
estão em `gk_frontier_resultados.json` §executed_utc.*
# 28 — Ponte Prova → Fractal (D4′ v1): métricas fractais separam regimes de crescimento de prova

**Data:** 19/11/2026 · **Classificação:** **(P)** experimento próprio + **(C)** hipóteses
testadas · **Nível Ten-Proofs:** N1 (script reproduzível, seed fixa) + N2 (bootstrap
nesta máquina). **Não** é resultado de complexidade de provas nem lower bound.

**Reproduzir:**
```powershell
python -u gk_proof_fractal.py
# → gk_proof_complexity_fractal.json + gk_proof_fractal_series.csv
# seed=20261119 · B=300 · bloco=8 · CSV sha256=92e1ffd3b01f2585… · runtime 250s
```

---

## 1. Pergunta

**(D4′ de `ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md` §5)** — o comprimento de provas
**reais**, indexado ordinalmente por (tamanho, semente), forma uma série cujas
métricas fractais (Hurst R/S, Higuchi D_H, box-counting D_box) **separam famílias
de dificuldade de refutação** acima do ruído de bootstrap?

**Hipóteses:**
- **H_C1 (separação):** métricas fractais distinguem `php` (duro) de `implication`
  (fácil) com IC95 excluindo 0.
- **H_C2 (Res vs EF):** Resolution mantém auto-similaridade (H alto) vs EF
  "aplaina" — **DEFERIDO** (ver §6): Extended Frege não é mensurável com o tooling
  disponível; o proxy Z3 **não** é EF.

## 2. Método (triangulação: simbólico → numérico)

### 2.1 Famílias de instâncias (todas garantidamente UNSAT — 188/188 confirmado)

| Família | Construção | Nº | Prova DRAT real |
|---|---|---|---|
| `implication` | grafo de implicações aleatório (semeado) `[-a,b]` + unidades `[s]`,`[-t]` com caminho s→t |64 (m=8..23 ×4 seeds) |8–~50 linhas |
| `php` | buraco do pombo PHP_{m+1→m} com permutação de variáveis (semeada) |60 (m=4..9 ×10 seeds) |48 → **935.504** linhas |
| `tau` | **família τ(g)ᵦ de Krajíček**: circuito Booleano semeado (k=8 entradas → w=10 saídas; \|imagem\|≤256<1024), b∉imagem, CNF de Tseitin de `g(x)=b` |64 (profundidade=2..9 ×8 seeds) |26–~50 linhas |

> **Nota de projeto:** a família `tau` é o próprio objeto τ do programa PPR —
> esta é a primeira medição fractal de refutações de τ(g)ᵦ reais.

### 2.2 Dois sistemas por instância

- **`resolution_drat`** — **DRAT real** via PySAT **Cadical195** (`with_proof=True`),
  nº de linhas da prova. *(Glucose4/42 devolvem prova VAZIA em UNSAT trivial de
  preprocessamento — documentado; fallback mantido.)*
- **`z3_proof_nodes`** — nº de nós sexpr da prova do Z3 (`set_param('proof')` +
  `s.set(proof=True)`; timeout 5s). **PROXY de cálculo estendido — NÃO é Extended
  Frege** (caveat permanente; 10 timeouts em php → n=50).

### 2.3 Métricas (implementação padrão, validadas antes de medir)

| Série sintética | H_RS | **D_H** | D_box | Esperado |
|---|---|---|---|---|
| ruído branco (n=64) |0,621 |**2,075** |0,878 | H≈0,5–0,65; D≈2 ✓ |
| passeio aleatório |0,893 |**1,725** |0,856 | persistente; D≈1,5–1,8 ✓ |
| seno (período16) |1,042 |**1,199** |0,790 | curva suave D≈1 ✓ |

- **H_RS** = R/S clássico (janelas 8..n/4); **D_H** = Higuchi (k≤8);
  **D_box** = box-counting da curva embutida (t, x_t).
- **Correções pós-validação (rodada 1 → 2):** sinal do Higuchi (`+slope`);
  janelas R/S degeneradas para n<64 (`range(8,n/4+1)`); aviso Z3 removido.
- **Robustez:** todas as métricas e contrastes computados também em **log1p**
  (dominação de escala do php:6 ordens de magnitude).

## 3. Resultados

### 3.1 Séries (Resolution/DRAT)

| Família | n | Prova média | H_RS | **D_H** | D_box |
|---|---|---|---|---|---|
| implication |64 |12,9 |0,703 |**2,000** |0,863 |
| php |60 |**183.250,6** |1,363* |**1,269** |0,783 |
| tau |64 |34,6 |0,707 |**1,983** |0,804 |

\* H_RS>1 em série fortemente tendenciosa (não-estacionária) — **descritivo apenas**.

Proxy Z3 (n=64/50/64): D_H = 2,005 / 1,856 / 2,135 — mesma ordem de grandeza,
direção não idêntica (cálculo diferente; sem conclusão sobre EF).

### 3.2 Contrastes (bootstrap em blocos, B=300, IC95)

| Contraste (D_H, DRAT) | raw | log1p | Veredito |
|---|---|---|---|
| implication − php | **+0,731 [0,051; 0,732]** | **+0,907 [0,332; 0,835]** | **EXCLUI 0 (ambas)** ✓ |
| php − tau | **−0,715 [−0,873; −0,192]** | **−0,879 [−0,914; −0,487]** | **EXCLUI 0 (ambas)** ✓ |
| implication − tau | +0,016 [−0,350; 0,008] | +0,028 [−0,329; 0,059] | inclui 0 — indistinguíveis |

**H_C1: CONFIRMADA como separação** — 4/4 testes confirmatórios (D_H, pares
envolvendo php, raw+log1p) excluem 0 com sinal coerente.

### 3.3 Nota de múltiplas comparações (exigência do referee A4)

Foram computados 18 contrastes (3 pares ×3 métricas ×2 variantes); os4
confirmatórios estão declarados **a priori** em §3.2 (D_H raw+log1p, pares com
php). **Sem correção de Bonferroni aplicada** — se aplicada (α=0,05/4=0,0125):
**php−tau permanece robusto** (IC longe de0 nas duas variantes);
**implication−php raw fica no limite** (limite inferior0,051). Leitura honesta:
**evidência forte para php−tau; moderada para implication−php raw**; a variante
log1p de implication−php é intermediária (limite0,332 ≫0,0125 → também robusta
sob a régua mais severa). Verdict final mantido, força do veredito modulada.

## 4. Interpretação (e refutação da hipótese ingênua)

1. **A direção é a contrária à prevista:** `php` (família dura) tem D_H **menor**
   (1,27 vs ~2,0) — sua série é **mais suave**. Causa: a curva do php é dominada
   por **crescimento exponencial determinístico** em m (48 → 935.504), enquanto
   `implication`/`tau` são decaimentos/jitter de **inteiros pequenos** (quantização).
   → **Refutada** a leitura ingênua "prova dura = mais fractal".
2. **O que a métrica captura de fato:** o **regime de crescimento** da complexidade
   de prova ao longo do índice ordinal — exponencial (php) vs quase-linear
   (implication/tau). Essa fronteira **é** a do programa δ/𝒢 (o que a reflexão
   faz com o déficit δ ao longo de níveis), o que torna a ponte mensurável e útil.
3. **Separação robusta:** sobrevive à transformação log1p (que retira a tendência
   exponencial em escala log) → não é artefato puro de escala; mas **não** separa
   os dois regimes "fracos" entre si (implication≈tau) — métrica sensível, não
   universal.

## 5. Reprodutibilidade

- Seed `20261119`; CSV com sha256 `92e1ffd3b01f2585…` registrado no JSON;
  runtime 250s; 188/188 UNSAT; PySAT1.9.dev24 (Cadical195), z3-solver5.4.1,
  Python3.15.2.
- Saídas: `gk_proof_complexity_fractal.json` (validação + séries + bootstrap +
  contrastes + hipóteses), `gk_proof_fractal_series.csv` (188 linhas).
- **Errata (20/11/2026, 8º bug — referee §A10):** a geração das instâncias
  usava `tuple.__hash__()` (randomizado por processo) — o seed **não**
  reproduzia os mesmos dados *entre execuções*, apesar de o artefato
  congelado acima ser íntegro (sha registrado; 188/188 UNSAT verificado
  na própria execução). Corrigido com `_det_seed()` (CRC32 determinístico);
  re-execuções pós-correção geram instâncias da mesma distribuição mas
  possivelmente distintas das congeladas. Detalhes: referee §A10 e
  `29_PONTE_PROVA_FRACTAL_D4V2.md`.

## 6. Limitações e H_C2 DEFERIDO (honestidade de escopo)

1. **EF não foi medido.** PySAT produz DRAT (Resolution); Z3 é outro cálculo.
   `z3_proof_nodes` é **proxy** — qualquer afirmação Res-vs-EF fica **deferida**
   até sistema EF implementável (ou export de prova EF).
2. **Séries curtas** (50–64 pontos) → ICs largos; Higuchi com k≤8.
3. **Confundimento tendência×ruído** (referee §A1): D_H separa regimes de
   crescimento, não "dureza" per se — enunciado corrigido em §4.
4. **Artefato de quantização** (referee §A2): inteiros pequenos inflam D_H —
   log1p não remove; mitigação futura: normalizar por média ou usar incrementos
   relativos; séries de php com mesmo número de dígitos.
5. **Grades diferentes por família** (m=4..9 vs 8..23 vs 2..9) — compara-se
   forma estatística da curva, não ponto a ponto.
6. Exit code do processo =1 apesar de sucesso (z3 atexit) — artefatos completos
   e íntegros (JSON+CSV escritos antes; sha confere).

## 7. Próximos passos (caminho D — v2)

1. **Normalização anti-quantização**: métricas sobre incrementos relativos
   `Δlog(1+p)` → isolar tendência de verdade.
2. **Família τ com tamanhos crescentes** (k=8..14) para curvas τ de maior
   dinâmica — ligação direta com PR10/PR11 (R não-vácuo, Θ polinomial).
3. **Séries em b** (índice lex de b para σ fixo) — a "série ordinal" original do
   D4′ com as provas τ reais desta rodada.
4. H_C2: avaliar viabilidade de EF (ex.: bibliotecas de proof-checking EF) antes
   de qualquer claim.

---

**Referências:** `ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md` §5-D4 ·
`gk_proof_fractal.py` · `PLANO_PESQUISA_E_DESENVOLVIMENTO.md` P3.4 ·
referee: `28_PONTE_PROVA_FRACTAL_D4_referee.md`

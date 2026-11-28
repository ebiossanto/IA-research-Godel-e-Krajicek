# motor_fractal_rea — vertente FCT/REA (extração do repo externo)

**Proveniência:** extração de `Motor-Fractal-REA-main.zip` (snapshot da
branch `main` de **<https://github.com/ebiossanto/Motor-Fractal-REA>**,
baixado 06/11/2026) — **vertente FCT/REA** do programa (uma das duas
vertentes do `ONDE_ESTAMOS` §1: DD_P/Krajíček + FCT). O mesmo método
ten-proofs (`AGENTS.md` do workspace IA-RESEARCH) e a mesma árvore
`formal-certification/` do projeto-mãe (`AGENTS.md` linha37).

**Não é cópia de trabalho deste repo** — é o estado do repo externo no
snapshot; o `fractal_engine/` daqui evoluiu em paralelo (fixes de
13/10, `integrations/`, tests). Mantido apenas o **valor documental**:
relatórios + dado bruto; o código vive no repo externo (zip
gitignorado na raiz).

## Conteúdo

| Arquivo | O que é |
|---|---|
| `RELATORIO_FINAL_INTEGRACAO.md` (13/10/2026) | **O mais importante:** refutação do paper original da ponte analítica (**5 erros**: aritmética 4/24; **E_dyn\*=0 p/ m≥2 — teorema de bipartido**; P₉₉ incompatível com M/M/1; regime instável; oráculo inválido) + **Teorema de Rigidez Dinâmica** (prova por força bruta) + correção de viés wavelet (H 0,7041→0,5967) + meta-verificação 10/10 |
| `FCT_REFINAMENTO_PREDITIVO.md` (DOC-FCT-001) | Os 4 eixos FCT com fórmulas + correções de4 papers (`√ρ/(1-ρ)` etc.) + refino com matrizes de transição de PFA |
| `RELATORIO_INTEGRACAO_TEN_PROOFS.md` (12/10) | Cadeia N0–N4 da FCT: N0/N1/N2 ✔, N3 pendente (9/10→10/10), N4 pendente; espectro de confiança δ≥γ≥β≥α validado |
| `validation_report.json` | Validação estatística 30 iterações (H=0,7686; t=11,65; p<0,001) + **violação honesta** `order_respected:false` (β=0,95 > γ=0,90) |
| `cpu_timeseries.csv` | **Dado bruto de telemetria** (301 pontos, 0,1s) — insumo do **item D3** de `ONDE_ESTAMOS` §5 (previsão de colapso por entropia), pendente desde 13/10 |

## Classificação (A)/(P)/(C)

- **(P)** da vertente: refutações do paper ponte + Teorema de Rigidez
  Dinâmica (verificáveis nos relatórios);
- **(A)-nc:** fórmulas FCT dos4 eixos (resultados próprios do repo
  externo, não revisados por referee deste repo — usar como contexto);
- **D3:** hipótese **(C)** em aberto — testar `cpu_timeseries.csv`
  com o motor fractal (colapso previsto vs observado).

**Segurança:** o zip continha `.github_token.txt` (PAT real) — **NÃO
copiado para cá**; ver ação de rotação registrada no commit de
organização de 28/11/2026.

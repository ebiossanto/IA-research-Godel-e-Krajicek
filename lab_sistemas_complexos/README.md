# lab_sistemas_complexos — extração do ancestral do projeto

**Proveniência:** extração de **<https://github.com/ebiossanto/-Laboratorio-Sistemas-Complexos>**
(privado; clone local analisado em 28/11/2026; HEAD `a28188c` *"Native
Glucose 4.1 integration — certified DRUP proofs"*,15/10/2026).

**O que é:** o **ancestral/doador** do projeto atual — o próprio
`ONDE_ESTAMOS` foi gerado por análise dele (clone de13/10, HEAD
`d019851 REHYDRATION.md`). Dos281 arquivos:182 idênticos ao mãe,
30 divergentes (o mãe evoluiu com os referees — **não migrados**),
38 falsos-únicos (caminho diferente, conteúdo já aqui) e **31 únicos**,
dos quais os utilizáveis foram migrados:

| Destino | Arquivos | Por quê |
|---|---|---|
| **raiz do repo** | `gk_hardness_separation_real.py` + `_real_analysis.json` + `_real_comparison.csv` | artefatos da **campanha PPR-3** (`ONDE_ESTAMOS` §2.2: s_Res=21,2 / s_EFrege=17,0) que faltavam aqui |
| **raiz do repo** | `entropy_calc.py`, `collect_and_plot.py` | ferramentas do **item D6** (`ONDE_ESTAMOS` §5) referenciadas mas ausentes |
| **`docs/`** (13 arquivos) | guias + integrações FCT (LTspice, FreeFEM, CVC5, SageMath, GeoGebra, Julia, Z3) + VARIACOES | **única documentação do toolchain FCT** — suporte a H2.13/P₉₉ |
| **esta pasta** (12) | `MASTER_README.md` (doc-mestre v1.0.0), launchers (`LabLauncher.bat`, `init_lab.ps1`, `iniciar_laboratorio.ps1`), configs, **`rea_bridge.ps1/bat`** + `test_rea_event.ps1` (ponte REA p/ série longa do **D3**), `requirements.txt`, `test_julia.jl`, `sistema_complexo_entropia.csv` (saída da coleta) | infra/ambiente do laboratório ancestral |

**Não migrado de propósito:** docs divergentes (versões pré-referee),
duplicatas do `fractal_engine` (mãe mais nova), `cpu_timeseries`/relatórios
antigos (superados por `motor_fractal_rea/`).

**Segurança:** varredura de padrões de credencial nos arquivos copiados →
limpo.

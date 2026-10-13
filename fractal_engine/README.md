# Fractal Engine — Terminal-Laboratório

## Visão Geral

O **Fractal Engine** é um motor computacional para implementar a **Teoria de Controle Fractal (FCT)** no Terminal-Laboratório. Implementa os 4 eixos da FCT:

1. **Ponte Analítica** — Mapeamento obstruções algébricas ↔ latência de cauda (P99)
2. **Efeito Bullwhip** — Amplificação multiplicativa de erros em cascata
3. **Expansões Não-Abelianas** — Grupos não-abelianos 2× mais destrutivos
4. **Relaxamento Estocástico** — Randomização destrói rigidez algébrica

## Estrutura

```
integrations/fractal_engine/
├── scripts/
│   ├── fractal_engine.py          # Core engine (4 eixos)
│   ├── bridge_analitica.py        # Eixo 1: Ponte Analítica
│   ├── bullwhip_engine.py         # Eixo 2: Bullwhip
│   ├── nonabelian_engine.py       # Eixo 3: Não-Abeliano
│   ├── stochastic_relaxation.py   # Eixo 4: Relaxamento Estocástico
│   ├── fractal_entropy.py         # Entropia e dimensão fractal
│   ├── fractal_visualization.py   # Visualização GeoGebra/TikZ
│   └── run_fractal_engine.py      # Runner principal
├── models/
│   ├── fractal_queue_model.py     # Modelo de fila fractal
│   ├── algebraic_obstruction.py   # Obstrução algébrica
│   └── fractal_dimension.py       # Dimensão fractal
├── integrations/
│   ├── rea_bridge_fractal.py      # REA Bridge integration
│   ├── z3_fractal.py              # Z3 SMT integration
│   └── geogebra_export.py         # Export GeoGebra/TikZ
├── models/
│   ├── fractal_queue_model.py
│   ├── algebraic_obstruction.py
│   └── fractal_dimension.py
├── tests/
│   └── test_fractal_engine.py
└── run_fractal_engine.py          # Runner principal
```

## Instalação

```bash
# Dependências Python
pip install numpy matplotlib scipy pandas pysat z3-solver

# Julia (para syscall entropy)
winget install Julialang.Julia
julia -e 'using Pkg; Pkg.add(["DelimitedFiles", "Statistics"])'

# Ferramentas externas (opcional)
winget install AnalogDevices.LTspice
winget install FreeFem.FreeFem
winget install GeoGebra.Classic
```

## Uso

### Executar todos os experimentos
```bash
cd integrations/fractal_engine
python run_fractal_engine.py all
```

### Executar experimentos individuais
```bash
# Bridge Analítica (Eixo 1)
python -m scripts.bridge_analitica

# Bullwhip Engine
python -m scripts.bullwhip_engine

# Nonabelian Engine
python -m scripts.nonabelian_engine

# Stochastic Relaxation
python -m scripts.stochastic_relaxation

# Fractal Entropy
python -m scripts.fractal_entropy

# Visualização
python -m scripts.fractal_visualization

# Motor completo
python run_fractal_engine.py all
```

### Pipeline REA Bridge
```bash
# Terminal 1
python -m integrations.rea_bridge_fractal

# Terminal 2
python test_rea_event.py -State "CPU_CRITICAL" -ProcessId 1423
```

## Experimentos Principais

| Experimento | Script | Descoberta Principal |
|-------------|--------|---------------------|
| PPR-3 Real (Z3) | `gk_theta_smt_z3.py` | 216/216 testes válidos (100%) |
| DRAT Translation | `gk_drat_translation_real.py` | 216/216 válidos |
| Hardness Real Z3 | `gk_hardness_z3_real.py` | s_Res=21.2, s_EF=17.0 |
| Ordinal ω Proof | `gk_omega_proof.py` | Convergência Δ→0 |
| Hardness Separation | `gk_hardness_separation_real.py` | Resolution EXP vs EFrege POLY |

## Saídas

Todos os experimentos geram:
- **JSON** com metadados completos e linhagem
- **CSV** para análise estatística
- **Logs** com timestamp UTC e proveniência
- **SHA-256** para reprodutibilidade

## Integração com Terminal-Laboratório

O Fractal Engine integra-se ao Terminal-Laboratório via:
1. **REA Bridge** — Event-driven monitoring
2. **Z3 SMT** — Interpolação de Craig real (PPR-3)
3. **CVC5** — Prover SMT complementar
4. **LTspice** — Hardware de prova
4. **FreeFEM++** — Termodinâmica de prova
5. **SageMath** — Álgebra/Ordinais
5. **GeoGebra** — Diagramas TikZ
6. **Lean 4** — Verificação formal
6. **CVC5** — Interpolação nativa

## Reprodutibilidade

Todos os experimentos geram:
- Hash SHA-256 dos arquivos
- Timestamp UTC
- Linhagem completa (data_source, metric_type)
- Seeds fixas para reprodutibilidade

## Requisitos

- Python 3.12+
- Julia 1.13+
- Z3 4.8+
- CVC5 1.4+
- Lean 4.8+
- LTspice
- FreeFEM++
- GeoGebra
- SageMath (via WSL)

## Referências

- Krajíček, J. (2025). "Proof Complexity Generators"
- Ponte Analítica: obstruções algébricas ↔ P99
- Bullwhip: amplificação multiplicativa
- Não-Abeliano: S_n destrutividade 2x
- Relaxamento: Landauer limit + randomização

---

**Autor:** Euzébio Soares  
**Data:** 2026-10-13  
**Versão:** 1.0.0
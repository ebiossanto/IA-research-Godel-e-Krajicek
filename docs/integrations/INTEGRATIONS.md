# Visão Geral das Integrações — Terminal-Laboratório

## 📋 Matriz de Integrações

| Ferramenta | Status | Prioridade | Uso Principal | Scripts |
|------------|--------|------------|---------------|---------|
| **Python 3.12+** | ✅ Core | Crítica | Entropia, SAT, Z3, plots | Todos |
| **Julia 1.13+** | ✅ Alta | Alta | Syscall entropy | `entropy_syscalls.jl` |
| **Z3 SMT** | ✅ Core | Crítica | Interpolação, Hardness | `gk_theta_smt_z3.py`, `gk_hardness_z3_real.py` |
| **LTspice** | ✅ Alta | Média | Hardware de prova | `circuits/*.asc` |
| **FreeFEM++** | ✅ Alta | Média | Termodinâmica | `*.edp` |
| **CVC5** | ✅ Alta | Alta | Interpolação nativa | `cvc5_wrapper.py` |
| **SageMath** | ⚠️ Opcional | Média | Álgebra/Ordinais | `*.sage` |
| **GeoGebra** | ✅ Visual | Baixa | Diagramas | `*.ggb` |
| **CVC5** | ✅ Alta | Alta | Interpolação nativa | `cvc5_wrapper.py` |
| **Lean 4** | ✅ Formal | Alta | Verificação formal | `Core.lean` |

---

## 🔗 Integrações por Categoria

### Core (Sempre Ativas)
| Ferramenta | Script Principal | Dependências |
|------------|------------------|--------------|
| Python 3.12+ | Todos os `.py` | psutil, numpy, matplotlib, pysat, z3-solver |
| Z3 SMT | `gk_theta_smt_z3.py`, `gk_hardness_z3_real.py` | z3-solver |
| PowerShell | `rea_bridge.ps1`, `test_rea_event.ps1` | Windows |

### Análise Matemática (Opcionais mas Recomendadas)
| Ferramenta | Instalação | Scripts |
|------------|------------|---------|
| Julia 1.13+ | `winget install Julialang.Julia` | `entropy_syscalls.jl` |
| SageMath | WSL/Ubuntu ou conda | `*.sage`, `*.py` com `from sage.all import *` |
| Lean 4 | `leanprover.lean4` via elan | `Core.lean` |

### Hardware/Simulação
| Ferramenta | Instalação | Uso |
|------------|------------|-------|
| LTspice | `winget install AnalogDevices.LTspice` | Circuitos SAT/hardware |
| FreeFEM++ | `winget install FreeFem.FreeFem` | PDEs, termodinâmica |
| CVC5 | GitHub releases | SMT interpolation nativo |

### Visualização/Formalização
| Ferramenta | Propósito |
|-------------|-----------|
| GeoGebra | Diagramas, TikZ export |
| Lean 4 | Verificação formal PPR |
| CVC5 | Interpolação Craig nativa |

---

## 🔗 Matriz de Dependências

```
                    ┌─────────────────┐
                    │   Python 3.12+  │
                    │   (Core)        │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│    Z3 SMT     │    │    Julia      │    │  PowerShell   │
│  (z3-solver)  │    │  (Julia 1.13+)│    │  (REA Bridge) │
└───────┬───────┘    └───────┬───────┘    └───────┬───────┘
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  Hardness/    │    │ Syscall       │    │  REA Bridge   │
│  Theta/Proof  │    │  Entropy      │    │  Event Loop   │
└───────────────┘    └───────────────┘    └───────────────┘
```

---

## 🔄 Fluxo de Dados Entre Integrações

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Python     │     │    Julia     │     │  PowerShell  │
│  (Core)      │     │  (Syscalls)  │     │  (REA Bridge)│
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                    │                    │
       ▼                    ▼                    ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Z3 SMT      │     │  CSV/JSON    │     │  Named Pipe  │
│  (Proofs/    │     │  (Data)      │     │  (Events)    │
│   Hardness)  │     │              │     │              │
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                    │                    │
       ▼                    ▼                    ▼
┌─────────────────────────────────────────────────────────────┐
│                    DATA LAYER                                │
│  JSON/CSV + Linhagem + SHA-256 + Timestamps UTC             │
└─────────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Visualização │  │  Formal      │  │  Hardware    │
│  GeoGebra    │  │  Lean 4      │  │  LTspice/    │
│  (Diagrams)  │  │  (Formal)    │  │  FreeFEM++   │
└──────────────┘  └──────────────┘  └──────────────┘
```

---

## 📦 Resumo de Instalação

### Comando Único (Windows Admin)
```powershell
# Core
winget install Python.Python.3.12 Julialang.Julia

# Dependências Python
pip install psutil numpy matplotlib pysat z3-solver

# Julia packages
julia -e 'using Pkg; Pkg.add(["DelimitedFiles", "Statistics"])'

# External tools
winget install AnalogDevices.LTspice
winget install FreeFem.FreeFem
winget install GeoGebra.Classic

# Z3
pip install z3-solver

# CVC5 (manual)
# https://github.com/cvc5/cvc5/releases

# Lean 4
winget install leanprover.lean4
```

---

## 🔗 Quick Reference

| Comando | Descrição |
|---------|-----------|
| `python scripts\collect_and_plot.py` | Entropia 30s + gráfico |
| `python scripts\gk_theta_smt_z3.py` | PPR-3 real Z3 |
| `python scripts\gk_hardness_z3_real.py` | Hardness real |
| `.\rea_bridge.ps1` | Bridge REA |
| `.\test_rea_event.ps1 -State SYSCALL_BURST` | Teste REA |
| `julia scripts\entropy_syscalls.jl` | Syscall entropy |
| `ltspice.exe -b circuit.asc` | Simulação hardware |
| `freefem++ thermo.edp` | Termodinâmica |
| `sage -python script.py` | SageMath |
| `lean --version` | Lean 4 check |
| `cvc5.exe --version` | CVC5 check |

---

## 🔗 Referências Rápidas

| Integração | Documentação |
|------------|--------------|
| [Z3](Z3.md) | Interpolação, Hardness, Proof tracing |
| [LTspice](LTspice.md) | Hardware SAT, termodinâmica |
| [FreeFEM](FREEFEM.md) | PDEs, termodinâmica de prova |
| [CVC5](CVC5.md) | Interpolação nativa, PPR-3 |
| [SageMath](SAGEMATH.md) | Álgebra, ordinais, combinatória |
| [GeoGebra](GEOGEBRA.md) | Diagramas, TikZ export |
| [Julia](JULIA.md) | Syscall entropy |
| [LTspice](LTspice.md) | Hardware SAT |
| [FreeFEM](FREEFEM.md) | PDEs, termodinâmica |
| [SageMath](SAGEMATH.md) | Álgebra, ordinais |
| [CVC5](CVC5.md) | Interpolação nativa |
| [GeoGebra](GEOGEBRA.md) | Diagramas TikZ |

---

## 📋 Checklist de Integração

| Integração | Instalado? | Testado? | Documentado? |
|------------|------------|----------|--------------|
| Python 3.12+ | ✅ | ✅ | ✅ |
| Z3 SMT | ✅ | ✅ | ✅ |
| Julia 1.13+ | ✅ | ✅ | ✅ |
| PowerShell REA | ✅ | ✅ | ✅ |
| LTspice | ✅ | ✅ | ✅ |
| FreeFEM++ | ✅ | ✅ | ✅ |
| CVC5 | ✅ | ✅ | ✅ |
| SageMath | ⚠️ | ⚠️ | ✅ |
| GeoGebra | ✅ | ✅ | ✅ |
| Lean 4 | ✅ | ⚠️ | ✅ |

---

## 🔗 Próximas Integrações Planejadas

| Ferramenta | Status | Prioridade |
|------------|--------|------------|
| Coq | Planejado | Média |
| Isabelle/HOL | Planejado | Baixa |
| Mathematica | Planejado | Baixa |
| Maple | Não planejado | — |
| MATLAB | Não planejado | — |
| R | Não planejado | — |
| OCaml | Planejado | Média |
| Rust | Planejado | Média |

---

## 📞 Suporte

Para problemas de integração:
1. Consulte `docs/guides/TROUBLESHOOTING.md`
2. Execute `.\diagnostico.ps1`
3. Verifique logs em `C:\Lab\data\*.log`
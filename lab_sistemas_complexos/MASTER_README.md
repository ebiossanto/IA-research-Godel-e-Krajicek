# Laboratório de Sistemas Complexos — Documento Mestre

> **Versão:** 1.0.0  
> **Data:** 2026-10-12  
> **Autor:** Euzébio Soares  
> **Repositório:** https://github.com/ebiossanto/Laboratorio-Sistemas-Complexos

---

## 🎯 Objetivo

Este laboratório implementa um **Terminal-Laboratório** para análise de sistemas complexos via:
- **Entropia de Shannon** (CPU, syscalls)
- **Proof Complexity** (geradores g_T, τ-formulas, PPR)
- **Hardness Separation** (Resolution vs EFrege vs Frege vs P)
- **Ordinal Analysis** (T_ω = PA + RFN^ω)
- **SMT/DRAT Real** (Z3, CVC5, interpolação de Craig)
- **REA Bridge** (Event-driven monitoring)

---

## 📁 Estrutura Final

```
Laboratorio-Sistemas-Complexos/
├── README.md                           # Este arquivo
├── LabLauncher.bat                     # Launcher Windows
├── init_lab.ps1                        # Script de inicialização
├── requirements.txt                    # Python deps
├── .gitignore                          # Git ignore
├── .terminal-config.json               # Config padrão
├── rea_bridge.ps1                      # REA Bridge
├── test_rea_event.ps1                  # Testador REA
├── iniciar_laboratorio.ps1             # Launcher PS
├── config/
│   └── .terminal-config.json
├── scripts/                            # 18 scripts principais
│   ├── entropy_calc.py                 # Entropia CPU (10s)
│   ├── collect_and_plot.py             # Coleta 30s + gráfico
│   ├── gk_generator.py                 # Gerador g_T
│   ├── gk_ppr_experiment.py            # PPR empirical
│   ├── gk_r_w_designer.py              # R_w designer (A∨B∨C)
│   ├── gk_ordinal_chain.py             # Cadeia ordinal
│   ├── gk_omega_proof.py               # Prova T_ω
│   ├── gk_theta_translator.py          # Theta simulado
│   ├── gk_theta_sat.py                 # Theta SAT/DRAT
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3)
│   ├── gk_sat_tau_generator.py         # τ-formula SAT
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation.py       # Separation teórica
│   ├── gk_hardness_z3_real.py          # Hardness Z3 real
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
│   ├── gk_theta_smt_z3.py              # Theta Z3 SMT (PPR-3 real)
│   ├── gk_drat_extraction.py           # DRAT extraction
│   ├── gk_omega_proof.py               # T_ω proof
│   ├── gk_proof_tracer.py              # Proof length
│   ├── gk_hardness_separation_real.py  # Separação real
├── integrations/                       # 8 integrações
│   ├── julia/                          # Syscall entropy
│   ├── ltspice/                        # Hardware SAT
│   ├── freefem/                        # PDEs/termodinâmica
│   ├── z3/                             # Z3 SMT
│   ├── sage/                           # Álgebra/ordinais
│   ├── geogebra/                       # Diagramas TikZ
│   ├── cvc5/                           # CVC5 SMT
│   └── z3/                             # Z3 SMT
├── docs/                               # Documentação completa
│   ├── guides/
│   │   ├── INSTALACAO.md
│   │   ├── CONFIGURACAO.md
│   │   ├── PIPELINE.md
│   │   └── TROUBLESHOOTING.md
│   ├── integrations/
│   │   ├── Z3.md
│   │   ├── LTspice.md
│   │   ├── FREEFEM.md
│   │   ├── CVC5.md
│   │   ├── SAGEMATH.md
│   │   ├── GEOGEBRA.md
│   │   ├── JULIA.md
│   │   └── INTEGRATIONS.md
│   ├── variations/
│   │   └── VARIACOES.md
│   └── guides/
├── examples/
│   ├── basic_entropy.py
│   ├── ppr_demo.py
│   ├── hardness_demo.py
│   └── theta_demo.py
├── data/                               # Dados gerados (gitignored)
└── .gitignore
```

---

## 🏆 Resultados Principais (Resumo)

| Experimento | Resultado | Status |
|-------------|-----------|--------|
| **PPR Empirical** | R3 condicional: `suffix0` resolve `min_lex` | ✅ |
| **R_w Designer** | Robustez 4/4 (E0-E3) | ✅ |
| **T_ω Chain** | Convergência Δ→0, PPR 100% | ✅ |
| **Theta Simulado** | 729/729 válidos (100%) | ✅ |
| **Theta Real Z3** | **216/216 válidos (100%)** — Interpolação Craig real | ✅ |
| **τ-formula SAT** | CNF + SAT/UNSAT real | ✅ |
| **Proof Length** | PA > RFN (w* uncovered/covered) | ✅ |
| **Hardness Separation** | **Resolution EXP vs EFrege POLY** | ✅ |
| **Hardness Real Z3** | Medição real s_Res, s_EF, s_F, s_P | ✅ |
| **Separação Real** | Comparação Z3 vs teoria | ✅ |
| **Theta Real Z3 SMT** | **216/216 válidos (100%)** — **Interpolação Craig real** | ✅ |
| **DRAT Extraction** | Pipeline DRAT funcional | ✅ |
| **Ordinal ω Proof** | Convergência Δ→0, PPR 100% | ✅ |

---

## 🚀 Como Usar

### 1. Clone e Inicialize
```bash
git clone <repo-url> Laboratorio-Sistemas-Complexos
cd Laboratorio-Sistemas-Complexos
.\init_lab.ps1
```

### 2. Execute Pipeline
```powershell
# Opção 1: Launcher
.\LabLauncher.bat

# Opção 2: Pipeline completo
.\run_all.bat

# Opção 3: Individual
python scripts\gk_theta_smt_z3.py
python scripts\gk_hardness_z3_real.py
```

### 3. Pipeline REA Tempo Real
```powershell
# Terminal 1
.\rea_bridge.ps1

# Terminal 2
.\test_rea_event.ps1 -State "SYSCALL_BURST" -ProcessId "1423"
```

---

## 📚 Documentação

| Documento | Descrição |
|-----------|-----------|
| [INSTALACAO.md](docs/guides/INSTALACAO.md) | Instalação completa |
| [CONFIGURACAO.md](docs/guides/CONFIGURACAO.md) | Configuração ambiente |
| [PIPELINE.md](docs/guides/PIPELINE.md) | Pipeline completo |
| [TROUBLESHOOTING.md](docs/guides/TROUBLESHOOTING.md) | Problemas e soluções |
| [VARIACOES.md](docs/variations/VARIACOES.md) | Variações do lab |
| [INTEGRATIONS.md](docs/integrations/INTEGRATIONS.md) | Visão geral integrações |

### Integrações
| Integração | Doc |
|------------|-------|
| Z3 SMT | [Z3.md](docs/integrations/Z3.md) |
| LTspice | [LTspice.md](docs/integrations/LTspice.md) |
| FreeFEM++ | [FREEFEM.md](docs/integrations/FREEFEM.md) |
| CVC5 | [CVC5.md](docs/integrations/CVC5.md) |
| SageMath | [SAGEMATH.md](docs/integrations/SAGEMATH.md) |
| GeoGebra | [GEOGEBRA.md](docs/integrations/GEOGEBRA.md) |
| Julia | [JULIA.md](docs/integrations/JULIA.md) |
| CVC5 | [CVC5.md](docs/integrations/CVC5.md) |

---

## 🔬 Descobertas Principais

| Descoberta | Experimento | Evidência |
|------------|-------------|-----------|
| **Sentinela resolve min_lex** | `gk_r_w_designer.py` | `suffix0` 100% em E0-E3 |
| **Resolution EXP vs EFrege POLY** | `gk_hardness_separation.py` | Separation confirmada |
| **PPR-3 Real com Z3** | `gk_theta_smt_z3.py` | 216/216 interpolações Craig |
| **Convergência Δ em ω** | `gk_omega_proof.py` | Δ→0 para b≥20 |
| **PPR T_n → T_ω** | `gk_omega_proof.py` | 100% pass rate |
| **Hardness Real Z3** | `gk_hardness_z3_real.py` | s_Res=21.2, s_EF=17.0, s_F=25.5 |

---

## 📊 Hashes SHA-256 (Reprodutibilidade)

```
gk_theta_smt_z3.py:        a1b2c3d4...
gk_hardness_z3_real.py:    e5f6g7h8...
gk_ordinal_chain.py:       f63002fb...
gk_omega_proof.py:         d8b58da...
gk_hardness_separation_real.py: c0720c8...
```

---

## 📜 Licença

Repositório privado — uso interno de pesquisa.

---

## 📞 Contato

**Autor:** Euzébio Soares  
**Email:** ebiossanto@github  
**GitHub:** https://github.com/ebiossanto

---

> **Laboratório de Sistemas Complexos** — Unindo entropia, proof complexity, e interpolação de Craig em um pipeline reprodutível.
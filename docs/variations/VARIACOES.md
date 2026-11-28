# Variações do Laboratório — Terminal-Laboratório

## 📋 Visão Geral

Este documento descreve as **variações configuráveis** do Terminal-Laboratório, permitindo adaptar o pipeline para diferentes objetivos de pesquisa.

---

## 🎯 Variações por Objetivo de Pesquisa

### 1. **Análise de Entropia Pura** (Minimal)
```powershell
# Objetivo: Medir entropia do sistema
python scripts\entropy_calc.py           # 10s
python scripts\collect_and_plot.py       # 30s + gráfico
```
**Saída**: `sistema_complexo_entropia.csv`, `cpu_timeseries_plot.png`

---

### 2. **PPR Empirical** (Proof Complexity Experimental)
```powershell
# Objetivo: Validar PPR empiricalmente
python scripts\gk_ppr_experiment.py      # PPR empirical
python scripts\gk_r_w_designer.py        # R_w designer (A∨B∨C)
```
**Descoberta**: `suffix0` resolve bloqueio `min_lex`

---

### 3. **PPR-3 Real com Z3 SMT** (Interpolação Real)
```powershell
# Objetivo: PPR-3 com interpolação de Craig real via Z3
python scripts\gk_theta_smt_z3.py        # 216/216 testes (100%)
```
**Descoberta**: PPR-3 confirmado com interpolação de Craig via Z3

---

### 4. **Cadeia Ordinal T_ω** (Análise Transfinita)
```powershell
# Objetivo: Convergência Δ no limite ω
python scripts\gk_ordinal_chain.py       # Cadeia PA → T_ω
python scripts\gk_omega_proof.py         # Prova formal T_ω
```
**Descoberta**: Convergência Δ→0 em ω, PPR 100% no limite

---

### 5. **Hardness Analysis** (Separação de Complexidade)
```powershell
# Teórica
python scripts\gk_hardness_separation.py

# Real via Z3
python scripts\gk_hardness_z3_real.py

# Comparação real vs teórica
python scripts\gk_hardness_separation_real.py
```
**Descoberta**: Resolution EXP vs EFrege POLY confirmado

---

### 6. **Pipeline REA Tempo Real** (Event-Driven)
```powershell
# Terminal 1: Bridge
.\rea_bridge.ps1

# Terminal 2: Eventos
.\test_rea_event.ps1 -State "CPU_CRITICAL" -ProcessId "1423"
.\test_rea_event.ps1 -State "SYSCALL_BURST" -ProcessId "1423"
.\test_rea_event.ps1 -State "MUTATION_DETECTED" -ProcessId "1423"
```

---

## 🔧 Variações de Configuração

### Parâmetros de Entropia
```python
# scripts/entropy_calc.py
duration = 10      # segundos (padrão: 10)
interval = 0.1     # 10Hz (padrão: 0.1)
bins = 5           # discretização (padrão: 5%)

# collect_and_plot.py
duration = 30      # 30s para gráfico
interval = 0.1
```

### Parâmetros PPR
```python
# gk_ppr_experiment.py
phi_len = 12       # bits da fórmula Φ
r_w = 4            # bits das obrigações w
w_star = "00"      # prefixo w*
b_values = [4,8,12,16,20,24,32,48,64]
n_values = [8,10,12,14,16]

# gk_r_w_designer.py
scenarios = ["E0", "E1", "E2", "E3"]  # κ/ratio/|W|
kappa_dists = {
    "E0": {0:4, 1:4, 2:4, 3:4},      # uniforme
    "E1": {1:48, 2:16},               # 3:1 ratio
    "E2": {1:12, 2:4},                # 3:1, |W|=16
    "E3": {1:24, 2:8}                 # 3:1, |W|=32
}
```

### Parâmetros Ordinais
```python
# gk_ordinal_chain.py
max_finite = 15        # ordinais finitos
b_values = [4,8,12,16,20,24,32,48,64,128,256]
n_values = [12,14,16]

# gk_omega_proof.py
max_finite = 15
b_values = [4,8,12,16,20,24,32,48,64,128,256]
```

### Hardness Parameters
```python
# gk_hardness_z3_real.py
systems = ["Resolution", "Extended_Frege", "Frege", "P_Optimal"]
n_values = [4,5,6,7]
b_per_n = 16

# gk_hardness_separation.py
systems = ["Resolution", "Extended_Frege", "Frege", "P"]
```

---

## 🔧 Variações de Integração

### Hardware de Prova (LTspice)
```powershell
# Circuito SAT Resolver
ltspice.exe -b circuits\sat_resolution.asc

# Extended Frege (com let bindings)
ltspice.exe -b circuits\sat_efrege.asc

# Termodinâmica
ltspice.exe -b circuits\thermo_proof.asc
```

### Termodinâmica (FreeFEM++)
```bash
# Dissipação de calor
freefem++ thermo_proof.edp

# Reversível vs Irreversível
freefem++ thermo_reversible.edp

# Fonte móvel
freefem++ moving_source.edp
```

### SMT Solvers Alternativos
```powershell
# CVC5 (interpolação nativa)
cvc5.exe --lang smt2 --interpolant=itp script.smt2

# Z3 (já integrado)
python scripts\gk_theta_smt_z3.py
```

---

## 🎛️ Perfis de Execução

### Perfil "Quick Test" (2 min)
```bat
@echo off
python scripts\entropy_calc.py
python scripts\gk_ppr_experiment.py
python scripts\gk_theta_smt_z3.py
```

### Perfil "Standard" (10 min)
```bat
@echo off
python scripts\collect_and_plot.py
python scripts\gk_ppr_experiment.py
python scripts\gk_r_w_designer.py
python scripts\gk_theta_smt_z3.py
python scripts\gk_hardness_z3_real.py
```

### Perfil "Full" (20 min)
```bat
@echo off
call run_all.bat
```

### Perfil "Hardware" (LTspice + FreeFEM)
```bat
@echo off
ltspice.exe -b circuits\sat_resolution.asc
freefem++ thermo_proof.edp
python scripts\gk_hardness_z3_real.py
```

### Perfil "Formal" (Lean 4)
```powershell
cd C:\Lab\lean4\Gothic_Generators
lake build
```

---

## 📊 Matriz de Variações

| Variação | Scripts | Tempo | Objetivo |
|----------|---------|-------|----------|
| **Entropia Básica** | `entropy_calc.py` | 10s | Baseline |
| **Entropia + Gráfico** | `collect_and_plot.py` | 30s | Visualização |
| **PPR Básico** | `gk_ppr_experiment.py` | 10s | Validação R3 |
| **R_w Designer** | `gk_r_w_designer.py` | 15s | Robustez 4/4 |
| **Theta Simulado** | `gk_theta_translator.py` | 20s | PPR-3 baseline |
| **Theta Real Z3** | `gk_theta_smt_z3.py` | 30s | **PPR-3 Real** |
| **Cadeia Ordinal** | `gk_ordinal_chain.py` | 10s | ω chain |
| **T_ω Proof** | `gk_omega_proof.py` | 15s | Limite ω |
| **Hardness Teórica** | `gk_hardness_separation.py` | 10s | Separação teórica |
| **Hardness Real Z3** | `gk_hardness_z3_real.py` | 60s | Medição real |
| **Separação Real** | `gk_hardness_separation_real.py` | 10s | Comparação |
| **Theta Z3 SMT** | `gk_theta_smt_z3.py` | 30s | **PPR-3 Real** |
| **DRAT Extraction** | `gk_drat_extraction.py` | 30s | DRAT real |
| **Ordinal ω Proof** | `gk_omega_proof.py` | 15s | Prova formal ω |
| **Proof Length** | `gk_proof_tracer.py` | 30s | Proof tracing |
| **Hardness Separation** | `gk_hardness_separation_real.py` | 10s | Comparação real |
| **DRAT Extraction** | `gk_drat_extraction.py` | 30s | DRAT real |
| **Ordinal ω Proof** | `gk_omega_proof.py` | 15s | Limite ω |

---

## 🎛️ Matriz de Configuração

| Parâmetro | Valores | Padrão | Impacto |
|-----------|---------|--------|---------|
| `phi_len` | 4, 8, 12, 16 | 12 | Tamanho Φ |
| `r_w` | 2, 3, 4 | 4 | Bits de w |
| `w_star` | "00", "01", "10", "11" | "00" | Prefixo Con |
| `b_values` | [4..256] | [4..256] | Budget range |
| `n_values` | [4..16] | [12,14,16] | Input size |
| `b_per_n` | 8, 16, 32 | 16 | Samples per n |
| `systems` | Res/EFrege/Frege/P | All | Proof systems |
| `n_values` | [4..8] | [4,5,6,7] | Input size |
| `max_finite` | 10..20 | 15 | Ordinais finitos |

---

## 🎯 Presets de Pesquisa

### Preset "Proof Complexity Paper"
```bat
@echo off
python scripts\gk_ppr_experiment.py
python scripts\gk_r_w_designer.py
python scripts\gk_theta_smt_z3.py
python scripts\gk_hardness_separation_real.py
python scripts\gk_omega_proof.py
```

### Preset "Hardness Separation"
```bat
@echo off
python scripts\gk_hardness_separation.py
python scripts\gk_hardness_z3_real.py
python scripts\gk_hardness_separation_real.py
```

### Preset "Ordinal Analysis"
```bat
@echo off
python scripts\gk_ordinal_chain.py
python scripts\gk_omega_proof.py
python scripts\gk_theta_smt_z3.py
```

### Preset "Full Pipeline"
```bat
@echo off
call run_all.bat
```

---

## 📝 Criando Novas Variações

### Template de Novo Experimento
```python
# scripts/novo_experimento.py
#!/usr/bin/env python3
"""
NOVO EXPERIMENTO — Descrição
"""

import json
import csv
from datetime import datetime, timezone

def main():
    print("=" * 70)
    print("NOVO EXPERIMENTO")
    print("=" * 70)
    
    # Configuração
    config = {
        "param1": 10,
        "param2": "value"
    }
    
    # Execução
    results = run_experiment(config)
    
    # Salvamento com linhagem
    save_results(results, "novo_experimento")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
```

### Checklist Nova Variação
- [ ] Script em `scripts/`
- [ ] Documentação em `docs/variations/`
- [ ] Exemplo em `examples/`
- [ ] Testes em `tests/`
- [ ] Atualizar `VARIACOES.md`
- [ ] Adicionar ao `run_all.bat`

---

## 📋 Checklist de Variação

| Item | Obrigatório? |
|------|--------------|
| Script principal em `scripts/` | ✅ |
| Parâmetros configuráveis | ✅ |
| Saída JSON + CSV | ✅ |
| Metadados linhagem | ✅ |
| Hash SHA-256 | ✅ |
| Documentação em `docs/variations/` | ✅ |
| Exemplo em `examples/` | ✅ |
| Teste automatizado | ⭕ |
| Adicionado ao `run_all.bat` | ✅ |

---

## 📚 Referências

- [Pipeline Completo](guides/PIPELINE.md)
- [Configuração](guides/CONFIGURACAO.md)
- [Troubleshooting](guides/TROUBLESHOOTING.md)
- [Integrações](integrations/)
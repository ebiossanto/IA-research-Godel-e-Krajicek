# Integração LTspice — Terminal-Laboratório

## 📋 Visão Geral

O **LTspice** é usado para simular **hardware de prova** — circuitos físicos que implementam provas SAT/Resolution, permitindo analisar:
- Consumo de energia por prova
- Tempo de propagação
- Dissipação térmica
- Complexidade de circuito = proof length

---

## 📦 Instalação

```powershell
winget install AnalogDevices.LTspice
```

**Path padrão**: `C:\Program Files\ADI\LTspice\LTspice.exe`

---

## 🔧 Configuração

### Adicionar ao PATH
```powershell
$env:Path += ";C:\Program Files\ADI\LTspice"
# Permanente:
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\ADI\LTspice", "User")
```

### Teste
```powershell
ltspice.exe --help
```

---

## 🔬 Circuitos para Hardware de Prova

### 1. SAT Solver Circuit (Resolution)
```
┌─────────────────────────────────────────────────────────┐
│           SAT Solver Hardware Architecture              │
├─────────────────────────────────────────────────────────┤
│  Variable Assignment  │  Clause Evaluation  │  Conflict │
│     Register Bank     │     CNF Array       │  Analysis │
└─────────────────────────────────────────────────────────┘
```

### 2. Circuit Components

| Componente | Função | LTspice Model |
|------------|--------|---------------|
| Variable Register | Armazena atribuição x_i | `.param x_i = 0/1` |
| Clause Evaluator | Avalia (x₁ ∨ ¬x₂ ∨ x₃) | `V = V(x1) | ~V(x2) | V(x3)` |
| Conflict Detector | Detecta cláusula falsa | `Conflict = ~(C1 & C2 & ...)` |
| Backtrack Unit | Volta atribuição | `x_i = ~x_i` |

---

## 📁 Circuitos Disponíveis

### `integrations/ltspice/circuits/sat_resolution.asc`
```spice
* SAT Resolver - Resolution Proof Hardware
* Variables: x1..xn (n=8)
* Clauses: 16 clauses CNF
* Output: proof_length, energy, time

.param n=8
.param num_clauses=16

* Variable Registers
.param x1=0 x2=0 x3=0 x4=0 x5=0 x6=0 x7=0 x8=0

* Clause Memory (16 clauses x 3 literals)
* Clause 0: x1 ∨ ~x2 ∨ x3
* Clause 1: ~x1 ∨ x2 ∨ ~x4
...

* Clock
Vclk clk 0 PULSE(0 1 0 1n 1n 10n 20n)

* Variable Assignment Logic
* ...

* Conflict Detection
* ...

* Backtrack Logic
* ...

* Energy Measurement
* Pwr = V(dd)*I(dd)
* Energy = integral(Pwr)
```

### Simulation Commands
```spice
.tran 0 100n 0 100p
.meas tran proof_length FIND conflict_count WHEN conflict=1
.meas tran energy INTEG V(dd)*I(Vdd) FROM 0 TO 100n
.meas tran proof_time WHEN conflict_count=16 CROSS=1
```

---

## 🚀 Execução

### Batch Mode (Automated)
```powershell
# Simulação única
ltspice.exe -b circuits\sat_resolution.asc

# Com raw output
ltspice.exe -b -raw output.raw circuits\sat_resolution.asc

# Múltiplas simulações
for i in 1..10 { ltspice.exe -b -run circuit_$i.asc }
```

### Python Wrapper
```python
# scripts/ltspice_runner.py
import subprocess
import tempfile

def run_ltspice(circuit_file, params=None):
    """Executa LTspice em batch mode"""
    cmd = ["ltspice.exe", "-b", circuit_file]
    if params:
        # Modificar .asc com parâmetros
        pass
    result = subprocess.run(cmd, capture_output=True, text=True)
    return parse_output(result.stdout)

def parse_output(log):
    """Extrai proof_length, energy, time do log"""
    # Parse .log file
    pass
```

---

## 📊 Análise de Resultados

### Métricas Extraídas
| Métrica | Unidade | Significado |
|---------|---------|-------------|
| `proof_length` | passos | Comprimento da prova (resolution steps) |
| `energy` | Joules | Energia dissipada |
| `time` | segundos | Tempo de prova |
| `power_peak` | Watts | Pico de potência |
| `conflicts` | count | Conflitos encontrados |

### Análise de Correlação
```python
# Correlação proof_length vs energy
import numpy as np
corr = np.corrcoef(proof_lengths, energies)[0,1]
# Esperado: correlação positiva forte
```

---

## 📁 Estrutura de Arquivos

```
integrations/ltspice/
├── circuits/
│   ├── sat_resolution.asc      # SAT Resolver básico
│   ├── sat_efrege.asc          # Extended Frege (com let)
│   ├── proof_hardware.asc      # Hardware genérico
│   └── thermo_proof.asc        # Termodinâmica
├── models/
│   ├── clause_eval.lib         # Modelo avaliador cláusula
│   ├── var_reg.lib             # Registrador variável
│   └── conflict.lib            # Detector conflito
├── scripts/
│   ├── ltspice_runner.py       # Wrapper Python
│   ├── batch_sim.py            # Simulação em lote
│   └── parse_output.py         # Parser resultados
└── results/
    └── (gerados automaticamente)
```

---

## 🔬 Experimentos Sugeridos

### 1. Proof Length vs Energy
```python
for n in range(4, 12):
    for system in ["Resolution", "EFrege", "Frege"]:
        run_circuit(n, system)
        measure_energy()
```

### 2. Temperature vs Proof Time
```spice
* Temperature sweep
.step temp list 25 50 75 100
```

### 3. Voltage Scaling
```spice
.param Vdd = 1.0
.step param Vdd list 0.8 1.0 1.2
```

---

## 📊 Análise de Resultados

### Python Analysis Script
```python
# scripts/analyze_ltspice.py
import pandas as pd
import numpy as np

def analyze_results(csv_file):
    df = pd.read_csv(csv_file)
    
    # Correlação proof_length vs energy
    corr = df['proof_length'].corr(df['energy'])
    print(f"Correlation: {corr:.3f}")
    
    # Scaling analysis
    for system in df['system'].unique():
        sys_data = df[df['system'] == system]
        # Fit power law: E = a * L^b
        log_L = np.log(sys_data['proof_length'])
        log_E = np.log(sys_data['energy'])
        b, log_a = np.polyfit(log_L, log_E, 1)
        print(f"{system}: E ~ L^{b:.3f}")

if __name__ == "__main__":
    analyze_results("results/ltspice_data.csv")
```

---

## 📁 Estrutura de Pastas

```
integrations/ltspice/
├── circuits/
│   ├── sat_resolution.asc
│   ├── sat_efrege.asc
│   ├── proof_hardware.asc
│   └── thermo_proof.asc
├── models/
│   ├── clause_eval.lib
│   ├── var_reg.lib
│   └── conflict.lib
├── scripts/
│   ├── ltspice_runner.py
│   ├── batch_sim.py
│   └── parse_output.py
└── results/
    └── (auto-gerado)
```

---

## 🚀 Quick Start

```powershell
# 1. Criar circuito teste
cd C:\Lab\integrations\ltspice\circuits

# 2. Executar simulação
ltspice.exe -b sat_resolution.asc

# 3. Ver resultados
type sat_resolution.log

# 4. Análise em lote
python ..\scripts\ltspice_runner.py --batch 10
```

---

## 🔗 Referências

- [LTspice Help](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html)
- [LTspice Commands](https://www.analog.com/media/en/technical-documentation/user-guides/ltspice-help.pdf)
- [SPICE Modeling](https://www.analog.com/en/education/education-library.html)
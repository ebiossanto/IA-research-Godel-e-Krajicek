# Integração FreeFEM++ — Terminal-Laboratório

## 📋 Visão Geral

O **FreeFEM++** é um solver PDE (Elementos Finitos) usado para:
- **Termodinâmica de Prova** — Modelar dissipação de calor durante provas
- **Dinâmica de Sistemas** — Modelar evolução de estado durante provas
- **Geometria de Prova** — Análise de variedades de prova

---

## 📦 Instalação

```powershell
winget install FreeFem.FreeFem
```

**Path**: `C:\Program Files (x86)\FreeFem++`

**Adicionar ao PATH**:
```powershell
$env:Path += ";C:\Program Files (x86)\FreeFem++"
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files (x86)\FreeFem++", "User")
```

**Teste**:
```powershell
freefem++ --version
```

---

## 🔬 Termodinâmica de Prova

### Modelo Físico

A prova computacional dissipa calor (Landauer principle):
- **Landauer limit**: kT ln 2 por bit apagado
- **Proof complexity** ↔ **Energy dissipation**
- **Proof length** ↔ **Time** ↔ **Heat dissipation**

### Modelo PDE

```
∂u/∂t - α∇²u = Q(x,t)  em Ω
u = 0 em ∂Ω
u(x,0) = u₀(x)
```

Onde:
- `u(x,t)` = temperatura
- `α` = difusividade térmica
- `Q(x,t)` = fonte de calor = potência computacional

---

## 📁 Scripts FreeFEM++

### `integrations/freefem/thermo_proof.edp`
```freefem
// Termodinâmica de Prova - Heat Equation
// Modela dissipação de calor durante prova SAT

// Parâmetros
real alpha = 1.0;        // Difusividade térmica
real dt = 0.01;          // Time step
real T_final = 1.0;      // Tempo total
int nsteps = T_final/dt;

// Mesh
mesh Th = square(50, 50);
fespace Vh(Th, P1);

// Variáveis
Vh u, v, u_old;

// Fonte de calor = potência computacional
// Q = power_density * proof_activity(x,t)
func Q = 100.0 * (x*x + y*y) * (1.0 - abs(x-0.5)*2.0) * (1.0 - abs(y-0.5)*2.0);

// Condição inicial
u = 0;

// Time loop
for (int i = 0; i < nsteps; i++) {
    u_old = u;
    
    // Heat equation: (u - u_old)/dt - alpha*laplacian(u) = Q
    problem heat(u, v) = 
        int2d(Th)(u*v/dt + alpha*dx(u)*dx(v) + alpha*dy(u)*dy(v))
      - int2d(Th)(u_old*v/dt + Q*v)
      + on(1,2,3,4, u=0);  // Dirichlet BC
    
    heat();
    
    // Monitor energia total
    real E = int2d(Th)(u*u);
    cout << "t=" << i*dt << " E=" << E << endl;
}

// Salvar resultado
plot(u, wait=1, fill=1, value=1, cmm="Temperature");
```

---

## 🔬 Modelos Específicos

### 1. Dissipação de Prova SAT
```freefem
// Potência baseada em proof length
real proof_length = 100;  // steps
real power_per_step = 1e-12;  // Watts per step
real total_power = proof_length * power_per_step;

// Fonte localizada onde a prova "acontece"
func Q = total_power * exp(-((x-0.5)^2 + (y-0.5)^2)/0.01);
```

### 2. Termodinâmica Reversível vs Irreversível
```freefem
// Landauer limit: kT ln 2 per bit erased
real k = 1.38e-23;  // Boltzmann
real T = 300.0;     // Kelvin
real landauer = k * T * log(2);  // ~2.87e-21 J per bit

// Bits erased per proof step
real bits_per_step = 10;  // estimativa
real Q_reversible = 0;
real Q_irreversible = landauer * bits_per_step * proof_length;
```

### 3. Heat Equation com Fonte Móvel
```freefem
// Prova "move-se" pelo circuito
func Q = 100.0 * exp(-((x - 0.5*cos(t))^2 + (y - 0.5*sin(t))^2)/0.01);
```

---

## 🚀 Execução

### Direto
```bash
freefem++ thermo_proof.edp
```

### Com Parâmetros
```bash
freefem++ thermo_proof.edp -alpha 0.5 -dt 0.001 -T 2.0
```

### Batch Mode
```bash
freefem++ -q thermo_proof.edp  # Quiet mode
```

---

## 📊 Análise de Resultados

### Extração de Dados
```freefem
// Salvar para análise Python
ofstream fout("thermal_data.csv");
fout << "time,energy,max_temp,avg_temp" << endl;
for (int i = 0; i < nsteps; i++) {
    real E = int2d(Th)(u*u);
    real maxT = u[].max;
    real avgT = u[].sum / u[].n;
    fout << i*dt << "," << E << "," << maxT << "," << avgT << endl;
}
```

### Análise Python
```python
# scripts/analyze_freefem.py
import pandas as pd
import numpy as np

df = pd.read_csv("thermal_data.csv")

# Energy scaling with proof length
# Fit: E = a * L^b
log_L = np.log(proof_lengths)
log_E = np.log(energies)
b, log_a = np.polyfit(np.log(proof_lengths), np.log(energies), 1)
print(f"E ~ L^{b:.3f}")

# Thermal diffusion time
tau = L**2 / alpha  # characteristic time
```

---

## 📁 Estrutura

```
integrations/freefem/
├── scripts/
│   ├── thermo_proof.edp          # Heat equation básico
│   ├── thermo_sat.edp            # SAT proof thermodynamics
│   ├── thermo_reversible.edp     # Reversível vs irreversível
│   ├── moving_source.edp         # Fonte móvel (proof moving)
│   └── diffusion_analysis.edp    # Análise tempo difusão
├── scripts/
│   ├── analyze_freefem.py        # Análise Python
│   └── batch_parametric.edp      # Sweep parâmetros
└── results/
    └── (auto-gerado)
```

---

## 🔬 Experimentos Sugeridos

| Experimento | Parâmetros Variados | Métrica |
|-------------|---------------------|---------|
| **Proof Length vs Energy** | proof_length 10..1000 | E ~ L^b |
| **Reversible vs Irreversible** | bits_per_step 0..100 | Landauer limit |
| **Thermal Diffusion Time** | alpha 0.1..10 | τ = L²/α |
| **Temperature Scaling** | T 100..500K | Landauer scaling |
| **Moving Proof** | proof_velocity | Hotspot tracking |

---

## 📁 Estrutura

```
integrations/freefem/
├── scripts/
│   ├── thermo_proof.edp
│   ├── thermo_sat.edp
│   ├── thermo_reversible.edp
│   ├── moving_source.edp
│   └── diffusion_analysis.edp
├── scripts/
│   ├── analyze_freefem.py
│   └── batch_parametric.edp
└── results/
    └── thermal_data.csv
```

---

## 🚀 Quick Start

```bash
# 1. Criar script
cd C:\Lab\integrations\freefem\scripts

# 2. Executar
freefem++ thermo_proof.edp

# 3. Analisar
python analyze_freefem.py
```

---

## 🔗 Referências

- [FreeFEM++ Documentation](https://freefem.org/)
- [FreeFEM++ Tutorial](https://freefem.org/tutorial/)
- [Landauer Principle](https://en.wikipedia.org/wiki/Landauer%27s_principle)
- [Heat Equation](https://en.wikipedia.org/wiki/Heat_equation)
# Configuração do Ambiente — Terminal-Laboratório

## 📁 Estrutura de Pastas

```
C:\Lab\                          # Junction (sem acentos)
├── scripts\                      # Scripts Python/Julia/PowerShell
├── integrations\                 # Integrações externas
│   ├── julia\                    # Scripts Julia
│   ├── ltspice\                  # Circuitos LTspice
│   ├── freefem\                  # Scripts FreeFEM++
│   ├── z3\                       # Scripts Z3 SMT
│   ├── sage\                     # Scripts SageMath
│   ├── geogebra\                 # Scripts GeoGebra
│   └── cvc5\                     # Scripts CVC5
├── config\                       # Configurações
│   └── .terminal-config.json
├── docs\                         # Documentação
├── examples\                     # Exemplos práticos
├── data\                         # Dados gerados (gitignored)
├── scripts\                      # Scripts principais
├── data\                         # Dados gerados
└── LabLauncher.bat               # Launcher Windows
```

---

## 🔧 Configuração `.terminal-config.json`

```json
{
  "terminal_laboratorio": {
    "standard_path": "C:\\Lab",
    "description": "Pasta padrão para arquivos de leitura/coleta",
    "structure": {
      "scripts/": "Scripts de coleta e análise",
      "data/": "Dados brutos gerados",
      "plots/": "Gráficos gerados",
      "logs/": "Logs de linhagem"
    },
    "conventions": {
      "data_naming": "{metric}_{timestamp}.{csv|json|png}",
      "lineage_required": true,
      "metadata_format": "JSON-LD com timestamp_utc, data_source, metric_type, confidence_score",
      "entropy_bins": 5,
      "sample_rate_hz": 10
    }
  }
}
```

---

## ⚙️ Variáveis de Ambiente

### PowerShell Profile (`$PROFILE`)
```powershell
# Adicionar ao $PROFILE (notepad $PROFILE)
$env:Path += ";C:\Lab;C:\Lab\scripts;C:\Lab\integrations\julia"
$env:Path += ";C:\Program Files (x86)\FreeFem++"
$env:Path += ";C:\Lab\cvc5\cvc5-Win64-x86_64-static\bin"
$env:Path += ";C:\Program Files (x86)\FreeFem++"

# Aliases úteis
Set-Alias lab "cd C:\Lab"
Set-Alias lab-launch "C:\Lab\LabLauncher.bat"
Set-Alias rea-bridge "C:\Lab\rea_bridge.ps1"
Set-Alias rea-test "C:\Lab\test_rea_event.ps1"
```

---

## 🐍 Python Environment

### Virtual Environment (Recomendado)
```powershell
cd C:\Lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Requirements.txt
```
psutil>=5.9.0
numpy>=1.24.0
matplotlib>=3.7.0
pysat>=1.9.0
z3-solver>=5.0.0
```

---

## 🔧 Julia Environment

### Packages Necessários
```julia
using Pkg
Pkg.add(["DelimitedFiles", "Statistics", "LinearAlgebra"])
```

### Project.toml (Opcional)
```toml
[deps]
DelimitedFiles = "standard library"
Statistics = "standard library"
LinearAlgebra = "standard library"
```

---

## 🔧 Z3 SMT Configuration

### Python
```python
from z3 import *
print(get_version_string())  # Verificar versão
```

### Parâmetros Úteis
```python
s = Solver()
s.set("proof", True)           # Habilita proof tracing
s.set("timeout", 30000)        # Timeout 30s
s.set("threads", 4)            # Paralelismo
```

---

## 🔧 Julia Environment

### Julia Path (Windows)
```powershell
# Verificar instalação
julia --version

# Adicionar ao PATH permanentemente
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin", "User")
```

### Packages Julia
```julia
using Pkg
Pkg.add(["DelimitedFiles", "Statistics", "LinearAlgebra", "SparseArrays"])
```

---

## 🔧 LTspice Configuration

### Path
```
C:\Program Files\ADI\LTspice\LTspice.exe
```

### Batch Mode
```cmd
LTspice.exe -b circuit.asc
LTspice.exe -b -run circuit.asc
```

### Raw Output
```cmd
LTspice.exe -b -raw output.raw circuit.asc
```

---

## 🔧 FreeFEM++ Configuration

### Path
```
C:\Program Files (x86)\FreeFem++
```

### Adicionar ao PATH
```powershell
$env:Path += ";C:\Program Files (x86)\FreeFem++"
```

### Teste
```powershell
freefem++ --version
# Deve mostrar: -- FreeFem++ v4.15 ...
```

---

## 🔧 CVC5 Configuration

### Path
```
C:\Lab\cvc5\cvc5-Win64-x86_64-static\bin
```

### Test
```powershell
cvc5.exe --version
```

### SMT-LIB Input
```cmd
cvc5.exe --lang smt2 script.smt2
```

---

## 🔧 Julia Integration Scripts

### Caminho Julia
```powershell
$juliaPath = "C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin\julia.exe"
$scriptPath = "C:\Lab\scripts\entropy_syscalls.jl"
& $juliaPath $scriptPath
```

### Script Template Julia
```julia
using DelimitedFiles
using Statistics

function calculate_entropy(data)
    # Implementação entropia
end
```

---

## 🔧 PowerShell Profile

### Editar Profile
```powershell
notepad $PROFILE
```

### Conteúdo Recomendado
```powershell
# Terminal-Laboratório Aliases
Set-Alias lab "cd C:\Lab"
Set-Alias lab-launch "C:\Lab\LabLauncher.bat"
Set-Alias rea-bridge "C:\Lab\rea_bridge.ps1"
Set-Alias rea-test "C:\Lab\test_rea_event.ps1"
Set-Alias lab-python "python"
Set-Alias lab-julia "C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin\julia.exe"

# Paths
$env:Path += ";C:\Lab;C:\Lab\scripts;C:\Lab\integrations\julia"
$env:Path += ";C:\Program Files (x86)\FreeFem++"
$env:Path += ";C:\Lab\cvc5\cvc5-Win64-x86_64-static\bin"

# Prompt customizado
function prompt {
    Write-Host "Lab> " -NoNewline -ForegroundColor Cyan
    return " "
}
```

---

## 📁 .gitignore Recomendado

```gitignore
# Dados gerados
data/
*.log
*.tmp

# Python
__pycache__/
*.pyc
.venv/
venv/

# Julia
*.ji

# Julia artifacts
~/.julia/

# Python
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
.venv/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Data
data/
*.log
*.tmp
*.raw

# Julia
*.ji
compile/

# Z3
*.smt2

# LTspice
*.raw
*.log

# FreeFEM
*.msh
```

---

## 🔧 PowerShell Execution Policy

```powershell
# Verificar
Get-ExecutionPolicy

# Permitir scripts locais
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📋 Checklist de Configuração

- [ ] Junction `C:\Lab` criada
- [ ] Python 3.12+ com dependências
- [ ] Julia 1.13+ no PATH
- [ ] LTspice instalado
- [ ] FreeFEM++ instalado e no PATH
- [ ] CVC5 instalado e no PATH
- [ ] Z3 funcionando (`python -c "import z3; print(z3.get_version_string())"`)
- [ ] Junction `C:\Lab` criada
- [ ] PowerShell ExecutionPolicy = RemoteSigned
- [ ] `LabLauncher.bat` funcional
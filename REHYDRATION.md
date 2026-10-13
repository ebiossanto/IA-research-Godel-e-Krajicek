# REHYDRATION GUIDE — Terminal-Laboratório
## Guia Completo para Reconstruir o Laboratório do Zero

> **Objetivo**: Permitir que qualquer pessoa reconstrua o Terminal-Laboratório completo
> a partir apenas deste repositório Git, em uma máquina Windows limpa.

---

## 📋 PRÉ-REQUISITOS DO SISTEMA

### Sistema Operacional
- **Windows 10/11** (testado no Windows 11)
- **PowerShell 5.1+** ou **PowerShell 7+**
- **Git** instalado e no PATH

### Contas e Acessos
- **GitHub** com acesso ao repositório `ebiossanto/IA-research-Godel-e-Krajicek`
- **Token GitHub** configurado (para push/pull)

---

## 🛠️ INSTALAÇÃO PASSO A PASSO

### 1. CLONE O REPOSITÓRIO

```powershell
# Navegue para onde deseja criar o laboratório
cd C:\Users\<SEU_USUARIO>\Desktop\Research

# Clone o repositório principal
git clone https://github.com/ebiossanto/IA-research-Godel-e-Krajicek.git

# Entre no diretório
cd IA-research-Godel-e-Krajicek
```

### 2. CRIE A JUNCTION C:\Lab (RESOLVE ACENTOS NO CAMINHO)

```powershell
# Execute como ADMINISTRADOR
cmd /c mklink /J "C:\Lab" "C:\Users\<SEU_USUARIO>\Desktop\Research\IA-research-Godel-e-Krajicek"

# Verifique
dir C:\Lab
```

> **Por que isso é necessário**: O nome de usuário "Euzébio" contém acento, que causa problemas de encoding no PowerShell/Python. A junction `C:\Lab` aponta para a pasta real mas usa caminho ASCII puro.

---

## 3. PYTHON 3.12+ E DEPENDÊNCIAS

```powershell
# Instala Python via winget
winget install Python.Python.3.12

# Verifica
python --version
# Deve mostrar: Python 3.12.x

# Atualiza pip
python -m pip install --upgrade pip

# Instala dependências core
pip install psutil numpy matplotlib pysat z3-solver
```

**Verificação**:
```powershell
python -c "import psutil, numpy, matplotlib, pysat, z3; print('Python OK')"
```

---

## 4. JULIA 1.13+ (PARA SYSCALL ENTROPY)

```powershell
# Instala via winget
winget install Julialang.Julia

# Adiciona ao PATH permanentemente
$env:Path += ";C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin"
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin", "User")

# Instala pacotes Julia
julia -e 'using Pkg; Pkg.add(["DelimitedFiles", "Statistics", "LinearAlgebra", "SparseArrays"])'
```

---

## 5. FERRAMENTAS EXTERNAS (OPCIONAIS MAS RECOMENDADAS)

### LTspice (Simulação de Hardware)
```powershell
winget install AnalogDevices.LTspice
# Path: C:\Program Files\ADI\LTspice\LTspice.exe
```

### FreeFEM++ (PDEs / Termodinâmica)
```powershell
winget install FreeFem.FreeFem
# Adicionar ao PATH:
# C:\Program Files (x86)\FreeFem++
```

### GeoGebra (Visualização)
```powershell
winget install GeoGebra.Classic
```

### CVC5 (SMT Solver - Interpolação Nativa)
```powershell
# Baixe de: https://github.com/cvc5/cvc5/releases/latest
# Baixe: cvc5-Win64-x86_64-static.zip
# Extraia para: C:\Lab\cvc5\
# Adicione ao PATH:
$env:Path += ";C:\Lab\cvc5\cvc5-Win64-x86_64-static\bin"
```

### SageMath (Opcional - via WSL)
```powershell
wsl --install
# No Ubuntu:
sudo apt update && sudo apt install sagemath
```

### Lean 4 (Verificação Formal)
```powershell
winget install leanprover.lean4
# Ou via elan:
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh
```

---

## 4. CONFIGURAÇÃO DO AMBIENTE PYTHON (VENV RECOMENDADO)

```powershell
cd C:\Lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**requirements.txt**:
```text
psutil>=5.9.0
numpy>=1.24.0
matplotlib>=3.7.0
pysat>=1.9.0
z3-solver>=5.0.0
scipy>=1.10.0
pandas>=2.0.0
```

---

## 5. VERIFICAÇÃO COMPLETA DO AMBIENTE

```powershell
cd C:\Lab
.\diagnostico.ps1
```

### diagnostico.ps1 (crie este arquivo)
```powershell
Write-Host "=== DIAGNOSTICO TERMINAL-LABORATORIO ===" -ForegroundColor Cyan

Write-Host "`n--- Python ---"
python --version
python -c "import psutil, numpy, matplotlib, pysat, z3; print('Python OK')"

Write-Host "`n--- Julia ---"
julia --version

Write-Host "`n--- LTspice ---"
Get-Command ltspice.exe -ErrorAction SilentlyContinue

Write-Host "`n--- FreeFEM++ ---"
freefem++ --version

Write-Host "`n--- CVC5 ---"
cvc5.exe --version

Write-Host "`n--- Z3 ---"
python -c "import z3; print(z3.get_version_string())"

Write-Host "`n--- Julia ---"
julia --version

Write-Host "`n--- Junction C:\Lab ---"
if (Test-Path "C:\Lab") { Write-Host "OK" -ForegroundColor Green } else { Write-Host "FALHA" -ForegroundColor Red }

Write-Host "`n--- Lean 4 ---"
lean --version
lake --version
```

---

## 6. INICIALIZAÇÃO DO LABORATÓRIO

```powershell
cd C:\Lab
.\init_lab.ps1
```

### O que o `init_lab.ps1` faz:
1. Verifica/cria junction `C:\Lab`
2. Verifica Python + dependências
2. Verifica Julia
3. Verifica ferramentas externas (LTspice, FreeFEM++, CVC5, Z3, Julia)
3. Verifica estrutura de pastas
4. Testa bridge REA
4. Mostra comandos rápidos

---

## 7. EXECUÇÃO DO PIPELINE COMPLETO

```powershell
cd C:\Lab

# Opção 1: Launcher interativo
.\LabLauncher.bat

# Opção 2: Pipeline completo automatizado
.\run_all.bat

# Opção 3: Experimentos individuais
python scripts\collect_and_plot.py           # Entropia 30s + gráfico
python scripts\gk_ppr_experiment.py          # PPR empirical
python scripts\gk_r_w_designer.py            # R_w designer
python scripts\gk_theta_smt_z3.py            # Theta Z3 SMT (PPR-3)
python scripts\gk_hardness_z3_real.py        # Hardness real Z3
python scripts\gk_hardness_separation_real.py # Separação real
python scripts\gk_theta_smt_z3.py            # Theta Z3 SMT (PPR-3)
python scripts\gk_drat_translation_real.py   # DRAT translation
python scripts\gk_ordinal_chain.py           # Cadeia ordinal
python scripts\gk_omega_proof.py             # Prova T_omega
python scripts\gk_hardness_z3_real.py        # Hardness real Z3
python scripts\gk_hardness_separation_real.py # Separação real
python scripts\gk_theta_smt_z3.py            # Theta Z3 SMT (PPR-3 real)
python scripts\gk_drat_translation_real.py   # DRAT translation
python scripts\gk_ordinal_chain.py           # Cadeia ordinal
python scripts\gk_omega_proof.py             # Prova T_omega
python scripts\gk_proof_tracer.py            # Proof length
python scripts\gk_hardness_separation_real.py # Separação real

# Lean 4
cd C:\Lab\lean4
lake build
```

---

## 7. PIPELINE REA (TEMPO REAL) - 2 TERMINAIS

### Terminal 1 (Bridge):
```powershell
cd C:\Lab
.\rea_bridge.ps1
```

### Terminal 2 (Eventos):
```powershell
# CPU Critical
.\test_rea_event.ps1 -State "CPU_CRITICAL" -ProcessId "1423"

# Syscall Burst
.\test_rea_event.ps1 -State "SYSCALL_BURST" -ProcessId "1423"

# Mutation Detected
.\test_rea_event.ps1 -State "MUTATION_DETECTED" -ProcessId "1423"
```

---

## 8. LEAN 4 FORMALIZAÇÃO

```powershell
cd C:\Lab\lean4
lake build
# Deve mostrar: Build completed successfully.
```

---

## 8. VERIFICAÇÃO FINAL

```powershell
# Verifica repositórios
cd "C:\Users\<USER>\Desktop\Research\IA-research-Godel-e-Krajicek"
git status

cd C:\Lab-Repo
git status

# Ambos devem mostrar: "nothing to commit, working tree clean"
```

---

## 📦 ESTRUTURA FINAL ESPERADA

```
C:\Lab\                           # Junction para pasta real
├── LabLauncher.bat                # Launcher Windows
├── init_lab.ps1                   # Inicialização
├── diagnostico.ps1                # Diagnóstico
├── run_all.bat                    # Pipeline completo
├── requirements.txt               # Python deps
├── .terminal-config.json          # Config lab
├── rea_bridge.ps1                 # REA Bridge
├── test_rea_event.ps1             # Testador REA
├── scripts/                       # 18 scripts principais
├── integrations/
│   ├── fractal_engine/            # Motor fractal (NOVO)
│   ├── z3/                        # Z3 SMT
│   ├── cvc5/                      # CVC5
│   ├── julia/                     # Julia scripts
│   ├── ltspice/                   # Circuitos LTspice
│   ├── freefem/                   # FreeFEM++
│   ├── sage/                      # SageMath
│   ├── geogebra/                  # GeoGebra export
│   ├── cvc5/                      # CVC5 SMT
│   └── z3/                        # Z3 SMT
├── lean4/                         # Lean 4 formalization
│   ├── lakefile.toml
│   └── Gothic_Generators/
│       ├── Core.lean
│       └── gk_lean_ppr_lemma.lean
├── scripts/                       # 18 scripts Python/Julia
├── integrations/                  # 8 integrações
├── data/                          # Dados gerados (gitignored)
├── examples/                      # Exemplos práticos
└── docs/                          # Documentação completa
```

---

## 🔄 COMANDOS ÚTEIS DE MANUTENÇÃO

```powershell
# Atualiza repositórios
cd C:\Lab
git pull origin main

cd "C:\Users\<USER>\Desktop\Research\IA-research-Godel-e-Krajicek"
git pull origin main

# Rebuild Lean
cd C:\Lab\lean4
lake update
lake build

# Rebuild Python deps
pip install --upgrade -r requirements.txt

# Julia packages update
julia -e 'using Pkg; Pkg.update()'

# Limpeza
Remove-Item -Recurse -Force C:\Lab\data\*.log
Remove-Item -Recurse -Force C:\Lab\data\*.tmp
```

---

## 🚨 TROUBLESHOOTING COMUM

| Problema | Solução |
|----------|---------|
| `UnicodeEncodeError` no PowerShell | Use `chcp 65001` antes de rodar scripts |
| `Named Pipe busy` | `Get-Process powershell | Stop-Process -Force` |
| `Z3 not found` | `pip install z3-solver` |
| `Julia not found` | Adicione ao PATH: `C:\Users\<USER>\AppData\Local\Programs\Julia-1.13.1\bin` |
| `LTspice not found` | Adicione `C:\Program Files\ADI\LTspice` ao PATH |
| `lake build failed` | `lake update` depois `lake build` |
| `Python module not found` | Ative venv: `.\.venv\Scripts\Activate.ps1` |
| Junction `C:\Lab` não funciona | Execute como Admin: `cmd /c mklink /J "C:\Lab" "C:\Users\<USER>\Desktop\Research\IA-research-Godel-e-Krajicek"` |

---

## 📞 SUPORTE

Se algo falhar:
1. Execute `.\diagnostico.ps1` e envie a saída
2. Verifique logs em `C:\Lab\data\*.log`
3. Consulte `docs/guides/TROUBLESHOOTING.md`
3. Verifique `C:\Lab\data\*.log` para logs detalhados

---

## ✅ CHECKLIST FINAL DE VALIDAÇÃO

- [ ] Repositório clonado
- [ ] Junction `C:\Lab` criada
- [ ] Python 3.12+ + deps instaladas
- [ ] Julia 1.13+ instalada e no PATH
- [ ] LTspice instalado e no PATH
- [ ] FreeFEM++ instalado e no PATH
- [ ] CVC5 instalado e no PATH
- [ ] Z3 funcionando (`python -c "import z3; print(z3.get_version_string())"`)
- [ ] Julia funcional (`julia --version`)
- [ ] Lean 4 + lake build OK
- [ ] Junction `C:\Lab` funcional
- [ ] `LabLauncher.bat` abre menu
- [ ] `.\rea_bridge.ps1` inicia bridge
- [ ] `.\test_rea_event.ps1 -State CPU_CRITICAL -ProcessId 1423` funciona
- [ ] `python scripts\gk_theta_smt_z3.py` roda (216/216 PASS)
- [ ] `python scripts\gk_drat_translation_real.py` roda (216/216 PASS)
- [ ] `python scripts\gk_hardness_z3_real.py` roda
- [ ] `lake build` no lean4 OK
- [ ] `git push` funcionando para ambos repositórios

---

**Última atualização**: 2026-10-13  
**Versão**: 1.0.0  
**Autor**: Euzébio Soares  
**Repositório**: https://github.com/ebiossanto/IA-research-Godel-e-Krajicek
**Lab Local**: `C:\Lab` (junction para `C:\Users\Euzébio Soares\Desktop\Research\IA-research-Godel-e-Krajicek`)

---

> **Nota**: Este documento deve ser mantido atualizado a cada mudança significativa no laboratório. 
> A reidratação completa deve ser testada periodicamente em máquina limpa.
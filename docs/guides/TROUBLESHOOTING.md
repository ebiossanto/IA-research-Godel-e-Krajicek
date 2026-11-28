# Troubleshooting — Terminal-Laboratório

## 🚨 Problemas Comuns e Soluções

---

## 🐍 Python Issues

### `ModuleNotFoundError: No module named 'z3'`
```powershell
pip install z3-solver
# Verificar
python -c "import z3; print(z3.get_version_string())"
```

### `ModuleNotFoundError: No module named 'pysat'`
```powershell
pip install python-sat
```

### `ModuleNotFoundError: No module named 'pysat.solvers'`
```powershell
pip install --upgrade python-sat
# Verificar
python -c "from pysat.solvers import Solver; print('OK')"
```

### `ImportError: DLL load failed` (Windows)
```powershell
# Reinstalar com wheels
pip uninstall z3-solver pysat
pip install --force-reinstall --no-binary :all: z3-solver python-sat
# Ou instalar Visual C++ Redistributable
# https://aka.ms/vs/17/release/vc_redist.x64.exe
```

### `UnicodeEncodeError: 'charmap' codec can't encode`
```powershell
# No script Python, adicionar no topo:
# -*- coding: utf-8 -*-
# Ou usar:
import sys
sys.stdout.reconfigure(encoding='utf-8')
```

---

## 🌀 Julia Issues

### `julia: command not found`
```powershell
# Verificar instalação
julia --version

# Adicionar ao PATH permanentemente
$env:Path += ";C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin"
# Ou permanentemente:
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin", "User")
```

### `UndefVarError: DelimitedFiles not defined`
```julia
using Pkg
Pkg.add("DelimitedFiles")
```

### `ERROR: LoadError: could not load library`
```julia
# Reinstalar Julia completamente
# 1. Desinstalar Julia
# 2. Deletar: %USERPROFILE%\.julia
# 3. Reinstalar via winget
winget install Julialang.Julia
```

### Julia lento na primeira execução
```julia
# Primeira execução compila (JIT)
# Execuções subsequentes são rápidas
# Use: @time para medir
```

---

## ⚡ PowerShell Issues

### `ExecutionPolicy` bloqueia scripts
```powershell
# Verificar
Get-ExecutionPolicy

# Permitir scripts locais
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Ou temporário
powershell -ExecutionPolicy Bypass -File script.ps1
```

### `&` não reconhecido
```powershell
# Use aspas para caminhos com espaços
& "C:\Lab\rea_bridge.ps1"
# Ou
& "C:\Lab\scripts\entropy_calc.py"
```

### `&&` não funciona
```powershell
# PowerShell não suporta &&
# Use ; ou linhas separadas
cd C:\Lab; python script.py
# Ou
Start-Process powershell -ArgumentList "-Command cd C:\Lab; python script.py"
```

### Acentos no caminho (`Euzébio`)
```powershell
# Use junction (já criado)
cd C:\Lab
# Ou use aspas
cd "C:\Users\Euzébio Soares\Desktop\Terminal-Laboratorio"
```

### `Start-Process` não espera
```powershell
# Use -Wait
Start-Process powershell -ArgumentList "-File rea_bridge.ps1" -Wait -WorkingDirectory "C:\Lab"
```

### Named Pipe `All pipe instances are busy`
```powershell
# Matar processos PowerShell órfãos
Get-Process powershell | Stop-Process -Force

# Verificar pipes ativos
Get-ChildItem \\.\pipe\

# Reiniciar bridge
Get-Process powershell | Where-Object {$_.MainWindowTitle -like "*rea_bridge*"} | Stop-Process -Force
```

---

## 🐍 Python Specific

### `pysat` não encontra solver
```powershell
# Instalar glucose4 ou cadical
pip install glucose4
# Ou
pip install cadical
```

### `z3.z3types.Z3Exception: unknown parameter 'drat'`
```python
# Z3 não suporta 'drat' diretamente
# Use apenas:
s.set("proof", True)
# Para DRAT, use solver externo (glucose4/cadical)
```

### `UnicodeEncodeError` ao imprimir
```python
# No topo do script
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Ou use ASCII only
print("[OK]" instead of "✓")
```

---

## 🌀 Julia Specific

### `ERROR: LoadError: could not load library`
```julia
# Rebuild packages
using Pkg
Pkg.build()
Pkg.precompile()
```

### `SystemError: opening file failed`
```julia
# Verificar permissões
# Executar Julia como Admin se necessário
```

### `ERROR: LoadError: UndefVarError: Z3 not defined`
```julia
# Z3 não é nativo em Julia
# Use Python + Z3 ou chame Z3 via CLI
```

---

## 🔌 LTspice Issues

### `LTspice.exe not found`
```powershell
# Verificar instalação
Get-Command ltspice.exe -ErrorAction SilentlyContinue

# Adicionar ao PATH
$env:Path += ";C:\Program Files\ADI\LTspice"
```

### Batch mode não funciona
```cmd
# Use caminho completo
"C:\Program Files\ADI\LTspice\LTspice.exe" -b circuit.asc

# Ou no PowerShell
& "C:\Program Files\ADI\LTspice\LTspice.exe" -b circuit.asc
```

---

## 🔧 FreeFEM++ Issues

### `freefem++ not found`
```powershell
# Verificar instalação
dir "C:\Program Files (x86)\FreeFem++\FreeFem++.exe"

# Adicionar ao PATH
$env:Path += ";C:\Program Files (x86)\FreeFem++"
```

### `Compile error` no script .edp
```freefem
// Verificar sintaxe
// FreeFEM++ é case-sensitive
// Use ; no final de cada linha
real x = 1;
cout << x << endl;
```

### `Error opening file`
```freefem
// Use caminho absoluto ou relativo correto
// Evite acentos no caminho
```

---

## ⚡ Z3 Issues

### `z3-solver` não instala
```powershell
# Atualizar pip
python -m pip install --upgrade pip
pip install z3-solver

# Se falhar, instale Visual C++ Redistributable
# https://aka.ms/vs/17/release/vc_redist.x64.exe
```

### `Z3Exception: unknown parameter`
```python
# Verificar parâmetros válidos
s = Solver()
s.set("proof", True)  # OK
# s.set("drat", True)  # ERRO - não existe
```

### `Z3Exception: model is not available`
```python
s = Solver()
if s.check() == sat:
    m = s.model()  # Só disponível se SAT
else:
    print("UNSAT")
```

---

## 🔧 LTspice Issues

### `LTspice.exe not found`
```powershell
# Verificar instalação
& "C:\Program Files\ADI\LTspice\LTspice.exe" --help
```

### `Error: Cannot open file`
```cmd
# Verificar caminho do arquivo .asc
# Use caminhos absolutos
LTspice.exe -b "C:\Lab\integrations\ltspice\circuits\sat_circuit.asc"
```

---

## 🔧 FreeFEM++ Issues

### `freefem++ not recognized`
```powershell
# Adicionar ao PATH
$env:Path += ";C:\Program Files (x86)\FreeFem++"
# Ou permanentemente
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files (x86)\FreeFem++", "User")
```

### `Exec format error`
```bash
# No WSL, use freefem++ (não freefem)
freefem++ script.edp
```

---

## 🔧 CVC5 Issues

### `cvc5.exe not found`
```powershell
# Verificar extração
ls C:\Lab\cvc5\cvc5-Win64-x86_64-static\bin\cvc5.exe

# Adicionar ao PATH
$env:Path += ";C:\Lab\cvc5\cvc5-Win64-x86_64-static\bin"
```

### `Unsupported logic`
```smt2
; Use lógica suportada
(set-logic QF_UFBV)
; ou
(set-logic QF_LIA)
```

---

## 🔧 SageMath Issues

### `sage not found`
```bash
# No WSL/Ubuntu
sudo apt update && sudo apt install sagemath

# No Windows nativo
# Baixar instalador de https://www.sagemath.org/download-windows.html
```

### `ModuleNotFoundError` no Python
```python
# SageMath tem seu próprio Python
# Use sage -python script.py
# Não use python do sistema
```

---

## 🔧 Lean 4 Issues

### `lean not found`
```powershell
winget install leanprover.lean4
# ou
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh
```

### `lake build` falha
```lean
# Verificar lean-toolchain
# No diretório do projeto:
lake update
lake build
```

---

## 🔧 Git Issues

### `fatal: not a git repository`
```powershell
cd C:\Lab-Repo
git init
git remote add origin <url>
```

### `Permission denied (publickey)`
```powershell
# Gerar SSH key
ssh-keygen -t ed25519 -C "email@exemplo.com"
# Adicionar ao GitHub
cat ~/.ssh/id_ed25519.pub
```

---

## 📋 Checklist de Diagnóstico

```powershell
# Executar diagnóstico completo
.\diagnostico.ps1
```

### diagnostico.ps1
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
Test-Path "C:\Lab"

Write-Host "`n--- Junction C:\Lab\scripts ---"
Test-Path "C:\Lab\scripts"
```

---

## 📞 Quando Nada Funciona

1. **Reinicie o computador** (resolve 90% dos problemas de PATH)
2. **Execute como Administrador** (PowerShell Admin)
3. **Verifique Windows Updates** (pendentes podem travar instalações)
4. **Desative Antivírus temporariamente** (pode bloquear pipes/named pipes)
5. **Reinicie junction**: `cmd /c rmdir C:\Lab && mklink /J "C:\Lab" "C:\Users\SeuUsuario\Desktop\Terminal-Laboratorio"`

---

## 📞 Suporte

Se nada resolver:
1. Colete logs: `Get-EventLog -LogName Application -Newest 50`
2. Capture screenshot do erro
3. Execute `.\diagnostico.ps1` e envie saída
4. Verifique `C:\Lab\data\*.log` para logs detalhados
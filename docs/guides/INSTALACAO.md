# Guia de Instalação Completa — Terminal-Laboratório

## 📋 Pré-requisitos do Sistema

- **Windows 10/11** (testado)
- **PowerShell 5.1+** ou **PowerShell 7+**
- **Python 3.12+** (recomendado 3.12+)
- **Git** para versionamento
- **Administrador** (para instalação de algumas ferramentas)

---

## 1. Python 3.12+

### Instalação via Winget
```powershell
winget install Python.Python.3.12
```

### Verificação
```powershell
python --version
# Python 3.12.x
pip --version
```

### Dependências Python
```powershell
pip install --upgrade pip
pip install psutil numpy matplotlib pysat z3-solver
```

---

## 2. Julia 1.13+

### Instalação via Winget
```powershell
winget install Julialang.Julia
```

### Configuração PATH (Importante!)
```powershell
# Adicionar ao PATH permanentemente
$env:Path += ";C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin"
# Ou adicione nas Variáveis de Ambiente do Windows
```

### Pacotes Julia
```powershell
julia -e 'using Pkg; Pkg.add("DelimitedFiles")'
```

---

## 3. LTspice (Simulador Circuitos)

```powershell
winget install AnalogDevices.LTspice
```

**Localização padrão**: `C:\Program Files\ADI\LTspice\LTspice.exe`

---

## 4. FreeFEM++ (PDEs)

```powershell
winget install FreeFem.FreeFem
```

**Adicionar ao PATH**:
```
C:\Program Files (x86)\FreeFem++
```

**Teste**:
```powershell
freefem++ --version
```

---

## 5. CVC5 (SMT Solver)

### Download Manual
1. Acesse: https://github.com/cvc5/cvc5/releases/latest
2. Baixe: `cvc5-Win64-x86_64-static.zip`
3. Extraia para: `C:\Lab\cvc5\`
4. Adicione ao PATH: `C:\Lab\cvc5\cvc5-Win64-x86_64-static\bin`

**Teste**:
```powershell
cvc5.exe --version
```

---

## 6. GeoGebra (Visualização)

```powershell
winget install GeoGebra.Classic
```

---

## 7. SageMath (Opcional - via WSL)

### Opção 1: WSL + Ubuntu (Recomendado)
```powershell
wsl --install
# Reiniciar
# No Ubuntu:
sudo apt update && sudo apt install sagemath
```

### Opção 2: Windows Native (Experimental)
Baixar de: https://www.sagemath.org/download-windows.html

---

## 8. Lean 4 (Formalização)

```powershell
# Via elan
winget install leanprover.lean4
# ou
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh
```

**Verificação**:
```powershell
lean --version
lake --version
```

---

## 8. Junction C:\Lab (Resolve Acentos)

```cmd
cmd /c mklink /J "C:\Lab" "%USERPROFILE%\Desktop\Terminal-Laboratorio"
```

---

## 9. Python Dependencies

```powershell
pip install -r requirements.txt
```

**requirements.txt**:
```
psutil>=5.9.0
numpy>=1.24.0
matplotlib>=3.7.0
pysat>=1.9.0
z3-solver>=5.0.0
```

---

## 10. Junction C:\Lab (Resolve Acentos no Windows)

```cmd
cmd /c mklink /J "C:\Lab" "%USERPROFILE%\Desktop\Terminal-Laboratorio"
```

---

## 11. Verificação Final

```powershell
# Testar tudo
python -c "import psutil, numpy, matplotlib, pysat, z3; print('Python OK')"
julia -e 'println("Julia OK")'
ltspice.exe --help 2>&1 | head -1
freefem++ --version
cvc5.exe --version
z3 --version
lean --version
```

---

## ✅ Checklist Final

- [ ] Python 3.12+ instalado
- [ ] Dependências Python instaladas
- [ ] Julia instalada e no PATH
- [ ] LTspice instalado
- [ ] FreeFEM++ instalado e no PATH
- [ ] CVC5 baixado e no PATH
- [ ] GeoGebra instalado
- [ ] Z3 funcionando (`python -c "import z3; print(z3.get_version_string())"`)
- [ ] Junction `C:\Lab` criada
- [ ] `LabLauncher.bat` funcionando
- [ ] Bridge REA iniciando (`.\rea_bridge.ps1`)
- [ ] Eventos REA funcionando (`.\test_rea_event.ps1 -State CPU_CRITICAL -ProcessId 1423`)

---

## 🔧 Próximos Passos

1. Execute `LabLauncher.bat` para abrir o laboratório
2. Leia `docs/guides/PIPELINE.md` para pipeline completo
3. Execute `.\rea_bridge.ps1` (Terminal 1)
4. Execute `.\test_rea_event.ps1 -State CPU_CRITICAL -ProcessId 1423` (Terminal 2)
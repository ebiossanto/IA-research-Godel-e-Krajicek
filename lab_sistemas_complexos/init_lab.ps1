<# 
.SYNOPSIS
    Inicializa o Laboratório de Sistemas Complexos no novo ambiente
.DESCRIPTION
    Configura junction C:\Lab, verifica dependências, e prepara o ambiente.
.EXAMPLE
    .\init_lab.ps1
#>

# Configura encoding UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║     INICIALIZAÇÃO - LABORATÓRIO DE SISTEMAS COMPLEXOS       ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$LabPath = "C:\Lab"

# 1. Verificar/Criar Junction C:\Lab
Write-Host "[1/6] Verificando junction C:\Lab..." -ForegroundColor Yellow
if (Test-Path $LabPath) {
    Write-Host "  ✓ Junction C:\Lab já existe" -ForegroundColor Green
} else {
    Write-Host "  Criando junction C:\Lab..." -ForegroundColor Yellow
    $source = "$env:USERPROFILE\Desktop\Terminal-Laboratorio"
    if (Test-Path $source) {
        cmd /c mklink /J "`"$LabPath`"" "`"$source`"" 2>$null
        if (Test-Path $LabPath) {
            Write-Host "  ✓ Junction criada com sucesso" -ForegroundColor Green
        } else {
            Write-Host "  ✗ Falha ao criar junction (precisa Admin?)" -ForegroundColor Red
        }
    } else {
        Write-Host "  ⚠ Fonte não encontrada: $source" -ForegroundColor Yellow
    }

# 2. Verificar Python
Write-Host "`n[2/6] Verificando Python..." -ForegroundColor Yellow
try {
    $pyVer = python --version 2>&1
    Write-Host "  ✓ $pyVer" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Python não encontrado" -ForegroundColor Red
}

# 3. Verificar dependências Python
Write-Host "`n[3/6] Verificando dependências Python..." -ForegroundColor Yellow
$deps = @("psutil", "numpy", "matplotlib", "pysat", "z3-solver")
foreach ($dep in $deps) {
    try {
        python -c "import $dep" 2>$null
        Write-Host "  ✓ $dep" -ForegroundColor Green
    } catch {
        Write-Host "  ✗ $dep (instale: pip install $dep)" -ForegroundColor Red
    }
}

# 4. Verificar Julia
Write-Host "`n[4/6] Verificando Julia..." -ForegroundColor Yellow
try {
    $jlVer = julia --version 2>&1
    Write-Host "  ✓ $jlVer" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Julia não encontrado (winget install Julialang.Julia)" -ForegroundColor Red
}

# 5. Verificar ferramentas externas
Write-Host "`n[5/6] Verificando ferramentas externas..." -ForegroundColor Yellow
$tools = @(
    @{Name="LTspice"; Cmd="ltspice.exe --help"; Path="C:\Program Files\ADI\LTspice\LTspice.exe"},
    @{Name="FreeFEM++"; Cmd="freefem++ --version"; Path="C:\Program Files (x86)\FreeFem++\FreeFem++.exe"},
    @{Name="CVC5"; Cmd="cvc5.exe --version"; Path="C:\Lab\cvc5\cvc5-Win64-x86_64-static\bin\cvc5.exe"},
    @{Name="Z3"; Cmd="python -c `import z3; print(z3.get_version_string())`"; Path=""},
    @{Name="Julia"; Cmd="julia --version"; Path=""},
    @{Name="Lean 4"; Cmd="lean --version"; Path=""}
)

foreach ($tool in $tools) {
    if ($tool.Path -and (Test-Path $tool.Path)) {
        Write-Host "  ✓ $($tool.Name) encontrado em $($tool.Path)" -ForegroundColor Green
    } elseif ($tool.Cmd) {
        try {
            $out = Invoke-Expression $tool.Cmd 2>$null
            Write-Host "  ✓ $($tool.Name): $out" -ForegroundColor Green
        } catch {
            Write-Host "  ⚠ $($tool.Name) não encontrado" -ForegroundColor Yellow
        }
    }
}

# 6. Verificar Junction C:\Lab
Write-Host "`n[6/6] Verificando estrutura C:\Lab..." -ForegroundColor Yellow
$required = @("scripts", "integrations", "docs", "config", "examples", "data")
foreach ($dir in $required) {
    if (Test-Path "C:\Lab\$dir") {
        Write-Host "  ✓ $dir" -ForegroundColor Green
    } else {
        Write-Host "  ⚠ $dir não encontrado" -ForegroundColor Yellow
    }
}

# Resumo
Write-Host "`n" + "=" * 60
Write-Host "RESUMO DA INICIALIZAÇÃO" -ForegroundColor Cyan
Write-Host "=" * 60
Write-Host "Diretório do Lab: C:\Lab"
Write-Host "Junction: " -NoNewline
if (Test-Path "C:\Lab") { Write-Host "OK" -ForegroundColor Green } else { Write-Host "FALHA" -ForegroundColor Red }

Write-Host "`n🚀 Próximos passos:"
Write-Host "  1. Execute: .\LabLauncher.bat"
Write-Host "  2. Ou manualmente:"
Write-Host "     Terminal 1: .\rea_bridge.ps1"
Write-Host "     Terminal 2: .\test_rea_event.ps1 -State CPU_CRITICAL -ProcessId 1423"
Write-Host "`n✅ Inicialização concluída!"
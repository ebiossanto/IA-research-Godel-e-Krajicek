# =====================================================================
# diagnostico_ambiente.ps1 — Terminal-Laboratorio (Godel / Krajicek)
# Verifica ferramentas, pacotes e permissoes do laboratorio.
# Uso:
#   powershell -ExecutionPolicy Bypass -File .\diagnostico_ambiente.ps1
#   powershell -ExecutionPolicy Bypass -File .\diagnostico_ambiente.ps1 -Build   # inclui lake build
# =====================================================================
param([switch]$Build)

$ErrorActionPreference = "SilentlyContinue"
$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$fail = 0

function Ok($msg)   { Write-Host "[OK]   $msg" -ForegroundColor Green }
function Warn($msg) { Write-Host "[AVISO] $msg" -ForegroundColor Yellow }
function Bad($msg)  { Write-Host "[FALHA] $msg" -ForegroundColor Red; $script:fail++ }

Write-Host "=== DIAGNOSTICO TERMINAL-LABORATORIO ===" -ForegroundColor Cyan
Write-Host "Repo: $repo`n"

# ---- Git -------------------------------------------------------------
Write-Host "--- Git ---" -ForegroundColor Cyan
$git = Get-Command git -ErrorAction SilentlyContinue
if ($git) {
    Ok ("git " + (git --version))
    $safe = git config --global --get-all safe.directory 2>$null
    $norm = $repo -replace '\\','/'
    if ($safe -contains $norm -or $safe -contains "*") { Ok "safe.directory configurado" }
    else { Warn "safe.directory ausente para $norm -> git config --global --add safe.directory $norm" }
    $remote = git -C $repo remote get-url origin 2>$null
    if ($remote) { Ok "remoto origin = $remote" } else { Bad "sem remoto origin" }
    $branch = git -C $repo branch --show-current 2>$null
    if ($branch) { Ok "branch = $branch" }
} else { Bad "git nao encontrado no PATH" }

# ---- Python ----------------------------------------------------------
Write-Host "`n--- Python + pacotes ---" -ForegroundColor Cyan
$py = Get-Command python -ErrorAction SilentlyContinue
if ($py) {
    Ok ("python " + (python --version 2>&1) + " @ " + $py.Source)
    foreach ($m in @("z3","sympy","numpy","pandas","scipy","matplotlib","psutil","pysat","mpmath")) {
        $r = python -c "import $m; print(getattr($m,'__version__','?'))" 2>&1
        if ($LASTEXITCODE -eq 0) { Ok "$m $r" } else { Bad "$m NAO importa (pip install ...)" }
    }
    # integridade sympy: RECORD vs arquivo real
    $sp = python -c "import site; print(site.getusersitepackages())" 2>$null
    $rec = Join-Path $sp "sympy-*.dist-info\RECORD"
    $recFile = Get-Item $rec -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($recFile) {
        $line = Select-String -Path $recFile.FullName -Pattern "sympy/printing/pretty/pretty_symbology.py" | Select-Object -First 1
        if ($line -and $line.Line -match "sha256=([^,]+),(\d+)") {
            $wantSize = [int]$Matches[2]
            $file = Join-Path $sp "sympy\printing\pretty\pretty_symbology.py"
            if (Test-Path $file) {
                $size = (Get-Item $file).Length
                if ($size -eq $wantSize) { Ok "sympy integro (pretty_symbology.py $size bytes = RECORD)" }
                else { Bad "sympy ADULTERADO? ($size bytes != RECORD $wantSize) -> pip install --force-reinstall --no-deps sympy==1.14.0" }
            }
        }
    }
} else { Bad "python nao encontrado no PATH" }

# ---- Julia -----------------------------------------------------------
Write-Host "`n--- Julia ---" -ForegroundColor Cyan
$jl = Get-Command julia -ErrorAction SilentlyContinue
if ($jl) { Ok ("julia " + (julia --version)) }
else {
    $cand = Get-ChildItem "D:\Biblioteca\Desktop-Pessoal\Julia\*\bin\julia.exe" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($cand) {
        $up = [Environment]::GetEnvironmentVariable("Path","User")
        if ($up -like "*julia*") { Warn "julia: binario OK mas nao visivel NESTA sessao (PATH User ja atualizado -> reabra o terminal)" }
        else { Warn ("julia fora do PATH User: " + $cand.FullName + " -- adicionar ao PATH User") }
    }
    else { Bad "julia nao encontrada" }
}

# ---- Lean / elan / Lake ---------------------------------------------
Write-Host "`n--- Lean 4 ---" -ForegroundColor Cyan
$elanDir = Join-Path $env:USERPROFILE ".elan\bin"
$elan = Join-Path $elanDir "elan.exe"
$lake = Join-Path $elanDir "lake.exe"
if (Test-Path $elan) {
    Ok ("elan " + ((& $elan --version) 2>$null))
    if ((Get-Command lake -ErrorAction SilentlyContinue) -or (Test-Path $lake)) {
        Ok ("lake " + ((& $lake --version) 2>$null | Select-Object -Last 1))
    } else { Bad "lake.exe ausente" }
    if ($Build) {
        Write-Host "  executando lake build (pode demorar na 1a vez)..." -ForegroundColor DarkGray
        Push-Location $repo
        & $lake build 2>&1 | ForEach-Object { Write-Host "  $_" }
        if ($LASTEXITCODE -eq 0) { Ok "lake build EXIT=0 (verde)" }
        else { Bad "lake build falhou" }
        Pop-Location
    } else { Warn "lake build nao executado (use -Build para verificar)" }
} else { Bad "elan nao encontrado em $elanDir" }

# ---- PATH ------------------------------------------------------------
Write-Host "`n--- PATH (User) ---" -ForegroundColor Cyan
$userPath = [Environment]::GetEnvironmentVariable("Path","User")
foreach ($need in @(".elan\bin", "julia-1.10.2\bin")) {
    if ($userPath -like "*$need*") { Ok "PATH contem $need" }
    else { Warn "PATH User sem $need" }
}

# ---- Ferramentas opcionais ------------------------------------------
Write-Host "`n--- Opcionais (FCT) ---" -ForegroundColor Cyan
if (Get-Command cvc5 -ErrorAction SilentlyContinue) { Ok "cvc5" } else { Warn "cvc5 ausente (opcional)" }
if (Test-Path "C:\Program Files\ADI\LTspice\LTspice.exe") { Ok "LTspice" } else { Warn "LTspice ausente (opcional)" }
if (Test-Path "C:\Program Files (x86)\FreeFem++") { Ok "FreeFEM++" } else { Warn "FreeFEM++ ausente (opcional)" }
if (Get-Command winget -ErrorAction SilentlyContinue) { Ok "winget" } else { Warn "winget ausente -> usar choco" }
if (Get-Command choco -ErrorAction SilentlyContinue) { Ok "choco" } else { Warn "choco ausente" }

# ---- Resumo ----------------------------------------------------------
Write-Host "`n=== RESUMO ===" -ForegroundColor Cyan
if ($fail -eq 0) { Write-Host "Ambiente OK (avisos sao opcionais)." -ForegroundColor Green }
else { Write-Host "$fail falha(s) obrigatoria(s) - ver [FALHA] acima." -ForegroundColor Red }
exit $fail

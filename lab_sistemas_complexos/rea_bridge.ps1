# rea_bridge.ps1 - Ponte de Automacao Event-Driven do Laboratorio (PowerShell)

$PIPE_NAME = "rea_telemetry_pipe"
$PIPE_PATH = "\\.\pipe\$PIPE_NAME"

Write-Host "[LABORATORIO] Aguardando transicoes de estado critico do REA..." -ForegroundColor Cyan
Write-Host "[INFO] Named Pipe: $PIPE_PATH" -ForegroundColor Gray

# Loop persistente que escuta os eventos do REA via Named Pipe
while ($true) {
    try {
        # Cria o Named Pipe Server
        $pipe = New-Object System.IO.Pipes.NamedPipeServerStream($PIPE_NAME, 'In', 1, 'Byte', 'None')
        
        Write-Host "[PIPE] Aguardando conexao..." -ForegroundColor Yellow
        $pipe.WaitForConnection()
        Write-Host "[PIPE] Conexao estabelecida!" -ForegroundColor Green
        $reader = New-Object System.IO.StreamReader($pipe)
        $line = $reader.ReadLine()
        Write-Host "[PIPE] Linha recebida: $line" -ForegroundColor Cyan
        $pipe.Disconnect()
        $pipe.Close()
        $reader.Close()
        
        if ($line -and $line.Trim()) {
            $TIMESTAMP = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
            $PARTS = $line.Split(',')
            $STATE = $PARTS[0].Trim()
            $SOURCE_PID = if ($PARTS.Count -gt 1) { $PARTS[1].Trim() } else { "unknown" }

            Write-Host "[EVENTO - $TIMESTAMP] Mudanca detectada pelo REA: $STATE no PID $SOURCE_PID" -ForegroundColor Green

            switch ($STATE) {
                "CPU_CRITICAL" { 
                    Write-Host "[OPENCODE] Invocando pipeline matematico para calculo de Entropia de Shannon (CPU)..." -ForegroundColor Magenta
                    & python scripts/entropy_calc.py --source=$SOURCE_PID
                }
                "OVERHEAD_HIGH" { 
                    Write-Host "[OPENCODE] Invocando pipeline matematico para calculo de Entropia de Shannon (CPU)..." -ForegroundColor Magenta
                    & python scripts/entropy_calc.py --source=$SOURCE_PID
                }
                "SYSCALL_BURST" { 
                    Write-Host "[OPENCODE] Roteando fluxo analitico de alta performance para o motor Julia..." -ForegroundColor Magenta
                    $juliaPath = "C:\Users\Euzébio Soares\AppData\Local\Programs\Julia-1.13.1\bin\julia.exe"
                    $scriptPath = "C:\Lab\scripts\entropy_syscalls.jl"
                    Write-Host "[DEBUG] Executando: $juliaPath $scriptPath" -ForegroundColor Yellow
                    & $juliaPath $scriptPath
                    Write-Host "[DEBUG] Julia exit code: $LASTEXITCODE" -ForegroundColor Yellow
                }
                "MUTATION_DETECTED" { 
                    Write-Host "[OPENCODE] Roteando fluxo analitico de alta performance para o motor Julia..." -ForegroundColor Magenta
                    $juliaPath = "C:\Users\Euzébio Soares\AppData\Local\Programs\Julia-1.13.1\bin\julia.exe"
                    $scriptPath = "C:\Lab\scripts\entropy_syscalls.jl"
                    Write-Host "[DEBUG] Executando: $juliaPath $scriptPath" -ForegroundColor Yellow
                    & $juliaPath $scriptPath
                    Write-Host "[DEBUG] Julia exit code: $LASTEXITCODE" -ForegroundColor Yellow
                }
                default { 
                    Write-Host "[INFO] Estado '$STATE' registrado, mas nenhuma regra de entropia critica associada." -ForegroundColor Gray
                }
            }
        }
    }
    catch {
        Write-Host "[ERRO] $($_.Exception.Message)" -ForegroundColor Red
        Start-Sleep -Seconds 1
    }
}
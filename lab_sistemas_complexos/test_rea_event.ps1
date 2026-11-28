# test_rea_event.ps1 - Simula eventos do REA para testar a ponte

param(
    [Parameter(Mandatory=$false)]
    [string]$State = "CPU_CRITICAL",
    
    [Parameter(Mandatory=$false)]
    [string]$ProcessId = "1423"
)

$PIPE_NAME = "rea_telemetry_pipe"
$PIPE_PATH = "\\.\pipe\$PIPE_NAME"

$message = "$State,$ProcessId"

Write-Host "[TESTE] Enviando evento simulado para o REA Bridge..." -ForegroundColor Cyan
Write-Host "[TESTE] Estado: $State | PID: $ProcessId" -ForegroundColor Gray

try {
    $pipeClient = New-Object System.IO.Pipes.NamedPipeClientStream(".", $PIPE_NAME, 'Out', 'None')
    $pipeClient.Connect(5000)  # Timeout 5 segundos
    
    $writer = New-Object System.IO.StreamWriter($pipeClient)
    $writer.AutoFlush = $true
    $writer.WriteLine($message)
    
    Write-Host "[TESTE] Evento enviado com sucesso!" -ForegroundColor Green
}
catch {
    Write-Host "[ERRO] Não foi possível conectar ao pipe. O bridge está rodando?" -ForegroundColor Red
    Write-Host "[ERRO] $($_.Exception.Message)" -ForegroundColor Red
}
finally {
    if ($writer) { $writer.Close() }
    if ($pipeClient) { $pipeClient.Close() }
}
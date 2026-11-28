<# 
.SYNOPSIS
    Inicia o Terminal-Laboratório na pasta padrão da Área de Trabalho

.DESCRIPTION
    Script de acesso rápido para o Terminal-Laboratório de Análise de Sistemas Complexos.
    Muda para o diretório padrão e mostra status dos arquivos.

.EXAMPLE
    .\iniciar_laboratorio.ps1
#>

$LAB_PATH = "C:\Lab"

Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║     TERMINAL-LABORATÓRIO — Sistema de Análise Complexa      ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

Set-Location $LAB_PATH
Write-Host "[DIR] Pasta ativa: $LAB_PATH" -ForegroundColor Green
Write-Host ""

Write-Host "📁 ESTRUTURA PRINCIPAL:" -ForegroundColor Yellow
Get-ChildItem -Directory | Select-Object Name, LastWriteTime | Format-Table -AutoSize

Write-Host ""
Write-Host "📄 ARQUIVOS DE DADOS RECENTES:" -ForegroundColor Yellow
Get-ChildItem *.csv, *.json, *.png -ErrorAction SilentlyContinue | 
    Sort-Object LastWriteTime -Descending | 
    Select-Object -First 10 Name, Length, LastWriteTime | 
    Format-Table -AutoSize

Write-Host ""
Write-Host "🚀 COMANDOS RÁPIDOS:" -ForegroundColor Magenta
Write-Host "  Coletar 30s + gráfico:  python scripts\collect_and_plot.py" -ForegroundColor Gray
Write-Host "  Entropia CPU (10s):     python scripts\entropy_calc.py" -ForegroundColor Gray
Write-Host "  Bridge REA (Terminal 1): .\rea_bridge.ps1" -ForegroundColor Gray
Write-Host "  Testar evento REA:      .\test_rea_event.ps1 -State CPU_CRITICAL -PID 1423" -ForegroundColor Gray
Write-Host "  Ver log linhagem:       type sistema_complexo_entropia.csv" -ForegroundColor Gray

Write-Host ""
Write-Host "✅ Pronto para uso!" -ForegroundColor Green
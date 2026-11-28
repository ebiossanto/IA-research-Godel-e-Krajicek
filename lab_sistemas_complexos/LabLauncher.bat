@echo off
REM LabLauncher.bat - Inicia o Terminal-Laboratorio com encoding UTF-8 correto
REM Resolve problemas de acentos no caminho do usuario

chcp 65001 >nul
cd /d C:\Lab

echo ============================================
echo  TERMINAL-LABORATORIO - Sistema de Analise
echo ============================================
echo.
echo [DIR] Pasta ativa: C:\Lab
echo.

echo ESTRUTURA PRINCIPAL:
dir /ad /b

echo.
echo ARQUIVOS DE DADOS RECENTES:
dir /b *.csv *.json *.png 2>nul

echo.
echo COMANDOS RAPIDOS:
echo   Coletar 30s + grafico:    python scripts\collect_and_plot.py
echo   Entropia CPU (10s):       python scripts\entropy_calc.py
echo   Bridge REA (Terminal 1):  .\rea_bridge.ps1
echo   Testar evento REA:        .\test_rea_event.ps1 -State CPU_CRITICAL -ProcessId 1423
echo   Ver log linhagem:         type sistema_complexo_entropia.csv
echo.
echo OK - Pronto para uso!
echo.

cmd /k
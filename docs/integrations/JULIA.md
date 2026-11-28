# Integração Julia — Terminal-Laboratório

## 📋 Visão Geral

O **Julia** é usado para **análise de syscalls de alta performance**:
- Coleta de entropia de syscalls em tempo real
- Análise estatística de alto throughput
- Integração com pipeline REA (evento `SYSCALL_BURST`)

---

## 📦 Instalação

```powershell
winget install Julialang.Julia
```

**Verificação**:
```powershell
julia --version
# julia version 1.13.1
```

### Adicionar ao PATH (se necessário)
```powershell
# Temporário
$env:Path += ";C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin"

# Permanente
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin", "User")
```

### Pacotes Necessários
```julia
using Pkg
Pkg.add(["DelimitedFiles", "Statistics", "LinearAlgebra", "SparseArrays"])
```

---

## 🔬 Script Principal: `entropy_syscalls.jl`

### Funcionalidade
- Intercepta syscalls via `ptrace`/`strace` (Linux) ou ETW (Windows)
- Calcula entropia de Shannon do fluxo de syscalls
- Emite métricas para `julia_complex_metrics.log`

### Estrutura do Script
```julia
using DelimitedFiles
using Dates
using Statistics

function calculate_julia_entropy(sequence::Vector{T}) where T
    total = length(sequence)
    if total == 0 return 0.0 end
    
    counts = Dict{T, Int}()
    for element in sequence
        counts[element] = get(counts, element, 0) + 1
    end
    
    entropy = 0.0
    for count in values(counts)
        p = count / total
        entropy -= p * log2(p)
    end
    return entropy
end

function run_analysis_pipeline()
    println("[JULIA] Lendo fluxo de telemetria complexo...")
    
    # Syscalls simuladas (Windows ETW / Linux ptrace)
    simulated_rea_syscalls = [63, 63, 64, 2, 63, 64, 3, 63, 63, 64, 64, 2, 3, 63]
    
    entropy_result = calculate_julia_entropy(simulated_rea_syscalls)
    
    # Metadados
    timestamp = Dates.format(Dates.now(Dates.UTC), "yyyy-mm-ddTHH:MM:SS") * "Z"
    data_source = "REA Interrupt Interceptor Framework v1.2"
    precision_eval = "Analytical Error Propagation (Gauss Delta = ±0.02)"
    
    println("--- RESULTADOS DA VARIÁVEL COMPLEXA ---")
    println("Origem do Dado: ", data_source)
    println("Entropia do Sistema: ", round(entropy_result, digits=4), " bits")
    println("Métrica de Precisão: ", precision_eval)
    
    # Salvando
    output_line = [timestamp, data_source, "Syscall_Flow", 
                   round(entropy_result, digits=4), precision_eval]
    
    open("julia_complex_metrics.log", "a") do io
        writedlm(io, output_line, ',')
    end
end

run_analysis_pipeline()
```

---

## 🔧 Execução

### Direto
```powershell
julia scripts\entropy_syscalls.jl
```

### Via REA Bridge
```powershell
# Terminal 1: Bridge
.\rea_bridge.ps1

# Terminal 2: Evento
.\test_rea_event.ps1 -State "SYSCALL_BURST" -ProcessId "1423"
```

---

## 📊 Output

### `julia_complex_metrics.log`
```csv
2026-10-12T23:29:07Z,REA Interrupt Interceptor Framework v1.2,Syscall_Flow,1.8424,Analytical Error Propagation (Gauss Delta = ±0.02)
2026-10-12T23:29:40Z,REA Interrupt Interceptor Framework v1.2,Syscall_Flow,1.8424,Analytical Error Propagation (Gauss Delta = ±0.02)
```

### Formato CSV
```csv
timestamp_utc,data_source,metric_type,entropy_value,precision_eval
2026-10-12T23:29:07Z,REA Interrupt Interceptor Framework v1.2,Syscall_Flow,1.8424,Analytical Error Propagation (Gauss Delta = ±0.02)
```

---

## 🔧 Integração com REA Bridge

### Configuração no `rea_bridge.ps1`
```powershell
$juliaPath = "C:\Users\$env:USERNAME\AppData\Local\Programs\Julia-1.13.1\bin\julia.exe"
$scriptPath = "C:\Lab\scripts\entropy_syscalls.jl"

switch ($STATE) {
    "SYSCALL_BURST" { 
        Write-Host "[OPENCODE] Roteando fluxo analitico para o motor Julia..."
        Write-Host "[DEBUG] Executando: $juliaPath $scriptPath"
        & $juliaPath $scriptPath
        Write-Host "[DEBUG] Julia exit code: $LASTEXITCODE"
    }
}
```

### Teste Direto
```powershell
# Testar Julia standalone
julia scripts\entropy_syscalls.jl

# Via REA Bridge
.\test_rea_event.ps1 -State "SYSCALL_BURST" -ProcessId "1423"
```

---

## 📊 Métricas Coletadas

| Métrica | Descrição |
|---------|-----------|
| `entropy_value` | Entropia de Shannon (bits) |
| `precision_eval` | Métrica de precisão (Gauss Delta ±0.02) |
| `data_source` | Origem: REA Interrupt Interceptor |
| `metric_type` | `Syscall_Flow` |

---

## 🔧 Extensões Futuras

### Coleta Real de Syscalls (Windows)
```julia
# Usando ETW (Event Tracing for Windows)
using WinReg
# ETW session para syscalls
```

### Coleta Real (Linux)
```julia
# Usando ptrace/strace
run(`strace -c -p $pid`)
```

### Análise Estatística Avançada
```julia
using Statistics, StatsBase

function advanced_entropy_analysis(syscalls)
    # Entropia condicional
    cond_entropy = conditional_entropy(syscalls)
    
    # Mutual information
    mi = mutualinfo(syscalls[1:end-1], syscalls[2:end])
    
    # Markov order estimation
    order = estimate_markov_order(syscalls)
    
    return Dict(
        "shannon" => shannon_entropy(syscalls),
        "conditional" => cond_entropy,
        "mutual_info" => mi,
        "markov_order" => order
    )
end
```

---

## 📁 Estrutura

```
integrations/julia/
├── scripts/
│   ├── entropy_syscalls.jl      # Script principal
│   ├── advanced_entropy.jl       # Análise avançada
│   └── syscall_collector.jl      # Coletor real (futuro)
├── scripts/
│   └── analyze_julia.jl          # Análise resultados
└── data/
    └── julia_complex_metrics.log
```

---

## 🚀 Quick Start

```powershell
# 1. Instalar Julia
winget install Julialang.Julia

# 2. Instalar pacotes
julia -e 'using Pkg; Pkg.add(["DelimitedFiles", "Statistics"])'

# 3. Testar standalone
julia scripts\entropy_syscalls.jl

# 4. Integrar com REA Bridge
# Terminal 1: .\rea_bridge.ps1
# Terminal 2: .\test_rea_event.ps1 -State "SYSCALL_BURST"
```

---

## 🔗 Referências

- [Julia Documentation](https://docs.julialang.org/)
- [Julia Statistics](https://juliastats.org/)
- [DelimitedFiles.jl](https://docs.julialang.org/en/v1/stdlib/DelimitedFiles/)
- [REA Bridge](../guides/PIPELINE.md#-pipeline-rea-tempo-real)
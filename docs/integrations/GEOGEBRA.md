# Integração GeoGebra — Terminal-Laboratório

## 📋 Visão Geral

O **GeoGebra** é usado para **visualização matemática** e **diagramas para papers**:
- **Geometria dinâmica** — diagramas de prova
- **Álgebra/gráficos** — visualização de funções de prova
- **CAS** — computação algébrica simbólica
- **Exportação** — TikZ, PNG, SVG, PDF para papers

---

## 📦 Instalação

```powershell
winget install GeoGebra.Classic
```

**Versões disponíveis**:
- `GeoGebra.Classic` — Versão 6 (recomendada)
- `GeoGebra.Classic.5` — Versão 5 (legacy)
- `GeoGebra.GraphingCalculator` — Calculadora gráfica
- `GeoGebra.CASCalculator` — CAS standalone
- `GeoGebra.Geometry` — Geometria pura

---

## 🔧 Configuração

### Exportação TikZ (para LaTeX)
1. **File > Export > Graphics View as PGF/TikZ**
2. Configurações recomendadas:
   - Format: PGF/TikZ (.tex)
   - Font size: 10pt
   - Line thickness: 0.6pt
   - Include preamble: ✓

### Exportação PNG/SVG
```
File > Export > Graphics View as Image
Format: PNG (300 DPI) ou SVG
Background: Transparent (para papers)
```

---

## 🔬 Aplicações no Laboratório

### 1. Diagramas de Estrutura de Prova

```geogebra
# Grafo de implicação CNF
# Vértices = literais
# Arestas = cláusulas compartilhadas

# No GeoGebra CAS:
Vertices = {A, B, C, D, E}
Edges = {(A,B), (B,C), (C,D), (A,C), (D,E)}

# Visualização
Graph(Vertices, Edges)
```

### 2. Diagramas de Ordinais

```geogebra
# Hierarquia de Beklemishev
# ω, ω^ω, ω^ω^ω, ...

# Curva exponencial ordinal
f(x) = ω^x
Plot(f(x), x, 0, 5)

# Fixed points
f(x) = x
Intersect(f(x), ω^x)
```

### 3. Estrutura de Prova (Grafos)

```geogebra
# Grafo de implicação CNF
# Vértices = variáveis/literais
# Arestas = co-ocorrência em cláusula

# Exemplo CNF: (x∨y∨¬z) ∧ (¬x∨y) ∧ (¬y∨z)
V = {x, ¬x, y, ¬y, z, ¬z}
E = {(x,y), (x,¬z), (y,¬x), (y,¬z), (z,¬y)}

# Visualização
Graph(V, E)
```

### 4. Visualização de Hardness

```geogebra
# Funções de crescimento
f_res(n) = 2^n           # Resolution
f_efrege(n) = n^3        # Extended Frege
f_frege(n) = n^4         # Frege
f_p(n) = n               # P_Optimal

Plot(f_res, f_efrege, f_frege, f_p, 1, 100)
```

---

## 📁 Templates GeoGebra

### Template 1: Grafo de Implicação CNF
```geogebra
# Template: cnf_implication_graph.ggb
# Input: CNF clauses
# Output: Grafo de implicação + métricas

# Input (modificar aqui)
Clauses = {{1, -2, 3}, {-1, 2}, {-2, -3, 4}}

# Auto-gerado
Vertices = Unique[Flatten[Abs[Clauses]]]
Edges = Zip({a, b}, Clauses, Sequence(Combinations(Abs[c], 2), c, Clauses))

# Métricas
VerticesCount = Length[Vertices]
EdgesCount = Length[Edges]
DegreeDist = Frequency[Degree[Vertices]]
Treewidth = Treewidth[Graph[Vertices, Edges]]
```

### 2. Diagrama de Ordinais
```geogebra
# ordinal_hierarchy.ggb
# Hierarquia de Beklemishev / Slow Consistency

# Funções
f_fast(x) = ω^(2*x)
f_slow(x) = ω^x
f_landauer(x) = k*T*ln(2)*x

# Plot
Plot(f_fast(x), x, 0, 5, Color(255,0,0))
Plot(f_slow(x), x, 0, 5, Color(0,0,255))
Plot(f_landauer(x), x, 0, 5, Color(0,255,0))

# Legenda
Text("Rápida (ω^(2α))", (1, 100), Red)
Text("Lenta (ω^α)", (1, 50), Blue)
Text("Landauer", (1, 10), Green)
```

### 3. Hardware de Prova
```geogebra
# proof_hardware.ggb
# Arquitetura de hardware de prova SAT

# Componentes
Components = {
  "VarReg": "Variable Register Bank",
  "ClauseMem": "Clause Memory (CNF)",
  "EvalUnit": "Clause Evaluator",
  "Conflict": "Conflict Analysis",
  "Backtrack": "Backtrack Unit"
}

Connections = {
  ("VarReg", "ClauseMem"),
  ("ClauseMem", "EvalUnit"),
  ("EvalUnit", "Conflict"),
  ("Conflict", "Backtrack"),
  ("Backtrack", "VarReg")
}

# Métricas
ProofLength = 100
Energy = ProofLength * 1e-12  # J
Time = ProofLength * 1e-9     # s
```

---

## 📁 Templates Disponíveis

```
integrations/geogebra/templates/
├── cnf_implication_graph.ggb      # Grafo implicação CNF
├── ordinal_hierarchy.ggb          # Hierarquia ordinal
├── proof_hardware.ggb             # Hardware de prova
├── hardness_comparison.ggb        # Comparação hardness
├── ordinal_hierarchy.ggb          # Hierarquia ordinal
├── proof_hardware.ggb             # Hardware de prova
├── thermo_proof.ggb               # Termodinâmica
├── ordinal_fixed_points.ggb       # Pontos fixos
├── landauer_limit.ggb             # Limite Landauer
└── ppr_diagram.ggb                # Diagrama PPR
```

---

## 🚀 Exportação para Papers

### TikZ Export (Recomendado para LaTeX)
```
File > Export > Graphics View as PGF/TikZ (.tex)
Settings:
  - Format: PGF/TikZ
  - Font: 10pt
  - Line width: 0.6pt
  - Include preamble: ✓
  - Scale: 1.0
```

### Uso no LaTeX
```latex
\documentclass{article}
\usepackage{tikz}
\usepackage{pgfplots}

\begin{document}
\input{diagram.tikz}
\end{document}
```

### PNG/SVG para Web/Word
```
File > Export > Graphics View as Image
Format: PNG (300 DPI) ou SVG
Background: Transparent
```

---

## 📁 Templates Disponíveis

```
integrations/geogebra/templates/
├── cnf_implication_graph.ggb
├── ordinal_hierarchy.ggb
├── proof_hardware.ggb
├── hardness_comparison.ggb
├── ordinal_hierarchy.ggb
├── proof_hardware.ggb
├── thermo_proof.ggb
├── ordinal_fixed_points.ggb
├── landauer_limit.ggb
└── ppr_diagram.ggb
```

---

## 🚀 Quick Start

```powershell
# 1. Abrir GeoGebra
start "" "C:\Program Files\GeoGebra\GeoGebra Classic 6\GeoGebra.exe"

# 2. Abrir template
# File > Open > C:\Lab\integrations\geogebra\templates\cnf_implication_graph.ggb

# 3. Modificar dados
# Editar Clauses no Algebra View

# 4. Exportar
# File > Export > Graphics View as PGF/TikZ
```

---

## 🔗 Referências

- [GeoGebra Manual](https://wiki.geogebra.org/en/Manual)
- [GeoGebra CAS](https://wiki.geogebra.org/en/CAS)
- [Export TikZ](https://wiki.geogebra.org/en/Export_as_PGF/TikZ)
- [GeoGebra Scripting](https://wiki.geogebra.org/en/Scripting)
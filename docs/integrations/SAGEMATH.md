# Integração SageMath — Terminal-Laboratório

## 📋 Visão Geral

O **SageMath** é um sistema matemático unificado que combina:
- **Álgebra computacional** (grupos, anéis, corpos, polinômios)
- **Teoria dos números** (forma modular, curvas elípticas)
- **Combinatória** (grafos, matroides, posets)
- **Teoria das categorias**
- **Cálculo simbólico** (via Maxima/SymPy)
- **Geometria algébrica**

---

## 📦 Instalação

### Opção 1: WSL + Ubuntu (Recomendado)
```powershell
# PowerShell Admin
wsl --install
# Reiniciar

# No Ubuntu:
sudo apt update && sudo apt install sagemath
```

### Opção 2: Windows Native (Experimental)
```powershell
# Baixar de: https://www.sagemath.org/download-windows.html
# Instalador .exe ou .msi
```

### Opção 3: Docker
```powershell
docker run -it sagemath/sage:latest sage
```

### Opção 4: Conda
```powershell
conda install -c conda-forge sage
```

---

## 🔧 Configuração

### Verificação
```bash
sage --version
# SageMath version 10.x

# No Python
sage -python -c "import sage.all; print(sage.version.version)"
```

### Jupyter Kernel
```bash
sage -n jupyter
# Abre Jupyter com kernel Sage
```

---

## 🔬 Aplicações no Laboratório

### 1. Teoria dos Números / Ordinais
```python
# sage -python ordinal_analysis.py

from sage.all import *

# Ordinais
omega = ordinals.omega
omega_pow = omega^omega
print(omega_pow)

# Funções normais
def f(alpha):
    return alpha + 1

# Fixed points
fp = fixed_points(f, omega)
print(fp)
```

### 2. Álgebra / Grupos / Anéis
```python
# Grupos de permutação (simetria de provas)
G = SymmetricGroup(5)
print(G.order())
print(G.conjugacy_classes())

# Anéis de polinômios (códigos de prova)
R.<x> = PolynomialRing(GF(2))
f = x^8 + x^4 + x^3 + x + 1  # AES polynomial
print(f.factor())
```

### 3. Combinatória / Grafos (Estrutura de Prova)
```python
# Grafo de implicação
G = Graph()
G.add_edges([(1,2), (2,3), (3,4), (1,3)])

# Propriedades
print("Connected:", G.is_connected())
print("Diameter:", G.diameter())
print("Chromatic number:", G.chromatic_number())

# Cliques (conjuntos consistentes)
print("Max cliques:", G.cliques_maximum())

# Tree decomposition (para proof complexity)
print("Treewidth:", G.treewidth())
```

### 4. Geometria Algébrica (Variedades de Prova)
```python
# Variedade de provas válidas
R.<x,y,z> = PolynomialRing(QQ, 3)
I = ideal(x^2 + y^2 - 1, x*z - y^2)
V = Variety(I)
print(V.dimension())
print(V.degree())

# Hilbert polynomial
R.<x> = PolynomialRing(QQ)
I = ideal(x^3 - 2)
print(HilbertPolynomial(I))
```

---

## 🐍 Sage + Python Integration

### Usando Sage no Python
```python
# sage -python script.py
from sage.all import *

# OU dentro do Python normal (se sage instalado via conda)
import sys
sys.path.append('/opt/sage/lib/python3.x/site-packages')
from sage.all import *
```

### Sage + Z3 Integration
```python
from sage.all import *
from z3 import *

# Converter fórmula Sage para Z3
def sage_to_z3(sage_formula):
    # Conversão simbólica
    pass

# Interpolação via Sage + Z3
from sage.all import *
from z3 import *

# Sage para manipulação algébrica
R.<x,y> = PolynomialRing(QQ, 2)
f = x^2 + y^2 - 1

# Z3 para SMT solving
from z3 import *
x_z3, y_z3 = Reals('x y')
s = Solver()
s.add(x_z3**2 + y_z3**2 == 1)
print(s.check())
```

---

## 🔬 Aplicações no Laboratório

### 1. Análise Ordinal (Beklemishev Hierarchy)
```python
# ordinal_analysis.py

from sage.all import *

# Hierarquia de Beklemishev
def beklemishev_hierarchy(alpha, n):
    """Constrói hierarquia de reflexão"""
    if n == 0:
        return alpha
    return ordinals.omega ** beklemishev_hierarchy(alpha, n-1)

# Progressão lenta (slow consistency)
def slow_consistency(T, alpha):
    """Slow consistency progression"""
    if alpha == 0:
        return T
    return slow_consistency(T + Con(T), alpha - 1)

# Teste
print(beklemishev_hierarchy(ordinals.omega, 3))
```

### 2. Proof Complexity via Sage
```python
# proof_complexity_sage.py

from sage.all import *

# Códigos de prova como polinômios
R.<x> = PolynomialRing(GF(2))
proof_poly = x^100 + x^50 + x^25 + 1

# Fatoração = estrutura da prova
factors = proof_poly.factor()
print("Fatores:", factors)

# Grau = proof length
print("Proof length:", proof_poly.degree())

# Irredutibilidade = prova irreduzível
print("Irredutível:", proof_poly.is_irreducible())
```

### 3. Combinatória de Prova (Graph Theory)
```python
# proof_graphs.py

from sage.all import *

def proof_implication_graph(clauses):
    """Grafo de implicação de cláusulas CNF"""
    G = Graph()
    var_map = {}
    idx = 0
    
    for clause in clauses:
        for lit in clause:
            var = abs(lit)
            if var not in var_map:
                var_map[var] = idx
                idx += 1
    
    # Adiciona arestas: lit1 -> lit2 se na mesma cláusula
    for clause in clauses:
        lits = [var_map[abs(lit)] for lit in clause]
        for i in range(len(lits)):
            for j in range(i+1, len(lits)):
                G.add_edge(lits[i], lits[j])
    
    return G

# Análise
clauses = [[1, -2, 3], [-1, 2], [-2, -3, 4]]
G = proof_implication_graph(clauses)

print("Vertices:", G.order())
print("Edges:", G.size())
print("Connected components:", G.connected_components_number())
print("Treewidth:", G.treewidth())
print("Chromatic number:", G.chromatic_number())
```

---

## 📁 Estrutura

```
integrations/sage/
├── scripts/
│   ├── ordinal_analysis.py       # Análise ordinal
│   ├── proof_complexity.py       # Complexidade via Sage
│   ├── proof_graphs.py           # Grafos de prova
│   ├── algebraic_proofs.py       # Provas algébricas
│   ├── combinatorics.py          # Combinatória
│   └── sage_z3_bridge.py         # Bridge Sage-Z3
├── examples/
│   ├── ordinal_hierarchy.sage
│   ├── proof_graph.sage
│   └── algebraic_proof.sage
└── notebooks/
    ├── ordinal_analysis.ipynb
    └── proof_complexity.ipynb
```

---

## 🚀 Quick Start

```bash
# 1. Verificar instalação
sage --version

# 2. Executar script
sage -python scripts/ordinal_analysis.py

# 3. Jupyter notebook
sage -n jupyter

# 3. Sage shell
sage
```

---

## 🔗 Referências

- [SageMath Documentation](https://doc.sagemath.org/)
- [SageMath Tutorial](https://doc.sagemath.org/html/en/tutorial/)
- [SageMath Reference](https://doc.sagemath.org/html/en/reference/)
- [SageMath Combinatorics](https://doc.sagemath.org/html/en/reference/combinat/)
- [SageMath Graph Theory](https://doc.sagemath.org/html/en/reference/graphs/)
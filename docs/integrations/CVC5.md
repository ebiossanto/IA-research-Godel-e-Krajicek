# Integração CVC5 — Terminal-Laboratório

## 📋 Visão Geral

O **CVC5** é um **SMT Solver** state-of-the-art, complementar ao Z3:
- Forte em **aritmética não-linear**, **bit-vectors**, **arrays**
- Suporte nativo a **interpolação de Craig**
- **Proof production** nativo (DRAT, LFSC)
- **SMT-LIB 2.6** compliant

---

## 📦 Instalação

### Windows (Static Binary)
```powershell
# 1. Baixar
# https://github.com/cvc5/cvc5/releases/latest
# Baixar: cvc5-Win64-x86_64-static.zip

# 2. Extrair
cd C:\Lab
# Extrair cvc5-Win64-x86_64-static.zip -> cvc5\

# 3. Adicionar ao PATH
$env:Path += ";C:\Lab\cvc5\cvc5-Win64-x86_64-static\bin"
```

### Verificação
```powershell
cvc5.exe --version
# cvc5 1.4.2 [git ...]
```

---

## 🔧 Uso Básico

### SMT-LIB Input
```smt2
; script.smt2
(set-logic QF_UFBV)
(declare-fun x () (_ BitVec 32))
(declare-fun y () (_ BitVec 32))
(assert (bvult x y))
(assert (bvugt x #x00000010))
(check-sat)
(get-model)
```

### Execução
```powershell
cvc5.exe --lang smt2 script.smt2
# ou
cvc5.exe --lang smt2 --produce-models script.smt2
```

---

## 🔬 Proof Production

### DRAT Proof
```bash
cvc5.exe --proof=drat --lang smt2 script.smt2
```

### LFSC Proof
```bash
cvc5.exe --proof=lfsc --lang smt2 script.smt2
```

### Python Wrapper
```python
import subprocess
import tempfile

def run_cvc5(smt2_script, proof_mode="drat"):
    """Executa CVC5 com proof production"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.smt2', delete=False) as f:
        f.write(smt2_script)
        smt_file = f.name
    
    proof_file = smt_file + f".{proof_mode}"
    
    cmd = [
        "cvc5.exe",
        f"--proof={proof_mode}",
        "--lang", "smt2",
        smt_file
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout, proof_file
```

---

## 🔬 Interpolação de Craig (CVC5)

### Suporte Nativo
CVC5 tem **suporte nativo completo** para interpolação de Craig:

```bash
# Gera interpolante
cvc5.exe --interpolant=itp --lang smt2 script.smt2
```

### Python Wrapper
```python
def cvc5_interpolation(A, B, shared_vars):
    """
    A ∧ B = UNSAT
    Retorna interpolante I tal que A => I e I ∧ B = UNSAT
    """
    script = f"""
    (set-logic QF_UF)
    {declare_shared_vars(shared_vars)}
    (assert (and {A} {B}))
    (check-sat)
    (get-interpolant)
    """
    
    result = run_cvc5_interpolation(script)
    return parse_interpolant(result)
```

### PPR-3 com CVC5
```python
def cvc5_ppp3(theta_t1, tau_formula_b, R_fn):
    """
    PPR-3 via CVC5 interpolation
    theta: prova em T1 de tau(g_T1)_beta
    Retorna prova em T0 de tau(g_T0)_b
    """
    # 1. Formular tau(g_T1)_beta como SMT-LIB
    smt_beta = tau_to_smt2(tau_formula_b)
    
    # 2. Resolver em T1 (mais forte)
    result = cvc5_check(smt_beta, "T1_axioms")
    
    if unsat:
        # 2. Obter interpolante para T0
        interpolant = cvc5_interpolate(
            A="T1_axioms",
            B=f"(not {tau_to_smt2(tau_formula_b)})",
            shared="shared_vars"
        )
        
        # 3. Traduzir para T0
        proof_t0 = translate_interpolant(interpolant, T0_axioms)
        
        # 4. Verificar bound polinomial
        poly_bound = poly_bound_check(len(interpolant), len(b), n)
        
        return proof_t0
```

---

## 🔧 Python Integration

### Wrapper Class
```python
import subprocess
import tempfile
import os

class CVC5Wrapper:
    def __init__(self, cvc5_path="cvc5.exe"):
        self.cvc5_path = cvc5_path
    
    def solve(self, smt2_script, logic="QF_UF", produce_proof=False, proof_format="drat"):
        """Resolve SMT problem"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.smt2', delete=False) as f:
            f.write(f"(set-logic {logic})\n{smt2_script}")
            smt_file = f.name
        
        cmd = [self.cvc5_path, "--lang", "smt2"]
        if proof_format:
            cmd.extend([f"--proof={proof_format}"])
        cmd.append(smt2_file)
        
        result = subprocess.run(
            [self.cvc5_path, "--lang", "smt2"] + 
            (["--proof=drat"] if produce_proof else []) + 
            [smt2_file],
            capture_output=True, text=True, timeout=60
        )
        
        os.unlink(smt2_file)
        return {
            "sat": "sat" in result.stdout.lower(),
            "unsat": "unsat" in result.stdout.lower(),
            "model": self._parse_model(result.stdout),
            "proof": self._extract_proof(result)
        }
    
    def interpolate(self, A, B, shared_vars):
        """Craig interpolation: A ∧ B = UNSAT => find I"""
        script = f"""
        (set-logic QF_UF)
        ; declare shared variables
        {''.join(f'(declare-fun {v} () Bool)\n' for v in shared_vars)}
        (assert (and {A} {B}))
        (check-sat)
        (get-interpolant)
        """
        return self._get_interpolant(script)
```

---

## 🔬 PPR-3 com CVC5

### Fluxo Completo
```python
def cvc5_ppp3_pipeline(T0, T1, b, R_fn):
    """
    PPR-3 via CVC5:
    1. tau(g_T1)_b em T1 (mais forte)
    2. Interpolante para tau(g_T0)_b em T0
    3. Verificar bound polinomial
    """
    
    # 1. Formula em T1
    smt_t1 = tau_to_smt2(T1, b)
    
    # 2. Check SAT/UNSAT em T1
    result_t1 = cvc5_check(smt_t1, logic="QF_UF", axioms=T1_axioms)
    
    if result_t1 == "unsat":
        # 2. Interpolante para T0
        interpolant = cvc5_interpolate(
            A="T1_axioms",
            B=f"(not {tau_to_smt2(tau_formula_b)})",
            shared="shared_vars"
        )
        
        # 3. Traduzir para T0
        proof_t0 = translate_to_T0(interpolant, T0_axioms)
        
        # 4. Verificar bound polinomial
        poly_bound = poly_bound_check(len(interpolant), len(b), n)
        
        return {
            "interpolant": interpolant,
            "proof_t0": proof_t0,
            "bound_satisfied": len(interpolant) <= poly_bound
        }
    return None
```

---

## 📊 Benchmarking CVC5 vs Z3

```python
def benchmark_cvc5_vs_z3(formulas):
    """Compara CVC5 vs Z3 em tau-formulas"""
    results = {"cvc5": [], "z3": []}
    
    for formula in formulas:
        # CVC5
        t0 = time.time()
        r1 = cvc5_solve(formula)
        results["cvc5"].append(time.time() - t0)
        
        # Z3
        t0 = time.time()
        r2 = z3_solve(formula)
        results["z3"].append(time.time() - t0)
    
    return results
```

---

## 📁 Scripts

```
integrations/cvc5/
├── scripts/
│   ├── cvc5_wrapper.py       # Wrapper Python
│   ├── cvc5_ppp3.py          # PPR-3 pipeline
│   ├── cvc5_interpolate.py   # Interpolação Craig
│   ├── cvc5_hardness.py      # Hardness measurement
│   └── cvc5_vs_z3_bench.py   # Benchmark
├── scripts_smt2/
│   ├── tau_template.smt2     # Template τ-formula
│   ├── interpolation.smt2    # Template interpolação
│   └── hardness_bench.smt2   # Benchmark hardness
└── bin/
    └── cvc5.exe
```

---

## 🚀 Quick Start

```powershell
# 1. Verificar instalação
cvc5.exe --version

# 2. Teste básico
echo "(set-logic QF_UF) (declare-fun x () Bool) (assert x) (check-sat)" | cvc5.exe --lang smt2

# 2. Teste interpolação
echo "(set-logic QF_UF) (declare-fun x () Bool) (declare-fun y () Bool) (assert (and x (not x))) (check-sat) (get-interpolant)" | cvc5.exe --lang smt2 --interpolant=itp

# 3. Teste proof
echo "(set-logic QF_UF) (declare-fun x () Bool) (assert x) (assert (not x)) (check-sat)" | cvc5.exe --lang smt2 --proof=drat
```

---

## 📁 Estrutura

```
integrations/cvc5/
├── bin/
│   └── cvc5.exe
├── scripts/
│   ├── cvc5_wrapper.py
│   ├── cvc5_ppp3.py
│   ├── cvc5_interpolate.py
│   ├── cvc5_hardness.py
│   └── cvc5_vs_z3_bench.py
├── scripts_smt2/
│   ├── tau_template.smt2
│   ├── interpolation.smt2
│   └── hardness_bench.smt2
└── docs/
    └── CVC5_INTEGRATION.md
```

---

## 🔗 Referências

- [CVC5 Website](https://cvc5.github.io/)
- [CVC5 Documentation](https://cvc5.github.io/docs/)
- [CVC5 GitHub](https://github.com/cvc5/cvc5)
- [SMT-LIB Standard](http://smtlib.cs.uiowa.edu/)
- [Craig Interpolation in CVC5](https://cvc5.github.io/docs/interpolation.html)
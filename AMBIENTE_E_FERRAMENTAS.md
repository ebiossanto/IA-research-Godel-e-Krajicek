# AMBIENTE, FERRAMENTAS E PERMISSÕES — Terminal-Laboratório

**Data:** 19/11/2026 · **Máquina:** Windows (usuário `Ebios/Euzebio`) · **Repo:**
`D:\Biblioteca\CyberAmbiente\IA-research-Godel-e-Krajicek`
**Propósito:** estado real das ferramentas, o que foi **restaurado/corrigido hoje**,
o que falta, e como verificar/reproduzir. Complementa `REHYDRATION.md` (guia de
reidratação de máquina limpa) e `PLANO_PESQUISA_E_DESENVOLVIMENTO.md` §6.

---

## 1. Estado das ferramentas (verificado em 19/11/2026)

### 1.1 Núcleo obrigatório — ✅ TODOS FUNCIONAIS

| Ferramenta | Versão | Caminho / Nota |
|---|---|---|
| **Git** | 2.56.0.windows.4 | `C:\Program Files\Git\cmd` — remoto `origin` = `https://github.com/ebiossanto/IA-research-Godel-e-Krajicek.git`, branch `main` |
| **Python** | 3.15.2 | `C:\Python315\python.exe` |
| — z3-solver | 5.4.1 | `import z3` ✅ (motor dos experimentos SAT/SMT) |
| — sympy | 1.14.0 | ✅ **restaurado hoje** (ver §3 — instalação estava adulterada) |
| — numpy / pandas / scipy / matplotlib / networkx | 2.5.4 / 3.1.0 / 1.18.1 / 3.11.2 / 3.7 | ✅ |
| — psutil | 7.2.2 | ✅ |
| — **python-sat (pysat)** | 1.9.dev24 | ✅ **instalado hoje** (usado por 5 scripts `gk_*` e `fractal_engine/integrations/z3_fractal.py`) |
| — mpmath | 1.3.0 | ✅ (dependência do sympy) |
| **Julia** | 1.10.2 | ✅ **restaurada hoje** — `D:\Biblioteca\Desktop-Pessoal\Julia\julia-1.10.2\bin\julia.exe` |
| **Lean 4 / elan / Lake** | Lean 4.34.0 · elan 4.2.4 · Lake 5.0.0 | ✅ toolchain **baixada hoje** em `C:\Users\Euzebio\.elan\` — `lean-toolchain` do repo resolve sozinho |
| **Node.js** | 22.23.4 | ✅ |
| **GitHub CLI** | — | ✅ no PATH |
| **Chocolatey** | — | ✅ `C:\ProgramData\chocolatey\bin` (alternativa ao winget) |

### 1.2 Verificação do build formal (executado hoje)

```powershell
cd D:\Biblioteca\CyberAmbiente\IA-research-Godel-e-Krajicek
& "$env:USERPROFILE\.elan\bin\lake.exe" build
# → Build completed successfully (4 jobs).
#   2 warnings 'declaration uses sorry' (DDP.lean:628 e :690) — PERMANENTES por natureza
```

**Resultado: VERDE** — idêntico ao registrado no `README.md` (reprodução de 12/10/2026).

### 1.3 Opcionais — ❌ NÃO INSTALADOS (instalar sob demanda)

| Ferramenta | Uso no projeto | Como instalar nesta máquina |
|---|---|---|
| **cvc5** | SMT com interpolação nativa | `choco install cvc5` ou zip em <https://github.com/cvc5/cvc5/releases> (ver `REHYDRATION.md` §5) |
| **LTspice** | simulação de hardware (Eixo FCT) | `choco install ltspice` ou ADI site |
| **FreeFEM++** | PDEs / termodinâmica | `choco install freefem` |
| **SageMath** | álgebra simbólica pesada | via WSL (`REHYDRATION.md` §5) |
| **GeoGebra** | visualização | `choco install geogebra` |
| **winget** | gerenciador de pacotes | **ausente nesta máquina** → usar **choco** ou downloads manuais |

> **Nenhum deles é bloqueante** para as frentes ativas (DD_P, δ/𝒢, PPR usam
> Python/Z3/Lean; FCT usa Python/Julia). Instalar apenas quando um experimento exigir.

### 1.4 Itens do `REHYDRATION.md` não aplicáveis aqui

- **Junction `C:\Lab`** → **desnecessária**: o caminho atual
  (`D:\Biblioteca\CyberAmbiente\...`) é ASCII puro; a junction só existia para
  contornar acento no usuário antigo ("Euzébio Soares").
- **Julia 1.13+ via winget** → usamos a **1.10.2 já presente** em
  `Desktop-Pessoal\Julia` (completa e funcional). Atualizar só se um pacote exigir.

---

## 2. Permissões e configuração (o que foi feito hoje)

| Ação | Escopo | Comando | Exige admin? |
|---|---|---|---|
| Git: exceção de diretório seguro (**"dubious ownership"** impedia QUALQUER comando git) | global (usuário) | `git config --global --add safe.directory D:/Biblioteca/CyberAmbiente/IA-research-Godel-e-Krajicek` | ❌ |
| PATH do usuário += `%USERPROFILE%\.elan\bin` | User | `[Environment]::SetEnvironmentVariable("Path", …, "User")` | ❌ |
| PATH do usuário += `D:\Biblioteca\Desktop-Pessoal\Julia\julia-1.10.2\bin` | User | idem | ❌ |
| Instalar `python-sat` | usuário | `pip install python-sat` | ❌ |
| Restaurar sympy oficial | usuário | `pip install --force-reinstall --no-deps sympy==1.14.0` | ❌ |
| Baixar toolchain Lean 4.34 | `%USERPROFILE%\.elan` | automático via `lake build` | ❌ |

> **Nenhuma ação exigiu elevação de administrador.** Sessões novas do terminal
> herdam o PATH atualizado (sessões já abertas precisam reabrir).

---

## 3. Incidente registrado: sympy adulterado (19/11/2026)

**Sintoma:** `import sympy` falhava com
`ImportError: cannot import name 'greeks' from 'std.unicode'`.

**Cadeia de diagnóstico (reproduzível):**

1. O RECORD oficial (`sympy-1.14.0.dist-info/RECORD`) manda:
   `sympy/printing/pretty/pretty_symbology.py` → `sha256=v4FyDz…`, **24112 bytes**.
2. O arquivo local tinha **19559 bytes** e hash `sha256=jubiYr6…` → **modificado**.
3. Comparação com o wheel oficial (`pip download sympy==1.14.0 --no-deps`):
   os arquivos `latex.py`, `pretty_symbology.py`, `stringpict.py`, `pretty.py`
   **divergiam** (ex.: `latex.py` 1985 linhas locais vs **3319** originais) e o
   original **não** contém `std.unicode`.
4. Os arquivos foram alterados em **13/11/2026 15:39**, junto com a instalação do
   pacote PyPI **`std.algorithm` 1.2.9** (autor "Cosmos"), cujo módulo `std/unicode.py`
   **não fornece** `greeks` — ou seja, o "remendo" estava incompleto e quebrou o sympy.

**Correção aplicada:** `pip install --force-reinstall --no-deps sympy==1.14.0`
(oficial do PyPI) + verificação:
```powershell
python -c "import sympy; from sympy import latex, sin, symbols; x=symbols('x'); print(sympy.__version__, latex(sin(x)**2))"
# → 1.14.0  \sin^{2}{\left(x \right)}
```

**Recomendações:**
- Se aparecer de novo: repetir o `--force-reinstall` e checar hash contra o RECORD
  (`Get-FileHash` após converter o base64 do RECORD).
- O pacote `std.algorithm` permanece instalado (é do PyPI e não apresentou código
  hostil na auditoria — só bibliotecas utilitárias); **nada importa dele hoje**.
  Para remover: `pip uninstall -y std.algorithm`.
- **Não** instalar sympy de fontes locais/wheels não oficiais.

---

## 4. Diagnóstico automatizado

Execute:

```powershell
powershell -ExecutionPolicy Bypass -File D:\Biblioteca\CyberAmbiente\IA-research-Godel-e-Krajicek\diagnostico_ambiente.ps1
```

O script verifica: Git (+ safe.directory), Python+pacotes-chave (z3/sympy/psutil/pysat),
Julia, elan/Lake/toolchain, `lake build` (opcional `-Build`), PATH, ferramentas
opcionais (cvc5/LTspice/FreeFEM) e emite ✅/❌ por item.

---

## 5. Checklist de reidratação (máquina nova — resumo executivo)

1. `git clone https://github.com/ebiossanto/IA-research-Godel-e-Krajicek.git`
2. `git config --global --add safe.directory <caminho>` (se dono diferente)
3. Python 3.12+ + `pip install psutil numpy matplotlib z3-solver python-sat sympy scipy pandas`
4. Julia (zip completo!) + PATH
5. `elan` (Windows: `winget install elan` ou zip) — `lake build` na raiz baixa a toolchain
6. Opcionais: cvc5, LTspice, FreeFEM (ver §1.3)
7. Rodar `diagnostico_ambiente.ps1` → tudo ✅

Detalhes e troubleshooting: `REHYDRATION.md`.

---

**Última atualização:** 19/11/2026

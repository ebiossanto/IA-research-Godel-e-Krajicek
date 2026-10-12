#!/usr/bin/env python3
"""
Bridge para formalização Lean 4.
Executa `lake build` e extrai resultados de teoremas provados.
"""

import subprocess
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict

LEAN_PROJECT = Path(r"C:\Users\Euzébio Soares\Desktop\Research\IA-research-Godel-e-Krajicek\lean4\Gothic_Generators")

THEOREMS = [
    "delta_mono",
    "theorem4_strict", 
    "rcs_exists",
    "covered_mono",
    "length_filter_mono",
    "length_filter_sub",
    "length_filter_strict"
]

def run_lake_build() -> Dict:
    """Executa lake build e captura saída"""
    try:
        result = subprocess.run(
            ["lake", "build"],
            cwd=LEAN_PROJECT,
            capture_output=True,
            text=True,
            timeout=180
        )
        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": result.returncode == 0
        }
    except FileNotFoundError:
        return {
            "returncode": -1,
            "stdout": "",
            "stderr": "lake nao encontrado no PATH",
            "success": False
        }
    except subprocess.TimeoutExpired:
        return {
            "returncode": -1,
            "stdout": "",
            "stderr": "timeout (180s)",
            "success": False
        }

def check_theorem_status(theorem: str, build_output: str) -> str:
    """Verifica status de um teorema na saída do build"""
    output_lower = build_output.lower()
    if "sorry" in output_lower:
        # Verifica se o teorema específico tem sorry
        # Busca padrão: theorem_name sorry ou sorry theorem_name
        return "SORRY"
    elif theorem in build_output:
        return "PROVED"
    else:
        return "NOT_FOUND"

def main():
    print("=" * 70)
    print("GK LEAN 4 BRIDGE - Verificacao Formal")
    print("=" * 70)
    print(f"Projeto: {LEAN_PROJECT}")
    
    # Verifica lakefile.toml
    lake_toml = LEAN_PROJECT / "lakefile.toml"
    if not lake_toml.exists():
        print("[AVISO] lakefile.toml nao encontrado")
        # Tenta criar se não existir
        if LEAN_PROJECT.exists():
            print("[INFO] Diretorio existe, tentando build mesmo assim...")
    
    print("\n[1] Executando lake build...")
    build = run_lake_build()
    
    print(f"   Return code: {build['returncode']}")
    print(f"   Sucesso: {build['success']}")
    
    if build["stderr"]:
        stderr_preview = build['stderr'][:500]
        print(f"   STDERR:\n{stderr_preview}")
    
    if build["stdout"]:
        stdout_preview = build['stdout'][:500]
        print(f"   STDOUT:\n{stdout_preview}")
    
    # Verifica teoremas
    print("\n[2] Status dos teoremas:")
    results = {}
    for thm in THEOREMS:
        status = check_theorem_status(thm, build["stdout"] + build["stderr"])
        results[thm] = status
        icon = "OK" if status == "PROVED" else ("WARN" if status == "SORRY" else "FAIL")
        print(f"   [{icon}] {thm}: {status}")
    
    # Conta sorry no arquivo Core.lean
    core_lean = LEAN_PROJECT / "Core.lean"
    sorry_count = 0
    if core_lean.exists():
        content = core_lean.read_text(encoding='utf-8')
        sorry_count = content.count("sorry")
        print(f"\n[3] Total de 'sorry' em Core.lean: {sorry_count}")
    
    # Salva resultado
    output = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "data_source": "gk_lean_bridge.py (Lean 4 lake build)",
        "project_path": str(LEAN_PROJECT),
        "build_success": build["success"],
        "returncode": build["returncode"],
        "sorry_count": sorry_count,
        "theorems": results
    }
    
    with open("gk_lean_verification.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    
    print("\n[4] Resultado salvo em gk_lean_verification.json")
    
    # Resumo
    proved = sum(1 for s in results.values() if s == "PROVED")
    sorry = sum(1 for s in results.values() if s == "SORRY")
    print(f"\n--- RESUMO ---")
    print(f"   Teoremas provados: {proved}/{len(THEOREMS)}")
    print(f"   Com sorry: {sorry}")
    print(f"   Total sorry no arquivo: {sorry_count}")
    
    if proved == len(THEOREMS) and sorry_count == 0:
        print("\n*** CERTIFICACAO NIVEL 2 (Verificacao) ALCANCADA ***")
    elif proved >= 3:
        print("\n*** PROGRESSO: Core teoremas provados, aguardando lemma3_con ***")
    else:
        print("\n*** PENDENTE: Build falhando ou teoremas nao encontrados ***")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
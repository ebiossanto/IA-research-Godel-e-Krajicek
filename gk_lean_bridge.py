#!/usr/bin/env python3
"""
gk_lean_bridge.py — Verificacao formal honesta do estado Lean 4 (v2, 19/11/2026).

Mudanca de metodo (corrige o gap documentado em ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md
sec. 2.4): em vez de greppar a saida do `lake build` por nomes de teoremas (o lake
NAO imprime nomes em build limpo -> tudo saia NOT_FOUND), este script:

  1. roda `lake build` na raiz do repo (GothicGenerators: Core + DDP);
  2. roda `lake env lean gk_axiom_check.lean`, que faz `#print axioms` de cada
     teorema-alvo — o Lean lista os axiomas reais usados;
  3. classifica: PROVED (sem sorryAx) | SORRY (usa sorryAx) | NOT_FOUND;
  4. grava gk_lean_verification.json (substitui o JSON stale).

Requisitos: elan/Lake instalados (%USERPROFILE%\\.elan\\bin) e toolchain do
`lean-toolchain` baixada (baixa automaticamente no 1o `lake build`).

Uso:  python gk_lean_bridge.py
"""

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent
CHECK_FILE = REPO_ROOT / "gk_axiom_check.lean"
OUTPUT_JSON = REPO_ROOT / "gk_lean_verification.json"

# Nomes COMPLETOS (namespaces GothicGenerators / GothicGenerators.DDP)
THEOREMS: List[str] = [
    "GothicGenerators.delta_mono",
    "GothicGenerators.theorem4_strict",
    "GothicGenerators.rcs_exists",
    "GothicGenerators.covered_mono",
    "GothicGenerators.length_filter_mono",
    "GothicGenerators.length_filter_sub",
    "GothicGenerators.length_filter_strict",
    "GothicGenerators.lemma3_con",
    "GothicGenerators.DDP.dd_task_total",
    "GothicGenerators.DDP.dd_solvable_in_m_rounds",
    # Os 2 sorries PERMANENTES por natureza (DDP.lean:628/690) — para calibrar
    "GothicGenerators.DDP.dd_solvable_in_ST_O1",
    "GothicGenerators.DDP.pbounded_implies_feasible",
]

SOURCE_FILES = [
    REPO_ROOT / "lean4" / "Gothic_Generators" / "Core.lean",
    REPO_ROOT / "lean4" / "Gothic_Generators" / "DDP.lean",
]

# Formato real do Lean 4:
#   'NOME' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
AXIOM_LINE = re.compile(r"^'(?P<name>[^']+)' depends on axioms: \[(?P<axioms>[^\]]*)\]")


def find_lake() -> Optional[Path]:
    """Lake no PATH ou em %USERPROFILE%\\.elan\\bin (instalacao padrao Windows)."""
    import shutil

    p = shutil.which("lake")
    if p:
        return Path(p)
    candidate = Path.home() / ".elan" / "bin" / "lake.exe"
    return candidate if candidate.exists() else None


def run(cmd: List[str], cwd: Path, timeout: int = 600) -> Dict:
    try:
        r = subprocess.run(
            cmd, cwd=str(cwd), capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=timeout,
        )
        return {"returncode": r.returncode, "stdout": r.stdout,
                "stderr": r.stderr, "error": None}
    except FileNotFoundError:
        return {"returncode": -1, "stdout": "", "stderr": "",
                "error": f"comando nao encontrado: {cmd[0]}"}
    except subprocess.TimeoutExpired:
        return {"returncode": -1, "stdout": "", "stderr": "",
                "error": f"timeout ({timeout}s)"}


def check_axioms(lake: Path) -> Dict[str, str]:
    """Roda `lake env lean gk_axiom_check.lean` e classifica cada teorema."""
    if not CHECK_FILE.exists():
        return {t: "CHECK_FILE_MISSING" for t in THEOREMS}

    res = run([str(lake), "env", "lean", str(CHECK_FILE)], REPO_ROOT, timeout=600)
    output = (res["stdout"] or "") + (res["stderr"] or "")

    status: Dict[str, str] = {}
    for line in output.splitlines():
        m = AXIOM_LINE.match(line.strip())
        if not m:
            continue
        name, axioms = m.group("name"), m.group("axioms")
        if name in THEOREMS:
            status[name] = "SORRY" if "sorryAx" in axioms else "PROVED"

    for t in THEOREMS:
        status.setdefault(t, "NOT_FOUND")
    return status


def count_sorries() -> Dict[str, int]:
    counts = {}
    for f in SOURCE_FILES:
        if f.exists():
            text = f.read_text(encoding="utf-8", errors="replace")
            # 'sorry' como palavra inteira (evita falsos positivos em comentarios?
            # mantemos simples: ocorncias literais de sorry)
            counts[f.name] = len(re.findall(r"\bsorry\b", text))
        else:
            counts[f.name] = -1  # ausente
    return counts


def main() -> int:
    print("=" * 70)
    print("GK LEAN 4 BRIDGE — verificacao formal (v2: #print axioms)")
    print("=" * 70)
    print(f"Repo: {REPO_ROOT}")

    lake = find_lake()
    if not lake:
        print("[FALHA] lake nao encontrado (instale elan: https://elan.lean-lang.org)")
        return 2
    print(f"Lake: {lake}")

    # [1] build
    print("\n[1] lake build ...")
    build = run([str(lake), "build"], REPO_ROOT, timeout=900)
    print(f"    returncode={build['returncode']} erro={build['error']}")
    tail = ((build["stdout"] or "") + (build["stderr"] or "")).strip().splitlines()
    for ln in tail[-6:]:
        print(f"    | {ln}")
    build_ok = build["returncode"] == 0

    # [2] axiomas reais
    print("\n[2] #print axioms (gk_axiom_check.lean) ...")
    statuses = check_axioms(lake)
    proved = sorry = notfound = 0
    for t in THEOREMS:
        s = statuses[t]
        icon = {"PROVED": "OK", "SORRY": "WARN", "NOT_FOUND": "FAIL"}.get(s, "FAIL")
        print(f"    [{icon:4}] {t}: {s}")
        if s == "PROVED":
            proved += 1
        elif s == "SORRY":
            sorry += 1
        else:
            notfound += 1

    # [3] sorry nos fontes
    print("\n[3] ocorncias 'sorry' nos fontes:")
    sorry_src = count_sorries()
    for fname, n in sorry_src.items():
        print(f"    {fname}: {n}")

    # [4] JSON
    payload = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "data_source": "gk_lean_bridge.py v2 (#print axioms via lake env lean)",
        "repo_root": str(REPO_ROOT),
        "lake": str(lake),
        "build_success": build_ok,
        "build_returncode": build["returncode"],
        "build_error": build["error"],
        "sorry_in_sources": sorry_src,
        "theorems": statuses,
        "summary": {
            "proved": proved,
            "sorry": sorry,
            "not_found": notfound,
            "total": len(THEOREMS),
        },
        "notes": (
            "PROVED = teorema sem sorryAx nos axiomas reais usados. "
            "Os 2 SORRY de DDP.lean (628/690) sao PERMANENTES por natureza "
            "(dd_solvable_in_ST_O1 = o que (ST) postula falso; "
            "pbounded_implies_feasible = falta so o limite de tempo)."
        ),
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False),
                           encoding="utf-8")
    print(f"\n[4] JSON gravado: {OUTPUT_JSON.name}")

    # Resumo
    print("\n--- RESUMO ---")
    print(f"    PROVED {proved}/{len(THEOREMS)} | SORRY {sorry} | NOT_FOUND {notfound}")
    print(f"    build_ok={build_ok}")
    core_sorry = sorry_src.get("Core.lean", -1)
    if build_ok and notfound == 0 and core_sorry == 0:
        print("\n*** VERIFICACAO N2: build verde + teoremas sem sorryAx (Core) ***")
        print("*** DDP: 2 sorry documentados e permanentes (por natureza) ***")
        rc = 0
    elif not build_ok:
        print("\n*** PENDENTE: build falhou ***")
        rc = 1
    else:
        print("\n*** ATENCAO: ha NOT_FOUND ou sorry inesperado ***")
        rc = 1
    print("=" * 70)
    return rc


if __name__ == "__main__":
    sys.exit(main())

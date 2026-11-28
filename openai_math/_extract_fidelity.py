"""Extrai famílias de lógica e TCS da fidelity table (varredura openai/math)."""
import csv
import pathlib

rows = list(csv.DictReader(pathlib.Path("openai_math/fidelity-table.csv").open(encoding="utf-8")))
print("total familias revisadas:", len(rows))

for subject in ("Mathematical logic", "Theoretical computer science"):
    sel = [r for r in rows if r["subject"] == subject]
    print(f"\n=== {subject} ({len(sel)}) ===")
    for r in sel:
        print(f"  {r['family']} [{r['verdict']:7}] {r['title'][:88]}")
        if subject == "Mathematical logic":
            print(f"       check={r['machine_check']} | challenges={r['challenges'][:70]}")

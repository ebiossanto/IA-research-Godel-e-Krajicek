#!/usr/bin/env python3
"""Extrai IDs de lemas (L-pcx/L-clb/L-meta/L-lib/L-alg) dos snapshots baixados do
pequalnp.com, para a tabela de PEQUALNP_MAPA.md.

Fontes (sha256 registrados em MAPEAMENTO_DDP_vs_PEqualNP.md §0):
  plan.json      -> targets, chains e hard_links por programa (com status)
  overview.json  -> linhas de ataque e suas rows (com status da linha)

Uso: python pequalnp/extract_ids.py          # tabelas markdown no stdout
"""
import json
import pathlib
import sys

BASE = pathlib.Path(__file__).resolve().parent
ENC = "utf-8"


def load(name: str) -> dict:
    return json.loads((BASE / name).read_text(encoding=ENC))


def main() -> int:
    plan, ov = load("plan.json"), load("overview.json")

    # ---- índice plan.json: lemma_id -> (programas, título, status, origem)
    by_id: dict[str, dict] = {}

    def put(lid: str, sn: str, title, status, where: str) -> None:
        e = by_id.get(lid)
        if e is None:
            by_id[lid] = {"prog": [sn], "title": title, "status": status, "where": where}
        else:
            if sn not in e["prog"]:
                e["prog"].append(sn)  # mesmo lemma em várias cadeias (ex.: L-pcx-022)

    for key, prog in plan.get("programs", {}).items():
        sn = prog.get("short_name", key)
        target = prog.get("target") or {}
        if target.get("lemma_id"):
            put(target["lemma_id"], sn, target.get("title"), target.get("status"), "target")
        for row in prog.get("chain", []):
            if not row.get("lemma_id"):
                continue  # row de contexto sem id (ex.: legenda de cadeia)
            put(row["lemma_id"], sn, row.get("title"), row.get("status"), "chain")
        hl = prog.get("hard_link") or {}
        if hl.get("lemma_id"):
            put(hl["lemma_id"], sn, hl.get("title"), hl.get("status"), "hard_link")

    # ---- índice overview.json: row -> linha de ataque
    attack_rows: dict[str, dict] = {}
    for line in ov.get("attack", []):
        for r in line.get("rows", []):
            attack_rows[r] = {
                "line": line["id"], "line_status": line.get("status"),
                "title": line.get("title"), "program": line.get("program"),
            }

    prefixes = sys.argv[1:] or ["L-pcx", "L-clb", "L-meta", "L-lib", "L-alg"]
    print("| ID | Programa | Título (fonte) | Status (deles) | Onde no registro |")
    print("|---|---|---|---|---|")
    for pref in prefixes:
        ids = sorted({i for i in (set(by_id) | set(attack_rows)) if i.startswith(pref)})
        for lid in ids:
            p, a = by_id.get(lid), attack_rows.get(lid)
            title = (p or a)["title"] or ""
            prog = " / ".join((p or {}).get("prog", [])) or (a or {}).get("program") or ""
            status = (p or {}).get("status") or (
                f"row de linha '{a['line']}' (status da linha: {a['line_status']})"
                if a else "?")
            where = (p or {}).get("where") or ("attack/rows" if a else "?")
            title = title.replace("|", "/").replace("\n", " ")
            print(f"| `{lid}` | {prog} | {title} | {status} | {where} |")
        print(f"<!-- fim {pref}: {len(ids)} ids -->", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

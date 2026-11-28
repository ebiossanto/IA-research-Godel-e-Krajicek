"""Extrai letters + news (com dek/covers) para a varredura 27/11."""
import json
import pathlib

B = pathlib.Path("pequalnp")

let = json.loads((B / "letters_novo.json").read_text(encoding="utf-8"))["letters"]
print("=== LETTERS ===")
for l in let:
    print(f"  {l['id']} [{l['status']}] {l['topic'][:75]}")
    if l.get("reply"):
        print("    reply:", str(l["reply"])[:220])
    print("    outcome:", str(l.get("outcome"))[:220])

n = json.loads((B / "news_novo.json").read_text(encoding="utf-8"))["articles"]
print("\n=== NEWS (16 mais recentes) ===")
for a in n[:16]:
    print(f"  {a['id']} {a['published_at'][:16]} [{a['program'][:4]}] {a['title'][:66]}")
    print(f"      covers={a.get('covers')} | {a['dek'][:160]}")
    print(f"      file={a.get('file')}")

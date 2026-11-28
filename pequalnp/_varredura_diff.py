"""Varredura 27/11/2026: diff dos snapshots pequalnp (26/11 -> 27/11)."""
import json
import pathlib

B = pathlib.Path("pequalnp")


def load(n):
    return json.loads((B / n).read_text(encoding="utf-8"))


old_ov, new_ov = load("overview.json"), load("overview_novo.json")
old_pl, new_pl = load("plan.json"), load("plan_novo.json")

print("=== PROGRAMAS (overview) ===")
newp = {p["id"]: p["counts"] for p in new_ov["programs"]}
for p in old_ov["programs"]:
    o = p["counts"]
    n = newp.get(p["id"], {})
    d = {k: (n.get(k, 0) - o.get(k, 0)) for k in set(o) | set(n) if n.get(k, 0) != o.get(k, 0)}
    print(f"  {p['id']:20} {d if d else 'sem mudanca'}")

print("\n=== LINHAS DE ATAQUE ===")
old_a = {l["id"]: l for l in old_ov["attack"]}
new_a = {l["id"]: l for l in new_ov["attack"]}
for i in new_a.keys() - old_a.keys():
    print(f"  NOVA: {i} [{new_a[i]['status']}] {new_a[i]['title'][:70]}")
for i in old_a.keys() - new_a.keys():
    print(f"  REMOVIDA: {i}")
for i in old_a.keys() & new_a.keys():
    if old_a[i]["status"] != new_a[i]["status"]:
        print(f"  STATUS: {i}: {old_a[i]['status']} -> {new_a[i]['status']}")
    ro, rn = set(old_a[i].get("rows", [])), set(new_a[i].get("rows", []))
    if rn - ro:
        print(f"  +rows em {i}: {sorted(rn - ro)}")

print("\n=== PLAN (targets/hard links) ===")
for k in old_pl["programs"]:
    o, n = old_pl["programs"][k], new_pl["programs"].get(k, {})
    ot, nt = (o.get("target") or {}), (n.get("target") or {})
    if ot.get("status") != nt.get("status"):
        print(f"  target {k}: {ot.get('status')} -> {nt.get('status')}")
    oh, nh = (o.get("hard_link") or {}), (n.get("hard_link") or {})
    if (oh.get("status"), oh.get("title")) != (nh.get("status"), nh.get("title")):
        print(f"  hard_link {k}: {oh.get('status')} -> {nh.get('status')}")
        if oh.get("title") != nh.get("title"):
            print(f"     novo enunciado: {(nh.get('title') or '')[:120]}")
    oc = {r.get("lemma_id") for r in o.get("chain", [])}
    nc = {r.get("lemma_id") for r in n.get("chain", [])}
    if nc - oc:
        print(f"  +chain {k}: {sorted(nc - oc)}")
    if oc - nc:
        print(f"  -chain {k}: {sorted(oc - nc)}")
print(f"  kills: {old_pl.get('kills')} -> {new_pl.get('kills')}")

print("\n=== PAPERS ===")
old_p = load("papers.json")
print("  papers.json NOVO = mesmo arquivo do 26/11 (hash igual no head.json) -> sem Note 2")
print(f"  (26/11: {[p['id'] for p in old_p['papers']]})")

print("\n=== ELIMINATED ===")
print(" ", (B / "eliminated_novo.json").read_text(encoding="utf-8")[:300])

print("\n=== NEWS (titulos) ===")
news = load("news_novo.json")
items = news.get("news") or news.get("items") or news
if isinstance(items, list):
    for it in items[:12]:
        print(f"  - {str(it.get('at', it.get('date', '')))[:10]} | "
              f"{str(it.get('title') or it.get('text', ''))[:90]}")
else:
    print("  chaves:", list(news.keys()))

print("\n=== LETTERS ===")
let = load("letters_novo.json")
ls = let.get("letters", let if isinstance(let, list) else [])
for l in (ls if isinstance(ls, list) else [])[:8]:
    print("  -", {k: str(v)[:80] for k, v in l.items() if k in
                 ("at", "date", "to", "subject", "status", "title")})

print("\n=== GRAVEYARD (resumo) ===")
gy = load("graveyard_novo.json")
ent = gy.get("entries") or []
print(f"  entradas: {len(ent)}")
from collections import Counter
codes = Counter(e[1] if isinstance(e, list) and len(e) > 1 else "?" for e in ent)
print(f"  codigos: {dict(codes)}")
ts = [e[3] for e in ent if isinstance(e, list) and len(e) > 3 and isinstance(e[3], int)]
if ts:
    import datetime as dt
    print(f"  periodo: {dt.datetime.utcfromtimestamp(min(ts)).date()} .. "
          f"{dt.datetime.utcfromtimestamp(max(ts)).date()}")
pref = Counter(e[0].rsplit("-", 1)[0] for e in ent if isinstance(e, list) and e)
print("  por serie:", dict(pref.most_common(8)))

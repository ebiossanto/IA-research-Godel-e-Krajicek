#!/usr/bin/env python3
"""
ROTINA DE VARREDURA pequalnp.com — executar no INÍCIO DE CADA SESSÃO (AGENTS.md §4).

O que faz (stdlib only, ~2 min):
  1. Baixa https://data.pequalnp.com/head.json (contadores + mapa de arquivos versionados).
  2. Compara com a última execução (pequalnp/last_state.json) e imprime deltas de contadores.
  3. Baixa SÓ os arquivos cujo hash mudou para pequalnp/daily/<YYYY-MM-DD>_<nome>.json
     (arquivo novo = evidência versionada; o anterior fica preservado).
  4. Diffs de conteúdo: overview (programas + status das linhas de ataque), plan/plan_v2
     (targets, ruled_out, decisions), news (artigos novos), letters (respostas novas).
  5. ALERTAS:
       * files.papers com hash NOVO ....... saiu NOTE (novo paper) -> baixar e ler
       * plan_v2 mudou .................... estratégia/cemitério novos (RULED_OUT)
       * letters com status replied ....... resposta de especialista disponível
  6. Atualiza last_state.json.

Uso:  python pequalnp/varredura.py
Dados relevantes para o projeto: anotar em pequalnp/VARREDURA_<data>.md + INDICE.md,
classificando como (A)/(A)-nc/(C). Sem deltas => só imprime "sem mudancas".
"""
import datetime as dt
import hashlib
import json
import pathlib
import sys
import urllib.request

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

BASE = "https://data.pequalnp.com/"
ROOT = pathlib.Path(__file__).resolve().parent          # pequalnp/
DAILY = ROOT / "daily"
STATE = ROOT / "last_state.json"
UA = {"User-Agent": "gk-varredura/1.0 (repositorio IA-research-Godel-e-Krajicek)"}

# nome lógico -> chave em head["files"]
FILES = {
    "overview": "map", "plan": "plan", "plan_v2": "plan_v2", "papers": "papers",
    "news": "news", "letters": "letters", "graveyard": "graveyard",
    "eliminated": "eliminated", "atlas": "atlas", "vocabulary": "vocabulary",
}
KEY_COUNTERS = ("checked", "conjecture", "refuted", "lemmas", "checked_last_hour",
                "messages_today")


def fetch(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def embedded_hash(rel_path: str) -> str | None:
    """'data/map/overview.124a0b784e1c.json' -> '124a0b784e1c' (hash embutido no nome)."""
    name = rel_path.rsplit("/", 1)[-1]
    parts = name.split(".")
    return parts[-2] if len(parts) >= 3 else None


def load(p: pathlib.Path):
    return json.loads(p.read_text(encoding="utf-8"))


def diff_overview(old: dict, new: dict) -> list[str]:
    out = []
    newp = {p["id"]: p["counts"] for p in new.get("programs", [])}
    for p in old.get("programs", []):
        o, n = p["counts"], newp.get(p["id"], {})
        d = {k: n.get(k, 0) - o.get(k, 0) for k in set(o) | set(n)
             if n.get(k, 0) != o.get(k, 0)}
        if d:
            out.append(f"  programa {p['id']}: {d}")
    oa = {l["id"]: l for l in old.get("attack", [])}
    na = {l["id"]: l for l in new.get("attack", [])}
    for i in sorted(na.keys() - oa.keys()):
        out.append(f"  NOVA linha: {i} [{na[i]['status']}] {na[i].get('title', '')[:60]}")
    for i in sorted(oa.keys() - na.keys()):
        out.append(f"  linha removida: {i}")
    for i in sorted(oa.keys() & na.keys()):
        if oa[i]["status"] != na[i]["status"]:
            out.append(f"  STATUS {i}: {oa[i]['status']} -> {na[i]['status']}")
        add = sorted(set(na[i].get("rows", [])) - set(oa[i].get("rows", [])))
        if add:
            out.append(f"  +rows {i}: {add[:12]}")
    return out


def diff_news(old: dict, new: dict) -> list[str]:
    """Artigos novos = ids em `new` ausentes de `old` — lista COMPLETA
    (bug28/11: o codigo inline usava [:8] e imprimia so8/24; extraido
    p/ teste offline). Ordenado por published_at (crescente)."""
    oa = {a["id"] for a in (old.get("articles") or [])}
    novos = sorted((a for a in (new.get("articles") or [])
                    if a["id"] not in oa),
                   key=lambda a: a.get("published_at") or "")
    out = []
    for a in novos:
        out.append(f"  artigo novo: {a['id']} {a.get('published_at', '')[:16]} "
                   f"| {a.get('title', '')[:64]} | covers={a.get('covers')}")
    if novos:
        out.append(f"  (total de artigos novos desde o snapshot anterior: "
                  f"{len(novos)})")
    return out


def diff_plan(old: dict, new: dict) -> list[str]:
    out = []
    for k in (old.get("programs") or {}):
        o = (old["programs"][k] or {})
        n = (new.get("programs", {}).get(k) or {})
        ot, nt = (o.get("target") or {}), (n.get("target") or {})
        if ot.get("status") != nt.get("status"):
            out.append(f"  target {k}: {ot.get('status')} -> {nt.get('status')}")
        oh, nh = (o.get("hard_link") or {}), (n.get("hard_link") or {})
        if oh.get("status") != nh.get("status"):
            out.append(f"  hard_link {k}: {oh.get('status')} -> {nh.get('status')}")
    ok = {(r.get("what") or "")[:70] for r in (old.get("ruled_out") or [])}
    nk = {(r.get("what") or "")[:70] for r in (new.get("ruled_out") or [])}
    for w in sorted(nk - ok):
        out.append(f"  RULED_OUT novo: {w}")
    odec = {(d.get("what") or "")[:70] for d in (old.get("decisions") or [])}
    ndec = {(d.get("what") or "")[:70] for d in (new.get("decisions") or [])}
    for w in sorted(ndec - odec):
        out.append(f"  DECISÃO nova: {w}")
    return out


def main() -> int:
    DAILY.mkdir(exist_ok=True)
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    head = json.loads(fetch(BASE + "head.json"))
    counters = head.get("counters", {})
    files = head.get("files", {})
    prev = load(STATE) if STATE.exists() else None

    print("=" * 68)
    print(f"VARREDURA PNP — {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%MZ')}"
          + ("  [PRIMEIRA EXECUCAO: baseline]" if prev is None else ""))
    print("=" * 68)

    # 1) contadores
    pc = (prev or {}).get("counters", {})
    for k in KEY_COUNTERS:
        v, pv = counters.get(k), pc.get(k)
        delta = f" ({v - pv:+d})" if isinstance(v, int) and isinstance(pv, int) else ""
        print(f"  {k}: {v}{delta}")

    # 2) arquivos alterados (o valor em head.files é o CAMINHO; o hash é embutido no nome)
    changed, alerts = [], []
    pf = (prev or {}).get("files", {})
    for name, key in FILES.items():
        h = files.get(key)
        if not h:
            continue
        if pf.get(name) != h:
            changed.append((name, key, h))
            # alertas só fazem sentido a partir da 2ª execucao (baseline nao e mudanca)
            if prev is not None:
                if name == "papers":
                    alerts.append("*** NOVO PAPER (hash de papers mudou) — baixar e ler! ***")
                elif name == "plan_v2":
                    alerts.append("*** plan_v2 mudou — RULED_OUT/DECISÕES novos possíveis ***")
                elif name == "letters":
                    alerts.append("*** letters mudou — verificar respostas (status replied) ***")

    # 3) downloads + diffs de conteúdo
    for name, key, h in changed:
        rel = files[key]
        data = fetch(BASE + rel)
        dest = DAILY / f"{today}_{name}.json"
        dest.write_bytes(data)
        print(f"  salvo: daily/{dest.name} ({len(data)} B)")
        # integridade: hash embutido no nome do arquivo versionado (12 hex)
        eh = embedded_hash(rel)
        if eh and not sha(data).startswith(eh):
            alerts.append(f"AVISO: integridade de {name} falhou (esperado {eh}…)")
        # diff de conteudo contra o snapshot anterior deste mesmo arquivo
        others = sorted(p for p in DAILY.glob(f"*_{name}.json") if p != dest)
        if others:
            try:
                old = load(others[-1])
                new = load(dest)
                if name == "overview":
                    for line in diff_overview(old, new):
                        print(line)
                elif name in ("plan", "plan_v2"):
                    for line in diff_plan(old, new):
                        print(line)
                elif name == "news":
                    for line in diff_news(old, new):
                        print(line)
                elif name == "letters":
                    st = {l["id"]: l["status"] for l in (old.get("letters") or [])}
                    for l in (new.get("letters") or []):
                        if st.get(l["id"]) != l["status"]:
                            print(f"  LETTER {l['id']}: {st.get(l['id'])} -> {l['status']} "
                                  f"| {l.get('topic', '')[:60]}")
            except Exception as e:  # noqa: BLE001
                print(f"  (diff de {name} falhou: {e})")

    # 4) estado
    STATE.write_text(json.dumps({
        "run_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "files": {n: files.get(k) for n, k in FILES.items() if files.get(k)},
        "counters": {k: counters.get(k) for k in KEY_COUNTERS},
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    if alerts:
        print("-" * 68)
        for a in alerts:
            print("  " + a)
    if not changed and prev is not None:
        print("  sem mudancas desde a ultima execucao")
    print("-" * 68)
    print("estado atualizado: pequalnp/last_state.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

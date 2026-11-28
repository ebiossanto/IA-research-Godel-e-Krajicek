"""Verifica (adversarial) o que os preprints 2604.04830 e 2607.13540 realmente dizem."""
import pathlib
import re

KEYS = ["2506.20221", "student-teacher", "student–teacher", "DD_P", "DD P",
        "weak feasible disjunction", "weak feasible", "resolution",
        "disjoint disjunction", "Ilango", "Ren et al", "gadget generator",
        "proof complexity generators", "NW generator", "range avoidance"]


def visible(p: pathlib.Path) -> str:
    s = p.read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s


for name in ("arxiv_2604.04830v3.html", "arxiv_2607.13540v1.html"):
    t = visible(pathlib.Path("krajicek_ddp/fontes") / name)
    print("=" * 70)
    print(name, "|", len(t), "chars visíveis")
    for k in KEYS:
        idxs = [m.start() for m in re.finditer(re.escape(k), t, re.I)]
        if idxs:
            print(f"  [{k}] {len(idxs)}x")
            for i in idxs[:2]:
                print("      …" + t[max(0, i - 90):i + 130].strip() + "…")

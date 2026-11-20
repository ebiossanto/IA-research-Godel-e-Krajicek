"""Testes de regressao do gk_dd_cert (rodar: python gk_dd_cert_test.py).
Cobre: extract (saturacao e DRAT), verify roundtrip, deteccao de
certificado adulterado, hipoteses do Teorema 4.3, violacao G1 em Res(k)."""
import json
import subprocess
import sys
from pathlib import Path

PY = sys.executable


def run(args):
    return subprocess.run([PY, "gk_dd_cert.py"] + args,
                          capture_output=True, text=True)


def main():
    fails = []

    # T1: extract via saturacao + verify
    Path("_t1_in.json").write_text(json.dumps(
        {"engine": "resolution", "sides": [[[1], [-1]], [[3, 4]]]}),
        encoding="utf-8")
    r = run(["extract", "_t1_in.json", "-o", "_t1_cert.json"])
    ok = r.returncode == 0 and "lado 0" in r.stdout
    print(f"[{'OK' if ok else 'FALHA'}] T1 extract/saturacao")
    if not ok:
        fails.append("T1")
    r = run(["verify", "_t1_cert.json"])
    ok = r.returncode == 0 and "ACEITO" in r.stdout
    print(f"[{'OK' if ok else 'FALHA'}] T1 verify roundtrip")
    if not ok:
        fails.append("T1v")

    # T2: extract via DRAT real (Cadical) + meta.source=drat
    from pysat.solvers import Cadical195
    g = [[1, 2], [1, -2], [-1]]
    with Cadical195(bootstrap_with=g, with_proof=True) as s:
        assert not s.solve()
        adds = [ln for ln in (s.get_proof() or []) if ln.strip()
                and ln.strip()[0] not in "dD"]
    assert adds, "sem adicoes DRAT"
    Path("_t2_in.json").write_text(json.dumps(
        {"engine": "resolution", "sides": [g, [[3, 4]]], "drat": adds}),
        encoding="utf-8")
    r = run(["extract", "_t2_in.json", "-o", "_t2_cert.json"])
    ok = r.returncode == 0
    print(f"[{'OK' if ok else 'FALHA'}] T2 extract/DRAT ({len(adds)} adicoes)")
    if not ok:
        fails.append("T2")
    else:
        cert = json.loads(Path("_t2_cert.json").read_text(encoding="utf-8"))
        ok = cert["meta"].get("source") == "drat" and cert["side"] == 0
        print(f"[{'OK' if ok else 'FALHA'}] T2 meta.source=drat, lado 0")
        if not ok:
            fails.append("T2m")

    # T3: certificado ADULTERADO deve ser recusado
    cert = json.loads(Path("_t1_cert.json").read_text(encoding="utf-8"))
    cert["steps"][-1]["line"] = [[1]]           # raiz deixa de ser vazia
    Path("_t3_bad.json").write_text(json.dumps(cert), encoding="utf-8")
    r = run(["verify", "_t3_bad.json"])
    ok = r.returncode == 1
    print(f"[{'OK' if ok else 'FALHA'}] T3 adulteracao RECUSADA")
    if not ok:
        fails.append("T3")

    # T4: lados nao-disjuntos -> rejeitado (hipotese do Teorema 4.3)
    Path("_t4_in.json").write_text(json.dumps(
        {"engine": "resolution", "sides": [[[1]], [[-1]]]}),
        encoding="utf-8")
    r = run(["extract", "_t4_in.json", "-o", "_t4_cert.json"])
    ok = r.returncode != 0 and "disjuntos" in (r.stdout + r.stderr)
    print(f"[{'OK' if ok else 'FALHA'}] T4 lados nao-disjuntos rejeitados")
    if not ok:
        fails.append("T4")

    # T5: demo completa (4 casos + verificacao)
    r = run(["demo"])
    ok = r.returncode == 0 and "DEMO OK" in r.stdout
    print(f"[{'OK' if ok else 'FALHA'}] T5 demo 4 casos")
    if not ok:
        fails.append("T5")

    # limpeza
    for f in ["_t1_in.json", "_t1_cert.json", "_t2_in.json",
              "_t2_cert.json", "_t3_bad.json", "_t4_in.json"]:
        Path(f).unlink(missing_ok=True)

    print("-" * 60)
    if fails:
        print(f"FALHAS: {fails}")
        return 1
    print("*** TODOS OS TESTES OK ***")
    return 0


if __name__ == "__main__":
    sys.exit(main())

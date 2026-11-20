#!/usr/bin/env python3
"""
gk_dd_cert.py — EXTRATOR DE CERTIFICADOS DD: o teorema DD_Res ∈ P
(C_disjuncao_viavel.md, Teorema 4.3) virando EXECUTAVEL.

Entrada:  lados Λ_1..Λ_m (CNFs, variaveis disjuntas) + (uma destas):
            - provador proprio (saturacao de resolucao com pais gravados)
            - DAG nativo (JSON, passos com justificativas)
            - prova DRAT ASCII (extracao de dependencias via UP)
          ou, para Res(k), um DAG de regras de Garlík (leaf/weaken/cut/and)
Saida:    CERTIFICADO JSON: lado i* + sub-derivacao PURA verificavel
            (toda linha só com variáveis de X_{i*}, folhas ∈ Λ_{i*}, raiz ∅,
             ≤ |π| linhas)
          ou RELATORIO DE VIOLACAO (Res(k): localiza a linha e o motivo —
            ex.: G1 retencao parcial de bloco — o detector automatico do r2)

Verificador INDEPENDENTE (modo `verify`): recheca o certificado sem
importar a logica do extrator — a piece que o auditor externo roda.

Modos:
  python gk_dd_cert.py demo             # 4 casos (resolucao x2, resk x2)
  python gk_dd_cert.py extract IN.json  # extrair certificado
  python gk_dd_cert.py verify CERT.json # verificar (exit 0/1)

Escopo honesto: instancias de fecho pequeno (cap do provador); resolucao
incondicional (Teo 4.3); Res(k) CONDICIONAL a promessa (violação = saida
legitima); nada de claims de complexidade.
"""

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from gk_c2_projection_sim import (
    Dag, run_projection, accessible, check_extraction,
    build_counterexample, block_of,
)

CLOSURE_CAP = 4000          # fecho maximo do provador proprio


# =====================================================================
# Motor RESOLUCAO — provador (saturacao com pais) + Teorema 4.3 (E-pass)
# =====================================================================
def saturate_with_parents(leaves_clauses):
    """Saturacao de resolucao (sem tautologias) gravando pais.
    Retorna lista de nos: {id, kind, clause, prems, side?} ou None se
    nao chega em vazio (satisfativel). leaves_clauses: [(clause, side)]."""
    nodes = []
    index = {}
    def add(clause, kind, prems, side=None):
        if clause in index:
            return index[clause]
        nid = len(nodes)
        nodes.append({"id": nid, "kind": kind, "clause": frozenset(clause),
                      "prems": prems, "side": side})
        index[clause] = nid
        return nid
    for cl, side in leaves_clauses:
        add(cl, "leaf", [], side)
    changed = True
    while changed:
        changed = False
        ids = list(index)
        for c1 in ids:
            for c2 in ids:
                if c1 == c2:
                    continue
                s1, s2 = set(c1), set(c2)
                for l in sorted(s1):
                    if -l in s2:
                        res = frozenset((s1 - {l}) | (s2 - {-l}))
                        if any(-x in res for x in res):
                            continue
                        if res not in index:
                            add(res, "resolve", [index[c1], index[c2]])
                            changed = True
                            if res == frozenset():
                                return nodes
        if len(index) > CLOSURE_CAP:
            raise SystemExit(f"[CAP] fecho > {CLOSURE_CAP} — use DAG/DRAT "
                             "para instancias grandes")
    return None if frozenset() not in index else nodes


def var_sides_from(leaves_clauses):
    """ mapa var -> lado (lados disjuntos); erro se sobreposicao."""
    vs = {}
    for cl, side in leaves_clauses:
        for l in cl:
            v = abs(l)
            if v in vs and vs[v] != side:
                raise SystemExit(f"[HIP] variavel {v} em dois lados "
                                 "(Teorema 4.3 exige disjuntos)")
            vs[v] = side
    return vs


def theorem43_resolution(nodes, var_side):
    """E-pass do Lema 4.1 + extracao (Teorema 4.3).
    Retorna (i*, cert_steps, root_id) ou (None, None, erro_str)."""
    w, E, epar = {}, {}, {}
    for v in nodes:                       # provador: folhas antes (ids menores)
        r, P, d = v["kind"], v["prems"], v["clause"]
        if r == "leaf":
            sides = {var_side[abs(l)] for l in d}
            if len(sides) != 1:
                return None, None, f"folha {v['id']} nao-pura"
            w[v["id"]] = sides.pop()
            E[v["id"]] = d
            epar[v["id"]] = []
        elif r == "weaken":
            u = P[0]
            w[v["id"]] = w[u]
            E[v["id"]] = E[u]            # descarta o enfraquecimento
            epar[v["id"]] = [u]
        elif r == "resolve":
            p1, p2 = P
            # pivot: l tal que lam(p1) = E... pivot vem das LINHAS ORIGINAIS:
            d1, d2 = nodes[p1]["clause"], nodes[p2]["clause"]
            piv = [l for l in d1 if -l in d2]
            if len(piv) != 1:
                return None, None, (f"resolve {v['id']}: pivô ambiguo "
                                    f"({len(piv)}) — formato nao canonico")
            l = piv[0]
            e1, e2 = E[p1], E[p2]
            if l in e1 and -l in e2:
                if w[p1] != w[p2]:
                    return None, None, (f"resolve {v['id']}: pais de lados "
                                        f"divergentes em retencao total")
                w[v["id"]] = w[p1]
                E[v["id"]] = (e1 - {l}) | (e2 - {-l})
                epar[v["id"]] = [p1, p2]
            elif l not in e1:
                w[v["id"]] = w[p1]
                E[v["id"]] = e1
                epar[v["id"]] = [p1]
            else:                       # l em e1, ~l nao em e2
                w[v["id"]] = w[p2]
                E[v["id"]] = e2
                epar[v["id"]] = [p2]
        else:
            return None, None, f"regra desconhecida {r}"
        if not E[v["id"]] <= d:
            return None, None, f"E ⊄ λ em {v['id']}"
        for t in E[v["id"]]:
            if var_side[abs(t)] != w[v["id"]]:
                return None, None, f"impureza em {v['id']}"
    # raiz = ∅ (o provador garante); seguir eparents ate o primeiro ∅
    # proprio (corte que produziu ∅ ou folha ∅)
    root = len(nodes) - 1
    if E[root]:
        return None, None, "raiz nao e vazio"
    cur = root
    seen = set()
    while True:
        if cur in seen:
            return None, None, "ciclo em eparents"
        seen.add(cur)
        P = epar[cur]
        if not P:                       # folha ∅
            i_star = w[cur]
            first_zero = cur
            break
        if len(P) == 2:                 # corte proprio produziu ∅
            if w[P[0]] != w[P[1]]:
                return None, None, "pais de lados distintos na raiz"
            i_star = w[P[0]]
            first_zero = cur
            break
        cur = P[0]                      # reuso: desce
    acc = accessible_nodes(nodes, epar, first_zero)
    for nid in acc:
        if w[nid] != i_star:
            return None, None, f"acessivel {nid} fora do lado {i_star}"
        if nodes[nid]["kind"] == "leaf":
            if nodes[nid]["side"] != i_star:
                return None, None, f"folha acessivel {nid} de outro lado"
    # certificado: sub-derivacao acessivel em ordem, RAIZ POR ULTIMO
    # (resolucao: clausula = UM termo — representacao unica com Res(k))
    order = sorted(acc)
    order.remove(first_zero)
    order.append(first_zero)             # raiz = ∅ no fim
    cert = [{"step": nid, "orig": nid, "kind": nodes[nid]["kind"],
             "prems": [p for p in epar[nid]],
             "line": ([sorted(E[nid])] if E[nid] else [])}
            for nid in order]
    return i_star, cert, None


def accessible_nodes(nodes, epar, root):
    seen, stack = set(), [root]
    while stack:
        i = stack.pop()
        if i in seen:
            continue
        seen.add(i)
        stack.extend(epar[i])
    return seen


# =====================================================================
# Ingestao DRAT -> DAG (extracao de dependencias via UP)
# =====================================================================
def up_dependencies(clause, alive):
    """UP em F=alive assumindo ~clause; retorna (usados:set, conflito:bool)
    ou None se nao conflita. alive: dict clause->id."""
    assign = {}                          # lit -> True(falso p/ formula)
    for l in clause:
        if -l in assign:
            return None                  # premissa interna inconsistente
        assign[-l] = True
    used = set()
    changed = True
    while changed:
        changed = False
        for c, cid in alive.items():
            falsos = [l for l in c if -assign.get(l, False) is True or
                      assign.get(l, False) is True and False]
            # avalia: l falsificado se assign[-l] verdadeiro
            vals = [assign.get(-l, False) for l in c]
            if all(vals):
                return used | {cid}, True            # conflito
            if sum(1 for v in vals if not v) == 1:
                # exatamente UM nao-falsificado -> unitario (UP correto:
                # torna o literal VERDADEIRO — assign[z]=True <=> z verdadeiro;
                # a v1 usava len(c)-1 [errada p/ >=3 lit] e assign[-l]
                # [sinal invertido — conflitos espurios])
                for l in c:
                    if not assign.get(-l, False):
                        if assign.get(l, False):
                            break          # ja verdadeiro: satisfaz; nada a fazer
                        assign[l] = True   # l := VERDADEIRO
                        used.add(cid)
                        changed = True
                        break
    return used, False


def drat_to_dag(sides_clauses, drat_lines):
    """Constroi DAG de resolucao a partir de DRAT ASCII (adicoes RUP).
    Cada adicao: UP com rastreio de dependencias -> clausulas usadas;
    depois saturacao LOCAL (U pequeno) para achar a derivacao explicita
    da clausula. Retorna (nodes, erro)."""
    var_side = var_sides_from(sides_clauses)
    nodes, alive = [], {}
    def add(clause, kind, prems, side=None):
        if clause in alive:
            return alive[clause]
        nid = len(nodes)
        nodes.append({"id": nid, "kind": kind, "clause": frozenset(clause),
                      "prems": prems, "side": side})
        alive[frozenset(clause)] = nid
        return nid
    for cl, side in sides_clauses:
        add(frozenset(cl), "leaf", [], side)

    def dep_is_leaf(c):
        return any(frozenset(c) == frozenset(x) for x, _ in sides_clauses)

    def build_derivation(clause, dep_clauses):
        """saturacao sobre dep_clauses ate `clause`; cria nos em `nodes`."""
        local = {}                      # clause -> id global
        prems_map = {}
        def ensure(c):
            if c in local:
                return local[c]
            if c in alive:              # no ja existente (adicao anterior)
                local[c] = alive[c]
                return local[c]
            if dep_is_leaf(c):
                side = next(s for x, s in sides_clauses
                            if frozenset(x) == c)
                nid = add(c, "leaf", [], side)
            else:
                nid = None              # sera preenchido na saturacao
            local[c] = nid
            return nid
        for c in dep_clauses:
            ensure(c)
        changed = True
        while changed:
            changed = False
            cs = [c for c in local if local[c] is not None]
            for c1 in cs:
                for c2 in cs:
                    if c1 == c2:
                        continue
                    s1, s2 = set(c1), set(c2)
                    for l in sorted(s1):
                        if -l in s2:
                            res = frozenset((s1 - {l}) | (s2 - {-l}))
                            if any(-x in res for x in res):
                                continue
                            if res == clause and res not in local:
                                nid = add(res, "resolve",
                                          [local[c1], local[c2]])
                                local[res] = nid
                                changed = True
                                return True
                            if res not in local and len(local) < 500:
                                nid = add(res, "resolve",
                                          [local[c1], local[c2]])
                                local[res] = nid
                                changed = True
        return clause in local and local[clause] is not None

    for raw in drat_lines:
        if isinstance(raw, bytes):
            raw = raw.decode("utf-8", "replace")
        raw = raw.strip()
        if not raw or raw[0] in "dD":
            continue
        if raw[0] in "aA":
            raw = raw[1:].strip()
        toks = raw.split()
        if not toks or toks[-1] != "0":
            continue
        try:
            lits = [int(x) for x in toks[:-1]]
        except ValueError:
            continue
        # (lits vazio permitido: clausula vazia = raiz da refutacao)
        C = frozenset(lits)
        if C in alive:
            continue
        res = up_dependencies(C, alive)
        if res is None:
            continue                    # nao RUP sob nosso replay: pula
        used, conflict = res
        if not conflict:
            continue
        dep_clauses = [nodes[i]["clause"] for i in used]
        ok = build_derivation(C, dep_clauses)
        if __import__("os").environ.get("DD_DEBUG"):
            print(f"  [dbg] C={sorted(C)} used={sorted(used)} "
                  f"deps={[sorted(c) for c in dep_clauses]} build={ok}")
        if not ok:
            continue                    # nao derivou explicitamente: pula
        alive[C] = len(nodes) - 1
        if frozenset() in alive:
            break
    if frozenset() not in alive:
        return None, ("DRAT: nao derivamos vazio (adicoes nao-RUP ou "
                      "extracao incompleta) — forneça DAG ou use o "
                      "provador proprio")
    # completa ids de nodes para bater com alive (add ja criou)
    return nodes, None


# =====================================================================
# Certificado comum + motor Res(k)
# =====================================================================
def make_certificate(engine, i_star, cert_steps, n_input, side_leaves,
                     meta):
    norm = []
    for c in side_leaves:
        if c and isinstance(next(iter(c)), int):
            norm.append([sorted(c)])              # clausula resolucao ->1 termo
        else:
            norm.append(sorted(map(sorted, c)))   # dnf Res(k)
    return {
        "type": "dd_certificate",
        "engine": engine,
        "side": i_star,
        "n_lines_input": n_input,
        "n_lines_cert": len(cert_steps),
        "size_bound_respected": len(cert_steps) <= n_input,
        "side_leaves": norm,
        "steps": cert_steps,
        "root": cert_steps[-1]["step"] if cert_steps else None,
        "meta": meta,
        "generated_utc": datetime.now(timezone.utc).isoformat()
                         .replace("+00:00", "Z"),
        "verifier": "python gk_dd_cert.py verify <este arquivo>",
    }


def _topo_reindex(lines):
    """Reordena linhas (indices de prems apontam p/ a propria lista) de modo
    que PREMISSAS tenham id MAIOR que o consumidor — o motor Res(k) do
    gk_c2_projection_sim processa em ordem reversa de id."""
    n = len(lines)
    for s in lines:
        for p in s.get("prems", []):
            if not (0 <= p < n):
                raise SystemExit(f"[INPUT] premissa {p} fora do intervalo")
    placed, topo, remaining = set(), [], list(range(n))
    while remaining:
        prog = False
        for i in list(remaining):
            if all(p in placed for p in lines[i].get("prems", [])):
                topo.append(i)
                placed.add(i)
                remaining.remove(i)
                prog = True
        if not prog:
            raise SystemExit("[INPUT] ciclo de premissas")
    order = list(reversed(topo))          # consumidor antes -> premissa c/ id maior
    remap = {old: new for new, old in enumerate(order)}
    out = []
    for old in order:
        s = dict(lines[old])
        s["prems"] = [remap[p] for p in s.get("prems", [])]
        out.append(s)
    return out


def run_resk_extract(input_obj):
    """Motor Res(k): DAG de regras de Garlík -> certificado ou violacao."""
    k = input_obj.get("k", 2)
    specs = _topo_reindex(input_obj["lines"])
    dag = Dag()
    promise = {}
    for spec in specs:
        nid = dag.add(spec["kind"], spec.get("prems", []),
                      frozenset(frozenset(t) for t in spec["dnf"]))
        L = dag.lines[nid]
        if spec["kind"] == "leaf":
            L["side"] = spec["side"]
        elif spec["kind"] == "cut":
            L["t"] = frozenset(spec["t"])
        elif spec["kind"] == "and":
            L["l1"] = spec["l1"]
            L["s"] = frozenset(spec["s"])
            promise[nid] = spec.get("promise_side")
    err = check_soundness_input(dag, k)
    if err:
        return {"status": "INVALID_INPUT", "reason": err}
    w, E, perr = run_projection(dag, promise)
    if perr:
        return {"status": "VIOLATION", "reason": perr,
                "engine": "resk",
                "leitura": ("promessa/algoritmo violado — o detector "
                            "automatico do r2 (hoje automatico aqui)")}
    # primeira linha com E vazio
    root = None
    for v in reversed(dag.lines):
        if not E[v["id"]]:
            root = v["id"]
            break
    if root is None:
        return {"status": "NO_ROOT", "reason": "nenhuma linha com E=∅"}
    cerr = check_extraction(dag, w, E, root)
    if cerr:
        return {"status": "EXTRACTION_FAILED", "reason": cerr}
    acc = accessible(dag, root, E)
    i_star = w[root]
    order = sorted(acc)
    if root in order:
        order.remove(root)
        order.append(root)               # raiz por ultimo
    cert = []
    for nid in order:
        v = dag.lines[nid]
        cert.append({
            "step": nid, "orig": nid, "kind": v["rule"],
            "prems": list(v.get("eparents", [])),
            "line": (sorted(map(sorted, E[nid])) if E[nid] else []),
            "orig_line": sorted(map(sorted, v["dnf"])),
        })
    side_leaves = [v["dnf"] for v in dag.lines
                   if v["rule"] == "leaf" and v["side"] == i_star]
    return {"status": "OK",
            "certificate": make_certificate(
                "resk", i_star, cert, len(dag.lines),
                side_leaves, {"k": k, **{kk: input_obj[kk]
                              for kk in input_obj if kk not in
                              ("lines",)}})}


def check_soundness_input(dag, k):
    """valida formas das regras de Garlík nas linhas de entrada."""
    for v in dag.lines:
        if v["rule"] == "cut":
            p1, p2 = dag.lines[v["prems"][0]], dag.lines[v["prems"][1]]
            t = v["t"]
            if t not in p1["dnf"]:
                return f"cut {v['id']}: t fora da premissa1"
            if not block_of(t) <= p2["dnf"]:
                return f"cut {v['id']}: bloco fora da premissa2"
            concl = (p1["dnf"] - {t}) | (p2["dnf"] - block_of(t))
            if not concl <= v["dnf"]:
                return f"cut {v['id']}: conclusao nao contem A u B"
        elif v["rule"] == "and":
            p1, p2 = dag.lines[v["prems"][0]], dag.lines[v["prems"][1]]
            sing, s = frozenset([v["l1"]]), v["s"]
            if sing not in p1["dnf"] or s not in p2["dnf"]:
                return f"and {v['id']}: pecas ausentes"
            if sing | s not in v["dnf"]:
                return f"and {v['id']}: termo combinado ausente"
            if len(sing | s) > k:
                return f"and {v['id']}: largura {len(sing|s)} > k"
        elif v["rule"] == "weaken":
            p1 = dag.lines[v["prems"][0]]
            if not p1["dnf"] <= v["dnf"]:
                return f"weaken {v['id']}: premissa ⊄ conclusao"
    return None


# =====================================================================
# VERIFICADOR INDEPENDENTE (sem importar a logica do extrator)
# Representacao unica: line = lista de TERMOS (termo = frozenset de
# literais); clausula de resolucao = um unico termo.
# =====================================================================
def _terms(line):
    if line and isinstance(line[0], int):
        return [frozenset(line)]          # legado: clausula plana
    return [frozenset(t) for t in line]


def _leaf_union(cl):
    """cl (folha) pode ser lista plana (resolucao) ou dnf (Res(k))."""
    if cl and isinstance(cl[0], int):
        return frozenset(cl)
    return frozenset().union(*[frozenset(t) for t in cl])


def verify_certificate(cert, verbose=True):
    fails = []
    def bad(msg):
        fails.append(msg)
    if cert.get("type") != "dd_certificate":
        bad("type != dd_certificate")
        return fails
    leaf_sets = {_leaf_union(cl)
                 for cl in cert.get("side_leaves", [])}
    side_vars = {abs(l) for ls in leaf_sets for l in ls}
    steps = cert.get("steps", [])
    if not steps:
        bad("sem passos")
        return fails
    by_step = {s["step"]: s for s in steps}
    if len(by_step) != len(steps):
        bad("steps duplicados")
    if steps[-1]["line"]:
        bad(f"raiz nao e vazio: {steps[-1]['line']}")
    seen, inprog = set(), set()

    def chk(step_id):
        if step_id in seen:
            return
        if step_id in inprog:
            bad(f"ciclo de premissas em {step_id}")
            return
        if step_id not in by_step:
            bad(f"step {step_id} ausente")
            return
        inprog.add(step_id)
        s = by_step[step_id]
        for p in s["prems"]:
            chk(p)                        # ordem: DAG, nao numerica
        kind, line = s["kind"], _terms(s["line"])
        if kind == "leaf":
            if frozenset().union(*line) not in leaf_sets:
                bad(f"leaf {step_id} fora de side_leaves")
        elif kind == "resolve":
            if len(s["prems"]) != 2:
                bad(f"resolve {step_id}: !=2 premissas")
            else:
                A = _terms(by_step[s["prems"][0]]["line"])
                B = _terms(by_step[s["prems"][1]]["line"])
                piv = [l for ta in A for l in ta
                       if any(-l in tb for tb in B)]
                if len(piv) != 1:
                    bad(f"resolve {step_id}: pivoto invalido ({len(piv)})")
                else:
                    l = piv[0]
                    want = {ta - {l} for ta in A if ta - {l}} | \
                           {tb - {-l} for tb in B if tb - {-l}}
                    if want != set(line):
                        bad(f"resolve {step_id}: conclusao errada")
        elif kind == "weaken":
            if len(s["prems"]) != 1:
                bad(f"weaken {step_id}: !=1 premissa")
            else:
                P = _terms(by_step[s["prems"][0]]["line"])
                if not set(P) <= set(line):
                    bad(f"weaken {step_id}: premissa nao-contida")
        elif kind == "cut":
            if len(s["prems"]) == 1:                      # reuso
                if set(line) != _terms(by_step[s["prems"][0]]["line"]):
                    bad(f"cut {step_id}: reuso nao bate com pai")
            elif len(s["prems"]) == 2:
                A = _terms(by_step[s["prems"][0]]["line"])
                B = _terms(by_step[s["prems"][1]]["line"])
                hit = False
                for t in A:
                    blk = {frozenset([-l]) for l in t}
                    if blk <= set(B):
                        want = (set(A) - {t}) | (set(B) - blk)
                        if want == set(line):
                            hit = True
                if not hit and set(line) not in (set(A), set(B)):
                    bad(f"cut {step_id}: nem corte valido nem reuso")
            else:
                bad(f"cut {step_id}: premissas invalidas")
        elif kind == "and":
            if len(s["prems"]) == 1:
                if set(line) != _terms(by_step[s["prems"][0]]["line"]):
                    bad(f"and {step_id}: reuso nao bate com pai")
            elif len(s["prems"]) == 2:
                A = _terms(by_step[s["prems"][0]]["line"])
                B = _terms(by_step[s["prems"][1]]["line"])
                kmax = cert.get("meta", {}).get("k", 99)
                hit = False
                for sg in A:
                    if len(sg) != 1:
                        continue
                    for tb in B:
                        want = (set(A) - {sg}) | (set(B) - {tb}) | \
                               {sg | tb}
                        if want == set(line) and len(sg | tb) <= kmax:
                            hit = True
                if not hit:
                    bad(f"and {step_id}: combinacao invalida ou >k")
            else:
                bad(f"and {step_id}: premissas invalidas")
        else:
            bad(f"{step_id}: kind desconhecido {kind}")
        inprog.discard(step_id)
        seen.add(step_id)

    chk(steps[-1]["step"])
    if len(seen) != len(steps):
        bad(f"{len(steps) - len(seen)} passos inacessiveis da raiz")
    for s in steps:
        for t in _terms(s["line"]):
            for l in t:
                if abs(l) not in side_vars:
                    bad(f"step {s['step']}: literal {l} fora do lado")
                    break
    if cert.get("n_lines_cert", 10**9) > cert.get("n_lines_input", 0):
        bad("n_lines_cert > n_lines_input (bound violado)")
    return fails


# =====================================================================
def demo():
    print("=" * 72)
    print("DD CERT — demonstracao (2 resolucao + 2 Res(k))")
    print("=" * 72)
    results = []

    # --- D1: resolucao via provador proprio (lado disjunto) ---
    sides1 = [
        [frozenset([1]), frozenset([-1])],          # lado0: UNSAT
        [frozenset([3, 4])],                        # lado1: SAT
    ]
    leaves1 = [(frozenset(c), i) for i, s in enumerate(sides1)
               for c in s]
    vs1 = var_sides_from(leaves1)
    nodes1 = saturate_with_parents(leaves1)
    i1, cert1, err1 = theorem43_resolution(nodes1, vs1)
    ok1 = err1 is None and i1 == 0
    print(f"  [{'OK' if ok1 else 'FALHA'}] D1 resolucao/provador: "
          f"lado={i1} passos={len(cert1) if cert1 else '-'} err={err1}")
    results.append({"demo": "D1_resolucao_provador", "ok": ok1,
                    "side": i1})

    # --- D2: resolucao com ENFRAQUECIMENTO MISTO na entrada ---
    #    L0={1}(lado0), L1={-1}(lado0), L2={-3}(lado1)
    #    L3 = weaken(L0) = {1,3}  (mistura a variavel 3 do lado1!)
    #    L4 = resolve(L3,L1,piv=1) = {3}
    #    L5 = resolve(L4,L2,piv=3) = ∅
    sides2 = [
        [frozenset([1]), frozenset([-1])],
        [frozenset([-3])],
    ]
    leaves2 = [(frozenset(c), i) for i, s in enumerate(sides2)
               for c in s]
    vs2 = var_sides_from(leaves2)
    n = []
    def mk(kind, prems, clause):
        n.append({"id": len(n), "kind": kind, "prems": prems,
                  "clause": frozenset(clause),
                  "side": None})
        return len(n) - 1
    l0 = mk("leaf", [], [1]); n[l0]["side"] = 0
    l1 = mk("leaf", [], [-1]); n[l1]["side"] = 0
    l2 = mk("leaf", [], [-3]); n[l2]["side"] = 1
    l3 = mk("weaken", [l0], [1, 3])
    l4 = mk("resolve", [l3, l1], [3])
    l5 = mk("resolve", [l4, l2], [])
    i2, cert2, err2 = theorem43_resolution(n, vs2)
    ok2 = err2 is None and i2 == 0
    print(f"  [{'OK' if ok2 else 'FALHA'}] D2 resolucao/enfraquecimento "
          f"misto: lado={i2} passos={len(cert2) if cert2 else '-'} "
          f"err={err2}")
    results.append({"demo": "D2_resolucao_misto", "ok": ok2, "side": i2})

    # --- D3: Res(k) puro (and-intro + corte) -> certificado ---
    # (nota: gk_c2_projection_sim tem VAR_SIDE fixo {1,2->lado1;3,4->lado2}
    #  — o demo usa vars 1,2 => lado 1 em todas as folhas)
    inp3 = {
        "k": 2,
        "lines": [
            {"kind": "leaf", "dnf": [[1]], "side": 1},
            {"kind": "leaf", "dnf": [[2]], "side": 1},
            {"kind": "leaf", "dnf": [[-1], [-2]], "side": 1},
            {"kind": "and", "prems": [0, 1], "l1": 1, "s": [2],
             "dnf": [[1, 2]], "promise_side": 1},
            {"kind": "cut", "prems": [3, 2], "t": [1, 2],
             "dnf": []},
        ],
    }
    r3 = run_resk_extract(inp3)
    ok3 = r3.get("status") == "OK"
    side3 = r3.get("certificate", {}).get("side")
    print(f"  [{'OK' if ok3 else 'FALHA'}] D3 Res(k)/puro: "
          f"status={r3.get('status')} lado={side3} "
          f"motivo={r3.get('reason', '')}")
    results.append({"demo": "D3_resk_puro", "ok": ok3, "side": side3})

    # --- D4: Res(k) = CONTRAEXEMPLO r2 (violacao G1 automatica) ---
    dag4, root4, prom4 = build_counterexample()
    lines4 = []
    for v in dag4.lines:
        spec = {"kind": v["rule"], "prems": list(v["prems"]),
                "dnf": [sorted(t) for t in v["dnf"]]}
        if v["rule"] == "leaf":
            spec["side"] = v.get("side", 0)
        if v["rule"] == "cut":
            spec["t"] = sorted(v["t"])
        if v["rule"] == "and":
            spec["l1"] = v["l1"]
            spec["s"] = sorted(v["s"])
            spec["promise_side"] = prom4.get(v["id"], 0)
        lines4.append(spec)
    r4 = run_resk_extract({"k": 2, "lines": lines4})
    ok4 = r4.get("status") == "VIOLATION" and "G1" in r4.get("reason", "")
    print(f"  [{'OK' if ok4 else 'FALHA'}] D4 Res(k)/contraexemplo r2: "
          f"status={r4.get('status')} motivo={r4.get('reason', '')[:70]}")
    results.append({"demo": "D4_resk_violacao", "ok": ok4,
                    "status": r4.get("status")})

    # --- verificacao independente dos certificados D1/D2/D3 ---
    print("\n  verificador INDEPENDENTE:")
    for name, cert in (("D1", cert1 and make_certificate(
                            "resolution", i1, cert1, len(nodes1),
                            [c for c, _ in leaves1], {"demo": "D1"})),
                       ("D2", cert2 and make_certificate(
                            "resolution", i2, cert2, len(n),
                            [c for c, _ in leaves2], {"demo": "D2"})),
                       ("D3", r3.get("certificate"))):
        if not cert:
            print(f"    [FALHA] {name}: sem certificado")
            results.append({"verify": name, "ok": False})
            continue
        fails = verify_certificate(cert)
        okv = not fails
        print(f"    [{'OK' if okv else 'FALHA'}] {name}: "
              f"{len(fails)} falhas" + (f" -> {fails[:3]}" if fails else
                                        f" (lado {cert['side']}, "
                                        f"{cert['n_lines_cert']} linhas)"))
        results.append({"verify": name, "ok": okv,
                        "fails": fails[:5]})

    all_ok = all(r.get("ok") for r in results)
    print("-" * 72)
    print("*** DEMO OK: extracao + violacao + verificacao ***"
          if all_ok else "*** DEMO COM FALHAS ***")
    Path("gk_dd_cert_demo.json").write_text(
        json.dumps({"results": results, "seed_note":
                    "deterministico (sem RNG)"}, indent=2,
                   ensure_ascii=False), encoding="utf-8")
    return 0 if all_ok else 1


# =====================================================================
# CLI
# =====================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", nargs="?", choices=["demo", "extract",
                                                "verify"],
                    default="demo")
    ap.add_argument("file", nargs="?")
    ap.add_argument("-o", "--out", default="gk_dd_certificate.json")
    args = ap.parse_args()

    if args.mode == "demo":
        return demo()

    if args.mode == "verify":
        if not args.file:
            raise SystemExit("verify exige um arquivo de certificado")
        cert = json.loads(Path(args.file).read_text(encoding="utf-8"))
        fails = verify_certificate(cert)
        if fails:
            print(f"RECUSADO ({len(fails)} falhas):")
            for f in fails[:10]:
                print(f"  - {f}")
            return 1
        print(f"ACEITO: lado {cert['side']}, "
              f"{cert['n_lines_cert']} linhas (bound "
              f"{cert['n_lines_input']}), motor {cert['engine']}")
        return 0

    # extract
    if not args.file:
        raise SystemExit("extract exige um arquivo de entrada")
    inp = json.loads(Path(args.file).read_text(encoding="utf-8"))
    engine = inp.get("engine", "resolution")

    if engine == "resk":
        out = run_resk_extract(inp)
        if out.get("status") == "OK":
            cert = out["certificate"]
            Path(args.out).write_text(json.dumps(cert, indent=2,
                                       ensure_ascii=False),
                                       encoding="utf-8")
            print(f"CERTIFICADO -> {args.out}: lado {cert['side']}, "
                  f"{cert['n_lines_cert']}/{cert['n_lines_input']} linhas")
            fails = verify_certificate(cert)
            print("verificacao independente:",
                  "OK" if not fails else f"FALHAS {fails[:3]}")
            return 0 if not fails else 1
        print(f"STATUS: {out.get('status')} — {out.get('reason')}")
        return 2

    # resolution: sides (+ opcional drat/dag)
    sides = [[frozenset(tuple(c) if isinstance(c, list) else c)
              for c in s] for s in inp["sides"]]
    sides_c = [(frozenset(c), i) for i, s in enumerate(sides)
               for c in s]
    vs = var_sides_from(sides_c)
    n_input = None
    if inp.get("dag"):
        nodes = [{"id": d["id"], "kind": d["kind"],
                  "prems": d.get("prems", []),
                  "clause": frozenset(tuple(x) if isinstance(x, list)
                                      else x for x in d["line"]),
                  "side": d.get("side")}
                 for d in inp["dag"]]
        n_input = len(nodes)
    elif inp.get("drat"):
        nodes, err = drat_to_dag(sides_c, inp["drat"])
        if err:
            print(f"ERRO: {err}")
            return 2
        n_input = len(nodes)
    else:
        nodes = saturate_with_parents(sides_c)
        if nodes is None:
            print("RESULTADO: Λ satisfativel (nenhum lado insat) — "
                  "sem certificado")
            return 3
        n_input = len(nodes)
    i_star, cert, err = theorem43_resolution(nodes, vs)
    if err:
        print(f"ERRO: {err}")
        return 2
    side_leaves = [c for c, s in sides_c if s == i_star]
    cert_obj = make_certificate("resolution", i_star, cert, n_input,
                                side_leaves,
                                {"source": "dag" if inp.get("dag")
                                 else ("drat" if inp.get("drat")
                                       else "saturacao")})
    Path(args.out).write_text(json.dumps(cert_obj, indent=2,
                               ensure_ascii=False), encoding="utf-8")
    print(f"CERTIFICADO -> {args.out}: lado {i_star}, "
          f"{cert_obj['n_lines_cert']}/{n_input} linhas")
    fails = verify_certificate(cert_obj)
    print("verificacao independente:",
          "OK" if not fails else f"FALHAS {fails[:3]}")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())

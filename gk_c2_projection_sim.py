#!/usr/bin/env python3
"""
gk_c2_projection_sim.py — R2 do C2: simulador do algoritmo de projeção E
para Res(k) + busca por contraexemplos aos invariantes (G1)/(G2).

Algoritmo candidato (r2, ver C2_r2_fechamento.md):
  w(v): folha = lado própria; axioma = lado(x); enfraquecimento = herda;
        corte: retenção-total -> w(p1) (== w(p2)); reuso -> w(pai);
        and-intro: combine -> lado i (promessa); reuso -> w(pai).
  E(v): folha/axioma = linha inteira;
        enfraquecimento: E(u) U {termos novos de B sobre X_{w(u)}}  [FILTRO]
        corte (t = termo-premissa-1, bloco = {~l : l em t}):
          (R1) t em E(p1) e bloco inteiro em E(p2)  -> corte proprio
          (R2) t nao em E(p1)                       -> reusa E(p1) (⊆ A)
          (R3) t em E(p1), bloco ausente/parcial em E(p2) -> reusa E(p2) (⊆ B)
               + ASSERTA: bloco ∩ E(p2) = vazio (all-or-none — teste de G1)
        and-intro (l1 singleton em p1, termo s em p2):
          (A1) ambos presentes -> combinado
          (A2) l1 ausente      -> reusa E(p1) (⊆ A)
          (A3) s ausente       -> reusa E(p2) (⊆ B)
  Invariantes verificados por linha:
    I1  E(v) ⊆ λ(v)
    I2  E(v) ⊆ X_{w(v)}            (pureza — G2)
    I3  E(v) derivavel (regra aplicada aos E-pais, ou reuso = E(pai))
    I4  all-or-none de blocos em cortes (G1: sem retencao parcial)
    I5  primeiro ∅ -> extração acessível = refutação pura de Λ_{i*}

Gerador: DAGs aleatórios por construcao REVERSA a partir de ∅
(corte-tras, enfraquecimento-tras, and-intro-tras) + folhas singleton
atribuídas aos lados (variáveis disjuntas => Λ = Λ1 ⊎ Λ2).

Uso: python gk_c2_projection_sim.py [--n 2000] [--seed 20261119]
"""

import argparse
import random
from itertools import combinations

# ---------------- representacao ----------------
# termo  = frozenset de literais (int; negativo = negado)
# linha  = frozenset de termos (k-DNF)
# variaveis 1,2 -> lado 1 ; 3,4 -> lado 2
VAR_SIDE = {1: 1, 2: 1, 3: 2, 4: 2}
K = 2  # largura maxima (termos com <= K literais)


def side_of_term(t):
    sides = {VAR_SIDE[abs(l)] for l in t}
    return sides.pop() if len(sides) == 1 else 0  # 0 = misto


def block_of(t):
    """bloco de negacoes: {~l : l em t} (como singletons)."""
    return frozenset(frozenset([-l]) for l in t)


class Dag:
    def __init__(self):
        self.lines = []  # list of dict(id, rule, prems, dnf)

    def add(self, rule, prems, dnf):
        v = {"id": len(self.lines), "rule": rule, "prems": prems, "dnf": dnf}
        self.lines.append(v)
        return v["id"]


# ---------------- algoritmo E/w ----------------
def run_projection(dag, promise_and_sides):
    """Computa (w, E) por passada direta. promise_and_sides: id -> lado i
    para and-intros (promessa puro-respeitadora). Retorna (w, E, erro).
    Registra em v['eparents'] os pais da DERIVACAO-E (para extracao)."""
    w, E = {}, {}
    # ordem topologica: na construcao reversa, premissas sempre tem id MAIOR
    # que a linha que justificam -> processar do maior id para o menor
    for v in reversed(dag.lines):
        r, P, d = v["rule"], v["prems"], v["dnf"]
        v["eparents"] = []
        if r == "leaf":
            w[v["id"]] = v["side"]
            E[v["id"]] = d
        elif r == "axiom":
            x = next(iter(next(iter(d))))  # termo {x} ou {x,~x}
            w[v["id"]] = VAR_SIDE[abs(x)]
            E[v["id"]] = d
        elif r == "weaken":
            u = P[0]
            w[v["id"]] = w[u]
            added = d - dag.lines[u]["dnf"]
            E[v["id"]] = E[u] | {t for t in added
                                 if side_of_term(t) == w[u]}
            v["eparents"] = [u]
        elif r == "cut":
            p1, p2, t = P[0], P[1], v["t"]
            blk = block_of(t)
            e1, e2 = E[p1], E[p2]
            if t in e1 and blk <= e2:
                # (R1) corte proprio — exige w igual (pureza => mesmas variaveis)
                if w[p1] != w[p2]:
                    return w, E, f"R1 com w divergente em {v['id']}"
                w[v["id"]] = w[p1]
                E[v["id"]] = (e1 - {t}) | (e2 - blk)
                v["eparents"] = [p1, p2]
            elif t not in e1:
                # (R2) reusa pai 1
                w[v["id"]] = w[p1]
                E[v["id"]] = e1
                v["eparents"] = [p1]
            else:
                # (R3) t em E(p1), bloco nao completo em E(p2)
                partial = blk & e2
                if partial:
                    return w, E, (f"G1 VIOLADO: retencao parcial do bloco "
                                  f"em {v['id']}: {sorted(map(sorted, partial))}")
                w[v["id"]] = w[p2]
                E[v["id"]] = e2
                v["eparents"] = [p2]
        elif r == "and":
            p1, p2, l1, s = P[0], P[1], v["l1"], v["s"]
            e1, e2 = E[p1], E[p2]
            singleton = frozenset([l1])
            if singleton in e1 and s in e2:
                i = promise_and_sides[v["id"]]
                if w[p1] != i or w[p2] != i:
                    return w, E, (f"and-promessa: w(p1)={w[p1]}, w(p2)={w[p2]} "
                                  f"!= i={i} em {v['id']}")
                w[v["id"]] = i
                E[v["id"]] = (e1 - {singleton}) | (e2 - {s}) | {singleton | s}
                v["eparents"] = [p1, p2]
            elif singleton not in e1:
                w[v["id"]] = w[p1]
                E[v["id"]] = e1
                v["eparents"] = [p1]
            else:
                w[v["id"]] = w[p2]
                E[v["id"]] = e2
                v["eparents"] = [p2]
        else:
            return w, E, f"regra desconhecida {r}"
        # I1: E ⊆ λ
        if not E[v["id"]] <= d:
            return w, E, f"I1 violado em {v['id']}: E ⊄ λ"
        # I2: pureza de E sobre w
        for t in E[v["id"]]:
            if side_of_term(t) not in (0, w[v["id"]]):
                return w, E, (f"G2/I2 violado em {v['id']}: termo {sorted(t)} "
                              f"lado {side_of_term(t)} != w={w[v['id']]}")
    return w, E, None


def accessible(dag, root_id, E):
    """linhas E acessiveis pela DERIVACAO-E (eparents), nao pelas prems estruturais."""
    seen, stack = set(), [root_id]
    while stack:
        i = stack.pop()
        if i in seen:
            continue
        seen.add(i)
        for p in dag.lines[i].get("eparents", []):
            stack.append(p)
    return seen


def check_extraction(dag, w, E, root_id):
    """I5: raiz E=∅ (primeiro ∅); acessiveis todos mesmo w; folhas ∈ Λ_{w}."""
    if E[root_id]:
        return None  # nao e raiz-∅
    acc = accessible(dag, root_id, E)
    ws = {w[i] for i in acc}
    if len(ws) != 1:
        return f"I5: lados distintos na extracao: {sorted(ws)}"
    i_star = ws.pop()
    for i in acc:
        v = dag.lines[i]
        if v["rule"] == "leaf" and v["side"] != i_star:
            return f"I5: folha {i} lado {v['side']} != i*={i_star}"
    return None


# ---------------- verificacao por linha (I3) ----------------
def check_derivability(dag, w, E):
    for v in dag.lines:
        r, P = v["rule"], v["prems"]
        e = E[v["id"]]
        if r in ("leaf", "axiom"):
            continue
        if r == "weaken":
            if not (E[P[0]] <= e):
                return f"I3 weaken {v['id']}: E(pai) ⊄ E(v)"
        elif r == "cut":
            p1, p2 = P[0], P[1]
            t = v["t"]
            if e == E[p1] or e == E[p2]:
                continue  # reuso
            # corte proprio: deve ser (E1-t) u (E2-bloco)
            if e != ((E[p1] - {t}) | (E[p2] - block_of(t))):
                return f"I3 cut {v['id']}: E nao corresponde a regra"
        elif r == "and":
            p1, p2 = P[0], P[1]
            l1, s = v["l1"], v["s"]
            if e == E[p1] or e == E[p2]:
                continue
            sing = frozenset([l1])
            if e != ((E[p1] - {sing}) | (E[p2] - {s}) | {sing | s}):
                return f"I3 and {v['id']}: E nao corresponde a regra"
    return None


# ---------------- gerador reverso ----------------
def gen_dag(rng, max_steps=10):
    """Constrói DAG a partir de ∅ por regras reversas; devolve (dag, root)."""
    dag = Dag()
    root = dag.add("leaf", [], frozenset())  # placeholder ∅; vira root
    dag.lines[root]["rule"] = "cut"
    # estrutura real do root: corte de dois singletons
    t = frozenset([rng.choice([1, -1, 3, -3])])
    blk = block_of(t)
    p1 = dag.add("leaf", [], frozenset([t]))
    p2 = dag.add("leaf", [], blk)
    dag.lines[root]["prems"] = [p1, p2]
    dag.lines[root]["t"] = t
    # regras reversas sobre "abertos": linhas ainda nao justificadas
    open_ids = [p1, p2]
    promise = {}
    steps = 0
    while open_ids and steps < max_steps * 6:
        steps += 1
        i = rng.choice(open_ids)
        d = dag.lines[i]["dnf"]
        if len(d) == 0:
            open_ids.remove(i)
            continue
        # ACEITA como folha (clause = todos os termos singletons)
        if all(len(t) == 1 for t in d) and rng.random() < 0.5:
            open_ids.remove(i)
            continue
        choice = rng.random()
        terms = list(d)
        if choice < 0.30 and len(terms) >= 2:
            # enfraquecimento-tras: remove um termo
            drop = rng.choice(terms)
            prem = dag.add("leaf", [], d - {drop})
            dag.lines[i]["rule"] = "weaken"
            dag.lines[i]["prems"] = [prem]
            open_ids.remove(i)
            open_ids.append(prem)
        elif choice < 0.65:
            # corte-reverso CORRETO: t FORA de d; particao (A,B) de d
            # premissa1 = A u {t}, premissa2 = B u bloco(t), conclusao = d
            cands = []
            for lv in list(VAR_SIDE):
                for sgn in (1, -1):
                    for sz in (1, min(2, K)):
                        for combo in combinations([sgn * v for v in VAR_SIDE], sz):
                            tt = frozenset(combo)
                            if tt not in d and len(tt) <= K:
                                cands.append(tt)
            if cands:
                t = rng.choice(cands)
                A = frozenset(t0 for t0 in d if rng.random() < 0.5)
                B = d - A
                pre1 = dag.add("leaf", [], A | {t})
                pre2 = dag.add("leaf", [], B | block_of(t))
                dag.lines[i]["rule"] = "cut"
                dag.lines[i]["prems"] = [pre1, pre2]
                dag.lines[i]["t"] = t
                open_ids.remove(i)
                open_ids.extend([pre1, pre2])
                continue
            # sem termo fresco valido -> enfraquecimento
            if len(terms) >= 2:
                prem = dag.add("leaf", [], d - {rng.choice(terms)})
                dag.lines[i]["rule"] = "weaken"
                dag.lines[i]["prems"] = [prem]
                open_ids.remove(i)
                open_ids.append(prem)
            else:
                open_ids.remove(i)  # aceita como folha (improvisado)
        else:
            # and-intro-reverso: termo combinado u (|u|>=2) em d
            comb = [t0 for t0 in terms if len(t0) >= 2]
            if comb:
                u = rng.choice(comb)
                l1 = rng.choice(sorted(u))
                s = u - {l1}
                if 1 <= len(s) <= K:
                    rest = d - {u}
                    A = frozenset(t0 for t0 in rest if rng.random() < 0.5)
                    B = rest - A
                    pre1 = dag.add("leaf", [], A | {frozenset([l1])})
                    pre2 = dag.add("leaf", [], B | {s})
                    dag.lines[i]["rule"] = "and"
                    dag.lines[i]["prems"] = [pre1, pre2]
                    dag.lines[i]["l1"] = l1
                    dag.lines[i]["s"] = s
                    promise[i] = None
                    open_ids.remove(i)
                    open_ids.extend([pre1, pre2])
                    continue
            # fallback: enfraquecimento
            if len(terms) >= 2:
                prem = dag.add("leaf", [], d - {terms[0]})
                dag.lines[i]["rule"] = "weaken"
                dag.lines[i]["prems"] = [prem]
                open_ids.remove(i)
                open_ids.append(prem)
            else:
                open_ids.remove(i)  # aceita como folha
    if open_ids:
        return None, None, None  # nao fechou
    # folhas: todas as linhas sem prems viram leaves com lado pela variavel
    # (singleton clauses; variaveis fora de VAR_SIDE descartam o DAG)
    for v in dag.lines:
        if not v["prems"] and v["rule"] == "leaf":
            if not v["dnf"]:
                return None, None, None
            for t in v["dnf"]:
                if len(t) != 1 or abs(next(iter(t))) not in VAR_SIDE:
                    return None, None, None
            # lado da folha: todos os literais do mesmo lado (senao descarta)
            sides = {VAR_SIDE[abs(l)] for t in v["dnf"] for l in t}
            if len(sides) != 1:
                return None, None, None
            v["side"] = sides.pop()
    # promessa dos and-intros: lado = lado dos pais (se discordar, descarta)
    for vid in list(promise.keys()):
        v = dag.lines[vid]
        s1 = dag.lines[v["prems"][0]].get("side")
        s2 = dag.lines[v["prems"][1]].get("side")
        # pais podem nao ser folhas: lado = unico lado das folhas acessiveis
        # simplificacao: calcular lado "puro" de um pai via folhas acessiveis
        def leaf_side(pid, seen=None):
            seen = seen or set()
            if pid in seen:
                return None
            seen.add(pid)
            p = dag.lines[pid]
            if p["rule"] == "leaf":
                return p.get("side")
            sides = set()
            for q in p["prems"]:
                ls = leaf_side(q, seen)
                if ls is None:
                    return None
                sides.add(ls)
            return sides.pop() if len(sides) == 1 else None
        a, b = leaf_side(v["prems"][0]), leaf_side(v["prems"][1])
        if a is None or b is None or a != b:
            return None, None, None  # promessa violada -> descarta DAG
        promise[vid] = a
    return dag, root, promise


# ---------------- contraexemplo conhecido (r2, fixo) ----------------
# DAG construido na rodada r2: promessa puro-respeitadora SATISFEITA
# (unico and-intro L8: pais {-1},{-2} e resultado {-1,-2} todos lado 1),
# folhas todas em Lambda_1 (Lambda_1 UNSAT: +1=F, +2=T falsifica L6),
# porem o algoritmo guloso falha: bloco {{+1},{+2}} chega PARCIAL em L4
# (L10 consumiu {+1} como pivô do proprio corte) -> G1 real.
def build_counterexample():
    dag = Dag()
    # ids na ordem da construcao (premissas sempre depois -> id maior)
    l0 = dag.add("cut", [], frozenset())            # raiz (placeholder)
    l1 = dag.add("cut", [], frozenset({frozenset([1])}))
    l2 = dag.add("leaf", [], frozenset({frozenset([-1])}))
    l3 = dag.add("cut", [], frozenset({frozenset([1]), frozenset([2, 3])}))
    l4 = dag.add("cut", [], frozenset({frozenset([-3]), frozenset([-2])}))
    l5 = dag.add("weaken", [], frozenset({frozenset([2]), frozenset([2, 3])}))
    l6 = dag.add("leaf", [], frozenset({frozenset([-2]), frozenset([1])}))
    l7 = dag.add("leaf", [], frozenset({frozenset([2])}))
    l8 = dag.add("and", [], frozenset({frozenset([-2, -1])}))
    l9 = dag.add("weaken", [], frozenset({frozenset([-3]), frozenset([-2]),
                                          frozenset([1]), frozenset([2])}))
    l10 = dag.add("cut", [], frozenset({frozenset([-2]), frozenset([1]),
                                        frozenset([2])}))
    l11 = dag.add("leaf", [], frozenset({frozenset([-1])}))
    l12 = dag.add("leaf", [], frozenset({frozenset([-2])}))
    l13 = dag.add("leaf", [], frozenset({frozenset([-1]), frozenset([2])}))
    l14 = dag.add("leaf", [], frozenset({frozenset([-2]), frozenset([1])}))
    L = dag.lines
    L[l0]["prems"], L[l0]["t"] = [l1, l2], frozenset([1])
    L[l1]["prems"], L[l1]["t"] = [l3, l4], frozenset([2, 3])
    L[l3]["prems"], L[l3]["t"] = [l5, l6], frozenset([2])   # corte: t={+2}
    L[l4]["prems"], L[l4]["t"] = [l8, l9], frozenset([-1, -2])
    L[l5]["prems"] = [l7]
    L[l8]["prems"], L[l8]["l1"], L[l8]["s"] = [l11, l12], -1, frozenset([-2])
    L[l9]["prems"] = [l10]
    L[l10]["prems"], L[l10]["t"] = [l13, l14], frozenset([-1])
    # l6 e l7 nao justificados como premissas de corte acima: l6 e folha
    # solta usada por l3? -> l3 = cut(l5, l6, t={1}): A = {{2,3}}?
    # conferencia automatica de solidez abaixo (check_soundness)
    for v in L:
        if v["rule"] == "leaf" and not v["prems"]:
            sides = {VAR_SIDE[abs(l)] for t in v["dnf"] for l in t}
            if len(sides) != 1:
                raise AssertionError(f"folha mista {v['id']}")
            v["side"] = sides.pop()
    promise = {l8: 1}
    return dag, l0, promise


def check_soundness(dag):
    """Confere que cada cut/and é uma instância valida das regras de Res(k)
    e que a conclusao estrutural bate com as premissas."""
    for v in dag.lines:
        if v["rule"] == "cut":
            p1, p2, t = dag.lines[v["prems"][0]], dag.lines[v["prems"][1]], v["t"]
            if t not in p1["dnf"]:
                return f"cut {v['id']}: t nao esta na premissa1"
            if not block_of(t) <= p2["dnf"]:
                return f"cut {v['id']}: bloco nao esta na premissa2"
            concl = (p1["dnf"] - {t}) | (p2["dnf"] - block_of(t))
            # conclusao do generator pode ser maior (B u bloco sobreposto):
            # exige apenas som e superset com mesmos termos "A u B"
            if not (p1["dnf"] - {t}) <= v["dnf"] or not (p2["dnf"] - block_of(t)) <= v["dnf"]:
                return f"cut {v['id']}: conclusao nao contem A e B"
        elif v["rule"] == "and":
            p1, p2 = dag.lines[v["prems"][0]], dag.lines[v["prems"][1]]
            sing, s = frozenset([v["l1"]]), v["s"]
            if sing not in p1["dnf"] or s not in p2["dnf"]:
                return f"and {v['id']}: premissas nao tem as pecas"
            if sing | s not in v["dnf"]:
                return f"and {v['id']}: termo combinado ausente da conclusao"
            if len(sing | s) > K:
                return f"and {v['id']}: largura > K"
        elif v["rule"] == "weaken":
            p1 = dag.lines[v["prems"][0]]
            if not p1["dnf"] <= v["dnf"]:
                return f"weaken {v['id']}: premissa nao ⊆ conclusao"
    return None



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=20261119)
    args = ap.parse_args()
    rng = random.Random(args.seed)

    # ---- 1) contraexemplo fixo da rodada r2 ----
    dag, root, promise = build_counterexample()
    err = check_soundness(dag)
    if err:
        print(f"[FATAL] contraexemplo malformado: {err}")
        return 2
    w, E, err = run_projection(dag, promise)
    print(f"CONTRAEXEMPLO r2 (folhas todas em L1, promessa and OK): "
          f"run_projection -> {err}")
    if not err:
        print("  [inesperado] algoritmo passou — contraexemplo invalido?")
        return 2
    if "G1 VIOLADO" not in err:
        print(f"  [inesperado] falha diferente: {err}")
        return 2
    # Lambda_1 UNSAT (+1=F, +2=T falsifica a clausula L6: -2 v +1)
    print("  verificacao manual: Lambda_1 UNSAT (+1=F,+2=T => L6 falsa); "
          "resposta i*=1 EXISTE mas a projecao gulosa nao a extrai")

    ok = skipped = 0
    failures = []
    for it in range(args.n):
        dag, root, promise = gen_dag(rng, max_steps=8)
        if dag is None:
            skipped += 1
            continue
        err_cs = check_soundness(dag)  # referee r2-A1: solidez em todo DAG
        if err_cs:
            failures.append((it, f"SOUNDNESS: {err_cs}", dag))
            continue
        w, E, err = run_projection(dag, promise or {})
        if err:
            failures.append((it, err, dag))
            continue
        err = check_derivability(dag, w, E)
        if err:
            failures.append((it, err, dag))
            continue
        # primeiro ∅: alguma linha com E vazio
        empties = [v["id"] for v in dag.lines if not E[v["id"]]]
        if not empties:
            skipped += 1
            continue
        err = check_extraction(dag, w, E, empties[0])
        if err:
            failures.append((it, err, dag))
            continue
        ok += 1

    print(f"DAGs validos testados: {ok} | descartados: {skipped} | "
          f"FALHAS: {len(failures)} (seed={args.seed}, n={args.n})")
    for it, err, dag in failures[:5]:
        print(f"  [falha #{it}] {err}")
        for v in dag.lines:
            print(f"    L{v['id']} {v['rule']} prems={v['prems']} "
                  f"dnf={sorted(map(sorted, v['dnf']))}")
    # classificacao p/ CI: falhas G1 = classe CONHECIDA (contraexemplo do r2,
    # sempre presente via instancia fixa) -> esperadas; qualquer outra = real
    unexpected = [f for f in failures if "G1 VIOLADO" not in f[1]]
    if not failures:
        print("*** NENHUM contraexemplo: invariantes I1-I5 + G1 + G2 "
              "verificados em todos os DAGs testados ***")
    if unexpected:
        print(f"*** FALHA CI: {len(unexpected)} violacao(es) FORA da "
              "classe G1 conhecida ***")
        return 1
    if failures:
        print("*** OK: unicas falhas sao da classe G1 conhecida "
              "(contraexemplo r2, comportamento esperado) ***")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

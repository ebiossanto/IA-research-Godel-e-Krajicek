#!/usr/bin/env python3
"""
EXTENDED CHAIN — T_ω = PA + RFN^ω(PA) (Limite Ordinal)
Estende a cadeia de teorias para o limite transfinito ω.
Testa comportamento de Δ, PPR e RBT no limite.
"""

import json
import math
import csv
import os
from dataclasses import dataclass, asdict
from typing import List, Dict, Set, Optional, Callable
from datetime import datetime, timezone
from itertools import product
from collections import Counter
import psutil
import numpy as np

@dataclass
class Obligation:
    idx: str
    is_wstar: bool
    kappa: int

@dataclass
class Theory:
    name: str
    sigma: int          # força de reflexão (ordinal aproximado)
    is_T1_plus: bool
    ordinal_rank: str   # "0", "1", "2", ..., "ω"

@dataclass
class OrdinalTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    theory_name: str
    ordinal_rank: str
    sigma: int
    b: int
    delta: int
    w0: str
    entropy: float
    cpu_percent: float
    memory_mb: float
    limit_behavior: str  # "FINITE", "LIMIT", "DIVERGENT"

class OrdinalChainExperiment:
    def __init__(self, phi_len: int = 12, r_w: int = 4, w_star: str = "00"):
        self.phi_len = phi_len
        self.r_w = r_w
        self.w_star = w_star
        self.obligations = self._build_obligations()
        self.telemetry_log: List[OrdinalTelemetry] = []
        
    def _build_obligations(self) -> List[Obligation]:
        obligations = []
        for bits in product('01', repeat=self.r_w):
            w = ''.join(bits)
            is_wstar = w.startswith(self.w_star)
            kappa = 2 if is_wstar else (sum(ord(c) for c in w) % 2)
            obligations.append(Obligation(idx=w, is_wstar=is_wstar, kappa=kappa))
        return obligations
    
    def proof_complexity(self, T: Theory, o: Obligation) -> int:
        INF = 10**9
        if T.is_T1_plus:
            if o.is_wstar:
                return 20
            h = sum(ord(c) for c in o.idx)
            return 8 + (h % 17)
        else:
            if o.is_wstar:
                return INF
            h = sum(ord(c) for c in o.idx)
            return 8 + (h % 17)
    
    def covered(self, T: Theory, b: int, o: Obligation) -> bool:
        return self.proof_complexity(T, o) <= b
    
    def delta(self, T: Theory, b: int) -> int:
        trues = [o for o in self.obligations if True]
        cov = [o for o in trues if self.covered(T, b, o)]
        return len(trues) - len(cov)
    
    def first_uncovered(self, T: Theory, b: int) -> Optional[str]:
        for o in sorted(self.obligations, key=lambda x: x.idx):
            if not self.covered(T, b, o):
                return o.idx
        return None
    
    def generator(self, T: Theory, u: str, a: Callable[[int], int], b: int) -> str:
        n = len(u)
        if n < self.phi_len or self.phi_len > a(n):
            return '0' * (n + 1)
        w0 = self.first_uncovered(T, b)
        if w0 is None:
            return '0' * (n + 1)
        return w0 + u[self.phi_len:]
    
    def compute_entropy(self, data: List[float]) -> float:
        if not data:
            return 0.0
        discretized = [round(d/5)*5 for d in data]
        counts = Counter(discretized)
        total = len(discretized)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())
    
    def build_ordinal_chain(self, max_finite: int = 10) -> List[Theory]:
        """Constrói cadeia: PA, PA+RFN_1, PA+RFN_2, ..., PA+RFN_ω"""
        chain = [Theory(name="PA", sigma=0, is_T1_plus=False, ordinal_rank="0")]
        
        # Teorias finitas: PA+RFN_n para n=1..max_finite
        for n in range(1, max_finite + 1):
            chain.append(Theory(
                name=f"PA+RFN_{n}", 
                sigma=n, 
                is_T1_plus=True, 
                ordinal_rank=str(n)
            ))
        
        # Limite ω: sigma = ω (aproximado por max_finite + 1 grande)
        # No modelo: sigma = max_finite + 100 (simula força infinita)
        chain.append(Theory(
            name="PA+RFN^ω", 
            sigma=max_finite + 100,  # "infinito" prático
            is_T1_plus=True, 
            ordinal_rank="ω"
        ))
        
        return chain
    
    def run_ordinal_experiment(self, max_finite: int = 10,
                               b_values: List[int] = None,
                               n_values: List[int] = None,
                               a: Callable[[int], int] = None) -> Dict:
        if b_values is None:
            b_values = [4, 8, 12, 16, 20, 24, 32, 48, 64, 128, 256]
        if n_values is None:
            n_values = [12, 14, 16]
        if a is None:
            a = lambda n: max(12, min(n, 16))
        
        theories = self.build_ordinal_chain(max_finite)
        cpu_history = []
        
        results = {
            "metadata": {
                "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                "phi_len": self.phi_len,
                "r_w": self.r_w,
                "w_star": self.w_star,
                "max_finite": max_finite,
                "theories": [f"{T.name}(σ={T.sigma}, ord={T.ordinal_rank})" for T in theories],
                "b_values": b_values,
                "n_values": n_values
            },
            "delta_by_theory": [],
            "rbt_by_theory": [],
            "limit_analysis": [],
            "ppr_to_omega": [],
            "phase_transitions": [],
            "telemetry_count": 0
        }
        
        print("=" * 70)
        print("EXTENDED CHAIN: T_omega = PA + RFN^omega(PA)")
        print("=" * 70)
        
        # 1. Delta chain para cada teoria
        for T in theories:
            T_results = {"theory": T.name, "ordinal": T.ordinal_rank, "sigma": T.sigma, "delta_table": [], "rbt_table": []}
            prev_w0 = None
            
            for b in b_values:
                d = self.delta(T, b)
                w0 = self.first_uncovered(T, b) or "ALL_COV"
                
                rbt = False
                if prev_w0 is not None and prev_w0 != "ALL_COV" and w0 != "ALL_COV" and w0 != prev_w0:
                    rbt = True
                
                T_results["delta_table"].append({"b": b, "delta": d, "w0": w0, "rbt": rbt})
                if rbt:
                    T_results["rbt_table"].append({"b": b, "w0": w0})
                    results["phase_transitions"].append({
                        "type": "RBT",
                        "theory": T.name,
                        "ordinal": T.ordinal_rank,
                        "b": b,
                        "w0_from": prev_w0,
                        "w0_to": w0
                    })
                
                prev_w0 = w0
                
                # Telemetria
                cpu = psutil.cpu_percent(interval=None)
                cpu_history.append(cpu)
                entropy = self.compute_entropy(cpu_history[-50:])
                
                limit_behavior = "FINITE"
                if T.ordinal_rank == "ω":
                    limit_behavior = "LIMIT"
                elif d == 0 and b >= 100:
                    limit_behavior = "STABLE_ZERO"
                
                tel = OrdinalTelemetry(
                    timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                    data_source="gk_ordinal_chain.py (T_ω Extended Chain)",
                    metric_type="ordinal_delta_telemetry",
                    theory_name=T.name,
                    ordinal_rank=T.ordinal_rank,
                    sigma=T.sigma,
                    b=b,
                    delta=d,
                    w0=w0,
                    entropy=entropy,
                    cpu_percent=cpu,
                    memory_mb=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
                    limit_behavior=limit_behavior
                )
                self.telemetry_log.append(tel)
            
            results["delta_by_theory"].append(T_results)
            d256 = next(r['delta'] for r in T_results['delta_table'] if r['b']==256)
            out = "  " + T.name + " (ord=" + T.ordinal_rank + ", sigma=" + str(T.sigma) + "): delta(b=256)=" + str(d256) + ", RBTs=" + str(len(T_results['rbt_table']))
            print(out.encode('ascii', 'ignore').decode('ascii'))
        
        # 2. Analise do Limite omega
        omega_theory = theories[-1]
        finite_theories = theories[:-1]
        
        print("\n--- Analise do Limite omega ---")
        
        # Convergência de Δ
        convergence = {}
        for b in b_values:
            deltas = [next(r['delta'] for r in T['delta_table'] if r['b']==b) for T in results["delta_by_theory"][:-1]]
            omega_delta = next(r['delta'] for r in results["delta_by_theory"][-1]['delta_table'] if r['b']==b)
            
            # Verifica se sequência converge
            if len(deltas) >= 3:
                stable = all(d == deltas[-1] for d in deltas[-3:])
                convergence[b] = {
                    "finite_deltas": deltas,
                    "omega_delta": omega_delta,
                    "converged": stable,
                    "limit_value": deltas[-1] if stable else None,
                    "omega_matches_limit": (omega_delta == deltas[-1]) if stable else False
                }
        
        results["limit_analysis"] = [{
            "b": b, **v
        } for b, v in convergence.items()]
        
        for b, v in convergence.items():
            status = "CONVERGIDO" if v["converged"] else "OSCILA"
            match = "SIM" if v["omega_matches_limit"] else "NAO"
            print(f"  b={b:3d}: delta_finito={v['finite_deltas'][-3:]} -> delta_omega={v['omega_delta']} | {status} | omega=lim? {match}")
        
        # 3. PPR das finitas para omega
        print("\n--- PPR: T_n -> T_omega ---")
        for T_fin in finite_theories[-3:]:  # últimas 3 finitas
            for R_name, R_fn in [("suffix0", lambda s: s + '0'), ("id", lambda s: s)]:
                violations_total = 0
                tests_total = 0
                
                for n in n_values:
                    if n < self.phi_len:
                        continue
                    u0_len = n - self.phi_len
                    phi_prefix = "PA_CONENCOD"[:self.phi_len].ljust(self.phi_len, '0')
                    
                    for b in b_values:
                        img_fin, img_omega = set(), set()
                        for bits in product('01', repeat=u0_len):
                            u = phi_prefix + ''.join(bits)
                            img_fin.add(self.generator(T_fin, u, a, b))
                            img_omega.add(self.generator(omega_theory, u, a, b))
                        
                        all_out = {''.join(p) for p in product('01', repeat=n+1)}
                        comp_fin = all_out - img_fin
                        
                        violations = 0
                        for b_out in comp_fin:
                            if R_fn(b_out) in img_omega:
                                violations += 1
                        
                        tests_total += 1
                        violations_total += violations
                
                passed = violations_total == 0
                results["ppr_to_omega"].append({
                    "from": T_fin.name,
                    "to": "PA+RFN^ω",
                    "R": R_name,
                    "tests": tests_total,
                    "violations": violations_total,
                    "passed": passed
                })
                status = "PASS" if passed else "FAIL"
                out = "  " + T_fin.name + " -> PA+RFN^omega via " + R_name + ": " + status + " (violations=" + str(violations_total) + ")"
                print(out.encode('ascii', 'ignore').decode('ascii'))
        
        results["telemetry_count"] = len(self.telemetry_log)
        return results
    
    def save_results(self, results: Dict, prefix: str = "gk_ordinal_chain"):
        with open(f"{prefix}.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, default=str)
        
        with open(f"{prefix}_delta.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["theory", "ordinal", "sigma", "b", "delta", "w0", "rbt"])
            writer.writeheader()
            for T_res in results["delta_by_theory"]:
                for row in T_res["delta_table"]:
                    writer.writerow({
                        "theory": T_res["theory"], "ordinal": T_res["ordinal"], 
                        "sigma": T_res["sigma"], "b": row["b"], 
                        "delta": row["delta"], "w0": row["w0"], "rbt": row["rbt"]
                    })
        
        with open(f"{prefix}_limit.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["b", "finite_deltas", "omega_delta", "converged", "limit_value", "omega_matches_limit"])
            writer.writeheader()
            for row in results["limit_analysis"]:
                writer.writerow(row)
        
        with open(f"{prefix}_ppr_omega.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["from", "to", "R", "tests", "violations", "passed"])
            writer.writeheader()
            writer.writerows(results["ppr_to_omega"])
        
        with open(f"{prefix}_telemetry.csv", "w", newline="", encoding="utf-8") as f:
            if self.telemetry_log:
                writer = csv.DictWriter(f, fieldnames=list(asdict(self.telemetry_log[0]).keys()))
                writer.writeheader()
                for t in self.telemetry_log:
                    writer.writerow(asdict(t))
        
        print(f"\n[ORDINAL] Resultados salvos: {prefix}.json, {prefix}_*.csv")

def main():
    print("=" * 70)
    print("EXTENDED CHAIN: T_omega = PA + RFN^omega(PA)")
    print("=" * 70)
    
    exp = OrdinalChainExperiment(phi_len=12, r_w=4, w_star="00")
    results = exp.run_ordinal_experiment(max_finite=8)
    exp.save_results(results, "gk_ordinal_chain")
    
    print("\n" + "=" * 70)
    print("RESUMO T_omega")
    print("=" * 70)
    
    # Verifica convergência
    converged_all = all(v.get("converged", False) for v in results["limit_analysis"])
    omega_matches = all(v.get("omega_matches_limit", False) for v in results["limit_analysis"])
    print(f"Convergencia delta (b>=20): {'SIM' if converged_all else 'PARCIAL'}")
    print(f"omega atinge limite: {'SIM' if omega_matches else 'NAO'}")
    
    # PPR para omega
    ppr_passed = sum(1 for r in results["ppr_to_omega"] if r["passed"])
    ppr_total = len(results["ppr_to_omega"])
    print(f"PPR T_n -> T_omega: {ppr_passed}/{ppr_total} passed")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
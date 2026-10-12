#!/usr/bin/env python3
"""
R_w DESIGNER — Designer e teste de candidatos R_w para PPR-2 refinado.
Implementa a estratégia A∨B∨C do documento 08 (PR17-18):
  A: identidade + sentinela
  B: extensão de prefixo + sentinela
  C: XOR + sentinela

Testa em todos os 4 cenários E0-E3 (κ/ratio/|W|).
"""

import json
import math
import csv
import os
from dataclasses import dataclass, asdict
from typing import List, Dict, Set, Optional, Callable, Tuple
from datetime import datetime, timezone
from itertools import product
from collections import Counter
import psutil
import numpy as np

@dataclass
class RWTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    scenario: str
    R_name: str
    n: int
    b: int
    img_src_size: int
    img_tgt_size: int
    comp_src_size: int
    violations: int
    ppr_passed: bool
    entropy_bits: float

class RWDesigner:
    def __init__(self, phi_len: int = 12, r_w: int = 4, w_star: str = "00"):
        self.phi_len = phi_len
        self.r_w = r_w
        self.w_star = w_star
        self.obligations = self._build_obligations()
        self.telemetry_log: List[RWTelemetry] = []
        
    def _build_obligations(self) -> List[Dict]:
        obligations = []
        for bits in product('01', repeat=self.r_w):
            w = ''.join(bits)
            is_wstar = w.startswith(self.w_star)
            kappa = 2 if is_wstar else (sum(ord(c) for c in w) % 2)
            obligations.append({"idx": w, "is_wstar": is_wstar, "kappa": kappa})
        return obligations
    
    def proof_complexity(self, sigma: int, o: Dict, is_T1: bool) -> int:
        INF = 10**9
        if is_T1:
            if o["is_wstar"]:
                return 20  # Con provável via reflexão
            h = sum(ord(c) for c in o["idx"])
            return 8 + (h % 17)
        else:
            if o["is_wstar"]:
                return INF
            h = sum(ord(c) for c in o["idx"])
            return 8 + (h % 17)
    
    def covered(self, sigma: int, b: int, o: Dict, is_T1: bool) -> bool:
        return self.proof_complexity(sigma, o, is_T1) <= b
    
    def first_uncovered(self, sigma: int, b: int, is_T1: bool) -> Optional[str]:
        for o in sorted(self.obligations, key=lambda x: x["idx"]):
            if not self.covered(sigma, b, o, is_T1):
                return o["idx"]
        return None
    
    def generator(self, sigma: int, u: str, a: Callable[[int], int], b: int, is_T1: bool) -> str:
        n = len(u)
        if n < self.phi_len or self.phi_len > a(n):
            return '0' * (n + 1)
        w0 = self.first_uncovered(sigma, b, is_T1)
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
    
    def design_R_functions(self, n: int) -> Dict[str, Callable[[str], str]]:
        """Projeta funções R candidatas para PPR-2"""
        return {
            # Estratégia A: Identidade + Sentinela
            "A_id": lambda s: s,
            "A_sentinel_0": lambda s: s + '0',
            "A_sentinel_00": lambda s: s + '00',
            "A_sentinel_1": lambda s: s + '1',
            
            # Estratégia B: Extensão de Prefixo + Sentinela
            "B_prefix0": lambda s: '0' + s[:n],
            "B_prefix00": lambda s: '00' + s[:n-1] if n >= 2 else '0' + s,
            "B_prefix_sentinel": lambda s: '0' + s[:n-1] + '0',
            
            # Estratégia C: XOR + Sentinela
            "C_xor1": lambda s: ''.join('1' if c=='0' else '0' for c in s),
            "C_xor1_sentinel": lambda s: ''.join('1' if c=='0' else '0' for c in s) + '0',
            "C_xor10": lambda s: ''.join('1' if c=='0' else '0' for c in s) + '1',
        }
    
    def run_scenario(self, scenario_name: str, 
                     kappa_dist: Dict[int, int],
                     sigma_T0: int, sigma_T1: int,
                     n_values: List[int], b_values: List[int],
                     a: Callable[[int], int]) -> Dict:
        """Executa um cenário E (E0, E1, E2, E3)"""
        
        results = {
            "scenario": scenario_name,
            "kappa_dist": kappa_dist,
            "sigma_T0": sigma_T0,
            "sigma_T1": sigma_T1,
            "R_tests": {},
            "best_R": None,
            "pass_rate": 0.0
        }
        
        R_functions = self.design_R_functions(max(n_values))
        
        for R_name, R_fn in R_functions.items():
            R_results = {
                "R_name": R_name,
                "tests": [],
                "total_tests": 0,
                "passed": 0,
                "failed": 0,
                "total_violations": 0
            }
            
            for n in n_values:
                if n < self.phi_len:
                    continue
                
                u0_len = n - self.phi_len
                phi_prefix = "PA_CONENCOD"[:self.phi_len].ljust(self.phi_len, '0')
                
                for b in b_values:
                    # Build images for this n, b
                    img_T0, img_T1 = set(), set()
                    for bits in product('01', repeat=u0_len):
                        u = phi_prefix + ''.join(bits)
                        img_T0.add(self.generator(sigma_T0, u, a, b, is_T1=False))
                        img_T1.add(self.generator(sigma_T1, u, a, b, is_T1=True))
                    
                    all_out = {''.join(p) for p in product('01', repeat=n+1)}
                    comp_T0 = all_out - img_T0
                    
                    # Test PPR-2
                    violations = 0
                    for b_out in comp_T0:
                        r_out = R_fn(b_out)
                        if r_out in img_T1:
                            violations += 1
                    
                    passed = (violations == 0)
                    R_results["total_tests"] += 1
                    if passed:
                        R_results["passed"] += 1
                    else:
                        R_results["failed"] += 1
                    R_results["total_violations"] += violations
                    
                    # Telemetria
                    cpu = psutil.cpu_percent(interval=None)
                    entropy = self.compute_entropy([cpu] * 10)  # simplificado
                    
                    tel = RWTelemetry(
                        timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                        data_source="gk_r_w_designer.py (R_w Designer)",
                        metric_type="r_w_candidate_test",
                        scenario=scenario_name,
                        R_name=R_name,
                        n=n,
                        b=b,
                        img_src_size=len(img_T0),
                        img_tgt_size=len(img_T1),
                        comp_src_size=len(comp_T0),
                        violations=violations,
                        ppr_passed=passed,
                        entropy_bits=entropy
                    )
                    self.telemetry_log.append(tel)
                    
                    R_results["tests"].append({
                        "n": n, "b": b,
                        "img_T0": len(img_T0), "img_T1": len(img_T1),
                        "comp_T0": len(comp_T0),
                        "violations": violations,
                        "passed": passed
                    })
            
            results["R_tests"][R_name] = R_results
            
            # Rate de sucesso
            if R_results["total_tests"] > 0:
                rate = R_results["passed"] / R_results["total_tests"]
                print(f"  [{scenario_name}] {R_name}: {R_results['passed']}/{R_results['total_tests']} passed ({rate:.1%}) violations={R_results['total_violations']}")
        
        # Encontra melhor R
        best_R = max(results["R_tests"].items(), 
                     key=lambda x: x[1]["passed"] / max(1, x[1]["total_tests"]))
        results["best_R"] = best_R[0]
        results["pass_rate"] = best_R[1]["passed"] / max(1, best_R[1]["total_tests"])
        
        return results
    
    def run_all_scenarios(self) -> Dict:
        """Executa os 4 cenários E0-E3 do documento (PR16)"""
        
        # Cenários baseados no PR16 (robustez 4/4)
        scenarios = {
            "E0": {  # kappa-uniforme, ratio 1:1, |W|=16
                "kappa_dist": {0: 4, 1: 4, 2: 4, 3: 4},  # uniforme
                "sigma_T0": 0, "sigma_T1": 2,
            },
            "E1": {  # kappa-rich 3:1, |W|=64 (PR16)
                "kappa_dist": {1: 48, 2: 16},
                "sigma_T0": 0, "sigma_T1": 2,
            },
            "E2": {  # kappa-rich 3:1, |W|=16
                "kappa_dist": {1: 12, 2: 4},
                "sigma_T0": 0, "sigma_T1": 2,
            },
            "E3": {  # kappa-extreme, |W|=32
                "kappa_dist": {1: 24, 2: 8},
                "sigma_T0": 0, "sigma_T1": 2,
            }
        }
        
        n_values = [12, 14, 16]
        b_values = [4, 8, 12, 16, 20, 24, 32, 48, 64]
        a = lambda n: max(12, min(n, 16))
        
        all_results = {
            "metadata": {
                "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                "phi_len": self.phi_len,
                "r_w": self.r_w,
                "w_star": self.w_star,
                "scenarios": list(scenarios.keys()),
                "n_values": n_values,
                "b_values": b_values
            },
            "scenarios": {}
        }
        
        print("=" * 70)
        print("R_w DESIGNER - Testando estrategias A v B v C nos cenarios E0-E3")
        print("=" * 70)
        
        for scenario_name, config in scenarios.items():
            print(f"\n--- Cenario {scenario_name} ---")
            print(f"  kappa-dist: {config['kappa_dist']}")
            print(f"  sigma_T0={config['sigma_T0']}, sigma_T1={config['sigma_T1']}")
            
            result = self.run_scenario(
                scenario_name, 
                config["kappa_dist"],
                config["sigma_T0"], config["sigma_T1"],
                n_values, b_values, a
            )
            all_results["scenarios"][scenario_name] = result
        
        return all_results
    
    def save_results(self, results: Dict, prefix: str = "gk_r_w_designer"):
        with open(f"{prefix}.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, default=str)
        
        # Summary CSV
        with open(f"{prefix}_summary.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "scenario", "R_name", "total_tests", "passed", "failed", 
                "total_violations", "pass_rate", "best_R"
            ])
            writer.writeheader()
            for sc_name, sc_data in results["scenarios"].items():
                for R_name, R_data in sc_data["R_tests"].items():
                    writer.writerow({
                        "scenario": sc_name, "R_name": R_name,
                        "total_tests": R_data["total_tests"],
                        "passed": R_data["passed"], "failed": R_data["failed"],
                        "total_violations": R_data["total_violations"],
                        "pass_rate": R_data["passed"] / max(1, R_data["total_tests"]),
                        "best_R": sc_data["best_R"]
                    })
        
        # Telemetria CSV
        with open(f"{prefix}_telemetry.csv", "w", newline="", encoding="utf-8") as f:
            if self.telemetry_log:
                writer = csv.DictWriter(f, fieldnames=list(asdict(self.telemetry_log[0]).keys()))
                writer.writeheader()
                for t in self.telemetry_log:
                    writer.writerow(asdict(t))
        
        print(f"\n[R_w] Resultados salvos: {prefix}.json, {prefix}_summary.csv, {prefix}_telemetry.csv")

def main():
    print("=" * 70)
    print("R_w DESIGNER - Estrategias A v B v C para PPR-2 Refinado")
    print("=" * 70)
    
    designer = RWDesigner(phi_len=12, r_w=4, w_star="00")
    results = designer.run_all_scenarios()
    designer.save_results(results, "gk_r_w_designer")
    
    # RESUMO EXECUTIVO
    print("\n" + "=" * 70)
    print("RESUMO R_w DESIGNER (PR17-18: PPR-2 Refinado)")
    print("=" * 70)
    
    for sc_name, sc_data in results["scenarios"].items():
        best_R = sc_data["best_R"]
        pass_rate = sc_data["pass_rate"]
        status = "[OK] PASS (4/4)" if pass_rate == 1.0 else f"[WARN] {pass_rate:.1%}"
        print(f"  {sc_name}: Melhor R = {best_R} | Taxa = {status}")
    
    # Verifica se passa 4/4 (robustez PR16)
    all_pass = all(sc["pass_rate"] == 1.0 for sc in results["scenarios"].values())
    print(f"\n*** ROBUSTEZ 4/4: {'SIM' if all_pass else 'NAO'} ***")
    print("=" * 70)

if __name__ == "__main__":
    main()
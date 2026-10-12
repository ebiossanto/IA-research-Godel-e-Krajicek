#!/usr/bin/env python3
"""
PPR-EMPIRICAL — Experimento empírico para investigar:
    T₀=PA ⊆ T₁=PA+RFN(PA) ⇒ g_T₀ ≼_ppr g_T₁ ?

Testa as três hipóteses:
  H₁: PPR válida (imagens compatíveis, R=suffix0 funciona)
  H₂: min_lex quebra PPR (w₀^T₁ >_lex w₀^T₀, imagens divergem)
  H₃: PPR condicional (válida só para b > b*)

Integra com Terminal-Laboratório: telemetria, REA Bridge, entropia.
"""

import json
import time
import math
import hashlib
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
class Obligation:
    idx: str
    is_wstar: bool
    kappa: int = 0  # 0, 1, 2 (custo reflexão)

@dataclass
class Theory:
    name: str
    sigma: int          # força de reflexão (0=PA, 1=RFN₁, 2=RFN₂, etc)
    is_T1_plus: bool    # True para teorias com reflexão

@dataclass
class PPRTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    theory_name: str
    sigma: int
    b: int
    n: int
    delta: int
    w0: str
    entropy_cpu: float
    entropy_syscall: float
    exec_time_ms: float
    memory_mb: float
    image_size: int
    comp_size: int
    rbt_detected: bool
    ppr_status: str

class PPRExperiment:
    def __init__(self, phi_len: int = 12, r_w: int = 4, w_star: str = "00"):
        self.phi_len = phi_len
        self.r_w = r_w
        self.w_star = w_star
        self.obligations = self._build_obligations()
        self.telemetry_log: List[PPRTelemetry] = []
        
    def _build_obligations(self) -> List[Obligation]:
        obligations = []
        for bits in product('01', repeat=self.r_w):
            w = ''.join(bits)
            is_wstar = w.startswith(self.w_star)
            kappa = 2 if is_wstar else (sum(ord(c) for c in w) % 2)
            obligations.append(Obligation(idx=w, is_wstar=is_wstar, kappa=kappa))
        return obligations
    
    def proof_complexity(self, T: Theory, o: Obligation) -> int:
        """Complexidade de prova em T para obrigação o"""
        INF = 10**9
        if T.is_T1_plus:
            # T com reflexão: Con(T) provável em 20, genéricas em 8-24
            if o.is_wstar:
                return 20
            h = sum(ord(c) for c in o.idx)
            return 8 + (h % 17)
        else:
            # PA base: Con(T) = INF, genéricas em 8-24
            if o.is_wstar:
                return INF
            h = sum(ord(c) for c in o.idx)
            return 8 + (h % 17)
    
    def covered(self, T: Theory, b: int, o: Obligation) -> bool:
        return self.proof_complexity(T, o) <= b
    
    def delta(self, T: Theory, b: int) -> int:
        trues = [o for o in self.obligations if not o.is_wstar or True]  # todas true no modelo
        cov = [o for o in trues if self.covered(T, b, o)]
        return len(trues) - len(cov)
    
    def first_uncovered(self, T: Theory, b: int) -> Optional[str]:
        for o in sorted(self.obligations, key=lambda x: x.idx):
            if not self.covered(T, b, o):
                return o.idx
        return None  # ALL_COV
    
    def generator(self, T: Theory, u: str, a: Callable[[int], int], b: int) -> str:
        n = len(u)
        if n < self.phi_len or self.phi_len > a(n):
            return '0' * (n + 1)
        w0 = self.first_uncovered(T, b)
        if w0 is None:
            return '0' * (n + 1)
        phi = u[:self.phi_len]
        u0 = u[self.phi_len:]
        return w0 + u0
    
    def compute_entropy(self, data: List[float]) -> float:
        if not data:
            return 0.0
        discretized = [round(d/5)*5 for d in data]
        counts = Counter(discretized)
        total = len(discretized)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())
    
    def build_theory_chain(self, max_sigma: int) -> List[Theory]:
        """Constrói cadeia T_0, T_1, ..., T_max_sigma"""
        chain = [Theory(name="PA", sigma=0, is_T1_plus=False)]
        for s in range(1, max_sigma + 1):
            chain.append(Theory(name=f"PA+RFN_{s}", sigma=s, is_T1_plus=True))
        return chain
    
    def run_ppr_test(self, T_src: Theory, T_tgt: Theory, 
                     n_values: List[int], b_values: List[int], 
                     a: Callable[[int], int], 
                     R_fn: Callable[[str], str],
                     R_name: str) -> Dict:
        """
        Testa PPR: g_T_src ≼_ppr g_T_tgt via R
        PPR-1: m ≤ p(n), |β| ≤ p(n+|b|)
        PPR-2: b ∉ rng(g_src) ⇒ R(b) ∉ rng(g_tgt)
        """
        results = {
            "R_name": R_name,
            "T_src": T_src.name,
            "T_tgt": T_tgt.name,
            "tests": [],
            "ppr_violations": 0,
            "ppr_passes": 0
        }
        
        for n in n_values:
            if n < self.phi_len:
                continue
            
            u0_len = n - self.phi_len
            phi_prefix = "PA_CONENCOD"[:self.phi_len].ljust(self.phi_len, '0')
            
            # Build images for this n
            img_src, img_tgt = set(), set()
            for bits in product('01', repeat=u0_len):
                u = phi_prefix + ''.join(bits)
                img_src.add(self.generator(T_src, u, a, 32))
                img_tgt.add(self.generator(T_tgt, u, a, 32))
            
            all_out = {''.join(p) for p in product('01', repeat=n+1)}
            comp_src = all_out - img_src
            
            for b in b_values:
                # Recompute images for this b (affects generator via first_uncovered)
                img_src_b, img_tgt_b = set(), set()
                for bits in product('01', repeat=u0_len):
                    u = phi_prefix + ''.join(bits)
                    img_src_b.add(self.generator(T_src, u, a, b))
                    img_tgt_b.add(self.generator(T_tgt, u, a, b))
                
                comp_src_b = all_out - img_src_b
                
                # Test PPR-2: for each b_out ∉ img_src, check R(b_out) ∉ img_tgt
                violations = 0
                for b_out in comp_src_b:
                    r_out = R_fn(b_out)
                    if r_out in img_tgt_b:
                        violations += 1
                
                passed = (violations == 0)
                if passed:
                    results["ppr_passes"] += 1
                else:
                    results["ppr_violations"] += violations
                
                results["tests"].append({
                    "n": n, "b": b,
                    "img_src_size": len(img_src_b),
                    "img_tgt_size": len(img_tgt_b),
                    "comp_src_size": len(comp_src_b),
                    "violations": violations,
                    "ppr_passed": passed
                })
        
        return results
    
    def run_full_experiment(self, max_sigma: int = 3, 
                            n_values: List[int] = None,
                            b_values: List[int] = None,
                            a: Callable[[int], int] = None):
        """Experimento completo: chain de teorias + PPR + telemetria"""
        if n_values is None:
            n_values = [12, 14, 16]
        if b_values is None:
            b_values = [4, 8, 12, 16, 20, 24, 32, 48, 64]
        if a is None:
            a = lambda n: max(12, min(n, 16))
        
        theories = self.build_theory_chain(max_sigma)
        R_functions = {
            "id": lambda s: s,
            "xor1": lambda s: ''.join('1' if c=='0' else '0' for c in s),
            "prefix0": lambda s: '0' + s[:len(s)-1],
            "suffix0": lambda s: s + '0',
            "suffix00": lambda s: s + '00',
        }
        
        results = {
            "metadata": {
                "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                "phi_len": self.phi_len,
                "r_w": self.r_w,
                "w_star": self.w_star,
                "theories": [f"{T.name}(σ={T.sigma})" for T in theories],
                "n_values": n_values,
                "b_values": b_values,
                "R_functions": list(R_functions.keys())
            },
            "delta_chain": [],
            "rbt_chain": [],
            "ppr_matrix": [],
            "image_analysis": [],
            "phase_transitions": [],
            "telemetry_count": 0
        }
        
        cpu_history = []
        
        # 1. CADEIA DE Delta (Delta chain) — para cada teoria
        print("=" * 70)
        print("PPR-EMPIRICAL: Cadeia de Teorias + Delta + RBT")
        print("=" * 70)
        
        for T in theories:
            T_results = {"theory": T.name, "sigma": T.sigma, "delta_table": [], "rbt_table": []}
            prev_w0 = None
            
            for b in b_values:
                d = self.delta(T, b)
                w0 = self.first_uncovered(T, b) or "ALL_COV"
                
                # RBT detection: mudança de w0 em relação à teoria anterior
                rbt = False
                if prev_w0 is not None and prev_w0 != "ALL_COV" and w0 != "ALL_COV" and w0 != prev_w0:
                    rbt = True
                    results["phase_transitions"].append({
                        "type": "RBT",
                        "from_theory": theories[theories.index(T)-1].name if T != theories[0] else "NONE",
                        "to_theory": T.name,
                        "b": b,
                        "w0_from": prev_w0,
                        "w0_to": w0
                    })
                
                T_results["delta_table"].append({
                    "b": b, "delta": d, "w0": w0, "rbt": rbt
                })
                if rbt:
                    T_results["rbt_table"].append({"b": b, "w0": w0})
                
                prev_w0 = w0
                
                # Telemetria
                cpu = psutil.cpu_percent(interval=None)
                cpu_history.append(cpu)
                entropy = self.compute_entropy(cpu_history[-50:])
                
                tel = PPRTelemetry(
                    timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                    data_source="gk_ppr_experiment.py (PPR-Empirical)",
                    metric_type="ppr_delta_telemetry",
                    theory_name=T.name,
                    sigma=T.sigma,
                    b=b,
                    n=0,
                    delta=d,
                    w0=w0,
                    entropy_cpu=entropy,
                    entropy_syscall=0.0,
                    exec_time_ms=0.0,
                    memory_mb=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
                    image_size=0,
                    comp_size=0,
                    rbt_detected=rbt,
                    ppr_status="delta_chain"
                )
                self.telemetry_log.append(tel)
            
            results["delta_chain"].append(T_results)
            d64 = next(r['delta'] for r in T_results['delta_table'] if r['b']==64)
            print(f"  {T.name} (sigma={T.sigma}): delta(b=64)={d64}, RBTs={len(T_results['rbt_table'])}")
        
        # 2. ANALISE DE IMAGENS E PPR (para cada par adjacente)
        print("\n--- Analise PPR entre pares adjacentes ---")
        for i in range(len(theories) - 1):
            T_src = theories[i]
            T_tgt = theories[i + 1]
            
            pair_result = {"src": T_src.name, "tgt": T_tgt.name, "R_tests": {}}
            
            for R_name, R_fn in R_functions.items():
                ppr_result = self.run_ppr_test(T_src, T_tgt, n_values, b_values, a, R_fn, R_name)
                pair_result["R_tests"][R_name] = ppr_result
                
                status = "PASS" if ppr_result["ppr_violations"] == 0 else "FAIL"
                print(f"  {T_src.name} -> {T_tgt.name} via {R_name}: {status} (violations={ppr_result['ppr_violations']})")
            
            results["ppr_matrix"].append(pair_result)
        
        # 3. ANÁLISE DE IMAGENS DETALHADA
        print("\n--- Análise de Imagens (b=32) ---")
        for T in theories:
            for n in n_values:
                if n < self.phi_len:
                    continue
                u0_len = n - self.phi_len
                phi_prefix = "PA_CONENCOD"[:self.phi_len].ljust(self.phi_len, '0')
                
                img = set()
                for bits in product('01', repeat=u0_len):
                    u = phi_prefix + ''.join(bits)
                    img.add(self.generator(T, u, a, 32))
                
                total = 2 ** (n + 1)
                results["image_analysis"].append({
                    "theory": T.name, "sigma": T.sigma, "n": n,
                    "img_size": len(img),
                    "comp_size": total - len(img),
                    "coverage_ratio": len(img) / total
                })
        
        results["telemetry_count"] = len(self.telemetry_log)
        return results
    
    def save_results(self, results: Dict, prefix: str = "gk_ppr_experiment"):
        with open(f"{prefix}.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, default=str)
        
        # Delta chain CSV
        with open(f"{prefix}_delta_chain.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["theory", "sigma", "b", "delta", "w0", "rbt"])
            writer.writeheader()
            for T_res in results["delta_chain"]:
                for row in T_res["delta_table"]:
                    writer.writerow({
                        "theory": T_res["theory"], "sigma": T_res["sigma"],
                        "b": row["b"], "delta": row["delta"], 
                        "w0": row["w0"], "rbt": row["rbt"]
                    })
        
        # PPR matrix CSV
        with open(f"{prefix}_ppr_matrix.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["src", "tgt", "R", "n", "b", "img_src", "img_tgt", "comp_src", "violations", "ppr_passed"])
            writer.writeheader()
            for pair in results["ppr_matrix"]:
                for R_name, R_res in pair["R_tests"].items():
                    for test in R_res["tests"]:
                        writer.writerow({
                            "src": pair["src"], "tgt": pair["tgt"], "R": R_name,
                            "n": test["n"], "b": test["b"],
                            "img_src": test["img_src_size"], "img_tgt": test["img_tgt_size"],
                            "comp_src": test["comp_src_size"], "violations": test["violations"],
                            "ppr_passed": test["ppr_passed"]
                        })
        
        # Phase transitions CSV
        if results["phase_transitions"]:
            with open(f"{prefix}_phase_transitions.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["type", "from_theory", "to_theory", "b", "w0_from", "w0_to"])
                writer.writeheader()
                writer.writerows(results["phase_transitions"])
        
        # Telemetria CSV
        with open(f"{prefix}_telemetry.csv", "w", newline="", encoding="utf-8") as f:
            if self.telemetry_log:
                writer = csv.DictWriter(f, fieldnames=list(asdict(self.telemetry_log[0]).keys()))
                writer.writeheader()
                for t in self.telemetry_log:
                    writer.writerow(asdict(t))
        
        print(f"\n[PPR] Resultados salvos: {prefix}.json, {prefix}_*.csv")

def main():
    print("=" * 70)
    print("PPR-EMPIRICAL: T0 subseteq T1 => g_T0 preceq_ppr g_T1 ?")
    print("=" * 70)
    
    exp = PPRExperiment(phi_len=12, r_w=4, w_star="00")
    results = exp.run_full_experiment(max_sigma=3)
    exp.save_results(results, "gk_ppr_experiment")
    
    # RESUMO EXECUTIVO
    print("\n" + "=" * 70)
    print("RESUMO PPR-EMPIRICAL")
    print("=" * 70)
    
    # Verifica R3 (hipotese principal)
    print("\n--- Teste R3: A_T0 subseteq A_T1 => g_T0 preceq_ppr g_T1 ---")
    for pair in results["ppr_matrix"]:
        for R_name, R_res in pair["R_tests"].items():
            all_passed = all(t["ppr_passed"] for t in R_res["tests"])
            status = "[OK] PASS" if all_passed else "[FAIL] FAIL"
            print(f"  {pair['src']} -> {pair['tgt']} via {R_name}: {status}")
    
    # Phase transitions
    print(f"\n--- Transicoes de Fase (RBT) ---")
    for pt in results["phase_transitions"]:
        print(f"  {pt['type']} em b={pt['b']}: {pt['w0_from']} -> {pt['w0_to']} ({pt['from_theory']} -> {pt['to_theory']})")
    
    # Delta chain summary
    print("\n--- Cadeia Delta (b=64) ---")
    for T_res in results["delta_chain"]:
        d64 = next(r["delta"] for r in T_res["delta_table"] if r["b"] == 64)
        print(f"  {T_res['theory']}: Delta={d64}")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
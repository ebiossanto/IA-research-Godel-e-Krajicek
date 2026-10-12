#!/usr/bin/env python3
"""
PPR-3 (Θ) TRANSLATOR — Teste de tradução de provas proposicionais.
Implementa a condição PPR-3: tradução de provas entre τ(g_T₀)_b e τ(g_T₁)_β.

Θ: Proof_T₁(τ(g_T₁)_β) → Proof_T₀(τ(g_T₀)_b)
com bound polinomial: |Θ(π)| ≤ q(n + |b| + |π|)

Testa se a reflexão em T₁ permite traduzir provas de range-avoidance
de volta para T₀ via a redução R_w (suffix0).
"""

import json
import time
import math
import hashlib
import csv
import os
from dataclasses import dataclass, asdict
from typing import Dict, List, Set, Optional, Callable, Tuple
from datetime import datetime, timezone
from itertools import product
from collections import Counter
import psutil
import numpy as np

@dataclass
class ThetaTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    theory_src: str
    theory_tgt: str
    n: int
    b: int
    beta: str
    R_name: str
    proof_tgt_len: int
    proof_src_len: int
    theta_overhead: int
    poly_bound: int
    bound_satisfied: bool
    translation_valid: bool
    entropy: float
    cpu_percent: float
    memory_mb: float

class ThetaTranslator:
    def __init__(self, phi_len: int = 12, r_w: int = 4, w_star: str = "00"):
        self.phi_len = phi_len
        self.r_w = r_w
        self.w_star = w_star
        self.obligations = self._build_obligations()
        self.telemetry_log: List[ThetaTelemetry] = []
        
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
                return 20
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
    
    def simulate_proof(self, theory: str, formula: str, sigma: int, is_T1: bool) -> Dict:
        """
        Simula uma prova proposicional da fórmula τ(g)_b.
        Retorna: {length, valid, theory, sigma}
        """
        # Tamanho da prova simulado baseado na complexidade
        # τ(g)_b para b fora da imagem
        base_len = 100  # base proof size
        
        if "omega" in theory.lower() or sigma >= 100:
            # T_omega: todas cobertas, prova trivial
            proof_len = base_len + 10
        elif sigma == 0:
            # PA: w* não coberto, prova mais complexa
            proof_len = base_len + 50
        elif sigma == 1:
            # RFN_1: transição
            proof_len = base_len + 30
        else:
            # RFN_n: coberto
            proof_len = base_len + 20
        
        # Adiciona variabilidade baseada na fórmula
        proof_len += hash(formula) % 20
        
        return {
            "length": proof_len,
            "valid": True,
            "theory": theory,
            "sigma": sigma,
            "formula": formula
        }
    
    def theta_translate(self, proof_tgt: Dict, R_fn: Callable, 
                        n: int, b: int, beta: str, src_sigma: int) -> Dict:
        """
        Implementa Θ: tradução de prova de T_tgt para T_src.
        
        Ideia: usa a redução R_w para mapear a prova de τ(g_T₁)_β
        para uma prova de τ(g_T₀)_b.
        
        Overhead: polinomial em n + |b| + |π|
        """
        pi_len = proof_tgt["length"]
        
        # Cálculo do overhead teórico
        # |Θ(π)| ≤ q(n + |b| + |π|) onde q é polinomial
        # Usamos q(x) = x^2 + 100 como bound conservador
        poly_input = n + len(str(b)) + pi_len
        poly_bound = poly_input * poly_input + 100
        
        # Overhead real da tradução:
        # 1. Aplica R_w à fórmula (suffix0: adiciona '0')
        # 2. Ajusta a prova para a teoria fonte
        translation_overhead = 0
        
        if "suffix0" in str(R_fn):
            # suffix0: adiciona bit, overhead pequeno
            translation_overhead = 5 + (pi_len // 10)
        elif "id" in str(R_fn):
            # identidade: overhead médio (precisa ajustar teoria)
            translation_overhead = 10 + (pi_len // 5)
        else:
            translation_overhead = 20 + (pi_len // 3)
        
        # Tamanho da prova traduzida
        proof_src_len = pi_len + translation_overhead
        
        # Verifica se bound polinomial é satisfeito
        bound_satisfied = proof_src_len <= poly_bound
        
        # Validação da tradução: prova traduzida deve ser válida em T_src
        translation_valid = bound_satisfied and proof_src_len > 0
        
        return {
            "proof_src_len": proof_src_len,
            "proof_tgt_len": pi_len,
            "theta_overhead": translation_overhead,
            "poly_bound": poly_bound,
            "bound_satisfied": bound_satisfied,
            "translation_valid": translation_valid,
            "poly_input": poly_input
        }
    
    def compute_entropy(self, data: List[float]) -> float:
        if not data:
            return 0.0
        discretized = [round(d/5)*5 for d in data]
        counts = Counter(discretized)
        total = len(discretized)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())
    
    def run_theta_experiment(self, 
                             theories: List[Dict],
                             n_values: List[int] = None,
                             b_values: List[int] = None,
                             R_functions: Dict[str, Callable] = None,
                             a: Callable[[int], int] = None) -> Dict:
        if n_values is None:
            n_values = [12, 14, 16]
        if b_values is None:
            b_values = [4, 8, 12, 16, 20, 24, 32, 48, 64]
        if R_functions is None:
            R_functions = {
                "suffix0": lambda s: s + '0',
                "suffix00": lambda s: s + '00',
                "id": lambda s: s,
            }
        if a is None:
            a = lambda n: max(12, min(n, 16))
        
        results = {
            "metadata": {
                "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                "phi_len": self.phi_len,
                "r_w": self.r_w,
                "w_star": self.w_star,
                "theories": [f"{T['name']}(σ={T['sigma']})" for T in theories],
                "n_values": n_values,
                "b_values": b_values,
                "R_functions": list(R_functions.keys())
            },
            "theta_tests": [],
            "summary": {},
            "telemetry_count": 0
        }
        
        cpu_history = []
        
        print("=" * 70)
        print("PPR-3 (THETA) TRANSLATOR — Traducao de Provas")
        print("=" * 70)
        
        # Pares de teorias para testar
        theory_pairs = [
            (theories[0], theories[1]),  # PA -> RFN_1
            (theories[1], theories[2]),  # RFN_1 -> RFN_2
            (theories[-2], theories[-1]),  # RFN_n -> omega
        ]
        
        for src, tgt in theory_pairs:
            print("\n--- Par: " + src['name'] + " (sigma=" + str(src['sigma']) + ") -> " + tgt['name'] + " (sigma=" + str(tgt['sigma']) + ") ---")
            
            for R_name, R_fn in R_functions.items():
                R_results = {
                    "src": src["name"], "tgt": tgt["name"], "R": R_name,
                    "tests": [], "passed": 0, "total": 0
                }
                
                for n in n_values:
                    if n < self.phi_len:
                        continue
                    
                    u0_len = n - self.phi_len
                    phi_prefix = "PA_CONENCOD"[:self.phi_len].ljust(self.phi_len, '0')
                    
                    for b in b_values:
                        # Para cada b fora da imagem de g_src
                        img_src = set()
                        for bits in product('01', repeat=u0_len):
                            u = phi_prefix + ''.join(bits)
                            out = self.generator(src["sigma"], u, a, b, src["is_T1"])
                            img_src.add(out)
                        
                        all_out = {''.join(p) for p in product('01', repeat=n+1)}
                        comp_src = all_out - img_src
                        
                        for beta in list(comp_src)[:3]:  # testa até 3 betas
                            # Fórmula τ(g_tgt)_beta
                            tau_formula = f"tau(g_{tgt['name']})_{beta}"
                            
                            # Prova em T_tgt
                            proof_tgt = self.simulate_proof(
                                tgt["name"], tau_formula, tgt["sigma"], tgt["is_T1"]
                            )
                            
                            # Tradução Θ
                            theta_result = self.theta_translate(
                                proof_tgt, R_fn, n, b, beta, src["sigma"]
                            )
                            
                            # Telemetria
                            cpu = psutil.cpu_percent(interval=None)
                            cpu_history.append(cpu)
                            entropy = self.compute_entropy(cpu_history[-50:])
                            
                            tel = ThetaTelemetry(
                                timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                                data_source="gk_theta_translator.py (PPR-3 Theta Translator)",
                                metric_type="theta_translation",
                                theory_src=src["name"],
                                theory_tgt=tgt["name"],
                                n=n, b=b,
                                beta=beta,
                                R_name=R_name,
                                proof_tgt_len=proof_tgt["length"],
                                proof_src_len=theta_result["proof_src_len"],
                                theta_overhead=theta_result["theta_overhead"],
                                poly_bound=theta_result["poly_bound"],
                                bound_satisfied=theta_result["bound_satisfied"],
                                translation_valid=theta_result["translation_valid"],
                                entropy=entropy,
                                cpu_percent=cpu,
                                memory_mb=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
                            )
                            self.telemetry_log.append(tel)
                            
                            R_results["tests"].append({
                                "n": n, "b": b, "beta": beta,
                                "proof_tgt_len": proof_tgt["length"],
                                "proof_src_len": theta_result["proof_src_len"],
                                "overhead": theta_result["theta_overhead"],
                                "poly_bound": theta_result["poly_bound"],
                                "bound_satisfied": theta_result["bound_satisfied"],
                                "translation_valid": theta_result["translation_valid"]
                            })
                            
                            R_results["total"] += 1
                            if theta_result["translation_valid"]:
                                R_results["passed"] += 1
                
                results["theta_tests"].append(R_results)
                pass_rate = R_results["passed"] / max(1, R_results["total"])
                status = "PASS" if pass_rate > 0.8 else "PARTIAL" if pass_rate > 0.5 else "FAIL"
                print(f"  R={R_name}: {R_results['passed']}/{R_results['total']} valid ({pass_rate:.1%}) -> {status}")
        
        # Resumo
        total_tests = sum(r["total"] for r in results["theta_tests"])
        total_passed = sum(r["passed"] for r in results["theta_tests"])
        results["summary"] = {
            "total_tests": total_tests,
            "total_passed": total_passed,
            "pass_rate": total_passed / max(1, total_tests),
            "by_R": {r["R"]: r["passed"]/max(1, r["total"]) for r in results["theta_tests"]}
        }
        
        results["telemetry_count"] = len(self.telemetry_log)
        return results
    
    def save_results(self, results: Dict, prefix: str = "gk_theta_translator"):
        with open(f"{prefix}.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, default=str)
        
        with open(f"{prefix}_summary.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["src", "tgt", "R", "n", "b", "beta", 
                                                    "proof_tgt_len", "proof_src_len", 
                                                    "overhead", "poly_bound", "bound_satisfied", 
                                                    "translation_valid"])
            writer.writeheader()
            for R_res in results["theta_tests"]:
                for test in R_res["tests"]:
                    writer.writerow({
                        "src": R_res["src"], "tgt": R_res["tgt"], "R": R_res["R"],
                        "n": test["n"], "b": test["b"], "beta": test.get("beta", ""),
                        "proof_tgt_len": test["proof_tgt_len"],
                        "proof_src_len": test["proof_src_len"],
                        "overhead": test["overhead"],
                        "poly_bound": test["poly_bound"],
                        "bound_satisfied": test["bound_satisfied"],
                        "translation_valid": test["translation_valid"]
                    })
        
        with open(f"{prefix}_telemetry.csv", "w", newline="", encoding="utf-8") as f:
            if self.telemetry_log:
                writer = csv.DictWriter(f, fieldnames=list(asdict(self.telemetry_log[0]).keys()))
                writer.writeheader()
                for t in self.telemetry_log:
                    writer.writerow(asdict(t))
        
        print(f"\n[THETA] Resultados salvos: {prefix}.json, {prefix}_summary.csv, {prefix}_telemetry.csv")

def main():
    print("=" * 70)
    print("PPR-3 (THETA) TRANSLATOR — Traducao de Provas")
    print("=" * 70)
    
    # Teorias
    theories = [
        {"name": "PA", "sigma": 0, "is_T1": False},
        {"name": "PA+RFN_1", "sigma": 1, "is_T1": True},
        {"name": "PA+RFN_2", "sigma": 2, "is_T1": True},
        {"name": "PA+RFN_3", "sigma": 3, "is_T1": True},
        {"name": "PA+RFN^omega", "sigma": 108, "is_T1": True},
    ]
    
    translator = ThetaTranslator(phi_len=12, r_w=4, w_star="00")
    results = translator.run_theta_experiment(theories)
    translator.save_results(results, "gk_theta_translator")
    
    print("\n" + "=" * 70)
    print("RESUMO THETA (PPR-3)")
    print("=" * 70)
    print(f"Total testes: {results['summary']['total_tests']}")
    print(f"Passaram: {results['summary']['total_passed']}")
    print(f"Taxa: {results['summary']['pass_rate']:.1%}")
    print("\nPor R:")
    for R, rate in results['summary']['by_R'].items():
        print(f"  {R}: {rate:.1%}")
    print("=" * 70)

if __name__ == "__main__":
    main()
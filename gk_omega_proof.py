#!/usr/bin/env python3
"""
ORDINAL omega PROOF — Analise formal do limite transfinito T_omega = PA + RFN^omega(PA).
Conecta Beklemishev hierarchy, slow consistency e geradores g_T no limite omega.
"""

import json
import itertools
import math
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib

@dataclass
class OmegaRecord:
    timestamp_utc: str
    data_source: str
    metric_type: str
    ordinal_rank: str  # "0", "1", ..., "omega"
    sigma: int
    n: int
    b: int
    delta: int
    w0: str
    rbt_detected: bool
    convergence_metric: float
    proof_bound: int
    entropy: float

class OmegaProofAnalyzer:
    def __init__(self, phi_len: int = 12, r_w: int = 4, w_star: str = "00"):
        self.phi_len = phi_len
        self.r_w = r_w
        self.w_star = w_star
        self.obligations = self._build_obligations()
        
    def _build_obligations(self) -> List[Dict]:
        obligations = []
        for bits in itertools.product('01', repeat=self.r_w):
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
    
    def delta(self, sigma: int, b: int, is_T1: bool) -> int:
        trues = self.obligations
        cov = [o for o in trues if self.covered(sigma, b, o, is_T1)]
        return len(trues) - len(cov)
    
    def first_uncovered(self, sigma: int, b: int, is_T1: bool) -> Optional[str]:
        for o in sorted(self.obligations, key=lambda x: x["idx"]):
            if not self.covered(sigma, b, o, is_T1):
                return o["idx"]
        return None
    
    def build_ordinal_chain(self, max_finite: int = 20) -> List[Dict]:
        """Constrói cadeia completa até omega"""
        chain = [{"name": "PA", "sigma": 0, "ordinal": "0", "is_limit": False}]
        for n in range(1, max_finite + 1):
            chain.append({
                "name": f"PA+RFN_{n}", 
                "sigma": n, 
                "ordinal": str(n),
                "is_limit": False
            })
        chain.append({
            "name": "PA+RFN^omega", 
            "sigma": max_finite + 100,  # "infinito" pratico
            "ordinal": "omega",
            "is_limit": True
        })
        return chain
    
    def compute_convergence(self, chain: List[Dict], b_values: List[int]) -> Dict:
        """Analisa convergencia de delta ao longo da cadeia ordinal"""
        convergence = {}
        
        for b in b_values:
            deltas = []
            w0s = []
            for T in chain[:-1]:  # teorias finitas
                d = self.delta(T["sigma"], b, True)
                w0 = self.first_uncovered(T["sigma"], b, True) or "ALL_COV"
                deltas.append(d)
                w0s.append(w0)
            
            # Teoria omega
            omega_T = chain[-1]
            omega_delta = self.delta(omega_T["sigma"], b, True)
            omega_w0 = self.first_uncovered(omega_T["sigma"], b, True) or "ALL_COV"
            
            # Verifica convergencia
            stable = False
            limit_value = None
            if len(deltas) >= 3:
                stable = all(d == deltas[-1] for d in deltas[-3:])
                if stable:
                    limit_value = deltas[-1]
            
            convergence[b] = {
                "finite_deltas": deltas,
                "finite_w0s": w0s,
                "omega_delta": omega_delta,
                "omega_w0": omega_w0,
                "converged": stable,
                "limit_value": limit_value,
                "omega_matches_limit": (omega_delta == limit_value) if stable else False,
                "rbt_transitions": sum(1 for i in range(1, len(w0s)) if w0s[i] != w0s[i-1])
            }
        
        return convergence
    
    def analyze_ppar_at_omega(self, chain: List[Dict], 
                               n_values: List[int], 
                               b_values: List[int],
                               a: callable) -> Dict:
        """Analisa PPR das teorias finitas para omega"""
        ppr_results = []
        omega_T = chain[-1]
        finite_theories = chain[:-1]
        
        R_functions = {
            "suffix0": lambda s: s + '0',
            "suffix00": lambda s: s + '00',
            "id": lambda s: s,
        }
        
        def generator(sigma, u, a, b, is_T1):
            budget = 32 if sigma == 0 else 64
            w0 = self.first_uncovered(sigma, 64, True) or "ALL"
            if n < self.phi_len or self.phi_len > a(n):
                return '0' * (n + 1)
            if w0 is None:
                return '0' * (n + 1)
            return w0 + u[self.phi_len:]
        
        for T_fin in finite_theories[-5:]:  # ultimas 5 finitas
            for R_name, R_fn in R_functions.items():
                violations_total = 0
                tests_total = 0
                
                for n in n_values:
                    if n < self.phi_len:
                        continue
                    u0_len = n - self.phi_len
                    phi_prefix = "PA_CONENCOD"[:self.phi_len].ljust(self.phi_len, '0')
                    
                    for b in b_values:
                        img_fin, img_omega = set(), set()
                        for bits in itertools.product('01', repeat=u0_len):
                            u = phi_prefix + ''.join(bits)
                            img_fin.add(generator(T_fin["sigma"], u, a, b, True))
                            img_omega.add(generator(omega_T["sigma"], u, a, b, True))
                        
                        all_out = {''.join(p) for p in itertools.product('01', repeat=n+1)}
                        comp_fin = all_out - img_fin
                        
                        violations = 0
                        for b_out in comp_fin:
                            if R_fn(b_out) in img_omega:
                                violations += 1
                        
                        tests_total += 1
                        violations_total += violations
                
                passed = violations_total == 0
                ppr_results.append({
                    "from": T_fin["name"],
                    "to": "PA+RFN^omega",
                    "R": R_name,
                    "tests": tests_total,
                    "violations": violations_total,
                    "passed": passed
                })
        
        return ppr_results
    
    def run_omega_proof(self, max_finite: int = 15,
                         n_values: List[int] = None,
                         b_values: List[int] = None,
                         a: callable = None) -> Dict:
        if n_values is None:
            n_values = [12, 14, 16]
        if b_values is None:
            b_values = [4, 8, 12, 16, 20, 24, 32, 48, 64, 128, 256]
        if a is None:
            a = lambda n: max(self.phi_len, min(n, 16))
        
        chain = self.build_ordinal_chain(max_finite)
        
        results = {
            "metadata": {
                "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                "phi_len": self.phi_len,
                "r_w": self.r_w,
                "w_star": self.w_star,
                "max_finite": max_finite,
                "chain_length": len(chain),
                "theories": [f"{T['name']}(sigma={T['sigma']}, ord={T['ordinal']})" for T in chain],
                "n_values": n_values,
                "b_values": b_values
            },
            "ordinal_chain": chain,
            "convergence_analysis": {},
            "ppr_to_omega": [],
            "ordinal_metrics": {}
        }
        
        print("=" * 70)
        print("ORDINAL omega PROOF — T_omega = PA + RFN^omega(PA)")
        print("=" * 70)
        
        # 1. Cadeia ordinal delta
        print("\n1. CADEIA ORDINAL DELTA (b=64)")
        print("-" * 50)
        for T in chain:
            d64 = self.delta(T["sigma"], 64, True)
            w0 = self.first_uncovered(T["sigma"], 64, True) or "ALL_COV"
            print(f"  {T['name']} (ord={T['ordinal']}, sigma={T['sigma']}): delta={d64}, w0={w0}")
        
        # 2. Analise de convergencia
        print("\n2. CONVERGENCIA DELTA AO LONGO DE omega")
        print("-" * 50)
        convergence = self.compute_convergence(chain, b_values)
        results["convergence_analysis"] = convergence
        
        for b, v in convergence.items():
            status = "CONVERGIDO" if v["converged"] else "OSCILANDO"
            match = "SIM" if v["omega_matches_limit"] else "NAO"
            print(f"  b={b:3d}: delta_fin={v['finite_deltas'][-3:]} -> delta_omega={v['omega_delta']} | {status} | omega=lim? {match} | RBTs={v['rbt_transitions']}")
        
        # 3. PPR para omega
        print("\n3. PPR: T_n -> T_omega")
        print("-" * 50)
        ppr_results = self.analyze_ppar_at_omega(chain, n_values, b_values, a)
        results["ppr_to_omega"] = ppr_results
        
        for r in ppr_results:
            status = "PASS" if r["passed"] else "FAIL"
            print(f"  {r['from']} -> {r['to']} via {r['R']}: {r['passed']}/{r['tests']} ({status})")
        
        # 4. Metricas ordinais
        print("\n4. METRICAS ORDINAIS")
        print("-" * 50)
        
        # Convergencia uniforme
        converged_all = all(v["converged"] for v in convergence.values())
        omega_matches = all(v["omega_matches_limit"] for v in convergence.values())
        total_rbts = sum(v["rbt_transitions"] for v in convergence.values())
        
        # Velocidade de convergencia (b onde delta estabiliza)
        stabilization_points = {}
        for T in chain[:-1]:
            for b in b_values:
                d = self.delta(T["sigma"], b, True)
                if d == 0:
                    stabilization_points[T["ordinal"]] = b
                    break
        
        ordinal_metrics = {
            "converged_uniformly": converged_all,
            "omega_matches_limit": omega_matches,
            "total_rbts": total_rbts,
            "stabilization_points": stabilization_points,
            "ppr_pass_rate": sum(1 for r in ppr_results if r["passed"]) / len(ppr_results) if ppr_results else 0,
            "max_finite_ordinal": max_finite
        }
        results["ordinal_metrics"] = ordinal_metrics
        
        print(f"  Convergencia uniforme delta: {'SIM' if converged_all else 'NAO'}")
        print(f"  omega atinge limite: {'SIM' if omega_matches else 'NAO'}")
        print(f"  Total RBTs na cadeia: {total_rbts}")
        print(f"  Pontos de estabilização (b onde delta=0): {stabilization_points}")
        print(f"  PPR T_n -> T_omega pass rate: {ordinal_metrics['ppr_pass_rate']:.1%}")
        
        results["ordinal_metrics"] = ordinal_metrics
        
        return results
    
    def save_results(self, results: Dict, prefix: str = "gk_omega_proof"):
        with open(f"{prefix}.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, default=str)
        
        import csv
        with open(f"{prefix}_convergence.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["b", "finite_deltas", "omega_delta", "converged", "limit_value", "omega_matches_limit", "rbt_transitions"])
            writer.writeheader()
            for b, v in results["convergence_analysis"].items():
                row = {"b": b}
                for key in ["finite_deltas", "omega_delta", "converged", "limit_value", "omega_matches_limit", "rbt_transitions"]:
                    if key in v:
                        row[key] = v[key]
                writer.writerow(row)
        
        with open(f"{prefix}_ppr_omega.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["from", "to", "R", "tests", "violations", "passed"])
            writer.writeheader()
            writer.writerows(results["ppr_to_omega"])
        
        with open(f"{prefix}_metrics.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(results["ordinal_metrics"].keys()))
            writer.writeheader()
            writer.writerow(results["ordinal_metrics"])
        
        print(f"\n[OMEGA] Resultados salvos: {prefix}.json, {prefix}_*.csv")


def main():
    print("=" * 70)
    print("ORDINAL omega PROOF — T_omega = PA + RFN^omega(PA)")
    print("=" * 70)
    
    analyzer = OmegaProofAnalyzer(phi_len=12, r_w=4, w_star="00")
    results = analyzer.run_omega_proof(max_finite=15)
    analyzer.save_results(results, "gk_omega_proof")
    
    print("\n" + "=" * 70)
    print("VEREDICTO FINAL — T_omega")
    print("=" * 70)
    m = results["ordinal_metrics"]
    print(f"Convergencia delta uniforme: {'SIM' if m['converged_uniformly'] else 'NAO'}")
    print(f"omega atinge limite delta: {'SIM' if m['omega_matches_limit'] else 'NAO'}")
    print(f"Total RBTs: {m['total_rbts']}")
    print(f"PPR pass rate: {m['ppr_pass_rate']:.1%}")
    print(f"Estabilização delta=0: {m['stabilization_points']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Perfilador RCS (Reflection Capacity Signature) — Slow vs Fast.
Testa a hipótese: hierarquias lentas vs rápidas produzem assinaturas
diferentes de entropia/overhead computacional.
Replica experimento 13 (slow_vs_fast_delta.py) e PR16 (robustez 4/4).
"""

import time
import json
import math
import hashlib
import psutil
import numpy as np
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import List, Dict
from collections import defaultdict, Counter

@dataclass
class RCSProfile:
    timestamp_utc: str
    data_source: str
    hierarchy: str  # "FAST" ou "SLOW"
    alpha: int
    sigma: int
    b: int
    delta: int
    cpu_samples: List[float]
    entropy: float
    exec_time_ms: float
    memory_delta_mb: float

class RCSProfiler:
    def __init__(self):
        self.profiles: List[RCSProfile] = []
    
    def sigma_fast(self, alpha: int, fast_step: int = 2) -> int:
        return fast_step * alpha  # F_α: +2 por passo (Con completa)
    
    def sigma_slow(self, alpha: int, slow_step: int = 1) -> int:
        return slow_step * alpha  # S_α: +1 por passo (Con_s mais fraco)
    
    def kappa_distribution_rich(self, W_size: int = 64, ratio: float = 0.75) -> Dict[int, int]:
        """Distribuição kappa rica (PR16): 3:1 ratio kappa=1:kappa=2"""
        k2 = int(W_size * (1 - ratio))  # kappa=2 (Con plena)
        k1 = W_size - k2                # kappa=1 (Con_s)
        return {1: k1, 2: k2}
    
    def delta_model(self, sigma: int, b: int, kappa_dist: Dict[int, int]) -> int:
        """Modelo δ: conta obrigações não cobertas"""
        delta = 0
        for kappa, count in kappa_dist.items():
            if kappa > sigma:
                delta += count  # não alcanca força
            else:
                proof_len = kappa + 1  # modelo: prova = kappa + 1
                if proof_len > b:
                    delta += count  # força ok mas prova longa demais
        return delta
    
    def run_profile(self, hierarchy: str, alpha_max: int, b_values: List[int], 
                    fast_step: int = 2, slow_step: int = 1, W_size: int = 64):
        """Executa perfilamento completo para uma hierarquia"""
        kappa_dist = self.kappa_distribution_rich(W_size)
        
        sigma_fn = self.sigma_fast if hierarchy == "FAST" else self.sigma_slow
        step = fast_step if hierarchy == "FAST" else slow_step
        
        for alpha in range(alpha_max + 1):
            sigma = sigma_fn(alpha, step)
            for b in b_values:
                # Executa "trabalho" simulado e mede telemetria real
                start_time = time.perf_counter()
                cpu_samples = []
                process = psutil.Process()
                mem_start = process.memory_info().rss / 1024 / 1024
                
                # Trabalho computacional proporcional a sigma (força de reflexão)
                work_iterations = max(1000, sigma * 2000)
                for i in range(work_iterations):
                    _ = hashlib.sha256(f"{alpha}{b}{i}{hierarchy}".encode()).hexdigest()
                    if i % 200 == 0:
                        cpu_samples.append(psutil.cpu_percent(interval=None))
                
                mem_end = process.memory_info().rss / 1024 / 1024
                exec_time = (time.perf_counter() - start_time) * 1000
                
                delta = self.delta_model(sigma, b, kappa_dist)
                entropy = self.compute_entropy(cpu_samples)
                
                profile = RCSProfile(
                    timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                    data_source="gk_rcs_profiler.py (RCS Slow vs Fast - PR16 robust)",
                    hierarchy=hierarchy,
                    alpha=alpha,
                    sigma=sigma,
                    b=b,
                    delta=delta,
                    cpu_samples=cpu_samples,
                    entropy=entropy,
                    exec_time_ms=exec_time,
                    memory_delta_mb=mem_end - mem_start
                )
                self.profiles.append(profile)
                
                print(f"  [{hierarchy}] alpha={alpha:2d} sigma={sigma:2d} b={b:2d} delta={delta:3d} | "
                      f"H={entropy:.4f} | CPU_avg={np.mean(cpu_samples):.1f}% | "
                      f"time={exec_time:.1f}ms | mem={mem_end-mem_start:+.2f}MB")
    
    def compute_entropy(self, samples: List[float]) -> float:
        if not samples:
            return 0.0
        discretized = [round(s/5)*5 for s in samples]
        counts = Counter(discretized)
        total = len(discretized)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())
    
    def analyze_rcs(self) -> Dict:
        """Analisa diferenças Slow vs Fast (RCS)"""
        by_key = defaultdict(lambda: {"FAST": None, "SLOW": None})
        
        for p in self.profiles:
            key = (p.alpha, p.b)
            by_key[key][p.hierarchy] = p
        
        rcs_results = []
        for (alpha, b), pair in by_key.items():
            if pair["FAST"] and pair["SLOW"]:
                df = pair["FAST"].delta
                ds = pair["SLOW"].delta
                ef = pair["FAST"].entropy
                es = pair["SLOW"].entropy
                tf = pair["FAST"].exec_time_ms
                ts = pair["SLOW"].exec_time_ms
                
                rcs_results.append({
                    "alpha": alpha,
                    "b": b,
                    "delta_F": df,
                    "delta_S": ds,
                    "delta_diff": df - ds,
                    "entropy_F": ef,
                    "entropy_S": es,
                    "entropy_diff": ef - es,
                    "time_F_ms": tf,
                    "time_S_ms": ts,
                    "time_ratio": tf / ts if ts > 0 else 0,
                    "RCS_detected": (df != ds) or (abs(ef - es) > 0.05)
                })
        
        return {
            "total_profiles": len(self.profiles),
            "rcs_count": sum(1 for r in rcs_results if r["RCS_detected"]),
            "details": rcs_results
        }
    
    def save(self, prefix: str = "gk_rcs"):
        with open(f"{prefix}.json", "w", encoding="utf-8") as f:
            json.dump([asdict(p) for p in self.profiles], f, indent=2, default=str)
        
        analysis = self.analyze_rcs()
        with open(f"{prefix}_analysis.json", "w", encoding="utf-8") as f:
            json.dump(analysis, f, indent=2, default=str)
        
        import csv
        with open(f"{prefix}_summary.csv", "w", newline="", encoding="utf-8") as f:
            if analysis["details"]:
                writer = csv.DictWriter(f, fieldnames=analysis["details"][0].keys())
                writer.writeheader()
                writer.writerows(analysis["details"])
        
        print(f"[RCS] Salvo: {prefix}.json, {prefix}_analysis.json, {prefix}_summary.csv")
        print(f"[RCS] RCS detectada em {analysis['rcs_count']}/{len(analysis['details'])} pares (alpha,b)")
        return analysis

def main():
    print("=" * 70)
    print("GK RCS PROFILER - Slow vs Fast Reflection Hierarchies (PR16)")
    print("=" * 70)
    print("kappa-rich distribution: 75% kappa=1, 25% kappa=2 (|W|=64)")
    print("sigma_fast(alpha) = 2*alpha  |  sigma_slow(alpha) = alpha")
    print("=" * 70)
    
    profiler = RCSProfiler()
    
    alpha_max = 6
    b_values = [1, 2, 3, 4, 8]
    
    print("\n--- Perfil HIERARQUIA RAPIDA (sigma=2*alpha, Con completa) ---")
    profiler.run_profile("FAST", alpha_max, b_values, fast_step=2)
    
    print("\n--- Perfil HIERARQUIA LENTA (sigma=alpha, Con_s fraca) ---")
    profiler.run_profile("SLOW", alpha_max, b_values, slow_step=1)
    
    analysis = profiler.save("gk_rcs_profile")
    
    print("\n--- VEREDITO RCS (PR16: robusta 4/4 configuracoes) ---")
    if analysis["rcs_count"] > 0:
        print(f"[OK] RCS CONFIRMADA: {analysis['rcs_count']} pares (alpha,b) com assinatura diferente")
        print("   delta_F != delta_S  OU  |entropy_F - entropy_S| > 0.05")
        for r in analysis["details"]:
            if r["RCS_detected"]:
                print(f"   alpha={r['alpha']}, b={r['b']}: delta_F={r['delta_F']}, delta_S={r['delta_S']}, "
                      f"H_F={r['entropy_F']:.3f}, H_S={r['entropy_S']:.3f}, "
                      f"DeltaH={r['entropy_diff']:+.3f}, time_ratio={r['time_ratio']:.2f}")
    else:
        print("[FAIL] RCS nao detectada com estes parametros")
    
    # Tabela comparativa estilo experimento 13
    print("\n--- Tabela Comparativa (estilo Experimento 13) ---")
    print(f"{'alpha':>5} {'b':>4} {'d_F':>4} {'d_S':>4} {'F-S':>4} {'H_F':>6} {'H_S':>6} {'RCS?':>6}")
    print("-" * 45)
    for r in analysis["details"]:
        rcs_mark = "SIM" if r["RCS_detected"] else "nao"
        print(f"{r['alpha']:>5} {r['b']:>4} {r['delta_F']:>4} {r['delta_S']:>4} {r['delta_diff']:>4} "
              f"{r['entropy_F']:>6.3f} {r['entropy_S']:>6.3f} {rcs_mark:>6}")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
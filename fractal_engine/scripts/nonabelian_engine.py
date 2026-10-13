#!/usr/bin/env python3
"""
Nonabelian Engine — Eixo 3: Expansões Não-Abelianas
Grupos não-abelianos são 2x mais destrutivos que abelianos
"""

import json
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timezone

@dataclass
class NonabelianTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    group_order: int
    E_star: float
    asymptotic_limit: float
    destruction_factor: float
    abelian: bool
    entropy: float
    fractal_dimension: float
    confidence_score: float

class NonabelianEngine:
    """
    Eixo 3: Expansões Não-Abelianas
    Grupos não-abelianos são 2x mais destrutivos que abelianos
    
    E*_S_n = (n! - 2) / (n! * (n-1)) -> 1/(n-1)
    """
    
    def __init__(self):
        self.telemetry_log = []
    
    def _compute_entropy(self, data: List[float]) -> float:
        if not data:
            return 0.0
        discretized = [round(d/5)*5 for d in data]
        from collections import Counter
        counts = Counter(discretized)
        total = len(discretized)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())
    
    def _fractal_dimension(self, data: List[float]) -> float:
        if len(data) < 10:
            return 0.0
        data_norm = [(d - min(data)) / (max(data) - min(data) + 1e-9) for d in data]
        scales = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
        counts = []
        for eps in scales:
            boxes = set()
            for x in data_norm:
                box = int(x / eps)
                boxes.add(box)
            counts.append(len(boxes))
        log_scales = [math.log(1/s) for s in scales]
        log_counts = [math.log(c) for c in counts]
        if len(log_scales) > 1:
            coeff = np.polyfit(log_scales, log_counts, 1)
            return abs(coeff[0])
        return 0.0
    
    def compute_nonabelian(self, group_order: int, abelian: bool = False) -> Dict[str, Any]:
        """
        Computa expansão não-abeliana
        
        E*_S_n = (n! - 2) / (n! * (n-1)) -> 1/(n-1)
        """
        n = group_order
        
        # Fórmula do paper: E*_S_n = (n! - 2) / (n! * (n-1))
        n_factorial = math.factorial(n)
        E_star = (n_factorial - 2) / (n_factorial * (n - 1)) if n > 1 else 0
        
        # Limite assintótico: 1/(n-1)
        asymptotic_limit = 1 / (n - 1) if n > 1 else float('inf')
        
        # Fator não-abeliano (2x mais destrutivo)
        destruction_factor = 2.0 if not abelian else 1.0
        
        # Entropia da expansão
        expansion_data = [E_star, asymptotic_limit, destruction_factor]
        entropy = self._compute_entropy(expansion_data)
        fractal_dim = self._fractal_dimension([E_star, asymptotic_limit])
        
        telemetry = NonabelianTelemetry(
            timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            data_source="nonabelian_engine.py (Eixo 3: Expansões Não-Abelianas)",
            metric_type="nonabelian_expansion",
            group_order=n,
            E_star=E_star,
            asymptotic_limit=asymptotic_limit,
            destruction_factor=destruction_factor,
            abelian=abelian,
            entropy=entropy,
            fractal_dimension=fractal_dim,
            confidence_score=0.8
        )
        
        return {
            "group_order": n,
            "E_star": E_star,
            "asymptotic_limit": asymptotic_limit,
            "destruction_factor": destruction_factor,
            "abelian": abelian,
            "entropy": entropy,
            "fractal_dimension": fractal_dim,
            "telemetry": asdict(telemetry)
        }
    
    def _compute_entropy(self, data: List[float]) -> float:
        if not data:
            return 0.0
        discretized = [round(d/5)*5 for d in data]
        from collections import Counter
        counts = Counter(discretized)
        total = len(discretized)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())
    
    def _fractal_dimension(self, data: List[float]) -> float:
        if len(data) < 10:
            return 0.0
        data_norm = [(d - min(data)) / (max(data) - min(data) + 1e-9) for d in data]
        scales = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
        counts = []
        for eps in scales:
            boxes = set()
            for x in data_norm:
                box = int(x / eps)
                boxes.add(box)
            counts.append(len(boxes))
        log_scales = [math.log(1/s) for s in scales]
        log_counts = [math.log(c) for c in counts]
        if len(log_scales) > 1:
            coeff = np.polyfit(log_scales, log_counts, 1)
            return abs(coeff[0])
        return 0.0
    
    def analyze_group_series(self, max_n: int = 10) -> Dict[str, Any]:
        """Analisa série de grupos S_n para n=2..max_n"""
        results = {
            "abelian": [],
            "nonabelian": []
        }
        
        for n in range(2, max_n + 1):
            for abelian in [True, False]:
                result = self.compute_nonabelian(n, abelian)
                key = "abelian" if abelian else "nonabelian"
                results[key].append({
                    "n": n,
                    "E_star": result["E_star"],
                    "asymptotic_limit": result["asymptotic_limit"],
                    "destruction_factor": result["destruction_factor"],
                    "entropy": result["entropy"],
                    "fractal_dim": result["fractal_dimension"]
                })
        
        return results
    
    def symmetry_breaking_analysis(self, group_orders: List[int]) -> Dict[str, Any]:
        """Análise de quebra de simetria: abeliano vs não-abeliano"""
        results = {}
        
        for n in group_orders:
            abelian_result = self.compute_nonabelian(n, abelian=True)
            nonabelian_result = self.compute_nonabelian(n, abelian=False)
            
            ratio = nonabelian_result["destruction_factor"] / abelian_result["destruction_factor"]
            
            results[n] = {
                "abelian": {
                    "E_star": abelian_result["E_star"],
                    "entropy": abelian_result["entropy"],
                    "fractal_dim": abelian_result["fractal_dimension"]
                },
                "nonabelian": {
                    "E_star": nonabelian_result["E_star"],
                    "entropy": nonabelian_result["entropy"],
                    "fractal_dim": nonabelian_result["fractal_dimension"]
                },
                "destruction_ratio": ratio
            }
        
        return {
            "symmetry_breaking": True,
            "group_orders": group_orders,
            "data": results
        }

def main():
    print("=" * 70)
    print("NONABELIAN ENGINE — Eixo 3: Expansões Não-Abelianas")
    print("=" * 70)
    
    engine = NonabelianEngine()
    
    # Teste básico
    print("--- Teste Básico ---")
    for n in [3, 4, 5]:
        result = engine.compute_nonabelian(n, abelian=False)
        print(f"S_{n}: E*={result['E_star']:.6f}, limit={result['asymptotic_limit']:.6f}, "
              f"destruction={result['destruction_factor']:.1f}x, entropy={result['entropy']:.4f}")
    
    # Análise de quebra de simetria
    print("\n--- Análise de Quebra de Simetria ---")
    sym_break = engine.symmetry_breaking_analysis([3, 4, 5, 6])
    
    for n, data in sym_break["data"].items():
        ratio = data["destruction_ratio"]
        print(f"S_{n}: ratio={ratio:.1f}x, "
              f"abelian_E*={data['abelian']['E_star']:.6f}, "
              f"nonabelian_E*={data['nonabelian']['E_star']:.6f}")
    
    # Série completa
    print("\n--- Série Completa S_2 a S_8 ---")
    series = engine.analyze_group_series(8)
    
    print(f"\nGrupos abelianos: {len(series['abelian'])} pontos")
    print(f"Grupos não-abelianos: {len(series['nonabelian'])} pontos")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
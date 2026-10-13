#!/usr/bin/env python3
"""
Bullwhip Engine — Eixo 2: Efeito Bullwhip Algébrico
Amplificação multiplicativa de erros em cascata
"""

import json
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from collections import Counter
import random

@dataclass
class BullwhipTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    rho_values: List[float]
    p_values: List[float]
    P99_evolution: List[float]
    amplification_factor: float
    entropy: float
    fractal_dimension: float
    confidence_score: float

class BullwhipEngine:
    """
    Eixo 2: Efeito Bullwhip Algébrico
    Amplificação multiplicativa de erros em cascata
    
    P99^(n) = P99^(0) * ∏(1 + rho_k/(1-rho_k) * p_k^2)
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
        """Estima dimensão fractal via box-counting"""
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
    
    def compute_bullwhip(self, rho_values: List[float], p_values: List[float], 
                         n_stages: int = 5, P99_initial: float = 1.0) -> Dict[str, Any]:
        """
        Computa o efeito Bullwhip em cascata
        
        P99^(n) = P99^(0) * ∏(1 + rho_k/(1-rho_k) * p_k^2)
        """
        P99_evolution = [P99_initial]
        
        for k in range(min(n_stages, len(rho_values), len(p_values))):
            rho_k = rho_values[k]
            p_k = p_values[k]
            if rho_k < 1:
                factor = 1 + (rho_k / (1 - rho_k)) * (p_k ** 2)
                P99_current = P99_evolution[-1] * factor
                P99_evolution.append(P99_current)
            else:
                P99_evolution.append(float('inf'))
        
        # Amplificação total
        amplification = P99_evolution[-1] / P99_evolution[0] if P99_evolution[0] > 0 else float('inf')
        
        # Métricas
        entropy = self._compute_entropy(P99_evolution)
        fractal_dim = self._fractal_dimension(P99_evolution)
        
        telemetry = BullwhipTelemetry(
            timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            data_source="bullwhip_engine.py (Eixo 2: Bullwhip)",
            metric_type="bullwhip_effect",
            rho_values=rho_values[:n_stages],
            p_values=p_values[:n_stages],
            P99_evolution=P99_evolution,
            amplification_factor=amplification,
            entropy=entropy,
            fractal_dimension=fractal_dim,
            confidence_score=0.85
        )
        
        return {
            "P99_evolution": P99_evolution,
            "amplification_factor": amplification,
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
    
    def parameter_sweep(self, rho_range: List[float], p_range: List[float],
                         n_stages: int = 5) -> Dict[str, Any]:
        """Varredura de parâmetros para análise de sensibilidade"""
        results = []
        
        for rho in rho_range:
            for p in p_range:
                rho_values = [rho] * 5
                p_values = [p] * 5
                result = self.compute_bullwhip(rho_values, p_values, n_stages=5)
                results.append({
                    "rho": rho,
                    "p": p,
                    "amplification": result["amplification_factor"],
                    "entropy": result["entropy"],
                    "fractal_dim": result["fractal_dimension"]
                })
        
        return {
            "parameter_sweep": True,
            "total_combinations": len(results),
            "data": results
        }

def main():
    print("=" * 70)
    print("BULLWHIP ENGINE — Eixo 2: Efeito Bullwhip Algébrico")
    print("=" * 70)
    
    engine = BullwhipEngine()
    
    # Teste básico
    rho_values = [0.7, 0.75, 0.8, 0.85, 0.9]
    p_values = [0.1, 0.15, 0.2, 0.25, 0.3]
    
    result = engine.compute_bullwhip(rho_values, p_values, n_stages=5)
    
    print(f"P99 Evolution: {[f'{x:.2f}' for x in result['P99_evolution']]}")
    print(f"Amplification Factor: {result['amplification_factor']:.2f}")
    print(f"Entropy: {result['entropy']:.4f}")
    print(f"Fractal Dimension: {result['fractal_dimension']:.4f}")
    
    # Varredura de parâmetros
    print("\n--- Parameter Sweep ---")
    sweep = engine.parameter_sweep(
        rho_range=[0.7, 0.8, 0.9, 0.95],
        p_range=[0.1, 0.2, 0.3],
        n_stages=5
    )
    
    print(f"Total combinations: {sweep['total_combinations']}")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
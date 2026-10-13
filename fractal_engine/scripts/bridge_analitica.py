#!/usr/bin/env python3
"""
Bridge Analítica — Eixo 1: Ponte Analítica
Mapeamento obstruções algébricas ↔ latência de cauda (P99)
"""

import json
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Callable, Any
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from collections import Counter
import hashlib

@dataclass
class BridgeTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    lambda_rate: float
    mu_rate: float
    rho: float
    algebraic_obstruction: float
    P99_ideal: float
    P99_actual: float
    entropy: float
    fractal_dimension: float
    confidence_score: float

class BridgeAnalitica:
    """
    Eixo 1: Ponte Analítica
    Mapeia obstruções algébricas ↔ latência de cauda (P99)
    
    Fórmula: P99 = P99_ideal * (1 + rho/(1-rho) * p^2)
    onde rho = lambda/mu, p = obstruction_probability
    """
    
    def __init__(self):
        self.telemetry_log = []
    
    def _compute_entropy(self, data: List[float]) -> float:
        if not data:
            return 0.0
        discretized = [round(d/5)*5 for d in data]
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
    
    def compute_bridge(self, lambda_rate: float, mu_rate: float, 
                       algebraic_obstruction: float) -> Dict[str, Any]:
        """
        Computa a ponte analítica: obstrução algébrica -> P99
        
        Args:
            lambda_rate: Taxa de chegada (lambda)
            mu_rate: Taxa de serviço (mu)
            algebraic_obstruction: Obstrução algébrica (0 a 1)
            
        Returns:
            Dict com P99_ideal, P99_actual, entropia, dimensão fractal
        """
        rho = lambda_rate / mu_rate if mu_rate > 0 else 1.0
        obstruction_prob = min(1.0, algebraic_obstruction)
        
        P99_ideal = rho / (1 - rho) if rho < 1 else float('inf')
        P99_actual = P99_ideal * (1 + (rho/(1-rho)) * obstruction_prob**2) if rho < 1 else float('inf')
        
        # Telemetria
        bridge_data = [lambda_rate, mu_rate, algebraic_obstruction, rho, P99_actual]
        entropy = self._compute_entropy(bridge_data)
        fractal_dim = self._fractal_dimension([P99_actual])
        
        telemetry = BridgeTelemetry(
            timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            data_source="bridge_analitica.py (Eixo 1: Ponte Analítica)",
            metric_type="bridge_analitica",
            lambda_rate=lambda_rate,
            mu_rate=mu_rate,
            rho=rho,
            algebraic_obstruction=algebraic_obstruction,
            P99_ideal=P99_ideal,
            P99_actual=P99_actual,
            entropy=entropy,
            fractal_dimension=fractal_dim,
            confidence_score=0.9 if lambda_rate > 0 and mu_rate > 0 else 0.5
        )
        
        return {
            "lambda_rate": lambda_rate,
            "mu_rate": mu_rate,
            "rho": rho,
            "algebraic_obstruction": algebraic_obstruction,
            "P99_ideal": P99_ideal,
            "P99_actual": P99_actual,
            "entropy": entropy,
            "fractal_dimension": fractal_dim,
            "telemetry": asdict(telemetry)
        }
    
    def compute_entropy(self, data: List[float]) -> float:
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
            for x in data:
                box = int(x / eps)
                boxes.add(box)
            counts.append(len(boxes))
        log_scales = [math.log(1/s) for s in scales]
        log_counts = [math.log(c) for c in counts]
        if len(log_scales) > 1:
            coeff = np.polyfit([math.log(1/s) for s in scales], [math.log(c) for c in counts], 1)
            return abs(coeff[0])
        return 0.0
    
    def sensitivity_analysis(self, lambda_range: List[float], 
                             mu_range: List[float],
                             obstruction_range: List[float]) -> Dict[str, Any]:
        """Análise de sensibilidade da ponte analítica"""
        results = []
        
        for lam in lambda_range:
            for mu in mu_range:
                for obs in [0.0, 0.2, 0.5, 0.8]:
                    rho = lam / 1.0 if 1.0 > 0 else 1.0
                    obs_prob = min(1.0, obs)
                    P99_ideal = rho / (1 - rho) if rho < 1 else float('inf')
                    P99_actual = P99_ideal * (1 + (rho/(1-rho)) * (obs ** 2)) if rho < 1 else float('inf')
                    
                    results.append({
                        "lambda": lam,
                        "mu": 1.0,
                        "obstruction": obs,
                        "rho": rho,
                        "P99_ideal": P99_ideal,
                        "P99_actual": P99_actual,
                        "ratio": P99_actual / P99_ideal if P99_ideal != 0 and P99_ideal != float('inf') else 1.0
                    })
        
        return {
            "sensitivity_analysis": True,
            "total_points": len(_results),
            "data": results
        }

def main():
    print("=" * 70)
    print("BRIDGE ANALÍTICA — Eixo 1: Ponte Analítica")
    print("=" * 70)
    
    bridge = BridgeAnalitica()
    
    # Teste básico
    result = bridge.compute_bridge(lambda_rate=0.8, mu_rate=1.0, algebraic_obstruction=0.3)
    print(f"λ=0.8, μ=1.0, obs=0.3:")
    print(f"  ρ = {result['rho']:.3f}")
    print(f"  P99_ideal = {result['P99_ideal']:.3f}")
    print(f"  P99_actual = {result['P99_actual']:.3f}")
    print(f"  Entropia = {result['entropy']:.4f}")
    print(f"  Dim. Fractal = {result['fractal_dimension']:.4f}")
    
    # Análise de sensibilidade
    print("\n--- Análise de Sensibilidade ---")
    sensitivity = bridge.sensitivity_analysis(
        lambda_range=[0.5, 0.7, 0.8, 0.9],
        mu_range=[1.0],
        obstruction_range=[0.0, 0.2, 0.5, 0.8]
    )
    
    print(f"Total pontos testados: {len(_results)}")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
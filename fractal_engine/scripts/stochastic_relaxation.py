#!/usr/bin/env python3
"""
Stochastic Relaxation Engine — Eixo 4: Relaxamento Estocástico
Randomização destrói rigidez algébrica e protege o sistema
"""

import json
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Callable, Any
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from collections import Counter
import random

@dataclass
class StochasticTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    ideal_latency: float
    P99_PFA: float
    rho: float
    randomness_factor: float
    protection_factor: float
    entropy: float
    fractal_dimension: float
    confidence_score: float

class StochasticRelaxationEngine:
    """
    Eixo 4: Relaxamento Estocástico
    Randomização destrói rigidez algébrica e protege o sistema
    
    P99(PFA) = P99_ideal * (1 + sqrt(rho) * p^2)
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
    
    def compute_relaxation(self, ideal_latency: float, rho: float, 
                           randomness_factor: float,
                           p_squared: float = 0.1) -> Dict[str, Any]:
        """
        Computa relaxamento estocástico
        
        P99(PFA) = P99_ideal * (1 + sqrt(rho) * p^2)
        """
        sqrt_rho = math.sqrt(rho) if rho > 0 else 0
        
        P99_ideal = ideal_latency
        P99_PFA = P99_ideal * (1 + sqrt_rho * p_squared**2)
        
        # Fator de proteção estocástica
        protection_factor = P99_ideal / P99_PFA if P99_PFA > 0 else 1.0
        
        # Entropia do relaxamento
        relaxation_data = [ideal_latency, P99_PFA, rho, randomness_factor]
        entropy = self._compute_entropy(relaxation_data)
        fractal_dim = self._fractal_dimension([P99_ideal, P99_PFA])
        
        telemetry = StochasticTelemetry(
            timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            data_source="stochastic_relaxation.py (Eixo 4: Relaxamento Estocástico)",
            metric_type="stochastic_relaxation",
            ideal_latency=ideal_latency,
            P99_PFA=P99_PFA,
            rho=rho,
            randomness_factor=randomness_factor,
            protection_factor=protection_factor,
            entropy=entropy,
            fractal_dimension=fractal_dim,
            confidence_score=0.8
        )
        
        return {
            "ideal_latency": ideal_latency,
            "P99_PFA": P99_PFA,
            "rho": rho,
            "randomness_factor": randomness_factor,
            "protection_factor": protection_factor,
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
    
    def parameter_sweep(self, rho_range: List[float], 
                         randomness_range: List[float],
                         ideal_latency: float = 10.0,
                         p_squared: float = 0.1) -> Dict[str, Any]:
        """Varredura de parâmetros para análise de sensibilidade"""
        results = []
        
        for rho in rho_range:
            for rand_factor in randomness_range:
                result = self.compute_relaxation(
                    ideal_latency=ideal_latency,
                    rho=rho,
                    randomness_factor=rand_factor
                )
                results.append({
                    "rho": rho,
                    "randomness_factor": rand_factor,
                    "P99_PFA": result["P99_PFA"],
                    "protection_factor": result["protection_factor"],
                    "entropy": result["entropy"],
                    "fractal_dim": result["fractal_dimension"]
                })
        
        return {
            "parameter_sweep": True,
            "total_combinations": len(results),
            "data": results
        }
    
    def monte_carlo_simulation(self, n_samples: int = 1000,
                                rho: float = 0.8,
                                ideal_latency: float = 10.0,
                                p_squared: float = 0.1) -> Dict[str, Any]:
        """Simulação Monte Carlo do relaxamento estocástico"""
        protection_factors = []
        entropies = []
        
        for _ in range(n_samples):
            randomness_factor = random.uniform(0.1, 1.0)
            result = self.compute_relaxation(ideal_latency, rho, randomness_factor)
            protection_factors.append(result["protection_factor"])
            entropies.append(result["entropy"])
        
        return {
            "monte_carlo": True,
            "n_samples": n_samples,
            "avg_protection_factor": np.mean(protection_factors),
            "std_protection_factor": np.std(protection_factors),
            "avg_entropy": np.mean(entropies),
            "std_entropy": np.std(entropies),
            "min_protection": np.min(protection_factors),
            "max_protection": np.max(protection_factors)
        }

def main():
    print("=" * 70)
    print("STOCHASTIC RELAXATION ENGINE — Eixo 4: Relaxamento Estocástico")
    print("=" * 70)
    
    engine = StochasticRelaxationEngine()
    
    # Teste básico
    print("--- Teste Básico ---")
    result = engine.compute_relaxation(ideal_latency=10.0, rho=0.8, randomness_factor=0.5)
    print(f"Latência ideal: {result['ideal_latency']:.2f}")
    print(f"P99_PFA: {result['P99_PFA']:.2f}")
    print(f"Fator proteção: {result['protection_factor']:.4f}")
    print(f"Entropia: {result['entropy']:.4f}")
    print(f"Dim. Fractal: {result['fractal_dimension']:.4f}")
    
    # Varredura de parâmetros
    print("\n--- Varredura de Parâmetros ---")
    sweep = engine.parameter_sweep(
        rho_range=[0.5, 0.7, 0.8, 0.9],
        randomness_range=[0.1, 0.3, 0.5, 0.7, 0.9]
    )
    print(f"Total combinações testadas: {sweep['total_combinations']}")
    
    # Monte Carlo
    print("\n--- Simulação Monte Carlo ---")
    mc = engine.monte_carlo_simulation(n_samples=1000, rho=0.8)
    print(f"Amostras: {mc['n_samples']}")
    print(f"Fator proteção médio: {mc['avg_protection_factor']:.4f} ± {mc['std_protection_factor']:.4f}")
    print(f"Entropia média: {mc['avg_entropy']:.4f} ± {mc['std_entropy']:.4f}")
    print(f"Range proteção: [{mc['min_protection']:.4f}, {mc['max_protection']:.4f}]")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
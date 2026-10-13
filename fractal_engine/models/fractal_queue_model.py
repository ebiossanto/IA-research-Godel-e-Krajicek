#!/usr/bin/env python3
"""
Fractal Queue Model — Modelo de fila fractal para análise de sistemas complexos
"""

import json
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timezone

@dataclass
class QueueMetrics:
    lambda_rate: float
    mu_rate: float
    rho: float
    P99_ideal: float
    P99_actual: float
    W_avg: float
    L_avg: float
    entropy: float
    fractal_dimension: float

class FractalQueueModel:
    """
    Modelo de fila fractal para análise de sistemas complexos
    Baseado em teoria de filas M/M/1 com extensões fractais
    """
    
    def __init__(self):
        self.metrics_history = []
    
    def compute_steady_state(self, lambda_rate: float, mu_rate: float) -> QueueMetrics:
        """Calcula estado estacionário M/M/1"""
        rho = lambda_rate / mu_rate if mu_rate > 0 else 1.0
        
        if rho >= 1:
            return QueueMetrics(
                lambda_rate=lambda_rate,
                mu_rate=mu_rate,
                rho=rho,
                P99_ideal=float('inf'),
                P99_actual=float('inf'),
                W_avg=float('inf'),
                L_avg=float('inf'),
                entropy=0.0,
                fractal_dimension=0.0
            )
        
        # Métricas padrão M/M/1
        P99_ideal = rho / (1 - rho)
        W_avg = 1 / (mu_rate - lambda_rate)
        L_avg = lambda_rate / (mu_rate - lambda_rate)
        
        # P99 com obstrução algébrica (fractal)
        obstruction = 0.3  # Parâmetro de obstrução
        p = 0.3
        P99_actual = (rho / (1 - rho)) * (1 + (rho/(1-rho)) * 0.3**2)
        
        # Entropia e dimensão fractal
        entropy = self._compute_entropy([rho, 1-rho])
        fractal_dim = self._fractal_dimension([rho, 1-rho])
        
        metrics = QueueMetrics(
            lambda_rate=lambda_rate,
            mu_rate=mu_rate,
            rho=rho,
            P99_ideal=rho/(1-rho),
            P99_actual=rho/(1-rho) * (1 + (rho/(1-rho)) * 0.09),
            W_avg=W_avg,
            L_avg=L_avg,
            entropy=self._compute_entropy([rho, 1-rho]),
            fractal_dimension=self._fractal_dimension([rho, 1-rho])
        )
        
        self.metrics_history.append(metrics)
        return metrics
    
    def _compute_entropy(self, data: List[float]) -> float:
        if not data:
            return 0.0
        from collections import Counter
        counts = Counter([round(d*10)/10 for d in data])
        total = len(data)
        return -sum((c/len(data)) * math.log2(c/len(data)) for c in counts.values())
    
    def _fractal_dimension(self, data: List[float]) -> float:
        if len(data) < 2:
            return 0.0
        data_norm = np.array(data)
        data_norm = (data_norm - np.min(data_norm)) / (np.max(data_norm) - np.min(data_norm) + 1e-9)
        scales = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
        counts = []
        for eps in scales:
            boxes = set()
            for x in data_norm:
                boxes.add(int(x / eps))
            counts.append(len(boxes))
        log_scales = [math.log(1/s) for s in scales]
        log_counts = [math.log(c) for c in counts]
        if len(log_scales) > 1:
            coeff = np.polyfit(log_scales, log_counts, 1)
            return abs(coeff[0])
        return 0.0
    
    def compute_transient(self, lambda_rate: float, mu_rate: float, 
                          t: float) -> Dict[str, float]:
        """Solução transiente M/M/1"""
        rho = lambda_rate / mu_rate if mu_rate > 0 else 1.0
        if rho >= 1:
            return {"L_t": float('inf'), "W_t": float('inf')}
        
        L_inf = rho / (1 - rho)
        decay = mu_rate - lambda_rate
        
        L_t = rho / (1 - rho) * (1 - math.exp(-decay * t))
        W_t = 1 / (mu_rate - lambda_rate) * (1 - math.exp(-decay * t))
        
        return {
            "L_t": L_t,
            "W_t": W_t,
            "L_inf": lambda_rate / (mu_rate - lambda_rate),
            "W_inf": 1 / (mu_rate - lambda_rate)
        }
    
    def fractal_queue_analysis(self, lambda_rate: float, mu_rate: float,
                               fractal_param: float = 0.5) -> Dict:
        """Análise de fila com parâmetro fractal"""
        rho = lambda_rate / mu_rate if mu_rate > 0 else 1.0
        
        if rho >= 1:
            return {"status": "unstable", "rho": rho}
        
        # Parâmetro fractal afeta variabilidade
        cv_squared = 1 + fractal_param  # Coeficiente de variação quadrado
        
        # Aproximação de Kingman para G/G/1
        W_q_approx = (rho / (1 - rho)) * (cv_squared + 1) / (2 * mu_rate * (1 - rho))
        L_q = lambda_rate * W_q
        
        return {
            "W_q": W_q,
            "L_q": L_q,
            "W": W_q + 1/mu_rate,
            "L": L_q + rho,
            "fractal_param": fractal_param
        }

def main():
    print("=" * 70)
    print("FRACTAL QUEUE MODEL — Modelo de Fila Fractal")
    print("=" * 70)
    
    model = FractalQueueModel()
    
    # Teste estado estacionário
    print("\n--- Estado Estacionário ---")
    for lambda_rate in [0.3, 0.5, 0.7, 0.9]:
        metrics = model.compute_steady_state(lambda_rate, 1.0)
        print(f"λ={lambda_rate:.1f}: ρ={metrics.rho:.3f}, "
              f"P99_ideal={metrics.P99_ideal:.2f}, "
              f"P99_actual={metrics.P99_actual:.2f}, "
              f"Entropy={metrics.entropy:.4f}, "
              f"FractalDim={metrics.fractal_dimension:.4f}")
    
    # Transiente
    print("\n--- Comportamento Transiente ---")
    for t in [0.5, 1.0, 2.0, 5.0, 10.0]:
        trans = model.compute_transient(0.8, 1.0, t)
        print(f"t={t}: L(t)={trans['L_t']:.3f}, W(t)={trans['W_t']:.3f}")
    
    # Fractal analysis
    print("\n--- Análise Fratal ---")
    for fp in [0.1, 0.3, 0.5, 0.8]:
        result = model.fractal_queue_analysis(0.8, 1.0, fp)
        print(f"fp={fp:.1f}: W_q={result['W_q']:.3f}, L_q={result['L_q']:.3f}")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
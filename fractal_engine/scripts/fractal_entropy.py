#!/usr/bin/env python3
"""
Fractal Entropy Engine — Cálculo avançado de entropia e dimensão fractal
Para análise de sistemas complexos no Terminal-Laboratório
"""

import json
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Callable, Any
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from collections import Counter
from itertools import product

@dataclass
class EntropyTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    shannon_entropy: float
    renyi_entropy_alpha2: float
    renyi_entropy_alpha05: float
    tsallis_entropy_q2: float
    fractal_dimension_box: float
    fractal_dimension_correlation: float
    multifractal_spectrum: Dict[str, float]
    confidence_score: float

class FractalEntropyEngine:
    """
    Motor avançado de entropia e dimensão fractal
    Para análise de sistemas complexos no Terminal-Laboratório
    """
    
    def __init__(self):
        self.telemetry_log = []
    
    # =========================================================================
    # ENTROPIA DE SHANNON
    # =========================================================================
    
    def shannon_entropy(self, data: List[float], bins: int = 10) -> float:
        """Entropia de Shannon clássica"""
        if data is None or len(data) == 0:
            return 0.0
        
        # Discretização em bins
        data_min, data_max = min(data), max(data)
        if data_max == data_min:
            return 0.0
        
        bins_edges = np.linspace(data_min, data_max, bins + 1)
        hist, _ = np.histogram(data, bins=bins_edges)
        probs = hist / len(data)
        probs = probs[probs > 0]
        
        return -np.sum(probs * np.log2(probs))
    
    def shannon_entropy_discrete(self, data: List[Any]) -> float:
        """Entropia de Shannon para dados discretos"""
        if data is None or len(data) == 0:
            return 0.0
        
        counts = Counter(data)
        total = len(data)
        probs = [c/total for c in counts.values() if c > 0]
        
        return -sum(p * math.log2(p) for p in probs)
    
    # =========================================================================
    # ENTROPIA DE RÉNYI
    # =========================================================================
    
    def renyi_entropy(self, data: List[float], alpha: float = 2.0, bins: int = 10) -> float:
        """
        Entropia de Rényi de ordem alpha
        H_alpha = 1/(1-alpha) * log(sum(p_i^alpha))
        """
        if alpha == 1.0:
            return self.shannon_entropy(data)
        
        if data is None or len(data) == 0:
            return 0.0
        
        data_min, data_max = min(data), max(data)
        if data_max == data_min:
            return 0.0
        
        bins_edges = np.linspace(data_min, data_max, 20 + 1)
        hist, _ = np.histogram(data, bins=bins_edges)
        probs = hist / len(data)
        probs = probs[probs > 0]
        
        if alpha == 0:
            return math.log2(len(probs))
        elif alpha == 2:
            return -math.log2(sum(p**2 for p in probs))
        else:
            sum_alpha = sum(p**alpha for p in probs)
            return (1/(1-alpha)) * math.log2(sum_alpha)
    
    def renyi_spectrum(self, data: List[float], 
                       alphas: List[float] = None) -> Dict[float, float]:
        """Espectro de entropia de Rényi para múltiplos alphas"""
        if alphas is None:
            alphas = [0, 0.5, 1, 2, 3, 5, 10]
        
        spectrum = {}
        for alpha in alphas:
            spectrum[alpha] = self.renyi_entropy(data, alpha)
        return spectrum
    
    # =========================================================================
    # ENTROPIA DE TSALLIS
    # =========================================================================
    
    def tsallis_entropy(self, data: List[float], q: float = 2.0, bins: int = 10) -> float:
        """
        Entropia de Tsallis
        S_q = (1 - sum(p_i^q)) / (q - 1)
        """
        if q == 1.0:
            return self.shannon_entropy(data)
        
        if data is None or len(data) == 0:
            return 0.0
        
        data_min, data_max = min(data), max(data)
        if data_max == data_min:
            return 0.0
        
        bins_edges = np.linspace(data_min, data_max, bins + 1)
        hist, _ = np.histogram(data, bins=bins_edges)
        probs = hist / len(data)
        probs = probs[probs > 0]
        
        if q == 1:
            return self.shannon_entropy(data)
        
        sum_q = sum(p**q for p in probs)
        return (1 - sum_q) / (q - 1)
    
    # =========================================================================
    # DIMENSÃO FRATAL - BOX COUNTING
    # =========================================================================
    
    def box_counting_dimension(self, data: List[float]) -> float:
        """Dimensão fractal via box-counting"""
        if len(data) < 10:
            return 0.0
        
        data_norm = np.array(data)
        data_norm = (data_norm - np.min(data_norm)) / (np.max(data_norm) - np.min(data_norm) + 1e-9)
        
        scales = np.logspace(-2, 0, 20)  # 0.01 a 1
        counts = []
        
        for eps in scales:
            boxes = set()
            for x in data_norm:
                box = int(x / eps)
                boxes.add(box)
            counts.append(len(boxes))
        
        # Regressão log-log
        log_scales = np.log(1 / np.array(scales))
        log_counts = np.log(np.array(counts) + 1)
        
        valid = np.isfinite(log_counts) & np.isfinite(log_scales)
        if np.sum(valid) > 1:
            coeff = np.polyfit(log_scales[valid], np.log(np.array(counts)[valid] + 1), 1)
            return abs(coeff[0])
        return 0.0
    
    def correlation_dimension(self, data: List[float], 
                              max_distance: float = 1.0) -> float:
        """Dimensão de correlação (Grassberger-Procaccia)"""
        if len(data) < 20:
            return 0.0
        
        data_array = np.array(data).reshape(-1, 1)
        distances = []
        
        for i in range(len(data_array)):
            for j in range(i+1, len(data_array)):
                dist = abs(data_array[i] - data_array[j])
                distances.append(dist)
        
        distances = np.array(distances)
        if len(distances) == 0:
            return 0.0
        
        # Correlação integral C(r)
        r_values = np.logspace(-3, 0, 30)
        C_r = []
        
        for r in r_values:
            count = np.sum(distances < r)
            C_r.append(count / len(distances))
        
        # Regressão log-log para estimar dimensão
        valid = [(r, c) for r, c in zip(r_values, C_r) if c > 0]
        if len(valid) > 2:
            log_r = [math.log(r) for r, _ in valid]
            log_c = [math.log(c) for _, c in valid]
            coeff = np.polyfit(log_r, log_c, 1)
            return coeff[0]
        return 0.0
    
    # =========================================================================
    # ESPECTRO MULTIFRATAL
    # =========================================================================
    
    def multifractal_spectrum(self, data: List[float], 
                              q_range: Tuple[float, float] = (-5, 5),
                              q_steps: int = 21) -> Dict[str, Any]:
        """
        Calcula espectro multifractal f(alpha) via partição de momentos
        """
        if len(data) < 20:
            return {}
        
        data_norm = np.array(data)
        data_norm = (data_norm - np.min(data_norm)) / (np.max(data_norm) - np.min(data_norm) + 1e-9)
        
        q_values = np.linspace(q_range[0], q_range[1], q_steps)
        tau_q = []
        alpha_q = []
        f_alpha = []
        
        for q in q_values:
            if q == 1:
                continue
            
            # Partição em caixas
            eps = 0.05
            boxes = {}
            for x in data:
                box = int(x / eps)
                boxes[box] = boxes.get(box, 0) + 1
            
            probs = np.array(list(boxes.values()))
            probs = probs / np.sum(probs)
            
            if q == 1:
                tau = -np.sum(probs * np.log2(probs))
            else:
                tau = np.log2(np.sum(probs ** q)) / (q - 1)
            
            tau_q.append(tau)
        
        # Legendre transform para obter f(alpha)
        if len(tau_q) > 2:
            q_vals = [q for q in q_values if q != 1]
            tau_vals = np.array(tau_q)
            
            # Derivada numérica para alpha
            alpha_vals = np.gradient(tau_vals, q_vals)
            
            # f(alpha) = q*alpha - tau(q)
            f_vals = np.array(q_vals) * alpha_vals - tau_vals
            
            return {
                "q_values": q_vals,
                "tau_q": tau_vals.tolist(),
                "alpha_q": alpha_vals.tolist(),
                "f_alpha": f_vals.tolist()
            }
        
        return {}
    
    # =========================================================================
    # ENTROPIA CONDICIONAL E MUTUAL INFORMATION
    # =========================================================================
    
    def conditional_entropy(self, X: List[float], Y: List[float], 
                            bins: int = 10) -> float:
        """H(X|Y) = H(X,Y) - H(Y)"""
        if len(X) != len(Y):
            return 0.0
        
        # Joint entropy H(X,Y)
        joint_data = list(zip(X, Y))
        H_XY = self.shannon_entropy_discrete(joint_data)
        
        # Marginal entropy H(Y)
        H_Y = self.shannon_entropy(Y)
        
        return H_XY - H_Y
    
    def mutual_information(self, X: List[float], Y: List[float], 
                           bins: int = 10) -> float:
        """Informação mútua I(X;Y) = H(X) + H(Y) - H(X,Y)"""
        H_X = self.shannon_entropy(X)
        H_Y = self.shannon_entropy(Y)
        H_XY = self.shannon_entropy_discrete(list(zip(X, Y)))
        
        return H_X + H_Y - H_XY
    
    def transfer_entropy(self, X: List[float], Y: List[float], 
                         lag: int = 1, bins: int = 10) -> float:
        """Entropia de transferência T_{Y->X}"""
        if len(X) <= lag or len(Y) <= lag:
            return 0.0
        
        # X_{t+1} dado X_t e Y_t
        X_future = X[lag:]
        X_past = X[:-lag]
        Y_past = Y[:-lag]
        
        # T_{Y->X} = H(X_{t+1}|X_t) - H(X_{t+1}|X_t, Y_t)
        H_X_given_X = self.conditional_entropy(X_future, X_past)
        H_X_given_XY = self.conditional_entropy_triple(X_future, X_past, Y_past)
        
        return H_X_given_X - H_X_given_XY
    
    def conditional_entropy_triple(self, X: List, Y: List, Z: List) -> float:
        """H(X|Y,Z)"""
        joint_YZ = list(zip(Y, Z))
        H_X_given_YZ = self.conditional_entropy(X, joint_YZ)
        return H_X_given_YZ
    
    def conditional_entropy(self, X: List, Y: List) -> float:
        return self.conditional_entropy(X, Y)
    
    # =========================================================================
    # ANÁLISE COMPLETA
    # =========================================================================
    
    def full_entropy_analysis(self, data: List[float]) -> Dict[str, Any]:
        """Análise completa de entropia e dimensão fractal"""
        
        results = {
            "shannon_entropy": self.shannon_entropy(data),
            "renyi_spectrum": self.renyi_spectrum(data),
            "tsallis_q2": self.tsallis_entropy(data, q=2.0),
            "tsallis_q05": self.tsallis_entropy(data, q=0.5),
            "box_counting_dim": self.box_counting_dimension(data),
            "correlation_dim": self.correlation_dimension(data),
            "multifractal_spectrum": self.multifractal_spectrum(data)
        }
        
        return results
    
    def save_results(self, results: Dict, prefix: str = "fractal_entropy"):
        with open(f"{prefix}.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"[Fractal Entropy] Resultados salvos: {prefix}.json")

def main():
    print("=" * 70)
    print("FRACTAL ENTROPY ENGINE — Análise Avançada de Entropia")
    print("=" * 70)
    
    engine = FractalEntropyEngine()
    
    # Dados de teste
    np.random.seed(42)
    data_normal = np.random.normal(0, 1, 1000)
    data_fractal = np.cumsum(np.random.normal(0, 1, 1000))  # Random walk
    
    print("\n--- Dados Normais ---")
    results_normal = engine.full_entropy_analysis(data_normal.tolist())
    for k, v in results_normal.items():
        if isinstance(v, (int, float)):
            print(f"  {k}: {v:.4f}")
        elif isinstance(v, dict):
            print(f"  {k}: {len(v)} pontos")
    
    print("\n--- Dados Fratais (Random Walk) ---")
    results_fractal = engine.full_entropy_analysis(data_fractal.tolist())
    for k, v in results_fractal.items():
        if isinstance(v, (int, float)):
            print(f"  {k}: {v:.4f}")
        elif isinstance(v, dict):
            print(f"  {k}: {len(v)} pontos")
    
    # Salva resultados
    engine.save_results(results_normal, "entropy_normal")
    engine.save_results(results_fractal, "entropy_fractal")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
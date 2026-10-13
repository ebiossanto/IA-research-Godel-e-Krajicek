#!/usr/bin/env python3
"""
Fractal Dimension Model — Modelos de dimensão fractal
Para análise de dimensão fractal em sistemas complexos
"""

import json
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Callable, Any
from dataclasses import dataclass, asdict
from datetime import datetime, timezone

@dataclass
class FractalDimensionMetrics:
    box_counting_dim: float
    correlation_dim: float
    information_dim: float
    hausdorff_dim_estimate: float
    multifractal_spectrum_width: float
    lacunarity: float

class FractalDimensionModel:
    """
    Modelos de dimensão fractal para análise de sistemas complexos
    """
    
    def __init__(self):
        self.history = []
    
    def box_counting(self, data: np.ndarray, 
                     min_scale: float = 0.01, max_scale: float = 1.0,
                     num_scales: int = 20) -> float:
        """
        Dimensão fractal via box-counting
        """
        data = np.asarray(data).flatten()
        if len(data) < 10:
            return 0.0
        
        # Normaliza
        data_norm = (data - np.min(data)) / (np.max(data) - np.min(data) + 1e-9)
        
        scales = np.logspace(np.log10(min_scale), np.log10(max_scale), 30)
        counts = []
        
        for eps in scales:
            boxes = set()
            for x in data:
                box = int(x / eps)
                boxes.add(box)
            counts.append(len(boxes))
        
        # Regressão log-log
        valid = np.array(counts) > 0
        if np.sum(valid) < 3:
            return 0.0
        
        log_scales = np.log(1 / np.array(scales))
        log_counts = np.log(np.array(counts))
        
        valid_mask = np.isfinite(np.log(np.array(counts))) & np.isfinite(np.log(1/np.array(scales)))
        if np.sum(valid_mask) < 3:
            return 0.0
            
        coeff = np.polyfit(np.log(1/np.array(scales))[valid_mask], 
                          np.log(np.array(counts))[valid_mask], 1)
        return abs(coeff[0])
    
    def correlation_dimension(self, data: np.ndarray, 
                              max_distance: float = None,
                              num_distances: int = 30) -> float:
        """
        Dimensão de correlação (Grassberger-Procaccia)
        """
        data = np.asarray(data).flatten()
        if len(data) < 20:
            return 0.0
        
        # Calcula distâncias
        distances = []
        for i in range(len(data)):
            for j in range(i+1, len(data)):
                distances.append(abs(data[i] - data[j]))
        
        distances = np.array(distances)
        if max_distance is None:
            max_distance = np.max(distances)
        
        r_values = np.logspace(np.log10(1e-6), np.log10(max_distance), 30)
        C_r = []
        
        for r in r_values:
            count = np.sum(distances < r)
            C_r = count / len(distances) if len(distances) > 0 else 0
            C_r.append(C_r)
        
        # Regressão log-log
        valid = np.array(C_r) > 0
        if np.sum(valid) < 3:
            return 0.0
            
        log_r = np.log(np.array(r_values)[valid])
        log_c = np.log(np.array(C_r)[valid])
        
        coeff = np.polyfit(np.log(r_values)[valid], np.log(np.array(C_r)[valid]), 1)
        return coeff[0]
    
    def information_dimension(self, data: np.ndarray, bins: int = 20) -> float:
        """
        Dimensão de informação (entropia de Shannon / log(1/eps))
        """
        if len(data) < 10:
            return 0.0
        
        data = np.asarray(data).flatten()
        data_min, data_max = np.min(data), np.max(data)
        if data_max == data_min:
            return 0.0
        
        epsilons = np.logspace(-3, 0, 15)
        H_eps = []
        eps_vals = []
        
        for eps in np.logspace(-3, 0, 15):
            bins = int(1/eps) + 1
            hist, _ = np.histogram(data, bins=min(bins, int(1/eps)+1), 
                                   range=(np.min(data), np.max(data)))
            probs = hist / len(data)
            probs = probs[probs > 0]
            H = -np.sum(probs * np.log2(probs))
            H_eps.append(H)
            eps_vals.append(eps)
        
        # Dimensão de informação = lim_{eps->0} H(eps) / log(1/eps)
        valid = np.array(eps_vals) > 0
        if np.sum(valid) > 2:
            coeff = np.polyfit(np.log(1/np.array(eps_vals)[valid]), 
                              np.array(H_eps)[valid], 1)
            return coeff[0]
        return 0.0
    
    def hausdorff_dimension_estimate(self, data: np.ndarray) -> float:
        """
        Estimativa da dimensão de Hausdorff via múltiplos métodos
        """
        bc_dim = self.box_counting(data)
        corr_dim = self.correlation_dimension(data)
        info_dim = self.information_dimension(data)
        
        # Hausdorff <= Information <= Correlation <= Box-counting
        # Usa o mínimo como estimativa conservadora
        dims = [d for d in [bc_dim, corr_dim, info_dim] if d > 0]
        return min(dims) if dims else 0.0
    
    def lacunarity(self, data: np.ndarray, box_size: int = 5) -> float:
        """
        Lacunaridade - medida de heterogeneidade espacial
        """
        if len(data) < 100:
            return 0.0
        
        # Divide em caixas
        box_size = box_size
        n_boxes = len(data) // box_size
        if n_boxes < 2:
            return 0.0
        
        # Reorganiza em grade (aproximação 1D)
        data_reshaped = data[:n_boxes * box_size].reshape(n_boxes, box_size)
        box_masses = np.sum(data_reshaped, axis=1)
        
        if np.mean(box_masses) == 0:
            return 0.0
        
        lac = np.var(box_masses) / (np.mean(box_masses) ** 2)
        return lac
    
    def multifractal_spectrum(self, data: np.ndarray, 
                               q_range: Tuple[float, float] = (-5, 5),
                               q_steps: int = 21) -> Dict[str, Any]:
        """
        Espectro multifractal f(alpha)
        """
        if len(data) < 20:
            return {}
        
        data_norm = np.asarray(data)
        data_norm = (data_norm - np.min(data_norm)) / (np.max(data_norm) - np.min(data_norm) + 1e-9)
        
        q_values = np.linspace(-5, 5, 21)
        tau_q = []
        
        for q in q_values:
            if q == 1:
                continue
            
            eps = 0.05
            boxes = {}
            for x in data:
                box = int(x / eps)
                boxes[box] = boxes.get(box, 0) + 1
            
            probs = np.array(list(boxes.values()))
            probs = probs / np.sum(probs)
            
            if q == 1:
                tau = -np.sum(probs * np.log2(probs + 1e-12))
            else:
                tau = np.log2(np.sum(probs ** q + 1e-12)) / (q - 1)
            
            tau_q.append(tau)
        
        # Transformada de Legendre para f(alpha)
        if len(tau_q) > 2:
            q_vals = np.array([q for q in np.linspace(-5, 5, 21) if q != 1])
            tau_vals = np.array(tau_q)
            
            alpha_vals = np.gradient(tau_vals, q_vals)
            f_alpha = q_vals * alpha_vals - tau_vals
            
            return {
                "q_values": q_vals.tolist(),
                "tau_q": tau_q,
                "alpha_q": alpha_vals.tolist(),
                "f_alpha": f_alpha.tolist(),
                "width": np.max(alpha_vals) - np.min(alpha_vals),
                "peak_f_alpha": np.max(f_alpha)
            }
        
        return {}
    
    def lacunarity(self, data: np.ndarray, box_sizes: List[int] = None) -> float:
        """
        Lacunaridade média em múltiplas escalas
        """
        if box_sizes is None:
            box_sizes = [4, 8, 16, 32]
        
        lacunarities = []
        for box_size in box_sizes:
            lac = self.lacunarity_at_scale(data, box_size)
            lacunarities.append(lac)
        
        return np.mean(lacunarities) if lacunarities else 0.0
    
    def lacunarity_at_scale(self, data: np.ndarray, box_size: int) -> float:
        if len(data) < box_size * 2:
            return 0.0
        
        n_boxes = len(data) // box_size
        if n_boxes < 2:
            return 0.0
        
        data_reshaped = data[:n_boxes * box_size].reshape(n_boxes, box_size)
        box_masses = np.sum(data_reshaped, axis=1)
        
        if np.mean(box_masses) == 0:
            return 0.0
        
        lac = np.var(box_masses) / (np.mean(box_masses) ** 2)
        return lac
    
    def analyze(self, data: np.ndarray) -> Dict[str, float]:
        """Análise completa de dimensão fractal"""
        results = {
            "box_counting_dim": self.box_counting(data),
            "correlation_dim": self.correlation_dimension(data),
            "information_dim": self.information_dimension(data),
            "hausdorff_estimate": self.hausdorff_dimension_estimate(data),
            "lacunarity": self.lacunarity(data),
            "multifractal_spectrum": self.multifractal_spectrum(data)
        }
        
        return results

def main():
    print("=" * 70)
    print("FRACTAL DIMENSION MODEL — Modelos de Dimensão Fractal")
    print("=" * 70)
    
    model = FractalDimensionModel()
    
    # Dados de teste
    np.random.seed(42)
    
    # Dados normais
    normal_data = np.random.normal(0, 1, 1000)
    
    # Dados fractais (random walk)
    fractal_data = np.cumsum(np.random.normal(0, 1, 1000))
    
    # Dados com estrutura de Cantor-like
    cantor_data = []
    for i in range(1000):
        x = i / 1000
        # Função de Cantor aproximada
        val = 0
        x_temp = i / 1000
        for k in range(10):
            if int(x_temp * 3**k) % 3 == 1:
                val += (2/3)**k
        cantor_data.append(val)
    
    print("=" * 70)
    print("FRACTAL DIMENSION MODEL — Análise de Dimensão Fractal")
    print("=" * 70)
    
    datasets = {
        "Normal": np.random.normal(0, 1, 1000),
        "Fractal (RW)": np.cumsum(np.random.normal(0, 1, 1000)),
        "Cantor-like": np.array(cantor_data)
    }
    
    for name, data in datasets.items():
        print(f"\n--- {name} ---")
        results = model.analyze(data)
        for k, v in results.items():
            if isinstance(v, (int, float)):
                print(f"  {k}: {v:.4f}")
            elif isinstance(v, dict):
                print(f"  {k}: width={v.get('width', 0):.4f}, peak={v.get('peak_f_alpha', 0):.4f}")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
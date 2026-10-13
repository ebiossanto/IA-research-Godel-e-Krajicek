#!/usr/bin/env python3
"""
Fractal Engine — Motor computacional para Teoria de Controle Fractal (FCT)
Implementa os 4 eixos: Ponte Analítica, Bullwhip, Expansão Não-Abeliana, Relaxamento Estocástico
"""

import json
import math
import numpy as np
import hashlib
from typing import List, Dict, List, Tuple, Optional, Callable, Any
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from itertools import product
from collections import Counter
import random

@dataclass
class FractalTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    axis: str
    value: float
    parameters: Dict[str, Any]
    entropy: float
    fractal_dimension: float
    confidence_score: float

@dataclass
class QueueState:
    """Estado de uma fila no modelo fractal"""
    lambda_rate: float
    mu_rate: float
    rho: float
    P99_ideal: float
    P99_actual: float
    algebraic_obstruction: float

class FractalEngine:
    """
    Motor Fractal — Implementa os 4 eixos da Teoria de Controle Fractal:
    
    1. Ponte Analítica: Mapeamento obstruções algébricas ↔ latência de cauda
    2. Efeito Bullwhip: Amplificação multiplicativa de erros em cascata
    3. Expansões Não-Abelianas: Grupos não-abelianos 2× mais destrutivos
    4. Relaxamento Estocástico: Randomização destrói rigidez algébrica
    """
    
    def __init__(self, phi_len: int = 12, r_w: int = 4, w_star: str = "00"):
        self.phi_len = phi_len
        self.r_w = r_w
        self.w_star = w_star
        self.obligations = self._build_obligations()
        self.telemetry_log: List[Dict] = []
        
    def _build_obligations(self) -> List[Dict]:
        """Constrói conjunto de obrigações W = {0,1}^r"""
        obligations = []
        for bits in product('01', repeat=4):
            w = ''.join(bits)
            is_wstar = w.startswith(self.w_star)
            kappa = 2 if is_wstar else (sum(ord(c) for c in w) % 2)
            obligations.append({"idx": w, "is_wstar": is_wstar, "kappa": kappa})
        return obligations
    
    def _proof_complexity(self, sigma: int, o: Dict, is_T1: bool) -> int:
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
    
    def _covered(self, sigma: int, b: int, o: Dict, is_T1: bool) -> bool:
        return self._proof_complexity(sigma, o, is_T1) <= b
    
    def _first_uncovered(self, sigma: int, b: int, is_T1: bool) -> Optional[str]:
        for o in sorted(self.obligations, key=lambda x: x["idx"]):
            if not self._covered(sigma, b, o, is_T1):
                return o["idx"]
        return None
    
    def _generator(self, sigma: int, u: str, a: callable, b: int, is_T1: bool) -> str:
        n = len(u)
        if n < self.phi_len or self.phi_len > a(n):
            return '0' * (n + 1)
        w0 = self._first_uncovered(sigma, b, is_T1)
        if w0 is None:
            return '0' * (n + 1)
        return w0 + u[self.phi_len:]
    
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
        # Normaliza dados
        data_norm = [(d - min(data)) / (max(data) - min(data) + 1e-9) for d in data]
        # Box-counting aproximado
        scales = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
        counts = []
        for eps in scales:
            boxes = set()
            for x in data_norm:
                box = int(x / eps)
                boxes.add(box)
            counts.append(len(boxes))
        # Regressão linear log-log
        log_scales = [math.log(1/s) for s in scales]
        log_counts = [math.log(c) for c in counts]
        if len(log_scales) > 1:
            coeff = np.polyfit(log_scales, log_counts, 1)
            return abs(coeff[0])
        return 0.0

    # =========================================================================
    # EIXO 1: PONTE ANALÍTICA
    # =========================================================================
    
    def bridge_analitica(self, lambda_rate: float, mu_rate: float, 
                         algebraic_obstruction: float) -> Dict[str, Any]:
        """
        Eixo 1: Ponte Analítica
        Mapeia obstruções algébricas → latência de cauda (P99)
        
        Fórmula: P99 = P99_ideal * (1 + rho/(1-rho) * p^2)
        onde rho = lambda/mu, p = obstruction_probability
        """
        rho = lambda_rate / mu_rate if mu_rate > 0 else 1.0
        obstruction_prob = min(1.0, algebraic_obstruction)
        
        P99_ideal = rho / (1 - rho) if rho < 1 else float('inf')
        P99_actual = P99_ideal * (1 + (rho/(1-rho)) * obstruction_prob**2) if rho < 1 else float('inf')
        
        # Entropia da ponte
        bridge_data = [lambda_rate, mu_rate, algebraic_obstruction, rho, P99_actual]
        entropy = self._compute_entropy(bridge_data)
        fractal_dim = self._fractal_dimension([P99_actual])
        
        telemetry = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "data_source": "fractal_engine.py (Eixo 1: Ponte Analítica)",
            "metric_type": "bridge_analitica",
            "axis": "ponte_analitica",
            "lambda_rate": lambda_rate,
            "mu_rate": mu_rate,
            "rho": rho,
            "algebraic_obstruction": algebraic_obstruction,
            "P99_ideal": P99_ideal,
            "P99_actual": P99_actual,
            "entropy": entropy,
            "fractal_dimension": fractal_dim,
            "confidence_score": 0.9 if lambda_rate > 0 and mu_rate > 0 else 0.5
        }
        
        self.telemetry_log.append(telemetry)
        return telemetry

    # =========================================================================
    # EIXO 2: EFEITO BULLWHIP
    # =========================================================================
    
    def bullwhip_effect(self, rho_values: List[float], p_values: List[float], 
                        n_stages: int = 5) -> Dict[str, Any]:
        """
        Eixo 2: Efeito Bullwhip Algébrico
        Amplificação multiplicativa de erros em cascata
        
        P99^(n) = P99^(0) * ∏(1 + rho_k/(1-rho_k) * p_k^2)
        """
        P99_initial = 1.0
        P99_evolution = [P99_initial]
        
        for k in range(min(n_stages, len(rho_values), len(p_values))):
            rho_k = rho_values[k]
            p_k = p_values[k]
            if rho_k < 1:
                factor = 1 + (rho_k / (1 - rho_k)) * (p_k ** 2)
                P99_initial *= factor
                P99_evolution.append(P99_initial)
            else:
                P99_evolution.append(float('inf'))
        
        # Amplificação total
        amplification = P99_evolution[-1] / P99_evolution[0] if P99_evolution[0] > 0 else float('inf')
        
        entropy = self._compute_entropy(P99_evolution)
        fractal_dim = self._fractal_dimension(P99_evolution)
        
        telemetry = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "data_source": "fractal_engine.py (Eixo 2: Bullwhip)",
            "metric_type": "bullwhip_effect",
            "axis": "bullwhip",
            "rho_values": rho_values[:n_stages],
            "p_values": p_values[:n_stages],
            "P99_evolution": P99_evolution,
            "amplification_factor": amplification,
            "entropy": entropy,
            "fractal_dimension": fractal_dim,
            "confidence_score": 0.85
        }
        
        self.telemetry_log.append(telemetry)
        return telemetry

    # =========================================================================
    # EIXO 3: EXPANSÕES NÃO-ABELIANAS
    # =========================================================================
    
    def nonabelian_expansion(self, group_order: int, abelian: bool = False) -> Dict[str, Any]:
        """
        Eixo 3: Expansões Não-Abelianas
        Grupos não-abelianos são 2x mais destrutivos que abelianos
        
        E*_S_n = (n! - 2) / (n! * (n-1)) -> 1/(n-1)
        """
        # Ordem do grupo simétrico S_n
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
        
        telemetry = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "data_source": "fractal_engine.py (Eixo 3: Expansões Não-Abelianas)",
            "metric_type": "nonabelian_expansion",
            "axis": "nonabelian_expansion",
            "group_order": n,
            "E_star": E_star,
            "asymptotic_limit": asymptotic_limit,
            "destruction_factor": destruction_factor,
            "abelian": abelian,
            "entropy": entropy,
            "fractal_dimension": fractal_dim,
            "confidence_score": 0.8
        }
        
        self.telemetry_log.append(telemetry)
        return telemetry

    # =========================================================================
    # EIXO 4: RELAXAMENTO ESTOCÁSTICO
    # =========================================================================
    
    def stochastic_relaxation(self, ideal_latency: float, rho: float, 
                              randomness_factor: float) -> Dict[str, Any]:
        """
        Eixo 4: Relaxamento Estocástico
        Randomização destrói rigidez algébrica e protege o sistema
        
        P99(PFA) = P99_ideal * (1 + sqrt(rho) * p^2)
        """
        p_squared = 0.1  # Parâmetro de probabilidade padrão
        sqrt_rho = math.sqrt(rho) if rho > 0 else 0
        
        P99_ideal = ideal_latency
        P99_PFA = P99_ideal * (1 + sqrt_rho * p_squared**2)
        
        # Fator de proteção estocástica
        protection_factor = P99_ideal / P99_PFA if P99_PFA > 0 else 1.0
        
        # Entropia do relaxamento
        relaxation_data = [ideal_latency, P99_PFA, rho, randomness_factor]
        entropy = self._compute_entropy(relaxation_data)
        fractal_dim = self._fractal_dimension([P99_ideal, P99_PFA])
        
        telemetry = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "data_source": "fractal_engine.py (Eixo 4: Relaxamento Estocástico)",
            "metric_type": "stochastic_relaxation",
            "axis": "stochastic_relaxation",
            "ideal_latency": ideal_latency,
            "P99_PFA": P99_PFA,
            "rho": rho,
            "randomness_factor": randomness_factor,
            "protection_factor": protection_factor,
            "entropy": entropy,
            "fractal_dimension": fractal_dim,
            "confidence_score": 0.8
        }
        
        self.telemetry_log.append(telemetry)
        return telemetry

    # =========================================================================
    # MÉTODOS DE APOIO
    # =========================================================================
    
    def compute_fractal_entropy(self, data: List[float]) -> Tuple[float, float]:
        """Calcula entropia e dimensão fractal"""
        entropy = self._compute_entropy(data)
        fractal_dim = self._fractal_dimension(data)
        return entropy, fractal_dim
    
    def run_full_analysis(self, lambda_rate: float = 0.8, mu_rate: float = 1.0,
                          algebraic_obstruction: float = 0.3,
                          rho_values: List[float] = None,
                          p_values: List[float] = None,
                          group_order: int = 5,
                          abelian: bool = False,
                          ideal_latency: float = 10.0,
                          rho: float = 0.8,
                          randomness_factor: float = 0.5) -> Dict[str, Any]:
        """Executa análise completa dos 4 eixos"""
        
        if rho_values is None:
            rho_values = [0.7, 0.75, 0.8, 0.85]
        if p_values is None:
            p_values = [0.1, 0.15, 0.2, 0.25]
        
        results = {
            "metadata": {
                "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                "data_source": "fractal_engine.py (Análise Completa 4 Eixos)",
                "engine_version": "1.0",
                "parameters": {
                    "lambda_rate": lambda_rate,
                    "mu_rate": mu_rate,
                    "algebraic_obstruction": algebraic_obstruction,
                    "rho_values": rho_values,
                    "p_values": p_values,
                    "group_order": group_order,
                    "abelian": abelian,
                    "ideal_latency": ideal_latency,
                    "rho": rho,
                    "randomness_factor": randomness_factor
                }
            },
            "eixo_1_ponte_analitica": self.bridge_analitica(lambda_rate, mu_rate, algebraic_obstruction),
            "eixo_2_bullwhip": self.bullwhip_effect(rho_values, p_values),
            "eixo_3_nonabelian": self.nonabelian_expansion(group_order, abelian),
            "eixo_4_relaxamento": self.stochastic_relaxation(ideal_latency, rho, randomness_factor),
        }
        
        # Métricas agregadas
        all_entropies = [r.get("entropy", 0) for r in [results["eixo_1_ponte_analitica"], 
                                                        results["eixo_2_bullwhip"],
                                                        results["eixo_3_nonabelian"],
                                                        results["eixo_4_relaxamento"]]]
        all_fractal_dims = [r.get("fractal_dimension", 0) for r in [results["eixo_1_ponte_analitica"],
                                                                     results["eixo_2_bullwhip"],
                                                                     results["eixo_3_nonabelian"],
                                                                     results["eixo_4_relaxamento"]]]
        
        results["summary"] = {
            "mean_entropy": np.mean(all_entropies) if all_entropies else 0,
            "mean_fractal_dimension": np.mean(all_fractal_dims) if all_fractal_dims else 0,
            "total_telemetry_entries": len(self.telemetry_log),
            "engine_status": "completed"
        }
        
        return results

    def save_results(self, results: Dict, prefix: str = "fractal_engine"):
        """Salva resultados em JSON e CSV com linhagem"""
        with open(f"{prefix}.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, default=str)
        
        import csv
        if self.telemetry_log:
            with open(f"{prefix}_telemetry.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(self.telemetry_log[0].keys()))
                writer.writeheader()
                writer.writerows(self.telemetry_log)
        
        print(f"[Fractal Engine] Resultados salvos: {prefix}.json, {prefix}_telemetry.csv")
        return results

def main():
    print("=" * 70)
    print("FRACTAL ENGINE — Teoria de Controle Fractal (4 Eixos)")
    print("=" * 70)
    
    engine = FractalEngine()
    results = engine.run_full_analysis()
    engine.save_results(results, "fractal_engine_analysis")
    
    print("\n" + "=" * 70)
    print("RESUMO DA ANÁLISE FRACtal (4 EIXOS)")
    print("=" * 70)
    for axis, data in results.items():
        if axis != "metadata" and axis != "summary" and isinstance(data, dict):
            axis_name = data.get("axis", "unknown")
            entropy = data.get("entropy", 0)
            fractal_dim = data.get("fractal_dimension", 0)
            print(f"  {axis_name}: Entropy={entropy:.4f}, FractalDim={fractal_dim:.4f}")
    
    print(f"\n  Entropia Média: {results['summary']['mean_entropy']:.4f}")
    print(f"  Dimensão Fractal Média: {results['summary']['mean_fractal_dimension']:.4f}")
    print(f"  Status: {results['summary']['engine_status']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
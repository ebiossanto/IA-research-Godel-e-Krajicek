#!/usr/bin/env python3
"""
Algebraic Obstruction Model — Modelo de obstrução algébrica
Para análise de obstruções em sistemas complexos
"""

import json
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timezone

@dataclass
class ObstructionMetrics:
    obstruction_type: str
    severity: float
    algebraic_structure: str
    obstruction_value: float
    entropy: float
    confidence: float

class AlgebraicObstructionModel:
    """
    Modelo de obstrução algébrica para sistemas complexos
    Baseado em teoria de grupos, anéis e corpos
    """
    
    def __init__(self):
        self.obstructions_log = []
    
    def group_obstruction(self, group_order: int, abelian: bool = False) -> ObstructionMetrics:
        """
        Obstrução baseada em teoria de grupos
        Grupos não-abelianos têm obstrução 2x maior
        """
        n = group_order
        n_factorial = math.factorial(n)
        
        if abelian:
            obstruction_value = 1.0 / (n - 1) if n > 1 else float('inf')
            obstruction_type = "abelian_group"
            severity = 1.0 / n
            algebraic_structure = f"Z_{n} (abelian)"
        else:
            # Grupo não-abeliano S_n
            E_star = (math.factorial(n) - 2) / (math.factorial(n) * (n - 1)) if n > 1 else 0
            obstruction_value = E_star * 2  # 2x mais destrutivo
            obstruction_type = "nonabelian_group"
            severity = 2.0 / (n - 1) if n > 1 else float('inf')
            algebraic_structure = f"S_{n} (non-abelian)"
        
        entropy = -sum(p * math.log2(p) for p in [0.5, 0.5])
        
        metrics = ObstructionMetrics(
            obstruction_type=obstruction_type,
            severity=severity,
            algebraic_structure=algebraic_structure,
            obstruction_value=obstruction_value,
            entropy=0.5,
            confidence=0.8
        )
        
        return metrics
    
    def ring_obstruction(self, ring_char: int, ideal_size: int) -> Dict[str, Any]:
        """
        Obstrução em anéis (característica, ideais)
        """
        # Característica do anel
        char = ring_char
        ideal_idx = ideal_size
        
        # Obstrução baseada em característica
        if char == 0:
            obstruction = 0.0  # Característica zero - sem obstrução finita
        else:
            obstruction = 1.0 / char  # Inversamente proporcional à característica
        
        # Índice do ideal
        ideal_factor = ideal_idx / 100.0
        
        obstruction_value = obstruction + ideal_factor * 0.5
        
        return {
            "ring_characteristic": char,
            "ideal_index": ideal_idx,
            "obstruction_value": obstruction_value,
            "obstruction_type": "ring_obstruction",
            "severity": obstruction_value
        }
    
    def field_obstruction(self, field_order: int) -> Dict[str, Any]:
        """
        Obstrução em corpos finitos
        """
        # Ordem do corpo: p^n
        # Obstrução relacionada à estrutura do grupo multiplicativo
        if field_order < 2:
            return {"obstruction": float('inf'), "type": "trivial"}
        
        # Grupo multiplicativo é cíclico de ordem q-1
        mult_group_order = field_order - 1
        
        # Obstrução baseada na fatoração de q-1
        factors = self._prime_factors(mult_group_order)
        obstruction = sum(1/p for p in factors) / len(factors) if factors else 0
        
        return {
            "field_order": field_order,
            "multiplicative_group_order": mult_group_order,
            "prime_factors": factors,
            "obstruction_value": obstruction,
            "obstruction_type": "field_obstruction"
        }
    
    def _prime_factors(self, n: int) -> List[int]:
        """Fatoração prima"""
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    def module_obstruction(self, module_rank: int, ring_char: int) -> Dict[str, Any]:
        """
        Obstrução em módulos
        """
        # Obstrução relacionada à estrutura do módulo
        torsion = 1.0 / ring_char if ring_char > 0 else 1.0
        free_part = module_rank
        
        obstruction = torsion / (free_part + 1)
        
        return {
            "module_rank": module_rank,
            "ring_characteristic": ring_char,
            "torsion_component": torsion,
            "free_rank": free_part,
            "obstruction_value": obstruction,
            "type": "module_obstruction"
        }
    
    def composite_obstruction(self, structures: List[Dict]) -> Dict[str, Any]:
        """
        Obstrução composta de múltiplas estruturas algébricas
        """
        total_obstruction = 0.0
        components = []
        
        for struct in structures:
            struct_type = struct.get("type", "unknown")
            if struct_type == "group":
                m = self.group_obstruction(struct.get("order", 2), struct.get("abelian", False))
                components.append(m)
                total_obstruction += m.obstruction_value
            elif struct_type == "ring":
                r = self.ring_obstruction(struct.get("char", 2), struct.get("ideal", 1))
                components.append(r)
                total_obstruction += r["obstruction_value"]
            elif struct_type == "field":
                f = self.field_obstruction(struct.get("order", 2))
                components.append(f)
                total_obstruction += f.get("obstruction_value", 0)
            elif struct_type == "module":
                m = self.module_obstruction(struct.get("rank", 1), struct.get("char", 2))
                components.append(m)
                total_obstruction += m["obstruction_value"]
        
        avg_obstruction = total_obstruction / len(structures) if structures else 0
        
        return {
            "total_obstruction": total_obstruction,
            "average_obstruction": avg_obstruction,
            "components": components,
            "num_structures": len(structures)
        }
    
    def obstruction_entropy(self, obstruction_values: List[float]) -> float:
        """Entropia da distribuição de obstruções"""
        if not obstruction_values:
            return 0.0
        
        # Normaliza
        total = sum(obstruction_values)
        if total == 0:
            return 0.0
        
        probs = [v / total for v in obstruction_values]
        return -sum(p * math.log2(p) for p in probs if p > 0)

def main():
    print("=" * 70)
    print("ALGEBRAIC OBSTRUCTION MODEL — Modelo de Obstrução Algébrica")
    print("=" * 70)
    
    model = AlgebraicObstructionModel()
    
    # Teste grupo
    print("\n--- Obstrução em Grupos ---")
    for n in [3, 4, 5, 6]:
        abelian = model.group_obstruction(n, abelian=True)
        nonab = model.group_obstruction(n, abelian=False)
        print(f"  S_{n}: abeliano={abelian.obstruction_value:.4f}, "
              f"não-abeliano={nonab.obstruction_value:.4f}, "
              f"ratio={nonab.obstruction_value/abelian.obstruction_value:.1f}x")
    
    # Teste anel
    print("\n--- Obstrução em Anéis ---")
    for char in [2, 3, 5, 7, 0]:
        ring = model.ring_obstruction(char, 1)
        print(f"  Char={char}: obstruction={ring['obstruction_value']:.4f}")
    
    # Campo
    print("\n--- Obstrução em Corpos ---")
    for order in [4, 8, 9, 16, 25]:
        field = model.field_obstruction(order)
        print(f"  GF({order}): obstruction={field.get('obstruction_value', 0):.4f}, "
              f"fatores={field.get('prime_factors', [])}")
    
    # Composto
    print("\n--- Obstrução Composta ---")
    structures = [
        {"type": "group", "order": 5, "abelian": False},
        {"type": "ring", "char": 5, "ideal": 1},
        {"type": "field", "order": 9},
        {"type": "module", "rank": 3, "char": 3}
    ]
    composite = model.composite_obstruction(structures)
    print(f"  Total: {composite['total_obstruction']:.4f}")
    print(f"  Média: {composite['average_obstruction']:.4f}")
    print(f"  Componentes: {composite['num_structures']}")
    
    # Entropia
    obs_values = [0.2, 0.5, 0.8, 1.0, 0.3]
    entropy = model.obstruction_entropy(obs_values)
    print(f"\nEntropia das obstruções: {entropy:.4f}")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
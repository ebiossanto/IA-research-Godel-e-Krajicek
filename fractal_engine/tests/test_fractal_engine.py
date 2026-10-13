#!/usr/bin/env python3
"""
Testes do Fractal Engine — Terminal-Laboratório
"""

import unittest
import numpy as np
import sys
import os

# Adiciona path dos scripts
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'models'))

from fractal_engine import FractalEngine
from bridge_analitica import BridgeAnalitica
from bullwhip_engine import BullwhipEngine
from nonabelian_engine import NonabelianEngine
from stochastic_relaxation import StochasticRelaxationEngine
from fractal_entropy import FractalEntropyEngine
from models.fractal_queue_model import FractalQueueModel
from models.algebraic_obstruction import AlgebraicObstructionModel
from models.fractal_dimension import FractalDimensionModel

class TestFractalEngine(unittest.TestCase):
    """Testes do motor fractal principal"""
    
    def setUp(self):
        self.engine = FractalEngine()
    
    def test_bridge_analitica(self):
        """Testa Eixo 1: Ponte Analítica"""
        result = self.engine.bridge_analitica(0.8, 1.0, 0.3)
        self.assertIn('P99_actual', result)
        self.assertIn('entropy', result)
        self.assertGreater(result['entropy'], 0)
    
    def test_bullwhip_effect(self):
        """Testa Eixo 2: Efeito Bullwhip"""
        rho_values = [0.7, 0.75, 0.8, 0.85]
        p_values = [0.1, 0.15, 0.2, 0.25]
        result = self.engine.bullwhip_effect(rho_values, p_values, n_stages=4)
        self.assertIn('amplification_factor', result)
        self.assertGreater(result['amplification_factor'], 1.0)
    
    def test_nonabelian_expansion(self):
        """Testa Eixo 3: Expansões Não-Abelianas"""
        result = self.engine.nonabelian_expansion(5, abelian=False)
        self.assertIn('E_star', result)
        self.assertEqual(result['destruction_factor'], 2.0)
        self.assertFalse(result['abelian'])
    
    def test_stochastic_relaxation(self):
        """Testa Eixo 4: Relaxamento Estocástico"""
        result = self.engine.stochastic_relaxation(ideal_latency=10.0, rho=0.8, randomness_factor=0.5)
        self.assertIn('protection_factor', result)
        self.assertLess(result['protection_factor'], 1.0)
    
    def test_full_analysis(self):
        """Testa análise completa dos 4 eixos"""
        results = self.engine.run_full_analysis()
        self.assertIn('eixo_1_ponte_analitica', results)
        self.assertIn('eixo_2_bullwhip', results)
        self.assertIn('eixo_3_nonabelian', results)
        self.assertIn('eixo_4_relaxamento', results)
        self.assertIn('summary', results)

class TestBridgeAnalitica(unittest.TestCase):
    """Testes da Bridge Analítica"""
    
    def setUp(self):
        from bridge_analitica import BridgeAnalitica
        self.bridge = BridgeAnalitica()
    
    def test_bridge_basic(self):
        result = self.bridge.compute_bridge(0.8, 1.0, 0.3)
        self.assertIn('P99_actual', result)
        self.assertGreater(result['P99_actual'], result['P99_ideal'])
    
    def test_sensitivity(self):
        sensitivity = self.bridge.sensitivity_analysis(
            lambda_range=[0.5, 0.7, 0.8, 0.9],
            mu_range=[1.0],
            obstruction_range=[0.0, 0.5, 0.8]
        )
        self.assertIn('sensitivity_analysis', sensitivity)

class TestBullwhipEngine(unittest.TestCase):
    """Testes do Bullwhip Engine"""
    
    def setUp(self):
        from bullwhip_engine import BullwhipEngine
        self.engine = BullwhipEngine()
    
    def test_bullwhip_basic(self):
        rho_values = [0.7, 0.8, 0.9]
        p_values = [0.1, 0.2, 0.3]
        result = self.engine.compute_bullwhip(rho_values, p_values, n_stages=3)
        self.assertIn('amplification_factor', result)
        self.assertGreater(result['amplification_factor'], 1.0)
    
    def test_parameter_sweep(self):
        sweep = self.engine.parameter_sweep(
            rho_range=[0.7, 0.8, 0.9],
            p_range=[0.1, 0.2, 0.3]
        )
        self.assertEqual(sweep['total_combinations'], 9)

class TestNonabelianEngine(unittest.TestCase):
    """Testes do Nonabelian Engine"""
    
    def setUp(self):
        from nonabelian_engine import NonabelianEngine
        self.engine = NonabelianEngine()
    
    def test_nonabelian_basic(self):
        result = self.engine.compute_nonabelian(5, abelian=False)
        self.assertEqual(result['destruction_factor'], 2.0)
        self.assertFalse(result['abelian'])
        self.assertGreater(result['E_star'], 0)
    
    def test_abelian_vs_nonabelian(self):
        abelian = self.engine.compute_nonabelian(5, abelian=True)
        nonabelian = self.engine.compute_nonabelian(5, abelian=False)
        self.assertGreater(nonabelian['destruction_factor'], abelian['destruction_factor'])
    
    def test_symmetry_breaking(self):
        result = engine.symmetry_breaking_analysis([3, 4, 5])
        self.assertIn('symmetry_breaking', result)

class TestStochasticRelaxation(unittest.TestCase):
    """Testes do Stochastic Relaxation Engine"""
    
    def setUp(self):
        from stochastic_relaxation import StochasticRelaxationEngine
        self.engine = StochasticRelaxationEngine()
    
    def test_relaxation_basic(self):
        result = engine.compute_relaxation(ideal_latency=10.0, rho=0.8, randomness_factor=0.5)
        self.assertIn('protection_factor', result)
        self.assertLess(result['protection_factor'], 1.0)
        self.assertGreater(result['entropy'], 0)
    
    def test_monte_carlo(self):
        mc = engine.monte_carlo_simulation(n_samples=100, rho=0.8)
        self.assertEqual(mc['n_samples'], 100)
        self.assertGreater(mc['avg_protection_factor'], 0)

class TestFractalEntropy(unittest.TestCase):
    """Testes do Fractal Entropy Engine"""
    
    def setUp(self):
        from fractal_entropy import FractalEntropyEngine
        self.engine = FractalEntropyEngine()
    
    def test_shannon_entropy(self):
        data = [1, 2, 2, 3, 3, 3]
        entropy = self.engine.shannon_entropy_discrete(data)
        self.assertGreater(entropy, 0)
    
    def test_renyi_entropy(self):
        data = [1, 1, 2, 2, 3, 3]
        entropy = self.engine.renyi_entropy(data, alpha=2)
        self.assertGreater(entropy, 0)
    
    def test_fractal_dimension(self):
        # Random walk data
        data = np.cumsum(np.random.normal(0, 1, 1000))
        dim = self.engine.box_counting_dimension(data)
        self.assertGreater(dim, 0)
        self.assertLess(dim, 2)

class TestFractalQueueModel(unittest.TestCase):
    """Testes do Fractal Queue Model"""
    
    def setUp(self):
        from models.fractal_queue_model import FractalQueueModel
        self.model = FractalQueueModel()
    
    def test_steady_state(self):
        metrics = model.compute_steady_state(0.8, 1.0)
        self.assertEqual(metrics.lambda_rate, 0.8)
        self.assertEqual(metrics.mu_rate, 1.0)
        self.assertEqual(metrics.rho, 0.8)
        self.assertLess(metrics.P99_actual, float('inf'))
    
    def test_transient(self):
        trans = model.compute_transient(0.8, 1.0, 1.0)
        self.assertIn('L_t', trans)
        self.assertIn('W_t', trans)

class TestAlgebraicObstruction(unittest.TestCase):
    """Testes do Algebraic Obstruction Model"""
    
    def setUp(self):
        from models.algebraic_obstruction import AlgebraicObstructionModel
        self.model = AlgebraicObstructionModel()
    
    def test_group_obstruction(self):
        abelian = model.group_obstruction(5, abelian=True)
        nonab = model.group_obstruction(5, abelian=False)
        self.assertEqual(abelian.obstruction_value, nonab.obstruction_value / 2)
    
    def test_composite(self):
        structures = [
            {"type": "group", "order": 5, "abelian": False},
            {"type": "ring", "char": 5, "ideal": 1}
        ]
        result = model.composite_obstruction(structures)
        self.assertIn('total_obstruction', result)

class TestFractalDimension(unittest.TestCase):
    """Testes do Fractal Dimension Model"""
    
    def setUp(self):
        from models.fractal_dimension import FractalDimensionModel
        self.model = FractalDimensionModel()
    
    def test_box_counting(self):
        # Random walk data
        data = np.cumsum(np.random.normal(0, 1, 1000))
        dim = model.box_counting_dimension(data)
        self.assertGreater(dim, 0)
        self.assertLess(dim, 2)
    
    def test_correlation_dimension(self):
        data = np.cumsum(np.random.normal(0, 1, 500))
        dim = model.correlation_dimension(data)
        self.assertGreater(dim, 0)

class TestFractalQueueModel(unittest.TestCase):
    """Testes do Fractal Queue Model"""
    
    def setUp(self):
        from models.fractal_queue_model import FractalQueueModel
        self.model = FractalQueueModel()
    
    def test_steady_state(self):
        metrics = model.compute_steady_state(0.8, 1.0)
        self.assertEqual(metrics.rho, 0.8)
        self.assertLess(metrics.P99_actual, float('inf'))

class TestFractalDimensionModel(unittest.TestCase):
    """Testes do Fractal Dimension Model"""
    
    def setUp(self):
        from models.fractal_dimension import FractalDimensionModel
        self.model = FractalDimensionModel()
    
    def test_box_counting(self):
        data = np.cumsum(np.random.normal(0, 1, 1000))
        dim = model.box_counting_dimension(data)
        self.assertGreater(dim, 0)
        self.assertLess(dim, 2)

if __name__ == '__main__':
    unittest.main()
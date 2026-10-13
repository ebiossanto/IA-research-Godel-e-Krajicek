#!/usr/bin/env python3
"""
Fractal Engine Runner — Script principal para executar o motor fractal
Terminal-Laboratório
"""

import sys
import os
import argparse

# Adiciona paths
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'integrations', 'fractal_engine', 'scripts'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'integrations', 'fractal_engine', 'models'))

def run_fractal_engine():
    """Executa motor fractal completo"""
    from scripts.fractal_engine import FractalEngine
    
    engine = FractalEngine()
    results = engine.run_full_analysis()
    engine.save_results(results, "fractal_engine_analysis")
    print("Fractal Engine executado com sucesso!")
    return True

def run_bridge_analitica():
    """Executa bridge analítica"""
    from bridge_analitica import BridgeAnalitica
    bridge = BridgeAnalitica()
    result = bridge.compute_bridge(0.8, 1.0, 0.3)
    print(f"Bridge Analítica: P99={result['P99_actual']:.3f}, Entropy={result['entropy']:.4f}")
    return True

def run_bullwhip():
    from bullwhip_engine import BullwhipEngine
    engine = BullwhipEngine()
    rho_values = [0.7, 0.75, 0.8, 0.85]
    p_values = [0.1, 0.15, 0.2, 0.25]
    result = engine.compute_bullwhip(rho_values, p_values, n_stages=4)
    print(f"Bullwhip: amplification={result['amplification_factor']:.2f}")
    return True

def run_nonabelian():
    from nonabelian_engine import NonabelianEngine
    engine = NonabelianEngine()
    result = engine.compute_nonabelian(5, abelian=False)
    print(f"Nonabelian: E*={result['E_star']:.6f}, destruction={result['destruction_factor']}")
    return True

def run_stochastic():
    from stochastic_relaxation import StochasticRelaxationEngine
    engine = StochasticRelaxationEngine()
    result = engine.compute_relaxation(ideal_latency=10.0, rho=0.8, randomness_factor=0.5)
    print(f"Stochastic: protection={result['protection_factor']:.4f}")
    return True

def run_fractal_entropy():
    from fractal_entropy import FractalEntropyEngine
    engine = FractalEntropyEngine()
    data = np.cumsum(np.random.normal(0, 1, 1000))
    results = engine.full_entropy_analysis(data)
    print(f"Entropy: {results['shannon_entropy']:.4f}, Dim={results['box_counting_dim']:.4f}")
    return True

def run_all():
    """Executa todos os experimentos"""
    print("=" * 70)
    print("EXECUTANDO TODOS OS EXPERIMENTOS DO FRACTAL ENGINE")
    print("=" * 70)
    
    tests = [
        ("Bridge Analítica", run_bridge_analitica),
        ("Bullwhip Engine", run_bullwhip),
        ("Nonabelian Engine", run_nonabelian),
        ("Stochastic Relaxation", run_stochastic),
        ("Fractal Entropy", run_fractal_entropy),
    ]
    
    results = {}
    for name, func in tests:
        try:
            print(f"\n--- Executando {name} ---")
            result = func()
            results[name] = "PASS" if result else "FAIL"
        except Exception as e:
            results[name] = f"ERROR: {e}"
            print(f"  ERRO: {e}")
    
    print("\n" + "=" * 70)
    print("RESUMO DOS TESTES")
    print("=" * 70)
    for name, status in results.items():
        print(f"  {name}: {status}")
    
    return all(status == "PASS" for status in results.values())

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "all":
            success = run_all()
            sys.exit(0 if success else 1)
        elif command == "bridge":
            run_bridge_analitica()
        elif command == "bullwhip":
            run_bullwhip()
        elif command == "nonabelian":
            run_nonabelian()
        elif command == "stochastic":
            run_stochastic()
        elif command == "entropy":
            run_fractal_entropy()
        else:
            print(f"Comando desconhecido: {command}")
            print("Comandos disponíveis: all, bridge, bullwhip, nonabelian, stochastic, entropy")
            sys.exit(1)
    else:
        # Default: roda tudo
        success = run_all()
        sys.exit(0 if success else 1)
#!/usr/bin/env python3
"""
REA Bridge Fractal — Integração do Motor Fractal com REA Bridge
Pipeline Event-Driven para análise fractal em tempo real
"""

import json
import time
import threading
import queue
import psutil
import os
import math
import hashlib
from typing import List, Dict, List, Tuple, Optional, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from collections import deque
from itertools import product

@dataclass
class FractalREAEvent:
    timestamp_utc: str
    data_source: str
    event_type: str
    axis: str
    lambda_rate: float
    mu_rate: float
    rho: float
    algebraic_obstruction: float
    P99_ideal: float
    P99_actual: float
    entropy: float
    fractal_dimension: float
    amplification_factor: float
    entropy_cpu: float
    cpu_percent: float
    memory_mb: float
    details: str

class FractalREABridge:
    """
    Integração do Motor Fractal com REA Bridge
    Monitora eventos REA e executa análise fractal correspondente
    """
    
    def __init__(self, phi_len: int = 12, r_w: int = 4, w_star: str = "00"):
        self.phi_len = phi_len
        self.r_w = r_w
        self.w_star = w_star
        
        # Importa engines dos eixos
        from scripts.bridge_analitica import BridgeAnalitica
        from scripts.bullwhip_engine import BullwhipEngine
        from scripts.nonabelian_engine import NonabelianEngine
        from scripts.stochastic_relaxation import StochasticRelaxationEngine
        from scripts.fractal_entropy import FractalEntropyEngine
        
        self.bridge_analitica = BridgeAnalitica()
        self.bullwhip_engine = BullwhipEngine()
        self.nonabelian_engine = NonabelianEngine()
        self.stochastic_engine = StochasticRelaxationEngine()
        self.entropy_engine = FractalEntropyEngine()
        
        # Estado do monitor
        self.running = False
        self.event_queue = queue.Queue()
        self.theories = {}
        self.active_R = {
            "suffix0": lambda s: s + '0',
            "suffix00": lambda s: s + '00',
            "id": lambda s: s,
        }
        
        # Named Pipe
        self.pipe_path = r"\\.\pipe\fractal_telemetry_pipe"
        
        # Histórico de CPU/entropia
        self.cpu_history = deque(maxlen=200)
        self.entropy_history = deque(maxlen=100)
    
    def register_theory(self, name: str, sigma: int, is_T1: bool, ordinal: str = ""):
        """Registra uma teoria no monitor"""
        self.theories[name] = {
            "sigma": sigma,
            "is_T1": is_T1,
            "ordinal": ordinal
        }
    
    def _send_to_pipe(self, event_type: str, payload: Dict):
        """Envia evento para REA Bridge via Named Pipe"""
        try:
            import win32pipe, win32file
            pipe_path = r"\\.\pipe\fractal_telemetry_pipe"
            message = f"{event_type},{json.dumps(payload)}"
            
            handle = win32file.CreateFile(
                pipe_path, win32file.GENERIC_WRITE, 0, None,
                win32file.OPEN_EXISTING, 0, None
            )
            win32file.WriteFile(handle, message.encode())
            win32file.CloseHandle(handle)
            return True
        except Exception as e:
            return False
    
    def emit_event(self, event: 'FractalREAEvent'):
        """Emite evento para queue e pipe"""
        self.event_queue.put(event)
        
        # Envia para pipe
        pipe_payload = {
            "event_type": event.event_type,
            "severity": event.severity,
            "theory_src": event.theory_src,
            "theory_tgt": event.theory_tgt,
            "axis": event.axis,
            "b": event.b,
            "n": event.n,
            "R_name": event.R_name,
            "violations": event.violations,
            "delta_src": event.delta_src,
            "delta_tgt": event.delta_tgt,
            "entropy_cpu": event.entropy_cpu,
            "details": event.details
        }
        self._send_to_pipe(event.event_type, pipe_payload)
    
    def check_ppr_pair(self, src: str, tgt: str, n: int, b: int, R_name: str, R_fn: Callable) -> Tuple[bool, int]:
        """Testa PPR-2 para par de teorias"""
        if n < self.phi_len:
            return True, 0
        
        u0_len = n - self.phi_len
        phi_prefix = "PA_CONENCOD"[:self.phi_len].ljust(self.phi_len, '0')
        
        img_src, img_tgt = set(), set()
        for bits in product('01', repeat=u0_len):
            u = phi_prefix + ''.join(bits)
            img_src.add(self.generator(self.theories[src]["sigma"], u, lambda x: max(12, min(x, 16)), b))
            img_tgt.add(self.generator(self.theories[tgt]["sigma"], u, lambda x: max(12, min(x, 16)), b))
        
        all_out = {''.join(p) for p in product('01', repeat=n+1)}
        comp_src = all_out - img_src
        
        violations = 0
        for b_out in comp_src:
            r_out = R_fn(b_out)
            if r_out in img_tgt:
                violations += 1
        
        return violations == 0, violations
    
    def generator(self, sigma: int, u: str, a: callable, b: int, is_T1: bool) -> str:
        n = len(u)
        if n < self.phi_len or self.phi_len > a(n):
            return '0' * (n + 1)
        w0 = self.first_uncovered(sigma, b, is_T1)
        if w0 is None:
            return '0' * (n + 1)
        return w0 + u[self.phi_len:]
    
    def first_uncovered(self, sigma: int, b: int, is_T1: bool) -> Optional[str]:
        for o in sorted(self.obligations, key=lambda x: x["idx"]):
            if not self.covered(sigma, b, o, is_T1):
                return o["idx"]
        return None
    
    def covered(self, sigma: int, b: int, o: Dict, is_T1: bool) -> bool:
        return self.proof_complexity(sigma, o, is_T1) <= b
    
    def proof_complexity(self, sigma: int, o: Dict, is_T1: bool) -> int:
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
    
    def covered(self, sigma: int, b: int, o: Dict, is_T1: bool) -> bool:
        return self.proof_complexity(sigma, o, is_T1) <= b
    
    def proof_complexity(self, sigma: int, o: Dict, is_T1: bool) -> int:
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
    
    def _build_obligations(self):
        obligations = []
        for bits in product('01', repeat=4):
            w = ''.join(bits)
            is_wstar = w.startswith(self.w_star)
            kappa = 2 if is_wstar else (sum(ord(c) for c in w) % 2)
            obligations.append({"idx": w, "is_wstar": is_wstar, "kappa": kappa})
        return obligations
    
    def emit_event(self, event_type: str, severity: str, 
                   theory_src: str, theory_tgt: str, ordinal_src: str, ordinal_tgt: str,
                   b: int, n: int, R_name: str, violations: int,
                   delta_src: int, delta_tgt: int, entropy_cpu: float, details: str):
        """Emite evento PPR para REA Bridge"""
        
        event = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "data_source": "rea_bridge_fractal.py",
            "event_type": event_type,
            "severity": severity,
            "theory_src": theory_src,
            "theory_tgt": theory_tgt,
            "ordinal_src": ordinal_src,
            "ordinal_tgt": ordinal_tgt,
            "b": b,
            "n": n,
            "R_name": R_name,
            "violations": violations,
            "delta_src": delta_src,
            "delta_tgt": delta_tgt,
            "entropy_cpu": entropy_cpu,
            "cpu_percent": psutil.cpu_percent(interval=None),
            "memory_mb": psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
            "details": details
        }
        
        self._send_to_pipe(event_type, payload)
        self.event_queue.put(payload)
    
    def monitor_loop(self, interval: float = 2.0):
        """Loop principal de monitoramento"""
        self.running = True
        
        # Registra teorias padrão
        self.register_theory("PA", 0, False, "0")
        self.register_theory("PA+RFN_1", 1, True, "1")
        self.register_theory("PA+RFN_2", 2, True, "2")
        self.register_theory("PA+RFN_3", 3, True, "3")
        self.register_theory("PA+RFN^omega", 100, True, "omega")
        
        theory_pairs = [
            ("PA", "PA+RFN_1"),
            ("PA+RFN_1", "PA+RFN_2"),
            ("PA+RFN_2", "PA+RFN_3"),
            ("PA+RFN_3", "PA+RFN^omega"),
        ]
        
        b_values = [4, 8, 12, 16, 20, 24, 32, 48, 64, 128, 256]
        n_values = [12, 14, 16]
        R_functions = {
            "suffix0": lambda s: s + '0',
            "suffix00": lambda s: s + '00',
            "id": lambda s: s,
        }
        
        print("[Fractal REA Bridge] Monitoramento iniciado...")
        print(f"[Fractal REA Bridge] Pipe: \\\\.\\pipe\\fractal_telemetry_pipe")
        print(f"[Fractal REA Bridge] Teorias registradas: {list(self.theories.keys())}")
        
        prev_deltas = {}
        
        while self.running:
            # 1. Coleta métricas de sistema
            cpu = psutil.cpu_percent(interval=None)
            self.cpu_history.append(cpu)
            entropy_cpu = self._compute_entropy(list(self.cpu_history)[-50:])
            
            # 2. Verifica PPR para cada par
            for src, tgt in [("PA", "PA+RFN_1"), ("PA+RFN_1", "PA+RFN_2"), 
                             ("PA+RFN_2", "PA+RFN_3"), ("PA+RFN_3", "PA+RFN^omega")]:
                for n in n_values:
                    for b in b_values:
                        for R_name, R_fn in [("suffix0", lambda s: s + '0'), 
                                              ("suffix00", lambda s: s + '00'),
                                              ("id", lambda s: s)]:
                            passed, violations = self.check_ppr_pair(
                                src, tgt, n, b, R_name, R_fn
                            )
                            
                            delta_src = self._compute_delta(src, b)
                            delta_tgt = self._compute_delta(tgt, b)
                            
                            if not passed:
                                self.emit_event(
                                    event_type="PPR_FAIL",
                                    severity="CRITICAL",
                                    theory_src=src,
                                    theory_tgt=tgt,
                                    ordinal_src=self.theories[src]["ordinal"],
                                    ordinal_tgt=self.theories[tgt]["ordinal"],
                                    b=b, n=n,
                                    R_name=R_name,
                                    violations=violations,
                                    delta_src=self._compute_delta(src, b),
                                    delta_tgt=self._compute_delta(tgt, b),
                                    entropy_cpu=entropy_cpu,
                                    details=f"PPR-2 FALHOU: {src}->{tgt} via {R_name} n={n} b={b}, violations={violations}"
                                )
                            elif self._check_rbt(src, tgt, b):
                                self.emit_event(
                                    event_type="RBT_DETECTED",
                                    severity="WARNING",
                                    theory_src=src,
                                    theory_tgt=tgt,
                                    ordinal_src=self.theories[src]["ordinal"],
                                    ordinal_tgt=self.theories[tgt]["ordinal"],
                                    b=b, n=n,
                                    R_name="",
                                    violations=0,
                                    delta_src=delta_src,
                                    delta_tgt=delta_tgt,
                                    entropy_cpu=entropy_cpu,
                                    details=f"RBT detectado: delta mudou {delta_src} -> {delta_tgt}"
                                )
        
            # 3. Verifica convergência delta
            for theory_name, theory in self.theories.items():
                delta = self._compute_delta(theory_name, 64)
                if theory_name in prev_deltas:
                    if delta != prev_deltas[theory_name]:
                        self.emit_event(
                            event_type="DELTA_CONVERGED",
                            severity="INFO",
                            theory_src=theory_name,
                            theory_tgt="",
                            ordinal_src=theories[theory_name]["ordinal"],
                            ordinal_tgt="",
                            b=64, n=0,
                            R_name="", violations=0,
                            delta_src=prev_deltas[theory_name],
                            delta_tgt=delta,
                            entropy_cpu=entropy_cpu,
                            details=f"Delta convergiu: {prev_deltas[theory_name]} -> {delta}"
                        )
                prev_deltas[theory_name] = delta
            
            # 3. Verifica convergência omega
            omega_delta = self._compute_delta("PA+RFN^omega", 64)
            if omega_delta == 0:
                self.emit_event(
                    event_type="OMEGA_CONVERGED",
                    severity="INFO",
                    theory_src="PA+RFN^omega",
                    theory_tgt="",
                    ordinal_src="omega",
                    ordinal_tgt="",
                    b=64, n=0,
                    R_name="", violations=0,
                    delta_src=0, delta_tgt=0,
                    entropy_cpu=entropy_cpu,
                    details="T_omega atingiu delta=0 (ALL_COV)"
                )
            
            # 4. Detecta spike de entropia CPU
            if len(self.entropy_history) >= 10:
                entropy_cpu = self._compute_entropy(list(self.cpu_history)[-50:])
                self.entropy_history.append(entropy_cpu)
                
                if len(self.entropy_history) >= 5:
                    baseline = np.mean(list(self.entropy_history)[-10:-1])
                    if entropy_cpu > baseline * 2:
                        self.emit_event(
                            event_type="ENTROPY_SPIKE",
                            severity="WARNING",
                            theory_src="SYSTEM",
                            theory_tgt="CPU",
                            ordinal_src="system",
                            ordinal_tgt="system",
                            b=0, n=0,
                            R_name="", violations=0,
                            delta_src=0, delta_tgt=0,
                            entropy_cpu=entropy_cpu,
                            details=f"Spike de entropia CPU: {entropy_cpu:.3f} (baseline={baseline:.3f})"
                        )
            
            time.sleep(interval)
    
    def _compute_delta(self, theory_name: str, b: int) -> int:
        theory = self.theories[theory_name]
        budget = 32 if theory["sigma"] == 0 else 64
        # Simplificado: usa first_uncovered do generator
        return 0  # Placeholder
    
    def _check_rbt(self, src: str, tgt: str, b: int) -> bool:
        """Detecta RBT: mudança de w0 entre teorias"""
        # Simplificado
        return False
    
    def _compute_entropy(self, data: List[float]) -> float:
        if not data:
            return 0.0
        discretized = [round(d/5)*5 for d in data]
        from collections import Counter
        counts = Counter(discretized)
        total = len(discretized)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())
    
    def start(self):
        """Inicia monitoramento em thread separada"""
        t = threading.Thread(target=self.monitor_loop, daemon=True)
        t.start()
        return t
    
    def stop(self):
        self.running = False
    
    def get_events(self, timeout: float = 1.0) -> List[Dict]:
        """Recupera eventos da queue"""
        events = []
        try:
            while True:
                events.append(self.event_queue.get(timeout=timeout))
        except queue.Empty:
            pass
        return events

def main():
    print("=" * 70)
    print("REA BRIDGE FRACTAL — Monitoramento Tempo Real Fractal")
    print("=" * 70)
    
    bridge = FractalREABridge()
    thread = bridge.start()
    
    print("[Fractal REA Bridge] Monitoramento iniciado...")
    print("[Fractal REA Bridge] Eventos serão enviados para Named Pipe: \\\\.\\pipe\\fractal_telemetry_pipe")
    print("[Fractal REA Bridge] Pressione Ctrl+C para parar")
    
    try:
        while True:
            events = bridge.get_events(timeout=5.0)
            for event in events:
                out = f"[{event['event_type']}] {event['details']}"
                print(out.encode('ascii', 'ignore').decode('ascii'))
            time.sleep(2)
    except KeyboardInterrupt:
        bridge.stop()
        print("\n[Fractal REA Bridge] Parado pelo usuário")

if __name__ == "__main__":
    main()
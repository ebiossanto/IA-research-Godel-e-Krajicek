#!/usr/bin/env python3
"""
PPR MONITOR — Monitor contínuo de eventos PPR via REA Bridge.
Detecta em tempo real:
  - RBT (Reflection Branch Transition)
  - PPR_PASS / PPR_FAIL (teste de candidatos R_w)
  - PHASE_TRANSITION (mudança de regime σ)
  - ENTROPY_SPIKE (pico de entropia = possível mudança de fase)

Integra com Terminal-Laboratório via Named Pipe.
"""

import json
import time
import math
import threading
import queue
import psutil
import hashlib
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Callable
from datetime import datetime, timezone
from collections import deque
import os

@dataclass
class PPREvent:
    timestamp_utc: str
    data_source: str
    event_type: str  # RBT, PPR_PASS, PPR_FAIL, PHASE_TRANSITION, ENTROPY_SPIKE
    severity: str    # INFO, WARNING, CRITICAL
    theory_src: str
    theory_tgt: str
    sigma_src: int
    sigma_tgt: int
    b: int
    n: int
    w0_src: str
    w0_tgt: str
    R_name: str
    violations: int
    delta_src: int
    delta_tgt: int
    entropy_cpu: float
    entropy_delta: float
    cpu_percent: float
    memory_mb: float
    details: str

class PPRMonitor:
    def __init__(self, phi_len: int = 12, r_w: int = 4, w_star: str = "00"):
        self.phi_len = phi_len
        self.r_w = r_w
        self.w_star = w_star
        
        # Estado do monitor
        self.running = False
        self.event_queue = queue.Queue()
        self.theories = {}
        self.prev_deltas = {}
        self.prev_w0s = {}
        self.entropy_history = deque(maxlen=100)
        self.cpu_history = deque(maxlen=200)
        
        # Configuração de alertas
        self.entropy_threshold = 0.5  # spike threshold
        self.entropy_baseline = None
        
        # R_w candidates ativos
        self.active_R = {
            "suffix0": lambda s: s + '0',
            "suffix00": lambda s: s + '00',
            "prefix0": lambda s: '0' + s[:len(s)-1],
        }
        
    def compute_entropy(self, data: List[float]) -> float:
        if not data:
            return 0.0
        discretized = [round(d/5)*5 for d in data]
        from collections import Counter
        counts = Counter(discretized)
        total = len(discretized)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())
    
    def register_theory(self, name: str, sigma: int, is_T1: bool):
        """Registra uma teoria no monitor"""
        self.theories[name] = {"sigma": sigma, "is_T1": is_T1}
        self.prev_deltas[name] = {}
        self.prev_w0s[name] = {}
    
    def proof_complexity(self, sigma: int, o_idx: str, is_wstar: bool, is_T1: bool) -> int:
        INF = 10**9
        if is_T1:
            if is_wstar:
                return 20
            h = sum(ord(c) for c in o_idx)
            return 8 + (h % 17)
        else:
            if is_wstar:
                return INF
            h = sum(ord(c) for c in o_idx)
            return 8 + (h % 17)
    
    def covered(self, sigma: int, b: int, o_idx: str, is_wstar: bool, is_T1: bool) -> bool:
        return self.proof_complexity(sigma, o_idx, is_wstar, is_T1) <= b
    
    def delta(self, theory_name: str, b: int) -> int:
        """Calcula δ para uma teoria em budget b"""
        T = self.theories[theory_name]
        obligations = []
        for bits in product('01', repeat=4):
            w = ''.join(bits)
            is_wstar = w.startswith(self.w_star)
            obligations.append((w, is_wstar))
        
        trues = obligations  # todas true
        cov = [(w, ws) for w, ws in trues if self.covered(T["sigma"], b, w, ws, T["is_T1"])]
        return len(trues) - len(cov)
    
    def first_uncovered(self, theory_name: str, b: int) -> Optional[str]:
        T = self.theories[theory_name]
        for bits in product('01', repeat=4):
            w = ''.join(bits)
            is_wstar = w.startswith(self.w_star)
            if not self.covered(T["sigma"], b, w, is_wstar, T["is_T1"]):
                return w
        return None
    
    def check_rbt(self, theory_src: str, theory_tgt: str, b: int) -> bool:
        """Verifica RBT: w0 muda entre teorias"""
        w0_src = self.first_uncovered(theory_src, b) or "ALL_COV"
        w0_tgt = self.first_uncovered(theory_tgt, b) or "ALL_COV"
        
        prev_src = self.prev_w0s[theory_src].get(b)
        prev_tgt = self.prev_w0s[theory_tgt].get(b)
        
        # RBT se w0 mudou entre teorias OU mudou em relação ao anterior
        rbt = (w0_src != w0_tgt) or \
              (prev_src is not None and w0_src != prev_src) or \
              (prev_tgt is not None and w0_tgt != prev_tgt)
        
        if rbt:
            self.prev_w0s[theory_src][b] = w0_src
            self.prev_w0s[theory_tgt][b] = w0_tgt
        
        return rbt, w0_src, w0_tgt
    
    def check_ppr(self, theory_src: str, theory_tgt: str, n: int, b: int, R_name: str, R_fn: Callable) -> Tuple[bool, int]:
        """Testa PPR-2 para um par de teorias"""
        T_src = self.theories[theory_src]
        T_tgt = self.theories[theory_tgt]
        
        if n < self.phi_len:
            return True, 0
        
        u0_len = n - self.phi_len
        phi_prefix = "PA_CONENCOD"[:self.phi_len].ljust(self.phi_len, '0')
        
        img_src, img_tgt = set(), set()
        for bits in product('01', repeat=u0_len):
            u = phi_prefix + ''.join(bits)
            img_src.add(self.generator(T_src["sigma"], u, lambda x: max(12, min(x, 16)), b, T_src["is_T1"]))
            img_tgt.add(self.generator(T_tgt["sigma"], u, lambda x: max(12, min(x, 16)), b, T_tgt["is_T1"]))
        
        all_out = {''.join(p) for p in product('01', repeat=n+1)}
        comp_src = all_out - img_src
        
        violations = 0
        for b_out in comp_src:
            r_out = R_fn(b_out)
            if r_out in img_tgt:
                violations += 1
        
        return violations == 0, violations
    
    def generator(self, sigma: int, u: str, a: Callable[[int], int], b: int, is_T1: bool) -> str:
        n = len(u)
        if n < self.phi_len or self.phi_len > a(n):
            return '0' * (n + 1)
        w0 = self.first_uncovered_sigma(sigma, b, is_T1)
        if w0 is None:
            return '0' * (n + 1)
        return w0 + u[self.phi_len:]
    
    def first_uncovered_sigma(self, sigma: int, b: int, is_T1: bool) -> Optional[str]:
        for bits in product('01', repeat=4):
            w = ''.join(bits)
            is_wstar = w.startswith(self.w_star)
            if not self.covered(sigma, b, w, is_wstar, is_T1):
                return w
        return None
    
    def emit_event(self, event: PPREvent):
        """Emite evento para queue e para REA Bridge (Named Pipe)"""
        self.event_queue.put(event)
        
        # Tenta enviar para REA Bridge via Named Pipe
        self._send_to_rea_bridge(event)
    
    def _send_to_rea_bridge(self, event: PPREvent):
        """Envia evento para REA Bridge via Named Pipe Windows"""
        try:
            import win32pipe, win32file
            pipe_path = r"\\.\pipe\rea_telemetry_pipe"
            message = f"{event.event_type},{json.dumps(asdict(event))}"
            
            handle = win32file.CreateFile(
                pipe_path, win32file.GENERIC_WRITE, 0, None,
                win32file.OPEN_EXISTING, 0, None
            )
            win32file.WriteFile(handle, message.encode())
            win32file.CloseHandle(handle)
        except:
            pass  # Bridge não está rodando
    
    def monitor_loop(self, interval: float = 1.0):
        """Loop principal de monitoramento"""
        self.running = True
        
        # Registra teorias padrão
        self.register_theory("PA", 0, False)
        self.register_theory("PA+RFN_1", 1, True)
        self.register_theory("PA+RFN_2", 2, True)
        self.register_theory("PA+RFN_3", 3, True)
        
        b_values = [4, 8, 12, 16, 20, 24, 32, 48, 64]
        n_values = [12, 14, 16]
        theory_pairs = [("PA", "PA+RFN_1"), ("PA+RFN_1", "PA+RFN_2"), ("PA+RFN_2", "PA+RFN_3")]
        
        print("[PPR Monitor] Iniciando monitoramento contínuo...")
        print(f"[PPR Monitor] Teorias: {list(self.theories.keys())}")
        print(f"[PPR Monitor] Intervalos: {interval}s")
        
        while self.running:
            # 1. Coleta métricas de sistema
            cpu = psutil.cpu_percent(interval=None)
            self.cpu_history.append(cpu)
            entropy_cpu = self.compute_entropy(list(self.cpu_history)[-50:])
            self.entropy_history.append(entropy_cpu)
            
            # Baseline de entropia
            if self.entropy_baseline is None and len(self.entropy_history) >= 10:
                self.entropy_baseline = np.mean(list(self.entropy_history)[-10:])
            
            # 2. Verifica RBT em todos os pares
            for src, tgt in theory_pairs:
                for b in b_values:
                    rbt, w0_src, w0_tgt = self.check_rbt(src, tgt, b)
                    if rbt:
                        delta_src = self.delta(src, b)
                        delta_tgt = self.delta(tgt, b)
                        
                        event = PPREvent(
                            timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                            data_source="gk_ppr_monitor.py (PPR Monitor)",
                            event_type="RBT",
                            severity="WARNING",
                            theory_src=src, theory_tgt=tgt,
                            sigma_src=self.theories[src]["sigma"],
                            sigma_tgt=self.theories[tgt]["sigma"],
                            b=b, n=0,
                            w0_src=w0_src, w0_tgt=w0_tgt,
                            R_name="", violations=0,
                            delta_src=delta_src, delta_tgt=delta_tgt,
                            entropy_cpu=entropy_cpu,
                            entropy_delta=0.0,
                            cpu_percent=cpu,
                            memory_mb=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
                            details=f"RBT detectado: w0({src})={w0_src} ≠ w0({tgt})={w0_tgt} em b={b}"
                        )
                        self.emit_event(event)
            
            # 3. Verifica PPR para candidatos R ativos
            for src, tgt in theory_pairs:
                for n in n_values:
                    for b in b_values:
                        for R_name, R_fn in self.active_R.items():
                            passed, violations = self.check_ppr(src, tgt, n, b, R_name, R_fn)
                            
                            if not passed:
                                event = PPREvent(
                                    timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                                    data_source="gk_ppr_monitor.py (PPR Monitor)",
                                    event_type="PPR_FAIL",
                                    severity="CRITICAL",
                                    theory_src=src, theory_tgt=tgt,
                                    sigma_src=self.theories[src]["sigma"],
                                    sigma_tgt=self.theories[tgt]["sigma"],
                                    b=b, n=n,
                                    w0_src="", w0_tgt="",
                                    R_name=R_name, violations=violations,
                                    delta_src=self.delta(src, b),
                                    delta_tgt=self.delta(tgt, b),
                                    entropy_cpu=entropy_cpu,
                                    entropy_delta=0.0,
                                    cpu_percent=cpu,
                                    memory_mb=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
                                    details=f"PPR-2 FALHOU: {src}→{tgt} via {R_name} em n={n}, b={b}, violations={violations}"
                                )
                                self.emit_event(event)
            
            # 4. Detecta spike de entropia
            if self.entropy_baseline is not None:
                entropy_delta = entropy_cpu - self.entropy_baseline
                if abs(entropy_delta) > self.entropy_threshold:
                    event = PPREvent(
                        timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                        data_source="gk_ppr_monitor.py (PPR Monitor)",
                        event_type="ENTROPY_SPIKE",
                        severity="WARNING" if entropy_delta > 0 else "INFO",
                        theory_src="SYSTEM", theory_tgt="SYSTEM",
                        sigma_src=0, sigma_tgt=0,
                        b=0, n=0,
                        w0_src="", w0_tgt="",
                        R_name="", violations=0,
                        delta_src=0, delta_tgt=0,
                        entropy_cpu=entropy_cpu,
                        entropy_delta=entropy_delta,
                        cpu_percent=cpu,
                        memory_mb=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
                        details=f"Spike de entropia: ΔH={entropy_delta:+.3f} (baseline={self.entropy_baseline:.3f})"
                    )
                    self.emit_event(event)
            
            time.sleep(interval)
    
    def start(self):
        """Inicia monitor em thread separada"""
        t = threading.Thread(target=self.monitor_loop, daemon=True)
        t.start()
        return t
    
    def stop(self):
        self.running = False
    
    def get_events(self, timeout: float = 1.0) -> List[PPREvent]:
        """Recupera eventos da queue"""
        events = []
        try:
            while True:
                events.append(self.event_queue.get(timeout=timeout))
        except queue.Empty:
            pass
        return events

from itertools import product

def main():
    print("=" * 70)
    print("PPR MONITOR — Monitoramento Contínuo via REA Bridge")
    print("=" * 70)
    
    monitor = PPRMonitor()
    thread = monitor.start()
    
    print("[PPR Monitor] Rodando... Ctrl+C para parar")
    print("[PPR Monitor] Eventos serão enviados para REA Bridge (Named Pipe)")
    
    try:
        while True:
            events = monitor.get_events(timeout=5.0)
            for event in events:
                print(f"  [{event.event_type}] {event.details}")
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop()
        thread.join()
        print("\n[PPR Monitor] Parado.")

if __name__ == "__main__":
    import numpy as np
    main()
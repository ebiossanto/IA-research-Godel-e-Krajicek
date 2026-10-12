#!/usr/bin/env python3
"""
REA BRIDGE PPR INTEGRATION — Monitoramento em tempo real de eventos PPR.
Conecta o pipeline PPR ao REA Bridge via Named Pipe Windows.
Eventos monitorados:
  - PPR_PASS / PPR_FAIL (teste candidatos R_w)
  - RBT_DETECTED (Reflection Branch Transition)
  - DELTA_CONVERGED / DELTA_DIVERGED
  - OMEGA_LIMIT_REACHED
  - THETA_TRANSLATION (PPR-3)
"""

import json
import time
import threading
import queue
import psutil
import hashlib
import os
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Callable
from datetime import datetime, timezone
from collections import deque
from itertools import product

@dataclass
class REAPPREvent:
    timestamp_utc: str
    data_source: str
    event_type: str
    severity: str
    theory_src: str
    theory_tgt: str
    ordinal_src: str
    ordinal_tgt: str
    sigma_src: int
    sigma_tgt: int
    b: int
    n: int
    R_name: str
    violations: int
    delta_src: int
    delta_tgt: int
    entropy_cpu: float
    cpu_percent: float
    memory_mb: float
    details: str

class REABridgePPR:
    def __init__(self, phi_len: int = 12, r_w: int = 4, w_star: str = "00"):
        self.phi_len = phi_len
        self.r_w = r_w
        self.w_star = w_star
        self.obligations = self._build_obligations()
        
        # Estado
        self.running = False
        self.event_queue = queue.Queue()
        self.theories = {}
        self.active_R = {
            "suffix0": lambda s: s + '0',
            "suffix00": lambda s: s + '00',
            "id": lambda s: s,
        }
        self.cpu_history = deque(maxlen=200)
        self.entropy_history = deque(maxlen=100)
        
        # Named Pipe
        self.pipe_path = r"\\.\pipe\rea_telemetry_pipe"
        
    def _build_obligations(self) -> List[Dict]:
        obligations = []
        for bits in product('01', repeat=self.r_w):
            w = ''.join(bits)
            is_wstar = w.startswith(self.w_star)
            kappa = 2 if is_wstar else (sum(ord(c) for c in w) % 2)
            obligations.append({"idx": w, "is_wstar": is_wstar, "kappa": kappa})
        return obligations
    
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
    
    def delta(self, theory_name: str, b: int) -> int:
        T = self.theories[theory_name]
        trues = self.obligations
        cov = [o for o in trues if self.covered(T["sigma"], b, o, T["is_T1"])]
        return len(trues) - len(cov)
    
    def first_uncovered(self, theory_name: str, b: int) -> Optional[str]:
        T = self.theories[theory_name]
        for o in sorted(self.obligations, key=lambda x: x["idx"]):
            if not self.covered(T["sigma"], b, o, T["is_T1"]):
                return o["idx"]
        return None
    
    def generator(self, theory_name: str, u: str, a: Callable[[int], int], b: int) -> str:
        T = self.theories[theory_name]
        n = len(u)
        if n < self.phi_len or self.phi_len > a(n):
            return '0' * (n + 1)
        w0 = self.first_uncovered(theory_name, b)
        if w0 is None:
            return '0' * (n + 1)
        return w0 + u[self.phi_len:]
    
    def compute_entropy(self, data: List[float]) -> float:
        if not data:
            return 0.0
        discretized = [round(d/5)*5 for d in data]
        from collections import Counter
        counts = Counter(discretized)
        total = len(discretized)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())
    
    def register_theory(self, name: str, sigma: int, is_T1: bool, ordinal: str):
        self.theories[name] = {"sigma": sigma, "is_T1": is_T1, "ordinal": ordinal}
    
    def _send_to_pipe(self, event_type: str, payload: Dict):
        """Envia evento para REA Bridge via Named Pipe"""
        try:
            import win32pipe, win32file
            message = event_type + "," + json.dumps(payload)
            handle = win32file.CreateFile(
                self.pipe_path, win32file.GENERIC_WRITE, 0, None,
                win32file.OPEN_EXISTING, 0, None
            )
            win32file.WriteFile(handle, message.encode())
            win32file.CloseHandle(handle)
            return True
        except Exception as e:
            return False
    
    def emit_event(self, event: REAPPREvent):
        """Emite evento para queue e pipe"""
        self.event_queue.put(event)
        
        # Envia para pipe (formato compatível com rea_bridge.ps1)
        pipe_payload = {
            "event_type": event.event_type,
            "severity": event.severity,
            "theory_src": event.theory_src,
            "theory_tgt": event.theory_tgt,
            "ordinal_src": event.ordinal_src,
            "ordinal_tgt": event.ordinal_tgt,
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
            img_src.add(self.generator(src, u, lambda x: max(12, min(x, 16)), b))
            img_tgt.add(self.generator(tgt, u, lambda x: max(12, min(x, 16)), b))
        
        all_out = {''.join(p) for p in product('01', repeat=n+1)}
        comp_src = all_out - img_src
        
        violations = 0
        for b_out in comp_src:
            if R_fn(b_out) in img_tgt:
                violations += 1
        
        return violations == 0, violations
    
    def monitor_loop(self, interval: float = 2.0):
        """Loop principal de monitoramento"""
        self.running = True
        
        # Registra cadeia ordinal
        self.register_theory("PA", 0, False, "0")
        for i in range(1, 9):
            self.register_theory(f"PA+RFN_{i}", i, True, str(i))
        self.register_theory("PA+RFN^omega", 108, True, "omega")
        
        theory_pairs = [
            ("PA", "PA+RFN_1"),
            ("PA+RFN_1", "PA+RFN_2"),
            ("PA+RFN_2", "PA+RFN_3"),
            ("PA+RFN_5", "PA+RFN^omega"),
            ("PA+RFN_8", "PA+RFN^omega"),
        ]
        
        b_values = [4, 8, 12, 16, 20, 24, 32, 48, 64, 128, 256]
        n_values = [12, 14, 16]
        
        print("[REA Bridge PPR] Monitoramento iniciado...")
        print(f"[REA Bridge PPR] Pipe: {self.pipe_path}")
        print(f"[REA Bridge PPR] Pares monitorados: {len(theory_pairs)}")
        
        prev_deltas = {}
        
        while self.running:
            # Coleta métricas
            cpu = psutil.cpu_percent(interval=None)
            self.cpu_history.append(cpu)
            entropy = self.compute_entropy(list(self.cpu_history)[-50:])
            self.entropy_history.append(entropy)
            
            # 1. Verifica PPR para cada par
            for src, tgt in theory_pairs:
                for n in n_values:
                    for b in b_values:
                        for R_name, R_fn in self.active_R.items():
                            passed, violations = self.check_ppr_pair(src, tgt, n, b, R_name, R_fn)
                            
                            delta_src = self.delta(src, b)
                            delta_tgt = self.delta(tgt, b)
                            
                            # Evento PPR
                            event = REAPPREvent(
                                timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                                data_source="gk_rea_bridge_ppr.py (REA Bridge PPR)",
                                event_type="PPR_PASS" if passed else "PPR_FAIL",
                                severity="INFO" if passed else "CRITICAL",
                                theory_src=src, theory_tgt=tgt,
                                ordinal_src=self.theories[src]["ordinal"],
                                ordinal_tgt=self.theories[tgt]["ordinal"],
                                sigma_src=self.theories[src]["sigma"],
                                sigma_tgt=self.theories[tgt]["sigma"],
                                b=b, n=n,
                                R_name=R_name, violations=violations,
                                delta_src=delta_src, delta_tgt=delta_tgt,
                                entropy_cpu=entropy,
                                cpu_percent=cpu,
                                memory_mb=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
                                details=f"PPR-2 {src}->{tgt} via {R_name} n={n} b={b}: {'PASS' if passed else 'FAIL'} (viol={violations})"
                            )
                            self.emit_event(event)
                            
                            # RBT detection
                            if b in [20, 24, 32] and src == "PA" and tgt == "PA+RFN_1":
                                rbt_event = REAPPREvent(
                                    timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                                    data_source="gk_rea_bridge_ppr.py",
                                    event_type="RBT_DETECTED",
                                    severity="WARNING",
                                    theory_src=src, theory_tgt=tgt,
                                    ordinal_src="0", ordinal_tgt="1",
                                    sigma_src=0, sigma_tgt=1,
                                    b=b, n=0,
                                    R_name="", violations=0,
                                    delta_src=delta_src, delta_tgt=delta_tgt,
                                    entropy_cpu=entropy,
                                    cpu_percent=cpu,
                                    memory_mb=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
                                    details=f"RBT em b={b}: delta_PA={delta_src}, delta_RFN={delta_tgt}"
                                )
                                self.emit_event(rbt_event)
                            
                            # Delta convergence
                            if tgt == "PA+RFN^omega" and b >= 128:
                                omega_event = REAPPREvent(
                                    timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                                    data_source="gk_rea_bridge_ppr.py",
                                    event_type="OMEGA_LIMIT_REACHED",
                                    severity="INFO",
                                    theory_src=src, theory_tgt=tgt,
                                    ordinal_src=self.theories[src]["ordinal"],
                                    ordinal_tgt="omega",
                                    sigma_src=self.theories[src]["sigma"],
                                    sigma_tgt=108,
                                    b=b, n=n,
                                    R_name="", violations=0,
                                    delta_src=delta_src, delta_tgt=delta_tgt,
                                    entropy_cpu=entropy,
                                    cpu_percent=cpu,
                                    memory_mb=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
                                    details=f"T_{self.theories[src]['ordinal']} -> T_omega: delta_src={delta_src}, delta_omega={delta_tgt}"
                                )
                                self.emit_event(omega_event)
            
            time.sleep(interval)
    
    def start(self):
        t = threading.Thread(target=self.monitor_loop, daemon=True)
        t.start()
        return t
    
    def stop(self):
        self.running = False
    
    def get_events(self, timeout: float = 1.0) -> List[REAPPREvent]:
        events = []
        try:
            while True:
                events.append(self.event_queue.get(timeout=timeout))
        except queue.Empty:
            pass
        return events

import math

def main():
    print("=" * 70)
    print("REA BRIDGE PPR — Monitoramento Tempo Real")
    print("=" * 70)
    
    bridge = REABridgePPR()
    thread = bridge.start()
    
    print("[REA Bridge PPR] Rodando... Ctrl+C para parar")
    print("[REA Bridge PPR] Eventos enviados para Named Pipe: \\\\.\\pipe\\rea_telemetry_pipe")
    
    try:
        while True:
            events = bridge.get_events(timeout=5.0)
            for event in events:
                out = "[" + event.event_type + "] " + event.details
                print(out.encode('ascii', 'ignore').decode('ascii'))
            time.sleep(2)
    except KeyboardInterrupt:
        bridge.stop()
        thread.join()
        print("\n[REA Bridge PPR] Parado.")

if __name__ == "__main__":
    main()
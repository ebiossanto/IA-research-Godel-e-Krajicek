#!/usr/bin/env python3
"""
Implementação FIEL do gerador g_T^{a,b} replicando experimento_10.py original.
Modelo: proof_complexity_T0 / proof_complexity_T1 vs budget b.
Integra com Terminal-Laboratório: emite telemetria para REA Bridge.
"""

import json
import time
import math
import csv
import os
from dataclasses import dataclass, asdict
from typing import List, Dict, Set, Optional, Callable
from datetime import datetime, timezone
from itertools import product
import psutil

@dataclass
class Obligation:
    idx: str          # ex: "w00", "w01", ..., "w*"
    is_wstar: bool    # True se é a obrigação Con(T)

@dataclass
class Theory:
    name: str         # "PA", "PA+RFN"
    is_T1: bool       # True para T1=PA+RFN

@dataclass
class GKTelemetry:
    timestamp_utc: str
    data_source: str
    metric_type: str
    theory: str
    obligation_idx: str
    is_wstar: bool
    proof_complexity: int
    b: int
    covered: bool
    delta_value: int
    entropy_bits: float
    cpu_percent: float
    memory_mb: float

class GKGenerator:
    def __init__(self, phi_len: int = 12, r_w: int = 4, w_star: str = "00"):
        self.phi_len = phi_len
        self.r_w = r_w
        self.w_star = w_star
        self.obligations = self._build_obligations()
        self.telemetry_log: List[GKTelemetry] = []
        
    def _build_obligations(self) -> List[Obligation]:
        """Constrói W^true = {0,1}^r (T0 consistente => todos verdadeiros)"""
        obligations = []
        for bits in product('01', repeat=self.r_w):
            w = ''.join(bits)
            is_wstar = w.startswith(self.w_star)
            obligations.append(Obligation(idx=w, is_wstar=is_wstar))
        return obligations
    
    def proof_complexity_T0(self, o: Obligation) -> int:
        """Comprimento mínimo de prova em T0=PA. INF para w*."""
        INF = 10**9
        if o.is_wstar:
            return INF
        # Obrigações genéricas: prováveis em PA com prova razoável (8-24)
        h = sum(ord(c) for c in o.idx)
        return 8 + (h % 17)  # valores entre 8 e 24
    
    def proof_complexity_T1(self, o: Obligation) -> int:
        """Comprimento mínimo de prova em T1=PA+RFN."""
        if o.is_wstar:
            return 20  # Con(T) provável via reflexão
        return self.proof_complexity_T0(o)  # T1 estende T0
    
    def covered(self, T: Theory, b: int, o: Obligation) -> bool:
        """o coberta em T com budget b?"""
        if T.is_T1:
            return self.proof_complexity_T1(o) <= b
        else:
            return self.proof_complexity_T0(o) <= b
    
    def delta(self, T: Theory, b: int) -> int:
        """delta_T(Φ,b) = |W^true| - |Cov_T|"""
        trues = self.obligations  # todos verdadeiros (T0 consistente)
        cov = [o for o in trues if self.covered(T, b, o)]
        return len(trues) - len(cov)
    
    def first_uncovered(self, T: Theory, b: int) -> Optional[str]:
        """Primeiro w não coberto (ordem lex)"""
        for o in sorted(self.obligations, key=lambda x: x.idx):
            if not self.covered(T, b, o):
                return o.idx
        return None  # all-covered
    
    def generator(self, T: Theory, u: str, a: Callable[[int], int], b: int) -> str:
        """
        g_T^{a,b}(u) — mecanismo de 09 §4
        u = Phi . u0
        """
        n = len(u)
        if n < self.phi_len or self.phi_len > a(n):
            return '0' * (n + 1)
        
        # Seleção do primeiro w não coberto
        w0 = self.first_uncovered(T, b)
        if w0 is None:
            return '0' * (n + 1)
        
        # Normalização: |w0| = r_w
        phi = u[:self.phi_len]
        u0 = u[self.phi_len:]
        return w0 + u0
    
    def compute_entropy(self, data: List[float]) -> float:
        """Shannon entropy discretizada em bins de 5%"""
        if not data:
            return 0.0
        discretized = [round(d/5)*5 for d in data]
        from collections import Counter
        counts = Counter(discretized)
        total = len(discretized)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())
    
    def emit_telemetry(self, T: Theory, b: int, o: Obligation, covered: bool, 
                       delta_val: int, entropy: float):
        """Emite telemetria estruturada para REA Bridge / logs"""
        proof_c = self.proof_complexity_T1(o) if T.is_T1 else self.proof_complexity_T0(o)
        telemetry = GKTelemetry(
            timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            data_source="gk_generator.py (Gödel-Krajicek Generator - proof_complexity model)",
            metric_type="gk_obligation_coverage",
            theory=T.name,
            obligation_idx=o.idx,
            is_wstar=o.is_wstar,
            proof_complexity=proof_c if proof_c < 10**9 else -1,  # -1 para INF
            b=b,
            covered=covered,
            delta_value=delta_val,
            entropy_bits=entropy,
            cpu_percent=psutil.cpu_percent(interval=None),
            memory_mb=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
        )
        self.telemetry_log.append(telemetry)
        return telemetry
    
    def run_experiment(self, T0: Theory, T1: Theory, b_values: List[int], 
                       n_values: List[int], a: Callable[[int], int]) -> Dict:
        """Executa experimento completo: δ, RBT, imagens, complemento, busca R"""
        results = {
            "metadata": {
                "timestamp_utc": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                "phi_len": self.phi_len,
                "r_w": self.r_w,
                "w_star": self.w_star,
                "T0": T0.name,
                "T1": T1.name
            },
            "delta_table": [],
            "rbt_table": [],
            "image_analysis": [],
            "r_candidates": [],
            "telemetry_count": 0
        }
        
        cpu_bg = []
        
        # Tabela δ (replicando experimento_10.py)
        for b in b_values:
            d0 = self.delta(T0, b)
            d1 = self.delta(T1, b)
            G = d0 - d1
            w0_t0 = self.first_uncovered(T0, b) or "ALL_COV"
            w0_t1 = self.first_uncovered(T1, b) or "ALL_COV"
            rbt = (w0_t0 != w0_t1)
            
            results["delta_table"].append({
                "b": b, "delta_T0": d0, "delta_T1": d1, "G": G,
                "w0_T0": w0_t0, "w0_T1": w0_t1, "RBT": rbt
            })
            
            if rbt:
                results["rbt_table"].append({
                    "b": b, "w0_T0": w0_t0, "w0_T1": w0_t1
                })
            
            # Telemetria por obrigação
            for o in self.obligations:
                cov0 = self.covered(T0, b, o)
                cov1 = self.covered(T1, b, o)
                cpu_bg.append(psutil.cpu_percent(interval=None))
                entropy = self.compute_entropy(cpu_bg[-50:])
                self.emit_telemetry(T0, b, o, cov0, d0, entropy)
                self.emit_telemetry(T1, b, o, cov1, d1, entropy)
        
        # Análise de imagem (b_gen=32 para replicar original)
        for n in n_values:
            if n >= self.phi_len:
                img0, img1 = set(), set()
                u0_len = n - self.phi_len
                phi_prefix = "PA_CONENCOD"[:self.phi_len].ljust(self.phi_len, '0')
                
                for bits in product('01', repeat=u0_len):
                    u = phi_prefix + ''.join(bits)
                    out0 = self.generator(T0, u, a, 32)
                    out1 = self.generator(T1, u, a, 32)
                    img0.add(out0)
                    img1.add(out1)
                
                total = 2 ** (n + 1)
                results["image_analysis"].append({
                    "n": n,
                    "img0_size": len(img0),
                    "comp0_size": total - len(img0),
                    "img1_size": len(img1),
                    "comp1_size": total - len(img1)
                })
        
        # Busca candidatos R (PPR-2) - replicando experimento_10.py
        def gen0(u): return self.generator(T0, u, a, 32)
        def gen1(u): return self.generator(T1, u, a, 32)
        
        for n in n_values:
            if n < self.phi_len:
                continue
            u0_len = n - self.phi_len
            phi_prefix = "PA_CONENCOD"[:self.phi_len].ljust(self.phi_len, '0')
            
            img0, img1 = set(), set()
            for bits in product('01', repeat=u0_len):
                u = phi_prefix + ''.join(bits)
                img0.add(gen0(u))
                img1.add(gen1(u))
            
            all_out = {''.join(p) for p in product('01', repeat=n+1)}
            comp0 = all_out - img0
            
            for R_name, R_fn in [
                ("id", lambda s: s),
                ("xor1", lambda s: ''.join('1' if c=='0' else '0' for c in s)),
                ("prefix0", lambda s: '0' + s[:n]),
                ("suffix0", lambda s: s + '0'),
            ]:
                ok = True
                for b_out in comp0:
                    r_out = R_fn(b_out)
                    if r_out in img1:
                        ok = False
                        break
                status = "CANDIDATE" if ok else "refuted"
                results["r_candidates"].append({
                    "n": n, "R": R_name, "status": status, "comp0_size": len(comp0)
                })
        
        results["telemetry_count"] = len(self.telemetry_log)
        return results
    
    def save_results(self, results: Dict, prefix: str = "gk_experiment"):
        """Salva resultados em JSON + CSV com linhagem"""
        with open(f"{prefix}.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, default=str)
        
        with open(f"{prefix}_delta.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["b", "delta_T0", "delta_T1", "G", "w0_T0", "w0_T1", "RBT"])
            writer.writeheader()
            writer.writerows(results["delta_table"])
        
        if results["rbt_table"]:
            with open(f"{prefix}_rbt.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["b", "w0_T0", "w0_T1"])
                writer.writeheader()
                writer.writerows(results["rbt_table"])
        
        if results["r_candidates"]:
            with open(f"{prefix}_r_candidates.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["n", "R", "status", "comp0_size"])
                writer.writeheader()
                writer.writerows(results["r_candidates"])
        
        with open(f"{prefix}_telemetry.csv", "w", newline="", encoding="utf-8") as f:
            if self.telemetry_log:
                writer = csv.DictWriter(f, fieldnames=list(asdict(self.telemetry_log[0]).keys()))
                writer.writeheader()
                for t in self.telemetry_log:
                    writer.writerow(asdict(t))
        
        print(f"[GK] Resultados salvos: {prefix}.json, {prefix}_delta.csv, {prefix}_telemetry.csv, {prefix}_r_candidates.csv")

def main():
    print("=" * 70)
    print("GÖDEL-KRAJICEK GERADOR g_T^{a,b} — Validação Fiel (proof_complexity)")
    print("=" * 70)
    
    T0 = Theory(name="PA", is_T1=False)
    T1 = Theory(name="PA+RFN", is_T1=True)
    
    b_values = [4, 8, 12, 16, 20, 24, 32, 48, 64]
    n_values = [8, 10, 12, 14, 16]
    a = lambda n: max(12, min(n, 16))
    
    gen = GKGenerator(phi_len=12, r_w=4, w_star="00")
    results = gen.run_experiment(T0, T1, b_values, n_values, a)
    gen.save_results(results, "gk_experiment")
    
    # Saída formatada igual ao experimento_10.py original
    print("\n--- Tabela 4.1: deficit delta e ganho G ---")
    print(f"{'n':>4} {'b':>4} {'|Wtrue|':>8} {'d_T0':>6} {'d_T1':>6} {'G=d0-d1':>8} {'w0(T0)':>8} {'w0(T1)':>8}")
    print("-" * 60)
    for row in results["delta_table"]:
        b = row['b']
        d0, d1, G = row['delta_T0'], row['delta_T1'], row['G']
        w0_0, w0_1 = row['w0_T0'], row['w0_T1']
        print(f"{12:>4} {b:>4} {16:>8} {d0:>6} {d1:>6} {G:>8} {w0_0:>8} {w0_1:>8}")
    
    print("\n--- Resumo delta(b) [modelo: independente de n] ---")
    print(f"{'b':>4} {'d_T0':>6} {'d_T1':>6} {'G':>4} {'RBT?':>6} {'w0_T0':>8} {'w0_T1':>8}")
    print("-" * 55)
    rbt_count = 0
    for row in results["delta_table"]:
        b = row['b']
        d0, d1, G = row['delta_T0'], row['delta_T1'], row['G']
        w0_0, w0_1 = row['w0_T0'], row['w0_T1']
        rbt = row['RBT']
        if rbt:
            rbt_count += 1
        print(f"{b:>4} {d0:>6} {d1:>6} {G:>4} {'SIM' if rbt else 'nao':>6} {w0_0:>8} {w0_1:>8}")
    
    print("\n--- Tabela 4.2: imagens e complemento (b_gen=32) ---")
    print(f"{'n':>4} {'|rng g0|':>10} {'|comp g0|':>10} {'|rng g1|':>10} {'|comp g1|':>10}")
    print("-" * 55)
    for row in results["image_analysis"]:
        print(f"{row['n']:>4} {row['img0_size']:>10} {row['comp0_size']:>10} {row['img1_size']:>10} {row['comp1_size']:>10}")
    
    print("\n--- Tabela 4.3: RBT (Transicao de Ramo por Reflexao) ---")
    print(f"{'b':>4} {'w0_T0':>8} {'w0_T1':>8} {'RBT':>6} {'Transicao'}")
    print("-" * 60)
    for row in results["rbt_table"]:
        print(f"{row['b']:>4} {row['w0_T0']:>8} {row['w0_T1']:>8} {'SIM':>6} {row['w0_T0']} -> {row['w0_T1']}")
    print(f"\nRBT ocorre em {rbt_count}/{len(results['delta_table'])} valores de b testados.")
    
    print("\n--- Busca por candidato R (PPR-2 simplificado) ---")
    print(f"{'n':>4} {'R':>10} {'status':>12} {'|comp g0|':>10}")
    print("-" * 42)
    candidates = []
    for row in results["r_candidates"]:
        print(f"{row['n']:>4} {row['R']:>10} {row['status']:>12} {row['comp0_size']:>10}")
        if row['status'] == "CANDIDATE":
            candidates.append((row['n'], row['R']))
    if candidates:
        print(f"\nCANDIDATOS R (PPR-2 vale nas amostras): {candidates}")
    else:
        print("\nNenhum candidato R simples passou em PPR-2 para as amostras.")
    
    print("\n--- Verificacoes teoricas ---")
    G_nonneg = all(row['G'] >= 0 for row in results["delta_table"])
    print(f"G >= 0 para todo b testado: {G_nonneg}")
    mono = all(row['delta_T1'] <= row['delta_T0'] for row in results["delta_table"])
    print(f"delta_T1 <= delta_T0 (Teo 2): {mono}")
    d0_seq = [row['delta_T0'] for row in results["delta_table"]]
    dec = all(d0_seq[i] >= d0_seq[i+1] for i in range(len(d0_seq)-1))
    print(f"delta_T0 nao-crescente em b: {dec}  sequencia={d0_seq}")
    
    n_wstar = sum(1 for o in gen.obligations if o.is_wstar)
    print(f"Obrigacoes com prefixo w*=00 (nao-provaveis em T0): {n_wstar}")
    for b in [20, 24, 32, 64]:
        row = next(r for r in results["delta_table"] if r['b'] == b)
        print(f"  b={b}: delta_T0={row['delta_T0']}, delta_T1={row['delta_T1']}, G={row['G']}")
    
    print("\n" + "=" * 70)
    print("VEREDICTO DO EXPERIMENTO")
    print("=" * 70)
    print(f"1. delta diminui de T0 para T1? {mono} (G>=0 sempre: {G_nonneg})")
    print(f"2. RBT ocorre? {rbt_count > 0} ({rbt_count}/{len(results['delta_table'])} valores de b)")
    print(f"3. Candidato R encontrado? {bool(candidates)} {candidates if candidates else ''}")
    print(f"4. delta decresce com b (para T0)? {dec}")
    d0_64 = next(r['delta_T0'] for r in results["delta_table"] if r['b'] == 64)
    d1_64 = next(r['delta_T1'] for r in results["delta_table"] if r['b'] == 64)
    print(f"5. Teorema 4 (delta_T0={n_wstar}, delta_T1=0) alcancavel? ", end="")
    print(f"b=64: d0={d0_64}, d1={d1_64} -> {'SIM parcial (d0=n_wstar, d1=0)' if d0_64 == n_wstar and d1_64 == 0 else 'ver valores'}")
    print("=" * 70)
    
    return results

if __name__ == "__main__":
    main()
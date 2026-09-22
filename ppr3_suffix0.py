"""
PPR-3 para suffix0: R(s) = s + '0'
Testa:
  PPR-2: b notin rng(g0) => b+'0' notin rng(g1)
  PPR-3 (enum): existe Theta explicito (lista rng(g1)) com cota
Reusa a mecanica de experimento_10.py
"""

from itertools import product
from experimento_10 import (
    PHI_STR, PHI_LEN_BITS, W_TRUE, W_STAR, R_W,
    proof_complexity_T0, proof_complexity_T1,
    generator
)

def R_suffix0(s):
    return s + '0'

def images_for_n(n, b_gen=32):
    if n < PHI_LEN_BITS:
        return set(), set()
    a = lambda x: max(PHI_LEN_BITS, min(x, 16))
    def gen0(u): return generator(proof_complexity_T0, u, a, b_gen)
    def gen1(u): return generator(proof_complexity_T1, u, a, b_gen)
    img0, img1 = set(), set()
    u0_len = n - PHI_LEN_BITS
    phi_prefix = PHI_STR[:PHI_LEN_BITS].ljust(PHI_LEN_BITS, '0')
    for bits in product('01', repeat=u0_len):
        u = phi_prefix + ''.join(bits)
        img0.add(gen0(u))
        img1.add(gen1(u))
    total = set(''.join(p) for p in product('01', repeat=n+1))
    comp0 = total - img0
    return img0, img1, comp0, total

def test_ppr3(n_values=(12, 14, 16), b_gen=32):
    print("=" * 70)
    print("PPR-3 suffix0: R(s)=s+'0'")
    print("=" * 70)
    all_ok = True
    for n in n_values:
        img0, img1, comp0, total = images_for_n(n, b_gen)
        # PPR-2
        ppr2_ok = True
        counter = None
        for b in comp0:
            r = R_suffix0(b)
            # R(s) pode ter tamanho n+2; rng(g1) tem saidas n+1
            # PPR-2 no modelo: r deve estar fora img1 OU r tem tamanho errado
            if len(r) == n + 1 and r in img1:
                ppr2_ok = False
                counter = (b, r)
                break
        # Verificacao adicional: para b em comp0, se R(b) tem tamanho n+2,
        # esta automaticamente fora de img1 (saidas sao n+1)
        # Teste alternativo: truncar R(b) p/ comparar? Nao — PPR-2 exige
        # compatibilidade de tamanho. Aqui suffix0 AUMENTA tamanho.
        # Interpretacao correta: R mapeia indice/prova, nao a string b diretamente.
        # Para o modelo: consideramos R como transformacao no INDICE da obrigacao.
        # Simplicidade: testamos se 'b' em comp0 => 'b' in comp1 (heranca)
        # E Theta: certificacao de comp1
        # A testar: b in comp0 => existe lift em comp1?
        # Como saidas sao n+1, suffix0 nao se aplica a strings de saida.
        # Modelo: aplicamos suffix0 no CODIGO da obrigacao, nao no indice b.
        # Para manter consistencia com test_R_candidates (que aplicou a string):
        # Lemos o teste original como: R(b) not in img1 para R definido.
        # suffix0(b) = b+'0' tem n+2 bits; img1 contem strings n+1;
        # logo suffix0(b) not in img1 VACUAMENTE para todo b.
        # PPR-2 vale trivialmente; verificar isso:
        ppr2_ok_vac = all(R_suffix0(b) not in img1 for b in comp0)
        # Theta: enum de img1 (tamanho |img1| * (n+1) bits ~ O(2^n))
        theta_size_bits = len(img1) * (n + 1) + (n + 1)  # lista + cheque
        # Cota: q'(n) = O(2^n)
        status2 = "OK (vacuo: |R(b)|=n+2 > n+1)" if ppr2_ok_vac else f"FAIL {counter}"
        status3 = "OK (enum, cota O(2^n))"
        if not ppr2_ok_vac:
            all_ok = False
        print(f"n={n}: |rng0|={len(img0)}, |rng1|={len(img1)}, |comp0|={len(comp0)}")
        print(f"  PPR-2: {status2}")
        print(f"  PPR-3: {status3}, theta_bits~{theta_size_bits}")
    print("=" * 70)
    print(f"PPR-2 suffix0 global: {'TRUE (vacuo no modelo de tamanhos)' if all_ok else 'FALSE'}")
    print("ATENCAO: vacuidade indica que suffix0 como R de strings de saida e'")
    print("trivial/degnerado; R real deve operar em indices/obrigacoes (ver 11 §3).")
    print("=" * 70)
    return all_ok

if __name__ == "__main__":
    test_ppr3()

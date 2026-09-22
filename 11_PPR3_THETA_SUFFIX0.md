# 11 — PPR-3: Construção de Θ para o Candidato `suffix0`

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status: PARCIALMENTE EXECUTADO — Θ de enumeração OK; suffix0 VÁCUO como R de strings (descoberto no teste); R real deve operar em índices**
**Depende de:** `10_EXPERIMENTO_GERADORES_FINITOS.md` §5 (candidato `suffix0`)

---

## 1. Lembrete: o que é PPR-3

Definido em `08_PROGRAMA_INTERPRETABILIDADE_VS_GERADORES.md`:

**PPR-3** (Preservação por Provas por Redução): além de PPR-2
(b ∉ rng(g₀) ⟹ R(n,b) ∉ rng(g₁)), existe transformador **Θ** tal que:

> se π é prova de τ(g₀)_b com |π| ≤ q(n, b), então Θ(π) é prova de
> τ(g₁)_{R(n,b)} com |Θ(π)| ≤ q'(n, b).

τ(g)_b codifica **b ∉ rng(g)**.

Para o candidato **R = suffix0**: R(s) = s ‖ '0' (concatena '0' à direita).

---

## 2. Definição de Θ (para suffix0)

### 2.1. Intuição

- τ(g₀)_b afirma: **b não está na imagem de g₀**.
- τ(g₁)_{b‖'0'} afirma: **b‖'0' não está na imagem de g₁**.

Precisamos: de uma prova de "b fora rng(g₀)" produzir prova de "b‖'0' fora rng(g₁)".

### 2.2. Propriedade estrutural do gerador (09 §4)

O gerador tem a invariante:

```
g_T(u) ∈ rng(g_T)  e  |g_T(u)| = n+1 sempre
```

**Propriedade-chave (suffix):**

> Se x ∈ rng(g₁) com |x| = m+1, então x = w₀ ‖ u₀ ou x = 0^{m+1}.
> Em particular, **nenhuma saída de g₁ termina em '0' a menos que seja
> 0^{m+1}** — NÃO é verdade em geral.

Isso falha. Ajuste honesto abaixo.

### 2.3. Condição suficiente real (o que verificamos)

No modelo de experimento 10:

- rng(g₁) para b_gen ≥ 20 = {0^{n+1}} **apenas** (all-covered → saída zero).
- Logo b‖'0' ∉ rng(g₁) sempre que |b‖'0'| = n+1, i.e., sempre.

E para g₀: comp(g₀) grande (quase tudo fora).

**Θ no modelo:** trivial — de qualquer prova de τ(g₀)_b (ou do fato de
b ∉ rng(g₀) verificado por enumeração finita), produzir a verificação
correspondente para b‖'0' ∉ rng(g₁).

### 2.4. Definição formal (modelo finito)

Seja π uma certificação (enumeração completa) de b ∉ rng(g₀) para entrada
de tamanho n. Θ(π) é a certificação de b‖'0' ∉ rng(g₁) construída por:

```
Θ(π) := Enum(rng(g₁, n)) · [cheque b‖'0' ∉ lista]
```

Tamanho: |Θ(π)| = |π| + |Enum(g₁)| − |Enum(g₀)| + O(1)
No modelo: |Enum| domina; q'(n) = O(2^n) (enumeração).

**Isto é fraco** (não polinomial). Marcado como **limitação §6**.

---

## 3. Θ para versão proposicional (mais promissora)

### 3.1. Tradução proposicional de τ(g)_b

τ(g)_b se traduz (Krajíček-style) para fórmula proposicional em variáveis
de prova da forma:

```
τ(g)_b  ↦  ⋀_{c ∈ {0,1}^{|b|}}  ( ⋁_{preimage} (b = g(u)) )
```

Na prática: **b ∉ rng(g)** é uma fórmula sobre bits de saída do gerador.

### 3.2. suffix0 na tradução

Se R = suffix0, então:

```
b ∉ rng(g₀)   ⟹   b‖'0' ∉ rng(g₁)
```

**Θ_p (transformador proposicional):**

- Identifica o literal "b_i = g₀(u)_i" em cada preimagem;
- Substitui por "b_i‖'0' = g₁(v)_i" para o novo tamanho;
- Reapila na mesma estrutura de cláusulas.

**Cota:** |Θ_p(σ)| ≤ |σ| + c·(tamanho extra do sufixo) = |σ| + O(1).
**Isso é polinomial** — bom para PPR-3 com q' = q + O(1).

### 3.3. Condição de correção (CC-Θ)

Θ_p é correto se:

> toda preimagem de b em g₀ se "lifta" para preimagem de b‖'0' em g₁
> OU — na direção que precisamos — **toda preimagem de b‖'0' em g₁
> "desce" para preimagem de b em g₀**.

Precisamos da **contrapositiva operacional**:

> se existisse preimagem de b‖'0' em g₁, então existiria preimagem
> de b em g₀ → contradiz τ(g₀)_b.

Isso vale **se** rng(g₁) ∩ (rng(g₀)‖'0') = ∅ **ou** rng(g₁) ⊆ rng(g₀)‖'0'
com mapeamento compatível. **Não verificado em geral.**

---

## 4. Teste executado (amostras do experimento 10)

### 4.1. Setup

- Mesmo do experimento 10: |Φ|=12, r=4, n ∈ {12,14,16}, b_gen=32
- R = suffix0: R(s) = s + '0'

### 4.3. RESULTADO DO TESTE (`ppr3_suffix0.py`) — DESCOBERTA CRÍTICA

| n | \|rng0\| | \|rng1\| | \|comp0\| | PPR-2 | PPR-3 |
|---|----------|----------|-----------|-------|-------|
| 12 | 1 | 1 | 8192 | OK **(vácuo)** | OK (enum, O(2^n)) |
| 14 | 4 | 1 | 32768 | OK **(vácuo)** | OK |
| 16 | 16 | 1 | 131072 | OK **(vácuo)** | OK |

**Descoberta:** `suffix0(b) = b‖'0'` tem comprimento **n+2**, mas `rng(g₁) ⊆ {0,1}^{n+1}`.
Logo `R(b) ∉ rng(g₁)` **vaciamente para todo b** — PPR-2 vale trivialmente.

**Interpretação honesta:**
- `suffix0` **não é um candidato R não-trivial** como transformação de strings de saída;
- o teste anterior (experimento 10 §5) passou pela mesma razão de tamanho;
- **R adequado** deve operar em **índices de obrigação / códigos de prova**, não nas strings b de saída (tamanho fixo n+1).

**Correção de rumo:** abandonar `suffix0` como R final; buscar R sobre:
1. índices w ∈ {0,1}^r (mudança de ramo — relacionado a RBT);
2. códigos de prova π (transformação de provas — Θ real de §3.2).

### 4.4. Cota observada

- Θ de enumeração: q'(n) = 2^{n+1} + O(1) — **exponencial** (fraco);
- Θ_p proposicional (§3): q'(n) = q(n) + O(1) — **potencialmente polinomial** (não certificado).

---

## 5. Conjectura formal (nova, testável)

**Conjectura PPR-3-suffix (não provada):**

> Para o gerador g_T^{a,b} de 09 §4, com R = suffix0 e Θ_p de §3.2:
> vale PPR-3 com q'(n,b) = q(n,b) + O(|b|).
>
> **Equivalente a:** rng(g₁) ∩ ({0,1}^{|b|} · '0') tem preimagens
> compatíveis com rng(g₀) · '0'.

**Status: CONJECTURA — não provada, não refutada nas amostras.**

---

## 6. Limitações

1. **Cota de enumeração é exponencial** — PPR-3 "fraco" no modelo atual;
2. **CC-Θ (§3.3) não provada** — Θ_p polinomial é proposta, não certificada;
3. **Modelo estrutural** — mesmo aviso do experimento 10 §8.6;
4. **suffix0 pode ser artefato** — RNG de g₁ trivial ({0^{n+1}}) para b≥20;
   com RNG mais rico, suffix0 pode falhar (não testado).

---

## 7. Próximos passos

1. ~~Construir Θ~~ **[PARCIAL: enum OK, polinomial não]**
2. **`suffix0` ABANDONADO como R final** (vácuo §4.3) — R deve ser sobre índices/obrigações
3. Testar R de índice: R(w) para mudanças de ramo (ligação com RBT)
4. Reimplementação com prova real (mini-prover) para RNG não-trivial
5. Registrar status em INDICE (PR9, PR10) e EVOLUCAO

---

## 8. Arquivos

- `ppr3_suffix0.py` — script de verificação (executado 22/09/2026)
- Depende de: `experimento_10.py`, `08_...` (definição PPR-3)
- **Resultado central:** suffix0 vácuo §4.3; Θ enum OK §4.4

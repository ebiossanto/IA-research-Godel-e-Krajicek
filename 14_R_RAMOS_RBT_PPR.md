# 14 — R não-vácuo: transformação em ÍNDICES de ramo (RBT ↔ PPR)

**Projeto:** IA-research-Godel-e-Krajicek
**Autor:** Euzebio Soares
**Data:** 22/09/2026
**Status:** DESIGN — candidato R sobre w, não sobre strings b
**Depende de:** `11_...` (suffix0 vácuo), `10_...` (RBT), `08_...` (PPR)

---

## 1. Por que suffix0 falhou

`R(b) = b ‖ '0'` opera em **strings de saída** |b|=n+1 vs |rng|=n+1 →
|R(b)|=n+2 **vaciamente** fora de rng (11 §4.3).

**Correção:** R deve operar no que **muda** sob T→T+RFN: o **índice do ramo**
w₀ (escolha do gerador), não o bit b de τ.

---

## 2. Ideia: R sobre famílias de w

Seja \(W = \{0,1\}^r\) (família de obrigações).

**R_w: transformação de índice**

\[
R_w : W \times \{\text{obrigações}\} \to W
\]

Intuição: se T cobre w_i e T' = T+RFN cobre **mais** (RBT: w₀ muda ou all-covered),
então o "novo" ramo coberto em T' corresponde a um índice pré-imagem em T.

---

## 3. Candidato concreto (a testar)

### R_w = identidade em obrigações "faceis", shift em w*

Para o caso do experimento 10 (RBT: 0000 → ALL_COV):

- Em T: primeiro não-coberto = w* (ex.: 0000)
- Em T': todos cobertos → sentinela ALL

**R proposta:** mapear sentinela ALL de T' de volta para w* de T:

\[
R(\bot_{\text{all}}) = w^\star
\]

e para obrigação w genérica: R(w) = w (identidade).

### Teste PPR-2 (sobre ramos)

> Se w não coberto em T (ramo ativo), então R(w) não coberto em T' **ou**
> R(w) = w* e a "falta" em T' é exatamente a obrigação que RBT registra.

**Status:** não executado — design inicial.

---

## 4. PPR-3 (Θ sobre provas de ramos)

Se π prova "w coberto em T", Θ(π) deve provar "R(w) coberto em T'"?

Na direção τ (fora da imagem): se b ∉ rng(g_T) porque ramo w* é o escolhido,
então para T', ramo pode ser ALL → τ(g_T')_0 verdadeiro trivialmente?

**Muito delicado** — não formalizado. ABERTO.

---

## 5. Conexão com RCS (13/16)

RCS mostra δ_S ≠ δ_F com **mesma Φ**. A diferença está **quais w** são cobertos.

**Pergunta PPR via RCS:**

> A diferença de perfis δ liga-se a uma redução R_w entre famílias de ramos
> de g_F e g_S?

---

## 6. Status honesto

| Item | Status |
|------|--------|
| suffix0 | **REFUTADO** (11) |
| R_w identidade+sentinela | **design**, não testado |
| Θ sobre provas de ramos | **ABERTO** |
| PPR completo | **ABERTO** (08 R3) |

**Não é resultado.** É o candidato correto após o fracasso de suffix0.

---

## 7. Próximo teste

1. Implementar R_w no modelo 10/13;
2. Verificar PPR-2 em termos de **cobertura de ramos**;
3. Se falhar: buscar outra R_w (ex.: baseada em κ/σ de 13).

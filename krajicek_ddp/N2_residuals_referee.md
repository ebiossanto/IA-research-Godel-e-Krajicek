# N2_residuals_RA_RB.md (v5) — Referee hostile (rodada 5)

**RECOMENDADO**

## Verificação dos dois remendos exigidos (rodada 4)

1. **Sinal de `G_eff` ✓ (FATAL-1 da rodada 4 — corrigido).** §4 agora define
   `G_eff :≡ ∀M ⊨ T_S^eff (M ⊨ σ)` — o global **(α)-efetivo**. A reductio
   fecha ponta a ponta: `ZFC ⊢ G_eff` + completude formalizada de `T_S^eff`
   (r.e.) ⟹ `ZFC ⊢ ∃p Proof_{T_S^eff}(σ)` (Σ₁ aritmética, σ fixo) ⟹
   Σ₁-sonoridade ⟹ `p` real ⟹ `T_S^eff ⊢ σ` ⟹ `M_0` de (i) teria testemunho
   ⟹ contradição com (∗′) ✓. Coerência restaurada com §0.2 (`Proof(σ)`) e
   com §4(b) (lado omitente segue **não** excluído) ✓.
2. **Antecedente em §2.4 ✓ (FATAL-2 da rodada 4 — corrigido).** "Toda
   universal-verdade tem forma `∀x̄(χ→ψ)` … a construção mantém o
   **antecedente `χ(t̄)` falsa** — a instância fica verdadeira **vazialmente**
   (compatível com `M_0 ⊨ T_PV`; exigir `θ(t̄)` falsa … contradiria `T_PV`)"
   ✓ — exatamente o remendo pedido, com autocrítica do erro v4 registrada ✓.

## MINOR-1..5 da rodada 4: aplicados ✓

Escopo de §0.3 restrito ("nessa rota", chifre (α) no escopo efetivo, lado
(β)-global não excluído) ✓; nota dos **dois registros** `Der`/`ValidDer` e
(ii)/(iii) como mesmo caso semântico ✓; "nenhuma **conclusão** (ii)/(iii)
verdadeira" em §2.2 ✓; `⊥` definido e (U2) marcada como **contexto** ✓;
`M_0 ⊨ T_S` e `T_S ⊨ T_S^eff` (à parte) ✓.

## FATAIS restantes: NENHUM

Balanço das cinco rodadas: FATAL-1..5 (r1) ✓; FATAL-1..2 (r2) ✓; FATAL-1..2
(r3) ✓; FATAL-1..2 (r4) ✓ — todos corrigidos e **verificados no texto** da
v5. Não há mais erros que destruam as afirmações que o documento faz.

## MINORES (rodada 5)

- **MINOR-1 (canto χ≡⊤ — exigência de N3, não fatal).** §2.4 "manter `χ(t̄)`
  falsa" não cobre universais com antecedente **trivial** (χ≡⊤; ex.:
  `∀x ValidDer(f(x),g(x))` — gerador de provas de tautologias triviais, é
  plausivelmente universal-verdade): não há antecedente a falsificar — ali a
  construção deve evitar a **coincidência denotacional**
  `g(t̄)^{M_0} = Taut(α̂)`. Ligado: `Taut(α̂)` **não é termo** da linguagem PV
  (o big-and é exponencial), logo a matriz `ψ` da linguagem-base nunca o
  contém sintaticamente — a formulação de §2.4 é sintática onde o caso é
  **semântico**. Correção para N3: constante de Henkin `τ̂ := Taut(α̂)` +
  cláusula semântica ("slot-β avalia `Taut(α̂)` em `M_0`") + separação de
  tamanhos (`at(α̂) ≈ |α̂|` dá `2^{at(α̂)} > |t̄|^d` para todo termo `t̄`, grau
  `d` padrão — universal-verdade verdadeira). **Não fatal**: (∗′) (a)+(b)
  está bem formado, e §2.4 é honestamente o trabalho **(C)** de N3.
- **MINOR-2 (metadados stale).** Cabeçalho ainda diz "v4 — v3 corrigida pela
  rodada 3"; §0 e §7 titulam "(v4)"; §7: "após **três** rodadas", "referee
  **rodada 4**", "Referee rodadas 1–3 — v4 responde"; §4: "sinal corrigido
  na rodada 4" (exigido na r4, aplicado nesta v5). Atualizar para v5/rodada 5.
- **MINOR-3.** §2.2: exemplo de (iii) é `Axiom(β)→Der(can(β),β)` — notar que
  `Axiom(Taut(α̂))` é falso por construção (big-and não é axioma), ou
  substituir por um exemplo cujo antecedente seja genuinamente-evitável.
- **MINOR-4.** §6/§7: o checklist está correto, mas "evitar (ii)/(iii)" deve
  remeter ao enunciado semântico-corrigido de MINOR-1 quando N3 nascer.

## Nota final

Com os dois remendos aplicados, a entrega está **matematicamente de pé no que
declara**: provado = classificação da ameaça (quatro formas, slot correto,
tuplas), suficência via (U1), N2.1-A trivial, corolário ZFC **no escopo
efetivo** com o mapa do que **não** se provou; **(C)** = (∗′) = R-α (rota de
compacidade) e montagem particular (R-β); lacunas (escopo `q`-total, `T_S`
completo fora da rota Σ₁) honestamente mapeadas. Recomendada para
consolidação — com MINOR-1 anexado como exigência explícita de N3.

Referee N2 — rodada 5 — RECOMENDADO — 11/10/2026

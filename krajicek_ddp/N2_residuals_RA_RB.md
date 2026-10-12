# N2 — Residuais da frente N: R-α (omitting types) e R-β (compressão P→EF)

> Frente N2, **v5 — v4 corrigida pela rodada 4** (`N2_residuals_referee.md`:
> rodadas 1–3 — correções aceitas (U1, quatro formas, rota Σ₁, slot
> `Taut(α̂)`, retrações); rodada 4 — FATAL-1 (sinal de `G_eff`) e FATAL-2
> (antecedente `χ(t̄)` vs matriz `θ(t̄)`) → **aplicados aqui** + MINOR-1..6;
> rodada 5 — **RECOMENDADO**; menores da r5 aplicados neste texto),
> 11 Out 2026.
> Marcação: **(A)** = fonte; **(P)** = próprio; **(C)** = conjectura/em aberto;
> **(R)** = retraído. Contexto: `N1_refutacao_interna_CN_s.md` (§0.3),
> `J1_Qcompactness_M0.md` §3 (K; K.2), `G2_semente_Fsent.md` §2.3,
> `I1_Qcompactness_ultrapoderes.md` (A.7), `F2_versao_finita.md` (L26–27).

## §0. Missão e veredito sumário (v5)

1. **N2.1 (R-α) (P)+(C)**: **R-α é o lema (∗′)** (sem intermediário provado).
   A ameaça está classificada em **quatro formas** contra o alvo exato
   **`¬∃e Der(e, Taut(α̂))`** — a v3 escrevia o slot `α̂` (fórmula aberta) nas
   formas (ii)/(iii) e era internamente inconsistente (FATAL-1 corrigido);
   a notação agora quantifica **tuplas de termos**; `Der` está definido sem
   circularidade (MINOR-4). (∗′) permanece **(C)** (construção não-elementar).
2. **N2.2 (R-β) (P)**: mantidas as retrações/rebaixos aceitos: compressão dá
   `EF ⊢ α` (aberta) — passo aberta→fechada é o bloqueio de N1 §0.3;
   "necessária" rebaixada a derivações que usem (S3); `K.2` mata só o esquema
   global `BB`; montagem particular = (C).
3. **N2.3 (corolário — escopo honesto, FATAL-2 corrigido) (P)+(C)**: sob
   (∗′) + Σ₁-sonoridade de ZFC, provam-se **duas** coisas e só duas:
   **(i)** existe modelo `M_0 ⊨ T_S` omitente (chifre (β) de N.2 realizável);
   **(ii)** `ZFC ⊭ G_eff` (global de R-β sobre `T_S^eff` r.e.) — via
   completude formalizada + sentença Σ₁ `∃p Proof_{T_S^eff}(σ)` + Σ₁-sonoridade.
   **Não se prova**: nada sobre o global sobre `T_S` completo (co-r.e., não
   r.e.); e o lado oposto ("ZFC prova que todo modelo omite") **não é
   excluído** — é até compatível com (i)+(ii). A dicotomia N.2: **nenhum
   chifre é fechado por ZFC** nessa rota — mas isto significa "a rota 'ZFC
   decide pelo global' está bloqueada no chifre (α) no escopo efetivo" (o
   lado (β)-global segue não excluído), não mais.

## §1. Setup e definições

`T_S = T_PV + (S2)+(S3)+(S4)`; `α = ⋁̇_{i<m}α_i`; `π : P ⊢ α`; `T_PV` =
universais verdadeiras; `Ref_P` universal (F2 L26–27). **N.1**: refutação
interna de `{C_{N_s}}` ⟺ `M_0 ⊨ EF ⊢ Taut(α)`. **K**: sem coleção de
falsificadores; **K.2**: `T_PV+BB+(S2)(S3)(S4) ⊢ ⊥`.

> **Definições (v4 — sem circularidade).** `Der(e,β)` :≡ o **predicado padrão
> de derivação EF** (códigos de sequências finitas; checagem p-decidível de
> axiomas e regras — codificação usual). `ValidDer(e,β)` :≡ a **checagem
> explícita** da mesma noção — os **dois registros** (sintético vs explícito)
> da **mesma** relação (as formas (ii)/(iii) de §2.2 são, semanticamente, o
> **mesmo** caso; mantidas as duas para rastrear a origem da instância) —
> **(U1)**
> `∀e,β(Der(e,β) → ValidDer(e,β))` vale **por construção**. **(U2)**
> `∀e,β,v(Der(e,β) ∧ ¬eval(v,β) → ⊥)` — sonoridade, universal (`⊥` = falsum
> proposicional; (U2) é **contexto**, consumida só em §2.3). Ambas ∈ `T_PV`.
> `σ :≡ ∃e Der(e, Taut(α̂))` — **sentença-alvo fixa** (MINOR-5: constante
> `α̂`, não `α_M` variando). `T_S^¬ := T_S + ¬σ`.

## §2. N2.1 — a ameaça contra `σ`, em quatro formas (corrigido o slot)

### 2.1 N2.1-A (trivial, honestamente)

R-α ⟺ consistência de `T_S^¬` (compacidade). Não é lema intermediário — o
conteúdo está todo em (∗′) (§2.4).

### 2.2 A classificação (com o slot `Taut(α̂)` e tuplas — FATAL-1 corrigido)

Pelo lema da constante fresca (**(P)** — padrão), a ameaça a `¬σ` vem só de
**instâncias qf** `θ(t̄)` de universal-verdades `∀x̄θ` da linguagem estendida.
Classificação — a conclusão de `θ(t̄)` pode ser:

- **(i) sem `Der/ValidDer`**: só qf-verdades sobre a configuração — por
  `(S2)(S3)(S4)`;
- **(ii) `ValidDer(t̄', Taut(α̂))`** (conclusão; `t̄'` sub-tupla de `t̄`):
  **força testemunho de `ValidDer`** se `θ(t̄)` for verdadeira no modelo —
  caso crítico;
- **(iii) `Der(t̄', Taut(α̂))`**: caso crítico (ex.: `Axiom(β) →
  Der(can(β),β)` com `β := Taut(α̂)` — nota r5: `Axiom(Taut(α̂))` é **falso
  por construção**, o big-and não é axioma; o exemplo serve só para ilustrar
  a forma sintática, e o caso genuinamente-evitável é o do canto χ≡⊤ de
  §2.4);
- **(iv) `Der/ValidDer` no antecedente** (`Der(t̄',Taut(α̂)) → χ`): satisfeito
  **vazialmente** quando o antecedente é **falso** (sob a omissão) — MINOR-1
  corrigido (era "conclusão-alvo falsa": invertido).

**Suficência (declarada)**: por (U1), `¬∃e ValidDer(e, Taut(α̂)) ⟹ ¬σ` —
a omissão do nível `ValidDer` basta, **desde que** nenhuma **conclusão**
(ii)/(iii) seja verdadeira no modelo (MINOR-3: instâncias com antecedente
falso são vazialmente verdadeiras — o alvo é a conclusão) — o que a última
cláusula de (∗′) assegura
**diretamente** (a v3 dizia "a cláusula com slot `α̂` fecha (ii)+(iii)" —
falsa como justificativa; corrigido).

### 2.3 Os testemunhos da configuração (mantida, aceita)

`(α̂,m̂,π̂)` escolhidos na construção: `m̂` não-padrão (K); `π̂` com `Der_P(π̂,α̂)`;
`α̂` tautologia no modelo (sem falsificadores — coerente com (U2) e `Ref_P`).
**(P)**.

### 2.4 (∗′) — o lema, na forma correta **(C)**

> **Lema (∗′) (C).** Existe modelo `M_0` de `T_PV` (**só** universais
> verdadeiras — **não-elementar**: extensões elementares de ℕ forçam o
> testemunho via completude Π₂ verdadeira, `I1 A.7`) contendo `α̂,π̂,m̂` tal
> que: **(a)** `(S2)(S3)(S4)` verdadeiras neles; **(b)** **nenhum** `e ∈ M_0`
> tem `ValidDer(e, Taut(α̂))` — daí, por (U1), `M_0 ⊭ σ` (R-α realizada).
>
> **O que a construção deve evitar** (a análise §2.2): tornar **verdadeiras
> conclusões** (ii)/(iii). Toda universal-verdade tem forma `∀x̄(χ(x̄) →
> ψ(x̄))`; quando `ψ` contém (positivamente) `ValidDer(t̄', Taut(α̂))` ou
> `Der(t̄', Taut(α̂))`, a construção mantém o **antecedente `χ(t̄)` falsa** —
> a instância fica verdadeira **vazialmente** (compatível com `M_0 ⊨ T_PV`;
> exigir `θ(t̄)` falsa, como a v4 inicial fazia, contradiria `T_PV` — erro
> corrigido na rodada 4) e a conclusão permanece falsa — coerente com (b).
>
> **Canto χ≡⊤ (exigência de `N3`, MINOR-1/r5)**: universais com antecedente
> **trivial** (`χ≡⊤`; ex.: `∀x ValidDer(f(x),g(x))` — gerador plausível de
> provas de tautologias triviais) não têm antecedente a falsificar — ali a
> construção deve evitar a **coincidência denotacional** `g(t̄)^{M_0} =
> Taut(α̂)`. Ademais `Taut(α̂)` **não é termo** da linguagem (o big-and é
> exponencial) — a formulação de §2.4 é sintática onde o caso é **semântico**:
> em `N3`, constante de Henkin `τ̂ := Taut(α̂)` + cláusula semântica
> (\"slot-β avalia `Taut(α̂)` em `M_0`\") + separação de tamanhos (`at(α̂) ≈
> |α̂|` dá `2^{at(α̂)} > |t̄|^d` para todo termo `t̄`, grau `d` padrão).
>
> **Escopo**: |A|=1. **Exigência honesta para `N3` (MINOR-3 corrigido)**:
> (∗′) quantifica sobre **todas** as universal-verdades (não-enumeráveis);
> a rota honesta da construção é **compacidade/satisfatibilidade finita** —
> para cada subconjunto finito, um modelo (ou um argumento de consistência);
> **não** enumeração de uma axiomatização efetiva (que meteria Π₁-completo
> num r.e. — inalcançável). Registrado.

## §3. N2.2 — R-β (mantida; sem mudanças substantivas)

**(a′)**: compressão `P→EF` ⟹ `EF ⊢_{M_0} α` (aberta); aberta→fechada =
bloqueio N1 §0.3; "necessária" só em derivações com (S3). **(b′)**: `K.2`
mata o **esquema global** `BB`; particular = **(C)**.

## §4. N2.3 — o corolário no escopo que ele realmente tem (FATAL-2 corrigido)

> **N2.3′ (P)+(C em (∗′)).** Sob (∗′) e **Σ₁-sonoridade de ZFC**:
> **(i)** existe `M_0 ⊨ T_S` com `M_0 ⊭ σ` — o chifre **(β)** de N.2 é
> **realizável**;
> **(ii)** `ZFC ⊭ G_eff`, com `G_eff :≡ ∀M ⊨ T_S^eff (M ⊨ σ)` — o global
> **(α)-efetivo** (todo modelo satisfaz σ; sinal **exigido na r4 e aplicado
> nesta v5**) — e
> **`T_S^eff ⊆ T_S` recursivamente axiomatizável** (ex.: axiomatização efetiva
> de `T_PV` provando o que o argumento usa + (S2)(S3)(S4)).
>
> **Prova.** (i) por (∗′) — `M_0 ⊨ T_S` e `T_S ⊨ T_S^eff` (à parte). (ii)
> reductio: `ZFC ⊢
> G_eff` + completude formalizada de `T_S^eff` (r.e.) ⟹ `ZFC ⊢ ∃p
> Proof_{T_S^eff}(σ)` — sentença **Σ₁ aritmética** (σ fixo, MINOR-5) —
> Σ₁-sonoridade de ZFC ⟹ `p` **existe realmente** ⟹ `T_S^eff ⊢ σ` ⟹ todo
> modelo de `T_S^eff` (inclusive `M_0`) tem testemunho ⟹ **contradiz (∗′)**.
> ∎
>
> **O que N2.3′ NÃO diz (honestidade — FATAL-2 corrigido)**:
> **(a)** nada sobre o global sobre o `T_S` **completo** — `T_PV` é co-r.e.
> (falsidade de `∀xθ` = contador-exemplo, Σ₁) **e Π₁-completo** (incompletude
> aritmética), logo não r.e. (MINOR-2 corrigido) — a rota Σ₁ não existe lá;
> **(b)** o lado oposto — "ZFC prova que **todo** modelo de `T_S` omite" —
> é **compatível** com (i)+(ii) e **não foi excluído** (poderia até ser
> verdadeiro); **(c)** logo o que (i)+(ii) entregam é: o chifre (β) é
> realizável, e a rota "ZFC decide pelo **global (α)**" está **bloqueada no
> escopo efetivo** — a dicotomia N.2 não fecha por ZFC **nessa rota**; as
> demais rotas (decidir (C1′) diretamente; compressão+montagem particular)
> permanecem **(C)**.

**Documentação do erro da v3**: o salto "(ii)⟹ nenhum chifre fecha" confundiu
`G_eff` (mais forte: mais modelos) com `G_full`, e Σ₁-sonoridade (só para
Σ₁ aritméticas) com sonoridade total — corrigido em (a)–(c).

## §5. Ressalvas

1. **(∗′) (C) = R-α** — construção via **compacidade** (N3), não enumeração.
2. **Escopo R1/`q`-total** (herdado; Q1 da carta).
3. **Σ₁-sonoridade de ZFC**: declarada (padrão).
4. **N2.3′**: escopo `T_S^eff`; lado (β)-global não excluído — declarado.
5. **`∃e` sem limitador**: irrelevante.

## §6. Checklist (status neutro; referee julga)

| # | Afirmação | Status | Onde |
|---|---|---|---|
| 1 | `Der`/`ValidDer` definidos; (U1) por construção; (U2) universal | (P)+(A) | §1 |
| 2 | lema da constante fresca; quatro formas com slot `Taut(α̂)` e tuplas | (P) | §2.2 |
| 3 | suficência via (U1) | (P) | §2.2 |
| 4 | (∗′): (a)+(b); evitar (ii)/(iii) **no enunciado semântico-corrigido (§2.4, χ≡⊤ incluído)**; não-elementaridade; rota compacidade | **(C)** | §2.4 |
| 5 | N2.2(a′)/(b′): retrações/rebaixos mantidos | (P) | §3 |
| 6 | N2.3′: (i) modelo omitente; (ii) `G_eff` não-demonstrável (Σ₁) | (P)+(C) | §4 |
| 7 | N2.3′: lado (β)-global não excluído; `T_S` completo fora do alcance | honesto | §4 |

## §7. Veredito e próximos passos (v5)

**Veredito (honesto)**: após **cinco** rodadas de referee (RECOMENDADO na r5),
o que está **provado**:
a classificação da ameaça a `σ` (quatro formas, slot correto, tuplas); a
suficência da omissão de `ValidDer` via (U1); o corolário **no escopo que
tem** — modelo omitente (chifre (β) realizável) + não-demonstrabilidade do
global **efetivo** (Σ₁); e o mapa honesto do que **não** se provou (global
completo; lado (β)-global; (∗′) em si). O que é **(C)**: (∗′) = R-α (rota
compacidade, `N3`); montagem particular (R-β).

**Próximos passos**: (1) **`N3`**: construção de (∗′) por compacidade
(modelos finitos de sub-teorias + amalgamação — frente nova), incorporando o
**canto χ≡⊤** (§2.4 — coincidência denotacional `g(t̄)^{M_0} = Taut(α̂)`) e a
formulação semântica com `τ̂` (exigências da rodada 5); (2) acoplar à resposta
de Krajíček (Q1 da carta).

**Lacunas honestas**: (∗′) **(C)** = R-α; montagem particular **(C)**; escopo
`q`-total; `T_S` completo fora da rota Σ₁.

Referee rodadas 1–4: `N2_residuals_referee.md` — **rodada 5: RECOMENDADO**
(v5 responde, com os menores da r5 aplicados).

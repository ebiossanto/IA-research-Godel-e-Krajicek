# Referee Hostile — N3 rodada 2 (movimento (ii) executado)

**Data:** 20/11/2026 · **Rodada:** r1 desta entrega (a frente N3 não tinha
referee próprio antes) · **Alvo:** `N3_construction_compactness_chi_top.md`
§7 + `n3_hsepar_instance.json` + `n3_hsepar_certificate.json`

---

## A. Achados

### A1 (GRAVE) — "Acoplamento desacoplado" está correto?
A §7.1 afirma que o contraexemplo r2/LP afeta só o ramo `Res(k)` e não a
projeção de resolução que H-separ usa. Conferência: H-separ (§4.1) diz
"separação via **Lema 4.1**" — Lema 4.1 = recorte de **resolução+enfraquecimento**
(`C_disjuncao` §2.2) ✓; Teorema 4.3 (incondicional, RECOMENDADO) ✓; r2
contraexemplo = `Res(k)` com ∧-intro (C2) ✓ sistemas distintos ✓;
`gk_dd_cert` implementa exatamente o Teorema 4.3 ✓ (teste T2/D2 com
enfraquecimento misto ✓).

**Resposta:** ACEITO — o desacoplamento é correto. **Ressalva registrada:**
o Teorema 4.3 é (P) RECOMENDADO (interno) — H-separ herda o mesmo status
epistêmico (não vira (A)); a §7.1 diz "(P) executável", não "(P) provado
externamente" ✓ linguagem adequada. ✅

### A2 — A instância de regressão modela fielmente "separação de tipo"?
A §7.4/§7.2 é honesta: modelo **finito do mecanismo** (lado leal inconsistente,
lado `χ_⊥` SAT), π misto, extração do lado leal. A §7.2 lista o lift como (C)
e a §7.4 declara "Não demonstra: o lift (3)".

**Resposta:** ACEITO com ressalva — a equivalência "lado1 SAT ≡ tipo `χ_⊥`
consistente" é uma **abstração proposicional** (as cláusulas `[3,4],[-3]` não
são as fórmulas (S2)(S3)(S4) reais) — declarado como "mecanismo N2" no
próprio JSON e na §7.4. Pendência r3: frase explícita "abstração, não
instância das (S2)(S3)(S4)" no JSON (1 linha). ✅ com pendência.

### A3 — Lema de constantes: trivialidade vs. valor
A §7.3 é elementar (contagem de aridades). É "bispo horizontal" mesmo?

**Resposta:** o checklist pedia exatamente "computar o número de constantes
(mínimo m) … função de |a_i|" — o lema entrega o bound `Σa_j + L` e
justifica a instância de Łoś. **Não é profundo, é obrigatório** — marcado
(P) com prova de2 linhas ✓ sem inflação de status. ✅

### A4 — Q4/H-χ: a §7 mantém a pendência externa correta?
Sim — §6 revisado lista Q4 como externo pendente e aponta o follow-up
(caminho A). Nenhuma promessa de fechamento. ✅

### A5 — Checklist §5: item1 marcado com base correta?
Sim — [x] com referência §7.3; item2 mantido [ ] com plano (§7.6-2);
item3 parcial declarado. ✅

---

## B. Veredito

**RECOMENDADO (r1)** com pendências r3: (i) frase de abstração no JSON da
regressão; (ii) ao fechar Q4, atualizar §7.2-(4).

**Escopo:** N3 permanece **(C)** — a entrega **não fecha** a frente; ela
(1) executa o movimento (ii), (2) localiza os dois bloqueios restantes
(lift §2.4 + Q4), (3) entrega mecanismo (P) executável + regressão + lema
de constantes.

**Proibição mantida:** nenhum claim de "M₀ construído", "χ_⊥ omitido" ou
fechamento de N/L2→L3.

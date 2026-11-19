# C2 — Teste LP da família alternante: critério decidido (RETRACAO da via LP)

**Data:** 19/11/2026 · **Classificação:** **(P)** experimento + teorema próprios ·
**Nível Ten-Proofs:** N1 (script reproduzível) + N2 (execuções desta máquina) ·
**Mandato:** `C2_r2_G1_contraexemplo.md` §5 — *critério-LP*: a família alternante
produz refutações `Res(2)` linha-puras? · **Ferramenta:**
`gk_alternating_family.py` (seed `20261119`)

**Saídas:** `gk_alternating_family_t6_n5.{json,csv}` (principal),
`gk_alternating_family_t2_n5.{json,csv}` (contraste).

---

## 1. Veredito executivo

1. **Critério-LP responde MISTO → RETRAÇÃO da via LP para a rota negativa**
   (regra do r2 §5), por dois caminhos independentes:
   - **(Nec) Teorema de Necessidade (§4):** toda família alternante com π
     polinomial é **necessariamente impura** nos pontos em que o lado insat é
     difícil para `Res(k)` — logo C2.2′ (linha-puro) **não se aplica** ao
     reductio;
   - **Candidato `(γ, REF_t(γ))` falha em alternar para t poli (§3):**
     empiricamente **0/92** γ-insat alternaram com t=6 (a alternância observada
     de8% é só o lado γ-SAT); teoricamente exige `t ≥ ref-length(γ)`, que é
     ilimitado.
   *Escopo (referee A2):* a retratação é **incondicional para o candidato
   testado** e **condicional (via Nec)** para famílias com lados difíceis;
   famílias sem lados difíceis no domínio permanecem **abertas, não
   testadas**.
2. **C2.2′ permanece teorema próprio (P)** — apenas **inaplicável** à rota
   negativa. **C2.2** (promessa original) segue **(C)** — única via restante,
   com o contraexemplo r2 como evidência negativa para projeção.
3. O reductio "DD∈P ⟹ P=NP" **não pode ser entregue por esta via** — resultado
   negativo honesto (a rota era "boa demais para ser verdade").

---

## 2. O candidato testado e a codificação

**Candidato (o do próprio projeto, `C2_ddres_k` §4):** dado γ (CNF sobre
`x₁..xₙ`):

- `Λ₁ := γ` — insat ⟺ γ ∈ UNSAT ✓;
- `Λ₂ := REF_t(γ)` — CNF de variáveis `y` codificando *"existe refutação
  Res(γ) com ≤ t **linhas**"*: `y_{j,C}` = "linha j é a cláusula C";
  restrições: (1) `y_{t,∅}`; (2) **exatamente-um** C por posição; (3)
  `y_{j,C}` → folha (C∈γ) ∨ cópia de `y_{j',C}` (j'<j) ∨ corte
  `c₁=S₁∪{l}, c₂=S₂∪{¬l}` com `S₁∪S₂=C` (pares por Tseitin auxiliar).

**Semântica correta = LINHAS** (não profundidade): com exatamente-um por
posição, `REF_t` = "sequência de ≤ t linhas" — **sem repetição WLOG** (se
existe refutação ≤ t, existe uma sem repetição, e é representável com
premissas em posições anteriores) — validação **fronteira exata**:
γ = `{[1,2],[1,-2],[-1]}` (refutação mínima =6 linhas): **REF_5=UNSAT,
REF_6=SAT** ✓; γ-SAT ⇒ REF_t=UNSAT ∀t ✓.

**Integridade do processo (N1):** a codificação passou por **5 bugs
encontrados e corrigidos pela validação** antes de confiar nela — (i)
off-by-one nos negativos de `sample_gamma` (var6 poluía γ); (ii) filtro de
tautologia errado em `all_clauses` (excluía `{1,-2}` válido — bug-raiz do REF
insatisfatível); (iii) cópia/corte emitidos como AND em vez de OR; (iv)
pares de corte sem as condições de sonsidade `l∉S₁, ¬l∉S₂` (permitia
derivados espúrios); (v) profundidade em vez de linhas. Cada bug teve teste
de sanidade que o expôs — o encoder final passa na fronteira exata acima.

---

## 3. Resultados (N2, seed `20261119`, n=5, m∈[25,45],100 amostras)

| Métrica | **t=6 (principal)** | t=2 (contraste) |
|---|---|---|
| γ-insat na amostra | 92/100 | 92/100 |
| **T1 alternância** (exatamente1 lado insat) | **8/100 (8%)** | 8/100 (8%) |
| — falhas (ambos insat: γ-insat com ref > t) | **92/92 γ-insat** | 92/92 |
| **T2 provas da união com ≥1 linha MISTA** | **0/100** (48.945 adições) | 0/100 (25.493 adições) |
| **T3 controle** (lado insat sozinho) com mistas | **0/100** | 0/100 |
| sha256 do CSV | `a26a56fceaad7629…` | `4b5a797baa045a7a…` |

**Leitura:**
- **T1:** a alternância observada é **exatamente o conjunto dos γ-SAT**
  (100−92=8). **Nenhum γ-insat alternou**: `REF_6` não cabe nas refutações
  desses γ (≥…todas >6 linhas). A igualdade t=2 vs t=6 confirma: os8 são o
  lado SAT (γ-insat falham em qualquer t < ref-length). **O candidato só
  "alterna" pelo lado trivial.**
- **T2:** provas do solver saem **puras** — mas porque γ deste tamanho são
  **fáceis** (prova pura curta existe; o solver refuta o lado sozinho e não
  precisa misturar). Isso **não** resgata a via: para γ difíceis (§4) prova
  pura curta **não existe**.
- **T3:** controle confirma que a detecção de mistas está calibrada (0
  esperado,0 obtido).

---

## 4. Teorema de Necessidade (P) — por que a via LP morre em γ difíceis

> **Teorema (Nec).** Seja `F` uma família alternante p-tempo: para toda γ,
> `(Λ₁(γ), Λ₂(γ))` disjuntas, refutação `Res(k)` **π(γ) de tamanho poli**
> construível, e **exatamente um** lado insat com `Λ₁` insat ⟺ γ ∈ UNSAT.
> Se existe γ₀ ∈ UNSAT tal que `Λ₁(γ₀)` exige refutações `Res(k)` de tamanho
> **superpolinomial**, então **π(γ₀) não é linha-pura**.

**Prova.** Suponha π(γ₀) linha-pura. Como as variáveis são disjuntas e as
regras de `Res(k)` com linhas puras preservam o lado (corte: pivô
compartilhado ⇒ mesmo lado; enfraquecimento: só termos do lado; ∧-intro: pais
e resultado puros ⇒ mesmo lado — ver C2.2′ §4), a parte acessível de π a partir
da raiz `∅` é uma refutação `Res(k)` de `Λ_{i*}` com `≤ |π|` linhas. Por
alternância, γ₀ insat ⇒ `Λ₁(γ₀)` é o único lado insat ⇒ `i*=1` ⇒ refutação
`Res(k)` superpolinomial **de `Λ₁(γ₀)` com `≤ |π|` = poli linhas** —
contradição. ∎

**Corolário (critério-LP):** para famílias cujo domínio contenha lados
insat difíceis (como exige o caso de uso "γ arbitrário" da redução), o
critério-LP do r2 §5 responde **MISTO** ⇒ **RETRAÇÃO da via LP** para a rota
negativa. `C2.2′` continua válido como teorema com sua própria promessa, mas
**não entrega o reductio**.

**Reserva honesta (Nec):** o teorema é condicional à existência de γ₀ com
lado difícil no domínio da família. Para `Λ₁ = γ` isso é a pergunta "existem
CNFs difíceis para `Res(k)`?" — Garlík (Thm 1(i)) fornece famílias difíceis
para **todo** `k≥1`, mas como `Aₙ` (sempre-insat, não-flipante); a existência
para o domínio flipante exige os tais γ — **não verificada aqui (lacuna)**.
Mesmo assim, o item1-§3 (candidato REF_t não alterna) é **incondicional** e
independente.

---

## 5. O que fica de pé (reclassificação final)

| Item | Status |
|---|---|
| C2.1 (largura-k, resolução) | **teorema** (inalterado) |
| C2.2′ (promessa linha-puro) | **teorema (P)** — standalone, inaplicável ao reductio |
| C2.2 (promessa original) | **(C)** — única via restante da rota negativa; evidência negativa = contraexemplo r2 + **Nec** |
| Candidato `(γ, REF_t)` (C2.3) | **RETRAÍDO como construção p-tempo alternante** (não alterna para t poli) |
| Rota negativa `DD∈P ⟹ P=NP` | **via LP retraída**; via C2.2 permanece (C) |

## 6. Próximos passos

1. **Referee** (obrigatório) — foco: semântica de linhas do REF (§2), Nec
   (§4) e a reserva de domínio difícil.
2. Se Nec+REF sobreviverem: registrar em `C2_ddres_k.md` v6 a retratação da
   rota LP e reorientar para C2.2 (promessa fraca) ou para a via **A**
   (auditoria externa/follow-up), que não depende deste bloqueio.
3. (Opcional, lacuna Nec): verificar se existem CNFs de `n` variáveis
   difíceis para `Res(2)` com `n` pequeno — evidência finita pro Nec.

---

*Reprodução:*
```
python gk_alternating_family.py --n 5 --t 6 --samples 100 --m-min 25 --m-max 45
python gk_alternating_family.py --n 5 --t 2 --samples 100 --m-min 25 --m-max 45
```
Validação do encoder: `build_ref_t({[1,2],[1,-2],[-1]},5,t)` → t=5 UNSAT, t=6 SAT.
Referências: `C2_r2_G1_contraexemplo.md` (r2 §5) · Garlík CCC 2024 Thm 1/18 ·
`gk_alternating_family.py`.

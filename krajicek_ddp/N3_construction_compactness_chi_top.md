# N3 — Construção (∗′) via compactness + χ≡⊤ (canto)

> **✅ ATUALIZAÇÃO 20/11/2026 (rodada 2 da frente):** o movimento **(ii) do
> §6 ("fechar H-separ via leitura literal de [K19 5.7] com a frente C2")
> FOI EXECUTADO** — e com desfecho melhor que o previsto: ver **§7**.
> Entregas: (a) **mecanismo de H-separ upgradeado para (P)** (Teorema 4.3
> executável via `gk_dd_cert.py` — a projeção é incondicional em resolução);
> (b) **instância de regressão executável** `n3_hsepar_instance.json` →
> `n3_hsepar_certificate.json` (lado leal extraído,4/7 linhas, verificado);
> (c) **Lema de constantes frescas (P)** — item1 do checklist §5;
> (d) acoplamento H-separ×C2 **desacoplado**: o contraexemplo r2/LP afeta o
> ramo `Res(k)`, não a projeção de resolução que H-separ usa. **Q4 (H-χ)
> segue pendente** — o lift model-teórico de §2.4 continua (C).

> Frente **N3**, aberta em `N2_residuals_RA_RB.md` (v5, rodada 4 ⟶ 5) e no
> relatório consolidado §0.1 (versão honseta): o lema (*′) sustenta a frente
> N2.1 (N2.1-A) e a frente N (K/N1), e é hoje (`N2_residuals_RA_RB.md` §0.1
> item 1) marcado como **(C)** — construção não-elementar. Esta entrega produz
> a **tentativa de construção** do lema (*′) e audita **o que** é (P),
> **o que** é (C) e **o que** permanece (H) — sem fechar indevidamente a
> frente. 13/10/2026.
>
> Marcação: (A) = fonte; (P) = próprio (verificado a partir de premises (A));
> (C) = conjectura; (H) = leitura a conferir em fonte externa; (R) = retraído.
> Contexto: `N2_residuals_RA_RB.md` (todas as refs "∗"); `N1_refutacao_interna_CN_s.md`
> §0.3; `J1_Qcompactness_M0.md` §3 (K, K.2); `I1_Qcompactness_ultrapoderes.md` (A.7); `F2_versao_finita.md`
> (L26–27); `G2_semente_Fsent.md` §2.3; `C_disjuncao_viavel.md`; carta
> `CARTA_FINAL_RECEBIDA.md` (terminologia 5).

## 0. A tarefa

Dadas
- `T_S = T_PV + (S2)+(S3)+(S4)` (formalizada em `N2_residuals_RA_RB.md` §1),
- `a = ⋀_{i<m} a_i`, `p : P → a`, sentenças-alvo e o **objeto**
  `s = ¬∃e Der(e, Taut(a^))` (terminologia 5, fechamento por carta Q1),
- a ameaça `(ii)/(iii)` (formas 4 `ValidDer/Der`) compilada em N2 §2.2,

a frente **N3** pede:

> (**∗′**) construir, sob compacidade, um modelo `M₀ ⊨ T_S` que
> (a) omite o tipo adversarial (canto c_N_s) e
> (b) provê a **chave (∗′)**:
>   χ (corner) ≡ ⊤ (a chapeleira verídica do canto adversarial), que
>   `Taut(a^)`-sentenças indizes específicos não colapse (ou que o derive-true
>   sejam todos o mesmo lado do gap).

(*′) é o **lema** que N2/A terra (P)+(C) afirma existir; essa frente torna
a prova do lema on-construction. Esta N3 não fechá, mas produz a **forma
exata** do argumento, os **placeholders** e o **teste de regressão** ao qual
ela será submetida quando a carta Q2–Q4 responderem.

### 0.1 Status honesto (preview)

| Sub-bloco | Status a priori | Status após esta entrega |
|---|---|---|
| Setup de compacidade (linguagem, constantes) | (C) | (P)-esboço → **(P) Lema de constantes (§7.3)** |
| Introdução de χ≡⊤ como canto universal | (H) | (H) (ainda a calibrar per Q2/Q4) |
| Extensão conservadora `T_S^∗` | (C) | (C) (aberto) |
| **Mecanismo de H-separ (projeção)** | (H) (via H-corte) | **(P)** — Teorema 4.3 executável (§7.1); regressão ✓ (§7.4) |
| **Lift model-teórico (χ_⊥ omittível em todo M)** | (C) | (C) (aberto em N2/§2.4 — localizado) |
| Conclusão "M₀ omite + preserva lado" | (C) | (C) (aberto em N2 fronteira) |
| Contraexemplo/regressão | (P) | (P) — **consolidado: instância executável commitada (§7.4)** |
| Veredito sobre a frente N | (C) | (C) |

**Subsítese:** esta entrega **não** fecha N3; ela deixa em claro o **mapa do
gap real**, que é justamente o (O)-elementar análogo ao que C2 exigia (O5).

## 1. Setup e preambulos

### 1.1 Linguagem-fonte e teorias

`ℒ_S = ℒ_IV + (S2)^∨ + (S3)^∨ + (S4)^∨` com
`(S2)` definindo a *safe predicate* (`safe(x,a)`), `(S3)` a provabilidade
de "decisão correta" via theorema `(S4)` (canto duplo).

`χ : ℒ_ℒ` é o **predicate de canto** que assume `0/1` em termos técnicos (ou
tentativas de omitir o tipo), e `χ≡⊤` é a sentença `∀x (χ(x) = ⊤)` (a
chapeleira universal) — abreviação "canto ativo" (calibração pendente: Q4
objeto).

### 1.2 A "classe dos modelos omitentes" `K`

`K(T_S) = { M ⊨ T_S c/ M omite o tipo advertorial χ_⊥ }`, onde
`χ_⊥` é o tipo consistente (singleton sem conclusão de `ValidDer`/`Der` —
ver N2 §2.2 (i)). A frente **K** diz: sem coleção finite de falsificadores
(K.1), e (K.2) `T_PV+BB+(S2)+(S3)+(S4) ⊢ ⊥`. N3 segue (K.2) (P)+(A).

## 2. A extensão compacta (!)

### 2.1 Linguagem expandida e constantes

`ℒ_S^∗ = ℒ_S + { x_l : l ∈ ℕ }` (constantes novas, uma por elemento da
ameaça/canto potencial).
Para cada `l`, introduzir a **sentença de canto**:
`χ_⊥(x_l) → ⊥`
que fuerza cada canto incubar a ser `⊤` (ou, o que é equivalente, nega o
corner c_N_s do que "omita").

### 2.2 A teoria compacta `T_S^χ`

`T_S^χ = T_S ∪ { χ_⊥(x_l) → ⊥ : l ∈ ℕ } ∪ { χ≡⊤ }`

A fórmula `χ≡⊤` (corner) é broadcast no nível do catálogo de tipos, não
da resolução — ela é a **restrição bridge L2↔L3** do esquema de modelos
omepresentes.

### 2.3 Teorema-base de compacidade (P)

> **(P) Compacidade Łoś** (omonômo, (A)): se todo subconjunto finito de
> com `T_S^χ` é contatível (cada subconj. tem M ⊨ ...), então `T_S^χ` tem
> modelo (por compacidade).

A parte "o argumento é P-aplicável" é (P) por standard.

### 2.4 O gap crucial (o que impded fechar)

A compacidade exige checar todo subconjunto finito de `T_S^χ`. A verificação
para subconjuntos que **exigem χ≡⊤é global** — por exemplo:
- O subconjunto `{ T_S ; χ_⊥(x_1)→⊥ ; χ≡⊤ }` pode ser contatível se
  (i) `M ⊨ T_S` e `χ_⊥(x_1)` não esteja em M; isso exige:
  (h) a separação do tipo χ_⊥ do modelo finite approval `M_N` — o
  "separação extensão do tipo" — que é **exatamente** o que define a
  **omissão de tipos ilimitada**.

A **consistência do lado leal do tipo χ_⊥** é a pergunta fundamental:

> χ_⊥ é omitível em toda `M ⊨ T_S`? Em particular, quando a linguagem contém
> funções que silenciosamente produz χ_⊥ via (S3)+(S4)?

Isto é **pergunta de (C)** — e não segue trivialmente de K.2 (que é de
consistência global/pre-sapiencia do re-negativo) ou da compactness. A
resposta depende de:

- Se `T_S ⊢ ∃! x (χ_⊥(x)→⊥)` (correctness theorem) — pode ser fechado pelo
  Lema 4.1 de `C_disjuncao_viavel` (uma versão p-time da resolução) se (H)
  valer.
- Se o corner χ≡⊤ é 'harmless' — definição em 1.1; essa é a calibração Q4.

## 3. Construção de M₀ (esboço)

### 3.1 Henkin + compacidade (P-esboço, contaminado pela (C) acima)

Assumindo que a separação 2.4 se resolve com "sim", construa `M₀` como
follow-up:

1. **Henkin closure**: dado `T_S^χ`, expanda para uma teoria completion
   Henkin `T_S^{χ,+}` com testemunhas (constantes frescas).

2. **Model M₀** = modelo de `T_S^{χ,+}` (por extensão compacta na
   extensão da linguagem).

3. **Omólogo** se `M₀ ⊨ χ≡⊤` (cor (c_N_s) é sempre `⊤`), e os χ_⊥ tipistas
   são omitted — isto segue da construção via o interlúdio 2.4 (se valer).

### 3.2 Verificação da propriedade (a) — "omissão do tipo adversarial"

`T_S ⊢ ∃!x (χ_⊥→⊥)` necessita:
- `T_S ⊢ χ≡⊤` (corner — marcada (C) até Q4 fechar)
- e a separação 2.4.

Se ambos valerem, M₀ tem (a). O "se ambos" é a ranhura de (C).

### 3.3 Verificação da propriedade (b) — "preserva o lado"

`M₀` preserves o "lado do gap" iff não existem dois modos de provar
`χ≡⊤` em `T_S` vs no universo de `M₀`. Isto é equivalente ao (O4) de C2
(assimetricidade da truncagem) — see `C2_O1_O5_K19_5_7.md` (O4).

#### 3.3.1 Quem é o "canto L2→L3"? (pilar institucional)

O `χ≡⊤` canto é o **conjunto bridge** que liga a estrutura de fórmulas
(L1 — tautologias, resolução, etc.) às estruturas de modelos (L2) que
aproximam a fronteira L3 (complexidade). Conforme §9.1 - §9.3 do
`RELATORIO_CONSOLIDADO.md`, o bridge L2→L3 **permanece aberto** — a N3
construção é justamente um dos caminhos para tentar fechar o bridge
unidirecional (L2 → L3, não L3→L2).

## 4. Hipótese e matricularização

### 4.1 Hipóteses pendentes

- **H-χ**: `χ≡⊤` é consistente com `T_S` (a calibração Q4 responderá).
- **H-om**: tipo χ_⊥ é omittível em toda `M ⊨ T_S` (2.4).
- **H-separ**: separação extensão do tipo vale via Lema 4.1 — **requer**
  (H-corte) de C2 `C2_O1_O5_K19_5_7.md` §2.
- **H-c corners**: foram verificados em `N2_residuals_RA_RB.md` §2.1? Rótulos
  (ii)/(iii) tratados como um-only (U1) — confirmados.

### 4.2 Consequência de cada "fechamento"

| Fechamento | (N2) afetado | (N) afetada |
|---|---|---|
| H-χ = falso | K.2 contradição concluida; (a) falha | N-chifre-2 fechado (anti-lógica) |
| H-om = falso | (*′) falha: a ameaça (ii) perde senso | N1-escopo permanece aberto |
| H-om = true, H-χ = true | (∗′) (P) — frontier fechado em (P) | "a rota ZFC decide pelo global" pode fechar via (N2.3 (i)+(ii)) |
| H-separ dependente de H-corte | se (H)-corte falso → N3 re-abre e C2 re-abre simultaneamente (acoplamento L2-L3) |  |

## 5. Teste de regressão N3 (protocolo Ten-Proofs, Selo N3.0)

Para alcançar (P) futuramente, a entrega precisa:

- [x] **Bispo horizontal na compacidade**: computar o número de constantes
  (mínimo m) para cada literal `a_i` em `a` em função de
  `|a_i|`. (Level 1 — definição, Prova do teorema de Łoś aplicável ao
  subconjunto finito com esse bound.) → **FEITO em §7.3 (Lema de constantes
  frescas, P)** — bound ≤ Σ aridades + L por subconjunto finito.
- [ ] Verificar que `T_S^χ` é consistente para cada subconjunto finito com
  o bound de 1. (Level 2 — verification, `lea build` ou model-checker
  para instâncias-pequena.) → **pendente** (plano: §7.6-iv; requer as
  instâncias (S2)(S3)(S4) de `A_teoremas_exatos.md`/`CONTEXTO_COMUM.md`).
- [ ] Produzir o ` certificate.json` (ten-proofs, schema
  `ten-proofs-certificate/v1`) quando (e somente quando) as duas anteriores
  fecharam com comando reproduzível + hash SHA-256. Enquanto, status
  permanece `pending`.
  *Parcial (20/11):* `n3_hsepar_certificate.json` = regressão do **mecanismo
  N2** (projeção/separação) — não é o certificado do lift (C).

## 6. Veredito (atualizado em 20/11/2026)

> A frente N3, por esta entrega (13/10) **e a rodada 2 (20/11, §7)**,
> permanece **(C)** com construção honesta — porém com o **mapa do gap
> agora preciso**: o **mecanismo** de H-separ (projeção/separação finita)
> é **(P) executável** (§7.1/§7.4); o que permanece (C) é exatamente **dois
> itens localizados**: (1) o **lift** "χ_⊥ é omittível em toda `M ⊨ T_S`"
> (§2.4 — a pergunta se (S3)+(S4) **produzem** χ_⊥) e (2) **H-χ** (canto
> χ≡⊤ — calibração Q4, externa).

**Lacunas honestas:**
- 2.4 não provado (aberto) — lift (C);
- 4.1 (H-χ) não provado (Q4 pendente — follow-up = caminho A);
- Fechar H-om via compactness não refutado;
- "N fechado" = dependente.

**Próximo epistemic move (revisado):**
1. ~~(ii) fechar H-separ via leitura literal de [K19 5.7] com a frente C2~~
   **✅ EXECUTADO — ver §7** (mecanismo (P), acoplamento desacoplado);
2. **(i) Q4** — pendente externo (follow-up Q2–Q4, janela vencida);
3. **(iv) NOVO — Level-2**: model-checker de consistência finita de
   `T_S^χ` em instâncias pequenas (checklist §5 item2) — usando as
   instâncias (S2)(S3)(S4) de `A_teoremas_exatos.md`;
4. **(iii) Ten-Proofs**: certificado completo quando (H-χ)+(H-om)
   fecharem; a regressão do mecanismo já está commitada.

---

## 7. Rodada 2 (20/11/2026) — movimento (ii) EXECUTADO

### 7.1 H-separ × C2: acoplamento DESACOPLADO (favorável)

O §4.1 marcava H-separ como "requer **(H-corte)** de C2". Os resultados da
frente C2 (rodadas 1–3, 19–20/11) mudam o quadro:

| Evento C2 | Efeito sobre H-separ |
|---|---|
| **r1**: texto exato de [K19 5.7] (regras de `Res(k)`) obtido | `(H-corte)` = **(A)** (regras) + **(P)** (projeção) |
| **r2**: contraexemplo — projeção por subconjunto **falha** em `Res(k)` sob promessa fraca | bloqueia o ramo **`Res(k)`** (C2.2) — **não** a projeção de resolução |
| **r3/LP**: via LP retraída; Nec | idem — ramo `Res(k)` |
| **`gk_dd_cert.py`**: Teorema 4.3 **executável** (DRAT/DAG/provador + verificador independente; teste7/7) | **mecanismo de H-separ = (P)** — incondicional em resolução |

**Conclusão:** a projeção que H-separ usa é o **Lema 4.1/Teorema 4.3 de
RESOLUÇÃO** (com enfraquecimento) — teorema **incondicional**
(`C_disjuncao_viavel.md` §4, RECOMENDADO) e agora **verificável por
máquina**. O contraexemplo r2 e a retratação LP pertencem ao ramo `Res(k)`
(C2.2) — **ramos distintos**. O "acoplamento L2–L3" do §4.2 resolve-se a
favor: **H-separ perde a dependência de (H-corte)**; permanece (C) só o
lift (§2.4) e H-χ (Q4).

### 7.2 O que H-separ precisa — formulagem final

Para cada subconjunto finito `F ⊆ T_S^χ`:
1. **(P)** a projeção separa a refutação de `F` no lado leal (Teorema 4.3 +
   `gk_dd_cert` — demonstrado na regressão §7.4);
2. **(P)** o lado adversarial (tipo `χ_⊥`) é **consistente** (SAT no
   instância finita — "tipo consistente" = o que a omissão exige);
3. **(C)** o lift: vale para **todo** F (compacidade) ⟹ `χ_⊥` omittível em
   toda `M ⊨ T_S` — **a pergunta §2.4** ("(S3)+(S4) produzem `χ_⊥`?");
4. **(H)** H-χ (canto `χ≡⊤` — Q4).

### 7.3 Lema de constantes frescas (P) — item1 do checklist §5

> **Lema (P).** Seja `F ⊆ T_S^χ` finito com k sentenças universais
> `∀x̄_j θ_j` (aridade `a_j ≤ |θ_j|`) e sentenças de canto
> `{χ_⊥(x_l) → ⊥ : l ≤ L}` (mais `χ≡⊤`, sem constante). Então a extensão
> de Henkin/frescas de `F` usa **≤ Σ_j a_j + L** constantes novas — em
> particular ≤ `k·N + L` se `|θ_j| ≤ N`.
>
> **Prova.** Cada universal instancia-se com no máximo `a_j` constantes
> (lema da constante fresca — padrão, (A)); cada canto indexado `l` usa
> exatamente `x_l`; `χ≡⊤` é sentença. A ordem das adições é irrelevante
> (soma comutativa). ∎
>
> **Consequência (A):** o subconjunto finito é satisfatível-sobrevivente
> com cardinalidade finita de símbolos → a instância de Łoś/compacidade é
> aplicável **com bound explícito** — o "bispo horizontal" do checklist
> está formalizado.

### 7.4 Regressão executável do mecanismo (checklist §5, parcial)

- **Entrada:** `n3_hsepar_instance.json` — lado0 (leal, inconsistente),
  lado1 (adversarial/`χ_⊥`, **SAT = tipo consistente**), π **misto**
  (enfraquecimento cruza lados: `[1,3]`).
- **Saída:** `n3_hsepar_certificate.json` — **lado0,4/7 linhas**;
  verificador independente **ACEITO** (`gk_dd_cert.py verify`, exit0).
- **Demonstra:** a projeção **separa** a contradição do lado leal mesmo
  com π misto — exatamente o passo (1)+(2) da §7.2.
- **Não demonstra:** o lift (3) [(C)] — declarado.

### 7.5 Impacto nas hipóteses (§4.1 atualizado)

- **H-separ**: mecanismo **(P)** (era (H)-corte-dependente) — lift (C);
- **H-χ**: inalterado — **(H)**/Q4 externo pendente;
- **H-om**: inalterado **(C)** — agora identificada com a pergunta
  §2.4 ((S3)+(S4) produzem `χ_⊥`?);
- **H-c corners (U1)**: confirmados (N2 §2.1).

### 7.6 Próximos passos (rodada 3+)

1. **Q4** → follow-up Q2–Q4 (caminho A — item nº1 do projeto);
2. **Level-2**: model-checker de `T_S^χ` para instâncias finitas pequenas
   (checklist §5 item2) — encoder SAT de (S2)(S3)(S4) instanciados +
   canto, buscar modelo para cada F pequeno (evidência N2, não prova);
3. Ten-Proofs completo quando (H-χ)+(H-om) fecharem.

---

Referência cruzada:
- `RELATORIO_CONSOLIDADO.md` (§0.1 e §9.1-§9.3, L2↔L3 bridge aberto).
- `CONTEXTO_COMUM.md` (terminologias 1-6, em especial 5 e 6).
- `N2_residuals_RA_RB.md` (v5, escopo corrigido `(i)+(ii)`, frente N3 referenced).
- `C2_ddres_k.md` (H-corte, H-and, H-weakening; obrigações (O1)-(O5)).
- `CARTA_FINAL_RECEBIDA.md` (Q4, 'i₀' authoritative).
- `AUDITORIA_EXTERNA_DDRES_G-N.md` (checklist (a)-(e)).
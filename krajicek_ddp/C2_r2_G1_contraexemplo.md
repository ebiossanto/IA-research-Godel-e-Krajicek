# C2 rodada 2 — Contraexemplo a (G1), retratação do candidato r1 e Teorema C2.2′ (linha-puro)

**Data:** 19/11/2026 · **Classificação:** **(P)** próprio, verificado por máquina (N2) +
referee `C2_r2_referee.md` · **Mandato:** referee r1 §B ("para r2: resolver A3
(conflito de demandas: política com prova OU contraexemplo exaustivo) e A4
(pureza Res(k))") · **Ferramenta:** `gk_c2_projection_sim.py`
(seed `20261119`; saída reproduzível).

---

## 1. Veredito executivo

1. **(G1) RESPONDIDO COM CONTRAEXEMPLO (A3 resolvido na via do contraexemplo):**
   existe refutação `Res(2)` de15 linhas, **com a promessa puro-respeitadora
   satisfeita**, em que **todo algoritmo de projeção por subconjunto com
   escolha gulosa (e a versão de demanda ingênua) falha** — enquanto a resposta
   `i* = 1` **existe**. Reproduzível: `python gk_c2_projection_sim.py`.
2. **Candidato de fechamento r1 RETRACTADO** (honestidade): a "passada de
   demanda" e o algoritmo de filtro falham na instância da §2. A leitura
   "all-or-none por lado" é **falsa em geral** — cortes **consomem** membros de
   blocos.
3. **(G2) pureza:** o invariante de pureza das linhas-E **passou em1602/1602
   DAGs aleatórios válidos** + no contraexemplo até o ponto de falha — mas é
   **insuficiente** para o fechamento (a falha é de retenção, não de pureza).
4. **O que SOBREVIVE como teorema (P): C2.2′ — promessa de linha-pura**
   (§4): se **toda linha** de Π é de um só lado (exclui enfraquecimentos
   mistos), a extração é imediata e `DD_{Res(k)} ∈ P` sob essa promessa —
   prova curta (§4.3).
5. **C2.2 (promessa original) permanece (C)** com **evidência negativa** para
   a família de algoritmos de projeção por subconjunto.

---

## 2. O contraexemplo (N2 — verificação por máquina + manual)

**Variáveis:** `X₁ = {1,2}` (lado 1), `X₂ = {3,4}` (lado 2) · `k = 2`.
**Λ₁ (lado 1, UNSAT):** cláusulas `L2:{-1}`, `L6:{-2,+1}`, `L7:{+2}`,
`L11:{-1}`, `L12:{-2}`, `L13:{-1,+2}`, `L14:{-2,+1}`.
**Λ₂ = ∅.** *UNSAT de Λ₁:* `+1=F, +2=T` ⇒ `L6 = (-2 ∨ +1) = (F ∨ F)` falsa ✓.

**Refutação `Res(2)` Π (15 linhas, regras de Garlík §2):**

| # | Regra | Detalhe |
|---|---|---|
| L11,L12,L13,L14,L6,L7,L2 | folhas | cláusulas acima (todas lado 1) |
| L8 | ∧-intro | `L11={-1}`, `L12={-2}` ⟹ `{-1,-2}` (promessa: pais+resultado lado 1 ✓) |
| L10 | Cut | `L13 ∨ {+1}-parte` com `t={-1}`: `(L13∖{-1}) ∪ (L14∖{+1}) = {{+2},{-2}}`… estrutura: `A={{+2}}`, `B={{-2}}`, bloco `{{+1}}` ⟹ λ(L10) `{{-2},{+1},{+2}}` |
| L5 | Weakening | `L7={{+2}}` ⟹ `{{+2},{+2,+3}}` — **adiciona termo MISTO `{+2,+3}`** |
| L9 | Weakening | `L10` ⟹ `{{-3},{-2},{+1},{+2}}` — adiciona `-3` (lado 2) |
| L3 | Cut | `t={+2}`: `(L5∖{+2}) ∪ (L6∖{-2}) = {{+2,+3},{+1}}` |
| L4 | Cut | `t={-1,-2}`: `(L8) ∪ (L9∖{{+1},{+2}}) = {{-3},{-2}}` |
| L1 | Cut | `t={+2,+3}`: `(L3∖t) ∪ (L4∖{{-2,-3}}) = {{+1}}` |
| L0 | Cut | `t={+1}`: `(L1∖t) ∪ (L2∖{{-1}}) = ∅` ← raiz |

**Promessa puro-respeitadora:** o único ∧-intro é L8, com pais e resultado
puros do lado 1 ✓ — **a instância está na classe de C2.2**.

**Falha do algoritmo (máquina):** `G1 VIOLADO: retencao parcial do bloco em 4`
— em L4, o bloco exigido `{{+1},{+2}}` chega **parcial** a `E(L9) = {{+2},{-2}}`:
o corte intermediário **L10 consumiu `{+1}` como pivô do próprio bloco** (regra
remove o bloco da conclusão). Análise de demanda (manual, §3): **nenhuma
escolha de ramos em L10 produz `{{+1},{+2}}`** — o conflito de demandas do
referee r1-A3 é **real e irremediável por reordenção gulosa**.

**Por que a resposta existe:** `Λ₁` é UNSAT (acima) — `i*=1` está lá; a
projeção por subconjunto simplesmente **não consegue extraí-lo**. (Nota: a
falha NÃO é de pureza — as linhas-E permanecem puras; é de **retenção**.)

**Varredura N2:** `--n 3000` → **1602 DAGs aleatórios válidos passam todos os
invariantes (I1–I5, pureza)**; **1 falha G1** = a mesma instância do
contraexemplo (o gerador semeado a reencontra) — ou seja, a classe é rara
(≈0,06% dos DAGs) mas **existe**.

---

## 3. Por que a versão de demanda também falha (r1-A3 confirmado)

Demanda de L4: `{{+1},{+2}} ⊆ E(L9)` ⟹ `⊆ E(L10)` (L9 só remove/adiciona
termos de lado 2 via filtro). Ramos de L10 (premissas fixas `L13,L14,t={-1}`):
- **corte próprio:** `E = {{+2},{-2}}` — come `{+1}` ✗;
- **reuso L13:** `{{-1},{+2}} ⊄ λ(L10)` ✗ (contém `-1`);
- **reuso L14:** `{{-2},{+1}}` — tem `{+1}` mas **perde `{+2}`** ✗.
**Nenhum ramo entrega o bloco completo** — demanda **insatisfatível** em L10;
a insatisfatibilidade só "sobe" para L8 (reuso A3: `E(L8):={{-2}} ⊆ λ(L4)` ✗
para a demanda de L1). **Não há atribuição E válida neste DAG** para a
projeção por subconjunto — o que explica por que o guloso falha em **dois**
pontos (L4 e, sem o ramo L8-A3, L1).

---

## 4. O que sobrevive: **C2.2′ — Teorema sob promessa de linha-pura (P)**

> **Teorema C2.2′ (P).** Seja `Λ = Λ₁ ⊎ … ⊎ Λ_m` (CNF, variáveis disjuntas)
> e `Π` uma refutação `Res(k)` de `Λ` **linha-pura**: *toda linha de `Π` usa
> variáveis de um único `X_i`* (exclui enfraquecimentos mistos). Então existe
> algoritmo `O(|Π|·m)` que devolve `i*` com refutação `Res(k)` de `Λ_{i*}` com
> `≤ |Π|` linhas e largura `k`. Em particular `DD_{Res(k)} ∈ P` **sob a
> promessa linha-pura** (verificável em `O(|Π|·k·m)`).

**Prova.** Para cada linha `v` denote `s(v)` o lado único de `λ(v)`.
(i) *Corte preserva o lado:* as premissas `A∨t` e `B∨(¬l₁…¬lⱼ)` compartilham
**todas** as variáveis do pivô; como `X₁,…,X_m` são disjuntos,
`s(p₁)=s(p₂)=:s`; `A ⊆ λ(p₁)`, `B ⊆ λ(p₂)` ⟹ `s(conclusão)=s`.
(ii) *Enfraquecimento:* `λ(v) ⊇ λ(u)` e ambas linha-puras ⟹ mesmo lado.
(iii) *∧-intro:* pela promessa (e também seguindo-se de linha-pura): mesmo
lado. (iv) *Extração:* caminhe para trás a partir da raiz `∅` seguindo as
premissas estruturais; por (i)–(iii) toda linha acessível tem o **mesmo** lado
`i*` (a raiz vem de corte ∧-intro com premissas de mesmo lado, ou é folha
`∅ ∈ Λ_{i*}`; **nota r2-A3:** a raiz `∅` só nasce de **corte** (conclusão
`A∨B=∅`) ou de **folha `∅`** — ∧-intro e enfraquecimento **nunca** produzem
`∅`, pois suas conclusões contêm termo/premissa não-vazio). Folhas acessíveis pertencem a `Λ_{i*}`; restringir `Π` às
linhas acessíveis dá uma refutação `Res(k)` válida de `Λ_{i*}` (cada
inferência continua válida e toda folha é de `Λ_{i*}`) com `≤ |Π|` linhas e
largura `≤ k`. Verificar a promessa: `O(|Π|·k·m)`. ∎

**Relação com o contraexemplo:** L5/L9 são enfraquecimentos **mistos** — a
instância é excluída pela promessa de linha-pura ✓. O contraexemplo mostra que
a promessa original de C2.2 (só ∧-intro puro) é **insuficiente** para
projeção por subconjunto; a linha-pura é **suficiente e verificável**.

**Reclassificação honesta:**
- **C2.1** (largura-k, resolução): permanece **teorema**.
- **C2.2** (promessa original): **(C)** — candidato r1 **retraído**; evidência
  negativa para projeção por subconjunto (§2–§3).
- **C2.2′** (linha-pura): **(P) TEOREMA** (§4).
- **`Res(1)`** sob promessa: continua **(C)** condicional a C2.2 (não a C2.2′).

---

## 5. Ataque à família alternante — critério tornado preciso (§5 do r1)

O teste N2 da família **muda de forma**: em vez de "a promessa se cumpre",
o critério é:

> **(P) Critério-LP:** a família alternante de Garlík produz refutações
> `Res(2)` **linha-puras**? Se **SIM** ⟹ C2.2′ aplica-se ⟹ `DD` decide a
> família ⟹ `UNSAT_CNF ∈ P` (rota negativa via esta via fecha — reductio
> gigante, exigindo revisão externa imediata). Se **NÃO** (enfraquecimento
> misto encontrado) ⟹ **esta via** (C2.2/C2.2′ com promessa linha-pura)
> **fecha como RETRAÇÃO** — a rota negativa em geral permanece aberta com
> método outro; o resultado "misto" é negativo honesto e documentável.

**Próximo passo N2 concreto:** `gk_alternating_family.py` — instâncias
pequenas de `SAT_n ∧ R^kREF_n` (Garlík Thm 6/Thm 1, explicitação do artigo),
refutação `Res(2)` pequena via upper bound `O(k2n^{7k+7})` ou busca, e
**inspeção de pureza linha-a-linha**. Discrimina: linha-pura vs mista.

---

## 6. Lacunas honestas

1. Contraexemplo **verificado por simulação + manual** — não por prova
   formal (Lean); a estrutura é finita e o checker está no script.
2. C2.2′ tem **escopo estrito** (promessa forte); não afirma nada sobre a
   promessa original.
3. O "1602 passam" é evidência, não prova, de que a classe boa é majoritária —
   e o gerador **não é uniforme** sobre refutações (construção reversa com
   folhas singleton; viés declarado).
4. Família alternante: **nenhum** resultado ainda — só o critério (P).
5. K19 livro (G4 do r1) segue não conferido — não afeta §2–§4 (regras de
   Garlík são a fonte usada).

---

*Reprodução:* `python gk_c2_projection_sim.py --n 3000 --seed 20261119`
→ contraexemplo r2 + 1602 válidos + 1 falha G1 (mesma instância).
Referências: `C2_K19_5_7_TEXTO_EXATO.md` (r1) · `C2_ddres_k.md` (v5) ·
Garlík CCC 2024 §2 · `C_disjuncao_viavel.md` (Teorema 4.3).

# REFEREE — piloto "leitura adversarial prosa×Lean" sobre §9.1 e o dossiê `DD_Res ∈ P`

**Rodada:** r1 · **Data:** 26/11/2026 · **Protocolo:** AGENTS §3 Passo 4 + modelo de red team
do pequalnp.com (lê cada afirmação da prosa contra o artefato formal; recusa o que a prosa
diz **mais** ou **menos** que o artefato).
**Alvos:** `krajicek_ddp/RELATORIO_CONSOLIDADO.md` §9.1–§9.3 (ponte L2→L3) ·
`krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md` (§A: `DD_Res ∈ P`).
**Contra:** `lean4/Gothic_Generators/DDP.lean` · `krajicek_ddp/C_disjuncao_viavel.md` ·
`krajicek_ddp/experimentos_disjuncao.py` · `krajicek_ddp/C2_ddres_k.md` ·
`krajicek_ddp/B_lean_relatorio.md` · `gk_lean_verification.json`.
**Ferramenta:** `gk_prosa_lean_lint.py` (P1–P6, executável, `--replay`).

---

## 1. Achados da leitura adversarial (semântica — feita à mão)

| # | Afirmação da prosa | Evidência | Veredito |
|---|---|---|---|
| **F1** | "2 `sorry`s documentados (`DDP.lean:628` e `:690`)" (AUDITORIA §D.1; RELATORIO §9.2.3; README; EVOLUCAO; AMBIENTE; ONDE_ESTAMOS) | `B_lean_relatorio.md:22–23` = warnings reais do Lean: `DDP.lean:628:8: declaration uses sorry` e `690:8`; tokens `sorry` (vazios) em 630/692 | ✅ **CONFIRMADO** — a prosa cita a **linha do warning do Lean** (declaração), convenção correta. Divergência aparente 628×630 resolvida; P1 agora automatiza essa checagem |
| **F2** | "O Lean cobre só o núcleo proposicional — **não** o Teorema 4.3" (AUDITORIA §D.1; §C) | `grep DD_Res` em `DDP.lean`: **0** ocorrências; JSON: 12 theorems (10 PROVED, 2 SORRY = `dd_solvable_in_ST_O1`, `pbounded_implies_feasible`) | ✅ **CONFIRMADO** — nenhum lemma de recorte/pureza/DD_Res em Lean; a prosa **não diz mais** que o artefato |
| **F2b** | JSON `sorry_in_sources: DDP.lean = 4` vs docs "2 `sorry`s" | Linhas com a *palavra* sorry: 32, 625 (comentários), 630, 692 (reais) | ✅ **CONSISTENTE** (4 = 2 comentários + 2 tokens); P2 imprime a reconciliação para não virar falsa divergência futura |
| **F3** | "Algoritmo de projeção 3000/3000 (100%)" (7 docs) + taxas 28.2/14.5/9.6/52.2/49.5% | **Re-execução** de `experimentos_disjuncao.py` (semente 20261010) nesta sessão: `3000/3000 corretos (100.0%)`, 847/436/289/1566/1485, \|π\| médio 7.0, máx 20, 3.1 — **saída idêntica** | ✅ **CONFIRMADO por reprodução** — prosa = artefato, byte a byte nos números |
| **F4** | AUDITORIA §A.1 rotulado "**verbatim**" mas era resumo: (i) omitia a cota prática `O(Σ_i \|D_i\|·\|D_{pares}\|)`; (ii) perdia a hipótese "**se** `E_t` é resolvente de …" do Lema 4.2(2); (iii) omitia `α_{i*} ∈ TAUT` | P3 rodou e **pegou as 3 omissões** ("PROSA DIZ MENOS") | ⚠️→✅ **CORRIGIDO em r1**: §A.1 reescrito com transcrição literal dos §§2.2–2.3 + corolário FDP e nota de custo separados. **Lição: rótulo "verbatim" é contrato — ou é literal, ou não se usa a palavra** |
| **F5** | Enunciado do Teorema 4.3 na **fonte** declara `O(\|Π\|·m)`, mas o passo (1) usa o Lema 4.1 (`O(\|Π\|²)`); a cota combinada só aparecia em `C2_ddres_k.md:73` | AUDITORIA §A.3(d) já reconhecia a tensão; a **fonte** não | ⚠️→✅ **NOTA ADICIONADA** em `C_disjuncao_viavel.md` §2.3 (Comentários): total honesto `O(\|Π\|² + \|Π\|·m)`, arbitragem do auditor preservada (não reescrevi o teorema — decisão de auditoria) |
| **F6** | §9.1: "ponte L2→L3 **NÃO** demonstrada; só condicionais `(2.1)+(ST)⟹NP≠coNP` e `¬(2.1)⟹P≠NP`" | Condicional explícito em RELATORIO 59/60/302/445; nota "aberta" em ≥14 arquivos (grep `L2→L3`) | ✅ **CONFIRMADO** — P5/P6 agora guardam isso mecanicamente |
| **F7** | §9.2(5): "checklist exato (recorte×enfraquecimento; DAG; pureza; tensão reconhecida)" | AUDITORIA §A.3 itens (a)–(e) todos presentes | ✅ **CONFIRMADO** |
| **F8** | "Nenhum `sorry` em `FoundationBridge/`" (RELATORIO §9.2.3) | grep: só prosa ("0 sorry", "sem sorry") — 0 tokens | ✅ **CONFIRMADO** |
| **F9** | AUDITORIA §A.5: "sanity check apenas; os experimentos não provam nada" | Fonte §7 "Leitura honesta dos dados": idem | ✅ **CONFIRMADO** — prosa **não diz mais** que a fonte |

**Nenhuma afirmação de L2→L3 fechada foi encontrada; nenhum `sorry` oculto; nenhum número
divergente.** O dossiê cumpre o que §9.1 exige (níveis separados; condicionais explícitos).

## 2. Correções aplicadas nesta rodada

1. `krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md` §A.1 → transcrição **literal** (3 enunciados),
   corolário FDP e nota de custo em linhas próprias.
2. `krajicek_ddp/C_disjuncao_viavel.md` §2.3 → **Nota de custo (r1)** com `O(|Π|² + |Π|·m)`.
3. `gk_prosa_lean_lint.py` (novo) → guardas P1–P6; `--replay` reproduz o experimento.

## 3. Autocrítica do próprio piloto (objeções à ferramenta)

- **(R1)** P5/P6 são **heurísticas de marcador**: um arquivo pode overclaimar numa linha e
  ter o marcador noutra. *Mitigação:* escopo P5/P6 = docs canônicos (FAIL) + WARN nos demais;
  a leitura semântica dos canônicos foi feita à mão nesta rodada (F6).
- **(R2)** P3 usa **8 tokens pivô**, não diff completo: outras omissões não-pivô passariam.
  *Mitigação:* tokens escolhidos pelos pontos que a avaliação externa já chamou de "maior peso".
- **(R3)** A transcrição "verbatim" de A.1 foi feita por mim e conferida só pelos tokens.
  *Pendência:* conferência caractere a caractere (diff normalizado) = extensão natural de P3.
- **(R4)** P4 `--replay` grepa só `3000/3000 corretos`; taxas e médias não são confrontadas
  automaticamente (conferi manualmente: batem). *Extensão:* incluir as 5 taxas + médias no grep.
- **(R5)** O piloto **não** verifica a matemática dos Lemas 4.1/4.2 (só prosa×artefato) —
  isso continua sendo papel do auditor externo (§A.3 permanece o contrato).
- **(R6)** `EVOLUCAO_PROJETO.md` **não** foi atualizado nesta sessão (estrutura de "Fases" do
  autor; última fase 13, 19/11) — decisão do autor registrada aqui como pendência.

## 4. Veredito e promoção

**r1 APROVADO COM CORREÇÕES (todas aplicadas).** Próximos passos sugeridos — **não promovidos
ainda**: (1) rodar `gk_prosa_lean_lint.py --replay` no CI ao lado de `gk_claims_lint.py`
(após r2 sem falhas); (2) P3→diff normalizado completo (R3); (3) aplicar o piloto às frentes
G–N (AUDITORIA §B) — cada prosa de frente × seus `*_referee.md` e invariantes.

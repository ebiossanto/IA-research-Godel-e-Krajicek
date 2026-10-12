# Referee C2 — rodada 5 — `C2_ddres_k.md` (v5)

**RECOMENDADO** (com os MENORES de rotulagem abaixo, a aplicar antes do arquivo final)

## (a) O rebaixamento é honesto e as (O1)–(O4) cobrem os fatais das rodadas 3–4?

Mapeamento verificado:

| Meu fatal | Obrigação na v5 | Status |
|---|---|---|
| FATAL-1/r3 ((c2) sem caso-pivô-perdido) + FATAL-1/r4 (pai errado, fim-em-∅) | **(O1)** — com o contraexemplo da rodada 4 reproduzido e a obrigação de "caracterizar a direção correta do reuso e provar que `E` termina em ∅" | **coberta** |
| FATAL-2/r4 (qualificador "usada como justificante" deixa o (r6)-final escapar) | **(O2)** — com as duas rotas que apontei (fechar a promessa no final OU traçar ancestrais não-neutros) | **coberta** |
| FATAL-3/r4 (dependentes ∧-intro de linhas eliminadas) | **(O3)** | **coberta no título**; no corpo restrita a ∧-intro — ver MINOR-2 (o canto "(r5) com ambos os pais eliminados" não está nomeado) |
| (c3)/(d) da v3 (estricidade do truncamento) | **(O4)** | **coberta** |
| FATAL-3/r3 (`Res(1)` incondicional) | §3.3 + §0.4: retração mantida, só sob promessa | **coberta** (exceto rótulo — MINOR-1) |
| FATAL-2/r3 (ordem/objeto: "recorte após si mesmo", "retro em Π") | não listada como (O) | **moot** — v5 não reivinda prova nem pipeline; a reescrita fica no próximo-passo (2). Recomenda-se registrar como (O5) — MINOR-3 |

Veredito de (a): **honesto e substancialmente completo** — as obrigações são,
de fato, as minhas, com os contraexemplos citados; nenhum ponto dos fatais das
rodadas 3–4 desapareceu silenciosamente.

## (b) Reivindicações residuais indevidas

Duas, nenhuma fatal:

1. **§0.4 / §3.3 / §6-linha 7 — `Res(1)` rotulado como assentado.** "DD ∈ P
   sob a promessa" é dito **na mesma proposição** da Conjectura C2.2 — que a v5
   rebaixa a **PROGRAMA (C)**. Logo o condicional de `Res(1)` também é **(C)**
   (condicional a C2.2), não status próprio; §0.4 e o checklist o apresentam sem
   o marcador, ao lado de itens marcados (C). Correção de uma linha: marcar
   "**(C)** condicional a C2.2" nos três lugares. A retração da versão
   incondicional está correta e mantida ✓.
2. **§7 — "entrega como fechado: ... C2.3 (ingrediente + redução)".** O que
   está fechado é a **redução condicional** à família (C); a **família
   alternante permanece aberta** (§0.3 e §4 marcam (C) corretamente). "Fechado"
   para o ingrediente contradiz o próprio §4 — trocar por "fechada a redução;
   o ingrediente é o problema nomeado, em aberto".

Ressalva de citação (não é defeito): §0.2 apoia a "plausibilidade" na minha
frase da rodada 3 ("a adaptação deve funcionar"); a citação é justa (eu disse
isso, com os fallbacks na direção correta — que é exatamente (O1)), e está
marcada (C) ✓; mantê-la com a data da rodada, pois nos fatores seguintes eu
derrubei a construção.

## (c) C2.1 e C2.3 — permanecem como aceitos?

- **C2.1 ✓**: teorema inalterado nas rodadas — corolário do Teorema 4.3,
  `E_i ⊆ D_i` ⟹ largura, bound `O(|Π|²+|Π|·m)` (FATAL-6/r1 mantido corrigido),
  FDP `p(t)=t` em nº de linhas com k constante, "distinção provada **só** para
  FDP" e "nenhuma conclusão sobre a causa da falha de Garlík" (FATAL-4/5/r1
  mantidos) ✓ **aceito como nas rodadas 1–4**.
- **C2.3 ✓**: família alternante com "exatamente um lado insat", entrada
  declarada (`α₁ := ¬γ` DNF `O(|γ|)`, `α₂` fresca), decodificação total
  (`γ∈UNSAT ⟹ 1`, `γ∈SAT ⟹ 2`) ⟹ `UNSAT ∈ P` ⟹ P=NP, `TAUT_DNF`
  coNP-completa e `UNSAT_CNF` como fonte (retratações da v1 mantidas), [Gar24]
  analisado corretamente, tudo marcado (C)+(P) ✓ **aceito como na rodada 2**.
- `Res(1)` ✓ rebaixado (só o rótulo, MINOR-1).

## MENORES (obrigatórios, correções de uma linha)

- **MINOR-1:** marcar `Res(1)`-sob-promessa como **(C)/condicional a C2.2** em
  §0.4, §3.3 e §6-linha 7 — hoje é a única reivindicação com status indevido.
- **MINOR-2:** alargar o corpo de **(O3)** para "dependentes de linhas
  eliminadas (**corte** e ∧-intro) — inclusive (r5) quando **ambos** os pais
  foram eliminados (`E(pai₂)` inexistente)" — o título já cobre, o corpo não.
- **MINOR-3:** registrar como **(O5)** o ensinamento do FATAL-2/r3: definir o
  objeto e a ordem únicos (pré-varredura → recorte → retro) antes de escrever a
  prova; sem isso, a reescrita do próximo-passo (2) pode recair na contradição
  da v3.
- **MINOR-4:** §3.1: a Conjectura diz "promessa verificável em `O(|Π|·m)`" sem
  dizer o objeto (**`Π` ou `E`** — e (O4) deixa a redefinição em aberto);
  explicitar "a ser fixada conforme (O4)".
- **MINOR-5:** §7 "entrega como fechado: ... C2.3" — restringir a "fechada a
  **redução**; a família é o problema nomeado, em aberto" (ver (b)-2).

## Veredito (d)

A v5 faz exatamente o que um referee pede quando a prova não fecha: **para de
reivindicá-la**, codifica cada objeção derrubada como obrigação aberta com seus
contraexemplos, e mantém como fechado só o que sobreviveu ao escrutínio
(C2.1, C2.3). Nenhuma das 4 rodadas anteriores é diluída ou contornada; os
dois residuais encontrados são de **rótulo**, corrigíveis em uma linha, e não
reinstalaram nenhuma afirmação que eu derrubei. **Recomendado** com os
MINOR-1..5 aplicados.

**Referee C2 — rodada 5 — RECOMENDADO — 11/10/2026**

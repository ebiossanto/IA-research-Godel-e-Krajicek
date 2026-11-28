# 04 — Continuidade entre as linhas de pesquisa

## 1. Mapa das linhas (26/09/2026)

| Linha | Pasta | Data | Núcleo |
|---|---|---|---|
| **Espectro de Limiares de Prova** (esta) | `Desktop\Lógica\docs\espectro-limiares\` | 26/09 | `ρ_T, B_T, C_T, R_T, g_T^[b], θ↦Φ_θ` |
| Projeto Gödel | `C:\Users\Euzebio\Documents\Default Project\Gödel\` | anterior | `δ, 𝒢, ρ_b, g^{a,b}, RBT, PPR, Con(T)` |
| Falha de colagem / perspectiva externa | `Desktop\Lógica\proofs\` (`*colagem*`, `principio_perspectiva*`) | 24/09 | linha paralela de reflexão, não misturar |

A linha nova **não substitui** as outras; nasce do mesmo terreno (geradores de Krajíček) mas com objeto diferente.

> **Unificação (26/09/2026):** a pasta `espectro-limiares` foi movida para dentro do projeto raiz `Desktop\Lógica\` (esta linha ocupa `docs\espectro-limiares\`; as fontes primárias ficam em `proofs\` e `docs\`; o script foi para `src\python\`).

---

## 2. Correspondências com o projeto Gödel (importante)

1. **Colisão de notação `ρ`.** Projeto Gödel: `ρ_b(Φ; H)` = *rank de cobertura* (estabilização da cobertura, `09_EVOLUCAO…` §20–21). Linha nova: `ρ_T(Φ)` = *limiar máximo de prova antes de `j*`*. **São objetos distintos.** Ação: manter os dois símbolos mas tabelar a distinção em todo texto que cite os dois, ou renomear o rank de cobertura.
2. **Dois orçamentos vs um.** Gödel: `g^{a,b}` com `|Φ| ≤ a(n)` e `|π| ≤ b(n)` (`09_EVOLUCAO…`, matrices (a,b)). Linha nova: `g_T^[b]` é o caso diagonal `a = b`. A generalização a dois orçamentos da linha nova está **não feita** — se um dia for feita, reutilizar a notação `g^{a,b}` do Gödel.
3. **O Lema 3 é o caso `θ = ⊥` de um gadget da família.** Em `Gödel/lean4/Gothic_Generators/Core.lean` está provado (em Lean, `lemma3_con`): `Φ_T^{w*} ↔ Con(T)` com `Φ_T(x) = ∃p,z[Prf_T(p,⊥) ∧ x = pad(w*,p,z)]`. Isso é o **gadget "padding"** com polaridade `Φ^{w*} ↔ T ⊬ θ`. O espectro usa o **gadget "timeout"** (`NH_θ`), de polaridade `Φ^{w*} ↔ T ⊢ θ`. As duas famílias compartilham o mesmo esqueleto (`Φ^w` fatia um cilindro de prefixo) e a mesma formalização de `Prf` — **material reaproveitável** (a instância `θ=⊥` já tem prova assistida por máquina numa direção).
4. **Convergência de perguntas abertas.** O projeto Gödel pergunta se `rng(g^{a,b})` evita coleções NP; Krajíček (ECCC TR23-030) pergunta o mesmo para `rng(g_T)`; a linha nova chega lá pela Etapa 15 (resultantes). As três linhas devem citar a mesma formulação do problema aberto.

### Tabela 1 — correspondências de notação (B1.4, fixada em 27/09/2026)

Regra normativa: **nunca usar um símbolo para os dois objetos**. Em qualquer texto que cite os dois projetos, incluir esta tabela (ou remeter a ela).

| Símbolo | Projeto Gödel (`…\Default Project\Gödel\`) | Linha do espectro | Status |
|---|---|---|---|
| `ρ` | `ρ_b(Φ; H)` = *rank de cobertura* (estabilização da cobertura sob teste `H`; `09_EVOLUCAO…` §20–21) | `ρ_T(Φ)` = *limiar máximo de prova* `= max 𝓑_T(Φ)`, o maior ponto de transição de `J_{T,Φ}` (equivalência `J(r-1) ≠ J(r) ⟺ r ∈ 𝓑_T(Φ)`; Teorema local 5.1) | **Objetos distintos.** Sufixos `_b` e `_T` são obrigatórios; não simplificar para `ρ`. |
| `g` | `g^{a,b}` = gerador de **dois** orçamentos (`\|Φ\| ≤ a(n)`, `\|π\| ≤ b(n)`; matrices (a,b)) | `g_T^[b]` = gerador de **um** orçamento, diagonal `a = b` | `g_T^[b]` é o caso diagonal de `g^{a,b}`. Generalização a dois orçamentos **não feita**; ao fazê-la, reutilizar `g^{a,b}`. |
| `R` | `RBT`, `PPR` (símbulos do Gödel; definições em `09_EVOLUCAO…` — **conferir antes de citar junto**) | `R_T(n)` = envelope de exigência de prova (Etapa 12) | **Ainda não tabelado com segurança** — não citar `RBT`/`PPR` lado a lado com `R_T` sem antes revisar `09_EVOLUCAO…`. |

---

## 3. Relação com a linha da "falha de colagem" (24/09)

Os documentos `documento_continuidade_perspectiva_colagem_reflexao_v1.md`, `continuacao_falha_colagem_interna_v02.md`, `custo_colagem_limites_reflexao_v03.md` tratam de **epistemologia da própria pesquisa** (colagem, custo, perspectiva externa). São linha paralela: nenhum teorema do espectro depende deles e nenhum deles depende do espectro. Manter separados; citar apenas na memória metodológica do projeto.

---

## 4. Convenções herdadas (para os documentos novos)

- Numerar documentos (`01_…`, `02_…`), manter `INDICE.md`/`README.md` como mapa e um `CONTINUIDADE` como histórico de decisões — mesmo padrão de `Gödel\`.
- Regra do projeto Gödel (aplicável aqui): *definições/objetos próprios não são rotulados como conhecidos na literatura sem verificação bibliográfica*.
- Níveis A–D (Etapa 18) em toda seção; "possível contribuição original" até a Etapa 17 fechar.
- Idioma: português.

---

## 5. Próximos passos concretos (em ordem)

1. Produzir `01_ambiente_formal_e_codificacoes.md` dentro de `espectro-limiares\` (Etapa 1) — decide `q(Φ)`, T, codificação; desbloqueia o gadget.
2. Consolidar `01_NUCLEO_DURO.md` §3 em texto único com provas (Ciclo 1 / Marco 1).
3. Auditar o gadget `θ↦Φ_θ` com a instância Lean do Lema 3 como calibração (Ciclo 2).
4. Rodar as queries bibliográficas pendentes (`02` §4.2), lendo os capítulos relevantes do livro de Krajíček (2025).
5. Só então iniciar a geometria de `C_T` (Ciclo 3).

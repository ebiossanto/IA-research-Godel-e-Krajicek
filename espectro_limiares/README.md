# espectro_limiares — extração da linha irmã `IA-RESEARCH-Logica`

**Proveniência:** extração de **<https://github.com/ebiossanto/IA-RESEARCH-Logica>**
(público;26/09–01/10/2026; clone analisado em28/11/2026; credenciais
varridas = limpo). **Linha paralela irmã** do eixo principal — mesmo
terreno (geradores de Krajíček), objeto diferente: **espectro de limiares
de prova** (`ρ_T, B_T, C_T, R_T, g_T^[b]`) vs interpretabilidade/perfis
do projeto-mãe. **O INDICE não referenciava nada dele** (lacuna fechada
nesta extração).

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `04_CONTINUIDADE.md` | **A ponte normativa** — Tabela1 de notação (fixada27/09): `ρ_b` (rank de cobertura, mãe) vs `ρ_T` (limiar de prova, espectro) = **objetos distintos, sufixos obrigatórios**; `g^{a,b}` vs `g_T^[b]` (diagonal); `RBT/PPR` vs `R_T` (**não citar lado a lado sem revisar `09_EVOLUCAO`**) · **Lema3 ↔ gadget:** o `lemma3_con` Lean-provado do mãe é a instância α=⊤ do gadget *padding*; o espectro usa o *timeout* — **mesmo esqueleto `α^w` e mesma formalização de `Prf` → material reaproveitável** · convergência do problema aberto: mãe ↔ Krajíček (ECCC TR23-030) ↔ espectro (Etapa15) perguntam o mesmo (`rng(g)` evita coleções NP?) → **citarem a mesma formulação** |
| `STATUS_MAPA_ESPECTRO.md` | **Estado por resultado** (29–30/09): verificados/condicionados/clássicos/não-iniciados — incl. `ρ` **limiar exato** (fortalecimento vs fonte), `M_T ≤ Thm(T)` (novo), gadget/Q3 condicionado, ponte `C_T→ω(g_T)` **não existe** (lacuna), "lei de crescimento" = **clássico** Gödel1936 (não reivindicar), Etapas10/12/13/18/19 com achados **A1–A44** e níveis B/C/D honestos |
| `01_NUCLEO_DURO.md` | Núcleo local definido e **verificado** (teoremas5.1,6.1–6.3, cor.7.x + `ρ` exato) |

**Fora da extração (referenciar por URL):** `paper/main.pdf` (18pp,
compilado — candidato à trilha de submissão H3), `src/python/
verifica_espectro.py` + `resultado_verificacao.txt` (**410.155 perfis,
7.737.331 pares — TODOS OS TESTES PASSARAM**, N2 reproduzível lá),
`proofs/` (10 cadeias), `docs/espectro-limiares/` completo (18), linha
*falha de colagem* (epistemologia — mantida separada por decisão do
próprio repo).

## Classificação (A)/(P)/(C)

- **(P) com verificação:** núcleo local + `ρ` exato + `M_T` (script +
  provas; artefatos **no repo-fonte**,不同于 transicao_dupla);
- **(C):** Q3/gadget (condicionado, formalização F1–F6 pendente),
  Conj-F (Nível D), janela exata (B condicional);
- **(A)-nc:** clássicos (Gödel1936 speed-up) — não reivindicar.

## Níveis

O espectro usa **A–D** (Etapa18); o projeto-mãe usa **Ten-Proofs
N0–N4** — mapeamento pendente antes de qualquer citação cruzada de
status.

## Regra de notação (obrigatória em textos que citam os dois projetos)

`ρ_b` ≠ `ρ_T` · `g^{a,b}` ⊃ `g_T^[b]` (diagonal) · `RBT/PPR` vs `R_T`
exige revisão de `09_EVOLUCAO` §— antes de uso conjunto (Tabela1 do
`04_CONTINUIDADE.md`).

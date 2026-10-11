# H1_referee — referee hostile de `H1_colecao_refutacao.md`

**Veredito geral: PARCIAL.** De pé: "nenhum G existe" (1ª metade do Thm 1.1) e o núcleo
condicional do Thm 2.1. Morto: a finitude do Thm 1.1 (ERRO fatal), o status incondicional de
Cor. 2.2, e a "eliminação" §3.2.

## S1 — Thm 1.1: PARCIAL (no-G OK; finitude = ERRO)

**PV vs T_PV: conferido, H1 está certo.** G2 2.1(a′) aceita exatamente `M' ⊨ PV` (rota externa:
`Prf_P`/`Fals` absolutos + soundness real; o menor contraexemplo cobre derivações não-padrões).
Kra98 Thm 4.1 dá `M[G] ⊨ PV` com G fechada sob EF-provability (o fecho das constantes-1 só serve
para Σ^b_1-elementaridade). Passos 1–2 OK (`i = ν_G(N)`; `δ_N` decide `ν_G(N)<m` por circuito
interno e absoluto); contradição com (a′) fecha. Ressalva de tipo: **τ_N ∉
`Circuit_M(p)`** se os átomos espelhos são "frescos" — `p=(r_i)_{i<m}` está todo ocupado por `φ`;
amplie a base de átomos ou Thm 1.1 fica mal-tipado.

**Finitude: ERRO.** "Refutação EF em `M`" **não** é finitária externamente: uma derivação
interna tem comprimento interno, possivelmente não-padrão, e usa um conjunto internamente finito
de premissas — externamente infinito. "Todo subconjunto finito EF-consistente ⟹ `𝒯`
EF-consistente" falha (não-compactude interna: premissas indexadas por `n∈M` não-padrão,
derivação de comprimento `n`). Zorn não conserta: Claim 2 exige `T` **sem refutação EF em `M`**
(propriedade global), não consistência dos subconjuntos finitos. E sob derivação não-padrão
o Thm 2.1 nem internaliza: os falsificadores cobririam um conjunto externamente infinito de
índices, e a substitução pode não pertencer a `M`.

**Sobrevive (1 linha):** "`𝒯` sem refutação EF interna alguma (⟺ nenhum G)"; o resto fica condicional a refutações finitas não provadas.
## S2 — Thm 2.1: PARCIAL (conclusão recuperável; texto = rascunho)

- Átomos de `N_j`: estão **sim** entre `p` (nomes são tuplas de `Circuit_M(p)`); `x` não é
  livre estendível a eles e `δ_{N_j}` é decidido por `x`. H1 ("não necessariamente") está errado;
  o caso-a-caso usa o próprio `x`.
- Compatibilidade dos `y_j`: **não endereçada**. Fecha por (S2): disjunção disjunta ⟹ átomos de
  `(α)_i` disjuntos ⟹ falsificadores de `i≠i'` compatíveis; `j`'s com mesmo `code` usam o
  **mesmo** falsificador. Escreva isto — hoje é buraco.
- Passo final: "EF⊢φ(x) p/ x arbitrário ⟹ EF⊢φ" **não** é "substituição p-tempo-fechada".
  Corrija: substituições constantes provadas ⟹ `φ` tautologia ⟹ EF (completo) prova `φ`;
  derivação real ∈ `M` ⟹ contradiz item (1).
- O parágrafo exibe deliberações visíveis ("hmm", "não — em vez disso"): não é teorema.

## S3 — Cor. 2.2: PARCIAL

- "`i ∉ M`" segue, mas exige dois passos: `code(N_j,v) ∈ M` (só **finitos** bits de `v`
  importam ⟹ código computável ⟹ ∈ `M`); e `i∈M∩m` + (S4) + absolutidade de `Fals` dão
  falsificador real, contradizendo a não-cobertura. Correto, falta escrever.
- "Certificada internamente por derivação EF de `¬τ`": **falso como está**. A refutação **não**
  o produz; as direções são triviais, não provadas: `EF⊢¬τ ⟹ realmente
  não-falsificável` só por soundness real de EF (menor contraexemplo; cobre não-padrões);
  `(α)_i` autologia `⟹ EF⊢(α)_i` por completude de EF. O valor de "sinal
  mensurável" da Cor. 2.2 é menor que H1 anuncia.

## S4 — §3.2: PARCIAL (conclusão certa, razão falsa)

"a saída do estudante **não precisa** pertencer a `M`" é **falso**: `M ⊨ PV` ⟹ toda função
p-tempo real mapeia `M` em `M` (PV define todas as p-tempo; existência única + avaliação
absoluta). Aplicado a `(|π|,|α|,m) ∈ M`, o estudante devolve `i ∈ M`. A trilha falha por motivos
outros: (a) (ST) só constrange instâncias **padrão** — nada garante correção na não-padrão;
(b) o estudante **falhar** não contraria (ST); (c) achar `i` resolvível exigiria
decidir tautologias em índices não-padrões — não p-tempo, nem sob NP=coNP. §4 lista "eliminação
da trilha falsa" entre os provados: **remova ou reescreva**.

## S5 — §3.3 rota (ii): ERRO (vazia; não é circular, é troca de hipótese)

Exigir (ST) interna ("`M ⊨` estudante resolve `DD_P`", estudante como função PV em `M`) não fecha:
a saída fica em `M∩m` e (S4) dá falsificador real de `α_i` ⟹ internal-(ST) é **refutável em ZFC**
dado `M⊨S`; com KPT + consistência de `S`, internal-(ST) ∧ (ST) real são **inconsistentes em ZFC**
— hipótese vazia (F2 §5.2), não produz NP≠coNP. O que fecharia: um teorema de extração —
sob NP=coNP+p-boundedness, converter o certificado EF do índice novo (Cor. 2.2) num procedimento
p-tempo com saída ∈ `M∩m` resolvendo `DD_P`. G1 Thm 4.3 + G2 2.1(a′) mostram isso impossível
sempre que o falsificador está numa extensão de PV: (ii) colapsa em (i) ou morre. "Decidível pela
redação de (ST)" está de mais: **ambas** as redações testadas e nenhuma fecha.

## Sobrevive (resumo)

Thm 1.1 sem a finitude ("nenhum G; `𝒯` sem refutação EF interna") + Thm 2.1/Cor 2.2 como
condicionais sobre refutações finitas. Peso para a nota ao autor, mas **não**
como "refutador finito": a finitude é o buraco do Claim 2 que H1 admite em §4 sem ver que corrói
M1.
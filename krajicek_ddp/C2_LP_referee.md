# Referee Hostile — C2_LP_familia_alternante (rodada 3 da linha LP)

**Data:** 19/11/2026 · **Rodada:** r1 deste documento · **Alvo:**
`C2_LP_familia_alternante.md` + `gk_alternating_family.py` (+ saídas t6/t2)

---

## A. Achados

### A1 (GRAVE) — Semântica "linhas" do REF: exatamente-um por posição é suficiente?
Com uma cláusula por posição e premissas em posições **anteriores quaisquer**,
`REF_t` modela sequências de ≤ t linhas com repetição permitida. Repetições
podem inflar o comprimento mínimo? Não: se existe refutação ≤ t, existe uma
**sem repetição** (repetir uma linha é desperdício) e é representável
(premissas em posições anteriores ✓). E a validação de fronteira (5/6) confirma
a calibragem. **Mas:** as folhas só podem aparecer na posição1? Não — na
posição j≥2 γ-livres são permitidos (o código libera `c ∈ γ` em todo j) ✓.
**Resposta:** ACEITO — suficientes e sonoros; validação empírica + argumento
de minimia. Registrar a frase "sem repetição WLOG" no doc (pendência r3). ✅

### A2 (GRAVE) — Nec: a reserva de domínio enfraquece o veredito?
Se a família nunca tiver lados difíceis, Nec não aplica e LP poderia valer.

**Resposta:** **ACEITO** — o doc declara a reserva em §4 e, crucialmente, o
**item independente** (candidato REF_t não alterna para t poli, §1-2/§3) não
depende de Nec: o candidato concreto está **retraído incondicionalmente**.
O veredito "via LP retraída" vale **para o candidato testado** e, via Nec,
para famílias com lados difíceis; famílias sem lados difíceis permanecem
**abertas mas não testadas** — a frase do §1 deve refletir isso (pendência
r3:1 linha no veredito). ✅

### A3 — T2=0 mistas não resgata a via (o doc diz isso?)
Sim — §3-T2 explica: γ pequenos têm prova pura curta (solver refuta o lado
sozinho); coerente com Nec (difíceis exigiriam impureza). **Nenhum claim de
"provas são puras em geral"** ✓. ✅

### A4 — Reprodutibilidade: t=2 e t=6 em arquivos distintos com shas
corretos? Saídas renomeadas por parâmetro (`_t{T}_n{N}`); console do t=2
preservado no histórico; t=6 canônico regerado.

**Resposta:** conferir no commit que os4 arquivos de saída existem e que os
metadados internos batem com os shas citados. Pendência r3 (checagem). ✅

### A5 — "5 bugs" — o processo de validação está documentado?
§2 lista os5 com o teste que expôs cada um — suficiente para auditoria de
processo; o código final contém comentários marcando as correções.

**Resposta:** ACEITO. ✅

---

## B. Veredito

**RECOMENDADO (r1)** com pendências r3 de1 frase cada (A1: "sem repetição
WLOG"; A2: refinamento do veredito p/ famílias sem lados difíceis; A4:
checar shas no commit).

**Mandato cumprido:** critério-LP decidido — **(a)** candidato concreto
`(γ, REF_t)` retrado (incondicional); **(b)** Nec restringe LP a famílias
com lados difíceis (condicional declarado); **(c)** via LP retraída para a
rota negativa; **(d)** C2.2 (promessa fraca) permanece a única via (C).

**Proibição mantida:** nenhum claim de `DD_{Res(k)} ∈ P` incondicional; nenhum
reductio "entregue"; Res(1) segue (C).

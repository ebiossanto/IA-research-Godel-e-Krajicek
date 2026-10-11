# CARTA FINAL PARA ENVIO — Krajíček (arXiv:2506.20221v5 / LMCS 22(2:14)2026)

> ## ✅ ENVIADO — 11 Out 2026, 18:14 (Gmail)
> **De:** Euzébio <euambiente@gmail.com>
> **Para:** jan.krajicek@protonmail.com **e** krajicek@karlin.mff.cuni.cz (ambos)
> **Assunto:** *A question on step (5) in the proof of Theorem 4 (v4) / Theorem 3
> (v5, LMCS) of arXiv:2506.20221*
> **Protocolo:** mensagem enviada por gmail.com em 11/10/2026 18:14 — registro no
> `EVOLUCAO_PROJETO.md` (Fase 11.4), `RELATORIO_CONSOLIDADO.md` §7 e `INDICE.md` (DD8).
> Status antigo: APROVADO pelo usuário em 11 Out 2026 (base:
> `NOTA_EDITORIAL_Krajicek.md`
> v4 — referee APROVADO —, §5(2): carta curta + apêndice resumido de 3 itens).
> Esta versão acrescenta, a pedido do usuário, a **apresentação de autor independent
> com apoio de IAs gratuitas** (OpenCode, MIMO e outras) + **GitHub + e-mail**.
> Revisão referee da apresentação: dispensada (é fato pessoal do autor, não conteúdo
> matemático; o corpo matemático é literalmente o aprovado em §1/§2/§4 da nota v4).

---

## Dados de envio

- **Para:** jan.krajicek@protonmail.com *(o endereço que ele dedica a "all other
  matters" — https://www.karlin.mff.cuni.cz/~krajicek/email.html)*
- **Alternativa institucional:** krajicek@karlin.mff.cuni.cz
- **Assunto:** *A question on step (5) in the proof of Theorem 4 (v4) / Theorem 3
  (v5, LMCS) of arXiv:2506.20221*
- **Assinatura do e-mail:** Euzebio Soares dos Santos — euambiente@gmail.com —
  https://github.com/ebiossanto

---

## A CARTA (pronta para copiar e colar)

> Dear Dr. Krajíček,
>
> I am reading arXiv:2506.20221v5 (LMCS 22(2:14), 2026) with great interest, and
> I would like to report what looks like a gap in the proof of Theorem 4 of arXiv
> v4 (renumbered as Theorem 3 in v5/LMCS), together with a few questions.
>
> First, allow me to introduce myself. I am an independent researcher and logic
> enthusiast without institutional affiliation. I conduct my studies with the help
> of free AI tools — in particular the OpenCode agent framework and the MIMO
> language model, as well as other freely available AIs — which I use as reading,
> cross-checking and drafting assistants; whatever gaps or errors remain are of
> course my own. My working notes are public at
> https://github.com/ebiossanto/IA-research-Godel-e-Krajicek, and you can reach
> me at euambiente@gmail.com.
>
> **The point.** In §3, item (5) of the proof, the sentence "But by (7) i_o is
> also already in M∗" seems to derive i_0 ∈ M\* from Log(M\*) = Log(M′). Since
> Log(M) = {|m| : m ∈ M} records only measures, and any new element j < m has
> |j| ≤ |m| (a measure already in Log(M)), condition (7) appears compatible with
> M′ containing indices below m outside M\*. The step would follow from the
> additional domain condition M′ ∩ m = M ∩ m; alternatively the axiom (8) could
> be required directly in M′.
>
> **A dichotomy our analysis suggests** (I state it as a question, not as a
> claim). If the intended reading is the strong one — item (i) of Problem 2.1
> read over M′ ("M′ preserves all Σ^b_1 properties of elements of M"), or item
> (iii) as M′ ∩ m = M ∩ m — then the configuration that item (5) requires
> ((ii) together with (8)/(F-sent) in M′) appears to be refuted by our Lemma
> (iv) below, in which case Problem 2.1 would be negative for this instance and,
> by footnote 2, would give P ≠ NP. If instead the strong reading is not the
> intended one, then item (5) appears to be missing its argument. Could you let
> me know which reading you had in mind, and whether the P ≠ NP horn is meant to
> be accepted?
>
> **Am I missing an argument** — e.g., a feature of the forcing in [7, Thm 9.4.2]
> that also prevents new elements of old measure below m? I would be glad to be
> shown the point.
>
> **Three structural obstacles we found** to the natural repairs (our own,
> unpublished work — I would welcome your criticism; full details and internal
> peer-review logs are in the repository above):
>
> **(i)** For the seed of the paper (M ⊨ (S1)–(S4)), the configuration M′ ⊨ T_PV
> with ¬φ satisfiable together with M′ ⊨ (F-sent) appears to be false in ZFC
> (it is (ii) together with (8)/(F-sent) in M′ that is refuted — exactly what
> item (5) needs; hypothesis (ii) per se is not refuted). Under NP = coNP the
> construction would be legitimate — and would already prove NP ≠ coNP.
>
> **(ii)** In no model M_0 ⊨ T_PV+(S2)+(S3)+(S4) can there be an internal
> collection F with ∀i<m Fals(F(i), α_i): collecting falsifiers one by one and
> gluing them is prohibited. Consistently with this, T_PV + BB + (S2)+(S3)+(S4)
> is inconsistent (BB collapses the KPT analysis of (1) — cf. your remark at L442).
>
> **(iii)** T_PV+(S4) ⊢ ∀rφ(r): ¬φ is internally unsatisfiable in every model of
> T_PV+(S4) with α, m named — the falsifier obtained in M′ must live exactly
> where (S4) fails, which is what pins the index i_0 of item (5).
>
> **Four questions** whose answers would delimit the residual analysis:
>
> **Q1.** Is the intended semantics of τ_N the reading (R1): τ_N = ⋁_q (q codes an
> assignment ∧ Fals(q, (α)_{code(N,q)}) = 1), with q a **total** assignment? (A
> partial q would change some of our conclusions for nonstandard names.)
>
> **Q2.** The code convention: do the bits of α enter the formulas as
> **constants**? (We read the paper this way; it is what supports our Lemma (iv)
> of the appendix.)
>
> **Q3.** Was (8) required in M′? And what are the intended readings of items
> (i)–(iii) of Problem 2.1 (to delimit the dichotomy above)? If you had a
> specific feature of [7, Thm 9.4.2] in mind when writing item (5), which one?
>
> **Q4.** Condition 1 (φ has no proof in M in any pps): intended as a hypothesis
> **on** the model, or as something to be **derived**? (Our Lemma (iv) shows
> that, as a hypothesis, it instantiates the very incompleteness you warn about
> at L21–22.)
>
> With best regards and respect for your work,
>
> Euzebio Soares dos Santos
> Independent researcher (no institutional affiliation)
> euambiente@gmail.com · https://github.com/ebiossanto

---

## Apêndice sugerido (meia página — anexar como nota ou segunda parte do e-mail)

*(Conteúdo: os itens (i)–(iv) já estão na carta acima na forma resumida — este
apêndice só acrescenta as localizações, para ele conferir sem buscar:)*

- Lacuna: §3, item (5) — *"But by (7) i_o is also already in M∗"* — presente em
  **v4, v5 e LMCS**; numeração: Teorema 4 (v4) = **Teorema 3** (v5/LMCS).
- Objetos: `(1)…(8)` são equações do artigo ((1) = condição da análise KPT);
  itens do Problema 2.1 são **(i)(ii)(iii)**; `(F-sent)` = a sentença de
  falsificador enviada com a semente.
- Nossos lemas (i)–(iv) acima correspondem, no dossiê público, a: `G2` Thm
  2.1/Cor 2.2; Teorema K (`J1` §3) + K.2; `L.1` (`L1` §1). Refutações internas
  com testemunha não-padrão seguem **abertas** (Q-compactness) — não afirmamos
  nada além do escopo destes lemas.
- Q-compactness de `𝒯` para **refutações genuínas** é **negativa**
  incondicionalmente (os únicos membros padrão de `𝒯` são constantes-1; `α` é
  não-padrão) — e o ponto fixo **padrão** existe (K-FP′): escolha padrão-muitos
  é inofensiva; uniformização não-padrão é o que o item (ii) acima proíbe.

---

## Checklist do envio (humanos)

- [ ] Revisar a carta acima (corpo matemático = nota v4 aprovada; apresentação
      pessoal acrescentada a pedido do autor do projeto).
- [ ] Enviar para **jan.krajicek@protonmail.com** (assunto acima); cc opcional
      para krajicek@karlin.mff.cuni.cz.
- [ ] Colar o apêndice como segunda parte do e-note ou anexo (mesmo e-mail).
- [ ] Guardar o protocolo (data/hora do envio) no registro do projeto.

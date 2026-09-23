# Rascunho MathOverflow — PERGUNTA (não publicado)

**Tag:** `proof-theory`
**Status:** RASCUNHO — **não postar sem confirmação do autor**
**Data:** 22/09/2026

---

## Título (sugestão)

**Covering deficits for reflection obligations vs. proof-length measures: is there a transfer lemma?**

(Alternativa PT/EN mais curta: *Does a polynomial proof-length saving for slow consistency show up in a "deficit of uncovered obligations"?*)

---

## Corpo (EN — proposto)

I am studying a finite combinatorial invariant attached to a formula family and a proof-theory budget, inspired by proof-complexity generators (Krajíček) and slow consistency (Freund–Pakhomov).

**Setup (finite model).** Fix a finite set of *obligations* \(W^{\mathrm{true}}\) (candidate statements \(\Phi^w\) that are true in \(\mathbb N\)). For a theory (or proof system) strength \(\sigma\) and a length budget \(b\), say that \(w\) is *covered* if the statement has a proof under \((\sigma,b)\). Define the **deficit**

\[
\delta(\sigma,b) := \#\{ w \in W^{\mathrm{true}} : w \text{ not covered}\}.
\]

Elementarily \(\delta(b)=0\) iff \(b \ge \max_w s(\Phi^w)\) and strength is large enough — so \(\delta(\cdot)\) is the survival function of the multiset of minimum proof lengths.

**What is known from the literature.** Freund–Pakhomov prove polynomial *proof lengths* in PA for certain *slow* consistency statements \(\mathrm{Con}(PA+\mathrm{Con}^*(PA))\restriction n\), while the corresponding fast climb behaves differently.

**Question.** Is there a standard *transfer* statement of the following shape, or a reference to one?

> If a family of statements has polynomial minimum proof lengths in \(P\) (resp. superpolynomial), then the aggregated deficit \(\delta(\cdot)\) over a fixed true-obligation set inherits the same growth class at polynomial budgets.

Equivalently: under what hypotheses on a translation \(\tau_n\) and a size bound \(q(n,m)\) (every \(P\)-proof of length \(m\) of \(\tau_n(\varphi)\) yields a \(T\)-proof of length \(\le q(n,m)\)) does an arithmetic lower bound transfer to \(P\)?

I am **not** claiming a new lower bound; I am looking for the precise folklore/formal name of this transfer, or citations where aggregation of proof lengths into a counting deficit is studied.

**Context tried to check:** Krajíček on proof-complexity generators; Beklemishev reflection; slow consistency (Friedman–Rathjen–Weiermann, Henk–Pakhomov, Freund–Pakhomov); Pudlák on local/global reflection. I did not find this exact formulation — but I may have missed it.

---

## Checklist antes de postar (autor)

- [ ] Conferir se a pergunta não é duplicata (busca no MO)
- [ ] Confirmar citações FP 2020 / Krajíček 2023
- [ ] **Confirmação explícita** para publicar
- [ ] Não reivindicar prioridade; só pedir referências

---

## Por que é PERGUNTA e não teorema

- Originalidade **não certificada** (auditoria + revisão externa);
- Sem \((\tau_n,q)\) concretos: nenhum limite inferior (Teorema Q);
- Resultado numérico PR7 é **modelo estrutural**, não PA real.

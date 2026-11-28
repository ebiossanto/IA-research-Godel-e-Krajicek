# REFEREE — A1: incorporação das referências novas (arXiv:2604.04830 e 2607.13540)

**Rodada:** r1 · **Data:** 27/11/2026 · **Origem:** varredura web (`varredura_web/VARREDURA_WEB_2026-11-27.md`, ação A1).
**Entrega:** duas entradas novas em `krajicek_ddp/C_disjuncao_viavel.md` §9 (só lista de
referências) + duas em `krajicek_ddp/D_geradores_consequencias.md` §8 — **corpos intocados**
(dossiê sob auditoria externa).

## 1. O que foi verificado (não de segunda mão)

1. **HTMLs baixados como evidência**: `fontes/arxiv_2604.04830v3.html` (177 KB) e
   `fontes/arxiv_2607.13540v1.html` (173 KB); extração de texto visível + **listas de
   referências completas** (18 refs em 2604: Ilango=ECCC TR25-190 [4], gadget generator=K.2007 [7],
   [12]=Kra25 LMS 497, **[16]=Ren–Wang–Zhong ITCS 2026**, [17]=Rudich demi-bits).
2. **Varredura de termos** (script reexecutável `krajicek_ddp/_verify_refs.py`):
   - `2604.04830`: **ZERO** ocorrências de `2506.20221`, `DD_P`, `student-teacher`,
     `resolution`, `weak feasible disjunction`, `disjoint disjunction`.
   - `2607.13540`: **ZERO** ocorrências de `2506.20221`/`DD_P`.
3. **Achado lateral relevante**: ambos citam **Ren–Wang–Zhong, "Hardness of Range Avoidance and
   Proof Complexity Generators from Demi-Bits", ITCS 2026** — o paper por trás da palestra de
   H. Ren no INI-LFC (ligação registrada em D §8).

## 2. Objeções do referee e respostas

| # | Objeção | Resposta/veredito |
|---|---|---|
| **A1-1** | "Verif. integral" seria exagero? Só li o texto visível do HTML | **Corrigido na entrada**: redigido como "verif. HTML: texto visível + lista de refs completa, salvos em `fontes/…`" — não afirmo leitura página-a-página |
| **A1-2** | Preprints não-referidos podem ser citados como (A)? | Classificados **(A)-nc** explicitamente nas entradas (mesma regra do MAPA §1) |
| **A1-3** | A entrada pode "dizer mais" que o paper? | Não: a entrada descreve o que a **varredura** achou (incluindo o negativo: "não menciona Resolução/`DD_P`") e remete a §A.3 para a busca de prior art permanecer aberta |
| **A1-4** | O check negativo salva a alegação do Lema 4.1 ("não discutido nas fontes")? | **Parcialmente**: sobrevive a **mais uma** rodada de busca, mas *ausência num paper ≠ prova de ausência na literatura* — a **carta/prior-art search continua sendo a condição de publicação** do item ② (mantido intacto) |
| **A1-5** | Editar docs sob auditoria sem novo referee? | **Feito o contrário**: só listas de referências, corpo intocado; esta rodada é o referee; auditoria externa §A.3 não é afetada |
| **A1-6** | Duplicatas/consistência de chaves? | Chaves novas (`Kra26-fdp`, `RWZ26`, `Kra26-zk`) não colidem com existentes (`K25`, `Pap26`, `Rud97`…); conferido contra as duas listas |

## 3. Resultado

- **r1 APROVADO** — duas entradas em C, duas em D; nenhum corpo alterado; nenhum status
  alterado; nenhuma claim nova sobre resultados alheios (só metadata + escopo negativo verificado).
- **Pendências herdados** (não desta rodada): prior-art search do Lema 4.1 via `letters`;
  auditoria externa de `DD_Res ∈ P`.
- **Lints:** `gk_claims_lint` e `gk_prosa_lean_lint` executados após a edição (ver saída da sessão).

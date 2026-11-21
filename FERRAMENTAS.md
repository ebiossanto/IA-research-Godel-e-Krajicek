# FERRAMENTAS — catálogo das extensões executáveis do projeto Gödel–Krajíček

**Origem:** todas as ferramentas abaixo são **extensões do repositório
[IA-research-Godel-e-Krajicek](https://github.com/ebiossanto/IA-research-Godel-e-Krajicek)**
(Gödel · Krajíček · Sistemas Complexos — licença **MIT**, citação em
[`CITATION.cff`](CITATION.cff)). Cada ferramenta **encarna um resultado
teórico do projeto como núcleo executável**: um teorema, um gadget ou uma
metodologia nasceram primeiro como pesquisa (`krajicek_ddp/`, Eixos 1–3)
e viraram software verificável. Documentação completa por ferramenta em
[`ferramentas/`](ferramentas/README.md).

**Data do catálogo:** 20/11/2026 · **Teste global:** `python gk_claims_lint.py`
+ CI (lint · `lake build` · smoke).

---

## Catálogo

| Ferramenta | Código | O que é (núcleo teórico) | Aplicações | Doc |
|---|---|---|---|---|
| **minref** | `gk_minref.py` | Comprimento **mínimo exato** de refutação Res via encoder `REF_t` (fecho + pares completos) — gadget das frentes **C2/LP** | complexidade de prova finita; calibrar D4′; validação de encoders; verificação92/92 do teste LP | [`ferramentas/gk_minref.md`](ferramentas/gk_minref.md) |
| **dd-cert** | `gk_dd_cert.py` | **Teorema 4.3 (`DD_Res ∈ P`)** executável: π (DRAT/DAG/saturação) → **certificado da sub-derivação pura** + verificador independente | **auditoria externa** (peça do dossiê); detector de contraexemplos; certificação de evidências | [`ferramentas/gk_dd_cert.md`](ferramentas/gk_dd_cert.md) |
| **claims-lint** | `gk_claims_lint.py` + `.github/workflows/ci.yml` | **Metodologia Ten-Proofs**:10 regras de consistência de claims/evidências (R1–R10) + CI | impedir regressão epistêmica; proteger hashes; padrão para pesquisa com IA | [`ferramentas/gk_claims_lint.md`](ferramentas/gk_claims_lint.md) |
| **proof-fractal** | `gk_proof_fractal.py` + `_v2.py` + `_v2_r2.py` + `_v3.py` | **D4′**: séries de comprimentos de prova → Hurst R/S, Higuchi D_H, box-counting + bootstrap (Eixo FCT); **v2** = comprimentos **mínimos canônicos** (`minref`) vs DRAT pareado, famílias n≤6; **r2** = BCa + TOST + MDE80; **r3** = **boxdim pré-registrado** em dados disjuntos (pista A4 confirmada com Bonferroni) | discriminar regimes de crescimento de prova; invariância de fonte, equivalência quantitativa e replicação pré-registrada (v2/r2/r3) | [`ferramentas/gk_proof_fractal.md`](ferramentas/gk_proof_fractal.md) |
| **alternating-family** | `gk_alternating_family.py` | Codificação `REF_t` (semântica de linhas) + **critério-LP** e **Teorema Nec** da família alternante (C2.3) | decidir a via LP da rota negativa; fronteira exata de t | [`ferramentas/gk_alternating_family.md`](ferramentas/gk_alternating_family.md) |
| **c2-projection-sim** | `gk_c2_projection_sim.py` | Projeção `E` em `Res(k)` com invariantes I1–I5 + **contraexemplo G1** determinístico (frente C2) | detector automático de contraexemplos; caixa de ensaio (O1)–(O5); regressão do CI | [`ferramentas/gk_c2_projection_sim.md`](ferramentas/gk_c2_projection_sim.md) |
| **diagnóstico** | `diagnostico_ambiente.ps1` | Verificação ✅/❌ do ambiente (Git/Python/Julia/Lean/PATH; `-Build` = `lake build`; hash do sympy) | setup e reidratação do laboratório | [`AMBIENTE_E_FERRAMENTAS.md`](AMBIENTE_E_FERRAMENTAS.md) |

## Repositórios separados (distribuições autocontidas)

Cada ferramenta pronta também tem seu **próprio repositório público**
(extração deste — mesmo código, MIT e `CITATION.cff`, com CI próprio):

| Ferramenta | Repositório |
|---|---|
| minref | <https://github.com/ebiossanto/IA-Research-GK-MinRef> |
| dd-cert | <https://github.com/ebiossanto/IA-Research-GK-DD-Cert> |
| claims-lint | <https://github.com/ebiossanto/IA-Research-GK-ClaimsLint> |
| proof-fractal | <https://github.com/ebiossanto/IA-Research-GK-ProofFractal> |
| alternating-family | <https://github.com/ebiossanto/IA-Research-GK-AltFamily> |
| c2-projection-sim | <https://github.com/ebiossanto/IA-Research-GK-C2Sim> |

A **proveniência teórica permanece aqui**: cada repo cita este como origem
(seção "Extração de …" no README) e remete aos documentos/referees
(`krajicek_ddp/`, `ferramentas/`) para o núcleo de cada resultado.

## Uso rápido

```bash
python gk_claims_lint.py                 # 10/10 regras (~1s)
python gk_minref.py demo                 # validação do minref
python gk_dd_cert_test.py                # 7/7 do extrator de certificados
python gk_c2_projection_sim.py --n 400   # invariantes + contraexemplo G1
python gk_proof_fractal.py               # D4′ v1 (seed fixa, ~4min)
python gk_proof_fractal_v2.py            # D4′ v2: minref canônico (~17min)
python gk_proof_fractal_v2_r2.py         # r2: BCa + TOST + MDE80 (~40s)
python gk_proof_fractal_v3.py            # r3: boxdim pré-registrado (~35min)
python gk_proof_fractal_v3.py --analyze-only  # re-análise (~1min)
python -File diagnostico_ambiente.ps1    # ambiente (-Build = lean)
```

## Tabela de evidências (afirmação ↔ arquivo que comprova)

> Diretriz de rigor: cada claim do catálogo é cruzado com o artefato que
> o testa — sem promessa sem prova.

| Afirmação (onde é feita) | Evidência executável / artefato |
|---|---|
| minref devolve comprimento mínimo **exato** (unidades=3, ABC=5, cadeias 2k+1) | `python gk_minref.py demo` → `VALIDACAO OK` (fronteiras conhecidas); auditoria: `gk_minref_referee.md` §A3 (92/92) |
| minref é determinístico e reproduzível | `gk_minref_results.json` (sha256 registrado) + R6 do lint |
| dd-cert extrai e **verifica** certificados (7/7) e recusa adulteração | `python gk_dd_cert_test.py` → `TODOS OS TESTES OK` (T3 adulteração RECUSADA); CI job `smoke` |
| claims-lint detecta claims inconsistentes (10/10 regras) | `python gk_claims_lint.py` → `LINT OK`; fixtures: `demo/` (exit 0) + `demo_bad/` (exit 1) no CI do repo `IA-Research-GK-ClaimsLint` |
| D4′ v1: D_H separa `php` (4/4 IC95 exclui 0) | `gk_proof_complexity_fractal.json` (§`contrasts`) + `gk_proof_fractal_series.csv` (sha `92e1ffd3…`); referee `28_..._referee.md` §B |
| D4′ v2: 192/192 UNSAT, 0 censuras, minref<DRAT | `gk_proof_fractal_v2_series.csv` (sha `b8aecc2d…` — reprodução byte-a-byte demonstrada, referee §A6) |
| D4′ v2: H_C3/H_C4 **sem separação** (6/6 incluem 0) | `gk_proof_fractal_v2.json` → `hypotheses.*.veredito` + `contrasts` |
| D4′ r2: BCa implementação correta | `gk_proof_fractal_v2_r2.json` → `selftest_bca` = `OK` vs `scipy.stats.bootstrap` (diff 0,013) |
| D4′ r2: equivalência ±0,20 = 6/6; ±0,10 inacessível (MDE80≈0,19) | `gk_proof_fractal_v2_r2_contrasts.csv` (colunas `equivalente_d*`, `mde80`; sha `ce26b53a…`) + doc `29_...` §8.2/§8.4 |
| D4′ r2: exclusão r1 **não conta** (incoerente) | `gk_proof_fractal_v2_r2.json` → `H_C4.*.incoerentes` + regra `metadata.regra_incoerencia` |
| D4′ r3: **pré-registro anterior ao run** (hipóteses/margens/grade) | commit `66f40ae` (push anterior à execução) + `30_...` §1 + `pre_registro` no `gk_proof_fractal_v3_analysis.json` |
| D4′ r3: dados disjuntos do r2 (anti-circularidade) | `gk_proof_fractal_v3.json` → `selftest_disj` = `OK`, interseção ∅ (aborta se intersectar) |
| D4′ r3: pista A4 **confirmada com Bonferroni** (Δ=−0,170) | `gk_proof_fractal_v3_contrasts.csv` → `drat:implication-cadeia:boxdim:raw` (`bca_bonf_*`, sha `0cb1dce2…`) |
| D4′ r3: padrão-τ 2/3; imp−cadeia não separa (eq±0,05 não certificável) | `gk_proof_fractal_v3_analysis.json` → `H_B1` (BC90/BC97,5% por teste) + tabela de sensibilidade `30_...` §3.1 |
| D4′ r3: incoerência é do par, não da métrica (H_B4 refutada) | `H_B4.por_metrica` (boxdim 3/27, higuchi 0/27, saltos 0/27) |
| D4′ r3: delete-d ≡ delete-1 (0/135) + tipo-I 0,04 + poder 9/10 | `contrasts.csv` coluna `jack_concordancia` + `gk_proof_fractal_v3.json` → `selftests.S4S5` |
| 7º/8º bugs corrigidos sem invalidar v1 | referee `28_...` §A9–A11 + errata `28_...` §5 (v1: 188/188 UNSAT por solver, CSV congelado) |
| Ferramentas públicas autocontidas com CI verde | 6 repos `IA-Research-GK-*` (links acima) + `.github/workflows/ci.yml` de cada um |
| Ambiente verificável | `python -File diagnostico_ambiente.ps1` → ✅/❌ (`AMBIENTE_E_FERRAMENTAS.md`) |

## Como citar

```bibtex
@software{soares2026godelkrajicek,
  author  = {Soares dos Santos, Euzébio},
  title   = {IA-research-Godel-e-Krajicek: G\"odel, Kraj\'icek e Sistemas Complexos},
  year    = {2026},
  url     = {https://github.com/ebiossanto/IA-research-Godel-e-Krajicek},
  license = {MIT}
}
```
Citações auxiliares por ferramenta: seção "Como citar" de cada doc em
[`ferramentas/`](ferramentas/README.md).

## Referências teóricas de base (do projeto)

1. Krajíček, J. *Proof Complexity*, CUP 2019 (caps. 5.7, 17.7) — DOI 10.1017/9781108242066.
2. Krajíček, J. *On NP∩coNP proof complexity generators*, arXiv:2506.20221 (LMCS 22(2:14)) — alvo da campanha DD_P.
3. Garlík, M. *Failure of FDP for k-DNF Resolution…*, CCC 2024 — DOI 10.4230/LIPIcs.CCC.2024.33.
4. Krajíček, J. & Pudlák, P. *Quantified propositional calculi…*, Z. math. Logik **36** (1990) 29–46.
5. Pudlák, P. *The Lengths of Proofs*, Handbook of Proof Theory ch. VIII (1998).
6. Documentos internos de origem: `krajicek_ddp/C_disjuncao_viavel.md` (Teo 4.3),
   `28_PONTE_PROVA_FRACTAL_D4.md` (D4′), `C2_LP_familia_alternante.md` (Nec),
   `C2_r2_G1_contraexemplo.md` (G1), `AGENTS.md` (Ten-Proofs).

---

*Organização: docs por ferramenta em `ferramentas/`; dados de resultado no
raiz (prefixo `gk_*`); auditorias/referees junto aos docs de origem.
Todo código é MIT e testado no CI deste repositório.*

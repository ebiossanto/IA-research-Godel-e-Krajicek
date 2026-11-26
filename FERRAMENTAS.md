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
| **proof-fractal** | `gk_proof_fractal.py` + `_v2.py` … `_v6.py` | **D4′**: séries de comprimentos de prova → Hurst R/S, Higuchi, box-counting, **boxdim** e **saltos** + bootstrap (Eixo FCT); **v2** = mínimos canônicos vs DRAT; **r2** = BCa+TOST; **r3** = boxdim pré-registrado; **r4** = diagnóstico de z0; **r5** = `saltos` primário 3/3 + método calibrado; **r6** = estratos exatos do `relinc` + **consolidação** (boxdim **6/6**, saltos **3/3 na4ª rodada**, Cochran sem heterogeneidade, MDE 6/6) | discriminar regimes de crescimento de prova; invariância de fonte, equivalência, replicação e **linha de inferência consolidada** (v2→r6) | [`ferramentas/gk_proof_fractal.md`](ferramentas/gk_proof_fractal.md) |
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
python gk_proof_fractal_v4.py            # r4: n=384 + z0 (~1.9h; usa --resume p/ retomar)
python gk_proof_fractal_v5.py            # r5: saltos prim. + estratificado (~3h; --resume)
python gk_proof_fractal_v6.py            # r6: relinc exato + consolid. (~3h; --resume)
python gk_proof_fractal_v6.py --reanalise-r5  # H_E1 (~36min)
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
| D4′ r4: **`saltos` CONFIRMADA 3/3 Bonferroni** (âncoras r3 replicadas) | `gk_proof_fractal_v4_contrasts.csv` → 3 chaves `*:saltos:raw` (`bca_bonf3_*` + `pct_*` concordam; sha `8419f25b…`) + `H_C2` no `gk_proof_fractal_v4_analysis.json` |
| D4′ r4: boxdim INDETERMINADO (2/6 contáveis, 4 incoerentes) pela régua exaustiva | `H_C1.veredito` no JSON (regras A3 no doc `31_` §1.5) + `veredito=INCOERENTE` no CSV |
| D4′ r4: mecanismo de z0 medido (viés/SE; incoerência 7%→33% com n) | `H_C3` no JSON (D1=0,94; D2 CONFIRMADA; 16 degenerados no clamp) + colunas `z0,bias_over_se,degenerate` |
| D4′ r4: alvo de poder 4/6 (falha declarada) | `H_C4_alvo_MDE.valores` (0,0609 e 0,0684 ≥ 0,06) |
| D4′ r4: crash CaDiCaL contido por checkpoint (3 tentativas, dados íntegros) | `3d244ab` (plumbing separado do pré-registro `9fe7165`) + `mode=resume+collect+analyze` no JSON + sha `c92f0968…` |
| D4′ r5: **`saltos` PRIMÁRIO CONFIRMADO 3/3 Bonferroni** (3ª rodada) | `gk_proof_fractal_v5_contrasts.csv` → 3 chaves `*:saltos:raw` (`pct_bonf3_*` excluem, pontos dentro) + `H_D1.veredito` no `gk_proof_fractal_v5_analysis.json` (sha `c30b13f2…`) |
| D4′ r5: método escolhido **pela calibração** (percentil estrat.: tipo-I 0,075 vs BCa 0,325) | `gk_proof_fractal_v5.json` → `selftests.calibracao.S4/S6` (gates pré-run) + `metadata.metodo_primario` |
| D4′ r5: incidência real 4,4% (r4:33%) + head-to-head bloco8 **0/9 vs 4/9** | `H_D3_incidencia` no JSON + colunas `block8_outside`/`discordante` no CSV |
| D4′ r5: H_D2 PARCIAL 5/6 (eq±0,05 certificada; (a) sem efeito 3ª vez) | `H_D2_boxdim_secundario.testes` no JSON (`equivalente_d0.05` em (c)) |
| D4′ r5: alvo de poder **6/6 ATINGIDO** (MDE 0,014–0,052) | `H_D4_alvo_MDE.valores` no JSON |
| D4′ r5:2 bugs de plumbing pós-pré-reg corrigidos, smoke test como procedimento | `8209433` + `0919e6b` (diffs separados do pré-registro `b6c359f`) + registro no doc `32_` §3 |
| D4′ r6: estratos exatos do `relinc` resolvem os5 discordantes do r5 | `gk_proof_fractal_v6_reanalise_r5.json` (H_E1: 5/45→2/45, sha `d3b6b336…`) + H_F3 (1/45 em dado novo) |
| D4′ r6: saltos **3/3 na4ª rodada** + **Cochran sem heterogeneidade** (sem tendência em4 rodadas) | `gk_proof_fractal_v6_analysis.json` → `H_F1_saltos_4a_rodada` (incl. `tendencia_Q` p=0,13–0,71) + `gk_proof_fractal_v6_contrasts.csv` (sha `c567dbfd…`) |
| D4′ r6: boxdim **CONFIRMADA 6/6** (2 equivalências +4 direcionais Bonferroni;5/6 bloqueados pelo método r4) | `H_F2_boxdim_consolidado.testes` no JSON + coluna `block8_outside` no CSV |
| D4′ r6: ramo concordante **disparou4×** (mantido — condição de remoção não ocorreu) | `H_F4_ramo_concordante.flags` no JSON |
| D4′ r6: poder no máximo da linha (MDE 0,014–0,042, 6/6) | `H_F5_poder.valores` no JSON |
| τ k↑: `minref_deep` estende o minref p/ n>6 (pools `d≤t`, pares dedup) | `gk_minref.py` (`minref_deep`, `tree_depths`) + propriedade **17/17** no `demo` (`python gk_minref.py demo` → `VALIDACAO OK`) + `ferramentas/gk_minref.md` §4.7–4.8 |
| τ k↑: **H_t1 CONFIRMADA** — n=7 exato em 89,4% (118/132) com max_aux=6M | `gk_tau_kup.json` → `H_t1_viabilidade.veredito` + distribuição 5:28/7:84/9:1/11:5 no `gk_tau_kup_series.csv` (sha `f5d51c57…`) |
| τ k↑: **H_t2 REFUTADA (0/2) — leitura dupla: contrastes INCONCLUSIVOS** (MDE 0,53/0,59; censura 0/11/58%) | `gk_tau_kup.json` → `H_t2_dinamica.testes` (k3−k2 = −0,243 [−0,606,+0,135]; k4−k3 = +0,106 [−0,323,+0,526]) + tabela `niveis` + condição de redação no referee `34_..._referee.md` §B |
| τ k↑: lacuna `drat−minref` cresce com k (1,79→3,47→4,49) = **(P) descritivo, não-claim** | `gk_tau_kup.json` → `niveis.*.drat_mean − minref_mean` + §4.3 do doc `34_` (candidata (C) só com pré-registro futuro) |
| τ k↑: ASSERT `minref ≥ d(∅)` **0/396** + patch `saturation` mid-run invariante | `gk_tau_kup.json` → `_assert.violacoes=[]` + §2.1 do doc `34_` (equivalência 28/28 + demo17/17 + 9/9 fecho×CSV; s=1655 `fecho=9061` idêntico à sonda) |
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

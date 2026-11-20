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
| **proof-fractal** | `gk_proof_fractal.py` | **D4′**: séries de comprimentos de prova → Hurst R/S, Higuchi D_H, box-counting + bootstrap (Eixo FCT) | discriminar regimes de crescimento de prova; base p/ provas mínimas (v2) | [`ferramentas/gk_proof_fractal.md`](ferramentas/gk_proof_fractal.md) |
| **alternating-family** | `gk_alternating_family.py` | Codificação `REF_t` (semântica de linhas) + **critério-LP** e **Teorema Nec** da família alternante (C2.3) | decidir a via LP da rota negativa; fronteira exata de t | [`ferramentas/gk_alternating_family.md`](ferramentas/gk_alternating_family.md) |
| **c2-projection-sim** | `gk_c2_projection_sim.py` | Projeção `E` em `Res(k)` com invariantes I1–I5 + **contraexemplo G1** determinístico (frente C2) | detector automático de contraexemplos; caixa de ensaio (O1)–(O5); regressão do CI | [`ferramentas/gk_c2_projection_sim.md`](ferramentas/gk_c2_projection_sim.md) |
| **diagnóstico** | `diagnostico_ambiente.ps1` | Verificação ✅/❌ do ambiente (Git/Python/Julia/Lean/PATH; `-Build` = `lake build`; hash do sympy) | setup e reidratação do laboratório | [`AMBIENTE_E_FERRAMENTAS.md`](AMBIENTE_E_FERRAMENTAS.md) |

## Uso rápido

```bash
python gk_claims_lint.py                 # 10/10 regras (~1s)
python gk_minref.py demo                 # validação do minref
python gk_dd_cert_test.py                # 7/7 do extrator de certificados
python gk_c2_projection_sim.py --n 400   # invariantes + contraexemplo G1
python gk_proof_fractal.py               # D4′ (seed fixa, ~4min)
python -File diagnostico_ambiente.ps1    # ambiente (-Build = lean)
```

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

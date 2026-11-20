# ferramentas/ — Documentação das ferramentas do projeto

**Origem:** todas as ferramentas deste diretório são **extensões do
repositório [IA-research-Godel-e-Krajicek](https://github.com/ebiossanto/IA-research-Godel-e-Krajicek)**
(Gödel · Krajíček · Sistemas Complexos, licença MIT) — cada uma carrega um
resultado teórico do projeto como núcleo executável. O catálogo completo
está em [`../FERRAMENTAS.md`](../FERRAMENTAS.md).

| Documento | Ferramenta (código na raiz) | Núcleo teórico de origem |
|---|---|---|
| [`gk_minref.md`](gk_minref.md) | `gk_minref.py` | Encoder REF_t (fre­ntes C2/LP) + R(f) de Krajíček |
| [`gk_dd_cert.md`](gk_dd_cert.md) | `gk_dd_cert.py` | **Teorema 4.3** (`DD_Res ∈ P`, `C_disjuncao_viavel.md`) |
| [`gk_claims_lint.md`](gk_claims_lint.md) | `gk_claims_lint.py` + `.github/workflows/ci.yml` | Metodologia Ten-Proofs + auditoria externa §4.5 |
| [`gk_proof_fractal.md`](gk_proof_fractal.md) | `gk_proof_fractal.py` | Experimento **D4′** (ponte prova→fractal) |
| [`gk_alternating_family.md`](gk_alternating_family.md) | `gk_alternating_family.py` | Família alternante (C2.3) + Teorema Nec |
| [`gk_c2_projection_sim.md`](gk_c2_projection_sim.md) | `gk_c2_projection_sim.py` | Contraexemplo r2 (G1) e invariantes de `Res(k)` |

**Como citar qualquer ferramenta:** ver a seção "Como citar" de cada
documento (formato compatível com [`../CITATION.cff`](../CITATION.cff)).

**Repositórios separados:** cada ferramenta pronta também está
distribuída em seu próprio repo público (extração deste, CI próprio) —
links na seção "Repositórios separados" de [`../FERRAMENTAS.md`](../FERRAMENTAS.md).

**Testes:** `python gk_dd_cert_test.py` · `python gk_minref.py demo` ·
`python gk_c2_projection_sim.py --n 400` · `python gk_claims_lint.py` —
todos rodando no CI (`.github/workflows/ci.yml`).

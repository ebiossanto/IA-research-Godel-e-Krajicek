# Onde Estamos, Próximos Passos e Descobertas Possíveis
### Terminal-Laboratório · IA-Research Gödel/Krajíček · FCT · Motor Fractal

> Documento próprio **(P)**, 13 Out 2026. Resposta prática à questão: *o que
> já temos, o que falta, como avançar em descobertas ou criar algo original,
> usando o laboratório e o motor fractal para testar ideias e gerar novos dados.*
> Escrito em regime Ten-Proofs (ver `AGENTS.md` e skill `ten-proofs`): nenhum "verificado"
> aqui significa comando reproduzível + saída congelada.

---

## 1. Mapa do programa (visão geral)

**Eixo único, duas vertentes:**

| Vertente | Pergunta | Evidência (nível) | Ferramentas |
|---|---|---|---|
| **DD_P — Krajíček** | A prova do Teorema 4 (v4)/3 (v5) de 2506.20221 fecha? | Lacuna verbatim (F1), Teorema K (J1), `C_{N_s}≡⊥` condicional (M.2), `DD_Res∈P` (C v1) | Lean 4, Z3/SAT, auditoria externa pendente |
| **FCT (Fractal Control Theory)** | Obstruções algébricas (grupos finitos, pps) → latência de cauda em filas | 4 eixos; P99 formula, bullwhip, não-abeliano 2×, PFA em `ρ_c=0.25` | motor fractal (Hurst, DFA, box-counting), LTspice/FreeFEM/CVC5 |

O **Terminal-Laboratório** (este repo) é o veículo experimental: coleção de telemetria +
análise de entropia + REA (Reverse Engineering Analysis) + Z3/SMT + julia + Lean.
O **Motor Fractal** (`integrations/fractal_engine/` → raiz `fractal_engine/`) implementa os 4 eixos.

---

## 2. Onde estamos hoje — estado honesto (Level 0→4)

### 2.1 DD_P / Krajíček
- **L0–L2 (constituído, referee-processado):** A–N + 3 frentes de 3ª onda (N2, C2, Q2)
  são **RECOMENDADO** (revisão **interna** — não peer review). Lacuna `Log(M*)=Log(M')→i₀∈M*`
  real em v4 e v5. Teorema K (coleção interna impossível), L.1, canto adversarial M.0–M.5
  (M.2 **condicional** à semântica de `τ_N` — Q1 da carta decide).
- **L1 (programa):** `DD_Res ∈ P` (T4.3, C2.1) é teorema **com auditoria externa
  pendente** (`krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md`).
- **L3+ (aberto declarado):** consequências para `NP≠coNP` só via
  `(2.1)+(ST)⟹NP≠coNP`; `¬2.1⟹P≠NP` — **nenhuma** afirmada incondicionalmente;
  ponte L2→L3 **não** demonstrada.
- **Carta a Krajíček**: ENVIADA 11/10/2026 (Q1–Q4) — aguardando resposta.
  Provedor cabeça: `localhost` (não afirma notificação/notary external).
- **Compilação:** Lean 4 raiz `lake build` → `Build completed successfully (4 jobs)` **confirmado
  em 13/10/2026**, com **2 `sorry`** documentados em `lean4/Gothic_Generators/DDP.lean:628/690`.

### 2.2 Campanha PPR-3 real (Z3/SAT, commits 12/10–13/10)
Reproduzida **nesta sessão** (Level 2):

| Experimento | Claim | Reprodução | Saída |
|---|---|---|---|
| `gk_theta_smt_z3.py` | PPR-3 real via Z3 (Craig interp.) | 216/216 válidos (100%) | `gk_theta_smt_z3*.json/csv` |
| `gk_drat_translation_real.py` | DRAT translation real | 216/216 válidos (100%) | `gk_drat_translation*.json/csv` |
| `gk_hardness_z3_real.py` | `s_Res=21.2`, `s_EFrege=17.0` medidos | reproduzido | `gk_hardness_z3_real*.json/csv` |
| `gk_omega_proof.py` | `T_ω=PA+RFN^ω`, δ→0 uniforme | convergência SIM, PPR pass 100% | `gk_omega_proof*.json/csv` |
| `gk_hardness_separation_real.py` | Resolution EXP vs EFrege POLY | (existente em JSON) | `gk_hardness_separation.json` |

### 2.3 Motor Fractal — **FRÁCIL, agora FUNCIONANDO (com fixes)**
- O commit `8f77799 "Fractal Engine Integration — completo"` tinha **runner quebrado**
  (`integrations/fractal_engine/*` inexistente; `Any` não importado em 7 módulos;
  `if not data` quebrando numpy arrays; `C_r = count/len; C_r.append(C_r)` no
  `correlation_dimension`; `predict_collapse_window` chamado onde não existe).
- **FIXES APLICADOS HOJE (13/10/2026):** corrigidos `paths` do runner, +`Any` em 7
  arquivos, guardas `if data is None or len(data)==0`, typo no correlation-dim.
- **RESULTADO:** `python fractal_engine/run_fractal_engine.py all` → **5/5 PASS**:
  Bridge (P99=5.440, H=0.7219), Bullwhip (amp=1.72), Nonabelian (E*=0.2458, destr=2),
  Stochastic (protection=0.9911), Fractal Entropy (H=2.7562, D=0.8247).
- **NOVO DADO GERADO:** `gk_fractal_engine_experiments.json` — **24 records** (4 kinds
  de regime × 3 seeds × 2 tamanhos) com os 4 eixos FCT + entropia real (box-counting).

### 2.4 Infra / reproduzibilidade (GAPs reais honestos)
1. `INDICE.md` ainda v6.17 — **não** indexa a campanha nova (PPR-3/Z3/DRAT/ω/fractal).
2. `EVOLUCAO_PROJETO.md` só chega até §11.8 (avaliação 12/10) — sem a fase 12+13.
3. `gk_lean_bridge.py` relata teoremas NOT_FOUND por limitação de tooling
   (greppeia output do lake build, que não imprime nomes). **Build real é verde**
   (Core.lean possui delta_mono, theorem4_strict, rcs_exists, covered_mono, etc.).
   → o JSON `gk_lean_verification.json` é stale (False) mas o estado real é Verde.

---

## 3. Ten-Proofs — nível de cada artefato (honestidade epistêmica)

| Artefato | N0 Proposição | N1 Prova escrita | N2 Verificação de máquina | N3 Meta-verif | N4 Externa |
|---|---|---|---|---|---|
| `DD_Res∈P` (T4.3) | ✔ | ✔ | **pendente** (auditor externo) | — | `pending` |
| Z3 PPR-3 real (216/216 ×2) | ✔ | ✔ (Z3) | ✔ **hoje** | — | `pending` |
| Hardness Z3 (`s_Res=21.2`) | ✔ | ✔ | ✔ **hoje** | — | `pending` |
| Ordinal ω chain | ✔ | ✔ | ✔ **hoje** | — | `pending` |
| Lean 4 Core | ✔ | ✔ | ✔ `lake build` verde | — | `pending` |
| Fractal Engine FCT 4 eixos | ✔ | ✔ | **✔ hoje (5/5)** | — | `pending` |
| Novo dado fractal (24 records) | — | ✔ | **✔ hoje** | — | `pending` |

**Higiene epistêmica:** "reproduzido aqui, hoje" vale para N2 machine-verifiable *desta máquina*;
N4 exige auditor externo — nenhuma dessas frentes tem ainda.

---

## 4. Próximos passos (prioridade realista)

### A. Curto prazo (dias, alto sinal/baixo custo)
1. **Responder quando a carta de Krajíček chegar** (Q1 decide o condicional M.2
   e o escopo de N) — registrar no dossiê + propagar.
2. **Auditoria externa de `DD_Res∈P`** (pacote já pronto) — enviar a um especialista
   de proof complexity (krajicek@karlin.mff.cuni.cz já está ciente; MathOverflow
   só com confirmação do autor).
3. **Varredura K19 caps. 9/17 + KP90** para fonte Σ₁ da Q2.4 (evita claim vazio).
4. **Atualizar INDICE (v6.18+) e EVOLUCAO_PROJETO (Fase 12+)** para indexar a
   campanha PPR-3 real/Z3/DRAT/ω/fractal — gap real.
5. **Regenerar `gk_lean_bridge.py` output** (ou substituir por um verificador baseado
   em `lean4` recente) para não deixar stale de verificação.

### B. Médio prazo (semanas)
6. **N3** — construir `(∗′)` por compactibilidade/omission types; incluir canto
   χ≡⊤ (coincidência denotacional `g(t̄)^{M0}=Taut(α̂)`).
7. **C2 (obrigações O1–O5)** — fechar o algoritmo para `Res(k)` com texto exato
   de [K19 5.7] + Lema 4.1; atacar a **família alternante (C)** via reflexão com
   lado "espectador" satisfatível.
8. **Lean: resolver os 2 `sorry`** em DDP.lean (ou justificar como laboratorial).
9. **Fractal Engine:** rodar os 5 módulos individuais para criar **datasets
   institucionais** (Bridge, Bullwhip, Nonabelian, Stochastic, Entropy) — as
   métricas hoje são sintéticas de seed fixa. Per ten-proofs, fixar seed + hash.
10. **Validar a fórmula `P_{99}=P^ideal(1+ρ/(1-ρ)·p²)`** contra os dados reais
    do `cpu_timeseries`/rea_bridge (quando disponível na máquina-alvo).

---

## 5. Descobertas originais possíveis — o que podemos criar hoje

Propostas **executáveis já**, com o laboratório + motor fractal tentando gerar
novos dados e talvez descobertas (todas marcadas com nível Ten-Proofs previsto):

### D1. Quantização do PFA à taxa de transição ρ_c
A fórmula `ρ_c=0.25` é derivada analiticamente. **Testar**: varrer
`controller_states m ∈ {2,3,4,5,6,7}` e `system_states n ∈ {4,8,16}` no motor
fractal e medir, via bootstrap sobre telemetria sintética, se o **mínimo
empírico** da curva inflação×ρ coincide com `1/4`. Se não coincidir → paper
refuting/enhancing a quarta onda.
**Novo dado:** `gk_fractal_phase_transition.csv` (m, n, ρ_c empírico, CI).
**Nível previsto:** N0 + N1, N2 via simulação. (C).

### D2. "Rigidez de grupos não-abelianos" como feature real
A destruição 2× para `S_n` é calculada. **Testar** em 2 séries reais: uma
cadeia de processos não-comutativos (multiplicadores matriciais / convolução
interfoliada) vs abeliana — medir se a dimensão fractal/box-counting e o H
realmente **sepam** as duas classes. Se o motor Distingue → um detector de
ordem de grupo de fonte de dados (talvez utilitário).
**Novo dado:** `fractal_nonabelian_SEPARATION.csv` (classe non/ab, n=..., métricas).
**Nível previsto:** N2 via cross-validation (β, ρ).

### D3. Predição de colapso em cpu_timeseries reais (aqui plausível de virar dado
novo).
Se `cpu_timeseries.csv` (presente no doc de reidratação) estiver coletado,
rodar `run_fractal_canary_test` nela e comparar **Huste ajustado vs colapso
observado nas 24h seguintes**. Se acertar → transforma o motor em instrumento
de monitoração real; se não → delimita honestamente o domínio (laboratorial).
**Novo dado:** `fractal_collapse_prediction_log.csv` (timestamp, H, predição, rótulo real).

### D4. "Proof Length → Fractal Dimension" (ponte original de maior valor)
Combinar a campanha PPR (216 testes Z3 reais) com o motor fractal: pegar
os 216 casos, calcular a **curva de "entropia de prova"** (`prob(z/¬z)` do
interpolante) como série ordinal e extrair H/D; testar se a provas de
Resolution (s_Res=21.2) exibem **fractalidade mais alta** que Extended Frege
(s_EF=17.0) e se essa diferença é estatisticamente significativa.
**Novo dado:** `gk_proof_complexity_fractal.json` (174?² tests × H,D).
**Nível previsto:** N1 (script reproduzível), N2 (estatística via bootstrap).
**Hipótese (C):** extensões de eficiência (EF) "aplaçam" a curva de prova → H
mais baixo; Resolution mantém auto-similaridade (H mais alto). Se falsa,
documenta.

### D5. ω como potencial verdadeiro (downstream do `T_ω`)
Usar os 17 termos da cadeia ordinal ω (η values) gerados por `gk_omega_proof.py`
como **entrada** para o motor fractal — produz um "perfil de convergência
fractal" do caminho `T_n → T_ω`. Se o H da série de η vai a 1 (persistente)
conforme n→∞, reforça a "estabilidade transfinite" empiricamente.
**Novo dado:** `gk_omega_fractal_profile.csv` (n, η_mean, H, D).
**Nível:** N2 automatizado.

### D6. Detecção de colapso por entropia (Shannon de CPU)
Continuar a coleta via `entropy_calc.py` (+ Julia syscalls) e rodar o motor
fractal sobre as séries coletadas. Objetivo: **provar ou refutar** a tese de
que o "atrito do observador" eleva artificialmente o H — em dados com carga
conhecida (synthetic load), a H corrigida deve ficar **dentro de ±0.15** da H
da série sem observador. Se o motor recomenda PFA em carga > `ρ_c`, testar se
a liberação `sqrt(ρ)` realmente protege.
**Novo dado:** série controlada em `cpu_timeseries.csv` (team).

---

## 6. O que NÃO devemos fazer (disciplina de pesquisa)

- **Não** apresentar PPR-3 real / Z3 como "prova de lower bound de proof
  complexity" — os 216/216 verificam a *tradução*, não a ausência de prova
  curta. (Lógica ≠ empiria — Hipótese δ≥γ≥β≥ρ.)
- **Não** chamar RECOMENDADO de peer review (P1 da avaliação 12/10).
- **Não** tratar `M.2` como teorema incondicional (depende de `τ_N`/Q1).
- **Não** empurrar o motor fractal em claims de complexidade computacional —
  ele mede séries temporais, não provas.
- **Não** committar experimentos sem reproduzibilidade (seed+hash+comando).

## 7. Compromisso prático (a próxima sessão, 13/10/2026)

1. Rodar `fractal_engine/run_fractal_engine.py all` em **seed fixa+hash** e commitar.
2. Atualizar INDICE (v6.18) + EVOLUCAO (Fase 12) em uma subárvore dedicada.
3. Reproduzir um dos D1–D6 e virar a descoberta em dado novo commitado
   (comando + saída congelada + SHA-256 → N2 Ten-Proofs).
4. Responder ao Krajíček (delta Q1–Q4) imediatamente ao chegar, propagando.
5. Enviar o pacote de auditoria `AUDITORIA_EXTERNA_DDRES_G-N.md` a um especialista
   (1 via).

## 8. Invariantes do método (obrigatórios aqui, por AGENTS.md)

- Toda descoberta nova entra **aditivamente** (`formal-certification/`); sem
  tocar na essência dos resultados existentes (D1–D6 retraídos ficam retraídos).
- Honestidade epistêmica: Nível não executado ⇒ `pending`. Auditor externo só conta
  com auditor externo real.
- Commit seletivo: `formal-certification/**` apenas para commits do método;
  commits de pesquisa (fixes+dados) separados.

---

*Gerado por análise do repositório clonado em 13/10/2026
(HEAD `d019851 feat: REHYDRATION.md`). Referência: `gk_fractal_engine_experiments.json`,
`CRITICA_EXTERNA_2026-10-12.md`, `AUDITORIA_EXTERNA_DDRES_G-N.md`, `RELATORIO_CONSOLIDADO.md`.*

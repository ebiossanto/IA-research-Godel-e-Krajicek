# gk_dd_cert — Extrator de certificados DD (o Teorema `DD_Res ∈ P` executável)

**Origem:** extensão do repositório
[IA-research-Godel-e-Krajicek](https://github.com/ebiossanto/IA-research-Godel-e-Krajicek)
(MIT) — núcleo teórico: **Teorema 4.3** de
[`krajicek_ddp/C_disjuncao_viavel.md`](../krajicek_ddp/C_disjuncao_viavel.md)
(frente C da campanha DD_P: **`DD_Res ∈ P`**, RECOMENDADO) + o simulador
`gk_c2_projection_sim.py` (frente C2, invariantes I1–I5).
**Código:** `gk_dd_cert.py` · **Teste:** `python gk_dd_cert_test.py` (7/7,
no CI) · **Auditoria:** [`gk_dd_cert_referee.md`](../gk_dd_cert_referee.md)
(r1 RECOMENDADO)

## Como citar

> Soares dos Santos, E. (2026). *gk_dd_cert — DD certificate extractor*
> [Software]. Em: IA-research-Godel-e-Krajicek.
> <https://github.com/ebiossanto/IA-research-Godel-e-Krajicek>. Licença MIT.
> Teorema-base: Soares dos Santos, E. (2026). *C — disjunção viável*
> (`krajicek_ddp/C_disjuncao_viavel.md`, Teorema 4.3) — ver `CITATION.cff`.

---

## 1. O que é

Executável do teorema **`DD_Res ∈ P`**: dado um problema de disjunção
`(π, ⋁_{i<m} Λᵢ)` — π refutação de `Λ = Λ₁ ⊎ … ⊎ Λₘ` (CNFs, variáveis
**disjuntas**), devolve:

- um lado **i\*** com **certificado**: a **sub-derivação pura** de `Λ_{i*}`
  (todas as linhas só com variáveis de `X_{i*}`, folhas ∈ `Λ_{i*}`, raiz `∅`,
  ≤ |π| linhas) — **JSON verificável**; ou
- **relatório de violação** (motor `Res(k)`: localiza a linha e o motivo —
  ex.: `G1` retenção parcial de bloco — o detector automático de
  contraexemplos do referee r2); ou
- recusa limpa de **hipóteses violadas** (lados não disjuntos, folhas
  impuras).

Inclui **verificador independente** (`verify`): recheca o certificado
*sem* importar a lógica do extrator — a peça que o **auditor externo**
roda (`exit 0/1`).

## 2. Para que serve (aplicações)

1. **Auditoria externa** de `DD_Res ∈ P` (`krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md`
   §A pede recorte/DAG/pureza — este é o artefato executável);
2. **Detector automático de contraexemplos** para promessas de projeção
   (era manual na frente C2);
3. **Certificação de evidência** em experimentos: qualquer entrega que
   precise "mostrar o lado tautológico" com prova verificável;
4. Pesquisa: testar variantes de promessa/extração (DRAT vs DAG vs
   saturação) sobre o mesmo teorema.

## 3. Como usar

```bash
python gk_dd_cert.py demo                  # 4 casos (2 resolução + 2 Res(k))
python gk_dd_cert.py extract entrada.json  # → gk_dd_cert_certificate.json
python gk_dd_cert.py verify  cert.json     # → exit 0 (ACEITO) / 1 (RECUSADO)
python gk_dd_cert_test.py                  # regressão completa (7 testes)
```

**Formato de entrada (resolution):**
```json
{"engine": "resolution",
 "sides": [[[1],[-1]], [[3,4]]],          // Λ₁ (insat), Λ₂ (sat) — disjuntos
 "drat": ["2 0", "0"]}                    // opcional: prova DRAT ASCII
```
Também aceita `"dag"` (passos com justificativas) ou nenhum dos dois →
**provador próprio** (saturação com pais gravados, cap de fecho4000).

**Formato (resk):** `{"engine":"resk","k":2,"lines":[...]}` com regras de
Garlík (`leaf/weaken/cut/and`) — ver `gk_c2_projection_sim.md`.

## 4. Arcabouço matemático

### 4.1 Teorema-base (origem)

> **Teorema 4.3 (P) — `DD_Res ∈ P`** [`C_disjuncao_viavel.md` §4].
> Seja `Λ = Λ₁ ⊎ … ⊎ Λₘ` com `Λᵢ` puro sobre `Xᵢ` (disjuntos) e `π` uma
> refutação de `Λ` por **resolução** (com ou sem enfraquecimento, tree ou
> dag). Em tempo `O(|π|·m)` devolve-se `i*` com `Λ_{i*}` insatisfatível e
> uma **refutação pura de `Λ_{i*}` com ≤ |π| linhas** (FDP com `p(t)=t`).

Depende de: **Lema 4.1 (recorte)** — elimina enfraquecimento definindo
`E_i ⊆ D_i`; **Lema 4.2 (pureza)** — indução: resolvente de linhas puras
compartilhando pivô ⇒ mesmo lado.

### 4.2 Algoritmo E (o que o extrator executa)

Para cada linha em ordem topológica:
- **Folha** `C ∈ Λᵢ`: `E := C`, `w := i`;
- **Enfraquecimento** `D = D′ ∪ F`: `E(D) := E(D′)` (descarta o acrescentado —
  `E ⊆ D′ ⊆ D` ✓; derivação preservada sem nova inferência);
- **Resolução** `D = (D_j∖{l}) ∪ (D_k∖{¬l})` (pivô `l` único):
  - **R1 retenção total** (`l ∈ E_j ∧ ¬l ∈ E_k`): `E := (E_j∖{l}) ∪ (E_k∖{¬l})`
    e `w := w(j) = w(k)` (pivô compartilhado ⇒ mesmo lado — Lema 4.2);
  - **R2** (`l ∉ E_j`): `E := E_j` (⊆ `D` pois `E_j ⊆ D_j∖{l} ⊆ D`);
  - **R3** (`l ∈ E_j ∧ ¬l ∉ E_k`): `E := E_k`.

Invariante: **`E(v) ⊆ λ(v)` e `E(v)` puro sobre `w(v)`** (indução).
Extração: seguir `eparents` até o **primeiro `∅` por corte próprio** (ou
folha `∅`) → lado `i* := w`; acessíveis todos do lado `i*` (por R1+w);
restrição da derivação = refutação pura de `Λ_{i*}`.

### 4.3 Ingestão DRAT → DAG (o ponto delicado)

DRAT ASCII não grava dependências. Extração por **UP com rastreio**:
para cada adição `C`: assumir `¬C`, propagar unidade rastreando as
cláusulas que **disparam** → conflito com conjunto usado `U` ⟹ `U ⊨ C`
(completude da propagação unitária); depois **saturação local em `U`**
(U pequeno) para produzir a derivação **explícita** de `C` a partir de `U`
(uma cadeia de resoluções — cada atribuição unitária vira um corte contra
a cláusula-fonte). Repetindo: a cláusula vazia final é justificada
recursivamente até as folhas. Limitação declarada: cobre adições **RUP**
(Cadical/Glucose ASCII); **RAT** não.

*Correções de engenharia (regressão automatizada):*3 bugs de UP
encontrados nos testes — condição `len(c)−1` (errada em ≥3 literais e
morta em unidades), **sinal invertido** `assign[−l]`, e `ensure` sem
consultar `alive`.

### 4.4 Motor `Res(k)` (regras de Garlík, CCC 2024 §2)

`Axiom x∨¬x` · `∧-intro: A∨l₁, B∨(l₂…lⱼ) ⟹ A∨B∨(l₁…lⱼ)` (j ≤ k) ·
`Weakening: A ⟹ A∨B` · `Cut: A∨(l₁…lⱼ), B∨¬l₁…∨¬lⱼ ⟹ A∨B`.
O motor reusa `gk_c2_projection_sim.py` (invariantes **I1–I5**: `E⊆λ`,
pureza, derivabilidade, **all-or-none de blocos**, extração) e devolve
**violação** (ex.: `G1 VIOLADO: retenção parcial do bloco em <linha>`) —
o detector automático do contraexemplo r2.

### 4.5 Verificador independente (confiança)

Não importa `theorem43_resolution`/`run_projection`. Checagens: folhas ∈
`side_leaves`; por passo — `resolve`: pivô único `l` com
`premissa₁ = resultado∪{l}`, `premissa₂ = resultado∪{¬l}`; `weaken`:
premissa ⊆ conclusão; `cut`/`and`: forma exata ou reuso = pai; largura
`≤ k`; pureza (todo literal ∈ lado); raiz `∅`; aciclicidade;
`n_lines_cert ≤ n_lines_input`. Teste T3: **adulterar a raiz → RECUSADO**.

### 4.6 Cálculo trabalhado

- **D2 (enfraquecimento misto):** `π` com linha `[1,3]` (cruzando lados)
  → certificado **lado0,4 linhas** — o termo estrangeiro3 é descartado
  em `E`.
- **DRAT real (ABC):** prova Cadical `['2 0','0']` → DAG de **8 nós**
  (`{2}`, `∅` justificados) → certificado **6/8 linhas, meta.source=drat**.
- **N3/H-separ:** `n3_hsepar_instance.json` → **lado leal,4/7** ✓
  (regressão do mecanismo de separação da frente N3).

## 5. Validação e limitações

- **Testes (7/7, no CI):** extract saturação · verify roundtrip · extract
  DRAT real · `meta.source=drat` · **adulteração recusada** ·
  **não-disjuntos rejeitados** · demo4 casos;
- **Escopo:** resolução **incondicional** (Teo 4.3) · `Res(k)`
  **condicional** a promessa (violação = saída legítima) · DRAT=RUP ·
  cap de fecho4000 · **nada de claims de complexidade** (o teorema é
  proposicional; p-time/NP≠coNP não estão formalizados).

## 6. Referências

- **Origem:** IA-research-Godel-e-Krajicek — `krajicek_ddp/C_disjuncao_viavel.md`
  (Teorema 4.3, Lemas 4.1/4.2), `krajicek_ddp/C2_r2_G1_contraexemplo.md`
  (contraexemplo G1), `krajicek_ddp/AUDITORIA_EXTERNA_DDRES_G-N.md`
  (dossiê de auditoria).
- Garlík, M. CCC 2024 (regras `Res(k)`) — DOI 10.4230/LIPIcs.CCC.2024.33.
- Krajíček, J. *Proof Complexity*, CUP 2019, cap. 17.7 (algoritmos de
  interpolação viável — contexto).
- Propagação unitária/completude: padrão (Davis–Putnam).

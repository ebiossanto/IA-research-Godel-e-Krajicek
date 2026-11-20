# gk_claims_lint — Sistema imunológico de claims (+ CI)

**Origem:** extensão do repositório
[IA-research-Godel-e-Krajicek](https://github.com/ebiossanto/IA-research-Godel-e-Krajicek)
(MIT) — núcleo: **metodologia Ten-Proofs** do projeto e a sugestão da
**avaliação externa de 11/10/2026 §4.5** (*"testes automáticos que falhem
se README/INDICE disser 'provado' para itens marcados 'rejeitado'"*),
após o incidente real de status obsoleto (Q1).
**Código:** `gk_claims_lint.py` · **CI:** `.github/workflows/ci.yml` ·
**Regra:** rodar antes de todo commit.

## Como citar

> Soares dos Santos, E. (2026). *gk_claims_lint — claims consistency
> checker* [Software]. Em: IA-research-Godel-e-Krajicek.
> <https://github.com/ebiossanto/IA-research-Godel-e-Krajicek>. MIT.

---

## 1. O que é

Verificador de **consistência de afirmações, evidências e marcadores de
honestidade** em todo o repositório (10 regras), mais o **pipeline de CI**
GitHub Actions que o executa a cada push com `lake build` e smoke tests.

## 2. Para que serve (aplicações)

1. **Impedir regressão epistêmica**: um item retraído reaparecendo como
   resultado, um status antigo ("aguardando resposta") sobrevivendo à
   resposta, o disclaimer "não é peer review" sumindo;
2. **Proteger evidências**: SHA-256 dos CSVs divergindo dos JSONs
   (manipulação/quebra de linha);
3. **Documentação viva**: links quebrados, canônicos não indexados;
4. **Como padrão de qualidade** para qualquer repositório de pesquisa
   assistida por IA (transferível).

## 3. Como usar

```bash
python gk_claims_lint.py        # local (≈1s) — exit 0 = OK, 1 = falhas
# CI: automático a cada push (job claims-lint) + lean + smoke
```

**Saída atual:** `*** LINT OK: claims consistentes, evidencias verificaveis ***`
(10/10 regras).

## 4. Arcabouço (as10 regras e o incidente que originou cada uma)

| # | Regra | Origem do incidente |
|---|---|---|
| **R1** | Padrões retraídos (escala exponencial, barreira, T\*) exigem marcador de retração (janela de2 linhas) | Retrações D1–D6 (auditoria 22/09) |
| **R2** | `"aguardando resposta"` só em contexto histórico (cronologia11/10) ou tachado `~~…~~` | **Resposta de Krajíček de12/10** não propagada (incidente real de19/11) |
| **R3** | Disclaimer `"NÃO é peer review"` em README/INDICE/CONTRIBUICOES | Avaliação externa12/10 (P1) |
| **R4** | `DD_Res` sempre com "auditoria externa pendente" | Resultado (P) sem N4 |
| **R5** | Links markdown locais resolvem | Higiene |
| **R6** | `sha256(CSV)` do JSON bate com o CSV (**bytes normalizados CRLF→LF**) | Falha de CI Windows×Linux (20/11) |
| **R7** | `gk_lean_verification.json`: build verde,0 `NOT_FOUND`, Core sem sorry | `gk_lean_bridge` stale (ONDE_ESTAMOS §2.4) |
| **R8** | Tabela DESCARTADOS com D1–D6 no INDICE | Guarda de retrações |
| **R9** | Docs canônicos indexados no INDICE | `ONDE_ESTAMOS` nunca indexado (achado do próprio lint) |
| **R10** | README declara o que **não** está formalizado em Lean | Honestidade de escopo (auditoria) |

### 4.1 Normalização de hash (por que R6 usa bytes normalizados)

CSVs escritos no Windows usam `\r\n`; o git normaliza para `\n` no objeto
e no checkout Linux → `SHA256(raw_local) ≠ SHA256(raw_checkout)`. Solução:
comparar `SHA256(bytes.replace(b"\r\n", b"\n"))` dos **dois** lados —
invariante em qualquer plataforma. Os geradores
(`gk_alternating_family.py`, `gk_proof_fractal.py`, `gk_minref.py`)
gravam já normalizados.

### 4.2 Pipeline CI (`.github/workflows/ci.yml`)

| Job | Conteúdo | Tempo |
|---|---|---|
| `claims-lint` | `python gk_claims_lint.py` | ~5 s |
| `lean` | `lake build` (leanprover/lean-action; toolchain via `lean-toolchain`) | ~20 s |
| `smoke-sim` | `gk_c2_projection_sim --n400` + `gk_dd_cert_test` | ~20 s |

## 5. Validação

O lint **pagou-se na primeira execução**: achou4 falhas reais (status
obsoleto na nota editorial; JSON t2 com CSV errado; `ONDE_ESTAMOS` não
indexado; janela R1) — todas corrigidas; e no primeiro run de CI achou a
divergência CRLF/LF. Regressão: rodar e ver10/10 OK.

## 6. Referências

- **Origem:** IA-research-Godel-e-Krajicek — `CRITICA_EXTERNA_2026-10-11.md`
  §4.5; `ONDE_ESTAMOS_E_PROXIMOS_PASSOS.md` (§2.4 gaps); `CARTA_FINAL_RECEBIDA.md`.
- Metodologia Ten-Proofs: `AGENTS.md` §3 (níveis N0–N4).

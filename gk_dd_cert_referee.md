# Referee Hostile — gk_dd_cert (extrator de certificados DD)

**Data:** 20/11/2026 · **Rodada:** r1 · **Alvo:** `gk_dd_cert.py`,
`gk_dd_cert_test.py`, `gk_dd_cert_demo.json` · **Mandato:** o teorema
`DD_Res ∈ P` (Teorema 4.3) virou executável — auditar correção, escopo e
valor para a auditoria externa.

---

## A. Achados

### A1 (GRAVE) — Correção do caminho DRAT (extração de dependências)
O UP (unit propagation) com rastreio teve **três bugs** encontrados e
corrigidos durante os testes: (i) condição `len(c)-1` errada (não dispara
em unidades; atribui indevidamente em ≥3 literais); (ii) **sinal invertido**
`assign[-l]` (conflitos espurios); (iii) `ensure` não consultava `alive`
(adicao anterior registrada como `None` bloqueava a derivação de ∅).

**Estado:** roundtrip completo **DRAT→DAG→certificado→verificação** OK no
caso ABC (2 adições: `2`,`0` → DAG de8 nós → cert6/8 linhas,
`meta.source=drat`) — T2 do teste automatizado. **Resposta:** os3 bugs têm
regressão automática (T2). Limitação: extração RUP só cobre adicoes
**RUP** (RAT não) — declarado no erro ("nao derivamos vazio... forneça
DAG"). ✅

### A2 — Verificador é realmente INDEPENDENTE?
Não importa `theorem43_resolution`/`run_projection`; re-implementa checagens
(pivô único, conclusão = premissas−pivô,⊆ em enfraquecimento, corte/reuso,
largura ≤k, folhas ∈ side_leaves, pureza, raiz vazia, bound de tamanho,
aciclicidade). Teste T3 **adultera a raiz** → recusado ✓.

**Resposta:** ACEITO com ressalva: o verificador **confiá** na
representação de linhas do certificado (não recheca contra o Λ original
fora das folhas) — para a auditoria, o pacote deve incluir o **input**
(lados) junto; meta do certificado não ancora hash do input (pendência r3:
adicionar `input_sha256`). ✅ com pendência.

### A3 — Motor Res(k): detecção de violação
D4 (contraexemplo r2) → `status=VIOLATION, G1 VIOLADO...` automático ✓;
D3 (puro) → certificado5 linhas verificado ✓. A promessa e a regra de
largura são checadas (`check_soundness_input` + promise do ∧-intro).

**Resposta:** ACEITO — o "detector de contraexemplos do r2" está
**automatizado** conforme o mandato. Pendência r3: o relatório de violação
deveria apontar **todos** os pontos falhos (hoje para no primeiro — o
simulador tem o mesmo comportamento; documentado). ✅

### A4 — Escopo do provador de saturação (motor resolução)
Fecho cap `CLOSURE_CAP=4000`; instâncias grandes → erro orientando a
DAG/DRAT. Teorema 4.3 é **incondicional** para resolução (diferente de
Res(k)) — o certificado não depende de promessa.

**Resposta:** ACEITO — escopo declarado; hipóteses do teorema (lados
disjuntos, folhas puras) **checadas na entrada** (T4) — rejeição limpa. ✅

### A5 — Valor para a auditoria externa
O dossiê `AUDITORIA_EXTERNA_DDRES_G-N.md` §A pede verificação de
recorte/DAG/pureza — o extrator fornece exatamente: certificado da
sub-derivação pura + verificador que o auditor roda sem confiar no
extrator (`python gk_dd_cert.py verify cert.json`, exit0/1).

**Resposta:** ACEITO — **peça entregue**; complementa (não substitui) a
prova escrita do `C_disjuncao` §4. ✅

---

## B. Veredito

**RECOMENDADO (r1)** com pendências r3: (i) `input_sha256` no certificado;
(ii) violação listando todos os pontos; (iii) nota no dossiê da auditoria
apontando esta ferramenta.

**Escopo declarado:** resolução incondicional (Teo 4.3) · Res(k)
condicional a promessa (violação = saída legítima) · DRAT=RUP (RAT não) ·
cap de fecho · sem claims de complexidade.

**Testes:** `python gk_dd_cert_test.py` (7/7) — ligado ao CI (job smoke).

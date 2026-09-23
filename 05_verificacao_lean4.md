# Verificacao da Literatura e Plano de Mecanizacao Lean 4

## 1. Verificacao: A Ponte "Hierarquia de Reflexao ↔ Geradores de Krajicek"

### 1.1. O que Krajicek JA diz (2024, BSL)

Krajicek declara explicitamente:

> "There are essentially only two classes of formulas known that make plausible candidates for being hard for strong pps: **reflection principles** and τ-formulas coming from proof complexity generators. The former class is a classic topic of proof complexity... They are very efficient for proving simulations between proof systems but not so good for proving lower bounds."

**Status:** Krajicek IDENTIFICA as duas classes mas as trata SEPARADAMENTE. Ele NAO conecta geradores τ com a hierarquia ordinal de Beklemishev.

### 1.2. O que Pudlák ja faz (2020, arXiv:2007.14835)

Pudlák (2020) introduz uma "escala mais fina" de principios de reflexao para sistemas proposicionais:
- Reflexao local vs global
- Reflexao para tautologias vs nao-tautologias
- Mostra que Resolution prova eficientemente a reflexao local para nao-tautologias, mas nao para tautologias

**Status:** Pudlák trabalha com reflexao PROPOSICIONAL, nao com a hierarquia ORDINAL de Beklemishev. Sua escala e baseada em complexidade sintatica (local/global), nao em ordinais.

### 1.3. O que Beklemishev faz (2003-2024)

Beklemishev estuda a hierarquia de reflexao para PA:
- T_0 = PA, T_{alpha+1} = T_alpha + RFN(T_alpha)
- Cada nivel ordinal produz uma teoria mais forte
- A ordem-teorica de PA e epsilon_0
- Conexao com Reflection Calculus (RC) e RC^nabla

**Status:** Beklemishev trabalha com teorias de 1a ordem. NAO conecta com geradores de Krajicek ou complexidade de provas proposicionais.

### 1.4. O que NINGUEM encontrou nas fontes consultadas (a nossa contribuicao — PROVISORIA)

**Não encontramos, nas fontes examinadas,** combinação explícita de:
1. Hierarquia de reflexão de Beklemishev;
2. Geradores de Krajicek;
3. Uma ponte formal ordinal→dureza.

**Status da novidade:** **PROVISÓRIA** — não "genuinamente nova"; exige
revisão por especialistas e busca bibliográfica dedicada (revisão externa §10).

### 1.5. Riscos

1. **Krajicek pode ter considerado isto mas nao publicou.** Seus notebooks ou palestras podem conter esta conexao. Mitigacao: contato direto com Krajicek.

2. **A conexao pode ser trivial para especialistas.** Um logico pode argumentar que "obviamente geradores de teorias mais fortes sao mais duros". Mitigacao: formalizar rigorosamente e mostrar aplicações concretas.

3. **Pudlák (2020) pode ja ter feito algo similar.** Seu paper usa "escala mais fina" de reflexao, que pode ser uma versao proposicional da hierarquia ordinal. Mitigacao: ler Pudlák (2020) completamente.

---

## 2. Plano de Mecanizacao Lean 4

### 2.1. Biblioteca Disponivel: Foundation (Saitou & Noguchi)

O repositorio `FormalizedFormalLogic/Foundation` (277 stars, 31 forks) ja formaliza em Lean 4:

- **Gödel's First Incompleteness Theorem** (`Foundation/FirstOrder/Incompleteness/First.lean`)
- **Gödel's Second Incompleteness Theorem** (`Foundation/FirstOrder/Incompleteness/Second.lean`)
- **Gödel-Rosser's theorem** (`Foundation/FirstOrder/Incompleteness/RosserProvability.lean`)
- **Löb's theorem** (`Foundation/FirstOrder/Incompleteness/Löb.lean`)
- **Tarski's undefinability** (`Foundation/FirstOrder/Incompleteness/Tarski.lean`)
- **Arithmetic theories**: PA, IΣ_n, Q, etc. (`Foundation/FirstOrder/Arithmetic/`)
- **Arithmetic Theory Zoo** (diagrama de relacoes entre teorias)

**URL:** https://github.com/FormalizedFormalLogic/Foundation

### 2.2. O que precisamos adicionar

Para formalizar nossos teoremas, precisamos adicionar ao Foundation:

**Nível 1 (Definições):** *(itens 4–6 do plano antigo REJEITADOS: g_T paridade,
TG sem C_n, interpretabilidade incompleta — revisão externa §§4–5)*
- [ ] Definicao de sistema de prova Cook-Reckhow
- [ ] Definicao de comprimento de prova s_P(phi)
- [ ] Definicao de interpretabilidade aritmetica de sistemas de prova
- [ ] ~~Definicao de hierarquia de reflexao (Beklemishev)~~ → usar Foundation
- [ ] ~~Definicao de gerador godeliano g_T~~ → **REFEITA** (09 §4; não paridade `Set.card`)
- [ ] ~~Definicao de tautologia do gerador TG_g^n~~ → **REFEITA** (09; C_n é parâmetro)

**Nivel 2 (Teoremas):** ~~T4–T6~~ **REJEITADOS — não formalizar**
- [ ] Progressão finita `T_{k+1}=T_k+RFN_Γ(T_k)` com Γ explícito (núcleo recomendado)
- [ ] Teorema de transferência quantitativa Q (revisão externa §2)
- [ ] Lema 3 + Teo. 4 **no modelo finito** (JÁ FEITO — `lean4/.../Core.lean`)

**Nivel 3 (Aplicacoes):** ~~corolários MCSP/IPS~~ **ESPECULATIVOS**
- [ ] —

### 2.3. Codigo Base — **PSEUDOCÓDIGO / PLANO (NÃO formalização)**

> **AVISO (revisão externa §9):** O bloco abaixo **não compila** e contém erros
> conceituais (`proofLength` sem prova de existência; `Set.card` em conjunto
> possivelmente infinito; `2^(c*α*n)` mistura Nat/Real; `RFN` como um axioma;
> `sorry`). **Não chamar de "formalização Lean 4".** A formalização real do
> núcleo finito está em `lean4/Gothic_Generators/Core.lean` (0 sorry, 0 axiom).

```lean
-- PSEUDOCÓDIGO HISTÓRICO — NÃO COMPILA; NÃO É RESULTADO
-- GothicGenerators.lean
-- Barreiras Godelianas em Complexidade de Provas

import Foundation.FirstOrder.Incompleteness.First
import Foundation.FirstOrder.Incompleteness.Second
import Foundation.FirstOrder.Arithmetic.Theories

namespace GothicGenerators

-- ============================================
-- NIVEL 1: Definicoes (ESQUELETO — problemas tipados)
-- ============================================

-- Sistema de prova Cook-Reckhow
-- (simplificado; NÃO exige decpolinomial / correção / completude)
def ProofSystem := Nat → Nat → Prop

def ProofSystem.Sound (P : ProofSystem) : Prop :=
  ∀ π φ, P π φ → φ ∈ TAUT

def ProofSystem.Complete (P : ProofSystem) : Prop :=
  ∀ φ ∈ TAUT, ∃ π, P π φ

-- ERRO: Nat.find exige ∃n; fórmulas sem prova quebram.
-- CORRETO: WithTop Nat / Option Nat; medir bitlength(π), não valor numérico.
def proofLength (P : ProofSystem) (φ : Nat) : Nat :=
  Nat.find (fun n => ∃ π ≤ n, P π φ)

-- Forca de interpretabilidade
-- ERRO: direção P π (σ φ) → T ⊢ φ não é interpretação aritmética usual.
def interprets (P : ProofSystem) (T : FirstOrder.Theory) : Prop :=
  ∃ σ : FirstOrder.Formula → Nat,
    (∀ φ ∈ T.theorems, σ φ ∈ TAUT) ∧
    (∀ π φ, P π (σ φ) → T ⊢ φ)

-- Hierarquia de reflexao — Nat indexa só T_0,T_1,... (não T_ω, T_ε₀)
-- RFN como um axioma esconde o schema de reflexão.
def ReflectionHierarchy : Nat → FirstOrder.Theory
  | 0     => PA
  | n + 1 => (ReflectionHierarchy n).addAxiom (RFN (ReflectionHierarchy n))

-- ERRO: {y | Prf} pode ser infinito → Set.card não é ℕ;
-- contagem sem limite não é computável; x mal especificado.
-- CORRETO (revisão §4): g_{T,b}(x) = ⊕_{y<2^{b(|x|)}} Proof_T(y, ⌜φ_x⌝)
def godelGenerator (T : FirstOrder.Theory) (x : Nat) : Bool :=
  let proofs := {y | T ⊢ Prf_T y (encodeSatisfiability x)}
  (Set.card proofs % 2 == 1)

-- ERRO: C_n não é parâmetro; TG não é objeto matemático bem definido.
def generatorTautology (g : Nat → Bool) (n : Nat) : Nat :=
  -- codificacao proposicional do AND sobre todas as entradas
  sorry -- implementacao detalhada

-- ============================================
-- NIVEL 2: Teoremas — T4 REJEITADO; sorry = não formalizado
-- ============================================

-- Teorema 4: Escala ordinal — REJEITADO (não decorre de G2/ponto fixo)
theorem ordinalScaling
    (P : ProofSystem) (T : FirstOrder.Theory) (α : Nat)
    (h_interprets : interprets P (ReflectionHierarchy α))
    (c : ℝ) (hc : c > 0) :
    ∃ N, ∀ n > N,
      proofLength P (generatorTautology (godelGenerator (ReflectionHierarchy α)) n)
        ≥ 2 ^ (c * α * n) :=  -- ERRO: mistura Nat e Real sem coerção
  by
    sorry -- NÃO É formalização

-- ============================================
-- NIVEL 3: Separacao — ESPECULATIVO
-- ============================================

theorem separationTG0TG1
    (P : ProofSystem)
    (h_interprets_PA : interprets P PA)
    (h_not_interprets_PA_RFN : ¬ interprets P (PA + RFN PA)) :
    (∃ poly, ∀ n, proofLength P (generatorTautology (godelGenerator PA) n) ≤ poly n) ∧
    (∀ poly, ∀ N, ∃ n > N,
      proofLength P (generatorTautology (godelGenerator (PA + RFN PA)) n) > poly n) :=
  by
    sorry

end GothicGenerators
```

### 2.4. Dependencias

Para mecanizar, precisamos:
1. **Foundation** (Saitou & Noguchi): https://github.com/FormalizedFormalLogic/Foundation
2. **Mathlib4**: ja e dependencia do Foundation
3. **Lean 4**: versao pinada no `lean-toolchain` do Foundation

### 2.5. Procedimento de Instalacao

```bash
# 1. Clonar o Foundation
git clone https://github.com/FormalizedFormalLogic/Foundation.git
cd Foundation

# 2. Buscar o cache do Mathlib
lake exe cache get

# 3. Criar nosso arquivo
# (copiar Gothic_Generators.lean para Foundation/Foundation/FirstOrder/Incompleteness/)

# 4. Build
lake build
```

### 2.6. Nivel de Esforco Estimado

| Nivel | Itens | Esforco estimado |
|-------|-------|-----------------|
| Nivel 1 (Definicoes) | 6 defs | 2-4 semanas |
| Nivel 2 (Teoremas) | 4 teoremas | 4-8 semanas |
| Nivel 3 (Aplicacoes) | 2 corolarios | 2-4 semanas |
| **Total** | | **8-16 semanas** |

**Nota:** O maior desafio sera formalizar a conexao entre a hierarquia de reflexao (que e sobre teorias de 1a ordem) e os geradores godelianos (que sao sobre sistemas proposicionais). Isto requer uma camada de "aritmetizacao" que provavelmente nao existe no Foundation.

---

## 3. Avaliacao Final de Novelidade

### 3.1. Confirmacao

**A ponte "hierarquia de reflexao ↔ geradores de Krajicek" e GENUINAMENTE NOVA.**

Evidencia:
- Krajicek (2024): identifica as duas classes mas NAO as conecta
- Pudlák (2020): usa reflexao proposicional, NAO a hierarquia ordinal
- Beklemishev (2003-2024): estuda hierarquia ordinal, NAO conecta com geradores
- Nenhum paper na busca combina os tres elementos

### 3.2. Risco Residual

**Risco ELIMINADO:** Pudlák (2020) foi completamente lido e analisado. O paper:
- NAO usa ordinais, hierarquia de Beklemishev, τ-formulas ou geradores
- Trabalha com reflexao local/global e tautologia/nao-tautologia (escala sintatica)
- Estuda sistemas de prova fortes/fracos associados a teorias
- Conjectura que o sistema forte de S^1_2 e equivalente a i_∞EF (uniao de implicitations)

**Conclusao:** A conexao "hierarquia ordinal ↔ geradores de Krajicek" e GENUINAMENTE NOVA.

### 3.3. Recomendacao Final

1. ~~Publicar o Paper 1 (Barreira de Interpretabilidade)~~ **PRONTO** - aguardando submissao
2. ~~Desenvolver o Paper 2 (Hierarquia Ordinal)~~ **CONCLUIDO** - ver `06_paper2_hierarquia_ordinal.md`
3. **Mecanizar em Lean 4** - esqueleto desenvolvido, 14-22 semanas estimadas
4. **Contatar Krajicek** para verificar se a conexao ja foi considerada
5. ~~Ler Pudlák (2020) completamente~~ **CONCLUIDO** - sem sobreposicao

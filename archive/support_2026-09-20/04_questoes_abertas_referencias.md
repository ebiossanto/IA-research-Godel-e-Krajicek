# Questoes Abertas, Programa de Pesquisa e Referencias

## 12. Questoes Abertas e Programa de Pesquisa

### 12.1. Questoes Abertas Imediatas (respondiveis em 1-2 anos)

**Q1. Tightness do Teorema 4.** O limite inferior 2^{c * |T_alpha| * n} e otimo? Existe um sistema P e um gerador g_alpha onde s_P(TG_alpha^n) = Theta(2^{c * |T_alpha| * n})?

**Q2. Aritmetizacao algebrica.** O gerador g_0 (nivel PA) pode ser aritmetizado em IPS? Se sim, qual e o limite inferior resultante?

**Q3. Mecanizacao.** Os Teoremas 4, 5, 6 podem ser mecanizados em Lean 4 (usando o trabalho de Saitou & Noguchi 2026)?

**Q4. Separacao concreta.** Podemos usar TG_0 e TG_1 para separar Cutting Planes de Frege usando APENAS argumentos de incompletude?

### 12.2. Questoes Abertas de Medio Prazo (2-5 anos)

**Q5. Conjectura de Krajicek via geradores godelianos.** O gerador g^* (nivel maximo) e hard para todos os sistemas? Isto e equivalente a conjectura de Krajicek (2004).

**Q6. Hierarquia continua.** A hierarquia {C(alpha)} (cortes no espaco de sistemas de prova) e isomorfa a hierarquia de ordinais recursivos? Ou existem "saltos"?

**Q7. Conexao com MCSP.** A redutibilidade MCSP -> geradores godelianos (Teorema 7) pode ser invertida? Isto conectaria incompletude com meta-complexidade de forma bidirecional.

**Q8. Limites para IPS.** O Teorema 8 (limite inferior condicional para IPS) pode ser demonstrado sem condicionalidade?

### 12.3. Questoes Abertas de Longo Prazo (5+ anos)

**Q9. Classificacao completa.** A funcao g(P) (complexidade godeliana) pode ser computada exatamente para sistemas de prova concretos?

**Q10. Unificacao.** Todos os limites inferiores em complexidade de provas sao, em ultima analise, de natureza godeliana? (Conjectura do Paper 1, Secao 6.2)

**Q11. Fronteira com fisica.** A hierarquia ordinal de geradores godelianos se conecta com hierarquias em fisica teorica (ex: hierarquias de teorias de campo)?

### 12.4. Programa de Pesquisa Estruturado

**Fase 1 (Ano 1): Fundamentos**
- Publicar o Paper 1 (Barreira de Interpretabilidade) com refinamento
- Mecanizar o Teorema 4 em Lean 4
- Explorar separacao concreta (Q4)

**Fase 2 (Ano 2): Geradores**
- Publicar o Paper 2 (Hierarquia Ordinal de Geradores)
- Investigar aritmetizacao algebrica (Q2)
- Conectar com trabalho de Krajicek (Q5)

**Fase 3 (Ano 3): Meta-Complexidade**
- Publicar o Paper 3 (Conexao MCSP <-> Geradores Godelianos)
- Investigar limites para IPS (Q8)
- Conectar com framework de Monroe (2026)

**Fase 4 (Anos 4-5): Unificacao**
- Investigar a Conjectura 10 (toda dureza e godeliana)
- Explorar conexoes com analise ordinal avancada
- Buscar aplicações em verificacao formal

---

## 13. Referencias Completas

### Referencias Classicas

[1] Gödel, K. (1931). "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I." Monatshefte für Mathematik und Physik, 38:173-198.

[2] Cook, S.A. and Reckhow, R.A. (1979). "The relative efficiency of propositional proof systems." JSL, 44(1):29-50.

[3] Turing, A.M. (1936). "On computable numbers, with an application to the Entscheidungsproblem." Proc. London Math. Soc., 42:230-265.

[4] Chaitin, G.J. (1966). "On the length of programs for computing finite binary sequences." JACM, 13(4):547-569.

### Referencias em Complexidade de Provas

[5] Krajíček, J. (1995). "Bounded Arithmetic, Propositional Logic, and Complexity Theory." Cambridge University Press.

[6] Krajíček, J. (2001). "Tautologies from pseudo-random generators." Bull. Symbolic Logic, 7(2):197-212.

[7] Krajíček, J. (2004). "Diagonalization in proof complexity." Fundamenta Mathematicae, 182:181-192.

[8] Krajíček, J. (2019). "Proof Complexity." Cambridge University Press.

[9] Krajíček, J. (2022/2023). "On the existence of strong proof complexity generators." arXiv:2208.11642.

[10] Krajíček, J. (2024). "Proof complexity generators." London Math. Soc. Lecture Note Series, no. 497.

[11] Krajíček, J. (2025). "A proof complexity conjecture and the incompleteness theorem." JSL, 90(3).

[12] Krajíček, J. (2025). "On NP ∩ coNP proof complexity generators." arXiv:2506.20221.

[13] Pudlák, P. (1997). "Lower bounds for resolution and cutting plane proofs and monotone computations." JSL, 62(3):981-998.

[14] Pudlák, P. (1998). "The lengths of proofs." In Handbook of Proof Theory, S.R. Buss ed., Elsevier, pp.547-637.

### Referencias em Principios de Reflexao e Analise Ordinal

[15] Beklemishev, L.D. (2003). "Proof-theoretic analysis by iterated reflection." Archive for Mathematical Logic, 42:515-532.

[16] Beklemishev, L.D. (2005). "Reflection principles and provability algebras in formal arithmetic." Russian Math. Surveys, 60:197-270.

[17] Beklemishev, L.D. (2010). "Gödel incompleteness theorems and the limits of their applicability. I." Russian Math. Surveys, 65:857-898.

[18] Beklemishev, L.D. (2024). "Reflection principles, algebras and progressions of theories." (Lecture notes)

[19] Walsh, J. (2022). "Characterizations of ordinal analysis." arXiv:2209.09765.

[20] Arai, T. (2020). "Ordinal Analysis with an Introduction to Proof Theory." Springer.

### Referencias em Meta-Complexidade

[21] Monroe, H. (2026). "Hardness as an Information Constraint: A Unifying Meta-Complexity Assumption." arXiv:2606.04257.

[22] Santhanam, R. (2025). "Meta-Complexity: A Brief Survey." CCR 2025.

[23] Oliveira, I.C. (2025). "Meta-Mathematics of Computational Complexity Theory." SIGACT News, Complexity Theory Column 124. arXiv:2504.04416.

[24] Hirahara, S. (2020). "Meta-Complexity Theoretic Approach to Complexity Theory." (Talk slides)

### Referencias em Sistemas Algebricos

[25] Grochow, J.A. and Pitassi, T. (2018). "The Ideal Proof System." J. ACM, 65(6):1-53.

[26] Hakoniemi, T., Limaye, N., and Tzameret, I. (2024). "Functional Lower Bounds in Algebraic Proofs: Symmetry, Lifting, and Barriers." STOC 2024.

[27] Elbaz, T., Govindasamy, N., Lu, J., and Tzameret, I. (2025). "Lower Bounds against the Ideal Proof System in Finite Fields." arXiv:2506.20221 (ECCC TR25-080).

[28] Forbes, M. (2024). "New Bounds for the Ideal Proof System in Positive Characteristic." CCC 2024.

### Referencias Recentes (2026)

[29] Saitou, S. and Noguchi, M. (2026). "Mechanizing Gödel's Incompleteness Theorems and Provability Logic." arXiv:2609.13780.

[30] Fang, W. et al. (2026). "Self-Referential K-SAT and the Finite Analogue of Gödel's Incompleteness Theorem." arXiv:2607.01671.

[31] arXiv:2604.07406 (2026). "On Formally Undecidable Propositions of Nondeterministic Complexity and Related Classes."

[32] Baaz, M. et al. (2025). "90 Years of Gödel's Incompleteness Theorems." J. Logic and Computation.

[33] Lu, J., Santhanam, R., and Tzameret, I. (2025). "p-Frege Cannot Efficiently Prove that Constant-Depth Algebraic Circuit Lower Bounds are Hard." ECCC TR25-134.

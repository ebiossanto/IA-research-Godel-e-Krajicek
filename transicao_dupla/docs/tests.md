# Testes e Provas

## Testes Unitários

Cada módulo de software deve ter testes unitários que cobram:
- Entradas válidas e inválidas.
- Comportamento consistente com a formalização matemática (definida em `docs/formalization.md`).
- Cobertura mínima de 80% de código.

## Provas Matemáticas

- Cada teorema do `docs/formalization.md` deve ter uma prova formal ou esboço de demonstração incluído nos testes de regressão.
- Utilizar frameworks de verificação formal (como Coq, Lean, ou Z3) para automação de provas, se aplicável.

## Exemplos de Testes

```python
def test_transition_double():
    """Testa a propriedade T^2 = T ∘ T"""
    from math_module import transition_double
    T = lambda x: (x + 1) % 10
    result = transition_double(T)(5)
    expected = T(T(5))
    assert result == expected
```
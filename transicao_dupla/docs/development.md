# Documento de Desenvolvimento

## Visão Geral

Este documento descreve o design, a arquitetura e as decisões de implementação do sistema.

### Arquitetura

- **Camada de Acesso Dados**: Responsável por operações de leitura/escrita no banco de dados. Utiliza padrão Repository.
- **Camada de Serviço**: Contém a lógica de negócio, integrando a formalização matemática (via serviços de cálculo).
- **Camada de API**: Exposição de endpoints REST/GraphQL para consumo por clientes.
- **Interfície Usuário**: Front-end em React/Angular (ou definição de terminal, conforme o produto).

### Integração Matemática

- Os resultados do `docs/formalization.md` são consumidos por serviços de cálculo especializados (`math-service`).
- Cada teorema é encapsulado em uma função pura com testes unitários.

### Plano de Implementação

1. **Sprint 1**: Modelagem de domínio e definição das estruturas de dados.
2. **Sprint 2**: Implementação da camada de serviço com integração matemática.
3. **Sprint 3**: Desenvolvimento da API e testes de integração.
4. **Sprint 4**: UI básica e correção de bugs.
5. **Sprint 5**: Preparação de certificados e documento de continuidade.

### Tecnologias

- Linguagem: Python 3.11 / TypeScript 5
- Framework: FastAPI (Python) ou NestJS (TypeScript)
- Banco de Dados: PostgreSQL
- Testes: Pytest / Jest
- CI/CD: GitHub Actions

## Próximos Passos

- Criar repositório de código (já está em processo).
- Definir schema do banco de dados.
- Implementar primeiro conjunto de teoremos como serviços.
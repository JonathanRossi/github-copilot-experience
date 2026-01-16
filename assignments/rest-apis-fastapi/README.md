# 📘 Assignment: Construindo APIs REST com Framework FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a construir APIs REST modernas utilizando o FastAPI, um framework Python rápido e fácil de usar. Você criará endpoints HTTP, aprenderá sobre verbos HTTP (GET, POST, PUT, DELETE), validação de dados e documentação automática de APIs.

## 📝 Tasks

### 🛠️ Tarefa 1: Criar uma API Básica de Tarefas

#### Description
Crie uma API REST simples para gerenciar uma lista de tarefas (todo list). A API deve permitir criar, ler, atualizar e deletar tarefas. Você trabalhará com dados em memória (sem banco de dados) para esta primeira tarefa.

#### Requirements
Completed program should:

- Implementar um endpoint GET `/tasks` que retorna todas as tarefas
- Implementar um endpoint POST `/tasks` que cria uma nova tarefa
- Implementar um endpoint GET `/tasks/{id}` que retorna uma tarefa específica
- Implementar um endpoint PUT `/tasks/{id}` que atualiza uma tarefa existente
- Implementar um endpoint DELETE `/tasks/{id}` que deleta uma tarefa
- Usar modelos Pydantic para validação de dados de entrada
- Retornar códigos de status HTTP apropriados (200, 201, 404, etc.)


### 🛠️ Tarefa 2: Adicionar Validação e Tratamento de Erros

#### Description
Expanda a API anterior adicionando validação robusta de dados de entrada, tratamento de erros apropriado e melhorias na estrutura. Implemente validações em tempo de requisição e respostas de erro claras.

#### Requirements
Completed program should:

- Usar validação Pydantic com campos obrigatórios e opcionais
- Adicionar validação de comprimento mínimo/máximo para campos de texto
- Implementar tratamento de exceções para casos como tarefa não encontrada
- Retornar mensagens de erro descritivas em formato JSON
- Adicionar timestamps de criação e atualização para cada tarefa
- Usar tipos de dados apropriados (str, int, bool, datetime, etc.)


### 🛠️ Tarefa 3: Expandir com Funcionalidades Avançadas

#### Description
Implemente funcionalidades mais avançadas na sua API, como filtragem, busca e status de tarefas. Adicione também documentação interativa e testes básicos.

#### Requirements
Completed program should:

- Adicionar filtro por status de conclusão (concluída/pendente)
- Implementar busca por palavra-chave no título ou descrição da tarefa
- Adicionar campo de status (pendente, em progresso, concluída)
- Usar a documentação automática do FastAPI (Swagger UI no `/docs`)
- Implementar testes usando `pytest` para pelos menos 3 endpoints
- Adicionar logging básico das requisições da API

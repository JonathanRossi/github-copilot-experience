# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados

- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

- **Conventional Commits**: Use o padrão de commits convencionais para manter um histórico claro e organizado:
  - `feat:` para novas funcionalidades
  - `fix:` para correções de bugs
  - `docs:` para documentação
  - `style:` para formatação (sem mudanças de lógica)
  - `refactor:` para refatoração de código
  - `test:` para testes
  - Exemplos: `feat: add assignment filtering by due date`, `fix: correct responsive header layout`, `docs: update setup instructions`
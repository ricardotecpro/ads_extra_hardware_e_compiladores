# Roadmap do Projeto: Hardware para Programadores

Este documento rastreia o progresso da refatoração e desenvolvimento do curso de Hardware voltado a C/C++ e arquitetura.

## ✅ Fase 1: Estruturação e Setup
- [x] Atualização de configurações (`pyproject.toml` e `mkdocs.yml`).
- [x] Limpeza de arquivos de log.
- [x] Adição do novo tema (Light/Dark mode) com `accent: amber`.
- [x] Correção do versionamento nativo Mermaid para `11.12.3` (evitando erro SyntaxError in text).

## 🚧 Fase 2: Correção de Componentes UI e Scripts (Em andamento)
- [ ] Conversor Automático de Fragmentos (SlideReveal): Atualização da transição no script.
- [ ] Retificar layout de Quizzes (interface circlar CSS para radio buttons e isolamento dos feedbacks).
- [ ] Termynal.js: Inserir atributos Markdown para correta compilação e parsing interno.

## 🚧 Fase 3: Conteúdo e Refatoração Intelectual (Em andamento)
- [ ] **Aulas (01 a 16)**: Re-desenho e fundamentação C/C++ da ementa (Processos, Diagramas de Memória).
- [ ] **Exercícios (16 listas)**: 5 exercícios progressivos.
- [ ] **Projetos (16 desafios)**: Profiling, medições de Cache, Multithreading Mutex.
- [ ] **Quizzes (16 questionários)**: 10 perguntas estritas focados na dinâmica de CPU e SO.

## 🚀 Fase 4: Automação e Validação Final
- [ ] Build de Validação Rigorosa: `mkdocs build --strict`.
- [ ] Validar compatibilidade dos scripts transicionais em localhost (`mkdocs serve`).
- [ ] Deploy Final Estável no repositório GitHub (`branch gh-pages`).
- [ ] Remoção de artefatos obsoletos e garantia do "estado da arte".

---
**Status Atual**: Fase 1 Finalizada / Fase 2 em Andamento.
**Última Atualização**: Fevereiro/2026

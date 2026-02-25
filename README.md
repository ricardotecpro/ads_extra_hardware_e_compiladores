# 💻 Hardware para Programadores - Curso

Curso de Hardware com ênfase em C/C++, abordando desde a arquitetura de computadores até a otimização de performance e concorrência no baixo nível.

## 🎯 Sobre o Curso

Este curso oferece uma base sólida para engenheiros de software que desejam dominar o funcionamento interno do computador. Através de uma abordagem prática, orientada a C/C++ e ferramentas modernas, os alunos aprendem o verdadeiro impacto do hardware no código.

### ✨ Destaques

- ✅ **16 Aulas Completas** - Do ciclo de instrução à otimização de memória.
- ✅ **Slides Modernos** - Apresentações Reveal.js interativas.
- ✅ **Quizzes Interativos** - Validação de conhecimento em tempo real.
- ✅ **Exercícios Práticos** - Codificação C/C++ (Ponteiros, Threads, Cache).
- ✅ **Projetos de Baixo Nível** - Aplicação prática e Profiling.
- ✅ **Design Premium** - Interface moderna com MkDocs Material.

## 🚀 Começando

### Pré-requisitos

- **Python 3.11+**
- **Poetry** (Gerenciador de dependências)

### Instalação

```bash
# Clonar repositório
git clone https://github.com/ricardotecpro/ads_extra_hardware_e_compiladores.git
cd ads_extra_hardware_e_compiladores

# Instalar dependências e ambiente
poetry install
```

## 📚 Comandos Disponíveis

O projeto utiliza **Taskipy** para atalhos de comandos comuns:

```bash
# Iniciar servidor local (MkDocs)
poetry run task docs

# Regenerar slides (Reveal.js)
poetry run task slides

# Converter/Regenerar quizzes
poetry run task quizzes

# Executar testes de integridade
poetry run task test

# Build do site estático
poetry run task build
```

## 📁 Estrutura do Projeto

```
ads_extra_hardware_e_compiladores/
├── docs/                      # Documentação e Conteúdo
│   ├── assets/                # Imagens, CSS, JS customizados
│   ├── aulas/                 # Conteúdo das 16 aulas
│   ├── exercicios/            # Listas de exercícios (C/C++)
│   ├── projetos/              # Projetos práticos
│   ├── quizzes/               # Quizzes interativos (.src e .md)
│   ├── slides/                # Slides Reveal.js (.src, .md e .html)
│   ├── setups/                # Guias de configuração de ambiente
│   └── index.md               # Homepage do site
├── scripts/                   # Scripts de automação (Python)
├── hooks/                     # Hooks customizados para MkDocs
├── pyproject.toml            # Configuração do Poetry e Tasks
└── mkdocs.yml                # Configuração principal do MkDocs
```

## 🎨 Tecnologias

- **MkDocs Material** - Documentação moderna e responsiva.
- **Reveal.js** - Slides baseados em web.
- **MathJax** - Renderização de fórmulas matemáticas.
- **Mermaid.js** - Diagramas e fluxogramas via código.
- **Termynal.js** - Simulação de terminal interativo.

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, siga o fluxo de Pull Request padrão do GitHub.

## 📝 Licença

Este projeto está sob a licença [MIT](LICENSE).

## 👤 Autor

**Ricardo Tec Pro**

- GitHub: [@ricardotecpro](https://github.com/ricardotecpro)
- LinkedIn: [ricardotecpro](https://linkedin.com/in/ricardotecpro)
- Portfólio: [ricardotecpro.github.io](https://ricardotecpro.github.io/)

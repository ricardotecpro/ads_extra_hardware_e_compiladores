# 🛠️ Plano de Refatoração e Padronização Universal de Cursos (MkDocs)

Este documento serve como um **Master Prompt** ou **Checklist de Auditoria** para ser utilizado em outros repositórios de cursos. O objetivo é replicar a exata consistência arquitetural, geração de scripts e resiliência de build rigoroso (`mkdocs build --strict`) que foi alcançada com sucesso no curso molde.

Ao aplicar este plano/prompt em uma nova IA ou em um novo repositório, basta substituir a variável `[TEMA DO CURSO]` pela tecnologia base (ex: *Java Spring Boot*, *React*, *Banco de Dados*).

---

## 📋 Como usar este documento como "Prompt" para uma IA:

Copie o texto abaixo e envie para o agente/assistente que estiver trabalhando no novo repositório:

> **PROMPT DE INICIALIZAÇÃO:**
> "Atue como um Engenheiro de Software Educacional Sênior focado na framework MkDocs. Estamos refatorando um curso sobre `[TEMA DO CURSO]`. Minha diretriz estrita é seguir o plano de padronização universal abaixo. Quero que você avalie o repositório atual e execute iterativamente cada uma dessas Fases de Refatoração, recriando os scripts em Python citados e adequando-os ao conteúdo deste repósitório. Trabalhe em etapas e vá me reportando."

---

## 🏆 Checklist de Refatoração (O Plano Universal)

### Fase 1: Diagnóstico de Configuração e Strict Build
- [ ] Inspecionar o arquivo `mkdocs.yml`.
- [ ] Confirmar se o tema é o clássico `material`, carregando os plugins de praxe (`search`, `git-authors`, `git-revision-date-localized`).
- [ ] Adicionar o plugin `awesome-pages` à lista do `mkdocs.yml` (isso evita falsos erros em páginas geradas automaticamente que não estão listadas explicitamente no nav).
- [ ] Rodar `mkdocs build --strict` para registrar a quantidade de quebras de links e macro-loops atuais.

### Fase 2: Sincronização e Geração Profunda de Materiais (`scripts/rebuild_all_materials.py`)
- [ ] O repositório deve ter a lógica de ensino primário estritamente dentro de `docs/aulas/aula-XX.md`.
- [ ] Criar/Adaptar um script Python (ex: `rebuild_all_materials.py`) que:
    1. Leia todas as `docs/aulas/aula-XX.md`.
    2. Extraia os títulos secundários (`##`) e o **parágrafo explicativo em texto puro** subsequente a eles.
    3. Escreva `docs/exercicios/exercicio-XX.md` criando perguntas abertas baseadas no contexto de cada tópico.
    4. Crie no rodapé de CADA exercício um botão do tipo: `[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-XX.md){ .md-button .md-button--primary }`.
    5. Escreva `docs/exercicios/solucao-XX.md` transcrevendo o contexto da aula como a resposta teoricamente embasada e com o botão de voltar.
    6. Escreva os `docs/projetos/projeto-XX.md` orientando implementações atreladas à tecnologia `[TEMA DO CURSO]` embasadas diretamente nos tópicos da aula.
    7. Escreva os `docs/quizzes/src/quiz-XX.md` como perguntas de múltipla-escolha que utilizem o texto original da aula tanto na resposta correta (A) quanto no campo de `*feedback:*` de acerto.
- [ ] Executar o script `convert_quizzes.py` após a geração do texto.

### Fase 3: Padronização da Árvore de Índices (Navagation)
- [ ] Existem múltiplos arquivos `index.md` perdidos no repositório (`docs/index.md`, `aulas/index.md`, `projetos/index.md`, etc) que comumente contêm grades curriculares (módulos) desatualizadas, copiadas de projetos anteriores.
- [ ] Criar/Adaptar um script Python (ex: `rewrite_indices.py`) que:
    1. Agrupe as aulas em _arrays_ definindo exatamente os Títulos e Módulos corretos perante os tópicos de `[TEMA DO CURSO]`.
    2. Reescreva integralmente TODOS os `index.md` do repositório programaticamente, injetando links nativos apontando para seus laboratórios, exercícios, quizzes e rotas `aula-XX.md`.

### Fase 4: Especialização do Ambiente (Setups)
- [ ] Revisar os manuais interativos de Instalação (`docs/setups/setup-01.md` e `setup-02.md`).
- [ ] Remover tutoriais descontextualizados (como pedir para instalar Python num curso de React, ou pedir NodeJS num curso de C).
- [ ] Reescrever `setup-01.md` para **Windows** focando nas dependências cruciais de `[TEMA DO CURSO]`.
- [ ] Reescrever `setup-02.md` para **Linux** (`apt`, `snap`) focando nas mesmas dependências rigorosas de `[TEMA DO CURSO]`.

### Fase 5: Integração de Slides
- [ ] Garantir que exista um script pipeline ou diretório revisor (como _revisao/slides-XX.md) que transpila via Markdown (Marp/Reveal) para a pasta `docs/slides/`.
- [ ] Slides não devem conter conteúdo genérico ("Tópico 1..."). Caso identifique boilerplate, mapear de onde os slides originais estão vindo (se de repositórios base ou se gerados pela própria aula) e copiá-los para `docs/slides/src/`.

### Fase 6: Git Assurance e Entrega (CI/CD)
- [ ] Todos os novos materiais gerados (Exercícios, Soluções, Projetos, Quizzes processados) devem ser salvos via commit no Git antes do run oficial, usando:
`git add docs/ && git commit -m "docs: geracao automatica de artefatos educacionais do curso"`
(Se isto não for feito, os plugins arquiteturais que exigem metadados de tempo de último acesso reprovarão a build estrita).
- [ ] Rodar localmente o comando `mkdocs build --strict`. O esperado é a saída final `Exit code: 0`. Tendo êxito, o site possui consistência modular profunda.

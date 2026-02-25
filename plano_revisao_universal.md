# 🛠️ Plano de Refatoração e Padronização Universal de Cursos (MkDocs)

Este documento atua como o **Master Prompt** ou **Plano de Revisão Completa com Tasks** para a refatoração e otimização dos repositórios de cursos `[NOME_DO_CURSO]`. O objetivo é replicar a exata consistência arquitetural, experiência de usuário (UX) premium, qualidade de conteúdo e resiliência de build rigoroso (`mkdocs build --strict`) através de todos os projetos educacionais.

A refatoração não deve alterar o núcleo pedagógico base aprovado, mas expandir sua profundidade para nível intermediário mantendo a progressão cognitiva, melhorando estruturalmente e tecnicamente como os materiais são apresentados.

---

## 📋 Como usar este documento como "Prompt" para uma IA:

Copie o texto inteiro e envie para o agente/assistente:

> **PROMPT DE INICIALIZAÇÃO:**
> "Atue como um Engenheiro de Software Educacional Sênior focado na framework MkDocs. Estamos refatorando o repositório de um curso específico. Minha diretriz estrita é seguir o plano de padronização universal detalhado abaixo. Trabalhe iterativamente através das fases propostas executando as tarefas. O foco é manter a máxima qualidade didática, UX premium nativa MkDocs, coesão nos índices e rigor técnico nos scripts e validações da CI/CD."

---

## 🧭 1. DIRETRIZES GERAIS (OBRIGATÓRIAS)

### 🇧🇷 Idioma
Todo o conteúdo sem exceções deve estar **100% em Português (Brasil)**:
- 16 Aulas, 16 Slides, 16 Quizzes, 16 Exercícios, 16 Projetos.
- Comentários de código.
- Terminais, Diagramas e Menus.
- Sem conteúdo ou jargões soltos em inglês (quando traduzíveis).

### 🎨 Padrão Visual Obrigatório e Componentes (UX/UI)
Cada aula deve obrigatoriamente conter a adoção dos plugins do Material for MkDocs:
- 😊 **Emojis**: Coerentes e moderados para sinalizar intenção visual.
- 💻 **Terminais Interativos**: Pelo menos 1 bloco de código/terminal simulado usando `TermynalJS` (`<div class="termy" markdown>`).
- 🧠 **Admonitions (Callouts)**: Uso padronizado de:
  - `!!! info` para Conceitos-chave.
  - `!!! warning` para Atenção/Erros comuns.
  - `!!! tip` para Dicas.
  - Assegurar espaçamento (*blank line*) garantido entre o sumário de um Admonition e o conteúdo/blocos adjacentes.
- 🗂️ **Content Tabs**: Uso de abas `=== "Abordagem A"` conectadas logicamente para transições teóricas sem espaços soltos quebradores.
- 📇 **Padrão de Cards**: Atualizar todos os arquivos `index.md` utilizando as sintaxes de layout moderno com a tag `<div class="grid cards" markdown>`.

### 🧮 Diagramas Mermaid e Fórmulas Matemáticas (MathJax)
- 📊 **Diagramas Mermaid**: A versão a ser instanciada no site deve ser `11.12.3` (via unpkg CDN). 
  - Regra OBRIGATÓRIA JS Reveal: Em slides, o HTML gerado deve ter um transpilador pós-build transformando `class="language-mermaid"` em `<div class="mermaid">` seguidos da init manual do renderizador.
  - Regra OBRIGATÓRIA MkDocs Macros: **Nunca** utilize strings como `{{ TEXTO }}` dentro do Mermaid. O MkDocs tentará parsear como macro jinja2 e abortará a compilação.
  - Regra OBRIGATÓRIA Typeset UML: A notação de visibilidade deve preceder o tipo (`+String` ou `+int`), e a setagem de herança `<|--` colocada obrigatoriamente *ao final* do gráfico instanciado.
- ➕ **Fórmulas Matemáticas (LaTeX/Mathjax)**: Testar compilação `$$` em equações. Em views que não usam o renderizador base Markdown (como os Slides RevealJS), deve-se EXPLICITAMENTE incluir o plugin `<script src=".../mathjax3/math.js">` e referenciar o array de init no Javascript da página.

### 📈 Progressão Cognitiva
Expandir o aprofundamento do conhecimento das `aula-XX.md` de nível básico para **intermediário**, garantindo uma progressão cognitiva fluida profunda com exemplos de software / compilação / SO reais.

---

## 📂 2. PLANO POR DIRETÓRIO (RESUMO DO CONTEÚDO)

### 📚 `/docs/aulas/` (16 aulas fixas)
- Manter os 16 arquivos existentes, expandindo-os e os padronizando conforme a arquitetura proposta acima.

### 📝 `/docs/exercicios/`
- Cada aula terá seu arquivo de exercícios refletindo inteiramente a profundidade abordada no texto da aula correspondente.
- A **Geração Automática (Scripts Python)** deve rigorosamente criar: **5 exercícios por página**.
  - 2 nível Básico.
  - 2 nível Intermediário.
  - 1 nível Desafio Arquitetural.
- Arquivos paralelos `solucao-XX.md` devem ser gerados.
- **Conectividade**: Rodapés obrigatoriamente apresentarão links cruzando exercício para solução através de botões `.md-button`.

### 🚀 `/docs/projetos/`
- Implementações baseadas no conhecimento da `aula-XX.md` base. `VERIFICAR` compatibilidade.
- Um roteiro claro numerado de `Projeto 01` a `Projeto 16` constando simulações reais/laboratórios.

### ❓ `/docs/quizzes/`
- Extraídos do Markdown `/docs/quizzes/src/` para HTML.
- **Geração Automática (Scripts)**: O script deve gerar incríveis **10 perguntas por Quiz** com abordagens de questionamento multi-ângulos.
  - Alternativas com marcações contextuais e Explicação/Feedback imediato justificado da alternativa verdadeira.
- **Micro-Correção de UI**: O CSS global de Quiz injetado no repositório DEVE ter `flex-shrink: 0` sob as esferas `radio-button` para garantir círculos perfeitamente isométricos renderizados pelo navegador.

### 🎞 `/docs/slides/`
- Acessados de `src/` e transpilados a `docs/slides/...html`.
- **Animações (Fragments)**: O interpretador Python gerador (`generate_slides_quizzes.py`) precisa realizar a conversão explícita Regex que *Substitua* o bloco `{ .fragment }` por `<!-- .element: class="fragment" -->`, ou os slides não exibirão animações gradativas.
- **Otimização Visual do HTML Gerado (Reveal JS UX)**:
  - Eliminar ou ocultar do Footer da grade HTML estática o menu central de dica crua de teclado (ex: "Atalhos: F (Tela Cheia)").
  - Customização CSS severa injetada em `.reveal .slide-number` no canto inferior esquerdo, garantindo contraste vibrante (Ex: #ffb300) moderno e proeminência em relação ao plano de fundo.

### ⚙️ `/docs/setups/`
- `setup-01.md`: Para o ambiente **Windows** (instalação específica da linguagem-alvo do curso).
- `setup-02.md`: Para o ecossistema GNU **Linux**.

### 📂 Log e Legados (`_legado` e `logs`)
- Nunca deletar pastas legadas.
- Todo output ou varredura em massa disparando avisos em execução de IA, realocar saídas (txt obsoletos) pra ramificação root `/logs/`.

---

## ⚙️ 3. PLANO DE CORREÇÕES TÉCNICAS E CONFIGURAÇÕES MKDOCS

### Mkdocs.yml - Dark Mode & Color Scheme Override
Atualizar a paleta gráfica abolindo a mecânica genérica de clique manual via _scheme default_ e injetando leitura nativa pelo OS (media query) adotando cor de alerta moderna (*amber*).

```yaml
  palette:
    # Light Mode (Default)
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: teal
      accent: amber
      toggle:
        icon: material/weather-sunny
        name: Mudar para modo escuro
    # Dark Mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: teal
      accent: amber
      toggle:
        icon: material/weather-night
        name: Mudar para modo claro
```

### Mkdocs.yml - Social Links Integrados
Assegurar o tracking dos dados profissionais correspondente a marca registrada do professor nas footers:
```yaml
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/ricardotecpro
    - icon: fontawesome/brands/linkedin
      link: https://linkedin.com/in/ricardotecpro
    - icon: fontawesome/solid/globe
      link: https://ricardotecpro.github.io/
    - icon: fontawesome/brands/youtube
      link: https://www.youtube.com/@ricardotecpro
    - icon: fontawesome/brands/x-twitter
      link: https://twitter.com/ricardotecpro
```

### Otimizações Premium de Navegação & Metadados (SEOs)
1. `navigation.sections`, `navigation.path` e `navigation.top`: *Ativados no YML*.
2. Em `pyproject.toml`, unificar as keys `name`, `description` garantindo que reflitam 1 para 1 a pasta de root local e com a tag de autores configurada em `Ricardo Tec Pro`.
3. Os índices mestres (`index.md`) de todo diretório do projeto deverão ser reescritos em Python impedindo qualquer URL *hardcoded* legada errônea.

---

## 📋 4. PLANO E ORDEM DE VALIDAÇÃO FINAL (QA RIGOROSO)

**O curso só será comissionado pro repositório live através destas validações cirúrgicas:**
1. [ ] A branch (Deploy Pipeline) estrita apontando estático no Github Actions (`gh-pages`).
2. [ ] Validação do Site Estático através do comando master: `mkdocs build --strict`. O framework não perdoará nenhum link quebrado e abortará instantaneamente em código de Saída *1* se algo colidir.
3. [ ] Todos os novos arquivos e correções gerados salvos em um novo commit `git add .` previamente à submissão do GitHub Action para retroalimentar o plugin Mkdocs de timestamp e controle versionado (`git-authors / git-revision`).
4. [ ] Inspecionar fisicamente os slides em HTML via browser assegurando a injeção funcional do MathJax e Mermaid pós-compilação.

**🏁 RESULTADO ESPERADO DA MÁQUINA DE AUTOMAÇÃO NESTE CHECKLIST**:
Um super-repositório educacional blindado contra ambiguidades UI e bugs do MkDocs material, ostentando recursos dinâmicos (Mermaid/Terminals) irretocáveis, exercicios de ponta coerentes extraídos das Aulas Core e deploys robustos e seguros com layouts sombrios autônomos.

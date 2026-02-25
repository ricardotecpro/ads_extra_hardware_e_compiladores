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
- 📊 **Diagramas Mermaid**: Pelo menos 1 diagrama `mermaid` relevante (versão `11.12.3` recomendada).
- 💻 **Terminais Interativos**: Pelo menos 1 bloco de código/terminal simulado usando `TermynalJS` (`<div class="termy" markdown>`).
- 🧠 **Admonitions (Callouts)**: Uso padronizado de:
  - `!!! info` para Conceitos-chave.
  - `!!! warning` para Atenção/Erros comuns.
  - `!!! tip` para Dicas.
  - Assegurar espaçamento (*blank line*) garantido entre o sumário de um Admonition e o conteúdo/blocos adjacentes.
- 🗂️ **Content Tabs**: Uso de abas `=== "Abordagem A"` conectadas logicamente para transições teóricas sem espaços soltos quebradores.
- 📝 **Exercícios Progressivos**
- 🚀 **Mini-projetos**
- 📇 **Padrão de Cards**: Atualizar todos os arquivos `index.md` utilizando as sintaxes de layout moderno com a tag `<div class="grid cards" markdown>`.

### 📈 Progressão Cognitiva
Expandir o aprofundamento do conhecimento das `aula-XX.md` de nível básico para **intermediário**, garantindo uma progressão cognitiva fluida. Falta mais exemplos de uso real e listação nos conteúdos das aulas.

---

## 📂 2. PLANO POR DIRETÓRIO (RESUMO DO CONTEÚDO)

### 📚 `/docs/aulas/` (16 aulas fixas)
- Manter os 16 arquivos existentes, expandindo-os e os padronizando conforme a arquitetura proposta (Mermaid, Termynal, Admonitions).

### 📝 `/docs/exercicios/`
- Cada aula terá seu arquivo de exercícios e cada exercício deve **REFLETIR ABSOLUTAMENTE O CONTEÚDO** explícito na aula respectiva. Sem enunciados genéricos soltos.
- **Sempre `VERIFICAR` a pertinência dos exercícios com os parágrafos teóricos.**
- Estrutura: exatos **5 exercícios por página**.
  - 2 básicos.
  - 2 intermediários.
  - 1 desafio.
- Para cada `exercicio-XX.md`, deve ser gerado ou criado um `solucao-XX.md` vinculado.
- **Conectividade**: O rodapé de todo documento de exercício possuirá um link/botão exato e direto direcionando para o documento de sua Solução correspondente e explicação detalhada.

### 🚀 `/docs/projetos/`
- Devem, também, representar implementações baseadas no conhecimento exato abordado em sua respectiva `aula-XX.md` base. `VERIFICAR` compatibilidade.
- Um roteiro claro numerado de `Projeto 01` a `Projeto 16`.

### ❓ `/docs/quizzes/`
- Configuração a partir dos originais na subpasta `src/`.
- Cada quiz deve ter:
  - Um mínimo de **10 perguntas**.
  - Alternativas coerentes.
  - Explicação imediata na marcação de `feedback` detalhando a justificativa da resposta.
  - Aderência total ao conteúdo da sua aula (`VERIFICAR`).
- **Correção Visual de Interface**: O CSS do construtor de botões de Quiz deve receber `flex-shrink: 0` para garantir círculos perfeitamente desenhados, e o conversor Python garantir a quebra do feedback não mesclado com a string de alternativa.

### 🎞 `/docs/slides/`
- Acessados via subpasta fonte `src/` transpilados ao site. `VERIFICAR` alinhamento integral com as aulas.
- Padronizar mesmo visual através dos módulos; emojis moderados, código em tamanho visível legível, Mermaids injetadas.
- Mínimo de **20 frames/lâminas** progressivas por Aula/Slide.
- Adoção das animações modernas do *Reveal.js* nos Headers de formatação (`transition: convex/slide` etc.).
- **Otimização Visual de UX no HTML Gerado (Reveal JS)**:
  - Eliminar ou ocultar do Footer HTML o menu central de dica crua de teclado (ex: "Press F for Fullscreen").
  - Modificar o CSS injetado em `slide-number` no canto esquerdo, garantindo contraste vibrante e moderno e proeminência em relação ao bg.

### ⚙️ `/docs/setups/`
- Os artefatos devem cobrir o cenário completo do stack da máquina virtual do estudante em vez de serem "chavões".
- `setup-01.md`: Para o ambiente **Windows** (instalação específica da linguagem-alvo do curso).
- `setup-02.md`: Para o ecossistema GNU **Linux**.
- Outros `.md` preexistentes podem ser mantidos.
- Sempre realizar `VERIFICAR` em como essas dependências convergem pra matéria desenvolvida.

### 📂 Diretório de Arquitetura do Repositório (`_legado` e `logs`)
- **Nunca** deletar/modificar a subpasta `_legado`.
- Auditar minuciosamente no root (`index.md`, `materiais.md`, `plano-ensino.md`, `project_roadmap.md`, `sobre.md`, `README.md`) e deletar rastro histórico residual do curso genérico e reescrever descrevendo a matéria atual ativa.
- **Log Central**: Todos os logs textuais do root (exceto `requirements.txt`) e relatórios Python devem ser limpos e expurgados para dentro de uma pasta fixa `logs/`.

---

## ⚙️ 3. PLANO DE CORREÇÕES TÉCNICAS E CONFIGURAÇÕES MKDOCS

### Mkdocs.yml - Dark Mode & Color Scheme Override
Atualizar a paleta gráfica abolindo a mecânica genérica de clique manual via _scheme default_ e injetando leitura pelo OS (media query preferences) adotando cor de alerta moderna (*amber*).

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
Substituir radicalmente o namespace `extra.social` antigo pelo blueprint global:
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
  version:
    provider: mike
    default: estavel
```

### Otimizações Premium de Navegação & SEO (no mkdocs.yml)
-  `navigation.sections`: *Ativar*.
-  `navigation.path` e `navigation.top`: *Ativar*.
-  Garantir a existência de `site_description` polida e instanciar uso de plugins de SEO e Meta cards e tags.
-  **Mermaid Script JS Update**: Trocar qualquer CDN antiga do pipeline de diagrama para `https://unpkg.com/mermaid@11.12.3/dist/mermaid.min.js` mitigando fatal crashes por _Syntax Error_ do renderizador antigo.

### Metadados Dinâmicos (pyproject.toml)
Garantir o match exato do nome de projeto com o *folder name* onde executa-se a IA submetida. Atualizar metadados dos autores para a fonte oficial.
```toml
[project]
name = "[nome_exato_da_pasta_em_underscores]"
version = "1.0.0"
description = "[nome_exato_da_pasta_em_underscores]"
authors = [
    {name = "Ricardo Tec Pro", email = "ricardotecpro@hotmail.com"}
]
```

### Prevenção de Falhas Críticas em Código / Mermaid e Mkdocs-Macros
- **Classes/Relacionamento (Mermaid)**: Primeiro, definir a Entidade/Typeset (`+String nome` invés de duplo pontuação), e posicionar a relação de ligação `<|--` *somente abaixo no fim do script UML* provendo estabilidade ao parser Mermaid V11.
- **Choque MkDocs Macros**: **NUNCA** construa caixas no Mermaid englobando duplo curley braces de sintaxe jinja (ex: `{{ Caixa }}`). Isso colidirá perigosamente com as macros! Use substitutos como `([ Conteudo ])`.
- **Termynal Blocks**: A tag pai nativa `<div class="termy">` necessita obrigatoriamente do marcador `markdown` embutido acompanhado de blank spacing de quebra de linhas para compilar devidamente a renderização no MkDocs.
- Fórmulas Matemáticas `MathJax` DEVEM sempre serem testadas compiladas se ativas (Ex: equação COCOMO) garantindo *syntax-safe* load-time.

---

## 🐍 4. OTIMIZAÇÃO DE SCRIPTS PYTHON CUSTUMIZÁVEIS

Os sub-sistemas de Python locais precisam aplicar duas medidas resolutivas críticas na pipeline MkDocs perante aos Slides & Quizzes:

1. **Scripts de Índices**: Os `index.md` no root e de todas a malha navegacional (`aulas/index.md`, `quizzes/index.md`) não devem ter sub-URLs hard-coded. O Script em Python reescreverá a arquitetura e deverá assinar explicitamente `*.html` nas chamadas ao subgrupo `slides/`.
2. **Resolução de Fragment Animation Bug nos Slides**: Havia falha renderizando em runtime as palavras soltas `{ .fragment }`. O interpretador Python gerador (`generate_slides_quizzes.py`) precisa realizar a conversão explícita Regex que *Substitua*:
 `{ .fragment }` >> `<!-- .element: class="fragment" -->`
3. **Paths de Varredura**: Refatorar qualquer script Python que busquava em diretórios errôneos como `.src/` para assegurar que eles miram diretórios validados públicos `src/`.

---

## 📋 5. PLANO E ORDEM DE VALIDAÇÃO FINAL (QA RIGOROSO)

**O curso só será embalado se preencher estritamente estas condições finais:**
1. [ ] A branch para Deploy e Build no Github Actions ser comissionada propriamente no canal `gh-pages`.
2. [ ] Testes de navegação `mkdocs build --strict` compilar com status impecável *Exit Code 0* (Nenhum warning, loop de link relacional quebrado).
3. [ ] Todos os novos arquivos e correções gerados salvos em um novo commit `git add .` para alimentar plugin de verificação de timestamp (`git-authors / git-revision`).
4. [ ] Menu de navegação íntegro e condizente (Módulos reais do curso). Absolutamente nada solto do Antigo Currículo presente.
5. [ ] **Verificação Manual**: 16 Aulas formatadas para jovens/adultos de forma neutra em PT-BR; Termynais interativos brilhando, transição de slides atinente.

**🏁 RESULTADO ESPERADO DA IA NESTE CHECKLIST**:
O projeto reformulado não apresentará buracos lógicos no frontend educativo, será didaticamente rico (nível intermediário pautado) e visualizado com temas Premium atrativos aos estudantes e recrutadores.

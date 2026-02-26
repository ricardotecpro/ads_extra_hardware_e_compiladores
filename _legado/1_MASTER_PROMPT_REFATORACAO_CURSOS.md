# 🤖 Master Prompt e Plano de Refatoração Universal de Cursos (MkDocs)

Este documento atua como o **Guia Mestre de Refatoração** para ser aplicado por IAs na padronização de todos os repositórios de cursos da grade. O objetivo é garantir consistência absoluta de UI/UX, arquitetura MkDocs, scripts em Python e progressão didática.

---

## 🏗️ 0. FILOSOFIA DE SINCRONIZAÇÃO: CONTEÚDO vs. INFRAESTRUTURA

A IA deve distinguir rigorosamente entre o que é **Motor** (Infraestrutura) e o que é **Label** (Conteúdo):

1. **Infraestrutura (Sincronização 100%):** Todos os cursos devem possuir os mesmos plugins, scripts de automação, hooks de build, estrutura de pastas, nomes de arquivos técnicos (ex: `aula-01.md`), CSS premium e configurações de UI.
2. **Conteúdo (Adaptação Contextual):** Os **títulos** internos, nomes dos módulos, descrições de aulas e labels nos arquivos `index.md` devem ser extraídos da matéria do curso atual. **NUNCA** copie labels literais do projeto de referência (ex: não deixe "Intro Mobile" em um curso de Hardware).

---

## 🧭 1. DIRETRIZES GERAIS (OBRIGATÓRIAS)

### 🇧🇷 Idioma
Todo o conteúdo sem exceção deve estar **100% em Português (Brasil)**:
- 16 Aulas fixas
- Comentários de código
- 16 Slides
- 16 Quizzes
- 16 Exercícios (e Soluções)
- 16 Projetos
- Terminais (Termynal)
- Diagramas e Menus

### 🎨 Padrão Visual Obrigatório
Atualizar todos os arquivos `index.md` seguindo o padrão moderno de cards MkDocs.
Cada aula deve conter estritamente:
- 😊 **Emojis** coerentes e moderados.
- 📊 **Modelagem**: Pelo menos 1 diagrama Mermaid relevante.
- 💻 **CLI**: Pelo menos 1 exemplo interativo usando TermynalJS.
- � **Índices**: Auditar e atualizar rigorosamente todos os arquivos `index.md` de subpastas (`aulas/`, `exercicios/`, `quizzes/`, `slides/`, `projetos/`) para que reflitam os títulos reais das aulas do curso atual, eliminando qualquer rastro de cursos anteriores.
- �🧠 **Admonitions**: Blocos MkDocs de destaque (`!!! info "Conceito"`, `!!! warning "Atenção"`, `!!! tip "Dica"`).
- 📝 **Prática**: Exercícios progressivos (linkados).
- 🚀 **Prática**: Mini-projeto.

### 📈 Progressão Cognitiva
Expandir o aprofundamento do conhecimento das `aulas-xx` para um nível **intermediário**, garantindo uma progressão cognitiva suave e didática da aula 01 à 16.

---

## 📂 2. PLANO POR DIRETÓRIO (RESPEITANDO ESTRUTURA ATUAL)

### 📚 `/docs/aulas/` (16 aulas fixas)
- Manter os arquivos existentes, mas **expandir e padronizar** o conteúdo.
- Nenhuma aula deve fugir do nicho específico do curso (ex: Engenharia de Software, C++, Nuvem).

### 📝 `/docs/exercicios/`
- Cada arquivo de `exercicio-01.md` a `exercicio-16.md` deve conter exatamente **5 exercícios**:
  - 2 Básicos
  - 2 Intermediários
  - 1 Desafio
- **Atenção (Soluções):** Para cada exercício proposto, criar um arquivo correspondente (`solucao-XX.md`) com a explicação detalhada.
- Adicionar ao final da página de cada exercício um **LINK** direto para o arquivo com a solução. 
- O conteúdo dos exercícios **deve refletir estritamente** o conteúdo ministrado na sua `aula-xx.md` correspondente.

### 🚀 `/docs/projetos/`
- Estrutura esperada: `Projeto 01` até o `Projeto 16`.
- O escopo dos projetos deve consolidar o conhecimento prático da sua aula base.

### ❓ `/docs/quizzes/`
- Arquivos base devem ficar em `\docs\quizzes\src\*.md`.
- **Interatividade:** Abandonar formatação estática Markdown nos quizzes. Cada quiz deve ser implementado usando blocos HTML nativos interativos via formulários e JavaScript.
- Estética e CSS Premium. Adicionar correção Mobile (`flex-shrink: 0` nos radio-buttons).
- Cada quiz deve ter no mínimo **10 perguntas**.
- Alternativas coerentes, **100% pt-BR**, e com explicação clara (feedback) interativa para a resposta em JS.
- O material avaliado no Quiz deve ser espelho exato da `aula-xx.md`.

- **Reveal.js:** Adicionar animações e transições MODERNAS.
- **Correção Crítica de Transições:** As transições podem bugar renderizando o texto `{ .fragment }` visível para o usuário. O script gerador Python deve aplicar regex (ou correção) convertendo isso para a sintaxe HTML limpa: `<!-- .element: class="fragment" -->` durante o build.
- **Transpilação Mermaid & MathJax:** O template HTML gerado deve incluir scripts para transpilar blocos `code.language-mermaid` para `div.mermaid` e carregar o `RevealMath.MathJax3` para fórmulas.
- **Navegação (Materiais):** No `mkdocs.yml`, os links de slides devem apontar para a versão `.html` gerada, oferecendo a experiência completa do Reveal.js sem barras laterais do MkDocs.

### 🛠️ `/docs/setups/`
- Os arquivos descrevem como o aluno deve configurar a máquina para desenvolver no curso.
- Padrão mínimo exigido:
  - `setup-01.md`: Ambiente Windows.
  - `setup-02.md`: Ambiente Linux.
  - `setup-03.md` (se aplicável): macOS.
- Manter formatação visual premium (Termynal, Admonitions, Mermaid).

### 📖 Projeto de Referência MkDocs
- O referencial técnico matriz (Padrão Ouro de Navegação, CSS, e UI) que a IA deve seguir espelhado para novos projetos é **estritamente** o repositório: `D:\SourceCode\REPOS\github.io\ads_extra_hardware_e_compiladores`. Todas as práticas de arquitetura MkDocs, layouts de exercícios e menus devem derivar deste molde.

### ⛓️ Pilha de Sincronização Obrigatória
Para cada refatoração, a IA deve analisar e sincronizar a seguinte base de infraestrutura:
1. **Configuração**: `mkdocs.yml` (Plugins, Fontes, Features, Paleta).
2. **Dependências**: `pyproject.toml` (Bibliotecas de build e plugins).
3. **Automação**: `scripts/generate_slides_quizzes.py` (Lógica de Reveal.js, Mermaid, MathJax).
4. **Hooks**: `hooks/copy_slides.py` (Lógica de pós-build e limpeza de caminhos).
5. **Customização**: Pasta `overrides/` (Templates HTML customizados).
6. **Normatização**: `.mailmap` (Identidade de autor no Git).
7. **Navegação (Índices)**: Todos os arquivos `index.md` (Aulas, Slides, Exercícios, Projetos, Setups). 
   - **Nota Crítica:** Sincronize o **LAYOUT** (ex: `grid cards`) e a **HIERARQUIA**, mas adapte todos os **TÍTULOS** aos nomes reais das aulas do curso em questão.
   - **Home Page (Gold Standard):** A página raiz (`docs/index.md`) deve seguir rigorosamente:
     1. **Header:** Ícone + Título + Citação em Blockquote relevante.
     2. **Atalhos Rápidos:** Grid de 6 itens (`Trilha`, `Slides`, `Quizzes`, `Projetos`, `Exercícios`, `Setups`).
     3. **Mapa da Jornada:** Resumo dos 4 módulos (sem listar todas as 16 aulas individualmente).
     4. **Dicas de Sucesso:** 3 dicas táticas específicas da matéria.
     5. **CTA:** Botão padrão `Ir para Aula 01` ao final.

   - **Sub-Índices de Conteúdo (Pattern):** Arquivos como `slides/index.md`, `exercicios/index.md`, `quizzes/index.md` e `projetos/index.md` devem seguir:
     1. **Título:** `# [Nome do Tipo] Interativos` ou `# [Nome do Tipo] Práticos`.
     2. **Intro:** 1-2 linhas de descrição descritiva.
     3. **Módulos:** Títulos `## Módulo X – [Nome do Módulo]`.
     4. **Itens:** Lista simples com ícone de seta: `- [:octicons-arrow-right-24: [Link Text]]([link])`.
     5. **Sem Grids:** Não use `grid cards` dentro destes sub-índices de 16 itens para evitar poluição visual.

   - **Materiais e Setups (Grid Pattern):**
     1. **Materiais (`docs/materiais.md`):** Título limpo `# Materiais` + Grid 5 itens.
     2. **Setups (`docs/setups/index.md`):** `# Configuração do Ambiente` + Grid 3 itens (OS) + Seção `## 📋 Próximos Passos`.
8. **Pipeline (CI/CD)**: Pasta `.github/workflows/` (Configurações de build automatizado, testes e deploy).
9. **Menu Superior (Tabs)**: O `nav` deve possuir **exatamente** 4 abas principais: `Informações`, `Aulas`, `Materiais` e `Impressão`. Não crie abas extras como `Outros`.
10. **Agrupamento de Aulas**: Dentro da aba `Aulas`, os links devem ser obrigatoriamente agrupados por **Módulos** (Ex: `Módulo 1 - Fundamentos`) para facilitar a navegação.

---

## ⚙️ 3. CONFIGURAÇÕES GLOBAIS (mkdocs.yml e pyproject.toml)

### A. Identidade Visual e Logotipo (`mkdocs.yml` e assets)
**Logo (SVG Transparente)**
- Logotipos PNGs frequentemente quebram nos modos escuro/claro, apresentando fundos estranhos. A IA **deve exigir ou criar** (se suportado) o logotipo oficial do curso em formato `.svg` na **cor branca ou adaptável**, **estritamente em fundo transparente**.
- Substituir globalmente o ícone `favicon` e `logo` no `mkdocs.yml`.

**Tipografia e Funcionalidades**
- **Fontes**: Usar `Roboto` para texto e `Roboto Mono` para código.
- **Features**: Habilitar obrigatoriamente:
  - `navigation.sections`, `navigation.path`, `navigation.instant`, `navigation.prune`.
  - `search.share`, `search.suggest`, `search.highlight`.
  - `content.code.copy`, `content.code.annotate`.
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

### B. Redes Sociais (`mkdocs.yml`)
A matriz extra social footer deve apontar sempre para o portfólio moderno:
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

### C. Plugins e Exclusões
- **Ordem dos Plugins**: O plugin `print-site` deve ser **estritamente o último** da lista no `mkdocs.yml`.
- **Plugins Essenciais**: Adicionar `minify`, `tags`, `awesome-pages` e `social` (cards: false).
- **Exclusão de Docs**: Adicionar `exclude_docs` para evitar avisos de links quebrados ou arquivos unmapped das pastas `src/` e arquivos `.md` de slides que são redundantes pós-geração do HTML:
```yaml
exclude_docs: |
  quizzes/src/*
  slides/src/*
  slides/slide-*.md
```

### D. Assinatura Universal (`pyproject.toml`)
Para cada curso validado, o `name` deve espelhar rigidamente a pasta pai (ex: `ads_<nome_generico_do_curso>`), e o author ser sobrescrito:
```toml
[project]
name = "ads_nome_do_curso" # Exemplo, atualizar caso a caso
version = "1.0.0"
description = "ads_nome_do_curso"
authors = [
    {name = "Ricardo Tec Pro", email = "ricardotecpro@hotmail.com"}
]
```

---

## 🔎 4. REVISÃO DE BUGS E SINTAXE (Troubleshooting)

1. **Mermaid.js CDNs & Macros**
   - Atualizar no `mkdocs.yml` o JS do Mermaid para a versão robusta: `https://unpkg.com/mermaid@11.12.3/dist/mermaid.min.js`.
   - **Prevenção de Erros ("Syntax Error"):** Em diagramas OO, relações (ex: `Pessoa <|-- Aluno`) devem ser plotadas preferencialmente após os blocos de definição das classes. Use tipagem unificada (ex: `+String nome`).
   - **Conflito de MkDocs-Macros:** Troque chaves duplas internas do mermaid `{{ ... }}` por colchetes em balão `([ ... ])` para evitar embate com o jinja renderer.

2. **Termynal Formatting**
   - Na injeção das Divs invisíveis (seja via classe HTML ou bloco `<!-- termynal -->`), use `markdown="1"` ou garanta os espaçamentos internos para que o texto MkDocs cruze a fronteira da tag como bloco visual íntegro.

3. **Admonitions & Tab Group Spacing**
   - Content Tabs `===` encavalados falham em processar o markdown interno se não tiverem linhas vazias de oxigênio entre o Header e o seu miolo. Remova linhas em branco avulsas entre várias de declarações de Headers de Tabs concorrentes, para amarrá-los numa janela única. Mas garanta sempre espaçamento interno perante Admonitions superiores.

4. **MathJax Rendering**
   - Validar massivamente se as fórmulas (LaTex) estão escapadas com clareza (testado com sucesso no modelo matemático de COCOMO e lógicas em aulas densas). Carregar o CDN MathJax caso offline configure quebra.

5. **Fix de Bug "Git Authors" Assinaturas**
   - Se os artigos acusarem e-mail de dev (`ricardo@example.com`), suba um artefato `.mailmap` na raiz mapeando o e-mail legado para `ricardotecpro@hotmail.com`.

6. **Conflitos de Rendering (ex: Svelte / Angular vs MkDocs Macros)**
   - Caso o curso lecione frameworks que utilizem interpolação com chaves duplas `{{ variavel }}`, configure compulsoriamente a flag `render_macros: false` no metadata (`frontmatter`) dos arquivos afetados para evitar quebra silenciosa ou erros de build do MkDocs Python jinja.

7. **Windows Compatibility (Unicode Errors)**
   - **CRÍTICO:** Evitar o uso de caracteres Unicode complexos (como `✓`, `→`, `⚠`) em mensagens de log impressas por scripts Python ou hooks. No Windows, isso causa `UnicodeEncodeError`. Use sempre equivalentes ASCII (ex: `OK`, `->`, `WARNING`).

8. **Testes Quirks (Quizzes & Terminais em Playwright/Selenium)**
   - O comportamento de botões de cópia (Termynal) e feedback boxes (Quizzes interativos) exige visibilidade real CSS. Testes que acessam o DOM correm risco de *Timeout*. Sempre instruir *asserts* para aguardar transições HTML antes de iterar testes automatizados nestes elementos.

---

## 🛡️ 5. PLANO DE VALIDAÇÃO FINAL (CHECKLIST)

Antes do commit da Release, a IA deve atestar:
- [ ] O Logo do curso foi auditado: Deve ser `.svg` de cor branca em fundo transparente, eliminando bordas visíveis em Dark/Light cases de UI MkDocs.
- [ ] Build do MkDocs passa com comando irrestrito sem lixo de log: `mkdocs build --strict` - é vital não tolerar NENHUM `unmapped file`.
- [ ] Os arquivos gerados de `solucao-XX.md` **estão obrigatoriamente incluídos no Navigation Block** (`mkdocs.yml`).
- [ ] Todos os caminhos (Links Internos) estão sólidos (referências relativas exatas entre aulas `->` soluções `->` exercícios `->` slides).
- [ ] Renderizadores UI operantes (Mermaid e Termynal não quebram formatações).
- [ ] O Menu (Nav) segue o padrão de 4 abas: *Informações*, *Aulas* (agrupadas por módulos), *Materiais* e *Impressão*.
- [ ] Auditoria de Índices concluída: `index.md`, `aulas/index.md`, `slides/index.md`, `exercicios/index.md`, `quizzes/index.md` e `projetos/index.md` estão 100% atualizados com os temas do curso, garantindo que o **layout** seja premium (como o de referência) mas o **conteúdo** seja o correto.
- [ ] Há um número padronizado de aulas, refletindo o escopo ideal do curso.
- [ ] O texto é fluído, 100% pt-BR, e **livre de menções literais a escopos mortos de outros cursos do passado**.
- [ ] **Mover Logs**: Todos os arquivos `.txt` e `.log` resultantes de builds experimentais na raiz devem ser movidos para o diretório `logs/` (criado se não existir).
- [ ] Organização estrutural em disco: Limpeza final de arquivos residuais e temporários.
- [ ] Diretório Sagrado `_legado`: **Nocivo intocável**. Nunca altere ou apague pastas com nome `_legado`.
- [ ] Revisão dos indíces velhos na raiz: `index.md`, `materiais.md`, `plano-ensino.md` (deve ser `plano.md`), `project_roadmap.md`, `sobre.md`, `README.md` expurgados sobre quaisquer rastros da tecnologia velha do repositório template.
- [ ] O deploy e CD está devidamente engatilhado no branch `gh-pages` com pipeline viável.

## 🎓 RESULTADO ESPERADO
- **Atratividade Material:** 🎨 Interface premium.
- **Didática:** 🧠 Focado em alunos iniciantes (jovens e adultos), neutro e robusto pedagogicamente.
- **Arquitetura:** 📂 Organizado e hiper-escalável.

---

## 📄 6. TEMPLATE: PLANO DE IMPLEMENTAÇÃO PADRÃO

A IA deve gerar um plano seguindo este esqueleto para cada novo curso:

# Plano de Implementação - Padronização de `[NOME_DO_REPOSITORIO]`

## ## Proposed Changes

### Configuration & Infrastructure
- **Logo/Favicon**: Auditoria do `.svg` (branco/transparente).
- **mkdocs.yml**: Refinar paleta, links sociais e assinaturas.
- **.mailmap**: Mapear autoria para `ricardotecpro@hotmail.com`.
- **Auditoria de Índices**: Limpar `index.md` de todas as pastas (remover rastros de templates).
- **Workflows**: Sincronizar `.github/workflows/` para garantir testes e deploy automatizados.

### Lessons (`/docs/aulas/`)
- Garantir as 16 aulas com Mermaid, Termynal, Admonitions e links práticos.

### Exercises & Solutions (`/docs/exercicios/`)
- 5 exercícios por aula + links para soluções detalhadas.

### Quizzes (`/docs/quizzes/`)
- Versão interativa HTML/JS premiun com correção mobile.

### Slides (`/docs/slides/`)
- Reveal.js com fragmentos corrigidos, MathJax e Mermaid transpiled.

### Setups (`/docs/setups/`)
- Triade padrão: Windows, Linux, macOS.

## ## Infrastructure Synchronization (Reference Project)

Sincronizar com `ads_extra_hardware_e_compiladores`:
- **Features**: sections, path, instant, prune, search.share.
- **Plugins**: social, tags, awesome-pages, minify, print-site (último).
- **Navigation**: Hierarquia modular (Informações, Aulas, Materiais).

## ## Verification Plan

### Automated Tests
- `mkdocs build --strict`
- `pytest tests/`

### Manual Verification
- `mkdocs serve` + Mobile Review + Mermaid/MathJax Check.

### Cleanup
- **Mover Logs**: Mover logs do raiz (`build_log*.txt`) para a pasta `\logs`.

# 🤖 Master Prompt e Plano de Refatoração Universal de Cursos (MkDocs)

Este documento atua como o **Guia Mestre de Refatoração** para ser aplicado por IAs na padronização de todos os repositórios de cursos da grade. O objetivo é garantir consistência absoluta de UI/UX, arquitetura MkDocs, scripts em Python e progressão didática.

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
- 🧠 **Admonitions**: Blocos MkDocs de destaque (`!!! info "Conceito"`, `!!! warning "Atenção"`, `!!! tip "Dica"`).
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
- Cada quiz deve ter no mínimo **10 perguntas**.
- Alternativas coerentes, **100% pt-BR**, e com explicação clara para a reposta correta.
- O material avaliado no Quiz deve ser espelho exato da `aula-xx.md`.
- Correção Visual de UI (`flex-shrink: 0` nos radio-buttons para Mobile).

### 🎞 `/docs/slides/`
- Arquivos base ficam em `\docs\slides\src\*.md`.
- **Tamanho:** Para aulas curtas, média de 20 slides. Para aulas muito densas, estender para média de 40 slides. *Não gerar slides vazios ou fugir do tema só para dar volume.*
- **Visual:** Emojis moderados, Diagramas Mermaid embutidos nativamente, trechos de código altamente visíveis.
- **Reveal.js:** Adicionar animações e transições modernas.
- **Correção Crítica de Transições:** As transições podem bugar renderizando o texto `{ .fragment }` visível para o usuário. O script gerador Python deve aplicar regex (ou correção) convertendo isso para a sintaxe HTML limpa: `<!-- .element: class="fragment" -->` durante o build. O gerador não deve ler da pasta oculta legada, mas sempre da original correta.

### 🛠️ `/docs/setups/`
- Os arquivos descrevem como o aluno deve configurar a máquina para desenvolver no curso.
- Padrão mínimo exigido:
  - `setup-01.md`: Ambiente Windows.
  - `setup-02.md`: Ambiente Linux.
  - `setup-03.md` (se aplicável): macOS.
- Manter formatação visual premium (Termynal, Admonitions, Mermaid).

>*Sempre VERIFICAR se todos os derivados (Slides, Quizzes, Setups, Projetos) estão de fato alinhados à matéria das aulas principais.*

---

## ⚙️ 3. CONFIGURAÇÕES GLOBAIS (mkdocs.yml e pyproject.toml)

### A. Paleta de Cores e Modo Dark/Light Nativo (`mkdocs.yml`)
Substitua e atualize o block de palette para garantir que responda à preferência do SO do usuário:
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

### C. Assinatura Universal (`pyproject.toml`)
Para cada curso validado, o `name` deve espelhar rigidamente a pasta pai, e o author ser sobrescrito:
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
   - Se os artigos acusarem e-mail de dev (`ricardo@example.com`), suba um artefato `.mailmap` oculto à raiz mapeando o e-mail legando para `ricardotecpro@hotmail.com` (O plugin lerá nativamente sem destruir a history branch).

---

## 🛡️ 5. PLANO DE VALIDAÇÃO FINAL (CHECKLIST)

Antes do commit da Release, a IA deve atestar:
- [ ] Build do MkDocs passa com comando irrestrito sem lixo de log: `mkdocs build --strict`.
- [ ] Todos os caminhos (Links Internos) estão sólidos (referências relativas exatas entre aulas `->` soluções `->` exercícios `->` slides).
- [ ] Renderizadores UI operantes (Mermaid e Termynal não quebram formatações).
- [ ] O Menu (Nav) obedece: *Informações (Curso, Plano, Projetos)* e *Configurações (Setups)* lógicos.
- [ ] Há apenas 16 Aulas.
- [ ] O texto é fluído, 100% pt-BR, e **livre de menções literais a escopos mortos de outros cursos do passado**.
- [ ] Organização estrutural em disco: **Mover** arquivos .txt resultantes de logs antigos (menos o `requirements.txt`) para um novo diretório limpo e organizado `logs/`.
- [ ] Diretório Sagrado `_legado`: **Nocivo intocável**. Nunca altere ou apague pastas com nome `_legado`.
- [ ] Revisão dos indíces velhos na raiz: `index.md`, `materiais.md`, `plano-ensino.md` (deve ser `plano.md`), `project_roadmap.md`, `sobre.md`, `README.md` expurgados sobre quaisquer rastros da tecnologia velha do repositório template.
- [ ] O deploy e CD está devidamente engatilhado no branch `gh-pages` com pipeline viável.

## 🎓 RESULTADO ESPERADO
- **Atratividade Material:** 🎨 Interface premium.
- **Didática:** 🧠 Focado em alunos iniciantes (jovens e adultos), neutro e robusto pedagogicamente.
- **Arquitetura:** 📂 Organizado e hiper-escalável.

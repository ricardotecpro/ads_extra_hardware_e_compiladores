# 🤖 Master Prompt e Plano de Refatoração Universal de Cursos (MkDocs)

> **Objetivo:** Este documento serve como um Prompt de Comando mestre e um Guia de Checklist detalhado para ser repassado a uma Inteligência Artificial (ou engenheiro). O objetivo é padronizar qualquer repositório antigo de curso no ecossistema atualizado, garantindo consistência técnica nos scripts `Python`, estabilidade do build e uma UI/UX Premium baseada no *Material for MkDocs*.

## 🎯 INSTRUÇÕES PARA A IA DE REFATORAÇÃO:

Quando você (a IA) adentrar num novo repositório de curso que ainda possui a estrutura crua/legada, você deve, OBRIGATORIAMENTE, seguir este plano de voo na ordem abaixo:

---

## FASE 1: Limpeza e Correções Estruturais

- [ ] **1. Identidade do Repositório (`pyproject.toml` e `.mailmap`)**
    - Abra o `pyproject.toml` e altere a estrofe de "autores" para: `authors = [{name = "Ricardo Tec Pro", email = "ricardotecpro@hotmail.com"}]`. O nome do projeto lá dentro deve coincidir com o nome raiz da pasta (ex: `ads_nome_do_curso`).
    - Crie/Sobrescreva na raiz o arquivo `.mailmap` contendo a regra que corrige o bug global de exibição de e-mail do autor (`ricardo@example.com`):
      ```text
      Ricardo <ricardotecpro@hotmail.com> <ricardo@example.com>
      Ricardo Tec Pro <ricardotecpro@hotmail.com> <ricardo@example.com>
      ```
    - *Não* tente realizar git rebases para reescrever centenas de commits em lote. Apenas suba o `.mailmap` e o plugin `git-authors-plugin` lerá automaticamente.

- [ ] **2. Correção Mestra de Top-Bar e Navegação (`mkdocs.yml`)**
    - Agrupe a navegação básica sob o nó `Informações:` e renomeie as tabs clássicas:
      - `Home: index.md` passa a ser `Curso: index.md`
      - `Plano de Ensino: plano-ensino.md` passa a ser `Plano: plano.md`.
    - Renomeie o arquivo físico rente (via `git mv`) `docs/plano-ensino.md` para `docs/plano.md`.
    - Sob o painel `Configuração:` no YAML, faça brotar as tabs para `Windows`, `Linux` e `Mac` apontando para seus respectivos `.md`.
    - Atualize as rotas de Social e Fontes para priorizar acessibilidade e remover referências do antigo autor.

- [ ] **3. Conserto Rigoroso dos Slides**
    - Vá na aba `docs/slides/_revisao` e garanta que o conteúdo de fato é a versão mais moderna.
    - O Script de slides deve ser corrigido para injetar caminhos de hiperlinks com subida `../../` (pois os links quebram ao entrar no index do html).
    - O Bug do hardcode `.fragment` precisa da regex Python consertando as caixas para o formato comment `<!-- .element: class="fragment" -->`.
    - Altere o template base do slide ou o CSS para remover os textos estáticos `"S"` e `"F"` intrusivos do miolo.
    - Garanta que o slide index puxa apenas de `docs/slides/src` rodando o gerador para re-compilar.

---

## FASE 2: Geração de Material Didático Inteligente e UI/UX Premium ✨

- [ ] **4. Refatoração Visual (UI/UX) Massiva**
    - Não tolere exercícios com formato cru (*Paredes de textos*).
    - Você deve criar ou adaptar scripts Python (`refactor_exercicios_ui.py`) que vasculhem a pasta `/docs/exercicios` e convertam blocos `## Questão` em Admonitions Interativas nativas:
      ```markdown
      !!! question "Título do Exercício ou Questão"
          **Contexto:** ...
      ```
    - Na pasta de `/docs/exercicios/` para as resoluções, deve-se gerar o Admonition verde (Sucesso):
      ```markdown
      !!! success "Solução da Questão X"
          **Explicação:** ...
      ```
    - Limpe os hífens decorativos `---` no miolo, pois quebram as endentações do Material MkDocs.

- [ ] **5. Restauração Global de Terminais (Fator Termynal JS)**
    - Cursos antigos usam a syntax estéril via div FastApi: `<div class="termy">...</div>`. Isso quebra o plugin do Python local.
    - Crie um script RegExp que varra todas as 16 aulas e substitua a Div envolvente estéril pelas flags Mágicas e Invisíveis `<!-- termynal -->` que são um requisito estrito do `mkdocs-termynal == 0.13.1`. O Botão Custom de copiar JS (que acompanha no repo) continuará rodando lindo e nativo!

- [ ] **6. Otimização do Script "Gerador Profundo" de Materiais**
    - Atualize a rotina para que o Script `rebuild_all_materials.py` garanta gerar no **mínimo 5 exercicios graduais** (2 básicos, 2 médios e 1 desafio).
    - O conteúdo base gerado dos Quizzes (`docs/quizzes/src`) deve sempre puxar do texto vivo da Aula correspondente `docs/aulas/aula-XX.md`.
    - Os quizzes gerados (*Quiz JS Form*) devem ter `flex-shrink: 0` fixado nos radio buttons para evitar bugs em telas menores (mobile).

---

## FASE 3: Conteúdo Específico e Validação

- [ ] **7. Ajuste Semântico Focado (Variável de Curso)**
    - *Isso é a única que difere nos projetos:* O texto e teor do curso (Ex: Aulas, Plano, Setups, Quizzes) **devem aderir perfeitamente ao nicho abordado (ex: Nuvem, C++, Typescript).** Não re-aproveite o mesmo setup se a tecnologia for radicalmente divergente.

- [ ] **8. Teste Estrito e Finalização**
    - Execute invariavelmente `mkdocs build --strict` para capturar Broken Links e conflitos de Macro no Mermaid 11+. Se acusar falhas em colchetes do mermaid `+Texto+`, trate ignorando a colisão das Macros usando o config do MkDocs (`render_macros: false` num block do arquivo md afetado).
    - Confira a integridade da suite PyTest com `pytest` (especialmente testes de Navbar e layout).
    - Escale para o Github (`git commit` + `git push`).

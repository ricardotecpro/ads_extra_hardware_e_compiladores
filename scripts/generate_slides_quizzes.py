"""
Script para gerar automaticamente todos os slides HTML e quizzes interativos
Baseado nos formatos antigos que funcionavam
"""
import pathlib
from rich import print
from rich.progress import track


def generate_slide_html(lesson_number: int) -> str:
    """Gera HTML para um slide específico"""
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula {lesson_number:02d} - Fundamentos da Computação</title>
    
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reset.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/theme/black.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/monokai.css">
    <link rel="stylesheet" href="../assets/css/reveal-custom.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section data-markdown="slide-{lesson_number:02d}.md"
                     data-separator="^\\n---\\n$"
                     data-separator-vertical="^\\n--\\n$">
            </section>
    <style>
        /* Personalização do badge de número de slides (Canto Inferior Esquerdo) */
        .reveal .slide-number {{
            background-color: #ffb300 !important;
            color: #000 !important;
            font-size: 16px !important;
            font-weight: bold !important;
            border-radius: 6px !important;
            padding: 6px 10px !important;
            bottom: 20px !important;
            left: 20px !important;
            right: auto !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }}
    </style>
    <!-- Dicas de Atalhos Centro Removidas Conforme Padrão V2 -->

    <script src="https://unpkg.com/reveal.js@4.5.0/dist/reveal.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/markdown/markdown.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/highlight.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/notes/notes.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/math/math.js"></script>
    <script src="https://unpkg.com/mermaid@11.12.3/dist/mermaid.min.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            slideNumber: 'c/t',
            showSlideNumber: 'all',
            controls: true,
            progress: true,
            transition: 'slide',
            transitionSpeed: 'default',
            backgroundTransition: 'fade',
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes, RevealMath.MathJax3 ],
            mathjax3: {{
                mathjax: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js',
                tex: {{
                    inlineMath: [ [ '$', '$' ], [ '\\\\(', '\\\\)' ] ]
                }},
                options: {{
                    skipHtmlTags: [ 'script', 'noscript', 'style', 'textarea', 'pre' ]
                }}
            }}
        }}).then(() => {{
            // Após o build do Reveal, transpilar classes markdown Mermaid para renders SVG reais
            document.querySelectorAll('pre code.language-mermaid').forEach(code => {{
                const pre = code.parentElement;
                const div = document.createElement('div');
                div.className = 'mermaid';
                div.textContent = code.textContent;
                pre.replaceWith(div);
            }});
            mermaid.initialize({{ startOnLoad: false, theme: 'dark' }});
            mermaid.run({{ querySelector: '.mermaid' }});
        }});

        // JS Customizado Removido (Dicas Ocultadas)
    </script>
</body>
</html>
'''


def clean_slide_markdown(md_path: pathlib.Path) -> None:
    """Remove frontmatter YAML dos slides markdown"""
    content = md_path.read_text(encoding='utf-8')
    
    # Remove frontmatter se existir
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            # Remove tudo até o segundo ---
            content = parts[2].lstrip()
            
            # Remove comentários Marp
            lines = content.split('\n')
            cleaned_lines = [line for line in lines if not line.strip().startswith('<!-- _class:')]
            content = '\n'.join(cleaned_lines)
            
            md_path.write_text(content, encoding='utf-8')
            print(f"  [green]✓[/green] Limpou frontmatter de {md_path.name}")


def generate_all_slides():
    """Gera arquivos HTML para todos os 16 slides"""
    slides_dst_dir = pathlib.Path('docs/slides')
    slides_src_dir = slides_dst_dir / 'src'
    
    if not slides_src_dir.exists():
        print("[yellow]⚠ Pasta docs/slides/src/ não encontrada.[/yellow]")
        return
    
    print("\n[bold cyan]📊 Gerando Slides HTML...[/bold cyan]")
    print(f"Fonte: {slides_src_dir}")
    
    for i in track(range(1, 17), description="Processando slides..."):
        src_md_name = f"slide-{i:02d}.md"
        src_md_path = slides_src_dir / src_md_name
        dst_md_path = slides_dst_dir / src_md_name
        html_path = slides_dst_dir / f"slide-{i:02d}.html"
        
        if src_md_path.exists():
            # 1. Ler fonte
            content = src_md_path.read_text(encoding='utf-8')
            
            # 2. Limpar (opcional, se já estiver limpo não faz mal)
            # A função clean_slide_markdown era in-place, vamos fazer em memória aqui ou adaptar
            # Para simplificar, copiamos e limpamos no destino
            
            # Remove frontmatter se existir
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2].lstrip()
            
            # Remove classes Marp (legado)
            lines = content.split('\n')
            content = '\n'.join([l for l in lines if not l.strip().startswith('<!-- _class:')])
            
            # Converte fragmentos: { .fragment } -> <!-- .element: class="fragment" -->
            content = content.replace('{ .fragment }', '<!-- .element: class="fragment" -->')
            
            # 3. Escrever Markdown runtime em docs/slides/
            dst_md_path.write_text(content.strip(), encoding='utf-8')
            
            # 4. Gerar HTML referenciando este markdown
            html_content = generate_slide_html(i)
            html_path.write_text(html_content, encoding='utf-8')
        else:
            print(f"[yellow]⚠ Fonte {src_md_path} não encontrada[/yellow]")
    
    print(f"[green]✓ {16} slides HTML e MD gerados com sucesso![/green]")


def convert_quiz_to_html(quiz_number: int) -> str:
    """Lê quiz markdown e retorna versão HTML (placeholder - precisa ser implementado)"""
    # Por enquanto retorna template básico
    # Você precisará implementar a conversão real baseado no conteúdo
    return f'''# Quiz {quiz_number:02d}

--8<-- "assets/quiz.html"

<!-- Adicione as perguntas aqui no formato HTML -->
<div class="quiz-container">
  <div class="quiz-question">Pergunta de exemplo</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto!">Opção correta</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">Opção incorreta</div>
  <div class="quiz-feedback"></div>
</div>
'''


def main():
    """Função principal"""
    print("[bold]🚀 Automação de Slides e Quizzes[/bold]")
    print("=" * 50)
    
    generate_all_slides()
    
    print("\n[yellow]⚠ Nota:[/yellow] Quizzes precisam ser convertidos manualmente")
    print("  Use o template em docs/quizzes/quiz-01.md como referência")
    
    print("\n[green]✅ Automação concluída![/green]")


if __name__ == '__main__':
    main()

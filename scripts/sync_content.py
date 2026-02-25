import os
import re
from pathlib import Path

# Paths relative to where the script is run (root of repo)
LESSONS_DIR = Path("docs/aulas")
SLIDES_DIR = Path("docs/slides")
QUIZZES_DIR = Path("docs/quizzes")
EXERCISES_DIR = Path("docs/exercicios")
PROJECTS_DIR = Path("docs/projetos")

# Basic check to ensure we are in root
if not LESSONS_DIR.exists():
    # Try looking for it relative to current script if run from scripts dir
    if Path("../docs/aulas").exists():
        os.chdir("..")
    else:
        print(f"Error: Could not find docs/aulas. Current dir: {os.getcwd()}")
        exit(1)

def get_lesson_info(lesson_path):
    content = lesson_path.read_text(encoding="utf-8")
    
    # Extract title with regex to handle potential formatting
    title_match = re.search(r"^title:\s*(.*)$", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else f"Aula {lesson_path.stem}"
    
    # Extract headers (h1, h2, h3) - prioritizing h2/h3 as h1 is usually title
    headers = re.findall(r"^(#{2,3})\s+(.*)$", content, re.MULTILINE)
    
    return {
        "title": title,
        "headers": headers,
        "stem": lesson_path.stem
    }

def generate_slide_md(info):
    # Extract number from aula-01 -> 01
    num = info['stem'].split('-')[-1]
    md_path = SLIDES_DIR / f"slide-{num}.md"
    html_path = SLIDES_DIR / f"slide-{num}.html"
    
    # Markdown Content
    md_content = f"""---
marp: true
theme: default
paginate: true
---

# {info['title']}

---

## Agenda

"""
    # Simply list all H2 headers
    for level, text in info['headers']:
        if level == "##":
            md_content += f"- {text}\n"

    # Create slides for headers
    for level, text in info['headers']:
        if level == "##":
            md_content += f"\n---\n\n# {text}\n"
        elif level == "###":
             md_content += f"\n---\n\n## {text}\n\n* Tópico importante...\n* Detalhes...\n"
             
    md_path.write_text(md_content, encoding="utf-8")
    print(f"  [MD] Created {md_path.name}")
    
    # HTML Wrapper (Reveal.js)
    html_content = f"""<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{info['title']}</title>
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reset.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/theme/black.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/monokai.css">
    <link rel="stylesheet" href="../assets/css/reveal-custom.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section data-markdown="slide-{num}.md"
                     data-separator="^---$"
                     data-separator-vertical="^--$">
            </section>
        </div>
    </div>
    
    <div class="reveal-shortcuts">
        Atalhos: F (Tela Cheia) | S (Speaker View)
    </div>

    <script src="https://unpkg.com/reveal.js@4.5.0/dist/reveal.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/markdown/markdown.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/highlight.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            slideNumber: 'c/t',
            showSlideNumber: 'all',
            plugins: [ RevealMarkdown, RevealHighlight ]
        }});
    </script>
</body>
</html>"""
    html_path.write_text(html_content, encoding="utf-8")
    print(f"  [HTML] Created {html_path.name}")

def generate_quiz(info):
    num = info['stem'].split('-')[-1]
    quiz_path = QUIZZES_DIR / f"quiz-{num}.md"
    
    content = f"""# Quiz: {info['title']}

<link rel="stylesheet" href="../../assets/css/quiz.css">
<script src="../../assets/js/quiz.js" defer></script>

<div class="quiz-container">
  <div class="quiz-item" id="q1">
    <div class="quiz-question">1. Qual o principal conceito de {info['title']}?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">A)</span> Resposta Correta (Conceito Chave).
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> Conceito incorreto.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Outra resposta errada.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
</div>
"""
    quiz_path.write_text(content, encoding="utf-8")
    print(f"  [Quiz] Created {quiz_path.name}")

def generate_exercise(info):
    num = info['stem'].split('-')[-1]
    ex_path = EXERCISES_DIR / f"exercicio-{num}.md"
    content = f"""# Exercício: {info['title']}

## Objetivo
Praticar os conceitos aprendidos em **{info['title']}**.

## Instruções
1. Crie um novo arquivo ou projeto.
2. Aplique a técnica de...
3. Documente seus resultados.

## Desafio
Tente explicar a um colega como funciona...
"""
    ex_path.write_text(content, encoding="utf-8")
    print(f"  [Ex] Created {ex_path.name}")

def generate_project(info):
    num = info['stem'].split('-')[-1]
    proj_path = PROJECTS_DIR / f"projeto-{num}.md"
    content = f"""# Projeto: {info['title']}

## Descrição
Desenvolva um pequeno projeto prático aplicando os conceitos de {info['title']}.

## Requisitos
- [ ] Implementar funcionalidade básica
- [ ] Testar casos de borda
- [ ] Documentar o código
"""
    proj_path.write_text(content, encoding="utf-8")
    print(f"  [Proj] Created {proj_path.name}")

def main():
    print(f"Syncing content from {LESSONS_DIR}...")
    
    files = sorted(list(LESSONS_DIR.glob("aula-*.md")))
    if not files:
        print("No lesson files found!")
        return

    for lesson_file in files:
        print(f"Processing {lesson_file.name}...")
        try:
            info = get_lesson_info(lesson_file)
            generate_slide_md(info)
            generate_quiz(info)
            generate_exercise(info)
            generate_project(info)
        except Exception as e:
            print(f"Error processing {lesson_file.name}: {e}")

    print("Sync complete.")

if __name__ == "__main__":
    main()

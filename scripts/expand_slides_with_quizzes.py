import pathlib
import re

SLIDES_DIR = pathlib.Path("docs/slides/src")
QUIZZES_DIR = pathlib.Path("docs/quizzes/src")

def expand_slides():
    for i in range(1, 17):
        slide_file = SLIDES_DIR / f"slide-{i:02d}.md"
        quiz_file = QUIZZES_DIR / f"quiz-{i:02d}.md"

        if not slide_file.exists() or not quiz_file.exists():
            continue

        slide_content = slide_file.read_text(encoding='utf-8')
        
        # Count current physical slides (separated by '---')
        slide_count = len(re.findall(r'^---$', slide_content, re.MULTILINE)) + 1
        
        # If already 20 or already has quiz section, skip
        if "🧠 Quiz Rápido" in slide_content or "Quiz Rápido" in slide_content:
            print(f"Aula {i:02d}: Já possui quiz anexado.")
            continue

        print(f"Aula {i:02d} possui {slide_count} slides. Anexando Quizzes...")

        quiz_content = quiz_file.read_text(encoding='utf-8')
        
        # Parse questions
        # Perguntas geralmente comecam com ### ou ## ou numero
        questions = re.split(r'^###\s+\d+\.\s+', quiz_content, flags=re.MULTILINE)
        
        if len(questions) <= 1:
            # Tentar outro padrao
            questions = re.split(r'^\d+\.\s+', quiz_content, flags=re.MULTILINE)
            
        if len(questions) > 1:
            appended_text = "\n\n---\n\n<!-- .element: class=\"fragment\" -->\n# 🧠 Quiz Rápido\n## Prática de Fixação\n\n"
            
            for q_idx, q_block in enumerate(questions[1:], 1):
                # Extrair titulo da pergunta e alternativas
                lines = q_block.strip().split('\n')
                question_title = lines[0]
                
                alts = []
                correct_alt = ""
                feedback = ""
                
                for line in lines[1:]:
                    if line.strip().startswith('- [x]') or line.strip().startswith('* [x]'):
                        alt_text = line.replace('- [x]', '').replace('* [x]', '').strip()
                        alts.append(f"- **{alt_text}**")
                        correct_alt = alt_text
                    elif line.strip().startswith('- [ ]') or line.strip().startswith('* [ ]'):
                        alt_text = line.replace('- [ ]', '').replace('* [ ]', '').strip()
                        alts.append(f"- {alt_text}")
                    elif line.strip().startswith('>'):
                        feedback += line.replace('>', '').strip() + " "
                
                # Montar o Slide da Pergunta
                appended_text += f"---\n\n### Pergunta {q_idx}\n{question_title}\n\n"
                for alt in alts:
                    appended_text += f"{alt}\n"
                
                appended_text += f"\n<span class=\"fragment\">\n\n**✅ Resposta:** {correct_alt}\n\n*{feedback.strip()}*\n</span>\n\n"
            
            # Escrever de volta
            slide_file.write_text(slide_content + appended_text, encoding='utf-8')
            print(f"Quiz anexado na Aula {i:02d} com sucesso! (+{len(questions)-1} slides)")

expand_slides()

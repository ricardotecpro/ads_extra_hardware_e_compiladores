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
        
        # Strip old quiz formats to prevent duplicates and recreate cleanly
        marker_match = re.search(r'\n---\n+<!-- \.element: class="fragment" -->\n# 🧠 Quiz', slide_content)
        if marker_match:
            slide_content = slide_content[:marker_match.start()].strip()
            
        marker_backup = re.search(r'\n---\n+.*🧠 Quiz', slide_content)
        if marker_backup:
            slide_content = slide_content[:marker_backup.start()].strip()

        print(f"Processando Aula {i:02d}...")

        quiz_content = quiz_file.read_text(encoding='utf-8')
        
        questions = re.split(r'^###\s+\d+\.\s+', quiz_content, flags=re.MULTILINE)
        if len(questions) <= 1:
            questions = re.split(r'^\d+\.\s+', quiz_content, flags=re.MULTILINE)
            
        if len(questions) > 1:
            appended_text = "\n\n---\n\n<!-- .element: class=\"fragment\" -->\n# 🧠 Quiz Rápido\n## Prática de Fixação\n\n"
            
            for q_idx, q_block in enumerate(questions[1:], 1):
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
                
                # Slide da Pergunta (Sem revelar a resposta ainda)
                appended_text += f"---\n\n### ❓ Pergunta {q_idx}\n{question_title}\n\n"
                for alt in alts:
                    appended_text += f"{alt}\n"
                
                # Novo slide exclusivo para a Resposta e Feedback (Gera o dobro de frames físicos)
                appended_text += f"\n---\n\n### ✅ Resposta - Pergunta {q_idx}\n\n**A alternativa correta é:**\n\n<span style=\"color:#42affa\">{correct_alt}</span>\n\n"
                if feedback:
                    appended_text += f"*{feedback.strip()}*\n\n"
            
            # Sem padding forçado. Mantemos as lâminas de quiz limpas para fechar na conta solicitada de ~25 a ~50.
            slide_file.write_text(slide_content + appended_text, encoding='utf-8')
            
            # Recalculate slides
            final_content = slide_file.read_text(encoding='utf-8')
            slide_count = len(re.findall(r'^---$', final_content, re.MULTILINE)) + 1
            print(f"Quiz duplo anexado na Aula {i:02d} com sucesso! (Total de Slides Físicos agora: {slide_count})")

expand_slides()

import os
import re
from pathlib import Path

LESSONS_DIR = Path("docs/aulas")
SLIDES_SRC_DIR = Path("docs/slides/src")

def extract_sections(content):
    # Split content by H2 headers
    sections = re.split(r'\n## ', content)
    
    intro = sections[0]
    
    title_match = re.search(r'^# (.*?)$', intro, re.MULTILINE)
    title = title_match.group(1) if title_match else "Aula"
    
    # Extract subtitle if any (like Aula 01 - Titulo -> Aula 01 \n Titulo)
    parts = title.split(' - ', 1)
    if len(parts) == 2:
        main_title = parts[1]
        sub_title = parts[0]
    else:
        main_title = title
        sub_title = ""
        
    slides = []
    
    title_slide = f"<!-- .element: class=\"fragment\" -->\n# {main_title}"
    if sub_title:
        title_slide += f"\n## {sub_title}"
    
    title_slide += "\n\n---"
    slides.append(title_slide)

    for sec in sections[1:]:
        lines = sec.split('\n')
        sec_title = lines[0].strip()
        sec_content = '\n'.join(lines[1:]).strip()
        
        # Clean up some markdown that doesn't render well in slides
        sec_content = re.sub(r'\[:octicons-.*?\]\(.*?\)\{.*?\}', '', sec_content)
        sec_content = re.sub(r'=== ".*?"', '', sec_content)
        
        # Remover links de estilo Markdown para evitar que o MkDocs strict quebre em dois níveis de diretórios diferentes
        sec_content = re.sub(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)', r'\1', sec_content)
        
        slide_content = f"## {sec_title}\n\n"
        
        # Keep only the first few blocks to avoid overcrowded slides
        paragraphs = re.split(r'\n\n', sec_content)
        short_content = []
        for p in paragraphs:
            if not p.strip():
                continue
            short_content.append(p)
            if len(short_content) > 3: # limit to ~3-4 blocks
                break
                
        slide_content += '\n\n'.join(short_content)
        slides.append(slide_content + "\n\n---")

    # Remove the last ---
    if slides:
        slides[-1] = slides[-1][:-4]
        
    return "\n\n".join(slides)

def main():
    SLIDES_SRC_DIR.mkdir(parents=True, exist_ok=True)
    
    for i in range(1, 17):
        num = f"{i:02d}"
        lesson_file = LESSONS_DIR / f"aula-{num}.md"
        
        if not lesson_file.exists():
            continue
            
        print(f"Processing {lesson_file.name}...")
        content = lesson_file.read_text(encoding="utf-8")
        
        slide_md = extract_sections(content)
        
        final_md = f"---\ntheme: white\ntransition: convex\n---\n\n{slide_md}\n"
        
        slide_path = SLIDES_SRC_DIR / f"slide-{num}.md"
        slide_path.write_text(final_md, encoding="utf-8")
        print(f"Generated {slide_path}")

if __name__ == "__main__":
    main()

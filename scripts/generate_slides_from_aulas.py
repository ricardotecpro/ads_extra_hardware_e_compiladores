import pathlib
import re

AULAS_DIR = pathlib.Path("docs/aulas")
SLIDES_SRC_DIR = pathlib.Path("docs/slides/src")

def parse_aula_to_slides(aula_path: pathlib.Path, slide_path: pathlib.Path):
    text = aula_path.read_text(encoding='utf-8')
    
    if "## 🎯 Próximos Passos" in text:
        text = text.split("## 🎯 Próximos Passos")[0]
        
    slides = []
    slides.append("---\ntheme: white\ntransition: convex\n---")
    
    m_h1 = re.search(r'^# (.*?)$', text, re.MULTILINE)
    title = m_h1.group(1) if m_h1 else "Aula"
    slides.append(f"<!-- .element: class=\"fragment\" -->\n# {title}\n## Apresentação")
    
    if m_h1:
        text = text.replace(m_h1.group(0), "")
        
    sections = re.split(r'^(## .*)$', text, flags=re.MULTILINE)
    
    current_h2 = ""
    for sec in sections:
        if not sec.strip():
            continue
            
        if sec.startswith("## "):
            current_h2 = sec.strip()
            slides.append(f"---\n\n<!-- .element: class=\"fragment\" -->\n# Novo Tópico\n{current_h2}")
            continue
            
        # Regex to tokenize the section without breaking multi-line blocks
        # We will extract special blocks first, replace them with placeholders, split by \n\n, then restore
        blocks = []
        
        # Protect Code blocks
        code_blocks = re.findall(r'```.*?```', sec, flags=re.DOTALL)
        for i, cb in enumerate(code_blocks):
            sec = sec.replace(cb, f"__CODE_BLOCK_{i}__")
            
        # Protect DIVs
        div_blocks = re.findall(r'<div.*?>.*?</div>', sec, flags=re.DOTALL)
        for i, db in enumerate(div_blocks):
            sec = sec.replace(db, f"__DIV_BLOCK_{i}__")
            
        raw_blocks = re.split(r'\n\n+', sec.strip())
        
        current_slide_content = []
        
        def push_slide(content_list):
            if not content_list: return
            content = "\n\n".join(content_list)
            
            # Restore protected blocks
            for i, cb in enumerate(code_blocks):
                content = content.replace(f"__CODE_BLOCK_{i}__", cb)
            for i, db in enumerate(div_blocks):
                content = content.replace(f"__DIV_BLOCK_{i}__", db)
                
            slide_str = f"---\n\n{current_h2}\n\n{content}" if current_h2 else f"---\n\n{content}"
            slides.append(slide_str.strip())
            content_list.clear()

        for b in raw_blocks:
            b = b.strip()
            if not b: continue
            
            is_special = (
                "__CODE_BLOCK_" in b or 
                "__DIV_BLOCK_" in b or 
                b.startswith(">") or 
                b.startswith("===") or 
                b.startswith("### ")
            )
            
            if is_special:
                push_slide(current_slide_content)
                
                if b.startswith("==="):
                    m_tab = re.match(r'^===\s+"(.*?)"\n(.*)$', b, re.DOTALL)
                    if m_tab:
                        b = f"### {m_tab.group(1)}\n\n<span class=\"fragment\">{m_tab.group(2).strip()}</span>"
                
                push_slide([b])
            else:
                current_slide_content.append(b)
                if len(current_slide_content) >= 2 or b.startswith("-") or b.startswith("*"):
                    push_slide(current_slide_content)
                    
        push_slide(current_slide_content)

    slide_path.write_text("\n\n".join(slides), encoding='utf-8')
    return len(slides)

def main():
    SLIDES_SRC_DIR.mkdir(parents=True, exist_ok=True)
    
    for i in range(1, 17):
        aula_file = AULAS_DIR / f"aula-{i:02d}.md"
        slide_file = SLIDES_SRC_DIR / f"slide-{i:02d}.md"
        
        if aula_file.exists():
            count = parse_aula_to_slides(aula_file, slide_file)
            print(f"Aula {i:02d} processada: {count} slides gerados.")

main()

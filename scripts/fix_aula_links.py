import pathlib
import re

def fix_footer_links():
    aulas_dir = pathlib.Path('docs/aulas')
    
    if not aulas_dir.exists():
        return
        
    for i in range(1, 17):
        filepath = aulas_dir / f'aula-{i:02d}.md'
        if not filepath.exists():
            continue
            
        content = filepath.read_text(encoding='utf-8')
        
        # O problema relacional: "../slides/slide-XX.html" quebra dependendo de como o MkDocs injeta as views (e.g aulas/)
        # A solução: Transformar "../" em abs root aware paths
        
        # 1. Slides HTML
        content = re.sub(r'\]\(\.\./slides/(slide-\d+\.html)\)', r'](../slides/\1)', content)
        # Fix the actual prefix since using `../` is causing the site to prepend `/aulas/` in some permalink cases 
        # MkDocs recommends using relative to the current physical page. 
        # If the page is at /aulas/aula-01/ index, `../` takes it to `/aulas/`. So `../../quizzes/` would be theoretically required.
        # However, MkDocs navigation naturally resolves absolute-like site roots `/quizzes/` or simply relative paths accurately.
        
        # Let's standardize everything to the reliable site root absolute prefix (without hardcoding the domain)
        # Mkdocs uses `/` directly mapping to the `docs/` dir internally when rendering final htmls if use_directory_urls is true 
        # Actually, `../slides/` Should work. Let's trace why `../quizzes/` generated `aulas/quizzes/` in production:
        # It's because Mkdocs generated `aulas/aula-02/index.html`. So `../` goes up to `/aulas/`. 
        # Therefore, we need `../../quizzes/quiz-02.html` OR root absolute `/quizzes/quiz-02.html`.
        # MkDocs prefers absolute URLs mapped from `docs` as root: `/slides/...`
        
        content = re.sub(r'\]\(\.\./slides/(.*?)\)', r'](/ads_extra_hardware_e_compiladores/slides/\1)', content)
        content = re.sub(r'\]\(\.\./quizzes/(.*?)\)', r'](/ads_extra_hardware_e_compiladores/quizzes/\1)', content)
        content = re.sub(r'\]\(\.\./exercicios/(.*?)\)', r'](/ads_extra_hardware_e_compiladores/exercicios/\1)', content)
        content = re.sub(r'\]\(\.\./projetos/(.*?)\)', r'](/ads_extra_hardware_e_compiladores/projetos/\1)', content)
        
        filepath.write_text(content, encoding='utf-8')
        print(f"URLs Absolutas de Produção corrigidos em: {filepath.name}")

fix_footer_links()

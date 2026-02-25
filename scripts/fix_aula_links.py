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
        
        # O problema relacional 2.0: Root Paths (ex: /ads_extra_hardware_e_compiladores/quizzes/...html) parecem não estar batendo
        # e o MkDocs exige que os links de navegação para as outras páginas .md usem extensões .md relativas puras,
        # senão o sistema de warning quebra e o roteamento interno (pjax/SPA) não acopla.
        
        # Para Slides: Eles de fato não são parseados para mkdocs, e sim HTML estáticos RevealJS puros na raiz do site.
        content = re.sub(r'\]\(/ads_extra_hardware_e_compiladores/slides/(.*?)\)', r'](../slides/\1)', content)
        
        # Para Quizzes / Exercicios / Projetos: Devem apontar para o .md relativo ascendente.
        # Ex: quizzes/quiz-16.html --> ../quizzes/quiz-16.md
        # O Mkdocs resolverá ../quizzes/quiz-16.md magicamente para a tag <a href="..../quizzes/quiz-16/"> no frontend.
        
        content = re.sub(r'\]\(/ads_extra_hardware_e_compiladores/quizzes/(.*?)\.html\)', r'](../quizzes/\1.md)', content)
        content = re.sub(r'\]\(/ads_extra_hardware_e_compiladores/exercicios/(.*?)\)', r'](../exercicios/\1)', content)
        content = re.sub(r'\]\(/ads_extra_hardware_e_compiladores/projetos/(.*?)\)', r'](../projetos/\1)', content)
        
        filepath.write_text(content, encoding='utf-8')
        print(f"URLs Relativas Nativas do MkDocs fixadas em: {filepath.name}")

fix_footer_links()

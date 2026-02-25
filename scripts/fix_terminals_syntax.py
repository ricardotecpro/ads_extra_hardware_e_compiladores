import pathlib
import re

def fix_all_termynals():
    aulas_dir = pathlib.Path('docs/aulas')
    count = 0
    
    for filepath in aulas_dir.glob('aula-*.md'):
        content = filepath.read_text(encoding='utf-8')
        
        # O problema:
        # <div class="termy" markdown="1">
        # ```console
        # ...
        # ```
        # </div>
        
        # O padrão exigido pelo mkdocs-termynal do python:
        # <!-- termynal -->
        # ```console
        # ...
        # ```
        
        # Padrão capturador exato para trocar o wrapper div inteiro 
        # (incluindo possíveis quebras de linha/espaços em branco) por <!-- termynal -->
        
        # Use a non-greedy regex that matches the wrapper div around code blocks
        pattern = re.compile(r'<div class="termy"[^>]*>\s*(```.*?```)\s*</div>', flags=re.DOTALL)
        
        new_content, num_subs = pattern.subn(r'<!-- termynal -->\n\1', content)
        
        if num_subs > 0:
            filepath.write_text(new_content, encoding='utf-8')
            count += num_subs
            print(f"Modificado {filepath.name}: {num_subs} blocos corrigidos.")
            
    print(f"Total de terminais corrigidos: {count}")

fix_all_termynals()

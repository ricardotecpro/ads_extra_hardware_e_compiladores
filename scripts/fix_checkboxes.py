import pathlib
import re

def normalize_tasklists_for_mkdocs():
    projetos_dir = pathlib.Path('docs/projetos')
    
    if not projetos_dir.exists():
        return
        
    for filepath in projetos_dir.glob('*.md'):
        content = filepath.read_text(encoding='utf-8')
        lines = content.split('\n')
        new_lines = []
        
        modified = False
        for line in lines:
            # Detectar linhas que comecam com [ ] ou [x] mas sem o hifen de lista do markdown antes
            if re.match(r'^\[[ xX]\]\s+', line):
                line = "- " + line
                modified = True
            new_lines.append(line)
            
        if modified:
            filepath.write_text('\n'.join(new_lines), encoding='utf-8')
            print(f"Checkboxes normalizados com sucesso para o MkDocs em: {filepath.name}")

normalize_tasklists_for_mkdocs()

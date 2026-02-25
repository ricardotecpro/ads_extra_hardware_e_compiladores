import pathlib
import re

def refactor_exercicio(content):
    # Split by exactly '## Questão '
    parts = re.split(r'^## Questão ', content, flags=re.MULTILINE)
    if len(parts) == 1:
        return content
        
    header = parts[0]
    blocks = parts[1:]
    
    new_content = header
    
    for block in blocks:
        # block contains the rest of the question title until the next '## Questão ' or '---' at the end
        lines = block.split('\n')
        title = lines[0].strip()
        body_lines = lines[1:]
        
        new_content += f'!!! question "{title}"\n'
        
        for line in body_lines:
            if line.startswith('[:octicons') or line.strip() == '---':
                # Reached footer
                new_content += line + '\n'
            else:
                new_content += '    ' + line if line.strip() else ''
                new_content += '\n'
                
    # Fix nested tags if any
    return new_content.replace('    ---', '') # Remove horizontal lines inside admonitions

def refactor_solucao(content):
    parts = re.split(r'^## Solução da ', content, flags=re.MULTILINE)
    if len(parts) == 1:
        return content
        
    header = parts[0]
    blocks = parts[1:]
    
    new_content = header
    
    for block in blocks:
        lines = block.split('\n')
        title = lines[0].strip()
        body_lines = lines[1:]
        
        new_content += f'!!! success "Solução da {title}"\n'
        
        for line in body_lines:
            if line.startswith('[:octicons') or line.strip() == '---' and 'Voltar' in '\n'.join(body_lines[-3:]):
                # Probably footer
                new_content += line + '\n'
            else:
                # Nest infos correctly
                if line.startswith('!!! info'):
                    new_content += '    ' + line + '\n'
                elif line.startswith('    '):
                    new_content += '        ' + line.strip() + '\n'
                else:
                    new_content += '    ' + line if line.strip() else ''
                    new_content += '\n'
                    
    # Clean up ---
    new_content = new_content.replace('    ---', '')
    return new_content

def process_all():
    base_dir = pathlib.Path('docs/exercicios')
    count = 0
    for md_file in base_dir.glob('exercicio-*.md'):
        content = md_file.read_text(encoding='utf-8')
        new_content = refactor_exercicio(content)
        md_file.write_text(new_content, encoding='utf-8')
        count += 1
        
    for md_file in base_dir.glob('solucao-*.md'):
        content = md_file.read_text(encoding='utf-8')
        new_content = refactor_solucao(content)
        md_file.write_text(new_content, encoding='utf-8')
        count += 1
        
    print(f"Refatorados {count} arquivos.")

if __name__ == '__main__':
    process_all()

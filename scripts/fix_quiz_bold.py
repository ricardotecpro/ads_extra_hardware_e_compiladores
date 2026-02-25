import pathlib
import re

def fix_bold_in_quizzes():
    dirs_to_clean = [
        pathlib.Path('docs/quizzes'),
        pathlib.Path('docs/quizzes/src'),
        pathlib.Path('docs/exercicios')
    ]
    
    for d in dirs_to_clean:
        if not d.exists():
            continue
            
        for filepath in d.glob('*.md'):
            content = filepath.read_text(encoding='utf-8')
            
            lines = content.split('\n')
            new_lines = []
            
            modified = False
            for line in lines:
                # Regras para corrigir as strings dependendo se está no .src/, na raiz /quizzes/ ou /exercicios/
                
                # Caso 1: Na div do HTML (quizzes compilados)
                if '<div class="quiz-question">' in line and '**' in line:
                    line = line.replace('**', '')
                    modified = True
                    
                # Caso 2: Em Markdown puro começando com número (quiz src)
                elif re.match(r'^\d+\.\s+.*?\*\*.*?\*\*.*$', line):
                    # Remove todos os pares de negrito na linha da pergunta
                    line = line.replace('**', '')
                    modified = True
                
                # Caso 3: Exercícios (Linha começando com **Pergunta:** ...)
                elif line.startswith('**Pergunta:** ') and line.count('**') > 2:
                    # Manter só o Pergunta:** em negrito, limpando o lixo do meio do texto
                    line = line.replace('**Pergunta:** ', '___PERG_PLACEHOLDER___')
                    line = line.replace('**', '')
                    line = line.replace('___PERG_PLACEHOLDER___', '**Pergunta:** ')
                    modified = True
                    
                new_lines.append(line)
                
            if modified:
                filepath.write_text('\n'.join(new_lines), encoding='utf-8')
                print(f"Limpo literais de negrito defeituosos em: {filepath.name}")

fix_bold_in_quizzes()

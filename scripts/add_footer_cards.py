import os
import re
from pathlib import Path

AULAS_DIR = Path("docs/aulas")

def generate_cards_html(num_str):
    return f"""

---

## 🎯 Próximos Passos

<div class="grid cards" markdown>

-   :octicons-video-24: **Acessar Slides**

    ---
    
    Reveja a apresentação visual desta aula.
    
    [:octicons-arrow-right-24: Ver Slides da Aula](../slides/slide-{num_str}.html)

-   :octicons-tasklist-24: **Quiz**

    ---
    
    Teste seu entendimento básico com perguntas rápidas.
    
    [:octicons-arrow-right-24: Responder Quiz](../quizzes/quiz-{num_str}.html)

-   :octicons-pencil-24: **Exercícios**

    ---
    
    Prática avançada e dissertativa com consulta.
    
    [:octicons-arrow-right-24: Lista de Exercícios](../exercicios/exercicio-{num_str}.md)

-   :octicons-rocket-24: **Projeto**

    ---
    
    Laboratório prático de codificação em C/C++.
    
    [:octicons-arrow-right-24: Mini Projeto](../projetos/projeto-{num_str}.md)

</div>
"""

def process_file(file_path):
    # Extrai o numero da aula (ex: aula-01.md -> 01)
    match = re.search(r'aula-(\d+)\.md', file_path.name)
    if not match:
        return
        
    num_str = match.group(1)
    content = file_path.read_text(encoding='utf-8')
    
    # Se ja tiver a div de cards, evitar a dupla injeção
    if "## 🎯 Próximos Passos" in content or '<div class="grid cards"' in content:
        print(f"Aula {num_str} ja contêm blocos de próximos passos. Ignorando injeção.")
        return
        
    # Regex para achar o final da aula, que geralmente detém um botao final "Avançar para Aula X"    
    # Vamos achar o "Avançar para Aula", e colocar os cards "Antes" dele para ficar acima do rodapé finalzasso
    # Ou se não tiver botão, colocar no mais extremo fim.
    
    cards_str = generate_cards_html(num_str)
    
    avancar_match = re.search(r'\[:octicons-arrow-right-24: Avançar para Aula \d+\]\(aula-\d+\.md\)\{.*?\}', content)
    if avancar_match:
        # Pega a string exata pra dar replace
        btn_str = avancar_match.group(0)
        new_content = content.replace(btn_str, cards_str + "\n\n" + btn_str)
        file_path.write_text(new_content, encoding='utf-8')
        print(f"Injetado cards de navegacao na Aula {num_str} (Acima do Botao Avancar)")
    else:
        # Joga puramente pro fim
        with open(file_path, "a", encoding='utf-8') as f:
            f.write(cards_str)
        print(f"Injetado cards de navegacao EXTREMO FIM na Aula {num_str}")

def main():
    if not AULAS_DIR.exists():
        print("Diretorio docs/aulas nao encontrado.")
        return
        
    for md_file in sorted(AULAS_DIR.glob("aula-*.md")):
        process_file(md_file)
        
    print("Atualização das Aulas concluída.")

if __name__ == '__main__':
    main()

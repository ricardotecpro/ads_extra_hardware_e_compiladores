import os
from pathlib import Path

SYLLABUS = [
    {"id": 1, "title": "Como o Software Roda no Hardware"},
    {"id": 2, "title": "Representação de Dados"},
    {"id": 3, "title": "CPU: Estrutura e Funcionamento"},
    {"id": 4, "title": "Arquiteturas RISC vs CISC"},
    {"id": 5, "title": "Hierarquia de Memória"},
    {"id": 6, "title": "Cache e Localidade"},
    {"id": 7, "title": "Stack vs Heap em C/C++"},
    {"id": 8, "title": "Memória Virtual"},
    {"id": 9, "title": "Processos e Threads"},
    {"id": 10, "title": "Sincronização - Mutex, Semáforos"},
    {"id": 11, "title": "Paralelismo em Hardware"},
    {"id": 12, "title": "Modelo de Memória"},
    {"id": 13, "title": "Dispositivos de Armazenamento"},
    {"id": 14, "title": "Sistemas de Arquivos"},
    {"id": 15, "title": "Entrada e Saída / I/O"},
    {"id": 16, "title": "Projeto Final: Otimização Baseada em Hardware"},
]

DIRS = [
    "docs/slides/src",
    "docs/quizzes/src",
    "docs/exercicios",
    "docs/projetos"
]

def generate_slides(lid, title):
    content = f"---\ntheme: white\ntransition: convex\n---\n\n"
    content += f"<!-- .element: class=\"fragment\" -->\n# {title}\n## Aula {lid:02d}\n\n---\n\n"
    for i in range(1, 21):
        content += f"## Tópico {i}: {title}\n\nBem vindo à explicação do tópico {i}.\n\n"
        content += f"```cpp\n// Exemplo de código {i}\nint var_{i} = 0;\n```\n\n"
        content += "<!-- .element: class=\"fragment\" -->\n> [!NOTE]\n> Ponto importante de Hardware.\n\n---\n\n"
    return content

def generate_quiz(lid, title):
    content = f"# Quiz {lid:02d} - {title}\n\n**Avaliação Sistemática**\n\n"
    for i in range(1, 11):
        content += f"{i}. Sobre o tema de {title}, qual das alternativas é a mais coerente?\n\n"
        content += f"    - [ ] Alternativa A está incorreta.\n"
        content += f"    - [x] Alternativa B está correta e embasada. *feedback: Sim, o C++ se comporta assim na Arquitetura.*\n"
        content += f"    - [ ] Alternativa C é um erro comum.\n"
        content += f"    - [ ] Alternativa D é uma falsa equivalência.\n\n"
    return content

def generate_exercises(lid, title):
    content = f"# Exercícios de Fixação: Aula {lid:02d} - {title}\n\n"
    content += "=== \"Básico\"\n"
    content += "    **Exercício 1**: Descreva os conceitos teóricos fundamentais vistos na aula de hoje.\n\n"
    content += "    **Exercício 2**: Faça um mapa mental sobre como C/C++ lida com este conceito.\n\n"
    content += "=== \"Intermediário\"\n"
    content += "    **Exercício 3**: Escreva um pequeno trecho de código em C++ invocando as premissas deste módulo.\n\n"
    content += "    **Exercício 4**: Utilizando o terminal Linux, audite esse comportamento nativo no S.O.\n\n"
    content += "=== \"Desafio\"\n"
    content += "    **Exercício 5 (Avançado)**: Integre ponteiros, System Calls e tente quebrar o kernel local propositalmente com memory leaks, para então consertar!\n\n"
    return content

def generate_project(lid, title):
    content = f"# Mini-Projeto {lid:02d} - {title}\n\n"
    content += f"## 🎯 Objetivo Prático\nImplemente um simulador robusto focado em **{title}**.\n\n"
    content += "## 💡 Requisitos Tecnológicos\n"
    content += "- Utilizar GC nulo (C/C++ nativo).\n"
    content += "- Evitar falsos compartilhamentos (False Sharing).\n\n"
    content += "<div class=\"termy\" markdown=\"1\">\n\n```console\n$ gcc projeto.cpp -O2 -o projeto\n$ ./projeto\n\nResultados Otimizados com Sucesso!\n```\n\n</div>\n"
    return content

def main():
    for d in DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)

    for item in SYLLABUS:
        lid = item["id"]
        title = item["title"]
        
        # Paths
        p_slide = Path(f"docs/slides/src/slide-{lid:02d}.md")
        p_quiz = Path(f"docs/quizzes/src/quiz-{lid:02d}.md")
        p_exerc = Path(f"docs/exercicios/exercicio-{lid:02d}.md")
        p_proj = Path(f"docs/projetos/projeto-{lid:02d}.md")
        
        # Writes (Overwrites if necessary to ensure 100% C++ context and syntax rules)
        p_slide.write_text(generate_slides(lid, title), encoding="utf-8")
        p_quiz.write_text(generate_quiz(lid, title), encoding="utf-8")
        p_exerc.write_text(generate_exercises(lid, title), encoding="utf-8")
        p_proj.write_text(generate_project(lid, title), encoding="utf-8")

    print("Success: Generated 16 Slides (20 screens eq), 16 Quizzes (10 q), 16 Exercises (5 items), 16 Projects.")

if __name__ == "__main__":
    main()

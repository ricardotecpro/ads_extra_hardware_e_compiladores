import os
import re
from pathlib import Path

LESSONS_DIR = Path("docs/aulas")
EXERCISES_DIR = Path("docs/exercicios")
PROJECTS_DIR = Path("docs/projetos")
QUIZZES_SRC_DIR = Path("docs/quizzes/src")

def clean_text(text):
    text = re.sub(r'\[:octicons-.*?\]\(.*?\)\{.*?\}', '', text)
    text = re.sub(r'=== ".*?"', '', text)
    text = re.sub(r'> \[\!.*?\]', '', text)
    text = re.sub(r'<div.*?>', '', text)
    text = re.sub(r'</div>', '', text)
    return text.strip()

def get_lesson_data(content):
    title_match = re.search(r'^# (.*?)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Aula"

    # Encontrar subtópicos H2
    sections = re.split(r'\n## ', content)
    topics = []
    
    for sec in sections[1:]:
        lines = sec.split('\n')
        if not lines: continue
        sec_title = lines[0].strip()
        sec_title_clean = re.sub(r'^[\d\. ]*?(.*)$', r'\1', re.sub(r'^[^\w\s]*\s*', '', sec_title)).strip()
        if not sec_title_clean:
            sec_title_clean = "Assunto Principal"
            
        # Obter os parágrafos de texto puro (ignorar código, tabelas, etc)
        paragraphs = []
        in_code_block = False
        for line in lines[1:]:
            line_stripped = line.strip()
            if line_stripped.startswith('```'):
                in_code_block = not in_code_block
                continue
            if in_code_block or line_stripped.startswith('*') or line_stripped.startswith('>'):
                continue
            if line_stripped:
                paragraphs.append(clean_text(line))
        
        context_full = '\n\n'.join(paragraphs) if paragraphs else "Conceito abordado na aula."
        context_short = paragraphs[0] if paragraphs else "Conceito abordado na aula."
        topics.append({
            'title': sec_title,
            'clean_title': sec_title_clean,
            'context_full': context_full,
            'context_short': context_short
        })
        
    return title, topics

def generate_exercise_and_solution(num_str, title, topics):
    ex_path = EXERCISES_DIR / f"exercicio-{num_str}.md"
    sol_path = EXERCISES_DIR / f"solucao-{num_str}.md"
    
    ex_content = f"# Exercícios: {title}\n\nResolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula {num_str}**.\n\n"
    sol_content = f"# Solução e Explicação Detalhada: {title}\n\nAbaixo estão as respostas esperadas e o embasamento teórico para os exercícios propostos na **Aula {num_str}**.\n\n"
    
    for i, t in enumerate(topics, 1):
        ex_content += f"## Questão {i} - {t['clean_title']}\n"
        ex_content += f"**Contexto:** {t['context_short']}\n\n"
        ex_content += f"**Pergunta:** Com base nos conceitos discutidos na aula sobre **{t['clean_title']}**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.\n\n"
        
        sol_content += f"## Solução da Questão {i} - {t['clean_title']}\n"
        sol_content += f"**Explicação Detalhada do Assunto:**\n\n{t['context_full']}\n\n"
        sol_content += f"> **Expectativa de Resposta do Aluno:** O aluno deve compreender a mecânica exata detalhada no texto acima. A resposta deve transparecer o entendimento arquitetural de que *{t['clean_title']}* não é apenas uma teoria, mas impacta diretamente a compilação, performance e os sinais elétricos controlados pelo código.\n\n"
        
    ex_content += f"\n---\n\n[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-{num_str}.md){{ .md-button .md-button--primary }}\n"
    sol_content += f"\n---\n\n[:octicons-arrow-left-24: Voltar para Exercício](exercicio-{num_str}.md){{ .md-button }}\n"
    
    ex_path.write_text(ex_content, encoding='utf-8')
    sol_path.write_text(sol_content, encoding='utf-8')

def generate_project(num_str, title, topics):
    proj_path = PROJECTS_DIR / f"projeto-{num_str}.md"
    
    content = f"# Projeto: {title}\n\n"
    if topics:
        core_topic = topics[0]
        content += f"## Desafio Prático\n"
        content += f"O objetivo deste projeto é desenvolver ou analisar uma pequena aplicação em C/C++ que comprove na prática os conceitos ensinados na Aula {num_str}, com ênfase em **{core_topic['clean_title']}**.\n\n"
        content += f"**Contexto Teórico Extraído da Aula:**\n\n> {core_topic['context_short']}\n\n"
        
    content += "## Tarefas do Projeto (Implementação/Verificação)\n"
    for i, t in enumerate(topics, 1):
        content += f"- [ ] **Módulo de {t['clean_title']}**: Demonstrar estruturalmente ou em código a afirmação de que _{t['context_short'][:80]}..._\n"
        
    content += "\n## Critérios de Qualidade e Avaliação\n"
    content += "- O código executa de maneira segura, com gestão correta de memória.\n- A modelagem está aderente aos conceitos explicados no material teórico (não apenas funciona superficialmente).\n"
    
    proj_path.write_text(content, encoding='utf-8')

def generate_quiz(num_str, title, topics):
    quiz_path = QUIZZES_SRC_DIR / f"quiz-{num_str}.md"
    
    content = f"# Quiz {num_str} - {title}\n\n**Avaliação Sistemática**\n\n"
    
    for i, t in enumerate(topics, 1):
        # Truncar short_context de forma limpa para não bugar o parser de opções de markdown
        short_context = t['context_short'][:180].replace('\n', ' ') + "..." if len(t['context_short']) > 180 else t['context_short'].replace('\n', ' ')
        
        content += f"{i}. Segundo a aula {num_str}, ao abordarmos o tópico de **{t['clean_title']}**, qual a premissa tecnológica subjacente a este conceito?\n\n"
        content += f"    - [x] {short_context} *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*\n"
        content += f"    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.\n"
        content += f"    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.\n"
        content += f"    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.\n\n"
        
    quiz_path.write_text(content, encoding='utf-8')

def main():
    EXERCISES_DIR.mkdir(parents=True, exist_ok=True)
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    QUIZZES_SRC_DIR.mkdir(parents=True, exist_ok=True)
    
    for i in range(1, 17):
        num_str = f"{i:02d}"
        lesson_file = LESSONS_DIR / f"aula-{num_str}.md"
        if not lesson_file.exists(): continue
        
        print(f"Processando Aula {num_str}...")
        text = lesson_file.read_text(encoding='utf-8')
        title, topics = get_lesson_data(text)
        
        generate_exercise_and_solution(num_str, title, topics)
        generate_project(num_str, title, topics)
        generate_quiz(num_str, title, topics)
        
    print("Sucesso! Materiais regenerados para refletirem o conteúdo.")

if __name__ == '__main__':
    main()

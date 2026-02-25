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

    sections = re.split(r'\n## ', content)
    topics = []
    
    for sec in sections[1:]:
        lines = sec.split('\n')
        if not lines: continue
        sec_title = lines[0].strip()
        sec_title_clean = re.sub(r'^[\d\. ]*?(.*)$', r'\1', re.sub(r'^[^\w\s]*\s*', '', sec_title)).strip()
        if not sec_title_clean:
            sec_title_clean = "Assunto Principal"
            
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
    
    # Padrão: 5 exercícios (2 básicos, 2 intermediários, 1 desafio)
    difficulties = ["Básico 1", "Básico 2", "Intermediário 1", "Intermediário 2", "Desafio"]
    
    for i in range(5):
        t = topics[i % len(topics)] if topics else {'clean_title': 'Conceito Geral', 'context_short': 'Geral', 'context_full': 'Explicação geral.'}
        diff = difficulties[i]
        
        ex_content += f"## Questão {i+1} - {t['clean_title']} ({diff})\n"
        ex_content += f"**Contexto:** \n\n> {t['context_short']}\n\n"
        if diff.startswith("Básico"):
            ex_content += f"**Pergunta:** Descreva o conceito fundamental de **{t['clean_title']}** e liste duas vantagens de seu uso.\n\n"
        elif diff.startswith("Intermediário"):
            ex_content += f"**Pergunta:** Analisando o funcionamento de **{t['clean_title']}**, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?\n\n"
        else:
            ex_content += f"**Pergunta (Desafio):** Elabore um cenário de arquitetura onde o uso incorreto ou a falta de entendimento de **{t['clean_title']}** cause um problema grave de performance ou vazamento de memória. Como você mitigaria estruturalmente esse gargalo?\n\n"
        
        sol_content += f"## Solução da Questão {i+1} - {t['clean_title']} ({diff})\n"
        sol_content += f"**Explicação Detalhada do Assunto:**\n\n{t['context_full']}\n\n"
        sol_content += f"!!! info \"Expectativa de Resposta\"\n    O aluno deve inferir com clareza que o conceito de *{t['clean_title']}* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.\n\n"
        
    ex_content += f"\n---\n\n[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-{num_str}.md){{ .md-button .md-button--primary }}\n"
    sol_content += f"\n---\n\n[:octicons-arrow-left-24: Voltar para Exercício](exercicio-{num_str}.md){{ .md-button }}\n"
    
    ex_path.write_text(ex_content, encoding='utf-8')
    sol_path.write_text(sol_content, encoding='utf-8')

def generate_project(num_str, title, topics):
    proj_path = PROJECTS_DIR / f"projeto-{num_str}.md"
    
    content = f"# Projeto {num_str}: {title}\n\n"
    
    content += f"## 🚀 Laboratório Prático: **{title}**\n\n"
    content += f"Construa uma simulação lógica ou um roteiro analítico em linguagem C/C++ focado no fenômeno real ocorrido no Hardware baseando-se em:\n\n"
    for t in topics[:3]:
        content += f"> {t['context_short'][:200]}...\n\n"
        
    content += "### Tarefas do Projeto\n"
    content += "- [ ] **Setup Inicial**: Alocar perfeitamente os arquivos como `main.cpp` em sua IDE configurando compilador GCC/Clang.\n"
    for i, t in enumerate(topics[:3], 1):
        content += f"- [ ] **Módulo {i}**: Implementar, prototipar ou demonstrar funcionalmente _{t['clean_title']}_ no código.\n"
    content += "- [ ] **Validação E Benchmark**: Fazer o build via terminal e testar limites de velocidade analiticamente comparando o log de transição.\n\n"
        
    content += "### 🏆 Critérios de Qualidade (Review)\n"
    content += "1. Compila estritamente sem nenhum warning de memory loss ou fallback.\n2. Adere e representa fielmente 100% à teoria aprendida do Markdown da Aula correspondente.\n3. Estruturação modular limpa para fácil manutenção.\n"
    
    proj_path.write_text(content, encoding='utf-8')

def generate_quiz(num_str, title, topics):
    quiz_path = QUIZZES_SRC_DIR / f"quiz-{num_str}.md"
    
    content = f"# Quiz {num_str} - {title}\n\n**Bateria Sistemática (10 Questões)**\n\n"
    
    angles = ["Sobre o funcionamento prático de", "No contexto analítico de", "Ao avaliar a característica inerente a", "A respeito da arquitetura sistêmica conectada a", "No que tange diretamente a lógica de"]
    
    for i in range(10):
        t = topics[i % len(topics)] if topics else {'clean_title': 'Conceito', 'context_short': 'Contexto curto'}
        short_context = t['context_short'][:220].replace('\n', ' ') + "..." if len(t['context_short']) > 220 else t['context_short'].replace('\n', ' ')
        angle = angles[i % len(angles)]
        
        content += f"{i+1}. {angle} **{t['clean_title']}** explicado em sala, indique a afirmativa verdadeira:\n\n"
        content += f"    - [x] {short_context} *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*\n"
        content += f"    - [ ] É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.\n"
        content += f"    - [ ] Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.\n"
        content += f"    - [ ] A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.\n\n"
        
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
        
    print("Sucesso! Materiais profundos processados gerando 5 Exercícios e 10 Quizzes por Aula.")

if __name__ == '__main__':
    main()

import os

M1 = [
    ("01", "Como o Software Roda no Hardware"),
    ("02", "Representação de Dados"),
    ("03", "CPU: Estrutura e Funcionamento"),
    ("04", "Arquiteturas RISC vs CISC")
]
M2 = [
    ("05", "Hierarquia de Memória"),
    ("06", "Cache e Localidade"),
    ("07", "Stack vs Heap"),
    ("08", "Memória Virtual")
]
M3 = [
    ("09", "Processos e Threads"),
    ("10", "Sincronização e Concorrência"),
    ("11", "Paralelismo no Hardware"),
    ("12", "O Modelo de Memória")
]
M4 = [
    ("13", "Dispositivos de Armazenamento"),
    ("14", "Sistemas de Arquivos"),
    ("15", "Entrada e Saída (I/O)"),
    ("16", "Projeto Final: Otimização Baseada em Hardware")
]

MODULES = [
    ("Módulo 1: Fundamentos de Arquitetura de Computadores", M1),
    ("Módulo 2: Memória e Performance", M2),
    ("Módulo 3: Concorrência e Paralelismo", M3),
    ("Módulo 4: Armazenamento, I/O e Prática", M4)
]

def write_index(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

def generate_aulas_index():
    c = "# Aulas do Curso\n\nBem-vindo à seção de aulas! Aqui você encontra todo o conteúdo do curso organizado por módulos.\n\n## 📚 Módulos do Curso\n\n<div class=\"grid cards\" markdown>\n\n"
    for i, (mod_name, aulas) in enumerate(MODULES, 1):
        c += f"-   :material-numeric-{i}-box: **{mod_name}**\n    ---\n"
        for num, title in aulas:
            c += f"    - [Aula {num} - {title}](aula-{num}.md)\n"
        c += "\n"
    c += "</div>"
    write_index("docs/aulas/index.md", c)

def generate_generic_index(folder, title, desc, link_prefix, link_ext, item_prefix, file_prefix):
    c = f"# {title}\n\n{desc}\n\n"
    for mod_name, aulas in MODULES:
        c += f"## {mod_name.replace(':', ' –')}\n"
        for num, aula_title in aulas:
            c += f"- [:octicons-arrow-right-24: {item_prefix} {num} - {aula_title}]({link_prefix}{file_prefix}-{num}.{link_ext})\n"
        c += "\n"
    write_index(f"docs/{folder}/index.md", c)

def generate_root_index():
    c = """# 🎓 Curso: Hardware para Programadores (C/C++)

> "Não basta o código compilar; é preciso entender como o silício e os elétrons o executam na prática."

Bem-vindo à sua jornada no coração da tecnologia. Este curso foi projetado para capacitar desenvolvedores a compreender como o hardware influencia performance, paralelismo, uso de memória e eficiência em software, com ênfase prática em C/C++.

---

## ⚡ Atalhos Rápidos

<div class="grid cards" markdown>

-   :material-book-open-page-variant: **Trilha de Aulas**
    ---
    16 lições modernas englobando arquitetura, CPU, memória e I/O.
    [:octicons-arrow-right-24: Iniciar Jornada](aulas/index.md)

-   :material-presentation: **Slides Interativos**
    ---
    Material visual otimizado com transições e suporte Reveal.js.
    [:octicons-arrow-right-24: Ver Slides](slides/index.md)

-   :material-school: **Quizzes e Prática**
    ---
    Avalie seu progresso com 160 questões técnicas exclusivas.
    [:octicons-arrow-right-24: Testar Conhecimento](quizzes/index.md)

-   :material-rocket: **Laboratórios e Projetos**
    ---
    Aplique conceitos de baixo nível em C/C++.
    [:octicons-arrow-right-24: Ver Projetos](projetos/index.md)

-   :material-dumbbell: **Exercícios Progressivos**
    ---
    Das questões conceituais ao desafio prático de código.
    [:octicons-arrow-right-24: Praticar Agora](exercicios/index.md)

-   :material-cog: **Setup e Ferramentas**
    ---
    Configurações essenciais para ecossistema C/C++ (GCC/G++).
    [:octicons-arrow-right-24: Configurar](setups/index.md)

</div>

---

## 🗺️ Mapa da Jornada (Módulos)

O curso está estruturado em **4 Módulos** cruciais para desenvolvedores backend/sistemas:

### 📦 Módulo 1: Fundamentos de Arquitetura de Computadores
*Como transformar instruções lógicas em pulso elétrico.*
- **Aulas 01 a 04**: Software x Hardware, Representação de Dados, Estrutura de CPU e RISC vs CISC.

### 📐 Módulo 2: Memória e Performance
*A anatomia do estado: velocidade versus capacidade.*
- **Aulas 05 a 08**: Hierarquia de Memória, Cache e Localidade, Stack vs Heap, e Memória Virtual.

### 🧠 Módulo 3: Concorrência e Paralelismo
*Vencendo as limitações do chip único.*
- **Aulas 09 a 12**: Processos e Threads, Sincronização, Paralelismo no Hardware e Modelo de Memória.

### 💻 Módulo 4: Armazenamento, I/O e Prática
*Onde a velocidade despenca e integrando todos os conceitos.*
- **Aulas 13 a 16**: Dispositivos de Armazenamento, Sistemas de Arquivos, I/O e Projeto Final Analítico.

---

## 💡 Dicas de Sucesso

1. **Entenda os Ponteiros**: No Módulo 2, faremos intenso uso do entendimento de Heap e Call Stack.
2. **Observe o Compilador**: Use o Terminal e veja suas saídas; entenda como o código compila nativamente.
3. **Diagramas são o Guia**: Utilize as tabelas verdade e fluxogramas para visualizar as decisões arquiteturais.

**Pronto para entender o Hardware?** [:material-rocket: Ir para Aula 01](aulas/aula-01.md){ .md-button .md-button--primary }
"""
    write_index("docs/index.md", c)

def generate_setups_index():
    c = """# Configuração do Ambiente

Bem-vindo à seção de configuração! Prepare seu ambiente para acompanhar as aulas de Hardware para Programadores focando na linguagem C e C++.

<div class="grid cards" markdown>

-   :material-microsoft-windows: **Configuração no Windows**
    
    - [Setup C/C++ (MSYS2)](setup-01.md)
    - Download dos Compiladores GCC/G++ em ambiente MSYS2
    - Instalação e Extensões no Visual Studio Code (C/C++ e Code Runner)

-   :material-linux: **Configuração no Linux**
    
    - [Setup C/C++ (build-essential)](setup-02.md)
    - Configurações com Aptitude usando pacotes base `build-essential` e `gdb`
    - Adicionando de forma nativa no VS Code

</div>

## 📋 Próximos Passos

Após configurar seu ambiente:

1. ✅ **Comprove o Compilador**: Teste a saída de comando do `g++ --version` ou `gcc --version`.
2. 📚 **Instale as extensões obrigatórias**: Adicione as bibliotecas do C/C++ da Microsoft em sua IDE conforme listado nos *setups*.
3. 🚀 **Comece a aventura**: [Mergulhe na Aula 01](../aulas/aula-01.md)
"""
    write_index("docs/setups/index.md", c)

if __name__ == "__main__":
    generate_aulas_index()
    generate_generic_index("exercicios", "Listas de Exercícios Práticos", "Cada sessão de atividades progressivas envolve as dinâmicas mais comuns em arquitetura de baixo nível C/C++.", "", "md", "Prática", "exercicio")
    generate_generic_index("projetos", "Laboratórios de Projetos", "Coloque em prática seu aprendizado de Hardware implementando ferramentas reais com C/C++.", "", "md", "Lab", "projeto")
    generate_generic_index("quizzes", "Quizzes Interativos", "Teste os seus conhecimentos adquiridos durantes as explorações teóricas.", "", "md", "Quiz", "quiz")
    generate_generic_index("slides", "Slides Interativos", "Nesta seção você acessa os slides completos de cada uma das 16 aulas do Curso. As apresentações foram desenhadas com visual otimizado Reveal.js.\n\nPara utilizar as transições (como as setas do teclado) em tela-cheia, pressione a tecla `F`.", "", "html", "Aula", "slide")
    generate_root_index()
    generate_setups_index()
    print("All index files rewritten successfully.")

# Projeto 12: Aula 12 - O Modelo de Memória

## 🚀 Laboratório Prático: **Aula 12 - O Modelo de Memória**

Construa uma simulação lógica ou um roteiro analítico em linguagem C/C++ focado no fenômeno real ocorrido no Hardware baseando-se em:

> Você codifica:...

> O C++11 emitiu formalmente o seu universal **Memory Model** definindo através da biblioteca `std::atomic` o que o Hardware tem permições para *Adiantar* vs *Trancar*....

> Se não tivessemos essa lei `std::atomic` no standard oficial do GCC, programávamos via "Gambiarra Intrinseca" de Processador (Ex: Comando Assembler **MFENCE** ou **SFENCE** no Intel). Os Fences proíbe...

### Tarefas do Projeto
- [ ] **Setup Inicial**: Alocar perfeitamente os arquivos como `main.cpp` em sua IDE configurando compilador GCC/Clang.
- [ ] **Módulo 1**: Implementar, prototipar ou demonstrar funcionalmente _1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)_ no código.
- [ ] **Módulo 2**: Implementar, prototipar ou demonstrar funcionalmente _2. O Memory Model (Consistências e Barreiras)_ no código.
- [ ] **Módulo 3**: Implementar, prototipar ou demonstrar funcionalmente _3. Memory Barriers (Fences) nas CPUs_ no código.
- [ ] **Validação E Benchmark**: Fazer o build via terminal e testar limites de velocidade analiticamente comparando o log de transição.

### 🏆 Critérios de Qualidade (Review)
1. Compila estritamente sem nenhum warning de memory loss ou fallback.
2. Adere e representa fielmente 100% à teoria aprendida do Markdown da Aula correspondente.
3. Estruturação modular limpa para fácil manutenção.

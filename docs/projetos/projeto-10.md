# Projeto 10: Aula 10 - Sincronização e Concorrência

## 🚀 Laboratório Prático: **Aula 10 - Sincronização e Concorrência**

Construa uma simulação lógica ou um roteiro analítico em linguagem C/C++ focado no fenômeno real ocorrido no Hardware baseando-se em:

> Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento"....

> A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclus...

> Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado?...

### Tarefas do Projeto
- [ ] **Setup Inicial**: Alocar perfeitamente os arquivos como `main.cpp` em sua IDE configurando compilador GCC/Clang.
- [ ] **Módulo 1**: Implementar, prototipar ou demonstrar funcionalmente _1. O Data Race: Uma Colisão Inevitável_ no código.
- [ ] **Módulo 2**: Implementar, prototipar ou demonstrar funcionalmente _2. Mutex e The Critical Section_ no código.
- [ ] **Módulo 3**: Implementar, prototipar ou demonstrar funcionalmente _3. O Dilema: Deadlock_ no código.
- [ ] **Validação E Benchmark**: Fazer o build via terminal e testar limites de velocidade analiticamente comparando o log de transição.

### 🏆 Critérios de Qualidade (Review)
1. Compila estritamente sem nenhum warning de memory loss ou fallback.
2. Adere e representa fielmente 100% à teoria aprendida do Markdown da Aula correspondente.
3. Estruturação modular limpa para fácil manutenção.

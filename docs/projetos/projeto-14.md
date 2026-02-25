# Projeto 14: Aula 14 - Sistemas de Arquivos

## 🚀 Laboratório Prático: **Aula 14 - Sistemas de Arquivos**

Construa uma simulação lógica ou um roteiro analítico em linguagem C/C++ focado no fenômeno real ocorrido no Hardware baseando-se em:

> Se no seu PC existe a pasta `Docs/foto.jpg`, no fundo, o Linux não rastreia o texto "foto.jpg" para pular de cluster em cluster....

> Mudar um arquivo é uma transação: Apagar o velho, escrever o novo, mudar o Inode....

> "Escrever no disco" via SysCall C++ `write()` ou `fwrite()` raramente vai pro HD!...

### Tarefas do Projeto
- [ ] **Setup Inicial**: Alocar perfeitamente os arquivos como `main.cpp` em sua IDE configurando compilador GCC/Clang.
- [ ] **Módulo 1**: Implementar, prototipar ou demonstrar funcionalmente _1. O V-Node / Inode_ no código.
- [ ] **Módulo 2**: Implementar, prototipar ou demonstrar funcionalmente _2. Journaling (A Prova contra Quedas)_ no código.
- [ ] **Módulo 3**: Implementar, prototipar ou demonstrar funcionalmente _3. Buffers e Page Cache (Por que Linux é Rápido)_ no código.
- [ ] **Validação E Benchmark**: Fazer o build via terminal e testar limites de velocidade analiticamente comparando o log de transição.

### 🏆 Critérios de Qualidade (Review)
1. Compila estritamente sem nenhum warning de memory loss ou fallback.
2. Adere e representa fielmente 100% à teoria aprendida do Markdown da Aula correspondente.
3. Estruturação modular limpa para fácil manutenção.

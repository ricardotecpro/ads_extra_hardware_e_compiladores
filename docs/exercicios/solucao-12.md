# Solução: Aula 12 - O Modelo de Memória

Abaixo estão as respostas esperadas para os exercícios propostos.

## Solução Questão 1 - 🔀 1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)
**Conceito Base:** Você codifica:
> *A resposta do aluno deve contemplar a premissa de que 🔀 1. A Reordenação do Compilador e CPU (Out-Of-Order Execution) é fundamental para compreender a base conceitual da aula.*

## Solução Questão 2 - 🚧 2. O Memory Model (Consistências e Barreiras)
**Conceito Base:** O C++11 emitiu formalmente o seu universal **Memory Model** definindo através da biblioteca `std::atomic` o que o Hardware tem permições para *Adiantar* vs *Trancar*.
> *A resposta do aluno deve contemplar a premissa de que 🚧 2. O Memory Model (Consistências e Barreiras) é fundamental para compreender a base conceitual da aula.*

## Solução Questão 3 - 🧱 3. Memory Barriers (Fences) nas CPUs
**Conceito Base:** Se não tivessemos essa lei `std::atomic` no standard oficial do GCC, programávamos via "Gambiarra Intrinseca" de Processador (Ex: Comando Assembler **MFENCE** ou **SFENCE** no Intel). Os Fences proíbem categoricamente a travessia de saltos das sub-operações em Assembly, estancando a execução como um sinaleiro fechado.
> *A resposta do aluno deve contemplar a premissa de que 🧱 3. Memory Barriers (Fences) nas CPUs é fundamental para compreender a base conceitual da aula.*

## Solução Questão 4 - 🚀 Resumo Prático
**Conceito Base:** - Se duas "Threads" conversam através das mesmas variáveis limpas de C e não possuam `std::mutex` da aula 10 as blindando, USE **`std::atomic<bool>`**. Do contrário você é uma vítima da *Superscalar Out Of Order Intel Architecture Pipeline* (a reordenação elétrica).
> *A resposta do aluno deve contemplar a premissa de que 🚀 Resumo Prático é fundamental para compreender a base conceitual da aula.*


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-12.md){ .md-button }

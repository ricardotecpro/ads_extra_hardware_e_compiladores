# Solução: Aula 07 - Stack vs Heap

Abaixo estão as respostas esperadas para os exercícios propostos.

## Solução Questão 1 - 🧱 1. A Pilha (Stack)
**Conceito Base:** A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out).
> *A resposta do aluno deve contemplar a premissa de que 🧱 1. A Pilha (Stack) é fundamental para compreender a base conceitual da aula.*

## Solução Questão 2 - 📦 2. O Monte (Heap)
**Conceito Base:** Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação Dinâmica).
> *A resposta do aluno deve contemplar a premissa de que 📦 2. O Monte (Heap) é fundamental para compreender a base conceitual da aula.*

## Solução Questão 3 - 💀 3. Memory Leaks (Vazamentos de Memória)
**Conceito Base:** Um clássico e letal bug de engenharia C++. Quando o desenvolvedor executa `new` ou `malloc` solicitando memória do **Heap**, mas quebra regras do fluxo perdendo o contato formal do **ponteiro** retornado do hardware sem antes ter reportado o fim via `delete` ou `free`.
> *A resposta do aluno deve contemplar a premissa de que 💀 3. Memory Leaks (Vazamentos de Memória) é fundamental para compreender a base conceitual da aula.*

## Solução Questão 4 - 🚀 Resumo Prático
**Conceito Base:** - Se não sabe onde colocar: Bote no STACK.
> *A resposta do aluno deve contemplar a premissa de que 🚀 Resumo Prático é fundamental para compreender a base conceitual da aula.*


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-07.md){ .md-button }

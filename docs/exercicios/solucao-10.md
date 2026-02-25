# Solução: Aula 10 - Sincronização e Concorrência

Abaixo estão as respostas esperadas para os exercícios propostos.

## Solução Questão 1 - 🏎️ 1. O Data Race: Uma Colisão Inevitável
**Conceito Base:** Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".
> *A resposta do aluno deve contemplar a premissa de que 🏎️ 1. O Data Race: Uma Colisão Inevitável é fundamental para compreender a base conceitual da aula.*

## Solução Questão 2 - 🛡️ 2. Mutex e The Critical Section
**Conceito Base:** A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion).
> *A resposta do aluno deve contemplar a premissa de que 🛡️ 2. Mutex e The Critical Section é fundamental para compreender a base conceitual da aula.*

## Solução Questão 3 - 🚦 3. O Dilema: Deadlock
**Conceito Base:** Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado?
> *A resposta do aluno deve contemplar a premissa de que 🚦 3. O Dilema: Deadlock é fundamental para compreender a base conceitual da aula.*

## Solução Questão 4 - 🚀 Resumo Prático
**Conceito Base:** - **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM).
> *A resposta do aluno deve contemplar a premissa de que 🚀 Resumo Prático é fundamental para compreender a base conceitual da aula.*


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-10.md){ .md-button }

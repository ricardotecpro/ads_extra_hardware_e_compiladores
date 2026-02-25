# Projeto: Aula 10 - Sincronização e Concorrência

## Desafio Prático
O objetivo deste projeto é desenvolver ou analisar uma pequena aplicação em C/C++ que comprove na prática os conceitos ensinados na Aula 10, com ênfase em **1. O Data Race: Uma Colisão Inevitável**.

**Contexto Teórico Extraído da Aula:**

> Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".

## Tarefas do Projeto (Implementação/Verificação)
- [ ] **Módulo de 1. O Data Race: Uma Colisão Inevitável**: Demonstrar estruturalmente ou em código a afirmação de que _Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumen..._
- [ ] **Módulo de 2. Mutex e The Critical Section**: Demonstrar estruturalmente ou em código a afirmação de que _A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou..._
- [ ] **Módulo de 3. O Dilema: Deadlock**: Demonstrar estruturalmente ou em código a afirmação de que _Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A es..._
- [ ] **Módulo de Resumo Prático**: Demonstrar estruturalmente ou em código a afirmação de que _- **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (..._

## Critérios de Qualidade e Avaliação
- O código executa de maneira segura, com gestão correta de memória.
- A modelagem está aderente aos conceitos explicados no material teórico (não apenas funciona superficialmente).

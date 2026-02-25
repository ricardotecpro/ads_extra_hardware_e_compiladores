# Exercícios: Aula 10 - Sincronização e Concorrência

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 10**.

## Questão 1 - 1. O Data Race: Uma Colisão Inevitável
**Contexto:** Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".

**Pergunta:** Com base nos conceitos discutidos na aula sobre **1. O Data Race: Uma Colisão Inevitável**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 2 - 2. Mutex e The Critical Section
**Contexto:** A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion).

**Pergunta:** Com base nos conceitos discutidos na aula sobre **2. Mutex e The Critical Section**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 3 - 3. O Dilema: Deadlock
**Contexto:** Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado?

**Pergunta:** Com base nos conceitos discutidos na aula sobre **3. O Dilema: Deadlock**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 4 - Resumo Prático
**Contexto:** - **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM).

**Pergunta:** Com base nos conceitos discutidos na aula sobre **Resumo Prático**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-10.md){ .md-button .md-button--primary }

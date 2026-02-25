# Exercícios: Aula 10 - Sincronização e Concorrência

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 10**.

!!! question "1 - 1. O Data Race: Uma Colisão Inevitável (Básico 1)"
    **Contexto:** 

    > Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".

    **Pergunta:** Descreva o conceito fundamental de 1. O Data Race: Uma Colisão Inevitável e liste duas vantagens de seu uso.


!!! question "2 - 2. Mutex e The Critical Section (Básico 2)"
    **Contexto:** 

    > A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion).

    **Pergunta:** Descreva o conceito fundamental de 2. Mutex e The Critical Section e liste duas vantagens de seu uso.


!!! question "3 - 3. O Dilema: Deadlock (Intermediário 1)"
    **Contexto:** 

    > Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado?

    **Pergunta:** Analisando o funcionamento de 3. O Dilema: Deadlock, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?


!!! question "4 - Resumo Prático (Intermediário 2)"
    **Contexto:** 

    > - **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM).

    **Pergunta:** Analisando o funcionamento de Resumo Prático, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?


!!! question "5 - 1. O Data Race: Uma Colisão Inevitável (Desafio)"
    **Contexto:** 

    > Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".

    **Pergunta (Desafio):** Elabore um cenário de arquitetura onde o uso incorreto ou a falta de entendimento de **1. O Data Race: Uma Colisão Inevitável** cause um problema grave de performance ou vazamento de memória. Como você mitigaria estruturalmente esse gargalo?


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-10.md){ .md-button .md-button--primary }


# Exercícios: Aula 12 - O Modelo de Memória

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 12**.

!!! question "1 - 1. A Reordenação do Compilador e CPU (Out-Of-Order Execution) (Básico 1)"
    **Contexto:** 

    > Você codifica:

    **Pergunta:** Descreva o conceito fundamental de 1. A Reordenação do Compilador e CPU (Out-Of-Order Execution) e liste duas vantagens de seu uso.


!!! question "2 - 2. O Memory Model (Consistências e Barreiras) (Básico 2)"
    **Contexto:** 

    > O C++11 emitiu formalmente o seu universal **Memory Model** definindo através da biblioteca `std::atomic` o que o Hardware tem permições para *Adiantar* vs *Trancar*.

    **Pergunta:** Descreva o conceito fundamental de 2. O Memory Model (Consistências e Barreiras) e liste duas vantagens de seu uso.


!!! question "3 - 3. Memory Barriers (Fences) nas CPUs (Intermediário 1)"
    **Contexto:** 

    > Se não tivessemos essa lei `std::atomic` no standard oficial do GCC, programávamos via "Gambiarra Intrinseca" de Processador (Ex: Comando Assembler **MFENCE** ou **SFENCE** no Intel). Os Fences proíbem categoricamente a travessia de saltos das sub-operações em Assembly, estancando a execução como um sinaleiro fechado.

    **Pergunta:** Analisando o funcionamento de 3. Memory Barriers (Fences) nas CPUs, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?


!!! question "4 - Resumo Prático (Intermediário 2)"
    **Contexto:** 

    > - Se duas "Threads" conversam através das mesmas variáveis limpas de C e não possuam `std::mutex` da aula 10 as blindando, USE **`std::atomic<bool>`**. Do contrário você é uma vítima da *Superscalar Out Of Order Intel Architecture Pipeline* (a reordenação elétrica).

    **Pergunta:** Analisando o funcionamento de Resumo Prático, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?


!!! question "5 - 1. A Reordenação do Compilador e CPU (Out-Of-Order Execution) (Desafio)"
    **Contexto:** 

    > Você codifica:

    **Pergunta (Desafio):** Elabore um cenário de arquitetura onde o uso incorreto ou a falta de entendimento de **1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)** cause um problema grave de performance ou vazamento de memória. Como você mitigaria estruturalmente esse gargalo?


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-12.md){ .md-button .md-button--primary }


# Exercícios: Aula 11 - Paralelismo no Hardware

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 11**.

!!! question "1 - 1. Multi-Core (Múltiplos Núcleos) (Básico 1)"
    **Contexto:** 

    > Diferente do passado, onde havia um único núcleo saltando entre aplicativos (Context Switch), hoje temos vários núcleos físicos no mesmo invólucro (Chip).

    **Pergunta:** Descreva o conceito fundamental de 1. Multi-Core (Múltiplos Núcleos) e liste duas vantagens de seu uso.


!!! question "2 - 2. Hyper-Threading (SMT - Symmetrical Multi-Threading) (Básico 2)"
    **Contexto:** 

    > A mágica comercial da Intel e AMD nos anos 2000. Como fazer "1 Core Físico" fingir ser "2 Cores Lógicos" para o Windows/Linux?

    **Pergunta:** Descreva o conceito fundamental de 2. Hyper-Threading (SMT - Symmetrical Multi-Threading) e liste duas vantagens de seu uso.


!!! question "3 - 3. GPUs: O Paralelismo Maciço (Intermediário 1)"
    **Contexto:** 

    > CPUs (Processadores) foram feitos para "Serem Rápidos executando sequências lógicas e IFs complexos". Possuem Caches gigantes.

    **Pergunta:** Analisando o funcionamento de 3. GPUs: O Paralelismo Maciço, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?


!!! question "4 - Resumo Prático (Intermediário 2)"
    **Contexto:** 

    > - **Task Paralelism**: Se tens lógica variada, use a *CPU Multi-Core C++ thread pool*.

    **Pergunta:** Analisando o funcionamento de Resumo Prático, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?


!!! question "5 - 1. Multi-Core (Múltiplos Núcleos) (Desafio)"
    **Contexto:** 

    > Diferente do passado, onde havia um único núcleo saltando entre aplicativos (Context Switch), hoje temos vários núcleos físicos no mesmo invólucro (Chip).

    **Pergunta (Desafio):** Elabore um cenário de arquitetura onde o uso incorreto ou a falta de entendimento de **1. Multi-Core (Múltiplos Núcleos)** cause um problema grave de performance ou vazamento de memória. Como você mitigaria estruturalmente esse gargalo?


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-11.md){ .md-button .md-button--primary }


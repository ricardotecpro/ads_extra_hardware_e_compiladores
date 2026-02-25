# Exercícios: Aula 09 - Processos e Threads

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 09**.

## Questão 1 - 1. Processos (Isolamento Forte) (Básico 1)
**Contexto:** 

> O Processo é o contêiner mestre do *Sistema Operacional*. Quando a execução do seu binário em C/C++ se inicia via Terminal, vira um Processo (`PID 2900`).

**Pergunta:** Descreva o conceito fundamental de **1. Processos (Isolamento Forte)** e liste duas vantagens de seu uso.

## Questão 2 - 2. Threads (Isolamento Fraco / Partilha) (Básico 2)
**Contexto:** 

> Quando se está em um jogo e, ao mesmo tempo que carrega os gráficos na GPU, uma música de CD está lendo sem travar, estamos olhando para **Multithreading**!

**Pergunta:** Descreva o conceito fundamental de **2. Threads (Isolamento Fraco / Partilha)** e liste duas vantagens de seu uso.

## Questão 3 - 3. Context Switch (A Faca de Dois Gumes) (Intermediário 1)
**Contexto:** 

> Quando escrevemos `"Hello World"`, achamos que a CPU roda por horas sem interrupções. Engano.

**Pergunta:** Analisando o funcionamento de **3. Context Switch (A Faca de Dois Gumes)**, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 4 - Resumo Prático (Intermediário 2)
**Contexto:** 

> - Se a tarefa for CPU-Bound (requerer Matemática Bruta Massiva / Machine Learning), você cria Threads numerando-as próximo número oficial de núcleos estritos da CPU, evitando desperdício de overhead com *Context Switches* ilusórios.

**Pergunta:** Analisando o funcionamento de **Resumo Prático**, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 5 - 1. Processos (Isolamento Forte) (Desafio)
**Contexto:** 

> O Processo é o contêiner mestre do *Sistema Operacional*. Quando a execução do seu binário em C/C++ se inicia via Terminal, vira um Processo (`PID 2900`).

**Pergunta (Desafio):** Elabore um cenário de arquitetura onde o uso incorreto ou a falta de entendimento de **1. Processos (Isolamento Forte)** cause um problema grave de performance ou vazamento de memória. Como você mitigaria estruturalmente esse gargalo?


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-09.md){ .md-button .md-button--primary }

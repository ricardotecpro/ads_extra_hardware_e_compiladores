# Exercícios: Aula 07 - Stack vs Heap

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 07**.

## Questão 1 - 1. A Pilha (Stack) (Básico 1)
**Contexto:** 

> A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out).

**Pergunta:** Descreva o conceito fundamental de 1. A Pilha (Stack) e liste duas vantagens de seu uso.

## Questão 2 - 2. O Monte (Heap) (Básico 2)
**Contexto:** 

> Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação Dinâmica).

**Pergunta:** Descreva o conceito fundamental de 2. O Monte (Heap) e liste duas vantagens de seu uso.

## Questão 3 - 3. Memory Leaks (Vazamentos de Memória) (Intermediário 1)
**Contexto:** 

> Um clássico e letal bug de engenharia C++. Quando o desenvolvedor executa `new` ou `malloc` solicitando memória do **Heap**, mas quebra regras do fluxo perdendo o contato formal do **ponteiro** retornado do hardware sem antes ter reportado o fim via `delete` ou `free`.

**Pergunta:** Analisando o funcionamento de 3. Memory Leaks (Vazamentos de Memória), como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 4 - Resumo Prático (Intermediário 2)
**Contexto:** 

> - Se não sabe onde colocar: Bote no STACK.

**Pergunta:** Analisando o funcionamento de Resumo Prático, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 5 - 1. A Pilha (Stack) (Desafio)
**Contexto:** 

> A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out).

**Pergunta (Desafio):** Elabore um cenário de arquitetura onde o uso incorreto ou a falta de entendimento de **1. A Pilha (Stack)** cause um problema grave de performance ou vazamento de memória. Como você mitigaria estruturalmente esse gargalo?


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-07.md){ .md-button .md-button--primary }

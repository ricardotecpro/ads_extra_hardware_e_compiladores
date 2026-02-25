# Exercícios: Aula 07 - Stack vs Heap

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 07**.

## Questão 1 - 1. A Pilha (Stack)
**Contexto:** A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out).

**Pergunta:** Com base nos conceitos discutidos na aula sobre **1. A Pilha (Stack)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 2 - 2. O Monte (Heap)
**Contexto:** Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação Dinâmica).

**Pergunta:** Com base nos conceitos discutidos na aula sobre **2. O Monte (Heap)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 3 - 3. Memory Leaks (Vazamentos de Memória)
**Contexto:** Um clássico e letal bug de engenharia C++. Quando o desenvolvedor executa `new` ou `malloc` solicitando memória do **Heap**, mas quebra regras do fluxo perdendo o contato formal do **ponteiro** retornado do hardware sem antes ter reportado o fim via `delete` ou `free`.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **3. Memory Leaks (Vazamentos de Memória)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 4 - Resumo Prático
**Contexto:** - Se não sabe onde colocar: Bote no STACK.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **Resumo Prático**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-07.md){ .md-button .md-button--primary }

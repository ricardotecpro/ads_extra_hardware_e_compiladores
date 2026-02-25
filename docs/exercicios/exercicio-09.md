# Exercícios: Aula 09 - Processos e Threads

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 09**.

## Questão 1 - 1. Processos (Isolamento Forte)
**Contexto:** O Processo é o contêiner mestre do *Sistema Operacional*. Quando a execução do seu binário em C/C++ se inicia via Terminal, vira um Processo (`PID 2900`).

**Pergunta:** Com base nos conceitos discutidos na aula sobre **1. Processos (Isolamento Forte)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 2 - 2. Threads (Isolamento Fraco / Partilha)
**Contexto:** Quando se está em um jogo e, ao mesmo tempo que carrega os gráficos na GPU, uma música de CD está lendo sem travar, estamos olhando para **Multithreading**!

**Pergunta:** Com base nos conceitos discutidos na aula sobre **2. Threads (Isolamento Fraco / Partilha)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 3 - 3. Context Switch (A Faca de Dois Gumes)
**Contexto:** Quando escrevemos `"Hello World"`, achamos que a CPU roda por horas sem interrupções. Engano.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **3. Context Switch (A Faca de Dois Gumes)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 4 - Resumo Prático
**Contexto:** - Se a tarefa for CPU-Bound (requerer Matemática Bruta Massiva / Machine Learning), você cria Threads numerando-as próximo número oficial de núcleos estritos da CPU, evitando desperdício de overhead com *Context Switches* ilusórios.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **Resumo Prático**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-09.md){ .md-button .md-button--primary }

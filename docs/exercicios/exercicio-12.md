# Exercícios: Aula 12 - O Modelo de Memória

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 12**.

## Questão 1 - 1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)
**Contexto:** Você codifica:

**Pergunta:** Com base nos conceitos discutidos na aula sobre **1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 2 - 2. O Memory Model (Consistências e Barreiras)
**Contexto:** O C++11 emitiu formalmente o seu universal **Memory Model** definindo através da biblioteca `std::atomic` o que o Hardware tem permições para *Adiantar* vs *Trancar*.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **2. O Memory Model (Consistências e Barreiras)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 3 - 3. Memory Barriers (Fences) nas CPUs
**Contexto:** Se não tivessemos essa lei `std::atomic` no standard oficial do GCC, programávamos via "Gambiarra Intrinseca" de Processador (Ex: Comando Assembler **MFENCE** ou **SFENCE** no Intel). Os Fences proíbem categoricamente a travessia de saltos das sub-operações em Assembly, estancando a execução como um sinaleiro fechado.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **3. Memory Barriers (Fences) nas CPUs**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 4 - Resumo Prático
**Contexto:** - Se duas "Threads" conversam através das mesmas variáveis limpas de C e não possuam `std::mutex` da aula 10 as blindando, USE **`std::atomic<bool>`**. Do contrário você é uma vítima da *Superscalar Out Of Order Intel Architecture Pipeline* (a reordenação elétrica).

**Pergunta:** Com base nos conceitos discutidos na aula sobre **Resumo Prático**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-12.md){ .md-button .md-button--primary }

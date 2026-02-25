# Exercícios: Aula 11 - Paralelismo no Hardware

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 11**.

## Questão 1 - 1. Multi-Core (Múltiplos Núcleos)
**Contexto:** Diferente do passado, onde havia um único núcleo saltando entre aplicativos (Context Switch), hoje temos vários núcleos físicos no mesmo invólucro (Chip).

**Pergunta:** Com base nos conceitos discutidos na aula sobre **1. Multi-Core (Múltiplos Núcleos)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 2 - 2. Hyper-Threading (SMT - Symmetrical Multi-Threading)
**Contexto:** A mágica comercial da Intel e AMD nos anos 2000. Como fazer "1 Core Físico" fingir ser "2 Cores Lógicos" para o Windows/Linux?

**Pergunta:** Com base nos conceitos discutidos na aula sobre **2. Hyper-Threading (SMT - Symmetrical Multi-Threading)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 3 - 3. GPUs: O Paralelismo Maciço
**Contexto:** CPUs (Processadores) foram feitos para "Serem Rápidos executando sequências lógicas e IFs complexos". Possuem Caches gigantes.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **3. GPUs: O Paralelismo Maciço**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 4 - Resumo Prático
**Contexto:** - **Task Paralelism**: Se tens lógica variada, use a *CPU Multi-Core C++ thread pool*.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **Resumo Prático**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-11.md){ .md-button .md-button--primary }

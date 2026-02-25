# Exercícios: Aula 06 - Cache e Localidade

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 06**.

## Questão 1 - 1. Cache Hit e Cache Miss (Básico 1)
**Contexto:** 

> O desempenho do seu loop `for()` depende maciçamente da *Cache Hit Rate*.

**Pergunta:** Descreva o conceito fundamental de 1. Cache Hit e Cache Miss e liste duas vantagens de seu uso.

## Questão 2 - 2. Localidade Espacial vs Temporal (Básico 2)
**Contexto:** 

> As duas premissas arquiteturais da Localidade em Sistemas de Computação (que fundamentam toda escrita C/C++ otimizada):

**Pergunta:** Descreva o conceito fundamental de 2. Localidade Espacial vs Temporal e liste duas vantagens de seu uso.

## Questão 3 - 3. False Sharing e Lógica Invertida (A Morte do C++) (Intermediário 1)
**Contexto:** 

> A estrutura define a localidade espacial. Prefira dezenas de minúsculas variáveis sequenciais nos métodos a usar longos grafos com saltos randômicos baseados em ponteiros, se for iterar a esmo.

**Pergunta:** Analisando o funcionamento de 3. False Sharing e Lógica Invertida (A Morte do C++), como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 4 - 1. Cache Hit e Cache Miss (Intermediário 2)
**Contexto:** 

> O desempenho do seu loop `for()` depende maciçamente da *Cache Hit Rate*.

**Pergunta:** Analisando o funcionamento de 1. Cache Hit e Cache Miss, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 5 - 2. Localidade Espacial vs Temporal (Desafio)
**Contexto:** 

> As duas premissas arquiteturais da Localidade em Sistemas de Computação (que fundamentam toda escrita C/C++ otimizada):

**Pergunta (Desafio):** Elabore um cenário de arquitetura onde o uso incorreto ou a falta de entendimento de **2. Localidade Espacial vs Temporal** cause um problema grave de performance ou vazamento de memória. Como você mitigaria estruturalmente esse gargalo?


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-06.md){ .md-button .md-button--primary }

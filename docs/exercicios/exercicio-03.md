# Exercícios: Aula 03 - CPU: Estrutura e Funcionamento

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 03**.

## Questão 1 - 1. O Triângulo de Ouro: ALU, CU e Registradores (Básico 1)
**Contexto:** 

> A arquitetura interna da CPU possui 3 órgãos vitais:

**Pergunta:** Descreva o conceito fundamental de **1. O Triângulo de Ouro: ALU, CU e Registradores** e liste duas vantagens de seu uso.

## Questão 2 - 2. O Ciclo de Instrução (Fetch-Decode-Execute) (Básico 2)
**Contexto:** 

> Cada operação ou linha de código C/C++ que você escreve é processada na cadência do *Clock* pelo ciclo clássico:

**Pergunta:** Descreva o conceito fundamental de **2. O Ciclo de Instrução (Fetch-Decode-Execute)** e liste duas vantagens de seu uso.

## Questão 3 - 3. Pipeline e Previsão de Desvio (Branch Prediction) (Intermediário 1)
**Contexto:** 

> Seu processador não faz essas 4 etapas de forma burra (uma por vez). Ele usa **Pipelining**: Enquanto a Instrução A está em Execute, a Instrução B já está em Decode e a Instrução C está em Fetch!

**Pergunta:** Analisando o funcionamento de **3. Pipeline e Previsão de Desvio (Branch Prediction)**, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 4 - Resumo Prático (Intermediário 2)
**Contexto:** 

> Registradores são seus maiores amigos de performance. Códigos C++ que permitem ao compilador prender cálculos pesados 100% dentro dos Registradores rodam em Nanossegundos, contra Milissegundos lendo sempre pela RAM.

**Pergunta:** Analisando o funcionamento de **Resumo Prático**, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 5 - 1. O Triângulo de Ouro: ALU, CU e Registradores (Desafio)
**Contexto:** 

> A arquitetura interna da CPU possui 3 órgãos vitais:

**Pergunta (Desafio):** Elabore um cenário de arquitetura onde o uso incorreto ou a falta de entendimento de **1. O Triângulo de Ouro: ALU, CU e Registradores** cause um problema grave de performance ou vazamento de memória. Como você mitigaria estruturalmente esse gargalo?


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-03.md){ .md-button .md-button--primary }

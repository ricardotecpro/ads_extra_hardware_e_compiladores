# Exercícios: Aula 15 - Entrada e Saída (I/O)

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 15**.

## Questão 1 - 1. System Calls (O Pedágio do Kernel) (Básico 1)
**Contexto:** 

> Programas nativos de C/C++ rodando na zona abstratamente segura (User Space) NÃO TÊM permissão física elétron-elétron para dar ordens ao cabo de Rede de imprimir um byte TCP. Tentar burlar isso gera um sumário e fulminante encerramento compulsório pelo Processador através do bloqueio de Anéis de Proteção.

**Pergunta:** Descreva o conceito fundamental de **1. System Calls (O Pedágio do Kernel)** e liste duas vantagens de seu uso.

## Questão 2 - 2. Interrupções vs Polling (Básico 2)
**Contexto:** 

> Seu App em Python/C diz: "Puxe o dado que está vindo no mouse".

**Pergunta:** Descreva o conceito fundamental de **2. Interrupções vs Polling** e liste duas vantagens de seu uso.

## Questão 3 - 3. DMA (Memória com Acesso Direto) (Intermediário 1)
**Contexto:** 

> Mesmo com as Interrupções ajudando a não ficar paralisado *Polling*... Fazer a Placa de Rede encher a placa RAM transitando Bit a Bit passando pelo miolo doloroso da CPU era impraticável em Gigabit Ethernets.

**Pergunta:** Analisando o funcionamento de **3. DMA (Memória com Acesso Direto)**, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 4 - Resumo Prático (Intermediário 2)
**Contexto:** 

> - Se a sua aplicação Web Framework assíncrona (como NodeJS ou Nginx C++) trava muito com "I/O", isso significa que o Sistema delega operações custosas pelo DMA ao Kernel, enquanto orquestra Event-Loops aguardando os famigerados Interrupts de retorno.

**Pergunta:** Analisando o funcionamento de **Resumo Prático**, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 5 - 1. System Calls (O Pedágio do Kernel) (Desafio)
**Contexto:** 

> Programas nativos de C/C++ rodando na zona abstratamente segura (User Space) NÃO TÊM permissão física elétron-elétron para dar ordens ao cabo de Rede de imprimir um byte TCP. Tentar burlar isso gera um sumário e fulminante encerramento compulsório pelo Processador através do bloqueio de Anéis de Proteção.

**Pergunta (Desafio):** Elabore um cenário de arquitetura onde o uso incorreto ou a falta de entendimento de **1. System Calls (O Pedágio do Kernel)** cause um problema grave de performance ou vazamento de memória. Como você mitigaria estruturalmente esse gargalo?


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-15.md){ .md-button .md-button--primary }

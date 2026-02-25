# Exercícios: Aula 14 - Sistemas de Arquivos

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 14**.

## Questão 1 - 1. O V-Node / Inode (Básico 1)
**Contexto:** 

> Se no seu PC existe a pasta `Docs/foto.jpg`, no fundo, o Linux não rastreia o texto "foto.jpg" para pular de cluster em cluster.

**Pergunta:** Descreva o conceito fundamental de **1. O V-Node / Inode** e liste duas vantagens de seu uso.

## Questão 2 - 2. Journaling (A Prova contra Quedas) (Básico 2)
**Contexto:** 

> Mudar um arquivo é uma transação: Apagar o velho, escrever o novo, mudar o Inode.

**Pergunta:** Descreva o conceito fundamental de **2. Journaling (A Prova contra Quedas)** e liste duas vantagens de seu uso.

## Questão 3 - 3. Buffers e Page Cache (Por que Linux é Rápido) (Intermediário 1)
**Contexto:** 

> "Escrever no disco" via SysCall C++ `write()` ou `fwrite()` raramente vai pro HD!

**Pergunta:** Analisando o funcionamento de **3. Buffers e Page Cache (Por que Linux é Rápido)**, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 4 - Resumo Prático (Intermediário 2)
**Contexto:** 

> - Ao usar C/C++, chame o instrínseco `fsync()` se seu App for um Banco de Dados ou Software Crítico Bancário forçando a Cache RAM descarregar a força e salvar permanentemente no silício do disco.

**Pergunta:** Analisando o funcionamento de **Resumo Prático**, como essa métrica interage em um ambiente prático de compilação ou execução de código C/C++ a nível de sistema operacional?

## Questão 5 - 1. O V-Node / Inode (Desafio)
**Contexto:** 

> Se no seu PC existe a pasta `Docs/foto.jpg`, no fundo, o Linux não rastreia o texto "foto.jpg" para pular de cluster em cluster.

**Pergunta (Desafio):** Elabore um cenário de arquitetura onde o uso incorreto ou a falta de entendimento de **1. O V-Node / Inode** cause um problema grave de performance ou vazamento de memória. Como você mitigaria estruturalmente esse gargalo?


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-14.md){ .md-button .md-button--primary }

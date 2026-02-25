# Exercícios: Aula 14 - Sistemas de Arquivos

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 14**.

## Questão 1 - 1. O V-Node / Inode
**Contexto:** Se no seu PC existe a pasta `Docs/foto.jpg`, no fundo, o Linux não rastreia o texto "foto.jpg" para pular de cluster em cluster.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **1. O V-Node / Inode**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 2 - 2. Journaling (A Prova contra Quedas)
**Contexto:** Mudar um arquivo é uma transação: Apagar o velho, escrever o novo, mudar o Inode.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **2. Journaling (A Prova contra Quedas)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 3 - 3. Buffers e Page Cache (Por que Linux é Rápido)
**Contexto:** "Escrever no disco" via SysCall C++ `write()` ou `fwrite()` raramente vai pro HD!

**Pergunta:** Com base nos conceitos discutidos na aula sobre **3. Buffers e Page Cache (Por que Linux é Rápido)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 4 - Resumo Prático
**Contexto:** - Ao usar C/C++, chame o instrínseco `fsync()` se seu App for um Banco de Dados ou Software Crítico Bancário forçando a Cache RAM descarregar a força e salvar permanentemente no silício do disco.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **Resumo Prático**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-14.md){ .md-button .md-button--primary }

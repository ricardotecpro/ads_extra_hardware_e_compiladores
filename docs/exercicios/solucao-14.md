# Solução: Aula 14 - Sistemas de Arquivos

Abaixo estão as respostas esperadas para os exercícios propostos.

## Solução Questão 1 - 🗂️ 1. O V-Node / Inode
**Conceito Base:** Se no seu PC existe a pasta `Docs/foto.jpg`, no fundo, o Linux não rastreia o texto "foto.jpg" para pular de cluster em cluster.
> *A resposta do aluno deve contemplar a premissa de que 🗂️ 1. O V-Node / Inode é fundamental para compreender a base conceitual da aula.*

## Solução Questão 2 - 🛡️ 2. Journaling (A Prova contra Quedas)
**Conceito Base:** Mudar um arquivo é uma transação: Apagar o velho, escrever o novo, mudar o Inode.
> *A resposta do aluno deve contemplar a premissa de que 🛡️ 2. Journaling (A Prova contra Quedas) é fundamental para compreender a base conceitual da aula.*

## Solução Questão 3 - 🚄 3. Buffers e Page Cache (Por que Linux é Rápido)
**Conceito Base:** "Escrever no disco" via SysCall C++ `write()` ou `fwrite()` raramente vai pro HD!
> *A resposta do aluno deve contemplar a premissa de que 🚄 3. Buffers e Page Cache (Por que Linux é Rápido) é fundamental para compreender a base conceitual da aula.*

## Solução Questão 4 - 🚀 Resumo Prático
**Conceito Base:** - Ao usar C/C++, chame o instrínseco `fsync()` se seu App for um Banco de Dados ou Software Crítico Bancário forçando a Cache RAM descarregar a força e salvar permanentemente no silício do disco.
> *A resposta do aluno deve contemplar a premissa de que 🚀 Resumo Prático é fundamental para compreender a base conceitual da aula.*


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-14.md){ .md-button }

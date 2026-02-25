# Projeto: Aula 14 - Sistemas de Arquivos

## Desafio Prático
O objetivo deste projeto é desenvolver ou analisar uma pequena aplicação em C/C++ que comprove na prática os conceitos ensinados na Aula 14, com ênfase em **1. O V-Node / Inode**.

**Contexto Teórico Extraído da Aula:**

> Se no seu PC existe a pasta `Docs/foto.jpg`, no fundo, o Linux não rastreia o texto "foto.jpg" para pular de cluster em cluster.

## Tarefas do Projeto (Implementação/Verificação)
- [ ] **Módulo de 1. O V-Node / Inode**: Demonstrar estruturalmente ou em código a afirmação de que _Se no seu PC existe a pasta `Docs/foto.jpg`, no fundo, o Linux não rastreia o te..._
- [ ] **Módulo de 2. Journaling (A Prova contra Quedas)**: Demonstrar estruturalmente ou em código a afirmação de que _Mudar um arquivo é uma transação: Apagar o velho, escrever o novo, mudar o Inode..._
- [ ] **Módulo de 3. Buffers e Page Cache (Por que Linux é Rápido)**: Demonstrar estruturalmente ou em código a afirmação de que _"Escrever no disco" via SysCall C++ `write()` ou `fwrite()` raramente vai pro HD..._
- [ ] **Módulo de Resumo Prático**: Demonstrar estruturalmente ou em código a afirmação de que _- Ao usar C/C++, chame o instrínseco `fsync()` se seu App for um Banco de Dados ..._

## Critérios de Qualidade e Avaliação
- O código executa de maneira segura, com gestão correta de memória.
- A modelagem está aderente aos conceitos explicados no material teórico (não apenas funciona superficialmente).

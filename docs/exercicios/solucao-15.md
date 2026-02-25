# Solução: Aula 15 - Entrada e Saída (I/O)

Abaixo estão as respostas esperadas para os exercícios propostos.

## Solução Questão 1 - 🚪 1. System Calls (O Pedágio do Kernel)
**Conceito Base:** Programas nativos de C/C++ rodando na zona abstratamente segura (User Space) NÃO TÊM permissão física elétron-elétron para dar ordens ao cabo de Rede de imprimir um byte TCP. Tentar burlar isso gera um sumário e fulminante encerramento compulsório pelo Processador através do bloqueio de Anéis de Proteção.
> *A resposta do aluno deve contemplar a premissa de que 🚪 1. System Calls (O Pedágio do Kernel) é fundamental para compreender a base conceitual da aula.*

## Solução Questão 2 - ⚠️ 2. Interrupções vs Polling
**Conceito Base:** Seu App em Python/C diz: "Puxe o dado que está vindo no mouse".
> *A resposta do aluno deve contemplar a premissa de que ⚠️ 2. Interrupções vs Polling é fundamental para compreender a base conceitual da aula.*

## Solução Questão 3 - 🚀 3. DMA (Memória com Acesso Direto)
**Conceito Base:** Mesmo com as Interrupções ajudando a não ficar paralisado *Polling*... Fazer a Placa de Rede encher a placa RAM transitando Bit a Bit passando pelo miolo doloroso da CPU era impraticável em Gigabit Ethernets.
> *A resposta do aluno deve contemplar a premissa de que 🚀 3. DMA (Memória com Acesso Direto) é fundamental para compreender a base conceitual da aula.*

## Solução Questão 4 - 🚀 Resumo Prático
**Conceito Base:** - Se a sua aplicação Web Framework assíncrona (como NodeJS ou Nginx C++) trava muito com "I/O", isso significa que o Sistema delega operações custosas pelo DMA ao Kernel, enquanto orquestra Event-Loops aguardando os famigerados Interrupts de retorno.
> *A resposta do aluno deve contemplar a premissa de que 🚀 Resumo Prático é fundamental para compreender a base conceitual da aula.*


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-15.md){ .md-button }

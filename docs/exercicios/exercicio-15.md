# Exercícios: Aula 15 - Entrada e Saída (I/O)

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 15**.

## Questão 1 - 1. System Calls (O Pedágio do Kernel)
**Contexto:** Programas nativos de C/C++ rodando na zona abstratamente segura (User Space) NÃO TÊM permissão física elétron-elétron para dar ordens ao cabo de Rede de imprimir um byte TCP. Tentar burlar isso gera um sumário e fulminante encerramento compulsório pelo Processador através do bloqueio de Anéis de Proteção.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **1. System Calls (O Pedágio do Kernel)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 2 - 2. Interrupções vs Polling
**Contexto:** Seu App em Python/C diz: "Puxe o dado que está vindo no mouse".

**Pergunta:** Com base nos conceitos discutidos na aula sobre **2. Interrupções vs Polling**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 3 - 3. DMA (Memória com Acesso Direto)
**Contexto:** Mesmo com as Interrupções ajudando a não ficar paralisado *Polling*... Fazer a Placa de Rede encher a placa RAM transitando Bit a Bit passando pelo miolo doloroso da CPU era impraticável em Gigabit Ethernets.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **3. DMA (Memória com Acesso Direto)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 4 - Resumo Prático
**Contexto:** - Se a sua aplicação Web Framework assíncrona (como NodeJS ou Nginx C++) trava muito com "I/O", isso significa que o Sistema delega operações custosas pelo DMA ao Kernel, enquanto orquestra Event-Loops aguardando os famigerados Interrupts de retorno.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **Resumo Prático**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-15.md){ .md-button .md-button--primary }

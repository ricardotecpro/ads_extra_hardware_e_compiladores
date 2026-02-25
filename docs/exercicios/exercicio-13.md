# Exercícios: Aula 13 - Dispositivos de Armazenamento

Resolver esses exercícios ajudará na fixação do conteúdo abordado na **Aula 13**.

## Questão 1 - 1. HDD (Hard Disk Drive) vs SSD (SATA)
**Contexto:** 

**Pergunta:** Com base nos conceitos discutidos na aula sobre **1. HDD (Hard Disk Drive) vs SSD (SATA)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 2 - 2. NVMe (O Limite PCIe)
**Contexto:** Para ultrapassar o gargalo da conexão SATA antiga, a tecnologia moveu os SSDs diretamente para injetarem dados nas pistas ultra-rápidas da placa-mãe (PCI-Express). Módulos NVMe M.2 se comunicam fisicamente por canais em que passam Gigabytes por segundo (ex: Gen4 cruza *7.000 MB/s*).

**Pergunta:** Com base nos conceitos discutidos na aula sobre **2. NVMe (O Limite PCIe)**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 3 - 3. IOPS - A Métrica Real do Servidor
**Contexto:** Se a banda (MB/s) diz o volume da mangueira, os **IOPS (Input/Output Operations Per Second)** dizem quantos golpes a mangueira dá por segundo.

**Pergunta:** Com base nos conceitos discutidos na aula sobre **3. IOPS - A Métrica Real do Servidor**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.

## Questão 4 - Resumo Prático
**Contexto:** O desenvolvedor C++ entende isso programando a I/O por grandes lotes (`Buffers`). Não escreva no disco `1 byte` no laço for por `1 milhão de vezes` (Destruição de IOPS).

**Pergunta:** Com base nos conceitos discutidos na aula sobre **Resumo Prático**, elabore uma explicação sobre sua importância, funcionamento prático e impactos no desenvolvimento de software de baixo nível em C/C++.


---

[:octicons-light-bulb-24: Ver Solução e Explicação Detalhada](solucao-13.md){ .md-button .md-button--primary }

# Solução e Explicação Detalhada: Aula 13 - Dispositivos de Armazenamento

Abaixo estão as respostas esperadas e o embasamento teórico para os exercícios propostos na **Aula 13**.

## Solução da Questão 1 - 1. HDD (Hard Disk Drive) vs SSD (SATA) (Básico 1)
**Explicação Detalhada do Assunto:**



O disco de pratos giratórios com uma agulha física.



Armazenamento em chips de memória Flash (NAND). Zero partes móveis.

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *1. HDD (Hard Disk Drive) vs SSD (SATA)* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 2 - 2. NVMe (O Limite PCIe) (Básico 2)
**Explicação Detalhada do Assunto:**

Para ultrapassar o gargalo da conexão SATA antiga, a tecnologia moveu os SSDs diretamente para injetarem dados nas pistas ultra-rápidas da placa-mãe (PCI-Express). Módulos NVMe M.2 se comunicam fisicamente por canais em que passam Gigabytes por segundo (ex: Gen4 cruza *7.000 MB/s*).

Isto alterou para sempre o Backend moderno: Os Softwares de Memória In-Memory (Redis) estão repensando paradigmas pois o Disco NVMe moderno às vezes responde com velocidade que roça a velha memória RAM DDR3!

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *2. NVMe (O Limite PCIe)* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 3 - 3. IOPS - A Métrica Real do Servidor (Intermediário 1)
**Explicação Detalhada do Assunto:**

Se a banda (MB/s) diz o volume da mangueira, os **IOPS (Input/Output Operations Per Second)** dizem quantos golpes a mangueira dá por segundo.

- Quando você hospeda um App Node/Python que grava 1 milhão de pequenos logs `.txt` de 1KB, não importa se você tem 7000 MB/s. Você precisa de IOPS Altíssimos, para que a fila matemática de *Write Requests* não trave seu servidor (`I/O Wait / Blocked`).

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *3. IOPS - A Métrica Real do Servidor* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 4 - Resumo Prático (Intermediário 2)
**Explicação Detalhada do Assunto:**

O desenvolvedor C++ entende isso programando a I/O por grandes lotes (`Buffers`). Não escreva no disco `1 byte` no laço for por `1 milhão de vezes` (Destruição de IOPS).

Acumule os dados num Buffer gigântico de `1 MB` na RAM, e comande gravar os dados no SSD em único e massivo Request! (Otimização máxima de Throughput).



!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *Resumo Prático* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 5 - 1. HDD (Hard Disk Drive) vs SSD (SATA) (Desafio)
**Explicação Detalhada do Assunto:**



O disco de pratos giratórios com uma agulha física.



Armazenamento em chips de memória Flash (NAND). Zero partes móveis.

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *1. HDD (Hard Disk Drive) vs SSD (SATA)* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-13.md){ .md-button }

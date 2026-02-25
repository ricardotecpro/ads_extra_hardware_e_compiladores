---
theme: white
transition: convex
---

<!-- .element: class="fragment" -->
# Dispositivos de Armazenamento
## Aula 13

---

## 💽 1. HDD (Hard Disk Drive) vs SSD (SATA)


    O disco de pratos giratórios com uma agulha física. 
    **Latência**: O motor precisa literalmente girar (Seek Time e Latência Rotacional) até o bloco desejado. As leituras sequenciais (filmes grandes contínuos) são aceitáveis, mas *Random Access* (leitura randômica de pequenos arquivos) é catastrófica, beirando a eternidade computacional.

    Armazenamento em chips de memória Flash (NAND). Zero partes móveis.
    **Latência**: Mil vezes superior ao HDD em acesso Randômico. Seu Banco de Dados Relacional MySQL renasce num SSD porque consegue varrer os índices disparatadamente sem esperar "O disco girar". Ele satura, porém, a banda do Barramento SATA (máx. 600 MB/s).

---

---

## ⚡ 2. NVMe (O Limite PCIe)

Para ultrapassar o gargalo da conexão SATA antiga, a tecnologia moveu os SSDs diretamente para injetarem dados nas pistas ultra-rápidas da placa-mãe (PCI-Express). Módulos NVMe M.2 se comunicam fisicamente por canais em que passam Gigabytes por segundo (ex: Gen4 cruza *7.000 MB/s*).

Isto alterou para sempre o Backend moderno: Os Softwares de Memória In-Memory (Redis) estão repensando paradigmas pois o Disco NVMe moderno às vezes responde com velocidade que roça a velha memória RAM DDR3!

---

---

## 📈 3. IOPS - A Métrica Real do Servidor

Se a banda (MB/s) diz o volume da mangueira, os **IOPS (Input/Output Operations Per Second)** dizem quantos golpes a mangueira dá por segundo. 

- Quando você hospeda um App Node/Python que grava 1 milhão de pequenos logs `.txt` de 1KB, não importa se você tem 7000 MB/s. Você precisa de IOPS Altíssimos, para que a fila matemática de *Write Requests* não trave seu servidor (`I/O Wait / Blocked`). 

> [!CAUTION]
> Ao configurar a AWS (Amazon Cloud), instâncias EBS (Discos elásticos anexados) cobram mais caro pela volumetria de **IOPS**. O gargalo da sua API lenta de CRUD nunca é a CPU, geralmente é porque o Disco Estourou sua cota de Burst de IOPS.

---

## 🚀 Resumo Prático

O desenvolvedor C++ entende isso programando a I/O por grandes lotes (`Buffers`). Não escreva no disco `1 byte` no laço for por `1 milhão de vezes` (Destruição de IOPS).
Acumule os dados num Buffer gigântico de `1 MB` na RAM, e comande gravar os dados no SSD em único e massivo Request! (Otimização máxima de Throughput).


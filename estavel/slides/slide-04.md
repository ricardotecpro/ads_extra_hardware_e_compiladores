<!-- .element: class="fragment" -->
# Aula 04 - Arquiteturas RISC vs CISC
## Apresentação

---

Por muito tempo, o ecossistema PC foi dominado pela Intel (CISC), enquanto celulares e embarcados (Raspberry Pi/STM32) focavam em ARM (RISC). Mas as linhas se cruzam hoje, especialmente com hardwares como a linha M da Apple operando em RISC com performance altíssima.

---

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🥊 1. Entendendo a Batalha

---

## 🥊 1. Entendendo a Batalha

A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas?

---

## 🥊 1. Entendendo a Batalha

### CISC (Complex Instruction Set Computer)

<span class="fragment">**Fios de Cabelo**: Possui instruções complexas que podem realizar tarefas gigantescas de uma vez (ex: "Leia da memória X, mude o bit Y, grave em Z" em apenas UMA instrução assembly).
    **Reis do pedaço**: Processadores Intel e AMD (x86_64).
    **Características**: Hardware muito complexo, consome mais energia para decodificar instruções multiformes.</span>

---

## 🥊 1. Entendendo a Batalha

### RISC (Reduced Instruction Set Computer)

<span class="fragment">**Lâmina Fina**: Possui pouquíssimas instruções, todas rápidas, simples e uniformes. Fazer "Leia da memória X, mude o bit Y, grave em Z" leva 3 a 4 comandos curtos no assembly.
    **Reis do pedaço**: Arquitetura ARM (Snapdragon, Apple Silicon M1-M3, AWS Graviton).
    **Características**: Consome pouca bateria e se destaca muito em *Pipelines* agressivos.</span>

---

## 🥊 1. Entendendo a Batalha

---

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🖨️ 2. Como isso afeta o Compilador C/C++?

---

## 🖨️ 2. Como isso afeta o Compilador C/C++?

Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas:

---

## 🖨️ 2. Como isso afeta o Compilador C/C++?

<div class="termy" markdown="1">

__CODE_BLOCK_0__

</div>

---

## 🖨️ 2. Como isso afeta o Compilador C/C++?

O código C++ original `app.c` não muda! Quem rala é o compilador, que na versão ARM gera dezenas de pequenas instruções curtas RISC, e na versão local gera um op-code gigante com microcódigos CISC internos da Intel.

---

## 🖨️ 2. Como isso afeta o Compilador C/C++?

> [!TIP]
> **Na nuvem:** A maioria dos serviços modernos baseados no Docker é Cross-Platform, mas as imagens contínuas não! Seu `Dockerfile` ou sua build em Go e Rust deve explicitamente compilar para as duplas natividades quando for fazer Load Balancer entre instâncias AWS Graviton (ARM) e Padrão (x86).

---

## 🖨️ 2. Como isso afeta o Compilador C/C++?

---

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🚀 Resumo Prático

---

## 🚀 Resumo Prático

- Historicamente, servidores eram puramente CISC (Intel).
- Hoje, o mercado clama por RISC graças à sustentabilidade térmica (menos energia e calor).
- Um bom engenheiro percebe que a ISA (aula anterior) CISC vai conter milhares de comandos Assembly, requerendo compiladores muito agressivos, enquanto a ISA RISC exigirá compiladores muito detalhistas e otimizados linearmente na alocação de registradores C/C++.

---

## 🚀 Resumo Prático

Caminho livre até aqui? Então agora vamos adentrar nas dores da "Memória".

---
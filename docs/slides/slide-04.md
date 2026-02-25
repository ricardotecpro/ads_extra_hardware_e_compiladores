<!-- .element: class="fragment" -->
# Arquiteturas RISC vs CISC
## Aula 04

---

## 🥊 1. Entendendo a Batalha

A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas?


    **Fios de Cabelo**: Possui instruções complexas que podem realizar tarefas gigantescas de uma vez (ex: "Leia da memória X, mude o bit Y, grave em Z" em apenas UMA instrução assembly).
    **Reis do pedaço**: Processadores Intel e AMD (x86_64).
    **Características**: Hardware muito complexo, consome mais energia para decodificar instruções multiformes.


    **Lâmina Fina**: Possui pouquíssimas instruções, todas rápidas, simples e uniformes. Fazer "Leia da memória X, mude o bit Y, grave em Z" leva 3 a 4 comandos curtos no assembly.
    **Reis do pedaço**: Arquitetura ARM (Snapdragon, Apple Silicon M1-M3, AWS Graviton).
    **Características**: Consome pouca bateria e se destaca muito em *Pipelines* agressivos.

---

---

## 🖨️ 2. Como isso afeta o Compilador C/C++?

Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas:

<div class="termy" markdown="1">

```console
$ # Compilando para a máquina local (digamos, x86_64 CISC)
$ gcc app.c -o app
$ # Compilando Cruzado (Cross-Compiling) de um PC x86 para rodar num Raspberry Pi (ARMv8):
$ aarch64-linux-gnu-gcc app.c -o app_arm
```

</div>

---

## 🚀 Resumo Prático

- Historicamente, servidores eram puramente CISC (Intel).
- Hoje, o mercado clama por RISC graças à sustentabilidade térmica (menos energia e calor).
- Um bom engenheiro percebe que a ISA (aula anterior) CISC vai conter milhares de comandos Assembly, requerendo compiladores muito agressivos, enquanto a ISA RISC exigirá compiladores muito detalhistas e otimizados linearmente na alocação de registradores C/C++.

Caminho livre até aqui? Então agora vamos adentrar nas dores da "Memória".
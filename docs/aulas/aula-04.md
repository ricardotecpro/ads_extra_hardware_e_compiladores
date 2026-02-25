# Aula 04 - Arquiteturas RISC vs CISC

Por muito tempo, o ecossistema PC foi dominado pela Intel (CISC), enquanto celulares e embarcados (Raspberry Pi/STM32) focavam em ARM (RISC). Mas as linhas se cruzam hoje, especialmente com hardwares como a linha M da Apple operando em RISC com performance altíssima.

---

## 🥊 1. Entendendo a Batalha

A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas?

=== "CISC (Complex Instruction Set Computer)"
    **Fios de Cabelo**: Possui instruções complexas que podem realizar tarefas gigantescas de uma vez (ex: "Leia da memória X, mude o bit Y, grave em Z" em apenas UMA instrução assembly).
    **Reis do pedaço**: Processadores Intel e AMD (x86_64).
    **Características**: Hardware muito complexo, consome mais energia para decodificar instruções multiformes.

=== "RISC (Reduced Instruction Set Computer)"
    **Lâmina Fina**: Possui pouquíssimas instruções, todas rápidas, simples e uniformes. Fazer "Leia da memória X, mude o bit Y, grave em Z" leva 3 a 4 comandos curtos no assembly.
    **Reis do pedaço**: Arquitetura ARM (Snapdragon, Apple Silicon M1-M3, AWS Graviton).
    **Características**: Consome pouca bateria e se destaca muito em *Pipelines* agressivos.

---

## 🖨️ 2. Como isso afeta o Compilador C/C++?

Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas:

<!-- termynal -->
```console
$ # Compilando para a máquina local (digamos, x86_64 CISC)
$ gcc app.c -o app
$ # Compilando Cruzado (Cross-Compiling) de um PC x86 para rodar num Raspberry Pi (ARMv8):
$ aarch64-linux-gnu-gcc app.c -o app_arm
```

O código C++ original `app.c` não muda! Quem rala é o compilador, que na versão ARM gera dezenas de pequenas instruções curtas RISC, e na versão local gera um op-code gigante com microcódigos CISC internos da Intel.

> [!TIP]
> **Na nuvem:** A maioria dos serviços modernos baseados no Docker é Cross-Platform, mas as imagens contínuas não! Seu `Dockerfile` ou sua build em Go e Rust deve explicitamente compilar para as duplas natividades quando for fazer Load Balancer entre instâncias AWS Graviton (ARM) e Padrão (x86).

---

## 🚀 Resumo Prático

- Historicamente, servidores eram puramente CISC (Intel).
- Hoje, o mercado clama por RISC graças à sustentabilidade térmica (menos energia e calor).
- Um bom engenheiro percebe que a ISA (aula anterior) CISC vai conter milhares de comandos Assembly, requerendo compiladores muito agressivos, enquanto a ISA RISC exigirá compiladores muito detalhistas e otimizados linearmente na alocação de registradores C/C++.

Caminho livre até aqui? Então agora vamos adentrar nas dores da "Memória".


---

## 🎯 Próximos Passos

<div class="grid cards" markdown>

-   :octicons-video-24: **Acessar Slides**

    ---
    
    Reveja a apresentação visual desta aula.
    
    [:octicons-arrow-right-24: Ver Slides da Aula](../slides/slide-04.html)

-   :octicons-tasklist-24: **Quiz**

    ---
    
    Teste seu entendimento básico com perguntas rápidas.
    
    [:octicons-arrow-right-24: Responder Quiz](../quizzes/quiz-04.md)

-   :octicons-pencil-24: **Exercícios**

    ---
    
    Prática avançada e dissertativa com consulta.
    
    [:octicons-arrow-right-24: Lista de Exercícios](../exercicios/exercicio-04.md)

-   :octicons-rocket-24: **Projeto**

    ---
    
    Laboratório prático de codificação em C/C++.
    
    [:octicons-arrow-right-24: Mini Projeto](../projetos/projeto-04.md)

</div>


[:octicons-arrow-right-24: Avançar para Aula 05](aula-05.md){ .md-button .md-button--primary }

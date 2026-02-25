---
theme: white
transition: convex
---

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

---

<!-- .element: class="fragment" -->
# 🧠 Quiz Rápido
## Prática de Fixação

---

### ❓ Pergunta 1
Sobre o funcionamento prático de **1. Entendendo a Batalha** explicado em sala, indique a afirmativa verdadeira:

- **A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 1

**A alternativa correta é:**

<span style="color:#42affa">A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 2
No contexto analítico de **2. Como isso afeta o Compilador C/C++?** explicado em sala, indique a afirmativa verdadeira:

- **Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 2

**A alternativa correta é:**

<span style="color:#42affa">Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 3
Ao avaliar a característica inerente a **Resumo Prático** explicado em sala, indique a afirmativa verdadeira:

- **- Historicamente, servidores eram puramente CISC (Intel). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 3

**A alternativa correta é:**

<span style="color:#42affa">- Historicamente, servidores eram puramente CISC (Intel). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 4
A respeito da arquitetura sistêmica conectada a **1. Entendendo a Batalha** explicado em sala, indique a afirmativa verdadeira:

- **A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 4

**A alternativa correta é:**

<span style="color:#42affa">A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 5
No que tange diretamente a lógica de **2. Como isso afeta o Compilador C/C++?** explicado em sala, indique a afirmativa verdadeira:

- **Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 5

**A alternativa correta é:**

<span style="color:#42affa">Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 6
Sobre o funcionamento prático de **Resumo Prático** explicado em sala, indique a afirmativa verdadeira:

- **- Historicamente, servidores eram puramente CISC (Intel). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 6

**A alternativa correta é:**

<span style="color:#42affa">- Historicamente, servidores eram puramente CISC (Intel). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 7
No contexto analítico de **1. Entendendo a Batalha** explicado em sala, indique a afirmativa verdadeira:

- **A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 7

**A alternativa correta é:**

<span style="color:#42affa">A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 8
Ao avaliar a característica inerente a **2. Como isso afeta o Compilador C/C++?** explicado em sala, indique a afirmativa verdadeira:

- **Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 8

**A alternativa correta é:**

<span style="color:#42affa">Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 9
A respeito da arquitetura sistêmica conectada a **Resumo Prático** explicado em sala, indique a afirmativa verdadeira:

- **- Historicamente, servidores eram puramente CISC (Intel). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 9

**A alternativa correta é:**

<span style="color:#42affa">- Historicamente, servidores eram puramente CISC (Intel). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 10
No que tange diretamente a lógica de **1. Entendendo a Batalha** explicado em sala, indique a afirmativa verdadeira:

- **A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 10

**A alternativa correta é:**

<span style="color:#42affa">A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

<!-- .element: class="fragment" -->
# 🥇 Conclusão Teórica
## Tópicos Superados

Você concluiu com sucesso a carga cognitiva desta apresentação teórica!

---

### 🚀 Próximas Etapas (Prática)

Agora que a conceituação inicial e os quizzes iterativos foram vencidos, aplique o conhecimento na prática:

- Acesse a plataforma e inicie o seu desafio em **Mini Projetos** de C/C++.
- Teste a fixação complexa com as questões dissertativas da **Lista de Exercícios**.


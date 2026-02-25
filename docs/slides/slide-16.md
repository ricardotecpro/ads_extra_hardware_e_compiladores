<!-- .element: class="fragment" -->
# Projeto Final: Otimização Baseada em Hardware
## Aula 16

---

## ⏱️ 1. Profiling Clássico (A Vida Real)

Adivinhar onde o código está lento é a armadilha suprema do júnior.
Usamos ferramentas robustas para que a Arquitetura Linux diga-nos onde os gargalos fervem a CPU.

* **gprof**: <span class="fragment">O padrão antigo C++. Ele recompila injetando marcações contábeis nas idas e vindas de funções, revelando "Quais chamadas consumiram O Tempo Global".</span>
* **Valgrind (Callgrind / Cachegrind):** Ferramenta extrema rodando seu executável numa sandbox virtual que mapeia cada instrução assembly. Traz gráficos massivos de onde **Ocorreram os Caches Misses** da Memória L1 de nossa Aula 06!
* **Perf**: <span class="fragment">O utilitário nativo dos programadores Linux Kernel, extraindo informações métricas em Eventos de Desvio (Branch Mispired da Aula 03) usando relógios internos dos registradores ocultos `PMU` do seu próprio Processador em tempo real, sem overhead sintético.</span>

---

---

## 🔬 2. O Grande Desafio (Mini-Projeto Prático)

O curso desafia todo programador C/C++ a desenvolver a Prova de Fogo do Hardware:

<div class="termy" markdown="1">

```console
$ # Desafio do Iterador de Matriz Contínua
$ g++ matriz_opt.cpp -O3 -o matriz
$ ./matriz 
Iteração Horizontal (Hit L1): Tempo 140ms
Iteração Vertical (Miss L1): Tempo 2100ms
```

</div>

---

## 🏆 3. Conclusão da Trilha

Você navegou nas extremas profundezas da arquitetura da Computação Modernizada.
Um engenheiro de Backend jamais olhará para `int x;` ou `for()` sem recordar os impactos térmicos, cache hits mortais de linha, L1 local, reordenações do std::atomic Memory Model ou Page Faults nos clusters de Sistema e Processos em Swap.

Parabéns pela resiliência no vale do Silício e da Matemática discreta profunda.
Nunca pare de medir e Otimizar. O Hardware dita as leis; o Software obedece.

:material-rocket: Finalizar e Visitar Projetos{ .md-button .md-button--primary }



---

<!-- .element: class="fragment" -->
# 🧠 Quiz Rápido
## Prática de Fixação

---

### Pergunta 1
Sobre o funcionamento prático de **1. Profiling Clássico (A Vida Real)** explicado em sala, indique a afirmativa verdadeira:

- **Adivinhar onde o código está lento é a armadilha suprema do júnior. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Adivinhar onde o código está lento é a armadilha suprema do júnior. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 2
No contexto analítico de **2. O Grande Desafio (Mini-Projeto Prático)** explicado em sala, indique a afirmativa verdadeira:

- **O curso desafia todo programador C/C++ a desenvolver a Prova de Fogo do Hardware: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** O curso desafia todo programador C/C++ a desenvolver a Prova de Fogo do Hardware: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 3
Ao avaliar a característica inerente a **3. Conclusão da Trilha** explicado em sala, indique a afirmativa verdadeira:

- **Você navegou nas extremas profundezas da arquitetura da Computação Modernizada. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Você navegou nas extremas profundezas da arquitetura da Computação Modernizada. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 4
A respeito da arquitetura sistêmica conectada a **1. Profiling Clássico (A Vida Real)** explicado em sala, indique a afirmativa verdadeira:

- **Adivinhar onde o código está lento é a armadilha suprema do júnior. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Adivinhar onde o código está lento é a armadilha suprema do júnior. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 5
No que tange diretamente a lógica de **2. O Grande Desafio (Mini-Projeto Prático)** explicado em sala, indique a afirmativa verdadeira:

- **O curso desafia todo programador C/C++ a desenvolver a Prova de Fogo do Hardware: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** O curso desafia todo programador C/C++ a desenvolver a Prova de Fogo do Hardware: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 6
Sobre o funcionamento prático de **3. Conclusão da Trilha** explicado em sala, indique a afirmativa verdadeira:

- **Você navegou nas extremas profundezas da arquitetura da Computação Modernizada. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Você navegou nas extremas profundezas da arquitetura da Computação Modernizada. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 7
No contexto analítico de **1. Profiling Clássico (A Vida Real)** explicado em sala, indique a afirmativa verdadeira:

- **Adivinhar onde o código está lento é a armadilha suprema do júnior. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Adivinhar onde o código está lento é a armadilha suprema do júnior. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 8
Ao avaliar a característica inerente a **2. O Grande Desafio (Mini-Projeto Prático)** explicado em sala, indique a afirmativa verdadeira:

- **O curso desafia todo programador C/C++ a desenvolver a Prova de Fogo do Hardware: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** O curso desafia todo programador C/C++ a desenvolver a Prova de Fogo do Hardware: *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 9
A respeito da arquitetura sistêmica conectada a **3. Conclusão da Trilha** explicado em sala, indique a afirmativa verdadeira:

- **Você navegou nas extremas profundezas da arquitetura da Computação Modernizada. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Você navegou nas extremas profundezas da arquitetura da Computação Modernizada. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 10
No que tange diretamente a lógica de **1. Profiling Clássico (A Vida Real)** explicado em sala, indique a afirmativa verdadeira:

- **Adivinhar onde o código está lento é a armadilha suprema do júnior. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Adivinhar onde o código está lento é a armadilha suprema do júnior. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>
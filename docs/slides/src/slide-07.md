---
theme: white
transition: convex
---

<!-- .element: class="fragment" -->
# Stack vs Heap
## Aula 07

---

## 🧱 1. A Pilha (Stack)

A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out). 


    - **Performance Imediata**: Não sofre do atraso monumental do Sistema Operacional rodando scripts para achar buracos vazios. A CPU avança 1 pino de hardware no SP (Stack Pointer) e empilha na RAM. Retirou, ele decrementa. Super rápido.
    - **Anti-Vazamento Automático**: Funções extintas são imediatamente retiradas (*popped*) num clique atômico LIFO e as fatias voltam a uso global. Memória protegida contra vazamentos lógicos (*memory leaks*) por definição estrita.
    - **Quente da CPU**: Frequentemente preza por Cache Hit. A Stack costuma viver majoritariamente no limiar da L1 Data Cache.

> [!CAUTION]
> Stack Overflow! A Pilha nunca é infinita, sendo tipicamente restrita pelo S.O. Windows/Linux (geralmente entre 1MB a 8MB max num Kernel Padrão X86). Tentar criar um `int array[9999999]` puro no escopo sem alocação dinâmica explodirá a Pilha e esmagará cruelmente (o temido `Segmentation Fault (core dumped)`).

---

---

## 📦 2. O Monte (Heap)

Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação Dinâmica).

<div class="termy" markdown="1">

```console
$ # Como você interage em baixo nível (C/C++)
$ cat code.c
#include <stdlib.h>

int main() {
    // malloc vai no Sistema Operacional e chora pedindo: "Me dê 10 inteiros!"
    int* array_gigante_dinamico = (int*)malloc(10 * sizeof(int));
    
    // Se você não limpar usando free(), a RAM apodrecerá lentamente (LEAK)
    free(array_gigante_dinamico);
}
```

---

## 💀 3. Memory Leaks (Vazamentos de Memória)

Um clássico e letal bug de engenharia C++. Quando o desenvolvedor executa `new` ou `malloc` solicitando memória do **Heap**, mas quebra regras do fluxo perdendo o contato formal do **ponteiro** retornado do hardware sem antes ter reportado o fim via `delete` ou `free`.
Resultado?  Aquela fatia na RAM física do servidor Linux ficará congelada, cega, retida unicamente pro seu app até que a nuvem AWS exaure toda a máquina do container num erro de Kernel `OOM Killer (Out Of Memory)`.

Em contra-partida: *Dangling Pointers*. Usar a área que o ponteiro apontava *depois* da libertação formal do free provoca instabilidade instantânea e corrupção silenciosa nos endereços da placa-mãe.

---

## 🚀 Resumo Prático

- Se não sabe onde colocar: Bote no STACK.
- É muito grande pra caber (Strings longas ou Arrays): Invoque HEAP com o `std::vector` (ele gerencia o malloc e free na destruição de escopo).



---

<!-- .element: class="fragment" -->
# 🧠 Quiz Rápido
## Prática de Fixação

---

### Pergunta 1
Sobre o funcionamento prático de **1. A Pilha (Stack)** explicado em sala, indique a afirmativa verdadeira:

- **A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 2
No contexto analítico de **2. O Monte (Heap)** explicado em sala, indique a afirmativa verdadeira:

- **Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação D... *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação D... *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 3
Ao avaliar a característica inerente a **3. Memory Leaks (Vazamentos de Memória)** explicado em sala, indique a afirmativa verdadeira:

- **Um clássico e letal bug de engenharia C++. Quando o desenvolvedor executa `new` ou `malloc` solicitando memória do **Heap**, mas quebra regras do fluxo perdendo o contato formal do **ponteiro** retornado do hardware sem ... *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Um clássico e letal bug de engenharia C++. Quando o desenvolvedor executa `new` ou `malloc` solicitando memória do **Heap**, mas quebra regras do fluxo perdendo o contato formal do **ponteiro** retornado do hardware sem ... *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 4
A respeito da arquitetura sistêmica conectada a **Resumo Prático** explicado em sala, indique a afirmativa verdadeira:

- **- Se não sabe onde colocar: Bote no STACK. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** - Se não sabe onde colocar: Bote no STACK. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 5
No que tange diretamente a lógica de **1. A Pilha (Stack)** explicado em sala, indique a afirmativa verdadeira:

- **A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 6
Sobre o funcionamento prático de **2. O Monte (Heap)** explicado em sala, indique a afirmativa verdadeira:

- **Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação D... *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação D... *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 7
No contexto analítico de **3. Memory Leaks (Vazamentos de Memória)** explicado em sala, indique a afirmativa verdadeira:

- **Um clássico e letal bug de engenharia C++. Quando o desenvolvedor executa `new` ou `malloc` solicitando memória do **Heap**, mas quebra regras do fluxo perdendo o contato formal do **ponteiro** retornado do hardware sem ... *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Um clássico e letal bug de engenharia C++. Quando o desenvolvedor executa `new` ou `malloc` solicitando memória do **Heap**, mas quebra regras do fluxo perdendo o contato formal do **ponteiro** retornado do hardware sem ... *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 8
Ao avaliar a característica inerente a **Resumo Prático** explicado em sala, indique a afirmativa verdadeira:

- **- Se não sabe onde colocar: Bote no STACK. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** - Se não sabe onde colocar: Bote no STACK. *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 9
A respeito da arquitetura sistêmica conectada a **1. A Pilha (Stack)** explicado em sala, indique a afirmativa verdadeira:

- **A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>

---

### Pergunta 10
No que tange diretamente a lógica de **2. O Monte (Heap)** explicado em sala, indique a afirmativa verdadeira:

- **Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação D... *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

<span class="fragment">

**✅ Resposta:** Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação D... *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*

**
</span>


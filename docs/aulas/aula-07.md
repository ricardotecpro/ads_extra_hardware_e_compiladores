# Aula 07 - Stack vs Heap

Agora mergulhamos no coração cirúrgico da engenharia C/C++: "Onde o S.O. decide alocar e liberar a sua variável física real na memória?". Essa escolha define vida, morte e performance do algoritmo em tempo real.

---

## 🧱 1. A Pilha (Stack)

A Stack é a fundação natural de blocos de toda variável ordinariamente declarada dentro do escopo de funções em C/C++ (`int x`, `float y`). Ela trabalha rigorosamente sob o conceito LIFO (Last In, First Out). 

=== "Vantagens C/C++ da Pilha"
    - **Performance Imediata**: Não sofre do atraso monumental do Sistema Operacional rodando scripts para achar buracos vazios. A CPU avança 1 pino de hardware no SP (Stack Pointer) e empilha na RAM. Retirou, ele decrementa. Super rápido.
    - **Anti-Vazamento Automático**: Funções extintas são imediatamente retiradas (*popped*) num clique atômico LIFO e as fatias voltam a uso global. Memória protegida contra vazamentos lógicos (*memory leaks*) por definição estrita.
    - **Quente da CPU**: Frequentemente preza por Cache Hit. A Stack costuma viver majoritariamente no limiar da L1 Data Cache.

> [!CAUTION]
> Stack Overflow! A Pilha nunca é infinita, sendo tipicamente restrita pelo S.O. Windows/Linux (geralmente entre 1MB a 8MB max num Kernel Padrão X86). Tentar criar um `int array[9999999]` puro no escopo sem alocação dinâmica explodirá a Pilha e esmagará cruelmente (o temido `Segmentation Fault (core dumped)`).

---

## 📦 2. O Monte (Heap)

Enquanto a Pilha é rígida, restrita e pré-delimitada, o Monte (Heap) é um vasto oceano caótico de Gigabytes gerenciado pelo Kernel do S.O. (Sistemas Operacionais). Você requer pedaços de memória "sob demanda" (Alocação Dinâmica).

<!-- termynal -->
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

=== "Diferenciais do C/C++"
    Você é o único árbitro. Diferente de Java, Python ou C# que usam complexos robôs vasculhadores ocultos (*Garbage Collectors*) na sombra consumindo até 20% do processador para auditar seu Heap e limpar os lixos. O Rust automatiza e barra alocações indevidas usando Ownership sem o robozinho. O C++ fornece ferramentas novas e maduras (`std::unique_ptr` ou `std::shared_ptr`) baseadas na contagem de referência.

---

## 💀 3. Memory Leaks (Vazamentos de Memória)

Um clássico e letal bug de engenharia C++. Quando o desenvolvedor executa `new` ou `malloc` solicitando memória do **Heap**, mas quebra regras do fluxo perdendo o contato formal do **ponteiro** retornado do hardware sem antes ter reportado o fim via `delete` ou `free`.
Resultado?  Aquela fatia na RAM física do servidor Linux ficará congelada, cega, retida unicamente pro seu app até que a nuvem AWS exaure toda a máquina do container num erro de Kernel `OOM Killer (Out Of Memory)`.

Em contra-partida: *Dangling Pointers*. Usar a área que o ponteiro apontava *depois* da libertação formal do free provoca instabilidade instantânea e corrupção silenciosa nos endereços da placa-mãe.

## 🚀 Resumo Prático

- Se não sabe onde colocar: Bote no STACK.
- É muito grande pra caber (Strings longas ou Arrays): Invoque HEAP com o `std::vector` (ele gerencia o malloc e free na destruição de escopo).



---

## 🎯 Próximos Passos

<div class="grid cards" markdown>

-   :octicons-video-24: **Acessar Slides**

    ---
    
    Reveja a apresentação visual desta aula.
    
    [:octicons-arrow-right-24: Ver Slides da Aula](../slides/slide-07.html)

-   :octicons-tasklist-24: **Quiz**

    ---
    
    Teste seu entendimento básico com perguntas rápidas.
    
    [:octicons-arrow-right-24: Responder Quiz](../quizzes/quiz-07.md)

-   :octicons-pencil-24: **Exercícios**

    ---
    
    Prática avançada e dissertativa com consulta.
    
    [:octicons-arrow-right-24: Lista de Exercícios](../exercicios/exercicio-07.md)

-   :octicons-rocket-24: **Projeto**

    ---
    
    Laboratório prático de codificação em C/C++.
    
    [:octicons-arrow-right-24: Mini Projeto](../projetos/projeto-07.md)

</div>


[:octicons-arrow-right-24: Avançar para Aula 08](aula-08.md){ .md-button .md-button--primary }

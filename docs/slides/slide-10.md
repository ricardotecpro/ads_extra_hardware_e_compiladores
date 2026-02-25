<!-- .element: class="fragment" -->
# Sincronização e Concorrência
## Aula 10

---

## 🏎️ 1. O Data Race: Uma Colisão Inevitável

Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".
O HW (Processador) traduz internamente num RMW: **R**ead (*Puxa os 100 da RAM para o Registrador EAX*), **M**odify (*Adiciona +10 e vira 110 na ALU*), e **W**rite (*Substitui na RAM os antigos 100 por 110*).

Se na fresta entre a **Thread 1** preencher o EAX e depois descer ao RAM o valor 110... a **Thread 2** rodar e "puxar os mesmíssimos originais 100" para outro registrador (Context Switch), quando abas enviarem pra RAM final as sobreposições as contas, um dos `10` desvanecerá, o banco perde e a variável fica logicamente corrompida.

---

---

## 🛡️ 2. Mutex e The Critical Section

A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion).

<div class="termy" markdown="1">

```console
$ # Em C++, protege-se a variável central assim:
$ cat bank.cpp
std::mutex portaCorredor;

void adiciona_10() {
    portaCorredor.lock();   // O Hardware garante atomicamente exclusão
    balance += 10;          // Apenas UM transita aqui adentro. 
    portaCorredor.unlock(); // O primeiro sai da sala, e notifica o Kernel
}
```

---

## 🚦 3. O Dilema: Deadlock

Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado?

Ambos processos morrem na tela, dormindo inertes (*Blocked State*), enquanto a barra de % CPU despenca lentamente para ZERO! Seu Sistema Paralelo entrou em **Deadlock**. (O Abraço Mortal Padrão The Dining Philosophers). Um design multi-thread exige uma heuristica sagrada de adquirir as trancas Lock C++ em idêntica e constante ordem arquitetural através dos sistemas, ou apelar a mecânicas `std::lock()` que aplicam garantias subjacentes do Kernel.

---

## 🚀 Resumo Prático

- **Mutex**: <span class="fragment">Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM).</span>
- Se a concorrência não tiver "Seção Crítica" que lida com Gravação e tiver "Só Read-only", não aplique trancas (Mutex) para não serializar as Threads da máquina.

---

<!-- .element: class="fragment" -->
# 🧠 Quiz Rápido
## Prática de Fixação

---

### ❓ Pergunta 1
Sobre o funcionamento prático de **1. O Data Race: Uma Colisão Inevitável** explicado em sala, indique a afirmativa verdadeira:

- **Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento". *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 1

**A alternativa correta é:**

<span style="color:#42affa">Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento". *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 2
No contexto analítico de **2. Mutex e The Critical Section** explicado em sala, indique a afirmativa verdadeira:

- **A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 2

**A alternativa correta é:**

<span style="color:#42affa">A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 3
Ao avaliar a característica inerente a **3. O Dilema: Deadlock** explicado em sala, indique a afirmativa verdadeira:

- **Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 3

**A alternativa correta é:**

<span style="color:#42affa">Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 4
A respeito da arquitetura sistêmica conectada a **Resumo Prático** explicado em sala, indique a afirmativa verdadeira:

- **- **Mutex**: <span class="fragment">Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***</span>
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 4

**A alternativa correta é:**

<span style="color:#42affa">- **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 5
No que tange diretamente a lógica de **1. O Data Race: Uma Colisão Inevitável** explicado em sala, indique a afirmativa verdadeira:

- **Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento". *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 5

**A alternativa correta é:**

<span style="color:#42affa">Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento". *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 6
Sobre o funcionamento prático de **2. Mutex e The Critical Section** explicado em sala, indique a afirmativa verdadeira:

- **A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 6

**A alternativa correta é:**

<span style="color:#42affa">A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 7
No contexto analítico de **3. O Dilema: Deadlock** explicado em sala, indique a afirmativa verdadeira:

- **Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 7

**A alternativa correta é:**

<span style="color:#42affa">Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado? *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 8
Ao avaliar a característica inerente a **Resumo Prático** explicado em sala, indique a afirmativa verdadeira:

- **- **Mutex**: <span class="fragment">Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***</span>
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 8

**A alternativa correta é:**

<span style="color:#42affa">- **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 9
A respeito da arquitetura sistêmica conectada a **1. O Data Race: Uma Colisão Inevitável** explicado em sala, indique a afirmativa verdadeira:

- **Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento". *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 9

**A alternativa correta é:**

<span style="color:#42affa">Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento". *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

---

### ❓ Pergunta 10
No que tange diretamente a lógica de **2. Mutex e The Critical Section** explicado em sala, indique a afirmativa verdadeira:

- **A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.***
- É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.
- Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.
- A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.

---

### ✅ Resposta - Pergunta 10

**A alternativa correta é:**

<span style="color:#42affa">A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion). *feedback: Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*</span>

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
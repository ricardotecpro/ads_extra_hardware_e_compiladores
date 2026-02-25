<!-- .element: class="fragment" -->
# Aula 10 - Sincronização e Concorrência
## Apresentação

---

Como abordado na Aula 09, a vantagem da extrema performance das *Threads* nativas possuírem acesso irrestrito e descontrolado à mesma Memória do processo C++ pode culminar na tragédia iminente conhecida como de **Condição de Corrida (Race Condition)**.

---

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🏎️ 1. O Data Race: Uma Colisão Inevitável

---

## 🏎️ 1. O Data Race: Uma Colisão Inevitável

Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".
O HW (Processador) traduz internamente num RMW: **R**ead (*Puxa os 100 da RAM para o Registrador EAX*), **M**odify (*Adiciona +10 e vira 110 na ALU*), e **W**rite (*Substitui na RAM os antigos 100 por 110*).

Se na fresta entre a **Thread 1** preencher o EAX e depois descer ao RAM o valor 110... a **Thread 2** rodar e "puxar os mesmíssimos originais 100" para outro registrador (Context Switch), quando abas enviarem pra RAM final as sobreposições as contas, um dos `10` desvanecerá, o banco perde e a variável fica logicamente corrompida.

---

## 🏎️ 1. O Data Race: Uma Colisão Inevitável

---

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🛡️ 2. Mutex e The Critical Section

---

## 🛡️ 2. Mutex e The Critical Section

A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion).

---

## 🛡️ 2. Mutex e The Critical Section

<!-- termynal -->
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

## 🛡️ 2. Mutex e The Critical Section

A área demarcada pelo *lock* a *unlock* é intitulada **Seção Crítica**. O poder e o problema do design residem aí: Se você for preguiçoso e prender 10.000 linhas da sua transação atrás da Seção Crítica Mestre, o teu glorioso Processador *Multicore Ultra de 32 cores* se comportará como um ridículo e solitário Processador Antigo Pentium de *1 core* single Threaded, derrubando teu design ao zero! Tudo vai rodar Enfileirado (Serializado). O bom C++ trava com extrema granuladidade e rapidíssimo na variável.

---

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🚦 3. O Dilema: Deadlock

---

## 🚦 3. O Dilema: Deadlock

Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado?

Ambos processos morrem na tela, dormindo inertes (*Blocked State*), enquanto a barra de % CPU despenca lentamente para ZERO! Seu Sistema Paralelo entrou em **Deadlock**. (O Abraço Mortal Padrão The Dining Philosophers). Um design multi-thread exige uma heuristica sagrada de adquirir as trancas Lock C++ em idêntica e constante ordem arquitetural através dos sistemas, ou apelar a mecânicas `std::lock()` que aplicam garantias subjacentes do Kernel.

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🚀 Resumo Prático

---

## 🚀 Resumo Prático

- **Mutex**: <span class="fragment">Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM).</span>
- Se a concorrência não tiver "Seção Crítica" que lida com Gravação e tiver "Só Read-only", não aplique trancas (Mutex) para não serializar as Threads da máquina.

---

## 🚀 Resumo Prático

---
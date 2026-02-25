# Solução e Explicação Detalhada: Aula 10 - Sincronização e Concorrência

Abaixo estão as respostas esperadas e o embasamento teórico para os exercícios propostos na **Aula 10**.

## Solução da Questão 1 - 1. O Data Race: Uma Colisão Inevitável (Básico 1)
**Explicação Detalhada do Assunto:**

Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".

O HW (Processador) traduz internamente num RMW: **R**ead (*Puxa os 100 da RAM para o Registrador EAX*), **M**odify (*Adiciona +10 e vira 110 na ALU*), e **W**rite (*Substitui na RAM os antigos 100 por 110*).

Se na fresta entre a **Thread 1** preencher o EAX e depois descer ao RAM o valor 110... a **Thread 2** rodar e "puxar os mesmíssimos originais 100" para outro registrador (Context Switch), quando abas enviarem pra RAM final as sobreposições as contas, um dos `10` desvanecerá, o banco perde e a variável fica logicamente corrompida.

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *1. O Data Race: Uma Colisão Inevitável* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 2 - 2. Mutex e The Critical Section (Básico 2)
**Explicação Detalhada do Assunto:**

A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion).





A área demarcada pelo *lock* a *unlock* é intitulada **Seção Crítica**. O poder e o problema do design residem aí: Se você for preguiçoso e prender 10.000 linhas da sua transação atrás da Seção Crítica Mestre, o teu glorioso Processador *Multicore Ultra de 32 cores* se comportará como um ridículo e solitário Processador Antigo Pentium de *1 core* single Threaded, derrubando teu design ao zero! Tudo vai rodar Enfileirado (Serializado). O bom C++ trava com extrema granuladidade e rapidíssimo na variável.

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *2. Mutex e The Critical Section* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 3 - 3. O Dilema: Deadlock (Intermediário 1)
**Explicação Detalhada do Assunto:**

Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado?

Ambos processos morrem na tela, dormindo inertes (*Blocked State*), enquanto a barra de % CPU despenca lentamente para ZERO! Seu Sistema Paralelo entrou em **Deadlock**. (O Abraço Mortal Padrão The Dining Philosophers). Um design multi-thread exige uma heuristica sagrada de adquirir as trancas Lock C++ em idêntica e constante ordem arquitetural através dos sistemas, ou apelar a mecânicas `std::lock()` que aplicam garantias subjacentes do Kernel.

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *3. O Dilema: Deadlock* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 4 - Resumo Prático (Intermediário 2)
**Explicação Detalhada do Assunto:**

- **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM).

- Se a concorrência não tiver "Seção Crítica" que lida com Gravação e tiver "Só Read-only", não aplique trancas (Mutex) para não serializar as Threads da máquina.



!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *Resumo Prático* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 5 - 1. O Data Race: Uma Colisão Inevitável (Desafio)
**Explicação Detalhada do Assunto:**

Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".

O HW (Processador) traduz internamente num RMW: **R**ead (*Puxa os 100 da RAM para o Registrador EAX*), **M**odify (*Adiciona +10 e vira 110 na ALU*), e **W**rite (*Substitui na RAM os antigos 100 por 110*).

Se na fresta entre a **Thread 1** preencher o EAX e depois descer ao RAM o valor 110... a **Thread 2** rodar e "puxar os mesmíssimos originais 100" para outro registrador (Context Switch), quando abas enviarem pra RAM final as sobreposições as contas, um dos `10` desvanecerá, o banco perde e a variável fica logicamente corrompida.

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *1. O Data Race: Uma Colisão Inevitável* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-10.md){ .md-button }

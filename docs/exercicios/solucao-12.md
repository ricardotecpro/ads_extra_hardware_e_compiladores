# Solução e Explicação Detalhada: Aula 12 - O Modelo de Memória

Abaixo estão as respostas esperadas e o embasamento teórico para os exercícios propostos na **Aula 12**.

## Solução da Questão 1 - 1. A Reordenação do Compilador e CPU (Out-Of-Order Execution) (Básico 1)
**Explicação Detalhada do Assunto:**

Você codifica:

Um programador esperançoso diz: "Vou ler a váriavel na Thread Oposta (Main)... e quando `FLAG` for *true*, sei que `X` é impreterivelmente *42* pois executei a linha acima primeiro na tela!"

1. O Compilador C++ (GCC -O3) pode achar que o PASSO B é irrelevante para o PASSO A (não usam das mesmas métricas) e *reordenar* por conta própria o seu executável para gravar a FLAG e depois o 42 nas linhas do assembly.

2. O CISC (Intel x86) Processador Superscalar Out-Of-Order percebe que a posição de `x` estava fria na Cache L3, mas a variável `FLAG` estava quente presa na L1D. Ele salva na FLAG imediatamente (*Store Buffers*), adiantando a etapa 2, antes da 1, para não morrer de ócio no Pipeline. E seu código multi-thread infarta com B chegando a ser lido remotamente como *TRUE* com A ainda em `0` (*zero*)!!

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 2 - 2. O Memory Model (Consistências e Barreiras) (Básico 2)
**Explicação Detalhada do Assunto:**

O C++11 emitiu formalmente o seu universal **Memory Model** definindo através da biblioteca `std::atomic` o que o Hardware tem permições para *Adiantar* vs *Trancar*.

1. Relaxed Consistensy (`std::memory_order_relaxed`): A CPU é dona, reordene como quiser em torno da sua vizinhança na RAM, apenas aplique na thread isolada em segurança. Performance brutal.

2. Release / Acquire (`std::memory_order_acquire / release`): O padrão para transferir fardos (como ler a Fila sem locks e sem medo da Out-Of-Order embaralhar *flags* finalizadoras de *Loop* C++ no hardware alheio do *Core 2).

3. Sequential Consistency (`std::memory_order_seq_cst`): O C++ por default invoca barreiras completas absolutas elétricas. Força todas as cores (L1/L2) da CPU e do compilador a não alterarem NADA a ordem que seu texto determinou. Seguro, mas castrador de velocidade em processadores ARM.

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *2. O Memory Model (Consistências e Barreiras)* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 3 - 3. Memory Barriers (Fences) nas CPUs (Intermediário 1)
**Explicação Detalhada do Assunto:**

Se não tivessemos essa lei `std::atomic` no standard oficial do GCC, programávamos via "Gambiarra Intrinseca" de Processador (Ex: Comando Assembler **MFENCE** ou **SFENCE** no Intel). Os Fences proíbem categoricamente a travessia de saltos das sub-operações em Assembly, estancando a execução como um sinaleiro fechado.

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *3. Memory Barriers (Fences) nas CPUs* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 4 - Resumo Prático (Intermediário 2)
**Explicação Detalhada do Assunto:**

- Se duas "Threads" conversam através das mesmas variáveis limpas de C e não possuam `std::mutex` da aula 10 as blindando, USE **`std::atomic<bool>`**. Do contrário você é uma vítima da *Superscalar Out Of Order Intel Architecture Pipeline* (a reordenação elétrica).

Isso enterra as nuances sombrias das memórias RAM + Cache. Agora mergulhemos no escuro do "Lento Discovoador": Os Armazenamentos (Avançar).



!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *Resumo Prático* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 5 - 1. A Reordenação do Compilador e CPU (Out-Of-Order Execution) (Desafio)
**Explicação Detalhada do Assunto:**

Você codifica:

Um programador esperançoso diz: "Vou ler a váriavel na Thread Oposta (Main)... e quando `FLAG` for *true*, sei que `X` é impreterivelmente *42* pois executei a linha acima primeiro na tela!"

1. O Compilador C++ (GCC -O3) pode achar que o PASSO B é irrelevante para o PASSO A (não usam das mesmas métricas) e *reordenar* por conta própria o seu executável para gravar a FLAG e depois o 42 nas linhas do assembly.

2. O CISC (Intel x86) Processador Superscalar Out-Of-Order percebe que a posição de `x` estava fria na Cache L3, mas a variável `FLAG` estava quente presa na L1D. Ele salva na FLAG imediatamente (*Store Buffers*), adiantando a etapa 2, antes da 1, para não morrer de ócio no Pipeline. E seu código multi-thread infarta com B chegando a ser lido remotamente como *TRUE* com A ainda em `0` (*zero*)!!

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-12.md){ .md-button }

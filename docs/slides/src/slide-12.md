---
theme: white
transition: convex
---

<!-- .element: class="fragment" -->
# O Modelo de Memória
## Aula 12

---

## 🔀 1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)

Você codifica:
```cpp
int x = 0;
int FLAG = false;

// Em uma Thread Secundária
x = 42;         // PASSO A
FLAG = true;    // PASSO B
```

Um programador esperançoso diz: "Vou ler a váriavel na Thread Oposta (Main)... e quando `FLAG` for *true*, sei que `X` é impreterivelmente *42* pois executei a linha acima primeiro na tela!"

**FALSO! MORTALMENTE FALSO!**

---

## 🚧 2. O Memory Model (Consistências e Barreiras)

O C++11 emitiu formalmente o seu universal **Memory Model** definindo através da biblioteca `std::atomic` o que o Hardware tem permições para *Adiantar* vs *Trancar*.

1. **Relaxed Consistensy** (`std::memory_order_relaxed`): A CPU é dona, reordene como quiser em torno da sua vizinhança na RAM, apenas aplique na thread isolada em segurança. Performance brutal.
2. **Release / Acquire** (`std::memory_order_acquire / release`): O padrão para transferir fardos (como ler a Fila sem locks e sem medo da Out-Of-Order embaralhar *flags* finalizadoras de *Loop* C++ no hardware alheio do *Core 2).
3. **Sequential Consistency** (`std::memory_order_seq_cst`): O C++ por default invoca barreiras completas absolutas elétricas. Força todas as cores (L1/L2) da CPU e do compilador a não alterarem NADA a ordem que seu texto determinou. Seguro, mas castrador de velocidade em processadores ARM.

---

---

## 🧱 3. Memory Barriers (Fences) nas CPUs

Se não tivessemos essa lei `std::atomic` no standard oficial do GCC, programávamos via "Gambiarra Intrinseca" de Processador (Ex: Comando Assembler **MFENCE** ou **SFENCE** no Intel). Os Fences proíbem categoricamente a travessia de saltos das sub-operações em Assembly, estancando a execução como um sinaleiro fechado.

> [!INFO]
> É por isso que programar Software Infra-estrutural de Baixo Nível (Databases, Motores de Redes Socket, SO Kernel Driver) é extremamente difícil: As reordenações da CPU nunca acontecem quando você depura linha a linha na IDE (pois a paralela não é instigada). Elas só geram *corrupções bizarras randômicas 1x na vida e morrem meses na escura neblina de servidores reais operando 100 mil Requests por Minuto no DataCenter*. Onde a pressão elástica exaure as Caches e expõe seus Bugs de Memory Models relaxados.

---

## 🚀 Resumo Prático

- Se duas "Threads" conversam através das mesmas variáveis limpas de C e não possuam `std::mutex` da aula 10 as blindando, USE **`std::atomic<bool>`**. Do contrário você é uma vítima da *Superscalar Out Of Order Intel Architecture Pipeline* (a reordenação elétrica).

Isso enterra as nuances sombrias das memórias RAM + Cache. Agora mergulhemos no escuro do "Lento Discovoador": Os Armazenamentos (Avançar).



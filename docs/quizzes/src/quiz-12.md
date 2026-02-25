# Quiz 12 - Aula 12 - O Modelo de Memória

**Avaliação Sistemática**

1. Segundo a aula 12, ao abordarmos o tópico de **1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)**, qual a premissa tecnológica subjacente a este conceito?

    - [x] Você codifica: *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

2. Segundo a aula 12, ao abordarmos o tópico de **2. O Memory Model (Consistências e Barreiras)**, qual a premissa tecnológica subjacente a este conceito?

    - [x] O C++11 emitiu formalmente o seu universal **Memory Model** definindo através da biblioteca `std::atomic` o que o Hardware tem permições para *Adiantar* vs *Trancar*. *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

3. Segundo a aula 12, ao abordarmos o tópico de **3. Memory Barriers (Fences) nas CPUs**, qual a premissa tecnológica subjacente a este conceito?

    - [x] Se não tivessemos essa lei `std::atomic` no standard oficial do GCC, programávamos via "Gambiarra Intrinseca" de Processador (Ex: Comando Assembler **MFENCE** ou **SFENCE** no Inte... *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

4. Segundo a aula 12, ao abordarmos o tópico de **Resumo Prático**, qual a premissa tecnológica subjacente a este conceito?

    - [x] - Se duas "Threads" conversam através das mesmas variáveis limpas de C e não possuam `std::mutex` da aula 10 as blindando, USE **`std::atomic<bool>`**. Do contrário você é uma víti... *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.


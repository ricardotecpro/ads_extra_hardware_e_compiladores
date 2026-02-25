# Quiz 10 - Aula 10 - Sincronização e Concorrência

**Avaliação Sistemática**

1. Segundo a aula 10, ao abordarmos o tópico de **1. O Data Race: Uma Colisão Inevitável**, qual a premissa tecnológica subjacente a este conceito?

    - [x] Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento". *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

2. Segundo a aula 10, ao abordarmos o tópico de **2. Mutex e The Critical Section**, qual a premissa tecnológica subjacente a este conceito?

    - [x] A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::m... *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

3. Segundo a aula 10, ao abordarmos o tópico de **3. O Dilema: Deadlock**, qual a premissa tecnológica subjacente a este conceito?

    - [x] Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado? *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

4. Segundo a aula 10, ao abordarmos o tópico de **Resumo Prático**, qual a premissa tecnológica subjacente a este conceito?

    - [x] - **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM). *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.


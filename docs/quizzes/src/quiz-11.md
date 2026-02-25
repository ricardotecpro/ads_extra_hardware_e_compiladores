# Quiz 11 - Aula 11 - Paralelismo no Hardware

**Avaliação Sistemática**

1. Segundo a aula 11, ao abordarmos o tópico de **1. Multi-Core (Múltiplos Núcleos)**, qual a premissa tecnológica subjacente a este conceito?

    - [x] Diferente do passado, onde havia um único núcleo saltando entre aplicativos (Context Switch), hoje temos vários núcleos físicos no mesmo invólucro (Chip). *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

2. Segundo a aula 11, ao abordarmos o tópico de **2. Hyper-Threading (SMT - Symmetrical Multi-Threading)**, qual a premissa tecnológica subjacente a este conceito?

    - [x] A mágica comercial da Intel e AMD nos anos 2000. Como fazer "1 Core Físico" fingir ser "2 Cores Lógicos" para o Windows/Linux? *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

3. Segundo a aula 11, ao abordarmos o tópico de **3. GPUs: O Paralelismo Maciço**, qual a premissa tecnológica subjacente a este conceito?

    - [x] CPUs (Processadores) foram feitos para "Serem Rápidos executando sequências lógicas e IFs complexos". Possuem Caches gigantes. *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

4. Segundo a aula 11, ao abordarmos o tópico de **Resumo Prático**, qual a premissa tecnológica subjacente a este conceito?

    - [x] - **Task Paralelism**: Se tens lógica variada, use a *CPU Multi-Core C++ thread pool*. *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.


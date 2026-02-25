# Quiz 14 - Aula 14 - Sistemas de Arquivos

**Avaliação Sistemática**

1. Segundo a aula 14, ao abordarmos o tópico de **1. O V-Node / Inode**, qual a premissa tecnológica subjacente a este conceito?

    - [x] Se no seu PC existe a pasta `Docs/foto.jpg`, no fundo, o Linux não rastreia o texto "foto.jpg" para pular de cluster em cluster. *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

2. Segundo a aula 14, ao abordarmos o tópico de **2. Journaling (A Prova contra Quedas)**, qual a premissa tecnológica subjacente a este conceito?

    - [x] Mudar um arquivo é uma transação: Apagar o velho, escrever o novo, mudar o Inode. *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

3. Segundo a aula 14, ao abordarmos o tópico de **3. Buffers e Page Cache (Por que Linux é Rápido)**, qual a premissa tecnológica subjacente a este conceito?

    - [x] "Escrever no disco" via SysCall C++ `write()` ou `fwrite()` raramente vai pro HD! *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.

4. Segundo a aula 14, ao abordarmos o tópico de **Resumo Prático**, qual a premissa tecnológica subjacente a este conceito?

    - [x] - Ao usar C/C++, chame o instrínseco `fsync()` se seu App for um Banco de Dados ou Software Crítico Bancário forçando a Cache RAM descarregar a força e salvar permanentemente no si... *feedback: Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*
    - [ ] É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.
    - [ ] A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.
    - [ ] Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.


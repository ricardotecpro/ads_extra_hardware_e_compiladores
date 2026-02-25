# Quiz 12 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Sobre o funcionamento prático de **1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)** explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">Você codifica:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. No contexto analítico de **2. O Memory Model (Consistências e Barreiras)** explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">O C++11 emitiu formalmente o seu universal **Memory Model** definindo através da biblioteca `std::atomic` o que o Hardware tem permições para *Adiantar* vs *Trancar*.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Ao avaliar a característica inerente a **3. Memory Barriers (Fences) nas CPUs** explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">Se não tivessemos essa lei `std::atomic` no standard oficial do GCC, programávamos via "Gambiarra Intrinseca" de Processador (Ex: Comando Assembler **MFENCE** ou **SFENCE** no Intel). Os Fences proíbem categoricamente a ...</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. A respeito da arquitetura sistêmica conectada a **Resumo Prático** explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">- Se duas "Threads" conversam através das mesmas variáveis limpas de C e não possuam `std::mutex` da aula 10 as blindando, USE **`std::atomic<bool>`**. Do contrário você é uma vítima da *Superscalar Out Of Order Intel Ar...</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. No que tange diretamente a lógica de **1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)** explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">Você codifica:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Sobre o funcionamento prático de **2. O Memory Model (Consistências e Barreiras)** explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">O C++11 emitiu formalmente o seu universal **Memory Model** definindo através da biblioteca `std::atomic` o que o Hardware tem permições para *Adiantar* vs *Trancar*.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. No contexto analítico de **3. Memory Barriers (Fences) nas CPUs** explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">Se não tivessemos essa lei `std::atomic` no standard oficial do GCC, programávamos via "Gambiarra Intrinseca" de Processador (Ex: Comando Assembler **MFENCE** ou **SFENCE** no Intel). Os Fences proíbem categoricamente a ...</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Ao avaliar a característica inerente a **Resumo Prático** explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">- Se duas "Threads" conversam através das mesmas variáveis limpas de C e não possuam `std::mutex` da aula 10 as blindando, USE **`std::atomic<bool>`**. Do contrário você é uma vítima da *Superscalar Out Of Order Intel Ar...</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. A respeito da arquitetura sistêmica conectada a **1. A Reordenação do Compilador e CPU (Out-Of-Order Execution)** explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">Você codifica:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No que tange diretamente a lógica de **2. O Memory Model (Consistências e Barreiras)** explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">O C++11 emitiu formalmente o seu universal **Memory Model** definindo através da biblioteca `std::atomic` o que o Hardware tem permições para *Adiantar* vs *Trancar*.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>


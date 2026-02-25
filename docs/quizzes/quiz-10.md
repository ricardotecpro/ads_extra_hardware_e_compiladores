# Quiz 10 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Sobre o funcionamento prático de 1. O Data Race: Uma Colisão Inevitável explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. No contexto analítico de 2. Mutex e The Critical Section explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Ao avaliar a característica inerente a 3. O Dilema: Deadlock explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. A respeito da arquitetura sistêmica conectada a Resumo Prático explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">- **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. No que tange diretamente a lógica de 1. O Data Race: Uma Colisão Inevitável explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Sobre o funcionamento prático de 2. Mutex e The Critical Section explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. No contexto analítico de 3. O Dilema: Deadlock explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Ao avaliar a característica inerente a Resumo Prático explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">- **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. A respeito da arquitetura sistêmica conectada a 1. O Data Race: Uma Colisão Inevitável explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No que tange diretamente a lógica de 2. Mutex e The Critical Section explicado em sala, indique a afirmativa verdadeira:</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo e Exato. Esta é rigorosamente a premissa central abordada no conteúdo de sala.*">A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::mutex` (Mutual Exclusion).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É uma limitação exclusiva de linguagens interpretadas muito antigas, sem nenhuma relação ao universo avançado do C/C++ moderno e CPUs atuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Este paradigma foi totalmente descontinuado das arquiteturas vigentes porque o processador atua hoje com barramentos perfeitamente abstratos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse sub-processo opera de maneira paralela puramente abstrata, eximindo o Kernel do SO de gerenciar filas de execução.</div>
  <div class="quiz-feedback"></div>
</div>


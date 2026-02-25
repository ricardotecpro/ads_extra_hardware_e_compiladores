# Quiz 10 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Segundo a aula 10, ao abordarmos o tópico de **1. O Data Race: Uma Colisão Inevitável**, qual a premissa tecnológica subjacente a este conceito?</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*">Imaginemos uma variável primitiva `int balance = 100;`. Em Assembly C/C++, aumentar uma quantia em `balance += 10;` não é "Um Único Movimento".</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Segundo a aula 10, ao abordarmos o tópico de **2. Mutex e The Critical Section**, qual a premissa tecnológica subjacente a este conceito?</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*">A solução em qualquer projeto multi-thread backend/C++ é envolver as memórias ou o fluxo com objetos pesados atômicos do Kernel: As **Locks (Travas)** como padrão Ouro C++: `std::m...</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Segundo a aula 10, ao abordarmos o tópico de **3. O Dilema: Deadlock**, qual a premissa tecnológica subjacente a este conceito?</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*">Mas e se o programador de *Backend C/C++* prender (usou lock() ou Mutex) em A esperando que B seja terminado.. mas B só termina porque B precisa pegar lock() em A que tá bloqueado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Segundo a aula 10, ao abordarmos o tópico de **Resumo Prático**, qual a premissa tecnológica subjacente a este conceito?</div>
  <div class="quiz-option" data-correct="true" data-feedback="Afirmativo. Esta é exatamente a dinâmica explicada no texto base da aula.*">- **Mutex**: Usa o sistema do núcleo para trancar áreas exclusivas do Hardware (RAM).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É um conceito restrito apenas a linguagens de script interpretadas de alto nível, não afetando ambientes de sistema operacional.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A execução desse processo independe da CPU, rodando inteiramente de forma abstrata na memória do monitor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Essa camada só existe em sistemas de 32 bits obsoletos e foi removida na computação moderna.</div>
  <div class="quiz-feedback"></div>
</div>


<!-- .element: class="fragment" -->
# Como o Software Roda no Hardware
## Aula 01

---

## 🏗️ 1. O Abismo entre Código e Silício

Escrevemos *software* (como C/C++, Java, Python) usando linguagens compreensíveis a humanos, porém processadores processam apenas **Sinais Elétricos** ou, abstraindo para o domínio digital, **Binários (0 e 1)**.

Como a sua frase `printf("Hello World");` chega aos pinos do processador? Através de uma cadeia de ferramentas (*Toolchain*).

### O Processo de Compilação (C/C++)

Linguagens compiladas de baixo nível seguem um caminho determinístico. Veja o diagrama abaixo de como um arquivo `.c` é fatiado:

---

## 🛠️ 2. Compiladores vs Interpretadores

A forma como seu código vira máquina dita o perfil da performance:


    O código é 100% transformado em binário *antes* de executar (AOT - Ahead of Time).
    **Pró**: Alta velocidade de execução. Hardware direto.
    **Contra**: O executável construído em Linux-x86 não roda nativamente em Windows-ARM sem ser recompilado.


    Um programa (Interpretador) lê o seu código fonte em tempo de execução e executa as ações simulando o comando subjacente para o S.O.
    **Pró**: Roda em qualquer SO que tiver o interpretador.
    **Contra**: Muito mais lento, por sofrer *overhead* da interpretação.


    Compilam para um formato intermediário (*Bytecode*), e a JVM ou CLR as compila JIT (Just-In-Time) na máquina cliente no instante de executar.

---

## 📐 3. ISA: O Contrato do Processador

**ISA (Instruction Set Architecture)** é o dicionário de um processador. É o conjunto de comandos numéricos que o CPU sabe, fisicamente, executar:

* *Puxar da Memória (LOAD)*
* *Somar (ADD)*
* *Gravar na Memória (STORE)*

Todo código, por mais sofisticado que seja, precisa ser reduzido a estas poucas operações ditadas pela ISA para rodar.

<div class="termy" markdown="1">

---

## 🚀 Resumo Prático

- Ao usar C/C++, você não lida com um motor intermediário te cobrindo (como a JVM), você escreve algoritmos cuja gestão é delegada ao S.O. e rodada pura em metal.
- O programador backend / performance critica deve inspecionar eventuais outputs em *Assembly* para verificar se a abordagem da linguagem otimiza tempo de registrador.

Pronto para entender profundamente os dados no Módulo Binário?
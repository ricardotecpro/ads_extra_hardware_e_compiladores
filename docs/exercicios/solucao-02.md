# Solução e Explicação Detalhada: Aula 02 - Representação de Dados

Abaixo estão as respostas esperadas e o embasamento teórico para os exercícios propostos na **Aula 02**.

## Solução da Questão 1 - 1. Sistema Binário e Hexadecimal (Básico 1)
**Explicação Detalhada do Assunto:**

O computador compreende nativamente a base 2 (Binário). Como a escrita binária é muito longa para os humanos, nós a agrupamos em Blocos de 4 (Base 16 - Hexadecimal).

Por que `Hexadecimal` é amado pelos desenvolvedores C/C++? Um *Byte* (8 bits) pode ser perfeitamente representado por exatos dois caracteres Hexadecimais. `FF` é o mesmo que `11111111`.





---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *1. Sistema Binário e Hexadecimal* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 2 - 2. Inteiros com e sem Sinal (Unsigned) (Básico 2)
**Explicação Detalhada do Assunto:**

Em C/C++, o rigor nos tipos provém diretamente do hardware:

No hardware, inteiros negativos são representados usando a regra de **Complemento de 2**. Para obtermos o binário do `-1`, invertemos todos os bits de `1` e somamos `1`.

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *2. Inteiros com e sem Sinal (Unsigned)* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 3 - 3. Ponto Flutuante (IEEE 754) (Intermediário 1)
**Explicação Detalhada do Assunto:**

Os famosos tipos `float` e `double`. O processador possui normalmente um setor dedicado de FPU (Floating Point Unit) para eles.

A representação oficial **IEEE 754** os divide em 3 porções:

### O Perigo da Precisão!

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *3. Ponto Flutuante (IEEE 754)* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 4 - Resumo Prático (Intermediário 2)
**Explicação Detalhada do Assunto:**

A maneira como você escolhe o tipo primitivo da variável modela a fisionomia do registrador acionado na máquina durante o *fetch*. Entender o *Overflow* é a proteção básica contra corrupção lógica do código.



!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *Resumo Prático* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 5 - 1. Sistema Binário e Hexadecimal (Desafio)
**Explicação Detalhada do Assunto:**

O computador compreende nativamente a base 2 (Binário). Como a escrita binária é muito longa para os humanos, nós a agrupamos em Blocos de 4 (Base 16 - Hexadecimal).

Por que `Hexadecimal` é amado pelos desenvolvedores C/C++? Um *Byte* (8 bits) pode ser perfeitamente representado por exatos dois caracteres Hexadecimais. `FF` é o mesmo que `11111111`.





---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *1. Sistema Binário e Hexadecimal* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-02.md){ .md-button }

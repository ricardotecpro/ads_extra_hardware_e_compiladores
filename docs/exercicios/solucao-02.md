# Solução e Explicação Detalhada: Aula 02 - Representação de Dados

Abaixo estão as respostas esperadas e o embasamento teórico para os exercícios propostos na **Aula 02**.

## Solução da Questão 1 - 1. Sistema Binário e Hexadecimal
**Explicação Detalhada do Assunto:**

O computador compreende nativamente a base 2 (Binário). Como a escrita binária é muito longa para os humanos, nós a agrupamos em Blocos de 4 (Base 16 - Hexadecimal).

Por que `Hexadecimal` é amado pelos desenvolvedores C/C++? Um *Byte* (8 bits) pode ser perfeitamente representado por exatos dois caracteres Hexadecimais. `FF` é o mesmo que `11111111`.





---

> **Expectativa de Resposta do Aluno:** O aluno deve compreender a mecânica exata detalhada no texto acima. A resposta deve transparecer o entendimento arquitetural de que *1. Sistema Binário e Hexadecimal* não é apenas uma teoria, mas impacta diretamente a compilação, performance e os sinais elétricos controlados pelo código.

## Solução da Questão 2 - 2. Inteiros com e sem Sinal (Unsigned)
**Explicação Detalhada do Assunto:**

Em C/C++, o rigor nos tipos provém diretamente do hardware:

No hardware, inteiros negativos são representados usando a regra de **Complemento de 2**. Para obtermos o binário do `-1`, invertemos todos os bits de `1` e somamos `1`.

---

> **Expectativa de Resposta do Aluno:** O aluno deve compreender a mecânica exata detalhada no texto acima. A resposta deve transparecer o entendimento arquitetural de que *2. Inteiros com e sem Sinal (Unsigned)* não é apenas uma teoria, mas impacta diretamente a compilação, performance e os sinais elétricos controlados pelo código.

## Solução da Questão 3 - 3. Ponto Flutuante (IEEE 754)
**Explicação Detalhada do Assunto:**

Os famosos tipos `float` e `double`. O processador possui normalmente um setor dedicado de FPU (Floating Point Unit) para eles.

A representação oficial **IEEE 754** os divide em 3 porções:

### O Perigo da Precisão!

> **Expectativa de Resposta do Aluno:** O aluno deve compreender a mecânica exata detalhada no texto acima. A resposta deve transparecer o entendimento arquitetural de que *3. Ponto Flutuante (IEEE 754)* não é apenas uma teoria, mas impacta diretamente a compilação, performance e os sinais elétricos controlados pelo código.

## Solução da Questão 4 - Resumo Prático
**Explicação Detalhada do Assunto:**

A maneira como você escolhe o tipo primitivo da variável modela a fisionomia do registrador acionado na máquina durante o *fetch*. Entender o *Overflow* é a proteção básica contra corrupção lógica do código.



> **Expectativa de Resposta do Aluno:** O aluno deve compreender a mecânica exata detalhada no texto acima. A resposta deve transparecer o entendimento arquitetural de que *Resumo Prático* não é apenas uma teoria, mas impacta diretamente a compilação, performance e os sinais elétricos controlados pelo código.


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-02.md){ .md-button }

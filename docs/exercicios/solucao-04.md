# Solução e Explicação Detalhada: Aula 04 - Arquiteturas RISC vs CISC

Abaixo estão as respostas esperadas e o embasamento teórico para os exercícios propostos na **Aula 04**.

## Solução da Questão 1 - 1. Entendendo a Batalha (Básico 1)
**Explicação Detalhada do Assunto:**

A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas?





---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *1. Entendendo a Batalha* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 2 - 2. Como isso afeta o Compilador C/C++? (Básico 2)
**Explicação Detalhada do Assunto:**

Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas:





O código C++ original `app.c` não muda! Quem rala é o compilador, que na versão ARM gera dezenas de pequenas instruções curtas RISC, e na versão local gera um op-code gigante com microcódigos CISC internos da Intel.

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *2. Como isso afeta o Compilador C/C++?* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 3 - Resumo Prático (Intermediário 1)
**Explicação Detalhada do Assunto:**

- Historicamente, servidores eram puramente CISC (Intel).

- Hoje, o mercado clama por RISC graças à sustentabilidade térmica (menos energia e calor).

- Um bom engenheiro percebe que a ISA (aula anterior) CISC vai conter milhares de comandos Assembly, requerendo compiladores muito agressivos, enquanto a ISA RISC exigirá compiladores muito detalhistas e otimizados linearmente na alocação de registradores C/C++.

Caminho livre até aqui? Então agora vamos adentrar nas dores da "Memória".



!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *Resumo Prático* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 4 - 1. Entendendo a Batalha (Intermediário 2)
**Explicação Detalhada do Assunto:**

A grande revolução do backend é: Seu *deploy* de aplicação na AWS/Azure precisa ser em instâncias baseadas em AMD/Intel x86 (CISC) ou instâncias AWS Graviton ARM (RISC), que normalmente são mais baratas?





---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *1. Entendendo a Batalha* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.

## Solução da Questão 5 - 2. Como isso afeta o Compilador C/C++? (Desafio)
**Explicação Detalhada do Assunto:**

Como programador, ao compilar nosso software, a *Target Architecture* é o divisor de águas:





O código C++ original `app.c` não muda! Quem rala é o compilador, que na versão ARM gera dezenas de pequenas instruções curtas RISC, e na versão local gera um op-code gigante com microcódigos CISC internos da Intel.

---

!!! info "Expectativa de Resposta"
    O aluno deve inferir com clareza que o conceito de *2. Como isso afeta o Compilador C/C++?* determina o desempenho global e não pode ser ignorado nas linguagens compiladas. Para níveis intermediários e desafio, exige-se consciência das integrações entre RAM, CPU e Kernel.


---

[:octicons-arrow-left-24: Voltar para Exercício](exercicio-04.md){ .md-button }

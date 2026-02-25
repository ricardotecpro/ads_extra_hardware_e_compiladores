<!-- .element: class="fragment" -->
# Aula 11 - Paralelismo no Hardware
## Apresentação

---

O código Multithreading (visto na Aula 09 e 10) é uma abstração do Sistema Operacional. Mas como a física do processador de fato abraça múltiplas frentes de execução simétrica simultânea?

---

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🏗️ 1. Multi-Core (Múltiplos Núcleos)

---

## 🏗️ 1. Multi-Core (Múltiplos Núcleos)

Diferente do passado, onde havia um único núcleo saltando entre aplicativos (Context Switch), hoje temos vários núcleos físicos no mesmo invólucro (Chip).

- **Core Físico:** É uma CPU completa e independente, com sua própria ALU, Unidade de Controle e Caches L1/L2 particulares.
- **Cache L3 Compartilhado:** Na maioria dos designs AMD e Intel reais, os Múltiplos Cores (Ex: 8 Cores) conversam e trocam estados através de uma suntuosa e lenta área comum L3 que circunda todos os processadores ali impressos no wafer.

---

## 🏗️ 1. Multi-Core (Múltiplos Núcleos)

> [!TIP]
> **Em Backend pesado:** Se o banco mapear duas Threads puras `backend` em dois Cores puramente isolados (Ex: Core 0 e Core 1), e elas lerem/trabalharem na mesma matriz contínua, o Hardware forçará intercâmbios elétricos no *Cache Coherence Protocol (MESI)* rodando por toda placa mãe. Fiquem espertos com o *False Sharing*!

---

## 🏗️ 1. Multi-Core (Múltiplos Núcleos)

---

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🧬 2. Hyper-Threading (SMT - Symmetrical Multi-Threading)

---

## 🧬 2. Hyper-Threading (SMT - Symmetrical Multi-Threading)

A mágica comercial da Intel e AMD nos anos 2000. Como fazer "1 Core Físico" fingir ser "2 Cores Lógicos" para o Windows/Linux?

Na aula 03, vimos que a execução cruza pelo Pipeline ou pode esbarrar em ciclos ociosos na CU aguardando a Memória Principal. O *Hyper-Threading* espeta um **Segundo conjunto de Registradores** e Hardware de Estado no mesmo Core. Enquanto o código da Thread "A" está 0.5 nanosegundo *travada* esperando chegar o dado lento da L3, o Core troca instantaneamente para o contexto da Thread "B", executando-o usando as mesmas Unidades Lógicas (ALU) num aproveitamento fabril monstruoso de 100%.

---

## 🧬 2. Hyper-Threading (SMT - Symmetrical Multi-Threading)

<div class="termy" markdown="1">

__CODE_BLOCK_0__

</div>

---

## 🧬 2. Hyper-Threading (SMT - Symmetrical Multi-Threading)

> Vemos 8 CPUs acima, mas fisicamente a máquina tem 4 motores reais.

---

## 🧬 2. Hyper-Threading (SMT - Symmetrical Multi-Threading)

---

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🎮 3. GPUs: O Paralelismo Maciço

---

## 🎮 3. GPUs: O Paralelismo Maciço

CPUs (Processadores) foram feitos para "Serem Rápidos executando sequências lógicas e IFs complexos". Possuem Caches gigantes.
GPUs (Placas de Vídeo) foram feitas para "Executar a MESMÍSSIMA MINÚSCULA matemática simultaneamente em milhares de pixels fracos". Sem grandes condicionais, focando no *Throughput*.

NVIDIA e CUDA (plataforma de C++) reinam supremas em *Deep Learning* e Criptografia exatamente porque pegam *Loops For* gigantescos de Álgebra Linear, e fracionam em **8.000 mini-núcleos (CUDA cores)** esmagando qualquer Intel Core i9 na latência matemática contínua pura.

---

<!-- .element: class="fragment" -->
# Novo Tópico
## 🚀 Resumo Prático

---

## 🚀 Resumo Prático

- **Task Paralelism**: <span class="fragment">Se tens lógica variada, use a *CPU Multi-Core C++ thread pool*.</span>
- **Data Paralelism**: <span class="fragment">Se a conta for a repetição retumbante de um algoritmo idêntico sobre 2 milhões de dados sem dependência de saltos complexos, mova-a da RAM à VRAM da *GPU via CUDA/OpenCL*. A métrica vai das horas paras os décimos de segundo.</span>

---

## 🚀 Resumo Prático

---
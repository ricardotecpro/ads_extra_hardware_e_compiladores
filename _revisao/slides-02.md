---
marp: true
theme: default
paginate: true
backgroundColor: #fff
header: 'Fundamentos da Computação'
footer: 'Aula 02'
---

# Aula 02: Conversão Decimal para Binário

---

# 🎯 Objetivos

- Aprender o método das divisões sucessivas
- Converter números decimais para binário
- Praticar a conversão manual

---

# Método das Divisões Sucessivas

1. Divida o número decimal por **2**.
2. Anote o resto (0 ou 1).
3. Pegue o quociente e divida por 2 novamente.
4. Repita até que o quociente seja **0**.
5. O número binário é formado pelos restos, lidos do **último para o primeiro**.

---

# Exemplo: 13 (Decimal)

$$
\begin{align*}
13 \div 2 &= 6, \text{ resto } \mathbf{1} \\
6 \div 2 &= 3, \text{ resto } \mathbf{0} \\
3 \div 2 &= 1, \text{ resto } \mathbf{1} \\
1 \div 2 &= 0, \text{ resto } \mathbf{1}
\end{align*}
$$

Lendo de baixo para cima: **1101**

---

# Resumo

- Divisões sucessivas por 2.
- A leitura é feita do último resto obtido até o primeiro.
- Dica: Se o número for par, termina em 0. Se ímpar, termina em 1.


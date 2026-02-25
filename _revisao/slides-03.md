---
marp: true
theme: default
paginate: true
backgroundColor: #fff
header: 'Fundamentos da Computação'
footer: 'Aula 03'
---

# Aula 03: Conversão Binário para Decimal

---

# 🎯 Objetivos

- Compreender a notação posicional
- Utilizar potências de 2
- Converter binário para decimal

---

# Notação Posicional (Binário)

Cada bit tem um peso baseado na sua posição (potência de 2).

$$
\begin{array}{|c|c|c|c|c|}
\hline
2^4 & 2^3 & 2^2 & 2^1 & 2^0 \\
\hline
16 & 8 & 4 & 2 & 1 \\
\hline
\end{array}
$$

---

# Exemplo: 10110

$$
1 \times 16 + 0 \times 8 + 1 \times 4 + 1 \times 2 + 0 \times 1
$$

$$
16 + 0 + 4 + 2 + 0 = \mathbf{22}
$$

---

# Exercício Rápido

Converta **111** para decimal.

- $1 \times 4 = 4$
- $1 \times 2 = 2$
- $1 \times 1 = 1$
- **Total**: $4 + 2 + 1 = 7$


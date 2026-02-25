---
marp: true
theme: default
paginate: true
backgroundColor: #fff
header: 'Fundamentos da Computação'
footer: 'Aula 05'
---

# Aula 05: Sistema Hexadecimal

---

# 🎯 Objetivos

- Conhecer a Base 16 (Hexadecimal)
- Entender o uso das letras A-F
- Relacionar Hex com 4 bits (Nibble)

---

# Dígitos Hexadecimais

| Dec | Hex | Bin | Dec | Hex | Bin |
|---|---|---|---|---|---|
| 0 | 0 | 0000 | 8 | 8 | 1000 |
| 1 | 1 | 0001 | 9 | 9 | 1001 |
| 2 | 2 | 0010 | 10 | **A** | 1010 |
| 3 | 3 | 0011 | 11 | **B** | 1011 |
| 4 | 4 | 0100 | 12 | **C** | 1100 |
| 5 | 5 | 0101 | 13 | **D** | 1101 |
| 6 | 6 | 0110 | 14 | **E** | 1110 |
| 7 | 7 | 0111 | 15 | **F** | 1111 |

---

# Decimal $\rightarrow$ Hex

Divisões sucessivas por **16**.

**Exemplo: 42**
1. $42 \div 16 = 2$, resto **10** (A)
2. $2 \div 16 = 0$, resto **2**

Resultado: **2A**

---

# Hex $\rightarrow$ Decimal

Soma ponderada por potências de 16.

**Exemplo: 3C**
$$ 3 \times 16^1 + 12 \times 16^0 $$
$$ 48 + 12 = \mathbf{60} $$


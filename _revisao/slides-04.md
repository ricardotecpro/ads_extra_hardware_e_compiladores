---
marp: true
theme: default
paginate: true
backgroundColor: #fff
header: 'Fundamentos da Computação'
footer: 'Aula 04'
---

# Aula 04: Sistema Octal

---

# 🎯 Objetivos

- Conhecer a Base 8 (Octal)
- Converter Decimal $\leftrightarrow$ Octal
- Entender a relação com bits

---

# Sistema Octal (Base 8)

- **Dígitos**: 0, 1, 2, 3, 4, 5, 6, 7
- **Fator de agrupamento**: 1 dígito octal = 3 bits ($2^3=8$)

---

# Decimal $\rightarrow$ Octal

Método das Divisões Sucessivas por 8.

**Exemplo: 60**
1. $60 \div 8 = 7$, resto **4**
2. $7 \div 8 = 0$, resto **7**

Resultado: **74** (octal)

---

# Octal $\rightarrow$ Decimal

Soma ponderada por potências de 8 ($8^0, 8^1, 8^2...$).

**Exemplo: 23 (octal)**
$$ 2 \times 8^1 + 3 \times 8^0 $$
$$ 16 + 3 = 19 \text{ (decimal)} $$


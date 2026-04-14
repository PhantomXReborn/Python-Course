"""
Lesson 4.2: Order of Operations (PEMDAS)
Description: Understanding operator precedence: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.2.1
result = 2 + 3 * 4
print(result)
result = (2 + 3) * 4
print(result)

# Questions for P&R 4.2.1:
# 1. Why are the two results different?
# 2. What does parentheses do?

# P&R 4.2.2
print(10 - 5 - 2)
print(10 - (5 - 2))

# Questions for P&R 4.2.2:
# 1. Are subtraction and addition left-associative?
# 2. Does parentheses change the order?

# P&R 4.2.3
print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
print(2 ** (3 ** 2))

# Questions for P&R 4.2.3:
# 1. Is exponentiation right-associative?
# 2. Which pair of parentheses matches the default?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.2.1
# Run this code and observe:
print(10 + 2 * 3 - 4 / 2)
print((10 + 2) * 3 - 4 / 2)
print(10 + 2 * (3 - 4) / 2)
print((10 + 2) * (3 - 4) / 2)

# Questions for Investigate 4.2.1:
# 1. How does each set of parentheses change the result?
# 2. Which expression gives the smallest number?

# Investigate 4.2.2
# Run this code and observe:
print(2 ** 2 ** 3)
print(2 ** (2 ** 3))
print((2 ** 2) ** 3)

# Questions for Investigate 4.2.2:
# 1. Which result is 256 and which is 64?
# 2. Which order does Python use by default?

# Investigate 4.2.3
# Run this code and observe:
a = 5
b = 10
c = 2
print(a + b * c)
print(a + (b * c))
print((a + b) * c)

# Questions for Investigate 4.2.3:
# 1. Are parentheses always necessary for multiplication first?
# 2. When are parentheses required?

# ========== MODIFY (3 exercises) ==========

# Modify 4.2.1
# TODO: Add parentheses so the result is 50 (currently 20)
result = 5 + 5 * 5
print(result)

# Modify 4.2.2
# TODO: Add parentheses so the result is 1 (currently 7)
result = 10 - 3 - 6
print(result)

# Modify 4.2.3
# TODO: Add parentheses to calculate: 2 raised to the power of (3 raised to the power of 2)
result = 2 ** 3 ** 2
print(result)

# ========== MAKE (3 exercises) ==========

# Make 4.2.1
# TODO: Write an expression without parentheses that equals 25. Then write the same expression with parentheses that equals 30.

# Make 4.2.2
# TODO: Calculate the average of 5, 8, and 12 using parentheses to control order.

# Make 4.2.3
# TODO: Create an expression that uses at least 4 operators. Write it with and without parentheses to show different results.
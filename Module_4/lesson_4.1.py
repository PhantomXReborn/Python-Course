"""
Lesson 4.1: Arithmetic Operators
Description: Using basic math operators: +, -, *, /, //, %, **
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.1.1
a = 15
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Questions for P&R 4.1.1:
# 1. What type is the result of a / b?
# 2. Which operation produces the largest result?

# P&R 4.1.2
print(17 // 5)
print(17 % 5)
print(divmod(17, 5))

# Questions for P&R 4.1.2:
# 1. What does // do?
# 2. What does % do?

# P&R 4.1.3
print(2 ** 3)
print(10 ** 0)
print(4 ** 0.5)

# Questions for P&R 4.1.3:
# 1. What does ** do?
# 2. What is 4 ** 0.5?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.1.1
# Run this code and observe:
x = 10
y = 3
print(x + y * 2)
print((x + y) * 2)

# Questions for Investigate 4.1.1:
# 1. Why are the results different?
# 2. What is the order of operations?

# Investigate 4.1.2
# Run this code and observe:
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 / 3 == 10 // 3 + (10 % 3) / 3)

# Questions for Investigate 4.1.2:
# 1. How are // and % related?
# 2. Is the equality True or False?

# Investigate 4.1.3
# Run this code and observe:
print(-5 // 2)
print(-5 % 2)
print(5 // -2)
print(5 % -2)

# Questions for Investigate 4.1.3:
# 1. How does floor division work with negatives?
# 2. Does modulo always give a positive remainder?

# ========== MODIFY (3 exercises) ==========

# Modify 4.1.1
# TODO: Calculate the area of a rectangle (width * height)
width = 12
height = 5
area = 0  # Fix this
print(area)

# Modify 4.1.2
# TODO: Calculate the perimeter of a rectangle (2 * width + 2 * height)
width = 7
height = 3
perimeter = 0  # Fix this
print(perimeter)

# Modify 4.1.3
# TODO: Calculate the remainder when 100 is divided by 7
dividend = 100
divisor = 7
remainder = 0  # Fix this
print(f"Remainder: {remainder}")

# ========== MAKE (3 exercises) ==========

# Make 4.1.1
# TODO: Ask for two numbers. Print their sum, difference, product, and quotient.

# Make 4.1.2
# TODO: Ask for a number of seconds. Convert to minutes and seconds (e.g., 130 seconds = 2 minutes 10 seconds).

# Make 4.1.3
# TODO: Calculate compound interest: principal * (1 + rate) ** years
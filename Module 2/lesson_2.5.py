"""
Lesson 2.5: Floats (float)
Description: Working with decimal numbers
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.5.1
x = 3.14
y = 0.5
z = -2.7
print(x + y)
print(x * z)

# Questions for P&R 2.5.1:
# 1. Can floats be negative?
# 2. What happens when you add an int and a float?

# P&R 2.5.2
print(1.1 + 2.2)
print(0.1 + 0.2)

# Questions for P&R 2.5.2:
# 1. Why isn't 0.1 + 0.2 exactly 0.3?
# 2. What causes floating point imprecision?

# P&R 2.5.3
print(round(3.14159, 2))
print(round(3.14159, 0))

# Questions for P&R 2.5.3:
# 1. What does round() do?
# 2. What does the second argument control?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.5.1
# Run this code and observe:
x = 1.5e3
y = 1.5e-3
print(x)
print(y)

# Questions for Investigate 2.5.1:
# 1. What does 'e' in 1.5e3 mean?
# 2. What is 1.5e-3 as a decimal?

# Investigate 2.5.2
# Run this code and observe:
from decimal import Decimal
a = 0.1 + 0.2
b = Decimal('0.1') + Decimal('0.2')
print(a)
print(b)

# Questions for Investigate 2.5.2:
# 1. Which result is more accurate?
# 2. When would you use Decimal?

# Investigate 2.5.3
# Run this code and observe:
x = 5 / 2
y = 5 // 2
z = 5 % 2
print(x, y, z)

# Questions for Investigate 2.5.3:
# 1. Which result is a float?
# 2. Which operations produce integers?

# ========== MODIFY (3 exercises) ==========

# Modify 2.5.1
# TODO: Round pi to 3 decimal places
pi = 3.14159265
print(pi)

# Modify 2.5.2
# TODO: Fix this division to get a float result
result = 10 // 3
print(result)

# Modify 2.5.3
# TODO: Calculate the area of a circle with radius 5 (area = π * r²)
# Use pi = 3.14159
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 2.5.1
# TODO: Ask for a price and a discount percentage (e.g., 20 for 20%). Calculate and print the final price.

# Make 2.5.2
# TODO: Calculate the average of three numbers: 85.5, 92.3, and 78.9

# Make 2.5.3
# TODO: Convert miles to kilometers (1 mile = 1.60934 km). Ask for miles, print kilometers with 2 decimals.
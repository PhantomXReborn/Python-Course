"""
Lesson 4.4: Built-in Math Functions
Description: Using abs(), round(), pow(), min(), max(), sum()
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.4.1
print(abs(-15))
print(abs(7))
print(abs(0))

# Questions for P&R 4.4.1:
# 1. What does abs() do?
# 2. Does it work with positive numbers?

# P&R 4.4.2
print(round(3.14159, 2))
print(round(3.14159))
print(round(3.5))

# Questions for P&R 4.4.2:
# 1. What does the second argument do?
# 2. How does round() handle .5?

# P&R 4.4.3
numbers = [5, 2, 8, 1, 9]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Questions for P&R 4.4.3:
# 1. What does min() do?
# 2. What does sum() do?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.4.1
# Run this code and observe:
print(pow(2, 3))
print(pow(2, 3, 5))
print(2 ** 3 % 5)

# Questions for Investigate 4.4.1:
# 1. What does the third argument to pow() do?
# 2. Are pow(2,3,5) and 2**3 % 5 the same?

# Investigate 4.4.2
# Run this code and observe:
print(round(2.675, 2))
print(round(2.665, 2))

# Questions for Investigate 4.4.2:
# 1. Are the results exactly what you expect?
# 2. What causes floating point rounding issues?

# Investigate 4.4.3
# Run this code and observe:
values = [10, 20, 30, 40, 50]
print(sum(values))
print(sum(values) / len(values))
print(max(values) - min(values))

# Questions for Investigate 4.4.3:
# 1. How do you calculate the average?
# 2. What is the range (max - min)?

# ========== MODIFY (3 exercises) ==========

# Modify 4.4.1
# TODO: Use round() to show pi with 1, 2, and 3 decimal places
pi = 3.1415926535
# Your code below:

# Modify 4.4.2
# TODO: Find the minimum, maximum, and sum of this list
scores = [85, 92, 78, 90, 88]
# Your code below:

# Modify 4.4.3
# TODO: Use pow() to calculate 3 to the 4th power, then modulo 10
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 4.4.1
# TODO: Ask for a negative number. Print its absolute value.

# Make 4.4.2
# TODO: Ask for 5 numbers, store in a list. Print sum, average, min, and max.

# Make 4.4.3
# TODO: Calculate compound interest with pow(): principal * (1 + rate) ** years
"""
Lesson 1.7: Variables with Numbers
Description: Storing and using integers and floats in variables
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 1.7.1
x = 10
y = 3
print(x + y)
print(x - y)

# Questions for P&R 1.7.1:
# 1. What values do x and y hold?
# 2. What operation is done in each print?

# P&R 1.7.2
price = 19.99
tax = 0.08
total = price + (price * tax)
print(total)

# Questions for P&R 1.7.2:
# 1. What type of number is price (integer or float)?
# 2. Does the calculation happen before print?

# P&R 1.7.3
a = 5
a = a + 2
print(a)

# Questions for P&R 1.7.3:
# 1. What is the final value of a?
# 2. How does 'a = a + 2' work?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 1.7.1
# Run this code and observe:
count = 0
count = count + 1
count = count + 1
print(count)

# Questions for Investigate 1.7.1:
# 1. How many times does count increase?
# 2. What is the final value?

# Investigate 1.7.2
# Run this code and observe:
num = 7
num += 3
print(num)
num *= 2
print(num)

# Questions for Investigate 1.7.2:
# 1. What does '+=' do?
# 2. What does '*=' do?

# Investigate 1.7.3
# Run this code and observe:
a = 10
b = 3
print(a // b)
print(a % b)

# Questions for Investigate 1.7.3:
# 1. What does '//' do?
# 2. What does '%' (modulo) do?

# ========== MODIFY (3 exercises) ==========

# Modify 1.7.1
# TODO: Change the values so the result is 50
num1 = 5
num2 = 10
print(num1 * num2)

# Modify 1.7.2
# TODO: Use += to add 5 to the variable 'score', then print it
score = 20
# Your code below:

# Modify 1.7.3
# TODO: Fix this calculation to find the remainder when 17 is divided by 4
result = 17 / 4
print("Remainder:", result)

# ========== MAKE (3 exercises) ==========

# Make 1.7.1
# TODO: Create variables 'width' and 'height' with numbers, then print their product (area)

# Make 1.7.2
# TODO: Create a variable 'temperature' in Celsius, convert to Fahrenheit (C * 9/5 + 32), and print

# Make 1.7.3
# TODO: Start with x = 100. Then subtract 10, then multiply by 2 using shortcuts (-= and *=)
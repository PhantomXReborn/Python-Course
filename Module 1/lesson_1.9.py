"""
Lesson 1.9: Converting Input Types
Description: Converting string input to integers or floats using int() and float()
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 1.9.1
num = int(input("Enter a number: "))
print(num + 10)

# Questions for P&R 1.9.1:
# 1. What does int() do to the input?
# 2. If you type 5, what prints?

# P&R 1.9.2
x = float(input("Enter a decimal: "))
print(x * 2)

# Questions for P&R 1.9.2:
# 1. What type does float() create?
# 2. Can you type 3 (without decimal) and still work?

# P&R 1.9.3
age = int(input("Age: "))
next_age = age + 1
print("Next year you'll be", next_age)

# Questions for P&R 1.9.3:
# 1. Why do we need int() here?
# 2. What would happen without int()?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 1.9.1
# Run this code and observe:
value = input("Enter 5: ")
print(value * 3)
value = int(value)
print(value * 3)

# Questions for Investigate 1.9.1:
# 1. Why does the first multiplication repeat the string?
# 2. What happens after converting to int?

# Investigate 1.9.2
# Run this code and observe:
num = int(input("Enter a number: "))
print(type(num))

# Questions for Investigate 1.9.2:
# 1. What type does type() show now?
# 2. Could you change this to float instead?

# Investigate 1.9.3
# Run this code and observe:
# text = int(input("Enter your name: "))  # Uncomment to see error

# Questions for Investigate 1.9.3:
# 1. What error appears if you type a name instead of a number?
# 2. What does ValueError mean?

# ========== MODIFY (3 exercises) ==========

# Modify 1.9.1
# TODO: Convert the input to float so decimal numbers work
price = input("Enter price: ")
total = price * 1.1
print("With tax:", total)

# Modify 1.9.2
# TODO: Get two numbers as integers, then print their sum
num1 = input("First: ")
num2 = input("Second: ")

# Modify 1.9.3
# TODO: Convert the result to an integer to remove decimals
result = 100 / 3
print("Integer result:", result)

# ========== MAKE (3 exercises) ==========

# Make 1.9.1
# TODO: Ask for a number, convert to int, and print its square (number * number)

# Make 1.9.2
# TODO: Ask for two decimal numbers, convert to float, and print their average

# Make 1.9.3
# TODO: Ask for a temperature in Fahrenheit, convert to float, then convert to Celsius and print
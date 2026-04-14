"""
Lesson 2.4: Integers (int)
Description: Working with whole numbers, positive and negative
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.4.1
x = 10
y = -5
z = 0
print(x + y)
print(x - z)

# Questions for P&R 2.4.1:
# 1. Can integers be negative?
# 2. Can integers be zero?

# P&R 2.4.2
big_number = 1000000
also_big = 1_000_000
print(big_number)
print(also_big)

# Questions for P&R 2.4.2:
# 1. Does the underscore change the number?
# 2. Why would you use underscores in numbers?

# P&R 2.4.3
print(10 ** 3)
print(10 ** 0)
print(2 ** 10)

# Questions for P&R 2.4.3:
# 1. What does ** do?
# 2. What is 10 ** 0?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.4.1
# Run this code and observe:
x = 7
y = 3
print(x // y)
print(x % y)

# Questions for Investigate 2.4.1:
# 1. What is floor division (//)?
# 2. What is modulo (%) useful for?

# Investigate 2.4.2
# Run this code and observe:
print(abs(-15))
print(pow(2, 4))
print(divmod(10, 3))

# Questions for Investigate 2.4.2:
# 1. What does abs() do?
# 2. What does divmod() return?

# Investigate 2.4.3
# Run this code and observe:
num = 42
print(bin(num))
print(oct(num))
print(hex(num))

# Questions for Investigate 2.4.3:
# 1. What base is bin() output?
# 2. What does hex() show?

# ========== MODIFY (3 exercises) ==========

# Modify 2.4.1
# TODO: Fix this calculation to get the remainder of 17 divided by 5
result = 17 / 5
print("Remainder:", result)

# Modify 2.4.2
# TODO: Use an operator to calculate 2 to the 8th power (256)
result = 2 * 8  # This is wrong
print(result)

# Modify 2.4.3
# TODO: Make the number negative and print its absolute value
number = 42
print(number)

# ========== MAKE (3 exercises) ==========

# Make 2.4.1
# TODO: Create variables for hours worked (40) and hourly rate (25). Calculate total pay.

# Make 2.4.2
# TODO: Ask for a number, then print if it's even or odd using modulo (number % 2)

# Make 2.4.3
# TODO: Calculate the number of seconds in a day (24 hours * 60 minutes * 60 seconds)
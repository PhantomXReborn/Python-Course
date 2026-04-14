"""
Lesson 2.3: The type() Function
Description: Using type() to check what kind of data a variable holds
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.3.1
x = 42
print(type(x))

# Questions for P&R 2.3.1:
# 1. What does type() return for an integer?
# 2. What is the output format (e.g., <class 'int'>)?

# P&R 2.3.2
y = 3.14
z = "Hello"
print(type(y))
print(type(z))

# Questions for P&R 2.3.2:
# 1. What type is 3.14?
# 2. What type is "Hello"?

# P&R 2.3.3
a = True
b = False
print(type(a))
print(type(b))

# Questions for P&R 2.3.3:
# 1. What type are True and False?
# 2. Do they need quotation marks?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.3.1
# Run this code and observe:
value = 100
print(type(value))
value = "100"
print(type(value))
value = 100.0
print(type(value))

# Questions for Investigate 2.3.1:
# 1. Can a variable's type change?
# 2. Is "100" different from 100?

# Investigate 2.3.2
# Run this code and observe:
print(type(5))
print(type(5.0))
print(type(5 + 0j))

# Questions for Investigate 2.3.2:
# 1. What is a complex number type?
# 2. Is 5.0 an int or float?

# Investigate 2.3.3
# Run this code and observe:
result = 10 / 2
print(type(result))
result = 10 // 2
print(type(result))

# Questions for Investigate 2.3.3:
# 1. Why does / produce a float?
# 2. Why does // produce an int?

# ========== MODIFY (3 exercises) ==========

# Modify 2.3.1
# TODO: Print the type of each variable
name = "Alice"
age = 25
height = 5.6
is_student = True
# Your code below:

# Modify 2.3.2
# TODO: Convert the type checks to use variables instead of direct values
print(type(42))
print(type("text"))
print(type(3.14))

# Modify 2.3.3
# TODO: Predict then check the type of each operation
result1 = 3 + 4
result2 = 3 + 4.0
result3 = "3" + "4"
# Add type() calls below:

# ========== MAKE (3 exercises) ==========

# Make 2.3.1
# TODO: Create one variable of each type: int, float, str, bool. Print each variable and its type.

# Make 2.3.2
# TODO: Ask the user for input, then print the type of what they entered

# Make 2.3.3
# TODO: Create a variable, print its type, then change it to a different type and print again
"""
Lesson 2.12: Mini Project - Data Type Explorer
Description: Combine everything from Module 2 to create an interactive data type exploration tool
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.12.1
# Read this complete program and predict the output:
print("DATA TYPE EXPLORER")
print("=" * 30)
sample_int = 42
sample_float = 3.14
sample_str = "Python"
sample_bool = True
print(f"int: {sample_int} -> {type(sample_int)}")
print(f"float: {sample_float} -> {type(sample_float)}")
print(f"str: {sample_str} -> {type(sample_str)}")
print(f"bool: {sample_bool} -> {type(sample_bool)}")

# Questions for P&R 2.12.1:
# 1. What types are shown in the output?
# 2. What does the f-string do?

# P&R 2.12.2
value = input("Enter something: ")
try:
    int_value = int(value)
    print(f"Converted to int: {int_value}")
except:
    print("Cannot convert to int")

# Questions for P&R 2.12.2:
# 1. What happens if you type "123"?
# 2. What happens if you type "abc"?

# P&R 2.12.3
def explore_type(var):
    print(f"Value: {var}")
    print(f"Type: {type(var)}")
    if type(var) == int:
        print(f"Square: {var ** 2}")
    elif type(var) == str:
        print(f"Length: {len(var)}")
    elif type(var) == bool:
        print(f"Opposite: {not var}")

explore_type(10)
explore_type("Hello")

# Questions for P&R 2.12.3:
# 1. What does explore_type(10) print?
# 2. What does explore_type("Hello") print?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.12.1
# Run this code and observe:
print("=== Type Conversion Chart ===")
values = [0, 1, 3.14, "0", "1", "Hello", "", True, False]
for v in values:
    print(f"{v:10} | int: {int(v) if str(v).isdigit() or isinstance(v, (int, float)) else 'N/A'}")

# Questions for Investigate 2.12.1:
# 1. Which values can convert to int successfully?
# 2. Why can't "Hello" convert to int?

# Investigate 2.12.2
# Run this code and observe:
a = 10
b = "5"
c = 3.2
results = [
    a + int(b),
    str(a) + b,
    a + c,
    str(a) + str(c)
]
for r in results:
    print(f"{r} -> {type(r)}")

# Questions for Investigate 2.12.2:
# 1. Which operations produce strings?
# 2. Which produce numbers?

# Investigate 2.12.3
# Run this code and observe:
user_input = input("Enter a number (or anything): ")
if user_input.isdigit():
    print(f"All digits! Converted: {int(user_input)}")
elif user_input.replace('.', '', 1).isdigit():
    print(f"Looks like a float: {float(user_input)}")
elif user_input.lower() in ["true", "false"]:
    print(f"Boolean: {user_input.lower() == 'true'}")
else:
    print(f"String: {user_input}")

# Questions for Investigate 2.12.3:
# 1. What does .isdigit() check for?
# 2. How does it detect a float?

# ========== MODIFY (3 exercises) ==========

# Modify 2.12.1
# TODO: Add a constant for the maximum number of conversions (MAX_CONVERSIONS = 5)
# Then limit the explorer to that many tries
# Your code below:

# Modify 2.12.2
# TODO: Add support for detecting and converting hexadecimal numbers (0x...)
user_value = input("Enter a value: ")
# Add hex detection here

# Modify 2.12.3
# TODO: Create a report that shows the memory size of each type using sys.getsizeof()
import sys
sample = 42
# Add getsizeof calls for different types

# ========== MAKE (3 exercises) ==========

# Make 2.12.1
# TODO: Create a program that asks for a value, then tries to convert it to int, float, and bool.
# Show each conversion result or "Cannot convert"

# Make 2.12.2
# TODO: Build a "Type Calculator" that asks for two values and an operation (+, -, *, /).
# Convert types appropriately and show the result with its type.

# Make 2.12.3
# TODO: Create a complete "Variable Inspector" that:
# - Asks for a variable name and value
# - Stores it in a dictionary
# - Allows the user to inspect any stored variable (shows value, type, and length/size if applicable)
# - Allows changing a variable's value and seeing the type change
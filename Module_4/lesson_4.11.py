"""
Lesson 4.11: Numeric Type Conversion and Limits
Description: Converting between int, float, complex; understanding numeric limits
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.11.1
x = 10
y = float(x)
z = complex(x)
print(type(x), type(y), type(z))
print(y, z)

# Questions for P&R 4.11.1:
# 1. What type is y after float(x)?
# 2. What is the imaginary part of complex(x)?

# P&R 4.11.2
x = 3.7
y = int(x)
print(y)
print(int(-3.7))

# Questions for P&R 4.11.2:
# 1. Does int() round or truncate?
# 2. What is int(-3.7)?

# P&R 4.11.3
print(float(1e308))
# print(float(1e309))  # Uncomment to see overflow

# Questions for P&R 4.11.3:
# 1. What is the maximum float size?
# 2. What happens when you exceed it?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.11.1
# Run this code and observe:
import sys
print(f"Max int: {sys.maxsize}")
print(f"Min int: {-sys.maxsize - 1}")
big = 10 ** 100
print(big)
print(type(big))

# Questions for Investigate 4.11.1:
# 1. Is there a practical limit for Python ints?
# 2. What is sys.maxsize?

# Investigate 4.11.2
# Run this code and observe:
import sys
print(f"Float max: {sys.float_info.max}")
print(f"Float min: {sys.float_info.min}")
print(f"Float epsilon: {sys.float_info.epsilon}")

# Questions for Investigate 4.11.2:
# 1. What is epsilon?
# 2. What happens at float max?

# Investigate 4.11.3
# Run this code and observe:
x = 1.0
while x + 1.0 > 1.0:
    x /= 2.0
print(f"Smallest x where x+1 > 1: {x}")

# Questions for Investigate 4.11.3:
# 1. What does this measure?
# 2. What is machine epsilon?

# ========== MODIFY (3 exercises) ==========

# Modify 4.11.1
# TODO: Convert this string to int, then to float, then to complex
num_str = "42"
# Your code below:

# Modify 4.11.2
# TODO: Safely convert user input to int, handle possible errors
user_input = input("Enter a number: ")
# Your code below:

# Modify 4.11.3
# TODO: Calculate the factorial of 100 and see how large Python ints can go
import math
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 4.11.1
# TODO: Create a program that shows the min, max, and epsilon for floats on your system.

# Make 4.11.2
# TODO: Demonstrate integer overflow (doesn't exist in Python) vs float overflow.

# Make 4.11.3
# TODO: Compare performance of int vs float for large loops.
"""
Lesson 4.9: Bitwise Operators
Description: Working with binary: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.9.1
a = 5   # binary: 0101
b = 3   # binary: 0011
print(a & b)   # AND
print(a | b)   # OR
print(a ^ b)   # XOR

# Questions for P&R 4.9.1:
# 1. What is 5 & 3? (0101 & 0011 = ?)
# 2. What is 5 | 3?

# P&R 4.9.2
print(5 << 1)   # Left shift
print(5 >> 1)   # Right shift
print(5 << 2)

# Questions for P&R 4.9.2:
# 1. What does left shift by 1 do mathematically?
# 2. What does right shift by 1 do?

# P&R 4.9.3
print(~5)
print(bin(~5))

# Questions for P&R 4.9.3:
# 1. What does ~ (NOT) do?
# 2. Why is ~5 = -6?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.9.1
# Run this code and observe:
for i in range(4):
    print(f"{i} & 1 = {i & 1}")

# Questions for Investigate 4.9.1:
# 1. What does i & 1 tell you about i?
# 2. How could you use this to check even/odd?

# Investigate 4.9.2
# Run this code and observe:
x = 0b1010  # binary 1010 = 10 decimal
print(bin(x))
print(bin(x >> 1))
print(bin(x >> 2))

# Questions for Investigate 4.9.2:
# 1. What happens to bits when shifting right?
# 2. Which bit falls off?

# Investigate 4.9.3
# Run this code and observe:
flags = 0
flags |= 1   # Set bit 0
flags |= 4   # Set bit 2
print(bin(flags))
print(flags & 1)   # Check bit 0
print(flags & 2)   # Check bit 1
print(flags & 4)   # Check bit 2

# Questions for Investigate 4.9.3:
# 1. How are bits used as flags?
# 2. How do you check if a specific bit is set?

# ========== MODIFY (3 exercises) ==========

# Modify 4.9.1
# TODO: Use a bitwise operator to check if a number is even (even numbers have bit 0 = 0)
num = 42
is_even = False  # Fix this
print(is_even)

# Modify 4.9.2
# TODO: Use left shift to multiply by 8 (same as << 3)
value = 5
multiplied = value  # Fix this
print(multiplied)

# Modify 4.9.3
# TODO: Toggle bit 2 (4) using XOR (^)
flags = 0b0010  # Currently bit 1 set
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 4.9.1
# TODO: Create a function that checks if bit n is set in a number.

# Make 4.9.2
# TODO: Use bitwise operators to combine permissions (read=1, write=2, execute=4)

# Make 4.9.3
# TODO: Convert a number to binary without using bin() (use bitwise shifts and &)
"""
Lesson 4.5: The math Module (part 1)
Description: Importing math module and using constants (pi, e, tau) and functions (ceil, floor, sqrt)
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.5.1
import math
print(math.pi)
print(math.e)
print(math.tau)

# Questions for P&R 4.5.1:
# 1. What value is math.pi?
# 2. What is math.tau (how does it relate to pi)?

# P&R 4.5.2
print(math.ceil(3.2))
print(math.ceil(3.8))
print(math.floor(3.2))
print(math.floor(3.8))

# Questions for P&R 4.5.2:
# 1. What does ceil() do?
# 2. What does floor() do?

# P&R 4.5.3
print(math.sqrt(16))
print(math.sqrt(2))
print(math.isqrt(17))

# Questions for P&R 4.5.3:
# 1. What does sqrt() return for 16?
# 2. What does isqrt() return for 17?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.5.1
# Run this code and observe:
import math
print(math.floor(-3.2))
print(math.floor(-3.8))
print(math.ceil(-3.2))
print(math.ceil(-3.8))

# Questions for Investigate 4.5.1:
# 1. How does floor work with negative numbers?
# 2. How does ceil work with negative numbers?

# Investigate 4.5.2
# Run this code and observe:
import math
print(math.trunc(3.7))
print(math.trunc(-3.7))
print(int(3.7))
print(int(-3.7))

# Questions for Investigate 4.5.2:
# 1. How is trunc() different from floor()?
# 2. Is trunc() the same as int()?

# Investigate 4.5.3
# Run this code and observe:
import math
print(math.factorial(5))
print(math.comb(5, 2))
print(math.perm(5, 2))

# Questions for Investigate 4.5.3:
# 1. What is 5! (factorial)?
# 2. What does comb(5,2) represent?

# ========== MODIFY (3 exercises) ==========

# Modify 4.5.1
# TODO: Import math and calculate the area of a circle with radius 5 (area = π * r²)
# Your code below:

# Modify 4.5.2
# TODO: Use ceil() to round up to the next integer (like for pricing)
price = 19.99
rounded_up = price  # Fix this
print(rounded_up)

# Modify 4.5.3
# TODO: Use sqrt() to calculate the hypotenuse of a right triangle (a² + b² = c²)
a = 3
b = 4
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 4.5.1
# TODO: Ask for a number. Print its ceiling, floor, and square root.

# Make 4.5.2
# TODO: Calculate the number of tiles needed for a floor (ceil(length / tile_size) * ceil(width / tile_size))

# Make 4.5.3
# TODO: Use math.comb to calculate how many ways to choose 3 items from 10.
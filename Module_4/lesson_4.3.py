"""
Lesson 4.3: Augmented Assignment Operators
Description: Using shortcuts like +=, -=, *=, /=, //=, %=, **=
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.3.1
x = 10
x += 5
print(x)
x -= 3
print(x)

# Questions for P&R 4.3.1:
# 1. What does x += 5 do?
# 2. What is the final value of x?

# P&R 4.3.2
y = 7
y *= 3
print(y)
y //= 2
print(y)

# Questions for P&R 4.3.2:
# 1. What does *= do?
# 2. What does //= do?

# P&R 4.3.3
z = 2
z **= 3
print(z)
z %= 5
print(z)

# Questions for P&R 4.3.3:
# 1. What does **= do?
# 2. What is the final value of z?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.3.1
# Run this code and observe:
count = 0
count += 1
count += 1
count += 1
print(count)

# Questions for Investigate 4.3.1:
# 1. How many times was count increased?
# 2. What is the final value?

# Investigate 4.3.2
# Run this code and observe:
total = 100
total -= 20
total -= 15
total -= 5
print(total)

# Questions for Investigate 4.3.2:
# 1. What operation is being repeated?
# 2. What is the final total?

# Investigate 4.3.3
# Run this code and observe:
value = 2
print(value)
value **= 2
print(value)
value **= 2
print(value)
value **= 2
print(value)

# Questions for Investigate 4.3.3:
# 1. What sequence of numbers is produced?
# 2. How many times did value grow?

# ========== MODIFY (3 exercises) ==========

# Modify 4.3.1
# TODO: Use augmented assignment to add 10 to score
score = 50
# Your code below:

# Modify 4.3.2
# TODO: Use augmented assignment to double the value (multiply by 2)
num = 15
# Your code below:

# Modify 4.3.3
# TODO: Use augmented assignment to reduce balance by 25%
balance = 100
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 4.3.1
# TODO: Start with x = 0. Use += to add 5, then 10, then 15. Print after each.

# Make 4.3.2
# TODO: Start with a number. Use *= to square it, then square it again, then square it again.

# Make 4.3.3
# TODO: Simulate a countdown: start at 10, use -= to subtract 1 until 0.
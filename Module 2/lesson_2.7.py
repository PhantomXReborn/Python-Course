"""
Lesson 2.7: Booleans (bool)
Description: Working with True and False values
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.7.1
is_sunny = True
is_rainy = False
print(is_sunny)
print(is_rainy)

# Questions for P&R 2.7.1:
# 1. What are the only two Boolean values?
# 2. Are True and False case-sensitive?

# P&R 2.7.2
print(10 > 5)
print(10 < 5)
print(10 == 10)

# Questions for P&R 2.7.2:
# 1. What does > do?
# 2. What does == do (double equals)?

# P&R 2.7.3
x = True
y = False
print(x and y)
print(x or y)
print(not x)

# Questions for P&R 2.7.3:
# 1. What does 'and' do?
# 2. What does 'not' do?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.7.1
# Run this code and observe:
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Hello"))

# Questions for Investigate 2.7.1:
# 1. What numbers are considered False?
# 2. What strings are considered False?

# Investigate 2.7.2
# Run this code and observe:
age = 18
has_permission = True
can_enter = age >= 18 and has_permission
print(can_enter)

# Questions for Investigate 2.7.2:
# 1. What does age >= 18 evaluate to?
# 2. How does 'and' combine the two Booleans?

# Investigate 2.7.3
# Run this code and observe:
x = 5
y = 10
print(x != y)
print(x is y)
print(x is not y)

# Questions for Investigate 2.7.3:
# 1. What does != do?
# 2. What does 'is' do?

# ========== MODIFY (3 exercises) ==========

# Modify 2.7.1
# TODO: Change the condition to check if age is 18 or older
age = 16
is_old_enough = age > 21
print(is_old_enough)

# Modify 2.7.2
# TODO: Use 'or' to check if temperature is below 32 OR above 100
temp = 75
is_extreme = temp < 32  # This only checks cold
print(is_extreme)

# Modify 2.7.3
# TODO: Negate the condition using 'not' to print the opposite
is_weekend = False
should_work = is_weekend  # This is wrong
print(should_work)

# ========== MAKE (3 exercises) ==========

# Make 2.7.1
# TODO: Create two Boolean variables: is_student and has_id. Print whether they can get a discount (both True).

# Make 2.7.2
# TODO: Ask for a number. Print True if it's between 1 and 10 (inclusive), False otherwise.

# Make 2.7.3
# TODO: Ask for two numbers. Print True if they are equal, False if they are different.
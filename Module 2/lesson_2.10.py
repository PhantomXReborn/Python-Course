"""
Lesson 2.10: Multiple Assignment
Description: Assigning values to multiple variables in one line
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.10.1
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Questions for P&R 2.10.1:
# 1. How many variables are assigned?
# 2. What value does each variable get?

# P&R 2.10.2
x = y = z = 10
print(x, y, z)
x = 20
print(x, y, z)

# Questions for P&R 2.10.2:
# 1. What value do all three start with?
# 2. Does changing x affect y and z?

# P&R 2.10.3
a, b = 5, 10
a, b = b, a
print(a, b)

# Questions for P&R 2.10.3:
# 1. What values do a and b end with?
# 2. What technique is shown here?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.10.1
# Run this code and observe:
name, age, city = "Alice", 25, "New York"
print(f"{name} is {age} and lives in {city}")

# Questions for Investigate 2.10.1:
# 1. How many variables are created in one line?
# 2. Can you mix different types in one assignment?

# Investigate 2.10.2
# Run this code and observe:
numbers = [1, 2, 3]
x, y, z = numbers
print(x, y, z)

# Questions for Investigate 2.10.2:
# 1. What is unpacking?
# 2. What must be true about the list and variable count?

# Investigate 2.10.3
# Run this code and observe:
*head, tail = [1, 2, 3, 4]
print(head)
print(tail)

# Questions for Investigate 2.10.3:
# 1. What does *head do?
# 2. How many items are in head?

# ========== MODIFY (3 exercises) ==========

# Modify 2.10.1
# TODO: Swap the values of red and blue using multiple assignment (not a temp variable)
red = "red"
blue = "blue"
# Your code below:

# Modify 2.10.2
# TODO: Assign the values 100, 200, 300 to variables low, medium, high in one line
# Your code below:

# Modify 2.10.3
# TODO: Assign the same value (0) to three variables: x, y, and z in one line
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 2.10.1
# TODO: Use multiple assignment to set first, second, third = "apple", "banana", "cherry". Print them.

# Make 2.10.2
# TODO: Ask the user for three favorite movies (separated by commas). Use split() and multiple assignment.

# Make 2.10.3
# TODO: Swap three variables (a, b, c = 1, 2, 3) so they become (3, 1, 2) using multiple assignment
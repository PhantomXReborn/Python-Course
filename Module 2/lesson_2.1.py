"""
Lesson 2.1: What is a Variable?
Description: Understanding variables as containers for storing data values
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.1.1
x = 5
y = 10
z = x + y
print(z)

# Questions for P&R 2.1.1:
# 1. What values are stored in x, y, and z?
# 2. Does print(z) show the calculation or the variable name?

# P&R 2.1.2
message = "Hello"
print(message)
message = "Goodbye"
print(message)

# Questions for P&R 2.1.2:
# 1. What is printed first and second?
# 2. Can a variable change what it stores?

# P&R 2.1.3
a = 10
b = a
a = 20
print(a)
print(b)

# Questions for P&R 2.1.3:
# 1. Does b change when a changes?
# 2. What is the final value of b?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.1.1
# Run this code and observe:
var = 100
print(var)
var = var - 25
print(var)

# Questions for Investigate 2.1.1:
# 1. How does 'var = var - 25' work?
# 2. What is the value after the subtraction?

# Investigate 2.1.2
# Run this code and observe:
x = 7
y = 3
temp = x
x = y
y = temp
print(x, y)

# Questions for Investigate 2.1.2:
# 1. What is the purpose of the 'temp' variable?
# 2. What are the final values of x and y?

# Investigate 2.1.3
# Run this code and observe:
my_var = 42
myVar = 99
myvar = 5
print(my_var, myVar, myvar)

# Questions for Investigate 2.1.3:
# 1. Are these three variables different or the same?
# 2. Does Python care about uppercase vs lowercase in variable names?

# ========== MODIFY (3 exercises) ==========

# Modify 2.1.1
# TODO: Create a variable called 'age' and store your age, then print it
# Your code below:

# Modify 2.1.2
# TODO: Swap the values of fruit1 and fruit2 using a temporary variable
fruit1 = "apple"
fruit2 = "banana"
# Your code below:

# Modify 2.1.3
# TODO: Fix the variable names to follow Python conventions (lowercase with underscores)

'''
my name = "John"
favorite number = 7
'''

# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 2.1.1
# TODO: Create three variables: your name, your age, and your city. Print all three.

# Make 2.1.2
# TODO: Create a variable 'total' that starts at 0. Add 5, then add 10, then subtract 3. Print total.

# Make 2.1.3
# TODO: Create variables for width=15 and height=8. Calculate and print the area (width * height).
"""
Lesson 2.11: Dynamic Typing
Description: Understanding that Python variables can change type at runtime
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.11.1
x = 10
print(x, type(x))
x = "Hello"
print(x, type(x))
x = 3.14
print(x, type(x))

# Questions for P&R 2.11.1:
# 1. Can x change from int to str?
# 2. Does Python care about type consistency?

# P&R 2.11.2
value = 42
print(value)
value = value + 10
print(value)
value = "The answer is " + str(value)
print(value)

# Questions for P&R 2.11.2:
# 1. How many type changes happen?
# 2. Why is str(value) needed at the end?

# P&R 2.11.3
def show_type(var):
    print(type(var))

show_type(10)
show_type("text")
show_type(True)

# Questions for P&R 2.11.3:
# 1. Does the function care what type it gets?
# 2. What is the benefit of dynamic typing?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.11.1
# Run this code and observe:
x = 5
y = "10"
# print(x + y)  # Uncomment to see error
print(x + int(y))
print(str(x) + y)

# Questions for Investigate 2.11.1:
# 1. Why does x + y cause an error?
# 2. How does dynamic typing make errors possible?

# Investigate 2.11.2
# Run this code and observe:
data = 100
print(data / 2)
data = "100"
# print(data / 2)  # Uncomment to see error
print(data * 2)

# Questions for Investigate 2.11.2:
# 1. Why does data * 2 work when data is a string?
# 2. What does "100" * 2 produce?

# Investigate 2.11.3
# Run this code and observe:
def flexible(value):
    print(f"Received: {value}")
    print(f"Type: {type(value)}")
    return value * 2

print(flexible(5))
print(flexible("Hi"))

# Questions for Investigate 2.11.3:
# 1. What does flexible(5) return?
# 2. What does flexible("Hi") return?

# ========== MODIFY (3 exercises) ==========

# Modify 2.11.1
# TODO: Change the variable 'item' from a number to a string to a float
item = 0
# Your code below:

# Modify 2.11.2
# TODO: Fix this code so it handles both number and string inputs safely
user_input = input("Enter something: ")
result = user_input * 3
print(result)

# Modify 2.11.3
# TODO: Add type checking to only multiply if it's a number
value = input("Enter a number: ")
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 2.11.1
# TODO: Create a variable that starts as an int, then becomes a str, then becomes a bool. Print each with its type.

# Make 2.11.2
# TODO: Write a program that asks for input, then prints its type. Do this 3 times with different inputs.

# Make 2.11.3
# TODO: Create a function that takes any type and returns a string describing what type it received.
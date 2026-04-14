"""
Lesson 1.8: Input from Users
Description: Getting text input from the user using input() and storing it in variables
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 1.8.1
name = input("Enter your name: ")
print("Hello", name)

# Questions for P&R 1.8.1:
# 1. What does input() do?
# 2. What appears inside the quotes during input?

# P&R 1.8.2
age = input("How old are you? ")
print("You are", age, "years old")

# Questions for P&R 1.8.2:
# 1. Is age stored as a number or text?
# 2. What happens if you type a number?

# P&R 1.8.3
color = input("Favorite color? ")
print(color + " is a nice color!")

# Questions for P&R 1.8.3:
# 1. Why is + used instead of a comma?
# 2. What would happen if you used a comma instead?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 1.8.1
# Run this code and observe:
result = input()
print("You typed:", result)

# Questions for Investigate 1.8.1:
# 1. What happens if you just press Enter without typing?
# 2. Is the prompt required inside input()?

# Investigate 1.8.2
# Run this code and observe:
first = input("First number: ")
second = input("Second number: ")
print(first + second)

# Questions for Investigate 1.8.2:
# 1. If you type 5 and 3, what prints? Why?
# 2. How is input treated by default?

# Investigate 1.8.3
# Run this code and observe:
data = input("Enter something: ")
print(type(data))

# Questions for Investigate 1.8.3:
# 1. What does type() show?
# 2. Is input always a string?

# ========== MODIFY (3 exercises) ==========

# Modify 1.8.1
# TODO: Change the prompt to ask for the user's favorite food
food = input("What is your favorite food? ")

# Modify 1.8.2
# TODO: Add a second input asking for the user's city, then print both name and city
name = input("Name: ")

# Modify 1.8.3
# TODO: Fix this so it prints "Your age is: X" where X is what the user enters
age = input("Enter age: ")
print("Your age is:" + age)

# ========== MAKE (3 exercises) ==========

# Make 1.8.1
# TODO: Ask the user for their pet's name, then print "Your pet's name is ___"

# Make 1.8.2
# TODO: Ask the user for two different words, then print them in reverse order (second then first)

# Make 1.8.3
# TODO: Ask the user for their favorite movie, then print "I like [movie] too!" using concatenation (+)
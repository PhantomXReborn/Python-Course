"""
Lesson 1.6: Variables with Strings
Description: Storing and printing text using string variables
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 1.6.1
name = "Alice"
print(name)

# Questions for P&R 1.6.1:
# 1. What value is stored in the variable 'name'?
# 2. Does print(name) need quotation marks?

# P&R 1.6.2
first = "John"
last = "Doe"
full = first + " " + last
print(full)

# Questions for P&R 1.6.2:
# 1. What does '+' do with strings?
# 2. Why is there " " between first and last?

# P&R 1.6.3
greeting = "Hello"
name = "Bob"
print(greeting, name)
print(greeting + name)

# Questions for P&R 1.6.3:
# 1. How is the comma different from the plus?
# 2. Which line has a space between words?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 1.6.1
# Run this code and observe:
message = "Python"
message = "Coding"
print(message)

# Questions for Investigate 1.6.1:
# 1. What is the final value of message?
# 2. Can a variable change what it stores?

# Investigate 1.6.2
# Run this code and observe:
city = "Toronto"
print(city.upper())
print(city.lower())
print(city)

# Questions for Investigate 1.6.2:
# 1. Does .upper() permanently change the variable?
# 2. What does .lower() do?

# Investigate 1.6.3
# Run this code and observe:
text = "  Hello  "
print(len(text))
print(len(text.strip()))

# Questions for Investigate 1.6.3:
# 1. What does len() show?
# 2. What does .strip() remove?

# ========== MODIFY (3 exercises) ==========

# Modify 1.6.1
# TODO: Change the variable values to your own first and last name
first_name = "Jane"
last_name = "Smith"
print(first_name, last_name)

# Modify 1.6.2
# TODO: Create a variable called 'sentence' that combines three string variables with spaces
word1 = "I"
word2 = "love"
word3 = "Python"

# Modify 1.6.3
# TODO: Print the variable 'word' in all uppercase letters without changing the original
word = "awesome"
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 1.6.1
# TODO: Create a variable called 'favorite_color' and store your favorite color, then print it

# Make 1.6.2
# TODO: Create two variables: 'adjective' and 'noun'. Combine them into a phrase and print

# Make 1.6.3
# TODO: Create a variable with your name, then print "My name is" followed by your name variable
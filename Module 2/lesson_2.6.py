"""
Lesson 2.6: Strings (str)
Description: Working with text data, quotes, and string operations
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.6.1
single = 'Hello'
double = "World"
triple = '''Python'''
print(single, double, triple)

# Questions for P&R 2.6.1:
# 1. Do single and double quotes work the same?
# 2. How many quotes for triple-quoted strings?

# P&R 2.6.2
text = "It's a nice day"
quote = 'He said "Hello"'
print(text)
print(quote)

# Questions for P&R 2.6.2:
# 1. How do you put an apostrophe in single quotes?
# 2. How do you put double quotes inside double quotes?

# P&R 2.6.3
text = "Hello"
print(text[0])
print(text[1])
print(text[-1])

# Questions for P&R 2.6.3:
# 1. What does [0] access?
# 2. What does [-1] access?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.6.1
# Run this code and observe:
text = "Python"
print(len(text))
print(text[0:2])
print(text[2:4])

# Questions for Investigate 2.6.1:
# 1. What does len() return?
# 2. What does slicing [0:2] do?

# Investigate 2.6.2
# Run this code and observe:
text = "Hello World"
print(text[6:])
print(text[:5])
print(text[::2])

# Questions for Investigate 2.6.2:
# 1. What does [6:] do?
# 2. What does [::2] do (step)?

# Investigate 2.6.3
# Run this code and observe:
text = "Python"
print(text[::-1])
print(text.upper())
print(text.lower())

# Questions for Investigate 2.6.3:
# 1. What does [::-1] do?
# 2. Are strings mutable or immutable?

# ========== MODIFY (3 exercises) ==========

# Modify 2.6.1
# TODO: Create a string with mixed quotes so you don't need escape characters
# Example: He said "It's great"
# Your code below:

# Modify 2.6.2
# TODO: Extract the word "World" from this string using slicing
text = "Hello World Python"
print(text)

# Modify 2.6.3
# TODO: Get the last 3 characters of this string
filename = "document.txt"
print(filename)

# ========== MAKE (3 exercises) ==========

# Make 2.6.1
# TODO: Create a string with your first and last name. Print the first character and last character.

# Make 2.6.2
# TODO: Ask for a word. Print it in reverse using slicing.

# Make 2.6.3
# TODO: Ask for a sentence. Print every other character (e.g., "Hello" -> "Hlo").
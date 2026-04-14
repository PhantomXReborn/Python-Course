"""
Lesson 3.1: String Concatenation
Description: Joining strings together using the + operator
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.1.1
first = "Hello"
second = "World"
result = first + second
print(result)

# Questions for P&R 3.1.1:
# 1. What is the output of first + second?
# 2. Is there a space between the words?

# P&R 3.1.2
word1 = "Python"
word2 = "is"
word3 = "fun"
sentence = word1 + " " + word2 + " " + word3
print(sentence)

# Questions for P&R 3.1.2:
# 1. Why are there " " between the variables?
# 2. What would happen without the spaces?

# P&R 3.1.3
a = "123"
b = "456"
print(a + b)
print(int(a) + int(b))

# Questions for P&R 3.1.3:
# 1. Why does a + b give "123456"?
# 2. What does converting to int do?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.1.1
# Run this code and observe:
greeting = "Hi"
name = "Alice"
message = greeting + " " + name + "!"
print(message)
print(len(message))

# Questions for Investigate 3.1.1:
# 1. How many strings are being concatenated?
# 2. What does len() show for the final string?

# Investigate 3.1.2
# Run this code and observe:
result = "Hello" + 5  # Uncomment to see error
print(result)

# Questions for Investigate 3.1.2:
# 1. What error appears and why?
# 2. How would you fix this?

# Investigate 3.1.3
# Run this code and observe:
part1 = "Programming"
part2 = " "
part3 = "is"
part4 = " "
part5 = "awesome"
full = part1 + part2 + part3 + part4 + part5
print(full)

# Questions for Investigate 3.1.3:
# 1. Is there a simpler way to add spaces?
# 2. What could you use instead of part2 and part4?

# ========== MODIFY (3 exercises) ==========

# Modify 3.1.1
# TODO: Add a space between word1 and word2
word1 = "Hello"
word2 = "World"
result = word1 + word2
print(result)

# Modify 3.1.2
# TODO: Create a full name by concatenating first, space, and last
first = "John"
last = "Doe"
# Your code below:

# Modify 3.1.3
# TODO: Fix this so it concatenates properly (convert the number to string)
text = "The answer is "
number = 42
result = text + number
print(result)

# ========== MAKE (3 exercises) ==========

# Make 3.1.1
# TODO: Create three string variables (adjective, noun, verb). Concatenate them into a sentence.

# Make 3.1.2
# TODO: Ask for a first name and last name. Concatenate them with a space and print.

# Make 3.1.3
# TODO: Create a username by concatenating first name, last initial, and a number (convert number to string)
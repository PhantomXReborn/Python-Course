"""
Lesson 3.3: String Indexing
Description: Accessing individual characters in a string using indices
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.3.1
word = "Python"
print(word[0])
print(word[1])
print(word[5])

# Questions for P&R 3.3.1:
# 1. What character is at index 0?
# 2. What character is at index 5?

# P&R 3.3.2
text = "Hello World"
print(text[-1])
print(text[-2])

# Questions for P&R 3.3.2:
# 1. What does -1 access?
# 2. What does -2 access?

# P&R 3.3.3
name = "Alice"
# print(name[5])  # Uncomment to see result
print(len(name))

# Questions for P&R 3.3.3:
# 1. What happens if you access index 5?
# 2. What is the last valid index?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.3.1
# Run this code and observe:
word = "Programming"
print(word[0])
print(word[3])
print(word[6])
print(word[9])

# Questions for Investigate 3.3.1:
# 1. What letters are at those indices?
# 2. What is the length of the word?

# Investigate 3.3.2
# Run this code and observe:
text = "abcdefg"
for i in range(len(text)):
    print(f"Index {i}: {text[i]}")

# Questions for Investigate 3.3.2:
# 1. What does the loop show?
# 2. What is the range of valid indices?

# Investigate 3.3.3
# Run this code and observe:
palindrome = "racecar"
first = palindrome[0]
last = palindrome[-1]
middle = palindrome[len(palindrome) // 2]
print(first, last, middle)

# Questions for Investigate 3.3.3:
# 1. What is the first, last, and middle character?
# 2. Why does integer division (//) work for finding the middle?

# ========== MODIFY (3 exercises) ==========

# Modify 3.3.1
# TODO: Print the first, middle, and last character of the word
word = "PythonProgramming"
# Your code below:

# Modify 3.3.2
# TODO: Check if the first and last characters are the same
word = "radar"
# Your code below:

# Modify 3.3.3
# TODO: Print every character on a new line using a loop
message = "Hello"
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.3.1
# TODO: Ask for a word. Print the first character, the last character, and the character at index 2.

# Make 3.3.2
# TODO: Ask for a word. Print "Same" if first and last letters match, otherwise "Different".

# Make 3.3.3
# TODO: Create a program that prints a word backwards by accessing indices in reverse order.
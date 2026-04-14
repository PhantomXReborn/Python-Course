"""
Lesson 3.4: String Slicing
Description: Extracting portions of strings using [start:end] syntax
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.4.1
word = "Python"
print(word[0:3])
print(word[2:5])

# Questions for P&R 3.4.1:
# 1. What does [0:3] return?
# 2. Does the end index (3) include character 3?

# P&R 3.4.2
text = "Hello World"
print(text[:5])
print(text[6:])
print(text[:])

# Questions for P&R 3.4.2:
# 1. What does [:5] mean?
# 2. What does [6:] mean?

# P&R 3.4.3
word = "abcdefgh"
print(word[::2])
print(word[1::2])
print(word[::-1])

# Questions for P&R 3.4.3:
# 1. What does ::2 do?
# 2. What does [::-1] do?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.4.1
# Run this code and observe:
sentence = "The quick brown fox"
print(sentence[4:9])
print(sentence[10:15])
print(sentence[16:19])

# Questions for Investigate 3.4.1:
# 1. What words are extracted?
# 2. How are the start and end indices determined?

# Investigate 3.4.2
# Run this code and observe:
url = "https://www.python.org"
domain = url[8:-4]
print(domain)

# Questions for Investigate 3.4.2:
# 1. Why start at 8 and end at -4?
# 2. What does this extract?

# Investigate 3.4.3
# Run this code and observe:
text = "Python"
print(text[0:6:2])
print(text[0:6:3])
print(text[5:0:-1])

# Questions for Investigate 3.4.3:
# 1. What does the third number (step) do?
# 2. What does a negative step do?

# ========== MODIFY (3 exercises) ==========

# Modify 3.4.1
# TODO: Extract "World" from this string using slicing
greeting = "Hello World!"
print(greeting)

# Modify 3.4.2
# TODO: Extract everything except the first and last character
word = "Python"
# Your code below:

# Modify 3.4.3
# TODO: Extract every other character starting from index 1
text = "abcdefghijk"
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.4.1
# TODO: Ask for a word. Print the first 3 letters, last 3 letters, and the middle.

# Make 3.4.2
# TODO: Ask for a sentence. Extract and print the first word (everything before the first space).

# Make 3.4.3
# TODO: Ask for a word. Print it backwards using slicing, then check if it's a palindrome.
"""
Lesson 1.10: String Methods
Description: Using built-in string methods like .upper(), .lower(), .capitalize(), and .title()
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 1.10.1
text = "hello"
print(text.upper())
print(text)

# Questions for P&R 1.10.1:
# 1. Does .upper() change the original variable?
# 2. What would .lower() do to "HELLO"?

# P&R 1.10.2
name = "john doe"
print(name.title())
print(name.capitalize())

# Questions for P&R 1.10.2:
# 1. What is the difference between .title() and .capitalize()?
# 2. Which one capitalizes every word?

# P&R 1.10.3
sentence = "  Python is fun  "
print(sentence.strip())
print(len(sentence))
print(len(sentence.strip()))

# Questions for P&R 1.10.3:
# 1. What does .strip() remove?
# 2. Why is the length different after stripping?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 1.10.1
# Run this code and observe:
word = "programming"
print(word.count("m"))
print(word.find("gram"))

# Questions for Investigate 1.10.1:
# 1. What does .count() do?
# 2. What does .find() return?

# Investigate 1.10.2
# Run this code and observe:
text = "one,two,three"
parts = text.split(",")
print(parts)
print(parts[0])

# Questions for Investigate 1.10.2:
# 1. What does .split() do?
# 2. What type of data is 'parts'?

# Investigate 1.10.3
# Run this code and observe:
greeting = "Hello"
print(greeting.isalpha())
print("123".isdigit())
print("Hello123".isalnum())

# Questions for Investigate 1.10.3:
# 1. What does .isalpha() check for?
# 2. What does .isdigit() check for?

# ========== MODIFY (3 exercises) ==========

# Modify 1.10.1
# TODO: Print the user's input in all uppercase letters
user_text = input("Type something: ")

# Modify 1.10.2
# TODO: Remove the extra spaces from both ends before printing
messy = "    Clean this up    "
print(messy)

# Modify 1.10.3
# TODO: Replace "cat" with "dog" in the sentence
sentence = "I have a cat. My cat is cute."
print(sentence)

# ========== MAKE (3 exercises) ==========

# Make 1.10.1
# TODO: Ask for a word, then print it in lowercase, uppercase, and title case

# Make 1.10.2
# TODO: Ask for a full name, then print how many characters it has (excluding spaces)

# Make 1.10.3
# TODO: Ask for a sentence, then count how many times the letter "e" appears
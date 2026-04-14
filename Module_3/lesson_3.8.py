"""
Lesson 3.8: String Methods (upper, lower, capitalize, title)
Description: Changing the case of strings
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.8.1
text = "Hello World"
print(text.upper())
print(text.lower())

# Questions for P&R 3.8.1:
# 1. What does upper() do?
# 2. Does it change the original text?

# P&R 3.8.2
name = "john doe"
print(name.capitalize())
print(name.title())

# Questions for P&R 3.8.2:
# 1. What does capitalize() do?
# 2. How is title() different from capitalize()?

# P&R 3.8.3
user_input = "  YeS  "
cleaned = user_input.strip().lower()
print(cleaned)
print(cleaned == "yes")

# Questions for P&R 3.8.3:
# 1. Why use strip() and lower() together?
# 2. What does the comparison check?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.8.1
# Run this code and observe:
text = "Python is FUN!"
print(text.swapcase())
print(text.casefold())

# Questions for Investigate 3.8.1:
# 1. What does swapcase() do?
# 2. How is casefold() different from lower()?

# Investigate 3.8.2
# Run this code and observe:
sentence = "the quick brown fox"
print(sentence.title())
print(sentence.capitalize())

# Questions for Investigate 3.8.2:
# 1. Does title() capitalize every word?
# 2. What about words like "the" or "and"?

# Investigate 3.8.3
# Run this code and observe:
password = "Secret123"
print(password.isupper())
print(password.islower())
print(password.upper().isupper())

# Questions for Investigate 3.8.3:
# 1. What do isupper() and islower() check?
# 2. After upper(), is the string all uppercase?

# ========== MODIFY (3 exercises) ==========

# Modify 3.8.1
# TODO: Convert the user's answer to lowercase for case-insensitive comparison
answer = input("Yes or No? ")
if answer == "yes":
    print("You said yes")
# Your code below:

# Modify 3.8.2
# TODO: Fix this name to proper case (first letter uppercase, rest lowercase)
name = "aLiCe"
# Your code below:

# Modify 3.8.3
# TODO: Make this sentence all uppercase and remove punctuation
sentence = "Hello, World!"
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.8.1
# TODO: Ask for a word. Print it in uppercase, lowercase, and title case.

# Make 3.8.2
# TODO: Ask for a sentence. Convert it to all caps and count how many characters changed.

# Make 3.8.3
# TODO: Create a case-insensitive login system. Ask for username (case-insensitive) and password (case-sensitive).
"""
Lesson 3.7: String Methods (strip, lstrip, rstrip)
Description: Removing whitespace and specific characters from string ends
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.7.1
text = "   Hello   "
print(f"'{text}'")
print(f"'{text.strip()}'")

# Questions for P&R 3.7.1:
# 1. What does strip() remove?
# 2. How many spaces are removed from each end?

# P&R 3.7.2
text = "***Hello***"
print(text.strip("*"))
print(text.lstrip("*"))
print(text.rstrip("*"))

# Questions for P&R 3.7.2:
# 1. What does lstrip() remove?
# 2. What does rstrip() remove?

# P&R 3.7.3
text = "  \t  Hello  \n  "
print(f"'{text.strip()}'")

# Questions for P&R 3.7.3:
# 1. What whitespace characters are removed?
# 2. Does strip() remove tabs and newlines?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.7.1
# Run this code and observe:
user_input = input("Enter your name: ")
print(f"Raw: '{user_input}'")
print(f"Stripped: '{user_input.strip()}'")

# Questions for Investigate 3.7.1:
# 1. What happens if you type spaces before your name?
# 2. Why is strip() useful for user input?

# Investigate 3.7.2
# Run this code and observe:
filename = "image.png"
print(filename.strip(".png"))
print(filename.rstrip(".png"))

# Questions for Investigate 3.7.2:
# 1. What does strip(".png") remove?
# 2. Why might this be dangerous?

# Investigate 3.7.3
# Run this code and observe:
text = ".,!Hello!,. "
print(text.strip(".,! "))
print(text.strip(" .,!"))

# Questions for Investigate 3.7.3:
# 1. Does order of characters in strip() matter?
# 2. What characters are removed?

# ========== MODIFY (3 exercises) ==========

# Modify 3.7.1
# TODO: Clean up this input by stripping whitespace and converting to lowercase
user_input = "  YES  "
# Your code below:

# Modify 3.7.2
# TODO: Remove the prefix "www." and suffix ".com" from the domain
domain = "www.google.com"
# Your code below:

# Modify 3.7.3
# TODO: Remove all punctuation from the ends but keep internal punctuation
text = "!!!Hello, world!!!"
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.7.1
# TODO: Ask for user input with possible extra spaces. Strip and print the cleaned version.

# Make 3.7.2
# TODO: Ask for a filename. Strip common extensions like .txt, .py, .jpg and print the base name.

# Make 3.7.3
# TODO: Clean up a messy string by removing leading/trailing spaces, tabs, newlines, and asterisks.
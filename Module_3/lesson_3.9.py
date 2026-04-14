"""
Lesson 3.9: String Validation (isalpha, isdigit, isalnum, isspace)
Description: Checking what characters a string contains
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.9.1
print("abc".isalpha())
print("123".isdigit())
print("abc123".isalnum())

# Questions for P&R 3.9.1:
# 1. What does isalpha() check for?
# 2. What does isalnum() allow?

# P&R 3.9.2
print("   ".isspace())
print("Hello".isalpha())
print("Hello123".isalpha())

# Questions for P&R 3.9.2:
# 1. Does isspace() return True for spaces only?
# 2. Is "Hello123" all letters?

# P&R 3.9.3
print("Hello".isupper())
print("hello".islower())
print("Hello".istitle())

# Questions for P&R 3.9.3:
# 1. What does isupper() check?
# 2. What does istitle() check?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.9.1
# Run this code and observe:
values = ["Python", "123", "Python123", "  ", "Hello!"]
for v in values:
    print(f"'{v}': alpha={v.isalpha()}, digit={v.isdigit()}, alnum={v.isalnum()}")

# Questions for Investigate 3.9.1:
# 1. Why does "Python123" return False for isalpha()?
# 2. Why does "Hello!" return False for isalnum()?

# Investigate 3.9.2
# Run this code and observe:
user_input = input("Enter a number: ")
if user_input.isdigit():
    print(f"You entered the number: {int(user_input)}")
else:
    print("That's not a valid number!")

# Questions for Investigate 3.9.2:
# 1. Does isdigit() work for negative numbers?
# 2. Does isdigit() work for decimals?

# Investigate 3.9.3
# Run this code and observe:
test_cases = ["Hello", "hello", "HELLO", "Hello World", "HelloWorld"]
for t in test_cases:
    print(f"'{t}': isupper={t.isupper()}, islower={t.islower()}, istitle={t.istitle()}")

# Questions for Investigate 3.9.3:
# 1. Why is "Hello World" not title case?
# 2. What would make it title case?

# ========== MODIFY (3 exercises) ==========

# Modify 3.9.1
# TODO: Check if the input contains only letters (no spaces or numbers)
user_input = input("Enter your name: ")
# Your code below:

# Modify 3.9.2
# TODO: Validate that a password contains only letters and numbers (no special chars)
password = input("Create password: ")
# Your code below:

# Modify 3.9.3
# TODO: Check if a string is empty or only whitespace
text = "   "
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.9.1
# TODO: Ask for a word. Print "Letters only" if isalpha(), "Numbers only" if isdigit(), else "Mixed or other".

# Make 3.9.2
# TODO: Validate a username: must be alphanumeric, at least 3 characters, no spaces.

# Make 3.9.3
# TODO: Ask for input until the user enters a valid number (digits only), then convert to int.
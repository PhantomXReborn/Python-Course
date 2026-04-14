"""
Lesson 1.5: Comments and Readability
Description: Using comments to document code and make programs easier to understand
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 1.5.1
# This is a comment
print("Hello")
# print("This won't run")

# Questions for P&R 1.5.1:
# 1. How many lines will actually print?
# 2. What character starts a comment?

# P&R 1.5.2
x = 10  # Store age
y = 5   # Store years until retirement
print(x + y)

# Questions for P&R 1.5.2:
# 1. What is the purpose of the comments after the code?
# 2. Does the comment affect how the code runs?

# P&R 1.5.3
"""
This is a
multi-line
comment
"""
print("Multi-line comment above")

# Questions for P&R 1.5.3:
# 1. How many quotes are used for a multi-line comment?
# 2. Does the text inside print?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 1.5.1
# Run this code and observe:
# print("Hidden message")
print("Visible message")
# print("Also hidden")

# Questions for Investigate 1.5.1:
# 1. What is a quick way to temporarily disable code?
# 2. What is this technique called?

# Investigate 1.5.2
# Run this code and observe:
print(5 + 3)  # Addition
print(10 - 4) # Subtraction
print(2 * 6)  # Multiplication

# Questions for Investigate 1.5.2:
# 1. How do comments at line ends help future readers?
# 2. Could you explain what each line does without running it?

# Investigate 1.5.3
# Run this code and observe:
# TODO: Fix this calculation
print(10 / 0)  # This will cause an error

# Questions for Investigate 1.5.3:
# 1. What does TODO usually mean in comments?
# 2. Does commenting out the error line fix the program?

# ========== MODIFY (3 exercises) ==========

# Modify 1.5.1
# TODO: Add a comment explaining what this code does
print("Welcome to Python")

# Modify 1.5.2
# TODO: Uncomment the line below so it prints, but keep the comment symbol on the other two
# print("First")
# print("Second")
# print("Third")

# Modify 1.5.3
# TODO: Add a TODO comment reminding yourself to change the message below
print("Change this message later")

# ========== MAKE (3 exercises) ==========

# Make 1.5.1
# TODO: Write code that prints "Comments are useful" and add a comment above explaining why

# Make 1.5.2
# TODO: Write three lines of code, each with a comment at the end explaining what it does

# Make 1.5.3
# TODO: Write a multi-line comment (using triple quotes) describing what you've learned in Module 1 so far
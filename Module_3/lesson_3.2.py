"""
Lesson 3.2: String Repetition
Description: Repeating strings multiple times using the * operator
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.2.1
star = "*"
print(star * 10)

# Questions for P&R 3.2.1:
# 1. What does "*" * 10 produce?
# 2. How many asterisks are printed?

# P&R 3.2.2
word = "Ha"
print(word * 3)
print((word + " ") * 3)

# Questions for P&R 3.2.2:
# 1. What does "Ha" * 3 give?
# 2. What does (word + " ") * 3 give?

# P&R 3.2.3
line = "-" * 20
print(line)
print("Hello" + line + "World")

# Questions for P&R 3.2.3:
# 1. How long is the line of dashes?
# 2. What does the final print look like?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.2.1
# Run this code and observe:
print("=" * 30)
print("WELCOME")
print("=" * 30)

# Questions for Investigate 3.2.1:
# 1. How would you change the width to 40?
# 2. What character would you use for a dotted line?

# Investigate 3.2.2
# Run this code and observe:
pattern = ".-"
print(pattern * 5)
print((".-" * 3) + ".")

# Questions for Investigate 3.2.2:
# 1. What pattern does .- repeated make?
# 2. How would you make ".-.-.-."?

# Investigate 3.2.3
# Run this code and observe:
print(" " * 5 + "X")
print(" " * 4 + "X")
print(" " * 3 + "X")

# Questions for Investigate 3.2.3:
# 1. What shape is being created?
# 2. How would you make a right-aligned triangle?

# ========== MODIFY (3 exercises) ==========

# Modify 3.2.1
# TODO: Print a border of 50 equals signs around the title
title = "MY PROGRAM"
print(title)

# Modify 3.2.2
# TODO: Create a pyramid pattern with 5 levels using spaces and "*"
# Level 1: "    *"
# Level 2: "   ***"
# Level 3: "  *****"
# Your code below:

# Modify 3.2.3
# TODO: Repeat the user's input 3 times with spaces between
user_word = input("Enter a word: ")
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.2.1
# TODO: Print a Christmas tree shape using "*" and spaces (3 levels plus trunk)

# Make 3.2.2
# TODO: Ask for a character and a number, then print a horizontal line of that character

# Make 3.2.3
# TODO: Create a loading bar that shows 0% to 100% in 10% increments using "#" * percentage
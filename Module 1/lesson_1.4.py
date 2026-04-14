"""
Lesson 1.4: Escape Sequences
Description: Using special characters like newline (\n) and tab (\t) in print statements
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 1.4.1
print("Line1\nLine2\nLine3")

# Questions for P&R 1.4.1:
# 1. How many lines of output will there be?
# 2. What does \n do?

# P&R 1.4.2
print("Name:\tJohn")
print("Age:\t25")

# Questions for P&R 1.4.2:
# 1. What does \t do to the text alignment?
# 2. Would the columns line up nicely?

# P&R 1.4.3
print("She said, \"Hello\"")

# Questions for P&R 1.4.3:
# 1. Why are there backslashes before the quotes?
# 2. What would happen without the backslashes?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 1.4.1
# Run this code and observe:
print("First\\Second")
print("First\tSecond")

# Questions for Investigate 1.4.1:
# 1. What does \\ produce?
# 2. How is \\ different from \t?

# Investigate 1.4.2
# Run this code and observe:
print("C:\\Users\\Name\\Desktop")

# Questions for Investigate 1.4.2:
# 1. Why are there double backslashes?
# 2. What would a single backslash do?

# Investigate 1.4.3
# Run this code and observe:
print("Hello\rWorld")

# Questions for Investigate 1.4.3:
# 1. What does \r (carriage return) do?
# 2. Which word actually appears on screen?

# ========== MODIFY (3 exercises) ==========

# Modify 1.4.1
# TODO: Add \n to split this into three separate lines
print("One Two Three")

# Modify 1.4.2
# TODO: Add tabs so that each item starts in its own column
print("Item:", "Price:", "$10")
print("Item:", "Tax:", "$1")

# Modify 1.4.3
# TODO: Add the correct escape sequence to print: He said "Python is great!"
print("He said Python is great!")

# ========== MAKE (3 exercises) ==========

# Make 1.4.1
# TODO: Write code that prints a small house using only one print() with \n (example: roof, walls, door)

# Make 1.4.2
# TODO: Write code that prints a file path like D:\MyFolder\MyFile.txt using the correct escapes

# Make 1.4.3
# TODO: Write code that prints a list of three items, each on a new line, with a tab before each item
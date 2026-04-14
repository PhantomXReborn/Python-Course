"""
Lesson 1.3: Printing Multiple Items
Description: Printing several things at once using commas and concatenation
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 1.3.1
print("Hello", "Python", "Learner")

# Questions for P&R 1.3.1:
# 1. How many items are being printed?
# 2. What separates the words in the output?

# P&R 1.3.2
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# Questions for P&R 1.3.2:
# 1. What is printed for the variable 'name'?
# 2. Are the words in quotes different from the variables?

# P&R 1.3.3
print("Hello" + "World")
print("Hello", "World")

# Questions for P&R 1.3.3:
# 1. What is the difference between + and , in print?
# 2. Why is there no space between Hello and World in the first line?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 1.3.1
# Run this code and observe:
print(10, 20, 30, sep="-")

# Questions for Investigate 1.3.1:
# 1. What does 'sep' do?
# 2. What would 'sep="*"' produce?

# Investigate 1.3.2
# Run this code and observe:
print("A", "B", "C", sep="", end="!")
print("D")

# Questions for Investigate 1.3.2:
# 1. What does sep="" do?
# 2. Why does "!" appear before D?

# Investigate 1.3.3
# Run this code and observe:
first = "Good"
second = "Morning"
print(first, second)
print(first + " " + second)

# Questions for Investigate 1.3.3:
# 1. Do both lines produce the same output?
# 2. Which method is simpler when you have many items?

# ========== MODIFY (3 exercises) ==========

# Modify 1.3.1
# TODO: Add two more items to this print statement
print("Apple", "Banana")

# Modify 1.3.2
# TODO: Change the separator to " | " (space pipe space)
print("Red", "Blue", "Green", sep=" - ")

# Modify 1.3.3
# TODO: Change the end character so the output ends with ">>>"
print("Calculation complete", end=".\n")

# ========== MAKE (3 exercises) ==========

# Make 1.3.1
# TODO: Write code that prints three of your hobbies on one line separated by commas

# Make 1.3.2
# TODO: Write code that prints your first name and last name with a space between them

# Make 1.3.3
# TODO: Write code that prints "The answer is:" followed by the result of 15 + 30
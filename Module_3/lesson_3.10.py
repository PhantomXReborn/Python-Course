"""
Lesson 3.10: String Formatting (old style %)
Description: Using % formatting to insert values into strings (older method)
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.10.1
name = "Alice"
age = 25
print("My name is %s and I am %d years old" % (name, age))

# Questions for P&R 3.10.1:
# 1. What does %s stand for?
# 2. What does %d stand for?

# P&R 3.10.2
price = 19.99
print("Price: $%.2f" % price)

# Questions for P&R 3.10.2:
# 1. What does %.2f do?
# 2. How would you show 3 decimal places?

# P&R 3.10.3
print("%s has %d apples" % ("Bob", 5))
print("%(name)s has %(count)d apples" % {"name": "Bob", "count": 5})

# Questions for P&R 3.10.3:
# 1. What is the difference between the two formats?
# 2. What does the dictionary version allow?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.10.1
# Run this code and observe:
print("Integer: %d" % 42)
print("Float: %f" % 3.14)
print("String: %s" % "Hello")
print("Hex: %x" % 255)
print("Scientific: %e" % 12345.67)

# Questions for Investigate 3.10.1:
# 1. What does %x do?
# 2. What does %e do?

# Investigate 3.10.2
# Run this code and observe:
print("Right aligned: %10s" % "Hi")
print("Left aligned: %-10s" % "Hi")
print("Zero padded: %05d" % 42)

# Questions for Investigate 3.10.2:
# 1. What does %10s do?
# 2. What does %05d do?

# Investigate 3.10.3
# Run this code and observe:
value = 0.123456
print("%.2f" % value)
print("%.4f" % value)
print("%.0f" % value)

# Questions for Investigate 3.10.3:
# 1. What does rounding do at .0f?
# 2. Does it round or truncate?

# ========== MODIFY (3 exercises) ==========

# Modify 3.10.1
# TODO: Use % formatting to create this sentence: "John is 30 years old"
name = "John"
age = 30
# Your code below:

# Modify 3.10.2
# TODO: Format this float to show 3 decimal places
pi = 3.14159265
# Your code below:

# Modify 3.10.3
# TODO: Align these columns (left align, width 10)
print("Name: Age:")
print("Alice: 25")
print("Bob: 30")
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.10.1
# TODO: Ask for a product name and price. Print "Product: X, Price: $Y.YY" using % formatting.

# Make 3.10.2
# TODO: Create a formatted table with 3 columns: Name, Score, Grade. Use width formatting.

# Make 3.10.3
# TODO: Use dictionary-style % formatting with a template that can be reused for different data.
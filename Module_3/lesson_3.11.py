"""
Lesson 3.11: String Formatting (format() method)
Description: Using the .format() method for more powerful string formatting
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.11.1
name = "Alice"
age = 25
print("My name is {} and I am {} years old".format(name, age))

# Questions for P&R 3.11.1:
# 1. What do the {} braces represent?
# 2. How are the arguments matched to braces?

# P&R 3.11.2
print("{1} {0}".format("World", "Hello"))
print("{name} is {age}".format(name="Bob", age=30))

# Questions for P&R 3.11.2:
# 1. What do the numbers inside braces do?
# 2. What do the named arguments do?

# P&R 3.11.3
print("{:.2f}".format(3.14159))
print("{:10}".format("Hi"))
print("{:^10}".format("Hi"))

# Questions for P&R 3.11.3:
# 1. What does {:.2f} do?
# 2. What does {:^10} do?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.11.1
# Run this code and observe:
print("{:>10}".format("right"))
print("{:<10}".format("left"))
print("{:^10}".format("center"))
print("{:*^10}".format("center"))

# Questions for Investigate 3.11.1:
# 1. What do >, <, ^ do?
# 2. What does the * in {:*^10} do?

# Investigate 3.11.2
# Run this code and observe:
value = 1234567
print("{:,}".format(value))
print("{:,.2f}".format(value))
print("{:b}".format(42))
print("{:x}".format(255))

# Questions for Investigate 3.11.2:
# 1. What does the comma do in formatting?
# 2. What does :b produce?

# Investigate 3.11.3
# Run this code and observe:
data = {"name": "Alice", "age": 25}
print("{name} is {age}".format(**data))
template = "Name: {name}, Age: {age}"
print(template.format(name="Bob", age=30))

# Questions for Investigate 3.11.3:
# 1. What does **data do?
# 2. Can templates be stored separately?

# ========== MODIFY (3 exercises) ==========

# Modify 3.11.1
# TODO: Format this number with commas and 2 decimal places
big_number = 1234567.8910
# Your code below:

# Modify 3.11.2
# TODO: Create a table with columns aligned left, center, and right
print("Name Score Grade")
print("Alice 95 A")
print("Bob 87 B")
# Your code below:

# Modify 3.11.3
# TODO: Use named placeholders to create a reusable template
product = "Laptop"
price = 999.99
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.11.1
# TODO: Ask for a number. Format it with thousands separators and 2 decimal places.

# Make 3.11.2
# TODO: Create a receipt that aligns item, quantity, and price in columns using .format()

# Make 3.11.3
# TODO: Create a reusable template for a business card (name, title, phone, email) and fill it with different data.
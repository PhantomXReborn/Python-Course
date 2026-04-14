"""
Lesson 1.11: F-Strings (Formatted Strings)
Description: Using f-strings to easily embed variables inside strings
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 1.11.1
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")

# Questions for P&R 1.11.1:
# 1. What does the 'f' before the string do?
# 2. What goes inside the {} braces?

# P&R 1.11.2
x = 10
y = 20
print(f"{x} + {y} = {x + y}")

# Questions for P&R 1.11.2:
# 1. Can you put calculations inside {}?
# 2. What would {x * y} produce?

# P&R 1.11.3
price = 19.9999
print(f"Price: {price:.2f}")

# Questions for P&R 1.11.3:
# 1. What does :.2f do to the number?
# 2. How would you show 3 decimal places?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 1.11.1
# Run this code and observe:
first = "John"
last = "Doe"
print(f"{first} {last}")
print(f"{last}, {first}")

# Questions for Investigate 1.11.1:
# 1. How are the two outputs different?
# 2. Can you rearrange variables freely?

# Investigate 1.11.2
# Run this code and observe:
value = 42
print(f"Decimal: {value}")
print(f"Hexadecimal: {value:x}")
print(f"Binary: {value:b}")

# Questions for Investigate 1.11.2:
# 1. What does :x do?
# 2. What does :b do?

# Investigate 1.11.3
# Run this code and observe:
number = 0.123456
print(f"{number:.3f}")
print(f"{number:.1f}")
print(f"{number:.0f}")

# Questions for Investigate 1.11.3:
# 1. What happens when you change the number after :.
# 2. Does .0f round or truncate?

# ========== MODIFY (3 exercises) ==========

# Modify 1.11.1
# TODO: Convert this to an f-string (remove + and ,)
name = "Bob"
age = 30
print("Name: " + name + ", Age: " + str(age))

# Modify 1.11.2
# TODO: Use an f-string to show the total with 2 decimal places
quantity = 3
price = 4.5
total = quantity * price
# Your f-string here:

# Modify 1.11.3
# TODO: Display the percentage with 1 decimal place and a % sign
score = 0.875
# Should print: 87.5%

# ========== MAKE (3 exercises) ==========

# Make 1.11.1
# TODO: Ask for a user's name and favorite number, then use an f-string to print both

# Make 1.11.2
# TODO: Create variables for length and width, then print "Area: X" where X is the product using f-string

# Make 1.11.3
# TODO: Ask for a temperature in Celsius, convert to Fahrenheit, and print using f-string with 1 decimal
"""
Lesson 2.8: Type Conversion (Casting)
Description: Converting between different data types using int(), float(), str(), and bool()
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.8.1
x = 10
y = 3.14
z = "42"
print(float(x))
print(int(y))
print(int(z))

# Questions for P&R 2.8.1:
# 1. What does float(10) become?
# 2. What does int(3.14) do to the decimal?

# P&R 2.8.2
num = 100
text = str(num)
print(text + " is a number")
print(text * 3)

# Questions for P&R 2.8.2:
# 1. What does str(100) produce?
# 2. What does "100" * 3 do?

# P&R 2.8.3
print(bool(1))
print(bool(0))
print(bool("False"))
print(bool(""))

# Questions for P&R 2.8.3:
# 1. Which numbers become False?
# 2. Does the string "False" become True or False?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.8.1
# Run this code and observe:
age = input("Enter your age: ")
next_age = int(age) + 1
print("Next year you'll be", next_age)

# Questions for Investigate 2.8.1:
# 1. Why do we need int(age)?
# 2. What happens if you type "twenty" instead of "20"?

# Investigate 2.8.2
# Run this code and observe:
print(int(True))
print(int(False))
print(bool(0))
print(bool(42))

# Questions for Investigate 2.8.2:
# 1. What integer is True equivalent to?
# 2. What integer is False equivalent to?

# Investigate 2.8.3
# Run this code and observe:
x = 10
y = "5"
# print(x + y)  # Uncomment to see error
print(x + int(y))

# Questions for Investigate 2.8.3:
# 1. Why does x + y cause an error?
# 2. How do we fix it?

# ========== MODIFY (3 exercises) ==========

# Modify 2.8.1
# TODO: Convert all values to strings before concatenating
number = 42
decimal = 3.14
truth = True
result = "Values: " + number + ", " + decimal + ", " + truth
print(result)

# Modify 2.8.2
# TODO: Fix this to calculate total (should be 15)
first = input("First number: ")
second = input("Second number: ")
total = first + second
print("Total:", total)

# Modify 2.8.3
# TODO: Convert the float to an integer (floor)
pi = 3.14159
rounded_down = pi
print(rounded_down)

# ========== MAKE (3 exercises) ==========

# Make 2.8.1
# TODO: Ask for two integers, convert to int, add them, and print the result

# Make 2.8.2
# TODO: Ask for a number as input, convert to int, then print it as a string repeated 3 times

# Make 2.8.3
# TODO: Create a float, convert it to int, then to str, then to bool. Print each result.
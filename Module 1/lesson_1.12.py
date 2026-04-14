"""
Lesson 1.12: Mini Project - Personal Greeting Card
Description: Combine everything from Module 1 to create a personalized greeting card program
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 1.12.1
# Read this complete program and predict the output:
print("=" * 20)
print("GREETING CARD MAKER")
print("=" * 20)
name = input("What is your name? ")
print(f"\nHello {name}!")
print("Hope you're having a great day!")

# Questions for P&R 1.12.1:
# 1. What does "=" * 20 do?
# 2. Where does the user's name appear?

# P&R 1.12.2
occasion = input("Occasion (birthday/holiday/just because): ")
message = input("Write your message: ")
print(f"\nDear {name},")
print(f"Happy {occasion}! {message}")
print("Sincerely, Computer")

# Questions for P&R 1.12.2:
# 1. How many pieces of user input are collected?
# 2. Where is the occasion used?

# P&R 1.12.3
from datetime import datetime
current_year = datetime.now().year
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print(f"\nFun fact: You are {age} years old (or will be this year)!")

# Questions for P&R 1.12.3:
# 1. What does datetime.now().year do?
# 2. Why do we use int() on birth_year?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 1.12.1
# Run this code and observe:
print("+" * 30)
print("|" + " " * 28 + "|")
print("|" + " " * 10 + "WOW!" + " " * 12 + "|")
print("|" + " " * 28 + "|")
print("+" * 30)

# Questions for Investigate 1.12.1:
# 1. How is the box created using strings?
# 2. What would changing the numbers do?

# Investigate 1.12.2
# Run this code and observe:
recipient = input("To: ")
sender = input("From: ")
card = f"""
********************
*                  *
*   Dear {recipient},   *
*                  *
*   Thinking of you *
*                  *
*   - {sender}        *
*                  *
********************
"""
print(card)

# Questions for Investigate 1.12.2:
# 1. What does the triple-quoted string allow?
# 2. How are variables embedded inside?

# Investigate 1.12.3
# Run this code and observe:
color = input("Favorite color: ").lower().strip()
if color == "blue":
    print("Blue like the sky!")
elif color == "red":
    print("Red like a rose!")
else:
    print(f"{color} is a nice color too!")

# Questions for Investigate 1.12.3:
# 1. Why is .lower() and .strip() used on the input?
# 2. What would happen without .lower()?

# ========== MODIFY (3 exercises) ==========

# Modify 1.12.1
# TODO: Add a border made of asterisks (*) around the greeting
name = input("Name: ")
print(f"Hello {name}!")

# Modify 1.12.2
# TODO: Ask for two more details (like favorite food or hobby) and include them in the greeting
name = input("Name: ")
print(f"Hello {name}!")

# Modify 1.12.3
# TODO: Add a message that changes based on the time of day (morning/afternoon/evening)
from datetime import datetime
hour = datetime.now().hour
# Add code to print "Good morning" before 12, "Good afternoon" 12-17, "Good evening" after 17

# ========== MAKE (3 exercises) ==========

# Make 1.12.1
# TODO: Create a birthday card that asks for name, age, and a wish. Use f-strings and borders.

# Make 1.12.2
# TODO: Create a fortune teller program. Ask for name, then print 3 different fortunes based on the length of the name.

# Make 1.12.3
# TODO: Create a complete greeting card with: a decorative border, user's name, a personal message, a fun fact using their input, and a closing signature. Use at least 3 different string methods.
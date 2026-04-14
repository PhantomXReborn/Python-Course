"""
Lesson 2.9: Constants
Description: Using uppercase naming convention for values that shouldn't change
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.9.1
PI = 3.14159
GRAVITY = 9.81
MAX_SPEED = 120
print(PI)
print(GRAVITY)

# Questions for P&R 2.9.1:
# 1. Why are these names in uppercase?
# 2. Can you change a constant's value?

# P&R 2.9.2
DAYS_IN_WEEK = 7
HOURS_IN_DAY = 24
print(DAYS_IN_WEEK * HOURS_IN_DAY)

# Questions for P&R 2.9.2:
# 1. What does this calculation find?
# 2. Why use constants instead of numbers directly?

# P&R 2.9.3
TAX_RATE = 0.08
price = 100
tax = price * TAX_RATE
print(tax)

# Questions for P&R 2.9.3:
# 1. What is the purpose of TAX_RATE?
# 2. If tax changes to 0.10, where do you update it?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.9.1
# Run this code and observe:
CONSTANT = 10
print(CONSTANT)
CONSTANT = 20  # Python allows this
print(CONSTANT)

# Questions for Investigate 2.9.1:
# 1. Does Python prevent changing constants?
# 2. Why use uppercase if Python doesn't enforce it?

# Investigate 2.9.2
# Run this code and observe:
SPEED_OF_LIGHT = 299792458  # meters per second
distance = SPEED_OF_LIGHT * 1  # 1 second
print(distance)

# Questions for Investigate 2.9.2:
# 1. Why is SPEED_OF_LIGHT a good constant?
# 2. What would happen if someone changed it accidentally?

# Investigate 2.9.3
# Run this code and observe:
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
seconds_per_day = SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY
print(seconds_per_day)

# Questions for Investigate 2.9.3:
# 1. How many constants are there?
# 2. Is seconds_per_day a constant? Why or why not?

# ========== MODIFY (3 exercises) ==========

# Modify 2.9.1
# TODO: Convert these to proper constant names (uppercase with underscores)
inches_per_foot = 12
feet_per_yard = 3
yards_per_mile = 1760
# Your code below:

# Modify 2.9.2
# TODO: Use a constant for the discount percentage instead of hardcoding 15
price = 100
discount = price * 0.15
final_price = price - discount
print(final_price)

# Modify 2.9.3
# TODO: Add a constant for the maximum login attempts (should be 3)
attempts = 0
while attempts < 5:  # This number should be a constant
    print("Login attempt", attempts + 1)
    attempts += 1

# ========== MAKE (3 exercises) ==========

# Make 2.9.1
# TODO: Create constants for: MONTHS_IN_YEAR, DAYS_IN_MONTH (average), and HOURS_IN_WEEK

# Make 2.9.2
# TODO: Write a program that converts kilometers to miles using a constant KM_TO_MILES = 0.621371

# Make 2.9.3
# TODO: Create a constant for a maximum score (e.g., MAX_SCORE = 100). Ask for a score and print what percentage it is.
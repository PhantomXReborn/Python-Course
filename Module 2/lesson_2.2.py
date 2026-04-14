"""
Lesson 2.2: Variable Naming Rules
Description: Learning the rules and conventions for naming variables in Python
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 2.2.1
name = "Alice"
_name = "Bob"
name2 = "Charlie"
print(name, _name, name2)

# Questions for P&R 2.2.1:
# 1. Can variables start with an underscore?
# 2. Can variables contain numbers?

# P&R 2.2.2
# 2var = 10  # This would cause an error
var2 = 10
print(var2)

# Questions for P&R 2.2.2:
# 1. Why is '2var' invalid?
# 2. What is the rule about numbers in variable names?

# P&R 2.2.3
my_name = "John"
myName = "Jane"
MY_NAME = "Bob"
print(my_name, myName, MY_NAME)

# Questions for P&R 2.2.3:
# 1. Are these considered different variables?
# 2. Which naming style uses underscores?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 2.2.1
# Run this code and observe:
first_name = "Alice"
lastName = "Smith"
print(first_name, lastName)

# Questions for Investigate 2.2.1:
# 1. What is snake_case and camelCase?
# 2. Which style is more common in Python?

# Investigate 2.2.2
# Run this code and observe:

'''
class = "Math"  # Uncomment to see error
print(class)
'''

# Questions for Investigate 2.2.2:
# 1. What error appears and why?
# 2. What are reserved keywords?

# Investigate 2.2.3
# Run this code and observe:
user_age = 25
user_age_2 = 30
userAge = 35
print(user_age, user_age_2, userAge)

# Questions for Investigate 2.2.3:
# 1. Which of these is most descriptive?
# 2. What makes a variable name "good"?

# ========== MODIFY (3 exercises) ==========

# Modify 2.2.1
# TODO: Rename these variables to follow Python snake_case convention
firstName = "Alice"
lastName = "Johnson"
homeTown = "Chicago"
# Your code below:

# Modify 2.2.2
# TODO: Fix these invalid variable names

'''
2cool = "too cool"
my-var = "hyphen"
total cost = 100
'''

# Your code below:

# Modify 2.2.3
# TODO: Create valid variable names for: a person's height, the current year, and a temporary value
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 2.2.1
# TODO: Create 5 valid variable names that describe your favorite things (e.g., favorite_movie)

# Make 2.2.2
# TODO: Create a variable using camelCase and another using snake_case. Print both.

# Make 2.2.3
# TODO: Try creating an invalid variable name and comment it out. Add a comment explaining why it's invalid.
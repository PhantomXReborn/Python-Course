"""
Lesson 3.6: String Methods (split, join)
Description: Breaking strings into lists and joining lists into strings
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.6.1
sentence = "apple banana cherry"
words = sentence.split()
print(words)
print(words[1])

# Questions for P&R 3.6.1:
# 1. What does split() with no argument do?
# 2. What is the second word?

# P&R 3.6.2
data = "one,two,three,four"
items = data.split(",")
print(items)
print(len(items))

# Questions for P&R 3.6.2:
# 1. What separator is used?
# 2. How many items are created?

# P&R 3.6.3
words = ["join", "these", "words"]
result = " ".join(words)
print(result)
result2 = "-".join(words)
print(result2)

# Questions for P&R 3.6.3:
# 1. What does join() do?
# 2. What is the difference between the two joins?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.6.1
# Run this code and observe:
text = "a  b   c    d"
parts = text.split()
print(parts)
parts_space = text.split(" ")
print(parts_space)

# Questions for Investigate 3.6.1:
# 1. What happens with multiple spaces and split()?
# 2. What happens with split(" ") (single space)?

# Investigate 3.6.2
# Run this code and observe:
csv_data = "name,age,city"
headers = csv_data.split(",")
print(headers)
row = "Alice,25,New York"
values = row.split(",")
for i in range(len(headers)):
    print(f"{headers[i]}: {values[i]}")

# Questions for Investigate 3.6.2:
# 1. What is CSV data?
# 2. How are headers matched with values?

# Investigate 3.6.3
# Run this code and observe:
words = ["Python", "is", "awesome"]
sentence = "***".join(words)
print(sentence)
original = sentence.split("***")
print(original)

# Questions for Investigate 3.6.3:
# 1. Can you use any string as a separator for join?
# 2. Does split reverse the join operation?

# ========== MODIFY (3 exercises) ==========

# Modify 3.6.1
# TODO: Split this sentence into words, then join with " | "
sentence = "One two three four five"
# Your code below:

# Modify 3.6.2
# TODO: Parse this log entry and extract the timestamp and message
log = "2024-01-15 10:30:45 - User logged in"
# Your code below:

# Modify 3.6.3
# TODO: Take a sentence, split into words, reverse the list, then join back
text = "Hello world from Python"
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.6.1
# TODO: Ask for a sentence. Split it into words and print each word on a new line.

# Make 3.6.2
# TODO: Ask for three favorite colors separated by commas. Split, sort, then join with newlines.

# Make 3.6.3
# TODO: Create a program that takes a sentence and capitalizes each word (split, capitalize each, join)
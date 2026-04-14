"""
Lesson 3.5: String Methods (find, count, replace)
Description: Searching and replacing within strings
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.5.1
sentence = "The cat in the hat"
print(sentence.find("cat"))
print(sentence.find("dog"))

# Questions for P&R 3.5.1:
# 1. What index does find() return for "cat"?
# 2. What does find() return when not found?

# P&R 3.5.2
text = "banana"
print(text.count("a"))
print(text.count("na"))
print(text.count("z"))

# Questions for P&R 3.5.2:
# 1. How many "a" characters are in banana?
# 2. Does count() count overlapping matches?

# P&R 3.5.3
message = "I like cats"
new_message = message.replace("cats", "dogs")
print(new_message)
print(message)

# Questions for P&R 3.5.3:
# 1. Does replace() change the original string?
# 2. What is the new message?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.5.1
# Run this code and observe:
text = "Hello Hello Hello"
print(text.find("Hello"))
print(text.find("Hello", 1))
print(text.find("Hello", 10))

# Questions for Investigate 3.5.1:
# 1. What does the second argument to find() do?
# 2. Why does the second find start later?

# Investigate 3.5.2
# Run this code and observe:
sentence = "the quick brown fox jumps over the lazy dog"
print(sentence.count("the"))
print(sentence.count("the", 10, 30))

# Questions for Investigate 3.5.2:
# 1. How many times does "the" appear?
# 2. What do the start and end arguments do?

# Investigate 3.5.3
# Run this code and observe:
story = "I love Python. Python is great!"
new_story = story.replace("Python", "JavaScript")
print(new_story)
new_story_limited = story.replace("Python", "JavaScript", 1)
print(new_story_limited)

# Questions for Investigate 3.5.3:
# 1. What does the third argument (count) do?
# 2. How many replacements happen with limit 1?

# ========== MODIFY (3 exercises) ==========

# Modify 3.5.1
# TODO: Replace all spaces with underscores
text = "Hello world from Python"
# Your code below:

# Modify 3.5.2
# TODO: Find the position of the second occurrence of "is"
sentence = "This is a test. Is it working?"
# Your code below:

# Modify 3.5.3
# TODO: Count how many vowels (a, e, i, o, u) are in the text
text = "Programming is fun"
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.5.1
# TODO: Ask for a sentence. Replace all spaces with hyphens and print the result.

# Make 3.5.2
# TODO: Ask for a word and a sentence. Count how many times the word appears in the sentence.

# Make 3.5.3
# TODO: Ask for a URL. Replace "http://" with "https://" if it exists.
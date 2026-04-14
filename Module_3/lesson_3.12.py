"""
Lesson 3.12: Mini Project - Text Analyzer
Description: Combine string manipulation techniques to analyze user-provided text
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 3.12.1
# Read this complete program and predict the output:
def analyze_text(text):
    print("=" * 40)
    print("TEXT ANALYZER")
    print("=" * 40)
    print(f"Original: '{text}'")
    print(f"Length: {len(text)} characters")
    print(f"Words: {len(text.split())}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")

analyze_text("  Hello World  ")

# Questions for P&R 3.12.1:
# 1. How many words are counted?
# 2. Does strip() affect word count?

# P&R 3.12.2
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

sample = "Hello World"
print(f"Vowels in '{sample}': {count_vowels(sample)}")

# Questions for P&R 3.12.2:
# 1. How many vowels are in "Hello World"?
# 2. Are both uppercase and lowercase counted?

# P&R 3.12.3
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

print(reverse_words("Python is fun"))
print(reverse_words("Hello world from Python"))

# Questions for P&R 3.12.3:
# 1. What does reverse_words do to word order?
# 2. Does it reverse characters or words?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 3.12.1
# Run this code and observe:
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

test_strings = ["racecar", "hello", "A man a plan a canal panama", "Python"]
for t in test_strings:
    result = is_palindrome(t)
    print(f"'{t}' -> {result}")

# Questions for Investigate 3.12.1:
# 1. Why do we remove spaces and convert to lowercase?
# 2. Is "A man a plan a canal panama" a palindrome?

# Investigate 3.12.2
# Run this code and observe:
def count_char_types(text):
    letters = sum(c.isalpha() for c in text)
    digits = sum(c.isdigit() for c in text)
    spaces = sum(c.isspace() for c in text)
    other = len(text) - letters - digits - spaces
    return letters, digits, spaces, other

sample = "Hello 123! How are you?"
l, d, s, o = count_char_types(sample)
print(f"Letters: {l}, Digits: {d}, Spaces: {s}, Other: {o}")

# Questions for Investigate 3.12.2:
# 1. What counts as "other" characters?
# 2. Are punctuation marks counted as other?

# Investigate 3.12.3
# Run this code and observe:
def find_common_words(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    common = words1 & words2
    return common

text_a = "the quick brown fox jumps"
text_b = "the lazy dog jumps over"
common = find_common_words(text_a, text_b)
print(f"Common words: {common}")

# Questions for Investigate 3.12.3:
# 1. What does the & operator do with sets?
# 2. Why convert to lowercase?

# ========== MODIFY (3 exercises) ==========

# Modify 3.12.1
# TODO: Add punctuation removal to the palindrome checker
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
# Add removal for commas, periods, exclamation marks

# Modify 3.12.2
# TODO: Add a feature to find the most common word in a text
text = "the cat and the dog and the bird"
# Your code below:

# Modify 3.12.3
# TODO: Create a word frequency counter (dictionary of word -> count)
sentence = "hello world hello python world hello"
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 3.12.1
# TODO: Create a complete text analyzer that shows: character count, word count, sentence count, average word length.

# Make 3.12.2
# TODO: Build a program that asks for a sentence, then asks for a word to replace and a new word, and shows the result.

# Make 3.12.3
# TODO: Create an acronym generator: ask for a phrase, extract first letter of each word, uppercase, and join.
"""
Lesson 4.7: The random Module
Description: Generating random numbers with random(), randint(), choice(), shuffle()
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.7.1
import random
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

# Questions for P&R 4.7.1:
# 1. What range of numbers can appear?
# 2. Are the numbers truly random?

# P&R 4.7.2
import random
print(random.random())
print(random.uniform(1, 10))

# Questions for P&R 4.7.2:
# 1. What range does random() return?
# 2. What does uniform(1,10) do?

# P&R 4.7.3
import random
colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors))
random.shuffle(colors)
print(colors)

# Questions for P&R 4.7.3:
# 1. What does choice() do?
# 2. What does shuffle() do to the list?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.7.1
# Run this code and observe:
import random
random.seed(42)
print(random.randint(1, 100))
print(random.randint(1, 100))
random.seed(42)
print(random.randint(1, 100))
print(random.randint(1, 100))

# Questions for Investigate 4.7.1:
# 1. What does seed() do?
# 2. Why are the sequences the same after resetting seed?

# Investigate 4.7.2
# Run this code and observe:
import random
items = ["a", "b", "c", "d", "e"]
print(random.sample(items, 3))
print(random.choices(items, k=3))

# Questions for Investigate 4.7.2:
# 1. Does sample() allow repeats?
# 2. Does choices() allow repeats?

# Investigate 4.7.3
# Run this code and observe:
import random
print(random.triangular(1, 10, 5))
print(random.gauss(0, 1))
print(random.expovariate(0.5))

# Questions for Investigate 4.7.3:
# 1. What distributions do these generate?
# 2. Which one is the normal distribution?

# ========== MODIFY (3 exercises) ==========

# Modify 4.7.1
# TODO: Generate a random even number between 1 and 100
import random
# Your code below:

# Modify 4.7.2
# TODO: Randomly select 3 unique winners from a list of 10 names
names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
# Your code below:

# Modify 4.7.3
# TODO: Simulate rolling two dice and print their sum
import random
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 4.7.1
# TODO: Create a random password generator: 8 characters, letters and numbers.

# Make 4.7.2
# TODO: Simulate a coin flip 100 times and count heads vs tails.

# Make 4.7.3
# TODO: Create a number guessing game (1-100) with random target.
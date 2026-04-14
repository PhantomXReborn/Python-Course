"""
Lesson 4.12: Mini Project - Scientific Calculator
Description: Combine all numeric operations into a scientific calculator
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.12.1
# Read this complete program and predict the output:
def basic_calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else "Error: Division by zero"
    elif op == '//':
        return a // b if b != 0 else "Error: Division by zero"
    elif op == '%':
        return a % b if b != 0 else "Error: Division by zero"
    elif op == '**':
        return a ** b

print(basic_calc(10, 3, '/'))
print(basic_calc(10, 0, '/'))

# Questions for P&R 4.12.1:
# 1. What does the function return for 10/3?
# 2. How does it handle division by zero?

# P&R 4.12.2
import math
def trig_calc(angle_deg, func):
    rad = math.radians(angle_deg)
    if func == 'sin':
        return math.sin(rad)
    elif func == 'cos':
        return math.cos(rad)
    elif func == 'tan':
        return math.tan(rad)

print(trig_calc(45, 'sin'))
print(trig_calc(60, 'cos'))
print(trig_calc(90, 'tan'))

# Questions for P&R 4.12.2:
# 1. What is sin(45°) approximately?
# 2. Why is tan(90°) large?

# P&R 4.12.3
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return complex((-b)/(2*a), math.sqrt(-discriminant)/(2*a)), complex((-b)/(2*a), -math.sqrt(-discriminant)/(2*a))
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

print(solve_quadratic(1, -3, 2))
print(solve_quadratic(1, 0, 1))

# Questions for P&R 4.12.3:
# 1. What are the roots of x² - 3x + 2 = 0?
# 2. What are the roots of x² + 1 = 0?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.12.1
# Run this code and observe:
import random
def roll_dice(sides, rolls):
    results = [random.randint(1, sides) for _ in range(rolls)]
    return sum(results), max(results), min(results), sum(results)/len(results)

total, highest, lowest, avg = roll_dice(6, 100)
print(f"Total: {total}, High: {highest}, Low: {lowest}, Avg: {avg:.2f}")

# Questions for Investigate 4.12.1:
# 1. What does the function return?
# 2. What would average be for fair dice?

# Investigate 4.12.2
# Run this code and observe:
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(84))
print(prime_factors(97))

# Questions for Investigate 4.12.2:
# 1. What are the prime factors of 84?
# 2. Is 97 prime?

# Investigate 4.12.3
# Run this code and observe:
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# Questions for Investigate 4.12.3:
# 1. What is the 10th Fibonacci number?
# 2. How fast do Fibonacci numbers grow?

# ========== MODIFY (3 exercises) ==========

# Modify 4.12.1
# TODO: Add a factorial function to the calculator
import math
def calculator():
    # Add factorial option here
    pass

# Modify 4.12.2
# TODO: Add logarithm functions (log, log10, log2) to the calculator
# Your code below:

# Modify 4.12.3
# TODO: Add a memory feature to store and recall previous results
memory = 0
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 4.12.1
# TODO: Create a complete scientific calculator with: basic ops, trig, logs, power, factorial, memory.

# Make 4.12.2
# TODO: Build a statistics calculator that takes a list of numbers and returns mean, median, mode, std dev.

# Make 4.12.3
# TODO: Create a unit converter: length (miles/km), temperature (C/F), weight (kg/lbs), currency.
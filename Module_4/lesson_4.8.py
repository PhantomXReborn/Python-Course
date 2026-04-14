"""
Lesson 4.8: Working with Fractions and Decimals
Description: Using Fraction for rational numbers and Decimal for precise decimals
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.8.1
from fractions import Fraction
f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
print(f1 + f2)
print(f1 - f2)

# Questions for P&R 4.8.1:
# 1. What is 1/3 + 1/6 as a fraction?
# 2. Does Fraction automatically simplify?

# P&R 4.8.2
from fractions import Fraction
print(Fraction(0.75))
print(Fraction("0.75"))

# Questions for P&R 4.8.2:
# 1. Why are the two results different?
# 2. Which method is more accurate?

# P&R 4.8.3
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))
print(0.1 + 0.2)

# Questions for P&R 4.8.3:
# 1. Which result is exact?
# 2. Why use Decimal for money?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.8.1
# Run this code and observe:
from fractions import Fraction
frac = Fraction(2, 4)
print(frac)
print(frac.numerator)
print(frac.denominator)
print(float(frac))

# Questions for Investigate 4.8.1:
# 1. Does Fraction(2,4) simplify to 1/2?
# 2. How do you get numerator and denominator?

# Investigate 4.8.2
# Run this code and observe:
from decimal import Decimal, getcontext
getcontext().prec = 4
print(Decimal('1') / Decimal('3'))
getcontext().prec = 10
print(Decimal('1') / Decimal('3'))

# Questions for Investigate 4.8.2:
# 1. What does getcontext().prec control?
# 2. How many digits are shown with prec=4?

# Investigate 4.8.3
# Run this code and observe:
from fractions import Fraction
total = Fraction(0)
for i in range(1, 11):
    total += Fraction(1, i)
print(total)
print(float(total))

# Questions for Investigate 4.8.3:
# 1. What is the sum of 1 + 1/2 + 1/3 + ... + 1/10?
# 2. Is the Fraction result exact?

# ========== MODIFY (3 exercises) ==========

# Modify 4.8.1
# TODO: Add 2/3 and 3/4 using Fraction
from fractions import Fraction
# Your code below:

# Modify 4.8.2
# TODO: Calculate 10% tax on $19.99 using Decimal (exact)
from decimal import Decimal
price = Decimal('19.99')
# Your code below:

# Modify 4.8.3
# TODO: Multiply Fraction(5, 8) by Fraction(2, 3)
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 4.8.1
# TODO: Create a recipe scaler that multiplies all fractions (e.g., 1/2 cup * 2 = 1 cup)

# Make 4.8.2
# TODO: Calculate compound interest with Decimal for exact money calculations

# Make 4.8.3
# TODO: Compare Fraction and float precision by calculating 1/3 + 1/3 + 1/3
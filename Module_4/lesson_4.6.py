"""
Lesson 4.6: The math Module (part 2)
Description: Trigonometric functions (sin, cos, tan) and logarithmic functions (log, log10, log2)
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.6.1
import math
print(math.sin(math.pi / 2))
print(math.cos(0))
print(math.tan(math.pi / 4))

# Questions for P&R 4.6.1:
# 1. What is sin(π/2)?
# 2. What is tan(π/4)?

# P&R 4.6.2
import math
print(math.degrees(math.pi))
print(math.radians(180))

# Questions for P&R 4.6.2:
# 1. What does degrees() do?
# 2. What does radians() do?

# P&R 4.6.3
import math
print(math.log(math.e))
print(math.log10(100))
print(math.log2(8))

# Questions for P&R 4.6.3:
# 1. What is log(e)?
# 2. What is log10(100)?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.6.1
# Run this code and observe:
import math
angle = 30
rad = math.radians(angle)
print(f"sin({angle}°) = {math.sin(rad):.4f}")
print(f"cos({angle}°) = {math.cos(rad):.4f}")
print(f"tan({angle}°) = {math.tan(rad):.4f}")

# Questions for Investigate 4.6.1:
# 1. Why convert degrees to radians?
# 2. What is sin(30°) approximately?

# Investigate 4.6.2
# Run this code and observe:
import math
print(math.asin(1))
print(math.acos(0))
print(math.atan(1))

# Questions for Investigate 4.6.2:
# 1. What do asin, acos, atan do?
# 2. What is atan(1) in degrees?

# Investigate 4.6.3
# Run this code and observe:
import math
print(math.log(100, 10))
print(math.log(64, 2))
print(math.log(81, 3))

# Questions for Investigate 4.6.3:
# 1. What does the second argument to log() do?
# 2. How is log(100,10) related to log10(100)?

# ========== MODIFY (3 exercises) ==========

# Modify 4.6.1
# TODO: Calculate the sine of 45 degrees (convert to radians first)
import math
angle_deg = 45
# Your code below:

# Modify 4.6.2
# TODO: Calculate log base 5 of 125 (should be 3)
import math
# Your code below:

# Modify 4.6.3
# TODO: Convert 2π radians to degrees
import math
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 4.6.1
# TODO: Ask for an angle in degrees. Print its sin, cos, and tan (rounded to 4 decimals).

# Make 4.6.2
# TODO: Calculate the distance between two points using math.hypot(x1-x2, y1-y2)

# Make 4.6.3
# TODO: Calculate the angle of a triangle given opposite and adjacent sides using math.atan2()
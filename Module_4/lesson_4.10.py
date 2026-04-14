"""
Lesson 4.10: Complex Numbers
Description: Working with complex numbers (real + imaginary parts)
"""

# ========== PREDICT & RUN (3 exercises) ==========

# P&R 4.10.1
z1 = 3 + 4j
z2 = 1 + 2j
print(z1 + z2)
print(z1 * z2)

# Questions for P&R 4.10.1:
# 1. What is the real and imaginary part of 3+4j?
# 2. What is (3+4j) * (1+2j)?

# P&R 4.10.2
z = 3 + 4j
print(z.real)
print(z.imag)
print(z.conjugate())

# Questions for P&R 4.10.2:
# 1. What does .real return?
# 2. What does .conjugate() do?

# P&R 4.10.3
import math
z = 3 + 4j
print(abs(z))
print(math.atan2(z.imag, z.real))

# Questions for P&R 4.10.3:
# 1. What does abs(z) calculate (magnitude)?
# 2. What is the angle of 3+4j?

# ========== INVESTIGATE (3 exercises) ==========

# Investigate 4.10.1
# Run this code and observe:
z = 1j
print(z ** 2)
print(z ** 3)
print(z ** 4)

# Questions for Investigate 4.10.1:
# 1. What is j²?
# 2. What pattern do you see in powers of j?

# Investigate 4.10.2
# Run this code and observe:
from cmath import phase, polar
z = 1 + 1j
print(phase(z))
print(polar(z))
print(abs(z))

# Questions for Investigate 4.10.2:
# 1. What is the phase of 1+1j in radians?
# 2. What does polar() return?

# Investigate 4.10.3
# Run this code and observe:
from cmath import exp, pi
z = exp(1j * pi)
print(z)
print(abs(z))

# Questions for Investigate 4.10.3:
# 1. What famous identity is this (e^(iπ) = ?)
# 2. What is the magnitude?

# ========== MODIFY (3 exercises) ==========

# Modify 4.10.1
# TODO: Calculate (5+2j) * (3-4j)
# Your code below:

# Modify 4.10.2
# TODO: Find the magnitude of 6+8j (should be 10)
z = 6 + 8j
magnitude = 0  # Fix this
print(magnitude)

# Modify 4.10.3
# TODO: Create a complex number from polar coordinates (r=5, theta=math.pi/3)
import math, cmath
r = 5
theta = math.pi / 3
# Your code below:

# ========== MAKE (3 exercises) ==========

# Make 4.10.1
# TODO: Ask for real and imaginary parts, create complex number, print its conjugate and magnitude.

# Make 4.10.2
# TODO: Solve quadratic equation ax² + bx + c = 0 with complex roots.

# Make 4.10.3
# TODO: Plot the Mandelbrot set using complex numbers (iterative calculation).
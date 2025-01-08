"""
The abs() Function in Python
The abs() function in Python is used to calculate the absolute value of a number. The absolute value of a number is its distance from zero on the number line, regardless of its sign. In other words:

For positive numbers, the result remains the same.
For negative numbers, the sign is removed, and the result becomes positive.

Syntax of abs() :
abs(number)

number: The number (an integer, float, or a complex number) for which you want to find the absolute value.
"""

# Examples of Using abs()
# Absolute Value of an Integer
result = abs(-10)
print(result)  # Output: 10

# Absolute Value of a Floating-Point Number
result = abs(-3.14)
print(result)  # Output: 3.14

# Absolute Value of Zero
result = abs(0)
print(result)  # Output: 0

# Absolute Value of a Complex Number
# For complex numbers, the abs() function calculates the magnitude using the formula:
#     magnitude = root of((real_part)**2 + (imaginary_part)**2)
result = abs(3 + 4j)
print(result)  # Output: 5.0






"""
The round() function in Python is used to round a floating-point number to a specified number of decimal places.

How round() Works
    If you provide the ndigits argument, round() will round the number to that many decimal places.
    If you don't provide ndigits, it will round the number to the nearest whole number (integer).
    Rounding behavior follows the round half to even strategy (also called bankers' rounding), which rounds halfway cases (like 2.5, 3.5) to the nearest even number.
"""
# Examples of Using round()
# Rounding to the Nearest Integer
# Round a floating-point number to the nearest integer
result = round(3.14159)
print(result)  # Output: 3

# Rounding to a Specific Number of Decimal Places
# Round to 2 decimal places
result = round(3.14159, 2)
print(result)  # Output: 3.14

# Rounding with a Negative ndigits
# You can round to the left of the decimal point (i.e., rounding to tens, hundreds, etc.) by using a negative value for ndigits.
# Round to the nearest ten
result = round(1234, -1)
print(result)  # Output: 1230

# Rounding a Halfway Case
# In Python, the round() function uses round half to even (also known as bankers' rounding), which rounds to the nearest even number when there is a tie.
# Round 2.5 and 3.5
print(round(2.5))  # Output: 2
print(round(3.5))  # Output: 4

"""
Important Notes
Rounding to Nearest Integer:
    If the number is exactly halfway between two integers (like 2.5 or 3.5), Python will round to the nearest even integer (also called bankers' rounding).
"""
# Floating Point Precision:
# Python's round() function does not solve the underlying issues with floating-point precision. It simply rounds the result to a specified number of decimal places.
print(round(0.1 + 0.2, 1))  # Output: 0.3


# Round to the nearest integer
print(round(5.7))  # Output: 6

# Round to 1 decimal place
print(round(3.14159, 1))  # Output: 3.1

# Round to the nearest ten
print(round(457, -1))  # Output: 460

# Round half to even
print(round(2.5))  # Output: 2
print(round(3.5))  # Output: 4



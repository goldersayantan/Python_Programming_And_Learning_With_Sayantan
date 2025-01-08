"""
Assignment operators are used to assign values to variables in Python.
They allow you to store data in variables, update their values,
or perform operations while assigning.
"""

# Examples of Assignment Operators
# Basic Assignment (=)
# The = operator is used to assign a value to a variable.
x = 10  # Assigns 10 to the variable x
print(x)  # Output: 10

# Add and Assign (+=)
# Adds the right operand to the left operand and assigns the result to the left operand.
x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8

# Subtract and Assign (-=)
# Subtracts the right operand from the left operand and assigns the result to the left operand.
x = 10
x -= 4  # Equivalent to x = x - 4
print(x)  # Output: 6

# Multiply and Assign( *=)
# Multiplies the left operand by the right operand and assigns the result to the left operand
x = 6
x *= 3  # Equivalent to x = x * 3
print(x)  # Output: 18

# Divide and Assign (/=)
# Divides the left operand by the right operand and assigns the result to the left operand.
x = 15
x /= 3  # Equivalent to x = x / 3
print(x)  # Output: 5.0 (result is always a float)

# Modulus and Assign (%=)
# Calculates the modulus of the left operand with the right operand and assigns the result to the left operand.
x = 17
x %= 5  # Equivalent to x = x % 5
print(x)  # Output: 2

# Floor Divide and Assign (//=)
# Performs floor division and assigns the result to the left operand.
x = 17
x //= 5  # Equivalent to x = x // 5
print(x)  # Output: 3

# Exponent and Assign (**=)
# Raises the left operand to the power of the right operand and assigns the result to the left operand.
x = 2
x **= 3  # Equivalent to x = x ** 3
print(x)  # Output: 8

# Bitwise AND and Assign (&=)
# Performs a bitwise AND operation and assigns the result to the left operand.
x = 5  # Binary: 0101
x &= 3  # Binary: 0011
print(x)  # Output: 1 (Binary: 0001)

# Bitwise OR and Assign (|=)
# Performs a bitwise OR operation and assigns the result to the left operand.
x = 5  # Binary: 0101
x |= 3  # Binary: 0011
print(x)  # Output: 7 (Binary: 0111)

# Bitwise XOR and Assign (^=)
# Performs a bitwise XOR operation and assigns the result to the left operand.
x = 5  # Binary: 0101
x ^= 3  # Binary: 0011
print(x)  # Output: 6 (Binary: 0110)

# Right Shift and Assign (>>=)
# Shifts the bits of the left operand to the right and assigns the result to the left operand.
x = 8  # Binary: 1000
x >>= 2  # Shift right by 2 bits
print(x)  # Output: 2 (Binary: 0010)

# Left Shift and Assign (<<=)
# Shifts the bits of the left operand to the left and assigns the result to the left operand.
x = 4  # Binary: 0100
x <<= 2  # Shift left by 2 bits
print(x)  # Output: 16 (Binary: 10000)









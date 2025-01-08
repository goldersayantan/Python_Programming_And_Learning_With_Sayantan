"""
Logical operators are used to combine conditional statements or
to evaluate multiple expressions simultaneously.
They work with Boolean values (True or False) and return a Boolean result.
"""

# Logical Operators in Action
# Logical AND (and)
# The and operator returns True if both conditions are True. If any condition is False, it returns False.
a = 10
b = 20

# Both conditions are True
print(a > 5 and b > 15)  # Output: True

# One condition is False
print(a > 15 and b > 15)  # Output: False

# Both conditions are False
print(a < 5 and b < 15)  # Output: False


# Logical OR (or)
# The or operator returns True if at least one condition is True. If both conditions are False, it returns False.
a = 10
b = 20

# Both conditions are True
print(a > 5 or b > 15)  # Output: True

# One condition is True
print(a > 15 or b > 15)  # Output: True

# Both conditions are False
print(a < 5 or b < 15)  # Output: False


# Logical NOT (not)
# The not operator inverts the Boolean value of the expression. If the expression is True, it becomes False and vice versa.
a = 10

# Original condition is True
print(not a > 5)  # Output: False

# Original condition is False
print(not a < 5)  # Output: True


# Chaining Logical Operators
# You can combine multiple logical operators in a single expression. Operator precedence determines the order of evaluation:
# 1. not
# 2. and
# 3. or

a = 10
b = 20
c = 30

# Without parentheses
print(a > 5 and b < 15 or c > 25)  # Output: True

# With parentheses
print((a > 5 and b < 15) or c > 25)  # Output: True





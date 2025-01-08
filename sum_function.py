"""
The sum() function in Python is used to calculate the total (sum) of all the elements in an iterable (like a list, tuple, or set).
It's a quick and convenient way to add up numbers.

Syntax of sum()
sum(iterable, start)

iterable: The iterable (e.g., list, tuple, set) containing numeric values to sum.
start (Optional): A value to add to the sum of the iterable. The default is 0.
"""

# Examples of Using sum()
# Sum of a List
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)  # Output: 15

# Sum of a Tuple
numbers = (10, 20, 30, 40)
result = sum(numbers)
print(result)  # Output: 100

# Using the start Parameter
numbers = [1, 2, 3, 4, 5]
result = sum(numbers, 10)
print(result)  # Output: 25

# Sum of a Set
numbers = {3, 6, 9}
result = sum(numbers)
print(result)  # Output: 18

# Sum of a List with Negative Numbers
numbers = [10, -5, 7, -3]
result = sum(numbers)
print(result)  # Output: 9

# Using sum() with Generator Expressions
result = sum(i for i in range(1, 6))
print(result)  # Output: 15

# Works Only with Numeric Values:
numbers = [1, 'two', 3]
result = sum(numbers)  # Raises TypeError

# Empty Iterable:
empty_result = sum([])
print(empty_result)  # Output: 0

# Precision with Floats:
# When summing floating-point numbers, be mindful of precision issues that arise due to the way floating-point numbers are stored in memory.
float_result = sum([0.1, 0.2, 0.3])
print(float_result)  # Output might be 0.6000000000000001
# We can use round function after it








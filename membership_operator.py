"""
Membership operators are used to test if a value exists in a sequence
(like a string, list, tuple, set, or dictionary).
They return a Boolean value (True or False).
"""

# Examples of Membership Operators
# Using in
# Example with string
text = "Python"
print('P' in text)  # Output: True
print('z' in text)  # Output: False

# Example with list
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # Output: True
print(6 in numbers)  # Output: False


# Using not in
# Example with string
text = "Python"
print('z' not in text)  # Output: True
print('P' not in text)  # Output: False

# Example with list
numbers = [1, 2, 3, 4, 5]
print(6 not in numbers)  # Output: True
print(3 not in numbers)  # Output: False


# Membership in Dictionaries
# For dictionaries, the in and not in operators check for keys (not values).
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Check for keys
print('a' in my_dict)  # Output: True
print('z' in my_dict)  # Output: False

# Check for values (you need to explicitly use `.values()`)
print(1 in my_dict.values())  # Output: True
print(4 in my_dict.values())  # Output: False


# Membership in Sets
# Membership operators are particularly efficient with sets, as sets are optimized for membership checks.
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True
print(6 not in my_set)  # Output: True


# Membership in Nested Structures
# You can use membership operators to check for values in nested structures like lists of lists, or dictionaries of lists.
nested_list = [[1, 2], [3, 4], [5, 6]]

# Check for sublist
print([1, 2] in nested_list)  # Output: True

# Check for an element within sublists (requires a loop or comprehension)
print(1 in nested_list[0])  # Output: True



















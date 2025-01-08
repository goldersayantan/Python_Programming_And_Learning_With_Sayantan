"""
Counting refers to finding the number of occurrences of an element in an iterable (e.g., a list, string, or tuple).
Python provides multiple ways to count elements effectively.

Using the count() Method
The count() method is available for lists, tuples, and strings. It counts the number of times a specific element appears in the iterable.

iterable.count(element)

element: The item whose occurrences you want to count.
"""

# Examples:
# Counting in a List:
numbers = [1, 2, 2, 3, 4, 2, 5]
count_of_2 = numbers.count(2)
print(count_of_2)  # Output: 3

# Counting in a String:
text = "hello world"
count_of_l = text.count('l')
print(count_of_l)  # Output: 3

# Counting in a Tuple:
colors = ('red', 'blue', 'red', 'green', 'red')
count_of_red = colors.count('red')
print(count_of_red)  # Output: 3

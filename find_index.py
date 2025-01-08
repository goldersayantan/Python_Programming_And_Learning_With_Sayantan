"""
In Python, you can find the index (position) of an element in an iterable (e.g., list, string, tuple) using the index() method or loops.
Below are the ways to achieve this.

Using the index() Method
The index() method is used to find the first occurrence of an element in a list, tuple, or string. If the element is not found, it raises a ValueError.

iterable.index(element, start=0, end=len(iterable))

element: The item to search for.
start (optional): The starting index for the search. Default is 0.
end (optional): The ending index for the search. Default is the length of the iterable.
"""

# Examples:
# Finding the Index of an Element in a List
numbers = [10, 20, 30, 40, 50]
index = numbers.index(30)
print(index)  # Output: 2

# Finding the Index in a Subrange
numbers = [10, 20, 30, 40, 30, 50]
index = numbers.index(30, 3)  # Start searching from index 3
print(index)  # Output: 4

# Finding the Index in a String
text = "hello world"
index = text.index("o")
print(index)  # Output: 4

# Error When Element is Not Found
numbers = [10, 20, 30]
print(numbers.index(40))  # Raises ValueError: 40 is not in list


# Using Loops to Find the Index
# If you want to avoid the ValueError when an element is not found, you can use a loop.

numbers = [10, 20, 30, 40, 50]
search_item = 30

# Using a for loop
for i, num in enumerate(numbers):
    if num == search_item:
        print(i)  # Output: 2
        break
else:
    print("Element not found")


# Finding All Indices of an Element
# The index() method only finds the first occurrence of an element. If you want to find all occurrences, you can use a loop or list comprehension.

numbers = [10, 20, 30, 20, 40, 20]
search_item = 20
# Using list comprehension
indices = [i for i, num in enumerate(numbers) if num == search_item]
print(indices)  # Output: [1, 3, 5]


# Finding the Index with Tuples
tuple_data = (10, 20, 30, 40, 50)
index = tuple_data.index(30)
print(index)  # Output: 2


# Finding the Index in a String
text = "banana"
index = text.index("a")
print(index)  # Output: 1

text = "banana"
index = text.find("z")
print(index)  # Output: -1


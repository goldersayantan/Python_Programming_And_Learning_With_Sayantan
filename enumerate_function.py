"""
The enumerate() function in Python is used to loop over an iterable (like a list, tuple, or string)
while keeping track of the index of the current item. It adds a counter to the iterable and
returns it in the form of an enumerate object, which can then be converted into a list of tuples,
where each tuple contains the index and the corresponding element.

Syntax of enumerate()
enumerate(iterable, start=0)

iterable: The iterable (e.g., list, tuple, string, etc.) you want to enumerate.
start (optional): The starting index for the counter. The default is 0.
"""

# Examples of Using enumerate()
# Basic Example
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry

# Changing the Starting Index
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):    # Index starting from 1.
    print(index, fruit)

# Output:
# 1 apple
# 2 banana
# 3 cherry

# Converting an Enumerate Object to a List
fruits = ['apple', 'banana', 'cherry']
enumerated_list = list(enumerate(fruits))
print(enumerated_list)
# Output:
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]


# Enumerating Strings
text = "hello"
for index, char in enumerate(text):
    print(index, char)
# Output:
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o


# Enumerating with a Set
numbers = {10, 20, 30}
for index, number in enumerate(numbers):
    print(index, number)

# Output (order may vary):
# 0 10
# 1 20
# 2 30

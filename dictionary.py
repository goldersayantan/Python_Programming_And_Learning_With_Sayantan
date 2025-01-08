"""In Python, a dictionary is an unordered, mutable, and indexed collection of key-value pairs.
It is one of the most powerful and widely used data types, enabling efficient data storage and retrieval.

Dictionaries are defined using curly braces {} with key-value pairs separated by a colon (:),
and each pair separated by a comma."""


# Creating a Dictionary
# Empty dictionary:
dict1 = {}

# Dictionary with key-value pairs:
dict2 = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using the dict() constructor
dict3 = dict(name="Bob", age=30, city="San Francisco")

# Nested dictionary:
dict4 = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}


# Accessing Dictionary Elements
# Accessing values using keys:
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 25

# Using the get() method (avoids errors if the key is not present):
my_dict = {"name": "Alice", "age": 25}
print(my_dict.get("name"))      # Output: Alice
print(my_dict.get("address"))   # Output: None
print(my_dict.get("address", "Not Found"))  # Output: Not Found

# Modifying a Dictionary
# Adding or updating key-value pairs:
my_dict = {"name": "Alice", "age": 25}
my_dict["city"] = "New York"  # Adding a new key-value pair
my_dict["age"] = 26           # Updating an existing key
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Removing key-value pairs:
# Using pop():
my_dict = {"name": "Alice", "age": 25}
removed_value = my_dict.pop("age")
print(my_dict)        # Output: {'name': 'Alice'}
print(removed_value)  # Output: 25

# Using del:
my_dict = {"name": "Alice", "age": 25}
del my_dict["age"]
print(my_dict)  # Output: {'name': 'Alice'}

# Using popitem() (removes the last inserted key-value pair):
my_dict = {"name": "Alice", "age": 25}
my_dict.popitem()
print(my_dict)  # Output: {'name': 'Alice'}

# Using clear() (removes all elements):
my_dict = {"name": "Alice", "age": 25}
my_dict.clear()
print(my_dict)  # Output: {}


# Dictionary Operations
# Checking if a key exists:
my_dict = {"name": "Alice", "age": 25}
print("name" in my_dict)    # Output: True
print("address" in my_dict) # Output: False

# Iterating through a dictionary:
# Keys:
my_dict = {"name": "Alice", "age": 25}
for key in my_dict:
    print(key)
# Output:
# name
# age

# Values:
for value in my_dict.values():
    print(value)
# Output:
# Alice
# 25

# Key-value pairs:
for key, value in my_dict.items():
    print(key, ":", value)
# Output:
# name : Alice
# age : 25

# Length of dictionary
my_dict = {"name": "Alice", "age": 25}
print(len(my_dict))  # Output: 2


# Dictionary Methods
# keys(): Returns a view object of all keys in the dictionary.
my_dict = {"name": "Alice", "age": 25}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# values(): Returns a view object of all values in the dictionary.
print(my_dict.values())  # Output: dict_values(['Alice', 25])

# items(): Returns a view object of key-value pairs.
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])

# update(): Updates the dictionary with key-value pairs from another dictionary or iterable.
my_dict = {"name": "Alice"}
my_dict.update({"age": 25, "city": "New York"})
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# copy(): Returns a shallow copy of the dictionary.
original = {"name": "Alice", "age": 25}
copy_dict = original.copy()
print(copy_dict)  # Output: {'name': 'Alice', 'age': 25}


# Nested Dictionary
# Dictionaries can contain other dictionaries as values, creating a nested structure
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(nested_dict["person1"])  # Output: {'name': 'Alice', 'age': 25}
print(nested_dict["person1"]["name"])  # Output: Alice


# Use Cases of Dictionaries
# Storing structured data:
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Representing mappings:
students = {101: "Alice", 102: "Bob", 103: "Charlie"}

# Counting occurrences:
text = "hello"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Storing configuration or settings:
config = {"theme": "dark", "language": "English", "version": 1.0}


# Copying a Dictionary in Python
# Shallow Copy (copy() Method)
# A shallow copy creates a new dictionary with the same key-value pairs as the original dictionary.
# It copies the references of any mutable objects (like lists, dictionaries, etc.) inside the dictionary, rather than the objects themselves.
original = {"a": 1, "b": [2, 3]}
copy_dict = original.copy()
print(copy_dict)  # Output: {'a': 1, 'b': [2, 3]}
# Modifying the copy
copy_dict["a"] = 10
copy_dict["b"].append(4)
# Original dictionary remains unchanged for keys with immutable values
print(original)  # Output: {'a': 1, 'b': [2, 3, 4]}


# Using the dict() Constructor
# Another way to make a shallow copy is by passing the original dictionary to the dict() constructor.
original = {"a": 1, "b": [2, 3]}
copy_dict = dict(original)
print(copy_dict)  # Output: {'a': 1, 'b': [2, 3]}
# Modifying the copy
copy_dict["b"].append(4)
# The original dictionary's mutable values are also affected
print(original)  # Output: {'a': 1, 'b': [2, 3, 4]}


# Deep Copy (Using copy Module)
# A deep copy creates a completely independent copy of the dictionary, including all nested objects.
# Changes to the copy do not affect the original dictionary, even for mutable objects.
# Use the copy.deepcopy() method for deep copying.
import copy
original = {"a": 1, "b": [2, 3]}
deep_copy_dict = copy.deepcopy(original)
print(deep_copy_dict)  # Output: {'a': 1, 'b': [2, 3]}
# Modifying the deep copy
deep_copy_dict["b"].append(4)
# Original dictionary remains unchanged
print(original)  # Output: {'a': 1, 'b': [2, 3]}


# get() method
"""
The get() method in Python is primarily used with dictionaries to safely retrieve the value of a key without raising an error if the key is not found. It is an alternative to accessing dictionary keys directly (e.g., dictionary[key]), which would throw a KeyError if the key doesn't exist.

Syntax of get()
dictionary.get(key, default=None)

key: The key whose value you want to retrieve.
default (optional): The value to return if the key is not found. By default, it is None.
"""

# Basic Example
student = {'name': 'Alice', 'age': 25, 'grade': 'A'}

# Using get()
print(student.get('name'))   # Output: 'Alice'
print(student.get('age'))    # Output: 25
# Key not found
print(student.get('address'))  # Output: None


# Providing a Default Value
student = {'name': 'Alice', 'age': 25}
# Key not found with default value
print(student.get('address', 'Not Available'))  # Output: 'Not Available'
print(student.get('grade', 'N/A'))             # Output: 'N/A'


# Using get() to Avoid Errors
# Without get()
student = {'name': 'Alice'}
# print(student['age'])  # Raises KeyError: 'age'
# With get()
print(student.get('age'))  # Output: None


"""In Python, tuples are an ordered, immutable collection of elements.
Like lists, tuples can hold elements of different data types,
but their immutability makes them more efficient and suitable for data
that should not change after creation."""

# Creating a Tuple
# Tuples are defined using parentheses (()), with elements separated by commas.
# Empty tuple
tuple1 = ()

# Tuple with a single element (comma is mandatory for a single-element tuple)
tuple2 = (5,)

# Tuple with multiple elements
tuple3 = (1, 2, 3)

# Tuple with mixed data types
tuple4 = (1, "Hello", 3.14, True)

# Nested tuple
tuple5 = (1, (2, 3), (4, 5))

# Without parentheses (Python automatically treats it as a tuple)
tuple6 = 1, 2, 3


# Accessing Tuple Elements
# Tuples support indexing and slicing, just like lists.
# Indexing: Access elements by their index (starting from 0).
my_tuple = (10, 20, 30, 40)
print(my_tuple[0])   # Output: 10
print(my_tuple[-1])  # Output: 40 (negative indexing starts from the end)

# Slicing: Extract a subset of the tuple.
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])  # Output: (20, 30, 40)
print(my_tuple[:3])   # Output: (10, 20, 30)
print(my_tuple[::2])  # Output: (10, 30, 50)


# Immutability of Tuple
# Tuples are immutable, meaning their elements cannot be changed, added, or removed after creation.
# Attempting to modify a tuple will raise an error:
my_tuple1 = (1, 2, 3)
# my_tuple1[0] = 10  # This will raise a TypeError

# However, if a tuple contains mutable objects (like lists), those objects can be modified:
my_tuple = (1, [2, 3], 4)
my_tuple[1][0] = 99
print(my_tuple)  # Output: (1, [99, 3], 4)


# Tuple Operations
# Concatenation: Combining two or more tuples using the + operator.
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
result = tup1 + tup2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition: Repeating a tuple using the * operator.
tup1 = (1, 2, 3)
print(tup1 * 2)  # Output: (1, 2, 3, 1, 2, 3)

# Membership: Checking if an element exists in a tuple using in or not in.
my_tuple = (1, 2, 3)
print(2 in my_tuple)  # Output: True
print(4 not in my_tuple)  # Output: True

# Iterating through a tuple:
my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3


# Built-in Tuple Methods
# Since tuples are immutable, they have fewer methods compared to lists. The key tuple methods are:

# count(): Returns the count of a specific element in the tuple.
my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2))  # Output: 2

# index(): Returns the index of the first occurrence of a value.
my_tuple = (1, 2, 3)
print(my_tuple.index(2))  # Output: 1


# Converting Between Tuples and Other Data Types
# Convert a list to a tuple:
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# Convert a tuple to a list:
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]


# Use cases of tuples
# Returning multiple values from a function:
def get_coordinates():
    return (10, 20)


coords = get_coordinates()
print(coords)  # Output: (10, 20)

# Storing data that should not be changed (e.g., days of the week):
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# As keys in dictionaries:
locations = {("40.7128° N", "74.0060° W"): "New York", ("34.0522° N", "118.2437° W"): "Los Angeles"}


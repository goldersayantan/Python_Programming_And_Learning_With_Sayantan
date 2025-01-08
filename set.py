"""In Python, a set is an unordered, mutable, and unindexed collection of unique elements.
Sets are useful when you need to store items without duplicates and perform operations
like unions, intersections, and differences efficiently.
        1. Unique elements
        2. Unordered
        3. Mutable
        4. Immutable elements
"""

# Creating a Set
# Empty Set: Use the set() function to create an empty set. Using {} will create an empty dictionary, not a set.
empty_set = set()
print(empty_set)  # Output: set()

# Set with Elements: Sets can be created by enclosing elements in curly braces {} or by using the set() function.
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

another_set = set([1, 2, 3, 3, 4])  # Removing duplicates from a list
print(another_set)  # Output: {1, 2, 3, 4}

# Set from String: Converting a string into a set splits it into unique characters.
char_set = set("hello")
print(char_set)  # Output: {'h', 'e', 'l', 'o'}


# Accessing Elements in a Set
# Since sets are unordered, elements cannot be accessed by indexing or slicing. Instead, you can:
# Iterate through the set:
my_set = {1, 2, 3, 4}
for item in my_set:
    print(item)

# Check membership:
my_set = {1, 2, 3, 4}
print(2 in my_set)    # Output: True
print(5 in my_set)    # Output: False


# Modifying a Set
# Adding Elements:
# Use add() to add a single element.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Adding Multiple Elements:
# Use update() to add multiple elements (can take any iterable like a list, tuple, or another set).
my_set = {1, 2, 3}
my_set.update([4, 5, 6])  # We are passing a list as argument.
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Use discard() to remove an element (does not raise an error if the element does not exist).
my_set = {1, 2, 3}
my_set.discard(4)  # No error, even though 4 is not in the set
print(my_set)  # Output: {1, 2, 3}

# Use pop() to remove and return an arbitrary element (since sets are unordered).
my_set = {1, 2, 3}
removed_element = my_set.pop()
print(removed_element)  # Output: 1 (or any other element)
print(my_set)  # Output: {2, 3}

# Clearing the Set:
# Use clear() to remove all elements.
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()


# Set Operations
# Union: Combines elements from both sets (removes duplicates).
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)          # Output: {1, 2, 3, 4, 5}
print(set1.union(set2))     # Output: {1, 2, 3, 4, 5}

# Intersection: Returns elements common to both sets.
print(set1 & set2)          # Output: {3}
print(set1.intersection(set2))  # Output: {3}

# Difference: Returns elements in the first set but not in the second.
print(set1 - set2)          # Output: {1, 2}
print(set1.difference(set2))  # Output: {1, 2}

# Symmetric Difference: Returns elements in either of the sets, but not in both.
print(set1 ^ set2)          # Output: {1, 2, 4, 5}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}


# Some another set methods
# issubset() and issuperset()
x_set = {1, 2, 3, 4, 5}
y_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(x_set.issubset(y_set))  # True: x_set is subset of y_set
print(y_set.issuperset(x_set))  # True: y_set is superset of x_set


# Frozen Sets
# A frozen set is an immutable version of a set. You cannot add, remove, or modify its elements after creation.
frozen = frozenset([1, 2, 3, 3])
print(frozen)  # Output: frozenset({1, 2, 3})

# Operations like union, intersection, etc., are still allowed
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])
print(set1 | set2)  # Output: frozenset({1, 2, 3, 4, 5})


# Use Cases of Sets
# Removing Duplicates:
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Membership Testing: Sets provide efficient membership testing compared to lists.
my_set = {1, 2, 3}
print(2 in my_set)  # Output: True

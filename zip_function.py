"""
The zip() function in Python is used to combine two or more iterables (like lists, tuples, or strings)
into a single iterator of tuples. Each tuple contains elements from the iterables at the same position (index).
It's a convenient way to "pair" data from multiple sources.

Syntax of zip()
zip(iterable1, iterable2, ..., iterableN)

iterable1, iterable2, ..., iterableN: The iterables to be combined (e.g., lists, tuples, strings, etc.).
"""

# Examples of Using zip()
# Zipping Two Lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
result = zip(names, ages)
print(list(result))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Zipping Lists of Unequal Length
list1 = [1, 2, 3]
list2 = ['a', 'b']
result = zip(list1, list2)
print(list(result))  # Output: [(1, 'a'), (2, 'b')]

# Zipping More Than Two Iterables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10.5, 20.5, 30.5]
result = zip(list1, list2, list3)
print(list(result))  # Output: [(1, 'a', 10.5), (2, 'b', 20.5), (3, 'c', 30.5)]

# Zipping Strings
string1 = "ABCD"
string2 = "1234"
result = zip(string1, string2)
print(list(result))  # Output: [('A', '1'), ('B', '2'), ('C', '3'), ('D', '4')]

# Unpacking Zipped Objects
zipped = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
names, ages = zip(*zipped)
print(names)  # Output: ('Alice', 'Bob', 'Charlie')
print(ages)   # Output: (25, 30, 35)







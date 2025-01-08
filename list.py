"""In Python, lists are one of the most versatile and widely used data types.
A list is an ordered, mutable (modifiable), and heterogeneous collection,
meaning it can store items of different data types, such as integers, floats, strings,
or even other lists."""

# Empty List
list1 = []

# List of integers
list2 = [1, 2, 3, 4, 5]

# List of mixed data types
list3 = [1, 2, "ABC", True, 3.14]

# Nested list
list4 = [1, [2, 3], [4, 5]]

# Using the list constructor
list5 = list((1, 2, 3, 4))  # Converting a tuple into a list


# Accessing list elements
# indexing : Accessing elements by their position (index start at 0).
my_lst = [10, 20, 30, 40, 50]
print(my_lst[0])
print(my_lst[-1])  # Negative indexing starts from the end

# slicing : Extracting a subset of the list
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40] (from index 1 to 3)
print(my_list[:3])   # Output: [10, 20, 30] (from start to index 2)
print(my_list[::2])  # Output: [10, 30, 50] (every second element)


# Modifying a List
# Lists are mutable, so you can modify their content.
# Changing an element
my_list = [1, 2, 3, 4, 5]
my_list[2] = 99
print(my_list)  # Output: [1, 2, 99, 4, 5]

# Adding elements
# Using append() function : Adds an element at the end of the list.
my_list.append(6)
print(my_list)  # Output: [1, 2, 99, 4, 5, 6]

# Using insert(): Adds an element at a specific index.
my_list = [1, 2, 3]
my_list.insert(1, 99)  # Inserts 99 at index 1
print(my_list)  # Output: [1, 99, 2, 3]

# Using extend(): Adds all elements of an iterable (e.g., another list).
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Using remove(): Removes the first occurrence of a value.
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

# Using pop(): Removes and returns an element at a specific index.
my_list = [1, 2, 3]
popped = my_list.pop(1)  # Removes the element at index 1
print(popped)  # Output: 2
print(my_list)  # Output: [1, 3]

# Using clear(): Removes all elements from the list.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []


# List operations
# Concatenation: Combining two or more lists using the + operator.
list6 = [1, 2, 3]
list7 = [4, 5, 6]
result = list6 + list7
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition: Repeating a list using the * operator
my_list = [1, 2, 3]
print(my_list * 2)  # Output: [1, 2, 3, 1, 2, 3]

# Membership: Checking if an element exists in a list using in or not in.
my_list = [1, 2, 3]
print(2 in my_list)  # Output: True
print(4 not in my_list)  # Output: True


# Built-in List methods
# len(): Returns the number of elements in a list.
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3

# sort(): Sorts the list in ascending order (modifies the list)
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

# sorted(): Returns a sorted version of the list (does not modify the original list).
my_list = [3, 1, 2]
print(sorted(my_list))  # Output: [1, 2, 3]

# reverse(): Reverses the order of elements in the list.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

# count(): Returns the count of occurrences of a value.
my_list = [1, 2, 2, 3]
print(my_list.count(2))  # Output: 2

# index(): Returns the index of the first occurrence of a value.
my_list = [1, 2, 3]
print(my_list.index(2))  # Output: 1


# Nested List
# Lists can contain other lists as elements, which allows for the creation of multi-dimensional
# data structures like matrices.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])  # Output: [1, 2, 3]
print(matrix[1][2])  # Output: 6 (row 2, column 3)


# List Concatenation and Multiplication in Python
# Python allows you to perform operations like concatenation and multiplication on lists.
# These operations are simple and very useful when working with collections of data.

# List Concatenation (+ Operator)
# Concatenation combines two or more lists into one.
# It does not modify the original lists; instead, it creates a new list.
l1 = [1, 2, 3]
l2 = [4, 5, 6]

# Concatenation
result = l1 + l2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# Original lists remain unchanged
print(l1)  # Output: [1, 2, 3]
print(l2)  # Output: [4, 5, 6]


# List Multiplication (* Operator)
# Multiplication creates a new list by repeating the elements of an existing list a specified number of times.
# Like concatenation, it does not modify the original list.
l1 = [1, 2, 3]

# Multiplication
result = l1 * 3
print(result)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Original list remains unchanged
print(l1)  # Output: [1, 2, 3]

# if you multiply by 0 or a negative number, you'll get an empty list.


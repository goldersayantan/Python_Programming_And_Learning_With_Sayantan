"""In Python, strings are one of the most commonly used data types. A string is a sequence of
characters enclosed in either single quotes (') or double quotes ("). Strings are immutable,
meaning that once a string is created, it cannot be changed."""


# Single-quoted string
str1 = 'Hello'

# Double-quoted string
str2 = "World"

# Triple-quoted string
str3 = '''This is a 
        multi-line string.'''

# using str() to convert other data types to strings
str4 = str(123)  # Converts integer to string


# String Indexing And Slicing
text = "Python"
print(text[0])
print(text[-1])  # Negative indexing starts from the end

text = "Python"
print(text[0:3])  # Characters from 0 to 2
print(text[::2])  # Every second Character


# String Operations
# Concatenation of strings
result = str1 + " " + str2
print(result)

# Repeating of strings
print(str1 * 3)  # HelloHelloHello

# Membership: Checking if a substring exists within a string
string1 = "Python Programming"
print("Python" in string1)  # True
print("P" in string1)  # True


# Common string methods
my_str = "Python"
print(len(my_str))  # length of the string
print(my_str.lower())  # Convert the string in lowercase
print(my_str.upper())  # Convert the string in uppercase

my_str1 = "    Hello    "
print(my_str1.strip())  # Removes leading and trailing spaces

my_str2 = "Hello World!"
print(my_str2.replace("World", "Sayantan"))  # Replacing "World" with "Sayanatn"

my_str3 = "Python,Java,C++"
print(my_str3.split(","))  # Splits a string into a list of substrings based on a delimiter(,).

lst = ["Python", "is", "fun"]
print(" ".join(lst))  # Joins elements of a list into a single string using a delimiter.


# String Formatting
# f-string
name = "Alice"
age = 18
print(f"My name is {name} and I am {age} years old.")

# format() method
name = "Alex"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# Percentage formatting
name = "Eve"
age = 22
print("My name is %s and I am %d years old." %(name, age))

# Immutability of string
text = "Hello"
# text[0] = 'h' -> This will raise an error.

text = "h" + text[1:]
print(text)  # It will replace "H" with "h"


# String Concatenation and Multiplication in Python
# String Concatenation (+ Operator)
# Concatenation combines two or more strings into one.
# The result is a new string, and the original strings remain unchanged.
str1 = "Hello"
str2 = "World"

# Concatenation
result = str1 + " " + str2
print(result)  # Output: "Hello World"

# Original strings remain unchanged
print(str1)  # Output: "Hello"
print(str2)  # Output: "World"


# String Multiplication (* Operator)
# Multiplication creates a new string by repeating the original string a specified number of times.
# The result is also a new string, and the original string remains unchanged.
str1 = "Hi"

# Multiplication
result = str1 * 3
print(result)  # Output: "HiHiHi"

# Original string remains unchanged
print(str1)  # Output: "Hi"

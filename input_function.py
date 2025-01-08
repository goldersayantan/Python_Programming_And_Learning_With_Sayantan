"""
The input() function in Python is used to take input from the user during the execution of a program.
It allows a program to pause and wait for user input before continuing.
"""
# Syntax of input()
input("prompt")

# Basic Usage of input()
# Taking input from the user
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Return Type:
# The input() function always returns the user input as a string, even if the user enters a number.
# If you need the input in a different data type (e.g., integer or float), you must explicitly convert it.
# Input as a string
age = input("Enter your age: ")
print(type(age))  # Output: <class 'str'>

# Converting the input to an integer
age = int(age)
print(type(age))  # Output: <class 'int'>

# Handling Numeric Input:
# If the user enters a non-numeric value while converting input to an integer or float, Python will raise a ValueError.
age = int(input("Enter your age: "))  # If the user types "twenty", this will raise ValueError.

# Prompt Message:
# If no prompt argument is passed, the function will just wait for the user to type something without displaying a message.
user_input = input()
print("You entered:", user_input)


# Converting Input to Different Data Types
# Integer Input
# Taking integer input
num = int(input("Enter a number: "))
print("The square of the number is:", num ** 2)

# Float Input
# Taking float input
price = float(input("Enter the price: "))
print("The price is:", price)

# Multiple Inputs
# You can use split() to take multiple inputs at once
# Taking multiple inputs
x, y = input("Enter two numbers separated by a space: ").split()
x = int(x)
y = int(y)
print("Sum:", x + y)





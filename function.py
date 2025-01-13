"""
Functions in Python
A function in Python is a reusable block of code designed to perform a specific task.
Functions help organize code, make it modular, and reduce redundancy.

Defining a Function:
A function is defined using the def keyword.

Syntax:

def function_name(parameters):
    "*****Optional docstring to describe the function.*****"
    # Code block
    return value  # Optional

function_name: The name of the function (should follow naming conventions).
parameters: Optional; values passed to the function when called.
return: Optional; specifies the output of the function.
"""

# Examples
# A Simple Function


def greet():
    print("Hello, world!")


# Calling the function:
greet()     # Output: Hello, world!


# Function with Parameters
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")    # Output: Hello, Alice!


# Function with Return Value
def add(a, b):
    return a + b


result = add(3, 5)
print(result)    # Output: 8


# Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")


greet()          # Output: Hello, Guest!
greet("Alice")   # Output: Hello, Alice!


# Keyword Arguments
def introduce(name, age):
    print(f"I am {name} and I am {age} years old.")


introduce(age=25, name="Alice")    # Output: I am Alice and I am 25 years old.


# Variable-Length Arguments
# Arbitrary Positional Arguments (*args)
def add_all(*args):
    return sum(args)


print(add_all(1, 2, 3, 4))  # Output: 10


# Arbitrary Keyword Arguments (**kwargs)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="Alice", age=25, city="Kolkata")    # Output:  name: Alice age: 25 city: Kolkata


# Scope of Variables
x = 10  # Global variable


def func():
    y = 5  # Local variable
    print("Inside function:", x + y)


func()
print("Outside function:", x)    # Output: Inside function: 15 Outside function: 10


# Anonymous Functions (lambda)
# A lambda function is a small, anonymous function defined using the lambda keyword.

# Syntax:
# lambda arguments: expression

square = lambda x: x ** 2
print(square(5))  # Output: 25


# Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # Output: 120














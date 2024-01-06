# In python functions are trated as first class citizens, allowing you to perform the  following operations on functions:
# - A function can take one or more functions as parameters
# - A function can be returned as a result of another function
# - A function can be modified
# - A function can be assigned to a variable

# In this section, we will cover:
# 1.- Handing functions as parameters
# 2.- Returning functions as return valie from another functions
# 3.- Using Python closures and decorators


# FUNCTIONS AS A PARAMETER

def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst):
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)

# FUNCTIONS AS A RETURN VALUE

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function_1(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute

result = higher_order_function_1("cube")
print(result(3))
result = higher_order_function_1("square")
print(result(3))
result = higher_order_function_1("absolute")
print(result(-3))


# PYRHON CLOSURES

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))

# PYTHON DECORATORS
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

# Creating Decorators

def greeting():
    return "Welcome to Python"
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())

## Lets implement the example above with a decorator

def uppercase_decorator_1(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator_1
def greeting_1():
    return "Welcome to Python"
print(greeting_1())













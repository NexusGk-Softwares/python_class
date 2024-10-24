# dealing all python functions
import os
import math
import random
import string
import re

# creating a function
def greet_user(name):
    return f"Hello, {name}!"

print(greet_user("John Doe"))  # Output: Hello, John Doe!

# defining a function with default argument
def greet_user_default(name="World"):
    return f"Hello, {name}!"

print(greet_user_default())  # Output: Hello, World!
print(greet_user_default("Jane Doe"))  # Output: Hello, Jane Doe!

# defining a function with variable number of arguments
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15

# defining a function with keyword arguments
def greet_user_kwargs(**kwargs):
    return f"Hello, {kwargs['name']}!"

print(greet_user_kwargs(name="John Doe"))  # Output: Hello, John Doe!

# defining a function with a lambda as an argument
def apply_operation(operation, num1, num2):
    return operation(num1, num2)

add = lambda x, y: x + y
print(apply_operation(add, 5, 3))  # Output: 8

# defining a function with a nested lambda
double_add = lambda x: lambda y: x + y(x)
print(double_add(5)(3))  # Output: 8

# defining a function with a variable number of arguments
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15

# defining a function with a dictionary as argument
def double_dict_values(dictionary):
    return {key: value * 2 for key, value in dictionary.items()}

print(double_dict_values({'a': 1, 'b': 2, 'c': 3}))  # Output: {'a': 2, 'b': 4, 'c': 6}

# defining a function with a list comprehension
def squares(numbers):
    return [num ** 2 for num in numbers]

print(squares([1, 2, 3, 4, 5]))  # Output: [1, 4, 9, 16, 25]

# defining a function with a generator expression
def squares_generator(numbers):
    return (num ** 2 for num in numbers)

print(list(squares_generator([1, 2, 3, 4, 5])))  # Output: [1, 4, 9, 16, 25]

# defining a function with a set comprehension
def unique_squares(numbers):
    return {num ** 2 for num in numbers}

print(unique_squares([1, 2, 3, 4, 5]))  # Output: {1, 4, 9, 16, 25}

# defining a function with a tuple comprehension    
def double_tuples(numbers):
    return (num * 2 for num in numbers)

print(list(double_tuples([1, 2, 3, 4, 5])))  # Output: [2, 4, 6, 8, 10]

# defining a function with a lambda as an argument
def multiply_by_three(x):
    return x * 3

def apply_operation_with_function(operation, num):
    return operation(num)

print(apply_operation_with_function(multiply_by_three, 5))  # Output: 15

# defining a function with a lambda as a class as argument
class Calculator:
    def add(self, x, y):
        return x + y

def apply_operation_with_class(operation, num1, num2):
    return operation.add(num1, num2)

calculator = Calculator()
print(apply_operation_with_class(calculator, 5, 7))  # Output: 12

# defining a function with a lambda as a nested function as argument
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_5_nested = outer_function(5)
print(add_5_nested(3))  # Output: 8

# defining a function with a lambda as a recursive function as argument
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

factorial_lambda = lambda n: 1 if n == 0 else n * factorial_lambda(n - 1)
print(factorial_lambda(5))  # Output: 120

# defining a function with a lambda as a lambda as a nested argument
square_lambda = lambda x: lambda y: x ** y
print(square_lambda(2)(3))  # Output: 8

# defining a function with a lambda as a variable number of arguments
def sum_lambda(*args):
    return sum(args)

print(sum_lambda(1, 2, 3, 4, 5))  # Output: 15

# defining a function with a lambda as a dictionary argument
def double_dict_values_lambda(dictionary):
    return {key: value * 2 for key, value in dictionary.items()}

print(double_dict_values_lambda({'a': 1, 'b': 2, 'c': 3}))  # Output: {'a': 2, 'b': 4, 'c': 6}

# defining a function with a lambda as a list comprehension
def squares_lambda(numbers):
    return [num ** 2 for num in numbers]

print(squares_lambda([1, 2, 3, 4, 5]))  # Output: [1, 4, 9, 16, 25]

# defining a function with a lambda as a generator expression
def squares_generator_lambda(numbers):
    return (num ** 2 for num in numbers)

print(list(squares_generator_lambda([1, 2, 3, 4, 5])))  # Output: [1, 4, 9, 16, 25]

# defining a function with a lambda as a set comprehension
def unique_squares_lambda(numbers):
    return {num ** 2 for num in numbers}

print(unique_squares_lambda([1, 2, 3, 4, 5]))  # Output: {1, 4, 9, 16, 25}

# defining a function with a lambda as a tuple comprehension
def double_tuples_lambda(numbers):
    return (num * 2 for num in numbers)

print(list(double_tuples_lambda([1, 2, 3, 4, 5])))  # Output: [2, 4, 6, 8, 10]

# defining a function with a lambda as a function as argument
def multiply_by_three_lambda(x):
    return x * 3

def apply_operation_with_function_lambda(operation, num):
    return operation(num)

print(apply_operation_with_function_lambda(multiply_by_three_lambda, 5))  # Output: 15

# defining a function with a lambda as a class as argument
class Calculator:
    def add(self, x, y):
        return x + y

def apply_operation_with_class_lambda(operation, num1, num2):
    return operation.add(num1, num2)

calculator = Calculator()
print(apply_operation_with_class_lambda(calculator, 5, 7))  # Output: 12



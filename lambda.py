# python lambda
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# nested lambda
double_add = lambda x: lambda y: x + y(x)
print(double_add(5)(3))  # Output: 8


# lambda with multiple arguments
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # Output: 24


# lambda as a function argument
def apply_operation(operation, num1, num2):
    return operation(num1, num2)

print(apply_operation(lambda x, y: x + y, 5, 3))  # Output: 8


# lambda as a return value
def calculate_sum(num1, num2):
    return lambda: num1 + num2

add_5 = calculate_sum(5, 3)
print(add_5())  # Output: 8

# lambda with a default value
multiply_by_two = lambda x=2: x * 2
print(multiply_by_two())  # Output: 4
print(multiply_by_two(5))  # Output: 10


# lambda with a variable number of arguments
sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# lambda with a dictionary as argument
double_dict_values = lambda dictionary: {key: value * 2 for key, value in dictionary
                                         .items()}
print(double_dict_values({'a': 1, 'b': 2, 'c':
    3}))  # Output: {'a': 2, 'b': 4, 'c': 6}

# lambda with a list comprehension
squares = lambda numbers: [num ** 2 for num in numbers]
print(squares([1, 2, 3, 4, 5]))  # Output: [1, 4, 9, 16, 25]

# lambda with a generator expression
squares_generator = lambda numbers: (num ** 2 for num in numbers)
print(list(squares_generator([1, 2, 3, 4, 5])))  # Output: [1, 4, 9, 16, 25]

# lambda with a set comprehension
unique_squares = lambda numbers: {num ** 2 for num in numbers}
print(unique_squares([1, 2, 3, 4, 5]))  # Output: {1, 4, 9, 16, 25}

# lambda with a tuple comprehension
double_tuples = lambda numbers: (num * 2 for num in numbers)
print(list(double_tuples([1, 2, 3, 4, 5])))  # Output: [2, 4, 6, 8, 10]


# lambda with a function as argument
def multiply_by_three(x):
    return x * 3

apply_operation_with_function = lambda operation, num: operation(num)
print(apply_operation_with_function(multiply_by_three, 5))  # Output: 15


# lambda with a class as argument
class Calculator:
    def add(self, x, y):
        return x + y

apply_operation_with_class = lambda operation, num1, num2: operation.add(num1, num2)
calculator = Calculator()
print(apply_operation_with_class(calculator, 5, 7))  # Output:
# 12


# lambda with a nested function as argument
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_5_nested = outer_function(5)
print(add_5_nested(3))  # Output: 8


# lambda with a recursive function as argument
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

factorial_lambda = lambda n: 1 if n == 0 else n * factorial_lambda(n - 1)
print(factorial_lambda(5))  # Output: 120

# lambda with a lambda as a nested argument
square_lambda = lambda x: lambda y: x ** y
print(square_lambda(2)(3))  # Output: 8



# lambda with a lambda as a variable number of arguments
sum_lambda = lambda *args: sum(args)
print(sum_lambda(1, 2, 3, 4, 5))  # Output: 15


# lambda with a lambda as a dictionary argument
double_dict_values_lambda = lambda dictionary: {key: value * 2 for key, value in dictionary
                                         .items()}
print(double_dict_values_lambda({'a': 1, 'b': 2, 'c': 3}))  # Output: {'a': 2, 'b': 4, 'c': 6}


# lambda with a lambda as a list comprehension
squares_lambda = lambda numbers: [num ** 2 for num in numbers]
print(squares_lambda([1, 2, 3, 4, 5]))  # Output: [1, 4, 9, 16, 25]


# lambda with a lambda as a generator expression
squares_generator_lambda = lambda numbers: (num ** 2 for num in numbers)
print(list(squares_generator_lambda([1, 2, 3, 4, 5])))  # Output: [1, 4, 9, 16, 25]


# lambda with a lambda as a set comprehension
unique_squares_lambda = lambda numbers: {num ** 2 for num in numbers}
print(unique_squares_lambda([1, 2, 3, 4, 5]))  # Output: {1, 4, 9, 16, 25}


# lambda with a lambda as a tuple comprehension
double_tuples_lambda = lambda numbers: (num * 2 for num in numbers)
print(list(double_tuples_lambda([1, 2, 3, 4, 5])))  # Output: [2, 4, 6, 8, 10]


# lambda with a lambda as a function as argument
multiply_by_three_lambda = lambda x: x * 3
apply_operation_with_function_lambda = lambda operation, num: operation(num)
print(apply_operation_with_function_lambda(multiply_by_three_lambda, 5))  # Output: 15


# lambda with a lambda as a class as argument
class Calculator:
    def add(self, x, y):
        return x + y

apply_operation_with_class_lambda = lambda operation, num1, num2: operation.add(num1, num2)
calculator = Calculator()


# lambda with a lambda as a nested function as argument
outer_function_lambda = lambda x: lambda y: x + y
add_5_nested_lambda = outer_function_lambda(5)
print(add_5_nested_lambda(3))  # Output: 8


# lambda with a lambda as a recursive function as argument
factorial_lambda = lambda n: 1 if n == 0 else n * factorial_lambda(n - 1)
print(factorial_lambda(5))  # Output: 120


# lambda with a lambda as a lambda as a nested argument
square_lambda = lambda x: lambda y: x ** y
print(square_lambda(2)(3))  # Output: 8




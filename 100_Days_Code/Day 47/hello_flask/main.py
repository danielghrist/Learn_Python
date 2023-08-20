# ## ********Day 54 Start**********
# ## Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# ##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(add, 2, 3)
# print(result)
#
#
# ##Functions can be nested in other functions
#
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
#
# outer_function()
#
#
# ## Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
#
# inner_function = outer_function()
# inner_function
#
# ## Simple Python Decorator Functions
# import time
#
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         # Do something before
#         function()
#         function()
#         # Do something after
#
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
#
# # With the @ syntactic sugar
# @delay_decorator
# def say_bye():
#     print("Bye")
#
#
# # Without the @ syntactic sugar
# def say_greeting():
#     print("How are you?")
#
#
# decorated_function = delay_decorator(say_greeting)
# decorated_function()

# Python Decorator Function
# import time
#
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before calling function
#         function()
#         # Do something after calling function
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     # time.sleep(2)
#     print("Hello")
#
# @delay_decorator
# def say_bye():
#     # time.sleep(2)
#     print("Bye")
#
# def say_greeting():
#     # time.sleep(2)
#     print("How are you?")
#
# say_greeting()

# DAY 54 FINAL CODING EXERCISE
import time


# FOR DECORATOR FUNCTIONS YOU RETURN THE WRAPPER FUNCTION AND DO NOT ADD THE "()"
# AS THAT WOULD RETURN THE RETURN OF THE WRAPPER FUNCTION NOT THE FUNCTION ITSELF.
def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        time_elapsed = end_time - start_time
        print(f"{function.__name__} Run Speed: {time_elapsed}")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


# fast_function()
# slow_function()


def logging_decorator(function):
    """
    Log the name of the function that was called, the arguments given, and the returned ouput
    :param function: func
    :return:
    """
    def wrapper_function(*args):
        name = function.__name__
        output = function(args)
        print(f"You called {name}{args}\nIt returned: {output}")
    return wrapper_function


@logging_decorator
def a_function(*args):
    return sum(list(args[0]))


a_function(1, 2, 3)

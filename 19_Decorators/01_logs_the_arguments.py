"""
Write a decorator that logs the arguments and output of a function each time
it’s called.
"""

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

add(5, 3)

"""
Develop a decorator that restricts a function from being called more than a
specified number of times (e.g., 5).
"""

def restrict_calls(max_calls):
    def decorator(func):
        func.call_count = 0

        def wrapper(*args, **kwargs):
            if func.call_count < max_calls:
                func.call_count += 1
                return func(*args, **kwargs)
            else:
                return "Function call limit exceeded"

        return wrapper
    return decorator

@restrict_calls(5)
def greet(name):
    return f"Hello, {name}!"

for i in range(7):
    print(greet("User"))

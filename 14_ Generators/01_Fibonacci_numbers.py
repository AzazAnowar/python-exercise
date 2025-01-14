"""
Create a generator that yields all Fibonacci numbers up to a given maximum
value
"""

def fibonacci_gen(max_value):
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b

# Example usage:
for num in fibonacci_gen(50):
    print(num, end=" ")

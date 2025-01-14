"""
Write a recursive function to find the nth Fibonacci number in the sequence.
"""

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10
print(f"{n}th Fibonacci number:", fibonacci_recursive(n))

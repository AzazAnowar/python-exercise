"""
Write a generator that produces the prime numbers up to a specified number.
"""

def prime_gen(max_value):
    for num in range(2, max_value + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            yield num

# Example usage:
for prime in prime_gen(50):
    print(prime, end=" ")

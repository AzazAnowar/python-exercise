"""
Write a program to display all prime numbers between 1 and 100 using a
nested loop.
"""
#prime number

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

# loop through the numbers
for num in range(1, 101):
    if is_prime(num):
        print(num)
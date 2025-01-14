"""
Create a function that splits a list into two separate lists—one containing all
even numbers, the other containing all odd numbers.
"""

"""
returning multiple values as tuples

import math

def circle_area(radius1, radius2):
    area1 = math.pi * radius1**2
    area2 = math.pi * radius2**2
    return area1, area2

a1, a2 = circle_area(12.5, 23.7)
print("Area 1: ", a1)
print("Area 2: ",a2)

"""

def even_odd_numbers(lst):
    even_numbers = []
    odd_numbers = []

    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = even_odd_numbers(lst)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

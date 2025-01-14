"""
Write a program that takes a tuple of numbers and returns a new tuple
containing the cumulative sum at each index.
"""

def cumulative_sum(tpl):
    total = 0
    result = []
    for num in tpl:
        total += num
        result.append(total)
    return tuple(result)

numbers = (1, 2, 3, 4, 5)
print("Cumulative sum:", cumulative_sum(numbers))
"""
Develop a program that takes two lists of equal length and divides each
element of the first list by the corresponding element in the second list, handling
exceptions for division by zero and mismatched list lengths.
"""

def safe_division(list1, list2):
    try:
        if len(list1) != len(list2):
            raise ValueError("Lists are not of equal length.")
        result = [a / b if b != 0 else "Error: Division by zero" for a, b in zip(list1, list2)]
        return result
    except ValueError as e:
        return str(e)

list1 = [10, 20, 30]
list2 = [2, 0, 5]
print("Result:", safe_division(list1, list2))
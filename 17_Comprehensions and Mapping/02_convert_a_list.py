"""
Use map() to convert a list of strings representing numbers into a list of
integers, and then filter out all numbers greater than a specified threshold.
"""

numbers = ["10", "20", "30", "40", "50"]
threshold = 25
result = list(filter(lambda x: x > threshold, map(int, numbers)))
print("Filtered numbers:", result)

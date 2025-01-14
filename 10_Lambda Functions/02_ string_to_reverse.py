"""
Create a lambda function that takes a string and returns it in reverse. Use it
with map() to reverse multiple strings in a list.
"""

reverse_string = lambda s: s[::-1]
strings = ["hello", "world", "python"]
reversed_strings = list(map(reverse_string, strings))
print("Reversed strings:", reversed_strings)
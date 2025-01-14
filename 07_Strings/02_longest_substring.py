"""
Problem 2: Implement a function that finds the longest substring without repeating
characters in a given string and returns its length.
"""

def longest_unique_substring(s):
    char_index = {}
    start = max_length = 0
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length

string = "abcabcbb"
print("Length of longest substring:", longest_unique_substring(string))
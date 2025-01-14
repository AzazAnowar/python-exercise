"""
Write a program that merges two dictionaries by adding values for any
common keys, otherwise keeping the values as is.
"""

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 35}
print("Merged dictionary:", merge_dictionaries(dict1, dict2))
"""
Implement a recursive function that flattens a nested list (e.g., [[1, 2,
[3]], 4] becomes [1, 2, 3, 4]).
"""

def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

nested_list = [[1, 2, [3]], 4]
print("Flattened list:", flatten_list(nested_list))

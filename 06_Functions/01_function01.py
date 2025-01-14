def find_pairs(numbers, target):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs

numbers = [2, 4, 3, 5, 7, 8, 1]
target = 9
print("Pairs:", find_pairs(numbers, target))
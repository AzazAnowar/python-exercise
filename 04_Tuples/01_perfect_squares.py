def filter_perfect_squares(tpl):
    return tuple(num for num in tpl if int(num**0.5) ** 2 == num)

numbers = (1, 4, 7, 9, 16, 20, 25)
print("Perfect squares:", filter_perfect_squares(numbers))
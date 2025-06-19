def multiply(num_list, multiplier):
    return [number * multiplier for number in num_list]

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]
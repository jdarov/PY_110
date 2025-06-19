def double_odd_index(my_list):
    return [number * 2 if idx % 2 == 1 else number for idx, number in enumerate(my_list)]

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_index(my_numbers))  # [2, 4, 6, 14, 2, 6]

print(my_numbers)                      # [1, 4, 3, 7, 2, 6]
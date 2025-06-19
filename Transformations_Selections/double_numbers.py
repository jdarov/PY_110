def double_numbers(numbers_list):
    return list(map(lambda x: x * 2, numbers_list))
my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                 # [1, 4, 3, 7, 2, 6]
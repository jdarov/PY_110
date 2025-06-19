lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

expected = [[], [3, 12], [9], [15, 18]]

new_list = [[number for number in sub_list if number % 3 == 0] for sub_list in lst]

print(new_list == expected)
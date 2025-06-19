lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

expected = [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

expected_list = sorted(lst, key=lambda x: sum(number for number in x if number % 2 == 1))

print(expected_list == expected)
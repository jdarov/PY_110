lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

expected = [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

expected_list = [sorted(sub_list, key=str) for sub_list in lst]

print(expected_list == expected)
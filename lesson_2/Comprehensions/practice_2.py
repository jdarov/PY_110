lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

expected = [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

expected_list = [sorted(nested_list) for nested_list in lst]
print(expected_list == expected)
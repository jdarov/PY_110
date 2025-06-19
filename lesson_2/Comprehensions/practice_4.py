lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

expected = {
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
}

expected_dict = {sub_lst[0]:sub_lst[1] for sub_lst in lst}

print(expected_dict == expected)
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

expected = [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]


def return_dict(old_dict):
    new_dict = {}
    for key in old_dict:
        new_dict[key] = old_dict[key] + 1
    return new_dict


new_list = [{k: v + 1 for k, v in d.items()} for d in lst]

print(new_list == expected)
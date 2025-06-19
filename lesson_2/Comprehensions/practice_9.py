lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

expected = [{'e': [8], 'f': [6, 10]}]

def all_even(lst):
    for number in lst:
        if number % 2 == 1:
            return False
    return True

def dict_even(dictionary):
    for key, lst in dictionary.items():
        if all_even(lst):
            continue
        return False
    return True

print([dict1 for dict1 in lst if dict_even(dict1)])

print(all_even([1,2,3]) == False)
print(all_even([2,4,6]) == True)


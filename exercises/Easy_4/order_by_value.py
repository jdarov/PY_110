def order_by_value(dictionary):
    return [keys for keys, values in sorted(dictionary.items(), key=lambda items: items[1])]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
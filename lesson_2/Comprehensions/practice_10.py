import random

HEXADECIMAL = '123456789abcdef'
number_sequence = [8, 4, 4, 4, 12]
def UUID():
    return '-'.join(random_string(number) for number in number_sequence)

def random_string(length_of_string):
    return ''.join(random.choice(HEXADECIMAL) for _ in range(length_of_string))

print(UUID())
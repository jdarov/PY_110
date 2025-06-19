# text = 'This is  some text'

# print(text.split(' '))
# # print(text.split(''))
# print(text.split())

# my_list = ['one', 2]

# print(my_list)

def less_than(upper_limit):
    numbers = []

    for candidate in range(1, upper_limit):
        numbers.append(candidate)

    return numbers

print(less_than(1))
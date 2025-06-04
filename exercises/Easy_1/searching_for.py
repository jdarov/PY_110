dict_nums = {
    1 : 'st',
    2 : 'nd',
    3 : 'rd',
}

number_list = [input(f'Enter the {str(i) + dict_nums.get(i, 'th')} number: ') for i in range(1,7)]

last_number = number_list.pop()
num_list_str = ','.join(number_list)

print(f'{last_number} is{'' if last_number in number_list else "n't"} in {num_list_str}')

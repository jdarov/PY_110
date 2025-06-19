def is_ascending(last_num, num):
    return num > last_num
def is_descending(last_num, num):
    return num < last_num
def is_bouncy(number):
    ascending = descending = False
    last_digit = number[0]

    for digit in number[1:]:
        if is_ascending(last_digit, digit) and not ascending:
            ascending = True
        if is_descending(last_digit, digit):
            descending = True
        if ascending and descending:
            return 1
        last_digit = digit
        
    return 0     

def bouncyCount(list_of_numbers):
    string_numbers = map(str, list_of_numbers)

    return sum(is_bouncy(number) for number in string_numbers)

print(bouncyCount([]) == 0)
print(bouncyCount([11, 0, 345, 21]) == 0)
print(bouncyCount([121, 4114]) == 2)
print(bouncyCount([176, 442, 80701644]) == 2)

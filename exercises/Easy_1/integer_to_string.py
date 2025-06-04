DICT_STR = {}

for i in range (0, 10):
    DICT_STR[i] = str(i)

def signed_integer_to_string(number):

    is_negative = number < 0
    number = abs(number)
    num_list = []
    if number == 0:
        return DICT_STR[number]
    while number > 0:
        num_list.append(number%10)
        number //= 10
    
    string_number = ''.join(DICT_STR[num] for num in reversed(num_list))
    return f'+{string_number}' if not is_negative else f'-{string_number}'

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

def string_to_signed_integer(numbers):
    
    def convert_to_numbers(number_string):
        dict_int = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
        }
        return [dict_int[num] for num in number_string if num.isdigit()]
    int_list = convert_to_numbers(numbers)
    
    result = 0
    for digit in int_list:
        result = result * 10 + digit
    return (result if numbers[0] != '-' else -result)

        
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
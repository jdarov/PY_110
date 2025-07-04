"""
C - 
O
D
E
"""
def digits_repeat(num):
    string_num = str(num)
    for digit in string_num:
        if string_num.count(digit) != 1:
            return True
    return False

def next_featured(number):
    error = ("There is no possible number that "
         "fulfills those requirements.")
    
    while number <= 9876543201:
        number += 1
        if number % 7 == 0 and number % 2 == 1 and not digits_repeat(number):
            return number
    return error

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
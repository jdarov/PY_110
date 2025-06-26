"""
C
    input: int
    output: int

    explicit:
        take an int and return sum of all multiple of 7 or 11 less than argument int
        if number is multiple of 7 and 11, count it only once
        ex:
            25: 7 + 11 + 14 + 21 + 22 == 75

    implicit:
        if int is 0 return 0
        if no multiples of 7 or 11 return 0 
        negative numbers return 0
O
D
    ints
    ranges

    simply return 0 if int <= 0

    sum all numbers returned from 1 to int that are divisible by 7 or 11
E
"""

def seven_eleven(number):
    return sum(x for x in range(1, number) if x % 7 == 0 or x % 11 == 0) if number >= 0 else 0
print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
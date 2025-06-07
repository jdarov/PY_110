def digit_list(integer):
    list_of_integers = []
    while integer >= 1:
        list_of_integers.append(integer%10)
        integer //= 10
    return list_of_integers[::-1]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
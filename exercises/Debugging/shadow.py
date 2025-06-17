def sum_of(numbers, factor): #fixed the name!
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_of(numbers, 2) == 20)
"""
C
    input: list of ints
    output: int

    explicit: 
        find the smallers int that can be added to list of ints so the sum of the list equals closest prime number
        that is greater than CURRENT sum of list without the appended number

        [1,2,3] == 6
        PRIME # after 6 = 7
        [1,2,3,1] == 7
        return 1 (1 appended to list to equal 7)

        list will always contain at least 2 ints
        all values in list > 0
        there can be multiple occurences of a number
    implicit:
        prime number is a number than can only be divided by 1 and itself 

O
D
    lists, ints

    functions
        find the nearest prime number
        check all numbers in a range starting from sum of the list 
        once we reach a prime number, return that number

    compute the current sum of the list and save that sum
    find the closest prime number after this sum
    return the difference between this prime number and the sum of the list 
E
"""
def next_prime_number(number):
    number += 1
    not_prime = True
    while not_prime:
        not_prime = False
        for num in range(2, number):
            if number % num == 0:
                number += 1
                not_prime = True
    return number
def nearest_prime_sum(list_of_ints):
    return next_prime_number(sum(list_of_ints)) - sum(list_of_ints)

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
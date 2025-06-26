"""
C
    input: list of ints
    output: int representing an index

    explicit:
        sum of all numbers less than element at index return the sum of all numbers greater than element at index

        ex:
            [1,2,4,4,2,3,2] == 3
            [1+2+4] = 7
            [2+3+2] = 7
    implicit:
        the index number is exclusive to both lists(dont count it)
        all lists have more than 2 numbers in it
O
D
    list of ints, lists, ints

    slice the list starting at :1, 2: and increment by 1
    if we reach end of list, stop
    return the index that we slice the list 
    if sum of entire list is 0, return 0
    if there is no answer, return -1


E
"""
def equal_sum_index(list_of_ints):
    if sum(list_of_ints) == 0:
        return 0
    i = 0

    while i + 1 < len(list_of_ints):
        if sum(list_of_ints[:i]) == sum(list_of_ints[i+1:]):
            return i
        i += 1
    return -1
print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)
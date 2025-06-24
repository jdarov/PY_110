"""
C - input = list of integers
    output = list of how many numbers smaller than element in list of integers

    explicit:
        if an element is the same as element, dont incremenet count (2 is not less than 2)
        count how many elements are less than current element 
        only count unique values
    implicit:
        if a number is the same as element, count doesnt increase
        if a single element is in list, simply return [0]
        [5, 4, 2, 2] == [2, 1, 0, 0]

O 
- print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
D - 
    lists of nums
    list
    
    functions: iterate with number and list 
    return count of items smaller than number 

    algorithm:
        iterate over the elements in the list
        for each element in the list, iterate over the the numbers in the list starting from index 0
            for each of these numbers, if the number is less than current element being tested, increment count
            if numbers are the same (eg index at 2 is 2 and index at 3 is 2): dont increment count
            append the count to new list
            reset count
        start next element and repeat
        return the new list
E
"""
def count_smaller_numbers(number, list_of_nums):
    count = 0
    counted_nums = set()
    for num in list_of_nums:
        if num < number and num not in counted_nums:
            counted_nums.add(num)
            count += 1
    return count

def smaller_numbers_than_current(list_of_numbers):
    return [count_smaller_numbers(number, list_of_numbers) for number in list_of_numbers]


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

# 6 minutes 
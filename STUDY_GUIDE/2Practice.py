"""
C 
    input: list of numbers(ints)
    ouput: int with sum of the 5 smalles numbers in list

    explicit: 
        return the minimum sum of 5 elements in a list 
        if list is less than 5 elements, return None
    implicit: 
        the sum must be of 5 CONSECUTIVE numbers (can't skip elements)
        find the smallest sum of all sums of 5 consecutive numbers in list
        return None if length of list less than 5
        all elements count even if they repeat 
            sum(1, 1, 1, 1, 2) = 6

O   
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

D
    data: lists, int

    funct: 
        consective_sums:
            for each element from list, create new lists from start to start+5
                if start+5 < length
            increment start by 1 and continue
        return this list of sublists containing 5 consecutive elements
        example:
            [1,2,3,4,5,6] = [1,2,3,4,5], [2,3,4,5,6]


    algo: 
        create a list of all sums of 5 consective numbers
        find the min of the sum of all these lists
        return this sum if lenght is 5 or more, or retur None if not
E
"""
def all_cons_five_element(number_list):
    sub_lists = list()
    for i in range(len(number_list)-4):
        sub_lists.append(number_list[i:i+5])
    return sub_lists
def sum_of_list(sub_list):
    return sum(sub_list)
def minimum_sum(list_of_nums):
    if len(list_of_nums) < 5:
        return None
    return min(sum(list_of_nums[i:i+5]) for i in range(len(list_of_nums)-4))


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

#20 minutes
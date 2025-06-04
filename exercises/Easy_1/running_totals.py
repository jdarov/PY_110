def running_total(list_of_nums):
    if not list_of_nums:
        return []
    running_list = [list_of_nums[0]]
    for i, num in enumerate(list_of_nums[1:], 1):
        running_list.append(running_list[i-1] + num)
    return running_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

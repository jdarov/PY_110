def sum_of_next(list_of_ints):
    return [integer+sum(list_of_ints[:idx]) for idx, integer in enumerate(list_of_ints)]

print(sum_of_next([1,2,3]))
print(sum_of_next([]))
print(sum_of_next([-1, -5, -10]))
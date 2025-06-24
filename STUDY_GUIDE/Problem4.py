"""
C
    input:
        list of ints
    output:
        tuple (int, int)
        two closest numbers together

    explicit:
        return two pairs of numbers that are closest together
        if multiple pairs are similarly close (12, 13) (14,15)
            return the pair that comes first (12, 13)
    implicit:
        tuple should be in order that number appears in list(not sorted)
        
        
O
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

D
    lists of ints
    tuples

    iterate through the list of ints

    function:
        create a list of tuples with every single set of numbers in the list
            iterate starting from 0
                iteratate from 1 to len(list)
                    create a tuple of ints at both these indexes

                [1, 2, 3, 4] = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)] 
                = indexs [(0,1), (0,2), (0,3)...]
                
    function:
        return the difference of the highest number in the tuple minus the lowest number in the tuple

    return the tuple with the smallest difference from the list of tuples (return the first one if multiple)
E
"""

def create_tuple_list(list_of_ints):
    return [(list_of_ints[x],list_of_ints[y]) for x in range(len(list_of_ints)) for y in range(x+1, len(list_of_ints))]
def difference(sub_tuple):
    return max(sub_tuple) - min(sub_tuple)
def closest_numbers(list_of_nums):
    return min(create_tuple_list(list_of_nums), key=difference)

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

#Finished in 20 minutes
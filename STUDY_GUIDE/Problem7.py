"""
C
    input: list of ints
    output: return int number of multiple occuring ints

    explict:
        return the number of ints that occur more than once
            [1,2,3,2,1] == (1,1), (2,2) == 2
        if list is empty or length of 1, return 0
    implicit:
        create tuples of all elements that match each other
        if their is an odd element out, it doesnt count
            [2,2,2,2,2] == 2 since (2,2), (2,2) and the remaing 2 can't be used in a tuple
        
O
D
    list of ints
    tuples
    int

    function:
        returns a list of tuples of multiple occuring elements
        iterates over list of ints
            if an int matches another int, and its index isn't already used, 
                create a tuple of those ints
            save the indexes of those ints in a set to remember ints already used in a tuple
    
    length of the list of tuples will be our final answer
E
"""
def list_of_occuring_tuples(list_of_ints):
    used_number_indexes = set()
    occuring_tuples = list()
    for x in range(len(list_of_ints)):
        for y in range(x+1, len(list_of_ints)):
            if (list_of_ints[x] == list_of_ints[y] 
                and x not in used_number_indexes
                and y not in used_number_indexes):
                    occuring_tuples.append((list_of_ints[x], list_of_ints[y]))
                    used_number_indexes.add(x)
                    used_number_indexes.add(y)
    return occuring_tuples
def pairs(list_of_nums):
     return len(list_of_occuring_tuples(list_of_nums)) if len(list_of_nums) > 1 else 0

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
""""
Must complete this challenge WITHOUT using any sorted() method
Return a new list with all elements from both lists sorted
"""

def sort_list(unsorted_list):

    sorted_list = unsorted_list.copy()
    
    unsorted = True

    while unsorted:
        unsorted = False
        for i in range(len(sorted_list)-1):
            if sorted_list[i] > sorted_list[i+1]:
                sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
                unsorted = True
    
    return sorted_list

def merge(list1, list2):
    return sort_list(list1 + list2)

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)

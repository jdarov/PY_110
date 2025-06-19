"""
C : 
    Input: List of strings
    output: Return the same list, sorted by adjacent consonants

    Explicit:
        Sort the list by adjacent consonants
        Consonants are considered adjacent if they are one after another or seperated by a space
            eg This is adjacent
        If 2 strings contain that same highest number of adjacent consonants, leave them in the same order
    Implicit:
        empty list should return an empty list (returns the same list but sorted)
        *Consonants are every letter except AEIOU
        *1 consonant and 0 consonants are equal, so should retain the same order 
        *Descending order (highest number to lowest number)

O - 
    my_list = ['aa', 'baa', 'ccaa', 'dddaa']
    print(sort_by_consonant_count(my_list))
    # ['dddaa', 'ccaa', 'aa', 'baa']

    my_list = ['can can', 'toucan', 'batman', 'salt pan']
    print(sort_by_consonant_count(my_list))
    # ['salt pan', 'can can', 'batman', 'toucan']

    my_list = ['bar', 'car', 'far', 'jar']
    print(sort_by_consonant_count(my_list))
    # ['bar', 'car', 'far', 'jar']

    my_list = ['day', 'week', 'month', 'year']
    print(sort_by_consonant_count(my_list))
    # ['month', 'day', 'week', 'year']

    my_list = ['xxxa', 'xxxx', 'xxxb']
    print(sort_by_consonant_count(my_list))
    # ['xxxx', 'xxxb', 'xxxa']

D - 
    List of strings => mutated list 

    Loop through each string in the list 
    For each string, caclulate the number of adjacent consonants (function)
        Function: 
        Loop through each character in string
        If character is consonant, append it to a string
        If character is vowel, hold the length of that consonant string and reset the string
        Return the highest consonant string length
    Represent each string based on this number
    
    Use the number of adjacent consonants to sort the list in descending order 
        if there is a similar number (3, 2a, 1, 2b) then leave them in that same order (3, 2a, 2b, 1)
        Sorted (key = function (returns number of adjacent consonants), reverse = True)
    
E : 

"""
VOWELS = 'aeiou'
def number_of_adjacent_consonants(string):
    total_adjacent = 0
    consonant_string = ''

    for char in string.lower():
        if char not in VOWELS and (char.isalpha() or char == ' '):
            consonant_string += char
            total_adjacent = max(total_adjacent, len(consonant_string))
        else:
            consonant_string = ''
    return total_adjacent if total_adjacent > 1 else 0

def sort_by_consonant_count(list_of_strings):
    return sorted(list_of_strings, key=number_of_adjacent_consonants, reverse=True)

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
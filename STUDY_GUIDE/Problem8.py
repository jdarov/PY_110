"""
C
    input: non empty string
    ouput: return the LENGTH of the longest substring of vowels in the string
    
    explicit:
        vowels = 'aeiou'
        all strings will contain some characters
        all strings will be all lowercased letters
    implicit:
        if no vowels are in string, return 0
        if one vowel appears by itself, return 1
        vowels must appear next to each other without being interrupted by a consonant to count
            'lAUnch schOOl' = 2 is longest length 'au' and 'oo'
        no spaces or punctuation in string
        
O

D
    strings
    lists
    characters

    function:
        return a list of every substring of vowels in a string
            iterate over all charcters in a string 
            if next character is a vowel
                append it to the string
                continue
            if not
                append this substring to list
                empty the string
                continue the loop
    
    find the max length of all substrings
    return this number

    'aeiou'
    'ee', 'a' 

    [0:1], [0:6]
E
"""
VOWELS = 'aeiou'
def all_vowel_substrings(string):
    vowel_string = ''
    list_of_vowel_strings = list()

    for x in range(len(string)):
        if string[x] in VOWELS:
            vowel_string += string[x]
            for y in range(x+1, len(string)):
                if string[y] in VOWELS:
                    vowel_string += string[y]
                    continue
                break
            list_of_vowel_strings.append(vowel_string)
            vowel_string = ''

    return list_of_vowel_strings

def lengths_of_strings(string_list):
    return [len(substring) for substring in string_list]

def longest_vowel_substring(string):
    if all_vowel_substrings(string):
        return max(lengths_of_strings(all_vowel_substrings(string)))
    return 0

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
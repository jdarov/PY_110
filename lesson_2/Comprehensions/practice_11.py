dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}


VOWELS = 'aeiou'
list_of_vowels = [
    char 
    for key,lst in dict1.items() 
    for string in lst 
    for char in string 
    if char in VOWELS
    ]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
"""
C
    input: string
    ouput: dictionary 
        key = lowercase letter in string
        value = number of times letter appears in string

    explict:
        return a dict with key lowercased character and value the count of character in string 
    implicit:
        each letter is assigned once as a key to dicitonary (so no recurring letters)
        dont count punctuation or spaces
        if a letter is uppercased, DO NOT COUNT IT!
        ONLY COUNT LOWERCASED LETTERS
        empty string or string with no letters (only punctuation) returns an empty dict
O
D
    string
    dictionary
    characters

    iterate through each character in a string
    determine if the character is not space or punuctuan AND is not uppercased
        if it is not any of these things, append as key to dictionary and assign count
        only count all lowercase iterations of the letter
    return the dictionary

    function:
        returns a new string with all punctuaion and uppercased letters removed?
    
E
"""
def is_lowercased(char):
    return char.lower() == char
def remove_all_but_lowercased(string):
    return ''.join(char for char in string if char.isalpha() and is_lowercased(char))
def count_letters(string):
    return {char:string.count(char) for char in remove_all_but_lowercased(string)}


expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
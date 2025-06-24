"""
C
    input: string
    output: character

    explicit:
        return the character that appears most often in a string
        if multiple characters appear the max amount of times, return the one that comes first
        uppercase and lowercase should be considered the SAME
    implicit:
        the character returned will always be lowercased
        punctuation and spaces dont change anything
O

D
    strings, character
    list of characters

    take a string and break it down into a list of each character
    assign each character to a value of how many times it appears (dictionary?)
    return the highest number count of the character , if multiple return the first one(max with a key)

    if we turn this into a dictionary of characters as key and counts as values then
        function: return values from the dictionary so we can use it as the key

    function:
        create a dictionary from the list of characters in a string and assign the count as their values
        we could do this as a tuple as well
E
"""

def create_dict_of_char_counts(string):
    return {char.lower():string.lower().count(char) for char in string if char.isalpha()}

def most_common_char(string):
    dictionary_of_chars = create_dict_of_char_counts(string)
    return max(dictionary_of_chars, key=dictionary_of_chars.get)

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str)=='p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.

P - 
    input: 'string'
    output: list [] - 'type(str)'

    rules:
        Explicit:
            Given a string, return a list of substrings
            substrings should be palindromes 
                palindrome is a word that is spelled the same way forwards as it is backwards
            substrings should be >= 2 char in length 
            Palindromes should be case sensitive
                example: 'abc' != 'Abc'
        implicit:
            Empty string returns empty list
            no palindromes or substrings returns an empty list

D - string, char, lists
A - palindrome_substrings(param:string)
        if string:
        loop over the string from index 0 to length(string)
        for each element - check if it matches its correpsonding element in end of string
            ex: 0 = -1
                1 = -2
                etc
                *element == -(element+1)
        if we run to the end, then we need to add this substring to the list(confirm palindrome)
        else continue on to the next char
        check for string length and if less than 2, BREAK
            index for the middle of the string, once we hit index, BREAK
        return [substrings]
"""

def is_palindrome(string):
    return string == string[::-1]

def substrings(s):
    all_substrings = []

    length = len(s)

    for start in range(length):
        for end in range(start+2, length+1):
            all_substrings.append(s[start:end])
    
    return all_substrings

def palindrome_substrings(string):

    return [sub for sub in substrings(string) if is_palindrome(sub)]

# Test cases:

# Comments show expected return values
print(palindrome_substrings("abcddcbA"))  # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]
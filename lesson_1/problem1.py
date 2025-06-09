def is_palindrome(word):
    return word.casefold() == word.casefold()[::-1] if len(word) > 1 else False

def change_me(sentence):
    return ' '.join([word.upper() if is_palindrome(word) else word for word in sentence.split()])

"""
PROBLEM:

Given a string, write a function `change_me` which returns the same
string but with all the words in it that are palindromes uppercased.
"""

# Comments show expected return values
print(change_me("We will meet at noon"))      # "We will meet at NOON"
print(change_me("No palindromes here"))      # "No palindromes here"
print(change_me(""))                           # ""
print(change_me("I LOVE mom and dad equally")) # "I LOVE MOM and DAD equally"
print(change_me("Hello Bob"))
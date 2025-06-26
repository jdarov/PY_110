"""
C
    input: string
    output: boolean

    explicit:
        return True if a string is Pangram, False if not
        A pangram is sentences that contain every letter of the alphabet at least once
    implicit:
        punctuation and space don't matter but can be in sentence
        all sentences will have something (no empty strings)

O
D
    strings, booleans

    1. check if alphabet in string?

    2. set of alphabet and set of string
        check if alphabet is subset of string (all elements in alphabet are in string)

    
E
"""
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def is_pangram(string):
    return ALPHABET in ''.join(sorted(set(string.lower())))
    return set(string.lower()) >= set(ALPHABET)

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)
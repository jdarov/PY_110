"""
C
    input: string
    output: int

    explicit:
        count distinct case-insensitive alphabetic and numeric digits that occur more than once
        ex:
            'xyz' is 0 (no repeating chars)
            'xxyypzzr' is 3 'x, y, z' repeat
    implicit:
        if no repeating chars, return 0
        strings will never be empty
        it doesn't matter how many times a char repeats, it only increments count by 1
O
D
    strings, list of chars, chars, ints

    functions:

    loop over each character in a string
    add that character to a list of characters in string 
    check if character is in this list of characters and not in a list of already used characters
        if it is, increment the count by 1 
        add it to a list of already used characters
    return count
E
"""
def distinct_multiples(string):
    return sum(string.lower().count(char) > 1 for char in set(string.lower()))

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
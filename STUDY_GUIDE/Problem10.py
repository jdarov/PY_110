"""
C
    input: string of digits
    output: int representing number of even numbered substrings

    explicit:
        return the number of even number substrings that can be made from string of digits
        ex: '1432' == 6 '14', '1432', '4', '432', '32' '2'
        multiple occurence of substrings count seperately

    implicit:
        '1432' returns:
            [0:2], [0:4(length)], [1], [1:4], [2:4], [4]
        if number in substring % 2 == 0:
            substring is good
        if no even numbers in string, return 0

O

D
    string of digits
    int

    function:
        returns all substring in a string
    function:
        returns the integer equivalent of string
    function:
        returns a list of strings that have even numbered integer equivalents
    
    return the length of this list
E
"""

def all_substrings(string):
    return [string[x:y] for x in range(len(string)) for y in range(x+1, len(string)+1)]
def even_substrings(digit_string):
    return len([num for num in all_substrings(digit_string) if int(num) % 2 == 0])

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)
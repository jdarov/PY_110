"""
C
    input:
        non empty string
    output:
        tuple (string, int)

    explicit:
        substring * int = string
        return shortest possible substring multiplied by int to return the string
        entirely lowercase alphabet (no punctuation or spaces
    implicit:
        an answer can be as small as a single char
        if there is no repeat substring, return string and 1 (string * 1 == string)
O
D
    strings, ints, tuples

    functions:
        return all possible substrings of string
            iteratet through string starting at 0-length
                iterate through string starting at 1-length
                    append substring to list
            return this list
        
        return if substring * an int == string
            initiate variables to hold current int and largest int
            iterate through all substrings
            multiply by all ints up to the length of the original string
            if sub * int == string, save int to variable
            save int to variable if its larger than the current largest int

            return tuple of (substring, largest int)
        
    create all possible tuple, int combinations for string
    find the tuple with the largest int
    return this tuple
            

E
"""

def all_substrings(string):
    return list(set(string[x:y] for x in range(len(string)) for y in range(x+1, len(string)+1)))

def create_tuple_sub_int(substring, original_string):
    for i in range(len(original_string)+1):
        if substring * i == original_string:
            return (substring, i)
    return 0

def repeated_substring(string):
    substrings = all_substrings(string)
    tuples = list()
    for sub in substrings:
        if create_tuple_sub_int(sub, string):
            tuples.append(create_tuple_sub_int(sub,string))
    if not tuples:
        return (string, 1)
    
    return max(tuples, key=lambda x: x[1])
    
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

#17 minutes :)
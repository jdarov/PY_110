"""
C
    input: two strings
    output: integer count number of times second string appears in first

    explicit:
        return the number of time the second string appears in first string
        overlapping strings DO NOT count 
            'babab' 'bab' returns 1 not 2, (because 'bab' the second 'b' is already used)
        2nd arg is never an empty string
    implicit:
        if first string empty, alwasy return 0
        if a single letter, simply return the count of that letter
        all strings will be lowercased
        all strings will be all letters and not contain punctuation or spaces
O
D
    string
    ints
    substrings

    if a single letter we can just return the count of that letter
    if first string is empty just return 0

    function:
        iterates over a splice of the string
        create a count variable storing number of time substring occurs
        start index at beginning
            check if start index and lenght of substring is longer than the lenght of string (avoid out of index)
            if it is then break out of the loop
            splice of string must start at start index and go an addtional length of substring over
            check if string splice is same as substring
            if not, increment start index by 1 and continue loop
            if yes
                increment count by 1
                start index = the ending index of splice
                    eg 'babab' check [0:3] if yes 'bab' the start index = 3 (starts from 'ab')
E
"""

def count_substrings(string, substring):
    count = 0
    start_index = 0

    for _ in range(start_index, len(string)):
        if start_index + len(substring) > len(string):
            break
        if string[start_index:start_index+len(substring)] == substring:
            count += 1
            start_index += len(substring)
            continue
        start_index += 1
    return count



print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)
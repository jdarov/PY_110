# Find the longest substring in alphabetical order.
# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# The input will only consist of lowercase characters and will be at least one letter long.
# If there are multiple solutions, return the one that appears first.

'''
Rules
    - case-insenstive
    - return the longest continously ascending alpha substring
    from the input
    - If multiple subs with same length, return the one appears first
    - if single char input -- > return the char
    - if there are ascending alpha chars in input, return first character


Data Structure

Input: lowercase string of alpha chars
Output: another string, longest substring


Intermediate

- List of alpha substrings - iteratively build this

'abcdeapbcdef'


abcde
ap
bcdef

return abcde




Algorithm
Iterate through each start char in input. Try and build ascending alpha substring, stop when the next character is LESS than current ( or first?) character, OR you get to the end of the string successfully. Append this substring to a "substrings" list.
- Start at the next char....
- Return the substring in "substrings" that has the longest length.
    - or the first one, if there are more than one.

- given "text" as input
- set "substrings_lst" list to empty list

- Iterate over the "start_chars" in "text"
    - "substring" to empty "start_char"
    - 

    - Iterate from "next_char" (to the end of "text")
        - check if "next_char" > last char in "substring"
            - if it is:
                - concatentae "next_char" to "substring"
                - continue iterating

            - if not:
                - append "substring" to "substrings"
                - break from innter loop, to (next start_char)

- return the longest item in "substrings"                 

'''
def substrings(string):
    if len(string) == 1:
        return string
    longest_sub = current_sub = string[0]

    for i in range(1, len(string)):
        if string[i] >= current_sub[-1]:
            current_sub += string[i]
        else:
            if len(current_sub) > len(longest_sub):
                longest_sub = current_sub
            current_sub = string[i]
    if len(current_sub) > len(longest_sub):
        longest_sub = current_sub
    return longest_sub

def longest(string):
    substrings_lst = []

    for start_idx, start_char in enumerate(string):
        substring = start_char

        for next_idx in range(start_idx + 1, len(string)):
            if string[next_idx] >= substring[-1]:
                substring += string[next_idx]
            
            else:
                substrings_lst.append(substring)
                break
        
        substrings_lst.append(substring)

    # print(substrings_lst)

    longest_str = max(substrings_lst, key=len)
    # print(longest_str)
    return longest_str
            
        # print(substrings_lst)
        
        # break

# Tests
print(longest('asd') == 'as')
print(longest('nab') == 'ab')
print(longest('abcdeapbcdef') ==  'abcde')
print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
print(longest('asdfbyfgiklag') == 'fgikl')
print(longest('z') == 'z')
print(longest('zyba') == 'z')
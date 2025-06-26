"""
C
    input: two strings
    output: boolean

    explicit:
        first string is substring
        check if substring is in the string
        return True if it is or False if it isn't
    implicit:
        strings will never be empty

O
D
    strings, sets

    function:

    check if char in list of string characters
    if not return false
    if we loop through all characters in string, and remove them from sub as we go
    see if sub is empty at the end


E
"""
def unscramble(sub, string):
    string_chars = list(string)
    for char in sub:
        if char in string_chars:
            string_chars.remove(char)
    
    return not string_chars


print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)
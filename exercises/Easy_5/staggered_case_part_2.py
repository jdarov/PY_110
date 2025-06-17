def staggered_case(string):
    new_string = []
    stagger = True
    for char in string:
        if char.isalpha():
            new_string.append(char.upper() if stagger else char.lower())
            stagger = not stagger
        else:
            new_string.append(char)
    return ''.join(new_string)

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
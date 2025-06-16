def is_consonant(char):
    return (char.isalpha() and (char.casefold() not in 'aeiou'))

def double_consonants(string):
    return ''.join(char*2 if is_consonant(char) else char for char in string)

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
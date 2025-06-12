def vowels(string):
    return ''.join([char.upper() if char.lower() in 'aeiou' else char.lower() for char in string])

print(vowels('aEIOu'))

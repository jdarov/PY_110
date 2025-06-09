def vowels(string):
    return ''.join([char.upper() if char.lower() in {'a', 'e', 'i', 'o', 'u'} else char.lower() for char in string])

print(vowels('aEIOu'))

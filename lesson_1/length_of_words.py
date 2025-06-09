def strip_punctuation(string_of_words):
    return ''.join([char for char in string_of_words if char.isalnum() or char.isspace()])

def length_of_words(string):
    return {word:len(word) for word in strip_punctuation(string).split()}

print(length_of_words('Hello! World? Hello!'))
print(length_of_words("What's up?"))
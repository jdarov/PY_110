def word_sizes(string):
    word_sizes = {}

    for words in string.split():
        clean_word = ''.join(char for char in words if char.isalnum())
        length = len(clean_word)
        word_sizes[length] = word_sizes.get(length, 0) + 1
    return word_sizes

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
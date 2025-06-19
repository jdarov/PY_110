NUMBER_DICT = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def word_to_digit(string):
    return ' '.join(word if word not in NUMBER_DICT else str(NUMBER_DICT[word]) for word in string.split())

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True


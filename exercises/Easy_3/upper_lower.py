def upper_lower(string):
    split_words = string.split(' ')
    upper = True
    print(split_words)
    for idx, word in enumerate(split_words):
        if word.isalpha():
            split_words[idx] = word.upper() if upper else word.lower()
            upper = not upper
        else:
            continue
    return ' '.join(split_words)
print(upper_lower('Hello   World') == 'HELLO   world')
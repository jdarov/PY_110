def is_it(sub_strings, string):

    count = 0
    copy_of_subs = sub_strings.copy()
    for words in copy_of_subs:
        copy_of_letters = set()
        for letter in words: 
            if letter not in copy_of_letters:
                print(letter)
                print(words)
                copy_of_letters.add(letter)
                if words.count(letter) > string.count(letter):
                    sub_strings.remove(words)
                    break

    print(sub_strings)
    return len(sub_strings)

print(is_it(['abc', 'ha'], 'hammock'))
print(is_it(['aaaa', 'aaa', 'aa'], 'abcdefgaa'))
print(is_it(['hello', 'what', 'some', 'aa', 'aabbc'], 'hello some what answers back'))
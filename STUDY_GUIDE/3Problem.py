"""
C 
    input: string
    output: new string

    explicit:
        every 2nd char in every 3rd word convert to uppercase
    implicit:
        all other chars besides target chars remain the same
        maintain spaces and puncutation

O 
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

D
    data: strings, list of words, list of chars

    func: 
        create a new word if it is the target word
        new word should contain every 2nd character uppercase
        return this new word string

    algo:
        break down string into list of words
        iterate through each character in the list of words
            determine if the word is a multiple of 3 
            iterate through the chars in that word
                determine if char is multiple of 2
                    uppercase that char
        join this list of words with the space between each word
E
"""
INDEX_OF_THIRD_WORDS = {2, 5, 8, 11}

def wordify(word):
    return ''.join(char.upper() if idx % 2 == 1 else char for idx, char in enumerate(word))
def to_weird_case(string):
    list_of_words = string.split()

    for i in range(len(list_of_words)):
        if (i+1) % 3 == 0:
            list_of_words[i] = wordify(list_of_words[i])
    return ' '.join(list_of_words)
    
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
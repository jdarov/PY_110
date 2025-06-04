def swap(string):
    swap_string = []
    for word in string.split():
        if len(word) < 2:
            swap_string.append(word)
        else:
            swap_string.append(word[-1] + word[1:-1] + word[0])
    return ' '.join(swap_string)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
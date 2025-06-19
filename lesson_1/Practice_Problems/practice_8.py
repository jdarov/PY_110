# Pretty printed for clarity
{
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}

statement = "The Flintstones Rock"
print({char:statement.count(char) for char in statement if char.isalpha()})
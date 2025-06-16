def sequence(integer):
    return list(range(1, integer+1)) if integer > 0 else []
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
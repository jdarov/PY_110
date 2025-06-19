# frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)
# print(frozen)

#error, frozensets are immutable

dog = 'fido'

letters = list(dog)
letters[0] = letters[0].upper()
dog = ''.join(letters)
print(dog)
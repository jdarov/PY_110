def triangle(x, y, z):
    if min(x, y) + min(y,z) > max(x,y,z) and x and y and z:
        if x == y and y == z:
            return 'equilateral'
        if (x != y and y != z) and z != x:
            return 'scalene'
        return 'isosceles'
    return 'invalid'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
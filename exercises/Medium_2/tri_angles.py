def triangle(x, y, z):
    if sum((x, y, z)) == 180 and x and y and z:
        if x < 90 and y < 90 and z < 90:
            return 'acute'
        if x > 90 or y > 90 or z > 90:
            return 'obtuse'
        return 'right'
    return 'invalid'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
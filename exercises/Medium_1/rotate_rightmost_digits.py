def rotate_rightmost_digits(number, count):
    string_number = str(number)
    if count <= 1:
        return number
    left = string_number[:-count]
    to_rotate = string_number[-count:]
    rotated = to_rotate[1:] + to_rotate[0]
    return int(left + rotated)


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
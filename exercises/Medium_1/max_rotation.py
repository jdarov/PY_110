"""
    explicit:
        1. rotate one digit from beginning to the end
        2. keep first digit in place, rotate next digits from 1:
        3. keep 2 digits fixed and rotate from 2: 
        4. keep 3 digits in place and rotate from 3: 
        5. keep 4 digits in place and rotate from 4: 
"""

def rotate_from_place(number, place):
    string_number = str(number)
    first_part = string_number[:place]
    rotate_part = string_number[place:]
    if len(rotate_part) <= 1:
        return string_number
    rotated_number = rotate_part[1:] + rotate_part[:1]

    return first_part + rotated_number

def max_rotation(number):
    new_number = number
    for i in range(len(str(number))-1):
        new_number = rotate_from_place(new_number, i)
    return int(new_number)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

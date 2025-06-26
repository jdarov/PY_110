"""
C
    input: string of numeric digits
    output: int

    explicit:
        return the greatest product (multiplication) of 4 consecutive numbers
        strings will always be at least length of 4
    implicit:
        numbers must be consecutive, so not 4 highest numbers but 4 highest consecutive numbers

O
D
    strings, ints

    functions:
        -create a list of all substrings of 4 consecutive numbers
            iterate through string of numbers
            slice it from beginning to beginning + 4
            continue until we reach end of the string
        -compute product of a string with 4 digits in it
            seperate the digits
            typecast digits from string to int (go through all the strings in the seperated digits)
            multiply them with each other
            return the product of all 4 of the digits

    create a list of products or use an iterator in max to determin highest product
    return this number

E
"""
def create_list_of_4digit_subs(string):
    sub_list = list()
    start, end = 0, 4
    while end <= len(string):
        sub_list.append(string[start:end])
        start += 1
        end += 1

    return sub_list
def product_of_digits(digit_string):
    product = 1
    digits = list(map(int, list(digit_string)))

    for digit in digits:
        product *= digit
    return product

def greatest_product(string_digits):
    return max(product_of_digits(digits) for digits in create_list_of_4digit_subs(string_digits))

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
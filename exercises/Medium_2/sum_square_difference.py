def sum_of_all_integers_squared(integer):
    return ((sum(range(1, integer+1)))**2)

def sum_of_integers_squared(integer):
    return (sum(x**2 for x in range(1, integer+1)))

def sum_square_difference(integer):
    return (sum_of_all_integers_squared(integer) - sum_of_integers_squared(integer))


print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
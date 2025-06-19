import sys

sys.set_int_max_str_digits(50_000)

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 2:
        result = 1
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    memo[n] = result
    return result

def find_fibonacci_index_by_length(length_of_num):
    iterator = 1
    while True:
        fib_num = fibonacci(iterator)
        if len(str(fib_num)) >= length_of_num:
            return iterator
        iterator += 1

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 2:
        result = 1
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    memo[n] = result
    return result

print(fibonacci(6))
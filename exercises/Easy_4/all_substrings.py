
def leading_substrings(string, i):
    return [string[i:idx+1] for idx in range(i, len(string))]

def substrings(string):
    print([substring for i in range(len(string)) for substring in leading_substrings(string, i)])

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
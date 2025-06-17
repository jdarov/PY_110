def is_palindrome(string):
    return len(string) > 1 and string == string[::-1]

def leading_substrings(string, i):
    return [string[i:idx+1] for idx in range(i, len(string))]

def substrings(string):
    return [substring for i in range(len(string)) for substring in leading_substrings(string, i)]

def palindromes(string):
    return [substring for substring in substrings(string) if is_palindrome(substring)]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True
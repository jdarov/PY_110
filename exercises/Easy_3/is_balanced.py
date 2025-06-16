def is_balanced(string):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{', '"': '"', "'": "'"}
    
    for char in string:
        if char in pairs.values():
            if char in ['"', "'"] and stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        elif char in pairs:  # closing
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

print(is_balanced("'whats up butter cup'"))

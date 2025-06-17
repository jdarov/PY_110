import copy

original = [[1], [2], [3]]
#highlight
copied = copy.deepcopy(original)
#endhighlight

original[0][0] = 99

print(copied[0] == [1])
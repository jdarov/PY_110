def multiply_list(lst):
    # for item in lst:
    #     item *= 2
#highlight
    return [item*2 for item in lst]
#endhighlight

print(multiply_list([1, 2, 3]) == [2, 4, 6])
def reverse_string(string):
#highlight
    # for char in string:
    #     string = char + string
#endhighlight
#highlight
    return string[::-1]
#endhighlight

print(reverse_string("hello") == "olleh")
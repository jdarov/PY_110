data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
#highlight
unique_data = list(dict.fromkeys(data))
#endhighlight
print(unique_data == [4, 2, 1, 3]) # order not guaranteed
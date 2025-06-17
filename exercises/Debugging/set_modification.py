data_set = {1, 2, 3, 4, 5}

#highlight
for item in list(data_set):
    #endhighlight
    if item % 2 == 0:
        data_set.remove(item)

print(data_set)
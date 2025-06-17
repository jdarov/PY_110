def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter) #counter is changed in local scope but not global, need to reassign

print('LAUNCH!')
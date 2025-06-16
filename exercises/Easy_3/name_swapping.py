def swap_name(name):
    split_names = name.split()
    length = len(split_names)

    first_name, last_name = ' '.join(split_names[:-1]), split_names[-1]
    return f'{last_name}, {first_name}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
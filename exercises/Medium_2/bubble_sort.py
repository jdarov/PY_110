def bubble_sort(my_list):
    while True:
        sorted_nums = True
        for i in range(len(my_list)-1):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                sorted_nums = False
        if sorted_nums:
            break

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                                                           

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7]) 

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)    
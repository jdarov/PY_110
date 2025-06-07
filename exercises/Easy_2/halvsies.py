def halvsies(whole_list):
    
    middle = len(whole_list)//2 + len(whole_list)%2
    
    return (whole_list[:middle], whole_list[middle:])
print(halvsies([1, 2, 3, 4, 5]))
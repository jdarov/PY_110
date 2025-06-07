def count_occurrences(list):
    repeated_elements = set()
    for element in list:
        if element not in repeated_elements:
            print(f'{element} => {list.count(element)}')
            repeated_elements.add(element)
    
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
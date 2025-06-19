dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

new_list = [
    [color.capitalize() for color in dict1[produce]['colors']]
      if dict1[produce]['type'] == 'fruit'
        else dict1[produce]['size'].upper() 
        for produce in dict1
    ]
expected = [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

print(new_list == expected)
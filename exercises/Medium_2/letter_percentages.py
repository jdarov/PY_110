def letter_percentages(string):
    upper_count = lower_count = other_count = 0
    length = len(string)
    
    for char in string:
        if char.isalpha():
            if char == char.lower():
                lower_count += 1
                continue
            upper_count += 1
            continue
        other_count += 1

    lower_percent = lower_count/length * 100
    upper_percent = upper_count/length * 100
    other_percent = other_count/length * 100
    
    return {
        'lowercase': f'{lower_percent:.2f}', 
        'uppercase': f'{upper_percent:.2f}', 
        'neither': f'{other_percent:.2f}'
        }

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
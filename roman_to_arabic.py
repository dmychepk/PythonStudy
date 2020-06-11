def roman_to_arabic(my_string):
    aplhabet = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    my_list = list(my_string)
    arabic_number = 0
    for i in range(len(my_list) - 1):
        if aplhabet[my_list[i + 1]] <= aplhabet[my_list[i]]:
            arabic_number += aplhabet[my_list[i]]
            if i == len(my_list) - 2:
                arabic_number += aplhabet[my_list[i + 1]]
        else:
            arabic_number += aplhabet[my_list[i + 1]] - aplhabet[my_list[i]]

    return arabic_number
#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    reverse_ = roman_string[::-1]
    char_ = 'I'
    total = 0
    for i in reverse_:
        if letters[i] >= letters[char_]:
            char_ = i
            total += letters[i]
        else:
            total -= letters[i]
    return total

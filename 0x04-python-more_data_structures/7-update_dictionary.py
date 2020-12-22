#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    i = 0
    for lkeys in a_dictionary:
        if lkeys == key:
            a_dictionary[lkeys] = value
            i = 1
    if i == 0:
        a_dictionary[key] = value
    return a_dictionary

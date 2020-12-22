#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    i = 0
    for l in a_dictionary:
        if l == key:
            i = 1
    if i == 1:
        del a_dictionary[key]
    return a_dictionary

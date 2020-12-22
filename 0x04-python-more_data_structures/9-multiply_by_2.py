#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    key = list(a_dictionary.keys())
    _dictionary = {}
    for i in key:
        _dictionary[i] = a_dictionary[i] * 2
    return _dictionary

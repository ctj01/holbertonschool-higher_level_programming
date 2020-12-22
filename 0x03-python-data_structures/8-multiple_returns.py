#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    c = ""
    if l == 0:
        c = None
    else:
        c = sentence[0]
    return (l, c)

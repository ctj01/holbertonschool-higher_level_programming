#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i is 8 and j is 9:
            print("{:d}{:d}".format(i, j))
        elif i < j:
            print("{:d}{:d}".format(i, j), end=", ")

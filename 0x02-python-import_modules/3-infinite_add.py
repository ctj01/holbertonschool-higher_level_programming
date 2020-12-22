#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    ar = len(argv[1:])
    addtion = 0
    for args in argv[1:]:
        if ar > 0:
            addtion += int(args)
    print(addtion)

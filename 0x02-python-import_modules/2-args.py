#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    ar = len(argv[1:])
    if ar == 1:
        print("{:d} argument:".format(ar))
    elif ar == 0:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(ar))

    ar = 0
    for args in argv[1:]:
        ar += 1
        print("{:d}: {:s}".format(ar, args))

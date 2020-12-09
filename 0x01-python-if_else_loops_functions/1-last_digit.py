#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
less = ""
if number < 0:
    number = -(number)
    less = "-"
modd = number % 10
if modd > 5:
    print("Last digit of {:s}{:d} is {:d} and is greater than 5"
          .format(less, number, modd))
elif modd < 6 and modd != 0:
    print("Last digit of {:s}{:d} is {:d} and is less than 6 and not 0"
          .format(less, number, modd))
elif modd == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, modd))

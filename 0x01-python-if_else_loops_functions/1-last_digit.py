#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last digit = -digit
    print("Last digit of {} is {} and is ".format(number, last digit), end="")
    if last digit > 5:
        print("greater than 5")
    elif last digit == 0:
        print("0")
    else:
        print("less than 6 and not 0")

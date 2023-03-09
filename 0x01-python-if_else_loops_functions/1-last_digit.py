#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10:
    if number < 0:
        last digit = -digit
    print("Last digit of {} is {} and is ".format(number, last digit), end="")
if last digit > 5:
    print("and is greater than 5")
elif digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

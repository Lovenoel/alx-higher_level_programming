#!/usr/bin/python3
# Importing functions from calculator file
from calculator_1 import add, sub, mul, div

# Variables
a = 10
b = 5
# Printing their various values
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))

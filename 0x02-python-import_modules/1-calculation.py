#!/usr/bin/python3
# Main program
a = 10
b = 5

# Importing functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Calling each imported function and printing the results
result_add = add(a, b)
result_subtract = sub(a, b)
result_multiply = mul(a, b)
result_divide = div(a, b)

# Printing results
print("{} + {} = {}".format(a, b, result_add))
print("{} - {} = {}".format(a, b, result_subtract))
print("{} * {} = {}".format(a, b, result_multiply))
print("{} / {} = {}".format(a, b, result_divide))

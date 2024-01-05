#!/usr/bin/python3
# Importing the argv variable from the sys module
from sys import argv
# Getting the number of arguments
num_arguments = len(argv) - 1  # Subtracting 1 to exclude the script name
# Printing the number of arguments
if num_arguments == 0:
    print("{} arguments.".format(num_arguments))
else:
    print("{} arguments:".format(num_arguments))
    # Printing each argument along with its position
    for i in range(num_arguments):
        print("{}: {}".format(i + 1, argv[i + 1]))

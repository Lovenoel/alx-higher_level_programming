#!/usr/bin/python3
import sys


def infinite_add():
    # Check if there are any arguments
    if len(sys.argv) > 1:
        # Sum all command-line arguments (converted to integers)
        result = sum(int(arg) for arg in sys.argv[1:])
        print(result)

    else:
        # No arguments, print 0
        print(0)


# Check if the script is being run as the main program
if __name__ == "__main__":
    infinite_add()

#!/usr/bin/python3
import sys


def print_argument_info():
    # Get the number of command-line arguments
    num_args = len(sys.argv) - 1  # 1 excludes the script name itself

    # Print the number of arguments
    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}", end='')

    # Check if there are any arguments
    if num_args > 0:
        print(":")

        # Print each argument along with its position
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

    else:
        # No arguments, print a dot and a new line
        print(".")


# Check if the script is being run as the main program
if __name__ == "__main__":
    print_argument_info()

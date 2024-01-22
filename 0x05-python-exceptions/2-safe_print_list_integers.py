#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counts the printed integers
    try:
        for i in range(x):
            if isinstance(my_list[i], int):  # Checks if the elem is an integer
                print("{:d}".format(my_list[i]), end="")
                count += 1
                print()
    except (IndexError, TypeError):
        pass
    return count

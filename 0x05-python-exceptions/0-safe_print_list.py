#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            if count < x:
                print("{:d}".format(item), end="")
                count += 1
    except TypeError:
        pass
    finally:
        print()
    return count

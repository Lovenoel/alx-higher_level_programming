#!/usr/bin/python3
def print_sorted_dictionary(a_dict):
    for n in sorted(a_dict.keys()):
        print("{}: {}".format(n, a_dict[n]))
        
#!/usr/bin/python3
def complex_delete(a_dict, value):
    temp = a_dict.copy()
    for r, h in temp.items():
        if value == h:
            a_dict.pop(r)
    return a_dict

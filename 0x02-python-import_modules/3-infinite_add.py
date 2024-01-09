#!/usr/bin/python3
def add_arg(argv):
    m = len(argv) - 1
    if m == 0:
        print("{}".format(m))
        return
    else:
        i = 1
        add = 0
        while i <= m:
            add += int(argv[i])
            i += 1
            print("{}".format(add))

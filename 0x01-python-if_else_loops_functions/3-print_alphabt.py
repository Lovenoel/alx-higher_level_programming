#!/usr/bin/python3
for xn in range(ord('a'), ord('z') + 1):
    if chr(xn) != 'q' and chr(xn) != 'e':
        print("{}".format(chr(xn)), end="")

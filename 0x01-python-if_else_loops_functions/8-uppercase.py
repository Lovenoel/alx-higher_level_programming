#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Convert each character to uppercase using ord() and chr()
        upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print(upper_char, end='')

    print()  # Print a new line after the uppercase string
